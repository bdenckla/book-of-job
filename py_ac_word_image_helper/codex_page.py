"""Aleppo Codex page utilities: index, download, bounding boxes."""

import json
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
LB_DIR = ROOT / "py_ac_loc" / "line-breaks"
CC_DIR = ROOT / "py_ac_loc" / "column-coordinates"
INDEX_PATH = ROOT / "py_ac_loc" / "codex-index" / "index-flat.json"
CACHE_DIR = ROOT / ".novc"


def _leaf_to_page_n(page_id):
    num = int(page_id[:-1])
    side = page_id[-1]
    return (num - 1) * 2 + 2 + (0 if side == "r" else 1)


def image_url(page_id, scale=2):
    n = _leaf_to_page_n(page_id)
    return (
        "https://ia601801.us.archive.org/BookReader/BookReaderImages.php"
        f"?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip"
        f"&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{n:04d}.jp2"
        f"&id=aleppo-codex&scale={scale}&rotate=0"
    )


def load_index():
    """Load page index: returns list of (leaf, ch_start, v_start, ch_end, v_end)."""
    with open(INDEX_PATH, encoding="utf-8") as f:
        data = json.load(f)
    pages = []
    for entry in data["body"]:
        leaf = entry["de_leaf"]
        tr = entry["de_text_range"]
        # tr = [["Job", ch, v], ["Job", ch, v]]
        if tr[0][0] != "Job" and tr[1][0] != "Job":
            continue
        # Start
        if tr[0][0] == "Job":
            ch_s, v_s = tr[0][1], tr[0][2]
        else:
            ch_s, v_s = 1, 1  # Page starts before Job
        # End (exclusive)
        if tr[1][0] == "Job":
            ch_e, v_e = tr[1][1], tr[1][2]
        else:
            ch_e, v_e = 99, 99  # Page extends past Job
        pages.append((leaf, ch_s, v_s, ch_e, v_e))
    return pages


def find_page_for_verse(pages, ch, v):
    """Find which page a verse is on."""
    for leaf, ch_s, v_s, ch_e, v_e in pages:
        start_ok = (ch, v) >= (ch_s, v_s)
        end_ok = (ch, v) < (ch_e, v_e)
        if start_ok and end_ok:
            return leaf
    # Could be the last word of a page (at the boundary)
    for leaf, ch_s, v_s, ch_e, v_e in pages:
        if (ch, v) >= (ch_s, v_s) and (ch, v) <= (ch_e, v_e):
            return leaf
    return None


def get_line_bbox(page_id, col, line_num, buffer_lines=2):
    """Get pixel bounding box for a line, with buffer lines above and below."""
    cc_path = CC_DIR / f"{page_id}.json"
    with open(cc_path, encoding="utf-8") as f:
        cc = json.load(f)

    col_key = f"col{col}"
    col_data = cc["columns"][col_key]["px"]
    img_w = cc["image_size"]["width"]
    img_h = cc["image_size"]["height"]

    x = col_data["x"]
    y = col_data["y"]
    w = col_data["w"]
    ls = col_data["line_spacing"]

    # Target line top and bottom
    line_top = y + (line_num - 1) * ls
    line_bot = line_top + ls

    # Add buffer
    crop_top = max(0, line_top - buffer_lines * ls)
    crop_bot = min(img_h, line_bot + buffer_lines * ls)

    # Expand horizontally a bit beyond the column
    margin_x = int(w * 0.05)
    crop_left = max(0, x - margin_x)
    crop_right = min(img_w, x + w + margin_x)

    return (
        int(crop_left), int(crop_top), int(crop_right), int(crop_bot),
        int(line_top - crop_top),  # target line offset from crop top
        int(ls),  # line spacing in px
    )


def download_page(page_id, scale=2):
    """Download page image from archive.org. Returns PIL Image."""
    url = image_url(page_id, scale=scale)
    cache_path = CACHE_DIR / f"page_cache_{page_id}_s{scale}.jpg"
    if cache_path.exists():
        print(f"  Using cached {cache_path.name}")
        return Image.open(cache_path)
    print(f"  Downloading {page_id} (scale={scale})...")
    data = urlopen(url).read()
    img = Image.open(BytesIO(data))
    img.save(cache_path, "JPEG")
    return img
