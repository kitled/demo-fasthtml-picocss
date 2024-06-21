from fasthtml.common import *
import json
website = "FastHTML 🧡 Pico CSS"
html = Html(lang='en', data_theme='dark')

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
prism_css_theme = Link(    # linked at the bottom of the HTML file
    rel="stylesheet", 
    href="style/prism-one-dark.css",
    type="text/css"
    )
demo_css = Link(           # Override some Prism styles
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

# TODO: functionalize all this shit below

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
    return Div(" • ", style='background:'+ to_rgb(color, shade)+';',)

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

# ↓



# css = Style(" ".join(o for o in css_overrides))
section_1 = Section(
    H2("Getting started"), 
    H3("Quick start"), 
    H4("Starter HTML template"),
    block_code,
    H3("Version picker"),
    color_palette,
    )
section_2 = Section(
    H2("Customization"), 
    H3("CSS variables"),
    )

# ↓

header = Header(H1(website), menu, Hr(), cls='container')
main   = Main(section_1, section_2, cls='container line-numbers')
footer = Footer(Hr(),P("Made by kit using FastHTML & Pico CSS, June 2024."), cls='container')
scripts = Script(src="style/prism.js")

# data_theme = attrdict(dict({'data-theme':'light'}))
# Home page (Cover page)
@rt("/")
def get():
    return html, Title(website), header, main, footer, scripts


# Style(':root {prefers-color-scheme: light;}')
