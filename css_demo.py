from fasthtml.common import *
from fasthtml.js import MarkdownJS, SortableJS

pico_css = Link(
    rel="stylesheet", 
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css", 
    type="text/css"
    )
prism_css_theme = Link(
    rel="stylesheet", 
    href="style/prism-one-dark.css",
    type="text/css"
    )
prism_css = Link(
    rel="stylesheet", 
    href="style/prism.css",
    type="text/css"
    )
prism_js = Script(src="style/prism.js")

# Override some Prism styles
css_overrides = [
    """:root {--pico-font-size: 100%; }""",
    """code[class*=language-]{padding:0em; }""",
    """:not(pre) > code[class*="language-"], pre[class*="language-"] {background: #80808028;}""",
    ]
css = Style(
    " ".join(o for o in css_overrides)
    )

app = FastHTML(hdrs=(
    pico_css,
    prism_css,
    prism_css_theme,
    css, 
    prism_js, 
    ))
rt = app.route

# This line ensures that the static files are served from the static folder.
# (req. for favicon, CSS etc.)
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')



hd = Header(H1("FastHTML 💙 Pico CSS"), cls='hd')
menu = Div(P(A("Notes", href="/log")), P(A("Demos", href="/llm")), cls='grid')
body = Body(P("Starter HTML template"), Code("some code"), )
ft = Footer(P("Made by kit using FastHTML & Pico CSS, June 2024."), cls='ft')

# Canonical HTML structure




# ↓



# ↓



# ↓


section = Section()
# sections = 
# ↓
header = Header()
main   = Main(section, cls='line-numbers')
footer = Footer()
# ↓
body   = Body(header, main, footer)



python_code = NotStr("""def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    7
    '''
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 - 1] + copy[size/2]) / 2
if __name__ == '__main__':
    import doctest
    doctest.testmod()""")



# Home page (Cover page)
@rt("/")
def get():
    return Title(
        "FastHTML 💙 Pico CSS"
        ), Body(
        hd, 
        Main(
          menu, 
          Pre(
            Code(python_code, 
            ), 
          cls='prismjs line-numbers language-python'), 
        ), 
        ft, 
        
    cls='container')

