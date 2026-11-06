# App shapes and the tech for each — Approach 3

Phase 1: five lenses (structured, community, wild internet, Instagram saves, Petr's notes) gave 240 categories, merged into 128 by «not what can be IN type 1. instead what can BE type 1». Phase 2: 3–5 options per category, from the plain default to the odd one.
Lens tags: **S** structured · **C** community · **W** wild internet · **I** Instagram saves · **N** Petr's notes.
Phase 1 lenses and merge: `a3-phase1/`. The Instagram and notes lenses are private; their tags stay.

**Total: 638 options in 128 categories.**

- [Batch 1 — Desktop & OS](#batch-1--desktop--os) — 19 categories, 95 options
- [Batch 2 — Terminal, files, scripts, services](#batch-2--terminal-files-scripts-services) — 16 categories, 80 options
- [Batch 3 — Web](#batch-3--web) — 22 categories, 110 options
- [Batch 4 — Browser, mobile, messengers, hosts](#batch-4--browser-mobile-messengers-hosts) — 16 categories, 80 options
- [Batch 5 — AI-native](#batch-5--ai-native) — 20 categories, 98 options
- [Batch 6 — Games, media, odd runtimes](#batch-6--games-media-odd-runtimes) — 19 categories, 95 options
- [Batch 7 — Devices, hardware, networks](#batch-7--devices-hardware-networks) — 16 categories, 80 options

# Batch 1 — Desktop & OS

## 1. Platform-native desktop toolkit — S C N
- **SwiftUI** — Swift · macOS · Apple's declarative default
- **AppKit** — Swift/Obj-C · macOS · original Cocoa; full control, more code
- **WinUI 3** — C#/C++ · Windows · current Windows App SDK UI layer
- **GTK 4 + libadwaita** — C/Rust/Python · Linux · GNOME's own look; Rust via Relm4 · https://relm4.org
- **Haiku Interface Kit** — C++ · Haiku OS · BeOS-lineage API; Haiku R1 still beta · https://www.haiku-os.org/docs/api/

## 2. Cross-platform native-widget wrapper — S C
- **wxWidgets** — C++ (wxPython) · Win/Mac/Linux · wraps real native controls since 1992
- **React Native for Windows + macOS** — JS/TS · Microsoft-maintained; React components → native controls · https://microsoft.github.io/react-native-windows/
- **.NET MAUI** — C# · Windows, Mac (Catalyst), iOS, Android · native controls
- **BeeWare Toga** — Python · native widgets per OS, mobile too · https://beeware.org/project/projects/libraries/toga/
- **IUP** — C/Lua · PUC-Rio's tiny native toolkit, from Lua's home · https://www.tecgraf.puc-rio.br/iup/

## 3. Self-drawn / GPU cross-platform GUI — S C
- **Qt / QML** — C++ or Python (PySide6) · industry default; paints its own widgets
- **Flutter desktop** — Dart · Impeller/Skia renderer, same pixels everywhere
- **iced** — Rust · Elm architecture on wgpu; System76 COSMIC desktop uses it
- **Avalonia** — C#/XAML · WPF-style successor, own renderer on every OS
- **Makepad** — Rust · shader-drawn UI, design DSL edited live · https://makepad.dev

## 4. Immediate-mode GUI — S C
- **Dear ImGui** — C++ · default for game and debug tools
- **egui** — Rust · pure Rust; native and web via WASM
- **Gio** — Go · immediate-mode GUI for Go, desktop and mobile · https://gioui.org
- **Nuklear** — C · single-header ANSI C, no dependencies · https://github.com/Immediate-Mode-UI/Nuklear
- **Clay** — C · layout library; declare tree each frame, any renderer · https://github.com/nicbarker/clay

## 5. Game engine as GUI toolkit — W
- **Godot** — GDScript/C# · Pixelorama, Material Maker; low-processor mode for apps
- **Unity UI Toolkit** — C# · UXML/USS UI for apps and editor tools
- **Unreal Slate** — C++ · the whole Unreal Editor is drawn with it · https://dev.epicgames.com/documentation/en-us/unreal-engine/slate-user-interface-programming-framework-for-unreal-engine
- **Bevy (bevy_ui)** — Rust · ECS engine, UI nodes are entities; pre-1.0
- **LÖVE** — Lua · 2D loop; draw any custom UI yourself

## 6. Bundled-browser shell (Electron-style) — S C
- **Electron** — JS/TS · Chromium + Node; VS Code, Slack, Discord
- **NW.js** — JS · older rival; DOM and Node share one context
- **CEF** — C++ · embed Chromium in any native app; Spotify desktop · https://bitbucket.org/chromiumembedded/cef
- **Ultralight** — C++ · lightweight WebKit-based GPU HTML renderer for apps, games · https://ultralig.ht
- **Sciter** — C++/JS · own tiny HTML/CSS engine, not Chromium; antivirus UIs · https://sciter.com

## 7. System-webview shell (Tauri-style) — S C N
- **Tauri 2** — Rust · OS webview, small binaries; iOS/Android too
- **Wails** — Go · Go backend, system webview frontend
- **pywebview** — Python · one call opens a native webview window
- **Electrobun** — TypeScript/Bun · Zig core, ~1 MB hello world; Chromium optional · https://electrobun.dev
- **Lorca** — Go · drives your installed Chrome over DevTools; dormant since Aug 2024 · https://github.com/zserge/lorca

## 8. RAD visual form designer — C
- **WinForms designer (Visual Studio)** — C#/VB.NET · Windows · drag controls, double-click for handler
- **Delphi (RAD Studio)** — Object Pascal · VCL/FireMonkey; commercial, free Community edition
- **Lazarus** — Free Pascal · open-source Delphi-alike, Win/Mac/Linux · https://www.lazarus-ide.org
- **Xojo** — Xojo (VB-like) · desktop, web, iOS from one designer; paid · https://xojo.com
- **Decker** — Lil · HyperCard revived: cards, widgets, scripts; web + native · https://beyondloom.com/decker/

## 9. Shared core + native shells — C
- **Kotlin Multiplatform** — Kotlin · shared logic; SwiftUI and Compose shells
- **Crux** — Rust · core as pure functions; Swift/Kotlin/TS shells · https://github.com/redbadger/crux
- **UniFFI** — Rust · Mozilla's binding generator; Firefox mobile uses it · https://github.com/mozilla/uniffi-rs
- **Djinni** — C++ IDL · Dropbox original archived 2020; Snapchat fork active · https://github.com/Snapchat/djinni
- **gomobile bind** — Go · Go core as iOS/Android library; experimental · https://pkg.go.dev/golang.org/x/mobile/cmd/gomobile

## 10. Menu bar / tray utility — S C W N
- **SwiftUI MenuBarExtra** — Swift · macOS 13+ native menu-bar scene
- **rumps** — Python · "Ridiculously Uncomplicated macOS Python Statusbar apps" · https://github.com/jaredks/rumps
- **SwiftBar** — any script · stdout becomes a live menu-bar item · https://swiftbar.app
- **tray-icon** — Rust · Tauri's cross-platform tray crate · https://github.com/tauri-apps/tray-icon
- **Raycast MenuBarExtra** — React/TS · menu-bar command hosted inside Raycast

## 11. Notch app — W
- **DynamicNotchKit** — Swift package · drop SwiftUI views into the notch · https://github.com/MrKai77/DynamicNotchKit
- **boring.notch** — SwiftUI · open-source Dynamic Island: media, shelf, HUD · https://github.com/TheBoredTeam/boring.notch
- **NotchNook** — macOS · commercial notch shelf and widgets · https://lo.cafe/notchnook
- **Notchmeister** — macOS · Iconfactory toy: playful effects around the notch · https://apps.apple.com/us/app/notchmeister/id1599169747
- **TopNotch** — macOS · the opposite: hides the notch; CleanShot team · https://topnotch.app

## 12. Summon-anywhere command (launcher, hotkey palette) — S C N
- **Raycast extensions** — React/TS · store of thousands of community commands
- **Alfred workflows** — any script · classic Mac launcher; Powerpack paid
- **Hammerspoon** — Lua · hotkeys, chooser palette, any OS event · https://www.hammerspoon.org
- **PowerToys Command Palette** — C#/.NET · Windows launcher with extensions · https://learn.microsoft.com/en-us/windows/powertoys/command-palette/overview
- **dmenu** — C/X11 · list on stdin, your pick on stdout · https://tools.suckless.org/dmenu/

## 13. Desktop widget / glanceable — S C
- **WidgetKit** — Swift · macOS desktop + iOS home/lock-screen widgets
- **Übersicht** — JSX + shell · HTML widgets on the Mac desktop · https://github.com/felixhageloh/uebersicht
- **Rainmeter** — INI/Lua · Windows desktop skins and meters
- **Conky** — Lua config · Linux system stats drawn on desktop · https://github.com/brndnmtthws/conky
- **Plash** — macOS · any website as your live wallpaper · https://github.com/sindresorhus/Plash

## 14. Desktop pet / cursor-side buddy — W I
- **oneko** — C/X11 · 1980s cat chasing your cursor; web port · https://github.com/adryd325/oneko.js
- **Shimeji-ee** — Java · Windows · climbing mascots, any artist's sprite set · https://kilkakon.com/shimeji/
- **Desktop Goose** — Windows/macOS · goose drags memes, steals your cursor · https://samperson.itch.io/desktop-goose
- **Bongo Cat** — Steam · cat punches your taskbar on every keypress · https://store.steampowered.com/app/3419430/Bongo_Cat/
- **OpenPets** — Swift · macOS · one pet showing agent progress via MCP/CLI · https://github.com/alterhq/openpets

## 15. Ambient juice layer over work — N
- **Claude Code hooks + afplay** — JSON hooks → shell · play a sound on Stop/Notification
- **peon-ping** — shell hooks · Warcraft III Peon voice when agents finish · https://github.com/PeonPing/peon-ping
- **Mechvibes** — Rust + Dioxus · mechanical-keyboard sound for every keystroke · https://github.com/hainguyents13/mechvibes
- **Ridiculous Coding** — Godot 4 addon · screenshake and explosions while you type · https://github.com/jotson/ridiculous_coding
- **NSHapticFeedbackManager** — Swift/AppKit · trackpad haptic tap from code; finger must touch

## 16. Home-cooked tool for one / own-it replacement for a paid product — W I
- **Docker Compose + awesome-selfhosted** — YAML · `docker compose up` a listed replacement · https://github.com/awesome-selfhosted/awesome-selfhosted
- **Coolify** — Docker · self-hosted Heroku/Vercel on your own box · https://coolify.io
- **Umbrel** — home-server OS · one-click app store for self-hosting · https://umbrel.com
- **Pinokio** — "AI browser" · one-click install of local AI apps · https://pinokio.co
- **BoopSnoop** — Swift/iOS · Robin Sloan's 4-person family messenger, never released · https://www.robinsloan.com/notes/home-cooked-app/

## 17. Kiosk / single-app locked device (incl. kid-proof) — S I N
- **Guided Access** — iOS/iPadOS · built-in: triple-click locks to one app · https://support.apple.com/en-us/111795
- **Android Lock Task mode** — Kotlin · device-owner kiosk pinning one app · https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode
- **NSApplication.PresentationOptions** — Swift/AppKit · hide Dock, block ⌘-Tab: Mac kiosk · https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct
- **FullPageOS** — Raspberry Pi distro · boots straight into fullscreen Chromium · https://github.com/guysoft/FullPageOS
- **BabySmash!** — C#/WPF · Windows · Hanselman's toddler keyboard-mashing game · https://github.com/shanselman/babysmash

## 18. Whole OS as the product (distro) — I
- **Omarchy** — Arch + Hyprland · DHH's opinionated setup as bootable ISO · https://omarchy.org
- **NixOS** — Nix · whole OS declared in one config file
- **Universal Blue (bootc)** — Containerfile · OS built as container image; Bazzite · https://universal-blue.org
- **Redox OS** — Rust · microkernel OS from scratch; pre-1.0 · https://www.redox-os.org
- **TempleOS** — HolyC · one man's 640×480 OS; unmaintained since 2018 · https://templeos.org

## 19. Boot-sector app — W
- **NASM + QEMU** — x86 asm · plain route: assemble 512 bytes, boot emulator
- **BootMine** — x86 asm · Minesweeper in a 512-byte boot sector · https://github.com/io12/BootMine
- **bootOS** — x86 asm · whole OS in 512 bytes (nanochess) · https://github.com/nanochess/bootOS
- **sectorlisp** — x86 asm · LISP interpreter in a boot sector · https://github.com/jart/sectorlisp
- **uefi-rs** — Rust · modern firmware app: no OS, no 512-byte cap · https://github.com/rust-osdev/uefi-rs

# Batch 2 — Terminal, files, scripts, services

## 20. One-shot CLI — S C N
- **getopts in a bash script** — POSIX shell · zero dependencies; the plain default
- **Typer** — Python · type hints become arguments and `--help`
- **clap** — Rust · derive macros; ships as one static binary
- **Cobra** — Go · subcommand trees behind kubectl, gh, Hugo
- **docopt** — Python + ports · write the help text; it becomes the parser · original frozen since 2014, fork docopt-ng active · http://docopt.org

## 21. Prompt wizard / REPL / one-paste installer — S C N
- **bash `read` + `select`** — shell builtins · ask, then pick from a numbered menu
- **gum** — Go binary (Charm) · pretty prompts, pickers, spinners for any shell script · https://github.com/charmbracelet/gum
- **prompt_toolkit** — Python · line-editing REPL engine behind IPython and ptpython
- **brew bundle** — Homebrew · one Brewfile installs a whole Mac · tap merged into brew core, 2025
- **expect** — Tcl · scripts the human side of someone else's wizard · https://en.wikipedia.org/wiki/Expect

## 22. Full-screen TUI — S C N
- **ncurses** — C · the old screen library nearly everything sits on
- **Ratatui** — Rust · immediate-mode widgets; successor of tui-rs
- **Textual** — Python · CSS-styled widgets; same app can serve to a browser
- **Ink** — Node / React · React components rendered to the terminal; Gemini CLI uses a fork
- **Notcurses** — C · bitmaps, video and true colour inside the terminal · https://github.com/dankamongmen/notcurses

## 23. SSH-served app — S W
- **OpenSSH `ForceCommand`** — sshd config · each login runs one program; no framework at all
- **Wish + Bubble Tea** — Go (Charm) · SSH middleware plus Elm-style TUI; powers terminal.shop · https://github.com/charmbracelet/wish
- **russh** — Rust · async SSH server and client library · https://github.com/Eugeny/russh
- **pico.sh** — SSH services · publish blog, pastes, sites with plain scp/rsync · https://pico.sh
- **ENiGMA½** — Node.js · a 90s-style BBS you reach over SSH · https://github.com/NuSkooler/enigma-bbs

## 24. Agent-first CLI (made for agents to call) — W
- **GitHub CLI `--json`** — Go · `--json fields --jq` makes a human CLI agent-readable
- **gws (Google Workspace CLI)** — Rust · every Workspace API, JSON-only output, built-in MCP mode · not an official Google product, pre-1.0 · https://github.com/googleworkspace/cli
- **agent-browser** — Rust (Vercel Labs) · headless browser driven by accessibility-tree refs · https://github.com/vercel-labs/agent-browser
- **mcporter** — TypeScript · turns any MCP server into a standalone CLI · https://github.com/openclaw/mcporter
- **jc** — Python · converts output of 100+ classic commands to JSON · https://github.com/kellyjonbrazil/jc

## 25. Plain file as the app (Markdown/outline is data and UI) — N
- **todo.txt** — plain-text format · one task per line; the format is the app · http://todotxt.org
- **Org mode** — Emacs · one outline is tasks, agenda, tables, runnable code
- **Obsidian Bases** — Obsidian core plugin · database views over Markdown frontmatter
- **hledger** — Haskell · plain-text accounting; the journal file is the books · https://hledger.org
- **Potluck** — web (Ink & Switch) · plain text notes grow live computed fields · research prototype, 2022, public demo · https://www.inkandswitch.com/potluck/

## 26. Spreadsheet / hosted table as the app — S C W N
- **Google Sheets + Apps Script** — Google cloud · sheet is the DB; script adds menus, triggers, web app
- **Airtable** — hosted · relational base with interfaces, forms, automations
- **Notion databases** — hosted · linked tables with filtered views and relations
- **Grist** — TypeScript + Python · open-source relational sheet, Python formulas, self-hostable · https://www.getgrist.com
- **Excel LAMBDA** — Microsoft Excel · formulas define named recursive functions; the sheet as language

## 27. Notebook — S
- **Jupyter** — Python + 40-odd kernels · `.ipynb` cells; the default everyone opens
- **marimo** — Python · reactive cells, saved as `.py`, runs as an app · https://marimo.io
- **Observable Notebooks 2.0** — JavaScript · reactive cells; Mac desktop app, open file format · technology preview · https://github.com/observablehq/notebook-kit
- **Livebook** — Elixir · collaborative, Smart cells, deploys a notebook as an app · https://livebook.dev
- **Glamorous Toolkit** — Pharo Smalltalk · moldable environment: every object gets its own views · https://gtoolkit.com

## 28. OS automation recipe (Shortcuts, AppleScript) — S C I N
- **AppleScript / JXA via `osascript`** — macOS · drives any scriptable app; the 1993 default
- **Apple Shortcuts** — iOS / macOS · action blocks fired by tap, time, SMS, NFC
- **Hammerspoon** — Lua on macOS · hotkeys, window and Wi-Fi events run scripts
- **AutoHotkey** — Windows · hotkeys, text expansion, GUI macros in one script
- **Talon** — Python config · voice, mouth noises and eye tracking drive the OS · https://talonvoice.com

## 29. Visual workflow automation (n8n-style) — S C N
- **IFTTT** — hosted · one trigger, one action; the simplest possible recipe
- **Zapier** — hosted · trigger→action chains across thousands of web apps
- **n8n** — TypeScript, self-hostable · node canvas with code nodes; fair-code licence
- **Node-RED** — Node.js · flow wiring for IoT, MQTT and local devices
- **Huginn** — Ruby, self-hosted · agents watch the web, then act; since 2013 · https://github.com/huginn/huginn

## 30. Scheduled background job / daemon — S N
- **cron** — Unix · one crontab line; silently skips runs missed asleep
- **launchd** — macOS · plist jobs; missed calendar runs fire on wake
- **systemd timers** — Linux · `Persistent=true` catches up runs missed while off
- **Temporal** — Go / Java / TS / Python SDKs · durable workflows resume after crashes, retries built in
- **Claude Code routines** — Anthropic cloud · scheduled agent sessions; your laptop can be off · research preview since Apr 2026

## 31. Trigger-only / serverless / edge function — S W
- **CGI script** — any language + web server · one process per request; serverless since 1993
- **AWS Lambda** — many runtimes · the 2014 function-as-a-service default
- **Cloudflare Workers** — JS / TS / WASM · V8 isolates at the edge; near-zero cold start
- **Val Town** — TypeScript · browser-edited functions fired by HTTP, cron, email · https://www.val.town
- **Spin** — Rust / Go / JS → WebAssembly · each handler is a sandboxed Wasm component · CNCF; Fermyon bought by Akamai, Dec 2025 · https://github.com/spinframework/spin

## 32. Headless API / library / MCP server (users are code or agents) — S I N W
- **Plain package (PyPI / npm / crates.io)** — any language · `import` it; no server, no UI
- **FastAPI** — Python · type hints give a validated JSON API and OpenAPI docs
- **FastMCP** — Python · decorated functions become MCP tools for agents · https://github.com/PrefectHQ/fastmcp
- **gRPC** — protobuf, many languages · contract-first typed calls between services
- **PostgREST** — Haskell · a Postgres schema becomes a REST API, no code · https://postgrest.org

## 33. Git-forge app (README, Issues, Actions are the app) — W
- **Issue forms + GitHub Actions** — YAML · filed issue triggers a workflow that commits the result
- **Upptime** — GitHub Actions · uptime monitor and status page running entirely on GitHub · https://upptime.js.org
- **Git scraping** — Actions cron · scheduled scrape commits diffs; repo history is the database · https://simonwillison.net/2020/Oct/9/git-scraping/
- **giscus** — GitHub Discussions · blog comments stored as repo discussions · https://giscus.app
- **timburgan community chess** — profile README · one public chess game, moves made by opening issues · https://github.com/timburgan/timburgan

## 34. Smart contract + dApp — S
- **Remix IDE** — browser, Solidity · write, compile, deploy a contract from one tab · https://remix.ethereum.org
- **Solidity + Foundry** — Rust toolchain · EVM contracts tested in Solidity itself · https://github.com/foundry-rs/foundry
- **Anchor** — Rust · Solana program framework with generated typed clients
- **wagmi + viem** — TypeScript / React · wallet connection and contract calls for the front end · https://wagmi.sh
- **Cairo** — Starknet · programs whose every run is provable by STARK proof · https://www.cairo-lang.org

## 35. Live instrument console (hardware data → gauges, rolling plots) — N
- **Arduino Serial Plotter** — Arduino IDE · print numbers over serial, get live lines
- **LabVIEW** — NI graphical language · wire a front panel of gauges to instruments · free Community Edition
- **Rerun** — Rust core, Python / C++ / Rust SDKs · log sensor streams, scrub the timeline live · https://rerun.io
- **ttyplot** — C · pipe numbers into stdin, get a rolling terminal plot · https://github.com/tenox7/ttyplot
- **phyphox** — iOS / Android · phone sensors become a lab instrument, viewable remotely · https://phyphox.org

---
Checked: GitHub API (not archived, recent push) for huginn, jc, notcurses, ttyplot, docopt and docopt-ng, timburgan, upptime, textual, ink, rerun, phyphox, mcporter (moved to openclaw), agent-browser, gws, grist-core, gtoolkit, livebook, notebook-kit, enigma-bbs, wish, russh, pico, fastmcp (moved to PrefectHQ), postgrest, wagmi, foundry, cairo, gum. Web/official pages: gws status, Claude Code routines preview, Fermyon→Akamai, Spin repo move, brew bundle merge, Gemini CLI's Ink fork, Potluck demo, Notebooks 2.0 preview. Not checked this session (search budget ran out; written from known facts): Talon, Obsidian Bases, hledger, Excel LAMBDA, LabVIEW Community Edition, launchd/systemd catch-up behaviour.

# Batch 3 — Web

## 36. Static site — S C
- **Plain HTML on GitHub Pages** — HTML/CSS · no generator, no build; push files, done
- **Hugo** — Go · single binary, builds thousands of pages per second
- **Astro** — JS/TS · content collections; zero JS unless an island opts in
- **Zola** — Rust · one binary, Tera templates, batteries included · https://www.getzola.org
- **Pollen** — Racket · the book is a program; markup is code · https://docs.racket-lang.org/pollen/

## 37. Client-rendered SPA — S C
- **React + Vite** — JS/TS · the default; one bundle, JSON API behind
- **Vue 3** — JS/TS · templates plus reactivity; gentlest big-framework learning curve
- **Svelte 5** — JS/TS · a compiler, no virtual DOM; runes for state
- **Elm** — Elm · pure functional, no runtime exceptions; last release 0.19.1 (2019)
- **VanJS** — JS · ~1 kB, no JSX, no build step · https://vanjs.org

## 38. Full-stack meta-framework — C
- **Next.js** — React · the default; server components, Vercel-native
- **Nuxt** — Vue · Next.js counterpart for Vue; file-based everything
- **SvelteKit** — Svelte · loaders and form actions; adapters for any host
- **Qwik City** — TS · resumable: no hydration, JS loads on interaction; v2 beta
- **Wasp** — Wasp DSL + React/Node · one config file declares auth, routes, jobs; pre-1.0 · https://wasp.sh

## 39. Server-rendered MVC monolith — C
- **Ruby on Rails** — Ruby · the archetype; one person ships a whole product
- **Django** — Python · free admin panel; ORM, auth, templates included
- **Laravel** — PHP · biggest PHP ecosystem; queues, auth, billing first-party
- **Loco** — Rust · Rails conventions for Rust, on Axum + SeaORM · https://loco.rs
- **Seaside** — Smalltalk (Pharo) · continuations, no templates; pages are live objects · https://github.com/SeasideSt/Seaside

## 40. HTML-over-the-wire / hypermedia — S C
- **htmx** — any backend · HTML attributes swap server-sent fragments; no build
- **Hotwire (Turbo + Stimulus)** — Rails / any · Rails default; Hotwire Native wraps it for mobile
- **Phoenix LiveView** — Elixir · server holds state, pushes DOM diffs over WebSocket
- **Blazor Server** — C# / .NET · C# components on server; UI diffs over SignalR
- **Datastar** — any backend · signals plus SSE streams from server; v1.0 out · https://data-star.dev

## 41. Script → web UI (Streamlit-style) — S C
- **Streamlit** — Python · the default; script reruns top-to-bottom on every click
- **Gradio** — Python · function in, function out; ML demos on Hugging Face Spaces
- **NiceGUI** — Python · event-driven widgets on Vue/Quasar; state survives clicks
- **Shiny** — R / Python · reactive graph; re-runs only what changed
- **PyWebIO** — Python · input()/put_text() script becomes a page; quiet since Oct 2023 · https://github.com/pywebio/PyWebIO

## 42. Installable PWA — S C N
- **Web App Manifest + hand-written service worker** — browser standard · plain default; Safari → Share → Add to Home Screen
- **Workbox** — JS (Google) · caching strategies and precaching as a library
- **vite-plugin-pwa** — Vite · zero-config manifest and service worker from your build
- **PWABuilder** — Microsoft · store packages (Windows, Android, iOS) from a URL · https://www.pwabuilder.com
- **Bubblewrap** — CLI (Chrome Labs) · wraps a PWA as Trusted Web Activity for Play · https://github.com/GoogleChromeLabs/bubblewrap

## 43. WASM-compiled app — S C
- **Leptos** — Rust · fine-grained signals; SSR with hydration or pure CSR
- **Blazor WebAssembly** — C# / .NET · .NET runtime in the browser; Razor components
- **PyScript** — Python (Pyodide / MicroPython) · `<script type="py">` inside plain HTML · https://pyscript.net
- **Flutter web (Wasm)** — Dart · self-drawn canvas UI; same code as the mobile app
- **Compose Multiplatform for web** — Kotlin/Wasm · Android's Compose UI in the browser; beta since Sep 2025

## 44. Canvas / GPU / 3D web scene — S I N
- **Canvas 2D API** — browser built-in · no library; requestAnimationFrame plus draw calls
- **Three.js (+ React Three Fiber)** — JS · the default 3D: scenes, GLTF, shaders, WebGPU renderer
- **PixiJS** — JS · fast 2D WebGL/WebGPU sprites, filters, particles
- **Spline** — no-code 3D editor · design in the editor, embed with one link · https://spline.design
- **Spark** — JS on three.js (World Labs) · Gaussian-splat scans rendered alongside ordinary meshes · https://sparkjs.dev

## 45. Embeddable widget — S
- **iframe + postMessage** — browser standard · plain default; isolated, talks to host by messages
- **Lit** — JS web components · a custom element drops into any site or framework
- **zoid** — JS (PayPal krakenjs) · cross-domain iframe components with props and callbacks · https://github.com/krakenjs/zoid
- **oEmbed provider** — open spec · paste your URL; WordPress, Discourse embed it themselves · https://oembed.com
- **github-readme-stats** — Node on Vercel · the widget is just an SVG image URL · https://github.com/anuraghazra/github-readme-stats

## 46. Single-file HTML tool / artifact shared by link — C W I N
- **Plain .html + CDN ES modules** — HTML/JS · one file importing from esm.sh; state in URL
- **Alpine.js** — JS · behaviour in HTML attributes; one script tag, no build
- **Claude Artifacts** — claude.ai · AI writes the page; private link to share
- **TiddlyWiki** — JS · a wiki that saves itself back into one file · https://tiddlywiki.com
- **vite-plugin-singlefile** — Vite · inlines any built app into one .html · https://github.com/richardtallent/vite-plugin-singlefile

## 47. Whole OS in one HTML file — W
- **WebContainers** — StackBlitz · Node.js and npm running inside a browser tab
- **v86** — Rust → Wasm · x86 emulator; boots Linux, Windows 98 in a tab · https://copy.sh/v86/
- **JSLinux** — C → Wasm (Fabrice Bellard) · emulated Linux and Windows, by QEMU's author · https://bellard.org/jslinux/
- **Puter** — JS · open-source "internet OS" desktop, self-hostable · https://github.com/HeyPuter/puter
- **Shiro** — TypeScript · 420 KB file: shell, git, npm; commands reimplemented, no kernel · https://shiro.computer

## 48. App in a link or QR code — W
- **data: URL** — browser built-in · `data:text/html,…`: the link is the page
- **itty.bitty.site** — JS · whole site compressed into the URL fragment · https://itty.bitty.site
- **textarea.my** — HTML/JS (Anton Medvedev) · editor saved in the URL hash; /qr makes a QR code · https://textarea.my
- **urlpages** — JS (jstrieb) · write HTML, get a URL that is the page · https://github.com/jstrieb/urlpages
- **Snake in a QR code** — Windows x86 binary (MattKC) · a runnable game packed into one QR code · https://mattkc.com/etc/snakeqr/

## 49. Multi-tab app (tabs talk to each other) — I
- **BroadcastChannel API** — browser standard · plain default; same-origin tabs publish and subscribe
- **SharedWorker** — browser standard · one worker and one socket shared by every tab
- **broadcast-channel (npm)** — JS (pubkey) · cross-tab messaging plus leader election · https://github.com/pubkey/broadcast-channel
- **Window Management API** — Chromium · code places windows across several screens
- **multipleWindow3dScene** — three.js + localStorage · one 3D scene spanning several windows · https://github.com/bgstaal/multipleWindow3dScene

## 50. Agent-readable site (llms.txt) — I
- **robots.txt + sitemap.xml** — web standard · the "no innovation" option crawlers already read
- **schema.org JSON-LD** — structured data · typed facts about businesses, products and events
- **llms.txt** — Markdown file · curated site summary and links for LLMs · https://llmstxt.org
- **NLWeb** — Python (Microsoft) · site answers natural-language queries; doubles as MCP server · https://github.com/microsoft/NLWeb
- **WebMCP** — browser API (Chrome) · page exposes tools to agents; Canary flag, experimental

## 51. Full-stack SaaS from a starter template — I N
- **create-t3-app** — TS (Next.js, tRPC, Prisma) · free, modular, type-safe default scaffold · https://create.t3.gg
- **ShipFast** — Next.js · paid indie-hacker boilerplate: auth, Stripe, emails, SEO
- **SaaS Pegasus** — Django · paid; teams, billing, Celery already wired · https://www.saaspegasus.com
- **Open SaaS** — Wasp (React + Node) · free; Stripe, admin, blog, AI example · https://opensaas.sh
- **Better-T-Stack** — TS CLI · pick the parts (Hono/Convex, React/Expo), then scaffold · https://better-t-stack.dev

## 52. Self-hosted on my own machine (tailnet / tunnel, no deploy) — I N
- **python -m http.server + launchd** — Python / macOS · plain default; an always-on page on my Mac
- **Tailscale Serve / Funnel** — Tailscale · HTTPS inside the tailnet, or Funnel for public
- **Cloudflare Tunnel** — cloudflared · outbound tunnel to your domain, no open ports
- **VS Code port forwarding (dev tunnels)** — VS Code · Ports tab gives a shareable URL in seconds
- **localhost.run** — plain SSH · `ssh -R` gives a public URL; nothing to install · https://localhost.run

## 53. Publish pipeline: one note → site, newsletter, channels — N
- **Quartz** — TS · Obsidian vault becomes a static digital-garden site · https://quartz.jzhao.xyz
- **Ghost** — Node · blog, newsletter and paid members in one
- **Buttondown** — hosted · Markdown newsletter with API; RSS-to-email · https://buttondown.com
- **Postiz** — TS, AGPL · self-hosted scheduler: X, Bluesky, Mastodon, LinkedIn, Threads · https://github.com/gitroomhq/postiz-app
- **Micro.blog** — hosted · POSSE: post once, cross-posts to Bluesky, Mastodon and more · https://micro.blog

## 54. Copy-paste component & effect registry — I
- **shadcn/ui** — React + Tailwind · the registry pattern: CLI copies source in · https://ui.shadcn.com
- **Aceternity UI** — React + Motion · flashy animated sections, ready to paste · https://ui.aceternity.com
- **React Bits** — React · animated text and backgrounds; install via shadcn or jsrepo · https://reactbits.dev
- **21st.dev** — community registry · shadcn-format marketplace; Magic MCP for agents · https://21st.dev
- **Uiverse** — HTML/CSS · community elements, no framework; copy the CSS · https://uiverse.io

## 55. Reference-cloned design — I
- **awesome-design-md** — Markdown (VoltAgent) · DESIGN.md files (Stitch format) extracted from famous sites · https://github.com/VoltAgent/awesome-design-md
- **screenshot-to-code** — Python/React (abi) · screenshot in, HTML/Tailwind/React out · https://github.com/abi/screenshot-to-code
- **html.to.design** — Figma plugin · any URL becomes editable Figma layers · https://html.to.design
- **Open Lovable** — TS (Firecrawl) · paste a URL, get a React clone · https://github.com/firecrawl/open-lovable
- **Same** — hosted · AI clones a live site's UI into code · https://same.new

## 56. Fake-door landing page (complaint-mined) — I
- **Carrd** — hosted · cheap one-page sites in minutes · https://carrd.co
- **Framer** — hosted · designer-grade landing pages; AI first draft
- **Tally** — hosted · free unlimited forms; the waitlist behind the button · https://tally.so
- **F5Bot** — free email alerts · Reddit and Hacker News keyword mentions to your inbox · https://f5bot.com
- **GummySearch** — hosted · Reddit complaint mining; **closed**, data deleted 1 Dec 2026 · https://gummysearch.com

## 57. Infinite canvas board — N
- **JSON Canvas** — open file format (Obsidian) · plain .canvas JSON: nodes, edges, groups · https://jsoncanvas.org
- **tldraw SDK** — React · embeddable whiteboard engine; source-available licence · https://tldraw.dev
- **Excalidraw** — React · hand-drawn look; embeddable, MIT
- **React Flow (xyflow)** — React / Svelte · node-and-edge graph canvas
- **Kinopio** — Vue · spatial-thinking web app; client code source-available · https://kinopio.club

# Batch 4 — Browser, mobile, messengers, hosts

## 58. Browser extension (incl. bridged to an agent) — S C I N
- **Plain Manifest V3** — JS · Chrome/Firefox/Edge · manifest.json plus content script; no build step
- **WXT** — TypeScript/Vite · current default framework; cross-browser, hot reload · https://wxt.dev
- **Plasmo** — TypeScript/React · stalled: last commit 17 May 2025 · https://github.com/PlasmoHQ/plasmo
- **Safari Web Extension** — JS inside a Swift app · Xcode converter; also runs in iPhone Safari
- **Browser MCP** — extension + MCP server · Claude/Cursor drive your logged-in Chrome · https://browsermcp.io

## 59. Userscript / bookmarklet / in-page layer on someone else's site — S C I N
- **Bookmarklet** — `javascript:` URL · zero install; drag to bookmarks bar, click on page
- **Tampermonkey** — JS userscript manager · `// ==UserScript==` header; `@match` picks the sites
- **vite-plugin-monkey** — TypeScript/Vite · npm packages and HMR, bundled into one .user.js · https://github.com/lisonge/vite-plugin-monkey
- **Stylus** — user CSS · restyle any site with zero JavaScript · https://github.com/openstyles/stylus
- **page-agent** — TypeScript · Alibaba; one script tag adds a natural-language GUI agent · https://github.com/alibaba/page-agent

## 60. Native mobile app — S C I
- **SwiftUI** — Swift · iOS · Apple's default declarative UI
- **Jetpack Compose** — Kotlin · Android · Google's default declarative UI
- **UIKit** — Swift/Obj-C · iOS · the plain pre-SwiftUI way, still everywhere
- **Swift Playgrounds** — Swift · iPad · build and submit to the App Store, no Mac
- **NativeActivity** — C/C++ · Android NDK · whole app without a line of Java · https://developer.android.com/ndk/reference/group/native-activity

## 61. Cross-platform compiled mobile — S C
- **React Native + Expo** — TypeScript · popular pick; real native widgets, over-the-air updates
- **Flutter** — Dart · self-drawn widgets (Impeller); same pixels on every phone
- **Kotlin Multiplatform + Compose Multiplatform** — Kotlin · shared UI; iOS stable since 1.8.0, May 2025
- **Skip** — Swift · SwiftUI app runs on Android; free, open source since Jan 2026 · https://skip.dev
- **Lynx** — TypeScript/CSS · ByteDance's TikTok engine; dual-thread, open-sourced Mar 2025 · https://lynxjs.org

## 62. Hybrid webview mobile — S C
- **Capacitor + Ionic** — web · default wrapper; native plugin bridge, store builds
- **Hotwire Native** — any HTML server (Rails) · server pages inside native navigation · https://native.hotwired.dev
- **Tauri 2 mobile** — Rust + web · same Tauri app ships to iOS and Android
- **Bubblewrap** — PWA → Android · Trusted Web Activity: Play Store app, zero native code · https://github.com/GoogleChromeLabs/bubblewrap
- **Hyperview** — HXML via React Native · server sends XML screens, rendered native, no webview · https://hyperview.org

## 63. Phone home-screen widget as the main surface — W N
- **WidgetKit** — SwiftUI · iOS · the default; interactive buttons since iOS 17
- **Jetpack Glance** — Kotlin · Android · Compose-style API for home-screen widgets
- **Scriptable** — JavaScript · iOS · widget from a script, no App Store release · https://scriptable.app
- **KWGT** — no-code · Android · drag-and-drop widget designer with formulas · https://kustom.rocks
- **Nothing Essential Apps** — prompt → widget · beta since Feb 2026, Nothing Phone (3) only · https://essential-apps-beta.nothing.tech/guide

## 64. Super-app mini app (Telegram Mini App, WeChat) — S C W N
- **Telegram Mini Apps** — web + WebApp JS SDK · Telegram login, payments, haptics for free · https://core.telegram.org/bots/webapps
- **WeChat Mini Program** — WXML/WXSS/JS · own markup dialect; China's default app surface
- **Taro** — React/Vue · one codebase compiles to WeChat, Alipay, Douyin, web · https://github.com/NervJS/taro
- **Discord Activities** — web + Embedded App SDK · app runs inside a voice channel, shared live · https://discord.com/developers/docs/activities/overview
- **WhatsApp Flows** — JSON screens · native forms inside a WhatsApp chat, no webview · https://developers.facebook.com/docs/whatsapp/flows

## 65. Personal chat bot (1:1) — S C N
- **aiogram** — Python · Telegram · async default; botspot is built on it
- **grammY** — TypeScript · Telegram · runs on Deno, Bun, Cloudflare Workers · https://grammy.dev
- **WhatsApp Cloud API** — HTTP · Meta's official API; 24-hour reply window, paid templates
- **maubot** — Python · Matrix · plugin bot system on your own homeserver · https://github.com/maubot/maubot
- **BlueBubbles** — macOS server · iMessage bot through REST + webhooks; needs a Mac · https://bluebubbles.app

## 66. Bot inside other people's chats (group, guest, inline) — N
- **Telegram guest mode** — Bot API 10.0 · @mention a bot in any chat unadded (May 2026) · https://telegram.org/blog/ai-bot-revolution-11-new-features
- **Telegram inline mode** — Bot API · type `@bot query`, post the result into any chat
- **discord.js** — TypeScript · Discord · slash commands and server-wide bots
- **Slack Bolt** — JS/Python/Java · Slack · workspace app: slash commands, Block Kit buttons
- **Recall.ai** — API · bot joins Zoom/Meet/Teams calls as a participant · https://recall.ai

## 67. Userbot (acting as my own account) — N
- **Telethon** — Python · Telegram MTProto · default userbot library; full account access
- **Pyrogram** — Python · archived 23 Dec 2024; maintained fork is Kurigram · https://github.com/KurimuzonAkuma/kurigram
- **Baileys** — TypeScript · WhatsApp Web protocol · unofficial, so your number can be banned · https://github.com/WhiskeySockets/Baileys
- **Telegram Business bots** — Bot API · official: a bot answers your private chats (Premium)
- **mautrix bridges** — Go/Python · Matrix · one Matrix account puppets Telegram, WhatsApp, Signal · https://docs.mau.fi/bridges/

## 68. Email / SMS as the interface — S W N
- **Google Apps Script** — JS · Gmail · timed trigger reads, labels, replies; zero hosting
- **Cloudflare Email Workers** — JS · a Worker runs on every incoming email · https://developers.cloudflare.com/email-routing/email-workers/
- **AgentMail** — API · inboxes made for agents: send, receive, threads · https://www.agentmail.to
- **Twilio Messaging** — HTTP · SMS/WhatsApp · default SMS API with inbound webhook
- **SMS Gateway for Android** — Android app · your old phone becomes the SMS API · https://github.com/capcom6/android-sms-gateway

## 69. Voice-first / dial-in / smart-speaker app — S C W N
- **Alexa Skills Kit** — Node/Python/Java · custom skills only on classic Alexa; Alexa+ uses new APIs
- **Yandex Dialogs** — webhook · Alice skills; the Russian-language smart-speaker platform · https://dialogs.yandex.ru
- **Home Assistant Assist** — local · voice satellites control your home, no cloud needed · https://www.home-assistant.io/voice_control/
- **Pipecat** — Python · realtime speech → LLM → speech pipeline, mic or phone · https://github.com/pipecat-ai/pipecat
- **Twilio Voice (TwiML)** — XML over HTTP · dial-in phone number; works from a landline

## 70. One-card-at-a-time review queue — N
- **Telegram inline keyboards** — Bot API · one message per item, 2–5 callback buttons
- **Prodigy** — Python · Explosion · accept/reject/skip one example at a time; paid · https://prodi.gy
- **Label Studio** — Python/web · open-source labeling queue with hotkeys · https://labelstud.io
- **AnkiConnect** — Anki add-on · Anki schedules re-reviews; GitHub archived Nov 2025, moved to sourcehut · https://git.sr.ht/~foosoft/anki-connect
- **Swiper (cards effect)** — JS · swipeable card-stack web page · https://swiperjs.com

## 71. Daily digest (push report) — I N
- **launchd/cron + Telegram sendMessage** — any language · plainest: one script at 9:00, one message
- **React Email + Resend** — TypeScript · designed HTML email built from React components · https://react.email
- **Claude Code routines** — scheduled cloud agent · the agent researches and writes the brief
- **ChatGPT scheduled tasks** — OpenAI · replaced Pulse daily briefs (Pulse closed June 2026)
- **Huginn** — Ruby · self-hosted agents; Email Digest Agent batches events · https://github.com/huginn/huginn

## 72. Plugin inside a host app (editor, notes, Figma, Office) — S C W I N
- **VS Code extension API** — TypeScript · biggest editor ecosystem; also loads in Cursor
- **Obsidian plugin** — TypeScript · commands, views, CodeMirror widgets inside your notes
- **Figma plugin API** — TypeScript · sandboxed code plus iframe UI on the canvas
- **Office.js add-in** — JS · Excel/Word/Outlook sidebar, web and desktop
- **Emacs Lisp package** — Elisp · the editor is a Lisp VM; redefine anything live

## 73. Audio / creative-tool plugin (VST, Blender add-on) — S C
- **JUCE** — C++ · default framework for VST3/AU/AAX/LV2 plugins
- **nih-plug** — Rust · VST3 + CLAP; maintenance mode, framework fork on Codeberg · https://github.com/robbert-vdh/nih-plug
- **Blender extension** — Python (bpy) · add-ons via the extensions platform since 4.2
- **Photoshop UXP plugin** — JS/HTML · panels and scripts inside Photoshop · https://developer.adobe.com/photoshop/uxp/
- **Max for Live** — Max patching · devices built as patches inside Ableton Live

# Batch 5 — AI-native

## 74. Talking to an agent is the app (personal agent, messenger contact) — C W I N
- **aiogram + one LLM call** — Python, Telegram · no framework: bot forwards each message to a model
- **Claude Agent SDK** — Python/TS · Claude Code's agent loop as a library, behind any chat
- **Letta** (ex-MemGPT) — Python server · agents with persistent long-term memory, reached by API · letta.com
- **OpenClaw** (ex-Clawdbot) — TypeScript, self-hosted · one agent you text on WhatsApp, Telegram, iMessage · github.com/openclaw/openclaw
- **Poke** — iMessage / SMS / Telegram contact · first third-party agent in Apple Messages (Jun 2026) · poke.com

## 75. App inside AI chat (MCP Apps, Apps SDK) — S C W I
- **Custom GPTs** — ChatGPT, no code · instructions + files + actions; sold as "branded GPTs"
- **OpenAI Apps SDK** — TS/Python on MCP · interactive apps inside ChatGPT, listed in its directory
- **MCP Apps** (`@modelcontextprotocol/ext-apps`) — TS · official MCP extension (Jan 2026); HTML views render in-chat
- **Skybridge** — React/TS · one codebase for ChatGPT Apps and MCP Apps · github.com/alpic-ai/skybridge
- **Claude AI-powered artifacts** — HTML/React on claude.ai · shared app that calls Claude on the viewer's own quota

## 76. Agent skill folder as the app — W I N
- **AGENTS.md** — one Markdown file · the no-folder default every coding agent reads · agents.md
- **Claude Agent Skills** (SKILL.md) — Markdown + scripts · loaded when relevant; open standard, 30+ tools adopted
- **skills.sh** (`npx skills add`) — Vercel CLI + directory · installs any skill into your agent's folder · skills.sh
- **Superpowers** — skill pack · forces brainstorm → plan → TDD on the agent · github.com/obra/superpowers
- **Impeccable** — skill pack · design vocabulary and commands for frontend work · impeccable.style

## 77. Mod / hook / skin for an agent harness — I N
- **Claude Code hooks** — shell commands in settings · fire on SessionStart, PreToolUse, Stop and other events
- **Claude Code plugins** — marketplace · bundles of commands, subagents, hooks, skills, MCP servers
- **peon-ping** — shell hook · Warcraft peon voice line when the agent needs you · github.com/PeonPing/peon-ping
- **opcode** (ex-Claudia) — Tauri desktop · GUI skin over Claude Code sessions and agents · github.com/getAsterisk/opcode
- **Pi** — TypeScript harness · four tools; agent writes and hot-reloads its own extensions · pi.dev

## 78. Agent fleet / org chart / long-running build loop — I N
- **Ralph Wiggum loop** — one bash `while` loop · re-feed the same PROMPT.md until it's done · ghuntley.com/ralph
- **Claude Code subagents** — built in · subagents, `claude --worktree`, agent teams (experimental)
- **Conductor** — macOS app · parallel Claude Code / Codex chats in git worktrees · conductor.build
- **CrewAI** — Python · crews of agents with roles, goals, backstories
- **Gas Town** — Go · Mayor + disposable Polecats run 20–30 agents; successor Gas City · github.com/steveyegge/gastown

## 79. Agent-to-agent network (friends' agents trade updates) — N
- **Matrix** — open federated chat · each friend's agent is a bot in shared E2EE rooms
- **A2A protocol** — open spec, Linux Foundation · agent cards + tasks between agents of any vendor · a2a-protocol.org
- **AgentMail** — API · real inboxes for agents; agents email each other · agentmail.to
- **Moltbook** — web · agent-only Reddit, humans watch; Meta acquired (Mar 2026), future unclear
- **Nostr DVMs** (NIP-90, draft) — Nostr relays · agents post jobs, others answer, paid in Lightning · github.com/nostr-protocol/nips/blob/master/90.md

## 80. Persona council / simulated experts — I
- **Character.AI** — hosted · plain default: chat with one persona at a time
- **LLM Council** — Python + React, OpenRouter · models answer, rank each other blind, chairman decides · github.com/karpathy/llm-council (weekend hack, unsupported)
- **TinyTroupe** — Python, Microsoft · simulated personas run focus groups and market tests · github.com/microsoft/TinyTroupe
- **Delphi** — hosted · licensed AI clones of real experts and coaches · delphi.ai
- **Generative Agents** (Smallville) — Python research code · 25 simulated townspeople with memory, plans, gossip · github.com/joonspk-research/generative_agents

## 81. Middleware proxy between agent and model — I
- **LiteLLM Proxy** — Python · one OpenAI-style endpoint, 100+ providers, budgets, fallbacks
- **OpenRouter** — hosted · one key and one bill across hundreds of models
- **claude-code-router** — Node · sends Claude Code's turns to other models per task · github.com/musistudio/claude-code-router
- **RouteLLM** — Python, LMSYS · trained router sends easy prompts to cheap models · github.com/lm-sys/RouteLLM
- **Headroom** — Python/npm · `headroom wrap claude`: reversible context compression, claims 60–95% fewer tokens · github.com/headroomlabs-ai/headroom

## 82. Generated-per-click app — W
- **AI Dungeon** — web/mobile, since 2019 · the old version: story world generated per command
- **Websim** — web · type any URL or prompt; the site gets invented · websim.ai
- **Imagine with Claude** — claude.ai · each window written live as you click; 5-day preview, ended (Oct 2025)
- **Gemini dynamic view** — Gemini app · codes a custom interactive page per prompt; experiment (Nov 2025)

## 83. LLM as the backend — W
- **Magentic** — Python · `@prompt` functions: signature in, model returns the typed value · github.com/jackmpcollins/magentic
- **backend-GPT** — Python · catch-all route + JSON state; 2023 hackathon winner, inactive · github.com/TheAppleTucker/backend-GPT
- **nokode** — Node server · every HTTP request asks the model; SQL + HTML tools · github.com/samrolken/nokode
- **Infinite Craft** — web game · every never-seen pair asks an LLM, then cached forever · neal.fun/infinite-craft

## 84. Neural-rendered computer — W
- **NeuralOS** — research, 2025 · diffusion model draws an Ubuntu desktop from your clicks · arxiv.org/abs/2507.08800
- **DIAMOND** — Python, open source · diffusion world model; play CS:GO Dust II locally · github.com/eloialonso/diamond
- **Oasis** — Decart, open weights · real-time Minecraft-like world, no engine; browser demo · oasis.decart.ai
- **WHAMM Quake II** — Microsoft Copilot Labs · Quake II level running inside a model; 2-minute sessions (research demo)
- **Project Genie** (Genie 3) — Google DeepMind · prompt → walkable world; prototype, US AI Ultra only

## 85. Agent-composed native UI (generative UI) — W
- **AI SDK generative UI** — TS, Vercel · plain default: tool calls render your own React components
- **CopilotKit + AG-UI** — React/TS · agent↔frontend event protocol; shared state, in-app components
- **A2UI** — Google open spec, Apache 2.0, pre-1.0 · agent streams JSON; Flutter, Lit, Angular, React render it · a2ui.org
- **json-render** — TS, Vercel Labs · Zod catalog; model may only emit those components · github.com/vercel-labs/json-render
- **Thesys C1** — OpenAI-compatible API · model replies with live UI, not text; Crayon React kit · thesys.dev

## 86. Self-rewriting app — W
- **Pharo** — Smalltalk image · no-AI original: edit any class while the app runs · pharo.org
- **Self-rewriting server** — Node · users vote features; AI writes them into the running server · loop.circleci.com/i-built-a-server-that-rewrites-itself-while-running
- **Manifest** — Bun/TS · agent edits a file, Bun hot-reloads, next request runs it · github.com/HazAT/manifest
- **Agentity** — Python, LangChain · agent edits own source, lints, restarts with context; experimental · github.com/v0lka/agentity
- **Darwin Gödel Machine** — Python, research · coding agent rewrites itself; SWE-bench 20% → 50% · github.com/jennyzzt/dgm

## 87. Malleable software — W
- **Emacs** — Elisp · the 40-year default: redefine any command while it runs
- **Glamorous Toolkit** — Pharo, MIT · build a custom view for every object, live · gtoolkit.com
- **Decker** — Lil, web + native · HyperCard revived; stacks export as one HTML file · internet-janitor.itch.io/decker
- **Potluck** — Ink & Switch research demo · plain-text notes become apps through search patterns · inkandswitch.com/potluck
- **Patchwork** — Ink & Switch research (2024–26) · version control for malleable, shared tools; unreleased · inkandswitch.com

## 88. Prompt-to-app generator — C W
- **Lovable** — hosted, React + Supabase · chat → deployed full-stack web app
- **bolt.new** — StackBlitz WebContainers · whole Node stack builds inside your browser tab
- **v0** — Vercel · Next.js + shadcn apps, one click to deploy
- **Rork** — hosted · prompt → store-ready mobile app (React Native/Expo; Swift on Max) · rork.com
- **make real** — tldraw · draw a wireframe, get working HTML · makereal.tldraw.com

## 89. On-device / tiny edge model as the product — W I
- **llama.cpp** — C/C++ · plain default: GGUF models on any laptop CPU or GPU
- **Apple Foundation Models** — Swift, iOS/macOS 26 · free on-device ~3B model, no key, offline
- **Chrome Prompt API** — JS, Gemini Nano · stable in extensions; web pages through origin trial
- **Kitten TTS** — Python/ONNX · 15M-param English TTS, ~25 MB int8, CPU-only · github.com/KittenML/KittenTTS
- **Cactus Needle** — Python · 14–29 MB tool-calling model for phones, wearables, robots · github.com/cactus-compute/needle

## 90. Personal search over my own data / second brain — I N
- **SQLite FTS5** — C, inside SQLite · plain default: full-text index in one file
- **Dogsheep + Datasette** — Python · your tweets, photos, mail into SQLite; browse and query · dogsheep.github.io
- **Khoj** — Python, self-hostable · AI second brain over notes, docs and web · khoj.dev
- **Screenpipe** — Rust, local · records screen + audio 24/7; searchable; MCP server · screenpi.pe
- **OpenViking** — Python, ByteDance · agent memory as a `viking://` filesystem: ls, find · github.com/volcengine/OpenViking

## 91. Scheduled pipeline + self-rebuilding dashboard — I
- **GitHub Actions cron + Pages** — YAML · git scraping: scheduled commit, site rebuilds itself · simonwillison.net/2020/Oct/9/git-scraping/
- **Apify** — hosted scrapers · scheduled Actors fill datasets for the dashboard
- **Evidence** — SQL + Markdown · BI as code; dashboard rebuilt as a static site · evidence.dev
- **Observable Framework** — JS · data loaders run at build; static data app · observablehq.com/framework
- **Claude Code routines** — Anthropic cloud · scheduled agent rebuilds the dashboard, laptop closed; research preview

## 92. Node-graph / natural-language generation pipeline — W I
- **ComfyUI** — Python, local · node graph for image, video, audio model pipelines
- **Langflow** — Python · drag LLM/agent flows; each flow becomes an API
- **Rivet** — TS, Ironclad · visual graph IDE for LLM prompt chains · rivet.ironcladapp.com
- **Figma Weave** (ex-Weavy) — hosted · node canvas chaining image and video models; Figma-owned since late 2025
- **tldraw computer** — web, Gemini · plain-English blocks wired on a canvas; experimental · computer.tldraw.com

## 93. AI media workshop / content factory — I N
- **fal.ai** — API · plain default: hundreds of image, video, audio models, one key
- **Suno** — hosted · prompt or lyrics → finished song with vocals
- **Higgsfield** — hosted · AI video with cinematic camera-move presets
- **Opus Clip** — hosted · long video → captioned vertical shorts, ranked by hook
- **NotebookLM Overviews** — Google · your docs → two-host podcast or narrated video

---
Checked by web search on 6 Nov 2026: Poke, OpenClaw, Skybridge, Agent Skills standard, skills.sh, peon-ping, Pi, Gas Town, Conductor, Nostr DVMs, LLM Council, Headroom, Imagine with Claude, nokode, Project Genie, WHAMM, Oasis, Gemini dynamic view, Websim, backend-GPT, A2UI, json-render, Thesys C1, Agentity/Manifest/CircleCI server, Darwin Gödel Machine, Patchwork, Decker, Glamorous Toolkit, Rork, Chrome Prompt API, Kitten TTS, Cactus Needle, Screenpipe, OpenViking, Claude Code routines, tldraw computer, Figma Weave, Moltbook. The rest come from model knowledge up to June 2026 and were not re-checked (the search budget ran out). Uncertain: the canonical Headroom repo owner, and nokode's language.

# Batch 6 — Games, media, odd runtimes

## 94. Editor-centric game engine — S C N
- **Godot** — GDScript/C# · MIT, free; its own editor is a Godot app
- **Unity** — C# · most-used engine; 2023 runtime-fee plan cancelled 2024
- **Unreal Engine 5** — C++/Blueprints · AAA photoreal; 5% royalty past $1M revenue
- **Defold** — Lua · tiny builds, King-backed, free source-available licence · https://defold.com
- **UPBGE** — Python/logic nodes · Blender's game engine, revived as a fork · https://upbge.org

## 95. Code-first game framework / browser game or toy — S C N
- **Plain `<canvas>` + requestAnimationFrame** — JS/browser · no framework; one HTML file, open and play
- **Phaser** — JS/TS · default 2D browser game framework
- **raylib** — C · small no-editor library; bindings for dozens of languages
- **Bevy** — Rust · data-driven ECS engine, code only, still pre-1.0
- **LÖVE** — Lua · 2D framework; Balatro shipped on it

## 96. No-code game maker — C
- **GDevelop** — web/desktop · open source; event sheets instead of code
- **Construct 3** — browser · event-sheet editor runs in a tab; subscription
- **RPG Maker MZ** — desktop/JS · JRPG maps, events and battles from templates
- **Bitsy** — browser · tiny 8×8-tile story games made in minutes · https://ledoux.itch.io/bitsy
- **Rosebud AI** — browser · prompt a game; it writes Phaser/Three.js code · https://rosebud.ai

## 97. Fantasy console — S C W
- **PICO-8** — Lua · paid; 128×128, 16 colours, carts saved as PNGs
- **TIC-80** — Lua and many more · free open-source alternative; 240×136 screen
- **Picotron** — Lua · Lexaloffle "fantasy workstation" with desktop; beta since 2026 · https://www.lexaloffle.com/picotron.php
- **WASM-4** — any WASM language · 160×160, 4 colours, 64 KB carts · https://wasm4.org
- **Uxn / Varvara** — Uxntal assembly · Hundred Rabbits' tiny VM; their own tools run on it · https://100r.co/site/uxn.html

## 98. Interactive fiction / narrative engine — S C
- **Twine** — browser · passages and links; exports one HTML file
- **Ink** — inkle script, Unity/web · powers 80 Days and Heaven's Vault
- **Ren'Py** — Python · visual-novel default; Doki Doki Literature Club
- **Inform 7** — natural English · parser fiction written as English sentences; open source since 2022
- **AI Dungeon** — web · an LLM improvises the story; no authored branches · https://aidungeon.com

## 99. Inside another game (mods, UGC platforms, redstone computers) — S C W
- **Roblox Studio** — Luau · publish to Roblox's players; cash out via DevEx
- **Fortnite UEFN** — Verse · Unreal Editor for Fortnite islands; engagement payouts
- **Minecraft Fabric** — Java · lightweight mod loader for Java Edition
- **Screeps** — JS · MMO where your code plays, running 24/7 · https://screeps.com
- **CraftGPT** — Minecraft redstone · 5M-parameter LLM built from ~439M blocks · https://github.com/sammyuri/craftgpt

## 100. Daily puzzle with work woven in — N
- **seedrandom** — JS · date-seeded RNG: everyone gets the same daily level · https://github.com/davidbau/seedrandom
- **Puzzmo** — web · daily puzzle hub; today free, archive paid · https://www.puzzmo.com
- **LinkedIn Games** — web/app · Queens, Tango, Zip: daily puzzles inside a work site
- **Habitica** — web/mobile · real to-dos become an RPG; open source · https://habitica.com
- **LeechBlock NG** — browser extension · redirect linkedin.com/games to your own puzzle page · https://www.proginosko.com/leechblock/

## 101. Learning sandbox game for kids — I
- **Scratch** — browser blocks · MIT's block coding; the kids' default
- **Minecraft Education** — Win/Mac/iPad · redstone, code builder and lessons for classrooms
- **Turing Complete** — Steam · build a computer from NAND gates up to assembly · https://turingcomplete.game
- **Human Resource Machine** — PC/Switch/mobile · office workers act out assembly programs · https://tomorrowcorporation.com/humanresourcemachine
- **Nandgame** — browser · free; NAND gates up to a working CPU · https://nandgame.com

## 102. Creative coding & live coding — S C W
- **p5.js** — JS · Processing for the browser; the sketch default
- **nannou** — Rust · creative-coding framework for visuals, audio and installations · https://nannou.cc
- **Strudel** — browser JS · TidalCycles music patterns live-coded in a tab · https://strudel.cc
- **Hydra** — browser JS · live-coded video synth; chained like patch cables · https://hydra.ojack.xyz
- **Orca** — esoteric grid language · Hundred Rabbits' 2D letter-grid sequencer sending MIDI · https://hundredrabbits.itch.io/orca

## 103. Node-based visual patching — C
- **Pure Data** — desktop · free open-source patcher, audio first, runs on a Pi
- **TouchDesigner** — Win/macOS · real-time visuals for shows; free non-commercial tier
- **Max/MSP** — Win/macOS · Cycling '74 paid patcher; lives inside Ableton as Max for Live
- **cables.gl** — browser/desktop · WebGL patcher; MIT open source since 2024 · https://cables.gl
- **VCV Rack** — desktop · virtual Eurorack: drag literal cables between modules · https://vcvrack.com

## 104. Rendered show: video or podcast from code — I N
- **ffmpeg + TTS** — shell · stitch images, clips and synthesized voice; no framework
- **Remotion** — React/TS · React components rendered to MP4; paid licence for companies
- **Manim** — Python · 3Blue1Brown's math animation engine; community edition · https://www.manim.community
- **HyperFrames** — HTML/CSS · HeyGen's agent-first plain HTML → MP4; Apache 2.0 · https://github.com/heygen-com/hyperframes
- **NotebookLM Audio Overviews** — Google web · two AI hosts make a podcast from your docs; closed

## 105. Interactive show (pauses for buttons, form, chat) — N
- **H5P Interactive Video** — open-source web · video pauses for quizzes, hotspots, branches · https://h5p.org
- **Remotion Player + React overlay** — React · the show pauses; forms and buttons drawn on top
- **Stornaway** — web · story-map editor for branching interactive video · https://stornaway.io
- **ElevenLabs Agents** — API/widget · voice host you interrupt and answer; formerly Conversational AI
- **Tavus CVI** — API/WebRTC · live AI video face that sees and talks back · https://tavus.io

## 106. Input-scrubbed AI video (fake 3D) — I
- **Canvas image sequence** — JS · scroll position picks the frame; Apple product-page trick
- **GSAP ScrollTrigger** — JS · scrub any timeline with scroll; all plugins free since 2025
- **Kling AI** — web/API · start and end frames → a clip to scrub · https://klingai.com
- **Depth Anything V2** — Python/ONNX · depth map from one image → mouse-parallax fake 3D · https://github.com/DepthAnything/Depth-Anything-V2
- **SuperSplat** — browser · Gaussian splats: real 3D captured from phone video · https://superspl.at

## 107. Diagram / board compiled from code — I
- **Graphviz** — DOT · the old plain default; auto-lays-out any graph
- **Mermaid** — Markdown-like text · renders natively in GitHub, Notion, Obsidian
- **D2** — Go CLI · modern diagram language; sketch mode, TALA layout · https://d2lang.com
- **tldraw SDK** — React · whiteboard driven by code; production needs licence key · https://tldraw.dev
- **Penrose** — DSL · math notation → diagrams by constraint optimisation (CMU) · https://penrose.cs.cmu.edu

## 108. App inside a PDF — W
- **Acrobat form JavaScript** — PDF/AcroForm · calculators and validation inside fillable forms; the plain default
- **pdftris** — PDF JS · Tetris in 60 KB; form fields are the pixels · https://github.com/ThomasRinsma/pdftris
- **DoomPDF** — PDF JS · Doom compiled to old asm.js; Chromium only · https://github.com/ading2210/doompdf
- **LinuxPDF** — PDF JS · a RISC-V emulator boots Linux inside a PDF · https://github.com/ading2210/linuxpdf
- **PoC||GTFO polyglots** — PDF · each issue is also a ZIP, ROM or script · https://www.alchemistowl.org/pocorgtfo/

## 109. App inside a font — W
- **Chartwell** — OpenType · typed numbers become charts via ligatures; commercial · https://typographica.org/typeface-reviews/chartwell/
- **Sans Bullshit Sans** — OpenType · ligatures black out buzzwords as you type · https://pixelambacht.nl/2015/sans-bullshit-sans
- **Fontemon** — OpenType · Pokémon-parody game played by typing; 970 KB font · https://waxy.org/2021/03/fontemon
- **HarfBuzz Wasm shaper** — C/Wasm · experimental: a font carries WebAssembly shaping code · https://github.com/harfbuzz/harfbuzz
- **llama.ttf** — Wasm inside a font · the font runs an LLM while you type · https://github.com/fuglede/llama.ttf

## 110. CSS-only computer — W
- **Checkbox hack + `:has()`** — HTML/CSS · hidden inputs hold the state; selectors are the logic
- **Rule 110 in HTML+CSS** — HTML/CSS · 2011 demo; your clicks drive the automaton · https://github.com/efoxepstein/stupid-machines
- **Jane Ori's CPU Hack** — CSS · animation loop re-evaluates custom properties: a CSS clock · https://dev.to/janeori/expert-css-the-cpu-hack-4ddj
- **x86CSS** — CSS · Lyra Rebane's x86 CPU emulator; no JavaScript · https://lyra.horse/x86css/
- **cssDOOM** — CSS + JS loop · Doom drawn as 3D-transformed divs; JS runs the logic · https://cssdoom.wtf

## 111. Type-checker program — W
- **C++ templates / constexpr** — C++ · compile-time computing; the mainstream original
- **type-challenges** — TypeScript · puzzle repo: solve problems with types alone · https://github.com/type-challenges/type-challenges
- **typenum** — Rust · numbers and arithmetic as types; used in real crates · https://crates.io/crates/typenum
- **HypeScript** — TypeScript types · a TS type checker written in TS types · https://github.com/ronami/HypeScript
- **Doom in TypeScript types** — TS types · Dimitri Mitropoulos, 2025; the compiler renders frames

## 112. Database / SQL as the runtime — W
- **PostgREST** — Postgres · the schema becomes a REST API; logic in SQL · https://postgrest.org
- **Datasette** — SQLite/Python · a SQLite file becomes a browsable, queryable site · https://datasette.io
- **Omnigres** — Postgres · HTTP server inside Postgres; handlers in SQL; pre-1.0 · https://github.com/omnigres/omnigres
- **tetris-sql** — PostgreSQL · Tetris as one recursive-CTE game loop · https://github.com/nuno-faria/tetris-sql
- **DOOMQL** — CedarDB SQL · multiplayer Doom-like; views raycast each frame at 30 fps · https://cedardb.com/blog/doomql

# Batch 7 — Devices, hardware, networks

## 113. Microcontroller firmware — S
- **Arduino** — C++ · AVR, ESP32, RP2040 · the plain default: setup() and loop(), any board
- **MicroPython** — Python · ESP32, RP2040 · live REPL on the chip over USB
- **Zephyr RTOS** — C · hundreds of boards · Linux Foundation RTOS: devicetree, threads, Bluetooth stack
- **Embassy** — Rust · nRF, STM32, RP2040 · async/await firmware, no RTOS needed
- **AtomVM** — Erlang/Elixir · ESP32, STM32, RP2040 · BEAM processes on a $4 chip · https://github.com/atomvm/AtomVM

## 114. Embedded screen HMI / cheap touchscreen gadget — S C W
- **LVGL** — C · MCU screens, tens of kB RAM · the default embedded widget library
- **Slint** — Rust/C++/JS · MCU to Linux · declarative .slint markup with live preview
- **ESPHome LVGL** — YAML · ESP32 Cheap Yellow Display · touchscreen pages from YAML, no code; Home Assistant-linked
- **Nextion** — Nextion Editor · serial HMI panels · the screen holds the UI; your MCU sends serial
- **Cage** — Wayland · Raspberry Pi / Linux · kiosk compositor: boots into one fullscreen app · https://github.com/cage-kiosk/cage

## 115. Wearable / watch app — S
- **watchOS SwiftUI** — Swift · Apple Watch · plain default; complications through WidgetKit
- **Compose for Wear OS** — Kotlin · Pixel / Galaxy Watch · Google's round-screen Compose toolkit
- **Garmin Connect IQ** — Monkey C · Garmin watches · own language, sport data fields, own store
- **Pebble SDK + Alloy** — C or JavaScript (Moddable XS) · Pebble Time 2, Round 2 · revived Pebble; JS apps since Feb 2026 · https://developer.repebble.com
- **Bangle.js 2** — JavaScript (Espruino) · open hackable watch · apps installed from a web-page app loader · https://banglejs.com

## 116. TV & car screens — S C N
- **tvOS SwiftUI** — Swift · Apple TV · focus engine handles remote navigation
- **Compose for TV** — Kotlin · Android TV / Google TV · Jetpack Compose with D-pad focus
- **Roku SceneGraph + BrightScript** — BrightScript · Roku · own BASIC-like language plus XML scenes
- **Lightning (LightningJS)** — JS / WebGL · set-top boxes, TV browsers · draws the UI on canvas, no DOM · https://lightningjs.io
- **Android for Cars App Library** — Kotlin · Android Auto / Automotive · template-only: lists, maps, no custom drawing

## 117. XR / spatial / AR overlay — S C I N
- **visionOS SwiftUI + RealityKit** — Swift · Apple Vision Pro · windows, volumes, immersive spaces
- **Unity XR (OpenXR)** — C# · Quest, Pico, Vision Pro, phones · the popular cross-headset default
- **WebXR with A-Frame / three.js** — JavaScript · any headset browser · AR/VR opened from a URL, no install
- **Android XR (Jetpack XR SDK)** — Kotlin · Samsung Galaxy XR · Google's headset platform, launched Oct 2025
- **Lens Studio** — TypeScript/JS · Snap Spectacles, Snapchat camera · AR lenses pinned to faces, walls, rooms

## 118. HUD glasses app — W
- **Even Hub SDK** — web (HTML/JS) · Even Realities G2 · web app on a green monochrome HUD · https://hub.evenrealities.com/docs/get-started/overview
- **MentraOS** — TypeScript · Even, Vuzix Z100, Mentra glasses · open-source glasses OS; apps run cloud-side · https://docs.mentraglass.com
- **Meta Wearables Device Access Toolkit** — Swift/Kotlin + web apps · Meta Ray-Ban Display · display access in developer preview, May 2026 · https://wearables.developer.meta.com
- **Brilliant Labs SDK** — Lua on-device + Python/Flutter/WebBluetooth · Halo, Frame · open hardware; a Lua VM runs on the glasses · https://docs.brilliant.xyz
- **Google Glass Enterprise Edition 2** — Android · Glass EE2 · the original HUD; discontinued 2023

## 119. Ambient e-ink / LED display — W
- **TRMNL** — HTML + Liquid · 7.5" e-ink · server renders a still frame; plugins, MCP
- **kindle-dash** — shell · old jailbroken Kindle 4 · e-reader shows a server-rendered PNG · https://github.com/pascalw/kindle-dash
- **Inkplate** — Arduino / MicroPython · Soldered ESP32 e-paper boards · Wi-Fi e-paper, deep sleep between refreshes · https://soldered.com
- **Tronbyt (Pixlet)** — Starlark · Tidbyt 64×32 LED · community server after Tidbyt sold to Modal · https://github.com/tronbyt
- **AWTRIX 3** — MQTT/HTTP · Ulanzi TC001 pixel clock · archived; successor AWTRIX NG; apps pushed in · https://github.com/Blueforcer/awtrix3

## 120. Receipt-printer app — W
- **python-escpos** — Python · any ESC/POS thermal printer · the plain default driver library
- **ReceiptLine** — JavaScript · ESC/POS, StarPRNT, SVG · markdown for receipts · https://github.com/receiptline/receiptline
- **Star CloudPRNT** — HTTP · Star Micronics printers · printer polls your server for jobs, no driver
- **Breaklist** — Go · thermal printer · morning brief: tasks, reminders, weather, HN · https://github.com/alibahmanyar/breaklist
- **Little Printers** — iOS app + Sirius backend · revived BERG Little Printer · a printer your friends message · https://github.com/nordprojects

## 121. Odd-input handheld (Playdate, Flipper Zero) — W
- **Playdate SDK** — Lua / C · Playdate · crank input, 1-bit screen, games as cartridges
- **Flipper Zero apps** — C (FAP) or mJS JavaScript · Flipper Zero · IR, sub-GHz radio, NFC as app inputs
- **M5Stack Cardputer** — Arduino / MicroPython / UIFlow · ESP32-S3 · credit-card computer with a tiny keyboard
- **Arduboy FX** — Arduino C++ · Arduboy · six-button card-sized game handheld with flash cart · https://arduboy.com
- **Analogue Pocket openFPGA** — Verilog/VHDL · Analogue Pocket · your app is a hardware core on the FPGA

## 122. Physical input for software (dials, cards) — I
- **Stream Deck SDK** — TypeScript (Node) · Elgato Stream Deck · LCD keys and dials run plugin actions
- **QMK / ZMK** — C / devicetree · custom keyboards · keymap and macros compiled into keyboard firmware
- **Codex Micro** — Codex app settings · OpenAI × Work Louder pad, 2026 · reasoning dial, voice key, joystick for agents
- **TonUINO** — Arduino + NFC · DIY kids' music box · tap a card, it plays that folder · https://www.tonuino.de
- **monome grid** — serialosc / OSC · lit button grid · no labels; each app defines every button · https://monome.org

## 123. Embodied robot / smart toy — I
- **ROS 2** — C++ / Python · any robot · the plain default: nodes, topics, Gazebo sim
- **Pybricks** — MicroPython · LEGO SPIKE / Technic hubs · replaces LEGO firmware; code from the browser · https://pybricks.com
- **Ozobot** — OzoBlockly / color codes · Ozobot Evo · drives the line you draw; colors are commands
- **LeRobot** — Python · SO-101 arms · Hugging Face: record demos, train a policy, run it
- **Crazyflie** — Python cflib / C firmware · Bitcraze 27 g drone · open-source nano quadcopter, flies in swarms · https://www.bitcraze.io

## 124. Room as the computer — W
- **Home Assistant** — YAML / Python · sensors, lights, speakers · plain default: the room's devices are the I/O
- **Folk Computer** — Tcl / C · projector + camera · open source; programs on paper, reactive database · https://folk.computer
- **Paper Programs** — JavaScript in browser · projector + webcam · Dynamicland-inspired; cloud version off, run locally · https://paperprograms.org
- **reacTIVision** — C++ · camera under a table · fiducial markers become TUIO touch events · https://github.com/mkalten/reacTIVision
- **Dynamicland Realtalk** — Realtalk · Dynamicland spaces only · the original; not publicly released · https://dynamicland.org

## 125. Local-first sync app — C W I
- **Syncthing + plain files** — any language · desktop / Android · no innovation: folder syncs, app just reads files
- **Yjs** — JavaScript · browser / Node · most-used CRDT; Automerge is its twin
- **Zero** — TypeScript + Postgres · web · Rocicorp sync engine; 1.0 shipped 2026; queries run locally
- **Jazz** — TypeScript · web / React Native · sync, auth and permissions built into the data · https://jazz.tools
- **Braid** — HTTP extension · any web server · sync built into HTTP itself; IETF draft · https://braid.org

## 126. Bluetooth mesh app — W
- **Bluetooth Mesh (Zephyr / nRF Connect SDK)** — C · nRF52 nodes · the official SIG mesh: lights and sensors relay
- **Multipeer Connectivity** — Swift · iPhone / Mac · Apple's plain nearby-peer API over Bluetooth and Wi-Fi
- **bitchat** — Swift · iOS / macOS · BLE mesh chat; no accounts, Nostr fallback · https://github.com/permissionlesstech/bitchat
- **Briar** — Java · Android · messenger over Bluetooth, Wi-Fi or Tor · https://briarproject.org
- **Meshtastic** — C++ firmware + phone app · LoRa radios · phone joins by BLE; radios mesh for kilometers

## 127. Serverless peer-to-peer app — W
- **Pear (Holepunch)** — JavaScript · desktop / terminal · app itself loads from peers by pear:// key · https://docs.pears.com
- **Trystero** — JavaScript · browser · WebRTC rooms matched over BitTorrent/Nostr/MQTT, no server · https://github.com/dmotz/trystero
- **Iroh** — Rust · any device · dial peers by public key; QUIC with hole-punching · https://iroh.computer
- **Holochain** — Rust / WASM · desktop · agent-centric DHT; each user keeps their own chain · https://holochain.org
- **Freenet** — Rust / WASM · desktop · new network since Dec 2025; River group chat · https://freenet.org

## 128. Protocol-native app (AT Protocol, Nostr) — W
- **AT Protocol** — TypeScript / Go · Bluesky network · data in the user's repo; apps define lexicons
- **Nostr (NDK)** — TypeScript · any client · signed events on relays; a keypair is the account
- **ActivityPub with Fedify** — TypeScript · fediverse · plain default federation, Mastodon-compatible · https://fedify.dev
- **Solid** — JavaScript (Inrupt SDK) · Solid pods · Berners-Lee's pods: apps read the user's own store · https://solidproject.org
- **Delta Chat webxdc** — HTML/JS zip · Delta Chat over email · mini apps shared in a chat over plain email · https://webxdc.org
