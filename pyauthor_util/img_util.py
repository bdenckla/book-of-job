import os
from pyauthor_util.short_id_etc import short_id

_INFO_ABOUT_OPTIONAL_IMAGES = [
    ("qr-aleppo-img", "Aleppo-CCVV.png"),
    ("qr-cam1753-img", "cam1753-CCVV.png"),
    ("qr-jc-img", "Jerusalem-Crown-CCVV.png"),
]


def get_auto_imgs(jobn_rel_top, quirkrec):
    """Auto-detect LC, Aleppo, and Cam1753 images if files exist on disk.

    Args:
        jobn_rel_top: path to the jobn directory, relative to repo root.
        quirkrec: quirkrec dict (must have at least qr-cv; qr-word-id
            is used if present to form the short ID).

    Returns:
        Dict of image-field keys (e.g. "qr-lc-img", "qr-aleppo-img")
        mapped to filename strings, for images that exist on disk.
    """
    out = {}
    sid = short_id(quirkrec)
    out["qr-lc-img"] = f"{sid}.png"
    # Auto-detect Aleppo, Cam1753, and other optional images
    for field, example_filename in _INFO_ABOUT_OPTIONAL_IMAGES:
        auto_img = example_filename.replace("-CCVV.png", f"-{sid}.png")
        auto_path = f"{jobn_rel_top}/img/{auto_img}"
        if os.path.exists(auto_path):
            out[field] = auto_img
    return out
