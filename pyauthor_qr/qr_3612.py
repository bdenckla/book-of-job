from py import my_html
from pyauthor_util import author
from pyauthor_util.job_common import CAM1753_PAGE_URL_BASE


_BHQ_COMMENT_3612 = [
    "Here $BHQ has a typo:",
    [" it has ", author.hbo("בִּבְלִ־"), " rather than ", author.hbo("בִּבְלִי־")],
    " in the word it reports for μA and μY.",
    " I.e. it is missing a final $yod before the מקף.",
    " The same typo appears in the $BHQ section “Commentary on the Critical Apparatus.”",
    " In addition to the typo, for some reason $BHQ reports this word as being the קרי",
    [" of μY, i.e. M", my_html.sup("Y(qere)")],
    [" rather than just M", my_html.sup("Y"), "."],
    " I see no “Masora dot pair”",
    " (μY’s equivalent of a masorah circle)",
    " on this word in μY.",
    " Nor do I see any קרי note in the margin.",
]
RECORD_3612 = {
    "qr-cv": "36:12",
    "qr-lc-proposed": "כִּבְלִי־",
    "qr-what-is-weird": "כ not ב",
    "qr-consensus": "בִּבְלִי־",
    "qr-generic-comment": [
        "Although my focus is pointing rather than spelling,",
        " I am interested in a spelling difference like this,",
        " since it is not just a חסר vs מלא difference.",
    ],
    "qr-highlight": 1,
    "qr-lc-loc": {"page": "407B", "column": 1, "line": 4},
    "qr-bhq-comment": [author.para(_BHQ_COMMENT_3612)],
    "qr-noted-by": "nBHQ-xBHL-nDM-nWLC",
    "qr-aleppo-page-url": "https://www.mgketer.org/mikra/29/36/1/mg/106",
    "qr-aleppo-img": "Aleppo-3612.png",
    "qr-cam1753-page-url": f"{CAM1753_PAGE_URL_BASE}/n87/mode/1up",
    "qr-cam1753-img": "Cam1753-3612.png",
    "qr-uxlc-needs-fix": "UXLC has kaf (as it should) but should note the divergence from consensus",
}
