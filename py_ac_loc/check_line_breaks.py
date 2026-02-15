"""
Stats reporter and consistency checker for line-break JSON files.

Checks each file in py_ac_loc/line-breaks/*.json for structural
consistency and reports summary statistics.

Usage:
    python py_ac_loc/check_line_breaks.py          # check all files
    python py_ac_loc/check_line_breaks.py 270v      # check one file
"""

import json
import sys
import webbrowser
from collections import Counter
from pathlib import Path

PROJ_DIR = Path(__file__).resolve().parent.parent
LB_DIR = PROJ_DIR / "py_ac_loc" / "line-breaks"
OUT_DIR = PROJ_DIR / ".novc"

EXPECTED_LINES_PER_COL = 28


def load_stream(path):
    return json.loads(path.read_text(encoding="utf-8"))


def classify_item(item):
    """Return a classification string for a stream item."""
    if isinstance(item, str):
        return "word"
    if isinstance(item, dict):
        for key in (
            "page-start", "page-end",
            "verse-start", "verse-end",
            "line-start", "line-end",
            "parashah",
        ):
            if key in item:
                return key
        return f"unknown-dict({sorted(item.keys())})"
    return f"unknown-type({type(item).__name__})"


def check_file(path, verbose=True):
    """Check a single line-break JSON file. Returns list of issues."""
    name = path.stem
    stream = load_stream(path)
    issues = []

    # Classify all items
    classes = Counter()
    for item in stream:
        classes[classify_item(item)] += 1

    # --- Structural checks ---

    # page-start / page-end
    if classes["page-start"] != 1:
        issues.append(f"Expected 1 page-start, found {classes['page-start']}")
    if classes["page-end"] != 1:
        issues.append(f"Expected 1 page-end, found {classes['page-end']}")

    # line-start / line-end pairing
    if classes["line-start"] != classes["line-end"]:
        issues.append(
            f"line-start ({classes['line-start']}) != "
            f"line-end ({classes['line-end']})"
        )

    # verse-start / verse-end
    vs_diff = classes["verse-start"] - classes["verse-end"]
    if abs(vs_diff) > 1:
        issues.append(
            f"verse-start ({classes['verse-start']}) and "
            f"verse-end ({classes['verse-end']}) differ by {vs_diff}"
        )

    # Unknown types
    for key, count in classes.items():
        if key.startswith("unknown"):
            issues.append(f"Unknown item type: {key} (×{count})")

    # --- Line marker checks ---

    # Collect line-start and line-end positions (stream index)
    line_starts = {}  # (col, line-num) -> stream index
    line_ends = {}    # (col, line-num) -> stream index
    col_lines = {}    # col -> list of line-nums (from line-end markers)

    for idx, item in enumerate(stream):
        cls = classify_item(item)
        if cls == "line-start":
            info = item["line-start"]
            key = (info["col"], info["line-num"])
            if key in line_starts:
                issues.append(f"Duplicate line-start(col={key[0]}, num={key[1]})")
            line_starts[key] = idx
        elif cls == "line-end":
            info = item["line-end"]
            col = info["col"]
            lnum = info["line-num"]
            key = (col, lnum)
            if key in line_ends:
                issues.append(f"Duplicate line-end(col={col}, num={lnum})")
            line_ends[key] = idx
            if col not in col_lines:
                col_lines[col] = []
            col_lines[col].append(lnum)

    # Check that every line-start has a matching line-end and vice versa
    start_keys = set(line_starts.keys())
    end_keys = set(line_ends.keys())
    for key in sorted(start_keys - end_keys):
        issues.append(f"line-start(col={key[0]}, num={key[1]}) with no matching line-end")
    for key in sorted(end_keys - start_keys):
        issues.append(f"line-end(col={key[0]}, num={key[1]}) with no matching line-start")

    # For matched pairs, check ordering (line-start should come before
    # line-end, unless the line is empty — which is fine)
    empty_lines = []
    for key in sorted(start_keys & end_keys):
        s_idx = line_starts[key]
        e_idx = line_ends[key]
        if e_idx < s_idx:
            # line-end before line-start: verify the line is empty
            # (no words between line-end and line-start)
            words_between = [
                stream[i] for i in range(e_idx + 1, s_idx)
                if classify_item(stream[i]) == "word"
            ]
            if words_between:
                issues.append(
                    f"line-end(col={key[0]}, num={key[1]}) comes before "
                    f"line-start but {len(words_between)} word(s) between them"
                )
            else:
                empty_lines.append(key)

    # Check lines per column
    for col in sorted(col_lines.keys()):
        nums = col_lines[col]
        n = len(nums)
        if n != EXPECTED_LINES_PER_COL:
            issues.append(
                f"Col {col}: {n} lines (expected {EXPECTED_LINES_PER_COL})"
            )
        # Check line numbering is sequential 1..N
        expected_nums = list(range(1, n + 1))
        if nums != expected_nums:
            issues.append(
                f"Col {col}: line numbers are {nums}, "
                f"expected {expected_nums}"
            )

    # Check that we have both columns (for poetry pages)
    if 1 not in col_lines:
        issues.append("No col 1 line markers")
    if 2 not in col_lines:
        issues.append("No col 2 line markers")

    # --- Verse continuity check ---
    # Verify verse-start values are well-formed "Book C:V"
    for item in stream:
        if isinstance(item, dict) and "verse-start" in item:
            vs = item["verse-start"]
            parts = vs.rsplit(" ", 1)
            if len(parts) != 2 or ":" not in parts[1]:
                issues.append(f"Malformed verse-start: {vs!r}")

    # --- Word count ---
    word_count = classes.get("word", 0)

    # --- Build stats dict ---
    stats = {
        "name": name,
        "words": word_count,
        "col_lines": {col: len(nums) for col, nums in sorted(col_lines.items())},
        "verse_starts": classes.get("verse-start", 0),
        "verse_ends": classes.get("verse-end", 0),
        "parashahs": classes.get("parashah", 0),
        "empty_lines": empty_lines,
        "issues": issues,
    }

    return stats


def main():
    # Determine which files to check
    if len(sys.argv) > 1:
        pages = sys.argv[1:]
        paths = []
        for p in pages:
            path = LB_DIR / f"{p}.json"
            if not path.exists():
                print(f"ERROR: {path} not found")
                sys.exit(1)
            paths.append(path)
    else:
        paths = sorted(LB_DIR.glob("*.json"))

    if not paths:
        print("No JSON files found in", LB_DIR)
        sys.exit(1)

    all_stats = []
    total_issues = 0

    for path in paths:
        stats = check_file(path)
        all_stats.append(stats)
        total_issues += len(stats["issues"])

    # --- Collect unique verse-start values ---
    all_verses = set()
    for path in paths:
        stream = load_stream(path)
        for item in stream:
            if isinstance(item, dict) and "verse-start" in item:
                all_verses.add(item["verse-start"])

    # --- Collect empty lines ---
    all_empty = []
    for s in all_stats:
        for col, lnum in s["empty_lines"]:
            all_empty.append((s["name"], col, lnum))

    # --- Totals ---
    tw = sum(s["words"] for s in all_stats)
    tc1 = sum(s["col_lines"].get(1, 0) for s in all_stats)
    tc2 = sum(s["col_lines"].get(2, 0) for s in all_stats)
    tvs = sum(s["verse_starts"] for s in all_stats)
    tve = sum(s["verse_ends"] for s in all_stats)
    tp = sum(s["parashahs"] for s in all_stats)
    tem = sum(len(s["empty_lines"]) for s in all_stats)

    # --- Build HTML ---
    passed = total_issues == 0
    verdict_class = "pass" if passed else "fail"
    verdict_text = "All checks passed" if passed else f"{total_issues} issue(s) found"

    rows_html = []
    for s in all_stats:
        c1 = s["col_lines"].get(1, 0)
        c2 = s["col_lines"].get(2, 0)
        em = len(s["empty_lines"])
        has_issues = bool(s["issues"])
        row_class = ' class="issue-row"' if has_issues else ""
        issue_cell = "; ".join(s["issues"]) if has_issues else "\u2714"
        issue_class = ' class="fail"' if has_issues else ' class="pass"'
        rows_html.append(
            f"<tr{row_class}>"
            f"<td>{s['name']}</td>"
            f"<td class='num'>{s['words']}</td>"
            f"<td class='num'>{c1}</td>"
            f"<td class='num'>{c2}</td>"
            f"<td class='num'>{s['verse_starts']}</td>"
            f"<td class='num'>{s['verse_ends']}</td>"
            f"<td class='num'>{s['parashahs']}</td>"
            f"<td class='num'>{em}</td>"
            f"<td{issue_class}>{issue_cell}</td>"
            f"</tr>"
        )

    empty_rows_html = ""
    if all_empty:
        elines = "".join(
            f"<tr><td>{p}</td><td class='num'>{c}</td><td class='num'>{ln}</td></tr>"
            for p, c, ln in all_empty
        )
        empty_rows_html = f"""
    <h2>Empty Lines ({len(all_empty)})</h2>
    <table>
      <tr><th>Page</th><th>Col</th><th>Line</th></tr>
      {elines}
    </table>"""

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Line-Break Checker Report</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2em; background: #fafafa; }}
  h1 {{ margin-bottom: 0.3em; }}
  .verdict {{ font-size: 1.3em; font-weight: bold; margin-bottom: 1.5em; }}
  .pass {{ color: #2a7d2a; }}
  .fail {{ color: #c03030; }}
  table {{ border-collapse: collapse; margin-bottom: 1.5em; }}
  th, td {{ border: 1px solid #ccc; padding: 4px 10px; text-align: left; }}
  th {{ background: #e8e8e8; }}
  td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  tr.issue-row {{ background: #fff0f0; }}
  tfoot td {{ font-weight: bold; background: #f0f0f0; }}
  .summary {{ margin-bottom: 1.5em; }}
  .summary span {{ margin-right: 2em; }}
</style>
</head>
<body>
<h1>Line-Break Checker Report</h1>
<div class="verdict {verdict_class}">{verdict_text}</div>

<div class="summary">
  <span>Unique verses: {len(all_verses)}</span>
  <span>Empty lines: {len(all_empty)}</span>
  <span>Pages: {len(all_stats)}</span>
</div>

<table>
  <thead>
    <tr>
      <th title="Codex page ID (e.g. 270r = leaf 270 recto)">Page</th>
      <th title="Hebrew word count">Words</th>
      <th title="Column 1 (right) line count">C1</th>
      <th title="Column 2 (left) line count">C2</th>
      <th title="Verse-start marker count">V-st</th>
      <th title="Verse-end marker count">V-en</th>
      <th title="Parashah marker count">Par</th>
      <th title="Empty lines (blank lines in the codex)">EmLn</th>
      <th title="Consistency check issues">Issues</th>
    </tr>
  </thead>
  <tbody>
    {"".join(rows_html)}
  </tbody>
  <tfoot>
    <tr>
      <th title="Codex page ID (e.g. 270r = leaf 270 recto)">Page</th>
      <th title="Hebrew word count">Words</th>
      <th title="Column 1 (right) line count">C1</th>
      <th title="Column 2 (left) line count">C2</th>
      <th title="Verse-start marker count">V-st</th>
      <th title="Verse-end marker count">V-en</th>
      <th title="Parashah marker count">Par</th>
      <th title="Empty lines (blank lines in the codex)">EmLn</th>
      <th title="Consistency check issues">Issues</th>
    </tr>
    <tr>
      <td>TOTAL</td>
      <td class="num">{tw}</td>
      <td class="num">{tc1}</td>
      <td class="num">{tc2}</td>
      <td class="num">{tvs}</td>
      <td class="num">{tve}</td>
      <td class="num">{tp}</td>
      <td class="num">{tem}</td>
      <td>{total_issues} issue(s)</td>
    </tr>
  </tfoot>
</table>
{empty_rows_html}

<h2>Checks Performed</h2>
<ol>
  <li>Exactly 1 <code>page-start</code> and 1 <code>page-end</code> marker per file</li>
  <li>Every <code>line-start</code> has a matching <code>line-end</code> with the same column and line number, and vice versa</li>
  <li>No duplicate <code>line-start</code> or <code>line-end</code> markers</li>
  <li>{EXPECTED_LINES_PER_COL} lines per column, numbered sequentially 1\u2013{EXPECTED_LINES_PER_COL}</li>
  <li>Both columns (1 and 2) present in every file</li>
  <li><code>verse-start</code> and <code>verse-end</code> counts differ by at most 1</li>
  <li><code>verse-start</code> values are well-formed (<code>Book C:V</code>)</li>
  <li>No unknown dict types in the stream</li>
  <li>Reversed-order pairs (line-end before line-start) must be truly empty (no words between them)</li>
</ol>
</body>
</html>
"""

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / "check_line_breaks.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Report written to {out_path}")
    webbrowser.open(out_path.as_uri())

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
