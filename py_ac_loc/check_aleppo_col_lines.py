"""
Validate consistency of redundant elements in aleppo_col_lines JSON files.

Checks:
1. col-ranges-friendly matches col-ranges (machine-readable -> friendly string)
2. col-blank-lines matches actual blank lines in column-{right,left}-lines
3. col-pe-lines matches actual {פ}-only lines in column-{right,left}-lines
4. ketiv bcv-fml-friendly matches bcv-fml (machine-readable -> friendly string)
5. ketiv words actually appear in the corresponding line data
6. line range annotations: null for blank/{פ} lines, non-null for text lines,
   and formatted as "Book ch:vs" or "Book ch:vs–ch:vs"
7. page-ranges-friendly matches merged column friendly ranges,
   and page-ranges (machine) matches page-ranges-friendly
8. file-description is the generic (non-page-specific) form

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
    leaf = data["page-id"]

    for col_key, lines_key in (("column-right", "column-right-lines"), ("column-left", "column-left-lines")):
        col = data[col_key]
        lines = data[lines_key]

        # --- Check 1: col-ranges-friendly matches col-ranges ---
        ranges = col["col-ranges"]
        rf = col["col-ranges-friendly"]
        if len(ranges) != len(rf):
            err(leaf, col_key, f"col-ranges has {len(ranges)} entries but col-ranges-friendly has {len(rf)}")
        else:
            for i, (r, f) in enumerate(zip(ranges, rf)):
                expected_start = endpoint_friendly(r["start"])
                expected_end = endpoint_friendly(r["end"])
                if f["start"] != expected_start:
                    err(leaf, col_key, f"col-ranges-friendly[{i}].start = {f['start']!r}, expected {expected_start!r}")
                if f["end"] != expected_end:
                    err(leaf, col_key, f"col-ranges-friendly[{i}].end = {f['end']!r}, expected {expected_end!r}")

        # Extract text from lines
        line_texts = [(entry["line-num"], entry["MAM-XML-fragment"]) for entry in lines]
        line_ranges = [(entry["line-num"], entry["range"]) for entry in lines]

        # --- Check 2: col-blank-lines matches actual blank lines ---
        actual_blanks = sorted(ln for ln, txt in line_texts if txt == "")
        declared_blanks = sorted(col.get("col-blank-lines", []))
        if actual_blanks != declared_blanks:
            err(leaf, col_key, f"col-blank-lines = {declared_blanks}, actual blanks = {actual_blanks}")

        # --- Check 3: col-pe-lines matches actual {פ}-only lines ---
        actual_pe = sorted(ln for ln, txt in line_texts if txt == "{פ}")
        declared_pe = sorted(col.get("col-pe-lines", []))
        if actual_pe != declared_pe:
            err(leaf, col_key, f"col-pe-lines = {declared_pe}, actual pe-only = {actual_pe}")

        # --- Check 4 & 5: ketiv entries ---
        for k in col.get("col-ketivs", []):
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
            endpoint_pat = re.compile(
                r'^[A-Za-z1-9]+ \d+:\d+-(first|mid|last)$'
            )
            for ln, rng in line_ranges:
                txt = dict(line_texts)[ln]
                is_blank = (txt == "" or txt == "{פ}")
                if is_blank and rng is not None:
                    err(leaf, col_key, f"line {ln}: blank/{'{'}פ{'}'} line should have null range, got {rng!r}")
                elif not is_blank and rng is None:
                    err(leaf, col_key, f"line {ln}: text line should have a range, got null")
                elif rng is not None:
                    if not isinstance(rng, dict) or set(rng.keys()) != {"start", "end"}:
                        err(leaf, col_key, f"line {ln}: range should be a dict with 'start' and 'end' keys, got {rng!r}")
                    else:
                        for key in ("start", "end"):
                            ep = rng[key]
                            if not isinstance(ep, str) or not endpoint_pat.match(ep):
                                err(leaf, col_key, f"line {ln}: range {key} {ep!r} does not match 'Book ch:vs-(first|mid|last)'")

    # --- Check 7: page-ranges-friendly matches merged column ranges ---
    overall_friendly = data.get("page-ranges-friendly")
    if overall_friendly is None:
        err(leaf, "(top)", "missing 'page-ranges-friendly' field")
    elif not isinstance(overall_friendly, list) or len(overall_friendly) == 0:
        err(leaf, "(top)", f"page-ranges-friendly should be a non-empty list, got {type(overall_friendly).__name__}")
    else:
        # Build expected list: merge all column ranges by book
        from collections import OrderedDict
        all_col_ranges = []
        for ck in ("column-right", "column-left"):
            all_col_ranges.extend(data[ck]["col-ranges-friendly"])
        by_book = OrderedDict()
        for rf in all_col_ranges:
            book = rf["start"].rsplit(" ", 1)[0]
            if book not in by_book:
                by_book[book] = {"start": rf["start"], "end": rf["end"]}
            else:
                by_book[book]["end"] = rf["end"]
        expected = list(by_book.values())
        if overall_friendly != expected:
            err(leaf, "(top)", f"page-ranges-friendly = {overall_friendly!r}, expected {expected!r}")

    # --- Check 7b: page-ranges matches page-ranges-friendly ---
    overall_machine = data.get("page-ranges")
    if overall_machine is None:
        err(leaf, "(top)", "missing 'page-ranges' field")
    elif not isinstance(overall_machine, list) or len(overall_machine) == 0:
        err(leaf, "(top)", f"page-ranges should be a non-empty list, got {type(overall_machine).__name__}")
    elif overall_friendly is not None and isinstance(overall_friendly, list):
        if len(overall_machine) != len(overall_friendly):
            err(leaf, "(top)", f"page-ranges has {len(overall_machine)} entries but friendly has {len(overall_friendly)}")
        else:
            for i, (m, f) in enumerate(zip(overall_machine, overall_friendly)):
                for key in ("start", "end"):
                    expected_friendly = endpoint_friendly(m[key])
                    if expected_friendly != f[key]:
                        err(leaf, "(top)", f"page-ranges[{i}].{key}: machine {m[key]!r} -> {expected_friendly!r} but friendly says {f[key]!r}")

    # --- Check 8: generic file-description ---
    GENERIC_DESC = [
        "Line-by-line alignment of an Aleppo Codex",
        " page image to the corresponding MAM-XML text."
    ]
    desc = data.get("file-description")
    if desc != GENERIC_DESC:
        err(leaf, "(top)", f"file-description is not the generic form: {desc!r}")

if errors:
    print(f"FAILED: {len(errors)} error(s):")
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print(f"OK: All redundant elements are consistent across {len(list(AC_DIR.glob('aleppo_col_lines_*.json')))} files.")