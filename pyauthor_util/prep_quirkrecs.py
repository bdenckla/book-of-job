import os
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


def _add_auto_imgs(jobn_rel_top, quirkrec):
    """Auto-detect LC, Aleppo, and Cam1753 images if files exist on disk."""
    result = quirkrec.copy()
    sid = short_id(quirkrec)
    # Auto-detect LC image (using lc_img function which handles extension)
    if not result.get("qr-lc-img"):
        result["qr-lc-img"] = lc_img(quirkrec)
    lc_img_path = f"{jobn_rel_top}/img/{result['qr-lc-img']}"
    assert os.path.exists(lc_img_path), f"Missing LC image: {lc_img_path}"
    # Auto-detect Aleppo and Cam1753 images
    for field, prefix in [("qr-aleppo-img", "Aleppo-"), ("qr-cam1753-img", "Cam1753-")]:
        if result.get(field):
            continue  # Already explicitly set
        auto_img = f"{prefix}{sid}.png"
        auto_path = f"{jobn_rel_top}/img/{auto_img}"
        if os.path.exists(auto_path):
            result[field] = auto_img
    return result


def _assert_lc_img_fields_filled(qrs):
    for qr in qrs:
        assert qr.get("qr-lc-img"), f"Missing qr-lc-img for {short_id(qr)}"


def _sort_key(quirkrec):
    return short_id(quirkrec)


def prep_quirkrecs(jobn_rel_top, json_outdir):
    qrs_1 = sorted(QUIRKRECS, key=_sort_key)
    qrs_2 = sl_map((_add_auto_imgs, jobn_rel_top), qrs_1)
    qrs_3 = sl_map(_add_nbd, qrs_2)
    qrs_4 = flatten_qrs(qrs_3)
    _assert_lc_img_fields_filled(qrs_4)
    write_qr_field_stats_json(
        qrs_4,
        f"{json_outdir}/qr-field-stats-ordered-by-count.json",
        f"{json_outdir}/qr-field-stats-ordered-by-field-name.json",
    )
    write_quirkrecs_json(qrs_4, f"{json_outdir}/quirkrecs.json")
    return qrs_4
