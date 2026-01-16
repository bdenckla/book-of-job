""" Exports gen_html_file and anchor """

from pyauthor_util import author
from pyauthor.common import D2_TITLE
from pyauthor.common import D2_H1_CONTENTS
from pyauthor.common import D2_FNAME
from py import my_html
from pyauthor_util.job1_records import RECORDS_MISSED_BY_BOTH
from pyauthor_util.job1_ov_and_de import make_overview_row
from pyauthor_util.job1_common import intro


def gen_html_file(tdm_ch):
    author.assert_stem_eq(__file__, D2_FNAME)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, _CBODY)


def num_range(start, stop):
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
_C_LIST_ITEMS_AFTER_PARA10 = [
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
    " These other editions include the following:",
]
_C_LIST_ITEMS_AFTER_PARA13 = [
    f"דעת מקרא (Breuer et al., {num_range(1970, 2003)})",
    "$BHL (Dotan, 2001)",
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
_C_LIST_ITEMS_AFTER_PARA15 = [
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
_CPARA17 = [
    "Having criticized $BHQ in general terms,",
    " I will now review the specifics of the $BHQ Book of Job.",
    #
    " As of now, it is the latest volume of $BHQ to be published.",
    #
    " First, the good news: the Job volume of $BHQ catches",
    " some quirks in μL that were missed by both $BHL Appendix A and דעת מקרא.",
    " They are as follows:",
]


def make_mini_table(records):
    rows = [make_overview_row(record) for record in records]
    return author.table_c(rows)


_CBODY = [
    author.heading_level_1(D2_H1_CONTENTS),
    author.para(_CPARA10),
    author.ordered_list(_C_LIST_ITEMS_AFTER_PARA10),
    author.para(_CPARA11),
    author.para(_CPARA12),
    author.para(_CPARA13),
    author.unordered_list(_C_LIST_ITEMS_AFTER_PARA13),
    author.para(_CPARA14),
    author.para(_CPARA15),
    author.unordered_list(_C_LIST_ITEMS_AFTER_PARA15),
    author.para(_CPARA16),
    author.para(_CPARA17),
    make_mini_table(RECORDS_MISSED_BY_BOTH),
    *intro("intro-job2"),
]
