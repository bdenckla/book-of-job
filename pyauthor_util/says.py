from pyauthor_util.english_list import english_list
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
    tbhq_and_adm,
)
from pycmn.my_utils import sl_map


def says(quirkrec):
    if nbhq_and_x3(quirkrec):
        return ["says $BHQ’s contribution"]
    if nbhq_and_n3(quirkrec):
        return ["says $BHQ’s reiteration"]
    if tbhq_and_n3(quirkrec):
        return ["says $BHQ’s implication"]
    if xbhq_and_n3(quirkrec):
        # yes, the double list, i.e. [[x, y, z]], is intentional below
        return [["says ", _english_says_who(quirkrec), " but not $BHQ"]]
    if tbhq_and_zdw(quirkrec) or tbhq_and_zmw(quirkrec):
        return ["says $BHQ but not $WLC"]
    if xbhq_and_nuxlc(quirkrec):
        return ["says $UXLC but not $BHQ"]
    if tbhq_and_zuxlc(quirkrec):
        return ["says $BHQ but not $UXLC"]
    if tbhq_and_adm(quirkrec):
        return ["says $DM"]
    assert False, "Unhandled case in says()"


def _english_says_who(quirkrec):
    dsw = sl_map(_dollar_editions, says_who(quirkrec))
    return english_list(dsw)


def _dollar_editions(e_colon_edition):
    return _DOLLAR[e_colon_edition]


_DOLLAR = {
    "e:BHL": "$BHL",
    "e:DM": "$DM",
    "e:WLC": "$WLC",
}
