from fasthtml.common import * # type: ignore
from fasthtml.js import MarkdownJS, SortableJS, HighlightJS

html = Html(lang='en')
head = (
    Meta(charset="utf-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1"),
    Meta(name="color-scheme", content="light dark"),
    )

title = "FastHTML 🧡 Pico CSS"
footer_text = P("Made by kit using FastHTML & Pico CSS + PrismJS, June 2024.")

pico_css = Link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css",
    type="text/css"
    )
page_css = Link(
    rel="stylesheet",
    href="style/single-page.css",
    type="text/css"
    )

app = FastHTML(hdrs=(
    head,
    pico_css,
    page_css,
    MarkdownJS('.markdown'),
    SortableJS('.sortable'),
    HighlightJS('.highlight'),
    ))
rt = app.route
@rt("/{fname:path}.{ext:static}") # Serve static files
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}') # type: ignore


# _Code = Code  # Trick! 😼
# def Code(*args, cls=None, **kwargs):
#     '''Hardcode `highlight` class.
#     '''
#     if cls:
#         cls = f"highlight {cls}"
#     else:
#         cls = "highlight"
#     return _Code(*args, cls=cls, **kwargs)


# H2 = [
#     "Getting started",
#     "Customization",
#     "Layout",
#     "Content",
#     "Forms",
#     "Components",
#     "About",
#     ]

# We define a bunch of functions that produce the ad hoc layout of the page.
# Most implement the generic FastHTML function, but some are specific to the page.
# The former is usually named like the FastHTML primitive without capitalization.
# E.g. "article", "section".
# Functions specific to the page have contextual names, e.g. "heading", "art_header", "art_footer".


def aside(*aside_tags):
    '''Returns an <aside> block. TODO: Implementation lol 😹
    `aside_tags` needs to be created (ToC) from the list of H2, H3, H4…
    '''
    return Aside(aside_tags)


def heading(lv:int, title:str, desc=None):
    '''Returns a header block with title and anchor link. Followed by optional description.
    '''
    h = [H1, H2, H3, H4, H5, H6]
    hn = h[lv-1]
    anchor = title.lower().replace(' ', '-')
    return (
        hn(
            title,
            A(
                '🔗',
                href='#'+anchor,
                id=anchor,
                cls='secondary',
                tabindex="-1",
            )
        ),
        P(desc) if desc else None,
    )

Style("""#content > section > section > p:nth-child(2) {}""")

#   +
def art_c(*c): # c for content
    return (*c, )
#   +
def art_footer(html, python):
    return Footer(Pre(Code(html)), Pre(Code(python)))
#   =
def article(c, hd=None, ft=None, **kwargs):
    return Card(*c, header=hd, footer=ft, **kwargs)


# c: lv2_s & lv3_s contain other sections (lv3_s & lv4_s respectively);
#    lv4_s contains c_n_m_k (tuple of HTML tags)
def section(*c, lv:int, title:str, desc=None, **kwargs):
    return Section(heading(lv=lv, title=title, desc=desc), *c, **kwargs)

# We wrap all lv2 (MAIN) sections in a div with proper id and role.
def div_lv2_s(*sections, **kwargs):
    return Div(*sections, id="content", role="document", **kwargs)

# Create <main> with flat lv2 (MAIN) sections. Optional aside etc.
def main(*lv2_s, aside_tags=None, **kwargs):
    return (
        Main(
            aside(aside_tags) if aside_tags else None,
            div_lv2_s(*lv2_s, **kwargs),
            cls="container",
        )
    )


def div_code(code, lang):
    return Div(
        Pre(
            Code(code,
                cls="highlight language-"+lang,
            ),
        ),
        cls="pre-code",
    ),



# s for section
# c for content
# d for div

c_1_1_1 = (
    P(
        A(
            "Download Pico",
            rel="noopener noreferrer",
            href="https://github.com/picocss/pico/archive/refs/heads/main.zip",
            target="_blank"
        ),
        """ and link """,
        Code("/css/pico.min.css"),
        """ in the """,
        Code("""<head>""", cls="highlight language-html", ),
        """ of your website.""",
    ),
    div_code("""<link rel="stylesheet" href="css/pico.min.css" />""", lang="html"),
)
#  🡇
s_1_1_1 = section(
    c_1_1_1,
    lv=4, title="Install manually",
)

#  ＋

c_1_1_2 = P(
    """Alternatively, you can use """,
    A(
        "jsDelivr CDN",
        rel="noopener noreferrer",
        href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/",
        target="_blank"
    ),
    """ to link """,
    Code("pico.min.css"),
    '.'
)
#  🡇
s_1_1_2 = section(
    c_1_1_2,
    lv=4, title="Usage from CDN",
)

#  ＋









#  🡇
# this must nest all lv4_s
s_1_1_0 = section(
    P("There are 4 ways to get started with pico.css:"),
    s_1_1_1,
    s_1_1_2,
    lv=3, title="Quick start",
    desc=(
        """Link """,
        Code("pico.css"),
         """ manually or via CDN for a dependency-free setup, or use NPM or Composer for advanced usage.""",
    ),
)









#  🡇
# lv2_s must nest all lv3_s
s_1_0_0 = section(
    s_1_1_0,
    lv=2, title="Getting started",
)





# # Create H2 headings
# headings = []
# for h in H2:
#     headings.append(heading(h, 2))



site = (main(s_1_0_0))

# Home page
@rt("/")
def get():
    return site
