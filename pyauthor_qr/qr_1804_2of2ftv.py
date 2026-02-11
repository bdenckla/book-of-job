from pyauthor_util.job_common import RECORD_1804_CMN_AB


_BHQ_COMMENT_1804_B = [
    "$BHQ notes that the דגש on the מ in μL disagrees with μA and μY.",
    " $BHQ misses the געיה in μA.",
    " This געיה is irrelevant to $BHQ’s point here, which is about the דגש.",
    " Still, it would have been nice if $BHQ had transcribed the געיה.",
]
RECORD_1804_2of2ftv = {
    **RECORD_1804_CMN_AB,
    "qr-n_of_m_for_this_verse": (2, 2),  # this is record 2 of 2 for this verse
    "qr-n_of_m_for_this_word": (2, 2),  # this is record 2 of 2 for this word
    "qr-what-is-weird": "מ has דגש",
    "qr-generic-comment": [
        "The quirk that the פתח on ה",
        " is חטף is discussed in a separate entry of mine.",
    ],
    "qr-ignore-g3yh-diff": True,
    "qr-highlight": 3,
    "qr-bhq-comment": _BHQ_COMMENT_1804_B,
    "qr-aleppo-page-url": "https://www.mgketer.org/mikra/29/18/1/mg/106",
    "qr-noted-by": "nBHQ-nBHL-nDM",
}
