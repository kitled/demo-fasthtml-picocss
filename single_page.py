from fasthtml.common import * # type: ignore


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

app = FastHTML(hdrs=(
    head,
    pico_css,
    ))
rt = app.route
@rt("/{fname:path}.{ext:static}") # Serve static files
async def get(fname:str, ext:str): return FileResponse(f'{fname}.{ext}') # type: ignore




# def make_section(section:dict):
#     items = []
#     for title, level in section.items():
#         items.append(heading(title, level))
#     return Section(*items)





# H2 = [
#     "Getting started",
#     "Customization",
#     "Layout",
#     "Content",
#     "Forms",
#     "Components",
#     "About",
#     ]






# let's begin by making the H3 section page replica.




#Let's think about











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
    TODO: Implement *contents to add block contents.
    '''
    h = [H1, H2, H3, H4, H5, H6]
    hn = h[lv-1]
    anchor = title.lower().replace(' ', '-')
    return hn(
        title, 
        A('🔗', href='#'+anchor, id=anchor, cls='secondary', tabindex="-1")
    ), P(desc) if desc else None

def art_header(lv, title, desc=None): 
    return heading(lv=lv, title=title, desc=desc)
#   +
def art_c(*c): # c for content
    return (*c, )
#   +
def art_footer(html, python): 
    return Footer(Pre(Code(html)), Pre(Code(python)))
#   =
def article(c, art_header=None, art_footer=None, **kwargs): 
    return Card(*c, header=art_header, footer=art_footer, **kwargs)


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




# s for section
# c for content
# d for div

c_1_1_1 = P(
    A(
        "Download Pico", 
        rel="noopener noreferrer", 
        href="https://github.com/picocss/pico/archive/refs/heads/main.zip", 
        target="_blank"
    ), 
    """ and link """, 
    Code("/css/pico.min.css"), 
    """ in the """, 
    Code("""<head>""", cls="language-html", ), 
    """ of your website.""",
    ), 

s_1_1_1 = section(
    c_1_1_1, 
    lv=4, title="Install manually",  
    )

# this must nest all lv4_s
s_1_1_0 = section(
    s_1_1_1, 
    P("There are 4 ways to get started with pico.css:"), 
    lv=3, title="Quick start", 
    desc="""Link <code>pico.css</code> manually or via CDN for a dependency-free setup, or use NPM or Composer for advanced&nbsp;usage.""", 
    )


# lv2_s must nest all lv3_s
s_1_0_0 = section(
    s_1_1_0, 
    lv=2, title="Getting started", 
    )


# # Create H2 headings
# headings = []
# for h in H2:
#     headings.append(heading(h, 2))





# Home page
@rt("/")
def get():
    return main(s_1_0_0, s_1_1_0, s_1_1_1)
