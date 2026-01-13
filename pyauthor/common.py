""" Common utilities for job documents """

from py import my_html
from pyauthor_util import author


D2_TITLE = "BHQ: Too Little, Too Late"
D2_H1_CONTENTS = "BHQ: Too Little, Too Late"
D2_FNAME = "job2.html"


def d2_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D2_FNAME}")
    return author.std_anchor(anc, D2_H1_CONTENTS)


D1D_TITLE = "Book of Job Document 1 - Details"
D1D_H1_CONTENTS = "Book of Job (ספר איוב) Document 1 - Details"
D1D_FNAME = "job1_details.html"


def d1d_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D1D_FNAME}")
    return author.std_anchor(anc, D1D_H1_CONTENTS)


D1V_TITLE = "Book of Job Document 1 - Overview"
D1V_H1_CONTENTS = "Book of Job (ספר איוב) Document 1 - Overview"
D1V_FNAME = "job1_overview.html"


def d1v_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D1V_FNAME}")
    return author.std_anchor(anc, D1V_H1_CONTENTS)
