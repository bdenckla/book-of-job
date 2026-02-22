from pyauthor_util import author

_COMMENT_PARA1 = [
    "In μY, the mark we would charitably transcribe as דחי",
    " appears far to the left of where we would expect it,",
    " i.e. far \u201Clater\u201D than we would expect it.",
    " Possibly the ל ascender from the line below",
    " encroached on the area where the $naqdan would normally put a דחי;",
    " possibly the descender of the preceding ק was in the way, too.",
    " See $link_35_14 for an analogous case",
    " and some further discussion of this phenomenon",
    " of \u201Clate\u201D דחי in general.",
]
_COMMENT_PARA2 = [
    "More significant than the \u201Clateness\u201D of the דחי in μY",
    " is its use of מונח rather than מקף on the previous atom,",
    [" i.e. on ", author.span_unpointed_tanakh("התשחק"), "."],
]
RECORD_4029 = {
    "qr-cv": "40:29",
    "qr-lc-proposed": "בּ֖וֹ",
    "qr-what-is-weird": "טרחא not דחי",
    "qr-consensus": "בּ֭וֹ",
    "qr-generic-comment": [
        author.para(_COMMENT_PARA1),
        author.para(_COMMENT_PARA2),
    ],
    "qr-highlight": 1,
    "qr-lc-loc": {"page": "409A", "column": 1, "line": 11},
    "qr-ac-loc": {"page": "281r", "column": 1, "line": 27, "word": 5},
    "qr-noted-by": "tBHQ-zdexiWLC",
}
