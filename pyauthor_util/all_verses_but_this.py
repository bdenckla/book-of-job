from pyauthor_util.english_list import english_list

# Job verses where L omits dagesh after מה
_NO_DAG_AFTER_MAH_VERSES = [
    "16:6",
    "21:15",
    "34:33@VMH0YD3F",
    "35:7",
]
_PTX_IS_NOT_XTF_VERSES = [
    "9:35",
    "27:9",
    "34:33@HM3M5",
]
_LEG_MISSING_BEFORE_G3YH_RBY3_VERSES = [
    "32:11",
    "34:33@YJLMNH_2_of_2_FTW",
]


def ptx_is_not_xtf(cv: str) -> list[str]:
    return [
        "As $DM footnote 20 mentions, this is one of three such cases, the other two being",
        *[" ", _all_verses_but_this(_PTX_IS_NOT_XTF_VERSES, cv), "."],
        " In all three cases,",
        " the consensus has געיה on an initial vocal שווא notated as a חטף פתח.",
        " In μL, the געיה is on an initial פתח,",
        " a full (albeit short) syllable rather than a שווא.",
    ]


def no_dag_after_mah(cv: str) -> list[str]:
    return [
        "As $DM footnote 25 mentions, the omission of דגש after %מה־",
        *[" is common in μL. See ", _all_ndam_but_this(cv), "."],
    ]


def leg_missing_before_g3yh_rby3(cv: str) -> list[str]:
    others = _all_verses_but_this(_LEG_MISSING_BEFORE_G3YH_RBY3_VERSES, cv)
    return [
        "As $DM footnote 32 mentions, in two cases in Job,",
        " μL omits the לגרמיה stroke before a word with געיה and רביע.",
        *[" The other such case is ", others, "."],
        " In both cases, it looks like there may have been an erasure in between the words,",
        " where one would expect a לגרמיה to have been, if one was originally present in μL.",
    ]


def _all_verses_but_this(verses: list[str], cv: str) -> str:
    """Return an English-formatted list of verses, excluding cv.

    Verses may carry a @WORDID suffix for disambiguated linking
    (e.g. "34:33@VMH0YD3F").  The suffix is retained in the output
    so dollar_sub can generate the correct link.
    """
    others = [v for v in verses if _bare_cv(v) != cv]
    return english_list(others)


def _bare_cv(v: str) -> str:
    """Strip ~ prefix and @WORDID suffix to get a plain chapter:verse."""
    v = v.lstrip("~")
    if "@" in v:
        v = v.split("@", 1)[0]
    return v


def _all_ndam_but_this(cv: str) -> str:
    return _all_verses_but_this(_NO_DAG_AFTER_MAH_VERSES, cv)
