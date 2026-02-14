"""
Generate interactive Aleppo Codex line-alignment HTML pages.

This module produces a self-contained HTML file with:
  - Left panel: clickable ground-truth words (RTL)
  - Right panel: manuscript page image
  - Click last word of each line → export Python tuple list

Usage from a thin column-specific script::

    from pycmn.aleppo_align_html import generate_alignment_html

    generate_alignment_html(
        out_path='.novc/aleppo_align_job37_col1.html',
        image_path='aleppo_job37_col1_page.png',   # relative to HTML file
        title='Job 37:9–38:20, Column 1 (right column)',
        column_var='COLUMN_1_LINES',
        xml_path=r'C:\\...\\Job.xml',
        book='Job',
        verse_range=((37, 9), (38, 20)),
        lead_in_words=['מִן־הַ֭חֶדֶר'],  # words already on prev column
        lead_in_skip=1,                    # how many words to skip from first verse
    )

To resume alignment with previously-completed lines locked::

    generate_alignment_html(
        ...,
        locked_lines=[
            '{פ}',
            'וַיַּעַן־יְהֹוָ֣ה אֶת־אִ֭יּוֹב ...',
            ...,
        ],
    )

For book-boundary pages (column spans two books), append additional
text sources via ``extra_sources``::

    generate_alignment_html(
        ...,
        xml_path=r'C:\\...\\Job.xml',
        book='Job',
        verse_range=((42, 11), (42, 17)),
        extra_sources=[
            {
                'xml_path': r'C:\\...\\Prov.xml',
                'book': 'Prov',
                'verse_range': ((1, 1), (1, 8)),
            },
        ],
    )
"""

import json
from pathlib import Path

from pycmn.mam_xml_verses import get_verses_in_range


def generate_alignment_html(
    *,
    out_path: str,
    image_path: str,
    title: str,
    column_var: str,
    xml_path: str,
    book: str,
    verse_range: tuple,
    lead_in_words: list[str] | None = None,
    lead_in_skip: int = 0,
    locked_lines: list[str] | None = None,
    extra_sources: list[dict] | None = None,
):
    """
    Generate an interactive alignment HTML file.

    Args:
        out_path: where to write the HTML file
        image_path: path to the page image, relative to the HTML file
        title: human-readable title (e.g., 'Job 37:9–38:20, Column 1')
        column_var: Python variable name for export (e.g., 'COLUMN_1_LINES')
        xml_path: absolute path to the MAM-XML file
        book: OSIS book prefix (e.g., 'Job')
        verse_range: ((start_ch, start_vs), (end_ch, end_vs))
        lead_in_words: words from previous column shown grayed out, or None
        lead_in_skip: number of words to skip from the start of the first verse
        locked_lines: previously-aligned line texts to lock in the HTML.
            These appear as non-clickable, pre-selected lines so the user
            can resume alignment where they left off (or review/edit).
        extra_sources: additional text sources for book-boundary pages.
            Each dict has keys: 'xml_path', 'book', 'verse_range'.
            Verses from these sources are appended after the primary source.
    """
    start_cv, end_cv = verse_range
    verses = get_verses_in_range(xml_path, book, start_cv, end_cv)

    if extra_sources:
        for src in extra_sources:
            src_start, src_end = src['verse_range']
            extra_verses = get_verses_in_range(
                src['xml_path'], src['book'], src_start, src_end,
            )
            # Prefix cv labels with book name to disambiguate
            for v in extra_verses:
                v['cv'] = f"{src['book']} {v['cv']}"
            verses.extend(extra_verses)
        # Also prefix primary book cv labels when mixing books
        for v in verses:
            if not v['cv'].startswith(book + ' ') and ' ' not in v['cv']:
                v['cv'] = f"{book} {v['cv']}"

    js_verses = _build_js_verses(verses, lead_in_words, lead_in_skip)
    verses_js = ',\n'.join(js_verses)

    locked_indices_js = '[]'
    if locked_lines:
        end_indices = _compute_locked_end_indices(locked_lines)
        locked_indices_js = json.dumps(end_indices)

    html = _HTML_TEMPLATE.format(
        title=title,
        image_path=image_path,
        column_var=column_var,
        verses_js=verses_js,
        locked_indices_js=locked_indices_js,
    )

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print(f'Wrote {out}')


def _build_js_verses(verses, lead_in_words, lead_in_skip):
    """Build the JavaScript verses array entries."""
    js_verses = []

    for i, v in enumerate(verses):
        parts = []
        parts.append(f'cv: {json.dumps(v["cv"])}')

        words = v['words']
        ketiv = v['ketiv_indices']

        if i == 0 and lead_in_words:
            parts.append(f'leadIn: {json.dumps(lead_in_words, ensure_ascii=False)}')
            words = words[lead_in_skip:]
            # Adjust ketiv indices
            ketiv = [k - lead_in_skip for k in ketiv if k >= lead_in_skip]

        parts.append(f'words: {json.dumps(words, ensure_ascii=False)}')

        if ketiv:
            parts.append(f'ketivIndices: {json.dumps(ketiv)}')

        if v.get('parashah_after'):
            parts.append(f'parashahAfter: {json.dumps(v["parashah_after"], ensure_ascii=False)}')

        js_verses.append('    { ' + ', '.join(parts) + ' }')

    return js_verses


Maqaf = '\u05BE'


def _count_maqaf_segments(line_text: str) -> int:
    """Count maqaf-split segments in a line, matching the JS splitAtMaqaf logic."""
    count = 0
    for token in line_text.split():
        parts = 0
        current = ''
        for ch in token:
            current += ch
            if ch == Maqaf:
                parts += 1
                current = ''
        if current:
            parts += 1
        count += parts
    return count


def _compute_locked_end_indices(locked_lines: list[str]) -> list[int]:
    """Compute allWords end-indices for each locked line by segment counting."""
    end_indices = []
    pos = 0
    for line_text in locked_lines:
        seg_count = _count_maqaf_segments(line_text)
        end_idx = pos + seg_count - 1
        end_indices.append(end_idx)
        pos = end_idx + 1
    return end_indices


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
# Uses {{ and }} for literal braces in the f-string.
# Substitutable placeholders: {title}, {image_path}, {column_var}, {verses_js},
# {locked_indices_js}

_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<title>Aleppo Line Alignment \u2014 {title}</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Segoe UI', sans-serif; background: #1e1e1e; color: #d4d4d4; }}
h1 {{ text-align: center; padding: 12px; font-size: 18px; }}
.container {{ display: flex; height: calc(100vh - 80px); }}
.col-image {{ flex: 1; overflow: auto; border-left: 2px solid #444; padding: 8px; direction: ltr; }}
.col-image img {{ max-width: 100%; }}
.col-words {{ flex: 1; overflow-y: auto; padding: 16px; direction: rtl; }}
.word {{
    display: inline-block;
    font-size: 22px;
    font-family: 'SBL Hebrew', 'Ezra SIL', 'Times New Roman', serif;
    padding: 4px 6px;
    margin: 2px;
    cursor: pointer;
    border-radius: 4px;
    border: 1px solid transparent;
    user-select: none;
    transition: background 0.15s;
}}
.word:hover {{ background: #333; }}
.word.line-end {{
    background: #264f2a;
    border-color: #4ec94e;
    border-left: 3px solid #4ec94e;
}}
.word.locked {{
    background: #2a2a4f;
    border-color: #6666cc;
    border-left: 3px solid #6666cc;
    cursor: default;
    opacity: 0.75;
}}
.word.ketiv {{
    color: #e0b060;
}}
.word.parashah {{
    color: #e07040;
}}
.word.maqaf-end {{
    margin-left: 0;
    padding-left: 0;
    margin-right: 0;
    padding-right: 0;
}}
.word.after-maqaf {{
    margin-right: 0;
    padding-right: 0;
}}
.line-num {{
    display: inline-block;
    color: #888;
    font-size: 13px;
    font-family: monospace;
    min-width: 28px;
    text-align: center;
    direction: ltr;
    margin-left: 4px;
}}
.verse-marker {{
    display: inline-block;
    color: #e0a040;
    font-size: 12px;
    font-family: monospace;
    direction: ltr;
    margin: 0 4px;
    vertical-align: super;
}}
br.linebreak {{ }}
.lead-in {{
    display: inline-block;
    font-size: 20px;
    font-family: 'SBL Hebrew', 'Ezra SIL', 'Times New Roman', serif;
    padding: 4px 6px;
    margin: 2px;
    color: #666;
    opacity: 0.5;
    user-select: none;
}}
.lead-in-label {{
    display: inline-block;
    color: #888;
    font-size: 11px;
    font-family: monospace;
    direction: ltr;
    margin-left: 8px;
    font-style: italic;
}}
.toolbar {{
    text-align: center; padding: 8px; background: #252526;
    border-top: 1px solid #444; direction: ltr;
}}
.toolbar button {{
    padding: 8px 16px; margin: 0 4px; cursor: pointer;
    background: #0e639c; color: #fff; border: none; border-radius: 4px;
    font-size: 14px;
}}
.toolbar button:hover {{ background: #1177bb; }}
#output {{
    display: none; direction: ltr; text-align: left;
    background: #1e1e1e; color: #9cdcfe; padding: 16px;
    font-family: 'Cascadia Code', 'Consolas', monospace; font-size: 13px;
    white-space: pre-wrap; border-top: 2px solid #444;
    max-height: 300px; overflow-y: auto;
}}
</style>
</head>
<body>

<h1>Aleppo Line Alignment \u2014 {title}</h1>
<div class="container">
    <div class="col-words" id="wordsPanel"></div>
    <div class="col-image" id="imagePanel">
        <img src="{image_path}" alt="Aleppo page">
    </div>
</div>
<div class="toolbar">
    <button onclick="copyToClipboard()">Copy to Clipboard</button>
</div>
<div id="output"></div>

<script>
const COLUMN_VAR = "{column_var}";
const verses = [
{verses_js}
];

const MAQAF = '\\u05BE';
function splitAtMaqaf(word) {{
    const parts = [];
    let current = '';
    for (const ch of word) {{
        current += ch;
        if (ch === MAQAF) {{
            parts.push(current);
            current = '';
        }}
    }}
    if (current) parts.push(current);
    return parts;
}}

let allWords = [];
verses.forEach(v => {{
    v.words.forEach((w, wi) => {{
        const segments = splitAtMaqaf(w);
        const isKetiv = v.ketivIndices && v.ketivIndices.includes(wi);
        segments.forEach((seg, si) => {{
            const prevEntry = allWords.length > 0 ? allWords[allWords.length - 1] : null;
            const afterMaqaf = prevEntry && prevEntry.endsWithMaqaf;
            allWords.push({{
                word: seg,
                cv: v.cv,
                wordIdx: wi,
                segIdx: si,
                isFirstInVerse: wi === 0 && si === 0,
                endsWithMaqaf: seg.endsWith(MAQAF),
                afterMaqaf: afterMaqaf,
                isKetiv: isKetiv,
                isParashah: false,
                leadInWords: (wi === 0 && si === 0 && v.leadIn) ? v.leadIn : null,
            }});
        }});
    }});
    if (v.parashahAfter) {{
        allWords.push({{
            word: v.parashahAfter,
            cv: v.cv,
            wordIdx: -1,
            segIdx: 0,
            isFirstInVerse: false,
            endsWithMaqaf: false,
            isKetiv: false,
            isParashah: true,
            leadInWords: null,
        }});
    }}
}});

let lockedEnds = new Set();
let lineEndIndices = new Set();

function render() {{
    const panel = document.getElementById('wordsPanel');
    panel.innerHTML = '';
    let lineNum = 1;

    allWords.forEach((entry, idx) => {{
        if (entry.isFirstInVerse && entry.leadInWords) {{
            const vm = document.createElement('span');
            vm.className = 'verse-marker';
            vm.textContent = entry.cv;
            panel.appendChild(vm);
            entry.leadInWords.forEach(w => {{
                const li = document.createElement('span');
                li.className = 'lead-in';
                li.textContent = w;
                panel.appendChild(li);
            }});
            const lbl = document.createElement('span');
            lbl.className = 'lead-in-label';
            lbl.textContent = '(prev col)';
            panel.appendChild(lbl);
            panel.appendChild(document.createElement('br'));
        }}
        if (entry.isFirstInVerse && !entry.leadInWords) {{
            const vm = document.createElement('span');
            vm.className = 'verse-marker';
            vm.textContent = entry.cv;
            panel.appendChild(vm);
        }}

        const span = document.createElement('span');
        span.className = 'word';
        if (entry.endsWithMaqaf) span.classList.add('maqaf-end');
        if (entry.afterMaqaf) span.classList.add('after-maqaf');
        if (entry.isKetiv) span.classList.add('ketiv');
        if (entry.isParashah) span.classList.add('parashah');
        span.textContent = entry.word;
        span.dataset.idx = idx;

        const isLocked = lockedEnds.has(idx);
        const isLineEnd = lineEndIndices.has(idx);

        if (isLocked) {{
            span.classList.add('locked');
            span.classList.add('line-end');
            span.title = `Line ${{lineNum}} (locked)`;
        }} else if (isLineEnd) {{
            span.classList.add('line-end');
            span.title = `Line ${{lineNum}}`;
        }}

        if (!isLocked) {{
            span.addEventListener('click', () => toggleLineEnd(idx));
        }}

        panel.appendChild(span);

        if (isLineEnd) {{
            const ln = document.createElement('span');
            ln.className = 'line-num';
            ln.textContent = lineNum;
            panel.appendChild(ln);
            panel.appendChild(document.createElement('br'));
            lineNum++;
        }}
    }});
}}

function toggleLineEnd(idx) {{
    if (lockedEnds.has(idx)) return;
    if (lineEndIndices.has(idx)) {{
        lineEndIndices.delete(idx);
    }} else {{
        lineEndIndices.add(idx);
    }}
    render();
}}

function getLines() {{
    let sorted = [...lineEndIndices].sort((a, b) => a - b);
    let lines = [];
    let start = 0;
    sorted.forEach((endIdx, li) => {{
        let text = '';
        for (let i = start; i <= endIdx; i++) {{
            if (text && !text.endsWith(MAQAF)) text += ' ';
            text += allWords[i].word;
        }}
        lines.push({{ num: li + 1, text: text.trim() }});
        start = endIdx + 1;
    }});
    return lines;
}}

function copyToClipboard() {{
    const lines = getLines();
    let out = COLUMN_VAR + ' = [\\n';
    lines.forEach(l => {{
        out += `    (${{l.num}}, "${{l.text}}"),\\n`;
    }});
    out += ']\\n';
    const el = document.getElementById('output');
    el.style.display = 'block';
    el.textContent = out;
    navigator.clipboard.writeText(out).then(() => {{
        alert('Copied to clipboard!');
    }});
}}

// Apply locked (pre-selected) lines
(function() {{
    const lockedIndices = {locked_indices_js};
    lockedIndices.forEach(idx => {{
        lineEndIndices.add(idx);
        lockedEnds.add(idx);
    }});
}})();

render();
</script>
</body>
</html>
'''
