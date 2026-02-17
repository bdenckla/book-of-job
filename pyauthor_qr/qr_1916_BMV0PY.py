from pyauthor_util import author

_GENCOM_PARA_1 = [
    "μL omits the רביע of רביע מוגרש,",
    " which is expected,",
    " since μL’s habit is to omit the רביע in cases like this,",
    " where the רביע and the גרש מוקדם would be cramped together on the same letter.",
    " So, while μL doesn’t literally match the consensus we have presented,",
    " we can say that it implies that consensus,",
    " that consensus being merely the explicit notation of what μL implies.",
]
_GENCOM_PARA_2 = [
    "In μL, there is some extra ink on the right side of the גרש מוקדם,",
    " which could, perhaps, be a misplaced רביע,",
    " but I find this unlikely.",
]
RECORD_1916_BMV0PY = {
    "qr-noted-by-mam": True,
    "qr-noted-by": "aDM",
    "qr-cv": "19:16",
    "qr-ac-proposed": "בְּ֝מוֹ־פִ֗י",
    "qr-consensus": "בְּמוֹ־פִ֝֗י",
    "qr-highlight-ac-proposed": [1, 5],
    "qr-highlight-consensus": 5,
    "qr-what-is-weird": "רביע מוגרש spans מקף",
    "qr-lc-loc": {"page": "402B", "column": 1, "line": 8},
    "qr-ac-loc": {"page": "275r", "column": 1, "line": 12, "word": 2},
    "qr-generic-comment": [
        author.para(_GENCOM_PARA_1),
        author.para(_GENCOM_PARA_2),
    ],
}
