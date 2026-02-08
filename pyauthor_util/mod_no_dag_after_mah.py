"""Data about omission of dagesh after the word 'מה' in the Leningrad Codex.

Per Da'at Miqra footnote 25:
השמטת דגש אחר תיבת 'מה' מצויה ב־ל. כך: טז ו (גם ב־ד); כא טו; לד לג; לה ז.
"The omission of dagesh after the word 'מה' is common in L. Thus: 16:6 (also in D); 21:15; 34:33; 35:7."
"""

from pyauthor_util.english_list import english_list

_SHADDAI_VERSES = [
    "21:15",
    "24:1",
    "27:13",
]
# Job verses where L omits dagesh after מה
_NO_DAG_AFTER_MAH_VERSES = [
    "16:6",
    *_SHADDAI_VERSES,
    "34:33",
    "35:7",
]
_PTX_IS_NOT_XTF_VERSES = [
    "9:35",
    "27:9",
    "34:33",
]


def _all_verses_but_this(verses: list[str], cv: str) -> str:
    """Return an English-formatted list of verses, excluding cv."""
    others = [v for v in verses if v != cv]
    return english_list(others)


def ptx_is_not_xtf(cv: str) -> list[str]:
    return [
        "As $DM footnote 20 mentions, this is one of three such cases, the other two being",
        *[" ", _all_verses_but_this(_PTX_IS_NOT_XTF_VERSES, cv), "."],
        " In all three cases,",
        " the consensus has געיה on an initial vocal שווא notated as a חטף פתח.",
        " In μL, the געיה is on an initial פתח,",
        " a full (albeit short) syllable rather than a שווא.",
    ]


def _all_ndam_but_this(cv: str) -> str:
    return _all_verses_but_this(_NO_DAG_AFTER_MAH_VERSES, cv)


def _all_shaddai_but_this(cv: str) -> str:
    return _all_verses_but_this(_SHADDAI_VERSES, cv)


def no_dag_after_mah(cv: str) -> list[str]:
    return [
        "As $DM footnote 25 mentions, the omission of דגש after מה־",
        " is common in μL. See ", _all_ndam_but_this(cv), ".",
    ]


def no_dag_after_mah_shaddai(cv: str) -> list[str]:
    return [
        *no_dag_after_mah(cv),
        " Of those, the following are שדי cases like this one:",
        *[" ",_all_shaddai_but_this(cv), "."],
    ]
