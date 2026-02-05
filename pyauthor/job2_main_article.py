""" Exports gen_html_file and anchor """

from py import my_html
from pyauthor_util.para_and_table import para_and_table
from pyauthor_util import author
from pyauthor_util.common_titles_etc import (
    D2_TITLE,
    D2_H1_CONTENTS,
    D2_FNAME,
    d3_anchor,
    d4_anchor,
)
from pyauthor_util.num_range import num_range
from pyauthor_util.intro import intro
from pycmn.my_utils import dv_map


def gen_html_file(tdm_ch, ov_and_de, qr_groups):
    author.assert_stem_eq(__file__, D2_FNAME)
    cbody = _make_cbody(tdm_ch, ov_and_de, qr_groups)
    author.help_gen_html_file(tdm_ch, D2_FNAME, D2_TITLE, cbody)


def _make_cbody(tdm_ch, ov_and_de, qr_groups):
    the_lens = dv_map(len, qr_groups)
    len_dexi = the_lens["tbhq_and_zdw"]
    len_misc = the_lens["tbhq_and_zmw"]
    cbody = [
        author.heading_level_1(D2_H1_CONTENTS),
        author.para_ol(_CPARA10, _CLIST10),
        author.para(_CPARA11),
        author.para(_CPARA12),
        author.para_ul(_CPARA13, _CLIST13),
        author.para_ul(_CPARA14, _CLIST14),
        author.para_ul(_CPARA15, _CLIST15),
        author.para(_CPARA24),
        author.para(_CPARA25),
        para_and_table(_cpara26, tdm_ch, ov_and_de, qr_groups, "nbhq_and_x3"),
        *intro("intro-job2"),
        author.para(_CPARA27),
        para_and_table(_cpara28, tdm_ch, ov_and_de, qr_groups, "nbhq_and_n3"),
        para_and_table(_cpara29, tdm_ch, ov_and_de, qr_groups, "tbhq_and_n3"),
        para_and_table(_cpara30, tdm_ch, ov_and_de, qr_groups, "xbhq_and_n3"),
        author.para(_cpara31()),
        author.para(_cpara32(len(qr_groups["nbhq_and_n3"]))),
        author.para(_cpara33(len_dexi, len_misc)),
        para_and_table(_cpara34_dexi, tdm_ch, ov_and_de, qr_groups, "tbhq_and_zdw"),
        para_and_table(_cpara35_misc, tdm_ch, ov_and_de, qr_groups, "tbhq_and_zmw"),
        author.para_ul(_CPARA36, _clist36(the_lens)),
        author.heading_level_2("Postscript 1: $UXLC"),
        author.para(_CPARA_UXLC),
        author.heading_level_2("Postscript 2: quirks in μA"),
        author.para(_CPARA_QUIRKS_IN_MU_A),
    ]
    return cbody


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
_CPARA24 = [
    "For all I know, those parts of $BHQ are of high quality.",
    #
    " But those parts are not my concern.",
]


_CPARA25 = [
    "Having criticized $BHQ in general terms,",
    " I will now review the specifics of the $BHQ Book of Job (2024).",
    #
    " As of now (January 2026), it is the latest volume of $BHQ to be published.",
]


def _cpara26(the_len):
    return [
        f"First, the good news: the Job volume of $BHQ notes {str(the_len)}",
        " quirks in μL that are not noted in any of the three editions listed above.",
        #
        " I.e. these are cases where $BHQ contributes something not available",
        " in any of those other three editions.",
        #
        " The contributions of $BHQ are as follows:",
    ]


_CPARA27 = [
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


_COUNT_OF_RNTQ = 3  # RNTQ: reiterations new to BHQ
_DESCRIPTION_OF_RNTQ = ["three that are new are the ones in 6:21, 18:4, and 19:16"]
_WORDS_FOR_NUMBERS = {1: "one", 2: "two", 3: "three", 4: "four"}


_CPARA18_PART2 = [
    " I.e. these are cases where $BHQ reiterates something available",
    " in one or more of the other three editions.",
    #
    " While a reiteration is not as valuable as a new contribution,",
    " it is still valuable.",
    #
    " Indeed my main criticism of $BHQ Job is that it",
    " should have reiterated most of what can be found in those other three editions.",
    #
    f" Unsurprisingly, all but",
    f" {_WORDS_FOR_NUMBERS[_COUNT_OF_RNTQ]}",
    f" of the $BHQ reiterations",
    f" are not new, i.e. they were already present in $BHS.",
    #
    [" (The ", _DESCRIPTION_OF_RNTQ, ".)"],
    #
    f" The reiterations made by $BHQ are as follows:",
]


def _cpara28(the_len):
    return _cpara18_part1(the_len) + _CPARA18_PART2


def _cpara30(the_len):
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


def _cpara29(the_len):
    return [
        f"Now for some mixed news:",
        f" the Job volume of $BHQ transcribes but does not note {str(the_len)}",
        f" quirks in μL that are noted in one or more of the other three editions.",
        #
        " We might say that in these cases $BHQ merely implies the quirk,",
        " because it is not explicit about it."
        #
        " (A note would be required to be explicit about it.)",
        #
        " Those quirks implied by $BHQ are as follows:",
    ]


_BHQ_HAS_TAR = "$BHQ has טרחא but should probably have דחי"
_BHQ_HAS_DEX = "$BHQ has דחי but should probably have טרחא"
_A_TAR_IN_BHQ = "a טרחא in $BHQ"


def _cpara33(len_dexi, len_misc):
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


def _cpara34_dexi(len_dexi):
    return [
        f"Here are the",
        f" {str(len_dexi)} cases noted in $WLC where {_BHQ_HAS_TAR}",
        f" (note that 18:6 and 22:28 could also be considered to be in this group):",
    ]


def _cpara35_misc(len_misc):
    return [
        f"Then there are the",
        f" {str(len_misc)} cases noted in $WLC where $BHQ is probably in error",
        f" but that error does not concern {_A_TAR_IN_BHQ}.",
        f" (One of those {str(len_misc)},",
        f" the one in 22:12 goes in the opposite direction: {_BHQ_HAS_DEX}.)",
        f" Here are those {str(len_misc)} cases:",
    ]


_CPARA36 = [
    "In conclusion, by using the other three editions, we find the following about $BHQ:",
]


def _clist36(the_lens):
    len_dexi = the_lens["tbhq_and_zdw"]
    len_misc = the_lens["tbhq_and_zmw"]
    len_total = len_dexi + len_misc
    b = str(the_lens["nbhq_and_x3"])
    c = str(the_lens["nbhq_and_n3"])
    d = str(the_lens["tbhq_and_n3"])
    e = str(the_lens["xbhq_and_n3"])
    f = str(len_total)
    return [
        f"$BHQ contributes notes on {b} quirks not found in those editions.",
        f"$BHQ reiterates notes on {c} quirks found in those editions.",
        f"$BHQ transcribes but does not note {d} quirks found in those editions.",
        f"$BHQ does not transcribe {e} quirks found in those editions.",
        f"$BHQ transcribes but does not note at least {f} likely-false quirks.",
    ]


def _cpara31():
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


def _cpara32(len_of_nbhq_and_n3):
    foo = len_of_nbhq_and_n3 - _COUNT_OF_RNTQ
    bar = len_of_nbhq_and_n3
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
        " reiterations were already present in $BHS.",
        f" The source of these {foo} reiterations is almost certainly $BHS,",
        " not one of the other three editions.",
    ]


_CPARA_UXLC = [
    "If $BHQ Job were being compiled today,",
    " $UXLC (a fork of $WLC) is another edition that could help.",
    " But $UXLC’s Job changes (and their accompanying notes)",
    " were made in 2022 and 2023,",
    " probably too late to be used by $BHQ.",
    " Nonetheless, $UXLC is an edition I would like to bring attention to.",
    " So, I would like to show the ways that $UXLC",
    " might contribute to $BHQ Job if it were being compiled today.",
    [" I do so in the ", d3_anchor()],
]
_CPARA_QUIRKS_IN_MU_A = [
    "Usually, μA agrees with the consensus.",
    #
    " Indeed, where extant, it more or less ",
    my_html.bold("defines"),
    " the consensus.",
    #
    " Nonetheless, there are cases where",
    " it is μA rather than μL that diverges from the consensus.",
    #
    " It is unclear what $BHQ Job’s policy is regarding such quirks in μA,",
    " but regardless of aspirational policy, in practice, I found no such notes in $BHQ Job.",
    #
    " To me, it would make sense for $BHQ to note them,",
    [" and therefore I note a few in the ", d4_anchor()],
]
