""" Exports gen_html_file and anchor """

from pyauthor.common import D1D_TITLE
from pyauthor.common import D1D_H1_CONTENTS
from pyauthor.common import D1D_FNAME
from pyauthor.util.job1_common import intro
from pycmn.my_utils import sl_map
from py import my_html
from pyauthor.util import author
from pyauthor.util.job1_records import RECORDS
from pyauthor.util.job1_make_per_case_data import make_per_case_data


def gen_html_file(tdm_ch):
    author.assert_stem_eq(__file__, D1D_FNAME)
    author.help_gen_html_file(tdm_ch, D1D_FNAME, D1D_TITLE, _CBODY)


_PER_CASE_DATA = sl_map(make_per_case_data, RECORDS)
_DETAILS = [pcd["details"] for pcd in _PER_CASE_DATA]
_CBODY = [
    author.heading_level_1(D1D_H1_CONTENTS),
    *intro("further expanding", "The header of each"),
    my_html.horizontal_rule(),
    *_DETAILS,
]
