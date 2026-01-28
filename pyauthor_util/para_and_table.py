""" Exports para_and_table """

from pyauthor_util import author
from pyauthor_util.job_ov_and_de import row_id


def para_and_table(para_func, ov_and_de, group_of_quirkrecs):
    return [
        author.para(para_func(len(group_of_quirkrecs))),
        _table_of_quirks(ov_and_de, group_of_quirkrecs),
    ]


def _overview(ov_and_de, quirkrec):
    the_row_id = row_id(quirkrec)
    return ov_and_de[the_row_id]["od-overview"]


def _table_of_quirks(ov_and_de, group_of_quirkrecs):
    rows = [_overview(ov_and_de, rec) for rec in group_of_quirkrecs]
    return author.table_c(rows)
