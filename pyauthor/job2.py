""" Exports gen_html_file and anchor """

from pyauthor.util import author
from pyauthor.common import D2_TITLE
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME


def gen_html_file(tdm_ch, jda):
    author.assert_stem_eq(__file__, D2_FNAME)
    _CBODY = [
        author.heading_level_1(D2_H1_CONTENTS),
        author.para(
            "This document discusses the BHQ edition of the Book of Job, "
            "focusing on its treatment of certain textual variants."
        ),
    ]
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, _CBODY)
