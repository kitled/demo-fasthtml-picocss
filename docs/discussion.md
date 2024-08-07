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


## Replicate with other CSS frameworks?

First of all, *be my guest!* : ) The more, the merrier… 

There are great candidates — Material etc. Classes won't directly transfer, so maybe we should make a classless skeleton for all HTML tags, or abstract classes generally and then translate for each CSS at hand.
