""" Exports gen_html_file and anchor """

from pyauthor.common import D1V_FNAME, d1d_anchor
from pyauthor.common import D1V_H1_CONTENTS
from pyauthor.common import D1V_TITLE
from pyauthor_util.job1_common import intro
from pycmn.my_utils import sl_map
from py import my_html
from pyauthor_util import author
from pyauthor_util.job1_records import RECORDS
from pyauthor_util.job1_make_per_case_data import make_per_case_data


def gen_html_file(tdm_ch):
    author.assert_stem_eq(__file__, D1V_FNAME)
    author.help_gen_html_file(tdm_ch, D1V_FNAME, D1V_TITLE, _CBODY)


_PER_CASE_DATA = sl_map(make_per_case_data, RECORDS)
_CONT_TABLE_1A_ROWS = [pcd["row"] for pcd in _PER_CASE_DATA]
_CBODY = [
    author.heading_level_1(D1V_H1_CONTENTS),
    intro("expanding", "Each", d1d_anchor()),
    my_html.horizontal_rule(),
    author.table_c(_CONT_TABLE_1A_ROWS),
]
