# FastHTML 🧡 Pico CSS

> 🡆 *Demonstrating Pico CSS in FastHTML.*

This demo is a rewrite of the "Docs" section of the Pico CSS website as one (long) page of FastHTML.

You can clone this repo and run `main.py` locally through `uvicorn` :

```bash
uvicorn main:app
```

> [!IMPORTANT]  
> - Currently a **Work-In-Progress**! (WIP)
> - **Friendly warning: there are garbage files** in that repo, lots of drafts & experiments. 
> - I haven't been able to deploy this particular app on my Linode VPS.  
> I've had success with other FastHTML apps, not sure what's up here.  
> **It "works on my machine", so hopefully on yours too.**  
> I'll redo the core properly if needed eventually.  
> (I should probably look into e.g. Railway I guess, but I'm not sure which template to choose for FastHTML.)
>
> If you can help me solve/learn ASGI Python web apps deployment, feel free to reach out.  
> → in [GH Issues](https://github.com/agenkit/demo-fasthtml-picocss/issues) or on [𝕏](https://x.com/x__kit)

> [!TIP]
> - The code of [`main.py`](https://github.com/agenkit/demo-fasthtml-picocss/blob/main/main.py) is discussed in [`docs/main.md`](https://github.com/agenkit/demo-fasthtml-picocss/blob/main/docs/main.md) (very rough, partly outdated draft)  
> - See further [`docs/discussion.md`](https://github.com/agenkit/demo-fasthtml-picocss/blob/main/docs/discussion.md)


## TL;DR

- **Unfinished** WIP. No ETA.

- It's one long web page, itself generated by one huge `main.py` file (plus some custom CSS, JS).

- Usage: classic **page search**, <kbd>Ctrl</kbd> ( <kbd>⌘</kbd> ) + <kbd>F</kbd>
  - Applies both to the web GUI and the Python file!

- (final form) About a hundred **1:1 pairs** of `HTML` ←→ `FastHTML` snippets for quick translation.

- Demonstrates **Pico CSS**,
  - which can work "classless" as well, wherein naked HTML tags are all you need for style.

- Comments warmly welcome 🎓🆘🙏 → [GH Issues](https://github.com/agenkit/demo-fasthtml-picocss/issues) or [𝕏](https://x.com/x__kit)

- Built while FastHTML was still in **beta** (June 2024), thus **may still contain errors and false information** (will be corrected eventually).  
Notably, **all HTML tags are now implemented** in FastHTML.




## Resources

### 📚 Docs

- FastHTML: <https://answerdotai.github.io/fasthtml>
- Pico CSS: <https://picocss.com/docs>
- `main.py`: https://github.com/agenkit/demo-fasthtml-picocss/blob/main/docs/main.md

### 🧬 Code

- FastHTML: [https://github.com/AnswerDotAI/fasthtml](https://github.com/AnswerDotAI/fasthtml)  
(⚖️ [Apache 2](https://github.com/AnswerDotAI/fasthtml/blob/main/LICENSE) )
- Pico CSS: [https://github.com/picocss/pico](https://github.com/picocss/pico)  
(⚖️ [MIT](https://github.com/picocss/pico/blob/main/LICENSE.md) )

### 💡 Misc

- Examples: <https://picocss.com/examples>  
  - Code: <https://github.com/picocss/examples>  
- Cursor (VSCode with *great* AI): <https://www.cursor.com/>


## How to

### Run

Clone this repo then run `main.py` with `uvicorn`.

```sh
git clone https://github.com/agenkit/demo-fasthtml-picocss.git
cd demo-fasthtml-picocss
uvicorn main:app
```

### Use

To quickly page-search for any concept, HTML tag, CSS class, variable, etc.

1. Press <kbd>Ctrl</kbd> ( <kbd>⌘</kbd> ) + <kbd>F</kbd> 

2. Type `THING` to find `THING`s on the page.

3. Hit <kbd>Enter</kbd> to reach the next occurrence ( `↓` )

  - <kbd>Shift</kbd> + <kbd>Enter</kbd> for previous ( `↑` )

Each HTML code snippet is (WIP: will be…) associated 1:1 to a Python FastHTML code snippet that generates it. The canonical section goes:

- Title
- \[Description\]
- Rendered example (HTML+CSS
- HTML code snippet
- FastHTML code snippet

Only the last part self-evidently differs from the Pico CSS website. Everything else should be identical.

> [!IMPORTANT]
> - FastHTML snippets are missing. WIP!
> - There is a noticeable gap between sections. This is normal during development. I'll revert to Pico CSS defaults after implementing section folding (`<summary>` tag).

Syntax highlighting is provided by [PrismJS](https://prismjs.com/), whose defaults fit better with PicoCSS than HighlightJS for me, on top of allowing inline highlighting.


## Further discussion

See [docs/discussion.md](https://github.com/agenkit/demo-fasthtml-picocss/blob/main/docs/discussion.md)


## About me

I'm *not* a web dev. I just made a few websites since 1999 (literally).  
In 2024, I try to suck less at AI and that's already a tall order for me.  
*Especially when geniuses throw FastHTML at me randomly on an otherwise perfectly good AI day.* 😅

So feel free to school me, I know I'm doing a lot of things wrong in my code.  
I just don't know what—*yet*—and that's where *you* come in!
