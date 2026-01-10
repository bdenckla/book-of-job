""" Exports maybe_sep_lcloc """

from py import my_html


def maybe_sep_lcloc(record, sep):
    if lcloc := record.get("lcloc"):
        page = lcloc["page"]
        line = lcloc["line"]
        column = lcloc["column"]
        abs_line, m_sp_cfb = _maybe_sp_cfb(line)
        m_sp_ibl = _maybe_sp_ibl(lcloc)
        return [
            sep,
            _lc_full_page_anc(page),
            f" (line {abs_line}{m_sp_cfb}{m_sp_ibl}, col. {column})",
        ]
    return []


def _lc_full_page_anc(page):
    # E.g. page == "397B"
    href = f"https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F{page}.jpg"
    return my_html.anchor_h(f"LC page {page}", href)


def _maybe_sp_ibl(lcloc):
    if ibl := lcloc.get("including-blank-lines"):
        return f" (including {ibl} blank line{'s' if ibl != 1 else ''})"
    return ""


def _maybe_sp_cfb(line):
    if line < 0:
        return -line, " (counting from bottom of page)"
    return line, ""
