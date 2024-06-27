from fasthtml.common import * #type: ignore

pico_css = Link(
    rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css")
enable_css = Style(":root { font-size: --pico-font-size; }")
app = FastHTML(hdrs=(pico_css, enable_css))
rt = app.route

# basic_html is a demonstration of basic HTML elements (Div, P, etc.) 
# as well as more advanced web semantics.

















dic = {'key': 'value', 'test': 'thing'}
values = Ul(*[Li(dic[o]) for o in dic])
keys = Ul(*[Li(o) for o in dic])

@rt("/")
def get():
    return Body(P('test'), keys, values, cls="container")
