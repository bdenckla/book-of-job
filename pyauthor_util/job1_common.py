from pyauthor_util import author
from pyauthor_util.job1_ov_and_de import make_example_row
from py import my_html

CAM1753_PAGE_URL_BASE = (
    "https://archive.org/details/ketuvim-cambridge-ms-add-1753-images/page"
)
_SEE_3419 = [" See my entry on נכר in 34:19 for further discusion."]
_CORR_IG_VARIANT_3419 = [
    " Since $BHQ does not note any uncertainty in its transcription here,",
    " it is hard to distinguish whether $BHQ has ignored the mark in question",
    " on purpose or by accident.",
    " More broadly, $BHQ Job never notes",
    " any uncertainty in its transcription of μL.",
    " This may mislead many readers.",
    " Despite the fact that high-resolution, color images of μL are now widely available,",
    " many readers will not engage with those images enough to understand how often",
    " there is great uncertainty in transcribing μL.",
    " And, even if the reader understands that such uncertainty exists in general,",
    " $BHQ should, in my opinion, indicate to the reader the specific places",
    " where its transcription is particularly uncertain.",
]
_CORR_IG_VARIANT = {
    "34:19": _CORR_IG_VARIANT_3419,
    "36:29": _SEE_3419,
    "17:4": _SEE_3419,
}


def suffix(contents):
    new_cont = "\N{EN DASH}\N{HAIR SPACE}" + contents
    return my_html.span(new_cont, {"dir": "rtl"})


def correctly_ignores(what, cv, adjective=""):
    adj = f" {adjective}" if adjective else ""
    variant = _CORR_IG_VARIANT[cv]
    out_parts = [
        f"$BHQ has no {what} here.",
        f" I happen to think that this is the best transcription of μL here,",
        f" but I don’t know whether $BHQ arrived at this transcription",
        f" on purpose or by accident.",
        f" Did the editors of $BHQ consider, but ultimately decide against,",
        f" the faint possible{adj} {what}?",
        f" Or did they simply ignore μL entirely, supplying the consensus pointing,",
        f" which has no {what}?",
        *variant,
    ]
    return "".join(out_parts)


BHQ_COMMENT_TBHQ_NELSEWHERE = [
    "$BHQ transcribes μL as shown above,",
    " but $BHQ does not note that this transcription diverges from consensus.",
]
BHQ_COMMENT_XELSEWHERE = [
    "$BHQ notes this, whereas this is not noted in the other editions under consideration."
]
BHQ_COMMENT_XELSEWHERE_DUBIOUS = [
    "$BHQ notes this possibility,",
    " whereas this is not noted in the other editions under consideration.",
    " It could be the editors of those other editions did not catch this,",
    " or it could be that they caught it",
    " but considered to be too slight a possibility to note it.",
]
BHQ_COMMENT_CMN_0409_AND_SIMILAR = [
    "This is one of seven similar cases in Job in μL.",
    " All are correctly transcribed in $BHQ, i.e. transcribed without a מפיק.",
    " Although all are correctly transcribed in $BHQ, they are noted to different extents in $BHQ.",
]
BHQ_COMMENT_LIKE_0409 = [
    *BHQ_COMMENT_CMN_0409_AND_SIMILAR,
    " 4:9 discusses the matter at greater length.",
]


def intro(ov_or_de):
    each = _VARIANTS[ov_or_de]
    return [
        author.para(_each(each)),
        author.table_c(make_example_row()),
        *_where(),
    ]


_VARIANTS = {
    "intro-overview": "Each entry below",
    "intro-details": "The header of each entry below",
    "intro-job2": "Each entry above",
}


def here_is(start, jda=None):
    out = [
        f"{start} some quirks in μL in the book of Job.",
    ]
    if jda is not None:
        jdae = [" For more details, see the ", jda]
        return out + jdae
    return out


def _each(each):
    return [f"{each} takes the following form:"]


_WHERE_LIST = [
    "μL-proposed is a proposed transcription of the Leningrad Codex",
    "consensus is the Masoretic consensus reading (or a good guess of it)",
    "# (hash sign) (number sign) is a link to more details on this quirk",
    "c:v is the chapter and verse of the book of Job",
]


def _where():
    return [
        author.para("Where:"),
        author.unordered_list(_WHERE_LIST),
    ]


BHQ_COMMENT_0914_AND_0930 = [
    "$BHQ silently supplies the סילוק that is the consensus expectation,",
    " despite little or no evidence for it in μL.",
]
RECORD_1804_CMN_AB = {
    "bhla-i": 24,
    "cv": "18:4",
    "lc": "הֲ֭לְמַּעַנְךָ",
    "mam": "הַֽ֭לְמַעַנְךָ",
    "bhq": "הַ֭לְמַּעַנְךָ",
    "lc-loc": {"page": "402A", "column": 1, "line": -4},
}
RECORD_2221_CMN_AB = {
    "cv": "22:21",
    "lc-loc": {"page": "403B", "column": 1, "line": -6},
    "lc-img": "2221.png",
}
BHQ_COMMENT_2808_AND_2911 = [
    "$BHQ silently supplies the חיריק that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
BHQ_COMMENT_CMN_3105_3206 = [
    "$BHQ silently supplies the marks in the vowel-then-accent order that is",
    " the consensus expectation, in clear contradiction of μL here.",
]


def num_range(start, stop):
    return f"{start}\N{THIN SPACE}\N{EN DASH}\N{THIN SPACE}{stop}"
