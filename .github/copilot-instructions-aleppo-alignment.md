# Procedure: Manual Line-by-Line Alignment of Aleppo Codex Pages

## Note on verification

Files in `py_ac_loc/` are **not** consumed by `main_gen_misc_authored_english_documents.py`. Changes to alignment data or alignment-related code here do **not** require running the generation script or checking `docs/` for changes.

However, after editing any `aleppo_col_lines_*.json` file, **always** run the consistency checker:

```
python py_ac_loc/check_aleppo_col_lines.py
```

This validates that all redundant/friendly fields are consistent with their machine-readable counterparts (ranges-friendly ↔ ranges, blank_lines ↔ actual blanks, pe_lines ↔ actual {פ} lines, ketiv bcv-fml-friendly ↔ bcv-fml, ketiv words present in line data, line range annotations consistent with line content, overall range ↔ column ranges, generic description).

## Goal

Align ground truth text (extracted from mam-xml) to the physical manuscript lines visible in an Aleppo Codex page image from mgketer.org.

## Inputs

- **Page index:** `C:\Users\BenDe\GitRepos\codex-index\aleppo\index-flat.json` — maps each Aleppo Codex leaf to a `[start_cv, end_cv]` text range. Key `"body"` contains the list; each entry has `de_leaf` (e.g., `"280r"`), `de_text_range` (e.g., `[["Job",37,9],["Job",38,30]]`), and `de_url`.
- **Ground truth text:** Extracted on the fly from MAM-XML via `py_ac_loc/mam_xml_verses.py`.
- **Page image:** Screenshot from one of the sources below, saved to `.novc/`

## Page Image Sources

### Primary: archive.org (page-based, recommended)

The full Aleppo Codex scan is at `https://archive.org/details/aleppo-codex` (CC0 license, 593 pages).
Each page in the scan corresponds to one leaf side (recto or verso). The URL pattern is:

```
https://archive.org/details/aleppo-codex/page/n{N}/mode/1up
```

where `N` is the 0-based page index. The mapping from leaf to page index is computed from the codex-index position. For Job leaves (all past the extra leaf 241a), the formula is:

```
N = (leaf_number - 1) × 2 + 2 + (0 for recto, 1 for verso)
```

Pre-computed mapping for all Job leaves:

```
Leaf    n     Text Range
270r    n540  Ps 149:1  – Job 1:16
270v    n541  Job 1:16  – Job 3:6
271r    n542  Job 3:6   – Job 5:10
271v    n543  Job 5:10  – Job 6:30
272r    n544  Job 7:1   – Job 9:5
272v    n545  Job 9:5   – Job 10:20
273r    n546  Job 10:20 – Job 13:2
273v    n547  Job 13:2  – Job 14:21
274r    n548  Job 14:22 – Job 16:12
274v    n549  Job 16:13 – Job 19:6
275r    n550  Job 19:7  – Job 20:26
275v    n551  Job 20:27 – Job 22:13
276r    n552  Job 22:13 – Job 24:14
276v    n553  Job 24:15 – Job 27:16
277r    n554  Job 27:16 – Job 29:14
277v    n555  Job 29:14 – Job 31:6
278r    n556  Job 31:7  – Job 32:7
278v    n557  Job 32:8  – Job 33:33
279r    n558  Job 34:1  – Job 35:10
279v    n559  Job 35:10 – Job 37:9
280r    n560  Job 37:9  – Job 38:30
280v    n561  Job 38:31 – Job 40:5
281r    n562  Job 40:6  – Job 41:22
281v    n563  Job 41:23 – Prov 1:8
```

To open a leaf for the user:
```powershell
cmd /c start "" "https://archive.org/details/aleppo-codex/page/n560/mode/1up"
```

### Secondary: mgketer.org (chapter-based)

Chapter-based viewer; useful for quick lookups but **not page-based** — inconvenient when a page spans multiple chapters.

```
https://www.mgketer.org/mikra/29/{chnu}/1/mg/106
```

(Job = book 29, `chnu` = chapter number.)

## Outputs

- **Alignment file:** `py_ac_loc/aleppo_col_lines_{leaf}.json` — one file per leaf (e.g., `aleppo_col_lines_280r.json`). See `py_ac_loc/aleppo_col_lines_format.md` for the full JSON schema documentation. Each line entry is `[line_num, range_or_null, text]` where `range_or_null` is a verse range string (e.g., `"Job 41:23"` or `"Job 35:9–35:10"`) or `null` for blank/parashah lines.
- **Interactive alignment tool:** `.novc/aleppo_align_{leaf}_col{N}.html` — an HTML page for the user to visually align text to the image.

## Page Lookup

To find the leaf for a given chapter, or what text a leaf contains:

```python
import json
with open(r'C:\Users\BenDe\GitRepos\codex-index\aleppo\index-flat.json') as f:
    pages = json.load(f)['body']
job_pages = [p for p in pages if p['de_text_range'][0][0] == 'Job' or p['de_text_range'][1][0] == 'Job']
for p in job_pages:
    tr = p['de_text_range']
    print(f"  {p['de_leaf']:6s}  {tr[0][0]} {tr[0][1]}:{tr[0][2]}  –  {tr[1][0]} {tr[1][1]}:{tr[1][2]}")
```

Job pages (for reference):
```
270r  Ps 149:1  – Job 1:16      279r  Job 34:1  – Job 35:9
270v  Job 1:16  – Job 3:6       279v  Job 35:10 – Job 37:8 (cont.)
271r  Job 3:6   – Job 5:10      280r  Job 37:9  – Job 38:30
271v  Job 5:10  – Job 6:30      280v  Job 38:31 – Job 40:5
272r  Job 7:1   – Job 9:5       281r  Job 40:6  – Job 41:22
272v  Job 9:5   – Job 10:20     281v  Job 41:23 – Prov 1:8
273r  Job 10:20 – Job 13:2
273v  Job 13:2  – Job 14:21
274r  Job 14:22 – Job 16:12
274v  Job 16:13 – Job 19:6
275r  Job 19:7  – Job 20:26
275v  Job 20:27 – Job 22:13
276r  Job 22:13 – Job 24:14
276v  Job 24:15 – Job 27:16
277r  Job 27:16 – Job 29:14
277v  Job 29:14 – Job 31:6
278r  Job 31:7  – Job 32:7
278v  Job 32:8  – Job 33:33
```

## Procedure

### 1. Prepare the ground truth

Use the reusable extraction module `py_ac_loc/mam_xml_verses.py`:

```python
from py_ac_loc.mam_xml_verses import get_verses_in_range

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

Download a hi-res image from archive.org's direct image API, then crop to the relevant column using Pillow.

**Direct image API URL:**
```
https://ia601801.us.archive.org/BookReader/BookReaderImages.php?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{NNNN}.jp2&id=aleppo-codex&scale={S}&rotate=0
```
- `{NNNN}` = zero-padded page number from the leaf mapping table above (e.g., `0560` for 280r)
- `{S}` = scale factor: `1` = hi-res (~2.5 MB), `2` = medium (~800 KB)

**Download and crop script (Python):**
```python
import urllib.request
from PIL import Image

LEAF = '281r'
N = 562  # from leaf mapping table
url = f'https://ia601801.us.archive.org/BookReader/BookReaderImages.php?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{N:04d}.jp2&id=aleppo-codex&scale=1&rotate=0'

# Download full page
page_path = f'.novc/aleppo_{LEAF}_page_hires.jpg'
urllib.request.urlretrieve(url, page_path)

# Crop to columns
img = Image.open(page_path)
w, h = img.size
img.crop((int(w * 0.4), 0, w, h)).save(f'.novc/aleppo_{LEAF}_col1.jpg')   # col1 = right 60%
img.crop((0, 0, int(w * 0.6), h)).save(f'.novc/aleppo_{LEAF}_col2.jpg')   # col2 = left 60%
```

Column 1 is the **right** column (crop right 60%), column 2 is the **left** column (crop left 60%).

**Fallback: mgketer.org screenshot:**
```powershell
Get-ChildItem "$env:USERPROFILE\OneDrive\Pictures\Screenshots" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
Copy-Item "$env:USERPROFILE\OneDrive\Pictures\Screenshots\<latest>.png" ".novc/aleppo_{leaf}_col{N}_page.png"
```

### 3. Generate the interactive alignment HTML

Use the reusable module `py_ac_loc/aleppo_align_html.py`. Create a thin column-specific script in `.novc/`:

```python
"""Generate alignment HTML for leaf NNNx Column M."""
import sys
sys.path.insert(0, r'C:\Users\BenDe\GitRepos\book-of-job')

from py_ac_loc.aleppo_align_html import generate_alignment_html

MAM_XML = r'C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam\Job.xml'

generate_alignment_html(
    out_path=r'.novc\aleppo_align_{leaf}_colM.html',
    image_path='aleppo_{leaf}_colM_page.png',
    title='Leaf NNNx, Job X:Y–A:B, Column M (right/left column)',
    column_key='column_m_lines',
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
- **Copy to Clipboard** exports the `column_{n}_lines` JSON array.

#### Parashah markers

Petuxah (`{פ}`) and setumah (`{ס}`) breaks from the MAM-XML appear inline as clickable words. When a parashah break causes a blank line in the manuscript, click the last real word of the line before it, then click the `{פ}`/`{ס}` marker itself. The exported line will contain `"{פ}"` (not an empty string).

#### Mid-verse continuation across pages

When a column starts mid-verse, pass `lead_in_words` (the words already on the previous column) and `lead_in_skip` (how many words to skip from the first verse). The lead-in words render grayed out with a "(prev col)" label and are not clickable.

#### Cross-page parashah breaks

When the previous page ends with a parashah break (e.g., `{פ}` after 40:5 on 280v), the new page may start with a blank line. To handle this:
1. Start `verse_range` at the verse with the trailing parashah (e.g., `(40, 5)`).
2. Pass all of that verse's words as `lead_in_words` (grayed out, not clickable).
3. Set `lead_in_skip` to the word count.
4. The `{פ}` marker itself remains clickable — click it to mark the blank line.

#### Tight maqaf display

Maqaf-joined word parts display with zero gap between them but each part remains independently clickable. This is handled automatically by the CSS classes `maqaf-end` (on the part ending with maqaf) and `after-maqaf` (on the following part). No special configuration needed.

#### Book-boundary pages

When a column spans two books (e.g., 281v col2: Job 42:11–42:17 + Prov 1:1–1:8), use the `extra_sources` parameter instead of writing an ad-hoc script:

```python
MAM_XML_DIR = r'C:\Users\BenDe\GitRepos\MAM-XML\out\xml-vtrad-mam'

generate_alignment_html(
    out_path=r'.novc\aleppo_align_281v_col2.html',
    image_path='aleppo_281v_col2.jpg',
    title='Leaf 281v, Job 42:11–Prov 1:8, Column 2',
    column_key='column_2_lines',
    xml_path=rf'{MAM_XML_DIR}\Job.xml',
    book='Job',
    verse_range=((42, 11), (42, 17)),
    extra_sources=[
        {
            'xml_path': rf'{MAM_XML_DIR}\Prov.xml',
            'book': 'Prov',
            'verse_range': ((1, 1), (1, 8)),
        },
    ],
)
```

This concatenates the verses from all sources, prefixing cv labels with the book name (e.g., `"Job 42:11"`, `"Prov 1:1"`) so the user can see the book boundary in the alignment UI.

**Book-boundary pages in the Aleppo Codex** (20 total across the Tanakh). The two that involve Job are:
- `270r`: Ps 149:1 – Job 1:16
- `281v`: Job 41:23 – Prov 1:8

After alignment, insert blank lines in the output file at the book boundary to represent the physical gap in the manuscript (e.g., 2 blank lines between Job 42:17 and Prov 1:1 on leaf 281v col2). Use empty strings `""` for blank line text.

### 4. User aligns text to image

The user opens the HTML in a browser, loads the image, and clicks the last word/segment of each manuscript line. When finished, clicks **Copy to Clipboard** and pastes the result.

### 5. Record the alignment

Replace the `column_{n}_lines` array in `py_ac_loc/aleppo_col_lines_{leaf}.json` with the pasted output.

**Note:** The clipboard export from `aleppo_align_html.py` produces 2-element entries `[line_num, text]`. After pasting, run the range annotation script (`.novc/add_line_ranges.py`) to convert these to 3-element entries `[line_num, range_or_null, text]` with verse range annotations derived from the MAM-XML ground truth.

After updating the line data, also update the column metadata (`ranges`, `ranges-friendly`, `line_count`, `blank_lines`, `pe_lines`, `ketivs`, `notes`) and the top-level fields (`overall range (all columns)`, `MAM-XML source file(s)`, `page_image`). See `py_ac_loc/aleppo_col_lines_format.md` for the full schema.

Then run the consistency checker:

```
python py_ac_loc/check_aleppo_col_lines.py
```

## Line Break Heuristics

- Early verses in Job's poetic sections often fit **one verse per line**.
- Longer verses (especially prose-like ones such as v10, v19, v20) often span **two lines**.
- When a verse spills, the break often falls at an etnachta or other major accent.
- Lines can also break at a maqaf (the maqaf is the last character on the line).

## Naming Conventions

- **Full page image:** `.novc/aleppo_{leaf}_page_hires.jpg` (e.g., `aleppo_281r_page_hires.jpg`)
- **Cropped column image:** `.novc/aleppo_{leaf}_col{N}.jpg` (e.g., `aleppo_281r_col1.jpg`)
- **Alignment HTML:** `.novc/aleppo_align_{leaf}_col{N}.html` (e.g., `aleppo_align_280r_col1.html`)
- **JSON output file:** `py_ac_loc/aleppo_col_lines_{leaf}.json` (e.g., `aleppo_col_lines_280r.json`) with `column_1_lines` and `column_2_lines`
- Each Aleppo page has two columns: column 1 = right, column 2 = left.
- The `{leaf}` identifier (e.g., `279r`, `280v`) comes from the Aleppo Codex index (`codex-index/aleppo/index-flat.json`).

## Completed Alignments

All details (ranges, blank lines, pe lines, ketivs, notes) are in the JSON files
themselves. See `py_ac_loc/aleppo_col_lines_format.md` for the schema.

| Leaf | Overall Range | File |
|------|---------------|------|
| 270r | Ps 149:1-first – Job 1:16-last | `aleppo_col_lines_270r.json` |
| 278v | Job 32:8-first – Job 33:33-first | `aleppo_col_lines_278v.json` |
| 279r | Job 34:1-first – Job 35:9-first | `aleppo_col_lines_279r.json` |
| 279v | Job 35:10-first – Job 37:8-first | `aleppo_col_lines_279v.json` |
| 280r | Job 37:9-mid – Job 38:30-first | `aleppo_col_lines_280r.json` |
| 280v | Job 38:31-first – Job 40:5-first | `aleppo_col_lines_280v.json` |
| 281r | Job 40:6-first – Job 41:22-first | `aleppo_col_lines_281r.json` |
| 281v | Job 41:23-first – Prov 1:8-first | `aleppo_col_lines_281v.json` |
