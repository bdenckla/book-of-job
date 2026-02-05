""" Exports para_and_table """

from pyauthor_util import author
from pyauthor_util.all_quirks import AllQuirks
from pyauthor_util.job_ov_and_de import row_id


def para_and_table(aq: AllQuirks, para_func, group_key):
    group_of_quirkrecs = aq.qr_groups[group_key]
    record_count = len(group_of_quirkrecs)
    link = _table_of_quirks(aq.tdm_ch, group_key, aq.ov_and_de, group_of_quirkrecs)
    return [
        author.para(para_func(record_count)),
        author.para(link),
    ]


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
        table,
    ]
    author.help_gen_html_file(tdm_ch, fname, title, cbody)
    # Return link to the file
    record_count = len(group_of_quirkrecs)
    link_text = f"View {record_count} records"
    return author.anc_h(link_text, fname)
