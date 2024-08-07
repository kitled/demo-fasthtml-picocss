# AI dataset?

> [!NOTE] 
> This is highly speculative. I need to run tests to know if my intuition makes sense here, and prove that current SOTA can't already do it well enough.

This project, eventually containing about 100 HTML:FastHTML pairs, is a small but 'functionally perfect' dataset.

I'd like to feed it to LLMs (prompt injection, RAG, finetune…), to see if it makes them very capable FastHTML writers and interpreters. I see three angles:

- Capture and convert HTML from any web page to FastHTML code.
- Conversely, output HTML from a FastHTML input.
- Finally, natural language (user prompt) to FastHTML (less-code AI assistant).

I think some of these use cases can be solved with a very small model, well-aligned for the purpose, because FastHTML is very concise (<1000 lines).


## HTML to FastHTML (and back)

Web conversion to FastHTML may work as a browser extension perhaps, to inspect & quickly capture any component/layout → I've no idea how to do that (yet).

The reverse, FastHTML to HTML, is more about testing whether LLMs can replace the Fast 'core'; i.e., output a usable `.html` file from FastHTML code.

## User prompt to FastHTML

Possible next step: add a "prompt" column, containing the user input that produces the FastHTML snippet as output. This may help us reach yet another goal:

- "Prompt to FastHTML" ← in plain English: make a website

Don't get me wrong, many "no code" tools are absolute rubbish (mere prompt injection wrapping some LLM), and the few that work are incredibly narrow in actual scope, beyond the fancy GUIs. However, we can indeed narrow the problem down—e.g., aim to generate custom components, from a known set of prototypes, and simply organize them properly on the page. Even just that could reduce friction immensely from backend work to live web prototype, as informing existing components requires virtually no skill (unlike setting up all the boilerplate and wiring, however minimalist the library).

## 

The reason why I think FastHTML lends itself impeccably well to reach great results with *less*-code LLM assistants is threefold:

- Lean and mean codebase (<1000 lines), a simple direct mapping of HTML: as narrow a scope as it could ever get to make web things in Python.
- All batteries included are straightforward as well, with sane *great defaults* ([HTMX](https://htmx.org/), [SQLite](https://www.sqlite.org/), [Uvicorn](https://www.uvicorn.org/), [Starlette](https://www.starlette.io/), mirroring the [FastAPI](https://fastapi.tiangolo.com/) syntax…)
- Underlying "[Hypermedia](https://hypermedia.systems/)" paradigm is deemed sound and *elegant* by many great programmers. (who am I to know any better)
