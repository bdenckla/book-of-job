""" Exports main """

from py import two_col_css_styles as tcstyles
from py import my_html
from pyauthor import job1_overview
from pyauthor import job1_details


def write_index_dot_html(css_hrefs, out_path, d1v_anchor):
    body_contents = (d1v_anchor,)
    write_ctx = my_html.WriteCtx("Job Documents", out_path, css_hrefs=css_hrefs)
    my_html.write_html_to_file(body_contents, write_ctx)


def main():
    # XXX TODO: rm *.html (to avoid stale files when output names change)
    #
    jobn_rel_top = "docs/jobn"
    jobn_rel_index_html = "./jobn"
    #
    css_href = "style.css"
    tcstyles.make_css_file_for_authored(f"docs/{css_href}")
    tcstyles.make_css_file_for_authored(f"{jobn_rel_top}/{css_href}")
    #
    tdm_ch = jobn_rel_top, css_href
    #
    job1_details.gen_html_file(tdm_ch)
    #
    d1v_anchor = job1_overview.gen_html_file(tdm_ch, jobn_rel_index_html)
    #
    write_index_dot_html((css_href,), "docs/index.html", d1v_anchor)


if __name__ == "__main__":
    main()
