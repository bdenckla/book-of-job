"""Resolve this repo's CODE root and its DATA root, which are one directory today.

THIS MODULE IS DELIBERATELY TWO-ROOTED, and that is the whole point of its
existence.  The code is still here in book-of-job, so ``code_root()`` and
``boj_data_root()`` return the same directory and every accessor below could just
as well have been a cwd-relative string.  They are named apart now, while the 701
tracked artifacts under ``gh-pages/`` and ``out/`` are an oracle that can prove a
path change harmless, so that the move out (Phase 3 of MAM-basics'
``doc/PLAN-evacuate-python-from-book-of-job.md``) changes one line rather than
auditing every path in the repo:

  * the CODE root is ``code_root()`` -- what the source lints scan, where the
    quirk-record package sits, what ``git`` acts on.  It follows the Python;
  * the DATA root is ``boj_data_root()`` -- ``gh-pages/``, ``out/`` and the
    gitignored ``.novc/``.  It stays here, with the Pages site served out of it.

What this replaces is of two kinds, and only the first kind is greppable.  Plain
cwd-relative literals -- ``"gh-pages/jobn"``, ``"./out"``, ``Path("pyauthor_qr")``,
an argparse ``default="gh-pages"`` -- resolved correctly only while the process ran
from this repo's root, and one of them would have overwritten MAM-basics' own
tracked ``gh-pages/index.html`` had a verification run been done from there.  The
second kind is a ``Path(__file__)`` walk that was cwd-independent already and still
conflated the two roots: ``check_spelling_in_html.main`` composed the ``gh-pages``
tree it reads and the custom dictionary that sits beside its own module off one
``Path(__file__).parent``, which is one expression standing for both roots at once.

WHY THIS DOES NOT DELEGATE TO ``mb_cmn.paths``, as ``py/uxlc_paths.py`` and
``py/hkq_paths.py`` in MAM-basics do.  This repo does not vendor ``mb_cmn/paths.py``
and must not start: ``paths.repo_root()`` is ``Path(__file__).resolve().parents[2]``,
correct for a ``py/mb_cmn/`` two levels down and wrong here, where ``mb_cmn/`` sits at
the repo root and that walk lands on ``GitRepos``.  Editing a vendored copy to suit
one repo is the drift Phase 0 of that plan exists to end, so ``code_root()`` below
walks up to ``.git`` instead -- depth-independent, and the same idiom the shared
``check_escape_sequences.py``, ``check_mark_order.py`` and ``fix_mark_order.py``
already use here.

AT THE MOVE, two lines change.  ``boj_data_root()`` becomes
``paths.require_sibling("book-of-job", paths.sibling_repo("book-of-job"))``, because
nothing else composes a data path off anything but that function; ``code_root()`` may
become ``paths.repo_root()`` or stay as it is, the ``.git`` walk resolving to
MAM-basics' root once the code lives there.
"""

from pathlib import Path

DATA_REPO_NAME = "book-of-job"

D1D_DIR = "jobn-details"
"""Directory name of the per-quirk detail pages, under ``gh_pages_dir()``.

Defined here rather than in ``pyauthor_util.common_titles_etc``, which imports it
from here, because the name is used as a path segment AND as an href segment
(``d1d_detail_href``) and the two must not drift apart.
"""


def code_root() -> Path:
    """Repo root of the Python: the nearest ancestor of this file holding ``.git``.

    Walks rather than counting ``parents[N]`` so that it stays right at whatever
    depth this file comes to rest -- the repo root today, MAM-basics' ``py/``
    after the move.  See the module docstring for why it does not delegate to
    ``mb_cmn.paths.repo_root()``.
    """
    here = Path(__file__).resolve()
    for candidate in here.parents:
        if (candidate / ".git").exists():
            return candidate
    raise SystemExit(f"{here} is not inside a git repository")


def boj_data_root() -> Path:
    """Path to the book-of-job corpus this code reads and writes.

    The one line that changes when the Python moves out -- see the module docstring.
    """
    return code_root()


def gh_pages_dir() -> Path:
    """Published-HTML tree, 694 tracked files, served at bdenckla.github.io/book-of-job.

    THE DEPLOY ROOT, not any one document under it: ``.github/workflows/pages.yml``
    hands exactly this directory to ``upload-pages-artifact``.  515 of those 694 are
    PNGs that no program in this repo writes, so a full regeneration rewrites a
    minority of this tree; see the plan's Phase 0 record for the split.
    """
    return boj_data_root() / "gh-pages"


def out_dir() -> Path:
    """Generated-JSON tree, 7 tracked files.

    Six are written by ``main_gen_misc_authored_english_documents``; the seventh,
    ``cam1753_crops_path()`` below, is appended to by the manual crop-ingest step
    and is the one file of the 701 whose checkout is still CRLF.
    """
    return boj_data_root() / "out"


def novc_dir() -> Path:
    """Gitignored scratch tree (``<data_root>/.novc``), where the two crop editors write."""
    return boj_data_root() / ".novc"


def jobn_dir() -> Path:
    """The main document's own directory (``<gh_pages_dir>/jobn``).

    Passed down the authoring pipeline as ``jobn_rel_top`` and used there purely as a
    filesystem path -- to delete stale HTML, to write each page, and to test whether an
    optional image exists.  The hrefs that reach the published pages are built from the
    bare filename instead, which is why turning this from a relative string into an
    absolute path leaves every artifact byte-identical.
    """
    return gh_pages_dir() / "jobn"


def jobn_img_dir() -> Path:
    """The main document's image tree (``<jobn_dir>/img``), 485 tracked PNGs."""
    return jobn_dir() / "img"


def aleppo_img_dir() -> Path:
    """Aleppo crops (``<jobn_img_dir>/Aleppo``), 160 tracked PNGs, written by no program here."""
    return jobn_img_dir() / "Aleppo"


def cam1753_img_dir() -> Path:
    """Cam1753 crops (``<jobn_img_dir>/cam1753``), 160 tracked PNGs.

    The only image tree here with even a manual producer: ``main_apply_cam1753_crops``
    writes it from a hand-made crop-editor export it takes as its argument.
    """
    return jobn_img_dir() / "cam1753"


def jobn_details_dir() -> Path:
    """The per-quirk detail pages (``<gh_pages_dir>/jobn-details``), 160 tracked HTML."""
    return gh_pages_dir() / D1D_DIR


def index_html_path() -> Path:
    """The site's landing page (``<gh_pages_dir>/index.html``).

    Spelled ``"gh-pages/index.html"`` until Phase 1, which is the same relative path
    MAM-basics' own landing page has -- so a verification run from MAM-basics, the
    convention the UXLC-utils and holman-ketiv-qere plans both used, would have
    overwritten a tracked file there rather than failing.
    """
    return gh_pages_dir() / "index.html"


def enriched_quirkrecs_path() -> Path:
    """The enriched quirk records (``<out_dir>/enriched-quirkrecs.json``).

    Written by ``main_gen_misc_authored_english_documents`` and read at MODULE IMPORT
    TIME by the two crop editors and by ``main_list_missing_aleppo_imgs``, which is the
    only sequencing among this repo's five entry points.
    """
    return out_dir() / "enriched-quirkrecs.json"


def cam1753_crops_path() -> Path:
    """Hand-made crop coordinates (``<out_dir>/cam1753-crops.json``), read by the authoring
    pipeline and appended to by ``main_apply_cam1753_crops``."""
    return out_dir() / "cam1753-crops.json"


def uxlc_dir() -> Path:
    """This repo's UXLC snapshot (``<data_root>/py_uxlc_loc/UXLC``), 39 XML, one per book.

    DATA under a ``py_``-prefixed directory, which is a trap this repo sets for anyone
    reading ``git ls-files`` by prefix: ``py_uxlc_loc/`` holds 40 data files as well as
    its 9 ``.py``, and the sibling ``py_ac_loc/`` holds 76 tracked files and no ``.py``
    at all.  At UXLC 2.5 since Phase 0, byte-identical to MAM-basics' ``in/UXLC-39/``
    and to UXLC-utils' copy.
    """
    return boj_data_root() / "py_uxlc_loc" / "UXLC"


def lci_recs_path() -> Path:
    """Leningrad column-index records (``<data_root>/py_uxlc_loc/UXLC-misc/lci_recs.json``).

    Hand-indexed for Job and held nowhere else until Phase 0 sent the finer records for
    pages 397A and 406A upstream.  The location cross-check goes quiet on this copy and
    prints two ``fline mismatch`` lines on MAM-basics' coarser one, which is how a
    regression here announces itself.
    """
    return boj_data_root() / "py_uxlc_loc" / "UXLC-misc" / "lci_recs.json"
