# Procedure: Generating Aleppo Codex Word Crops for Quirkrecs

This describes the workflow for supplying μA (Aleppo Codex) word-level
image crops to quirkrecs that lack them. It replaces the old manual
screenshot workflow (in `copilot-instructions-aleppo-images.md`) with a
semi-automated approach that uses the column-coordinate and line-break
data already captured for all 24 Job pages.

## Overview

143 of the 156 quirkrecs are missing a `qr-aleppo-img`. The goal is to
supply these by:

1. Looking up each quirkrec's verse+word in the line-break data → page,
   column, line number, word index within that line
2. Looking up that page/col/line in the column-coordinate data → pixel
   bounding box for the line
3. Opening an interactive crop editor (served as local HTML) that shows
   the relevant line from the archive.org image with the target word
   highlighted, and lets the user adjust the crop rectangle
4. Exporting the crop as a PNG saved to `docs/jobn/img/Aleppo-{sid}.png`

## Prerequisites

All 24 Job pages (270r–281v) must have:
- Line-break data in `py_ac_loc/line-breaks/{page}.json`
- Column-coordinate data in `py_ac_loc/column-coordinates/{page}.json`

Both are already complete.

## Data flow

```
quirkrec (qr-cv, qr-consensus)
  → line-break files → page, col, line-num, word position within line
  → column-coordinate files → pixel bbox for that line
  → archive.org image URL (scale=1 for hi-res)
  → interactive crop editor → user adjusts crop → saves PNG
```

## Key data sources

### Line-break files (`py_ac_loc/line-breaks/{page}.json`)

Flat JSON arrays interleaving structural markers and Hebrew words.
Each word sits between `line-start` and `line-end` markers that record
`col` (1=right, 2=left) and `line-num` (1–28). Verse boundaries are
marked with `verse-start` / `verse-end` / `verse-fragment-start` /
`verse-fragment-end`.

To find a word: scan for the `verse-start` (or `verse-fragment-start`)
matching the quirkrec's chapter:verse, then locate the word matching
`qr-consensus` (stripping cantillation/vowels for comparison if needed).
The surrounding `line-start` marker gives col and line-num.

### Column-coordinate files (`py_ac_loc/column-coordinates/{page}.json`)

JSON with `columns.col1` and `columns.col2`, each having `px` (pixel)
coordinates: `x, y, w, h, top_angle, bot_angle, line_spacing`.

To get pixel bbox for line L of column C:
```
col = columns["col" + str(C)]
line_top_y = col.px.y + (L - 1) * col.px.line_spacing
line_bot_y = line_top_y + col.px.line_spacing
line_left_x = col.px.x
line_right_x = col.px.x + col.px.w
```
(Skew angles can refine this if needed.)

### Archive.org image URL

```
https://ia601801.us.archive.org/BookReader/BookReaderImages.php?zip=/7/items/aleppo-codex/Aleppo%20Codex_jp2.zip&file=Aleppo%20Codex_jp2/Aleppo%20Codex_{NNNN}.jp2&id=aleppo-codex&scale=1&rotate=0
```

Page number `NNNN` is computed from the leaf using the table in
`copilot-instructions-aleppo-line-breaks.md`.

## Scripts

### `py_ac_loc/gen_word_crop_editor.py`

Generates an interactive HTML editor for cropping a word from the
Aleppo Codex image. Usage:

```
python py_ac_loc/gen_word_crop_editor.py <short_id>
```

where `<short_id>` is the quirkrec's short ID (e.g. `0119`, `0816-HVA`).

The script:
1. Loads the quirkrec from `pyauthor_util/job_quirkrecs.py`
2. Locates the word in the line-break data
3. Computes pixel coordinates from column-coordinate data
4. Generates `.novc/word_crop_{short_id}.html` and opens it in browser

The HTML editor:
- Shows the relevant section of the archive.org page image
- Pre-positions a draggable/resizable crop rectangle around the target
  line, roughly centered on the estimated word position
- The user adjusts the crop to tightly frame the word
- Click **Export** to save the crop as a PNG

### `py_ac_loc/list_missing_aleppo_imgs.py`

Lists all quirkrecs that don't yet have an Aleppo image on disk.

```
python py_ac_loc/list_missing_aleppo_imgs.py
```

## Image naming convention

Same as existing convention (see `pyauthor_util/img_util.py`):
- `Aleppo-{short_id}.png` where `short_id` = `CCVV` or `CCVV-WORDID`
- Saved to `docs/jobn/img/`

## Batch workflow

1. Run `list_missing_aleppo_imgs.py` to get the list of missing images
2. For each missing quirkrec:
   a. Run `gen_word_crop_editor.py {short_id}`
   b. Adjust the crop in the browser
   c. Export the PNG (saved automatically to `docs/jobn/img/`)
   d. Run `python main_gen_misc_authored_english_documents.py` to rebuild
   e. Verify the image appears correctly in the HTML output
3. Commit in batches (e.g. per-chapter or per-page)

## After adding images

After adding new Aleppo PNGs:

```
python main_gen_misc_authored_english_documents.py
git status --porcelain docs/
```

The `get_auto_imgs()` function in `pyauthor_util/img_util.py`
auto-detects new `Aleppo-{sid}.png` files in `docs/jobn/img/` and
populates `qr-aleppo-img` in the generated output.
