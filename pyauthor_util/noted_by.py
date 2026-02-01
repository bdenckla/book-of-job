import re
from pycmn.my_utils import sl_map


_DEFAULT = {
    "e:BHQ": "xBHQ",
    "e:BHL": "xBHL",
    "e:DM": "xDM",
    "e:WLC": "xWLC",
    "e:UXLC": "xUXLC",
}
_STARTSWITH_N = {
    "e:BHQ": "nBHQ",
    "e:BHL": "nBHL",
    "e:DM": "nDM",
    "e:WLC": "nWLC",
    "e:UXLC": "nUXLC",
}
_STARTSWITH_X = {
    "e:BHQ": "xBHQ",
    "e:BHL": "xBHL",
    "e:DM": "xDM",
    "e:WLC": "xWLC",
    "e:UXLC": "xUXLC",
}
EDITIONS = tuple(k for k in _DEFAULT.keys())


def nb_dict(quirkrec):
    parts = quirkrec["qr-noted-by"].split("-")
    pairs = sl_map(_nb_pair, parts)
    sparse_dict = dict(pairs)
    full_dict = _fill_in(sparse_dict)
    _do_asserts(full_dict)
    return full_dict


def startswith_n(nbd, edition_key):
    return nbd[edition_key] == _STARTSWITH_N[edition_key]


def startswith_x(nbd, edition_key):
    return nbd[edition_key] == _STARTSWITH_X[edition_key]


def x_uclc(quirkrec):
    nbd = nb_dict(quirkrec)
    return nbd["e:UXLC"] == "xUXLC"


def _do_asserts(nbd):
    bhq, bhl, dm, wlc, uxlc = (nbd[e] for e in EDITIONS)
    _do_solo_asserts(bhq, bhl, dm, wlc, uxlc)
    _do_combo_asserts(bhq, bhl, dm, wlc, uxlc)


def _do_solo_asserts(bhq, bhl, dm, wlc, uxlc):
    assert bhq in ("nBHQ", "xBHQ", "tBHQ")
    assert bhl in ("nBHL", "xBHL")
    assert dm in ("nDM", "xDM")
    assert wlc in ("nWLC", "xWLC", "zmiscWLC", "zdexiWLC")
    assert uxlc in ("nUXLC", "xUXLC", "zUXLC")


def _do_combo_asserts(bhq, bhl, dm, wlc, uxlc):
    if wlc in ("zmiscWLC", "zdexiWLC"):
        assert (bhq, bhl, dm, uxlc) == ("tBHQ", "xBHL", "xDM", "xUXLC")
    if uxlc == "zUXLC":
        assert (bhq, bhl, dm, wlc) == ("tBHQ", "xBHL", "xDM", "xWLC")
    if uxlc == "nUXLC":
        assert (bhq, bhl, dm, wlc) == ("xBHQ", "xBHL", "xDM", "xWLC")


def _fill_in(nb_dict):
    full = {e: nb_dict.get(e) or _DEFAULT[e] for e in EDITIONS}
    return full


def _nb_pair(part):
    """Turns e.g. "xBHL" into ("e:BHL", "xBHL")"""
    match = re.match(r"^([a-z]+)([A-Z].*)$", part)
    assert match is not None, f"part={part}"
    assert len(match.groups()) == 2
    _lower, upper = match.groups()
    return f"e:{upper}", part
