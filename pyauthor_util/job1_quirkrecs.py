# XXX study WLC notes in Job
# XXX study UXLC changes in Job
# XXX review quirks-Daat-Miqra.txt
# XXX review quirks-BHQ.txt

from pyauthor_util import author
from py import my_html

_CAM1753_PAGE_URL_BASE = (
    "https://archive.org/details/ketuvim-cambridge-ms-add-1753-images/page"
)

_CORR_IG_VARIANT = {
    "34:19": [
        " Since $BHQ does not note any uncertainty in its transcription here,"
        " it is hard to distinguish whether $BHQ has ignored the mark in question",
        " on purpose or by accident.",
        " More broadly, $BHQ Job never notes",
        " any uncertainty in its transcription of μL.",
        " This may mislead many readers."
        " Despite the fact that high-resolution, color images of μL are now widely available,",
        " many readers will not engage with those images enough to understand how often",
        " there is great uncertainty in transcribing μL.",
        " And, even if the reader understands that such uncertainty exists in general,",
        " $BHQ should, in my opinion, indicate to the reader the specific places",
        " where its transcription is particularly uncertain.",
    ],
    "36:29": [" See my entry on 34:19 for further discusion."],
}


def _correctly_ignores(what, cv, adjective=""):
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


_BHQ_COMMENT_XELSEWHERE = [
    "$BHQ noted this, whereas this is not noted in the other editions under consideration."
]
_BHQ_COMMENT_XELSEWHERE = [
    "$BHQ noted this possibility,",
    " whereas this is not noted in the other editions under consideration.",
    " It could be the editors of those other editions did not catch this,",
    " or it could be that they caught it",
    " but considered to be too slight a possibility to note it.",
]
_RECORD_0121 = {
    "bhla-i": 1,
    "cv": "1:21",
    "lc": "שָׁ֔מָה",
    "what-is-weird": "מ lacks דגש",
    "mam": "שָׁ֔מָּה",
    "comment": "",
    "highlight": 2,
    "lc-loc": {"page": "397B", "column": 1, "line": 1},
    "lc-img": "0121.png",
    "bhq-comment": [
        "$BHQ noted this quirk."
        " As usual, it does so by noting that μA and μY agree, and μL disagrees with them.",
        " I.e. μA=μY=x, μL=w, and w≠x."
        " So what we boldly call the consensus, $BHQ merely calls the matching contents of μA and μY.",
    ],
    "noted-by": "BHQ-BHL-DM-WLC",
    "wlc-422-note": "]1",
}
_BHQ_COMMENT_CMN_0409_AND_SIMILAR = [
    "This is one of seven similar cases in Job in μL.",
    " All are correctly transcribed in $BHQ, i.e. transcribed without a מפיק.",
    " Although all are correctly transcribed in $BHQ, they are noted to different extents in $BHQ.",
]
_BHQ_COMMENT_LIKE_0409 = [
    *_BHQ_COMMENT_CMN_0409_AND_SIMILAR,
    " 4:9 discusses the matter at greater length.",
]
_BHQ_COMMENT_0409 = [
    *_BHQ_COMMENT_CMN_0409_AND_SIMILAR,
    " Six of these seven, including this one, are noted in the entry for 4:9 in the $BHQ"
    " section “Commentary on the Critical Apparatus.”",
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
    "bhq-comment": _BHQ_COMMENT_0409,
    "noted-by": "BHQ-BHL-DM",
}
_BHQ_COMMENT_0417 = [
    *_BHQ_COMMENT_CMN_0409_AND_SIMILAR,
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
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_0701 = {
    "bhla-i": 4,
    "cv": "7:1",
    "lc": "וְכִימֵ֖֗י",
    "what-is-weird": "רביע fights טרחא",
    "mam": "וְכִימֵ֖י",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "399A", "column": 1, "line": 4},
    "lc-img": "0701.png",
    "bhq-comment": "$BHQ silently ignores the possible רביע.",
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_0709 = {
    "bhla-i": 5,
    "cv": "7:9",
    "lc": "יַעֲלֽ͏ֶה׃",
    "what-is-weird": "סילוק precedes סגול",
    "mam": "יַעֲלֶֽה׃",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "399A", "column": 1, "line": 14},
    "lc-img": "0709.png",
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_0721 = {
    "bhla-i": 6,
    "cv": "7:21",
    "lc": "וְשִׁ֖חֲרְתַּ֣נִי",
    "what-is-weird": "פתח on ח is חטף",
    "mam": "וְשִׁ֖חַרְתַּ֣נִי",
    "comment": "It doesn’t make sense to have a חטף vowel (aka a חטף שווא) followed by a simple שווא.",
    "highlight": 3,
    "lc-loc": {"page": "399A", "column": 2, "line": 3},
    "lc-img": "0721.png",
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_0801 = {
    "bhla-i": 7,
    "cv": "8:1",
    "lc": "וַיֹאמַֽר׃",
    "what-is-weird": "$yod (י) lacks דגש",
    "mam": "וַיֹּאמַֽר׃",
    "comment": "",
    "highlight": 2,
    "lc-loc": {"page": "399A", "column": 2, "line": 5, "including-blank-lines": 1},
    "lc-img": "0801.png",
    "bhq-comment": "This quirk is noted in $BHQ.",
    "noted-by": "BHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_0807 = {
    "bhla-i": 8,
    "cv": "8:7",
    "lc": "וְּ֝אַחֲרִיתְךָ֗",
    "what-is-weird": "שורוק dot fights שווא",
    "mam": "וְ֝אַחֲרִֽיתְךָ֗",
    "comment": "The געיה difference is not important to us here.",
    "highlight": 1,
    "lc-loc": {"page": "399A", "column": 2, "line": 13, "including-blank-lines": 1},
    "lc-img": "0807.png",
    "bhq-comment": "$BHQ silently ignores the possible שורוק dot.",
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_0906 = {
    "cv": "9:6",
    "lc": "יִתְפַלָּצֽוּן׃",
    "what-is-weird": "פ lacks דגש",
    "mam": "יִתְפַּלָּצֽוּן׃",
    "comment": "There is a bump on the פ that might be a misplaced דגש.",
    "highlight": 3,
    "lc-loc": {"page": "399B", "column": 1, "line": 12, "including-blank-lines": 1},
    "lc-img": "0906.png",
    "noted-by": "tBHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]1",
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
    "noted-by": "xBHQ-BHL-xDM",
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
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_0935 = {
    "bhla-i": 11,
    "cv": "9:35",
    "lc": "אַֽ֭דַבְּרָה",
    "what-is-weird": "פתח on א is not חטף",
    "mam": "אֲֽ֭דַבְּרָה",
    "comment": "",
    "highlight": 1,
    "lc-loc": {"page": "399B", "column": 2, "line": -8},
    "lc-img": "0935.png",
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_1001 = {
    "bhla-i": 12,
    "cv": "10:1",
    "lc": "אֲ֝דַבְּרָה֗",
    "what-is-weird": "רביע is on ה not ר",
    "mam": "אֲ֝דַבְּרָ֗ה",
    "comment": "",
    "highlight-lc": 5,
    "highlight-mam": 4,
    "lc-loc": {"page": "399B", "column": 2, "line": -6},
    "lc-img": "1001.png",
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_1015 = {
    "bhla-i": 13,
    "cv": "10:15",
    "lc": "עָנְיֽ͏ִי׃",
    "what-is-weird": "סילוק precedes חיריק",
    "mam": "עׇנְיִֽי׃",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "400A", "column": 1, "line": 14},
    "lc-img": "1015.png",
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_1103 = {
    "bhla-i": 14,
    "cv": "11:3",
    "lc": "יַחֲרִ֑ישׁו",
    "what-is-weird": "שורוק dot is missing",
    "mam": "יַחֲרִ֑ישׁוּ",
    "comment": "",
    "highlight": 6,
    "lc-loc": {"page": "400A", "column": 1, "line": -1},
    "lc-img": "1103.png",
    "noted-by": "tBHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_1106 = {
    "bhla-i": 15,
    "cv": "11:6",
    "lc": "אֱ֝ל֗וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱ֝ל֗וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "400A", "column": 2, "line": 5},
    "lc-img": "1106.png",
    "bhq-comment": _BHQ_COMMENT_LIKE_0409,
    "noted-by": "BHQ-BHL-DM",
    # Above, note BHQ-... not tBHQ-...
    # I.e. note that BHQ not only transcribed this right,
    # but also noted it in the (bottom-of-page) critical apparatus.
}
_RECORD_1107 = {
    "bhla-i": 16,
    "cv": "11:7",
    "lc": "אֱל֣וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱל֣וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "400A", "column": 2, "line": 6},
    "lc-img": "1107.png",
    "bhq-comment": _BHQ_COMMENT_LIKE_0409,
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_1113 = {
    "cv": "11:13",
    "lc": "אַ֭תָּ֗ה",
    "what-is-weird": "רביע on ת fights דחי",
    "mam": "אַ֭תָּה",
    "comment": "",
    "highlight": 2,
    "lc-loc": {"page": "400A", "column": 2, "line": 13},
    "lc-img": "1113.png",
    "noted-by": "tBHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]1",
    "noted-by-mam": True,
    "noted-by-uxlc": True,
}
_RECORD_1216 = {
    "cv": "12:16",
    "lc": "וְתֽוּשִׁיָּ֑ה",
    "lc-q": "(?)",
    "what-is-weird": "ת may have געיה",
    "mam": "וְתוּשִׁיָּ֑ה",
    "comment": [
        "There is a blob of ink below the ת.",
        " Most likely, this mark is a malformed masorah circle",
        " on the word מוליך on the line below.",
    ],
    "bhq-comment": [
        "$BHQ seems to transcribe the blob of ink as both",
        " a געיה on ת and a masorah circle on מוליך.",
        " $BHS did not have this געיה;",
        " I wish $BHQ had left well enough alone.",
    ],
    "highlight": 2,
    "lc-loc": {"page": "400B", "column": 1, "line": 11},
    "lc-img": "1216.png",
    "noted-by": "tBHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_BHQ_COMMENT_1203 = [
    "$BHQ silently supplies the מקף that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
_RECORD_1203 = {
    "bhla-i": 17,
    "cv": "12:3",
    "lc": "וְאֶת_",
    "what-is-weird": "מקף is missing",
    "mam": "וְאֶת־",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "400A", "column": 2, "line": -1},
    "lc-img": "1203.png",
    "bhq-comment": _BHQ_COMMENT_1203,
    "noted-by": "xBHQ-BHL-DM",
}
_RECORD_1409 = {
    "bhla-i": 18,
    "cv": "14:9",
    "lc": "מֵרֵ֣יַּח",
    "what-is-weird": "$yod (י) has דגש",
    "mam": "מֵרֵ֣יחַ",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "401A", "column": 1, "line": -9},
    "lc-img": "1409.png",
    "bhq-comment": "$BHQ silently ignores the possible דגש.",
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_1508 = {
    "bhla-i": 19,
    "cv": "15:8",
    "lc": "אֱל֣וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱל֣וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "401A", "column": 2, "line": -7},
    "lc-img": "1508.png",
    "bhq-comment": _BHQ_COMMENT_LIKE_0409,
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_1534 = {
    "bhla-i": 20,
    "cv": "15:34",
    "lc": "שֹֽׁ֥חַד׃",
    "what-is-weird": "מרכא fights סילוק",
    "mam": "שֹֽׁחַד׃",
    "comment": "",
    "highlight": 1,
    "lc-loc": {"page": "401B", "column": 1, "line": -3},
    "lc-img": "1534.png",
    "bhq-comment": "$BHQ silently ignores the possible מרכא.",
    "noted-by": "xBHQ-BHL-xDM",
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
    "mam": "ל֤וּ_",
    "comment": _COMMENT_1604,
    "highlight": 2,
    "lc-loc": {"page": "401B", "column": 2, "line": 3},
    "lc-img": "1604.png",
    "bhq-comment": _BHQ_COMMENT_1604,
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_1613 = {
    "bhla-i": 22,
    "cv": "16:13",
    "lc": "מְרֵרָֽתִי׃",
    "what-is-weird": "סילוק is on 2nd ר not ת",
    "mam": "מְרֵרָתִֽי׃",
    "comment": "",
    "highlight-lc": 3,
    "highlight-mam": 4,
    "lc-loc": {"page": "401B", "column": 2, "line": -10},
    "lc-img": "1613.png",
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_1620 = {
    "bhla-i": 23,
    "cv": "16:20",
    "lc": "אֱ֝ל֗וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱ֝ל֗וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "401B", "column": 2, "line": -2},
    "lc-img": "1620.png",
    "bhq-comment": _BHQ_COMMENT_LIKE_0409,
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_1704 = {
    "cv": "17:4",
    "lc": "מִּשָּׂ֑כֶל",
    "what-is-weird": "מ has דגש",
    "mam": "מִשָּׂ֑כֶל",
    "comment": [
        "Surprisingly, $BHL just includes this דגש in its body text.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "402A", "column": 1, "line": 7},
    "lc-img": "1704.png",
    "bhq-comment": "",
    "noted-by": "tBHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]p",
    "uxlc-needs-fix": "UXLC has דגש on מ (as it should) but should note the divergence from consensus",
}
_RECORD_1706 = {
    "cv": "17:6",
    "lc": "וְתֹ֖פֶתּ",
    "what-is-weird": "final ת has דגש",
    "mam": "וְתֹ֖פֶת",
    "comment": [
        "A דגש in a final ת doesn’t make sense without a קמץ or a שווא נח below.",
        " But the dot is convincing.",
    ],
    "highlight": 4,
    "lc-loc": {"page": "402A", "column": 1, "line": 7},
    "lc-img": "1706.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
}
_RECORD_1711 = {
    "cv": "17:11",
    "lc": "לְבָבִּֽי׃",
    "what-is-weird": "second ב has דגש",
    "mam": "לְבָבִֽי׃",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "402A", "column": 1, "line": 13},
    "lc-img": "1711.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
}
_BHQ_COMMENT_1804_A = [
    "$BHQ silently ignores the possible שווא part of the possible חטף פתח.",
    " It also silently ignores the possible intepretation of that ink as a געיה.",
    " I.e. other than the prepositive דחי accent,",
    " $BHQ supplies only the (full) פתח that is the consensus expectation here.",
    " $BHQ does so silently, i.e. with no note about the pointing of ה.",
]
_RECORD_1804_A = {
    "bhla-i": 24,
    "cv": "18:4",
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "n_of_m_for_this_word": (1, 2),  # this is record 1 of 2 for this word
    "lc": "הֲ֭לְמַּעַנְךָ",
    "what-is-weird": "פתח on ה is חטף.",
    "mam": "הַֽ֭לְמַעַנְךָ",
    "comment": [
        "The quirk that מ has דגש is discussed in a separate entry of mine.",
        " The געיה difference is not important to us here.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "402A", "column": 1, "line": -4},
    "lc-img": "1804.png",
    "bhq-comment": _BHQ_COMMENT_1804_A,
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/18/1/mg/106",
    "aleppo-img": "Aleppo-1804.png",
    "bhq": "הַ֭לְמַּעַנְךָ",
    "noted-by": "xBHQ-BHL-DM",
}
_BHQ_COMMENT_1804_B = [
    "$BHQ noted that the דגש on the מ in μL disagrees with μA and μY.",
    " $BHQ misses the געיה in μA.",
    " This געיה is irrelevant to $BHQ’s point here, which is about the דגש.",
    " Still, it would have been nice if $BHQ had transcribed the געיה.",
]
_RECORD_1804_B = {
    **_RECORD_1804_A,
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "n_of_m_for_this_word": (2, 2),  # this is record 2 of 2 for this word
    "what-is-weird": "מ has דגש.",
    "mam": "הַֽ֭לְמַעַנְךָ",
    "comment": [
        "The quirk that the פתח on ה is חטף is discussed in a separate entry of mine.",
        " The געיה difference is not important to us here.",
    ],
    "highlight": 3,
    "bhq-comment": _BHQ_COMMENT_1804_B,
    "noted-by": "BHQ-BHL-DM",
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
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_1809 = {
    "cv": "18:9",
    "lc": "בְּעָּקֵ֣ב",
    "lc-q": "(?)",
    "what-is-weird": "ע may have דגש",
    "mam": "בְּעָקֵ֣ב",
    "comment": [
        "A דגש in a ע doesn’t make sense.",
        " But the dot is convincing,",
        " despite being a little close to the right arm of the ע.",
    ],
    "highlight": 2,
    "lc-loc": {"page": "402A", "column": 2, "line": 2},
    "lc-img": "1809.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
}
_RECORD_1905 = {
    "bhla-i": 26,
    "cv": "19:5",
    "lc-q": "(?)",
    "lc": "חֶרְפָּתִּֽֿי",
    "what-is-weird": "דגש may fight with רפה",
    "mam": "חֶרְפָּתִֽי׃",
    "comment": [
        "A דגש on a letter with רפה doesn’t make sense.",
        " Color photos show דגש to be unlikely.",
    ],
    "highlight": 4,
    "lc-loc": {"page": "402A", "column": 2, "line": -5},
    "lc-img": "1905.png",
    "bhq-comment": [
        "$BHQ drops the note that $BHS has on this quirk, which is extraordinary."
        " As usual, we don’t know whether $BHQ dropped this note on purpose or by accident.",
        " $BHQ silently lets the faint possible דגש “win” over the clear רפה in μL.",
        " In my opinion, $BHQ should have transcribed either both marks (דגש and רפה) or neither.",
        " Thus I consider $BHQ to have not accurately transcribed μL here."
        " Also, $BHQ should have had a note.",
    ],
    "noted-by": "xBHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_1916 = {
    "bhla-i": 27,
    "cv": "19:16",
    "lc-q": "(?)",
    "lc": "קָּ֭רָאתִי",
    "what-is-weird": "ק may have דגש",
    "mam": "קָ֭רָאתִי",
    "comment": "The dot is suspiciously brown rather than black.",
    "highlight": 1,
    "lc-loc": {"page": "402B", "column": 1, "line": 8},
    "lc-img": "1916.png",
    "bhq-comment": "$BHQ noted that the דגש on the ק in μL disagrees with μA and μY.",
    "noted-by": "tBHQ-BHL-xDM",
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
    "what-is-weird": "ו has חיריק not שווא",
    "mam": "וְלֹֽא־",
    "comment": _COMMENT_2125,
    "highlight": 1,
    "lc-loc": {"page": "403A", "column": 2, "line": 13},
    "lc-img": "2125.png",
    "bhq-comment": _BHQ_COMMENT_2125,
    "noted-by": "xBHQ-BHL-xDM",
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
    "$BHQ fails to note that the אתנח it transcribed on עמו",
    " disagrees with μA and μY.",
]
_BHQ_COMMENT_2221_B = [
    "$BHQ (charitably) transcribed the top dot of the שווא",
    " using, as one often has to, faint evidence bolstered by consensus expectations.",
    " $BHQ noted (as did $BHS) that whereas the ל of ושלם is unpointed in μL,",
    " that ל has קמץ and אתנח in μA and μY.",
]
_CAM1753_IMG_INTRO_2221 = [
    "note that instead of a masorah circle, μY uses a pair of above-dots",
    " as a “callout” for a Masorah parva note;",
    " hence the pair of above-dots above ל in ושלם.",
]
_RECORD_2221_A = {
    "bhla-i": 29,
    "cv": "22:21",
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "lc-q": "(?)",
    "lc": "עִמּ֑וֹ",
    "what-is-weird": "אתנח not מונח",
    "mam": "עִמּ֣וֹ",
    "comment": _COMMENT_2221_A,
    "highlight": 2,
    "lc-loc": {"page": "403B", "column": 1, "line": -6},
    "lc-img": "2221.png",
    "bhq-comment": _BHQ_COMMENT_2221_A,
    "noted-by": "tBHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/22/1/mg/106",
    "aleppo-img": "Aleppo-2221.png",
    "cam1753-page-url": f"{_CAM1753_PAGE_URL_BASE}/n83/mode/1up",
    "cam1753-img": "Cam1753-2221.png",
    "cam1753-img-intro": _CAM1753_IMG_INTRO_2221,
}
_RECORD_2221_B = {
    **_RECORD_2221_A,
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "lc": "וּשְׁלם",
    "what-is-weird": "ל lacks קמץ־אתנח",
    "mam": "וּשְׁלָ֑ם",
    "comment": _COMMENT_2221_B,
    "highlight": 3,
    "lc-loc": {"page": "403B", "column": 1, "line": -6},
    "lc-img": "2221.png",
    "bhq-comment": _BHQ_COMMENT_2221_B,
    "noted-by": "BHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]1",
}
del _RECORD_2221_B["bhla-i"]
del _RECORD_2221_B["lc-q"]
del _RECORD_2221_B["aleppo-img"]
del _RECORD_2221_B["cam1753-img"]
_BHQ_COMMENT_2228 = [
    "$BHQ places the mark a little left of center.",
    # XXX add BHQ image
    " Though this placement is odd,",
    " this makes it clear that a טרחא was intended by $BHQ rather than a דחי.",
    " Thus $BHQ somewhat-accurately transcribed the quirk in μL,",
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
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_2230_A = {
    "cv": "22:30",
    "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    "lc": "יֽ͏ְמַלֵּ֥ט",
    "lc-q": "(?)",
    "what-is-weird": "$yod (י) may have געיה",
    "mam": "יְמַלֵּ֥ט",
    "comment": [
        "The possible געיה is before שווא.",
        " There is another mark below those marks.",
        " It is likely unintentional,",
        " and is treated accordingly, i.e. ignored,",
        " by all editions I know.",
    ],
    "highlight": 1,
    "lc-loc": {"page": "403B", "column": 2, "line": 4},
    "lc-img": "2230_A.png",
    "bhq-comment": [
        "$BHQ has the געיה but makes no note as to whether the געיה diverges from consensus.",
        " There is no consensus in many cases of געיה, since most cases of געיה are optional.",
        " געיה with שווא (whether before or after שווא) occurs often,",
        " but further research would be needed to say whether this is a case in which",
        " געיה with שווא would be expected (or at least an expected option).",
    ],
    # XXX add Aleppo image and update comments accordingly
    "noted-by": "tBHQ-xBHL-xDM-WLC",
    "wlc-422-note": "]1",
    "uxlc-needs-fix": "add t-note (transcription uncertain)",
}
_RECORD_2230_B = {
    "cv": "22:30",
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "lc": "וְ֝נִּמְלַ֗ט",
    "lc-q": "(?)",
    "what-is-weird": "נ may have דגש",
    "mam": "וְ֝נִמְלַ֗ט",
    "comment": "The dot in question is suspiciously smaller than nearby ones.",
    "highlight": 2,
    "lc-loc": {"page": "403B", "column": 2, "line": 4},
    "lc-img": "2230.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
}
_RECORD_2416 = {
    "cv": "24:16",
    "lc": "יָ֥דְּֿעוּ",
    "lc-q": "(?)",
    "what-is-weird": "דגש may fight with רפה",
    "mam": "יָ֥דְעוּ",
    "comment": [
        "A דגש on a letter with רפה doesn’t make sense.",
        " The dot in question is suspiciously larger than nearby ones,",
        " and looks different from them in other ways.",
    ],
    "highlight": 2,
    "lc-loc": {"page": "404A", "column": 1, "line": -12},
    "lc-img": "2416.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
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
    "what-is-weird": "ע may have צירה not סגול",
    "mam": "רֹעֶ֣ה",
    "comment": _COMMENT_2421,
    "highlight": 2,
    "lc-loc": {"page": "404A", "column": 2, "line": -2},
    "lc-img": "2421.png",
    "bhq-comment": _BHQ_COMMENT_2421,
    "noted-by": "xBHQ-BHL-DM",
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
    "lc": "חַי_",
    "what-is-weird": "מקף is missing",
    "mam": "חַי־",
    "comment": _COMMENT_2702,
    "highlight": 2,
    "lc-loc": {"page": "404A", "column": 2, "line": -2},
    "lc-img": "2702.png",
    "bhq-comment": _BHQ_COMMENT_2702,
    "noted-by": "xBHQ-BHL-DM",
}
_BHQ_COMMENT_2808_AND_2911 = [
    "$BHQ silently supplies the חיריק that is the consensus expectation,",
    " despite no evidence for it in μL.",
]
_RECORD_2808 = {
    "bhla-i": 33,
    "cv": "28:8",
    "lc": "הִדְריכֻ֥הוּ",
    "what-is-weird": "חיריק is missing",
    "mam": "הִדְרִיכ֥וּהוּ",
    "comment": "The מלא/חסר spelling difference is not important to us here.",
    "highlight": 3,
    "lc-loc": {"page": "404B", "column": 2, "line": 5},
    "lc-img": "2808.png",
    "bhq-comment": _BHQ_COMMENT_2808_AND_2911,
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_2911 = {
    "bhla-i": 34,
    "cv": "29:11",
    "lc": "וְעַ֥ין",
    "what-is-weird": "חיריק is missing",
    "mam": "וְעַ֥יִן",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "405A", "column": 1, "line": -12},
    "lc-img": "2911.png",
    "bhq-comment": _BHQ_COMMENT_2808_AND_2911,
    "noted-by": "xBHQ-BHL-xDM",
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
    "noted-by": "tBHQ-BHL-xDM",
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
    "noted-by": "xBHQ-BHL-xDM",
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
    " $BHQ noted that here μL disagrees with μA and μY.",
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
    "noted-by": "xBHQ-BHL-DM-WLC",
    "wlc-422-note": "]1",
    # Above we consider this xBHQ because:
    #    Though it attempts to transcribe the quirk, it does so inaccurately.
    #    Though it notes the quirk, it does so inaccurately.
}
_RECORD_3133 = {
    "bhla-i": 38,
    "cv": "31:33",
    "lc": "עֲוֺֽנִי׃",
    "what-is-weird": "סילוק is on ו not נ",
    "mam": "עֲוֺנִֽי׃",
    "comment": "",
    "highlight-lc": 2,
    "highlight-mam": 3,
    "lc-loc": {"page": "405B", "column": 2, "line": -3},
    "lc-img": "3133.png",
    "noted-by": "tBHQ-BHL-DM",
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
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_3312 = {
    "bhla-i": 40,
    "cv": "33:12",
    "lc": "אֱ֝ל֗וֹהַ",
    "what-is-weird": "ה has no מפיק",
    "mam": "אֱ֝ל֗וֹהַּ",
    "comment": "",
    "highlight": 4,
    "lc-loc": {"page": "406B", "column": 1, "line": 2},
    "lc-img": "3312.png",
    "bhq-comment": _BHQ_COMMENT_LIKE_0409,
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_3330 = {
    "bhla-i": 41,
    "cv": "33:30",
    "lc": "הַֽחַיִּים׃",
    "what-is-weird": "סילוק is on syl. 1 not 3",
    "mam": "הַחַיִּֽים׃",
    "comment": "",
    "highlight-lc": 1,
    "highlight-mam": 3,
    "lc-loc": {"page": "406B", "column": 1, "line": -1},
    "lc-img": "3330.png",
    "bhq-comment": [
        "$BHQ noted that here μL disagrees with μA and μY,",
        " which have the consensus pointing.",
    ],
    "noted-by": "BHQ-BHL-DM",
}
_RECORD_3419 = {
    "bhla-i": 42,
    "cv": "34:19",
    "lc": "נִּכַּר־",
    "what-is-weird": "נ has דגש",
    "mam": "נִכַּר־",
    "comment": "The possible דגש is faint, especially compared with the adjacent דגש on כ.",
    "highlight": 1,
    "lc-loc": {"page": "406B", "column": 2, "line": -2},
    "lc-img": "3419.png",
    "bhq-comment": _correctly_ignores("דגש", "34:19", "full"),
    "noted-by": "xBHQ-BHL-DM",
}
_BHQ_COMMENT_3612 = [
    "Here $BHQ has a typo:",
    [" it has ", author.hbo("בִּבְלִ־"), " rather than ", author.hbo("בִּבְלִי־")],
    " in the word it reports for μA and μY.",
    " I.e. it is missing a final $yod (י) before the מקף."
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
    "noted-by": "BHQ-xBHL-DM-WLC",
    "wlc-422-note": "]1",
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/36/1/mg/106",
    "aleppo-img": "Aleppo-3612.png",
    "cam1753-page-url": f"{_CAM1753_PAGE_URL_BASE}/n87/mode/1up",
    "cam1753-img": "Cam1753-3612.png",
    "uxlc-needs-fix": "UXLC has kaf (as it should) but should note the divergence from consensus",
}
_COMMENT_3629 = [
    "The color image strongly suggests that the mark in question is not ink.",
    " A געיה right next to סילוק like that would be extraordinary, by the way,",
    " though I feel no appeal to expectations is needed to dismiss this possible געיה.",
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
    "bhq-comment": _correctly_ignores("געיה", "36:29", "large"),
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_3706 = {
    "bhla-i": 44,
    "cv": "37:6",
    "lc": "לַשֶּׁ֨לַג׀",
    "what-is-weird": "2nd ל has פתח not סגול",
    "mam": "לַשֶּׁ֨לֶג׀",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "407B", "column": 2, "line": 7},
    "lc-img": "3706.png",
    "noted-by": "tBHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_3812 = {
    "bhla-i": 45,
    "cv": "38:12",
    "lc": "הְֽ֭מִיָּמֶיךָ",
    "what-is-weird": "simple שווא not חטף פתח",
    "mam": "הֲֽ֭מִיָּמֶיךָ",
    "comment": "39:20 is similar",
    "highlight": 1,
    "lc-loc": {"page": "408A", "column": 1, "line": -12},
    "lc-img": "3812.png",
    "bhq-comment": [
        "$BHQ noted that here μL disagrees with μA and μY,",
        " which have the consensus pointing.",
    ],
    "noted-by": "BHQ-BHL-DM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_3817 = {
    "cv": "38:17",
    "lc": "צַלְמָּ֣וֶת",
    "what-is-weird": "מ has דגש",
    "mam": "צַלְמָ֣וֶת",
    "comment": "",
    "highlight": 3,
    "lc-loc": {"page": "408A", "column": 1, "line": -5},
    "lc-img": "3817.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
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
    "noted-by": "xBHQ-BHL-xDM",
    # Perhaps I should have been charitable to BHQ and said tBHQ instead of xBHQ,
    # since BHQ’s transcription of רביע is somewhat reasonable if it were accompanied by a note.
    # But it is not accompanied by a note, and without a note, BHQ needs to make weird things in μL
    # look weird. So רביע is not the right transcription for a diplomatic edition having no note
    # in this location.
}
_RECORD_3906 = {
    "bhla-i": 47,
    "cv": "39:6",
    "lc": "מְלֵֽחָה׃",
    "what-is-weird": "סילוק is on ל not ח",
    "mam": "מְלֵחָֽה׃",
    "comment": "",
    "highlight-lc": 2,
    "highlight-mam": 3,
    "lc-loc": {"page": "408B", "column": 1, "line": 3},
    "lc-img": "3906.png",
    "noted-by": "tBHQ-BHL-DM",
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
        " but as is so often the case, $BHQ should have had a note about this quirk.",
    ],
    "noted-by": "tBHQ-BHL-xDM",
}
_RECORD_3920 = {
    "bhla-i": 49,
    "cv": "39:20",
    "lc": "הְֽ֭תַרְעִישֶׁנּוּ",
    "what-is-weird": "simple שווא not חטף פתח",
    "mam": "הֲֽ֭תַרְעִישֶׁנּוּ",
    "comment": "38:12 is similar",
    "highlight": 1,
    "lc-loc": {"page": "408B", "column": 1, "line": -10},
    "lc-img": "3920.png",
    "noted-by": "tBHQ-BHL-DM",
}
_RECORD_4010 = {
    "bhla-i": 50,
    "cv": "40:10",
    "lc-q": "(?)",
    "lc": "גָֽא֣וֹן",
    "what-is-weird": "געיה may be present (on ג)",
    "mam": "גָא֣וֹן",
    "comment": "The mark in question could easily be accidental.",
    "highlight": 1,
    "lc-loc": {"page": "408B", "column": 2, "line": -11},
    "lc-img": "4010.png",
    "noted-by": "tBHQ-BHL-xDM-WLC",
    "wlc-422-note": "]1",
}
_RECORD_4026 = {
    "bhla-i": 51,
    "cv": "40:26",
    "lc": "לֶֽחֱיוֹ׃",
    "what-is-weird": "סילוק on ל not $yod (י)",
    "mam": "לֶחֱיֽוֹ׃",
    "comment": "",
    "highlight-lc": 1,
    "highlight-mam": 3,
    "lc-loc": {"page": "409A", "column": 1, "line": 8},
    "lc-img": "4026.png",
    "noted-by": "tBHQ-BHL-DM",
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
    "noted-by": "xBHQ-BHL-xDM",
}
_RECORD_4213 = {
    "cv": "42:13",
    "lc": "בָנֽוֹת׃",
    "what-is-weird": "ב lacks דגש",
    "mam": "בָּנֽוֹת׃",
    "comment": "",
    "highlight": 1,
    "lc-loc": {"page": "409B", "column": 1, "line": -9, "including-blank-lines": 1},
    "lc-img": "4213.png",
    "bhq-comment": _BHQ_COMMENT_XELSEWHERE,
    "noted-by": "BHQ-xBHL-xDM",
    "uxlc-needs-fix": True,
}
QUIRKRECS = [
    _RECORD_0121,
    _RECORD_0409,
    _RECORD_0417,
    _RECORD_0701,
    _RECORD_0709,
    _RECORD_0721,
    _RECORD_0801,
    _RECORD_0807,
    _RECORD_0906,
    _RECORD_0914,
    _RECORD_0930,
    _RECORD_0935,
    _RECORD_1001,
    _RECORD_1015,
    _RECORD_1103,
    _RECORD_1106,
    _RECORD_1107,
    _RECORD_1113,
    _RECORD_1203,
    _RECORD_1216,
    _RECORD_1409,
    _RECORD_1508,
    _RECORD_1534,
    _RECORD_1604,
    _RECORD_1613,
    _RECORD_1620,
    _RECORD_1704,
    _RECORD_1706,
    _RECORD_1711,
    _RECORD_1804_A,
    _RECORD_1804_B,
    _RECORD_1806,
    _RECORD_1809,
    _RECORD_1905,
    _RECORD_1916,
    _RECORD_2125,
    _RECORD_2221_A,
    _RECORD_2221_B,
    _RECORD_2228,
    _RECORD_2230_A,
    _RECORD_2230_B,
    _RECORD_2416,
    _RECORD_2421,
    _RECORD_2702,
    _RECORD_2808,
    _RECORD_2911,
    _RECORD_2919,
    _RECORD_3105,
    _RECORD_3107,
    _RECORD_3133,
    _RECORD_3206,
    _RECORD_3312,
    _RECORD_3330,
    _RECORD_3419,
    _RECORD_3612,
    _RECORD_3629,
    _RECORD_3706,
    _RECORD_3812,
    _RECORD_3817,
    _RECORD_3902,
    _RECORD_3906,
    _RECORD_3913,
    _RECORD_3920,
    _RECORD_4010,
    _RECORD_4026,
    _RECORD_4125,
    _RECORD_4213,
]
