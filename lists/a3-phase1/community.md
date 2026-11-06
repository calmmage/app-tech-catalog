Lens: app categories as developers themselves carve them up: awesome-list sections, survey categories, roadmap tracks and recurring "what should I use for X" threads.

Sources (read on 6 Nov 2026 through a summarising fetch; awesome-go and awesome-rust only partly, because the pages are too long. Reddit could not be fetched, because old.reddit is blocked and the mirrors are down, so no Reddit thread is listed):
- https://github.com/rothgar/awesome-tuis
- https://areweguiyet.com/
- https://www.boringcactus.com/2025/04/13/2025-survey-of-rust-gui-libraries.html
- https://github.com/sindresorhus/awesome-electron
- https://roadmap.sh/roadmaps
- https://2024.stateofjs.com/en-US/libraries/
- https://survey.stackoverflow.co/2025/technology
- https://www.thoughtworks.com/radar/languages-and-frameworks (Vol. 35, Nov 2026)
- https://hn.jakechampion.name/item/43941727 (Ask HN: best framework for Mac/Windows desktop apps in 2025)
- https://hn.jakechampion.name/item/44848058 (Ask HN: desktop toolchains in 2025)
- https://github.com/vinta/awesome-python
- https://github.com/avelino/awesome-go (partial)
- https://github.com/rust-unofficial/awesome-rust (table of contents only)
- https://github.com/shadawck/awesome-cli-frameworks
- https://github.com/Calinou/awesome-gamedev
- https://github.com/terkelg/awesome-creative-coding
- https://github.com/alexanderop/awesome-local-first
- https://github.com/fregante/Awesome-WebExtensions
- https://github.com/bvolpato/awesome-userscripts
- https://github.com/hemanth/awesome-pwa
- https://github.com/ebertti/awesome-telegram
- https://core.telegram.org/bots/webapps
- https://github.com/justjavac/awesome-wechat-weapp
- https://github.com/kairichard/awesome-nocode-lowcode
- https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/
- https://hypermedia.systems/
- https://jamstack.org/generators/
- https://github.com/mbasso/awesome-wasm
- https://simonwillison.net/2025/Dec/10/html-tools/
- https://redbadger.github.io/crux/
- https://github.com/ocornut/imgui
- https://github.com/lvgl/lvgl
- https://github.com/raycast/extensions
- https://github.com/viatsko/awesome-vscode
- https://github.com/obsidianmd/obsidian-sample-plugin
- https://github.com/felixhageloh/uebersicht
- https://www.hammerspoon.org/
- https://nodered.org/
- https://docs.godotengine.org/en/stable/tutorials/ui/creating_applications.html
- https://github.com/paladin-t/fantasy
- https://github.com/tajmone/awesome-interactive-fiction
- https://tech-insider.org/roblox-studio-vs-unity-vs-godot-2026/
- https://gdevelop.io/
- https://juce.com/
- https://github.com/tomkrikorian/awesome-visionOS
- https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md
- https://developer.amazon.com/en-US/alexa/alexa-skills-kit
- https://github.com/pipecat-ai/pipecat
- https://marimo.io/
- https://uibakery.io/blog/bolt-vs-lovable-vs-v0
- https://dev.to/hamzan/why-i-built-a-15mb-swiftui-menu-bar-app-instead-of-reaching-for-electron-1boe

## Client-rendered SPA
- shape: one JS bundle renders every screen in the browser; server only returns JSON.
- e.g.: React, Svelte
- source: State of JS 2024 "Front-end Frameworks"; roadmap.sh Frontend, React, Vue and Angular tracks

## Full-stack JS meta-framework
- shape: one codebase renders on the server, hydrates in the browser; routes double as API.
- e.g.: Next.js, SvelteKit
- source: State of JS 2024 "Meta-Frameworks"; roadmap.sh Next.js track

## Server-rendered MVC monolith
- shape: server owns routes, data and HTML templates; the browser only displays pages.
- e.g.: Ruby on Rails, Django
- source: Stack Overflow 2025 "Web frameworks and technologies" (Django, Laravel, Rails, ASP.NET Core); roadmap.sh Backend, Django, Laravel and Rails tracks; awesome-python "Web Frameworks"

## HTML-over-the-wire
- shape: server sends HTML fragments or live diffs; no client-side state framework.
- e.g.: htmx, Phoenix LiveView
- source: hypermedia.systems (htmx "without using SPA frameworks"); State of JS 2024 lists HTMX among front-end frameworks; Stack Overflow 2025 lists Phoenix

## Static content site
- shape: pages built once at deploy time from Markdown and served as plain files.
- e.g.: Astro, Hugo
- source: jamstack.org/generators (~377 generators, filtered by language and template); awesome-python "Static Site Generators"

## Installable PWA
- shape: web app with manifest and service worker; installs, works offline, no store.
- e.g.: Workbox, PWABuilder
- source: hemanth/awesome-pwa "Tools" (Service Worker Libraries, Generators and CLIs)

## WebAssembly browser app
- shape: a non-JS language compiled to WASM drives the page or a canvas.
- e.g.: Yew, Blazor WebAssembly
- source: mbasso/awesome-wasm "Web frameworks-libraries" (Blazor, Yew, Vugu, seed); boringcactus survey treats Leptos and Dominator as web-only

## Local-first sync app
- shape: data lives on the device first; a CRDT or sync engine merges it between devices.
- e.g.: Automerge, Jazz
- source: alexanderop/awesome-local-first (CRDT Libraries, State Management & Sync, Frameworks & Platforms)

## Single-file HTML tool
- shape: one .html file with inline JS and CDN dependencies; no build step, no backend.
- e.g.: vanilla HTML+JS on GitHub Pages, Alpine.js
- source: Simon Willison "HTML tools" (150+ single-file tools, prompted "No React"); Ask HN 2025 toolchains ("single-file apps with a dumb server and Syncthing")

## Python script → browser UI
- shape: write only a Python script or notebook; the framework serves the web UI.
- e.g.: Streamlit, marimo
- source: awesome-python "Dashboards and Apps" (streamlit, dash, gradio) and "GUI Development › Web-based" (nicegui, flet); marimo.io (a notebook served as a web app); boringcactus survey (GemGui serves HTML to the browser)

## Bundled-Chromium desktop app
- shape: ships its own browser engine plus Node; a web UI shown as a desktop window.
- e.g.: Electron, NW.js
- source: sindresorhus/awesome-electron; State of JS 2024 "Mobile & Desktop"; both 2025 Ask HN desktop threads

## System-webview shell
- shape: tiny native host; the web UI renders in the OS's own webview.
- e.g.: Tauri, Wails
- source: boringcactus survey "diet Electron" group (Tauri, Dioxus); Ask HN 2025 toolchains (Wails, Tauri); awesome-python "Web-based" (pywebview)

## OS-native desktop app
- shape: uses the platform's own UI framework; one OS, deepest integration.
- e.g.: SwiftUI/AppKit (macOS), WinUI/WPF (Windows)
- source: Ask HN 2025 toolchains (Swift/AppKit, WPF, WinForms, MFC); areweguiyet tags MacOS and WinApi (cacao, WinSafe); roadmap.sh Swift & SwiftUI

## Cross-platform native-widget toolkit
- shape: one API wraps or emulates the classic widgets on every desktop OS.
- e.g.: Qt, wxWidgets
- source: awesome-python "GUI Development" (PySide6, wxPython, tkinter, toga); boringcactus "bindings to established toolkits" (GTK, Qt, FLTK, Tk); Ask HN 2025 (Qt, Tcl/Tk, Java Swing)

## Custom-drawn GPU toolkit
- shape: its own renderer draws every pixel, so it looks the same on all platforms.
- e.g.: Flutter, Iced / Slint
- source: areweguiyet tags (winit, WebGPU, skia); boringcactus "Elm-inspired" and "DSL-driven" groups; Ask HN 2025 (Flutter, Avalonia, Fyne)

## Immediate-mode GUI
- shape: code redraws the UI every frame; no widget tree or retained state.
- e.g.: Dear ImGui, egui
- source: areweguiyet "Immediate mode API" tag; ocornut/imgui (game-engine tooling and debug tools); boringcactus "Immediate mode" group; Ask HN 2025 (egui, Dear ImGui)

## RAD visual form designer
- shape: drag widgets onto forms in an IDE, then double-click to write handlers.
- e.g.: Delphi, Lazarus
- source: Ask HN 2025 toolchains (Delphi "the easiest and most integrated way", Lazarus/Free Pascal, Xojo)

## Shared core + native shells
- shape: business logic is shared in one language; each platform writes its own native UI.
- e.g.: Crux, Kotlin Multiplatform
- source: Crux docs (Rust core; Swift, Kotlin and TS shells); boringcactus survey (Crux, flutter_rust_bridge and Rinf flagged as "not really GUI libraries")

## Native mobile app
- shape: each phone OS's own SDK and language; full device APIs, store distribution.
- e.g.: SwiftUI (iOS), Jetpack Compose (Android)
- source: roadmap.sh Android, iOS, Swift & SwiftUI and Kotlin tracks

## Cross-platform mobile framework
- shape: one codebase compiles to real iOS and Android apps.
- e.g.: React Native + Expo, Flutter
- source: State of JS 2024 "Mobile & Desktop" (React Native, Expo, NativeScript); roadmap.sh React Native and Flutter tracks

## Webview-wrapped mobile app
- shape: a web app inside a native shell, with plugin bridges to device APIs.
- e.g.: Capacitor/Ionic, Hotwire Native
- source: State of JS 2024 "Mobile & Desktop" (Capacitor, Ionic, Cordova); Ask HN 2025 (Hotwire Native); hypermedia.systems (Hyperview for mobile)

## Menu bar / tray utility
- shape: a menu bar or tray icon opens a popover; no main window.
- e.g.: SwiftUI MenuBarExtra, Electron Tray
- source: dev.to SwiftUI menu-bar vs Electron write-up (native "first-class", Electron "limited"); Godot "Creating applications" docs (tray icons)

## Desktop widgets & glanceables
- shape: small always-visible views on the desktop, home screen, lock screen or watch face.
- e.g.: Übersicht, WidgetKit
- source: felixhageloh/uebersicht (React widgets on the macOS desktop); Ask HN 2025 toolchains (Quickshell)

## Host-app plugin / launcher extension
- shape: code runs inside another app through its plugin API and UI slots.
- e.g.: Raycast extension, VS Code extension
- source: raycast/extensions (Raycast Store, built with React); awesome-vscode "Resources for extension developers"; obsidian-sample-plugin; awesome-go "Editor Plugins"

## OS automation script
- shape: no window; a hotkey, OS event or schedule runs local actions.
- e.g.: Hammerspoon, AutoHotkey
- source: hammerspoon.org ("just a bridge between the operating system and a Lua scripting engine")

## Cloud workflow automation
- shape: trigger → action chains across web services, wired in a flow editor.
- e.g.: n8n, Node-RED
- source: kairichard/awesome-nocode-lowcode "Automation" (Zapier, n8n, Make); nodered.org ("Low-code programming for event-driven applications")

## CLI command & prompt wizard
- shape: runs with arguments or step-by-step prompts, prints text, then exits.
- e.g.: clap / Typer, Inquirer.js
- source: shadawck/awesome-cli-frameworks (26 languages; argument parsers and prompt libraries); awesome-python "CLI Development" (click, typer, prompt_toolkit); awesome-go "Standard CLI" vs "Advanced Console UIs" (huh)

## Full-screen TUI
- shape: keyboard-driven panes and widgets drawn on the terminal's character grid.
- e.g.: Ratatui, Bubble Tea
- source: rothgar/awesome-tuis "Libraries", grouped by language (Textual, Bubble Tea, Ratatui, FTXUI, Terminal.Gui); awesome-python "TUI Frameworks"

## Browser extension
- shape: a packaged add-on with a popup, content scripts and a background worker.
- e.g.: WXT, webextension-polyfill
- source: fregante/Awesome-WebExtensions "Libraries and Frameworks", "Boilerplates"

## Userscript
- shape: a single JS file that a manager injects into someone else's website.
- e.g.: Tampermonkey, Violentmonkey
- source: bvolpato/awesome-userscripts (managers: Tampermonkey, Violentmonkey, ScriptCat, Userscripts for Safari)

## Messenger bot
- shape: the UI is chat messages, commands and inline buttons inside a messenger.
- e.g.: aiogram, grammY
- source: ebertti/awesome-telegram "Bot Libs" (libraries in ~15 languages); awesome-go "Bot Building" (telebot, slacker)

## Super-app mini app
- shape: a web app launched inside a messenger or super-app, using its SDK, login and payments.
- e.g.: Telegram Mini Apps, WeChat Mini Programs (Taro)
- source: core.telegram.org/bots/webapps; justjavac/awesome-wechat-weapp (Taro, uni-app, WePY)

## In-chat AI app (MCP App)
- shape: a tool returns an interactive HTML view that renders inside an AI chat.
- e.g.: MCP Apps (`@modelcontextprotocol/ext-apps`), OpenAI Apps SDK
- source: MCP blog, 26 Jan 2026 (the first official MCP extension; supported in Claude, ChatGPT, Goose and VS Code)

## LLM agent app
- shape: a model-plus-tools loop does the work; the UI is a conversation or task log.
- e.g.: LangGraph, Deep Agents
- source: ThoughtWorks Radar Vol. 35 (Deep Agents, Kagent, Hindsight); roadmap.sh AI Agents and AI Engineer tracks; awesome-python "AI and Agents"; kairichard "Agentic Apps"

## Voice app
- shape: no screen; speech in, speech out, conversational turns.
- e.g.: Alexa Skills Kit, Pipecat
- source: Amazon Alexa Skills Kit ("like apps for Alexa"); pipecat-ai/pipecat (real-time voice agents)

## Visual no-code app builder
- shape: drag components and wire workflows in a hosted editor; the platform runs the app.
- e.g.: Bubble, Retool
- source: kairichard/awesome-nocode-lowcode "Web Apps", "Internal Tools", "Mobile Apps"

## Spreadsheet / database as app
- shape: a sheet or table base is the backend, with views, forms and scripts on top.
- e.g.: Airtable, AppSheet / Google Apps Script
- source: kairichard "Databases" (Airtable, NocoDB, Baserow) and "Business Apps" (AppSheet)

## Prompt-to-app generator
- shape: describe the app in chat; the platform writes, hosts and iterates the code.
- e.g.: Lovable, v0
- source: roadmap.sh "Vibe Coding" and "AI Product Builders" tracks; UI Bakery comparison of Bolt, Lovable and v0

## Editor-first game engine
- shape: a scene editor with scripting, physics and an asset pipeline; exports to many platforms.
- e.g.: Godot, Unity
- source: Calinou/awesome-gamedev "Engines"; Godot "Creating applications" docs (Godot as an Electron/Qt alternative: Pixelorama, Material Maker); roadmap.sh Game Developer

## Code-first game framework
- shape: a library for the window, input, drawing and sound; you write the game loop.
- e.g.: LÖVE, raylib / Phaser (browser)
- source: awesome-python "Game Frameworks" (pygame, pyglet, arcade), listed apart from "3D Engines"; Calinou "Engines › HTML5" (Phaser, Excalibur.js); Ask HN 2025 (LÖVE for custom UI)

## No-code game maker
- shape: event sheets or visual rules instead of code; the editor exports the game.
- e.g.: GDevelop, RPG Maker
- source: gdevelop.io ("make games without writing code", "truly unique event system")

## Fantasy console
- shape: virtual retro hardware with tight limits; code, art and sound live in one cart.
- e.g.: PICO-8, TIC-80
- source: paladin-t/fantasy (PICO-8, TIC-80, Picotron, Pyxel, WASM-4)

## Narrative / interactive-fiction engine
- shape: story text with choices or a parser; the engine handles branching, saves and presentation.
- e.g.: Ren'Py, Twine / Ink
- source: tajmone/awesome-interactive-fiction "IF Authoring Tools" (Inform, TADS, Twine, Ink); awesome-python "Visual Novels" (renpy)

## Platform-hosted game world
- shape: built in the host's studio; runs only inside its platform, for its audience.
- e.g.: Roblox Studio (Luau), Minecraft mods
- source: tech-insider "Roblox Studio vs Unity vs Godot 2026" (runs only inside Roblox; paid through DevEx)

## Creative-coding sketch / live coding
- shape: a short program that draws visuals or sound, changed live as art.
- e.g.: p5.js, Sonic Pi
- source: terkelg/awesome-creative-coding "Frameworks • Libraries", "Sound Programming Languages", "Online" (Processing, openFrameworks, nannou, Hydra)

## Node-based visual patching
- shape: wire boxes into a dataflow graph; the patch is the app.
- e.g.: TouchDesigner, Max/MSP
- source: terkelg/awesome-creative-coding "Visual Programming Languages" (TouchDesigner, vvvv, Max, Pure Data)

## Audio plugin
- shape: a DSP module with a small UI that a DAW host loads.
- e.g.: JUCE, nih-plug
- source: juce.com (VST, VST3, AU, AAX, LV2 plug-ins); Ask HN 2025 toolchains (JUCE with a webview UI for audio software)

## XR / spatial app
- shape: 3D content placed in the room or fully immersive; driven by hands, gaze and head.
- e.g.: RealityKit (visionOS), WebXR
- source: tomkrikorian/awesome-visionOS (RealityKit & ARKit; WWDC WebXR session; react-native-visionos)

## TV / 10-foot app
- shape: remote-control focus navigation on a big screen viewed from the couch.
- e.g.: Roku SceneGraph + BrightScript, tvOS SwiftUI
- source: Roku developer docs (SceneGraph XML for UI plus BrightScript for behaviour)

## Embedded / MCU display UI
- shape: UI on a microcontroller screen with ~100 kB of RAM, bare-metal or on an RTOS.
- e.g.: LVGL, Slint
- source: lvgl/lvgl (MCUs; ePaper, OLED and TFT; Zephyr, NuttX); areweguiyet "Embedded" tag; boringcactus survey (lvgl bindings)
