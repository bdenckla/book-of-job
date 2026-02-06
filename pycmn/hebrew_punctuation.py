import re

SOPA = "\N{HEBREW PUNCTUATION SOF PASUQ}"  # ׃
MAQ = "\N{HEBREW PUNCTUATION MAQAF}"  # ־
PASOLEG = "\N{HEBREW PUNCTUATION PASEQ}"  # ׀
NUN_HAF = "\N{HEBREW PUNCTUATION NUN HAFUKHA}"
GERSHAYIM = "\N{HEBREW PUNCTUATION GERSHAYIM}"  # ״
# GERESH = '\N{HEBREW PUNCTUATION GERESH}'
UPDOT = "\N{HEBREW MARK UPPER DOT}"  # aka extraordinary upper dot
LODOT = "\N{HEBREW MARK LOWER DOT}"  # aka extraordinary lower dot
MCIRC = "\N{HEBREW MARK MASORA CIRCLE}"
#
MAQ_RE = r"\u05be"

NU_GMAQ = "~"  # non-unicode gray maqaf (tilde)


def split_at_maq(string):
    return string.split(MAQ)


def split_at_bog_maq(phrase):
    return atoms_and_bog_maqs(phrase)[0]


def atoms_and_bog_maqs(phrase):
    """Split at black or gray maqaf"""
    maq_and_sp = MAQ + NU_GMAQ + " "
    parts = re.split(f"([{maq_and_sp}])", phrase)
    atoms = parts[0::2]
    atom_seps = parts[1::2]
    assert len(atoms) == 1 + len(atom_seps)
    return atoms, atom_seps
