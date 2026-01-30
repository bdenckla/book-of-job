from pyauthor_util import author
from pyauthor_util.job_common import correctly_ignores


RECORD_3419 = {
    "qr-bhla-i": 42,
    "qr-cv": "34:19",
    "qr-n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "qr-lc-proposed": "נִּכַּר־",
    "qr-what-is-weird": "נ has דגש",
    "qr-consensus": "נִכַּר־",
    "qr-generic-comment": [
        "The possible דגש is faint.",
        " The adjacent דגש (on כ) and other nearby marks are quite clear,",
        " casting suspicion on the legitimacy of this דגש.",
    ],
    "qr-highlight": 1,
    "qr-lc-loc": {"page": "406B", "column": 2, "line": -2},
    "qr-bhq-comment": [author.para(correctly_ignores("דגש", "34:19"))],
    "qr-noted-by": "xBHQ-nBHL-nDM",
}
