from fasthtml.common import *
from fasthtml.js import MarkdownJS, SortableJS

picocsslink = Link(
    rel="stylesheet", 
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.pumpkin.min.css", 
    type="text/css")

# 𝚔𝚒𝚝 custom CSS
#   - font variables: `sourceSansPro` (sans-serif), `sauceCodeProNerd` (monospace)
fontcsslink = Link(
    rel="stylesheet", 
    href="/style/fonts.css", 
    type="text/css")

css = Style(':root {--pico-font-size: 100%; }')

db = database('db/logs-test-001.db')
logs = db.t.logs
if logs not in db.t:
    logs.create(id=int, title=str, done=bool, name=str, details=str, priority=int, pk='id')
Log = logs.dataclass()

app = FastHTML(hdrs=(picocsslink, fontcsslink, css,
                     SortableJS('.sortable', 'todo-list'),
                     MarkdownJS('.markdown')))
rt = app.route

# This line ensures that the static files are served from the static folder.
# (req. for favicon, CSS etc.)
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')


hd = Header(H1("🧰 kit.gdn"), cls='hd')
menu = Div(P(A("Notes", href="/log")), P(A("Demos", href="/llm")), cls='grid')
body = Body(Code("""We'll def test():"""), P("TEST llm for real this time"))
ft = Footer(P("© 2024 kit.gdn"), cls='ft')


# Home page (Cover page)
@rt("/")
def get():
    return Title("Hello, World!"), hd, Main(menu, cls='container'), ft


