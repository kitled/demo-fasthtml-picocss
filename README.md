# FastHTML 🧡 Pico CSS
*Demonstrating Pico CSS in FastHTML.*

This demo is a rewrite of the "Docs" section of the Pico CSS website as one (long) page of FastHTML.

View it live at: <https://kit.gdn/fasthtml-picocss-demo/>

## Take-away

- unfinished, work in progress, no ETA
- usage: press <kbd>CTRL</kbd>|<kbd>⌘</kbd> + <kbd>F</kbd> to find things
- (final form) About a hundred 1:1 pairs of HTML ←→ FasHTML snippets for quick translation
- demonstrates Pico CSS 
  - It mostly works classless as well, wherein the naked HTML tag is all you need for style.
- I'm not a web dev 😅 I try to suck less at AI and that's already a tall order for me.
- Comments warmly welcome 🎓🆘🙏 → [GH Issues](https://github.com/agenkit/demo-fasthtml-picocss/issues) or [𝕏](https://x.com/x__kit)
- built while FastHTML was in beta (June 2024), thus may contain errors and false information (will be correct eventually)



## Motivation & Purpose

I did this naive rewrite as a learning exercise, as I haven't done much web stuff for years, wanted to get my hands dirty with FastHTML, while diving deep enough into Pico CSS, and *oh why not* test CursorAI, my new editor (!), all at once. The latter would prove nigh indispensable to 'write'—or should I say <kbd>Tab</kbd>—those 4600-ish lines (never fear: most of them are sub-30 columns).

A primary goal was to have a website in one plain and simple file. 

When completed, you should be able to quickly search (<kbd>CTRL</kbd> / <kbd>CMD</kbd> + <kbd>F</kbd>) any concept, HTML tag, CSS class, variable, etc.

Each HTML code snippet will be associated 1:1 to a Python FastHTML code snippet that generates it. The canonical lowest-level section goes:

- Title
- Description
- HTML snippet
- FastHTML snippet

Only the last part differs from the Pico CSS website.

> [!IMPORTANT]
> FastHTML snippets are missing in v0.0.1-alpha (current latest). WIP!

Syntax highlighting is provided by [PrismJS](https://prismjs.com/), whose defaults fit better with PicoCSS than HighlightJS for me, on top of allowing inline highlighting.



## Resources

### 📚 Docs
Official documentation. <!-- and other useful resources. -->

- FastHTML: <https://answerdotai.github.io/fasthtml>
- Pico CSS: <https://picocss.com/docs>

### 🧬 Repo

- FastHTML: [https://github.com/AnswerDotAI/fasthtml](https://github.com/AnswerDotAI/fasthtml)  
(⚖️ [Apache 2](https://github.com/AnswerDotAI/fasthtml/blob/main/LICENSE) )
- Pico CSS: [https://github.com/picocss/pico](https://github.com/picocss/pico)  
(⚖️ [MIT](https://github.com/picocss/pico/blob/main/LICENSE.md) )

### Additional resources

Examples: <https://picocss.com/examples>  
Code: <https://github.com/picocss/examples>




## Discussion

### Current status

This is a side project, and summer is always busy for me, so no ETA for completion. I intend to use it for myself, and this is just a naive ..1 version, a static PoC for something much larger that has yet to fully take form in my head.

> [!NOTE]
> **Pre-release `v0.0.1-alpha` is a test version.**  
> 
> It has *most* of the Pico CSS Docs reimplemented, but:
> 
> - still misses critical information, (e.g., CSS variables)
> - behaviors, (e.g., switching color templates)
> - and FastHTML snippets.
> - Parts of the code may be ugly.



### Future



#### Features

The single-page layout was inspired by GameFaqs, whose plain-text UX is by far the most straightforward (no boilerplate) I've ever used. It's a niche use-case: you're busy with a big main thing (game, code editor, whatever) and you just need extensive docs by the side that you can quickly query for anything and get there in seconds. GameFaqs did it in plain text; we can do better with HTML, but the principle stands.

I've yet to make all proper web features.

- Some ToC doubling as navigation.
- Folding sections,
  - with collapse all/none buttons for each \[sub\]section.
- Working anchors (I'm dumb and didn't anticipate many evidently have the same name, duh.)
- Some short code form (e.g. section numbering in the Python file) for quick search
- Fix some dynamic JS things
- Search feature with nice-enough UI to quicly glance at the desired part.



#### AI

> [!NOTE] 
> This is highly speculative. I need to run tests to know if my intuition makes sense here, and prove that current SOTA can't already do it well enough.

There's a total of about 100 HTML:FastHTML pairs. That's a 'functionally perfect' dataset I'd like to feed some LLMs to see if it makes them great FastHTML writers and interpreters.

Two cool goals might be

- "Any webpage to FastHTML" generates FH code from web pages
  - as a browser extension perhaps, to inspect & quickly capture any component/layout
- "FastHTML to HTML" ← doing what FastHTML does, output into a usable `.html` file

Possible next step, add a "prompt" column: user input that produces the FastHTML snippet as output.  
This may help us reach yet another goal:

- "Prompt to FastHTML" ← in plain English: make a website

Don't get me wrong, many "no code" tools are absolute rubbish (mere prompt injection wrapping some LLM), and the few that work are incredibly narrow in actual scope, beyond the fancy GUIs. However, we can indeed narrow the problem down—e.g., aim to generate custom components, from a known set of prototypes, and simply organize them properly on the page. Even just that could reduce friction immensely from backend work to live web prototype, as informing existing components requires virtually no skill (unlike setting up all the boilerplate and wiring, however minimalist the library).

The reason why I think FastHTML lends itself impeccably well to reach great results with *less*-code LLM assistants is threefold:

- lean and mean codebase, simple direct mapping of HTML: as narrow a scope as it gets to make web things in Py
- all batteries included are straightforward as well (HTMX, SQLite, Uvicorn, Starlette…)
- 

In testing CursorAI, comments I'd heard about it "solving boilerplate" became so salient… That Cursor thing with Sonnet 3.5 under the hood managed to nearly rewrite the website on its own just going off a few first examples and the title structure in comments. I must have hit 'Tab' 1000 times or more. It took me some time to get going, but it eventually nailed the form perfectly and wrote close to a *hundred* lines by the *minute* (like 3 or 4 every 2 seconds).

It would sometimes guess subsection titles, or the very text of the website. The code snippets seemed obvious to it, nearly perfectly on many occasions. It had effortlessly learned FastHTML and Pico CSS without prior exposition.

This doesn't mean I wasn't involved in the loop for minor corrections all. the. time. It's not the job of Cursor to make websites on its own. But seeing how well it did, I realized we can do crazy-great stuff with natural language interfaces.



##




