""" Exports gen_html_file and anchor """

from pyauthor_util.common_titles_etc import D1D_TITLE, D1D_H1_CONTENTS, D1D_FNAME
from pyauthor_util.introduce_quirkrec_table import intro, here_is
from py import my_html
from pyauthor_util import author


def gen_html_file(tdm_ch, ov_and_de):
    author.assert_stem_eq(__file__, D1D_FNAME)
    cbody = _make_cbody(ov_and_de)
    author.help_gen_html_file(tdm_ch, D1D_FNAME, D1D_TITLE, cbody)


def _make_cbody(ov_and_de):
    details = [od["od-details"] for od in ov_and_de.values()]
    cbody = [
        author.heading_level_1(D1D_H1_CONTENTS),
        author.para(here_is("This document presents")),
        *intro("intro-details"),
        my_html.horizontal_rule(),
        *details,
    ]
    return cbody
