from pyauthor_util.golinets import golinets_citation
from pyauthor_util.uxlc_change import uxlc_change
import pyauthor_util.author as author


_COMPAR1 = [
    "There is little or no evidence of a דגש in the צ,",
    " and the consensus has no such דגש.",
]
_COMPAR2 = [
    "It is said (from direct inspection of μL in Russia) that there is",
    " “a pale yellow dot in the [צ]",
    " which could be the trace of a worn-off [דגש]”",
    [" in ", golinets_citation("242")],
]
_COMPAR3 = [
    "This is interesting to know, since this pale yellow dot is not visible in the color image.",
    " All that is present in the color image is a slight smudge between the צ and the נ.",
    " This smudge closely resembles other nearby smudges.",
]
_COMPAR4 = [
    "Though interesting, this report of a pale yellow dot still falls well under the “little”",
    " of my assessment that their is little or no evidence of a דגש here.",
]

RECORD_0505 = {
    "qr-cv": "5:5",
    "qr-lc-proposed": "מִצִּנִּ֥ים",
    "qr-what-is-weird": "צ has דגש",
    "qr-consensus": "מִצִנִּ֥ים",
    "qr-highlight": 2,
    "qr-comment-has-paras": True,
    "qr-comment": [
        author.para(_COMPAR1),
        author.para(_COMPAR2),
        author.para(_COMPAR3),
        author.para(_COMPAR4),
    ],
    "qr-lc-loc": {"page": "398A", "column": 2, "line": 22},
    "qr-bhq-comment": [
        "$BHQ is the source of the proposed transcription of μL above."
        " The proposed transcription",
        " must either be a simple typo or",
        " must spring from some source other than μL or the consensus.",
    ],
    "qr-noted-by": "tBHQ-xBHL-xDM-xWLC-zUXLC",
    "qr-uxlc-change-url": uxlc_change("2023.10.19", "2023.06.10-1"),
}
