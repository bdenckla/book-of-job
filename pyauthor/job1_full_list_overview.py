""" Exports gen_html_file and anchor """

from pyauthor_util.common_titles_etc import (
    D1V_FNAME,
    d1d_anchor,
    D1V_H1_CONTENTS,
    D1V_TITLE,
)
from pyauthor_util.introduce_quirkrec_table import intro, here_is
from py import my_html
from pyauthor_util import author


def gen_html_file(tdm_ch, ov_and_de):
    author.assert_stem_eq(__file__, D1V_FNAME)
    cbody = _make_cbody(ov_and_de)
    author.help_gen_html_file(tdm_ch, D1V_FNAME, D1V_TITLE, cbody)


def _make_cbody(ov_and_de):
    overview = [od["od-overview"] for od in ov_and_de.values()]
    cbody = [
        author.heading_level_1(D1V_H1_CONTENTS),
        author.para(here_is("Below is a table summarizing", d1d_anchor())),
        *intro("intro-header-only"),
        my_html.horizontal_rule(),
        author.table_c(overview),
    ]
    return cbody
