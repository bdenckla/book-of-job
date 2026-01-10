""" Exports make_per_case_data """

from py import my_html
from pyauthor.util import author
from pyauthor.job1_highlight import highlight
from pyauthor.job1_lcloc import maybe_sep_lcloc


def make_per_case_data(record):
    return {
        "row": _make_row(record),
        "details": _make_details(record),
    }


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


def _maybe_img(record):
    if img_fname := record.get("img"):
        img_tag = my_html.img({"src": f"img/{img_fname}"})
        return [img_tag]
    return []


def _make_details(record):
    sep = " \N{EM DASH} "
    cv = record["cv"]
    uxlc_href = f"https://tanach.us/Tanach.xml?Job{cv}"
    uxlc_anc = my_html.anchor_h("UXLC", uxlc_href)
    cnvm = "c" + cv.replace(":", "v")
    mwd_href = f"https://bdenckla.github.io/MAM-with-doc/D3-Job.html#{cnvm}"
    mwd_anc = my_html.anchor_h("MwD", mwd_href)
    dpe = [uxlc_anc, sep, mwd_anc, *maybe_sep_lcloc(record, sep)]
    if comment := record["comment"]:
        dpe.append(sep)
        dpe.append(comment)
    details_proper = my_html.para(dpe)
    return [
        author.table_c(_make_row(record)),
        details_proper,
        *_maybe_img(record),
        my_html.horizontal_rule(),
    ]
