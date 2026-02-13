# Procedure: Manual Line-by-Line Alignment of Aleppo Codex Pages

## Goal

Align ground truth text (extracted from mam-xml) to the physical manuscript lines visible in an Aleppo Codex page image from mgketer.org.

## Inputs

- **Ground truth text file:** `.novc/job{CC}_{V1}-{V2}.txt` — verses extracted from mam-xml, one verse per line, with verse number prefix (e.g., ` 1: ...`)
- **Page image:** Screenshot from `https://www.mgketer.org/mikra/29/{chnu}/1/mg/106` (Job = book 29), saved to `.novc/`

## Outputs

- **Alignment file:** `py_uxlc_loc/aleppo_col_lines_job{CC}.py` — a Python file with a list of `(line_number, text)` tuples recording the text content of each physical manuscript line.
- **Interactive alignment tool:** `.novc/aleppo_align_job{CC}.html` — an HTML page for the user to visually align text to the image.

## Procedure

### 1. Prepare the ground truth

Extract verses from MAM-XML into a text file. See `.github/copilot-instructions-mam-xml.md` for general MAM-XML documentation.

#### How to extract verse text for this task

The ground truth source is the MAM-XML repo at `C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam\Job.xml`.

**Extraction script pattern** (save to `.novc/` and run):

```python
import xml.etree.ElementTree as ET
from pathlib import Path

XML_PATH = r'C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam\Job.xml'
OUT_PATH = Path(__file__).parent / 'job{startCh}_{startVs}-{endCh}_{endVs}.txt'

def get_verse_text(verse_el):
    """Extract plain text from a <verse> element."""
    if 'text' in verse_el.attrib:
        return verse_el.attrib['text']
    # Complex verse: concatenate <text> children
    return ''.join(
        c.attrib['text'] for c in verse_el if c.tag == 'text'
    )

tree = ET.parse(XML_PATH)
book39 = tree.getroot()[0]  # <book39 osisID="Job">

verses = []
for child in book39:
    if child.tag != 'chapter':
        continue
    osis = child.attrib.get('osisID', '')  # e.g. "Job.34"
    ch = int(osis.split('.')[-1])
    for v in child:
        if v.tag != 'verse':
            continue
        vs = int(v.attrib['osisID'].split('.')[-1])
        if (ch, vs) >= (START_CH, START_VS) and (ch, vs) <= (END_CH, END_VS):
            text = get_verse_text(v)
            verses.append(f'{ch}:{vs}: {text}')

OUT_PATH.write_text('\n'.join(verses) + '\n', encoding='utf-8')
print(f'Wrote {len(verses)} verses to {OUT_PATH}')
```

**Key points:**
- Read from `xml-vtrad-mam/` (MAM's native versification) — not BHS or Sefaria variants.
- For simple verses, the text is in the `text` attribute of the `<verse>` element directly.
- For complex verses (containing legarmeih, paseq, ketiv/qere, etc.), concatenate the `text` attributes of all `<text>` child elements.
- The output is plain Hebrew text with vowels and accents — no HTML markup, no parashah markers, no thin-spaces.
- **Do NOT use the mam-for-sefaria CSV** (`mam-for-sefaria/out/csv/Job.csv`) — it contains HTML entities (`&thinsp;`, `&nbsp;`) and parashah markers (`{פ}`) that would need stripping. Read the XML directly instead.

### 2. Get the page image

Take a screenshot from mgketer.org and copy it to `.novc/`:

```powershell
Get-ChildItem "$env:USERPROFILE\OneDrive\Pictures\Screenshots" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
Copy-Item "$env:USERPROFILE\OneDrive\Pictures\Screenshots\<latest>.png" ".novc/aleppo_job{CC}_page.png"
```

### 3. Generate the interactive alignment HTML

Create `.novc/aleppo_align_job{CC}_col{N}.html` with:
- **Left panel (RTL):** All ground truth words as clickable elements, split at maqaf (U+05BE) boundaries so line breaks can occur at maqaf positions.
- **Right panel:** The page image loaded from `.novc/`.
- **Pre-locked lines:** Any previously confirmed line endings (shown in blue, not editable).
- **Click a word** to toggle it as the last word on a manuscript line (turns green with line number).
- **Export Python / Copy to Clipboard** buttons to generate the `COLUMN_{N}_LINES` list.
- **Truncated export:** The export only includes lines up to the last clicked line-end; remaining unassigned words are discarded.

Key design details:
- Words containing maqaf are split into separate clickable segments (the maqaf stays attached to the preceding segment).
- When exporting, segments separated by maqaf rejoin without spaces.
- Verse numbers appear as small gold superscripts for orientation.

#### Mid-verse continuation across pages

When a column starts mid-verse (i.e., the previous page/column ended partway through a verse):
- Include the **full verse** in the `verses` array but mark the lead-in words with a `leadIn` property:
  ```js
  { cv: "35:10", leadIn: ["וְֽלֹא־אָמַ֗ר", "אַ֭יֵּה", "אֱל֣וֹהַּ"], words: ["עֹשָׂ֑י", "נֹתֵ֖ן", "זְמִר֣וֹת", "בַּלָּֽיְלָה׃"] },
  ```
- The `leadIn` words render grayed out on their own line with a "(prev page)" label. They are not clickable and not included in the export.
- Only the `words` array contains the clickable text expected in the current image.

### 4. User aligns text to image

The user opens the HTML in a browser, loads the image, and clicks the last word/segment of each manuscript line. When finished, clicks **Copy to Clipboard** and pastes the result.

### 5. Record the alignment

Replace the `COLUMN_1_LINES` list in `py_uxlc_loc/aleppo_col_lines_job{CC}.py` with the pasted output.

## Line Break Heuristics

- Early verses in Job's poetic sections often fit **one verse per line**.
- Longer verses (especially prose-like ones such as v10, v19, v20) often span **two lines**.
- When a verse spills, the break often falls at an etnachta or other major accent.
- Lines can also break at a maqaf (the maqaf is the last character on the line).

## Naming Conventions

- **Ground truth file:** `.novc/job{startCh}_{startVs}-{endCh}_{endVs}.txt` (e.g., `job35_10-36_25.txt`)
- **Screenshot:** `.novc/aleppo_job{CC}_col{N}_page.png` (e.g., `aleppo_job35_col1_page.png`)
- **Alignment HTML:** `.novc/aleppo_align_job{CC}_col{N}.html`
- **Python output file:** `py_uxlc_loc/aleppo_col_lines_job{CC}.py` with `COLUMN_{N}_LINES` lists
- Each Aleppo page has two columns: column 1 = right, column 2 = left.

## Completed Alignments

- **Job 34:1–23, Column 1:** 28 lines. File: `py_uxlc_loc/aleppo_col_lines_job34.py`, `COLUMN_1_LINES`
- **Job 34:24–35:9, Column 2:** 28 lines. File: `py_uxlc_loc/aleppo_col_lines_job34.py`, `COLUMN_2_LINES`
