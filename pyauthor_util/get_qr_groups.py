from pycmn.my_utils import dv_map


def _bhq_and_t4o(quirkrec):
    """t4o: the four others (BHL, DM, WLC, & UXLC)"""
    parts = quirkrec["qr-noted-by"].split("-")
    bhq, bhl, dm = parts[0], parts[1], parts[2]
    wlc = "xWLC" if len(parts) <= 3 else parts[3]
    uxlc = "xUXLC" if len(parts) <= 4 else parts[4]
    _do_solo_asserts(bhq, bhl, dm, wlc, uxlc)
    _do_combo_asserts(bhq, bhl, dm, wlc, uxlc)
    the_4_others = bhl, dm, wlc, uxlc
    return bhq, the_4_others


def _do_solo_asserts(bhq, bhl, dm, wlc, uxlc):
    assert bhq in ("nBHQ", "xBHQ", "tBHQ")
    assert bhl in ("nBHL", "xBHL")
    assert dm in ("nDM", "xDM")
    assert wlc in ("nWLC", "xWLC", "zWLCmisc", "zWLCdexi")
    assert uxlc in ("nUXLC", "xUXLC", "zUXLC")


def _do_combo_asserts(bhq, bhl, dm, wlc, uxlc):
    if wlc in ("zWLCmisc", "zWLCdexi"):
        assert (bhq, bhl, dm, uxlc) == ("tBHQ", "xBHL", "xDM", "xUXLC")
    if uxlc == "zUXLC":
        assert (bhq, bhl, dm, wlc) == ("tBHQ", "xBHL", "xDM", "xWLC")
    if uxlc == "nUXLC":
        assert (bhq, bhl, dm, wlc) == ("tBHQ", "xBHL", "xDM", "xWLC")


def _bhq_and_t3o(quirkrec):
    """t3o: the three others (BHL, DM, & WLC)"""
    bhq, t4o = _bhq_and_t4o(quirkrec)
    return bhq, t4o[:3]


def _startswith_n(part):
    return part.startswith("n")


def _startswith_x(part):
    return part.startswith("x")


def _foobhq_and_n3(foobhq, quirkrec):
    bhq, t3o = _bhq_and_t3o(quirkrec)
    return bhq == foobhq and any(_startswith_n(part) for part in t3o)


def _nbhq_and_x3(quirkrec):
    bhq, t3o = _bhq_and_t3o(quirkrec)
    return bhq == "nBHQ" and all(_startswith_x(part) for part in t3o)


def _nbhq_and_n3(quirkrec):
    return _foobhq_and_n3("nBHQ", quirkrec)


def _xbhq_and_n3(quirkrec):
    return _foobhq_and_n3("xBHQ", quirkrec)


def _tbhq_and_n3(quirkrec):
    return _foobhq_and_n3("tBHQ", quirkrec)


def _tbhq_and_zwd(quirkrec):
    _bhq, t3o = _bhq_and_t3o(quirkrec)
    return t3o[2] == "zWLCdexi"


def _tbhq_and_zwm(quirkrec):
    _bhq, t3o = _bhq_and_t3o(quirkrec)
    return t3o[2] == "zWLCmisc"


def _tbhq_and_nu(quirkrec):
    _bhq, t4o = _bhq_and_t4o(quirkrec)
    return t4o[3] == "nUXLC"


def _tbhq_and_zu(quirkrec):
    _bhq, t4o = _bhq_and_t4o(quirkrec)
    return t4o[3] == "zUXLC"


def _filter(quirkrecs, filter_fn):
    return list(filter(filter_fn, quirkrecs))


_FILTER_FNS = {
    "nbhq_and_x3": _nbhq_and_x3,
    "nbhq_and_n3": _nbhq_and_n3,
    "xbhq_and_n3": _xbhq_and_n3,
    "tbhq_and_n3": _tbhq_and_n3,
    "tbhq_and_zwd": _tbhq_and_zwd,
    "tbhq_and_zwm": _tbhq_and_zwm,
    "tbhq_and_nu": _tbhq_and_nu,
    "tbhq_and_zu": _tbhq_and_zu,
}
# nbhq: noted (as a quirk) in BHQ
# xbhq: not noted (as a quirk) in BHQ
# n3, noted (as a quirk) in one of "the three"
# x3: not noted (as a quirk) in one of "the three"
# zw (zWLCmisc): noted (as consensus) by WLC (combined with MAM):
#     flagged as a change in WLC relative to BHS, e.g. a bracket-c or bracket-v note.
#     comparison with MAM revealed that it is a change back towards consensus,
#     i.e. this is BHS/BHQ proposing a quirk that is not in μL (according to WLC at least)


def get_qr_groups(quirkrecs):
    groups = dv_map((_filter, quirkrecs), _FILTER_FNS)
    return groups
