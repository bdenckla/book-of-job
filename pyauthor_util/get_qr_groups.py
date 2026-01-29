def _bhq_and_t4o(quirkrec):
    """t4o: the four others (BHL, DM, WLC, & UXLC)"""
    parts = quirkrec["noted-by"].split("-")
    bhq, bhl, dm = parts[0], parts[1], parts[2]
    wlc = "xWLC" if len(parts) <= 3 else parts[3]
    uxlc = "xUXLC" if len(parts) <= 4 else parts[4]
    assert bhq in ("nBHQ", "xBHQ", "tBHQ")
    assert bhl in ("nBHL", "xBHL")
    assert dm in ("nDM", "xDM")
    assert wlc in ("nWLC", "xWLC", "zWLCmisc", "zWLCdexi")
    assert uxlc in ("nUXLC", "xUXLC", "zUXLC")
    #
    if wlc in ("zWLCmisc", "zWLCdexi"):
        assert (bhq, bhl, dm, uxlc) == ("tBHQ", "xBHL", "xDM", "xUXLC")
    #
    the_4_others = bhl, dm, wlc, uxlc
    return bhq, the_4_others


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


def get_qr_groups(quirkrecs):
    # nbhq, xbhq: noted (as a quirk) in BHQ, not noted (as a quirk) in BHQ
    # ne, xe: noted (as a quirk) elsewhere, not noted (as a quirk) elsewhere
    # zw (zWLCmisc): noted (as consensus) by WLC (combined with MAM):
    #     flagged as a change in WLC relative to BHS, e.g. a bracket-c or bracket-v note.
    #     comparison with MAM revealed that it is a change back towards consensus,
    #     i.e. this is BHS/BHQ proposing a quirk that is not in μL
    q_nbhq_and_x3 = list(filter(_nbhq_and_x3, quirkrecs))
    q_nbhq_and_n3 = list(filter(_nbhq_and_n3, quirkrecs))
    q_xbhq_and_n3 = list(filter(_xbhq_and_n3, quirkrecs))
    q_tbhq_and_n3 = list(filter(_tbhq_and_n3, quirkrecs))
    q_tbhq_and_zwm = list(filter(_tbhq_and_zwm, quirkrecs))
    q_tbhq_and_zwd = list(filter(_tbhq_and_zwd, quirkrecs))
    groups = {
        "nbhq_and_x3": q_nbhq_and_x3,
        "nbhq_and_n3": q_nbhq_and_n3,
        "xbhq_and_n3": q_xbhq_and_n3,
        "tbhq_and_n3": q_tbhq_and_n3,
        "tbhq_and_zwd": q_tbhq_and_zwd,
        "tbhq_and_zwm": q_tbhq_and_zwm,
    }
    return groups
