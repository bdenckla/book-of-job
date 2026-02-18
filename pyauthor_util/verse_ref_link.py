"""Auto-link chapter:verse references to quirkrec detail rows."""

from py import my_html
from pyauthor_util.short_id_etc import short_id

# Module-level verse-link mapping, set by init_verse_links().
# Maps chapter:verse strings (e.g. "27:13") to a list of SIDs.
_cv_to_sids = None
_d1d_fname = None


def init_verse_links(enriched_quirkrecs, d1d_fname):
    """Build and store the verse-reference linking map.

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
    """Return extra $-dispatch entries for verse-ref linking.

    These cover:
    - $link_C_V: single-record Job verses linked to their detail row
    - $link_C_V_WORDID: multi-record Job verses linked to a specific row

    Plain-text entries ($plain_C_V, $BOOK_C_V) are in the static
    dispatch dict in author.py since they must be available at import time.
    """
    entries = {}
    # Single-record Job verses: auto-generate $link_C_V for each
    for cv, sids in _cv_to_sids.items():
        if len(sids) == 1:
            ch, vs = cv.split(":")
            sid = sids[0]
            href = f"{_d1d_fname}#row-{sid}"
            entries[f"$link_{ch}_{vs}"] = my_html.anchor_h(cv, href)
    # Multi-record Job verses: disambiguated links
    for cv, cv_under, wordid in [
        ("18:4", "18_4", "HLM3N5_2_of_2_FTW"),
        ("19:16", "19_16", "QRAFY"),
        ("22:21", "22_21", "3MV"),
        ("38:12", "38_12", "YD3F_HJXR"),
        ("38:12", "38_12", "HMYMY5"),
        ("34:33", "34_33", "VMH0YD3F"),
        ("34:33", "34_33", "HM3M5"),
        ("34:33", "34_33", "YJLMNH_2_of_2_FTW"),
    ]:
        entries[f"$link_{cv_under}_{wordid}"] = _link_to_sid(cv, wordid)
    return entries
