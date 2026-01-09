""" Exports main """

from py import two_col_css_styles as tcstyles
from py import my_html
from pyauthor import prov1


def write_index_dot_html(css_hrefs, out_path, prov1_anchor):
    body_contents = (
        prov1_anchor,
    )
    write_ctx = my_html.WriteCtx(
        "Proverbs Documents", out_path, css_hrefs=css_hrefs
    )
    my_html.write_html_to_file(body_contents, write_ctx)


def main():
    # XXX TODO: rm *.html (to avoid stale files when output names change)
    #
    provn_rel_top = "docs/provn"
    provn_rel_docs = "./provn"
    #
    css_href = "style.css"
    tcstyles.make_css_file_for_authored(f"docs/{css_href}")
    tcstyles.make_css_file_for_authored(f"{provn_rel_top}/{css_href}")
    #
    tdm_ch = provn_rel_top, css_href
    #
    prov1.gen_html_file(tdm_ch)
    prov1_anchor = prov1.anchor(provn_rel_docs)
    #
    write_index_dot_html((css_href,), "docs/index.html", prov1_anchor)



if __name__ == "__main__":
    main()
