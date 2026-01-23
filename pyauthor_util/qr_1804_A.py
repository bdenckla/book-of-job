from pyauthor_util.job1_common import RECORD_1804_CMN_AB


_BHQ_COMMENT_1804_A = [
    "$BHQ silently ignores the possible שווא part of the possible חטף פתח.",
    " It also silently ignores the possible interpretation of that ink as a געיה.",
    " I.e. other than the prepositive דחי accent,",
    " $BHQ supplies only the (full) פתח that is the consensus expectation here.",
    " $BHQ does so silently, i.e. with no note about the pointing of ה.",
]
RECORD_1804_A = {
    **RECORD_1804_CMN_AB,
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "n_of_m_for_this_word": (1, 2),  # this is record 1 of 2 for this word
    "what-is-weird": "פתח on ה is חטף.",
    "comment": [
        "The quirk that מ has דגש is discussed in a separate entry of mine.",
        " The געיה difference is not important to us here.",
    ],
    "highlight": 1,
    "bhq-comment": _BHQ_COMMENT_1804_A,
    "noted-by": "xBHQ-nBHL-nDM",
}
