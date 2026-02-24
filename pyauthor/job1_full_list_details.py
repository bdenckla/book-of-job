"""Generate individual detail HTML files, one per quirkrec."""

import os
from pyauthor_util.common_titles_etc import D1D_DIR
from py import my_html


def gen_html_files(ov_and_de):
    """Write one HTML file per quirkrec into docs/jobn-details/.

    Args:
        ov_and_de: dict mapping row IDs ("row-{SID}") to sub-dicts
            with keys "od-details", "od-quirkrec", etc.
    """
    out_dir = f"docs/{D1D_DIR}"
    os.makedirs(out_dir, exist_ok=True)
    css_href = "../jobn/style.css"
    items = list(ov_and_de.items())
    for idx, (row_key, od) in enumerate(items):
        sid = row_key.removeprefix("row-")
        cv = od["od-quirkrec"]["qr-cv"]
        title = f"Job {cv}"
        prev_sid = items[idx - 1][0].removeprefix("row-") if idx > 0 else None
        next_sid = (
            items[idx + 1][0].removeprefix("row-") if idx < len(items) - 1 else None
        )
        nav = _nav_bar(prev_sid, next_sid)
        body = [*od["od-details"], nav, _nav_key_script(prev_sid, next_sid)]
        out_path = f"{out_dir}/{sid}.html"
        write_ctx = my_html.WriteCtx(title, out_path, css_hrefs=(css_href,))
        my_html.write_html_to_file(body, write_ctx)


def _nav_bar(prev_sid, next_sid):
    """Return a <p> element with prev/next navigation links."""
    parts = []
    if prev_sid is not None:
        parts.append("[p] ")
        parts.append(my_html.anchor_h("← prev", f"{prev_sid}.html"))
    if prev_sid is not None and next_sid is not None:
        parts.append(" \u2003 ")
    if next_sid is not None:
        parts.append(my_html.anchor_h("next →", f"{next_sid}.html"))
        parts.append(" [n]")
    return my_html.para(parts, {"class": "center", "style": "margin-top: 2em"})


def _nav_key_script(prev_sid, next_sid):
    """Return a <script> element for keyboard navigation (p/n keys)."""
    cases = []
    if prev_sid is not None:
        cases.append(f'case "p": location.href = "{prev_sid}.html"; break;')
    if next_sid is not None:
        cases.append(f'case "n": location.href = "{next_sid}.html"; break;')
    js = (
        "document.addEventListener("
        '"keydown", e => {'
        "if (e.target.tagName === "
        '"INPUT" || e.target.tagName === "TEXTAREA") return; '
        "switch (e.key) {" + " ".join(cases) + "}})"
    )
    return my_html.htel_mk("script", flex_contents=(js,))
