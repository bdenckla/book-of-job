import os
from collections import Counter
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
from py_ac_word_image_helper.codex_page import find_page_for_verse, load_index
from py_ac_word_image_helper.linebreak_search import find_word_in_linebreaks
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
    result = _enrich_quirkrecs_by_adding_word_ids(RAW_QUIRKRECS)
    # Adding word IDs is not pointwise: it requires the whole set
    # of quirkrecs (to detect same-verse duplicates). It also must
    # precede the pointwise pass, since auto-imgs use word IDs in
    # their filenames.
    pages = load_index()
    result = sl_map(
        (_do_pointwise_enrichments_of_one_qr, jobn_rel_top, pages), result
    )
    return result


def _do_pointwise_enrichments_of_one_qr(jobn_rel_top, pages, pe_quirkrec):
    """Apply all per-quirkrec enrichments that don't need cross-quirkrec context.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root
            (used to locate image files on disk).
        pages: page index from load_index() (for Aleppo location lookup).
        pe_quirkrec: partially-enriched quirkrec dict (word ID already
            added, but no other enrichments yet).
    """
    result = _enrich_one_qr_by_adding_auto_imgs(jobn_rel_top, pe_quirkrec)
    result = _enrich_one_qr_by_adding_aleppo_loc(pages, result)
    result = _enrich_one_qr_by_adding_nbd(result)
    result = _enrich_one_qr_by_adding_pgroup(result)
    result = _enrich_one_qr_by_adding_auto_diff(result)
    result = _enrich_one_qr_by_flattening_strs(result)
    _assert_lc_img_fields_filled(result)
    return result


def _enrich_one_qr_by_adding_aleppo_loc(pages, quirkrec):
    """Add aleppo-img-intro with manuscript location if an Aleppo image exists."""
    if "qr-aleppo-img" not in quirkrec:
        return quirkrec
    cv = quirkrec["qr-cv"]
    ch, v = (int(x) for x in cv.split(":"))
    page_id = find_page_for_verse(pages, ch, v)
    if page_id is None:
        return quirkrec
    consensus = quirkrec["qr-consensus"]
    lb_word = quirkrec.get("qr-consensus-ketiv", consensus)
    col, line_num, word_idx, _line_words = find_word_in_linebreaks(
        page_id, ch, v, lb_word
    )
    if col is None:
        return quirkrec
    intro = f"page {page_id}, col {col}, line {line_num}, word {word_idx + 1}"
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


def _enrich_quirkrecs_by_adding_word_ids(raw_quirkrecs):
    """Add qr-word-id to quirkrecs that share a verse with another quirkrec.

    Args:
        raw_quirkrecs: list of raw quirkrec dicts (no enrichments yet).

    Returns:
        New list of quirkrec dicts, where same-verse quirkrecs gain a
        qr-word-id field derived from their consensus string.
    """
    by_cv = {}
    for qr in raw_quirkrecs:
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
