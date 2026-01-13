""" Exports make_per_case_data, make_example_row """

from py import my_html
from pyauthor_util import author
from pyauthor_util.job1_highlight import highlight, color
from pyauthor_util.job1_lcloc import lcloc


def make_per_case_data(record):
    return {
        "row": _make_row(record),
        "details": _make_details(record),
    }


def make_example_row():
    hbhla = color("BHL-A", "bhla")
    hmam = color("consensus", "mam")
    bhla_and_mam = [hbhla, my_html.line_break(), hmam]
    return my_html.table_row(
        [
            my_html.table_datum(bhla_and_mam),
            my_html.table_datum("c:v"),
            my_html.table_datum("how BHL-A differs from consensus"),
        ]
    )


def _make_row(record):
    hbhla = highlight(record, "bhla")
    hmam = highlight(record, "mam")
    if blha_q := record["bhla-q"]:
        assert blha_q == "(?)"
        bhla_and_q = [hbhla, " (?)"]
    else:
        bhla_and_q = [hbhla]
    bhla_and_mam = [*bhla_and_q, my_html.line_break(), hmam]
    hbo_attrs = {"lang": "hbo", "dir": "rtl"}
    return my_html.table_row(
        [
            # str(record["bhla-i"]),
            my_html.table_datum(bhla_and_mam, hbo_attrs),
            my_html.table_datum(record["cv"]),
            my_html.table_datum(record["what-is-weird"]),
        ]
    )


def _img(img):
    return my_html.img({"src": f"img/{img}"})


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
        intro = f" ({maybe_img_intro})"
    else:
        intro = ""
    cpara = f"{ms_name}{intro}:"
    return [my_html.para(cpara), _img(maybe_img_path)]


def _maybe_bhq(bhq):
    if bhq is None:
        return []
    cont_p = ["BHQ: ", author.hbo(bhq)]
    return [my_html.para(cont_p)]


_DEFAULT_BHQ_COMMENT = "BHQ agrees with BHL-A here, but BHQ makes no note of μL’s divergence from consensus."


def _make_details(record):
    sep = " \N{EM DASH} "
    cv = record["cv"]
    uxlc_href = f"https://tanach.us/Tanach.xml?Job{cv}"
    uxlc_anc = my_html.anchor_h("UXLC", uxlc_href)
    cnvm = "c" + cv.replace(":", "v")
    mwd_href = f"https://bdenckla.github.io/MAM-with-doc/D3-Job.html#{cnvm}"
    mwd_anc = my_html.anchor_h("MwD", mwd_href)
    dpe = [uxlc_anc, sep, mwd_anc, sep, *lcloc(record.get("lc-loc"))]
    if comment := record["comment"]:
        dpe.append(sep)
        dpe.append(comment)
    bhq_comment = record.get("bhq-comment") or _DEFAULT_BHQ_COMMENT
    dpe.append(sep)
    dpe.append(bhq_comment)
    return [
        author.table_c(_make_row(record)),
        *_maybe_bhq(record.get("bhq")),
        my_html.para(dpe),
        _img(record["lc-img"]),
        *_maybe_img(record, "mi-args-aleppo"),
        *_maybe_img(record, "mi-args-cam1753"),
        my_html.horizontal_rule(),
    ]
