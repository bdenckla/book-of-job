""" Exports gen_html_file and anchor """

from pyauthor_util import author
from pyauthor.common import D2_TITLE
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME
from py import my_html
from pyauthor_util.job1_quirkrecs import QUIRKRECS_BY_PERF
from pyauthor_util.job1_ov_and_de import row_id
from pyauthor_util.job1_common import intro


def gen_html_file(tdm_ch, ov_and_de):
    author.assert_stem_eq(__file__, D2_FNAME)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, _make_cbody(ov_and_de))


def _make_cbody(ov_and_de):
    cbody = [
        author.heading_level_1(D2_H1_CONTENTS),
        author.para_ol(_CPARA10, _C_LIST10),
        author.para(_CPARA11),
        author.para(_CPARA12),
        author.para_ul(_CPARA13, _C_LIST13),
        author.para(_CPARA14),
        author.para_ul(_CPARA15, _C_LIST15),
        author.para(_CPARA16),
        author.para(_CPARA17),
        _table_of_quirks(ov_and_de, _QUIRKS_ONLY_NOTED_IN_BHQ),
        *intro("intro-job2"),
        author.para(_CPARA18),
        _table_of_quirks(ov_and_de, _QUIRKS_NOTED_IN_BHQ_AND_ELSEWHERE),
        author.para(_CPARA19),
        _table_of_quirks(ov_and_de, _QUIRKS_NOT_TRANSCRIBED_IN_BHQ),
    ]
    return cbody


def _table_of_quirks(ov_and_de, quirkrecs):
    rows = [_overview(ov_and_de, rec) for rec in quirkrecs]
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
        "The דעת מקרא series,",
        " particularly the volumes with sections called",
        f" “הנוסח ומקורותיו”",
        f" (Breuer et al., {_num_range(1970, 2003)})",
    ],
    ["Biblia Hebraica Leningradensia ($BHL) (Dotan, 2001)"],
]
_CPARA14 = [
    "The first volume of $BHQ (Megilloth) came out in 2004.",
    #
    " All but a few volumes of דעת מקרא came long before that.",
    #
    " Even Dotan’s $BHL was available in plenty of time to be used in all volumes of $BHQ.",
    #
    " Before he died, Dotan was even a consultant for $BHQ.",
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
_QUIRKS_ONLY_NOTED_IN_BHQ = QUIRKRECS_BY_PERF.get("BHQ-xBHL-xDM") or []
_QUIRKS_NOTED_IN_BHQ_AND_ELSEWHERE = [
    *(QUIRKRECS_BY_PERF.get("BHQ-xBHL-DM") or []),
    *(QUIRKRECS_BY_PERF.get("BHQ-BHL-xDM") or []),
    *(QUIRKRECS_BY_PERF.get("BHQ-BHL-DM") or []),
]
_QUIRKS_NOT_TRANSCRIBED_IN_BHQ = [
    *(QUIRKRECS_BY_PERF.get("xBHQ-xBHL-DM") or []),
    *(QUIRKRECS_BY_PERF.get("xBHQ-BHL-xDM") or []),
    *(QUIRKRECS_BY_PERF.get("xBHQ-BHL-DM") or []),
]
_CPARA17 = [
    "Having criticized $BHQ in general terms,",
    " I will now review the specifics of the $BHQ Book of Job.",
    #
    " As of now, it is the latest volume of $BHQ to be published.",
    #
    " First, the good news: the Job volume of $BHQ notes",
    [" ", str(len(_QUIRKS_ONLY_NOTED_IN_BHQ))],
    " quirks in μL that were not noted in either $BHL Appendix A or דעת מקרא.",
    " They are as follows:",
]
_CPARA18 = [
    "It is also good news that the Job volume of $BHQ notes",
    [" ", str(len(_QUIRKS_NOTED_IN_BHQ_AND_ELSEWHERE))],
    " quirks in μL that are noted in $BHL Appendix A and/or דעת מקרא.",
]
_CPARA19 = [
    "Now for some bad news: the Job volume of $BHQ fails to transcribe",
    [" ", str(len(_QUIRKS_NOT_TRANSCRIBED_IN_BHQ))],
    " quirks in μL that are noted in $BHL Appendix A and/or דעת מקרא.",
    " And, either by coincidence or editorial policy,",
    " $BHQ never notes a quirk it does not transcribe."
]
