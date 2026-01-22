""" Exports highlight and color"""

import re
from py import my_html


def highlight(quirkrec, key):
    zbhls = _zb_highlights(quirkrec, key)  # zero-based highlights
    rk = quirkrec[key]
    clusters = re.findall(r"[א-ת ][^א-ת ]*", rk)
    jc = "".join(clusters)
    assert jc == rk
    out = [cl if i not in zbhls else color(cl, key) for i, cl in enumerate(clusters)]
    return out


def color(text, key):
    color = _RK_COLOR[key]
    return my_html.span(text, {"style": f"color: {color}"})


_RK_COLOR = {
    "lc": "red",
    "mam": "green",
}
_RK_HL_SPECIFIC = {
    "lc": "highlight-lc",
    "mam": "highlight-mam",
}


def _zb_highlights(quirkrec, key):
    hl_both = quirkrec.get("highlight")
    hl_spec = quirkrec.get(_RK_HL_SPECIFIC[key])
    assert (hl_both is None) or (hl_spec is None)
    hl = hl_both or hl_spec
    if hl is None:
        return []
    if isinstance(hl, int):
        return [hl - 1]
    assert isinstance(hl, list)
    return [obi - 1 for obi in hl]
