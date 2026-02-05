""" Common utilities for job documents """

from py import my_html
from pyauthor_util import author


D4_TITLE = "BHQ Job: quirks in μA"
D4_H1_CONTENTS = D4_TITLE
D4_FNAME = "job4_quirks_in_mu_a.html"


def d4_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D4_FNAME}")
    return author.std_anchor(anc, D4_H1_CONTENTS)


D3_TITLE = "BHQ Job: cases where UXLC could have helped"
D3_H1_CONTENTS = D3_TITLE
D3_FNAME = "job3_uxlc.html"


def d3_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D3_FNAME}")
    return author.std_anchor(anc, D3_H1_CONTENTS)


D2_TITLE = "BHQ Job was made in a bubble"
D2_H1_CONTENTS = D2_TITLE
D2_FNAME = "job2_main_article.html"


def d2_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D2_FNAME}")
    return author.std_anchor(anc, D2_H1_CONTENTS)


D1D_TITLE = "Quirks in μL in Job"
D1D_H1_CONTENTS = D1D_TITLE
D1D_FNAME = "job1_full_list_details.html"


def d1d_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D1D_FNAME}")
    return author.std_anchor(anc, D1D_H1_CONTENTS)


D1V_TITLE = "Quirks in μL in Job - Overview"
D1V_H1_CONTENTS = D1V_TITLE
D1V_FNAME = "job1_full_list_overview.html"


def d1v_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D1V_FNAME}")
    return author.std_anchor(anc, D1V_H1_CONTENTS)
