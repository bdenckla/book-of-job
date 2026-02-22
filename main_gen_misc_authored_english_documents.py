"""Generate HTML documentation for this project."""

import glob
import os
from pyauthor_util import author
from pyauthor_util.prep_quirkrecs import get_enriched_quirkrecs
from py import two_col_css_styles as tcstyles
from py import my_html
from pyauthor import (
    job1_full_list_details,
    job2_main_article,
    job3_uxlc,
    job4_quirks_in_mu_a,
    job5_orphan_qere_points,
    job6_cam1753_mentions,
)
from pyauthor_util.all_quirks import AllQuirks
from pyauthor_util.common_titles_etc import d2_anchor, d6_anchor, D1D_DIR
from pyauthor_util.job_ov_and_de import make_ov_and_de
from pyauthor_util.get_qr_groups import get_qr_groups
import check_spelling_in_html

__all__ = ["main"]


def main():

    jobn_rel_top = "docs/jobn"
    # Delete all HTML and CSS files to avoid stale files when output names change
    _delete_files(jobn_rel_top, ["*.html", "*.css"])
    _delete_files(f"docs/{D1D_DIR}", ["*.html"])
    #
    css_href = "style.css"
    tcstyles.make_css_file_for_authored(f"docs/{css_href}")
    tcstyles.make_css_file_for_authored(f"{jobn_rel_top}/{css_href}")
    #
    tdm_ch = jobn_rel_top, css_href
    #
    eqrs = get_enriched_quirkrecs(jobn_rel_top, "./out")
    ov_and_de = make_ov_and_de(eqrs)
    qr_groups = get_qr_groups(eqrs)
    aq = AllQuirks(tdm_ch, ov_and_de, qr_groups)
    job1_full_list_details.gen_html_files(ov_and_de)
    job2_main_article.gen_html_file(aq)
    job3_uxlc.gen_html_file(aq)
    job4_quirks_in_mu_a.gen_html_file(aq)
    job5_orphan_qere_points.gen_html_file(tdm_ch)
    job6_cam1753_mentions.gen_html_file(tdm_ch, eqrs)
    _write_index_dot_html((css_href,), "docs/index.html")
    check_spelling_in_html.main()


def _write_index_dot_html(css_hrefs, out_path):
    write_ctx = my_html.WriteCtx("Job Documents", out_path, css_hrefs=css_hrefs)
    my_html.write_html_to_file(author.para_ul(_CBODY, _CBODY_LIST), write_ctx)


def _delete_files(directory, patterns):
    for pattern in patterns:
        for file_path in glob.glob(f"{directory}/{pattern}"):
            os.remove(file_path)


_CBODY = ["This repository hosts:"]

_FIRST_DETAIL_ANCHOR = my_html.anchor_h("Job 1:19", f"./{D1D_DIR}/0119.html")

_LIST_ITEM_1 = ["A ", d2_anchor("./jobn")]
_LIST_ITEM_2 = [
    "A series of details pages used by that document, starting with",
    [" ",_FIRST_DETAIL_ANCHOR, "."],
    " While most readers will only be interested in those details as presented inside the main document,",
    " some may want to peruse the details pages directly.",
    " (They can be navigated in reading order.)",
]
    
_LIST_ITEM_3 = [
    "A ",
    d6_anchor("./jobn"),
]

_CBODY_LIST = [
    _LIST_ITEM_1,
    _LIST_ITEM_2,
    _LIST_ITEM_3,
]


if __name__ == "__main__":
    main()
