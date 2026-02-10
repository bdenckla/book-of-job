from py import my_html


def is_lop(obj):
    """lop: list of paras"""
    if obj is None or isinstance(obj, str):
        return False
    assert isinstance(obj, list)
    el0 = obj[0]
    return my_html.is_htel(el0) and my_html.htel_get_tag(el0) == "p"