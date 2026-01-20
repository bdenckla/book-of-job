""" Exports:
        make_ov_and_de_for_all_quirkrecs
        make_example_row
        row_id
"""

from py import my_html
from pyauthor.common import D1D_FNAME
from pyauthor_util import author
from pyauthor_util.job1_highlight import highlight, color
from pyauthor_util.job1_lcloc import lcloc
from pycmn.my_utils import sl_map


def make_ov_and_de_for_all_quirkrecs(quirkrecs):
    ids = sl_map(row_id, quirkrecs)
    assert _unique(ids)
    ovdes = sl_map(_make_ov_and_de_for_one_record, quirkrecs)
    return dict(zip(ids, ovdes))


def make_example_row():
    hlc = color("μL", "lc")
    hmam = color("consensus", "mam")
    lc_and_mam = [hlc, my_html.line_break(), hmam]
    return my_html.table_row(
        [
            my_html.table_datum("#"),
            my_html.table_datum(lc_and_mam),
            my_html.table_datum("c:v"),
            my_html.table_datum("how μL differs from consensus"),
        ]
    )


def row_id(record):
    cn_v_vn = record["cv"].replace(":", "v")  # E.g. 1:2 becomes 1v2
    ftv = record.get("n_of_m_for_this_verse")
    ftv_str = f"-{ftv[0]}of{ftv[1]}ftv" if ftv else ""  # E.g. -1of2ftv
    return f"row-{cn_v_vn}{ftv_str}"


def sort_key(record):
    cv_as_toi = tuple(int(part) for part in record["cv"].split(":"))
    ftv = record.get("n_of_m_for_this_verse")
    ftv0 = ftv[0] if ftv else 1
    return *cv_as_toi, ftv0


def _unique(seq):
    return len(set(seq)) == len(seq)


def _make_ov_and_de_for_one_record(record):
    return {
        "od-overview": _make_overview_row(record),
        "od-details": _make_details_row(record),
    }


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
        my_html.table_datum(anc),
        my_html.table_datum(_lc_and_mam(record), hbo_attrs),
        my_html.table_datum(record["cv"]),
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
    return [my_html.para(cont_p)]


_DEFAULT_BHQ_COMMENT = "$BHQ agrees with μL here, but $BHQ makes no note of μL’s divergence from consensus."
_SEP = " \N{EM DASH} "


def _maybe_sep_comment(record):
    if comment := record.get("comment"):
        return [_SEP, comment]
    return []


def _sep_bhq_comment(record):
    bhq_comment = record.get("bhq-comment") or _DEFAULT_BHQ_COMMENT
    return [_SEP, bhq_comment]


def _make_details_row(record):
    cv = record["cv"]
    uxlc_href = f"https://tanach.us/Tanach.xml?Job{cv}"
    uxlc_anc = my_html.anchor_h("UXLC", uxlc_href)
    cn_v_vn = "c" + cv.replace(":", "v")
    mwd_href = f"https://bdenckla.github.io/MAM-with-doc/D3-Job.html#{cn_v_vn}"
    mwd_anc = my_html.anchor_h("MwD", mwd_href)
    dpe = [
        uxlc_anc,
        _SEP,
        mwd_anc,
        _SEP,
        *lcloc(record.get("lc-loc")),
        *_maybe_sep_comment(record),
        *_sep_bhq_comment(record),
    ]
    return [
        author.table_c(_make_overview_row(record)),
        *_maybe_bhq(record.get("bhq")),
        author.para(dpe),
        _img(record["lc-img"]),
        *_maybe_img(record, "mi-args-aleppo"),
        *_maybe_img(record, "mi-args-cam1753"),
        my_html.horizontal_rule(),
    ]
