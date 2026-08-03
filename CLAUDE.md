# CLAUDE.md

## Regenerate, then read the diff — that is the test

There is no test suite. The tracked HTML under `gh-pages/` is the check: after changing any
Python, regenerate and see what moved.

```bash
.venv/Scripts/python.exe main_gen_misc_authored_english_documents.py
```

Then `git status --porcelain gh-pages/`. A refactor meant to be output-neutral must leave that
empty; for an intended change, read the HTML diff and confirm it is the change you meant. An
unexplained diff is a failure until it is explained. Run everything from the repo top — this
repo has a flat layout, with the `main_*` and `check_*` scripts at the root rather than under
`py/`.

`check_all.py` is the lint side of the same idea, and its docstring lists what it runs: quirkrec
spell check, public-before-private function ordering, quirkrec filename/record/word-id
consistency, cross-record relation validity, Hebrew combining-mark order, unnecessary `\uXXXX`
escapes, and an HTML lint (`--w3c` to send the output to the W3C validator).

## Quirkrecs: read the enriched JSON, edit the Python

The 160 records under `pyauthor_qr/qr_XXYY.py` (chapter, then verse, both zero-padded; a verse
with more than one record takes a suffix, as in `qr_0816_HVA.py`) are the source, and comments
are added there. But to *read* quirkrecs, prefer `out/enriched-quirkrecs.json` over importing
`RAW_QUIRKRECS` from `pyauthor_util.job_quirkrecs`: the enriched form carries fields the raw one
lacks, including `qr-word-id`, which is what distinguishes two quirkrecs in one verse. Name the
loop variable `eqr` rather than `qr` when iterating the enriched form, so which one is in hand
stays visible. `main_gen_misc_authored_english_documents.py` regenerates the JSON along with the
HTML.

## Docs

Procedures that were `.github/copilot-instructions-*.md` until 2026-08-03, when GitHub Copilot
stopped being used here:

| For | Read |
|---|---|
| Cropping a word from the Aleppo Codex (μA) | [`doc/aleppo-word-crops.md`](doc/aleppo-word-crops.md) |
| Cropping a word from Cambridge MS Add. 1753 (μC) | [`doc/cam1753-word-crops.md`](doc/cam1753-word-crops.md) |
| Cropping a word from the Leningrad Codex (μL) | [`doc/leningrad-word-crops.md`](doc/leningrad-word-crops.md) |
| Scaling a Leningrad image to match the Aleppo one's height | [`doc/leningrad-image-scaling.md`](doc/leningrad-image-scaling.md) |
| Adding or updating a quirkrec comment | [`doc/quirkrec-comments.md`](doc/quirkrec-comments.md) |
| Keeping a crop reproducible at any resolution | [`doc/image-crop-reproducibility.md`](doc/image-crop-reproducibility.md) |
| Reading a PNG's embedded metadata | [`doc/viewing-image-metadata.md`](doc/viewing-image-metadata.md) |
| Opening the generated HTML, including `#fragment` anchors | [`doc/opening-html-files.md`](doc/opening-html-files.md) |
| The MAM-simple XML format | [`doc/reading-mam-simple.md`](doc/reading-mam-simple.md) |

Those files were written for Copilot and have not all been re-verified since; where one gives a
command that conflicts with the global conventions in `~/.claude/CLAUDE.md` — a `python -c`
one-liner, a bare `python`, `PYTHONIOENCODING` — the global conventions win.
