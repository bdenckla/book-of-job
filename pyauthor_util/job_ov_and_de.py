""" Exports:
        make_ov_and_de_for_all_quirkrecs
        make_example_row
        row_id
"""

from py import my_html
from pycmn import my_utils
from pycmn.my_utils import intersperse, sl_map
from pyauthor_util.common_titles_etc import D1D_FNAME
from pyauthor_util import author
from pyauthor_util.says import says
from pyauthor_util.short_id_etc import short_id
from pyauthor_util.job1_highlight import highlight, color
from pyauthor_util.job1_lcloc import lcloc
from py_uxlc_loc import my_uxlc_location
from py_uxlc_loc import my_tanakh_book_names as py_uxlc_loc_tbn


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
    hlcp = color("μL-proposed", "qr-lc-proposed")
    hcon = color("consensus", "qr-consensus")
    lcp_and_con = [hlcp, my_html.line_break(), hcon]
    return my_html.table_row(
        [
            my_html.table_datum(lcp_and_con),
            my_html.table_datum("# c:v"),
            my_html.table_datum("how μL-proposed differs from consensus"),
        ]
    )


def row_id(quirkrec):
    return f"row-{short_id(quirkrec)}"


def _duplicates(seq):
    seen = set()
    dups = set()
    for item in seq:
        if item in seen:
            dups.add(item)
        else:
            seen.add(item)
    return dups


def _make_one_ov_and_de(uxlc, pbi, quirkrec):
    std_bcvp_quad = _std_bcvp_quad(quirkrec)
    pg_dict = my_uxlc_location.page_and_guesses(uxlc, pbi, std_bcvp_quad)
    pg_diff = _pg_diff(pg_dict, quirkrec["qr-lc-loc"])
    if pg_diff is not None:
        ri = row_id(quirkrec)
        print(ri, pg_diff)
        print(ri, pg_dict)
        print(ri, quirkrec["qr-lc-loc"])
    return {
        "od-overview": _make_overview_row(quirkrec),
        "od-details": _make_details_html(quirkrec),
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
        return (
            "fline mismatch: pg_dict fline-guess"
            + f" {pg_dict['fline-guess']} vs lc_loc fline {fline}"
        )
    return None


def _std_bcvp_quad(quirkrec):
    cn_colon_vn = quirkrec["qr-cv"]
    upwv = quirkrec.get("qr-uxlc-position-within-verse")
    pwv = upwv or 1  # use the position within verse if available, else 1
    bkid = py_uxlc_loc_tbn.BK_JOB
    chnu_str, vrnu_str = cn_colon_vn.split(":")
    chnu = int(chnu_str)
    vrnu = int(vrnu_str)
    atnu = pwv  # atom number within verse
    return bkid, chnu, vrnu, atnu


def _key_for_proposed(quirkrec):
    lcp = quirkrec.get("qr-lc-proposed")
    acp = quirkrec.get("qr-ac-proposed")
    assert not (lcp and acp), "Both qr-lc-proposed and qr-ac-proposed are set!"
    if lcp:
        return "qr-lc-proposed"
    if acp:
        return "qr-ac-proposed"
    assert False, f"Neither qr-lc-proposed nor qr-ac-proposed is set! {quirkrec}"


def _lcp_and_con(quirkrec):
    hlcp = highlight(quirkrec, _key_for_proposed(quirkrec))
    hcon = highlight(quirkrec, "qr-consensus")
    if lc_q := quirkrec.get("qr-lc-q"):
        assert lc_q == "(?)"
        lc_and_q = [hlcp, " (?)"]
    else:
        lc_and_q = [hlcp]
    lcp_and_con = [*lc_and_q, my_html.line_break(), hcon]
    return lcp_and_con


def _make_overview_row(quirkrec):
    hbo_rtl = {"lang": "hbo", "dir": "rtl"}
    nowrap = {"style": "text-wrap: nowrap"}
    td1_attrs = {**hbo_rtl, **nowrap, **_els(quirkrec)}
    the_row_id = row_id(quirkrec)
    anc = my_html.anchor_h("#", f"{D1D_FNAME}#{the_row_id}")  # self-anchor
    tr_contents = [
        my_html.table_datum(_lcp_and_con(quirkrec), td1_attrs),
        my_html.table_datum([anc, " ", quirkrec["qr-cv"]]),
        author.table_datum(_what_is_weird(quirkrec)),
    ]
    tr_attrs = {"id": the_row_id}
    return my_html.table_row(tr_contents, tr_attrs)


def _what_is_weird(quirkrec):
    wiw_in_mu_ell = [quirkrec["qr-what-is-weird"], " in μL,"]
    parts = [wiw_in_mu_ell, *says(quirkrec)]
    wiw_and_says = intersperse(my_html.line_break(), parts)
    return wiw_and_says


def _els(quirkrec):
    if quirkrec.get("qr-extra-letter-spacing"):
        return {"class": "extra-letter-spacing"}
    return {}


def _img(img):
    return author.para_for_img(img, "maxwidth50pc")


_MI_ARGS = {
    "mi-args-aleppo": [
        "μA (Aleppo)",
        "aleppo-img-intro",
        "qr-aleppo-img",
    ],
    "mi-args-cam1753": [
        "μY (Cambridge 1753)",
        "qr-cam1753-img-intro",
        "qr-cam1753-img",
    ],
}


def _maybe_img(quirkrec, mi_args):
    ms_name, iikey, ipkey = _MI_ARGS[mi_args]
    maybe_img_path = quirkrec.get(ipkey)
    if maybe_img_path is None:
        return []
    if maybe_img_intro := quirkrec.get(iikey):
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


def _maybe_inline(yyycom):
    return [] if yyycom is None else [yyycom]


def _maybe_para(yyycom):
    return [] if yyycom is None else [_ensure_lop(yyycom)]


def _ensure_lop(yyycom):
    """lop: list of paras"""
    return yyycom if _is_lop(yyycom) else [author.para(yyycom)]


def _ancs(quirkrec):
    cv = quirkrec["qr-cv"]
    uxlc_href = f"https://tanach.us/Tanach.xml?Job{cv}"
    uxlc_anc = my_html.anchor_h("U", uxlc_href)
    cn_v_vn = "c" + cv.replace(":", "v")
    mwd_href = f"https://bdenckla.github.io/MAM-with-doc/D3-Job.html#{cn_v_vn}"
    mwd_anc = my_html.anchor_h("M", mwd_href)
    return uxlc_anc, mwd_anc


def _dpe(quirkrec):
    fn = _dpe_stretched if _use_stretched_format(quirkrec) else _dpe_inline
    return fn(quirkrec)


def _use_stretched_format(quirkrec):
    gencom = quirkrec.get("qr-generic-comment")
    bhqcom = quirkrec.get("qr-bhq-comment")
    return _is_lop(gencom) or _is_lop(bhqcom)


def _is_lop(yyycom):
    """lop: list of paras"""
    if yyycom is None or isinstance(yyycom, str):
        return False
    assert isinstance(yyycom, list)
    el0 = yyycom[0]
    return my_html.is_htel(el0) and my_html.htel_get_tag(el0) == "p"


def _dpe_inline(quirkrec):
    dpe1 = [
        *_maybe_inline(quirkrec.get("qr-generic-comment")),
        *_maybe_inline(quirkrec.get("qr-bhq-comment")),
        *_ancs_and_loc(quirkrec),
    ]
    return _parasperse(dpe1)


def _dpe_stretched(quirkrec):
    return [
        *_maybe_para(quirkrec.get("qr-generic-comment")),
        *_maybe_para(quirkrec.get("qr-bhq-comment")),
        _parasperse(_ancs_and_loc(quirkrec)),
    ]


def _parasperse(items):
    return author.para(my_utils.intersperse(_SEP, items))


def _ancs_and_loc(quirkrec):
    uxlc_anc, mwd_anc = _ancs(quirkrec)
    return [
        uxlc_anc,
        mwd_anc,
        lcloc(quirkrec.get("qr-lc-loc")),
    ]


def _make_details_html(quirkrec):
    return [
        author.table_c(_make_overview_row(quirkrec)),
        *_maybe_bhq(quirkrec.get("qr-bhq")),
        _dpe(quirkrec),
        _img(quirkrec["qr-lc-img"]),
        *_maybe_img(quirkrec, "mi-args-aleppo"),
        *_maybe_img(quirkrec, "mi-args-cam1753"),
        my_html.horizontal_rule(),
    ]
