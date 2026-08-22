# CLAUDE.md

## There is no Python here — the code that writes this site lives in MAM-basics

This repo tracked **268 `.py`** until 2026-08-21 and tracks **none** now. The review of BHQ Job
that this repo publishes is still authored in Python, but that Python is
`C:\Users\BenDe\GitRepos\MAM-basics\py\` — 241 modules, moved there on 2026-08-19 and deleted
here on 2026-08-21, under
[`MAM-basics/doc/PLAN-evacuate-python-from-book-of-job.md`](../MAM-basics/doc/PLAN-evacuate-python-from-book-of-job.md).
The 160 quirk records went with it: they are Python modules, one per record, and they are
content rather than tooling, so `py/author_boj_qr/qr_XXYY.py` in MAM-basics is where a record is
read and edited.

What stays here is the corpus and the published site: `gh-pages/` (694 tracked files), `out/`
(7 JSON), `py_ac_loc/` (76 files of Aleppo Codex line-break, column-coordinate and MAM-XML data,
despite the `py_` prefix — it holds no Python and never did), `doc/` and this file.

Everything below runs from **MAM-basics' repo root**, `C:\Users\BenDe\GitRepos\MAM-basics`, on
**MAM-basics' interpreter**. Nothing runs from here, and there is no `.venv` here to run it with.

## Regenerate, then read the diff — that is the test

There is no test suite for this repo's artifacts. The tracked HTML under `gh-pages/` is the
check: after changing any of the Python in MAM-basics, regenerate and see what moved.

```bash
.venv/Scripts/python.exe py/main_gen_misc_authored_english_documents.py
```

Then read the diff. **Use `git diff`, not `git status --porcelain`** — the latter is the wrong
instrument in this repo, and has been wrong three separate times during the evacuation. A no-op
regeneration has left it reporting 183 modified files whose blobs were unchanged, git's cached
stat sizes being the pre-run CRLF ones, and `git update-index --refresh` did not clear them:

```bash
git -C ../book-of-job diff --stat HEAD -- gh-pages/ out/
```

A change meant to be output-neutral must leave that empty. For an intended change, read the HTML
diff and confirm it is the change you meant. An unexplained diff is a failure until it is
explained. When it matters to be sure, compare each file's bytes against its HEAD blob with
`git cat-file` rather than trusting either command.

## Which entry point writes what

Five entry points, all at the top of MAM-basics' `py/`. **Only the first writes tracked
artifacts as a regeneration**, so it is the whole of "regenerate the site":

| Entry point | What it writes here |
|---|---|
| `py/main_gen_misc_authored_english_documents.py` | **183 tracked artifacts** — 175 HTML, 2 CSS, and 6 of the 7 `out/*.json` |
| `py/main_apply_cam1753_crops.py` | PNGs under `gh-pages/jobn/img/cam1753/`, and appends `out/cam1753-crops.json` — but only for the crops in a hand-made editor export it takes as its argument, so it is a manual ingest step rather than a regenerator |
| `py/main_gen_aleppo_crop_editor.py` | `.novc/` here only, which is gitignored |
| `py/main_gen_cam1753_crop_editor.py` | `.novc/` here only |
| `py/main_list_missing_aleppo_imgs.py` | nothing; it prints |

The last three read `out/enriched-quirkrecs.json` **at module import time**, so each depends on
the first having run. That is the only sequencing there is.

Regenerating this site also needs **UXLC-utils** checked out beside MAM-basics, since 2026-08-19:
the location cross-check reads UXLC-utils' copy of the UXLC snapshot and of `lci_recs.json`,
where it used to read a copy kept here. That copy — 39 XML and one JSON under `py_uxlc_loc/` —
was deleted with the Python, being one blob with UXLC-utils' and MAM-basics' copies and read by
nothing.

## 518 of the 701 tracked artifacts are written by no program

Every file under `gh-pages/` and `out/` looks generated. Most are not, and **deleting one on the
assumption it will come back would lose it.** Of the 701:

| Files | Written by |
|---|---|
| 175 HTML, 2 CSS, 6 `out/*.json` | `py/main_gen_misc_authored_english_documents.py` — **regenerable** |
| 160 PNG, `gh-pages/jobn/img/cam1753/` | `py/main_apply_cam1753_crops.py`, from a hand-made crop export. A manual producer, not a regenerator |
| 160 PNG, `gh-pages/jobn/img/Aleppo/` | **nothing** — hand-made, one crop at a time |
| 160 PNG, `gh-pages/jobn/img/Lenin/` | **nothing** — hand-made, screenshots glued together |
| 30 PNG, `gh-pages/jobn/img-orphans/` | **nothing** |
| 5 PNG, loose in `gh-pages/jobn/img/` | **nothing** — `Aleppo-2Kings-c4v7`, `Jerusalem-Crown-3812-YD3F_HJXR`, `Lenin-2Kings-c4v7`, `Lenin-2Samuel-c18v20`, `Sassoon-1053-Lamentations-c4v16` |
| 2 woff2 | **nothing** — vendored fonts |
| `out/cam1753-crops.json` | appended to by the cam1753 ingest step; never rewritten whole |

So 515 PNG, 2 woff2 and `out/cam1753-crops.json` come back from no command. Re-establish the
counts with:

```bash
git -C ../book-of-job ls-files 'gh-pages/*' | sed 's/.*\.//' | sort | uniq -c
```

## The lints run from MAM-basics too

`check_all.py` is the lint side of the same idea, and it is `py/check_all.py` in MAM-basics now:

```bash
.venv/Scripts/python.exe py/check_all.py
```

Seven checks — quirkrec spell check, public-before-private function ordering, quirkrec
filename/record/word-id consistency, cross-record relation validity, Hebrew combining-mark order,
unnecessary `\uXXXX` escapes, and an HTML lint (`--w3c` to send the output to the W3C validator).

Four of them read **both** repos, and that is deliberate rather than incidental: mark order
scans this repo's `.json` as well as MAM-basics' `.py`, because the 24 hand-made line-break files
under `py_ac_loc/line-breaks/` are hand-authored Hebrew like any other. The HTML lint reads
`gh-pages/` here. `py/boj_paths.py` in MAM-basics is what names both roots, and its docstrings are
the statement of record for which tree holds what.

## Quirkrecs: read the enriched JSON, edit the Python

The 160 records are `py/author_boj_qr/qr_XXYY.py` in MAM-basics (chapter, then verse, both
zero-padded; a verse with more than one record takes a suffix, as in `qr_0816_HVA.py`). They are
the source, and comments are added there. But to *read* quirkrecs, prefer this repo's
`out/enriched-quirkrecs.json` over importing `RAW_QUIRKRECS` from
`author_boj_util.job_quirkrecs`: the enriched form has fields the raw one lacks, including
`qr-word-id`, which is what distinguishes two quirkrecs in one verse. Name the loop variable
`eqr` rather than `qr` when iterating the enriched form, so which one is in hand stays visible.
`py/main_gen_misc_authored_english_documents.py` regenerates the JSON along with the HTML.

## Docs

Two procedures are still here, both about looking at what this repo holds:

| For | Read |
|---|---|
| Opening the generated HTML, including `#fragment` anchors | [`doc/opening-html-files.md`](doc/opening-html-files.md) |
| The MAM-simple XML format, and what `py_ac_loc/MAM-XML/` is | [`doc/reading-mam-simple.md`](doc/reading-mam-simple.md) |

**Seven others moved to MAM-basics on 2026-08-21, following the code they describe**, and are
`doc/boj-*.md` there: `boj-aleppo-word-crops.md`, `boj-cam1753-word-crops.md`,
`boj-leningrad-word-crops.md`, `boj-leningrad-image-scaling.md`,
`boj-image-crop-reproducibility.md`, `boj-viewing-image-metadata.md`, `boj-quirkrec-comments.md`.
Every path in them was repointed at MAM-basics' `py/` and at this repo as `../book-of-job/`.

All nine were `.github/copilot-instructions-*.md` until 2026-08-03, when GitHub Copilot stopped
being used here, and they have not all been re-verified since. Where one gives a command that
conflicts with the global conventions in `~/.claude/CLAUDE.md` — a `python -c` one-liner, a bare
`python`, `PYTHONIOENCODING`, a `Start-Process` that opens a page rather than handing over a
`file:///` link — the global conventions win.
