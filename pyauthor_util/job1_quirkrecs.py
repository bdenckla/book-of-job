# XXX study WLC notes in Job
# XXX study UXLC changes in Job
# XXX review quirks-Daat-Miqra.txt
# XXX review quirks-BHQ.txt

from pyauthor_util import author
from py import my_html
from pyauthor_util.qr_0709 import RECORD_0709
from pyauthor_util.qr_0721 import RECORD_0721
from pyauthor_util.qr_0906 import RECORD_0906
from pyauthor_util.qr_0935 import RECORD_0935
from pyauthor_util.qr_1001 import RECORD_1001
from pyauthor_util.qr_1015 import RECORD_1015
from pyauthor_util.qr_1103 import RECORD_1103
from pyauthor_util.qr_1106 import RECORD_1106
from pyauthor_util.qr_1107 import RECORD_1107
from pyauthor_util.qr_1113 import RECORD_1113
from pyauthor_util.qr_1508 import RECORD_1508
from pyauthor_util.qr_1613 import RECORD_1613
from pyauthor_util.qr_1620 import RECORD_1620
from pyauthor_util.qr_1704 import RECORD_1704
from pyauthor_util.qr_1706 import RECORD_1706
from pyauthor_util.qr_1711 import RECORD_1711
from pyauthor_util.qr_1809 import RECORD_1809
from pyauthor_util.qr_2230_B import RECORD_2230_B
from pyauthor_util.qr_2416 import RECORD_2416
from pyauthor_util.qr_2614 import RECORD_2614
from pyauthor_util.qr_3133 import RECORD_3133
from pyauthor_util.qr_3312 import RECORD_3312
from pyauthor_util.qr_3419 import RECORD_3419
from pyauthor_util.qr_3706 import RECORD_3706
from pyauthor_util.qr_3812_B import RECORD_3812_B
from pyauthor_util.qr_3817 import RECORD_3817
from pyauthor_util.qr_3906 import RECORD_3906
from pyauthor_util.qr_4010 import RECORD_4010
from pyauthor_util.qr_4026 import RECORD_4026
from pyauthor_util.qr_4213 import RECORD_4213
from pyauthor_util.job1_common import (
    CAM1753_PAGE_URL_BASE,
    correctly_ignores,
    BHQ_COMMENT_TBHQ_NELSWHERE,
    BHQ_COMMENT_CMN_0409_AND_SIMILAR,
)
from pyauthor_util.qr_0121 import RECORD_0121
from pyauthor_util.qr_0629 import RECORD_0629
from pyauthor_util.qr_0701 import RECORD_0701
from pyauthor_util.qr_0801 import RECORD_0801
from pyauthor_util.qr_0807 import RECORD_0807
from pyauthor_util.qr_1216 import RECORD_1216
from pyauthor_util.qr_1409 import RECORD_1409
from pyauthor_util.qr_1534 import RECORD_1534
from pyauthor_util.qr_1905 import RECORD_1905
from pyauthor_util.qr_1916 import RECORD_1916
from pyauthor_util.qr_2230_A import RECORD_2230_A
from pyauthor_util.qr_2826 import RECORD_2826
from pyauthor_util.qr_3330 import RECORD_3330
from pyauthor_util.qr_3812_A import RECORD_3812_A
BHQ_COMMENT_0409 = [
    *BHQ_COMMENT_CMN_0409_AND_SIMILAR,
    ' Six of these seven, including this one, are noted in the entry for 4:9 in the $BHQ',
    ' section “Commentary on the Critical Apparatus.”',
    " Only this one and 11:6",
    " are noted in the bottom-of-page critical apparatus as well.",
    " The one in 4:17 is not noted in any way in $BHQ.",
]

_RECORD_0409 = {
    "bhla-i": 2,
    "cv": "4:9",
    "lc": "אֱל֣וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱל֣וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "398A", "column": 1, "line": -2},
    "lc-img": "0409.png",
    "bhq-comment": BHQ_COMMENT_0409,
    "noted-by": "nBHQ-nBHL-nDM",
}
_BHQ_COMMENT_0417 = [
    *BHQ_COMMENT_CMN_0409_AND_SIMILAR,
    " This is the only one of these seven not noted in any way in $BHQ.",
    " For more details, see my entry on 4:9.",
]
_RECORD_0417 = {
    "bhla-i": 3,
    "cv": "4:17",
    "lc": "מֵאֱל֣וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "מֵאֱל֣וֹהַּ",
    "comment": "",
    "highlight": 5,
    "lc-loc": {"page": "398A", "column": 2, "line": 10},
    "lc-img": "0417.png",
    "bhq-comment": _BHQ_COMMENT_0417,
    "noted-by": "tBHQ-nBHL-nDM",
}
_BHQ_COMMENT_0914_AND_0930 = [
    "$BHQ silently supplies the סילוק that is the consensus expectation,",
    " despite little or no evidence for it in μL.",
]
_RECORD_0914 = {
    "bhla-i": 9,
    "cv": "9:14",
    "lc-q": "(?)",
    "lc": "עִמּוֹ׃",
    "what-is-weird": "סילוק may be missing",
    "mam": "עִמּֽוֹ׃",
    "comment": "",
    "highlight": 2,
    "lc-loc": {"page": "399B", "column": 1, "line": 22, "including-blank-lines": 1},
    "lc-img": "0914.png",
    "bhq-comment": _BHQ_COMMENT_0914_AND_0930,
    "noted-by": "xBHQ-nBHL-xDM",
}
_RECORD_0930 = {
    "bhla-i": 10,
    "cv": "9:30",
    "lc-q": "(?)",
    "lc": "כַּפָּי׃",
    "what-is-weird": "סילוק may be missing",
    "mam": "כַּפָּֽי׃",
    "comment": "",
    "highlight": 2,
    "lc-loc": {"page": "399B", "column": 2, "line": 15},
    "lc-img": "0930.png",
    "bhq-comment": _BHQ_COMMENT_0914_AND_0930,
    "noted-by": "xBHQ-nBHL-xDM",
}
_BHQ_COMMENT_1203 = [
    "$BHQ silently supplies the מקף that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
_RECORD_1203 = {
    "bhla-i": 17,
    "cv": "12:3",
    "lc": "וְאֶת",
    "what-is-weird": "מקף is missing",
    "mam": "וְאֶת־",
    "comment": "",
    "highlight-mam": 4,
    "lc-loc": {"page": "400A", "column": 2, "line": -1},
    "lc-img": "1203.png",
    "bhq-comment": _BHQ_COMMENT_1203,
    "noted-by": "xBHQ-nBHL-nDM",
}
_COMMENT_1604 = [
    "Though it is not relevant to the point at hand, which is the presence of a מקף,",
    " note that in μL, the shape we take to be מחפך is touching the bottom of the ל (lamed).",
]
_BHQ_COMMENT_1604 = [
    "Though it is not relevant to the point at hand,",
    " note that $BHQ continues to fail to distinguish",
    " between גלגל and אתנח הפוך.",
]
_RECORD_1604 = {
    "bhla-i": 21,
    "cv": "16:4",
    "lc": "ל֤וּ־",
    "what-is-weird": "מקף is present",
    "mam": "ל֤וּ",
    "comment": _COMMENT_1604,
    "highlight-lc": 3,
    "lc-loc": {"page": "401B", "column": 2, "line": 3},
    "lc-img": "1604.png",
    "bhq-comment": _BHQ_COMMENT_1604,
    "noted-by": "tBHQ-nBHL-xDM",
}
_BHQ_COMMENT_1804_A = [
    "$BHQ silently ignores the possible שווא part of the possible חטף פתח.",
    " It also silently ignores the possible intepretation of that ink as a געיה.",
    " I.e. other than the prepositive דחי accent,",
    " $BHQ supplies only the (full) פתח that is the consensus expectation here.",
    " $BHQ does so silently, i.e. with no note about the pointing of ה.",
]
_RECORD_1804_CMN_AB = {
    "bhla-i": 24,
    "cv": "18:4",
    "lc": "הֲ֭לְמַּעַנְךָ",
    "mam": "הַֽ֭לְמַעַנְךָ",
    "bhq": "הַ֭לְמַּעַנְךָ",
    "lc-loc": {"page": "402A", "column": 1, "line": -4},
    "lc-img": "1804.png",
}
_RECORD_1804_A = {
    **_RECORD_1804_CMN_AB,
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "n_of_m_for_this_word": (1, 2),  # this is record 1 of 2 for this word
    "what-is-weird": "פתח on ה is חטף.",
    "comment": [
        "The quirk that מ has דגש is discussed in a separate entry of mine.",
        " The געיה difference is not important to us here.",
    ],
    "highlight": 1,
    "bhq-comment": _BHQ_COMMENT_1804_A,
    "noted-by": "xBHQ-nBHL-nDM",
}
_BHQ_COMMENT_1804_B = [
    "$BHQ notes that the דגש on the מ in μL disagrees with μA and μY.",
    " $BHQ misses the געיה in μA.",
    " This געיה is irrelevant to $BHQ’s point here, which is about the דגש.",
    " Still, it would have been nice if $BHQ had transcribed the געיה.",
]
_RECORD_1804_B = {
    **_RECORD_1804_A,
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "n_of_m_for_this_word": (2, 2),  # this is record 2 of 2 for this word
    "what-is-weird": "מ has דגש.",
    "comment": [
        "The quirk that the פתח on ה is חטף is discussed in a separate entry of mine.",
        " The געיה difference is not important to us here.",
    ],
    "highlight": 3,
    "bhq-comment": _BHQ_COMMENT_1804_B,
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/18/1/mg/106",
    "aleppo-img": "Aleppo-1804.png",
    "noted-by": "nBHQ-nBHL-nDM",
}
_BHQ_COMMENT_1806 = [
    "$BHQ positions the mark ambiguously.",
    " The mark is a little to the right of center.",
    " So it is not centered, as one would expect a טרחא to be,",
    " but neither is it as far to the right as דחי normally is in $BHQ.",
    # XXX add BHQ image
]
_RECORD_1806 = {
    "bhla-i": 25,
    "cv": "18:6",
    "lc": "א֖וֹר",
    "what-is-weird": "דחי is placed like a טרחא",
    "mam": "א֭וֹר",
    "comment": "",
    "highlight": 1,
    "lc-loc": {"page": "402A", "column": 1, "line": -2},
    "lc-img": "1806.png",
    "bhq-comment": _BHQ_COMMENT_1806,
    "noted-by": "tBHQ-nBHL-xDM",
}
_COMMENT_2125 = [
    "The dot is suspiciously brown rather than black,",
    " making me wonder whether the ו was pointed at all.",
]
_BHQ_COMMENT_2125 = [
    "$BHQ silently supplies the שווא that is the consensus expectation,",
    " despite little or no evidence for it in μL.",
]
_RECORD_2125 = {
    "bhla-i": 28,
    "cv": "21:25",
    "lc": "וִלֹֽא־",
    "what-is-weird": "חיריק not שווא",
    "mam": "וְלֹֽא־",
    "comment": _COMMENT_2125,
    "highlight": 1,
    "lc-loc": {"page": "403A", "column": 2, "line": 13},
    "lc-img": "2125.png",
    "bhq-comment": _BHQ_COMMENT_2125,
    "noted-by": "xBHQ-nBHL-xDM",
}
_COMMENT_2221_A = [
    "A dot under the מ of עמו is fairly clear.",
    " It is (charitably) not transcribed by $BHL_A,",
    " presumably based on the consensus expectation that it is absent.",
]
_COMMENT_2221_B = [
    "Perhaps some super-faint remains of an אתנח under ל can be seen.",
    " The top dot of the שווא (under the ש) is super-faint.",
    " See my entry for 22:21 עמי for μA and μY images.",
]
_BHQ_COMMENT_2221_A = [
    "$BHQ fails to note that the אתנח it transcribes on עמו",
    " disagrees with μA and μY.",
]
_BHQ_COMMENT_2221_B = [
    "$BHQ (charitably) transcribes the top dot of the שווא",
    " using, as one often has to, faint evidence bolstered by consensus expectations.",
    " $BHQ notes (as does $BHS) that whereas the ל of ושלם is unpointed in μL,",
    " that ל has קמץ and אתנח in μA and μY.",
]
_CAM1753_IMG_INTRO_2221 = [
    "note that instead of a masorah circle, μY uses a pair of above-dots",
    " as a “callout” for a Masorah parva note;",
    " hence the pair of above-dots above ל in ושלם.",
]
_RECORD_2221_CMN_AB = {
    "cv": "22:21",
    "lc-loc": {"page": "403B", "column": 1, "line": -6},
    "lc-img": "2221.png",
}
_RECORD_2221_A = {
    **_RECORD_2221_CMN_AB,
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
_RECORD_2221_B = {
    **_RECORD_2221_CMN_AB,
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "lc": "וּשְׁלם",
    "what-is-weird": "ל lacks קמץ־אתנח",
    "mam": "וּשְׁלָ֑ם",
    "comment": _COMMENT_2221_B,
    "highlight": 3,
    "lc-loc": {"page": "403B", "column": 1, "line": -6},
    "lc-img": "2221.png",
    "bhq-comment": _BHQ_COMMENT_2221_B,
    "noted-by": "nBHQ-xBHL-xDM-nWLC",
}
_BHQ_COMMENT_2228 = [
    "$BHQ places the mark a little left of center.",
    # XXX add BHQ image
    " Though this placement is odd,",
    " this makes it clear that a טרחא was intended by $BHQ rather than a דחי.",
    " Thus $BHQ somewhat-accurately transcribes the quirk in μL,",
    " but should have noted the quirk.",
]
_RECORD_2228 = {
    "bhla-i": 30,
    "cv": "22:28",
    "lc": "א֖וֹמֶר",
    "what-is-weird": "דחי is placed like a טרחא",
    "mam": "אֹ֭מֶר",
    "comment": "The מלא/חסר spelling difference is not important to us here.",
    "highlight": 1,
    "lc-loc": {"page": "403B", "column": 2, "line": 2},
    "lc-img": "2228.png",
    "bhq-comment": _BHQ_COMMENT_2228,
    "noted-by": "tBHQ-nBHL-xDM",
}
_COMMENT_2421 = [
    "Perhaps there is some super-faint evidence of a third dot that would make a סגול,",
    " but this could be just wishful thinking.",
    " Note that there is a third dot above the two clearer dots,",
    " but I take that to be part of the ע that did not flake off like its neighboring ink did.",
]
_BHQ_COMMENT_2421 = [
    "$BHQ silently supplies the סגול that is the consensus expectation.",
    " I.e. despite little or no evidence for it in μL,",
    " $BHQ silently infers a third dot centered below the two clearer dots.",
]
_RECORD_2421 = {
    "bhla-i": 31,
    "cv": "24:21",
    "lc-q": "(?)",
    "lc": "רֹעֵ֣ה",
    "what-is-weird": "maybe צירה not סגול",
    "mam": "רֹעֶ֣ה",
    "comment": _COMMENT_2421,
    "highlight": 2,
    "lc-loc": {"page": "404A", "column": 2, "line": -2},
    "lc-img": "2421.png",
    "bhq-comment": _BHQ_COMMENT_2421,
    "noted-by": "xBHQ-nBHL-nDM",
}
_COMMENT_2702 = [
    "Perhaps there is some super-faint evidence of a מקף that was ignored during re-inking.",
    " By the way, the evidence for the דחי on the א of the next word is super-faint.",
]
_BHQ_COMMENT_2702 = [
    "$BHQ silently supplies the מקף that is the consensus expectation,",
    " despite little or no evidence for it in μL.",
]
_RECORD_2702 = {
    "bhla-i": 32,
    "cv": "27:2",
    "lc": "חַי",
    "what-is-weird": "מקף is missing",
    "mam": "חַי־",
    "comment": _COMMENT_2702,
    "highlight-mam": 3,
    "lc-loc": {"page": "404A", "column": 2, "line": -2},
    "lc-img": "2702.png",
    "bhq-comment": _BHQ_COMMENT_2702,
    "noted-by": "xBHQ-nBHL-nDM",
}
_BHQ_COMMENT_2808_AND_2911 = [
    "$BHQ silently supplies the חיריק that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
_RECORD_2808 = {
    "bhla-i": 33,
    "cv": "28:8",
    "lc": "הִדְריכֻ֥הוּ",
    "what-is-weird": "ר lacks חיריק",
    "mam": "הִדְרִיכ֥וּהוּ",
    "comment": "The מלא/חסר spelling difference is not important to us here.",
    "highlight": 3,
    "lc-loc": {"page": "404B", "column": 2, "line": 5},
    "lc-img": "2808.png",
    "bhq-comment": _BHQ_COMMENT_2808_AND_2911,
    "noted-by": "xBHQ-nBHL-xDM",
}
_RECORD_2911 = {
    "bhla-i": 34,
    "cv": "29:11",
    "lc": "וְעַ֥ין",
    "what-is-weird": "$yod (י) lacks חיריק",
    "mam": "וְעַ֥יִן",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "405A", "column": 1, "line": -12},
    "lc-img": "2911.png",
    "bhq-comment": _BHQ_COMMENT_2808_AND_2911,
    "noted-by": "xBHQ-nBHL-xDM",
}
_COMMENT_2919 = [
    "Probably the ascender of the ל on the line below",
    f" “forced” the סילוק to be early.",
]
_RECORD_2919 = {
    "bhla-i": 35,
    "cv": "29:19",
    "lc": "בִּקְצִירֽ͏ִי׃",
    "what-is-weird": "סילוק precedes חיריק",
    "mam": "בִּקְצִירִֽי׃",
    "comment": _COMMENT_2919,
    "highlight": 5,
    "lc-loc": {"page": "405A", "column": 1, "line": -4},
    "lc-img": "2919.png",
    "bhq-comment": BHQ_COMMENT_TBHQ_NELSWHERE,
    "noted-by": "tBHQ-nBHL-xDM",
}
_BHQ_COMMENT_CMN_3105_3206 = [
    "$BHQ silently supplies the marks in the vowel-then-accent order that is",
    " the consensus expectation, in clear contradiction of μL here.",
]
_BHQ_COMMENT_3105 = [
    *_BHQ_COMMENT_CMN_3105_3206,
    " 32:6 is similar.",
    " In my opinion $BHQ shows itself to be out of date by continuing to aspire,",
    " as $BHS did,",
    " to reflect all such ordering quirks.",
    " I think the modern consensus is that these orderings are as meaningless as",
    " the variable length of ascenders on ל.",
    " Nonetheless, since $BHQ still aspires to get these orderings right,",
    " it is fair for me to point out when it fails to do so.",
]
_RECORD_3105 = {
    "bhla-i": 36,
    "cv": "31:5",
    "lc": "רַגְלֽ͏ִי׃",
    "what-is-weird": "סילוק precedes חיריק",
    "mam": "רַגְלִֽי׃",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "405B", "column": 1, "line": -9, "including-blank-lines": 1},
    "lc-img": "3105.png",
    "bhq-comment": _BHQ_COMMENT_3105,
    "noted-by": "xBHQ-nBHL-xDM",
}
_BHQ_COMMENT_3107 = [
    "$BHQ reflects neither μL nor the consensus expectation here.",
    " It reflects μL except it places the סילוק under the א.",
    " This not only contradicts μL,",
    " but also makes no sense given the רפה on the א.",
    " One might argue that this רפה should have been shown,",
    " despite the general policy of $BHQ to ignore רפה marks in μL.",
    " Regardless of whether the רפה should have been shown,",
    " its presence in μL should have excluded the possibility of",
    " a סילוק under its letter (א)!",
    " $BHQ notes that here μL disagrees with μA and μY.",
    " But $BHQ gives the מ in μA and μY a מרכא rather than a סילוק,",
    " which seems more likely a typo than a deliberate choice.",
]
_RECORD_3107 = {
    "bhla-i": 37,
    "cv": "31:7",
    "lc": "מֻאֿוּֽם׃",
    "what-is-weird": "קבוץ and סילוק not סילוק and ∅",
    "mam": "מֽאֿוּם׃",
    "comment": "",
    "highlight": [1, 3],
    "lc-loc": {"page": "405B", "column": 1, "line": -6, "including-blank-lines": 1},
    "lc-img": "3107.png",
    "bhq-comment": _BHQ_COMMENT_3107,
    "bhq": "מֻאֽוּם׃",
    "noted-by": "xBHQ-nBHL-nDM-nWLC",
    # Above we consider this xBHQ because:
    #    Though it attempts to transcribe the quirk, it does so inaccurately.
    #    Though it notes the quirk, it does so inaccurately.
}
_BHQ_COMMENT_3206 = [
    *_BHQ_COMMENT_CMN_3105_3206,
    "31:5 is similar and discusses the matter at greater length.",
]
_RECORD_3206 = {
    "bhla-i": 39,
    "cv": "32:6",
    "lc": "יְשִׁישׁ֑‍ִים",
    "what-is-weird": "אתנח precedes חיריק",
    "mam": "יְשִׁישִׁ֑ים",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "406A", "column": 1, "line": -6},
    "lc-img": "3206.png",
    "bhq-comment": _BHQ_COMMENT_3206,
    "noted-by": "xBHQ-nBHL-xDM",
}
_BHQ_COMMENT_3612 = [
    "Here $BHQ has a typo:",
    [" it has ", author.hbo("בִּבְלִ־"), " rather than ", author.hbo("בִּבְלִי־")],
    " in the word it reports for μA and μY.",
    " I.e. it is missing a final $yod (י) before the מקף.",
    " The same typo appears in the $BHQ section “Commentary on the Critical Apparatus.”",
    " In addition to the typo, for some reason $BHQ reports this word as being the קרי",
    [" of μY, i.e. M", my_html.sup("Y(qere)")],
    [" rather than just M", my_html.sup("Y"), "."],
    " I see no “Masora dot pair”",
    " (μY’s equivalent of a masorah circle)",
    " on this word in μY.",
    " Nor do I see any קרי note in the margin.",
]
_RECORD_3612 = {
    "cv": "36:12",
    "lc": "כִּבְלִי־",
    "what-is-weird": "כ not ב",
    "mam": "בִּבְלִי־",
    "comment": [
        "Although my focus is pointing rather than spelling,",
        " I am interested in a spelling difference like this,",
        " since it is not just a חסר vs מלא difference.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "407B", "column": 1, "line": 4},
    "lc-img": "3612.png",
    "bhq-comment": _BHQ_COMMENT_3612,
    "noted-by": "nBHQ-xBHL-nDM-nWLC",
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/36/1/mg/106",
    "aleppo-img": "Aleppo-3612.png",
    "cam1753-page-url": f"{CAM1753_PAGE_URL_BASE}/n87/mode/1up",
    "cam1753-img": "Cam1753-3612.png",
    "uxlc-needs-fix": "UXLC has kaf (as it should) but should note the divergence from consensus",
}
_COMMENT_3629 = [
    "The color image strongly suggests that the mark in question is not ink.",
    " A געיה right next to סילוק like that would be extraordinary, by the way,",
    " though no appeal to expectations is needed to dismiss this possible געיה.",
]
_RECORD_3629 = {
    "bhla-i": 43,
    "cv": "36:29",
    "lc": "סֻכָּֽתֽוֹ׃",
    "what-is-weird": "כ has געיה",
    "mam": "סֻכָּתֽוֹ׃",
    "comment": _COMMENT_3629,
    "highlight": 2,
    "lc-loc": {"page": "407B", "column": 1, "line": -5},
    "lc-img": "3629.png",
    "bhq-comment": correctly_ignores("געיה", "36:29", "large"),
    "noted-by": "tBHQ-nBHL-xDM",
}
_COMMENT_3902 = [
    "The mark in question is very heavy,",
    " having a stroke width more typical of a letter-stroke than of a niqqud-stroke.",
    " Its clarity suggests it is part of the re-inking.",
    " Indeed perhaps it is only part of the re-inking,",
    " i.e. perhaps it reflects no mark (or only a much smaller mark) in the original.",
    " The mark in question may be two marks,",
    " a רביע (expected) overlaid with a גרש (unexpected).",
    " Or, it may be only a single mark whose lower end is, for some reason, a blob.",
]
_RECORD_3902 = {
    "bhla-i": 46,
    "cv": "39:2",
    "lc": "וְ֝יָדַעְתָּ֜",
    "what-is-weird": "גרש not רביע",
    "mam": "וְ֝יָדַעְתָּ֗",
    "comment": _COMMENT_3902,
    "highlight": 5,
    "lc-loc": {"page": "408A", "column": 2, "line": -3},
    "lc-img": "3902.png",
    "bhq-comment": "$BHQ silently supplies the רביע that is the consensus expectation.",
    "noted-by": "xBHQ-nBHL-xDM",
    # Perhaps I should have been charitable to BHQ and said tBHQ instead of xBHQ,
    # since BHQ’s transcription of רביע is somewhat reasonable if it were accompanied by a note.
    # But it is not accompanied by a note, and without a note, BHQ needs to make weird things in μL
    # look weird. So רביע is not the right transcription for a diplomatic edition having no note
    # in this location.
}
_COMMENT_3913 = [
    "A more charitable interpretation of the image is that the רביע is present",
    " but is merged with the masorah circle.",
    " (It is fairly clear that a masorah circle is present.)",
    " Note that the vertical line above the ר is a סילוק from the line above.",
]
_RECORD_3913 = {
    "bhla-i": 48,
    "cv": "39:13",
    "lc-q": "(?)",
    "lc": "אֶ֝בְרָה",
    "what-is-weird": "רביע מגרש may lack רביע",
    "mam": "אֶ֝בְרָ֗ה",
    "comment": _COMMENT_3913,
    "highlight": 3,
    "lc-loc": {"page": "408B", "column": 1, "line": 11},
    "lc-img": "3913.png",
    "bhq-comment": [
        "$BHQ seems to split the mark(s) in question",
        " into a רביע on ר and a masorah circle on ב.",
        " This is a reasonable (though somewhat charitable) interpretation of μL,",
        " but as is so often the case, $BHQ should have noted this quirk.",
    ],
    "noted-by": "tBHQ-nBHL-xDM",
}
_RECORD_3920 = {
    "bhla-i": 49,
    "cv": "39:20",
    "lc": "הְֽ֭תַרְעִישֶׁנּוּ",
    "what-is-weird": "simple שווא not חטף פתח",
    "mam": "הֲֽ֭תַרְעִישֶׁנּוּ",
    "comment": "The situation with המימיך in 38:12 is similar.",
    "highlight": 1,
    "lc-loc": {"page": "408B", "column": 1, "line": -10},
    "lc-img": "3920.png",
    "bhq-comment": BHQ_COMMENT_TBHQ_NELSWHERE,
    "noted-by": "tBHQ-nBHL-nDM",
}
_BHQ_COMMENT_4125 = [
    "$BHQ silently supplies the סילוק that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
_RECORD_4125 = {
    "bhla-i": 52,
    "cv": "41:25",
    "lc": "לִבְלִי־חָת׃",
    "what-is-weird": "סילוק missing",
    "mam": "לִבְלִי־חָֽת׃",
    "comment": "",
    "highlight": 5,
    "lc-loc": {"page": "409A", "column": 2, "line": 14},
    "lc-img": "4125.png",
    "bhq-comment": _BHQ_COMMENT_4125,
    "noted-by": "xBHQ-nBHL-xDM",
}
QUIRKRECS = [
    RECORD_0121,
    _RECORD_0409,
    _RECORD_0417,
    RECORD_0629,
    RECORD_0701,
    RECORD_0709,
    RECORD_0721,
    RECORD_0801,
    RECORD_0807,
    RECORD_0906,
    _RECORD_0914,
    _RECORD_0930,
    RECORD_0935,
    RECORD_1001,
    RECORD_1015,
    RECORD_1103,
    RECORD_1106,
    RECORD_1107,
    RECORD_1113,
    _RECORD_1203,
    RECORD_1216,
    RECORD_1409,
    RECORD_1508,
    RECORD_1534,
    _RECORD_1604,
    RECORD_1613,
    RECORD_1620,
    RECORD_1704,
    RECORD_1706,
    RECORD_1711,
    _RECORD_1804_A,
    _RECORD_1804_B,
    _RECORD_1806,
    RECORD_1809,
    RECORD_1905,
    RECORD_1916,
    _RECORD_2125,
    _RECORD_2221_A,
    _RECORD_2221_B,
    _RECORD_2228,
    RECORD_2230_A,
    RECORD_2230_B,
    RECORD_2416,
    _RECORD_2421,
    RECORD_2614,
    _RECORD_2702,
    _RECORD_2808,
    RECORD_2826,
    _RECORD_2911,
    _RECORD_2919,
    _RECORD_3105,
    _RECORD_3107,
    RECORD_3133,
    _RECORD_3206,
    RECORD_3312,
    RECORD_3330,
    RECORD_3419,
    _RECORD_3612,
    _RECORD_3629,
    RECORD_3706,
    RECORD_3812_A,
    RECORD_3812_B,
    RECORD_3817,
    _RECORD_3902,
    RECORD_3906,
    _RECORD_3913,
    _RECORD_3920,
    RECORD_4010,
    RECORD_4026,
    _RECORD_4125,
    RECORD_4213,
]
