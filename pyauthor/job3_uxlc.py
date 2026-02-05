""" Exports gen_html_file and anchor """

from pyauthor_util import author
from pyauthor_util.para_and_table import para_and_table
from pyauthor_util.common_titles_etc import D3_TITLE, D3_H1_CONTENTS, D3_FNAME


def gen_html_file(tdm_ch, ov_and_de, qr_groups):
    author.assert_stem_eq(__file__, D3_FNAME)
    cbody = _make_cbody(ov_and_de, qr_groups)
    author.help_gen_html_file(tdm_ch, D3_FNAME, D3_TITLE, cbody)


def _make_cbody(ov_and_de, qr_groups):
    cbody = [
        author.heading_level_1(D3_H1_CONTENTS),
        para_and_table(_cpara_xn, ov_and_de, qr_groups["xbhq_and_nuxlc"]),
        para_and_table(_cpara_tz, ov_and_de, qr_groups["tbhq_and_zuxlc"]),
    ]
    return cbody


def _cpara_xn(the_len):
    """xn: xbhq_and_nuxlc"""
    return [
        ["$BHQ does not transcribe ", str(the_len)],
        [" quirks in μL that are noted"],
        [" in $UXLC. They are as follows:"],
    ]


def _cpara_tz(the_len):
    """tz: tbhq_and_zuxlc"""
    return [
        ["$BHQ transcribes but does not note ", str(the_len)],
        [" quirks in μL that are noted"],
        [" as likely false by $UXLC. They are as follows:"],
    ]
