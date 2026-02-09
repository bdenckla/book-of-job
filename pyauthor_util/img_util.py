import os
from pyauthor_util.noted_by import x_uclc
from pyauthor_util.short_id_etc import short_id


def lc_img(quirkrec):
    use_png = x_uclc(quirkrec)
    ext = ".png" if use_png else ".jpg"
    return quirkrec.get("qr-lc-img") or f"{short_id(quirkrec)}{ext}"


_INFO_ABOUT_OPTIONAL_IMAGES = [
    ("qr-aleppo-img", "Aleppo-CCVV.png"),
    ("qr-cam1753-img", "Cam1753-CCVV.png"),
    ("qr-jc-img", "Jerusalem-Crown-CCVV.png"),
]


def get_auto_imgs(jobn_rel_top, quirkrec):
    """Auto-detect LC, Aleppo, and Cam1753 images if files exist on disk."""
    out = {}
    sid = short_id(quirkrec)
    # Auto-detect LC image (using lc_img function which handles extension)
    if not quirkrec.get("qr-lc-img"):
        out["qr-lc-img"] = lc_img(quirkrec)
    # Auto-detect Aleppo, Cam1753, and other optional images
    for field, example_filename in _INFO_ABOUT_OPTIONAL_IMAGES:
        if quirkrec.get(field):
            continue  # Already explicitly set
        auto_img = example_filename.replace("-CCVV.png", f"-{sid}.png")
        auto_path = f"{jobn_rel_top}/img/{auto_img}"
        if os.path.exists(auto_path):
            out[field] = auto_img
    return out
