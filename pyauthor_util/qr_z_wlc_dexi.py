from pycmn import hebrew_accents as ha
from pycmn.my_utils import sl_map
from py import my_html

_BASICS = [
    ("3:3", "י֭וֹם", ("397B", 2, 12)),
    ("4:4", "כּ֭וֹשֵׁל", ("398A", 1, 20)),
    ("8:16", "ה֭וּא", ("399A", 2, 23)),
    # ("18:6", "א֭וֹר", None),
    # above is commented out since it already exists as a normal record
    ("19:28", "תֹ֭אמְרוּ", ("402B", 1, 23)),
    ("20:23", "בּ֭וֹ", ("402B", 2, 26)),
    ("22:14", "ל֭וֹ", ("403B", 1, 14)),
    # ("22:28", "א֭וֹמֶר", None),
    # above is commented out since it already exists as a normal record
    ("23:6", "כֹּ֭חַ", ("403B", 2, 11)),
    ("28:24", "ה֭וּא", ("404B", 2, 25)),
    ("30:18", "כֹּ֭חַ", ("405A", 2, 25)),
    ("30:22", "ר֭וּחַ", ("405B", 1, 3)),
    ("30:30", "ע֭וֹרִי", ("405B", 1, 12)),
    ("31:4", "ה֭וּא", ("405B", 1, 17)),
    ("31:19", "א֭וֹבֵד", ("405B", 2, 9)),
    ("31:28", "ה֭וּא", ("405B", 2, 18)),
    ("31:39", "כֹּ֭חָהּ", ("406A", 1, 5)),
    ("34:19", "שׁ֭וֹעַ", ("406B", 2, 26)),
    ("34:22", "חֹ֭שֶׁךְ", ("407A", 1, 3)),
    ("35:14", "תֹ֭אמַר", ("407A", 2, 12)),
    ("36:19", "שׁ֭וּעֲךָ", ("407B", 1, 11)),
    ("37:19", "ה֭וֹדִיעֵנוּ", ("407B", 2, 23)),
    ("37:20", "ל֭וֹ", ("407B", 2, 24)),
    ("38:27", "שֹׁ֭אָה", ("408A", 2, 6)),
    ("39:11", "בּ֭וֹ", ("408B", 1, 8)),
    ("39:12", "בּ֭וֹ", ("408B", 1, 9)),
    ("40:19", "ה֭וּא", ("408B", 2, 27)),
    ("40:29", "בּ֭וֹ", ("409A", 1, 11)),
]

_COMMENT_3619 = [
    "All but the southeast end of the דחי seems to have flaked off,",
    " but luckily left some faint trace behind."
    " To charitably transcribe this word, we must not only transcribe this faint trace",
    [" but also ", my_html.bold("decline"), " to transcribe the similarly faint blob"],
    " (an erasure?) right next to it under the ש.",
]
_COMMENT_3719 = [
    "The pointing of this word must, by necessity, be transcribed with much charity.",
    " Nonetheless, the mark in question here is fairly clearly positioned",
    " as a דחי not a טרחא, though it is, unfortunately, attached to the right leg of the ה.",
    " (At least, it is attached to the right leg of the re-inked ה.)",
]
_EXTRAS = {
    "8:16": {
        "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    },
    "34:19": {
        "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    },
    "36:19": {
        "comment": _COMMENT_3619,
    },
    "37:19": {
        "comment": _COMMENT_3719,
    },
}


def _one_basic_to_record(cv_and_wlc):
    cv_str, wlc, lcloc = cv_and_wlc
    page, column, line = lcloc or ("40XY", 0, 0)
    cvlc_rec = {
        "cv": cv_str,
        "lc": wlc.replace(ha.DEX, ha.TIP),
        "what-is-weird": "טרחא not דחי",
        "mam": wlc,
        "comment": "",
        "highlight": 1,
        "lc-loc": {"page": page, "column": column, "line": line},
        "bhq-comment": [
            "$BHQ is the source of this (flawed) transcription.",
        ],
        "noted-by": "tBHQ-xBHL-xDM-zWLCdexi",
    }
    extras = _EXTRAS.get(cv_str)
    record = {**cvlc_rec, **extras} if extras else cvlc_rec
    return record


RECORDS_Z_WLC_DEXI = sl_map(_one_basic_to_record, _BASICS)
