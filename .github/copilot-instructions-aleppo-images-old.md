# Procedure: Adding Aleppo Codex (μA) Images

This describes the workflow for handling GitHub issues titled "Add Aleppo Codex image for ..." or "Add μA image for ...".

## 1. Find the next issue

```powershell
gh issue list -s open --json number,title -L 30
```

Look for issues mentioning "Aleppo Codex image" or "μA image". Get the issue details:

```powershell
gh issue view <number> --json title,body
```

## 2. Look up the quirkrec

Search `out/quirkrecs.json` for the verse (e.g. `"qr-cv": "6:17"`). Note:
- **`qr-consensus`**: the consensus reading (what Aleppo is expected to match)
- **`qr-lc-proposed`**: what μL (Leningrad Codex) has instead
- **`qr-what-is-weird`**: short description of the difference
- **`qr-word-id`**: used for filename qualification when needed
- **`qr-lc-img`**: the existing LC image filename (tells you the CCVV pattern)

## 3. Show the full verse

Find the verse in `..\..\GitRepos\mam-for-sefaria\out\csv\Job.csv`:

```powershell
Select-String -Path "..\..\GitRepos\mam-for-sefaria\out\csv\Job.csv" -Pattern "6.17" | Select-Object -First 3 Line
```

## 4. Open mgketer.org

Open the Aleppo Codex image for the relevant chapter in the user's default browser:

```powershell
Start-Process "https://www.mgketer.org/mikra/29/{chnu}/1/mg/106"
```

For Job, `bknu` is always **29**. For other books, look up via `pycmn.bib_locales.get_bknu(bk39id)`.

Present the word and what to check, phrased as: "checking that indeed Aleppo matches consensus in having [consensus accent] (as opposed to μL, which has [divergent accent])".

## 5. User takes a screenshot

Wait for the user to take a screenshot from mgketer.org.

## 6. Move and rename the screenshot

Find the most recent screenshot:

```powershell
Get-ChildItem "$env:USERPROFILE\OneDrive\Pictures\Screenshots" | Sort-Object LastWriteTime -Descending | Select-Object -First 3 Name, LastWriteTime
```

Copy to `docs/jobn/img/` with the naming convention:
- **One quirkrec for the verse**: `Aleppo-CCVV.png` (e.g. `Aleppo-3405.png`)
- **Multiple quirkrecs for the verse**: `Aleppo-CCVV-WORDID.png` (e.g. `Aleppo-2230-YMLE.png`)

Where `CCVV` is the zero-padded chapter and verse (e.g. `0617` for 6:17, `2230` for 22:30), and `WORDID` is the `qr-word-id` value from the quirkrec.

Check how many quirkrecs share the same verse to decide whether qualification is needed.

## 7. Rebuild HTML

```powershell
python ./main_gen_misc_authored_english_documents.py
```

## 8. Preview in Simple Browser

A local HTTP server should be running (start one if needed):

```powershell
python -m http.server 8932 --directory docs
```

Then open in VS Code's Simple Browser:

```
http://localhost:8932/jobn/job1_full_list_details.html#row-CCVV
```

or with word-ID qualifier if applicable:

```
http://localhost:8932/jobn/job1_full_list_details.html#row-CCVV-WORDID
```

## 9. Commit and push

After the user confirms it looks good:

```powershell
git add docs/jobn/img/Aleppo-CCVV.png
git commit -m "Add μA image for CC:VV. Closes #<number>"
git push
```
