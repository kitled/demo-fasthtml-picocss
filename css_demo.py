from fasthtml.common import *
import json

website = "FastHTML 🧡 Pico CSS"
html    = Html(lang='en', 
    data_theme='dark',   # also helps bg color hack in demo.css
    )

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
head = Meta(charset="utf-8"), Meta(name="viewport", content="width=device-width, initial-scale=1"), Meta(name="color-scheme", content="light dark")

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
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

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
def to_rgb(color_name, shade):
    with open('style/pico-color-palette.json', 'r') as file:
        color_data = json.load(file)
    return str(color_data[color_name][shade])

def make_div(color, shade):
    return Div(Strong("●"), style='background:'+ to_rgb(color, shade)+';',)

def make_divs(colors=colors, shades=shades):
    divs = tuple()
    for i in range(len(colors)):
        divs += (make_div(colors[i], shades[i]),)
    return divs

color_palette = Article(Header(
    make_divs(),
    cls='grid', style='background: #000;',
), style='background: #000;',
)

# sections dictionaries
# - key:str = name of the title
# - value:int = n in <hn> (n:int=1|2|3|4|5|6)
section_1 = {
    "Getting started": 2,
    "Quick start": 3,
    "Starter HTML template": 4,
    "Version picker": 3,
    "Color schemes": 3,
    "Class-less version": 3,
    "Conditional styling": 3,
    "RTL": 3,
}

section_2 = {
    "Customization": 2,
    "CSS Variables": 3,
    "Sass": 3,
    "Colors": 3,
}
section_3 = {
    "Layout": 2,
    "Container": 3,
    "Landmarks & section": 3,
    "Grid": 3,
    "Overflow auto": 3,
}
section_4 = {
    "Content": 2,
    "Typography": 3,
    "Link": 3,
    "Button": 3,
    "Table": 3,
}
section_5 = {
    "Forms": 2,
    "Overview": 3,
    "Input": 3,
    "Textarea": 3,
    "Select": 3,
    "Checkboxes": 3,
    "Radios": 3,
    "Switch": 3,
    "Range": 3,
}
section_6 = {
    "Components": 2,
    "Accordion": 3,
    "Card": 3,
    "Dropdown": 3,
    "Group NEW": 3,
    "Loading": 3,
    "Modal": 3,
    "Nav": 3,
    "Progress": 3,
    "Tooltip": 3,
}
section_7 = {
    "About": 2,
    "What’s new in v2?": 3,
    "Mission": 3,
    "Usage scenarios": 3,
    "Brand": 3,
    "Built With": 3,
}









































# These functions assemble the page using all data above.
def make_h(title:str='title', lv:int=3):
    h = [H1, H2, H3, H4, H5, H6]
    hn = h[lv-1]
    formatted_title = title.lower().replace(' ', '-')
    return hn(title, A('🔗', href='#'+formatted_title, id=formatted_title, cls='secondary', tabindex="-1"))

def make_section(section:dict):
    items = []
    for title, level in section.items():
        items.append(make_h(title, level))
    return Section(*items)

def make_sections(*sections):
    all_sections = ()
    for section in sections:
        all_sections += (make_section(section),)
    return all_sections

sections = Div(make_sections(section_1, section_2, section_3, section_4, section_5, section_6, section_7), id="content", role="document",)

header = Header(H1(website), menu, Hr(), cls='container')
main   = Main(sections, cls='container line-numbers')
footer = Footer(Hr(),P("Made by kit using FastHTML & Pico CSS, June 2024."), cls='container')
scripts = Script(src="style/prism.js")

# Home page (Cover page)
@rt("/")
def get():
    return html, Title(website), header, main, footer, scripts
