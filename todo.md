## TODO

This isn't meant for public use, I'm just leaving it here because why not let you see what's in my head'.


- demonstrate easy changes with simple CSS or FastHTML tags
  - e.g. change `background` color taking `prefers-color-scheme: dark|light` into account (so two colors, two selectors)


- make each section a color: 7 sections = 7 emojis
	-  ⚪｜⚫＋🔴🟠🟡🟢🔵🟣 
	- dark|light mode


### 24F25

2024.06.25 — this is a WIP, a list of ideas, thinking out loud much of the time. **Not everything** can (or should) be done!

- some is required (usually prefixed with 🧡)
- some are ideas for extension (not all realistic, I don't filter things at this level)

---

#### SHORT LIST

- [x] 🧡fix **code highlighting** with highlightJS
- [x] 🧡**check if** those are actually **used**: Hyperscript  line 14
- [x] 🧡**fix** get/post **HTMX** + ids etc → learn simple btn show/hide div
- [ ] Anchors don't work because of name collisions: do concat H3-H4
- [ ] 🧡**FastHTML code** → dual with Pico CSS HTML
- [ ] 🧡make **ASIDE** with cool btn absolute position corner
- [ ] 🧡make **Folding** structure for all headings
      SIMPLEST IMPLEMENTATION in PicoCSS using Accordions `<summary>` tags.
- [ ] 🧡redo app basis: use the "**first app**" demo or something like that, then see from there
- [ ] make BASIC_**HTML** (section 0)
- [ ] make **HTMX** (section 8)
- [ ] make **Surreal** + **CSS Scope Inline**
- [ ] at that point, make categories → single page won't do and makes no sense
	- [ ] this website really is becoming "`fasthtml.examples.kit`"
- [ ] check `@threaded` decorator from FastCore 🡆 and learn that shit too 
- [ ] Cool stuff:
	- [ ] daisyUI
	- [ ] DoodleCSS
	- [ ] Find something that does cool アニメ 「anime」 animations in `svg` / `css` ideally to enrich behviors (things appearing, disappearing etc.)  
	      → eg カメハ 「kameha」 🡆 `<div display="block">` !



#### FULL DETAIL

- [ ] 🧡fix **code highlighting** with highlightJS
	- [ ] learn to make code highlight theme to make FastHTML theme (fork the python rules)
		- [ ] First just a spec
		- [ ] Then VSCode extension, JS plugin on `unpkg`
		- [ ] "Ad hoc theming"
			- [ ] e.g. normal Python is blue+yellow
			- [ ] FastHTML is `primary-color` eg red
			- [ ] code highlighter (HighlightJS etc) is `secondary-color` eg green
				- [ ] or whatever ad hoc thing is used, like `claudette` or whatever
	- [ ] I think Pico CSS takes PrismJS for syntax parsing and then applies its own calculated colors `--pico-code-...` to each type.
- [ ] try `<hgroup>` implementation
- [ ] `.chapter` = H2 CSS
- [ ] 🧡**FastHTML code** → dual with Pico CSS HTML
	- [ ] basic should be vanilla FastHTML (no wrapper)
	- [ ] for F♥P website, maybe think about reimplementing things with our classes in our wrapper functions
- [ ] 🧡**check if** those are actually **used**:
	- [ ] Hyperscript  line 14
- [ ] 🧡**fix** get/post **HTMX** + ids etc
	- [ ] POWERFUL ABSTRACTION: maybe try HTMX as a generic wrapper for *any* Py function → then call that
		- [ ] goal: you don't need to know HTMX to do things in Py
		- [ ] just a custom router probably that takes some  
		      `@rt(/{fn}-{*args}-{**kwargs})`  
		      and uses that to call the eponym function  
		      `def fn(*args, **kwargs)`
- [ ] 🧡make **ASIDE**
- [ ] 🧡make **Folding** structure: each heading can fold its content; up to a list of 7 H2().  
      DEMONSTRATE SIMPLEST IMPLEMENTATION in PicoCSS using Accordions `<summary>` tags.
	- [ ] All titles are embedded in `<summary>` (such that title name doesn't disappear when folded, only when folding the parent title).
	- [ ] This is hacky, will add L/R margins, so fix CSS for it with its own class or in `container` class or whatever. Compare with/without folding to make it look as identical as possible to keep everything else working fine.
	- [ ] Shift + click (or diff button upon hover) to collapse/expand ALL
	- [ ] differentiate between `fast_X_Y_Z` snippets (vanilla FastHTML) and the website design itself (see "README > How to use > Website" for that view)
- [ ] KEYBOARD SHORTCUTS! How hard is it? `?` for modal with keybindings
- [ ] think about breaking down that big-ass file maybe
	- [ ] if you do, absolutely put wrapper structural functions into their own module, to have them available everywhere with a simple import
		- [ ] maybe that prefix could be useful to diff with same name: `Div()` for FastHTML vanilla, `x.Div()` for my extension thereof.
	- [ ] 🧡use the "**first app**" demo or something like that, then see from there
		- [ ] redo "starter HTML template" with that
	- [ ] use it for small demos too, maybe a generic page per feature (1 `pico_` variable for each page)
	- [ ] when HTMX is required, we add that snippet too
- [ ] implement **themes** ← in addition to dark/light
- [ ] embed **𝕩post**, YT, etc.
- [ ] **HTML parser 🡆 to FastHTML translator?** would be really cool, try to find an existing library to parse HTML maybe
	- [ ] make new project with FastHTML demo and translations and ask Cursor about it
- [ ] something really cool: **Modal (any serverless) hooks to run any Python "in the browser"** (although technically not, but it gives us basic REPL in pure Python, no translation, transpiling, whatsoever)
	- [ ] this is hacky but it works and is the only way
	- [ ] yes you must pay. or use some free compute somewhere (there's a lot of that)
	- [ ] alternatively of course, use local user python install + CPU but… hooks must be hard otherwise everyone would be doing it (wouldn't require notebooks with iPy kernels etc)
- [ ] make **different versions** of the website
	- [ ] **pure vanilla** (demonstrates limitations, unfortunately, especially without some custom CSS)
	- [ ] **PrismJS** (no HighlightJS) → copy Pico CSS website
	- [ ] **multi-page** see above breaking down in files
	- [ ] **my CSS theme** over Pico (Goku palette)
- [ ] create a helper wrapper library for FastHTML that makes common things even simpler to do.  
      Look at `xtend.py` in FastHTML to do it well (copy that thing).
    - For example:
		- [ ] Login modal
		- [ ] side-by-side code block with custom highlighting (just ad hoc string patterns)
		- [ ] endpoint for common APIs like icanhazip, Anthropic, Modal, etc. (all the free compute credit things if we can)
		- [ ] typical dashboard for LLMs (with 'tokens', 'temp' etc. prewired)
		- [ ] … Look at what exists and re-do that
	- [ ] **make it really easy to extend/tweak/customize → see how it's best done in python**
	- [ ] make a GEM (Graphical Extravaganza Module) → lots of super-cool fancy features like bg-video, shiny, sparkly, and shit.
		- [ ] helps selling your website!
- [ ] make abstraction layer for "Table of Contents" with auto-numbering and ordering
	- [ ] SOA: simple hierarchical list in some variable or text file
	- [ ] parser will make Headings with proper Hn("`title`") & numbering
	- [ ] then you just reference that in Python somehow in your wrapper functions (neither name nor number is hardwired in the variable name, so it's easy to change later in the SOA)
- [ ] COLORS: create `ahls` for A-weighted HLS that will correctly normalize L,S values to be consistent across all Hues (same concept as A-weighted db gain in audio)



