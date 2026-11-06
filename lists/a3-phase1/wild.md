Lens: wild and experimental. These are new shapes of apps that people on HN, Lobsters, Reddit, Product Hunt and GitHub actually shipped in 2025–2026, and each one links to something that exists.

Sources (pages I read; researched 2026-11-06)
- https://www.inkandswitch.com/malleable-software/
- https://simonwillison.net/2025/Feb/5/ambsheets/
- https://simonwillison.net/2025/Dec/10/html-tools/
- https://www.robinsloan.com/notes/home-cooked-app/
- https://hn-reader-qhungg289.vercel.app/story/45783640
- https://hn.jakechampion.name/item/47062726
- https://lobsters.jakechampion.name/item/nxmzzn
- https://www.bgr.com/1981449/claude-sonnet-4-5-imagine-feature/
- https://bgr.com/tech/mind-blowing-ai-instantly-makes-artificial-web-pages-from-anything-you-type/
- https://arxiv.org/abs/2507.08800
- https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/
- https://workos.com/blog/2026-01-27-mcp-apps
- https://sdtimes.com/ai/google-launches-a2ui-project-to-enable-agents-to-build-contextually-relevant-uis/
- https://github.com/openclaw/openclaw
- https://builtin.com/articles/what-is-moltbook-openclaw
- https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/
- https://claude.com/blog/skills
- https://loop.circleci.com/i-built-a-server-that-rewrites-itself-while-running
- https://techcrunch.com/2025/09/30/nothing-launches-ai-tool-for-building-mini-apps-using-prompts/
- https://sacra.com/c/lovable/
- https://the-decoder.com/tldraw-unveils-experimental-natural-language-computer-powered-by-gemini-2-0/
- https://developer.chrome.com/docs/ai/built-in
- https://github.com/pipecat-ai/pipecat
- https://www.macrumors.com/2024/12/18/openai-chatgpt-phone-line/
- https://www.agentmail.to/
- https://mattkc.com/etc/snakeqr/
- https://hackaday.com/2018/07/07/tiny-websites-have-no-server
- https://github.com/ading2210/linuxpdf
- https://github.com/fuglede/llama.ttf
- https://lyra.horse/x86css/
- https://softwareengineeringdaily.com/?p=9367
- https://cedardb.com/blog/doomql
- https://github.com/sammyuri/craftgpt
- https://dev.to/balastrong/play-4-multiplayer-games-on-github-profiles-readmemd-m83
- https://charm.land/blog/terminaldotshop
- https://core.telegram.org/bots/webapps
- https://developers.raycast.com/
- https://github.com/swiftbar/SwiftBar
- https://github.com/TheBoredTeam/boring.notch
- https://github.com/alterhq/openpets
- https://www.val.town/
- https://gamefromscratch.com/godot-developed-non-game-applications/
- https://enginesdatabase.com/blog/free-alternatives-to-pico-8-fantasy-console/
- https://cdm.link/musical-powerful-live-coding-in-the-browser-is-near-with-strudel-usable-now/
- https://github.com/io12/BootMine
- https://trmnl.com/developers
- https://github.com/tidbyt/pixlet
- https://joeldare.com/trying-to-stop-procrastination-with-my-receipt-printer
- https://hub.evenrealities.com/docs/get-started/overview
- https://sdk.play.date/inside-playdate/
- https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display
- https://dynamicland.org/2024/FAQ/
- https://folk.computer/
- https://archive.fosdem.org/2026/schedule/track/local-first
- https://github.com/permissionlesstech/bitchat
- https://docs.pears.com/
- https://techcrunch.com/2025/03/30/beyond-bluesky-these-are-the-apps-building-social-experiences-on-the-at-protocol/

## Generated-per-click apps
- shape: no code exists until you click; the model writes each screen live
- e.g.: Imagine with Claude; Websim (any URL or prompt becomes a generated site)
- seen at: https://www.bgr.com/1981449/claude-sonnet-4-5-imagine-feature/

## LLM as the backend
- shape: every HTTP request goes to a model with DB tools; no routes or logic
- e.g.: nokode (Show HN, Nov 2025)
- seen at: https://hn-reader-qhungg289.vercel.app/story/45783640

## Neural-rendered computers
- shape: no program at all; a diffusion model predicts every frame from your input
- e.g.: NeuralOS (simulated Ubuntu desktop); Project Genie / Genie 3 (playable worlds)
- seen at: https://arxiv.org/abs/2507.08800

## Apps inside AI chat
- shape: a tool returns a sandboxed HTML widget that renders inline in a Claude/ChatGPT conversation
- e.g.: MCP Apps (ui:// resources); OpenAI Apps SDK
- seen at: https://workos.com/blog/2026-01-27-mcp-apps

## Agent-composed native UI
- shape: agent streams declarative JSON; the client renders it with its own trusted component catalog
- e.g.: Google A2UI (Flutter GenUI, Lit, React renderers)
- seen at: https://sdtimes.com/ai/google-launches-a2ui-project-to-enable-agents-to-build-contextually-relevant-uis/

## Personal agent as the app
- shape: one self-hosted agent you message on WhatsApp/Telegram replaces many single-purpose apps
- e.g.: OpenClaw (formerly Clawdbot)
- seen at: https://github.com/openclaw/openclaw

## Apps whose users are agents
- shape: only AI agents post or act; humans just watch
- e.g.: Moltbook (agent-only Reddit with "submolts")
- seen at: https://builtin.com/articles/what-is-moltbook-openclaw

## Agent-first CLIs
- shape: a command line designed for AI agents first: JSON output, schemas, dry-runs
- e.g.: Google Workspace CLI (gws); Codex `$cli-creator` skill
- seen at: https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/

## Skill folders as apps
- shape: the app is a folder of instructions and scripts that an agent loads on demand
- e.g.: Claude Agent Skills (SKILL.md); Custom GPTs
- seen at: https://claude.com/blog/skills

## Self-rewriting apps
- shape: the running app takes feature requests, writes its own code and hot-reloads itself
- e.g.: vote-driven self-rewriting Node server (CircleCI blog); Agentity
- seen at: https://loop.circleci.com/i-built-a-server-that-rewrites-itself-while-running

## Prompted phone widgets
- shape: the phone OS turns a text prompt into a shareable, remixable home-screen widget
- e.g.: Nothing Playground / Essential Apps
- seen at: https://techcrunch.com/2025/09/30/nothing-launches-ai-tool-for-building-mini-apps-using-prompts/

## Prompt-to-deployed full-stack apps
- shape: describe the app in chat; the platform generates, hosts and iterates the whole stack
- e.g.: Lovable; bolt.new
- seen at: https://sacra.com/c/lovable/

## Home-cooked software for one
- shape: built for one family or person, never scaled and never sold
- e.g.: Robin Sloan's BoopSnoop (a family messenger with four users)
- seen at: https://www.robinsloan.com/notes/home-cooked-app/

## Malleable software
- shape: users reshape the running tool itself, with little friction, instead of filing requests
- e.g.: Ink & Switch Patchwork; Potluck (text documents become apps)
- seen at: https://www.inkandswitch.com/malleable-software/

## Natural-language node canvas
- shape: an infinite canvas where each block is an LLM procedure wired to others
- e.g.: tldraw computer; tldraw workflow starter kit
- seen at: https://the-decoder.com/tldraw-unveils-experimental-natural-language-computer-powered-by-gemini-2-0/

## On-device model web apps
- shape: the page calls an LLM that ships inside the browser; works offline, no API key
- e.g.: Chrome Prompt API (Gemini Nano); WebLLM
- seen at: https://developer.chrome.com/docs/ai/built-in

## Voice-only and dial-in apps
- shape: no screen; a realtime speech pipeline reached by mic or an ordinary phone call
- e.g.: Pipecat / LiveKit Agents; 1-800-ChatGPT (works from a landline)
- seen at: https://github.com/pipecat-ai/pipecat

## Email as the interface
- shape: you email the app and it emails back; the inbox is the UI
- e.g.: AgentMail (inboxes via API); Mixus (email agent@mixus.com)
- seen at: https://www.agentmail.to/

## Single-file HTML tools
- shape: the whole app is one .html file, no build; state in URL or localStorage
- e.g.: Simon Willison's 150+ HTML tools; TiddlyWiki
- seen at: https://simonwillison.net/2025/Dec/10/html-tools/

## Whole OS in one HTML file
- shape: a static page boots a shell, filesystem, git and npm entirely client-side
- e.g.: Shiro (420 KB Unix in one file); StackBlitz WebContainers
- seen at: https://hn.jakechampion.name/item/47062726

## App in a link or QR code
- shape: the entire program is encoded in a URL fragment or a printed QR code
- e.g.: itty.bitty.site; MattKC's Snake in a QR code
- seen at: https://mattkc.com/etc/snakeqr/

## App inside a PDF
- shape: the PDF's embedded JavaScript runs the program, so a document is the runtime
- e.g.: DoomPDF; LinuxPDF (a RISC-V emulator inside a PDF)
- seen at: https://github.com/ading2210/linuxpdf

## App inside a font
- shape: the font's shaping engine runs code, so typing characters triggers the program
- e.g.: llama.ttf (an LLM run by HarfBuzz's Wasm shaper); Fontemon (a game built from ligatures)
- seen at: https://github.com/fuglede/llama.ttf

## CSS-only computers
- shape: the stylesheet alone does the computing; CSS is the CPU, with no JavaScript
- e.g.: x86CSS (Lyra Rebane)
- seen at: https://lyra.horse/x86css/

## Type-checker programs
- shape: the program runs at compile time inside the type system; the compiler executes it
- e.g.: Doom in TypeScript types (Dimitri Mitropoulos)
- seen at: https://softwareengineeringdaily.com/?p=9367

## Database-rendered games
- shape: state lives in tables; SQL views raycast and render each frame
- e.g.: DOOMQL (CedarDB); DuckDB-DOOM (DuckDB-WASM)
- seen at: https://cedardb.com/blog/doomql

## Spreadsheet as the runtime
- shape: cells hold state, formulas are logic; one cell can hold several scenarios
- e.g.: Ink & Switch Ambsheets; Doom.xls
- seen at: https://simonwillison.net/2025/Feb/5/ambsheets/

## Computers built inside a game
- shape: logic gates are made of game blocks, and the app runs inside a game world
- e.g.: CraftGPT (an LLM built from Minecraft redstone); MCHPRS server
- seen at: https://github.com/sammyuri/craftgpt

## Git-forge apps
- shape: the README is the screen, issues are the input, and Actions is the backend
- e.g.: GitHub profile chess, 2048 and Connect 4
- seen at: https://dev.to/balastrong/play-4-multiplayer-games-on-github-profiles-readmemd-m83

## SSH apps
- shape: `ssh host` opens a TUI, and your public key is your account
- e.g.: terminal.shop (Wish + Bubble Tea); snakes.run
- seen at: https://charm.land/blog/terminaldotshop

## Messenger mini-apps
- shape: a web app embedded in a messenger or voice channel, using its identity and payments
- e.g.: Telegram Mini Apps; Discord Activities (Embedded App SDK)
- seen at: https://core.telegram.org/bots/webapps

## Host-app extensions
- shape: the app lives inside another tool's launcher or editor and uses its UI kit
- e.g.: Raycast extensions (React/TS); Obsidian plugins
- seen at: https://developers.raycast.com/

## Menu-bar script apps
- shape: any script's stdout becomes a live menu-bar item and dropdown
- e.g.: SwiftBar; xbar
- seen at: https://github.com/swiftbar/SwiftBar

## Notch apps
- shape: the MacBook notch becomes a Dynamic Island for media, a file shelf and the HUD
- e.g.: boring.notch (SwiftUI); NotchNook
- seen at: https://github.com/TheBoredTeam/boring.notch

## Desktop pets for agents
- shape: an animated creature on the desktop shows what agents and apps are doing
- e.g.: OpenPets (MCP/CLI-driven); VibePet
- seen at: https://github.com/alterhq/openpets

## Trigger-only functions
- shape: no UI; a function at a URL, fired by HTTP, cron or incoming email
- e.g.: Val Town vals
- seen at: https://www.val.town/

## Game engine as GUI toolkit
- shape: desktop tools built in a game engine that redraws the window like a game
- e.g.: Godot apps (Pixelorama, Material Maker)
- seen at: https://gamefromscratch.com/godot-developed-non-game-applications/

## Fantasy consoles
- shape: an imaginary retro machine with hard limits; apps are tiny shareable cartridges
- e.g.: PICO-8; TIC-80
- seen at: https://enginesdatabase.com/blog/free-alternatives-to-pico-8-fantasy-console/

## Live-coded performance apps
- shape: you edit the code while it runs, and that editing is the performance
- e.g.: Strudel (TidalCycles in the browser); Sonic Pi
- seen at: https://cdm.link/musical-powerful-live-coding-in-the-browser-is-near-with-strudel-usable-now/

## Boot-sector apps
- shape: 512 bytes that the BIOS boots directly, with no operating system
- e.g.: BootMine; BootLife
- seen at: https://github.com/io12/BootMine

## Ambient glanceable displays
- shape: an always-on e-ink or LED screen showing a server-rendered still frame or loop
- e.g.: TRMNL (HTML + Liquid, MCP); Tidbyt Pixlet (Starlark, 64×32 LED)
- seen at: https://trmnl.com/developers

## Receipt-printer apps
- shape: the output is paper; a thermal printer prints tasks or daily briefs
- e.g.: tickit (Joel Dare); Breaklist
- seen at: https://joeldare.com/trying-to-stop-procrastination-with-my-receipt-printer

## HUD glasses apps
- shape: a web app projected onto the monochrome heads-up display of smart glasses
- e.g.: Even Hub SDK (Even G2)
- seen at: https://hub.evenrealities.com/docs/get-started/overview

## Odd-input handhelds
- shape: a dedicated pocket device with a crank, IR or radio; apps are cartridges
- e.g.: Playdate SDK (Lua/C, crank); Flipper Zero apps (FAP, mJS)
- seen at: https://sdk.play.date/inside-playdate/

## $15 touchscreen gadgets
- shape: an app flashed onto a cheap ESP32 board with its own touchscreen
- e.g.: ESP32 Cheap Yellow Display (LVGL, ESPHome)
- seen at: https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display

## Room as the computer
- shape: programs are printed on paper, and cameras and projectors run them on tables
- e.g.: Dynamicland Realtalk; Folk Computer
- seen at: https://dynamicland.org/2024/FAQ/

## Local-first sync apps
- shape: data lives on the device first; CRDT sync merges peers and server later
- e.g.: Automerge; Jazz
- seen at: https://archive.fosdem.org/2026/schedule/track/local-first

## Bluetooth mesh apps
- shape: phones relay messages to each other over Bluetooth, with no internet and no accounts
- e.g.: bitchat
- seen at: https://github.com/permissionlesstech/bitchat

## Serverless peer-to-peer apps
- shape: the app itself is loaded from peers, so there is no server to host it
- e.g.: Pear runtime (Holepunch); Keet
- seen at: https://docs.pears.com/

## Protocol-native apps
- shape: user data sits in their own repo; many apps share one open data layer
- e.g.: AT Protocol apps (Smoke Signal events, WhiteWind blogs)
- seen at: https://techcrunch.com/2025/03/30/beyond-bluesky-these-are-the-apps-building-social-experiences-on-the-at-protocol/
