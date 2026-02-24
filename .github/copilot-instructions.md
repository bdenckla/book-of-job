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

When working with Hebrew text, maintain the project\u2019s standard combining-mark
order within each base-letter cluster.  The authoritative implementation is
`pycmn/uni_denorm.py` (`give_std_mark_order`), and the CI-style checker is
`check_mark_order.py` (also wired into `check_all.py`).

The standard order places these four marks first (in this order), followed by
all other marks in their original relative order:

1. Shin dot (U+05C1)
2. Sin dot (U+05C2)
3. Dagesh / mapiq / shuruq dot (U+05BC)
4. Rafeh (U+05BF)

In practice this means: **base letter \u2192 shin/sin dot \u2192 dagesh \u2192 rafeh \u2192 vowels / meteg / accents** (the remaining marks keep whatever mutual order they already had).

When in doubt, pass the text through `give_std_mark_order` rather than
hand-ordering codepoints.

## Temporary Generated Files

Place any temporary generated files (scripts, HTML reports, debugging output, etc.) into the `.novc/` folder. This folder is excluded from version control.

## Running Python Code

**Always use the project venv Python** (`.venv\Scripts\python.exe`) when running scripts — never the bare `python` command, which may resolve to a system Python missing project dependencies.

**Never run Python one-liners via `python -c "..."` in the terminal.** These invariably fail due to character encoding and/or shell escaping issues, especially with Hebrew text. Instead, always create an actual `.py` file in `.novc/` and run it with `.venv\Scripts\python.exe .novc/<filename>.py`.

**Always set `$env:PYTHONIOENCODING="utf-8"` before running any Python command in PowerShell.** The Windows console defaults to cp1252, which cannot encode Hebrew characters and causes `UnicodeEncodeError` on any `print()` that includes Hebrew text. Set the variable once per terminal session before the first Python invocation.

**Running Black:** From the repo top directory, run:
```
.venv\Scripts\python.exe -m black .
```
Black respects `.gitignore` by default, so this covers all tracked Python files without needing an explicit glob.

## Installing Python Packages

**Never install packages to the system Python.** Always install into the project venv using `.venv\Scripts\pip.exe install <package>` (or ensure the venv is activated first). Add new dependencies to `requirements.txt` at the top level.

## Python Package `__init__.py` Style

Keep `__init__.py` files **minimal** — they exist only as package markers so that explicit submodule imports work (e.g. `from py_ac_word_image_helper.codex_page import ...`). Do **not** add re-exports to `__init__.py`; always import directly from the submodule that defines the symbol.

## Global Variables

Avoid the `global` keyword and avoid mutating module-level variables. If a function needs shared state, pass it as a parameter or return it. Module-level constants (ALL_CAPS) are fine as long as they remain immutable after definition.

## Reading and Writing Python Files

When reading or modifying Python source files in this project:

**Reading Python data:** Import modules directly rather than parsing as text:
```python
from pyauthor_qr.qr_0119 import RECORD_0119
```

**Reading quirkrecs data:** Prefer loading `out/enriched-quirkrecs.json` over importing `RAW_QUIRKRECS` from `pyauthor_util.job_quirkrecs`. The JSON has enriched fields like `qr-word-id` (which disambiguates multiple quirkrecs in the same verse) and `qr-aleppo-img`. `RAW_QUIRKRECS` lacks these. When iterating enriched quirkrecs, use `eqr` as the loop variable (not `qr`) to make the distinction clear.

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

**Output JSON:** `out/enriched-quirkrecs.json` contains all enriched quirkrecs as JSON. Regenerate with:
```
python main_gen_misc_authored_english_documents.py
```

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

## Authorship Marking

When generating a new version-controlled file (Python script, Markdown doc, etc.), include an authorship comment as the **first line**:

- **Python:** `# Initially generated by GitHub Copilot.`
- **Markdown/HTML:** `<!-- Initially generated by GitHub Copilot. -->`

This does not apply to throwaway files in `.novc/`.

## Git Discipline

- **Never auto-commit.** Only commit when the user explicitly asks.
- **Always use fresh commits.** Never use `git commit --amend` unless the user explicitly requests it.
- **Before discarding work** (`git reset`, `git checkout -- .`, `git stash drop`, etc.): always run `git status` and `git diff --stat` first. If there are uncommitted changes beyond the current experiment, alert the user and ask them to commit or stash before proceeding.
- **Before a series of experiments** that might need to be thrown away: ask the user to commit the current clean state first, so there is a safe baseline to return to.

## Markdown formatting

- **Avoid strikethrough:** Do not use bare tildes (`~`) as an
  abbreviation for “approximately.” Markdown renderers interpret text
  between two `~` characters as strikethrough. Instead, write out
  “approx.” or “approximately,” or escape the tilde (`\~`).

## Workflow Reference

The following workflow docs are available via `#file` when needed:

| When you need to… | Attach this file |
|---|---|
| Crop a word from the Aleppo Codex (μA) | `copilot-instructions-aleppo-word-crops.md` |
| Crop a word from Cambridge MS Add. 1753 (μC) | `copilot-instructions-cam1753-crops.md` |
| Crop a word from the Leningrad Codex (μL) | `copilot-instructions-leningrad-crops.md` |
| Scale a Leningrad image to match Aleppo height | `copilot-instructions-leningrad-scaling.md` |
| Add/update quirkrec comments | `copilot-instructions-quirkrec-comments.md` |
| Open HTML files / fragment anchors / caching | `copilot-instructions-opening-html.md` |
| View image metadata (XnView MP) | `copilot-instructions-image-metadata.md` |
| Image crop reproducibility rules | `copilot-instructions-image-crop-reproducibility.md` |
| Work with MAM-XML files | `copilot-instructions-mam-xml.md` |
| Work with MAM parsed data | `copilot-instructions-mam-parsed.md` |

All files are in `.github/`.
