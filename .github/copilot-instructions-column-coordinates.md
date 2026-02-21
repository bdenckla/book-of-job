# Column Coordinate Editing Workflow

To measure column positions on an Aleppo Codex page image:

1. **Generate the interactive HTML editor:**
   ```
   python py_ac_loc/gen_col_location_editor.py <page_id>
   ```
   This opens a browser editor with draggable side-midpoint handles and skew (rotation) controls for two columns of 28 lines each. If a coordinate file already exists for that page, it loads those values as defaults.

2. **Adjust columns** using handles, skew buttons (rotate ↶/↷), and fine mode. The "skew" label on the image shows which edge angle is being adjusted.

3. **Export JSON** by clicking the Export button (copies to clipboard).

4. **Paste the JSON into the chat.** The assistant saves it to `py_ac_loc/column-coordinates/<page_id>.json`.

5. **Pages for Book of Job:** 270r through 281v (24 pages total). Check which are done by listing `py_ac_loc/column-coordinates/`.
