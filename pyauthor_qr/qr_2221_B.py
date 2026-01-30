from pyauthor_util.job_common import RECORD_2221_CMN_AB


_COMMENT_2221_B = [
    "Perhaps some super-faint remains of an אתנח under ל can be seen.",
    " The top dot of the שווא (under the ש) is super-faint.",
    " See my entry for 22:21 עמי for μA and μY images.",
]
_BHQ_COMMENT_2221_B = [
    "$BHQ (charitably) transcribes the top dot of the שווא",
    " using, as one often has to, faint evidence bolstered by consensus expectations.",
    " $BHQ notes (as does $BHS) that whereas the ל of ושלם is unpointed in μL,",
    " that ל has קמץ and אתנח in μA and μY.",
]
RECORD_2221_B = {
    **RECORD_2221_CMN_AB,
    "qr-n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "qr-lc-proposed": "וּשְׁלם",
    "qr-what-is-weird": "ל lacks קמץ־אתנח",
    "qr-consensus": "וּשְׁלָ֑ם",
    "qr-generic-comment": _COMMENT_2221_B,
    "qr-highlight": 3,
    "qr-lc-loc": {"page": "403B", "column": 1, "line": -6},
    "qr-bhq-comment": _BHQ_COMMENT_2221_B,
    "qr-noted-by": "nBHQ-xBHL-xDM-nWLC",
}
