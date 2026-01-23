from py import my_html


RECORD_3812_B = {
    "cv": "38:12",
    "n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "lc": "יִדַּ֖עְתָּה הַשַּׁ֣חַר",
    "what-is-weird": "ה copied not moved in קרי",
    "mam": "יִדַּ֖עְתָּ הַשַּׁ֣חַר",
    "comment": [
        "The consensus is that this is one of those כתיב/קרי cases",
        " where the word boundary shifts from being after a ה to before that ה.",
        " I.e. ידעתה שחר becomes ידעת השחר.",
        " I.e. the ה that is at the end of the first word in the כתיב",
        " moves to the start of the second word in the קרי.",
        " Similar cases include",
        " 2 Samuel 5:2 (the כתיב is הייתה מוציא) and",
        " Ezekiel 42:9 (the כתיב is ומתחתה לשכות).",
        " In contrast to the consensus, in going from כתיב to קרי,",
        [" μL can be though of as having ", my_html.bold("copied")],
        " the ה to the second word rather than moving it.",
    ],
    "highlight-lc": 5,
    "lc-loc": {"page": "408A", "column": 1, "line": -11},
    "lc-img": "3812_B.png",
    "aleppo-img": "Aleppo-3812_B.png",
    "aleppo-page-url": "https://www.mgketer.org/mikra/29/38/1/mg/106",
    "bhq-comment": [
        "$BHS does not catch this quirk in μL: it reflects the consensus rather than μL.",
        " $BHQ half-fixes the error in $BHS:",
        " it updates its marginal קרי note to reflect μL rather than the consensus,",
        " but it does not correspondingly update its bottom-of-page critical apparatus note.",
        " This is similar to what happened with 26:14.",
    ],
    "noted-by": "xBHQ-xBHL-xDM-nWLC",
}