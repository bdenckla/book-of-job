"""
Validate consistency of redundant elements in aleppo_col_lines JSON files.

Checks:
1. ranges-friendly matches ranges (machine-readable -> friendly string)
2. blank_lines matches actual blank lines in column_N_lines
3. pe_lines matches actual {פ}-only lines in column_N_lines
4. ketiv bcv-fml-friendly matches bcv-fml (machine-readable -> friendly string)
5. ketiv words actually appear in the corresponding line data
6. line range annotations: null for blank/{פ} lines, non-null for text lines,
   and formatted as "Book ch:vs" or "Book ch:vs–ch:vs"

Usage:
    python py_ac_loc/check_aleppo_col_lines.py
"""

import json
import sys
from pathlib import Path

AC_DIR = Path(__file__).resolve().parent

SUFFIX = {"first-word": "-first", "a-middle-word": "-mid", "last-word": "-last"}

errors = []


def err(leaf, col, msg):
    errors.append(f"  {leaf} {col}: {msg}")


def endpoint_friendly(ep):
    """Convert [book, ch, vs, fml] -> 'Book ch:vs-suffix'"""
    return f"{ep[0]} {ep[1]}:{ep[2]}{SUFFIX[ep[3]]}"


for json_path in sorted(AC_DIR.glob("aleppo_col_lines_*.json")):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    leaf = data["leaf"]

    for col_idx in (1, 2):
        col_key = f"column_{col_idx}"
        lines_key = f"column_{col_idx}_lines"
        col = data[col_key]
        lines = data[lines_key]

        # --- Check 1: ranges-friendly matches ranges ---
        ranges = col["ranges"]
        rf = col["ranges-friendly"]
        if len(ranges) != len(rf):
            err(leaf, col_key, f"ranges has {len(ranges)} entries but ranges-friendly has {len(rf)}")
        else:
            for i, (r, f) in enumerate(zip(ranges, rf)):
                expected_start = endpoint_friendly(r["start"])
                expected_end = endpoint_friendly(r["end"])
                if f["start"] != expected_start:
                    err(leaf, col_key, f"ranges-friendly[{i}].start = {f['start']!r}, expected {expected_start!r}")
                if f["end"] != expected_end:
                    err(leaf, col_key, f"ranges-friendly[{i}].end = {f['end']!r}, expected {expected_end!r}")

        # Extract text from lines (handle both 2-element and 3-element format)
        if lines and len(lines[0]) == 3:
            line_texts = [(entry[0], entry[2]) for entry in lines]  # [ln, range, txt]
            line_ranges = [(entry[0], entry[1]) for entry in lines]  # [ln, range]
        else:
            line_texts = [(entry[0], entry[1]) for entry in lines]  # [ln, txt]
            line_ranges = None

        # --- Check 2: blank_lines matches actual blank lines ---
        actual_blanks = sorted(ln for ln, txt in line_texts if txt == "")
        declared_blanks = sorted(col.get("blank_lines", []))
        if actual_blanks != declared_blanks:
            err(leaf, col_key, f"blank_lines = {declared_blanks}, actual blanks = {actual_blanks}")

        # --- Check 3: pe_lines matches actual {פ}-only lines ---
        actual_pe = sorted(ln for ln, txt in line_texts if txt == "{פ}")
        declared_pe = sorted(col.get("pe_lines", []))
        if actual_pe != declared_pe:
            err(leaf, col_key, f"pe_lines = {declared_pe}, actual pe-only = {actual_pe}")

        # --- Check 4 & 5: ketiv entries ---
        for k in col.get("ketivs", []):
            bcv = k["bcv-fml"]
            friendly = k["bcv-fml-friendly"]
            word = k["word"]

            # Check 4: friendly matches machine-readable
            expected_friendly = endpoint_friendly(bcv)
            if friendly != expected_friendly:
                err(leaf, col_key, f"ketiv bcv-fml-friendly = {friendly!r}, expected {expected_friendly!r}")

            # Check 5: ketiv word appears in line data
            found = False
            for ln, txt in line_texts:
                if word in txt:
                    found = True
                    break
            if not found:
                err(leaf, col_key, f"ketiv word {word!r} (at {friendly}) not found in any line")

        # --- Check 6: line range annotations ---
        if line_ranges is not None:
            import re
            range_pat = re.compile(
                r'^[A-Za-z]+ \d+:\d+'
                r'(?:\u2013\d+:\d+)?$'  # optional en-dash range
            )
            for ln, rng in line_ranges:
                txt = dict(line_texts)[ln]
                is_blank = (txt == "" or txt == "{פ}")
                if is_blank and rng is not None:
                    err(leaf, col_key, f"line {ln}: blank/{'{'}פ{'}'} line should have null range, got {rng!r}")
                elif not is_blank and rng is None:
                    err(leaf, col_key, f"line {ln}: text line should have a range, got null")
                elif rng is not None and not range_pat.match(rng):
                    err(leaf, col_key, f"line {ln}: range {rng!r} does not match expected format")

if errors:
    print(f"FAILED: {len(errors)} error(s):")
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print(f"OK: All redundant elements are consistent across {len(list(AC_DIR.glob('aleppo_col_lines_*.json')))} files.")
