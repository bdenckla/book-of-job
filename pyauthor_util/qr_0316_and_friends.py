from pyauthor_util import author
from pyauthor_util.job1_common import num_range

RECORD_0316 = {
    "cv": "3:16",
    "lc": "א֚וֹ",
    "what-is-weird": "יתוב not מהפך",
    "mam": "א֤וֹ",
    "comment": [
        "יתוב doesn’t make sense here because"
        " this is in the poetic rather than prose section of Job",
        [" ", author.paren(num_range("3:2", "42:6")), "."],
    ],
    "highlight": 1,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
        " I don’t think $BHQ is really proposing that μL has יתיב here.",
        " This is more likely a typo (inherited from $BHS) than a deliberate choice.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLC",
}
RECORD_0816 = {
    "cv": "8:16",
    "lc": "יֹ֭נַקְתּ֥וֹ",
    "what-is-weird": "דחי not געיה",
    "mam": "יֹֽנַקְתּ֥וֹ",
    "comment": [
        "Above I have asserted that the consensus has געיה here,",
        " but this געיה, like most cases of געיה, is optional.",
        " Therefore, one could just as easily assert the consensus has no געיה.",
        " I have chosen the consensus to be as close as possible",
        " to the proposed transcription of μL.",
        " I did this in order to make the proposed transcription",
        " seem no weirder than it really is.",
        " In other words, it is better to frame this as a question of דחי vs געיה",
        " than as a question of דחי vs no mark at all.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLC",
}
_COS_CMN = "https://www.chorev.co.il/%D7%98%D7%A2%D7%9E%D7%99-%D7%94%D7%9E%D7%A7%D7%A8%D7%90"
_COS_ENG_REST = "%D7%91%D7%90%D7%A0%D7%92%D7%9C%D7%99%D7%AA-THE-CANTILLATION-OF-SCRIPTURE"
_COS_ENG_ANC = author.anc_h("translation", f"{_COS_CMN}-{_COS_ENG_REST}.htm")
_COS_HEB_ANC = author.anc_h("original", f"{_COS_CMN}.htm")
_FOI_H2 = "foi-sec-star-breuer-cos.html#intro-11.66.rn1"
_FOI_H1 = "https://bdenckla.github.io/MAM-with-doc/foi/"
_FOI_ANC = author.anc_h("here", f"{_FOI_H1}{_FOI_H2}")
_MAM_ANC = author.anc_h("$MAM", "https://purl.org/mam/hebrew-wikisource")
_COMMENT_1413_PARA1 = [
    "$WLC is the source of this (flawed) transcription.",
    #
    " Note that the word in question has a rare and hard-to-understand",
    " phenomenon called “secondary מהפך” by Breuer."
    #
    " It may seem rather extraordinary that this געיה",
    " immediately follows the מהפך,",
    " but this is actually expected (or at least “allowed”)",
    " if the מהפך is secondary, as it is here.",
]
_COMMENT_1413_PARA2 = [
    ["The word ",author.hbo("תָּ֤שִֽׁית")," may be easier to understand"],
    " if one considers it",
    [" and ", author.hbo("לִ֖י"), " (the next word)"],
    " to form a compound word"
    " whose the מקף is, somewhat inexplicably, left implicit.",
    " If the מקף were made explicit, the compound would be written as",
    [" ", author.hbo("תָּ֤שִֽׁית־לִ֖י")],
    " and indeed that is the way that word is written (albeit with the מקף colored gray)"
    " in some editions of ",_MAM_ANC," (מקרא על פי המסורה).",
    #
    " This and a handful of analogous cases are listed",
    [" ",_FOI_ANC, ", with the implicit מקף represented as a tilde (~)."],
]
_COMMENT_1413_PARA3 = [
    "See Breuer CoS sections 11.66.rn1 and 11.79.",
    " (CoS = The Cantillation of Scripture; rn = Roman numeral.)",
    [" (Note that an English ", _COS_ENG_ANC, " of CoS is now available,"],
    " a great boon to students of cantillation who cannot easily read",
    [" the ", _COS_HEB_ANC, " in its modern Hebrew.)"],
]
_COMMENT_1413 = [
    author.para(_COMMENT_1413_PARA1),
    author.para(_COMMENT_1413_PARA2),
    author.para(_COMMENT_1413_PARA3),
]
RECORD_1413 = {
    "cv": "14:13",
    "lc": "תָּ֤שִׁ֥ית",
    "lc-q": "(?)",
    "what-is-weird": "maybe מרכא not געיה",
    "mam": "תָּ֤שִֽׁית",
    "comment-should-not-be-para-wrapped": True,
    "comment": _COMMENT_1413,
    "highlight": 2,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "use-stretched-format": True,
    "bhq-comment": [
        "$BHQ benefits from ignoring $WLC here,",
        " though $BHQ likely ignored $WLC as a whole",
        " rather than considering and rejecting",
        " this particular change in $WLC relative to $BHS.",
    ],
    "noted-by": "xBHQ-xBHL-xDM-nWLC",
}
RECORD_1535 = {
    "cv": "15:35",
    "lc": "וְיָלֹ֣ד",
    "what-is-weird": "מונח on ל not $yod (י)",
    "mam": "וְיָ֣לֹד",
    "comment": [
        "foo",
    ],
    "highlight-lc": 3,
    "highlight-mam": 2,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLC",
}
RECORD_2212 = {
    "cv": "22:12",
    "lc": "רֹ֭אשׁ",
    "what-is-weird": "דחי not טרחא",
    "mam": "רֹ֖אשׁ",
    "comment": [
        "foo",
    ],
    "highlight": 1,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLC",
}
RECORD_3410 = {
    "cv": "34:10",
    "lc": "אַֽנֲשֵׁ֥י",
    "what-is-weird": "געיה not מרכא (on א)",
    "mam": "אַ֥נֲשֵׁ֥י",
    "comment": [
        "foo",
    ],
    "highlight": 1,
    "lc-loc": {"page": "40XY", "column": 0, "line": 0},
    "lc-img": ".png",
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLC",
}
# RECORD_BLANK = {
#     "cv": "foo",
#     "lc": "אבגדהוז",
#     "what-is-weird": "foo",
#     "mam": "foo",
#     "comment": [
#         "foo",
#     ],
#     "highlight": 0,
#     "lc-loc": {"page": "40XY", "column": 0, "line": 0},
#     "lc-img": ".png",
#     "bhq-comment": [
#         "$BHQ is the source of this (flawed) transcription.",
#     ],
#     "noted-by": "tBHQ-xBHL-xDM-zWLC",
# }
