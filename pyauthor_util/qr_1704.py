from pyauthor_util.job1_common import correctly_ignores


RECORD_1704 = {
    "cv": "17:4",
    "lc": "מִּשָּׂ֑כֶל",
    "lc-q": "(?)",
    "what-is-weird": "מ may have דגש",
    "mam": "מִשָּׂ֑כֶל",
    "comment": [
        "The color image of μL reveals this דגש to be unlikely.",
        " Surprisingly, $BHL includes this דגש in its body text rather than noting it in $BHL_A.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "402A", "column": 1, "line": 5},
    "lc-img": "1704.png",
    "bhq-comment": correctly_ignores("דגש", "17:4"),
    "noted-by": "xBHQ-xBHL-xDM-nWLC",
    "uxlc-needs-fix": [
        "UXLC should do one of the following.",
        "(1) Remove the דגש from מ and note the uncertainty in transcription.",
        "(2) Leave the דגש and note the divergence from consensus as well as the uncertainty in transcription.",
    ],
    # This is a bracket-p note in WLC.
    # We take it to note a quirk because MAM reveals that WLC is diverging from consensus here.
    # (Normally we only take WLC to note a quirk in the case of bracket-1 notes.)
}