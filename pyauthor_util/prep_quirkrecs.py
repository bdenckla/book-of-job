import os
from pyauthor_util.img_util import _INFO_ABOUT_OPTIONAL_IMAGES, get_auto_imgs
from pyauthor_util.short_id_etc import short_id
from pyauthor_util.noted_by import nb_dict
from pyauthor_util.flatten_qrs import flatten_strings_in_one_qr
from pyauthor_util.get_qr_groups import get_pgroup
from pyauthor_util.job_quirkrecs import QUIRKRECS
from pyauthor_util.qr_make_json_outputs import (
    write_qr_field_stats_json,
    write_quirkrecs_json,
)
from pydiff_mm.diff_mm_diffs_description import get1 as get_diff_description
from pyauthor_util.proposed import proposed
from pycmn.my_utils import sl_map
from pycmn import hebrew_points as hpo


def prep_quirkrecs(jobn_rel_top, json_outdir):
    qrs_5 = sorted(QUIRKRECS, key=_sort_key)
    qrs_6 = sl_map((_add_auto_imgs, jobn_rel_top), qrs_5)
    qrs_7 = sl_map(_add_nbd, qrs_6)
    qrs_8 = sl_map(_add_pgroup, qrs_7)
    qrs_8b = sl_map(_add_auto_diff, qrs_8)
    qrs_9 = sl_map(flatten_strings_in_one_qr, qrs_8b)
    _assert_lc_img_fields_filled(qrs_9)
    write_qr_field_stats_json(
        qrs_9,
        f"{json_outdir}/qr-field-stats-ordered-by-count.json",
        f"{json_outdir}/qr-field-stats-ordered-by-field-name.json",
    )
    write_quirkrecs_json(qrs_9, f"{json_outdir}/quirkrecs.json")
    return qrs_9


def _add_nbd(quirkrec):
    return {**quirkrec, "nbd": nb_dict(quirkrec)}


def _add_pgroup(quirkrec):
    return {**quirkrec, "pgroup": get_pgroup(quirkrec)}


_CGJ = "\u034F"  # combining grapheme joiner
_METEG = hpo.MTGOSLQ


def _add_auto_diff(quirkrec):
    pro = proposed(quirkrec).replace(_CGJ, "")
    consensus = quirkrec.get("qr-intermediate", quirkrec["qr-consensus"]).replace(_CGJ, "")
    if quirkrec.get("qr-ignore-g3yh-diff"):
        pro, consensus = _strip_g3yh_meteg(pro, consensus)
    auto_diff = get_diff_description(consensus, pro)
    return {**quirkrec, "qr-auto-diff": auto_diff}


def _strip_g3yh_meteg(pro, consensus):
    pro_count = pro.count(_METEG)
    con_count = consensus.count(_METEG)
    assert (pro_count, con_count) in ((1, 0), (0, 1)), (
        f"Expected exactly one meteg in exactly one of proposed/consensus, "
        f"got pro={pro_count}, con={con_count}"
    )
    return pro.replace(_METEG, ""), consensus.replace(_METEG, "")


def _add_auto_imgs(jobn_rel_top, quirkrec):
    out = {**quirkrec, **get_auto_imgs(jobn_rel_top, quirkrec)}
    #
    lc_img_name = out["qr-lc-img"]
    lc_img_path = f"{jobn_rel_top}/img/{lc_img_name}"
    assert os.path.exists(lc_img_path), f"Missing LC image: {lc_img_path}"
    #
    for field, _ in _INFO_ABOUT_OPTIONAL_IMAGES:
        if opt_img_name := out.get(field):
            opt_path = f"{jobn_rel_top}/img/{opt_img_name}"
            assert os.path.exists(opt_path), f"Missing optional image: {opt_path}"
    #
    return out


def _assert_lc_img_fields_filled(qrs):
    for qr in qrs:
        assert qr.get("qr-lc-img"), f"Missing qr-lc-img for {short_id(qr)}"


def _sort_key(quirkrec):
    return short_id(quirkrec)
