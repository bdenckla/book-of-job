import json
import os
from collections import Counter
from pathlib import Path
from pyauthor_util.add_auto_diff import _enrich_one_qr_by_adding_auto_diff
from pyauthor_util.flatten_qrs import _enrich_one_qr_by_flattening_strs
from pyauthor_util.author import consensus_to_ascii
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

_CAM1753_CROPS_PATH = (
    Path(__file__).resolve().parent.parent / "out" / "cam1753-crops.json"
)


def _load_cam1753_crops():
    """Load cam1753-crops.json if it exists, return dict keyed by SID."""
    if _CAM1753_CROPS_PATH.exists():
        return json.loads(_CAM1753_CROPS_PATH.read_text("utf-8"))
    return {}


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
    _assert_word_ids(RAW_QUIRKRECS)
    cam1753_crops = _load_cam1753_crops()
    result = sl_map(
        (_do_pointwise_enrichments_of_one_qr, jobn_rel_top, cam1753_crops),
        RAW_QUIRKRECS,
    )
    return result


def _do_pointwise_enrichments_of_one_qr(jobn_rel_top, cam1753_crops, pe_quirkrec):
    """Apply all per-quirkrec enrichments that don't need cross-quirkrec context.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root
            (used to locate image files on disk).
        cam1753_crops: dict from cam1753-crops.json keyed by SID.
        pe_quirkrec: raw quirkrec dict (qr-word-id is already present
            for multi-record verses, hard-coded in the source file).
    """
    result = _enrich_one_qr_by_adding_auto_imgs(jobn_rel_top, pe_quirkrec)
    result = _enrich_one_qr_by_adding_cam1753_loc(cam1753_crops, result)
    result = _enrich_one_qr_by_adding_nbd(result)
    result = _enrich_one_qr_by_adding_pgroup(result)
    result = _enrich_one_qr_by_adding_auto_diff(result)
    result = _enrich_one_qr_by_flattening_strs(result)
    _assert_lc_img_fields_filled(result)
    _assert_img_implies_loc(result)
    return result


def _enrich_one_qr_by_adding_cam1753_loc(cam1753_crops, quirkrec):
    """Add qr-cam1753-loc from cam1753-crops.json if available.

    Note the architectural inconsistency: qr-lc-loc and qr-ac-loc are
    hand-authored in each qr_*.py source file, but qr-cam1753-loc is
    computed here from an external JSON file (cam1753-crops.json).
    """
    sid = short_id(quirkrec)
    crop = cam1753_crops.get(sid)
    if crop is None:
        return quirkrec
    loc = {
        "page": crop["page"],
        "column": crop["col"],
    }
    if crop.get("split"):
        parts = crop["parts"]
        loc["line"] = parts[0]["line_num"]
        loc["line2"] = parts[1]["line_num"]
    else:
        loc["line"] = crop["line_num"]
        if crop.get("word_idx") is not None:
            loc["word"] = crop["word_idx"] + 1  # 1-based for display
    return {**quirkrec, "qr-cam1753-loc": loc}


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


# Image key → location key, for each manuscript.
# Note: qr-lc-loc and qr-ac-loc are hand-authored in qr_*.py files and
# pass through enrichment unchanged; qr-cam1753-loc is the odd one out,
# computed during enrichment from cam1753-crops.json (see above).
_IMG_LOC_PAIRS = [
    ("qr-lc-img", "qr-lc-loc"),
    ("qr-aleppo-img", "qr-ac-loc"),
    ("qr-cam1753-img", "qr-cam1753-loc"),
]


def _assert_img_implies_loc(qr):
    """Assert that every manuscript image has a corresponding location."""
    sid = short_id(qr)
    for img_key, loc_key in _IMG_LOC_PAIRS:
        if qr.get(img_key) and not qr.get(loc_key):
            raise AssertionError(f"{sid}: has {img_key} but missing {loc_key}")


def _assert_word_ids(raw_quirkrecs):
    """Assert that hard-coded qr-word-id values match what would be computed.

    Single-record verses must not have qr-word-id.
    Multi-record verses must have qr-word-id matching the value derived
    from consensus_to_ascii (with _N_of_M_FTW suffix when needed).
    """
    by_cv = {}
    for qr in raw_quirkrecs:
        by_cv.setdefault(qr["qr-cv"], []).append(qr)
    for cv, group in by_cv.items():
        if len(group) == 1:
            assert (
                "qr-word-id" not in group[0]
            ), f"{cv}: single-record verse should not have qr-word-id"
            continue
        base_wids = [consensus_to_ascii(qr["qr-consensus"]) for qr in group]
        wid_counts = Counter(base_wids)
        for qr, base_wid in zip(group, base_wids):
            if wid_counts[base_wid] > 1:
                n, m = qr["qr-n_of_m_for_this_word"]
                expected = f"{base_wid}_{n}_of_{m}_FTW"
            else:
                expected = base_wid
            actual = qr.get("qr-word-id")
            assert actual == expected, (
                f"{cv}: qr-word-id mismatch: "
                f"hard-coded {actual!r} != computed {expected!r}"
            )


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
