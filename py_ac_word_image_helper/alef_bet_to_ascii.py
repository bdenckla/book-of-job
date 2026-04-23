"""Convert Hebrew consonantal text to an ASCII word-identifier.

Strips all niqqud and accents, then transliterates each Hebrew letter
to a single ASCII character.  Same scheme as mgketer
``hebrew_word_id.py`` and book-of-job ``author.py``.

    >>> heb_alef_bet_to_ascii("לֶֽאֱנ֣וֹשׁ")
    'LANVJ'
"""

import re

# fmt: off
_HEBREW_TO_ASCII_FROM = (
    "\u05d0\u05d1\u05d2\u05d3\u05d4"   # אבגדה
    "\u05d5\u05d6\u05d7\u05d8\u05d9"   # וזחטי
    "\u05db\u05dc\u05de\u05e0\u05e1"   # כלמנס
    "\u05e2\u05e4\u05e6\u05e7\u05e8"   # עפצקר
    "\u05e9\u05ea"                      # שת
    "\u05da\u05dd\u05df\u05e3\u05e5"   # ךםןףץ
    "\u05be "                           # maqaf, space
)
_HEBREW_TO_ASCII_TO = (
    "ABGDH" "VZXEY" "KLMNO" "3PCQR" "JF" "56789" "0_"
)
# fmt: on

_HEBREW_TO_ASCII = str.maketrans(_HEBREW_TO_ASCII_FROM, _HEBREW_TO_ASCII_TO)
_KEEP_RE = re.compile(f"[{re.escape(_HEBREW_TO_ASCII_FROM)}]+")


def heb_alef_bet_to_ascii(hebrew_text):
    """Strip niqqud/accents from *hebrew_text*, transliterate to ASCII.

    Only Hebrew consonants (incl. final forms), maqaf, and space are
    kept; everything else is discarded.  The result is safe for use in
    filenames and HTML identifiers.
    """
    kept = "".join(_KEEP_RE.findall(hebrew_text))
    return kept.translate(_HEBREW_TO_ASCII)
