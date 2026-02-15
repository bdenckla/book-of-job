# Aleppo Codex Alignment JSON Format

## Overview

Each `py_ac_loc/aleppo_col_lines_{page}.json` file records the line-by-line
alignment of one Aleppo Codex page image to the corresponding MAM-XML text.

## Consistency Checker

After editing any alignment JSON file, run:

```
python py_ac_loc/check_aleppo_col_lines.py
```

This validates that all redundant/friendly fields are consistent with their
machine-readable counterparts.

## Top-Level Keys

| Key | Type | Description |
|-----|------|-------------|
| `file-description` | list of strings | Generic description (same in every file) |
| `page-id` | string | Page identifier, e.g. `"281v"` |
| `page-ranges` | list of range objects | Overall text extent of the page in machine-readable form, split per book (see [Range Object](#range-object)) |
| `page-ranges-friendly` | list of ranges-friendly objects | Human-readable version of `page-ranges` (see [Ranges-Friendly](#ranges-friendly-format)). **Redundant** — must match `page-ranges`. |
| `page-MAM-XML-files` | list of strings | Repo-relative paths to source XML files, e.g. `"py_ac_loc/MAM-XML/Job.xml"` |
| `page-image` | string | URL to the page image on archive.org |
| `page-col-positions-possible` | list of strings | All possible column positions for this page, e.g. `["right", "left"]`. Future pages may include `"middle"`. |
| `page-column-symbol-recs` | list of column-symbol-rec objects | Maps symbolic column key names to their header and lines keys (see [Column Symbol Rec](#column-symbol-rec)) |
| `column-right` | object | Metadata for the right column (see [Column Object](#column-object)) |
| `column-left` | object | Metadata for the left column (see [Column Object](#column-object)) |
| `column-right-lines` | list of line objects | Line data for the right column (see [Line Data](#line-data)) |
| `column-left-lines` | list of line objects | Line data for the left column (see [Line Data](#line-data)) |

## Column Symbol Rec

Each entry in `page-column-symbol-recs` identifies the JSON key names for a column's header object and line data:

| Key | Type | Description |
|-----|------|-------------|
| `csr-header` | string | Key name of the column header object, e.g. `"column-right"` |
| `csr-lines` | string | Key name of the column line data array, e.g. `"column-right-lines"` |

## Column Object

Each column object (`column-right`, `column-left`) contains:

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `col-position` | string | yes | `"right"` for `column-right`, `"left"` for `column-left` |
| `col-ranges` | list of range objects | yes | Machine-readable text ranges (see [Range Object](#range-object)) |
| `col-ranges-friendly` | list of ranges-friendly objects | yes | Human-readable version of `col-ranges` (see [Ranges-Friendly](#ranges-friendly-format)). **Redundant** — must match `col-ranges`. |
| `col-line-count` | integer | yes | Number of lines in the column (typically 28) |
| `col-blank-lines` | list of integers | if any | Line numbers that are blank (empty string). Used at book boundaries. |
| `col-pe-lines` | list of integers | if any | Line numbers containing only `{פ}` (parashah pe break). |
| `col-ketivs` | list of ketiv objects | if any | Ketiv readings in this column (see [Ketiv Object](#ketiv-object)) |
| `col-notes` | list of strings | if any | Free-form English notes for anything not captured by the structured fields above |

Keys are omitted when the list would be empty (`col-blank-lines`, `col-pe-lines`,
`col-ketivs`, `col-notes`).

## Range Object

Each range object represents a contiguous text span within one book:

```json
{
  "start": ["Job", 41, 23, "first-word"],
  "end": ["Job", 42, 10, "first-word"]
}
```

Each endpoint is a 4-element array: `[book, chapter, verse, fml]`

The `fml` (first/middle/last) value indicates where the column boundary falls
within the verse:

| Value | Meaning |
|-------|---------|
| `"first-word"` | The column starts/ends at the first word of this verse |
| `"a-middle-word"` | The column starts/ends at a middle word (verse is split across columns) |
| `"last-word"` | The column starts/ends at the last word of this verse |

**Cross-book ranges** are split into separate within-book range objects.
For example, a column spanning Job 42:11–Prov 1:8 has two range objects:
one for `Job 42:11–42:17` and one for `Prov 1:1–1:8`.

## Ranges-Friendly Format

A human-readable mirror of the machine-readable range. Each endpoint becomes
a single string:

```json
{
  "start": "Job 41:23-first",
  "end": "Job 42:10-first"
}
```

The suffix mapping is:

| Machine-readable | Friendly suffix |
|-----------------|----------------|
| `"first-word"` | `-first` |
| `"a-middle-word"` | `-mid` |
| `"last-word"` | `-last` |

The top-level `"page-ranges"` uses the machine-readable
range-object format, and `"page-ranges-friendly"` uses the
ranges-friendly format. Both are lists of range objects (one per book),
derived by merging all column ranges across both columns and grouping by book.

## Ketiv Object

Records a ketiv (written) reading that differs from the qere (read) form:

```json
{
  "bcv-fml": ["Job", 42, 2, "first-word"],
  "bcv-fml-friendly": "Job 42:2-first",
  "word": "ידעת"
}
```

| Key | Type | Description |
|-----|------|-------------|
| `bcv-fml` | 4-element array | `[book, chapter, verse, fml]` — locates the ketiv word |
| `bcv-fml-friendly` | string | Human-readable version. **Redundant** — must match `bcv-fml`. |
| `word` | string | The ketiv word as it appears in the manuscript (unpointed or partially pointed) |

The `fml` value here indicates where the ketiv word falls within its verse
(first word, a middle word, or last word).

## Line Data

Each `column-right-lines` / `column-left-lines` array contains objects with the following fields:

| Key | Type | Description |
|-----|------|-------------|
| `line-num` | integer | 1-based line number, sequential |
| `range` | `[string, string]` or `null` | Verse range on this line (see below), or `null` for blank/{פ} lines |
| `MAM-XML-fragment` | string | The text content of the line |

```json
[
  {"line-num": 1, "range": ["Job 41:23-first", "Job 41:23-last"], "MAM-XML-fragment": "יַרְתִּ֙יחַ כַּסִּ֙יר מְצוּלָ֑ה יָם׀ח יָשִׂ֥ים כַּמֶּרְקָחָֽה׃"},
  {"line-num": 2, "range": ["Job 41:24-first", "Job 41:24-last"], "MAM-XML-fragment": "אַ֭חֲרָיו יָאִ֙יר נָתִ֑יב יַחְשֹׁ֖ב תְּה֙וֹם לְשֵׂיבָֽה׃"},
  {"line-num": 3, "range": ["Job 41:25-mid", "Job 41:26-mid"], "MAM-XML-fragment": "אֵֽין־עַל־עָפָ֥ר ..."},
  ...
]
```

The **range** field is either `null` or a 2-element `[start, end]`
array indicating the verse range that appears on that line.

Each endpoint is a string in the format `"Book ch:vs-qualifier"` where the
qualifier indicates the word position within the verse:

| Qualifier | Meaning |
|-----------|---------|
| `-first` | The line includes the first word of this verse |
| `-mid` | The line starts/ends at a middle word (neither first nor last) |
| `-last` | The line includes the last word of this verse |

Examples:

| Range | Meaning |
|-------|---------|
| `["Job 41:23-first", "Job 41:23-last"]` | Full verse on one line |
| `["Job 1:1-first", "Job 1:1-mid"]` | First part of a verse |
| `["Job 1:1-mid", "Job 1:1-last"]` | Last part of a verse |
| `["Job 1:7-mid", "Job 1:8-mid"]` | End of one verse + start of the next |
| `null` | Blank line or {פ}-only line |

Special line types:
- **Blank line:** `{"line-num": 17, "range": null, "MAM-XML-fragment": ""}` — used at book boundaries
- **Pe-only line:** `{"line-num": 5, "range": null, "MAM-XML-fragment": "{פ}"}` — parashah pe break occupying an entire line
- **Pe within text:** `{"line-num": 6, "range": ["Job 1:5-mid", "Job 1:5-last"], "MAM-XML-fragment": "כָּכָה יַעֲשֶׂ֥ה אִיֹּ֖ב כָּל־הַיָּמִֽים׃ {פ}"}` — pe marker at end of a text line

Line numbers are 1-based and sequential.
## Redundancy

Several fields are intentionally redundant to aid human readability:

| Friendly field | Must match |
|----------------|-----------|
| `col-ranges-friendly` | `col-ranges` |
| `page-ranges` | `page-ranges-friendly` (machine ↔ friendly) |
| `page-ranges-friendly` | Merge of all column `col-ranges-friendly` entries, grouped by book |
| `bcv-fml-friendly` (in ketivs) | `bcv-fml` |
| `col-blank-lines` | Lines in `column-right-lines` / `column-left-lines` with empty text |
| `col-pe-lines` | Lines in `column-right-lines` / `column-left-lines` with text `"{פ}"` |
| ketiv `word` | Must appear in some line in `column-right-lines` / `column-left-lines` |
| line range | `null` for blank/{פ} lines; non-null `[start, end]` range pair for text lines |

Run `python py_ac_loc/check_aleppo_col_lines.py` to verify all of these.

## Example (Minimal Column)

```json
{
  "col-position": "right",
  "col-ranges": [
    {
      "start": ["Job", 32, 8, "first-word"],
      "end": ["Job", 33, 11, "first-word"]
    }
  ],
  "col-ranges-friendly": [
    {
      "start": "Job 32:8-first",
      "end": "Job 33:11-first"
    }
  ],
  "col-line-count": 28
}
```

## Example (Column with All Optional Fields)

```json
{
  "col-position": "right",
  "col-ranges": [
    {
      "start": ["Job", 41, 23, "first-word"],
      "end": ["Job", 42, 10, "first-word"]
    }
  ],
  "col-ranges-friendly": [
    {
      "start": "Job 41:23-first",
      "end": "Job 42:10-first"
    }
  ],
  "col-line-count": 28,
  "col-pe-lines": [5, 14],
  "col-ketivs": [
    {
      "bcv-fml": ["Job", 42, 2, "first-word"],
      "bcv-fml-friendly": "Job 42:2-first",
      "word": "ידעת"
    },
    {
      "bcv-fml": ["Job", 42, 10, "a-middle-word"],
      "bcv-fml-friendly": "Job 42:10-mid",
      "word": "אֶת־שבית"
    }
  ]
}
```
