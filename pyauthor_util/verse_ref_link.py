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
            f"({', '.join(sids)}). Use an explicit link instead."
        )
    sid = sids[0]
    href = f"{_d1d_fname}#row-{sid}"
    return my_html.anchor_h(cv, href)
