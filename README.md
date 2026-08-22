# book-of-job

A review of BHQ's edition of the book of Job (ספר איוב), published as a static site at
[bdenckla.github.io/book-of-job](https://bdenckla.github.io/book-of-job/). Its main document is
"BHQ Job was made in a bubble," which argues that BHQ Job has at its core a lightly updated BHS
rather than a modern scholarly edition of the Masoretic Text, and that it still transcribes μL
(the Leningrad Codex) inaccurately and still leaves μL's disagreements with other Tiberian
manuscripts unnoted.

Behind that document sit **160 detail pages**, one per quirk record — one place in Job where μL
as printed is odd, with the consensus form beside it, what is odd about it, and where to find it
in μL and in μA (the Aleppo Codex), page, column and line. Each detail page has word-level image
crops from all three of μA, μL and μY (Cambridge MS Add. 1753) — 160 of each, one per page — so
a reader can look at the manuscripts rather than take the description on trust.
`gh-pages/index.html` is the way in.

**This repository contains no code.** As of 2026-08-21 all of its Python — 241 modules,
including the 160 one-record modules the review is written in — lives in the sibling repository
[MAM-basics](https://github.com/bdenckla/MAM-basics), under `py/`, and generates into this one.
Every command runs from `C:\Users\BenDe\GitRepos\MAM-basics` on that repository's interpreter.

## What is here

- `gh-pages/` — the published site, 694 tracked files: 175 HTML, 515 PNG, 2 CSS, 2 woff2.
- `out/` — 7 JSON, six of them regenerated with the site. `out/enriched-quirkrecs.json` is the
  form to read a quirk record from; `out/cam1753-crops.json` holds hand-made crop coordinates.
- `py_ac_loc/` — 76 files of Aleppo Codex data: line breaks and column coordinates for all 24
  Job pages (270r–281v), a codex index, and a vendored snapshot of MAM-simple's XML. **The `py_`
  prefix is misleading and always was — there is no Python in it.**
- `doc/` — two procedures about reading what is here; the seven about how it is made went to
  MAM-basics with the code.

**Most of what is under `gh-pages/` is not regenerable.** 515 PNG, 2 woff2 and
`out/cam1753-crops.json` — 518 of the 701 tracked artifacts — are hand-made or vendored, and no
command brings them back. [CLAUDE.md](CLAUDE.md) has the table of which files those are, along
with which entry point writes which of the other 183.
