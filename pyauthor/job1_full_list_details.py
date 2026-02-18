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
    for row_key, od in ov_and_de.items():
        sid = row_key.removeprefix("row-")
        cv = od["od-quirkrec"]["qr-cv"]
        title = f"Job {cv}"
        out_path = f"{out_dir}/{sid}.html"
        write_ctx = my_html.WriteCtx(title, out_path, css_hrefs=(css_href,))
        my_html.write_html_to_file(od["od-details"], write_ctx)
