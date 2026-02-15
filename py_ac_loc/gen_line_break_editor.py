"""
Generate an interactive HTML editor for adding/editing line-break
markers in flat-stream JSON files.

Reads a flat-stream JSON from py_ac_loc/line-breaks/<page>.json,
produces a self-contained HTML file with:
  - Left panel: clickable ground-truth words (RTL) with existing
    line-break markers shown
  - Right panel: Aleppo Codex page image (from archive.org)

Click the last word of each line to toggle line-end markers.
"Export JSON" copies the updated flat-stream (with line-start/line-end
markers inserted) to the clipboard.

Usage:
    python py_ac_loc/gen_line_break_editor.py 270v 1   # column 1 (right)
    python py_ac_loc/gen_line_break_editor.py 270v 2   # column 2 (left)
    python py_ac_loc/gen_line_break_editor.py 270r 1   # view/edit existing
"""

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AC_DIR = BASE / "py_ac_loc"
LB_DIR = AC_DIR / "line-breaks"
OUT_DIR = BASE / ".novc"


def _leaf_to_page_n(page_id):
    """Convert a leaf ID like '270r' to the archive.org 0-based page index."""
    num = int(page_id[:-1])
    side = page_id[-1]
    # For Job leaves (past the extra leaf 241a):
    # N = (leaf_number - 1) * 2 + 2 + (0 for recto, 1 for verso)
    return (num - 1) * 2 + 2 + (0 if side == "r" else 1)


def _image_url(page_id):
    """Build archive.org direct image URL for an Aleppo Codex page."""
    n = _leaf_to_page_n(page_id)
    return (
        "https://ia601801.us.archive.org/BookReader/BookReaderImages.php"
        f"?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip"
        f"&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{n:04d}.jp2"
        f"&id=aleppo-codex&scale=2&rotate=0"
    )


def load_stream(page_id):
    """Load the flat-stream JSON for a page."""
    path = LB_DIR / f"{page_id}.json"
    if not path.exists():
        print(f"ERROR: {path} not found")
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_words_and_markers(stream):
    """Extract word list and pre-existing line-end indices from a flat stream.

    Returns:
        words: list of dicts describing each word/parashah token
        line_ends: list of (word_index, col, line_num) for existing line-end markers
        page_start_idx: word index of the first word on the page (from
            line-start col 1 line-num 1), or None if not yet set
    """
    words = []
    line_ends = []
    page_start_idx = None
    current_verse = None
    word_idx = 0

    for item in stream:
        if isinstance(item, str):
            is_first = (current_verse is not None and
                        (len(words) == 0 or
                         words[-1].get("verse_label") != current_verse or
                         words[-1].get("is_parashah")))
            words.append({
                "text": item,
                "is_verse_start": is_first,
                "verse_label": current_verse,
                "is_parashah": False,
            })
            word_idx += 1
        elif isinstance(item, dict):
            if "verse-start" in item:
                current_verse = item["verse-start"]
            elif "verse-end" in item:
                pass
            elif "parashah" in item:
                words.append({
                    "text": item["parashah"],
                    "is_verse_start": False,
                    "verse_label": current_verse,
                    "is_parashah": True,
                    "parashah_value": item["parashah"],
                })
                word_idx += 1
            elif "line-start" in item:
                ls = item["line-start"]
                if ls["col"] == 1 and ls["line-num"] == 1:
                    page_start_idx = word_idx
            elif "line-end" in item:
                if word_idx > 0:
                    line_ends.append((
                        word_idx - 1,
                        item["line-end"]["col"],
                        item["line-end"]["line-num"],
                    ))
            # page-start, page-end: skip

    return words, line_ends, page_start_idx


def generate_editor_html(page_id, col):
    """Generate the HTML editor file for a page, cropped to a column.

    col: 1 = right column (right 60%), 2 = left column (left 60%)
    """
    stream = load_stream(page_id)
    words, line_ends, page_start_idx = _extract_words_and_markers(stream)
    image_url = _image_url(page_id)

    # CSS crop: col 1 shows right 60%, col 2 shows left 60%
    # We set the image wider than its container and offset it.
    #
    # "Skinny mode" crops tighter: showing only 30% of the image
    # centered on the actual text column.
    # Think of the page as 10 equal strips each 10% wide.
    #   col 1 normal: strips 5–10 (right 60%)   skinny: strips 6–8 (50%–80%)
    #   col 2 normal: strips 1–6 (left 60%)    skinny: strips 3–5 (20%–50%)
    if col == 1:
        # Right 60%: image at 166% width, shifted left by 66%
        img_css = "width: 166%; max-width: none; margin-left: -66%;"
        # Skinny: show 50%-80% of image (strips 6-8)
        img_css_skinny = "width: 333%; max-width: none; margin-left: -167%;"
    else:
        # Left 60%: image at 166% width, no offset (left portion shows)
        img_css = "width: 166%; max-width: none; margin-left: 0;"
        # Skinny: show 0%-30% of image (strips 1-3)
        img_css_skinny = "width: 333%; max-width: none; margin-left: 0;"

    # Build JS data
    js_words = []
    for w in words:
        entry = {
            "text": w["text"],
            "isVerseStart": w["is_verse_start"],
            "verseLabel": w["verse_label"] or "",
            "isParashah": w["is_parashah"],
        }
        js_words.append(entry)

    # Pre-existing line-end word indices with col/line info
    js_line_ends = []
    for (widx, col_num, lnum) in line_ends:
        js_line_ends.append({"idx": widx, "col": col_num, "lineNum": lnum})

    # Build the stream without line markers for export reconstruction
    stream_no_lines = [item for item in stream
                       if not (isinstance(item, dict) and
                               ("line-start" in item or "line-end" in item))]

    words_json = json.dumps(js_words, ensure_ascii=False, indent=None)
    line_ends_json = json.dumps(js_line_ends, ensure_ascii=False)
    stream_json = json.dumps(stream_no_lines, ensure_ascii=False, indent=2)
    page_start_js = "null" if page_start_idx is None else str(page_start_idx)

    col_label = '1 (right)' if col == 1 else ('2 (left)' if col == 2 else '3 (center/prose)')

    html = _HTML_TEMPLATE.format(
        page_id=page_id,
        image_url=image_url,
        img_css=img_css_skinny,
        img_css_normal=img_css,
        img_css_skinny=img_css_skinny,
        col_label=col_label,
        col_num=col,
        words_json=words_json,
        line_ends_json=line_ends_json,
        stream_json=stream_json,
        page_start_idx_js=page_start_js,
    )

    out_path = OUT_DIR / f"lb_editor_{page_id}_col{col}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path}")
    return out_path


_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<title>Line Break Editor \u2014 {page_id}</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Segoe UI', sans-serif; background: #1e1e1e; color: #d4d4d4; }}
h1 {{ text-align: center; padding: 10px; font-size: 17px; background: #252526; border-bottom: 1px solid #444; direction: ltr; }}
h1 button {{
    padding: 4px 12px; margin: 0 4px; cursor: pointer;
    background: #0e639c; color: #fff; border: none; border-radius: 4px;
    font-size: 13px; vertical-align: middle;
}}
h1 button:hover {{ background: #1177bb; }}
#status {{
    display: inline-block; margin-left: 12px;
    font-size: 13px; color: #888;
}}
.container {{ display: flex; height: calc(100vh - 45px); }}
.col-words {{
    overflow-y: auto; padding: 16px; direction: rtl;
    font-size: 22px;
    font-family: 'SBL Hebrew', 'Ezra SIL', 'Times New Roman', serif;
}}
.divider {{
    width: 6px;
    cursor: col-resize;
    background: transparent;
    transition: background 0.15s;
    flex-shrink: 0;
}}
.divider:hover, .divider.active {{
    background: #0e639c;
}}
.col-image {{
    overflow-x: hidden; overflow-y: auto;
    padding: 8px; direction: ltr;
}}
.col-image img {{ {img_css} cursor: crosshair; transition: width 0.2s, margin-left 0.2s; }}
.word {{
    display: inline-block;
    padding: 3px 5px;
    margin: 1px;
    cursor: pointer;
    border-radius: 3px;
    border: 1px solid transparent;
    user-select: none;
    transition: background 0.12s;
    line-height: 1.8;
}}
.word:hover {{ background: #333; }}
.word.line-end {{
    background: #264f2a;
    border-color: #4ec94e;
    border-left: 3px solid #4ec94e;
}}
.word.parashah {{
    color: #e07040;
    font-size: 16px;
    font-family: monospace;
    cursor: pointer;
}}
.word.lead-in {{
    opacity: 0.35;
    cursor: default;
}}
.word.page-start {{
    background: #3a2a5f;
    border-color: #9a7adf;
    border-right: 3px solid #9a7adf;
}}
.page-start-label {{
    display: inline-block;
    color: #9a7adf;
    font-size: 11px;
    font-family: monospace;
    direction: ltr;
    margin-left: 4px;
}}
.word.verse-start {{
    border-bottom: 2px solid #5a5a8a;
}}
.word.maqaf-end {{
    margin-left: 0; padding-left: 0;
}}
.word.after-maqaf {{
    margin-right: 0; padding-right: 0;
}}
.line-num {{
    display: inline-block;
    color: #888;
    font-size: 12px;
    font-family: monospace;
    min-width: 40px;
    text-align: center;
    direction: ltr;
    margin-left: 4px;
}}
.col-label {{
    display: inline-block;
    color: #cc0;
    font-size: 11px;
    font-family: monospace;
    direction: ltr;
    margin-left: 2px;
    vertical-align: super;
}}

</style>
</head>
<body>

<h1>Line Break Editor \u2014 {page_id} \u2014 Col {col_label}
    <button onclick="exportJSON()">Export</button>
    <button id="skinnyBtn" onclick="toggleSkinnyMode()">Go wide</button>
    <span id="status"></span>
</h1>
<div class="container" id="container">
    <div class="col-words" id="wordsPanel"></div>
    <div class="divider" id="divider"></div>
    <div class="col-image" id="imagePanel">
        <img src="{image_url}" alt="Aleppo Codex {page_id}">
    </div>
</div>

<script>
const PAGE_ID = "{page_id}";
const MAQAF = '\\u05BE';
// Skinny / normal image crop modes
const IMG_CSS_NORMAL = "{img_css_normal}";
const IMG_CSS_SKINNY = "{img_css_skinny}";
let isSkinnyMode = true; // skinny is default
const allWords = {words_json};
const preExistingLineEnds = {line_ends_json};
const baseStream = {stream_json};

// State: Map<wordIdx, {{col, lineNum}}>
let lineEndMap = new Map();

// Page-start: index of the first word actually on this page.
// Words before this are lead-in from the previous page.
// null means not set (or page starts at word 0).
let pageStartIdx = {page_start_idx_js};

// Initialize from pre-existing line ends
preExistingLineEnds.forEach(le => {{
    lineEndMap.set(le.idx, {{col: le.col, lineNum: le.lineNum}});
}});

const CURRENT_COL = {col_num};
function currentCol() {{
    return CURRENT_COL;
}}

function recalcLineNums() {{
    // For each column, renumber lines sequentially
    const byCols = {{}};
    const sorted = [...lineEndMap.entries()].sort((a, b) => a[0] - b[0]);
    sorted.forEach(([idx, info]) => {{
        if (!byCols[info.col]) byCols[info.col] = [];
        byCols[info.col].push(idx);
    }});
    for (const col in byCols) {{
        byCols[col].forEach((idx, i) => {{
            lineEndMap.get(idx).lineNum = i + 1;
        }});
    }}
}}

function render() {{
    const panel = document.getElementById('wordsPanel');
    panel.innerHTML = '';

    const isLeadIn = (idx) => pageStartIdx !== null && idx < pageStartIdx;

    allWords.forEach((entry, idx) => {{
        const span = document.createElement('span');
        span.className = 'word';
        span.textContent = entry.text;
        span.dataset.idx = idx;

        const endsMaqaf = entry.text.endsWith(MAQAF);
        const prevEndsMaqaf = idx > 0 && allWords[idx - 1].text.endsWith(MAQAF);
        if (endsMaqaf) span.classList.add('maqaf-end');
        if (prevEndsMaqaf) span.classList.add('after-maqaf');

        if (isLeadIn(idx)) {{
            span.classList.add('lead-in');
        }} else if (entry.isParashah) {{
            span.classList.add('parashah');
            span.addEventListener('click', () => toggleLineEnd(idx));
        }} else {{
            if (entry.isVerseStart) {{
                span.classList.add('verse-start');
                span.title = entry.verseLabel;
            }}
            span.addEventListener('click', () => toggleLineEnd(idx));
        }}

        // Page-start marker
        if (pageStartIdx === idx) {{
            span.classList.add('page-start');
        }}

        // Right-click to set/clear page-start
        span.addEventListener('contextmenu', (e) => {{
            e.preventDefault();
            togglePageStart(idx);
        }});

        const leInfo = lineEndMap.get(idx);
        if (leInfo && !isLeadIn(idx)) {{
            span.classList.add('line-end');
            span.title = `Col ${{leInfo.col}}, Line ${{leInfo.lineNum}}`;
        }}

        panel.appendChild(span);

        // Page-start label
        if (pageStartIdx === idx) {{
            const lbl = document.createElement('span');
            lbl.className = 'page-start-label';
            lbl.textContent = '\u25C0 page start';
            panel.appendChild(lbl);
        }}

        if (leInfo && !isLeadIn(idx)) {{
            const colLbl = document.createElement('span');
            colLbl.className = 'col-label';
            colLbl.textContent = `c${{leInfo.col}}`;

            const ln = document.createElement('span');
            ln.className = 'line-num';
            ln.textContent = leInfo.lineNum;

            panel.appendChild(colLbl);
            panel.appendChild(ln);
            panel.appendChild(document.createElement('br'));
        }}
    }});

    updateStatus();
}}

function toggleLineEnd(idx) {{
    if (lineEndMap.has(idx)) {{
        lineEndMap.delete(idx);
    }} else {{
        const col = currentCol();
        lineEndMap.set(idx, {{col: col, lineNum: 0}});
    }}
    recalcLineNums();
    render();
}}

function togglePageStart(idx) {{
    if (pageStartIdx === idx) {{
        pageStartIdx = null;  // clear it
    }} else {{
        pageStartIdx = idx;
        // Remove any line-end markers on lead-in words
        for (const [k, _] of lineEndMap) {{
            if (k < idx) lineEndMap.delete(k);
        }}
        recalcLineNums();
    }}
    render();
}}

function updateStatus() {{
    const counts = {{}};
    lineEndMap.forEach(info => {{
        counts[info.col] = (counts[info.col] || 0) + 1;
    }});
    const parts = Object.entries(counts)
        .sort((a, b) => a[0] - b[0])
        .map(([c, n]) => `Col ${{c}}: ${{n}} lines`);
    const psInfo = pageStartIdx !== null ? `Page start: word ${{pageStartIdx}}` : 'No page start set';
    document.getElementById('status').textContent =
        psInfo + (parts.length ? ' | ' + parts.join(' | ') : '');
}}

function buildExportStream() {{
    // Rebuild the stream: take baseStream and insert line-start/line-end
    // around the words according to lineEndMap.
    const sorted = [...lineEndMap.entries()].sort((a, b) => a[0] - b[0]);
    const endSet = new Map();
    sorted.forEach(([idx, info]) => endSet.set(idx, info));

    // Compute line-start indices for each column
    const byCols = {{}};
    sorted.forEach(([idx, info]) => {{
        if (!byCols[info.col]) byCols[info.col] = [];
        byCols[info.col].push(idx);
    }});

    const startSet = new Map(); // wordIdx -> {{col, lineNum}}
    for (const col in byCols) {{
        const ends = byCols[col];
        for (let i = 0; i < ends.length; i++) {{
            let startIdx;
            if (i === 0) {{
                if (parseInt(col) === 1 && pageStartIdx !== null) {{
                    // Col 1 line 1 starts at the page-start word
                    startIdx = pageStartIdx;
                }} else {{
                    // First line of this col: after the last line-end
                    // from another col that comes before this col's first end
                    const allEndsBefore = sorted.filter(([eidx, _]) => eidx < ends[i]);
                    if (allEndsBefore.length > 0) {{
                        startIdx = allEndsBefore[allEndsBefore.length - 1][0] + 1;
                    }} else {{
                        startIdx = pageStartIdx !== null ? pageStartIdx : 0;
                    }}
                }}
            }} else {{
                startIdx = ends[i - 1] + 1;
            }}
            const lineNum = lineEndMap.get(ends[i]).lineNum;
            startSet.set(startIdx, {{col: parseInt(col), lineNum: lineNum}});
        }}
    }}

    const result = [];
    let wordIdx = 0;

    for (const item of baseStream) {{
        if (typeof item === 'string' || (typeof item === 'object' && item !== null && 'parashah' in item)) {{
            if (startSet.has(wordIdx)) {{
                const info = startSet.get(wordIdx);
                result.push({{"line-start": {{"col": info.col, "line-num": info.lineNum}}}});
            }}
            result.push(item);
            if (endSet.has(wordIdx)) {{
                const info = endSet.get(wordIdx);
                result.push({{"line-end": {{"col": info.col, "line-num": info.lineNum}}}});
            }}
            wordIdx++;
        }} else {{
            result.push(item);
        }}
    }}

    return result;
}}

function toggleSkinnyMode() {{
    isSkinnyMode = !isSkinnyMode;
    const img = document.querySelector('.col-image img');
    const css = isSkinnyMode ? IMG_CSS_SKINNY : IMG_CSS_NORMAL;
    img.style.cssText = css + ' cursor: crosshair;';
    document.getElementById('skinnyBtn').textContent =
        isSkinnyMode ? 'Go wide' : 'Go skinny';
}}

function exportJSON() {{
    const stream = buildExportStream();
    const jsonStr = JSON.stringify(stream, null, 2) + '\\n';
    navigator.clipboard.writeText(jsonStr).then(() => {{
        document.getElementById('status').textContent = 'Copied to clipboard!';
        setTimeout(updateStatus, 2000);
    }}).catch(err => {{
        const ta = document.createElement('textarea');
        ta.value = jsonStr;
        ta.style.cssText = 'position:fixed;top:10%;left:10%;width:80%;height:80%;z-index:999;font-size:12px;';
        document.body.appendChild(ta);
        ta.select();
        document.getElementById('status').textContent = 'Clipboard failed \\u2014 select all and copy manually';
    }});
}}

render();

// Auto-scroll: if editing col 2 and col 1 markers exist, scroll to
// show the last col 1 line-end (so user is "ready for col 2").
if (CURRENT_COL === 2) {{
    const col1Ends = [...lineEndMap.entries()]
        .filter(([_, info]) => info.col === 1)
        .sort((a, b) => a[0] - b[0]);
    if (col1Ends.length > 0) {{
        const lastCol1Idx = col1Ends[col1Ends.length - 1][0];
        const el = document.querySelector(`.word[data-idx="${{lastCol1Idx}}"]`);
        if (el) {{
            const panel = document.getElementById('wordsPanel');
            panel.scrollTop = el.offsetTop - 40;
        }}
    }}
}}

// --- Resizable divider ---
(function() {{
    const container = document.getElementById('container');
    const words = document.getElementById('wordsPanel');
    const divider = document.getElementById('divider');
    const image = document.getElementById('imagePanel');
    // Default 45/55
    let wordsPct = 45;
    words.style.flex = '0 0 ' + wordsPct + '%';
    image.style.flex = '1 1 0%';
    let dragging = false;
    divider.addEventListener('mousedown', (e) => {{
        e.preventDefault();
        dragging = true;
        divider.classList.add('active');
    }});
    document.addEventListener('mousemove', (e) => {{
        if (!dragging) return;
        const rect = container.getBoundingClientRect();
        // RTL layout: words panel is on the right, image on the left
        let pct = ((rect.right - e.clientX) / rect.width) * 100;
        pct = Math.max(10, Math.min(pct, 80));
        wordsPct = pct;
        words.style.flex = '0 0 ' + pct + '%';
    }});
    document.addEventListener('mouseup', () => {{
        if (dragging) {{
            dragging = false;
            divider.classList.remove('active');
        }}
    }});
}})();
</script>
</body>
</html>
'''


def main():
    if len(sys.argv) < 3:
        print("Usage: python py_ac_loc/gen_line_break_editor.py <page_id> <col>")
        print("  e.g. python py_ac_loc/gen_line_break_editor.py 270v 1")
        print("  col 1 = right column, col 2 = left column")
        sys.exit(1)
    page_id = sys.argv[1]
    col = int(sys.argv[2])
    out_path = generate_editor_html(page_id, col)
    import webbrowser
    webbrowser.open(str(out_path))


if __name__ == "__main__":
    main()
