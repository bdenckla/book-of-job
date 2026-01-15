""" Exports gen_html_file and anchor """

from pyauthor.common import D1D_TITLE
from pyauthor.common import D1D_H1_CONTENTS
from pyauthor.common import D1D_FNAME
from pyauthor_util.job1_common import intro, here_is
from py import my_html
from pyauthor_util import author


def gen_html_file(tdm_ch, ov_and_de):
    author.assert_stem_eq(__file__, D1D_FNAME)
    author.help_gen_html_file(tdm_ch, D1D_FNAME, D1D_TITLE, _make_cbody(ov_and_de))


def _make_cbody(ov_and_de):
    details = [od["od-details"] for od in ov_and_de]
    cbody = [
        author.heading_level_1(D1D_H1_CONTENTS),
        author.para(here_is("This document presents")),
        *intro("intro-details"),
        my_html.horizontal_rule(),
        *details,
    ]
    return cbody