from fasthtml.common import * # type: ignore
import json

html    = Html(lang='en', 
    # data_theme='dark',   # also helps bg color hack in demo.css
    )
title = "FastHTML 🧡 Pico CSS"
footer_text = P("Made by kit using FastHTML & Pico CSS + PrismJS, June 2024.")

pico_css = Link(
    rel="stylesheet", 
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css", 
    type="text/css"
    )
prism_css = Link(
    rel="stylesheet", 
    href="style/prism.css",
    type="text/css"
    )
prism_css_theme = Link(     # linked at the bottom of the HTML file
    rel="stylesheet", 
    href="style/prism-one-dark.css",
    type="text/css"
    )
demo_css = Link(            # Override some Prism styles
    rel="stylesheet", 
    href="style/demo.css",
    type="text/css"
    )
prism_js = Script(src="style/prism.js")

# css_overrides = []
# css = Style(" ".join(o for o in css_overrides))
head = Meta(charset="utf-8"), Meta(name="viewport", 
    content="width=device-width, initial-scale=1"), Meta(
    name="color-scheme", content="light dark") 
#                PLAY WITH THIS 🔥☯️ 🡅🡅🡅 ☯️🔥
#                                   BUTTONS!
app = FastHTML(hdrs=(
    head,
    pico_css,
    prism_css,
    prism_css_theme,
    demo_css, 
    # css,         # use for in-file custom CSS; otherwise in demo.css
    ))
rt = app.route

# This line ensures that the static files are served from the static folder.
# (req. for favicon, CSS etc.)
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}') # type: ignore

# TODO: functionalize all of it
#       [x] Colors
#       [x] Sections
#       [ ] 
#       [ ] 

# Canonical HTML structure
menu = Div(P(A("Notes", href="/log")), P(A("Demos", href="/llm")), cls='grid')

# Our data
starter_html_template = NotStr("""&lt;!doctype html>
&lt;html lang="en">
  &lt;head>
    &lt;meta charset="utf-8">
    &lt;meta name="viewport" content="width=device-width, initial-scale=1">
    &lt;meta name="color-scheme" content="light dark" />
    &lt;link rel="stylesheet" href="css/pico.min.css">
    &lt;title>Hello world!&lt;/title>
  &lt;/head>
  &lt;body>
    &lt;main class="container">
      &lt;h1>Hello world!&lt;/h1>
    &lt;/main>
  &lt;/body>
&lt;/html>""")
# ↓
block_code = Pre(Code(starter_html_template, cls='language-html'), cls='prismjs')


colors = [
    'red','pink','fuchsia','purple','violet','indigo','blue','azure','cyan','jade',
    'green','lime','yellow','amber','pumpkin','orange','sand','grey','zinc','slate']
shades = [
    '550', '500', '550', '600', '600', '600', '550', '550', '550', '550', 
    '500', '200', '100', '200', '300', '500', '200', '300', '550', '600']
# ↓
def to_rgb(color, shade) -> str:
    '''Returns color shade from the Pico color palette as RGB string.
    '''
    with open('style/pico-color-palette.json', 'r') as file:
        color_data = json.load(file)
    return str(color_data[color][shade])

def make_div(color, shade):
    '''Returns a div with a color dot.
    '''
    return Div(Strong("●"), style='background: '+ to_rgb(color, shade), cls='color-pick')

def make_divs(colors=colors, shades=shades):
    '''Returns a tuple of divs with color dots.
    '''
    divs = tuple()
    for i in range(len(colors)):
        divs += (make_div(colors[i], shades[i]),)
    return divs

color_palette = Article(Header(
    make_divs(),
    cls='grid', 
    # style='background: #000;',
), cls='color-picker',
# style='background: #000;',
)

d1_2_0 = (color_palette, ) # should have an example card below, and divs buttons to switch color (whole page btw)

# sections dictionaries
# - key:str = name of the title
# - value:int = n in <hn> (n:int=1|2|3|4|5|6)
# - comment: numbering
section_1 = {
    "Getting started": 2,       # 1_0_0
    "Quick start": 3,           # 1_1_0      
    "Starter HTML template": 4, # 1_1_5
    "Version picker": 3,        # 1_2_0
    "Color schemes": 3,         # 1_3_0
    "Usage": 4,                 # 1_3_1
    "Card example": 4,          # 1_3_2
    "Class-less version": 3,    # 1_4_0
    "Conditional styling": 3,   # 1_5_0
    "RTL": 3,                   # 1_6_0
}

section_2 = {
    "Customization": 2,         # 2_0_0
    "CSS Variables": 3,         # 2_1_0
    "Sass": 3,                  # 2_2_0
    "Colors": 3,                # 2_3_0
}
section_3 = {
    "Layout": 2,                # 3_0_0
    "Container": 3,             # 3_1_0
    "Landmarks & section": 3,   # 3_2_0
    "Grid": 3,                  # 3_3_0
    "Overflow auto": 3,         # 3_4_0
}
section_4 = {
    "Content": 2,               # 4_0_0
    "Typography": 3,            # 4_1_0
    "Link": 3,                  # 4_2_0
    "Button": 3,                # 4_3_0
    "Table": 3,                 # 4_4_0
}
section_5 = {
    "Forms": 2,                 # 5_0_0
    "Overview": 3,              # 5_1_0
    "Input": 3,                 # 5_2_0
    "Textarea": 3,              # 5_3_0
    "Select": 3,                # 5_4_0
    "Checkboxes": 3,            # 5_5_0
    "Radios": 3,                # 5_6_0
    "Switch": 3,                # 5_7_0
    "Range": 3,                 # 5_8_0
}
section_6 = {
    "Components": 2,            # 6_0_0
    "Accordion": 3,             # 6_1_0
    "Card": 3,                  # 6_2_0
    "Dropdown": 3,              # 6_3_0
    "Group NEW": 3,             # 6_4_0
    "Loading": 3,               # 6_5_0
    "Modal": 3,                 # 6_6_0
    "Nav": 3,                   # 6_7_0
    "Progress": 3,              # 6_8_0
    "Tooltip": 3,               # 6_9_0
}
section_7 = {
    "About": 2,                 # 7_0_0
    "What’s new in v2?": 3,     # 7_1_0
    "Mission": 3,               # 7_2_0
    "Usage scenarios": 3,       # 7_3_0
    "Brand": 3,                 # 7_4_0
    "Built With": 3,            # 7_5_0
}


# NEW PLAN! 🔥😼🔥
# [ ] all code snippets are files in ./code/
# [ ] named by section number (4_2 becomes demo_4_2.py)
# [ ] Python imported as modules → feed to make_ fns (fastHTML funcs)
# [ ] independently, PrismJS will source .py, .html, .css for display/highlight



# All demos are indexed by section number
d1_1_5 = Div(block_code, cls='code', id='demo-1-1-5')



d1_3_2_1 = Article("…", data_theme="light"), Article("…", data_theme="dark")










# These functions assemble the page using all data above.
# Page is made of Sections
# Sections are made of blocks
# Blocks have a title, anchor link, and contents 🡄TODO
# Contents are made of HTML Tags i.e. FastHTML functions: tuple(Div(), P(), A()…)
# We implement the above in reverse order: contents → h block → section → page

def make_contents():
    return

def make_h(title:str, lv:int, *contents):
    '''Returns a headed block with title and anchor link.
    TODO: Implement *contents to add block contents.
    '''
    h = [H1, H2, H3, H4, H5, H6]
    hn = h[lv-1]
    formatted_title = title.lower().replace(' ', '-')
    return hn(title, A('🔗', href='#'+formatted_title, id=formatted_title, cls='secondary', tabindex="-1")), *contents

def make_section(section:dict):
    items = []
    for title, level in section.items():
        items.append(make_h(title, level))
    return Section(*items)

def make_page(*sections):
    all_sections = ()
    for section in sections:
        all_sections += (make_section(section),)
    return all_sections

sections = Div(make_page(
    section_1, section_2, section_3, section_4, section_5, 
    section_6, section_7), id="content", role="document",)



# 🡇🡇🡇 BEGIN TEST 🡇🡇🡇
test = make_h("Test", 2, color_palette, d1_1_5, d1_3_2_1)
# 🡅🡅🡅  END TEST  🡅🡅🡅


# transparency header
# we'll use cls="top_header"

# CSS
# body>header.is-fixed-above-lg {
#     z-index: 2;
#     position: sticky;
#     top: 0;
#     -webkit-backdrop-filter: blur(1rem);
#     backdrop-filter: blur(1rem);
#     background-color: var(--pico-header-background);

# HTML
# header cls="is-fixed-above-lg is-fixed" (we don't do the toggle thing)
#   div cls="container"
#     a home/logo
#     nav
#       ul's
#         li's
#

top_header = Header(
  Div(
    A(H1(title), href="/"), 
    Nav(
      Ul(
          Li(A("Light", href="/")),
          Li(A("Dark", href="/components")),
          Li(A("Code", href="/about")),
      ),
      Ul(
          Li(A("FastHTML", href="/")),
          Li(A("Pico CSS", href="/components")),
          Li(A("About", href="/about")),
      ), 
    ), 
    cls="container",  
  ), 
  cls="top_header",
)



scripts = Script(src="style/prism.js")

# header = Header(H1(title), menu, Hr(), cls='container') # TODO: make proper header with nav etc.
main   = Main(test, sections, cls='container line-numbers')
footer = Footer(Hr(), footer_text, cls='container')

website = (html, Title(title), top_header, main, footer, scripts)

# Home page
@rt("/")
def get():
    return website
