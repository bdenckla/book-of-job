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
    from pyauthor_util.author import add_dollar_sub_entries

    add_dollar_sub_entries(dollar_sub_extras())


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
            f"Use a $-entry to suppress auto-linking."
        )
    if len(sids) > 1:
        assert False, (
            f"Verse reference {cv} has multiple quirkrec records "
            f"({', '.join(sids)}). "
            f"Use a $link_ or $plain_ entry to handle this."
        )
    sid = sids[0]
    href = f"{_d1d_fname}#row-{sid}"
    return my_html.anchor_h(cv, href)


def _link_to_sid(cv, wordid):
    """Build an <a> element linking to a specific multi-record row."""
    ch, vs = cv.split(":")
    sid = f"{int(ch):02d}{int(vs):02d}-{wordid}"
    sids = _cv_to_sids.get(cv, [])
    assert sid in sids, (
        f"$link_{ch}_{vs}_{wordid} → SID {sid} "
        f"not found in known SIDs for {cv}: {sids}"
    )
    href = f"{_d1d_fname}#row-{sid}"
    return my_html.anchor_h(cv, href)


def dollar_sub_extras():
    """Return extra $-dispatch entries for verse-ref special cases.

    These cover:
    - $plain_C_V: multi-record Job verses rendered as plain text
    - $link_C_V_WORDID: multi-record Job verses linked to a specific row
    - $BOOK_C_V: non-Job bible references rendered as plain text
    """
    entries = {}
    # Multi-record Job verses: plain text (no link)
    for cv_under, display in [
        ("3_2", "3:2"),
        ("42_6", "42:6"),
        ("18_4", "18:4"),
        ("19_16", "19:16"),
        ("34_33", "34:33"),
    ]:
        entries[f"$plain_{cv_under}"] = display
    # Multi-record Job verses: disambiguated links
    for cv, cv_under, wordid in [
        ("22:21", "22_21", "3MV"),
        ("38:12", "38_12", "YD3F_HJXR"),
        ("38:12", "38_12", "HMYMY5"),
        ("34:33", "34_33", "VMH0YD3F"),
        ("34:33", "34_33", "HM3M5"),
        ("34:33", "34_33", "YJLMNH_2_of_2_FTW"),
    ]:
        entries[f"$link_{cv_under}_{wordid}"] = _link_to_sid(cv, wordid)
    # Non-Job bible references: plain text
    for key, display in [
        ("$2Kings_4_7", "2 Kings 4:7"),
        ("$Lamentations_4_16", "Lamentations 4:16"),
        ("$2Samuel_18_20", "2 Samuel 18:20"),
        ("$1Samuel_12_10", "1 Samuel 12:10"),
    ]:
        entries[key] = display
    return entries
