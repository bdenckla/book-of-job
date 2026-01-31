from py import my_html


def _span_rtl(contents):
    return my_html.span(contents, {"dir": "rtl"})


RECORD_1535 = {
    "qr-cv": "15:35",
    "qr-lc-proposed": "וְיָלֹ֣ד",
    "qr-lc-q": "(?)",
    "qr-what-is-weird": [_span_rtl("∅-מונח"), " not מונח-געיה"],
    "qr-consensus": "וְיָ֣לֹֽד",
    "qr-extra-letter-spacing": True,
    "qr-generic-comment": [
        "The proposed transcription of μL above shows nothing (∅) on $yod and מונח on ל.",
        " (By “nothing” on $yod I mean nothing other than קמץ.)",
        " In contrast, the consensus transcription shows מונח on $yod and געיה on ל.",
        " (The געיה on ל is extraordinary since it follows the accent (מונח).)",
        " The proposed transcription seems far-fetched because"
        " there is little evidence of a מונח in any location on this word.",
        " There is a mark that looks like a פתח between the $yod and the ל,",
        " but that is grammatically implausible.",
    ],
    "qr-highlight": [2, 3],
    "qr-lc-loc": {"page": "401B", "column": 1, "line": -3},
    "qr-bhq-comment": [
        "$BHQ has the proposed transcription of μL above.",
    ],
    "qr-noted-by": "tBHQ-xBHL-nDM",
}
