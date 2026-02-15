"""
Generate a flat-stream JSON file for a given page and write it
to py_ac_loc/line-breaks/<page>.json (without line-break markers).
This is the starting point for interactively adding line breaks.

Usage:
    python py_ac_loc/gen_lb_flat_stream.py 270v
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from py_ac_loc.gen_flat_stream import load_index, get_page_verses, build_flat_stream

BASE = Path(__file__).resolve().parent.parent
OUT_DIR = BASE / "py_ac_loc" / "line-breaks"


def main():
    if len(sys.argv) < 2:
        print("Usage: python py_ac_loc/gen_lb_flat_stream.py <page_id>")
        sys.exit(1)
    page_id = sys.argv[1]
    index = load_index()
    if page_id not in index:
        print(f"ERROR: {page_id} not found in index-flat.json")
        sys.exit(1)
    text_range = index[page_id]
    print(f"{page_id}: {text_range[0]} .. {text_range[1]}")
    verses = get_page_verses(text_range)
    stream = build_flat_stream(page_id, verses)
    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{page_id}.json"
    out_path.write_text(
        json.dumps(stream, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    word_count = sum(1 for x in stream if isinstance(x, str))
    verse_count = sum(1 for x in stream if isinstance(x, dict) and "verse-start" in x)
    print(f"  -> {out_path.name}: {verse_count} verses, {word_count} words")


if __name__ == "__main__":
    main()
