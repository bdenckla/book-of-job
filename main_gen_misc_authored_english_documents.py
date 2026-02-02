""" Exports main """

import glob
import os
import os.path
from py import two_col_css_styles as tcstyles
from py import my_html
from pycmn.my_utils import sl_map
from pyauthor import (
    job1_full_list_overview,
    job3_uxlc,
    job1_full_list_details,
    job2_main_article,
)
from pyauthor_util.common_titles_etc import d2_anchor
from pyauthor_util.qr_field_stats import write_qr_field_stats_json
from pyauthor_util.get_qr_groups import get_qr_groups
from pyauthor_util.noted_by import nb_dict
from pyauthor_util.short_id_etc import lc_img
from pyauthor_util.job_quirkrecs import QUIRKRECS
from pyauthor_util.job_ov_and_de import make_ov_and_de, sort_key


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
    qr_groups = get_qr_groups(qrs)
    job1_full_list_overview.gen_html_file(tdm_ch, ov_and_de)
    job1_full_list_details.gen_html_file(tdm_ch, ov_and_de)
    job2_main_article.gen_html_file(tdm_ch, ov_and_de, qr_groups)
    job3_uxlc.gen_html_file(tdm_ch, ov_and_de, qr_groups)
    #
    _write_index_dot_html((css_href,), "docs/index.html")


def _prep(jobn_rel_top):
    qrs = sorted(QUIRKRECS, key=sort_key)
    _assert_all_img_paths_exist(jobn_rel_top, qrs)
    qrs = [qr for qr in qrs if qr.get("qr-lc-proposed")]  # XXX temporary
    qrs_with_nbd = sl_map(_add_nbd, qrs)
    write_qr_field_stats_json(qrs_with_nbd, "out/qr-field-stats.json")
    ov_and_de = make_ov_and_de(qrs_with_nbd)
    return qrs_with_nbd, ov_and_de


def _add_nbd(quirkrec):
    return {**quirkrec, "nbd": nb_dict(quirkrec)}


def _assert_all_img_paths_exist(jobn_rel_top, qrs):
    for qr in qrs:
        if qr.get("qr-under-construction"):
            continue
        lc_img_path = f"{jobn_rel_top}/img/{lc_img(qr)}"
        assert os.path.exists(lc_img_path), f"Missing LC image: {lc_img_path}"


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
