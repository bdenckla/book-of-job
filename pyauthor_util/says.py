from pyauthor_util.get_qr_groups import (
    says_who,
    xbhq_and_n3,
    nbhq_and_n3,
    nbhq_and_x3,
    tbhq_and_n3,
    tbhq_and_zdw,
    tbhq_and_zmw,
    xbhq_and_nuxlc,
    tbhq_and_zuxlc,
)
from pycmn.my_utils import sl_map


def says(quirkrec):
    if nbhq_and_x3(quirkrec):
        return ["in μL, says $BHQ’s contribution"]
    if nbhq_and_n3(quirkrec):
        return ["in μL, says $BHQ’s reiteration"]
    if tbhq_and_n3(quirkrec):
        return ["in μL, says $BHQ’s implication"]
    if xbhq_and_n3(quirkrec):
        # yes, the double list is intentional below
        return [["in μL, says ", _english_says_who(quirkrec), " but not $BHQ"]]
    if tbhq_and_zdw(quirkrec) or tbhq_and_zmw(quirkrec):
        return ["in μL, says $BHQ but not $WLC"]
    if xbhq_and_nuxlc(quirkrec):
        return ["in μL, says $UXLC but not $BHQ"]
    if tbhq_and_zuxlc(quirkrec):
        return ["in μL, says $BHQ but not $UXLC"]
    return []


def _english_says_who(quirkrec):
    dsw = sl_map(_dollar_editions, says_who(quirkrec))
    return _english_list(dsw)


def _dollar_editions(e_colon_edition):
    return _DOLLAR[e_colon_edition]


_DOLLAR = {
    "e:BHL": "$BHL",
    "e:DM": "$DM",
    "e:WLC": "$WLC",
}


def _english_list(elements):
    assert len(elements) >= 1
    if len(elements) == 1:
        return elements[0]
    if len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    return ", ".join(elements[:-1]) + f", and {elements[-1]}"
