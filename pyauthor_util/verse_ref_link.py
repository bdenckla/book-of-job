"""Auto-link chapter:verse references to quirkrec detail rows."""

from py import my_html
from pyauthor_util.short_id_etc import short_id

# Module-level verse-link mapping, set by init_verse_links().
# Maps chapter:verse strings (e.g. "27:13") to a list of SIDs.
_cv_to_sids = None
_d1d_fname = None


def init_verse_links(enriched_quirkrecs, d1d_fname):
    """Build and store the verse-reference auto-linking map.

    Args:
        enriched_quirkrecs: list of enriched quirkrec dicts
            (each must have at least "qr-cv").
        d1d_fname: filename for the detail page (e.g. "job1_full_list_details.html").
    """
    global _cv_to_sids, _d1d_fname
    _d1d_fname = d1d_fname
    mapping = {}
    for eqr in enriched_quirkrecs:
        cv = eqr["qr-cv"]
        mapping.setdefault(cv, []).append(short_id(eqr))
    _cv_to_sids = mapping


def verse_ref_link(cv):
    """Convert a chapter:verse string to a link, or assert on problems.

    Returns an <a> element linking to the detail row for unambiguous
    verses.  Asserts (fails the build) when the verse has no record or
    has multiple records.
    """
    if _cv_to_sids is None:
        # Verse linking not initialized; pass through as plain text.
        return cv
    sids = _cv_to_sids.get(cv)
    if sids is None:
        assert False, (
            f"Verse reference {cv} has no quirkrec record. "
            f"If this is intentional (e.g. a non-Job reference), "
            f"prefix with ~ to suppress auto-linking: ~{cv}"
        )
    if len(sids) > 1:
        assert False, (
            f"Verse reference {cv} has multiple quirkrec records "
            f"({', '.join(sids)}). "
            f"Use @WORDID to disambiguate, e.g. {cv}@WORDID"
        )
    sid = sids[0]
    href = f"{_d1d_fname}#row-{sid}"
    return my_html.anchor_h(cv, href)


def verse_ref_link_disambig(cv, wordid):
    """Link to a specific record for a multi-record verse.

    Args:
        cv: chapter:verse string, e.g. "38:12".
        wordid: word identifier suffix, e.g. "HMYMY5".

    The SID is constructed as CCVV-WORDID and validated against the
    known quirkrec records.
    """
    if _cv_to_sids is None:
        return cv
    ch, vs = cv.split(":")
    sid = f"{int(ch):02d}{int(vs):02d}-{wordid}"
    sids = _cv_to_sids.get(cv, [])
    assert sid in sids, (
        f"Disambiguated verse ref {cv}@{wordid} → SID {sid} "
        f"not found in known SIDs for {cv}: {sids}"
    )
    href = f"{_d1d_fname}#row-{sid}"
    return my_html.anchor_h(cv, href)
