from pyauthor_util import author
from pyauthor_util.job_common import suffix


_BHQ_COMMENT_2614 = [
    "$BHS does not catch this quirk in μL: it reflects the consensus rather than μL.",
    " $BHQ half-fixes the error in $BHS:",
    " it updates its marginal קרי note to reflect μL rather than the consensus,",
    " but it does not correspondingly update its bottom-of-page critical apparatus note.",
    " This is similar to what happened with the μL קרי of ידעתה השחר in 38:12.",
]

_COMMENT_2614 = [
    "The consensus is that חולם stays חסר in the קרי, i.e. ",
    [suffix("רתו"), " in the כתיב merely expands to "],
    [suffix("רתיו"), " in the קרי."],
    " In contrast to the consensus, in μL, ",
    [suffix("רתו"), " in the כתיב expands all the way to "],
    [suffix("רותיב"), " in the קרי."],
    " The marginal קרי note in μL is a little hard to parse until you realize",
    " that it is “invaded” from above by the descender of a big dotted ק.",
]

RECORD_2614 = {
    "qr-cv": "26:14",
    "qr-lc-proposed": "גְּ֝בוּרוֹתָ֗יו",
    "qr-what-is-weird": "חולם becomes מלא in קרי",
    "qr-consensus": "גְּ֝בוּרֹתָ֗יו",
    "qr-comment": [author.para(_COMMENT_2614)],
    "qr-highlight-lc-proposed": 5,
    "qr-lc-loc": {"page": "404A", "column": 2, "line": -5},
    "qr-aleppo-img": "Aleppo-2614.png",
    "qr-aleppo-page-url": "https://www.mgketer.org/mikra/29/26/14/mg/106",
    "qr-bhq-comment": _BHQ_COMMENT_2614,
    "qr-noted-by": "xBHQ-xBHL-xDM-nWLC",
}
