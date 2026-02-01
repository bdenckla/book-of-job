"""Generate HTML comparison table of consensus vs proposed values using difflib."""

import unicodedata
from difflib import SequenceMatcher

# Data extracted from git diff: (file_id, consensus, proposed, what_is_weird)
changes = [
    ("qr_0617", "בְּעֵ֣ת", "בְּ֭עֵת", "dexi not munax"),
    ("qr_0627", "עַֽל־רֵיעֲכֶֽם׃", "עַל־רֵֽיעֲכֶֽם׃", "געיה on רי not על"),
    ("qr_0720", "הָ֫אָדָ֥ם", "הָאָ֫דָ֥ם", "oleh on א not ה (noted by MAM but perhaps the note should mention LC)"),
    ("qr_0802", "כַּ֝בִּ֗יר", "כַּ֝בִּיר", "revia of g. m. is left implicit"),
    ("qr_1209", "יַד־יְ֝הֹוָ֗ה", "יַד־יְ֝הֹוָה", "revia of g. m. is left implicit"),
    ("qr_1606", "מַה־מִּנִּ֥י", "מַה־מִנִּ֥י", "מ lacks dagesh (DM footnote 25)"),
    ("qr_1703", "עׇרְבֵ֣נִי", "עַרְבֵ֣נִי", "פתח not קמץ (קטן) (opposite of 3:4)"),
    ("qr_2001", "הַֽנַּעֲמָתִ֗י", "הַנַּֽעֲמָתִ֗י", "געיה on נ not ה"),
    ("qr_2107", "מַ֭דּוּעַ", "מַ֣דּוּעַ", "munax not dexi"),
    ("qr_2115", "מַה־שַּׁדַּ֥י", "מַה־שַׁדַּ֥י", "ש lacks dagesh (DM footnote 25)"),
    ("qr_2210", "וִ֝יבַהֶלְךָ֗", "וִ֝יבַהֶלְךָ", "revia of g. m. is left implicit"),
    ("qr_2224", "וּכְצ֖וּר", "וּבְצ֖וּר", "bet not kaf"),
    ("qr_2413", "בְּֽמֹרְדֵ֫י א֥וֹר", "בְּֽמֹרְדֵ֫י־א֥וֹר", "maqaf is present. Gray maqaf in MAM. Perhaps MAM should note maqaf in L."),
    ("qr_2418", "לֹא־יִ֝פְנֶ֗ה", "לֹא־יִ֝פְנֶה", "revia of g. m. is left implicit"),
    ("qr_2709", "הֲֽ֭צַעֲקָתוֹ", "הַֽ֭צַעֲקָתוֹ", "patax is full not חטף (DM footnotes 19 & 20)"),
    ("qr_2903", "לְ֝אוֹר֗וֹ", "לְ֝אוֹרוֹ", "revia of g. m. is left implicit"),
    ("qr_3102", "וּמֶ֤ה", "וּמֶ֤ה׀", "has legarmeh. Noted by MAM."),
    ("qr_3120", "כְּ֝בָשַׂ֗י", "כְּ֝בָשַׂי", "revia of g. m. is left implicit"),
    ("qr_3211", "הוֹחַ֨לְתִּי׀", "הוֹחַ֨לְתִּי", "lacks legarmeh. (DM footnotes 19 & 32)"),
    ("qr_3328", "וְ֝חַיָּת֗וֹ", "וְ֝חַיָּתוֹ", "revia of g. m. is left implicit (qere shown)"),
    ("qr_3405", "כִּֽי־אָמַ֣ר", "כִּֽי־אָ֭מַר", "dexi not munax"),
    ("qr_3433_A", "הֲֽמֵעִמְּךָ֬", "הַֽמֵעִמְּךָ֬", "patax is full not חטף (DM footnotes 19 & 20)"),
    ("qr_3433_B", "יְשַׁלְּמֶ֨נָּה׀", "יְשַׁלְמֶ֨נָּה׀", "lamed lacks dagesh"),
    ("qr_3433_C", "יְשַׁלְּמֶ֨נָּה׀", "יְשַׁלְּמֶ֨נָּה", "lacks legarmeh. (DM footnote 32)"),
    ("qr_3433_D", "וּֽמַה־יָּדַ֥עְתָּ", "וּֽמַה־יָדַ֥עְתָּ", "lacks dagesh in yod (DM footnote 25)"),
    ("qr_3437", "יִשְׂפּ֑וֹק", "יִסְפּ֑וֹק", "has samekh not shin. Perhaps this is more likely a quirk in Aleppo, not a quirk in Leningrad?"),
    ("qr_3507", "מַה־מִּיָּדְךָ֥", "מַה־מִיָּדְךָ֥", "lacks dagesh in מ (DM footnote 25)"),
    ("qr_3829", "שָׁ֝מַ֗יִם", "שָׁ֝מַיִם", "revia of g. m. is left implicit"),
    ("qr_3915", "תְדוּשֶֽׁהָ׃", "תְּדוּשֶֽׁהָ׃", "tav has dagesh"),
    ("qr_3925", "שָׂ֝רִ֗ים", "שָׂ֝רִים", "revia of g. m. is left implicit"),
    ("qr_4019_B", "הָ֝עֹשׂ֗וֹ", "הָ֝עֹשׂוֹ", "revia of g. m. is left implicit"),
]

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
