from pycmn import hebrew_accents as ha
from pycmn.my_utils import sl_map

_BASICS = [
    ("3:3", "י֭וֹם"),
    ("4:4", "כּ֭וֹשֵׁל"),
    ("8:16", "ה֭וּא"),
    # ("18:6", "א֭וֹר"),
    # above is commented out since it already exists as a normal record
    ("19:28", "תֹ֭אמְרוּ"),
    ("20:23", "בּ֭וֹ"),
    ("22:14", "ל֭וֹ"),
    # ("22:28", "א֭וֹמֶר"),
    # above is commented out since it already exists as a normal record
    ("23:6", "כֹּ֭חַ"),
    ("28:24", "ה֭וּא"),
    ("30:18", "כֹּ֭חַ"),
    ("30:22", "ר֭וּחַ"),
    ("30:30", "ע֭וֹרִי"),
    ("31:4", "ה֭וּא"),
    ("31:19", "א֭וֹבֵד"),
    ("31:28", "ה֭וּא"),
    ("31:39", "כֹּ֭חָהּ"),
    ("34:19", "שׁ֭וֹעַ"),
    ("34:22", "חֹ֭שֶׁךְ"),
    ("35:14", "תֹ֭אמַר"),
    ("36:19", "שׁ֭וּעֲךָ"),
    ("37:19", "ה֭וֹדִיעֵנוּ"),
    ("37:20", "ל֭וֹ"),
    ("38:27", "שֹׁ֭אָה"),
    ("39:11", "בּ֭וֹ"),
    ("39:12", "בּ֭וֹ"),
    ("40:19", "ה֭וּא"),
    ("40:29", "בּ֭וֹ"),
]

_EXTRAS = {
    "8:16": {
        "n_of_m_for_this_verse": (1, 2),  # this is record 1 of 2 for this verse
    },
    "34:19": {
        "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    },
}


def _one_basic_to_record(cvlc):
    cv, lc = cvlc
    cvlc_rec = {
        "cv": cv,
        "lc": lc,
        "what-is-weird": "דחי not טרחא",
        "mam": lc.replace(ha.DEX, ha.TIP),
        "comment": "",
        "highlight": 1,
        "lc-loc": {"page": "40XY", "column": 0, "line": 0},
        "lc-img": f"{cv.replace(':', '')}.png",
        "bhq-comment": [
            "$BHQ is the source of this (flawed) transcription.",
        ],
        "noted-by": "tBHQ-xBHL-xDM-zWLCdexi",
    }
    extras = _EXTRAS.get(cv)
    if extras:
        return {**cvlc_rec, **extras}
    return cvlc_rec


RECORDS_Z_WLC_DEXI = sl_map(_one_basic_to_record, _BASICS)
