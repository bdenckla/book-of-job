def _bhq_and_others(quirkrec):
    parts = quirkrec["noted-by"].split("-")
    bhq, bhl, dm = parts[0], parts[1], parts[2]
    wlc = "xWLC" if len(parts) == 3 else parts[3]
    assert bhq in ("nBHQ", "xBHQ", "tBHQ")
    assert bhl in ("nBHL", "xBHL")
    assert dm in ("nDM", "xDM")
    assert wlc in ("nWLC", "xWLC", "zWLCmisc", "zWLCdexi")
    others = bhl, dm, wlc
    return bhq, others


def _startswith_n(part):
    return part.startswith("n")


def _foobhq_and_ne(foobhq, quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == foobhq and any(_startswith_n(part) for part in others)


def _nbhq_and_ne(quirkrec):
    return _foobhq_and_ne("nBHQ", quirkrec)


def _xbhq_and_ne(quirkrec):
    return _foobhq_and_ne("xBHQ", quirkrec)


def _tbhq_and_ne(quirkrec):
    return _foobhq_and_ne("tBHQ", quirkrec)


def _tbhq_and_zwd(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "tBHQ" and others == ("xBHL", "xDM", "zWLCdexi")


def _tbhq_and_zwm(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "tBHQ" and others == ("xBHL", "xDM", "zWLCmisc")


def _startswith_x(part):
    return part.startswith("x")


def _nbhq_and_xe(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "nBHQ" and all(_startswith_x(part) for part in others)


def get_groups(quirkrecs):
    # nbhq, xbhq: noted (as a quirk) in BHQ, not noted (as a quirk) in BHQ
    # ne, xe: noted (as a quirk) elsewhere, not noted (as a quirk) elsewhere
    # zw (zWLCmisc): noted (as consensus) by WLC (combined with MAM):
    #     flagged as a change in WLC relative to BHS, e.g. a bracket-c or bracket-v note.
    #     comparison with MAM revealed that it is a change back towards consensus,
    #     i.e. this is BHS/BHQ proposing a quirk that is not in μL
    q_nbhq_and_xe = list(filter(_nbhq_and_xe, quirkrecs))
    q_nbhq_and_ne = list(filter(_nbhq_and_ne, quirkrecs))
    q_xbhq_and_ne = list(filter(_xbhq_and_ne, quirkrecs))
    q_tbhq_and_ne = list(filter(_tbhq_and_ne, quirkrecs))
    q_tbhq_and_zwm = list(filter(_tbhq_and_zwm, quirkrecs))
    q_tbhq_and_zwd = list(filter(_tbhq_and_zwd, quirkrecs))
    groups = [
        q_nbhq_and_xe,
        q_nbhq_and_ne,
        q_xbhq_and_ne,
        q_tbhq_and_ne,
        q_tbhq_and_zwd,
        q_tbhq_and_zwm,
    ]
    return groups
