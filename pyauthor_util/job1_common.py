from pyauthor_util import author
from pyauthor_util.job1_make_per_case_data import make_example_row


def intro(expanding, each, jda=None):
    return [
        author.para(_here_is(expanding, jda)),
        author.para(_each(each)),
        author.table_c(make_example_row()),
        author.para(_where()),
    ]


def _here_is(expanding, jda=None):
    out = [
        f"Here is a table {expanding} upon the entries for the book of Job",
        " in BHL Appendix A.",
    ]
    if jda is not None:
        jdae = [" For more details, see the ", jda]
        return out + jdae
    return out


def _each(each):
    return [f"{each} entry below takes the following form:"]


def _where():
    return [
        "Where c:v is the chapter and verse of the book of Job and BHL-A is entry in the BHL Appendix A."
    ]
