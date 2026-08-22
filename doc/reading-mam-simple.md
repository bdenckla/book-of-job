# Reading MAM-simple

The guide to the MAM-simple format lives in the MAM-simple repo, and is canonical there:

- [doc/reading-mam-simple.md](https://github.com/bdenckla/MAM-simple/blob/main/doc/reading-mam-simple.md) — file layout, and reading MAM-simple from Python
- [doc/reading-mam-simple-xml.md](https://github.com/bdenckla/MAM-simple/blob/main/doc/reading-mam-simple-xml.md) — the XML hierarchy, element types, and verse attributes
- [doc/reading-mam-simple-json.md](https://github.com/bdenckla/MAM-simple/blob/main/doc/reading-mam-simple-json.md) — the JSON format

This file used to be a fuller copy of that guide. The copy went stale — it still had the
XML under `out/xml-vtrad-mam`, a directory MAM-simple moved to the repo root — so on
2026-08-03 its content was merged into the canonical guide and this pointer left behind.
What remains below is what is specific to this repo.

## What this repo has

`py_ac_loc/MAM-XML/` is a snapshot of MAM-simple's `xml-vtrad-mam`, one file per book24.
It is vendored, not generated here: see
[`py_ac_loc/MAM-simple-provenance.md`](../py_ac_loc/MAM-simple-provenance.md) for the
commit and date it was copied from. Update it by re-copying, never by editing in place.

No code here reads it — and since 2026-08-21 there is no code here at all. The one tracked file
that names the directory does so to **exclude** it, on the grounds that it is vendored:
`../MAM-basics/py/tests/test_h_dot_below_nfc.py` skips it when checking normalization, under
that file's `_BOJ_EXCLUDE_DIR_PREFIXES`. (This sentence counted two such files until 2026-08-21;
the other, `.novc/count_scope.py`, which left the directory out of the line counts, was a
gitignored throwaway rather than a tracked file.)

The repos that do read this XML are codex-index-aleppo and codex-index-cam1753, each with
a separate `mam_xml_verses.py`.
