import re
from py import my_html
from pycmn.my_utils import sl_map


def dollar_sub_g(dispatch, contents):
    """The parameter "dispatch" is a dict.
    It maps strings like "$tsinnorit" to functions that take no
    arguments and return an HTML element (usually a span)."""
    flat_1 = my_html.flatten(contents)
    assert flat_1 is not None
    return sl_map((_dollar_sub_flat_el, dispatch), flat_1)


def _dollar_sub_flat_el(dispatch, flat_el):
    if isinstance(flat_el, str):
        return _dollar_sub_str(dispatch, flat_el)
    return flat_el


def _dollar_sub_str(dispatch, str):
    parts = re.split("([$][a-zA-Z0-9_]+)", str)
    return sl_map((_dollar_sub_str_part, dispatch), parts)


def _dollar_sub_str_part(dispatch, part):
    return dispatch[part] if part.startswith("$") else part
