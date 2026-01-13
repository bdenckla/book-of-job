""" Exports gen_html_file and anchor """

from pyauthor_util import author
from pyauthor.common import D2_TITLE, d1v_anchor
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME
from py import my_html


def gen_html_file(tdm_ch):
    author.assert_stem_eq(__file__, D2_FNAME)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, _CBODY)


_CPARA1 = [
    "Like many students of the Hebrew Bible,",
    " I started out in the cult of $BHS.",
    " I thought $BHS was",
    " ",
    my_html.bold("the"),
    " definitive edition of the Hebrew Bible.",
    #
    " Unlike many students of the Hebrew Bible,",
    " I eventually soured on $BHS,",
    " and began to look for better editions.",
    #
    " Such is the power of the cult that",
    " the first alternative I looked into was $BHQ (Biblia Hebraica Quinta).",
    #
    " I was only bold enough to look outside of the cult of $BHS,",
    " not outside of the cult of $DBG (Deutsche Bibelgesellschaft).",
    #
]
_CPARA2 = [
    "I found $BHQ disappointing, for my purposes."
    #
    " First of all, $BHQ is not only incomplete",
    " but also will not be complete for many years.",
    #
    " More importantly, $BHQ, though it improves upon $BHS in many ways,",
    " is still not quite",
    " ",
    my_html.bold("modern"),
    "."
    #
    " What I mean by “not quite modern” is that it fails to incorporate",
    " the work of other editions."
    " These other editions include the following:",
]
def num_range(start, stop):
    return f"{start}\N{THIN SPACE}\N{EN DASH}\N{THIN SPACE}{stop}"

_C_LIST_ITEMS_AFTER_PARA2 = [
    "$BHL (Dotan, 2001)",
    f"דעת מקרא (Breuer et al., {num_range(1970, 2003)})",
]
_CPARA_2B = [
    "Even the first volume of $BHQ (Megilloth) came out late enough (2004)",
    " to incorporate Dotan’s work in $BHL.",
    " The חמש מגילות volume of דעת מקרא came long before, in 1990.",
]
_CPARA3 = [
    "Since I have said that I found $BHQ disappointing, for my purposes,",
    " I should state what my purposes are.",
    " My purposes are narrowly focused on the Masoretic text.",
    " I am not concerned with",
    " the many parts of $BHQ that deal with the following:",
]
_C_LIST_ITEMS_AFTER_PARA3 = [
    "sources in languages other than Hebrew",
    "non-Masoretic (e.g. unpointed) Hebrew sources",
    "Masorah magna and parva",
    "the meaning of the text",
]
_CPARA4 = [
    "For all I know, these parts of $BHQ are of the highest quality, and improve greatly on $BHS.",
    " But these parts are not my concern.",
]
_CPARA17 = [
    "This document discusses the $BHQ edition of the Book of Job,",
    " focusing on its treatment of certain textual variants.",
    " Right now it consists merely of this",
    " ",
    d1v_anchor(),
]
_CBODY = [
    author.heading_level_1(D2_H1_CONTENTS),
    author.para(_CPARA1),
    author.para(_CPARA2),
    author.unordered_list(_C_LIST_ITEMS_AFTER_PARA2),
    author.para(_CPARA_2B),
    author.para(_CPARA3),
    author.unordered_list(_C_LIST_ITEMS_AFTER_PARA3),
    author.para(_CPARA4),
    author.para(_CPARA17),
]
