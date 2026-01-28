""" Exports gen_html_file and anchor """

from py import my_html
from pyauthor_util import author
from pyauthor.common import D3_TITLE
from pyauthor.common import D3_H1_CONTENTS
from pyauthor.common import D3_FNAME
from pyauthor.uxlc_changes_of_interest import COI_LIST
from pycmn.my_utils import sl_map


def _coi_to_quirkrec(coi):
    # Convert a change of interest to a quirk record
    # Implementation depends on the structure of COI_LIST items
    cn_colon_vn, _wn = coi["citation"].removeprefix("Job ").split(".")
    (page, column_colon_line) = coi["lc"].removeprefix("Folio_F").split(" ")
    column, line = column_colon_line.split(":")
    release = coi["release"]
    changeset = coi["changeset"]
    changeset_index = coi["n"]
    uxlc_change_url = (
        f"https://tanach.us/Changes/{release}%20-%20Changes/"
        f"{release}%20-%20Changes.xml?"
        f"{changeset}-{changeset_index}"
    )
    out = {
        "cv": cn_colon_vn,
        "lc": coi["reftext"],
        "what-is-weird": coi["description"],
        "mam": coi["changetext"],
        "comment": coi["notes"],
        "highlight": 1,
        "lc-loc": {"page": page, "column": int(column), "line": int(line)},
        "bhq-comment": [
            "$BHQ is the source of this (flawed) transcription.",
        ],
        "noted-by": "tBHQ-xBHL-xDM-xWLC-zUXLC",
        "uxlc-change-url": uxlc_change_url,
    }
    return out


def gen_html_file(tdm_ch, ov_and_de, quirkrecs):
    quirkrecs = sl_map(_coi_to_quirkrec, COI_LIST)
_write_quirkrecs_to_file(quirkrecs, "output_quirkrecs.py")
    author.assert_stem_eq(__file__, D3_FNAME)
    cbody = _make_cbody(ov_and_de, quirkrecs)
    author.help_gen_html_file(tdm_ch, D3_FNAME, D3_TITLE, cbody)


def _make_cbody(ov_and_de, quirkrecs):
    groups = _get_groups(quirkrecs)
    cbody = [
        author.heading_level_1(D3_H1_CONTENTS),
        _para_and_table(_cpara18, ov_and_de, groups[1]),
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


def _write_quirkrecs_to_file(quirkrecs, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("# Auto-generated quirkrecs\n\n")
        f.write("QUIRKRECS = [\n")
        for rec in quirkrecs:
            f.write("    {\n")
            for key, value in rec.items():
                f.write(f"        {key!r}: {value!r},\n")
            f.write("    },\n")
        f.write("]\n")
