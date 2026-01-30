from pyauthor_util.uxlc_change import uxlc_change
from pyauthor_util.golinets import golinets_citation
from pyauthor_util import author


_UXLC_CHANGE_2022_02_17_1 = uxlc_change("2022.04.01", "2022.02.17-1")
_ISAIAH_1306 = author.anc_h("Isaiah 13:6", _UXLC_CHANGE_2022_02_17_1)


_COMMENT_PARA_1 = [
    "The writing is not well preserved here:",
    " the letters have been re-inked,",
    " but among the points, only the דגש in the ד has been re-inked.",
    " So, a דגש in the ש could easily have been lost.",
    " But, because other similar words lack דגש in μL",
    [" (e.g., 27:13, ", _ISAIAH_1306, ", Joel 1:15),"],
    " it seems likely that there was never a דגש in the ש to begin with.",
]
_COMMENT_PARA_2 = [
    ["This case and that of 27:13 are raised in ", golinets_citation("242")],
]
_COMMENT_PARA_3 = [
    "Aside: note that the final פתה",
    " is charitably transcribed as belonging to the ד rather than the $yod.",
]

RECORD_2401 = {
    "qr-cv": "24:1",
    "qr-lc-proposed": "מִ֭שַׁדַּי",
    "qr-what-is-weird": "ש lacks דגש",
    "qr-consensus": "מִ֭שַּׁדַּי",
    "qr-generic-comment": [
        author.para(_COMMENT_PARA_1),
        author.para(_COMMENT_PARA_2),
        author.para(_COMMENT_PARA_3),
    ],
    "qr-highlight": 2,
    "qr-lc-loc": {"page": "403B", "column": 2, "line": 25},
    "qr-noted-by": "tBHQ-xBHL-xDM-xWLC-nUXLC",
    "qr-uxlc-change-url": uxlc_change("2022.04.01", "2022.02.17-2"),
}
