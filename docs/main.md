# `main.py` meta-docs

> [!NOTE]
> This is a side project, and these are notes taken on-the-fly more than proper documentation.  
Feel free to ask anything in GH Issues or hit me on 𝕏.

## README`.md`

This was originally intended as the README, but speaks more of the code itself, so it's become a doc file.

### Why this project

Initially, I wanted to make a short summary of Pico CSS features, the exhaustive book of KISS recipes. There is still that, but in browsing their docs I realized there's a lot of interactivity on their website to demonstrate features. Buttons to add/remove divs to play with `grid`, color switches, and so on. I started wondering if and how I could implement those in FastHTML. My primary limitation is that I don't know much about Javascript in general and a at best cursory awareness of HTMX—I've yet to dive deep in this [hypermedia](https://hypermedia.systems/) marvel. While a great occasion, I just don't have much time for that, so learned as I went.

There is no database, because I didn't want to add an abstraction layer between the data and the code—reading it should be self-sufficient to work out exactly how what you put in Python comes out the other side in HTML. This includes custom CSS beyond the Pico framework.

> [!TIP]
> *A complete website, mostly below 100 columns for readability, makes for very long files: search* ( <kbd>Ctrl</kbd>+<kbd>F</kbd> ) *is your friend; use your IDE features.*

### How to use

#### Code

There are three parts in the file, besides the idiomatic top imports.

1. Logic
2. Data
3. Routing

The logic part is necessary for the data section, which is why it comes first in Python. These functions implement the HTML layout of the Pico CSS Docs pages in one "doubly" single-page FastHTML app: both the code and the result sit in one page, respectively `.py` and on the web. *It's just one big script… with lots of \<section\> nesting!*

The data part is entirely composed of string assignments, processed by our functions to generate the correct layout—tags, attributes, nesting.

The routing part comes last by necessity to wire all the things and implement dynamic HTMX features—not many. *I don't know HTMX.*

Classes, ids, etc. are kept to a bare minimum for a functional website, to demonstrate Pico CSS greatness and the power of semantic HTML.

> [!NOTE]
> There is a classless version of Pico CSS, which though less featureful yields minimal HTML.

#### Website

There are three view modes.

1. Normal single-page website (HTML, CSS, Js)
2. Under the hood / look behind the curtains (Python)
3. Side-by-side comparison

*Normal* is self-explanatory. *Under the hood* "reverses" the side of the website and shows the full Python code, although not as in the file: we display the code that makes each part in place of said part, such that you can switch back and forth to see the code and the result. This involves a bit of redundancy (reminders for definitions notably), but avoids endless scrolling to get context (which is something that happens a lot when working on the file itself, but IDE solve that with splits). Speaking of which, *side-by-side* is exactly what it means, and combines the two views for convenience.

*Later on, when I integrate other CSS themes (like Tokyo Night or Atom One or my own), there will be switches and side-by-sides to compare these.*


### Important advice to myself for FastHTML

- create wrappers to ensure you can modify all calls from a single source
	- you want to hard-wire as little as possible (e.g. classes)
	- you want to abstract actual attributes etc. (even with a similar name) so these are general variables for you to peruse.
		- e.g. make a variable `h = 'html'` and `p = 'python'` and use those in `lang=LANGUAGE_NAME` because it allows you to quickly switch them all (e.g. to some custom theme `fasthtml` that forks `python` for instance).
		- these only become an actual class in the wrapper function → you can filter things there too, testing if `lang` exists or equals whatever.
- my suggestion of **minimal CSS for code highlighting** proper → gives you back your CSS
	- WHY? 🡄 code highlighters (hljs, prism, etc.) will add their own classes, messing up with Pico CSS
	- **removes all `hljs` BS**
	- same with PrismJS


### Cursor

Consider using Cursor. Here's a self-obvious example why.

It took me three <kbd>Tab</kbd> hits—all of 3 seconds—to get from this

```python
body_4_1_1 = Table( # ↓ naive copy/paste from website below, no tags no fns no nothing just contents
	Thead(Breakpoint	xs	sm	md	lg	xl	xxl
		Base	16px	17px	18px	19px	20px	21px
		<h1>	32px	34px	36px	38px	40px	42px
		<h2>	28px	29.75px	31.5px	33.25px	35px	36.75px
		<h3>	24px	25.5px	27px	28.5px	30px	31.5px
		<h4>	20px	21.25px	22.5px	23.75px	25px	26.25px
		<h5>	18px	19.125px	20.25px	21.375px	22.5px	23.625px
		<h6>	16px	17px	18px	19px	20px	21px
		<small>	14px	14.875px	15.75px	16.625px	17.5px	18.375px
),
)
```

to that.

```python
body_4_1_1 = Table( # ↓ perfectly formatted contents
    Thead(
        Tr(Th("Breakpoint"),Th("xs"),Th("sm"),Th("md"),Th("lg"),Th("xl"),Th("xxl")),
    ),
    Tbody(
        Tr(Td("Base"),Td("16px"),Td("17px"),Td("18px"),Td("19px"),Td("20px"),Td("21px")),
        Tr(Td("<h1>"),Td("32px"),Td("34px"),Td("36px"),Td("38px"),Td("40px"),Td("42px")),
        Tr(Td("<h2>"),Td("28px"),Td("29.75px"),Td("31.5px"),Td("33.25px"),Td("35px"),Td("36.75px")),
        Tr(Td("<h3>"),Td("24px"),Td("25.5px"),Td("27px"),Td("28.5px"),Td("30px"),Td("31.5px")),
        Tr(Td("<h4>"),Td("20px"),Td("21.25px"),Td("22.5px"),Td("23.75px"),Td("25px"),Td("26.25px")),
        Tr(Td("<h5>"),Td("18px"),Td("19.125px"),Td("20.25px"),Td("21.375px"),Td("22.5px"),Td("23.625px")),
        Tr(Td("<h6>"),Td("16px"),Td("17px"),Td("18px"),Td("19px"),Td("20px"),Td("21px")),
        Tr(Td("<small>"),Td("14px"),Td("14.875px"),Td("15.75px"),Td("16.625px"),Td("17.5px"),Td("18.375px")),
    ),
    cls="overflow-auto",
)
```

Sorry for the new bill! But it's well worth it. It understands a lot of things, including Markdown, or FastHTML functions.


### Contribute

Do other CSS themes and various Javascript frameworks like code syntax highlighters or whatever cool thing you want.

The M.O (how we roll) is simple: **reimplement the integrated tool's demo and/or docs in FastHTML**, to demonstrate both at once in proper HTML.

It doesn't have to be a single file as I did for the data, but **make sure the types and exact characters being processed are easy to see**, just by reading the code, optionally helped by some handy REPL. If you use a database, provide helper functions to inspect the data and feed that base. 

The name of the game is **frictionless reproducibility**, that's our North.  
Great open code should be *stupidly easy* to steal.






## arch

### HTML structure

🡇 We're going for something like this. Pay attention to nesting, as it's essential to properly structure your FastHTML function calls nesting. This intends to reproduce the exact Pico CSS website's HTML (the whole "Docs" section, flattened as one page).

```html
<main>


<!-- MAIN (H2) -->
  <section>                                           <!-- 1_0_0 -->
    <header><h2>Getting started</h2></header>
    <p>Details about Getting started</p>
    
    <!-- SUB (H3) -->
    <section>                                         <!-- 1_1_0 -->
      <header><h3>Quick start</h3></header>
      <p>Details about Quick start</p>
      
      <article>                                       <!-- 1_1_1 -->
        <header><h4>Starter HTML template</h4></header>
        <p>Details about Starter HTML template</p>
        <!-- 
        … 
        article contents
        …
        -->
        <footer>
          <pre>                                       <!-- Pico CSS -->
            <code>
            <!-- … -->
            </code>
        </pre>
          <pre>                                       <!-- FastHTML -->
            <code>
            <!-- … -->
            </code>
          </pre>
        </footer>
      </article>
      
    </section>
    
    <!-- SUB (H3) -->
    <section>                                         <!-- 1_2_0 -->
      <header><h3>Version picker</h3></header>
      <p>Details about Version picker</p>
      <article>                                       <!-- 1_2_1 -->
        <header><h4>Stuff</h4></header>
        <p>Details about Stuff</p>
        <footer><pre><code><!--…--></code></pre><pre><code><!--…--></code></pre></footer>
      </article>
      <article>                                       <!-- 1_2_2 -->
        <header><h4>More stuff</h4></header>
        <p>Details about More Stuff</p>
        <footer><pre><code><!--…--></code></pre><pre><code><!--…--></code></pre></footer>
      </article>
    </section>
    <!-- more SUB (H3) SECTIONS -->
  </section>


<!-- MAIN (H2) -->
  <section>                                           <!-- 2_0_0 -->
      <h2>Customization</h2>
      <p>Description...</p>
      <!-- … -->
  </section>
  <!-- more MAIN (H2) SECTIONS -->


</main>
```


- Each section (& article) begins with a first block: Header(Hn(section title))
- Followed by flat block of contents: 
  - `<p>` description (if any)
  - `<article>` (actual meat usually, letting semantic search ignore most everything else)
- Hn Nesting follows numbering: 1_1_0, 1_1_1, 1_1_2, 1_2_0, 1_2_1, 1_2_2, …
- Knowing that "`<header>`, `<main>` and `<footer>` as direct children of `<body>` provide a responsive vertical padding"

```html
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
```


On the Pico CSS/Docs website, there's a pattern for each `<section>` (titled topic).
1. `<h2>` 
2. `<p>`'s to explain (and whatever else fits there)
3. `<article>` ← each article is unique, actual content is here
     - `<any>` whatever the demo shows (`<input>`, `<button>`, …)
     - `<any>` 
     - …
     - `<footer>`
      - `<pre>`
        - `<code>` # contains the article's code

- `<h2>` ↓
  - we will use `<h3>` (because 2 is section, 3 is sub-section = section on Pico CSS Docs)
  - nest it within a `<header>` tag for best semantic practice
- We will add a second `<pre><code>` to that to display FastHTML code.
  - either side by side if viewport is \>1024px
  - or stacked, and hidden by folding if \<1024 px (option to hide all Python or all HTML)


```
<main>

nav???
aside id="documentation-menu"
  header???
    nav
      details [open]
        summary → title of section (h2 below)
        ul
          li × n
            a → title of block (h3 below)
      details
        summary → title of section
        ul
          li × n
            a
       …
hgroup
aside id="table-of-contents"
div id="content" role="document"
  section
    h2
      p or article
    h3
      p or article
    h3
      p or article
  section
  section
```

(this might be outdated, see actual `main.py` file)

```python
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
```



Load after page:

```html
<img loading="lazy" />
<script defer >…</script>
```


### `fh` function nesting 


#### MAIN (H2) Section



```html
<section>                                           <!-- 1_0_0 -->
    <header><h2>Getting started</h2></header>
    <p>Details about Getting started</p>
```

```python
Section(
    Header(H2("…", ), ), #← assume each line is 1 item of a tuple fed to the parent function (`Section()` here)
    P("…"),
    # SUB (H3),
    # SUB (H3),
    # …
) # ← MAIN section closes after nesting all its SUBs.
```



#### SUB (H3) Section



```html
<section>                                         <!-- 1_1_0 -->
      <header><h3>Quick start</h3></header>
      <p>Details about Quick start</p>
```

```python
Section(                                          # child of MAIN (H2) section
    Header(H3("…")),
    P("…"),
    # ARTICLE (H4),
    # ARTICLE (H4),
    # …,
) # ← SUB section closes after nesting all its ARTICLEs.
```



#### Article (H4)



```html
<article>                                         <!-- 1_1_1 -->
  <header>
    <h4>
      "Starter HTML template"
      <a href="">#</a>
    </h4>
  </header>
  <p>Details about Starter HTML template</p>
  <!-- article contents
	…
	…
	…
	…
	…
  -->
  <footer>
    <pre>                                         <!-- Pico CSS -->
      <code>
      <!-- … -->
      </code>
    </pre>
    <pre>                                         <!-- FastHTML -->
      <code>
      <!-- … -->
      </code>
    </pre>
  </footer>
</article>
```

```python
Article(                                          # child of SUB (H3) section
    Header(H4("…", ), ),
    P("…"),
    # ARTICLE CONTENTS 
    # → flat tuple(Tag1(), Tag2(), …, TagN)
    # → nesting as required: (P(A(Span(…)))
    Footer(
        Pre(Code("…"), ),
        Pre(Code("…"), ),
    ),
) # ← ARTICLE closes after nesting its HEADER, CONTENTS, and FOOTER.
```


#### Anchors ⚓

All H$n$ titles have an anchor link attached to them, and optionally a description below, so `Header()` with a `H2()`, `H3()`, `H4()` call in fact looks like:

```html
<header>
  <h3>
    Overview
    <a href="#overview" tabindex="-1" id="overview" class="secondary" name="overview">🔗</a>
  </h3>
</header>
```

We sanitize the section title first in FastHTML. The `secondary` class has no effect on emojis (you may use `#` or any other char instead).

```python
anchor = title.lower().replace(' ', '-')
H2(title, 
   A('🔗', href='#'+anchor, id=anchor, cls='secondary', tabindex="-1"),
)
```

Here's a generalized function that works for any title level. You want to nest it inside a `Header()` call to implement our pure semantic HTML schema above.

```python
def make_heading(title:str, lv:int):
    '''Returns a heading block with title and anchor link.
    '''
    h = [H1, H2, H3, H4, H5, H6]
    hn = h[lv-1]
    anchor = title.lower().replace(' ', '-')
    return hn(
	          title, 
	          A('🔗', href='#'+anchor, id=anchor, cls='secondary', tabindex="-1")
		   )
```



## Layout data structure

Let's think of a good data structure to represent the layout of an HTML page.

HTML will nest most of the structure, but when reading a page, we tend to think of it linearly. A db table is also but a sequence of rows. When manipulating (writing, editing) a page content, we'd usually prefer a flat linear structure. We just inform it semantically for our functions to properly nest it into HTML. There are few required parameters:

- parent relation (flat, nest) i.e. *next* (both block or inline) or *child*.
	- a simple bool (bit) will do. 
		- `True` means nested (child), 
		- `False` means flat (next).
- HTML tag type (p, a, span, code, etc.)
	- attributes (class="…", id="…", etc.)
	- contents (usually within the tag)

So, a given entry

```
True, "p", ({"attr": "value"}, ), "contents"
```

Should be easily interpreted, sequentially when building the page: a `<p>` nested in its parent, with attribute "`attr`" equal to "`value`" containing "`contents`".

This should be simple enough db to make. 🡄 *try, see in practice*


---



## Notepad

just random notes for myself



Link `pico.css` manually or via CDN for a dependency-free setup, or use NPM or Composer for advanced usage.

---

```python
# H2 = [
#     "Getting started",
#     "Customization",
#     "Layout",
#     "Content",
#     "Forms",
#     "Components",
#     "About",
#     ]
```

---

```python
# Set all <code> blocks to have `highlight` class
# _Code = Code  # Trick! 😼
# def Code(*args, cls=None, **kwargs):
#     '''Hardcode `highlight` class.
#     '''
#     if cls:
#         cls = f"highlight {cls}"
#     else:
#         cls = "highlight"
#     return _Code(*args, cls=cls, **kwargs)
```
























---

```html

<table class="striped">
    <thead>
        <tr>
            <th>Device
            </th>
            <th>Breakpoint
            </th>
            <th>Viewport
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Extra small
            </td>
            <td>&lt;576px
            </td>
            <td>100%
            </td>
        </tr>
	        <tr>
	        <td>Small
	        </td>
	        <td>≥576px
	        </td>
	        <td>510px
	        </td>
        </tr>
        <tr>
	        <td>Medium
	        </td>
	        <td>≥768px
	        </td>
	        <td>700px
	        </td>
	    </tr>
        <tr>
	        <td>Large
	        </td>
	        <td>≥1024px
	        </td>
	        <td>950px
	        </td>
        </tr>
        <tr>
	        <td>Extra large
	        </td>
	        <td>≥1280px
	        </td>
	        <td>1200px
	        </td>
        </tr>
        <tr>
	        <td>Extra extra large
	        </td>
	        <td>≥1536px
	        </td>
	        <td>1450px
	        </td>
        </tr>
    </tbody>
</table>

```


























