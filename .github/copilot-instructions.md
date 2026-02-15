# Copilot Instructions for book-of-job

## Unicode Character Preservation

This project uses typographically correct Unicode characters. **Never convert these to ASCII equivalents.**

### Characters to preserve:

- **Curly apostrophe:** `'` (U+2019 RIGHT SINGLE QUOTATION MARK) — not straight `'` (U+0027)
- **Curly quotes:** `"` (U+201C) and `"` (U+201D) — not straight `"` (U+0022)
- **Hebrew characters:** All Hebrew letters, vowel points, cantillation marks, and other marks must be preserved exactly

### When editing files:

1. Always read the file first to see what character style is used
2. Copy exact characters from existing content rather than retyping
3. When uncertain, use Python scripts with explicit `chr()` codes:
   - `chr(8217)` = `'` (curly apostrophe)
   - `chr(8220)` = `"` (left curly quote)
   - `chr(8221)` = `"` (right curly quote)
   - `chr(39)` = `'` (straight apostrophe — avoid)
   - `chr(34)` = `"` (straight quote — avoid)

### Hebrew Unicode ordering:

When working with Hebrew text, maintain proper Unicode normalization order:
- Shin/sin dots (U+05C1, U+05C2) should come immediately after the shin letter
- Dagesh (U+05BC) should come after shin/sin dot but before rafeh
- Rafeh (U+05BF) should come after dagesh but before vowel points
- **Accents (cantillation marks) almost always come AFTER vowels**, not before them, when both appear on the same letter

Full order: **base letter → shin/sin dot → dagesh → rafeh → vowels → meteg → accents**

## Temporary Generated Files

Place any temporary generated files (scripts, HTML reports, debugging output, etc.) into the `.novc/` folder. This folder is excluded from version control.

## Running Python Code

**Never run Python one-liners via `python -c "..."` in the terminal.** These invariably fail due to character encoding and/or shell escaping issues, especially with Hebrew text. Instead, always create an actual `.py` file in `.novc/` and run it with `python .novc/<filename>.py`.

## Reading and Writing Python Files

When reading or modifying Python source files in this project:

**Reading Python data:** Import modules directly rather than parsing as text:
```python
from pyauthor_qr.qr_0119 import RECORD_0119
from pyauthor_util.job_quirkrecs import QUIRKRECS
```

**Writing/modifying Python (preserving comments):** Use **LibCST** when comments must be preserved:

```python
import libcst as cst

tree = cst.parse_module(source)

class MyTransformer(cst.CSTTransformer):
    def leave_Dict(self, original_node, updated_node):
        # Modify dict while preserving comments
        ...

modified = tree.visit(MyTransformer())
Path(file).write_text(modified.code)
```

LibCST preserves comments, whitespace, and formatting. Install with `pip install libcst`.

**Writing/modifying Python (simple cases):** For files without comments or where comment loss is acceptable, use the standard AST approach:

1. Parse with `ast.parse(source)`
2. Modify the AST (e.g., insert keys into `ast.Dict` nodes)
3. Generate code with `ast.unparse(tree)` (Python 3.9+)
4. Reformat with Black: `python -m black <file>`

⚠️ **Warning:** `ast.unparse()` discards all comments. Use LibCST if comments must be preserved.

Both approaches guarantee syntactically valid output. Avoid fragile regex-based or string-based text replacements.

**Output JSON:** `out/quirkrecs.json` contains all quirkrecs as JSON. Regenerate with:
```
python main_gen_misc_authored_english_documents.py
```

## mgketer.org Aleppo Codex Images

To view an Aleppo Codex (μA) image for a given chapter on mgketer.org, use:

```
https://www.mgketer.org/mikra/{bknu}/{chnu}/1/mg/106
```

where `bknu` is the 1-based book number and `chnu` is the chapter number. The book number can be looked up via `pycmn.bib_locales.get_bknu(bk39id)`. For reference, Job = 29.

## Screenshots

When the user refers to "the most recent screenshot" or similar, this means the most recent file (by last-write time) in:

```
C:\Users\BenDe\OneDrive\Pictures\Screenshots
```

## Verification After Refactoring

After making changes to Python source files, verify the HTML output is unchanged:

1. Run: `python ./main_gen_misc_authored_english_documents.py`
2. Check: `git status --porcelain docs/`
3. If any files in `docs/` are modified, investigate and fix the differences before considering the task complete

## Line Break Editing Workflow

To add line-break markers for an Aleppo Codex page column:

1. **Generate the flat-stream JSON** (if it doesn't already exist in `py_ac_loc/line-breaks/`):
   ```
   python py_ac_loc/gen_lb_flat_stream.py <page_id>
   ```

2. **Generate the interactive HTML editor:**
   ```
   python py_ac_loc/gen_line_break_editor.py <page_id> <col>
   ```
   where col 1 = right column, col 2 = left column. This opens a browser editor.

3. **Mark line breaks** in the editor by clicking the last word of each line, then click **Export JSON to Clipboard**.

4. **Paste directly** into `py_ac_loc/line-breaks/<page_id>.json`, replacing its entire contents.

**Do NOT** paste the exported JSON into the chat window — that causes Unicode NFC normalization of Hebrew text. Pasting directly into the file preserves the original byte sequences and avoids the need for `merge_line_markers.py`.

## Git Discipline

- **Never auto-commit.** Only commit when the user explicitly asks.
- **Before discarding work** (`git reset`, `git checkout -- .`, `git stash drop`, etc.): always run `git status` and `git diff --stat` first. If there are uncommitted changes beyond the current experiment, alert the user and ask them to commit or stash before proceeding.
- **Before a series of experiments** that might need to be thrown away: ask the user to commit the current clean state first, so there is a safe baseline to return to.
