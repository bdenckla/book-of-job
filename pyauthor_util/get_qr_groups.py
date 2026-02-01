from pyauthor_util.noted_by import nb_dict, startswith_n, startswith_x
from pycmn.my_utils import dv_map


def _foobhq_and_n3(foobhq, nbd):
    return nbd["e:BHQ"] == foobhq and any(
        startswith_n(nbd, e) for e in ("e:BHL", "e:DM", "e:WLC")
    )


def _foobhq_and_x3(foobhq, nbd):
    return nbd["e:BHQ"] == foobhq and all(
        startswith_x(nbd, e) for e in ("e:BHL", "e:DM", "e:WLC")
    )


def _nbhq_and_n3(quirkrec):
    nbd = nb_dict(quirkrec)
    return _foobhq_and_n3("nBHQ", nbd)


def _nbhq_and_x3(quirkrec):
    nbd = nb_dict(quirkrec)
    return _foobhq_and_x3("nBHQ", nbd)


def _xbhq_and_n3(quirkrec):
    nbd = nb_dict(quirkrec)
    return _foobhq_and_n3("xBHQ", nbd)


def _tbhq_and_n3(quirkrec):
    nbd = nb_dict(quirkrec)
    return _foobhq_and_n3("tBHQ", nbd)


def _tbhq_and_zwd(quirkrec):
    nbd = nb_dict(quirkrec)
    return nbd["e:WLC"] == "zdexiWLC"


def _tbhq_and_zwm(quirkrec):
    nbd = nb_dict(quirkrec)
    return nbd["e:WLC"] == "zmiscWLC"


def _xbhq_and_nuxlc(quirkrec):
    nbd = nb_dict(quirkrec)
    return nbd["e:UXLC"] == "nUXLC"


def _tbhq_and_zuxlc(quirkrec):
    nbd = nb_dict(quirkrec)
    return nbd["e:UXLC"] == "zUXLC"


def _filter(quirkrecs, filter_fn):
    return list(filter(filter_fn, quirkrecs))


_FILTER_FNS = {
    "nbhq_and_x3": _nbhq_and_x3,
    "nbhq_and_n3": _nbhq_and_n3,
    "xbhq_and_n3": _xbhq_and_n3,
    "tbhq_and_n3": _tbhq_and_n3,
    "tbhq_and_zwd": _tbhq_and_zwd,
    "tbhq_and_zwm": _tbhq_and_zwm,
    "xbhq_and_nuxlc": _xbhq_and_nuxlc,
    "tbhq_and_zuxlc": _tbhq_and_zuxlc,
}
# nbhq: noted (as a quirk) in BHQ
# xbhq: not noted (as a quirk) in BHQ
# n3, noted (as a quirk) in one of "the three"
# x3: not noted (as a quirk) in one of "the three"
# zw (zmiscWLC): noted (as consensus) by WLC (combined with MAM):
#     flagged as a change in WLC relative to BHS, e.g. a bracket-c or bracket-v note.
#     comparison with MAM revealed that it is a change back towards consensus,
#     i.e. this is BHS/BHQ proposing a quirk that is not in μL (according to WLC at least)


def get_qr_groups(quirkrecs):
    groups = dv_map((_filter, quirkrecs), _FILTER_FNS)
    return groups
