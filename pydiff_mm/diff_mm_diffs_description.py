""" Exports get1 & get2 """

from pydiff_mm import diff_mm_uni_name
from pydiff_mm import diff_mm_simplify_simple_diffs as ssd
from pycmn import my_diffs
from pycmn.hebrew_punctuation import MAQ as _MAQAF
from py import hebrew_letter_words as hlw
from py import uni_heb_char_classes as uhc


def get1(str1, str2):
    """
    If possible, get a human-friendly description of the diffs
    between str1 & str2.
    Returns a pair with the following contents:
    Element 1 of the pair is a string describing the diff in detail.
    Element 2 of the pair is a string describing the category, i.e. the kind of diff.
    """
    qc1 = ssd.qualify_code_points(str1)
    qc2 = ssd.qualify_code_points(str2)
    diffs = my_diffs.get(qc1, qc2)
    named_diffs = tuple(map(_get_unicode_names_for_diff, diffs))
    if _letters_differ(str1, str2):
        maqaf_desc = _maqaf_space_diff(str1, str2)
        if maqaf_desc:
            return maqaf_desc
        return _get_dide_incl_letter_changes(str1, str2, named_diffs)
    return ssd.simplify_simple_diffs(named_diffs)


def get2(mlist_a, mlist_b):
    """
    If possible, get a human-friendly description of the diffs
    between mlist1 & mlist2. (mlist: maybe a list, i.e. a list or None)
    """
    rstra = _get_refinable_str(mlist_a)
    rstrb = _get_refinable_str(mlist_b)
    return rstra and rstrb and get1(rstra, rstrb)


def _letters_differ(str1, str2):
    lm1 = hlw.letters_and_maqafs(str1)
    lm2 = hlw.letters_and_maqafs(str2)
    return lm1 != lm2


def _maqaf_space_diff(str1, str2):
    """If the only diffs between str1 and str2 are maqaf/space related, describe them."""
    # Case 1: same length, maqaf↔space swaps at matching positions
    if str1.replace(_MAQAF, " ") == str2.replace(_MAQAF, " "):
        m2s = sum(1 for a, b in zip(str1, str2) if a == _MAQAF and b == " ")
        s2m = sum(1 for a, b in zip(str1, str2) if a == " " and b == _MAQAF)
        if m2s > 0 and s2m > 0:
            return None  # mixed directions, too complex
        if m2s > 0:
            return f"replace {m2s} maqaf mark(s) with space", "maqaf/space"
        if s2m > 0:
            return f"replace {s2m} space(s) with maqaf", "maqaf/space"
    # Case 2: one string is the other plus a trailing maqaf
    if str1 == str2 + _MAQAF:
        return "remove trailing maqaf", "maqaf/space"
    if str1 + _MAQAF == str2:
        return "add trailing maqaf", "maqaf/space"
    return None


def _get_dide_incl_letter_changes(_str1, _str2, named_diffs):
    return str(named_diffs), "deep diff"


def _get_refinable_str(mlist):
    if mlist is None:
        return None
    assert isinstance(mlist, list)
    if not len(mlist) == 1:
        return None
    if not isinstance(mlist[0], str):
        return None
    inter = set(uhc.VOWEL_POINTS).intersection(mlist[0])
    if len(inter) == 0:
        return None
    return mlist[0]


def _get_unicode_names_for_diff(diff):
    assert len(diff) == 2  # an "A" side and a "B" side
    return tuple(map(_get_unicode_names_for_side, diff))


def _get_unicode_names_for_side(side):
    return side and tuple(map(_get_unicode_names_for_side_el, side))


def _get_unicode_names_for_side_el(side):
    letter = ssd.qcp_get(side, "letter")
    return ssd.qcp_make(
        diff_mm_uni_name.name(ssd.qcp_get(side, "code_point")),
        letter and diff_mm_uni_name.name(letter),
        ssd.qcp_get(side, "count"),
    )
