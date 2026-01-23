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
- Dagesh (U+05BC) should come before vowel points

## Verification After Refactoring

After making changes to Python source files, verify the HTML output is unchanged:

1. Run: `python ./main_gen_misc_authored_english_documents.py`
2. Check: `git status --porcelain docs/`
3. If any files in `docs/` are modified, investigate and fix the differences before considering the task complete
