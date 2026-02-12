"""Common utilities for job documents"""

from py import my_html
from pyauthor_util import author


def d4_toh(bhq):
    return f"{bhq} Job: quirks in μA"


D4_TITLE = d4_toh("BHQ")
D4_H1_CONTENTS = d4_toh("$BHQ")
D4_FNAME = "job4_quirks_in_mu_a.html"


D5_TITLE = "Orphan pointing"
D5_H1_CONTENTS = D5_TITLE
D5_FNAME = "job5_orphan_qere_points.html"


def d5_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D5_FNAME}")
    return author.std_anchor(anc, D5_H1_CONTENTS)


def d4_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D4_FNAME}")
    return author.std_anchor(anc, D4_H1_CONTENTS)


def d3_toh(bhq, uxlc):
    return f"{bhq} Job: cases where {uxlc} could have helped"


D3_TITLE = d3_toh("BHQ", "UXLC")
D3_H1_CONTENTS = d3_toh(bhq="$BHQ", uxlc="$UXLC")
D3_FNAME = "job3_uxlc.html"


def d3_anchor(jobn_dir="."):
    anc = my_html.anchor_h("document", f"{jobn_dir}/{D3_FNAME}")
    return author.std_anchor(anc, D3_H1_CONTENTS)


def d2_toh(bhq):
    return f"{bhq} Job was made in a bubble"


D2_TITLE = d2_toh("BHQ")
D2_H1_CONTENTS = d2_toh("$BHQ")
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
