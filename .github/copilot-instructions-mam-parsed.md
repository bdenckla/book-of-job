# How to Read MAM-parsed JSON

> **Canonical documentation:** The MAM-parsed repo has human-readable format guides at:
> - `C:\Users\BenDe\GitRepos\MAM-parsed\doc\reading-mam-parsed-plain.md`
> - `C:\Users\BenDe\GitRepos\MAM-parsed\doc\reading-mam-parsed-plus.md`
>
> This file is a Copilot-oriented summary with local path references and usage patterns.

## What is MAM-parsed?

MAM-parsed is a JSON format containing the MAM (Miqra According to the Masorah) data
with Wikitext templates parsed into structured objects.
It comes in two flavors: **plain** (close to the Google Sheet) and **plus** (enhanced).

**Repository:** `C:\Users\BenDe\GitRepos\MAM-parsed` (or [github.com/bdenckla/MAM-parsed](https://github.com/bdenckla/MAM-parsed))

## File Layout

```
MAM-parsed/
  plain/    # Plain format: close to Google Sheet
  plus/     # Plus format: enhanced, cleaned up
```

Each directory has 24 JSON files, one per book of the Miqra.
Naming: `{section}{number}-{Name}.json`, e.g. `D3-Job.json`.

Sections: A=Torah, B=Former Prophets, C=Latter Prophets,
D=Wisdom, E=Five Scrolls, F=Late Books.

## JSON Hierarchy

```
root
  ├── header: { book24_names, sub_book_names, chapter_counts }
  └── book39s: [                    ← array, usually 1 item; 2+ for composite books
        ├── book24_name: "ספר איוב"
        ├── sub_book_name: null     ← non-null for composite books (Samuel, Kings, etc.)
        ├── good_ending_plus: ...   ← plus only; null for most books
        └── chapters: {             ← dict keyed by Hebrew letter names
              "א": {                ← chapter 1
                "א": [D, CP, EP],  ← verse 1
                "ב": [D, CP, EP],  ← verse 2
                ...
              }
            }
      ]
```

### Key difference: Hebrew keys, not numbers

Chapters and verses are keyed by **Hebrew letter names** (gematria):
`"א"` = 1, `"ב"` = 2, ..., `"י"` = 10, `"יא"` = 11, ..., `"לד"` = 34.

Note: 15 is `"טו"` (not `"יה"`) and 16 is `"טז"` (not `"יו"`).

## Verse Structure: `[D, CP, EP]`

Each verse is a 3-element array corresponding to Google Sheet columns:

| Index | Name | Content |
|-------|------|---------|
| 0 | D | Section markers: `["__"]` (continuation), `[{"tmpl_name":"פפ"}]` (petuchah), etc. |
| 1 | CP | Verse reference template (`מ:פסוק`). In plus, only first verse per chapter. |
| 2 | EP | Verse text: mixed array of strings (Hebrew text) and template objects |

## Template Representation

### Plain format: `stmpl` (stringified)

```json
{"stmpl": "קו\"כ|את|אַ֠תָּ֠ה"}
```

Pipe-delimited: first segment = template name, rest = arguments.

### Plus format: `tmpl_name`/`tmpl_args`/`tmpl_params`

```json
{
  "tmpl_name": "קו\"כ",
  "tmpl_args": ["את", "אַ֠תָּ֠ה"],
  "tmpl_params": {"1": "את", "2": "אַ֠תָּ֠ה"}
}
```

Arguments can be strings, arrays, or nested template objects.

## Plain-Only Features

- Pseudo-verses `"0"` (pre-chapter) and `"תתת"` (post-chapter)
- `{"custom_tag": "noinclude"}` XML-like tags
- `{"tmpl": [...]}` parsed template trees
- `"//"` Wikitext line breaks in D column
- `{"stmpl": "גלגל-2|word"}` — galgal accent annotation

## Plus-Only Features

- `good_ending_plus` on book39 (for books that repeat penultimate verse)
- `{"tmpl_name": "מ:אות-מיוחדת-במילה", ...}` — special letter marking
- Targeted ketiv-qere: `מ:כו"ק כתיב מילה חדה וקרי תרתין מילין`
- No pseudo-verses, no custom XML tags, no `"//"` separators

## Common Templates in EP (Verse Text)

| Template | Purpose | Key Args |
|----------|---------|----------|
| `מ:לגרמיה-2` | Legarmeih accent | (no args) |
| `קו"כ` | Ketiv-qere | arg1=ketiv, arg2=qere |
| `נוסח` | Variant reading | arg1=primary text, arg2=variant description |
| `מ:דחי` | Dechik accent | arg1=word, arg2=variant |
| `מ:פסק` | Pasek mark | (no args) |
| `מ:מקף אפור` | Gray maqaf | (no args) |
| `ר0`–`ר4` | Re'via tiers | (no args) |

## Extracting Verse Text

### From plain format

```python
import json
from pathlib import Path

book = json.loads(Path('C:/Users/BenDe/GitRepos/MAM-parsed/plain/D3-Job.json').read_text('utf-8'))
chapters = book['book39s'][0]['chapters']

def plain_verse_text(ep):
    parts = []
    for atom in ep:
        if isinstance(atom, str):
            parts.append(atom)
        elif isinstance(atom, dict):
            stmpl = atom.get('stmpl', '')
            name = stmpl.split('|')[0] if '|' in stmpl else stmpl
            args = stmpl.split('|')[1:] if '|' in stmpl else []
            if name in ('קו"כ', 'קו"כ-אם') and len(args) >= 2:
                parts.append(args[1])  # qere
            elif name == 'נוסח' and args:
                parts.append(args[0])  # primary
            elif name == 'גלגל-2' and args:
                parts.append(args[0])
    return ''.join(parts).strip()

# Job 1:1
print(plain_verse_text(chapters['א']['א'][2]))
```

### From plus format

```python
book = json.loads(Path('C:/Users/BenDe/GitRepos/MAM-parsed/plus/D3-Job.json').read_text('utf-8'))
chapters = book['book39s'][0]['chapters']

def plus_verse_text(ep):
    parts = []
    for atom in ep:
        if isinstance(atom, str):
            parts.append(atom)
        elif isinstance(atom, dict):
            name = atom.get('tmpl_name', '')
            args = atom.get('tmpl_args', [])
            if name in ('קו"כ', 'קו"כ-אם') and len(args) >= 2:
                if isinstance(args[1], str):
                    parts.append(args[1])
            elif name == 'נוסח' and args:
                if isinstance(args[0], str):
                    parts.append(args[0])
                elif isinstance(args[0], dict):
                    parts.append(plus_verse_text([args[0]]))
            elif name.startswith('מ:כו"ק') and len(args) >= 2:
                qere = args[1]
                if isinstance(qere, str):
                    parts.append(qere)
                elif isinstance(qere, list):
                    parts.append(plus_verse_text(qere))
            elif name == 'מ:אות-מיוחדת-במילה' and len(args) >= 2:
                if isinstance(args[1], str):
                    parts.append(args[1])
    return ''.join(parts).strip()

# Job 1:1
print(plus_verse_text(chapters['א']['א'][2]))
```

## When to Use Which Format

- **Plain**: When you need content close to the Google Sheet, including page navigation markup
- **Plus**: When you want clean verse data with enhanced annotations (special letters, targeted ketiv-qere)
- **MAM-XML**: When you want simple verse text extraction without template parsing (see `copilot-instructions-mam-xml.md`)

For the Aleppo Codex alignment task, **MAM-XML** is the preferred source
since it provides clean verse text directly in the `text` attribute.
