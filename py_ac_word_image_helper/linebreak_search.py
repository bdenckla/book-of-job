"""Search for words in Aleppo Codex line-break data."""

import json
from pathlib import Path

from .hebrew_metrics import strip_heb

ROOT = Path(__file__).resolve().parent.parent
LB_DIR = ROOT / "py_ac_loc" / "line-breaks"


def find_word_in_linebreaks(page_id, ch, v, consensus):
    """Find a word in the line-break data.

    Returns (col, line_num, word_index_in_line, line_words)
    where line_words is the list of all words on that line.
    """
    lb_path = LB_DIR / f"{page_id}.json"
    with open(lb_path, encoding="utf-8") as f:
        stream = json.load(f)

    verse_label = f"Job {ch}:{v}"
    in_verse = False
    cur_col = None
    cur_line = None
    word_idx = 0  # 0-based index within current line

    consensus_stripped = strip_heb(consensus)

    # First pass: find which col+line the word is on.
    target_col = None
    target_line = None
    target_word_idx = None
    for item in stream:
        if isinstance(item, dict):
            if item.get("verse-start") == verse_label or item.get("verse-fragment-start") == verse_label:
                in_verse = True
                continue
            if item.get("verse-end") == verse_label or item.get("verse-fragment-end") == verse_label:
                in_verse = False
                continue
            if "line-start" in item:
                cur_col = item["line-start"]["col"]
                cur_line = item["line-start"]["line-num"]
                word_idx = 0
                continue
            if "line-end" in item:
                continue
        elif isinstance(item, str) and in_verse:
            item_stripped = strip_heb(item)
            if item == consensus or item_stripped == consensus_stripped:
                target_col, target_line = cur_col, cur_line
                target_word_idx = word_idx
                break
            if consensus.endswith("\u05BE") and item_stripped == strip_heb(consensus[:-1]):
                target_col, target_line = cur_col, cur_line
                target_word_idx = word_idx
                break
            word_idx += 1

    if target_col is None:
        return None, None, None, []

    # Second pass: collect all words on that line
    in_target_line = False
    cur_line_words = []
    for item in stream:
        if isinstance(item, dict):
            if "line-start" in item:
                ls = item["line-start"]
                if ls["col"] == target_col and ls["line-num"] == target_line:
                    in_target_line = True
                    cur_line_words = []
                continue
            if "line-end" in item and in_target_line:
                break
        elif isinstance(item, str) and in_target_line:
            cur_line_words.append(item)

    return target_col, target_line, target_word_idx, cur_line_words
