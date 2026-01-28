""" Exports main """

import glob
import os
import os.path
from py import two_col_css_styles as tcstyles
from py import my_html
from pyauthor import (
    job1_full_list_overview,
    job3_uxlc,
    job1_full_list_details,
    job2_main_article,
)
from pyauthor.common import d2_anchor
from pyauthor_util.short_id_etc import lc_img
from pyauthor_util.job1_quirkrecs import QUIRKRECS
from pyauthor_util.job1_ov_and_de import make_ov_and_de, sort_key


def main():

    jobn_rel_top = "docs/jobn"
    # Delete all HTML and CSS files to avoid stale files when output names change
    _delete_files(jobn_rel_top, ["*.html", "*.css"])
    #
    css_href = "style.css"
    tcstyles.make_css_file_for_authored(f"docs/{css_href}")
    tcstyles.make_css_file_for_authored(f"{jobn_rel_top}/{css_href}")
    #
    tdm_ch = jobn_rel_top, css_href
    #
    qrs, ov_and_de = _prep(jobn_rel_top)
    job1_full_list_overview.gen_html_file(tdm_ch, ov_and_de)
    job1_full_list_details.gen_html_file(tdm_ch, ov_and_de)
    job2_main_article.gen_html_file(tdm_ch, ov_and_de, qrs)
    job3_uxlc.gen_html_file(tdm_ch, ov_and_de, qrs)

    #
    _write_index_dot_html((css_href,), "docs/index.html")


def _prep(jobn_rel_top):
    qrs = sorted(QUIRKRECS, key=sort_key)
    for qr in qrs:
        lc_img_path = f"{jobn_rel_top}/img/{lc_img(qr)}"
        assert os.path.exists(lc_img_path), f"Missing LC image: {lc_img_path}"
    ov_and_de = make_ov_and_de(qrs)
    return qrs, ov_and_de


def _write_index_dot_html(css_hrefs, out_path):
    write_ctx = my_html.WriteCtx("Job Documents", out_path, css_hrefs=css_hrefs)
    my_html.write_html_to_file(_CBODY, write_ctx)


def _delete_files(directory, patterns):
    for pattern in patterns:
        for file_path in glob.glob(f"{directory}/{pattern}"):
            os.remove(file_path)


_CBODY = [
    "Currently this repository hosts only one",
    " ",
    d2_anchor("./jobn"),
]


if __name__ == "__main__":
    main()
