Lens: a stack-picker's taxonomy, sorted by where the app runs and how its UI exists.

## Desktop · Platform-native toolkit
- shape: One OS's own UI framework; real native controls, no portability.
- e.g.: SwiftUI/AppKit, WinUI 3

## Desktop · Native-widget cross-platform wrapper
- shape: One API mapped onto each OS's real native controls.
- e.g.: wxWidgets, SWT

## Desktop · Self-drawn cross-platform GUI
- shape: Toolkit paints its own widgets everywhere; retained widget tree, same look.
- e.g.: Qt/QML, Rust iced

## Desktop · Immediate-mode GUI
- shape: UI redrawn from code every frame; no widget objects or state tree.
- e.g.: Dear ImGui, egui

## Desktop · Bundled-browser shell
- shape: Web app shipped with its own Chromium and Node runtime.
- e.g.: Electron, NW.js

## Desktop · System-webview shell
- shape: Web UI in the OS's built-in webview; small native backend.
- e.g.: Tauri, Wails

## Device · Glanceable mini-surface
- shape: Tiny always-visible UI: menu-bar item, tray icon, widget, watch complication.
- e.g.: SwiftBar/rumps, WidgetKit

## Device · TV & car screens
- shape: Remote, voice or glance input; focus navigation or template-only UI.
- e.g.: tvOS SwiftUI, Android for Cars App Library

## Device · XR / spatial
- shape: UI placed in 3D space around the user; headset or AR phone.
- e.g.: visionOS RealityKit, WebXR

## Terminal · One-shot CLI
- shape: Arguments in, text and exit code out; composes in pipes and scripts.
- e.g.: Rust clap, Python Typer

## Terminal · Interactive prompt & REPL
- shape: Line-by-line terminal conversation: prompts, pickers, read-eval loop.
- e.g.: gum, prompt_toolkit

## Terminal · Full-screen TUI
- shape: Takes over the terminal screen; keyboard-driven panes, lists, live redraws.
- e.g.: Ratatui, Textual

## Terminal · SSH-served app
- shape: App runs on a server; users connect with plain ssh, nothing installed.
- e.g.: Charm Wish, russh

## Web · Static site
- shape: Prebuilt HTML/CSS/JS files on a CDN; no server logic.
- e.g.: Astro, Hugo

## Web · Client-side JS app
- shape: JavaScript renders the UI in the browser; server mostly serves data.
- e.g.: React + Vite, SvelteKit

## Web · Server-rendered hypermedia
- shape: Server owns UI and state, sends HTML or live diffs; minimal client JS.
- e.g.: htmx + Django, Phoenix LiveView

## Web · Script-to-web-UI
- shape: Plain Python/R script declares widgets; framework generates the page.
- e.g.: Streamlit, Gradio

## Web · Notebook
- shape: Cells of code, output and prose; the document itself is the app.
- e.g.: Jupyter, marimo

## Web · Installable PWA
- shape: Web app installed to home screen or dock, offline via service worker.
- e.g.: vite-plugin-pwa, Workbox

## Web · WASM-compiled app
- shape: Non-JS language compiled to WebAssembly runs the whole app in browser.
- e.g.: Leptos, Blazor WebAssembly

## Web · Canvas / GPU scene
- shape: One canvas drawn by WebGL/WebGPU; scene graph instead of DOM.
- e.g.: Three.js, PixiJS

## Web · Embeddable widget
- shape: Snippet or component that lives inside other people's websites.
- e.g.: Lit web components, iframe embed

## Browser · Extension
- shape: Packaged add-on: toolbar popup, side panel, scripts on any page.
- e.g.: WXT, Plasmo

## Browser · Userscript / bookmarklet
- shape: Single script injected into a specific site to change or automate it.
- e.g.: Tampermonkey, Violentmonkey

## Mobile · Platform-native
- shape: Separate codebase per mobile OS in its first-party UI framework.
- e.g.: SwiftUI, Jetpack Compose

## Mobile · Cross-platform compiled
- shape: One codebase compiled to iOS and Android, native or self-drawn widgets.
- e.g.: Flutter, React Native

## Mobile · Hybrid webview
- shape: Web app wrapped in a store-installable shell with native plugin bridge.
- e.g.: Capacitor, Ionic

## Mobile · Super-app mini-app
- shape: Runs inside a messenger or super-app, borrowing its login, payments, sharing.
- e.g.: Telegram Mini Apps, WeChat Mini Programs

## Conversation · Chat bot
- shape: Lives in a messenger; UI is messages, buttons and commands.
- e.g.: aiogram, discord.py

## Conversation · Voice-first assistant
- shape: Speech in, speech out; turn-taking and latency are the UI.
- e.g.: Pipecat, Alexa Skills Kit

## Conversation · LLM-hosted app / agent tool
- shape: Exposes tools or widgets an AI assistant calls inside its chat.
- e.g.: MCP server SDK, OpenAI Apps SDK

## Conversation · Email / SMS interface
- shape: Users send or reply to emails or texts; inbound webhook drives logic.
- e.g.: Postmark inbound, Twilio Messaging

## Plugin · Editor / IDE / notes extension
- shape: Adds commands, panels and views inside a code editor or notes app.
- e.g.: VS Code extension API, Obsidian plugin

## Plugin · Office & spreadsheet add-on
- shape: Spreadsheet or document is the UI; scripts, macros, sidebars extend it.
- e.g.: Google Apps Script, Office.js

## Plugin · Creative-tool plugin
- shape: Loaded by a DAW, 3D or image tool; works on the host's media.
- e.g.: JUCE (VST/AU), Blender Python add-on

## Plugin · Launcher & OS automation
- shape: Hooks into launcher, hotkeys or OS shell; tiny scripted UI, system actions.
- e.g.: Raycast extension, Hammerspoon

## Plugin · Game mod / UGC platform
- shape: Built inside an existing game's engine, assets and player base.
- e.g.: Roblox Studio (Luau), Minecraft Fabric

## Builder · Low/no-code app
- shape: Drag-and-drop UI bound to data sources, hosted by the builder.
- e.g.: Retool, Glide

## Builder · Visual flow automation
- shape: Nodes and wires connecting triggers and services; no UI of its own.
- e.g.: n8n, Node-RED

## Game · Editor-centric engine
- shape: Scene editor, asset pipeline, scripting; you build inside the engine's IDE.
- e.g.: Godot, Unity

## Game · Code-first framework
- shape: Library gives loop, input, rendering; everything else is your code.
- e.g.: Bevy, raylib

## Game · Fantasy console
- shape: Tiny virtual machine with fixed resolution, palette, size limits and built-in editors.
- e.g.: PICO-8, TIC-80

## Game · Interactive fiction / narrative
- shape: Story graph of passages and choices; engine handles text, saves, branching.
- e.g.: Twine, Ren'Py

## Game · Creative coding & patching
- shape: Sketch loop or node patch making real-time visuals, sound, installations.
- e.g.: p5.js, TouchDesigner

## Backend · HTTP / API service
- shape: Long-running server answering requests; UI lives elsewhere or nowhere.
- e.g.: FastAPI, Axum

## Backend · Daemon, job, worker
- shape: No requests, no UI; runs on schedule, events or queue.
- e.g.: launchd + Python, Temporal

## Backend · Serverless / edge function
- shape: Single handler on a platform; spins up per request, scales to zero.
- e.g.: Cloudflare Workers, AWS Lambda

## Backend · Smart contract + dApp
- shape: Logic deployed on a blockchain; wallet-connected web front end.
- e.g.: Solidity + Foundry, Solana Anchor

## Hardware · Microcontroller firmware
- shape: Code on a chip with no OS; buttons, LEDs, sensors, tiny screens.
- e.g.: Arduino, Rust Embassy

## Hardware · Embedded screen HMI / kiosk
- shape: Device boots straight into one fullscreen GUI on its panel.
- e.g.: LVGL, Slint
