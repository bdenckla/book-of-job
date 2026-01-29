""" Exports gen_html_file and anchor """

from py import my_html
from pyauthor_util import author
from pyauthor_util.para_and_table import para_and_table
from pyauthor_util.common_titles_etc import D3_TITLE, D3_H1_CONTENTS, D3_FNAME


def gen_html_file(tdm_ch, ov_and_de, qr_groups):
    author.assert_stem_eq(__file__, D3_FNAME)
    cbody = _make_cbody(ov_and_de, qr_groups)
    author.help_gen_html_file(tdm_ch, D3_FNAME, D3_TITLE, cbody)


def _make_cbody(ov_and_de, qr_groups):
    cbody = [
        author.heading_level_1(D3_H1_CONTENTS),
        para_and_table(_cpara18, ov_and_de, qr_groups["nbhq_and_n3"]),
    ]
    return cbody


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
