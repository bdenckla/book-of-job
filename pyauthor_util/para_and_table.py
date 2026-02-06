"""Generate paragraph and table of quirks for a group."""

from pyauthor_util import author
from pyauthor_util.all_quirks import AllQuirks
from pyauthor_util.intro import intro
from pyauthor_util.job_ov_and_de import row_id

__all__ = ["para_and_table"]


def para_and_table(aq: AllQuirks, para_func, group_key, extra_paras=None):
    group_of_quirkrecs = aq.qr_groups[group_key]
    record_count = len(group_of_quirkrecs)
    link = _table_of_quirks(aq.tdm_ch, group_key, aq.ov_and_de, group_of_quirkrecs)
    result = [author.para(para_func(record_count))]
    if extra_paras:
        for para in extra_paras:
            result.append(author.para(para))
    result.append(author.para(link))
    return result


def _overview(ov_and_de, quirkrec):
    the_row_id = row_id(quirkrec)
    return ov_and_de[the_row_id]["od-overview"]


def _table_of_quirks(tdm_ch, group_key, ov_and_de, group_of_quirkrecs):
    rows = [_overview(ov_and_de, rec) for rec in group_of_quirkrecs]
    table = author.table_c(rows)
    # Generate filename and title from group_key
    fname = f"grp_{group_key}.html"
    title = f"Group: {group_key}"
    # Generate the HTML file
    cbody = [
        author.heading_level_1(title),
        *intro("intro-header-only"),
        table,
    ]
    author.help_gen_html_file(tdm_ch, fname, title, cbody)
    # Return link to the file
    record_count = len(group_of_quirkrecs)
    link_text = f"View {record_count} entries"
    return author.anc_h(link_text, fname)
