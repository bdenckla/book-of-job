import re

from py import my_html
from pycmn.my_utils import sl_map
from pyauthor_util.verse_ref_link import verse_ref_link, verse_ref_link_disambig


def dollar_sub_g(dispatch, contents):
    """Perform dollar-sign substitution on HTML contents.

    Args:
        dispatch: dict mapping dollar-prefixed keys (e.g. "$tsinnorit")
            to zero-argument callables that return an HTML element
            (usually a span).
        contents: HTML content tree (strings and nested lists) to
            process.
    """
    flat_1 = my_html.flatten(contents)
    assert flat_1 is not None
    _check_no_undollared(dispatch, flat_1)
    return sl_map((_dollar_sub_flat_el, dispatch), flat_1)


def _check_no_undollared(dispatch, flat_list):
    """Check that un-dollared identifiers don’t appear in the input.

    Args:
        dispatch: the dollar-substitution dispatch dict (keys are
            dollar-prefixed strings like "$tsinnorit").
        flat_list: flattened list of strings and HTML elements to scan.
    """
    strings = [el for el in flat_list if isinstance(el, str)]
    full_text = "".join(strings)
    for key in dispatch:
        if key.startswith("$"):
            undollared = key[1:]
            if re.search(rf"(?<!\$)\b{re.escape(undollared)}\b", full_text):
                snippet = full_text[:200] if len(full_text) > 200 else full_text
                raise ValueError(
                    f"Found '{undollared}' without '$' prefix. "
                    f"Did you mean '{key}'?\n"
                    f"Context: {snippet!r}"
                )


def _dollar_sub_flat_el(dispatch, flat_el):
    if isinstance(flat_el, str):
        return _dollar_sub_str(dispatch, flat_el)
    return flat_el


def _dollar_sub_str(dispatch, str):
    parts = re.split(
        "([$][a-zA-Z0-9_]+|%[\u05d0-\u05ea\u05be]+|~\d+:\d+|\d+:\d+@[A-Za-z0-9_]+|\d+:\d+)",
        str,
    )
    return sl_map((_dollar_sub_str_part, dispatch), parts)


def _dollar_sub_str_part(dispatch, part):
    if part.startswith("$"):
        return dispatch[part]
    if part.startswith("%"):
        return my_html.span_c(part[1:], "unpointed-tanakh")
    if part.startswith("~") and ":" in part:
        # Suppressed verse reference: strip ~ and emit as plain text.
        return part[1:]
    if "@" in part:
        cv, wordid = part.split("@", 1)
        if re.fullmatch(r"\d+:\d+", cv):
            return verse_ref_link_disambig(cv, wordid)
    if re.fullmatch(r"\d+:\d+", part):
        return verse_ref_link(part)
    return part
