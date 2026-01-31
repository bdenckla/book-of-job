from pyauthor_util import author
from pyauthor_util.uxlc_change import uxlc_change

_URL = "https://bdenckla.github.io/MAM-with-doc/misc/tsinnorit_and_oleh_on_ivs.html"
doc = author.anc_h("document", _URL)

RECORD_3611 = {
    "qr-cv": "36:11",
    "qr-lc-proposed": "וְֽיַעֲ֫בֹ֥דוּ",
    "qr-what-is-weird": "עולה is over ע",
    "qr-consensus": "וְֽיַ֫עֲבֹ֥דוּ",
    "qr-generic-comment": [
        "In the middle of a word,",
        " the “half-accent” עולה (half of עולה ויורד)",
        " should never appear on a letter with a vocal שווא,",
        " regardless of whether the שווא is notated as a simple שווא or a חטף vowel.",
        " Yet, here is just such an עולה, on the letter ע with a חטף פתח.",
        " (Rarely, עולה appears on a letter with a vocal שווא at the beginning of a word.",
        [" See my ", doc, ", “Tsinnorit & Oleh on Initial Vocal Shewa” for details.)"],
    ],
    "qr-lc-img": "3611-custom.jpg",
    # Above, we use the UXLC change record screen snip (a .jpg) rather than one we took
    # ourselves (a .png). We use the UXLC screen snip just for convenience, to avoid
    # having to make our own. Except for this screen snip, we don’t care about the note
    # in UXLC on this issue, because we don’t care about notes in UXLC if there is a note
    # in one of the three earlier-published editions: BHL, DM, & WLC.
    "qr-highlight-lc-proposed": 3,
    "qr-highlight-consensus": 2,
    "qr-lc-loc": {"page": "407B", "column": 1, "line": 1},
    "qr-noted-by": "tBHQ-xBHL-nDM",
}
