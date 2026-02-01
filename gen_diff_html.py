"""Generate HTML comparison table of consensus vs proposed values using difflib.

This script reads directly from the source qr_*.py files to avoid Unicode normalization issues.
"""

import sys
import unicodedata
from difflib import SequenceMatcher

sys.path.insert(0, 'pyauthor_qr')

# List of records that have qr-lc-proposed
record_names = [
    'qr_0617', 'qr_0627', 'qr_0720', 'qr_0802', 'qr_1209', 'qr_1606', 'qr_1703',
    'qr_2001', 'qr_2107', 'qr_2115', 'qr_2210', 'qr_2224', 'qr_2413', 'qr_2418',
    'qr_2709', 'qr_2903', 'qr_3102', 'qr_3120', 'qr_3211', 'qr_3328', 'qr_3405',
    'qr_3433_A', 'qr_3433_B', 'qr_3433_C', 'qr_3433_D', 'qr_3437', 'qr_3507',
    'qr_3829', 'qr_3915', 'qr_3925', 'qr_4019_B'
]

# Load data directly from source files
changes = []
for rec in record_names:
    mod = __import__(rec)
    rec_name = 'RECORD_' + rec[3:]
    data = getattr(mod, rec_name)
    if 'qr-lc-proposed' in data:
        changes.append((
            rec,
            data['qr-consensus'],
            data['qr-lc-proposed'],
            data.get('qr-what-is-weird', '')
        ))

def char_info(ch):
    """Get Unicode info for a character."""
    cp = ord(ch)
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "(unknown)"
    return f"U+{cp:04X}", name

def char_display(ch):
    """Get display string for a character."""
    if not ch:
        return ""
    cp = f"U+{ord(ch):04X}"
    if ch.strip():
        return ch
    return f"({cp})"

def get_diff_opcodes(consensus, proposed):
    """Use SequenceMatcher to get opcodes for the diff."""
    matcher = SequenceMatcher(None, list(consensus), list(proposed))
    return matcher.get_opcodes()

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>qr-consensus vs qr-lc-proposed comparison</title>
<style>
body { font-family: sans-serif; margin: 20px; }
h1 { color: #333; }
h2 { color: #555; margin-top: 30px; border-bottom: 1px solid #ccc; padding-bottom: 5px; }
.hebrew { font-size: 24px; font-family: "SBL Hebrew", "Ezra SIL", serif; direction: rtl; }
table { border-collapse: collapse; margin: 10px 0; }
th, td { border: 1px solid #ccc; padding: 4px 8px; text-align: left; }
th { background: #f0f0f0; }
.diff-delete { background-color: #ffcccc; }
.diff-insert { background-color: #ccffcc; }
.diff-replace-old { background-color: #ffddaa; }
.diff-replace-new { background-color: #aaddff; }
.diff-equal { background-color: #f9f9f9; color: #999; }
.codepoint { font-family: monospace; }
.char { font-size: 18px; font-family: "SBL Hebrew", "Ezra SIL", serif; }
.summary { margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 4px; }
.op-tag { font-weight: bold; font-size: 11px; }
</style>
</head>
<body>
<h1>qr-consensus vs qr-lc-proposed: Character-by-character comparison</h1>
<p>Legend: 
<span style="background:#ffcccc;padding:2px 6px;">Delete (in consensus only)</span> 
<span style="background:#ccffcc;padding:2px 6px;">Insert (in proposed only)</span>
<span style="background:#ffddaa;padding:2px 6px;">Replace from</span> →
<span style="background:#aaddff;padding:2px 6px;">Replace to</span>
</p>
"""

for file_id, consensus, proposed, what_is_weird in changes:
    html += f'<h2>{file_id}</h2>\n'
    html += f'<div class="summary">'
    html += f'<strong>What is weird:</strong> {what_is_weird}<br>'
    html += f'<strong>Proposed:</strong> <span class="hebrew">{proposed}</span><br>'
    html += f'<strong>Consensus:</strong> <span class="hebrew">{consensus}</span>'
    html += f'</div>\n'
    
    opcodes = get_diff_opcodes(consensus, proposed)
    
    html += '<table>\n'
    html += '<tr><th>Op</th><th>Char</th><th class="codepoint">Code</th><th>Name</th></tr>\n'
    
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == 'equal':
            # Show equal sections dimmed
            for idx in range(i1, i2):
                ch = consensus[idx]
                cp, name = char_info(ch)
                disp = char_display(ch)
                html += f'<tr class="diff-equal">'
                html += f'<td class="op-tag">=</td>'
                html += f'<td class="char">{disp}</td>'
                html += f'<td class="codepoint">{cp}</td>'
                html += f'<td>{name}</td>'
                html += f'</tr>\n'
        elif tag == 'delete':
            # Characters in consensus but not in proposed
            for idx in range(i1, i2):
                ch = consensus[idx]
                cp, name = char_info(ch)
                disp = char_display(ch)
                html += f'<tr class="diff-delete">'
                html += f'<td class="op-tag">−</td>'
                html += f'<td class="char">{disp}</td>'
                html += f'<td class="codepoint">{cp}</td>'
                html += f'<td>{name}</td>'
                html += f'</tr>\n'
        elif tag == 'insert':
            # Characters in proposed but not in consensus
            for idx in range(j1, j2):
                ch = proposed[idx]
                cp, name = char_info(ch)
                disp = char_display(ch)
                html += f'<tr class="diff-insert">'
                html += f'<td class="op-tag">+</td>'
                html += f'<td class="char">{disp}</td>'
                html += f'<td class="codepoint">{cp}</td>'
                html += f'<td>{name}</td>'
                html += f'</tr>\n'
        elif tag == 'replace':
            # Characters replaced: show old then new
            for idx in range(i1, i2):
                ch = consensus[idx]
                cp, name = char_info(ch)
                disp = char_display(ch)
                html += f'<tr class="diff-replace-old">'
                html += f'<td class="op-tag">−</td>'
                html += f'<td class="char">{disp}</td>'
                html += f'<td class="codepoint">{cp}</td>'
                html += f'<td>{name}</td>'
                html += f'</tr>\n'
            for idx in range(j1, j2):
                ch = proposed[idx]
                cp, name = char_info(ch)
                disp = char_display(ch)
                html += f'<tr class="diff-replace-new">'
                html += f'<td class="op-tag">+</td>'
                html += f'<td class="char">{disp}</td>'
                html += f'<td class="codepoint">{cp}</td>'
                html += f'<td>{name}</td>'
                html += f'</tr>\n'
    
    html += '</table>\n'

html += """
</body>
</html>
"""

with open("diff_comparison.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated diff_comparison.html")
