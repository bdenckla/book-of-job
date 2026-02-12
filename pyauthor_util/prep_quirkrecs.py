import os
from collections import Counter
from pyauthor_util.add_auto_diff import add_auto_diff
from pyauthor_util.author import consensus_to_ascii
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
from pycmn.my_utils import sl_map


def prep_quirkrecs(jobn_rel_top, json_outdir):
    qrs_4 = _add_word_ids(QUIRKRECS)
    qrs_5 = sorted(qrs_4, key=_sort_key)
    qrs_6 = sl_map((_prep_one_quirkrec, jobn_rel_top), qrs_5)
    write_qr_field_stats_json(
        qrs_6,
        f"{json_outdir}/qr-field-stats-ordered-by-count.json",
        f"{json_outdir}/qr-field-stats-ordered-by-field-name.json",
    )
    write_quirkrecs_json(qrs_6, f"{json_outdir}/quirkrecs.json")
    return qrs_6


def _prep_one_quirkrec(jobn_rel_top, quirkrec):
    qr_6 = _add_auto_imgs(jobn_rel_top, quirkrec)
    qr_7 = _add_nbd(qr_6)
    qr_8 = _add_pgroup(qr_7)
    qr_8b = add_auto_diff(qr_8)
    qr_9 = flatten_strings_in_one_qr(qr_8b)
    _assert_lc_img_fields_filled(qr_9)
    return qr_9


def _add_nbd(quirkrec):
    return {**quirkrec, "nbd": nb_dict(quirkrec)}


def _add_pgroup(quirkrec):
    return {**quirkrec, "pgroup": get_pgroup(quirkrec)}


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


def _assert_lc_img_fields_filled(qr):
    assert qr.get("qr-lc-img"), f"Missing qr-lc-img for {short_id(qr)}"


def _add_word_ids(quirkrecs):
    by_cv = {}
    for qr in quirkrecs:
        by_cv.setdefault(qr["qr-cv"], []).append(qr)
    result = []
    for group in by_cv.values():
        if len(group) == 1:
            result.extend(group)
            continue
        base_wids = [consensus_to_ascii(qr["qr-consensus"]) for qr in group]
        wid_counts = Counter(base_wids)
        for qr, base_wid in zip(group, base_wids):
            if wid_counts[base_wid] > 1:
                n, m = qr["qr-n_of_m_for_this_word"]
                wid = f"{base_wid}_{n}_of_{m}_FTW"
            else:
                wid = base_wid
            result.append({**qr, "qr-word-id": wid})
    return result


def _sort_key(quirkrec):
    return short_id(quirkrec)
