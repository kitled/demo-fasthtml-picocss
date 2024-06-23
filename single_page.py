from fasthtml.common import * # type: ignore
from fasthtml.js import MarkdownJS, SortableJS, HighlightJS
from fastapi import Request

#—————————————————————————————————————————————————————————————————————————————
# HTML 5 conventions
html = Html(lang='en', 
    # data_theme="light"
    )
head = (
    Meta(charset="utf-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1"),
    Meta(name="color-scheme", content="light dark"),
    )
#—————————————————————————————————————————————————————————————————————————————
# Page-specific
title = "FastHTML 🧡 Pico CSS"
footer_text = P("Made by kit using FastHTML & Pico CSS + PrismJS, June 2024.")
#—————————————————————————————————————————————————————————————————————————————
# <head> scripts & css
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
#—————————————————————————————————————————————————————————————————————————————
# FastHTML app
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

#—————————————————————————————————————————————————————————————————————————————
# Features
# Dark/Light mode toggle
def theme_switch():
    return Article(
        Button(
        f"Toggle theme",
        cls="contrast",
        hx_post="/toggle_theme",
        hx_swap="outerHTML",
        hx_target="#theme-switcher"
        ),
        id="theme-switcher",
        aria_label="Theme switcher",
    )

#—————————————————————————————————————————————————————————————————————————————
# Helper functions to build proper HTML structure (nesting, etc.)

def div_code(code, lang=None):
    '''Returns a <div> wrapping a <pre><code> block.
    Use within <h4> sections to display code examples.
    '''
    return Div(
        Pre(
            Code(code,
                cls="highlight language-"+lang if lang else "highlight",
            ),
        ),
        cls="pre-code",
    )

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

#   ➕
def art_c(*c): # c for content
    return (*c, )

#   ➕
def art_footer(html, python):
    return Footer(Pre(Code(html)), Pre(Code(python)))

#   🡇
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



# code_N_N_N
# body_N_N_N
# sec_N_N_N for section

code_1_1_1 = div_code(
    """<link rel="stylesheet" href="css/pico.min.css" />""",
    lang="html",
    )
#    🡇🡇🡇
body_1_1_1 = (
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
    code_1_1_1,
)
#   🡇🡇🡇
sec_1_1_1 = section(body_1_1_1,
    lv=4, title="Install manually",
)

#  ＋

code_1_1_2 = div_code(
"""<link 
  rel="stylesheet" 
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
/>""",
  lang="html",
)
#    🡇🡇🡇
body_1_1_2 = P(
    """Alternatively, you can use """,
    A(
        "jsDelivr CDN",
        rel="noopener noreferrer",
        href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/",
        target="_blank"
    ),
    """ to link """,
    Code("pico.min.css"),
    '.',
    code_1_1_2,
)
# 🡇🡇🡇
sec_1_1_2 = section(body_1_1_2,
    lv=4, title="Usage from CDN",
)

#  ＋

code_1_1_5 = div_code(
"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark" />
    <link rel="stylesheet" href="css/pico.min.css">
    <title>Hello world!</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello world!</h1>
    </main>
  </body>
</html>""",
    lang="html",
)
# 🡇🡇🡇
sec_1_1_5 = section(code_1_1_5,
    lv=4, title="Starter HTML template",
)

#   🡇🡇🡇
# this must nest all lv4_s
sec_1_1_0 = section(
    P("There are 4 ways to get started with pico.css:"),
    sec_1_1_1,
    sec_1_1_2,
    sec_1_1_5,
    lv=3, title="Quick start",
    desc=(
        """Link """,
        Code("pico.css"),
         """ manually or via CDN for a dependency-free setup, or use NPM or Composer for advanced usage.""",
    ),
)





sec_1_3_0 = section(
    P("""The default…"""),
    theme_switch(),
    lv=2, title="Color Schemes",
    desc=(
        """Pico CSS comes with both Light and Dark color schemes, automatically enabled based on user preferences."""
    )
)





#  🡇
# lv2_s must nest all lv3_s
sec_1_0_0 = section(
    sec_1_1_0,
    sec_1_3_0,
    lv=2, title="Getting started",
)





sec_2_0_0 = section(

    lv=2, title="Customization",
)



sec_3_0_0 = section(

    lv=2, title="Layout",
)



sec_4_0_0 = section(

    lv=2, title="Content",
)



sec_5_0_0 = section(

    lv=2, title="Forms",
)


sec_6_0_0 = section(

    lv=2, title="Components",
)



sec_7_0_0 = section(
    
    lv=2, title="About",
)

sections = (
    sec_1_0_0,
    sec_2_0_0,
    sec_3_0_0,
    sec_4_0_0,
    sec_5_0_0,
    sec_6_0_0,
    sec_7_0_0,
)


site = (main(sections))

# Home page
@rt("/")
def get():
    return html, site

# Dark/Light theme switch
@rt("/toggle_theme")
async def post(request: Request):
    # Get the current theme from the button's name attribute
    current_theme = request.headers.get("HX-Trigger-Name", "").split("(")[-1].strip(")")
    new_theme = "light" if current_theme == "dark" else "dark"

    response_content = f"""
    <article id="theme-switcher" aria-label="Theme switcher">
        <button class="contrast" hx-post="/toggle_theme" hx-swap="outerHTML" hx-target="#theme-switcher" name="theme-toggle({new_theme})">
            Make {new_theme}!
        </button>
    </article>
    <script>
        document.documentElement.setAttribute('data-theme', '{current_theme}');
    </script>
    """
    
    return HTMLResponse(content=response_content)
