""" Exports gen_html_file and anchor """

from pyauthor_util import author
from pyauthor_util.para_and_table import para_and_table
from pyauthor_util.common_titles_etc import D4_TITLE, D4_H1_CONTENTS, D4_FNAME


def gen_html_file(tdm_ch, ov_and_de, qr_groups):
    author.assert_stem_eq(__file__, D4_FNAME)
    cbody = _make_cbody(tdm_ch, ov_and_de, qr_groups)
    author.help_gen_html_file(tdm_ch, D4_FNAME, D4_TITLE, cbody)


def _make_cbody(tdm_ch, ov_and_de, qr_groups):
    cbody = [
        author.heading_level_1(D4_H1_CONTENTS),
        para_and_table(_cpara_adm, tdm_ch, ov_and_de, qr_groups, "tbhq_and_adm"),
    ]
    return cbody


def _cpara_adm(the_len):
    return ["The following quirks in μA are reported by $DM but not by $BHQ."]
