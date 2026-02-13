"""
Extract verse words from MAM-XML (xml-vtrad-mam) for Aleppo Codex alignment.

Handles all special MAM-XML elements:
  - <text>: plain text spans
  - <lp-legarmeih>, <lp-paseq>: append paseq (U+05C0) to preceding word
  - <kq>: ketiv/qere — use ketiv (kq-k child, unpointed) for manuscript alignment
  - <kq-trivial>: trivial ketiv/qere — use text attribute (pointed)
  - <slh-word>: suspended-letter word — use slhw-desc-0 (full pointed word)
  - <implicit-maqaf>: no visible text, skip
  - <spi-pe2>: petuxah (open paragraph) break — emitted as {פ}
  - <spi-samekh2>: setumah (closed paragraph) break — emitted as {ס}

Usage:
    from pycmn.mam_xml_verses import get_verses_in_range

    verses = get_verses_in_range(
        r'C:\\path\\to\\MAM-XML\\out\\xml-vtrad-mam\\Job.xml',
        'Job', (37, 9), (38, 20),
    )
    # Returns: [{'cv': '37:9', 'words': [...], 'ketiv_indices': [], 'parashah_after': None}, ...]
    # parashah_after is None, '{פ}', or '{ס}'
"""

import xml.etree.ElementTree as ET

PASEQ = '\u05C0'
MAQAF = '\u05BE'


def get_verse_words(verse_el):
    """
    Extract the word list from a MAM-XML <verse> element.

    Returns a dict:
        words: list of str — space-separated words (maqaf-connected words joined)
        ketiv_indices: list of int — indices in `words` that are ketiv (unpointed)
    """
    raw_words = []
    ketiv_flags = []

    if 'text' in verse_el.attrib:
        # Simple verse: text is directly on the element
        raw_words = verse_el.attrib['text'].split()
        ketiv_flags = [False] * len(raw_words)
    else:
        # Complex verse: iterate children
        for child in verse_el:
            tag = child.tag
            if tag == 'text':
                text = child.attrib.get('text', '').strip()
                if text:
                    ws = text.split()
                    raw_words.extend(ws)
                    ketiv_flags.extend([False] * len(ws))
            elif tag in ('lp-legarmeih', 'lp-paseq'):
                # Append paseq to the last word
                if raw_words:
                    raw_words[-1] = raw_words[-1] + PASEQ
            elif tag == 'kq':
                # Non-trivial ketiv/qere — use ketiv text (unpointed)
                kq_k = child.find('kq-k')
                if kq_k is not None:
                    kt = kq_k.attrib.get('text', '').strip()
                    if kt:
                        ws = kt.split()
                        raw_words.extend(ws)
                        ketiv_flags.extend([True] * len(ws))
            elif tag == 'kq-trivial':
                # Trivial k/q — use pointed text attribute
                text = child.attrib.get('text', '').strip()
                if text:
                    ws = text.split()
                    raw_words.extend(ws)
                    ketiv_flags.extend([False] * len(ws))
            elif tag == 'slh-word':
                # Suspended-letter word — use desc-0 (full pointed word)
                text = child.attrib.get('slhw-desc-0', '').strip()
                if text:
                    ws = text.split()
                    raw_words.extend(ws)
                    ketiv_flags.extend([False] * len(ws))
            elif tag == 'implicit-maqaf':
                pass  # No visible text
            # Other unknown tags: silently skip

    # Join maqaf-connected words
    joined = []
    joined_ketiv = []
    for w, is_k in zip(raw_words, ketiv_flags):
        if joined and joined[-1].endswith(MAQAF):
            joined[-1] = joined[-1] + w
            # If either part is ketiv, mark the joined word as ketiv
            joined_ketiv[-1] = joined_ketiv[-1] or is_k
        else:
            joined.append(w)
            joined_ketiv.append(is_k)

    ketiv_indices = [i for i, k in enumerate(joined_ketiv) if k]
    return {'words': joined, 'ketiv_indices': ketiv_indices}


def get_verses_in_range(xml_path, book_osis_prefix, start_cv, end_cv):
    """
    Extract verses from a MAM-XML file in a chapter:verse range.

    Args:
        xml_path: path to the MAM-XML file (e.g., .../xml-vtrad-mam/Job.xml)
        book_osis_prefix: e.g., 'Job'
        start_cv: (chapter, verse) tuple, inclusive
        end_cv: (chapter, verse) tuple, inclusive

    Returns:
        list of dicts, each with:
            cv: str — e.g., '37:9'
            words: list of str — maqaf-joined words
            ketiv_indices: list of int — indices of ketiv (unpointed) words
            parashah_after: None, '{פ}', or '{ס}' — break after this verse
    """
    tree = ET.parse(xml_path)
    book39 = tree.getroot()[0]

    # First pass: collect parashah breaks between chapters (book-level siblings)
    inter_chapter_breaks = {}  # ch_num -> break string
    prev_chapter_num = None
    for child in book39:
        if child.tag == 'chapter':
            osis = child.attrib.get('osisID', '')
            if osis.startswith(book_osis_prefix + '.'):
                prev_chapter_num = int(osis.split('.')[-1])
        elif child.tag in ('spi-pe2', 'spi-samekh2') and prev_chapter_num is not None:
            brk = '{פ}' if child.tag == 'spi-pe2' else '{ס}'
            inter_chapter_breaks[prev_chapter_num] = brk

    verses = []
    for child in book39:
        if child.tag != 'chapter':
            continue
        osis = child.attrib.get('osisID', '')  # e.g., 'Job.37'
        if not osis.startswith(book_osis_prefix + '.'):
            continue
        ch = int(osis.split('.')[-1])

        # Collect intra-chapter parashah breaks: verse osisID -> break string
        intra_breaks = {}
        ch_children = list(child)
        for i, el in enumerate(ch_children):
            if el.tag in ('spi-pe2', 'spi-samekh2'):
                brk = '{פ}' if el.tag == 'spi-pe2' else '{ס}'
                # Find the preceding verse
                for j in range(i - 1, -1, -1):
                    if ch_children[j].tag == 'verse':
                        intra_breaks[ch_children[j].attrib['osisID']] = brk
                        break

        # Find the last verse number in this chapter (for inter-chapter break check)
        last_vs_in_ch = max(
            (int(vv.attrib['osisID'].split('.')[-1]) for vv in child if vv.tag == 'verse'),
            default=0,
        )

        for v in child:
            if v.tag != 'verse':
                continue
            v_osis = v.attrib['osisID']
            vs = int(v_osis.split('.')[-1])
            if (ch, vs) < start_cv or (ch, vs) > end_cv:
                continue
            result = get_verse_words(v)
            result['cv'] = f'{ch}:{vs}'

            # Check for parashah break after this verse
            if v_osis in intra_breaks:
                result['parashah_after'] = intra_breaks[v_osis]
            elif vs == last_vs_in_ch and ch in inter_chapter_breaks:
                result['parashah_after'] = inter_chapter_breaks[ch]
            else:
                result['parashah_after'] = None

            verses.append(result)

    return verses
