import os
from pyauthor_util.add_auto_diff import _enrich_one_qr_by_adding_auto_diff
from pyauthor_util.flatten_qrs import _enrich_one_qr_by_flattening_strs
from pyauthor_util.img_util import _INFO_ABOUT_OPTIONAL_IMAGES, get_auto_imgs
from pyauthor_util.short_id_etc import short_id
from pyauthor_util.noted_by import nb_dict
from pyauthor_util.get_qr_groups import get_pgroup
from pyauthor_util.job_quirkrecs import RAW_QUIRKRECS
from pyauthor_util.qr_make_json_outputs import (
    write_qr_field_stats_json,
    write_enriched_quirkrecs_json,
)
from pycmn.my_utils import sl_map


def get_enriched_quirkrecs(jobn_rel_top, json_outdir):
    """Run the full raw → enriched quirkrec pipeline and write outputs.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root
            (used to locate image files on disk).
        json_outdir: directory path for writing enriched-quirkrecs.json
            and field-stats JSON files.

    Returns:
        List of fully-enriched quirkrec dicts.
    """
    eqrs = _enrich_quirkrecs(jobn_rel_top)
    write_qr_field_stats_json(
        eqrs,
        f"{json_outdir}/qr-field-stats-ordered-by-count.json",
        f"{json_outdir}/qr-field-stats-ordered-by-field-name.json",
    )
    write_enriched_quirkrecs_json(eqrs, f"{json_outdir}/enriched-quirkrecs.json")
    return eqrs


def _enrich_quirkrecs(jobn_rel_top):
    _assert_cv_ordering(RAW_QUIRKRECS)
    result = sl_map((_do_pointwise_enrichments_of_one_qr, jobn_rel_top), RAW_QUIRKRECS)
    return result


def _do_pointwise_enrichments_of_one_qr(jobn_rel_top, pe_quirkrec):
    """Apply all per-quirkrec enrichments that don't need cross-quirkrec context.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root
            (used to locate image files on disk).
        pe_quirkrec: raw quirkrec dict (qr-word-id is already present
            for multi-record verses, hard-coded in the source file).
    """
    result = _enrich_one_qr_by_adding_auto_imgs(jobn_rel_top, pe_quirkrec)
    result = _enrich_one_qr_by_adding_aleppo_intro(result)
    result = _enrich_one_qr_by_adding_nbd(result)
    result = _enrich_one_qr_by_adding_pgroup(result)
    result = _enrich_one_qr_by_adding_auto_diff(result)
    result = _enrich_one_qr_by_flattening_strs(result)
    _assert_lc_img_fields_filled(result)
    return result


def _enrich_one_qr_by_adding_aleppo_intro(quirkrec):
    """Add aleppo-img-intro from the static qr-ac-loc field, if present."""
    ac_loc = quirkrec.get("qr-ac-loc")
    if ac_loc is None:
        return quirkrec
    intro = (
        f"page {ac_loc['page']}, col {ac_loc['column']}, "
        f"line {ac_loc['line']}, word {ac_loc['word']}"
    )
    return {**quirkrec, "aleppo-img-intro": intro}


def _enrich_one_qr_by_adding_nbd(quirkrec):
    """Add the noted-by dict (nbd) to a quirkrec."""
    return {**quirkrec, "nbd": nb_dict(quirkrec)}


def _enrich_one_qr_by_adding_pgroup(quirkrec):
    """Add the presentation group key to a quirkrec."""
    return {**quirkrec, "pgroup": get_pgroup(quirkrec)}


def _enrich_one_qr_by_adding_auto_imgs(jobn_rel_top, quirkrec):
    """Add auto-detected image fields and assert all required images exist.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root.
        quirkrec: partially-enriched quirkrec dict.
    """
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


def _cv_key(quirkrec):
    ch, vr = (int(x) for x in quirkrec["qr-cv"].split(":"))
    return (ch, vr)


def _assert_cv_ordering(raw_quirkrecs):
    for i in range(1, len(raw_quirkrecs)):
        prev = _cv_key(raw_quirkrecs[i - 1])
        curr = _cv_key(raw_quirkrecs[i])
        assert prev <= curr, (
            f"RAW_QUIRKRECS not in chapter-verse order: "
            f"{raw_quirkrecs[i-1]['qr-cv']} > {raw_quirkrecs[i]['qr-cv']} "
            f"at index {i}"
        )
