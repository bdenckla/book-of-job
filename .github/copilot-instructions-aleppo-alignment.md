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

Use the reusable extraction module `pycmn/mam_xml_verses.py`:

```python
from pycmn.mam_xml_verses import get_verses_in_range

verses = get_verses_in_range(
    r'C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam\Job.xml',
    'Job', (37, 9), (38, 20),
)
```

This handles all special MAM-XML elements:
- `<text>`: plain text spans
- `<lp-legarmeih>`, `<lp-paseq>`: appends paseq (U+05C0) to preceding word
- `<kq>`: ketiv/qere — uses ketiv (`kq-k` child, unpointed) for manuscript alignment
- `<kq-trivial>`: uses `text` attribute (pointed)
- `<slh-word>`: suspended-letter word — uses `slhw-desc-0` (full pointed word)
- `<implicit-maqaf>`: no visible text, skipped
- `<spi-pe2>`, `<spi-samekh2>`: parashah breaks — returned as `parashah_after` field

Each verse dict contains:
- `cv`: chapter:verse string (e.g., `'37:9'`)
- `words`: list of maqaf-joined words
- `ketiv_indices`: indices of words that are ketiv (unpointed)
- `parashah_after`: `None`, `'{פ}'`, or `'{ס}'`

**Key points:**
- Read from `xml-vtrad-mam/` (MAM's native versification).
- For Aleppo alignment, only **ketiv** matters — it's the unpointed text visible in the manuscript's main column.
- **Do NOT use the mam-for-sefaria CSV** — it contains HTML entities and parashah markers that would need stripping.

### 2. Get the page image

Take a screenshot from mgketer.org and copy it to `.novc/`:

```powershell
Get-ChildItem "$env:USERPROFILE\OneDrive\Pictures\Screenshots" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
Copy-Item "$env:USERPROFILE\OneDrive\Pictures\Screenshots\<latest>.png" ".novc/aleppo_job{CC}_page.png"
```

### 3. Generate the interactive alignment HTML

Use the reusable module `pycmn/aleppo_align_html.py`. Create a thin column-specific script in `.novc/`:

```python
"""Generate alignment HTML for Job NN Column M."""
import sys
sys.path.insert(0, r'C:\Users\BenDe\GitRepos\book-of-job')

from pycmn.aleppo_align_html import generate_alignment_html

MAM_XML = r'C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam\Job.xml'

generate_alignment_html(
    out_path=r'.novc\aleppo_align_jobNN_colM.html',
    image_path='aleppo_jobNN_colM_page.png',
    title='Job X:Y–A:B, Column M (right/left column)',
    column_var='COLUMN_M_LINES',
    xml_path=MAM_XML,
    book='Job',
    verse_range=((X, Y), (A, B)),
    lead_in_words=['...'],  # words from prev column, or omit if starts at verse boundary
    lead_in_skip=1,         # how many words to skip from first verse
)
```

The generated HTML includes:
- **Left panel (RTL):** All ground truth words as clickable elements, split at maqaf (U+05BE) boundaries.
- **Right panel:** The page image.
- **Ketiv words** styled in gold.
- **Parashah markers** (`{פ}`, `{ס}`) shown inline as clickable orange pseudo-words.
- **Click a word** to toggle it as the last word on a manuscript line (turns green with line number).
- **Copy to Clipboard** exports the `COLUMN_{N}_LINES` Python list.

#### Parashah markers

Petuxah (`{פ}`) and setumah (`{ס}`) breaks from the MAM-XML appear inline as clickable words. When a parashah break causes a blank line in the manuscript, click the last real word of the line before it, then click the `{פ}`/`{ס}` marker itself. The exported line will contain `"{פ}"` (not an empty string).

#### Mid-verse continuation across pages

When a column starts mid-verse, pass `lead_in_words` (the words already on the previous column) and `lead_in_skip` (how many words to skip from the first verse). The lead-in words render grayed out with a "(prev col)" label and are not clickable.

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
- **Job 35:10–36:18 (partial), Column 1:** 28 lines. File: `py_uxlc_loc/aleppo_col_lines_job35.py`, `COLUMN_1_LINES`
- **Job 36:18 (cont.)–37:8, Column 2:** 28 lines. File: `py_uxlc_loc/aleppo_col_lines_job35.py`, `COLUMN_2_LINES`
- **Job 37:9 (cont.)–38:6, Column 1:** 28 lines (line 21 = `"{פ}"` pe break). File: `py_uxlc_loc/aleppo_col_lines_job37.py`, `COLUMN_1_LINES`
