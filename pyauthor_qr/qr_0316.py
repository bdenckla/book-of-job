from pyauthor_util import author
from pyauthor_util.num_range import num_range


RECORD_0316 = {
    "cv": "3:16",
    "lc": "א֚וֹ",
    "what-is-weird": "יתיב not מהפך",
    "mam": "א֤וֹ",
    "comment": [
        "יתיב doesn’t make sense here because"
        " this is in the poetic rather than prose section of Job",
        [" ", author.paren(num_range("3:2", "42:6")), "."],
    ],
    "highlight": 1,
    "lc-loc": {"page": "398A", "column": 1, "line": 3},
    "bhq-comment": [
        "$BHQ is the source of this (flawed) transcription.",
        " I don’t think $BHQ is really proposing that μL has יתיב here.",
        " This is more likely a typo (inherited from $BHS) than a deliberate choice.",
    ],
    "noted-by": "tBHQ-xBHL-xDM-zWLCmisc",
}
