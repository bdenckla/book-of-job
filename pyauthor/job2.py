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
    " I was initially in the cult of BHS:",
    " I thought its was",
    " ",
    my_html.bold("the"),
    " definitive edition of the Hebrew Bible.",
    #
    " Unlike many students of the Hebrew Bible,",
    " I eventually discovered many shortcomings of BHS,",
    " and began to look for better editions.",
    #
    " Such is the power of the cult that",
    " the first alternative I looked into was BHQ (Biblia Hebraica Quinta).",
    #
    " I was only bold enough to look outside of the cult of BHS,",
    " not outside of the cult of DBG (Deutsche Bibelgesellschaft).",
    #
]
_CPARA2 = [
    "What I found was that, for my purposes at least, BHQ was too little, too late."
    #
    " It was too little in two senses: many books of the Bible were not done,",
    " and those that were done did not substantially improve on BHS.",
    #
    " It was too late in the sense that",
    " even when the first volume of BHQ came out (Megillot, 2004),",
    " better, complete editions were already available from other publishers.",
]
_CPARA3 = [
    "I have said that for my purposes BHQ was too little, too late.",
    " But I have not yet said what my purposes are.",
    " My purposes are narrowly focused on the Masoretic Text.",
    " I am not concerned with",
    " the many parts of BHQ that deal with the following:",
]
_C_LIST_ITEMS_AFTER_PARA3 = [
    "sources in languages other than Hebrew,",
    "non-Masoretic (e.g. unpointed) Hebrew sources,",
    "Masorah magna and parva,",
    "the meaning of the text, in any language",
]
_CPARA4 = [
    "For all I know, these parts of BHQ are of the highest quality, and improve greatly on BHS.",
    " But these parts are not my concern.",
]
_CPARA17 = [
    "This document discusses the BHQ edition of the Book of Job,",
    " focusing on its treatment of certain textual variants.",
    " Right now it consists merely of this",
    " ",
    d1v_anchor(),
]
_CBODY = [
    author.heading_level_1(D2_H1_CONTENTS),
    author.para(_CPARA1),
    author.para(_CPARA2),
    author.para(_CPARA3),
    author.unordered_list(_C_LIST_ITEMS_AFTER_PARA3),
    author.para(_CPARA4),
    author.para(_CPARA17),
]
