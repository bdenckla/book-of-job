""" Exports gen_html_file and anchor """

from py import my_html
from pycmn.my_utils import my_groupby
from pyauthor_util import author
from pyauthor.common import D2_TITLE
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME
from pyauthor_util.job1_ov_and_de import row_id, sort_key
from pyauthor_util.job1_common import intro
from pycmn.my_utils import sl_map

def gen_html_file(tdm_ch, ov_and_de, quirkrecs):
    author.assert_stem_eq(__file__, D2_FNAME)
    cbody = _make_cbody(ov_and_de, quirkrecs)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, cbody)


def _make_cbody(ov_and_de, quirkrecs):
    groups = _get_groups(quirkrecs)
    cbody = [
        author.heading_level_1(D2_H1_CONTENTS),
        author.para_ol(_CPARA10, _C_LIST10),
        author.para(_CPARA11),
        author.para(_CPARA12),
        author.para_ul(_CPARA13, _C_LIST13),
        author.para(_CPARA14),
        author.para_ul(_CPARA15, _C_LIST15),
        author.para(_CPARA16),
        _para_and_table(cpara17, ov_and_de, groups[0]),
        *intro("intro-job2"),
        _para_and_table(cpara18, ov_and_de, groups[1]),
        _para_and_table(cpara19, ov_and_de, groups[2]),
        _para_and_table(cpara20, ov_and_de, groups[3]),
        author.para_ul(_CPARA21, clist21(sl_map(len, groups))),
    ]
    return cbody

def _get_groups(quirkrecs):
    qr_by_perf = my_groupby(quirkrecs, _noted_by)
    q_only_noted_in_bhq = qr_by_perf.get("BHQ-xBHL-xDM") or []
    q_noted_in_bhq_and_elsewhere = [
        *(qr_by_perf.get("BHQ-xBHL-DM") or []),
        *(qr_by_perf.get("BHQ-BHL-xDM") or []),
        *(qr_by_perf.get("BHQ-BHL-DM") or []),
    ]
    q_noted_in_bhq_and_elsewhere.sort(key=sort_key)
    q_not_transcribed_in_bhq = [
        *(qr_by_perf.get("xBHQ-xBHL-DM") or []),
        *(qr_by_perf.get("xBHQ-BHL-xDM") or []),
        *(qr_by_perf.get("xBHQ-BHL-DM") or []),
    ]
    q_not_transcribed_in_bhq.sort(key=sort_key)
    q_tbnn_in_bhq = [  # transcribed but not noted
        *(qr_by_perf.get("tBHQ-xBHL-DM") or []),
        *(qr_by_perf.get("tBHQ-BHL-xDM") or []),
        *(qr_by_perf.get("tBHQ-BHL-DM") or []),
    ]
    q_tbnn_in_bhq.sort(key=sort_key)
    groups = [
        q_only_noted_in_bhq,
        q_noted_in_bhq_and_elsewhere,
        q_not_transcribed_in_bhq,
        q_tbnn_in_bhq,
    ]
    return groups


def _para_and_table(para_func, ov_and_de, group_of_quirkrecs):
    return [
        author.para(para_func(len(group_of_quirkrecs))),
        _table_of_quirks(ov_and_de, group_of_quirkrecs),
    ]


def _noted_by(quirkrec):
    return quirkrec.get("noted-by")


def _table_of_quirks(ov_and_de, group_of_quirkrecs):
    rows = [_overview(ov_and_de, rec) for rec in group_of_quirkrecs]
    return author.table_c(rows)


def _overview(ov_and_de, quirkrec):
    the_row_id = row_id(quirkrec)
    return ov_and_de[the_row_id]["od-overview"]


def _num_range(start, stop):
    return f"{start}\N{THIN SPACE}\N{EN DASH}\N{THIN SPACE}{stop}"


_CPARA10 = [
    "Like many students of Tanakh, I started out in the cult of $BHS.",
    #
    [" I thought $BHS was", " ", my_html.bold("the")],
    " definitive edition.",
    #
    " Unlike many students of Tanakh, I eventually soured on $BHS,",
    " for the following reasons:",
]
#
_C_LIST10 = [
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
    "I continued my search for better editions, and I was fortunate to find some.",
    #
    " This made me even more disappointed with $BHQ, in retrospect.",
    #
    " I can see why something like a fresh transcription of μL was beyond the scope of $BHQ.",
    #
    " But I can’t see why $BHQ would neglect the work already done in other editions.",
    #
    " The editions most relevant to $BHQ are the following two:",
]
_C_LIST13 = [
    [
        "The דעת מקרא (Da-at Miqra) series,",
        " particularly the volumes with sections called",
        f" “הנוסח ומקורותיו”",
        f" (Breuer et al., {_num_range(1970, 2003)})",
    ],
    ["Biblia Hebraica Leningradensia ($BHL) (Dotan, 2001)"],
]
_CPARA14 = [
    "The first volume of $BHQ (Megilloth) came out in 2004.",
    #
    " All but a few volumes of דעת מקרא came out long before that.",
    #
    " Even Dotan’s $BHL was available in plenty of time to be used in all volumes of $BHQ.",
    #
    " Before he died, Dotan was even a consultant to the $BHQ project.",
    #
    " What’s more, his $BHL is sometimes used as a source in $BHQ.",
    #
    " So it is particularly puzzling that his $BHL, in particular its monumental Appendix A,"
    " was not used (or was not thoroughly used) in $BHQ.",
]
_CPARA15 = [
    "Although it may already be clear, I should explicitly state that",
    " my purposes are narrowly focused on the Masoretic text.",
    #
    " Thus I am not concerned with",
    " the many parts of $BHQ that deal with the following:",
]
_C_LIST15 = [
    "sources in languages other than Hebrew",
    "non-Masoretic (e.g. unpointed) Hebrew sources",
    "Masorah magna and parva",
    "the meaning of the text",
]
_CPARA16 = [
    "For all I know, those parts of $BHQ are of high quality.",
    #
    " But those parts are not my concern.",
]
_CPARA21 = [
    "In conclusion, compared to the μL quirks noted in $BHL and דעת מקרא:",
]


def cpara17(the_len):
    return [
        "Having criticized $BHQ in general terms,",
        " I will now review the specifics of the $BHQ Book of Job.",
        #
        " As of now, it is the latest volume of $BHQ to be published.",
        #
        f" First, the good news: the Job volume of $BHQ notes {str(the_len)}",
        " quirks in μL that were not noted in either $BHL Appendix A or דעת מקרא.",
        " I.e. these are places where $BHQ contributes something not available",
        " in either of those two other editions.",
        " It is perhaps not coincidental that none of these contributions",
        " were already present in $BHS."
        " Those contributions are as follows:",
    ]


def cpara18(the_len):
    return [
        f"It is also good news that the Job volume of $BHQ notes {str(the_len)}",
        " quirks in μL that are noted in $BHL Appendix A and/or דעת מקרא.",
        " I.e. these are places where $BHQ reiterates something available",
        " in one or both of those two other editions.",
        " While reiteration is not as valuable as new contributions,",
        " it is still valuable.",
        " Indeed my main criticism of $BHQ Job is that it",
        " should have reiterated most or all of what can be found in those editions.",
        " It is perhaps not coincidental that all but one of the $BHQ reiterations",
        " were already present in $BHS."
        " (The one new to $BHQ is the one in 18:4.)",
        " The reiterations made by $BHQ are as follows:",
    ]


def cpara19(the_len):
    return [
        f"Now for some bad news: the Job volume of $BHQ fails to transcribe {str(the_len)}",
        " quirks in μL that are noted in $BHL Appendix A and/or דעת מקרא.",
        " And, either by coincidence or editorial policy,",
        " $BHQ never notes a quirk it does not transcribe.",
    ]


def cpara20(the_len):
    return [
        f"Now for some mixed news: the Job volume of $BHQ transcribes but does not note {str(the_len)}",
        " quirks in μL that are noted in $BHL Appendix A and/or דעת מקרא.",
        " Those transcriptions without notes are as follows:",
    ]


def clist21(the_lens):
    return [
        f"$BHQ contributes notes on {str(the_lens[0])} quirks not found in those sources.",
        f"$BHQ reiterates notes on {str(the_lens[1])} quirks are found those sources.",
        f"$BHQ fails to transcribe (or note) {str(the_lens[2])} quirks noted in those sources.",
        f"$BHQ transcribes but does not note {str(the_lens[3])} quirks noted in those sources.",
    ]       