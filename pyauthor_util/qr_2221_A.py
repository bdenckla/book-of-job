from pyauthor_util.job1_common import RECORD_2221_CMN_AB, CAM1753_PAGE_URL_BASE


_COMMENT_2221_A = [
    "A dot under the מ of עמו is fairly clear.",
    " It is (charitably) not transcribed by $BHL_A,",
    " presumably based on the consensus expectation that it is absent.",
]
_BHQ_COMMENT_2221_A = [
    "$BHQ fails to note that the אתנח it transcribes on עמו",
    " disagrees with μA and μY.",
]
_CAM1753_IMG_INTRO_2221 = [
    "note that instead of a masorah circle, μY uses a pair of above-dots",
    " as a “callout” for a Masorah parva note;",
    " hence the pair of above-dots above ל in ושלם.",
]
RECORD_2221_A = {
    **RECORD_2221_CMN_AB,
    "bhla-i": 29,
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "lc-q": "(?)",
    "lc": "עִמּ֑וֹ",
    "what-is-weird": "אתנח not מונח",
    "mam": "עִמּ֣וֹ",
    "comment": _COMMENT_2221_A,
    "highlight": 2,
    "bhq-comment": _BHQ_COMMENT_2221_A,
    "noted-by": "tBHQ-nBHL-xDM-nWLC",
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/22/1/mg/106",
    "aleppo-img": "Aleppo-2221.png",
    "cam1753-page-url": f"{CAM1753_PAGE_URL_BASE}/n83/mode/1up",
    "cam1753-img": "Cam1753-2221.png",
    "cam1753-img-intro": _CAM1753_IMG_INTRO_2221,
}
