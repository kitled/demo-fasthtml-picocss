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
title = Title('FastHTML 🧡 Pico CSS')
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
    # title,
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

def div_code_footer(code, lang=None):
    '''Returns a <footer> wrapping a <pre><code> block.
    Use in <article> to display code examples.
    '''
    return Footer(div_code(code, lang), cls="code")

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

def aside(*aside_tags):
    '''Returns an <aside> block. TODO: Implementation lol 😹
    `aside_tags` needs to be created (ToC) from the list of H2, H3, H4…
    '''
    return Aside(aside_tags)

#   ➕
# def art_c(*c): # c for content
#     return (*c, )

# #   ➕
# def art_footer(html, python):
#     return Footer(Pre(Code(html)), Pre(Code(python)))

#   🡇
def article(*c, hd=None, ft=None, card=False, **kwargs):
    return Card(*c, header=hd, footer=ft, **kwargs) if card else Article(*c, header=hd, footer=ft, **kwargs)


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

#—————————————————————————————————————————————————————————————————————————————
# PAGE CONTENTS

# pico_ → HTML/CSS code
# fh_   → FastHTML (Python) code
# body_ → Tags
# sec_  → section
# #_#_# → section number
# lv#_sec → <h#> (h2, h3, h4) section

#——————————————————————————————————————————————————————————————————————————— 1
# 1. Getting started
# 1.1. Quick start
# 1.2. Version picker
# 1.3. Color schemes
# 1.4. Class-less version
# 1.5. Conditional styling
# 1.6. RTL

#—————————————————————————————————— 1.1
# 1.1 Quick start
# 1.1.1 Install manually
# 1.1.2 Usage from CDN
# 1.1.3 Usage with NPM
# 1.1.4 Install with Composer
# 1.1.5 Starter HTML template

pico_1_1_1 = div_code(
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
    pico_1_1_1,
)
#   🡇🡇🡇
sec_1_1_1 = section(body_1_1_1,
    lv=4, title="Install manually",
)

#  ＋

pico_1_1_2 = div_code(
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
    pico_1_1_2,
)
# 🡇🡇🡇
sec_1_1_2 = section(body_1_1_2,
    lv=4, title="Usage from CDN",
)

#  ＋

pico_1_1_5 = div_code(
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

fh_1_1_5 = div_code(
"""from fasthtml.common import *

html = Html(lang='en')
head = (
    Meta(charset="utf-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1"),
    Meta(name="color-scheme", content="light dark"),
    Link(rel="stylesheet", 
        href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css"
        )
    )

app = FastHTML(hdrs=head)
rt = app.route

@rt("/")
def get():
    return html, Main(H1('Hello world!'), cls="container")""",
    lang="python",
)


# 🡇🡇🡇
sec_1_1_5 = section(pico_1_1_5, fh_1_1_5,
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


#—————————————————————————————————— 1.2



sec_1_2_0 = section(
    lv=3, title="Version picker",
    desc="Easily select the ideal Pico CSS version variant to match your project's needs."
)









#—————————————————————————————————— 1.3


body_1_3_1 = (
    P(  "Color schemes can be defined for the entire document using ",
        Code('<html data-theme="light">', cls='highlight language-html'),
        " or for specific HTML elements, such as ",
        Code('<article data-theme="dark">', cls='highlight language-html'),
        ".",
    ),
    P(  "Color schemes at the HTML tag level work great for elements such as ",
        Code('<a>', cls='highlight language-html'), ', ',
        Code('<button>', cls='highlight language-html'), ', ',
        Code('<table>', cls='highlight language-html'), ', ',
        Code('<input>', cls='highlight language-html'), ', ',
        Code('<textarea>', cls='highlight language-html'), ', ',
        Code('<select>', cls='highlight language-html'), ', ',
        Code('<article>', cls='highlight language-html'), ', ',
        Code('<dialog>', cls='highlight language-html'), ', ',
        Code('<progress>', cls='highlight language-html'), '.',
    ),
    P(  "CSS variables specific to the color scheme are assigned to every HTML tag. However, we have not enforced specific background and color settings across all HTML tags to maintain transparent backgrounds and ensure colors are inherited from the parent tag."
    ),
    P(  "For some other HTML tags, you might need to explicitly set ",
    Code('background-color', cls='highlight'),
    " and ",
    Code('color', cls='highlight'),
    "."
    ),
),

css_1_3_1 = div_code(
"""section {
  background-color: var(--pico-background-color);
  color: var(--pico-color);
}""",
    lang="css",
)


sec_1_3_1 = section(body_1_3_1, css_1_3_1, 
    lv=4, title="Usage",
)

def art_1_3_2(dark:bool=False) -> Article:
    if dark:
        theme, title = "dark", H2("Dark card")
    else:
        theme, title = "light", H2("Light card")
    aria = f"Forced {theme} theme example"
    pico = f"<article data-theme={theme}>\n  …\n</article>"
    footer = Footer(Pre(Code(pico, cls='highlight language-html'),),cls="code",)
    form = Form(
        Fieldset(
            Input(type="text",
                name="login",
                placeholder="Login",
                aria_label="Login",
                autocomplete="username",
            ),
            Input(type="password",
                name="password",
                placeholder="Password",
                aria_label="Password",
                autocomplete="current-password",
            ),
            Button("Login", type="submit"),
            cls='grid',
        ),
        Fieldset(
            Label(
                Input(type="checkbox", 
                    role="switch", 
                    name="switch", 
                    checked="",
                ),
                "Remember me",
            ),
        ),
    )
    return Article(
    title,
    form,
    footer,
    cls="card",
    data_theme=theme,
    aria_label=aria,
    )

art_1_3_2a = art_1_3_2()
art_1_3_2b = art_1_3_2(dark=True), 
fh_1_3_2 = P("FastHTML 🡇", cls="fh-cue"), div_code(
"""Article(…, data_theme="light")\nArticle(…, data_theme="dark")""", 
    lang="python",
    )

sec_1_3_2 = section(
    art_1_3_2a, 
    art_1_3_2b,
    fh_1_3_2,
    lv=4, title="Card example",
)

sec_1_3_0 = section(
    P("""The default color scheme is Light. The Dark scheme is automatically enabled if the user has dark mode enabled """, 
      Code("prefers-color-scheme: dark;", cls="highlight"), '.'),
    theme_switch(),
    sec_1_3_1,
    sec_1_3_2,
    lv=3, title="Color Schemes",
    desc=(
        """Pico CSS comes with both Light and Dark color schemes, automatically enabled based on user preferences."""
    )
)

#—————————————————————————————————— 1.4

sec_1_4_0 = section(
    lv=3, title="Class-less version",
    desc=(
        "Embrace minimalism with Pico’s ",
        Code(".classless"),
        " version, a semantic option for wild HTML purists who prefer a stripped-down approach.",
    ),
)

#—————————————————————————————————— 1.5

sec_1_5_0 = section(
    lv=3, title="Conditional styling",
    desc=(
        "Apply Pico CSS styles selectively by wrapping elements in a ",
        Code(".pico"),
        " container, ideal for mixed-style environments.",
    ),
)

#—————————————————————————————————— 1.6

sec_1_6_0 = section(
    lv=3, title="RTL",
    desc="Support for Right-To-Left text."
)

#  🡇
# lv2_s must nest all lv3_s
sec_1_0_0 = section(
    sec_1_1_0,
    sec_1_2_0,
    sec_1_3_0,
    sec_1_4_0,
    sec_1_5_0,
    sec_1_6_0,
    lv=2, title="Getting started",
)
#——————————————————————————————————————————————————————————————————————————— 2
# 2. Customization
# 2.1 CSS Variables
# 2.2 Sass
# 2.3 Colors

#—————————————————————————————————— 2.1

sec_2_1_0 = section(
    lv=3, title="CSS Variables",
    desc="Customize Pico's design system with over 130 CSS variables to create a unique look and feel."
)

#—————————————————————————————————— 2.2

sec_2_2_0 = section(
    lv=3, title="Sass",
    desc=(
        "Build your own minimal design system by compiling a custom version of Pico CSS framework with ",
        A("SASS"),
        "."),
)

#—————————————————————————————————— 2.3

sec_2_3_0 = section(
    lv=3, title="Colors",
    desc="Pico comes with 380 manually crafted colors to help you personalize your brand design system."
)


sec_2_0_0 = section(
    sec_2_1_0,
    sec_2_2_0,
    sec_2_3_0,
    lv=2, title="Customization",
)

#——————————————————————————————————————————————————————————————————————————— 3
# 3.Layout
# 3.1 Container
# 3.2 Landmarks & section
# 3.3 Grid
# 3.4 Overflow auto NEW

#—————————————————————————————————— 3.1
# 3.1 Container
# 3.1.1 Breakpoints
# 3.1.2 Fixed width
# 3.1.3 Fluid width
# 3.1.4 Semantic containers

body_3_1_1a = (
    P("Pico includes six default breakpoints. These breakpoints can be customized with ",
      A("Sass", href="https://picocss.com/docs/sass"), "."),
)

table_3_1_1 = Table(
    Thead(Tr(Th("Device"), Th("Breakpoint"), Th("Viewport"))),
    Tbody(
        Tr(Td("Extra small"), Td("<576px"), Td("100%")),
        Tr(Td("Small"), Td("≥576px"), Td("510px")),
        Tr(Td("Medium"), Td("≥768px"), Td("700px")),
        Tr(Td("Large"), Td("≥1024px"), Td("950px")),
        Tr(Td("Extra large"), Td("≥1280px"), Td("1200px")),
        Tr(Td("Extra extra large"), Td("≥1536px"), Td("1450px")),
    ),
)

body_3_1_1b = (
    P(Code(".container"),
    " and ",
    Code(".container-fluid"),
    " are not available in the ",
    A("class‑less version", href="https://picocss.com/docs/classless"),
    " (see ",
    A("Semantic containers", href="https://picocss.com/docs/container#semantic-containers"),
    " for an alternative)."),
)

sec_3_1_1 = section(
    body_3_1_1a,
    table_3_1_1,
    body_3_1_1b,
    lv=4, title="Breakpoints",
)

body_3_1_2 = (
    P(Code(".container"), " provides a centered container with a fixed width."),
    div_code(
"""<body>
  <main class="container">
    ...
  </main>
</body>
""", lang="html"),
)

sec_3_1_2 = section(
    body_3_1_2,
    lv=4, title="Fixed width",
)

body_3_1_3 = (
    P(Code(".container-fluid"), " provides a full-width container."),
    div_code(
"""<body>
  <main class="container-fluid">
    ...
  </main>
</body>
""", lang="html"),
)

sec_3_1_3 = section(
    body_3_1_3,
    lv=4, title="Fluid width",
)

body_3_1_4 = (
    P(
        "In the classless version, ",
        Code("<header>", cls="highlight"), ", ",
        Code("<main>", cls="highlight"), ", and ",
        Code("<footer>", cls="highlight"),
        " inside ",
        Code("<body>", cls="highlight"),
        " act as containers to define a centered or a fluid viewport."),
    P("See ", A("Class-less version", href="https://picocss.com/docs/classless"), "."),
)

sec_3_1_4 = section(
    body_3_1_4,
    lv=4, title="Semantic containers",
)

sec_3_1_0 = section(
    sec_3_1_1,
    sec_3_1_2,
    sec_3_1_3,
    sec_3_1_4,
    lv=3, title="Container",
    desc=("Use ", Code('.container'), "for a centered viewport or ", Code('.container-fluid'), " for a full-width layout.")
)

#—————————————————————————————————— 3.2
# 3.2 Landmarks & section
# 3.2.1 Landmarks
# 3.2.2 Custom root container
# 3.2.3 Section


body_3_2_1 = (
    P(
        Code("<header>", cls="highlight"), ", ",
        Code("<main>", cls="highlight"), ", and ",
        Code("<footer>", cls="highlight"),
        " as direct children of ",
        Code("<body>", cls="highlight"),
        " provide a responsive vertical padding.",
    ),
)

pico_3_2_1 = div_code(
"""<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
""", lang="html"),


sec_3_2_1 = section(
    body_3_2_1,
    pico_3_2_1,
    lv=4, title="Landmarks",
)

body_3_2_2a = (
    P(
        "If you need to customize the default root container for ",
        Code("<header>", cls="highlight"), ", ",
        Code("<main>", cls="highlight"), ", and ",
        Code("<footer>", cls="highlight"),
        ", you can recompile Pico with another CSS selector.",
    ),
    P("Useful for ", A("React", href="https://reactjs.org/"), ", ", A("Gatsby", href="https://www.gatsbyjs.com/"), " or ", A("Next.js", href="https://nextjs.org/"), "."),
)

pico_3_2_2a = div_code(
"""/* Custom Class-less version for React */
@use "pico" with (
  
  // Define the root element used to target <header>, <main>, <footer>
  // with $enable-semantic-container and $enable-responsive-spacings
  $semantic-root-element: "#root";
  
  // Enable <header>, <main>, <footer> inside $semantic-root-element as containers
  $enable-semantic-container: true;

  // Enable .classes
  $enable-classes: false;
)
""", lang="jsx"),

body_3_2_2b = (
    P("The code above will compile Pico with the containers defined like this:"),
)

pico_3_2_2b = div_code(
"""/* Containers */
#root > header,
#root > main,
#root > footer {
  ...
}
""", lang="css"),

body_3_2_2c = (
    P(
        "Learn more about ", 
        A("compiling a custom version of Pico with SASS", 
          href="https://picocss.com/docs/sass"), "."),
)

sec_3_2_2 = section(
    body_3_2_2a,
    pico_3_2_2a,
    body_3_2_2b,
    pico_3_2_2b,
    body_3_2_2c,
    lv=4, title="Custom root container",
)


body_3_2_3 = (
    P(
        Code("<section>", cls="highlight"), 
        " provides a responsive margin-bottom to separate your sections."),
)

sec_3_2_3 = section(
    body_3_2_3,
    lv=4, title="Section",
)

sec_3_2_0 = section(
    sec_3_2_1,
    sec_3_2_2,
    sec_3_2_3,
    lv=3, title="Landmarks & section",
    desc="Structure your pages with semantic landmarks and sections for better accessibility and graceful spacings.",
)

#—————————————————————————————————— 3.3
# 3.3 Grid
# 3.3.1 Syntax
# 3.3.2 About CSS Grids

art_3_3_1 = Article(
    Div(
        Div(1),
        Div(2),
        Div(3),
        Div(4),
        cls="grid"
    ),
    Footer(
        div_code(
"""<div class="grid">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>""", 
        lang="html"),
        cls="code",
    ),
    cls="component"
)

body_3_3_1 = (
    P("Columns intentionally collapse on small devices (", Code("<768px"), ")."),
    P(Code(".grid"), "is not available in the ", A("class‑less", href="https://picocss.com/docs/classless"), " version."),
)

sec_3_3_1 = section(
    art_3_3_1,
    body_3_3_1,
    lv=4, title="Syntax",
)

body_3_3_2 = (
    P("As Pico focuses on native HTML elements, we kept this grid system minimalist."),
    P("A complete grid system in flexbox, with all the ordering, offsetting, and breakpoints utilities, can be heavier than the total size of the Pico library. Not really in the Pico spirit."),
    P("If you need a quick way to prototype or build a complex layout, you can look at ", Strong("Flexbox grid layouts"), "—for example, ", A("Bootstrap Grid System", href="https://getbootstrap.com/docs/4.2/getting-started/contents/"), " or ", A("Flexbox Grid", href="http://flexboxgrid.com/"), "."),
    P("If you need a light and custom grid, you can look at CSS Grid Generators—for example, ", A("CSS Grid Generator", href="https://cssgrid-generator.netlify.com/"), ", ", A("Layoutit!", href="http://grid.layoutit.com/"), " or ", A("Griddy", href="https://griddy.io/"), "."),
    P("Alternatively, you can ", A("learn about CSS Grid", href="https://learncssgrid.com/"), "."),
)

sec_3_3_2 = section(
    body_3_3_2,
    lv=4, title="About CSS Grids",
)



sec_3_3_0 = section(
    sec_3_3_1,
    sec_3_3_2,
    lv=3, title="Grid",
    desc=(
        "Create minimal responsive layouts with ", 
        Code(".grid"), 
        " to enable auto-layout columns."),
)

#—————————————————————————————————— 3.4
# 3.4 Overflow auto


body_3_4_1 = (
    P("Useful to have responsive ", Code("<table>", cls="highlight"), "."),
)

table_3_4_1 = (Div(
    Table(
        Thead(
            Tr(Th("Heading"),Th("Heading"),Th("Heading"),Th("Heading"),
               Th("Heading"),Th("Heading"),Th("Heading"),Th("Heading"),
               Th("Heading"),Th("Heading"),Th("Heading"),Th("Heading"))),
        Tbody(
            Tr(Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),
               Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell")),
            Tr(Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),
               Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell")),
            Tr(Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),
               Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell"),Td("Cell")),)
    ), 
    cls="overflow-auto",
))

pico_3_4_1 = div_code(
"""<div class="overflow-auto">
  <table>
    …
  </table>
</div>""", 
        lang="html"
)

sec_3_4_0 = section(
    body_3_4_1,
    table_3_4_1,
    pico_3_4_1,
    lv=3, title="Overflow auto",
    desc=(
        Code(".overflow-auto"),
        " enables automatic scrollbars to an element if its content extends beyond its limits."),
)

sec_3_0_0 = section(
    sec_3_1_0,
    sec_3_2_0,
    sec_3_3_0,
    sec_3_4_0,
    lv=2, title="Layout",
)
#————————————————————————————————————————————————————————————————————————————4
# 4. Content
# 4.1 Typography
# 4.2 Link
# 4.3 Button
# 4.4 Table

#—————————————————————————————————— 4.1
# 4.1 Typography
# 4.1.1 Font sizes
# 4.1.2 Headings
# 4.1.3 Heading group
# 4.1.4 Inline text elements
# 4.1.5 Blockquote
# 4.1.6 Horizontal rule

table_4_1_1a = Table(
    Thead(
        Tr(Th("Breakpoint"),Th("xs"),Th("sm"),Th("md"),Th("lg"),Th("xl"),Th("xxl")),
    ),
    Tbody(
        Tr(Td("Base"),Td("16px"),Td("17px"),Td("18px"),    Td("19px"),   Td("20px"),    Td("21px")),
        Tr(Td(Code("<h1>")   ),  Td("32px"),Td("34px"),    Td("36px"),   Td("38px"),    Td("40px"),  Td("42px")),
        Tr(Td(Code("<h2>")   ),  Td("28px"),Td("29.75px"), Td("31.5px"), Td("33.25px"), Td("35px"),  Td("36.75px")),
        Tr(Td(Code("<h3>")   ),  Td("24px"),Td("25.5px"),  Td("27px"),   Td("28.5px"),  Td("30px"),  Td("31.5px")),
        Tr(Td(Code("<h4>")   ),  Td("20px"),Td("21.25px"), Td("22.5px"), Td("23.75px"), Td("25px"),  Td("26.25px")),
        Tr(Td(Code("<h5>")   ),  Td("18px"),Td("19.125px"),Td("20.25px"),Td("21.375px"),Td("22.5px"),Td("23.625px")),
        Tr(Td(Code("<h6>")   ),  Td("16px"),Td("17px"),    Td("18px"),   Td("19px"),    Td("20px"),  Td("21px")),
        Tr(Td(Code("<small>")),  Td("14px"),Td("14.875px"),Td("15.75px"),Td("16.625px"),Td("17.5px"),Td("18.375px")),
    ),
    cls="overflow-auto",
)

body_4_1_1a = P("In ", Code("rem"), " units:")

table_4_1_1b = Table(
    Thead(
        Tr(Th("Breakpoint"),Th("xs"),Th("sm"),Th("md"),Th("lg"),Th("xl"),Th("xxl")),
    ),
    Tbody(
        Tr(Td("Base"),Td("100%"),Td("106.25%"),Td("112.5%"),Td("118.75%"),Td("125%"),Td("131.25%")),
        Tr(Td(Code("<h1>")   ),Td("x 2rem"),Td("x 2rem"),Td("x 2rem"),Td("x 2rem"),Td("x 2rem"),Td("x 2rem")),
        Tr(Td(Code("<h2>")   ),Td("x 1.75rem"),Td("x 1.75rem"),Td("x 1.75rem"),Td("x 1.75rem"),Td("x 1.75rem"),Td("x 1.75rem")),
        Tr(Td(Code("<h3>")   ),Td("x 1.5rem"),Td("x 1.5rem"),Td("x 1.5rem"),Td("x 1.5rem"),Td("x 1.5rem"),Td("x 1.5rem")),
        Tr(Td(Code("<h4>")   ),Td("x 1.25rem"),Td("x 1.25rem"),Td("x 1.25rem"),Td("x 1.25rem"),Td("x 1.25rem"),Td("x 1.25rem")),
        Tr(Td(Code("<h5>")   ),Td("x 1.125rem"),Td("x 1.125rem"),Td("x 1.125rem"),Td("x 1.125rem"),Td("x 1.125rem"),Td("x 1.125rem")),
        Tr(Td(Code("<h6>")   ),Td("x 1rem"),Td("x 1rem"),Td("x 1rem"),Td("x 1rem"),Td("x 1rem"),Td("x 1rem")),
        Tr(Td(Code("<small>")),Td("x 0.875em"),Td("x 0.875em"),Td("x 0.875em"),Td("x 0.875em"),Td("x 0.875em"),Td("x 0.875em")),
    ),
    cls="overflow-auto",
)

body_4_1_1b = (
    P("To ensure that the user’s default font size is followed, the base font size is defined as a percentage that grows with the user’s screen size, while HTML elements are defined in ", Code("rem"), "."), 
    P("Since ", Code("rem"), " is a multiplier of the HTML document font size, all HTML element’s font sizes grow proportionally with the size of the user’s screen.")
    )

sec_4_1_1 = section(
    body_4_1_1a,
    table_4_1_1a,
    body_4_1_1b,
    table_4_1_1b,
    lv=4, title="Font sizes",
)

#——————————————————
art_4_1_2 = article(
    H1("Heading 1"),
    H2("Heading 2"),
    H3("Heading 3"),
    H4("Heading 4"),
    H5("Heading 5"),
    H6("Heading 6"),)
    
pico_4_1_2 = div_code(
code="""<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>""",
lang="html"),

sec_4_1_2 = section(
    art_4_1_2,
    pico_4_1_2,
    lv=4, title="Headings",
)

#——————————————————

sec_4_1_3 = section(
    P("Not implemented in FastHTML (as of 2024.06.24)."),
    P("I've done a basic rendering (in CSS) of the ", Code("<hgroup>"), " demo on the Pico CSS website to style this page's ", Code("<h3>"), " titles."),

    lv=4, title="Heading group",
)

#——————————————————
body_4_1_4 = Div(
    Div(P("Abbr.", Code("<abbr>", cls="highlight language-html")),
    P("Bold", Code("<strong>", cls="highlight language-html"), Code("<b>", cls="highlight language-html")),
    P("Italic", Code("<i>", cls="highlight language-html"), Code("<em>", cls="highlight language-html"), Code("<cite>", cls="highlight language-html")),
    P("Deleted", Code("<del>", cls="highlight language-html")),
    P("Inserted", Code("<ins>", cls="highlight language-html")),
    P("Ctrl + S", Code("<kbd>", cls="highlight language-html")),
    ),
    Div(P("Highlighted", Code("<mark>", cls="highlight language-html")),
    P("Strikethrough", Code("<s>", cls="highlight language-html")),
    P("Small", Code("<small>", cls="highlight language-html")),
    P("Text Sub", Code("<sub>", cls="highlight language-html")),
    P("Text Sup", Code("<sup>", cls="highlight language-html")),
    P("Underline", Code("<u>", cls="highlight language-html")),
    ),
    cls="grid",
)

sec_4_1_4 = section(
    P("Some of these are not implemented in FastHTML (as of 2024.06.24)."),
    body_4_1_4,
    lv=4, title="Inline text elements",
)
#——————————————————
sec_4_1_5 = section(
    P("Not implemented in FastHTML (as of 2024.06.24)."),
    lv=4, title="Blockquote",
)
#——————————————————
art_4_1_6 = article(
    P("Paragraph above the horizontal line."),
    Hr(),
    P("Paragraph below the horizontal line."),
)
pico_4_1_6 = div_code(
    code="""<p>Paragraph above the horizontal line.</p>
<hr />
<p>Paragraph below the horizontal line.</p>""",
    lang="html",
)
sec_4_1_6 = section(
    art_4_1_6,
    pico_4_1_6,
    lv=4, title="Horizontal rule",
)

#——————————————————
sec_4_1_0 = section(
    sec_4_1_1,
    sec_4_1_2,
    sec_4_1_3,
    sec_4_1_4,
    sec_4_1_5,
    sec_4_1_6,
    lv=3, title="Typography",
    desc="All typographic elements are responsive and scale gracefully across devices and viewports.",
)

#—————————————————————————————————— 4.2
# 4.2 Link


art_4_2_0a = article(
    A("Primary"),
    Br(),
    A("Secondary", cls="secondary"),
    Br(),
    A("Contrast", cls="contrast"),
)

pico_4_2_0a = div_code(
    code="""<a href="#">Primary</a>
<a href="#" class="secondary">Secondary</a>
<a href="#" class="contrast">Contrast</a>""",
    lang="html",
)

body_4_2_0a = (
    P(
        Code(".secondary"), 
        " and ", 
        Code(".contrast"), 
        " classes are not available in the class‑less version."
    ), 
    P(
        Code("aria-current"), 
        " send the active state to assistive technologies and is displayed as the hover links."
    ),
)


art_4_2_0b = article(
    A("Regular link"),
    Br(),
    A("Active link", aria_current="page"),
    Br(),
    A("Regular link"),
)

pico_4_2_0b = div_code(
    code="""<a href="#">Regular link</a>
<a href="#" aria-current="page">Active link</a>
<a href="#">Regular link</a>""",
    lang="html",
)



sec_4_2_0 = section(
    art_4_2_0a,
    pico_4_2_0a,
    body_4_2_0a,
    art_4_2_0b,
    pico_4_2_0b,
    lv=3, title="Link",
    desc=(
        "Links come with ",
        Code(".secondary"),
        " and ",
        Code(".contrast"),
        " styles."
    ),
)

#—————————————————————————————————— 4.3
# 4.3 Button
# 4.3.1 Syntax
# 4.3.2 Variants
# 4.3.3 Form buttons
# 4.3.4 Disabled
# 4.3.5 Role button
# 4.3.6 Usage with group

#——————————————————
art_4_3_1 = article(
    Button("Button"),
)

pico_4_3_1 = div_code(
    code="""<button>Button</button>""",
    lang="html",
)

sec_4_3_1 = section(
    art_4_3_1,
    pico_4_3_1,
    lv=4, title="Syntax",
)

#——————————————————
body_4_3_2a = P("Buttons come with ", Code(".secondary"), " and ", Code(".contrast"), "styles (not available in the ", A("class-less version", href="https://picocss.com/docs/classless"), ")."),

art_4_3_2a = article(Div(
    Button("Secondary", cls="secondary"),
    Button("Contrast", cls="contrast"),
    cls="grid",
    )
)

pico_4_3_2 = div_code(
    code="""<button class="secondary">Button</button>
<button class="contrast">Button</button>""",
    lang="html",
)

body_4_3_2b = P("They also come with a classic outline style (not available in the ", A("class-less version", href="https://picocss.com/docs/classless"), ").")

art_4_3_2b = article(Div(
    Button("Primary", cls="outline"),
    Button("Secondary", cls="outline secondary"),
    Button("Contrast", cls="outline contrast"),
    cls="grid",
))

pico_4_3_2b = div_code(
    code="""<button class="outline">Primary</button>
<button class="outline secondary">Secondary</button>
<button class="outline contrast">Contrast</button>""",
    lang="html",
)

sec_4_3_2 = section(
    body_4_3_2a,
    art_4_3_2a,
    pico_4_3_2,
    body_4_3_2b,
    art_4_3_2b,
    pico_4_3_2b,
    lv=4, title="Variants",
)

#——————————————————

body_4_3_3a = P(
    Code('type="submit"'), 
    " and ", 
    Code('type="button"'), 
    " inputs are also displayed as buttons. All form buttons are ", 
    Code('width: 100%;'), 
    " by default, to match with the other form elements."
)

art_4_3_3a = article(
    Input(type="submit"),
    Input(type="button", value="Input"),
)

pico_4_3_3a = div_code(
    code="""<input type="submit" />
<input type="button" value="Input" />""",
    lang="html",
)

body_4_3_3b = P("Reset inputs have the secondary style by default.")

art_4_3_3b = article(
    Input(type="reset"),
)

pico_4_3_3b = div_code(
    code="""<input type="reset" />""",
    lang="html",
)

sec_4_3_3 = section(
    body_4_3_3a,
    art_4_3_3a,
    pico_4_3_3a,
    body_4_3_3b,
    art_4_3_3b,
    pico_4_3_3b,
    lv=4, title="Form buttons",
)

#——————————————————

body_4_3_4 = (
    P("Not implemented in FastHTML (as of 2024.06.24)."),
    P("Buttons come with a disabled style."),
    )

art_4_3_4 = article(
    Button("Button", disabled=True),
)

pico_4_3_4 = div_code(
    code="""<button disabled>Button</button>""",
    lang="html",
)

sec_4_3_4 = section(
    body_4_3_4,
    art_4_3_4,
    pico_4_3_4,
    lv=4, title="Disabled",
)

#——————————————————

body_4_3_5 = P("Clickable elements with ", 
               Code("role='button'"), 
               " are rendered as buttons.")

art_4_3_5 = article(
    Div("Div as a button", role="button", tabindex="0"),
)

pico_4_3_5 = div_code(
    code="""<div role="button" tabindex="0">Div as a button</div>""",
    lang="html",
)

sec_4_3_5 = section(
    body_4_3_5,
    art_4_3_5,
    pico_4_3_5,
    lv=4, title="Role button",
)

#——————————————————

body_4_3_6 = P("You can use ", Code("role='group'"), " with buttons. See Group.")

art_4_3_6 = article(
    Div(
        Button("Button"),
        Button("Button"),
        Button("Button"),
        role="group",
    )
)

pico_4_3_6 = div_code(
    code="""<div role="group">
  <button>Button</button>
  <button>Button</button>
  <button>Button</button>
</div>""",
    lang="html",
)

sec_4_3_6 = section(
    body_4_3_6,
    art_4_3_6,
    pico_4_3_6,
    lv=4, title="Usage with group",
)

#——————————————————
sec_4_3_0 = section(
    sec_4_3_1,
    sec_4_3_2,
    sec_4_3_3,
    sec_4_3_4,
    sec_4_3_5,
    sec_4_3_6,
    lv=3, title="Button",
    desc=(
        "Buttons are using the native ",
        Code("<button>", cls="highlight"),
        " tag, without ",
        Code(".classes"),
        ". for the default style."),
)

#—————————————————————————————————— 4.4
# 4.4 Table
# 4.4.1 Syntax
# 4.4.2 Color schemes
# 4.4.3 Striped

table_4_4_1 = Table(
    Thead(
        Tr(
            Th("Planet"),
            Th("Diameter (km)"),
            Th("Distance to Sun (AU)"),
            Th("Orbit (days)"),
        )
    ),
    Tbody(
        Tr(
            Td("Mercury"),
            Td("4,880"),
            Td("0.39"),
            Td("88"),
        ),
        Tr(
            Td("Venus"),
            Td("12,104"),
            Td("0.72"),
            Td("225"),
        ),
        Tr(
            Td("Earth"),
            Td("12,742"),
            Td("1.00"),
            Td("365"),
        ),
        Tr(
            Td("Mars"),
            Td("6,779"),
            Td("1.52"),
            Td("687"),
        ),
        Tfoot(
            Td("Average"),
            Td("9,126"),
            Td("0.91"),
            Td("341"),
        ),
    )
)

pico_4_4_1 = div_code(
    code="""<table>
  <thead>
    <tr>
      <th scope="col">Planet</th>
      <th scope="col">Diameter (km)</th>
      <th scope="col">Distance to Sun (AU)</th>
      <th scope="col">Orbit (days)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Mercury</th>
      <td>4,880</td>
      <td>0.39</td>
      <td>88</td>
    </tr>
    <tr>
      <th scope="row">Venus</th>
      <td>12,104</td>
      <td>0.72</td>
      <td>225</td>
    </tr>
    <tr>
      <th scope="row">Earth</th>
      <td>12,742</td>
      <td>1.00</td>
      <td>365</td>
    </tr>
    <tr>
      <th scope="row">Mars</th>
      <td>6,779</td>
      <td>1.52</td>
      <td>687</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Average</th>
      <td>9,126</td>
      <td>0.91</td>
      <td>341</td>
    </tr>
  </tfoot>
</table>""",
    lang="html",
)


sec_4_4_1 = section(
    table_4_4_1,
    pico_4_4_1,
    lv=3, title="Table",
    desc=(
        "Clean and minimal styles for ",
        Code("<table>", cls="highlight"),
        ", providing consistent spacings and a minimal unbordered look."),
)

#——————————————————
body_4_4_2 = P(
    Code("data-theme='light'", cls="highlight"),
    " or ",
    Code("data-theme='dark'", cls="highlight"),
    " can be used at any level: ",
    Code("<table>", cls="highlight"),
    ", ",
    Code("<thead>", cls="highlight"),
    ", ",
    Code("<tbody>", cls="highlight"),
    ", ",
    Code("<tfoot>", cls="highlight"),
    ", ",
    Code("<tr>", cls="highlight"),
    ", ",
    Code("<th>", cls="highlight"),
    ", ",
    Code("<td>", cls="highlight"),
    ".",
)

table_4_4_2 = Table(
    Thead(
        Tr(
            Th("Planet"),
            Th("Diameter (km)"),
            Th("Distance to Sun (AU)"),
            Th("Orbit (days)"),
        ),
        data_theme="light",
    ),
    Tbody(
        Tr(
            Td("Mercury"),
            Td("4,880"),
            Td("0.39"),
            Td("88"),
        ),
        Tr(
            Td("Venus"),
            Td("12,104"),
            Td("0.72"),
            Td("225"),
        ),
        Tr(
            Td("Earth"),
            Td("12,742"),
            Td("1.00"),
            Td("365"),
        ),
        Tr(
            Td("Mars"),
            Td("6,779"),
            Td("1.52"),
            Td("687"),
        ),
        Tfoot(
            Td("Average"),
            Td("9,126"),
            Td("0.91"),
            Td("341"),
        ),
    )
)

pico_4_4_2 = div_code(
    code="""<table>
  <thead data-theme="light">
    ...
  </thead>
  <tbody>...</tbody>
  <tfoot>...</tfoot>
</table>""",
    lang="html",
)

sec_4_4_2 = section(
    body_4_4_2,
    table_4_4_2,
    pico_4_4_2,
    lv=4, title="Color schemes",
)


#——————————————————

body_4_4_3 = P(
    Code(".striped"),
    " enable striped rows (not available in the class‑less version).",
)

table_4_4_3 = Table(
    Thead(
        Tr(
            Th("Planet"),
            Th("Diameter (km)"),
            Th("Distance to Sun (AU)"),
            Th("Orbit (days)"),
        ),
    ),
    Tbody(
        Tr(
            Td("Mercury"),
            Td("4,880"),
            Td("0.39"),
            Td("88"),
        ),
        Tr(
            Td("Venus"),
            Td("12,104"),
            Td("0.72"),
            Td("225"),
        ),
        Tr(
            Td("Earth"),
            Td("12,742"),
            Td("1.00"),
            Td("365"),
        ),
        Tr(
            Td("Mars"),
            Td("6,779"),
            Td("1.52"),
            Td("687"),
        ),
        Tfoot(
            Td("Average"),
            Td("9,126"),
            Td("0.91"),
            Td("341"),
        ),
    ),
    cls="striped",
)

pico_4_4_3 = div_code(
    code="""<table class="striped">
  ...
</table>""",
    lang="html",
)



sec_4_4_3 = section(
    body_4_4_3,
    table_4_4_3,
    pico_4_4_3,
    lv=4, title="Striped",
)


#——————————————————
sec_4_4_0 = section(
    sec_4_4_1,
    sec_4_4_2,
    sec_4_4_3,
    lv=2, title="Table",
)

#——————————————————
sec_4_0_0 = section(
    sec_4_1_0,
    sec_4_2_0,
    sec_4_3_0,
    sec_4_4_0,
    lv=2, title="Content",
)
#————————————————————————————————————————————————————————————————————————————5
# 5. Forms
# 5.1 Overview
# 5.2 Input
# 5.3 Textarea
# 5.4 Select
# 5.5 Checkboxes
# 5.6 Radios
# 5.7 Switch
# 5.8 Range

#—————————————————————————————————— 5.1
# 5.1 Overview
# 5.1.1 Introduction
# 5.1.2 Helper text
# 5.1.3 Usage with grid
# 5.1.4 Usage with group

body_5_1_1a = P(
    "Inputs are ",
    Code("width: 100%;", cls="highlight"),
    " by default and are the same size as the buttons to build consistent forms."
)

art_5_1_1a = article(
    Form(Fieldset(
        Label(
            "First name", 
            Input(name="first_name", placeholder="First name", autocomplete="given-name"),
        ),
        Label("Email", For="email"),
            Input(type="email", id="email", placeholder="Email", autocomplete="email"),
        ),
    ),
    Input(type="submit", value="Subscribe"),
)
   

pico_5_1_1a = div_code(
    code="""<form>
  <fieldset>
    <label>
      First name
      <input
        name="first_name"
        placeholder="First name"
        autocomplete="given-name"
      />
    </label>
    <label>
      Email
      <input
        type="email"
        name="email"
        placeholder="Email"
        autocomplete="email"
      />
    </label>
  </fieldset>

  <input
    type="submit"
    value="Subscribe"
  />
</form>""",
    lang="html",
)

body_5_1_1b = P(
    Code("<input>", cls="highlight"),
    " can be inside or outside ",
    Code("<label>", cls="highlight"),
    "."
)

art_5_1_1b = article(
    Form(
        Label("First name", Input(name="first_name", placeholder="First name", autocomplete="given-name")),
        Label("Email", For="email"),
        Input(name="email", placeholder="Email", autocomplete="email"),
    ),
)

pico_5_1_1b = div_code(
    code="""<form>
  
  <!-- Input inside label -->
  <label>
    First name
    <input
      name="first_name"
      placeholder="First name"
      autocomplete="given-name"
    />
  </label>

  <!-- Input outside label -->
  <label for="email">Email</label>
  <input
    type="email"
    id="email"
    placeholder="Email"
    autocomplete="email"
  />

</form>""",
    lang="html",
)

sec_5_1_1 = section(
    body_5_1_1a,
    art_5_1_1a,
    pico_5_1_1a,
    body_5_1_1b,
    art_5_1_1b,
    pico_5_1_1b,
    lv=3, title="Introduction",
)
#——————————————————
body_5_1_2 = P(
    Code("<small>", cls="highlight"),
    " below form elements are muted and act as helper texts.",
)

art_5_1_2 = article(
    Input(type="email", name="email", placeholder="Email", autoComplete="email", aria_label="Email", aria_describedby="email-helper"),
    Small("We'll never share your email with anyone else.", id="email-helper"),
)

pico_5_1_2 = div_code(
    code="""<input
  type="email"
  name="email"
  placeholder="Email"
  autoComplete="email"
  aria-label="Email"
  aria-describedby="email-helper"
/>
<small id="email-helper">
  We'll never share your email with anyone else.
</small>""",
    lang="html",
)

sec_5_1_2 = section(
    body_5_1_2,
    art_5_1_2,
    pico_5_1_2,
    lv=3, title="Helper text",
)
#——————————————————
body_5_1_3 = P(
    "You can use ",
    Code(".grid"),
    " inside a form. See ",
    A("Grid", href="https://picocss.com/docs/grid"),
    ".",
)

art_5_1_3 = article(
    Form(
        Fieldset(
            Input(name="login", placeholder="Login", aria_label="Login", autocomplete="username"),
            Input(type="password", name="password", placeholder="Password", aria_label="Password", autocomplete="current-password"),
            Input(type="submit", value="Log in"),
            cls="grid"
        ),
    ),
)

pico_5_1_3 = div_code(
    code="""<form>
  <fieldset class="grid">
    <input 
      name="login"
      placeholder="Login"
      aria-label="Login"
      autocomplete="username"
    />
    <input
      type="password"
      name="password"
      placeholder="Password"
      aria-label="Password"
      autocomplete="current-password"
    />
    <input
      type="submit"
      value="Log in"
    />
  </fieldset>
</form>""",
    lang="html",
)

sec_5_1_3 = section(
    body_5_1_3,
    art_5_1_3,
    pico_5_1_3,
    lv=3, title="Usage with grid",
)
#——————————————————
body_5_1_4 = P(
    "You can use ",
    Code('role="group"'),
    " inside a form. See ",
    A("Group", href="https://picocss.com/docs/group"),
    ".",
)

art_5_1_4 = article(
    Form(
        Fieldset(
            Input(type="email", name="email", placeholder="Enter your email", autocomplete="email"),
            Input(type="submit", value="Subscribe"),
            role="group"
        ),
    ),
)

pico_5_1_4 = div_code(
    code="""<form>
  <fieldset role="group">
    <input
      type="email"
      name="email"
      placeholder="Enter your email"
      autocomplete="email"
    />
    <input type="submit" value="Subscribe" />
  </fieldset>
</form>""",
    lang="html",
)

sec_5_1_4 = section(
    body_5_1_4,
    art_5_1_4,
    pico_5_1_4,
    lv=3, title="Usage with group",
)
#——————————————————
sec_5_1_0 = section(
    sec_5_1_1,
    sec_5_1_2,
    sec_5_1_3,
    sec_5_1_4,
    lv=3, title="Overview",
    desc="All form elements are fully responsive with pure semantic HTML, enabling forms to scale gracefully across devices and viewports."
)

#—————————————————————————————————— 5.2
# 5.2 Input
# 5.2.1 Syntax
# 5.2.2 Datetime
# 5.2.3 Search
# 5.2.4 Color
# 5.2.5 File
# 5.2.6 Disabled
# 5.2.7 Readonly
# 5.2.8 Validation states

art_5_2_1 = article(
    Input(type="text", name="text", placeholder="Text", aria_label="Text"),
    Input(type="email", name="email", placeholder="Email", aria_label="Email", autocomplete="email"),
    Input(type="number", name="number", placeholder="Number", aria_label="Number"),
    Input(type="password", name="password", placeholder="Password", aria_label="Password"),
    Input(type="tel", name="tel", placeholder="Tel", aria_label="Tel", autocomplete="tel"),
    Input(type="url", name="url", placeholder="Url", aria_label="Url"),
)

pico_5_2_1 = div_code(
    code="""<input type="text" name="text" placeholder="Text" aria-label="Text" />
<input type="email" name="email" placeholder="Email" aria-label="Email" autocomplete="email" />
<input type="number" name="number" placeholder="Number" aria-label="Number" />
<input type="password" name="password" placeholder="Password" aria-label="Password" />
<input type="tel" name="tel" placeholder="Tel" aria-label="Tel" autocomplete="tel" />
<input type="url" name="url" placeholder="Url" aria-label="Url" />""",
    lang="html",
)

sec_5_2_1 = section(
    art_5_2_1,
    pico_5_2_1,
    lv=3, title="Syntax",
)

#——————————————————
body_5_2_2 = P("Datetime inputs come with an icon.")

art_5_2_2 = article(
    Input(type="date", name="date", aria_label="Date"),
    Input(type="datetime-local", name="datetime-local", aria_label="Datetime local"),
    Input(type="month", name="month", aria_label="Month"),
    Input(type="time", name="time", aria_label="Time"),
)

pico_5_2_2 = div_code(
    code="""<input type="date" name="date" aria-label="Date" />
<input type="datetime-local" name="datetime-local" aria-label="Datetime local" />
<input type="month" name="month" aria-label="Month" />
<input type="time" name="time" aria-label="Time" />""",
    lang="html",
)

sec_5_2_2 = section(
    body_5_2_2,
    art_5_2_2,
    pico_5_2_2,
    lv=3, title="Datetime",
)


body_5_2_3 = P(
    Code('type="search"'),
    " comes with a distinctive style.")

art_5_2_3 = article(
    Input(type="search", name="search", aria_label="Search"),
)

pico_5_2_3 = div_code(
    code="""<input type="search" name="search" placeholder="Search" aria-label="Search" />""",
    lang="html",
)

sec_5_2_3 = section(
    body_5_2_3,
    art_5_2_3,
    pico_5_2_3,
    lv=3, title="Search",
)
#——————————————————
body_5_2_4 = P(
    Code('type="color"'),
    " is also consistent with the other input types.",
)

art_5_2_4 = article(
    Input(type="color", value="#ff9500", aria_label="Color picker"),
)

pico_5_2_4 = div_code(
    code="""<input
  type="color"
  value="#ff9500"
  aria-label="Color picker"
/>""",
    lang="html",
)

sec_5_2_4 = section(
    body_5_2_4,
    art_5_2_4,
    pico_5_2_4,
    lv=3, title="Color",
)
#——————————————————
body_5_2_5 = P("Input type file button has a ", Code("secondary button style"), ".")

art_5_2_5 = article(
    Input(type="file"),
)

pico_5_2_5 = div_code(
    code="""<input type="file" />""",
    lang="html",
)

sec_5_2_5 = section(
    body_5_2_5,
    art_5_2_5,
    pico_5_2_5,
    lv=3, title="File",
)
#——————————————————
art_5_2_6 = article(
    Input(type="text", 
          name="text",
          placeholder="Disabled",
          aria_label="Disabled input", 
          disabled=True,),
)

pico_5_2_6 = div_code(
    code="""<input
  type="text"
  name="text"
  placeholder="Disabled"
  aria-label="Disabled input"
  disabled
/>""",
    lang="html",
)

sec_5_2_6 = section(
    art_5_2_6,
    pico_5_2_6,
    lv=3, title="Disabled",
)
#——————————————————
art_5_2_7 = article(
    Input(type="text", name="text", value="Read-only", aria_label="Read-only input", readonly=True),
)

pico_5_2_7 = div_code(
    code="""<input
  type="text"
  name="text"
  value="Read-only"
  aria-label="Read-only input"
  readonly
/>""",
    lang="html",
)

sec_5_2_7 = section(
    art_5_2_7,
    pico_5_2_7,
    lv=3, title="Readonly",
)
#——————————————————
body_5_2_8a = P("Validation states are provided with ",Code("aria-invalid"), ".")

art_5_2_8a = article(
    Input(type="text", name="valid", value="Valid", aria_invalid="false"),
    Input(type="text", name="invalid", value="Invalid", aria_invalid="true"),
)

pico_5_2_8a = div_code(
    code="""<input
  type="text"
  name="valid"
  value="Valid"
  aria-invalid="false"
/>

<input
  type="text"
  name="invalid"
  value="Invalid"
  aria-invalid="true"
/>""",
    lang="html",
)

body_5_2_8b = P("Helper texts, defined with ", Code("<small>"), ", below the form element, inherit the validation state color.")

art_5_2_8b = article(
    Input(type="text", name="valid", value="Valid", aria_invalid="false", aria_describedby="valid-helper"),
    Small("Looks good!"),
    Input(type="text", name="invalid", value="Invalid", aria_invalid="true", aria_describedby="invalid-helper"),
    Small("Please provide a valid value!"),
)

pico_5_2_8b = div_code(
    code="""<input
  type="text"
  name="valid"
  value="Valid"
  aria-invalid="false"
  aria-describedby="valid-helper"
/>
<small id="valid-helper">Looks good!</small>

<input
  type="text"
  name="invalid"
  value="Invalid"
  aria-invalid="true"
  aria-describedby="invalid-helper"
/>
<small id="invalid-helper">
  Please provide a valid value!
</small>""",
    lang="html",
)

sec_5_2_8 = section(
    body_5_2_8a,
    art_5_2_8a,
    pico_5_2_8a,
    body_5_2_8b,
    art_5_2_8b,
    pico_5_2_8b,
    lv=3, title="Validation states",
)
#——————————————————
sec_5_2_0 = section(
    sec_5_2_1,
    sec_5_2_2,
    sec_5_2_3,
    sec_5_2_4,
    sec_5_2_5,
    sec_5_2_6,
    sec_5_2_7,
    sec_5_2_8,
    lv=3, title="Input",
    desc="All input types are consistently styled and come with validation states."
)

#—————————————————————————————————— 5.3
# 5.3 Textarea
# 5.3.1 Syntax
# 5.3.2 Disabled
# 5.3.3 Readonly
# 5.3.4 Validation states
#——————————————————

art_5_3_1 = article(
    Textarea(name="bio", placeholder="Write a professional short bio...", aria_label="Professional short bio"),
)

pico_5_3_1 = div_code(
    code="""<textarea
  name="bio"
  placeholder="Write a professional short bio..."
  aria-label="Professional short bio"
>
</textarea>""",
    lang="html",
)

sec_5_3_1 = section(
    art_5_3_1,
    pico_5_3_1,
    lv=3, title="Syntax",
)
#——————————————————

art_5_3_2 = article(
    Textarea("Disabled", name="disabled", disabled=True),
)

pico_5_3_2 = div_code(
    code="""<textarea name="disabled" disabled>
  Disabled
</textarea>""",
    lang="html",
)

sec_5_3_2 = section(
    art_5_3_2,
    pico_5_3_2,
    lv=3, title="Disabled",
)
#——————————————————

art_5_3_3 = article(
    Textarea("Read-only", name="readonly", readonly=True),
)

pico_5_3_3 = div_code(
    code="""<textarea name="readonly" readonly>
  Read-only
</textarea>""",
    lang="html",
)

sec_5_3_3 = section(
    art_5_3_3,
    pico_5_3_3,
    lv=3, title="Readonly",
)
#——————————————————

body_5_3_4a = P("Validation states are provided with ", Code("aria-invalid"), ".")

art_5_3_4a = article(
    Textarea("Valid", name="valid", aria_invalid="false", aria_describedby="valid-helper"),
    Small("Looks good!"),
)

pico_5_3_4a = div_code(
    code="""<textarea name="valid" aria-invalid="false">
  Valid
</textarea>

<textarea name="invalid" aria-invalid="true">
  Invalid
</textarea> """,
    lang="html",
)

body_5_3_4b = P("Helper texts, defined with ", Code("<small>"), ", below the form element, inherit the validation state color.")

art_5_3_4b = article(
    Textarea("Valid", name="valid", aria_invalid="false", aria_describedby="valid-helper"),
    Small("Looks good!"),
    Textarea("Invalid", name="invalid", aria_invalid="true", aria_describedby="invalid-helper"),
    Small("Please provide a valid value!"),
)

pico_5_3_4b = div_code(
    code="""<textarea
  name="valid"
  aria-invalid="false"
  aria-describedby="valid-helper"
>
  Valid
</textarea>
<small id="valid-helper">Looks good!</small>

<textarea
  name="invalid"
  aria-invalid="true"
  aria-describedby="invalid-helper"
>
  Invalid
</textarea>
<small id="invalid-helper">
  Please provide a valid value!
</small>""",
    lang="html",
)

sec_5_3_4 = section(
    body_5_3_4a,
    art_5_3_4a,
    pico_5_3_4a,
    body_5_3_4b,
    art_5_3_4b,
    pico_5_3_4b,
    lv=3, title="Validation states",
)
#——————————————————
sec_5_3_0 = section(
    sec_5_3_1,
    sec_5_3_2,
    sec_5_3_3,
    sec_5_3_4,
    lv=3, title="Textarea",
    desc=(
        "The native ",
        Code("<textarea>", cls="highlight"),
        " is styled like the input for consistency."
    ),
)
#—————————————————————————————————— 5.4
# 5.4 Select
# 5.4.1 Syntax
# 5.4.2 Multiple
# 5.4.3 Disabled
# 5.4.4 Validation states
# 5.4.5 Dropdown
#———————————————————
art_5_4_1 = article(
    Select(
        "Select your favorite cuisine...", 
        Option("Select your favorite cuisine...", disabled=True, selected=True),
        Option("Italian"),
        Option("Japanese"),
        Option("Indian"),
        Option("Thai"),
        Option("French"),
        name="favorite-cuisine", 
        aria_label="Select your favorite cuisine...", 
        required=True,
    ),
)

pico_5_4_1 = div_code(
    code="""<select name="favorite-cuisine" aria-label="Select your favorite cuisine..." required>
  <option selected disabled value="">
    Select your favorite cuisine...
  </option>
  <option>Italian</option>
  <option>Japanese</option>
  <option>Indian</option>
  <option>Thai</option>
  <option>French</option>
</select>""",
    lang="html",
)

sec_5_4_1 = section(
    art_5_4_1,
    pico_5_4_1,
    lv=3, title="Syntax",
)
#——————————————————
art_5_4_2 = article(
    Select(
        "Select your favorite snacks...", 
        Option("Select your favorite snacks...", disabled=True),
        Option("Cheese"),
        Option("Fruits", selected=True),
        Option("Nuts", selected=True),
        Option("Chocolate"),
        Option("Crackers"),
        multiple=True, 
        size="6",
        aria_label="Select your favorite snacks...",
    ),
)

pico_5_4_2 = div_code(
    code="""<select aria-label="Select your favorite snacks..." multiple size="6">
  <option disabled>
    Select your favorite snacks...
  </option>
  <option>Cheese</option>
  <option selected>Fruits</option>
  <option selected>Nuts</option>
  <option>Chocolate</option>
  <option>Crackers</option>
</select>""",
    lang="html",
)

sec_5_4_2 = section(
    art_5_4_2,
    pico_5_4_2,
    lv=3, title="Multiple",
)
#——————————————————
art_5_4_3 = article(
    Select(
        Option("Select a meal type…"),
        Option("…"),
        name="meal-type", 
        aria_label="Select a meal type…",
        disabled=True,
    ),
)

pico_5_4_3 = div_code(
    code="""<select name="meal-type" aria-label="Select a meal type..." disabled>
  <option>Select a meal type...</option>
  <option>...</option>
</select>""",
    lang="html",
)

sec_5_4_3 = section(
    art_5_4_3,
    pico_5_4_3,
    lv=3, title="Disabled",
)
#——————————————————
body_5_4_4 = P("Validation states are provided with ", Code("aria-invalid"), ".")

art_5_4_4 = article(
    Select(
        Option("Select your favorite pizza topping…", selected=True, disabled=True),
        Option("Pepperoni"),
        Option("Mushrooms"),
        Option("Onions"),
        Option("Pineapple"),
        Option("Olives"),
        aria_invalid="false"
    ),
    Small("Great choice!"),
    Select(
        Option("Select your favorite pizza topping…", selected=True, disabled=True),
        Option("Pepperoni"),
        Option("Mushrooms"),
        Option("Onions"),
        Option("Pineapple"),
        Option("Olives"),        
        aria_invalid="true"
    ),
    Small("Please select your favorite pizza topping!"),
)

pico_5_4_4 = div_code(
    code="""<select aria-invalid="false">
  ...
</select>
<small>Great choice!</small>

<select required aria-invalid="true">
  ...
</select>
<small>
  Please select your favorite pizza topping!
</small>>""",
    lang="html",
)

sec_5_4_4 = section(
    body_5_4_4,
    art_5_4_4,
    pico_5_4_4,
    lv=3, title="Validation states",
)
#——————————————————
body_5_4_5 = P("The dropdown component allows you to build a custom select with the same style as the native select. See ", A("dropdown", href="https://picocss.com/docs/dropdown"), ".")

sec_5_4_5 = section(
    body_5_4_5,
    lv=3, title="Dropdown",
)
#———————————————————
sec_5_4_0 = section(
    sec_5_4_1,
    sec_5_4_2,
    sec_5_4_3,
    sec_5_4_4,
    sec_5_4_5,
    lv=3, title="Select",
    desc=(
        "The native ",
        Code("<select>", cls="highlight"),
        " is styled like the input for consistency."
    ),
)
#—————————————————————————————————— 5.5
# 5.5 Checkboxes
# 5.5.1 Syntax
# 5.5.2 Horizontal stacking
# 5.5.3 Indeterminate
# 5.5.4 Validation states
#———————————————————

art_5_5_1 = article(
    Fieldset(
        Legend("Language preferences:"),
        Label(Input("English",  type="checkbox", name="english", checked=True)),
        Label(Input("French",   type="checkbox", name="french", checked=True)),
        Label(Input("Mandarin", type="checkbox", name="mandarin")),
        Label(Input("Thai",     type="checkbox", name="thai")),
        Label(Input("Dothraki", type="checkbox", name="dothraki", disabled=True)),
    ),
)

pico_5_5_1 = div_code(
    code="""<fieldset>
  <legend>Language preferences:</legend>
  <label>
    <input type="checkbox" name="english" checked />
    English
  </label>
  <label>
    <input type="checkbox" name="french" checked />
    French
  </label>
  <label>
    <input type="checkbox" name="mandarin" />
    Mandarin
  </label>
  <label>
    <input type="checkbox" name="thai" />
    Thai
  </label>
  <label aria-disabled="true">
    <input type="checkbox" name="dothraki" disabled />
    Dothraki
  </label>
</fieldset>""",
    lang="html",
)

sec_5_5_1 = section(
    art_5_5_1,
    pico_5_5_1,
    lv=3, title="Syntax",
)
#———————————————————
art_5_5_2 = article(
    Fieldset(
        Legend("Language preferences:"),
        Input("Hindi", type="checkbox", id="hindi", name="hindi", checked=True),
        Label("Swahili", Input("Swahili", type="checkbox", id="swahili", name="swahili")),
        Label("Na'vi", Input("Na'vi", type="checkbox", id="navi", name="navi", disabled=True)),
    ),
)

pico_5_5_2 = div_code(
    code="""<fieldset>
  <legend>Language preferences:</legend>
  <input type="checkbox" id="hindi" name="hindi" checked />
  <label htmlFor="hindi">Hindi</label>
  <input type="checkbox" id="swahili" name="swahili" />
  <label htmlFor="swahili">Swahili</label>
  <input type="checkbox" id="navi" name="navi" disabled />
  <label htmlFor="navi" aria-disabled="true">Na'vi</label>
</fieldset>""",
    lang="html",
)

sec_5_5_2 = section(
    art_5_5_2,
    pico_5_5_2,
    lv=3, title="Horizontal stacking",
)
#———————————————————
body_5_5_3 = P("You can change a checkbox to an indeterminate state by setting the ", Code("indeterminate"), " property to ", Code("true"), ".")

art_5_5_3 = article(
    Label(Input(
        "Indeterminate", 
        type="checkbox", 
        id="indeterminate", 
        name="indeterminate"
    )),
)

script_5_5_3 = Script(
    """const checkbox = document.querySelector('#indeterminate');
    checkbox.indeterminate = true;"""
)

pico_5_5_3 = div_code(
    code="""<label>
  <input type="checkbox" id="indeterminate" name="indeterminate" />
  Indeterminate
</label>

<script>
  const checkbox = document.querySelector('#indeterminate');
  checkbox.indeterminate = true;
</script>
""",
    lang="html",
)

sec_5_5_3 = section(
    body_5_5_3,
    art_5_5_3,
    pico_5_5_3,
    script_5_5_3,
    lv=3, title="Indeterminate",
)
#———————————————————

body_5_5_4 = P("Validation states are provided with ", Code(".aria-invalid."), ".")

art_5_5_4 = article(
    Label(Input("Valid", type="checkbox", name="valid", aria_invalid="false")),
    Label(Input("Invalid", type="checkbox", name="invalid", aria_invalid="true")),
)

pico_5_5_4 = div_code(
    code="""<label>
  <input type="checkbox" name="valid" aria-invalid="false" />
  Valid
</label>

<label>
  <input type="checkbox" name="invalid" aria-invalid="true" />
  Invalid
</label>""",
    lang="html",
)

sec_5_5_4 = section(
    body_5_5_4,
    art_5_5_4,
    pico_5_5_4,
    lv=3, title="Validation states",
)
#———————————————————
sec_5_5_0 = section(
    sec_5_5_1,
    sec_5_5_2,
    sec_5_5_3,
    sec_5_5_4,
    lv=3, title="Checkboxes",
    desc=(
        "The native ",
        Code("<input type='checkbox'>", cls="highlight"),
        " with a custom and responsive style."
    ),
)
#—————————————————————————————————— 5.6
# 5.6 Radios
# 5.6.1 Syntax
# 5.6.2 Horizontal stacking
# 5.6.3 Validation states
#———————————————————
art_5_6_1 = article(
    Fieldset(
        Legend("Language preference:"),
        Label(Input("English", type="radio", name="language", checked=True)),
        Label(Input("French", type="radio", name="language")),
        Label(Input("Mandarin", type="radio", name="language")),
        Label(Input("Thai", type="radio", name="language")),
        Label(Input("Dothraki", type="radio", name="language", disabled=True)),
    ),
)

pico_5_6_1 = div_code(
    code="""<fieldset>
  <legend>Language preference:</legend>
  <label>
    <input type="radio" name="language" checked />
    English
  </label>
  <label>
    <input type="radio" name="language" />
    French
  </label>
  <label>
    <input type="radio" name="language" />
    Mandarin
  </label>
  <label>
    <input type="radio" name="language" />
    Thai
  </label>
  <label aria-disabled="true">
    <input type="radio" name="language" disabled />
    Dothraki
  </label>
</fieldset>""",
    lang="html",
)

sec_5_6_1 = section(
    art_5_6_1,
    pico_5_6_1,
    lv=3, title="Syntax",
)
#———————————————————
art_5_6_2 = article(
    Fieldset(
        Legend("Second language:"),
        Input("Hindi", type="radio", id="hindi", name="second-language", checked=True),
        Input("Swahili", type="radio", id="swahili", name="second-language"),
        Input("Na'vi", type="radio", id="navi", name="second-language", disabled=True),
    ),
)

pico_5_6_2 = div_code(
    code="""<fieldset>
  <legend>Second language:</legend>
  <input type="radio" id="hindi" name="second-language" checked />
  <label htmlFor="hindi">Hindi</label>
  <input type="radio" id="swahili" name="second-language" />
  <label htmlFor="swahili">Swahili</label>
  <input type="radio" id="navi" name="second-language" disabled />
  <label htmlFor="navi" aria-disabled="true">Na'vi</label>
</fieldset>""",
    lang="html",
)

sec_5_6_2 = section(
    art_5_6_2,
    pico_5_6_2,
    lv=3, title="Horizontal stacking",
)
#———————————————————
body_5_6_3 = P("Validation states are provided with ", Code(".aria-invalid."), ".")

art_5_6_3 = article(
    Label(Input(type="radio", name="valid", aria_invalid="false"), "Valid", ),
    Label(Input(type="radio", name="invalid", aria_invalid="true"), "Invalid", ),
)

pico_5_6_3 = div_code(
    code="""<label>
  <input type="radio" name="valid" aria-invalid="false" />
  Valid
</label>

<label>
  <input type="radio" name="invalid" aria-invalid="true" />
  Invalid
</label>""",
    lang="html",
)

sec_5_6_3 = section(
    body_5_6_3,
    art_5_6_3,
    pico_5_6_3,
    lv=3, title="Validation states",
)
#———————————————————
sec_5_6_0 = section(
    sec_5_6_1,
    sec_5_6_2,
    sec_5_6_3,
    lv=3, title="Radios",
    desc=(
        "The native ",
        Code("<input type='radio'>", cls="highlight"),
        " with a custom and responsive style."
    ),
)
#—————————————————————————————————— 5.7
# 5.7 Switch
# 5.7.1 Syntax
# 5.7.2 Disabled
# 5.7.3 Validation states
art_5_7_1 = article(
    Fieldset(
        Label(Input("I agree to the Terms", type="checkbox", name="terms", role="switch")),
        Label(Input("Receive news and offers", type="checkbox", name="opt-in", role="switch", checked=True)),
    ),
)

pico_5_7_1 = div_code(
    code="""<fieldset>
  <label>
    <input name="terms" type="checkbox" role="switch" />
    I agree to the Terms
  </label>
  <label>
    <input name="opt-in" type="checkbox" role="switch" checked />
    Receive news and offers
  </label>
</fieldset>""",
    lang="html",
)

sec_5_7_1 = section(
    art_5_7_1,
    pico_5_7_1,
    lv=3, title="Syntax",
)
#———————————————————
art_5_7_2 = article(
    Fieldset(
        Label(Input("Publish on my profile", type="checkbox", name="publish", role="switch", disabled=True)),
        Label(Input("Change my password at next login", type="checkbox", name="change-password", role="switch", checked=True, disabled=True))
    ),
)

pico_5_7_2 = div_code(
    code="""<fieldset>
  <label>
    <input name="publish" type="checkbox" role="switch" disabled />
    Publish on my profile
  </label>
  <label>
    <input name="change-password" type="checkbox" role="switch" checked disabled />
    Change my password at next login
  </label>
</fieldset>""",
    lang="html",
)

sec_5_7_2 = section(
    art_5_7_2,
    pico_5_7_2,
    lv=3, title="Disabled",
)


#———————————————————

art_5_7_3 = article(
    Fieldset(
        Label(Input("Enable two-factor authentication", type="checkbox", name="2fa", role="switch", aria_invalid="false")),
        Label(Input("Automatic subscription renewal", type="checkbox", name="subscription", role="switch", aria_invalid="true")),
    ),
)

pico_5_7_3 = div_code(
    code="""<fieldset>
  <label>
    <input name="2fa" type="checkbox" role="switch" aria-invalid="false" />
    Enable two-factor authentication
  </label>
  <label>
    <input name="subscription" type="checkbox" role="switch" aria-invalid="true" />
    Automatic subscription renewal
  </label>
</fieldset>""",
    lang="html",
)

sec_5_7_3 = section(
    art_5_7_3,
    pico_5_7_3,
    lv=3, title="Validation states",
)
#———————————————————
sec_5_7_0 = section(
    sec_5_7_1,
    sec_5_7_2,
    sec_5_7_3,
    lv=3, title="Switch",
    desc=(
        "A switch component in pure CSS, using the checkbox syntax."
    ),
)
#—————————————————————————————————— 5.8
# 5.8 Range
#———————————————————
art_5_8_1 = article(
    Label(Input("Brightness", type="range")),
    Label(Input("Contrast", type="range", value="40")),
)

pico_5_8_1 = div_code(
    code="""<label>
  Brightness
  <input type="range" />
</label>

<label>
  Contrast
  <input type="range" value="40" />
</label>""",
    lang="html",
)

sec_5_8_0 = section(
    art_5_8_1,
    pico_5_8_1,
    lv=3, title="Range",
    desc=(
        "Create a slider control with ",
        Code("<input type='range'>", cls="highlight"),
        "."
    ),
)
#——————————————————————————————————
sec_5_0_0 = section(
    sec_5_1_0,
    sec_5_2_0,
    sec_5_3_0,
    sec_5_4_0,
    sec_5_5_0,
    sec_5_6_0,
    sec_5_7_0,
    sec_5_8_0,
    lv=2, title="Forms",
)
#————————————————————————————————————————————————————————————————————————————6
# 6. Components
# 6.1 Accordion
# 6.2 Card
# 6.3 Dropdown
# 6.4 Group NEW
# 6.5 Loading
# 6.6 Modal
# 6.7 Nav
# 6.8 Progress
# 6.9 Tooltip

#—————————————————————————————————— 6.1
# 6.1 Accordions
# 6.1.1 Overview
# 6.1.2 Button variants

art_6_1_1 = article(
    Details(Summary("Accordion 1"), P("...")),
    Details(Summary("Accordion 2"), Ul(Li("..."), Li("..."))),
)

pico_6_1_1 = div_code(
    code="""<details open>
  <summary>Accordion 1</summary>
  <p>...</p>
</details>

<hr />

<details>
  <summary>Accordion 2</summary>
  <ul>
    <li>...</li>
    <li>...</li>
  </ul>
</details>""",
    lang="html",
)

sec_6_1_1 = section(
    lv=4, title="Overview",
)

#———————————————————
sec_6_1_0 = section(
    lv=3, title="Accordion",
    desc=(
        "Toggle sections of content in pure HTML, without JavaScript, using minimal and semantic markup."
    ),
)

#—————————————————————————————————— 6.2
# 6.2 Card
# 6.2.1 Syntax
# 6.2.2 Sectioning



#———————————————————
sec_6_2_0 = section(
    lv=3, title="Card",
    desc=(
        "Create flexible cards with a semantic markup that provides graceful spacings across various devices and viewports."
    ),
)

#—————————————————————————————————— 6.3
# 6.3 Dropdown
# 6.3.1 Syntax
# 6.3.2 Checkboxes and radios
# 6.3.3 Button variants
# 6.3.4 Validation states
# 6.3.5 Usage with nav




#———————————————————
sec_6_3_0 = section(
    lv=3, title="Dropdown",
    desc="Create dropdown menus and custom selects with minimal and semantic HTML, without JavaScript."
)

#—————————————————————————————————— 6.4
# 6.4 Group
# 6.4.1 Forms
# 6.4.2 Search
# 6.4.3 Buttons





#———————————————————
sec_6_4_0 = section(
    lv=3, title="Group",
    desc=(
        "Stack forms elements and buttons horizontally with ",
        Code("role='group'"),
        " and ",
        Code("role='search'"),
        "."
    ),
)

#—————————————————————————————————— 6.5
# 6.5 Loading




#———————————————————
sec_6_5_0 = section(
    lv=3, title="Loading",
    desc=(
        "Add a loading indicator with ",
        Code("aria-busy='true'"),
        "."
    ),
)

#—————————————————————————————————— 6.6
# 6.6 Modal
# 6.6.1 Syntax
# 6.6.2 Demo
# 6.6.3 Utilities





#———————————————————
sec_6_6_0 = section(
    lv=3, title="Modal",
    desc=(
        "The classic modal component with graceful spacings across devices and viewports, using the semantic HTML tag ",
        Code("<dialog>", cls="highlight"),
        "."
    ),
)

#—————————————————————————————————— 6.7
# 6.7 Nav
# 6.7.1 Syntax
# 6.7.2 Link variants
# 6.7.3 Buttons
# 6.7.4 Dropdowns
# 6.7.5 Vertical stacking
# 6.7.6 Breadcrumb
# 6.7.7 Overflow





#———————————————————
sec_6_7_0 = section(
    lv=3, title="Nav",
    desc="The essential navbar component in pure semantic HTML."
)

#—————————————————————————————————— 6.8
# 6.8 Progress
# 6.8.1 Syntax
# 6.8.2 Indeterminate




#———————————————————
sec_6_8_0 = section(
    lv=3, title="Progress",
    desc="The progress bar element in pure HTML, without JavaScript."
)

#—————————————————————————————————— 6.9
# 6.9 Tooltip
# 6.9.1 Syntax
# 6.9.2 Placement





#———————————————————
sec_6_9_0 = section(
    lv=3, title="Tooltip",
    desc="Enable tooltips everywhere, without JavaScript."
)
#———————————————————
sec_6_0_0 = section(
    sec_6_1_0,
    sec_6_2_0,
    sec_6_3_0,
    sec_6_4_0,
    sec_6_5_0,
    sec_6_6_0,
    sec_6_7_0,
    sec_6_8_0,
    sec_6_9_0,
    lv=2, title="Components",
)
#————————————————————————————————————————————————————————————————————————————7
# 7. About
# 7.1 What’s new in v2?
# 7.2 Mission
# 7.3 Usage scenarios
# 7.4 Brand
# 7.5 Built With

#—————————————————————————————————— 7.1

sec_7_1_0 = section(
    lv=3, title="What’s new in v2?",
    desc="Pico v2.0 features better accessibility, easier customization with SASS, a complete color palette, a new group component, and 20 precompiled color themes totaling over 100 combinations accessible via CDN."
)

#—————————————————————————————————— 7.2

sec_7_2_0 = section(
    lv=3, title="Mission",
    desc="Pico CSS is a minimalist and lightweight starter kit that prioritizes semantic syntax, making every HTML element responsive and elegant by default."
)

#—————————————————————————————————— 7.3

sec_7_3_0 = section(
    lv=3, title="Usage scenarios",
    desc="How does Pico fit into your project?"
)

#—————————————————————————————————— 7.4

sec_7_4_0 = section(
    lv=3, title="Brand",
    desc="Pico CSS brand assets and usage guidelines."
)

#—————————————————————————————————— 7.5

sec_7_5_0 = section(
    lv=3, title="Built With",
    desc="Relevant packages, tools, and resources we depend on."
)


sec_7_0_0 = section(
    sec_7_1_0,
    sec_7_2_0,
    sec_7_3_0,
    sec_7_4_0,
    sec_7_5_0,
    lv=2, title="About",
)
#—————————————————————————————————————————————————————————————————————————————
sections = (
    sec_1_0_0,
    sec_2_0_0,
    sec_3_0_0,
    sec_4_0_0,
    sec_5_0_0,
    sec_6_0_0,
    sec_7_0_0,
)
page = (title, html, main(sections))

# Home page
@rt("/")
def get():
    return page

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
