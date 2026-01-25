from pycmn import hebrew_accents as ha
from pycmn.my_utils import sl_map
from pyauthor_util.job1_ov_and_de import short_id

_BASICS = [
    ("3:3", "י֭וֹם", ("397B", 2, 12)),
    ("4:4", "כּ֭וֹשֵׁל", ("398A", 1, 20)),
    ("8:16", "ה֭וּא", ("399A", 2, 23)),
    # ("18:6", "א֭וֹר", None),
    # above is commented out since it already exists as a normal record
    ("19:28", "תֹ֭אמְרוּ", ("402B", 1, 23)),
    ("20:23", "בּ֭וֹ", None),
    ("22:14", "ל֭וֹ", None),
    # ("22:28", "א֭וֹמֶר", None),
    # above is commented out since it already exists as a normal record
    ("23:6", "כֹּ֭חַ", None),
    ("28:24", "ה֭וּא", None),
    ("30:18", "כֹּ֭חַ", None),
    ("30:22", "ר֭וּחַ", None),
    ("30:30", "ע֭וֹרִי", None),
    ("31:4", "ה֭וּא", None),
    ("31:19", "א֭וֹבֵד", None),
    ("31:28", "ה֭וּא", None),
    ("31:39", "כֹּ֭חָהּ", None),
    ("34:19", "שׁ֭וֹעַ", None),
    ("34:22", "חֹ֭שֶׁךְ", None),
    ("35:14", "תֹ֭אמַר", None),
    ("36:19", "שׁ֭וּעֲךָ", None),
    ("37:19", "ה֭וֹדִיעֵנוּ", None),
    ("37:20", "ל֭וֹ", None),
    ("38:27", "שֹׁ֭אָה", None),
    ("39:11", "בּ֭וֹ", ("408B", 1, 9)),
    ("39:12", "בּ֭וֹ", ("408B", 1, 10)),
    ("40:19", "ה֭וּא", ("408B", 2, 27)),
    ("40:29", "בּ֭וֹ", ("409A", 1, 11)),
]

_EXTRAS = {
    "8:16": {
        "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    },
    "34:19": {
        "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
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
    img_basename = short_id(record)
    return {**record, "lc-img": f"{img_basename}.png"}


RECORDS_Z_WLC_DEXI = sl_map(_one_basic_to_record, _BASICS)
