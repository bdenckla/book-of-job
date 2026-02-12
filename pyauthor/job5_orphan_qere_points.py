"""Exports gen_html_file"""

from py import my_html
from py_uxlc_loc import my_tanakh_book_names as tbn
from pyauthor_util import author
from pyauthor_util.common_titles_etc import D5_TITLE, D5_H1_CONTENTS, D5_FNAME

_MWD = "https://bdenckla.github.io/MAM-with-doc"
_UXLC = "https://tanach.us/Tanach.xml"


def _links_to_u_and_m(bkid, ch, vr):
    cv = f"{ch}:{vr}"
    cn_v_vn = f"c{ch}v{vr}"
    osdf = tbn.ordered_short_dash_full(bkid)
    u = my_html.anchor_h("U", f"{_UXLC}?{bkid}{cv}")
    m = my_html.anchor_h("M", f"{_MWD}/{osdf}.html#{cn_v_vn}")
    return u, ", ", m


def gen_html_file(tdm_ch):
    author.assert_stem_eq(__file__, D5_FNAME)
    cbody = _make_cbody()
    author.help_gen_html_file(tdm_ch, D5_FNAME, D5_TITLE, cbody)


def _make_cbody():
    return [
        author.heading_level_1(D5_H1_CONTENTS),
        author.para(_INTRO),
        #
        author.heading_level_2("2 Kings 4:7"),
        author.para(_KINGS_INTRO),
        author.para(_KINGS_DISCUSSION),
        _img("Aleppo-2Kings-c4v7.png"),
        _img("2Kings-c4v7.png"),
        #
        author.heading_level_2("Lamentations 4:16"),
        author.para(_LAMENTATIONS_INTRO),
        author.para(_LAMENTATIONS_DISCUSSION),
        _img("Sassoon-1053-Lamentations-c4v16.png"),
        #
        author.heading_level_2("2 Samuel 18:20"),
        author.para(_SAMUEL_INTRO),
        author.para(_SAMUEL_DISCUSSION),
        _img("2-Samuel-c18v20.jpg"),
    ]


def _img(img):
    return author.para_for_img(img, "maxwidth50pc")


_INTRO = [
    "In Job 38:12, the Jerusalem Crown edition puts a פתח on no letter.",
    " The פתח floats before the ש of %שחר.",
    #
    " Although this is not the way μA or μL presents this כתיב/קרי,",
    " there is manuscript precedent for such a floating presentation.",
    " This page presents some examples of that precedent.",
]

_KINGS_INTRO = [
    ["In 2 Kings 4:7 (", *_links_to_u_and_m(tbn.BK_SND_KGS, 4, 7), "),"],
    [" there is a קרי of ", author.hbo("וּבָנַ֔יִךְ")],
    [" corresponding to a כתיב of ", author.hbo("בניכי"), "."],
]
_KINGS_DISCUSSION = [
    "This is hard to show in the “pointed כתיב”",
    " style of קרי/כתיב presentation favored by the manuscripts.",
    " In such a style, the three diagonal קובוץ dots must float before the ב.",
    " The dots are “orphans”: they belong to no letter of the כתיב word.",
    " The first image below is from μA; the second is from μL.",
    " The קובוץ dots are faint in μL, almost invisible.",
    " (They are under the ת of the previous word.)",
]

_LAMENTATIONS_INTRO = [
    ["In Lamentations 4:16 (", *_links_to_u_and_m(tbn.BK_LAMENT, 4, 16), "),"],
    [" there is a קרי of ", author.hbo("וּזְקֵנִ֖ים")],
    [" corresponding to a כתיב of ", author.hbo("זקנים"), "."],
]
_LAMENTATIONS_DISCUSSION = [
    "As in 2 Kings 4:7,",
    " the קובוץ dots must float before the first letter of the word,",
    " which in this case is ז.",
    " Here is the way this word looks in Sassoon 1053:",
]

_SAMUEL_INTRO = [
    ["2 Samuel 18:20 (", *_links_to_u_and_m(tbn.BK_SND_SAM, 18, 20), ")"],
    [" is a קרי ולא כתיב: the word ", author.hbo("כֵּ֥ן")],
    " is read but not written.",
]
_SAMUEL_DISCUSSION = [
    "So there are no letters %כן in the body text on which to put the קרי pointing.",
    #
    " This represents a more extreme case of orphan קרי points than the previous two examples,"
    " since there is no word to which the orphan points can “snuggle up” to.",
    #
    " In other words, the vowel and accent marks of the קרי word, כן,",
    " float in the space between the surrounding כתיב words.",
    #
    " Or rather, the marks would float in that space if enough space had been left for them.",
    #
    " As it is, they somewhat awkwardly and confusingly reside beneath the ל.",
]
