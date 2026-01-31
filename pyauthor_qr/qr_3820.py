from pyauthor_util.uxlc_change import uxlc_change


RECORD_3820 = {
    "qr-cv": "38:20",
    "qr-lc-proposed": "תָ֝בִין",
    "qr-what-is-weird": "ב lacks רביע",
    "qr-consensus": "תָ֝בִ֗ין",
    "qr-generic-comment": [
        "The only mark above the ב is a רפה.",
    ],
    "qr-lc-img": "3820-custom.png",
    # Above, we use our own screen snip (a .png) rather than one taken
    # from the UXLC change record (a .jpg), which is what we do in all other cases.
    "qr-highlight": 2,
    "qr-lc-loc": {"page": "408A", "column": 1, "line": 24},
    "qr-noted-by": "tBHQ-xBHL-xDM-xWLC-nUXLC",
    "qr-uxlc-change-url": uxlc_change("2023.10.19", "2023.06.10-45"),
}
