from pycmn.shrink import shrink
from pycmn.my_utils import sl_map
from py import my_html


def flatten_qrs(qrs):
    return sl_map(_flatten_one_qr, qrs)


def _flatten_one_qr(quirkrec):
    gencom = quirkrec.get("qr-generic-comment")
    bhqcom = quirkrec.get("qr-bhq-comment")
    flat_gencom = gencom and _flatten_yyycom(gencom)
    flat_bhqcom = bhqcom and _flatten_yyycom(bhqcom)
    new_gencom = {"qr-generic-comment": flat_gencom} if flat_gencom else {}
    new_bhqcom = {"qr-bhq-comment": flat_bhqcom} if flat_bhqcom else {}
    return {**quirkrec, **new_gencom, **new_bhqcom}


def _flatten_yyycom(yyycom):
    if isinstance(yyycom, str):
        return yyycom
    assert isinstance(yyycom, list)
    if all(isinstance(item, str) for item in yyycom):
        flat = my_html.flatten(yyycom)
        return shrink(flat)
    return yyycom
