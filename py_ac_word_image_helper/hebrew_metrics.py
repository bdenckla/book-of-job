"""Hebrew text utilities: width metrics, stripping, maqaf joining."""

import unicodedata


def strip_heb(s):
    """Strip cantillation marks and vowels from Hebrew text for matching."""
    out = []
    for ch in s:
        cat = unicodedata.category(ch)
        # Keep letters (Lo) and punctuation (Po for maqaf etc.), skip Mn (marks)
        if cat != "Mn":
            out.append(ch)
    return "".join(out)


def join_maqaf(words):
    """Join maqaf-ending words with the following word. Returns new list."""
    result = []
    for w in words:
        if result and result[-1].endswith("\u05BE"):
            result[-1] = result[-1] + w
        else:
            result.append(w)
    return result


# Relative width metrics for Hebrew characters (proportional, not monospace).
# Based on typical manuscript/printed Hebrew proportions.
# Values are relative to an "average" letter width of 1.0.
HEB_WIDTHS = {
    # Very narrow
    "\u05D9": 0.4,  # yod
    "\u05D5": 0.5,  # vav
    "\u05DF": 0.5,  # nun sofit
    # Narrow
    "\u05D6": 0.6,  # zayin
    "\u05D2": 0.7,  # gimel
    "\u05E8": 0.7,  # resh
    "\u05DA": 0.7,  # kaf sofit
    "\u05E3": 0.7,  # pe sofit
    # Medium
    "\u05D1": 0.85,  # bet
    "\u05D3": 0.85,  # dalet
    "\u05D4": 0.9,  # he
    "\u05DB": 0.85,  # kaf
    "\u05DC": 0.7,  # lamed
    "\u05E0": 0.7,  # nun
    "\u05E2": 0.9,  # ayin
    "\u05E4": 0.9,  # pe
    "\u05E5": 0.8,  # tsade sofit
    "\u05E6": 0.8,  # tsade
    "\u05E7": 0.9,  # qof
    "\u05EA": 0.9,  # tav
    # Wide
    "\u05D0": 1.0,  # alef
    "\u05D7": 1.0,  # chet
    "\u05D8": 1.0,  # tet
    "\u05DE": 1.0,  # mem
    "\u05E1": 1.0,  # samekh
    "\u05E9": 1.1,  # shin
    # Very wide
    "\u05DD": 1.1,  # mem sofit
    # Punctuation
    "\u05BE": 0.6,  # maqaf
    "\u05C0": 0.3,  # paseq
    "\u05C3": 0.3,  # sof pasuq
    "\u003A": 0.3,  # colon (sometimes used for sof pasuq in data)
}

# Inter-word space
SPACE_WIDTH = 0.5


def word_width(word):
    """Estimate the rendered width of a Hebrew word using character metrics."""
    w = 0.0
    for ch in word:
        cat = unicodedata.category(ch)
        if cat == "Mn":
            # Combining marks (vowels, accents) have zero width
            continue
        w += HEB_WIDTHS.get(ch, 0.85)  # default to average
    return w


def line_widths(words):
    """Return list of word widths and total line width including spaces."""
    word_ws = [word_width(w) for w in words]
    spaces = SPACE_WIDTH * max(0, len(words) - 1)
    total = sum(word_ws) + spaces
    return word_ws, total
