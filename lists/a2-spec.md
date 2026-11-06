# Spec: full catalog of app tech (approach 2)

Goal: one markdown file listing every technology and framework you can use to build an app. At least 1000 distinct items. Petr browses it to pick options for any app idea.

## Scope (cover all)
- Languages used for apps, including niche ones
- Desktop GUI by language (example: Rust → iced, egui, …)
- macOS / Apple native, Windows native, Linux native
- Web-tech desktop wrappers (Electron, Tauri, …)
- Web frontend: UI libs, meta-frameworks, web UI in non-JS languages, CSS, components, state, charts, editors, 2D/3D
- Mobile native and cross-platform
- TUI frameworks per language; CLI frameworks per language
- Game engines: big engines, per-language libraries, no-code makers, fantasy consoles, interactive fiction
- Backend frameworks per language, BaaS, databases, ORMs, realtime, local-first sync
- AI/LLM app frameworks, bots, browser extensions and plugin platforms, low-code, internal tools, notebooks
- Embedded, TV / car / wearable / XR, WebAssembly
- Tooling: runtimes, bundlers, package managers, testing, packaging, app stores, hosting, observability

## Format
- `## N. Section` → `### Subgroup` (usually a language) → `- Name — note`
- Note ≤ 8 words. Name the language when the subgroup isn't one. Mark archived / deprecated / end of life / closed beta when true.
- Top: one-line intro and a table of contents. Bottom: item count per section and total.

## Quality
- Only real projects. If unsure a name exists or its current name (renames like EdgeDB → Gel, Coq → Rocq, NextUI → HeroUI), check with web search; drop it if you can't verify.
- One home per item; cross-list only when genuinely primary in both.
- Include 2025–2026 newcomers: at least 10 web searches like "new <kind> framework 2026" across sections.
- No padding with versions or plugins of the same thing.

## Output
Write to `a2-spec-catalog.md`. Work independently.
Final reply: total count, the 10 most surprising items you added, and which searches you ran.
