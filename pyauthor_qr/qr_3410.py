from pyauthor_util import author

_COMMENT_PARA1 = [
    "Note that consensus has a rare and hard-to-understand",
    " phenomenon called “secondary מרכא” by Breuer."
    #
    " It may seem rather extraordinary to have two מרכא marks on the same word,",
    " but this is actually expected (or at least “allowed”).",
]
_FOI_H2 = "foi-sec-merk.html#intro-poetic/(mer)/(mer),(mer)"
_FOI_H1 = "https://bdenckla.github.io/MAM-with-doc/foi/"
_FOI_ANC = author.anc_h("here", f"{_FOI_H1}{_FOI_H2}")
_COMMENT_PARA2 = [
    "This is one of about a dozen analogous cases listed",
    [" ", _FOI_ANC, "."],
]
_COS_CMN = (
    "https://www.chorev.co.il/%D7%98%D7%A2%D7%9E%D7%99-%D7%94%D7%9E%D7%A7%D7%A8%D7%90"
)
_COS_ENG_REST = (
    "%D7%91%D7%90%D7%A0%D7%92%D7%9C%D7%99%D7%AA-THE-CANTILLATION-OF-SCRIPTURE"
)
_COS_ENG_ANC = author.anc_h("translation", f"{_COS_CMN}-{_COS_ENG_REST}.htm")
_COS_HEB_ANC = author.anc_h("original", f"{_COS_CMN}.htm")
_COMMENT_PARA3 = [
    "See Breuer CoS sections 9.23, 9.24, and 11.20.",
    " (CoS = The Cantillation of Scripture.)",
    [" (Note that an English ", _COS_ENG_ANC, " of CoS is now available,"],
    " a great boon to students of cantillation who cannot easily read",
    [" the ", _COS_HEB_ANC, " in its modern Hebrew.)"],
]
RECORD_3410 = {
    "qr-cv": "34:10",
    "qr-lc-proposed": "אַֽנֲשֵׁ֥י",
    "qr-what-is-weird": "געיה not מרכא (on א)",
    "qr-consensus": "אַ֥נֲשֵׁ֥י",
    "qr-generic-comment": [
        author.para(_COMMENT_PARA1),
        author.para(_COMMENT_PARA2),
        author.para(_COMMENT_PARA3),
    ],
    "qr-highlight": 1,
    "qr-lc-loc": {"page": "406B", "column": 2, "line": 14},
    "qr-ac-loc": {"page": "279r", "column": 1, "line": 10, "word": 5},
    "qr-noted-by": "tBHQ-zmiscWLC",
}
