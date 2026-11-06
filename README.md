<img src="icon.svg" width="48" height="48" alt="" align="left">

# App Tech Catalog

**Every way to build an app in one searchable page: 128 app types with picks, 2,265 frameworks and 3,810 names.**

Page: https://calmmage.github.io/app-tech-catalog/

<br clear="left">

## What's inside

| List | Items | How it was made |
|---|---|---|
| [App types](lists/a3-app-types.md) | 638 picks · 128 types | Phase 1: five agents each proposed app types from a different angle (structured, community, wild, Instagram saves, personal notes), then merged. Phase 2: subagents gave 3–5 picks per type |
| [Frameworks](lists/a2-spec-catalog.md) | 2,265 · 38 sections | One Opus agent with a [written spec](lists/a2-spec.md) and 36 web searches |
| [From the original ask](lists/a1-petr-words.md) | 2,429 · 54 sections | One Opus agent given the original message as is, from memory |
| [Direct](lists/a0-direct.md) | 1,807 · 36 sections | One go, from memory |

All names merged: 3,810. 61% of the App types picks are in no other list: notch app, receipt-printer app, app in a font, Telegram Mini App.

## Story

[story.md](story.md): what one go produced and what two phases produced.

## Build

```
python3 build.py
```

The script reads `lists/` and `story.md`, then writes `index.html`, a single page with no dependencies beyond Google Fonts.

## Caveats

- Checked 6 Nov 2026. Many notes in the App types list and in From the original ask come from memory and were not web-checked.
- The page was tested on desktop Chrome in light and dark themes. Phone width was not tested.
