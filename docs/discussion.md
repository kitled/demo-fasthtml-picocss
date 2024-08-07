# Discussion

A primary goal was to have a whole website in one plain and simple file. I like very portable things.

- Custom JS, CSS isn't embedded in the Python file, but you could.
- Alternatively, with a SQLite db file, you can trim this massive Python code to a small fraction of its current size.
- I wanted the least obfuscated, most directly visible *everything—"Show me the f\*\*\*\*ng input!"*—such that reading the python file is all you need, so I opted for inline strings since it's all static.  
Self-evidently, this is for learning purposes. I wouldn't *generally* recommend such heresy.


## Background story

*I did this naive rewrite as a learning exercise. Hadn't done much web for years; wanted to get my hands dirty with FastHTML, while diving deep enough into Pico CSS; and test CursorAI, my new editor… All at once. The latter would prove nigh in-dis-pen-sable to 'write'—or should I say* <kbd>Tab</kbd>*—those 4600-ish lines (never fear: most of them are sub-30 columns).  
It all took much less time that one would think, although I'll gladly admit I underestimated **greatly** the amount of work. lol. Silly me.* 😅


## Current status

This is a side project, and summer is always busy for me (right now I'm redeploying my entire home+SOHO infra… good times… *not*). So sadly, no ETA for completion. I intend to use it for myself eventually, and this is just a naive alpha.


## Features

The single-page layout was inspired by GameFaqs, whose plain-text UX is by far the most straightforward (no boilerplate) I've ever used. It's a niche use-case: you're busy with a big main thing (game, code editor, whatever) and you just need extensive docs by the side that you can quickly query for anything and get there in seconds. GameFaqs did it in plain text; we can do better with HTML, but the principle stands.

I've yet to make all proper web features.

- Some ToC doubling as navigation.
- Folding sections,
  - with collapse all/none buttons for each \[sub\]section.
- Working anchors (I'm dumb and didn't anticipate many evidently have the same name, duh.)
- Some short code form (e.g. section numbering in the Python file) for quick search
- Fix some dynamic JS things
- Search feature with nice-enough UI to quicly glance at the desired part.


## AI generation for websites (ideas)

> [!NOTE] 
> This is highly speculative. I need to run tests to know if my intuition makes sense here, and prove that current SOTA can't already do it well enough.

There's (*will be*) a total of about 100 HTML:FastHTML pairs. That's a 'functionally perfect' dataset I'd like to feed some LLMs to see if it makes them great FastHTML writers and interpreters.

Two cool goals might be

- "Any webpage to FastHTML" generates FH code from web pages
  - as a browser extension perhaps, to inspect & quickly capture any component/layout → I've no idea how to do that (yet)
- "FastHTML to HTML" ← can LLMs replace the Fast 'core', doing what FastHTML does, output into a usable `.html` file?

Possible next step: add a "prompt" column → user input that produces the FastHTML snippet as output.  
This may help us reach yet another goal:

- "Prompt to FastHTML" ← in plain English: make a website

Don't get me wrong, many "no code" tools are absolute rubbish (mere prompt injection wrapping some LLM), and the few that work are incredibly narrow in actual scope, beyond the fancy GUIs. However, we can indeed narrow the problem down—e.g., aim to generate custom components, from a known set of prototypes, and simply organize them properly on the page. Even just that could reduce friction immensely from backend work to live web prototype, as informing existing components requires virtually no skill (unlike setting up all the boilerplate and wiring, however minimalist the library).

The reason why I think FastHTML lends itself impeccably well to reach great results with *less*-code LLM assistants is threefold:

- Lean and mean codebase, a simple direct mapping of HTML: as narrow a scope as it could ever get to make web things in Python.
- All batteries included are straightforward as well, with sane *great defaults* ([HTMX](https://htmx.org/), [SQLite](https://www.sqlite.org/), [Uvicorn](https://www.uvicorn.org/), [Starlette](https://www.starlette.io/), mirroring the [FastAPI](https://fastapi.tiangolo.com/) syntax…)
- Underlying "[Hypermedia](https://hypermedia.systems/)" paradigm is deemed sound and *elegant* by many great programmers. (who am I to know any better)




## Replicate with other CSS frameworks?

First of all, *be my guest!* : ) The more, the merrier… 

There are great candidates — Material etc. Classes won't directly transfer, so maybe we should make a classless skeleton for all HTML tags, or abstract classes generally and then translate for each CSS at hand.
