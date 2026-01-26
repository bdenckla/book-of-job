""" Exports:
        make_ov_and_de_for_all_quirkrecs
        make_example_row
        row_id
"""

from py import my_html
from pyauthor.common import D1D_FNAME
from pyauthor_util import author
from pyauthor_util.short_id_etc import lc_img
from pyauthor_util.short_id_etc import short_id
from pyauthor_util.job1_highlight import highlight, color
from pyauthor_util.job1_lcloc import lcloc
from pycmn import my_utils
from pycmn.my_utils import sl_map
from py_uxlc_loc import my_uxlc_location
from py_uxlc_loc import my_tanakh_book_names as py_uxlc_loc_tbn


_CSNBPR = "comment-should-not-be-para-wrapped"


def make_ov_and_de(quirkrecs):
    ids = sl_map(row_id, quirkrecs)
    dups = _duplicates(ids)
    assert not dups, f"Duplicate row IDs found: {dups}"
    paths_dict = {
        "path_to_uxlc": "py_uxlc_loc/UXLC",
        "path_to_lci_recs": "py_uxlc_loc/UXLC-misc/lci_recs.json",
    }
    uxlc, pbi = my_uxlc_location.prep(paths_dict)
    ovdes = sl_map((_make_one_ov_and_de, uxlc, pbi), quirkrecs)
    return dict(zip(ids, ovdes))


def make_example_row():
    hlc = color("μL-proposed", "lc")
    hmam = color("consensus", "mam")
    lc_and_mam = [hlc, my_html.line_break(), hmam]
    return my_html.table_row(
        [
            my_html.table_datum(lc_and_mam),
            my_html.table_datum("# c:v"),
            my_html.table_datum("how μL-proposed differs from consensus"),
        ]
    )


def row_id(record):
    return f"row-{short_id(record)}"


def sort_key(record):
    return short_id(record)


def _duplicates(seq):
    seen = set()
    dups = set()
    for item in seq:
        if item in seen:
            dups.add(item)
        else:
            seen.add(item)
    return dups


def _make_one_ov_and_de(uxlc, pbi, record):
    std_bcvp_quad = _std_bcvp_quad(record)
    pg_dict = my_uxlc_location.page_and_guesses(uxlc, pbi, std_bcvp_quad)
    pg_diff = _pg_diff(pg_dict, record["lc-loc"])
    if pg_diff is not None:
        ri = row_id(record)
        print(ri, pg_diff)
        print(ri, pg_dict)
        print(ri, record["lc-loc"])
    return {
        "od-overview": _make_overview_row(record),
        "od-details": _make_details_html(record),
    }


def _pg_diff(pg_dict, lc_loc):
    if pg_dict["page"] != lc_loc["page"]:
        return f"Page mismatch: pg_dict page {pg_dict['page']} vs lc_loc page {lc_loc['page']}"
    lcl = lc_loc["line"]
    if lcl < 1:
        assert lcl != 0
        pline = 27 + (lcl + 1)
    else:
        pline = lcl
    fline = pline + 27 * (lc_loc["column"] - 1)
    flg = float(pg_dict["fline-guess"])
    balm = 2  # biggest acceptable line mismatch
    if abs(flg - fline) > balm:
        return f"fline mismatch: pg_dict fline-guess {pg_dict['fline-guess']} vs lc_loc fline {fline}"
    return None


def _std_bcvp_quad(record):
    cn_colon_vn = record["cv"]
    upwv = record.get("uxlc-position-within-verse")
    pwv = upwv or 1  # use the position within verse if available, else 1
    bkid = py_uxlc_loc_tbn.BK_JOB
    chnu_str, vrnu_str = cn_colon_vn.split(":")
    chnu = int(chnu_str)
    vrnu = int(vrnu_str)
    atnu = pwv  # atom number within verse
    return bkid, chnu, vrnu, atnu


def _lc_and_mam(record):
    hlc = highlight(record, "lc")
    hmam = highlight(record, "mam")
    if lc_q := record.get("lc-q"):
        assert lc_q == "(?)"
        lc_and_q = [hlc, " (?)"]
    else:
        lc_and_q = [hlc]
    lc_and_mam = [*lc_and_q, my_html.line_break(), hmam]
    return lc_and_mam


def _make_overview_row(record):
    hbo_attrs = {"lang": "hbo", "dir": "rtl"}
    the_row_id = row_id(record)
    anc = my_html.anchor_h("#", f"{D1D_FNAME}#{the_row_id}")  # self-anchor
    tr_contents = [
        my_html.table_datum(_lc_and_mam(record), hbo_attrs),
        my_html.table_datum([anc, " ", record["cv"]]),
        author.table_datum(record["what-is-weird"]),
    ]
    tr_attrs = {"id": the_row_id}
    return my_html.table_row(tr_contents, tr_attrs)


def _img(img):
    return author.para_for_img(img, "maxwidth50pc")


_MI_ARGS = {
    "mi-args-aleppo": [
        "μA (Aleppo)",
        "aleppo-img-intro",
        "aleppo-img",
    ],
    "mi-args-cam1753": [
        "μY (Cambridge 1753)",
        "cam1753-img-intro",
        "cam1753-img",
    ],
}


def _maybe_img(record, mi_args):
    ms_name, iikey, ipkey = _MI_ARGS[mi_args]
    maybe_img_path = record.get(ipkey)
    if maybe_img_path is None:
        return []
    if maybe_img_intro := record.get(iikey):
        intro = [" (", maybe_img_intro, ")"]
    else:
        intro = []
    cpara = [ms_name, *intro, ":"]
    return [author.para(cpara), _img(maybe_img_path)]


def _maybe_bhq(bhq):
    if bhq is None:
        return []
    cont_p = ["BHQ: ", author.hbo(bhq)]
    return [author.para_cc(cont_p)]


_SEP = " \N{EM DASH} "


def _maybe_comment(record):
    if comment := record.get("comment"):
        return [comment]
    return []


def _maybe_para_comment(record):
    if comment := record.get("comment"):
        if record.get(_CSNBPR):
            return [comment]
        return [author.para(comment)]
    return []


def _ancs(record):
    cv = record["cv"]
    uxlc_href = f"https://tanach.us/Tanach.xml?Job{cv}"
    uxlc_anc = my_html.anchor_h("U", uxlc_href)
    cn_v_vn = "c" + cv.replace(":", "v")
    mwd_href = f"https://bdenckla.github.io/MAM-with-doc/D3-Job.html#{cn_v_vn}"
    mwd_anc = my_html.anchor_h("M", mwd_href)
    return uxlc_anc, mwd_anc


def _use_stretched(record):
    return record.get("use-stretched-format") or record.get(_CSNBPR)


def _dpe(record):
    fn = _dpe_stretched if record.get("use-stretched-format") else _dpe_inline
    return fn(record)


def _dpe_inline(record):
    dpe1 = [
        *_maybe_comment(record),
        record["bhq-comment"],
        *_ancs_and_loc(record),
    ]
    return _parasperse(dpe1)


def _dpe_stretched(record):
    return [
        *_maybe_para_comment(record),
        author.para(record["bhq-comment"]),
        _parasperse(_ancs_and_loc(record)),
    ]


def _parasperse(items):
    return author.para(my_utils.intersperse(_SEP, items))


def _ancs_and_loc(record):
    uxlc_anc, mwd_anc = _ancs(record)
    return [
        uxlc_anc,
        mwd_anc,
        lcloc(record.get("lc-loc")),
    ]


def _make_details_html(record):
    return [
        author.table_c(_make_overview_row(record)),
        *_maybe_bhq(record.get("bhq")),
        _dpe(record),
        _img(lc_img(record)),
        *_maybe_img(record, "mi-args-aleppo"),
        *_maybe_img(record, "mi-args-cam1753"),
        my_html.horizontal_rule(),
    ]
