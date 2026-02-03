from pyauthor_util.short_id_etc import lc_img, short_id
from pyauthor_util.noted_by import nb_dict
from pyauthor_util.flatten_qrs import flatten_qrs
from pyauthor_util.job_quirkrecs import QUIRKRECS
from pyauthor_util.qr_make_json_outputs import (
    write_qr_field_stats_json,
    write_quirkrecs_json,
)
from pycmn.my_utils import sl_map


def _add_nbd(quirkrec):
    return {**quirkrec, "nbd": nb_dict(quirkrec)}


def _assert_all_img_paths_exist(jobn_rel_top, qrs):
    for qr in qrs:
        if qr.get("qr-under-construction"):
            continue
        lc_img_path = f"{jobn_rel_top}/img/{lc_img(qr)}"
        assert os.path.exists(lc_img_path), f"Missing LC image: {lc_img_path}"


def _sort_key(quirkrec):
    return short_id(quirkrec)


def prep_quirkrecs(jobn_rel_top, json_outdir):
    qrs_1 = sorted(QUIRKRECS, key=_sort_key)
    _assert_all_img_paths_exist(jobn_rel_top, qrs_1)
    qrs_1 = [qr for qr in qrs_1 if qr.get("qr-lc-proposed")]  # XXX temporary
    qrs_2 = sl_map(_add_nbd, qrs_1)
    qrs_3 = flatten_qrs(qrs_2)
    write_qr_field_stats_json(qrs_3, f"{json_outdir}/qr-field-stats.json")
    write_quirkrecs_json(qrs_3, f"{json_outdir}/quirkrecs.json")
    return qrs_3
