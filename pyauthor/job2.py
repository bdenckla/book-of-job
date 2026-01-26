""" Exports gen_html_file and anchor """

from py import my_html
from pyauthor_util import author
from pyauthor.common import D2_TITLE
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME
from pyauthor_util.job1_common import num_range
from pyauthor_util.job1_common import intro
from pyauthor_util.job1_ov_and_de import row_id
from pycmn.my_utils import sl_map


def gen_html_file(tdm_ch, ov_and_de, quirkrecs):
    author.assert_stem_eq(__file__, D2_FNAME)
    cbody = _make_cbody(ov_and_de, quirkrecs)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, cbody)


def _make_cbody(ov_and_de, quirkrecs):
    groups = _get_groups(quirkrecs)
    cbody = [
        author.heading_level_1(D2_H1_CONTENTS),
        author.para_ol(_CPARA10, _CLIST10),
        author.para(_CPARA11),
        author.para(_CPARA12),
        author.para_ul(_CPARA13, _CLIST13),
        author.para_ul(_CPARA14, _CLIST14),
        author.para_ul(_CPARA15, _CLIST15),
        author.para(_CPARA16),
        author.para(_CPARA17A),
        _para_and_table(_cpara17b, ov_and_de, groups[0]),
        *intro("intro-job2"),
        author.para(_CPARA17C),
        _para_and_table(_cpara18, ov_and_de, groups[1]),
        _para_and_table(_cpara19, ov_and_de, groups[2]),
        _para_and_table(_cpara20, ov_and_de, groups[3]),
        author.para(_cpara22()),
        author.para(_cpara23(len(groups[1]))),
        author.para(_cpara24a(len(groups[4]), len(groups[5]))),
        _para_and_table(_cpara24b_dexi, ov_and_de, groups[4]),
        _para_and_table(_cpara24c_misc, ov_and_de, groups[5]),
        author.para_ul(_CPARA25, _clist25(sl_map(len, groups))),
    ]
    return cbody


def _startswith_n(part):
    return part.startswith("n")


def _startswith_x(part):
    return part.startswith("x")


def _bhq_and_others(quirkrec):
    parts = quirkrec["noted-by"].split("-")
    bhq, bhl, dm = parts[0], parts[1], parts[2]
    wlc = "xWLC" if len(parts) == 3 else parts[3]
    assert bhq in ("nBHQ", "xBHQ", "tBHQ")
    assert bhl in ("nBHL", "xBHL")
    assert dm in ("nDM", "xDM")
    assert wlc in ("nWLC", "xWLC", "zWLCmisc", "zWLCdexi")
    others = bhl, dm, wlc
    return bhq, others


def _nbhq_and_xe(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "nBHQ" and all(_startswith_x(part) for part in others)


def _foobhq_and_ne(foobhq, quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == foobhq and any(_startswith_n(part) for part in others)


def _nbhq_and_ne(quirkrec):
    return _foobhq_and_ne("nBHQ", quirkrec)


def _xbhq_and_ne(quirkrec):
    return _foobhq_and_ne("xBHQ", quirkrec)


def _tbhq_and_ne(quirkrec):
    return _foobhq_and_ne("tBHQ", quirkrec)


def _tbhq_and_zwd(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "tBHQ" and others == ("xBHL", "xDM", "zWLCdexi")


def _tbhq_and_zwm(quirkrec):
    bhq, others = _bhq_and_others(quirkrec)
    return bhq == "tBHQ" and others == ("xBHL", "xDM", "zWLCmisc")


def _get_groups(quirkrecs):
    # nbhq, xbhq: noted (as a quirk) in BHQ, not noted (as a quirk) in BHQ
    # ne, xe: noted (as a quirk) elsewhere, not noted (as a quirk) elsewhere
    # zw (zWLCmisc): noted (as consensus) by WLC (combined with MAM):
    #     flagged as a change in WLC relative to BHS, e.g. a bracket-c or bracket-v note.
    #     comparison with MAM revealed that it is a change back towards consensus,
    #     i.e. this is BHS/BHQ proposing a quirk that is not in μL
    q_nbhq_and_xe = list(filter(_nbhq_and_xe, quirkrecs))
    q_nbhq_and_ne = list(filter(_nbhq_and_ne, quirkrecs))
    q_xbhq_and_ne = list(filter(_xbhq_and_ne, quirkrecs))
    q_tbhq_and_ne = list(filter(_tbhq_and_ne, quirkrecs))
    q_tbhq_and_zwm = list(filter(_tbhq_and_zwm, quirkrecs))
    q_tbhq_and_zwd = list(filter(_tbhq_and_zwd, quirkrecs))
    groups = [
        q_nbhq_and_xe,
        q_nbhq_and_ne,
        q_xbhq_and_ne,
        q_tbhq_and_ne,
        q_tbhq_and_zwd,
        q_tbhq_and_zwm,
    ]
    return groups


def _para_and_table(para_func, ov_and_de, group_of_quirkrecs):
    return [
        author.para(para_func(len(group_of_quirkrecs))),
        _table_of_quirks(ov_and_de, group_of_quirkrecs),
    ]


def _table_of_quirks(ov_and_de, group_of_quirkrecs):
    rows = [_overview(ov_and_de, rec) for rec in group_of_quirkrecs]
    return author.table_c(rows)


def _overview(ov_and_de, quirkrec):
    the_row_id = row_id(quirkrec)
    return ov_and_de[the_row_id]["od-overview"]


_CPARA10 = [
    "Like many students of Tanakh, I started out in the cult of $BHS.",
    #
    [" I thought $BHS was ", my_html.bold("the")],
    " definitive edition.",
    #
    " Unlike many students of Tanakh, I eventually soured on $BHS,",
    " for the following reasons:",
]
#
_CLIST10 = [
    "It often fails to accurately transcribe μL (the Leningrad Codex).",
    #
    "It often fails to note where μL disagrees with other manuscripts.",
    #
    "It emphasizes manuscript quantity over quality.",
]
_CPARA11 = [
    "My first candidate for a $BHS alternative was $BHQ (Biblia Hebraica Quinta).",
    #
    " (Though I had soured on $BHS, I still hadn’t fully escaped its cult.)",
]
_CPARA12 = [
    "But I soon soured on $BHQ as well."
    #
    " I was dismayed to find that $BHQ will not be complete for many years.",
    #
    " Perhaps more importantly, I found that $BHQ still suffers from some of the",
    " same problems as $BHS.",
    #
    " Although $BHQ now emphasizes manuscript quality over quantity,",
    " the other two problems listed above remain, albeit to a lesser degree.",
]
_CPARA13 = [
    "I continued my search for better editions, and I found some.",
    #
    " This made me even more disappointed with $BHQ.",
    #
    " It seems to have been made in a bubble:",
    " its editors seem to have been",
    " unaware of or uninterested in",
    " relevant work done in other editions.",
    #
    " I can see why something like a fresh transcription of μL was beyond the scope of $BHQ.",
    #
    " But I can’t see why $BHQ would ignore the work already done in other editions,",
    #
    " in particular the following:",
]
_CLIST13 = [
    [
        "The דעת מקרא (Da-at Miqra) series,",
        " particularly the volumes with sections called",
        f" “הנוסח ומקורותיו”",
        f" (Breuer et al., {num_range(1970, 2003)})",
    ],
    ["Biblia Hebraica Leningradensia ($BHL) (Dotan, 2001)"],
    ["The Westminster Leningrad Codex ($WLC) (electronic)"],
]
_CPARA14 = [
    "The first volume of $BHQ (Megilloth) came out in 2004.",
    #
    " That means that all three of the above editions were available to the $BHQ editors.",
]
_CLIST14_ITEM1 = ["All volumes of דעת מקרא predate $BHQ Megilloth."]
_CLIST14_ITEM2 = [
    "Dotan’s $BHL predates $BHQ Megilloth.",
    #
    " Before he died, Dotan was even a consultant to the $BHQ project.",
    #
    " What’s more, his $BHL is sometimes cited as a source in $BHQ.",
    #
    " So it is particularly puzzling that his $BHL,",
    " in particular its monumental Appendix A,"
    " was not used (or was not thoroughly used) in $BHQ.",
]
_CLIST14_ITEM3 = [
    "$WLC has had various releases over its decades, many predating $BHQ Megilloth."
]
_CLIST14 = [
    _CLIST14_ITEM1,
    _CLIST14_ITEM2,
    _CLIST14_ITEM3,
]
_CPARA15 = [
    "Although it may already be clear, I should explicitly state that",
    " my purposes are narrowly focused on the Masoretic text.",
    #
    " Thus I am not concerned with",
    " the many parts of $BHQ that deal with the following:",
]
_CLIST15 = [
    "sources in languages other than Hebrew",
    "non-Masoretic (e.g. unpointed) Hebrew sources",
    "Masorah magna and parva (other than קרי Mp)",
    "the meaning of the text",
]
_CPARA16 = [
    "For all I know, those parts of $BHQ are of high quality.",
    #
    " But those parts are not my concern.",
]


_CPARA17A = [
    "Having criticized $BHQ in general terms,",
    " I will now review the specifics of the $BHQ Book of Job (2024).",
    #
    " As of now (January 2026), it is the latest volume of $BHQ to be published.",
]


def _cpara17b(the_len):
    return [
        f"First, the good news: the Job volume of $BHQ notes {str(the_len)}",
        " quirks in μL that are not noted in any of the three editions listed above.",
        #
        " I.e. these are places where $BHQ contributes something not available",
        " in any of those other three editions.",
        #
        " The contributions of $BHQ are as follows:",
    ]


_CPARA17C = [
    "Unsurprisingly, all of these contributions",
    " are new, i.e. not present in $BHS.",
    #
    " I find some of these proposed transcriptions",
    " far-fetched, i.e. unlikely to have been the scribe’s intention.",
    #
    " Nonetheless, I consider even those ones to be valuable contributions",
    " to the documentation of μL.",
]


def _cpara18_part1(the_len):
    return [
        ["It is also good news that the Job volume of $BHQ notes ", str(the_len)],
        [" quirks in μL that ", my_html.bold("are"), " noted"],
        [" in one or more of the other three editions."],
    ]


_CPARA18_PART2 = [
    " I.e. these are places where $BHQ reiterates something available",
    " in one or more of the other three editions.",
    #
    " While a reiteration is not as valuable as a new contribution,",
    " it is still valuable.",
    #
    " Indeed my main criticism of $BHQ Job is that it",
    " should have reiterated most of what can be found in those other three editions.",
    #
    " Unsurprisingly, all but one of the $BHQ reiterations",
    " are not new, i.e. they were already present in $BHS.",
    #
    " (The one that is new is the one regarding the דגש in the מ of הלמענך in 18:4.)",
    " The reiterations made by $BHQ are as follows:",
]


def _cpara18(the_len):
    return _cpara18_part1(the_len) + _CPARA18_PART2


def _cpara19(the_len):
    return [
        f"Now for some bad news:",
        f" the Job volume of $BHQ does not transcribe {str(the_len)}",
        f" quirks in μL that are noted in one or more of the other three editions.",
        #
        f" Not all such missing transcriptions are a bad thing,",
        f" as the other editions may occasionally propose transcriptions that are",
        f" far-fetched, i.e. unlikely to have been the scribe’s intention.",
        #
        f" But overall these missing transcriptions reflect poorly on $BHQ Job.",
        #
        f" In all but one case, a note is also lacking.",
        f" (The one with a note is the one regarding מאום in 31:7,",
        f" although the note, too, is inaccurate.)",
    ]


def _cpara20(the_len):
    return [
        f"Now for some mixed news:",
        f" the Job volume of $BHQ transcribes but does not note {str(the_len)}",
        f" quirks in μL that are noted in one or more of the other three editions.",
        #
        f" Those transcriptions without notes are as follows:",
    ]


_BHQ_HAS_TAR = "$BHQ has טרחא but should probably have דחי"
_BHQ_HAS_DEX = "$BHQ has דחי but should probably have טרחא"
_A_TAR_IN_BHQ = "a טרחא in $BHQ"


def _cpara24a(len_dexi, len_misc):
    len_total = len_dexi + len_misc
    return [
        f"Finally, some $WLC notes help us identify that",
        f" the Job volume of $BHQ transcribes but does not note at least {str(len_total)}",
        f" quirks in μL that,",
        [" ", my_html.bold("for good reason"), ","],
        " are not noted in any of the other three editions.",
        #
        f" The good reason is that all of these are unlikely to be the scribe’s intention,",
        f" i.e. are more likely quirks in $BHQ than quirks in μL.",
        #
        f" These {str(len_total)} likely-false quirks can be divided into two groups:",
        f" a group of {str(len_dexi)} cases where {_BHQ_HAS_TAR} and",
        f" a group of {str(len_misc)} cases not concerning {_A_TAR_IN_BHQ}.",
    ]


def _cpara24b_dexi(len_dexi):
    return [
        f"Here are the",
        f" {str(len_dexi)} cases noted in $WLC where {_BHQ_HAS_TAR}",
        f" (note that 18:6 and 22:28 could also be considered to be in this group):",
    ]


def _cpara24c_misc(len_misc):
    return [
        f"Then there are the",
        f" {str(len_misc)} cases noted in $WLC where $BHQ is probably in error",
        f" but that error does not concern {_A_TAR_IN_BHQ}.",
        f" (One of those {str(len_misc)},",
        f" the one in 22:12 goes in the opposite direction: {_BHQ_HAS_DEX}.)",
        f" Here are those {str(len_misc)} cases:",
    ]


_CPARA25 = [
    "In conclusion, by using the other three editions, we find the following about $BHQ:",
]


def _clist25(the_lens):
    len_dexi = the_lens[4]
    len_misc = the_lens[5]
    len_total = len_dexi + len_misc
    return [
        f"$BHQ contributes notes on {str(the_lens[0])} quirks not found in those editions.",
        f"$BHQ reiterates notes on {str(the_lens[1])} quirks found in those editions.",
        f"$BHQ does not transcribe {str(the_lens[2])} quirks found in those editions.",
        f"$BHQ transcribes but does not note {str(the_lens[3])} quirks found in those editions.",
        f"$BHQ transcribes but does not note at least {str(len_total)} likely-false quirks.",
    ]


def _cpara22():
    return [
        "I would not expect $BHQ to transcribe and/or note all the above quirks.",
        #
        " For example it would be reasonable for the $BHQ editors",
        " to find some of them unlikely to have been the scribe’s intention,",
        " for example finding some of them more likely to have been",
        " an ink-mark made accidentally, or a mark not made by ink at all.",
        #
        " It would also be reasonable for the $BHQ editors",
        " to find some of them likely to have been the scribe’s intention,",
        " and therefore worthy of transcription,",
        " but differing from μA and/or μY in ways too minor to note.",
    ]


def _cpara23(the_len_of_the_2nd_group):
    foo = the_len_of_the_2nd_group - 1
    bar = the_len_of_the_2nd_group
    return [
        "Nonetheless, the quirks not transcribed and/or noted by $BHQ",
        " are of high quantity and high average quality.",
        " This strongly suggest that $BHQ’s editors were either",
        " unaware of or uninterested in",
        " the other three editions.",
        #
        " I.e. it is unlikely that all these quirks were considered but rejected:",
        " it is more likely that they were simply not considered at all.",
        #
        f" This conclusion is strengthened by the fact that {foo} of the {bar}",
        " reiterations in the second group above were already present in $BHS.",
        f" I.e., the source of these {foo} reiterations is almost certainly $BHS,",
        " not one of the other three editions.",
    ]
