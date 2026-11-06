# App tech catalog

Every language, framework, engine and tool for building an app — 2,264 items, checked November 2026.

## Contents

- [1. Languages](#1-languages) — 119
- [2. Desktop GUI by language](#2-desktop-gui-by-language) — 106
- [3. Apple native (macOS, iOS, iPadOS)](#3-apple-native-macos-ios-ipados) — 49
- [4. Windows native](#4-windows-native) — 16
- [5. Linux & other desktop OS native](#5-linux--other-desktop-os-native) — 27
- [6. Web-tech desktop wrappers](#6-web-tech-desktop-wrappers) — 30
- [7. Web frontend frameworks (JavaScript/TypeScript)](#7-web-frontend-frameworks-javascripttypescript) — 72
- [8. Web UI in non-JS languages](#8-web-ui-in-non-js-languages) — 56
- [9. CSS, styling & component libraries](#9-css-styling--component-libraries) — 99
- [10. Frontend state, data & forms (JS/TS)](#10-frontend-state-data--forms-jsts) — 47
- [11. Charts, maps & data viz](#11-charts-maps--data-viz) — 49
- [12. Editors: rich text, code & canvas (JS)](#12-editors-rich-text-code--canvas-js) — 30
- [13. Web graphics, animation & media](#13-web-graphics-animation--media) — 65
- [14. Mobile native & cross-platform](#14-mobile-native--cross-platform) — 44
- [15. TUI frameworks](#15-tui-frameworks) — 47
- [16. CLI frameworks](#16-cli-frameworks) — 72
- [17. Game engines & game tech](#17-game-engines--game-tech) — 126
- [18. Backend frameworks](#18-backend-frameworks) — 178
- [19. Backend-as-a-service & app services](#19-backend-as-a-service--app-services) — 111
- [20. Databases](#20-databases) — 107
- [21. ORMs, query builders & migrations](#21-orms-query-builders--migrations) — 55
- [22. Realtime, messaging & local-first sync](#22-realtime-messaging--local-first-sync) — 57
- [23. AI & LLM app frameworks](#23-ai--llm-app-frameworks) — 105
- [24. Bots & messaging platforms](#24-bots--messaging-platforms) — 39
- [25. Browser extensions & plugin platforms](#25-browser-extensions--plugin-platforms) — 39
- [26. Low-code, no-code & AI app builders](#26-low-code-no-code--ai-app-builders) — 62
- [27. Notebooks & data apps](#27-notebooks--data-apps) — 28
- [28. Embedded & IoT](#28-embedded--iot) — 48
- [29. TV, car, wearables & XR](#29-tv-car-wearables--xr) — 31
- [30. WebAssembly](#30-webassembly) — 24
- [31. Runtimes & engines](#31-runtimes--engines) — 19
- [32. Build tools, bundlers & linters](#32-build-tools-bundlers--linters) — 42
- [33. Package managers & environments](#33-package-managers--environments) — 47
- [34. Testing & QA](#34-testing--qa) — 58
- [35. Packaging, distribution & app stores](#35-packaging-distribution--app-stores) — 50
- [36. Hosting, deployment & CI](#36-hosting-deployment--ci) — 49
- [37. Observability, analytics & feature flags](#37-observability-analytics--feature-flags) — 41
- [38. IDEs & AI coding agents](#38-ides--ai-coding-agents) — 20
- [Item counts](#item-counts)

## 1. Languages

### Mainstream app languages
- JavaScript — the web's language; runs nearly everywhere
- TypeScript — typed JavaScript; default for web apps
- Python — scripting, data, AI, backends, glue
- Java — JVM backends, Android, enterprise apps
- C# — .NET apps, Unity games, Windows
- C++ — native speed: engines, Qt, plugins
- C — systems, embedded, portable libraries
- Go — simple compiled language for services, CLIs
- Rust — memory-safe systems, CLIs, GUIs, Wasm
- Kotlin — Android default; JVM and multiplatform
- Swift — Apple platforms; also Linux, Windows servers
- PHP — web backends: WordPress, Laravel
- Ruby — Rails web apps and scripting
- Dart — Flutter's language

### Systems & performance
- Zig — C replacement with comptime, great C interop
- Odin — data-oriented language popular for games
- Nim — Python-like syntax, compiles to C/JS
- Crystal — Ruby-like syntax, compiled and typed
- D — C++ alternative with optional GC
- V — simple compiled language, fast builds
- Hare — minimal systems language, QBE backend
- C3 — evolution of C, keeps C ABI
- Carbon — Google's experimental C++ successor
- Jai — Jonathan Blow's game language; closed beta
- Mojo — Python superset for AI and GPUs
- Ada — safety-critical systems; SPARK proofs
- Fortran — scientific computing, still maintained
- Pony — actor-based, capability-safe concurrency
- Hylo — value-semantics systems language (formerly Val)
- Vale — region-based memory safety, experimental
- Jakt — SerenityOS's memory-safe language
- Inko — actor concurrency with single ownership

### JVM & .NET languages
- Scala — functional plus OO on the JVM
- Groovy — JVM scripting; Gradle and Grails
- F# — functional-first .NET language
- Visual Basic .NET — BASIC on .NET, legacy-friendly
- Ballerina — cloud integration language (WSO2)

### Scripting & embeddable
- Lua — tiny embeddable scripting; games, configs
- Luau — Roblox's typed, fast Lua
- Teal — typed Lua dialect
- Perl — text processing, legacy web
- Raku — Perl's redesigned sibling language
- Tcl — scripting with Tk GUIs
- Bash — Unix shell scripting
- PowerShell — object-based shell, Windows automation
- Nushell — structured-data shell and language
- Wren — small class-based scripting for games
- Squirrel — embeddable game scripting language
- AngelScript — C++-like embeddable game scripting
- Red — Rebol successor with built-in GUI
- Ring (language) — practical multi-paradigm language, RingQt GUIs

### Compile-to-JavaScript
- CoffeeScript — Ruby-ish JS dialect, legacy
- Civet — modern CoffeeScript-like TypeScript superset
- ReScript — fast typed language compiling to JS
- PureScript — Haskell-like, compiles to JS
- Elm — functional web language, no runtime errors
- Imba — web language with built-in tags, styles
- Haxe — compiles to JS, C++, many targets
- Reason (ReasonML) — OCaml syntax for JS developers

### Functional
- Haskell — pure functional, strong types
- OCaml — fast ML-family functional language
- Elixir — BEAM language; Phoenix, LiveView
- Erlang — fault-tolerant BEAM original
- Gleam — typed BEAM language, also targets JS
- Roc — fast friendly functional language, pre-1.0
- Idris — dependently typed programming
- Lean 4 — theorem prover and general language
- Unison — content-addressed, distributed code
- Koka — effect-typed research language (Microsoft)
- Flix — functional-logic language on JVM
- Coalton — statically typed functional inside Common Lisp

### Lisp family
- Common Lisp — mature Lisp; SBCL native compiler
- Clojure — Lisp on the JVM, immutable data
- ClojureScript — Clojure compiled to JavaScript
- Babashka — fast native Clojure scripting
- Jank — Clojure dialect on LLVM, alpha
- Racket — Scheme descendant, language workbench
- Rhombus — Racket-based language; 1.0 in 2026
- GNU Guile — GNU's Scheme, extension language
- Chicken Scheme — Scheme compiled to C
- Fennel — Lisp that compiles to Lua
- Janet — small embeddable Lisp
- Hy — Lisp on Python

### Mobile platform languages
- Objective-C — classic Apple language
- ArkTS — HarmonyOS app language, TypeScript-based

### Game & creative languages
- GDScript — Godot's Python-like language
- Verse — Epic's language for Fortnite (UEFN)
- Lobster — statically typed game-focused language

### Data & scientific
- R — statistics; Shiny apps
- Julia — fast scientific computing
- MATLAB — engineering computing; App Designer GUIs
- GNU Octave — open MATLAB-compatible language
- SQL — query language everywhere
- Wolfram Language — Mathematica's symbolic language
- APL — original array language
- BQN — modern APL dialect
- Uiua — stack-based array language, new
- J — ASCII array language
- q (kdb+) — time-series language for finance

### Logic & stack languages
- Prolog — logic programming (SWI-Prolog)
- Forth — tiny stack language for small systems
- Factor — concatenative language with GUI listener

### Parallel & experimental
- Bend — massively parallel language on HVM
- MoonBit — new language for Wasm and cloud
- Grain — functional language built for Wasm

### Education & visual
- Scratch — block-based programming for kids
- Snap! — Berkeley's advanced block language
- Blockly — Google's block-editor library (JS)
- Hedy — gradual Python-like teaching language
- Pyret — teaching language from Brown
- Microsoft Small Basic — beginner BASIC, low activity

### Legacy still shipping apps
- Delphi (Object Pascal) — RAD desktop apps (Embarcadero)
- Free Pascal — open Pascal compiler
- COBOL — banking and government backends
- Visual Basic 6 — end of life IDE; runtime lingers
- Pharo — modern live Smalltalk environment
- Squeak — classic Smalltalk with Etoys
- Eiffel — design-by-contract OO language
- Rebol — tiny messaging language, Red's ancestor

## 2. Desktop GUI by language

### Rust
- iced — Elm-style cross-platform GUI
- egui — immediate-mode GUI, easy to embed
- Slint — declarative UI DSL; also C++, JS, Python
- Dioxus — React-like; desktop, web, mobile
- Makepad — GPU UI with live design editing
- Xilem — Linebender's reactive UI, experimental
- Masonry — Linebender widget toolkit under Xilem
- Floem — reactive GUI from the Lapce team
- Freya — Dioxus components rendered with Skia
- Vizia — declarative GUI; signals since 0.4
- GPUI — Zed editor's GPU-accelerated UI framework
- gpui-component — ready-made widgets for GPUI apps
- Relm4 — Elm-style GTK 4 apps
- gtk-rs — Rust bindings for GTK
- cxx-qt — Qt/QML from Rust (KDAB)
- fltk-rs — FLTK bindings for Rust
- Ribir — non-intrusive declarative Rust GUI
- Blitz — native HTML/CSS renderer from Dioxus
- Kas — efficient retained-state Rust GUI
- Azul — CSS-styled desktop GUI, early stage
- Horizon Lattice — Qt-inspired pure-Rust GUI; 1.0 2026
- Druid — discontinued; succeeded by Xilem

### C and C++
- Qt — big cross-platform framework: Widgets + QML
- wxWidgets — native-look C++ toolkit
- Dear ImGui — immediate-mode GUI for tools
- FLTK — tiny fast C++ toolkit
- JUCE — audio apps and plugin GUIs
- U++ (Ultimate++) — C++ RAD framework with IDE
- CopperSpice — Qt fork for modern C++
- Nana — modern C++ GUI library
- Elements (Cycfi) — lightweight resolution-independent C++ GUI
- NanoGUI — minimal OpenGL widget library
- Nuklear — single-header immediate-mode C GUI
- microui — tiny immediate-mode C UI
- raygui — immediate-mode GUI for raylib
- Clay — fast C layout library for UIs
- IUP — portable C toolkit, native controls
- libui-ng — minimal native-widget C library
- RmlUi — HTML/CSS-like C++ UI for games
- NoesisGUI — XAML UI middleware for games
- Visage — GPU UI library from Vital's author

### Go
- Fyne — Material-like cross-platform Go GUI
- Gio — immediate-mode Go GUI, also mobile
- Cogent Core — Go GUI for desktop, mobile, web
- gotk4 — GTK 4 bindings for Go
- miqt — Qt Widgets bindings for Go
- giu — Dear ImGui wrapper for Go
- Walk — Windows-native widgets for Go
- Shirei — immediate-mode pure-Go GUI; new 2026

### Python
- Tkinter — built-in Tk bindings
- CustomTkinter — modern-looking Tkinter widgets
- PyQt — Riverbank's Qt bindings
- PySide — official Qt for Python
- wxPython — wxWidgets for Python
- PyGObject — GTK bindings for Python
- Kivy — touch-friendly UI, desktop and mobile
- Toga (BeeWare) — native widgets, desktop and mobile
- Flet — Flutter-rendered UI from Python
- Dear PyGui — GPU-accelerated immediate-mode Python GUI
- Dear ImGui Bundle — ImGui plus extras for Python/C++
- PySimpleGUI — simple wrapper; went commercial 2024
- FreeSimpleGUI — LGPL community fork of PySimpleGUI
- Gooey — turn argparse CLIs into GUIs

### Java & JVM
- Swing — classic JDK GUI toolkit
- JavaFX (OpenJFX) — modern JVM GUI toolkit
- SWT — Eclipse's native-widget toolkit
- AWT — original JDK toolkit, legacy
- QtJambi — Qt bindings for Java/Kotlin
- ScalaFX — Scala DSL over JavaFX
- cljfx — declarative Clojure wrapper for JavaFX
- HumbleUI — Clojure desktop UI toolkit, alpha
- TornadoFX — Kotlin JavaFX DSL; archived

### C# and .NET
- Avalonia — XAML cross-platform desktop UI
- Uno Platform — WinUI API on every platform
- Eto.Forms — native-widget cross-platform .NET UI
- Gir.Core — GTK 4 bindings for .NET
- GtkSharp — GTK 3 bindings for .NET

### JavaScript (native widgets, no webview)
- NodeGui — Qt widgets from JavaScript; low activity
- Proton Native — React for native desktop; unmaintained
- Native SDK — Vercel Labs; TypeScript compiled to native; experimental

### Swift (beyond Apple)
- SwiftCrossUI — SwiftUI-like UI across platforms
- Adwaita for Swift — GNOME apps written in Swift

### Pascal & Delphi
- VCL — Delphi's Windows-native component library
- FireMonkey (FMX) — Delphi's cross-platform GPU UI
- Lazarus — free Delphi-like IDE with LCL

### Other languages
- NiGui — native GUI toolkit for Nim
- Owlkettle — declarative GTK 4 for Nim
- Capy — native-widget GUI for Zig
- dvui — immediate-mode GUI for Zig
- monomer — Elm-style Haskell desktop GUI
- gi-gtk — Haskell GTK bindings
- LablGTK — OCaml GTK bindings
- McCLIM — Common Lisp Interface Manager
- LispWorks CAPI — commercial Common Lisp GUI
- racket/gui — Racket's built-in GUI toolkit
- Tk — Tcl's classic GUI toolkit
- Glimmer — Ruby DSL GUIs over many toolkits
- Shoes — beginner Ruby GUI; mostly dormant
- DlangUI — cross-platform D GUI; low activity
- V UI — V's cross-platform UI library
- HaxeUI — cross-framework UI for Haxe

### RAD tools & cross-platform IDEs
- Xojo — BASIC-like RAD for desktop, web, mobile
- PureBasic — compiled BASIC with native GUIs
- B4X — BASIC for Android, iOS, desktop
- LiveCode — English-like RAD; community edition ended
- C++Builder — Embarcadero RAD for C++
- 4D — RAD platform with built-in database

## 3. Apple native (macOS, iOS, iPadOS)

### UI frameworks
- SwiftUI — declarative UI for all Apple platforms
- UIKit — classic iOS/iPadOS UI framework
- AppKit — classic macOS UI framework
- Mac Catalyst — run iPad apps on Mac
- React Native macOS — Microsoft's React Native for Mac
- Observation — @Observable state for SwiftUI
- Combine — Apple's reactive streams framework
- TipKit — in-app feature tips
- Swift Charts — native declarative charts
- Core Animation — layer-based animation engine
- Core Graphics — Quartz 2D drawing
- PencilKit — Apple Pencil drawing canvas

### System integration
- WidgetKit — widgets: home, lock screen, desktop
- App Intents — Siri, Shortcuts, Spotlight actions
- ActivityKit — Live Activities and Dynamic Island
- UserNotifications — local and push notifications
- StoreKit — in-app purchases and subscriptions
- MapKit — maps, annotations, location search
- Core Location — GPS and geofencing
- HealthKit — health and fitness data
- HomeKit — smart-home accessories
- EventKit — calendars and reminders
- PhotoKit — photo library access
- AVFoundation — audio/video capture and playback
- Core Bluetooth — Bluetooth LE devices
- Network.framework — modern sockets and TLS
- ScreenCaptureKit — macOS screen and audio capture
- Virtualization framework — run Linux/macOS VMs
- GameKit — Game Center, leaderboards, multiplayer

### Data & AI
- SwiftData — Swift-native persistence over Core Data
- Core Data — object graph and persistence
- CloudKit — iCloud database and sync
- Core ML — on-device ML models
- Create ML — train models on a Mac
- Vision — image and text analysis
- NaturalLanguage — on-device text analysis
- Foundation Models — on-device Apple Intelligence LLM API

### Graphics & games
- Metal — Apple's low-level GPU API
- SpriteKit — 2D games framework
- SceneKit — 3D scenes; soft-deprecated 2025
- GameplayKit — game logic: pathfinding, state machines

### Automation & scripting
- AppleScript — classic macOS app scripting
- JXA — JavaScript for Automation on macOS
- Shortcuts — Apple's visual automation, all devices

### Tools & architecture
- Xcode — Apple's IDE, simulators, Instruments
- Swift Playgrounds — build apps on iPad or Mac
- The Composable Architecture — Point-Free's Swift state architecture
- Tuist — Xcode project generation and caching
- XcodeGen — generate Xcode projects from YAML

## 4. Windows native

### UI frameworks
- WinUI 3 — modern Windows App SDK UI
- Windows App SDK — modern APIs for desktop apps
- WPF — XAML desktop UI on .NET
- Windows Forms — classic .NET RAD UI
- UWP — maintenance mode; superseded by WinUI 3
- React Native for Windows — Microsoft's React Native for Windows
- XAML Islands — host WinUI controls in Win32

### Low-level & graphics
- Win32 API — raw Windows C API
- MFC — C++ wrapper over Win32, legacy
- WTL — lightweight C++ Win32 templates
- C++/WinRT — modern C++ projection of WinRT
- windows-rs — Rust bindings for Windows APIs
- Win2D — GPU 2D drawing for WinUI
- DirectX 12 — Windows graphics and game APIs

### Automation
- AutoHotkey — Windows hotkeys and automation scripting
- AutoIt — BASIC-like Windows GUI automation

## 5. Linux & other desktop OS native

### GNOME & GTK
- GTK — GNOME's C toolkit (GTK 4)
- libadwaita — GNOME HIG widgets for GTK 4
- Blueprint (GTK) — markup language for GTK UIs
- Cambalache — visual GTK UI designer
- Glade — legacy GTK 3 UI designer
- Workbench — GNOME code and UI playground
- Vala — C#-like language compiling to GObject C
- GJS — GNOME JavaScript bindings
- Granite — elementary OS widget library

### KDE & Qt
- KDE Frameworks — Qt add-on libraries from KDE
- Kirigami — KDE's convergent QML UI framework
- Quickshell — QML toolkit for desktop shells

### Other toolkits
- libcosmic — System76 COSMIC toolkit, built on iced
- EFL — Enlightenment Foundation Libraries (C)
- Motif — classic X11 toolkit, legacy

### Desktop widgets, bars & script UIs
- AGS (Aylur's GTK Shell) — desktop widgets in TypeScript
- Eww — ElKowar's wacky widgets, Lisp-like config
- gtk4-layer-shell — Wayland panels, bars, overlays
- Rofi — scriptable launcher and menus
- dmenu — minimal X11 menu for scripts
- Zenity — GTK dialogs from shell scripts
- KDialog — KDE dialogs from shell scripts

### Platform plumbing
- Wayland (libwayland) — Wayland protocol client library
- XCB — low-level X11 protocol bindings
- D-Bus — Linux desktop IPC bus
- xdg-desktop-portal — sandbox-safe system access portals

### Other OSes
- Haiku API — Haiku OS's native C++ kits

## 6. Web-tech desktop wrappers

### Chromium-based
- Electron — Chromium plus Node desktop apps
- NW.js — Chromium plus Node, Electron's elder peer
- CEF — Chromium Embedded Framework for native apps
- CefSharp — CEF for .NET WinForms/WPF
- JCEF — CEF for Java
- JxBrowser — commercial Chromium for Java apps
- DotNetBrowser — commercial Chromium for .NET
- MōBrowser — commercial Chromium desktop framework (TeamDev)

### System webview
- Tauri — Rust core, system webview; mobile too
- Wry — Tauri's cross-platform webview crate (Rust)
- Wails — Go backend with system webview
- Neutralinojs — tiny webview apps, any backend
- Electrobun — Bun plus Zig desktop apps; v1 2026
- Photino — lightweight webview apps, .NET first
- pywebview — webview windows from Python
- webview — tiny C/C++ webview library, many bindings
- Saucer — modern C++ webview library
- WebUI — any installed browser as GUI
- Pake — wrap any website as desktop app
- Socket Runtime — webview runtime with P2P APIs
- Elixir Desktop — LiveView apps on desktop, mobile
- Blazor Hybrid — Blazor UI in MAUI/WPF/WinForms
- WebView2 — Edge Chromium control for Windows apps
- WKWebView — Apple's WebKit view
- Eel — Python plus Chrome app mode; low activity
- Lorca — Go plus Chrome UI; archived
- Nativefier — wrap sites in Electron; archived

### Lightweight HTML engines
- Sciter — embeddable HTML/CSS/JS UI engine
- Ultralight — lightweight GPU HTML renderer

### Installable web
- Progressive Web Apps (PWA) — installable, offline-capable web apps
## 7. Web frontend frameworks (JavaScript/TypeScript)

### Component frameworks
- React — dominant component UI library (Meta)
- Vue — progressive framework with single-file components
- Svelte — compiler-first; runes in Svelte 5
- Angular — Google's full framework, now signals
- SolidJS — fine-grained reactivity with JSX
- Preact — 3 kB React-compatible library
- Qwik — resumable apps, near-zero JS
- Lit — Google's web components library
- Ember.js — convention-heavy framework, long support
- Mithril — tiny framework with routing, XHR
- Inferno — very fast React-like library
- Marko — eBay's streaming compiled UI
- Riot.js — small component library
- Hyperapp — tiny functional UI library
- Aurelia — standards-based framework
- Stencil — web components compiler (Ionic)
- FAST — Microsoft's web components foundation
- Mitosis — write once, compile to many frameworks
- Ripple — TypeScript-first compiled UI, new 2025
- Sigment — simple React alternative, new 2026
- VanJS — ~1 kB reactive UI, no build
- Arrow.js — tiny reactive templating, no build
- petite-vue — tiny Vue subset for sprinkles
- Backbone.js — early MVC library, legacy
- Knockout.js — MVVM library, legacy
- jQuery — DOM utility, still everywhere
- AngularJS — end of life since 2022

### HTML-first & hypermedia
- htmx — HTML attributes for AJAX and swaps
- Alpine.js — sprinkles of reactivity in HTML
- Hotwire — HTML-over-the-wire: Turbo + Stimulus (Rails)
- Datastar — hypermedia plus signals, SSE-driven
- Unpoly — progressive enhancement, HTML over the wire
- _hyperscript — event scripting language for HTML

### Meta-frameworks
- Next.js — React full-stack framework (Vercel)
- Nuxt — Vue full-stack framework
- SvelteKit — Svelte's app framework
- Astro — content sites, islands; Cloudflare-owned since 2026
- SolidStart — SolidJS meta-framework
- TanStack Start — type-safe React/Solid full-stack
- Analog — Angular meta-framework on Vite
- React Router — routing plus framework mode (ex-Remix v2)
- Remix — React-free v3 rewrite; RC Aug 2026
- Waku — minimal React Server Components framework
- Vike — flexible Vite SSR framework
- RedwoodSDK — React on Cloudflare, from RedwoodJS team
- One (onestack.dev) — React plus React Native, one router
- Fresh — Deno's islands framework
- Enhance — HTML-first web components framework
- Quasar — Vue: SPA, SSR, mobile, desktop
- Inertia.js — SPAs on Laravel/Rails backends
- Gatsby — React SSG; largely unmaintained

### Static sites & docs
- Hugo — fast Go static site generator
- Jekyll — Ruby SSG, GitHub Pages classic
- Eleventy — simple JS static site generator
- Zola — single-binary Rust SSG
- Hexo — Node blog framework
- Pelican — Python static site generator
- Lume — Deno static site generator
- Bridgetown — Ruby SSG, Jekyll successor
- Quartz — publish Obsidian notes as a site
- Docusaurus — Meta's React docs framework
- VitePress — Vue-powered docs generator
- Starlight — Astro docs framework
- Nextra — Next.js docs framework
- Fumadocs — Next.js docs framework
- MkDocs — Python Markdown docs; stagnant since 2024
- Material for MkDocs — maintenance mode; see Zensical
- Zensical — Rust-core SSG from Material team, 2025
- Sphinx — Python docs standard
- mdBook — Rust's Markdown book generator
- Mintlify — hosted docs platform
- GitBook — hosted docs and knowledge base

## 8. Web UI in non-JS languages

### Rust
- Leptos — fine-grained reactive full-stack Rust
- Yew — component-based Rust web UI
- Sycamore — reactive Rust web library
- MoonZoon — Rust full-stack framework

### Python
- NiceGUI — Python UI in browser, Vue/Quasar inside
- Reflex — full-stack Python (formerly Pynecone)
- Mesop — Google's Python UI framework
- Rio — React-style Python apps, no JS
- Solara — React-style Python web apps
- ReactPy — React-like components in Python
- FastHTML — HTML-first Python web apps with htmx
- PyScript — Python in HTML via Wasm
- Brython — Python 3 in the browser
- Transcrypt — Python compiled to JavaScript
- Anvil — drag-and-drop Python web apps

### Go
- templ — typed HTML templates for Go
- go-app — PWAs in Go with Wasm
- gomponents — HTML components in pure Go
- GopherJS — Go compiled to JavaScript

### C# and F#
- Blazor — C# web UI, server or Wasm
- OpenSilver — Silverlight/WPF-style XAML on Wasm
- Bolero — F# on Blazor
- Fable — F# compiled to JS, Python
- WebSharper — F# full-stack web

### Java & Kotlin
- Vaadin — Java web UI, server-driven
- Hilla — React frontends with Spring backends
- Apache Wicket — component-based Java web framework
- Jakarta Faces — server-side Java UI (JSF), legacy
- GWT — Java-to-JS toolkit, legacy
- TeaVM — Java bytecode to JS and Wasm
- KVision — Kotlin/JS web UI framework
- Kobweb — Compose HTML framework for Kotlin

### PHP
- Livewire — reactive Laravel UIs without JS
- Symfony UX — Stimulus and Live Components

### Ruby
- Phlex — Ruby view components as objects
- ViewComponent — GitHub's Rails view components

### Elixir & Gleam
- Phoenix LiveView — server-rendered realtime UIs
- Hologram — Elixir compiled to browser JS
- Lustre — Elm-style web framework for Gleam

### Elm, PureScript & Haskell
- Elm Land — Elm app framework
- elm-pages — Elm full-stack and static sites
- Halogen — PureScript UI library
- Miso — Haskell isomorphic web framework
- Reflex-FRP — Haskell FRP for web and mobile

### OCaml
- Melange — OCaml/ReasonML to JavaScript
- js_of_ocaml — OCaml bytecode to JS
- Ocsigen — OCaml full-stack (Eliom)

### Clojure
- Reagent — minimal React for ClojureScript
- re-frame — data-oriented ClojureScript framework
- Fulcro — full-stack Clojure(Script) framework
- Electric Clojure — reactive code spanning client and server

### Scala
- Scala.js — Scala compiled to JavaScript
- Laminar — reactive Scala.js UI library

### Other languages
- Karax — Nim single-page apps
- Jaspr — Dart web framework, Flutter-like
- Elementary UI — Swift frontends in the browser

## 9. CSS, styling & component libraries

### CSS frameworks
- Tailwind CSS — utility-first CSS
- Bootstrap — classic responsive CSS components
- Bulma — Flexbox CSS framework
- Foundation — Zurb's responsive framework; low activity
- UnoCSS — instant on-demand atomic CSS
- Pico CSS — minimal styles for semantic HTML
- Water.css — classless drop-in stylesheet
- Open Props — CSS custom-property design tokens
- Fomantic-UI — community fork of Semantic UI
- UIkit (YOOtheme) — modular front-end framework
- Tachyons — functional CSS, legacy

### Preprocessors & CSS-in-JS
- Sass — CSS preprocessor
- Less — CSS preprocessor, legacy
- PostCSS — CSS transform pipeline
- Lightning CSS — Rust CSS parser and minifier
- CSS Modules — locally scoped class names
- Panda CSS — zero-runtime styled-system
- Vanilla Extract — typed zero-runtime stylesheets
- StyleX — Meta's atomic CSS-in-JS
- Emotion — CSS-in-JS library
- styled-components — CSS-in-JS; maintenance mode since 2025
- Linaria — zero-runtime CSS-in-JS
- Pigment CSS — MUI's zero-runtime CSS-in-JS
- Stitches — CSS-in-JS; unmaintained

### Icons
- Lucide — clean open icon set
- Heroicons — Tailwind Labs icons
- Font Awesome — classic icon font
- Material Symbols — Google's variable icons
- Phosphor Icons — flexible icon family
- Tabler Icons — 5000+ stroke icons
- Iconify — unified access to 200k icons
- SF Symbols — Apple's system icons

### React components
- shadcn/ui — copy-in components; Base UI default 2026
- Radix UI — unstyled accessible primitives
- Base UI — unstyled primitives from MUI team
- React Aria — Adobe's accessibility hooks
- React Spectrum — Adobe's design system
- Headless UI — Tailwind Labs' unstyled components
- Ariakit — accessible primitives
- MUI — Material UI components
- Chakra UI — accessible themable components
- Mantine — 100+ components and hooks
- Ant Design — enterprise design system (Ant Group)
- HeroUI — Tailwind components (formerly NextUI)
- Fluent UI — Microsoft's design system
- Blueprint (Palantir) — dense desktop-style data UIs
- PrimeReact — big component suite
- Semi Design — ByteDance's design system
- Arco Design — ByteDance design system
- Grommet — accessible React components
- React Bootstrap — Bootstrap as React components
- Tamagui — universal UI for React Native and web
- gluestack UI — universal React Native plus web components
- Aceternity UI — copy-paste animated components
- Magic UI — animated landing-page components
- Untitled UI React — designed component library

### Vue components
- Vuetify — Material Vue components
- Element Plus — Vue 3 desktop components
- Naive UI — TypeScript Vue 3 components
- PrimeVue — big Vue component suite
- Nuxt UI — Tailwind components for Vue/Nuxt
- Reka UI — headless Vue (formerly Radix Vue)
- shadcn-vue — shadcn/ui port for Vue
- Vant — mobile Vue components

### Svelte components
- shadcn-svelte — shadcn/ui port for Svelte
- Skeleton — Tailwind design system for Svelte
- Bits UI — headless Svelte primitives
- Melt UI — headless Svelte builders

### Angular components
- Angular Material — Material components for Angular
- PrimeNG — big Angular suite
- NG-ZORRO — Ant Design for Angular
- Spartan — shadcn-style Angular primitives
- Taiga UI — Angular component kit

### Solid components
- Kobalte — accessible Solid primitives

### Multi-framework & web components
- Ark UI — headless components for React, Vue, Solid, Svelte
- Web Awesome — web components (formerly Shoelace)
- daisyUI — Tailwind component class names
- Flowbite — Tailwind components, many frameworks
- Preline UI — Tailwind components
- Material Web — Google MD3 web components; maintenance mode
- Spectrum Web Components — Adobe's web components
- Carbon Design System — IBM's design system
- Primer — GitHub's design system
- Polaris — Shopify's admin design system
- Cloudscape — AWS's design system
- Elastic UI (EUI) — Elastic's React components
- UI5 Web Components — SAP's enterprise components
- GOV.UK Frontend — UK government design system
- Lion — ING's white-label web components
- Kendo UI — Telerik commercial suite, many frameworks
- DevExtreme — DevExpress commercial JS components
- Syncfusion Essential Studio — commercial components for every platform
- Sencha Ext JS — enterprise JS framework, commercial

### Tables & grids
- AG Grid — feature-rich JS data grid
- TanStack Table — headless table logic
- Handsontable — spreadsheet-like data grid
- Glide Data Grid — canvas grid for millions of rows
- Tabulator — interactive JS tables
- Grid.js — lightweight JS table

## 10. Frontend state, data & forms (JS/TS)

### State management
- Redux Toolkit — standard Redux, less boilerplate
- Zustand — small hook-based store
- Jotai — atomic state for React
- Valtio — proxy-based state
- MobX — observable state
- XState — state machines and statecharts
- Pinia — Vue's official store
- Vuex — old Vue store; Pinia recommended
- NgRx — Redux-style Angular state
- Preact Signals — signals for Preact and React
- Alien Signals — very fast signals; powers Vue
- Legend-State — fast signals with sync
- Effector — event-driven reactive state
- Nano Stores — tiny framework-agnostic stores
- RxJS — reactive streams
- Immer — immutable updates via mutation
- Recoil — Meta's atomic state; archived 2025

### Data fetching
- TanStack Query — server-state caching
- SWR — Vercel's stale-while-revalidate hooks
- Apollo Client — GraphQL client with cache
- urql — lightweight GraphQL client
- Relay — Meta's GraphQL client
- Axios — promise-based HTTP client
- ky — tiny fetch-based HTTP client

### Forms & validation
- React Hook Form — performant React forms
- TanStack Form — type-safe headless forms
- Formik — React forms; low activity
- Conform — progressive-enhancement forms
- VeeValidate — Vue form validation
- FormKit — Vue form framework
- Superforms — SvelteKit forms
- Zod — TypeScript schema validation
- Valibot — modular tiny schema validation
- Yup — object schema validation
- ArkType — TS-syntax runtime validation

### Routing
- TanStack Router — type-safe React router
- Vue Router — official Vue router
- Wouter — tiny React router

### i18n & dates
- i18next — popular i18n framework
- FormatJS — ICU message formatting (react-intl)
- Lingui — compile-time i18n
- Paraglide JS — compiled tree-shakable i18n (inlang)
- vue-i18n — Vue internationalization
- date-fns — modular date utilities
- Day.js — 2 kB Moment alternative
- Luxon — Intl-powered dates and times
- Moment.js — legacy; maintenance mode

## 11. Charts, maps & data viz

### JavaScript charts
- D3.js — low-level data visualization toolkit
- Chart.js — simple canvas charts
- Apache ECharts — rich interactive charts
- Recharts — React charts on D3
- Nivo — React dataviz components
- visx — Airbnb's low-level React viz
- Victory — React and React Native charts
- Highcharts — commercial charting library
- Plotly.js — scientific interactive charts
- Vega-Lite — declarative grammar of graphics
- Observable Plot — concise exploratory charts
- ApexCharts — modern interactive charts
- uPlot — tiny fast time-series charts
- Lightweight Charts — TradingView financial charts
- amCharts — commercial charts and maps
- AntV G2 — grammar-of-graphics charts (Ant Group)
- LayerChart — Svelte charts
- Tremor — React dashboard components; Vercel-owned
- Perspective — streaming data viz (FINOS)
- deck.gl — WebGL large-scale data viz

### Graphs & diagrams
- Cytoscape.js — JS graph analysis and visualization
- Sigma.js — large graph rendering in JS
- vis-network — JS network diagrams
- React Flow (xyflow) — node-based editors for React/Svelte
- Mermaid — diagrams from text (JS)
- Graphviz — classic graph layout (C)
- JointJS — JS diagramming library
- GoJS — commercial JS interactive diagrams

### Charts in other languages
- Matplotlib — Python's base plotting
- Seaborn — statistical Python plots
- Bokeh — interactive Python web plots
- Altair — declarative Python charts (Vega-Lite)
- Plotly (Python) — interactive Python charts
- ggplot2 — R grammar of graphics
- Makie — Julia interactive plotting
- Plotters — Rust plotting
- ScottPlot — .NET plotting
- LiveCharts2 — animated .NET charts

### Maps
- Leaflet — classic lightweight JS web maps
- MapLibre GL JS — open vector tile maps
- Mapbox GL JS — Mapbox's vector maps
- OpenLayers — full-featured JS web mapping
- Google Maps Platform — maps, places, routes APIs
- CesiumJS — 3D globes and geospatial
- Protomaps — single-file PMTiles basemaps
- MapLibre Native — vector maps for mobile, desktop
- OpenStreetMap — open map data
- Turf.js — geospatial analysis in JS
- H3 — Uber's hexagonal geo index

## 12. Editors: rich text, code & canvas (JS)

### Rich text
- ProseMirror — toolkit for rich-text editors
- Tiptap — headless editor on ProseMirror
- Lexical — Meta's extensible editor
- Slate — customizable React editor framework
- Plate — Slate-based plugin editor
- Quill — classic rich-text editor
- CKEditor — commercial-grade WYSIWYG
- TinyMCE — classic WYSIWYG editor
- Editor.js — block-style JSON editor
- BlockNote — Notion-style block editor
- Novel — Notion-style editor with AI
- Milkdown — plugin-driven Markdown editor
- Trix — Basecamp's rich-text editor
- Draft.js — Meta's editor; archived

### Code
- Monaco Editor — VS Code's editor component
- CodeMirror — extensible browser code editor
- Ace — embeddable code editor
- Tree-sitter — incremental parsing for editors (C)
- Shiki — VS Code-grade syntax highlighting
- Prism — lightweight syntax highlighter
- highlight.js — auto-detecting syntax highlighter

### Canvas, whiteboards & page builders
- Excalidraw — hand-drawn whiteboard, embeddable
- tldraw — infinite canvas SDK
- GrapesJS — web page builder framework
- Puck — React drag-and-drop visual editor
- Craft.js — React page editor framework
- Univer — open spreadsheet and doc suite SDK

### PDF & documents
- PDF.js — Mozilla's PDF renderer
- pdf-lib — create and edit PDFs in JS
- React-pdf — PDFs from React components

## 13. Web graphics, animation & media

### 3D (JS)
- Three.js — the standard WebGL/WebGPU 3D library
- Babylon.js — Microsoft's full 3D engine
- React Three Fiber — React renderer for Three.js
- Threlte — Three.js for Svelte
- TresJS — Three.js for Vue
- OGL — minimal WebGL library
- model-viewer — 3D model web component (Google)
- Needle Engine — Unity/Blender scenes to web
- Spline — browser 3D design, embeddable scenes
- Spark — Gaussian splats in Three.js
- Filament (Google) — PBR renderer, mobile and web
- Theatre.js — motion design editor for web

### 2D (JS)
- PixiJS — fast 2D WebGL/WebGPU renderer
- Konva — interactive canvas shapes
- Fabric.js — canvas object model with editing
- Paper.js — vector graphics scripting
- Two.js — renderer-agnostic 2D drawing
- Rough.js — hand-drawn sketchy graphics
- Zdog — pseudo-3D flat illustrations
- SVG.js — SVG manipulation library

### Animation
- GSAP — pro JS animation; free since 2025
- Motion — JS animation (formerly Framer Motion)
- Anime.js — lightweight JS animation
- Lottie — After Effects animations as JSON
- Rive — interactive state-machine animations
- React Spring — spring-physics React animations
- AutoAnimate — zero-config JS transitions
- Lenis — smooth scroll library (JS)
- Remotion — make videos with React
- Motion Canvas — code-driven animated videos (TS)
- Revideo — Motion Canvas fork for video apps
- Manim — math animations in Python

### Creative coding
- p5.js — Processing for the web (JS)
- Processing — Java creative coding sketches
- openFrameworks — C++ creative coding toolkit
- Cinder — C++ creative coding library
- nannou — Rust creative coding framework
- TouchDesigner — node-based realtime visuals
- vvvv — visual live-programming environment (.NET)
- Max — Cycling '74 visual audio/media programming
- Pure Data — open visual audio programming
- cables.gl — node-based web visuals
- Hydra — live-coding video synth in browser

### Audio & video
- Tone.js — Web Audio music framework
- Howler.js — simple cross-browser audio
- wavesurfer.js — audio waveform player
- Elementary Audio — declarative audio DSP in JS
- Video.js — HTML5 video player
- hls.js — HLS streaming in browsers
- Plyr — simple accessible media player
- Sonic Pi — live-coding music (Ruby-based)
- Strudel — live-coding music patterns in browser
- SuperCollider — audio synthesis language and server

### Graphics APIs & renderers
- WebGPU — modern browser GPU API
- WebGL — browser OpenGL ES API
- Vulkan — cross-platform low-level GPU API
- OpenGL — classic cross-platform GPU API
- wgpu — Rust WebGPU implementation, native too
- Dawn — Google's C++ WebGPU implementation
- bgfx — cross-platform C++ rendering library
- sokol — single-header C graphics, app, audio
- Diligent Engine — modern cross-API graphics layer (C++)
- Skia — Google's 2D graphics engine (C++)
- Vello — GPU compute 2D renderer (Rust)
- Cairo — 2D vector graphics library (C)
## 14. Mobile native & cross-platform

### Android native
- Jetpack Compose — modern declarative Android UI (Kotlin)
- Android Views — classic XML layouts
- Android NDK — native C/C++ on Android

### Cross-platform frameworks
- Flutter — Dart UI on mobile, web, desktop
- React Native — native apps from React
- Expo — React Native framework and tooling
- Kotlin Multiplatform — share Kotlin logic everywhere
- Compose Multiplatform — Compose UI on iOS, desktop, web
- .NET MAUI — .NET cross-platform native UI
- Xamarin — .NET mobile; end of life May 2024
- Ionic Framework — web components mobile UI
- Capacitor — native runtime for web apps
- Apache Cordova — hybrid web apps, legacy but alive
- PhoneGap — discontinued 2020; use Cordova
- NativeScript — native APIs from JS/TS
- Lynx — ByteDance's dual-thread native UI (JS)
- Valdi — Snap's TSX-to-native UI; beta
- Skip — Swift/SwiftUI apps on Android too
- Framework7 — iOS/Android-style web UI
- Onsen UI — hybrid mobile UI; low activity
- Titanium SDK — JS to native, community-run
- Codename One — Java to native mobile
- Gluon Mobile — JavaFX on iOS and Android
- Felgo — Qt-based cross-platform SDK
- RubyMotion — Ruby for iOS/Android, niche

### React Native ecosystem
- Expo Router — file-based routing for React Native
- React Navigation — standard React Native navigation
- React Native Reanimated — smooth native-thread animations
- React Native Skia — Skia drawing in React Native
- React Native Paper — Material components for React Native
- NativeWind — Tailwind for React Native
- React Native Web — React Native components on web
- Ignite — Infinite Red's React Native boilerplate

### Mini programs & super-apps
- WeChat Mini Programs — apps inside WeChat
- Alipay Mini Programs — apps inside Alipay
- LINE MINI App — web apps inside LINE
- Taro — React multi-platform mini programs (JD)
- uni-app — Vue apps for mini programs, mobile

### Other mobile OSes
- ArkUI — HarmonyOS NEXT declarative UI
- KaiOS — web apps for feature phones
- Sailfish OS — Silica Qt UI for Linux phones
- Ubuntu Touch — Lomiri Linux phone platform
- Plasma Mobile — KDE on Linux phones
- Phosh — GNOME-based Linux phone shell

## 15. TUI frameworks

### Rust
- Ratatui — leading Rust TUI library
- Cursive — high-level Rust TUI views
- crossterm — cross-platform terminal manipulation
- termion — low-level Rust terminal library
- tui-realm — component framework on Ratatui
- iocraft — React-like declarative Rust TUIs
- Ratzilla — Ratatui apps in the browser

### Go
- Bubble Tea — Elm-style Go TUI (Charm)
- Bubbles — ready components for Bubble Tea
- Lip Gloss — terminal styling for Go
- tview — rich widget Go TUI
- tcell — low-level Go terminal cells
- gocui — minimalist Go console UI

### Python
- Textual — modern Python TUI framework
- urwid — classic Python console UI
- prompt_toolkit — interactive prompts and fullscreen apps
- Asciimatics — Python TUI and animations
- curses — Python stdlib curses bindings
- Blessed (Python) — terminal formatting and keyboard input
- npyscreen — form-based Python TUIs, old

### JavaScript & TypeScript
- Ink — React for terminal apps
- OpenTUI — Zig core, TS/React/Solid TUIs (opencode)
- terminal-kit — Node terminal toolkit
- blessed (Node) — curses-like Node TUI; unmaintained

### C and C++
- ncurses — classic terminal UI library
- notcurses — modern rich TUI for C
- FTXUI — functional C++ terminal UI
- Turbo Vision — modern port of Borland's TUI
- termbox2 — minimal terminal library
- ImTui — Dear ImGui in the terminal
- FINAL CUT — C++ text widget toolkit

### JVM
- Lanterna — Java curses-like library
- TamboUI — Java TUI framework, new 2026
- Mosaic — Compose for terminal UIs (Kotlin)
- Kotter — declarative Kotlin terminal UIs

### .NET
- Terminal.Gui — .NET cross-platform TUI toolkit
- Consolonia — Avalonia UI rendered in terminal

### Other languages
- libvaxis — modern Zig TUI library
- Brick — declarative Haskell TUIs
- Notty — declarative OCaml terminal graphics
- Minttea — Bubble Tea-style OCaml TUIs
- illwill — Nim terminal library
- SwiftTUI — SwiftUI-like terminal apps, experimental

### Terminal tooling
- xterm.js — terminal emulator component for web
- Wish — serve TUIs over SSH (Charm, Go)
- VHS — script terminal recordings to GIF
- asciinema — record and share terminal sessions

## 16. CLI frameworks

### Rust
- clap — full-featured argument parser
- argh — Google's derive-based minimal parser
- bpaf — combinator or derive argument parser
- pico-args — tiny zero-dependency parser
- dialoguer — interactive prompts
- inquire — interactive prompts library
- indicatif — progress bars and spinners

### Go
- Cobra — CLI framework behind kubectl, gh
- urfave/cli — simple Go CLI framework
- Kong — struct-based command parser
- Viper — config files, env, flags
- Huh — terminal forms and prompts (Charm)
- Gum — shell-script UI components (Charm)
- survey — Go prompts; archived

### Python
- Click — composable decorator-based CLIs
- Typer — type-hint CLIs on Click
- argparse — stdlib argument parser
- Python Fire — auto-CLI from any object (Google)
- Cyclopts — type-hint CLIs, Typer alternative
- docopt — CLIs from help text; unmaintained
- cmd2 — interactive command-line shells
- Cleo — Poetry's CLI framework
- Rich — rich terminal output, tables, progress
- Questionary — interactive prompts
- tqdm — progress bars everywhere

### JavaScript & TypeScript
- Commander.js — standard Node CLI framework
- yargs — argument parsing with rich help
- oclif — Salesforce's CLI framework with plugins
- citty — modern ESM CLI builder (UnJS)
- Stricli — Bloomberg's type-safe CLI framework
- cac — simple CLI builder
- meow — tiny CLI helper
- Clack — beautiful prompts
- Inquirer.js — interactive prompts
- Enquirer — stylish prompts
- Chalk — terminal colors
- Ora — terminal spinners
- Listr2 — task lists with progress
- zx — Google's shell scripting in JS
- Cliffy — Deno CLI framework

### C# and .NET
- System.CommandLine — official .NET parser
- Spectre.Console — rich console output and prompts
- CliFx — class-first .NET CLI framework
- CommandLineParser — attribute-based .NET parser
- Cocona — minimal-API-style .NET CLIs

### JVM
- picocli — annotation-based Java CLIs, GraalVM-ready
- JCommander — annotation-based Java parser
- Apache Commons CLI — classic Java option parsing
- Clikt — Kotlin CLI framework
- JLine — readline-style input for JVM
- Spring Shell — interactive Spring shells

### Ruby & PHP
- Thor — Ruby CLI toolkit (Rails generators)
- TTY Toolkit — Ruby terminal components
- Dry::CLI — Ruby command framework
- GLI — git-like Ruby command suites
- Symfony Console — PHP console component
- Laravel Zero — micro-framework for PHP CLIs
- Laravel Prompts — beautiful PHP prompts

### C and C++
- CLI11 — header-only C++ CLI parser
- cxxopts — lightweight C++ option parser
- argparse (C++) — Python-style C++ parser
- Boost.Program_options — Boost's option parsing
- getopt — POSIX C option parsing
- linenoise — tiny readline replacement (C)

### Other languages
- Swift Argument Parser — Apple's Swift CLI parser
- optparse-applicative — Haskell applicative CLI parsing
- Cmdliner — OCaml declarative CLIs
- cligen — Nim CLIs from proc signatures
- zig-clap — Zig argument parser
- tools.cli — Clojure command-line parsing
- Owl — Elixir CLI toolkit
- Bashly — generate Bash CLIs from YAML

## 17. Game engines & game tech

### Major engines
- Unreal Engine — AAA C++/Blueprints engine (Epic)
- Unity — C# engine, mobile to console
- Godot — open-source 2D/3D, GDScript/C#
- Redot — community fork of Godot
- CryEngine — Crytek's high-fidelity C++ engine
- O3DE — Open 3D Engine (Linux Foundation, C++)
- GameMaker — 2D engine with GML
- Defold — free Lua 2D/3D engine
- Cocos Creator — TS 2D/3D engine, MIT as COCOS 4
- Stride — open-source C# 3D engine
- Flax Engine — C#/C++ 3D engine
- Evergine — C# industrial 3D engine
- s&box — Facepunch's C# games on Source 2
- Wicked Engine — open C++ 3D engine
- Open Engine — C++20 MIT engine; alpha 2026
- Torque 3D — open-source legacy C++ engine

### Rendering & classic 3D engines
- OGRE — open C++ 3D rendering engine
- Panda3D — Python/C++ 3D engine
- jMonkeyEngine — Java 3D engine
- Irrlicht — legacy C++ 3D engine
- Armory3D — Blender-integrated Haxe engine
- UPBGE — Blender game engine fork

### Web engines (JS/TS)
- PlayCanvas — WebGL/WebGPU engine and editor
- Phaser — HTML5 2D games
- Excalibur.js — TypeScript 2D engine
- melonJS — lightweight HTML5 engine
- KAPLAY — fun JS games (formerly Kaboom.js)
- LittleJS — tiny fast JS engine
- Wonderland Engine — WebXR-focused web engine

### C and C++ libraries
- raylib — simple C games library
- SDL — cross-platform media layer (SDL3)
- SFML — simple C++ multimedia library
- Allegro — long-lived C game library
- Cocos2d-x — C++ 2D engine; legacy
- Axmol — maintained Cocos2d-x fork

### C#
- MonoGame — XNA successor framework
- FNA — accurate XNA reimplementation

### Rust
- Bevy — data-driven ECS engine
- Fyrox — Rust engine with scene editor
- Macroquad — simple Rust games, raylib-like
- ggez — lightweight Rust 2D framework
- gdext — Rust bindings for Godot 4

### Go & Zig
- Ebitengine — simple Go 2D engine
- Mach — Zig game engine and graphics toolkit

### Lua
- LÖVE — Lua 2D framework
- LÖVR — Lua VR framework
- Solar2D — Lua 2D mobile engine (ex-Corona)
- Gideros — Lua cross-platform engine

### Python
- Pygame — classic Python game library
- pygame-ce — community edition fork of Pygame
- pyglet — OpenGL windowing and multimedia
- Arcade — modern Python 2D library
- Ursina — easy Python 3D on Panda3D

### JVM
- libGDX — Java cross-platform framework
- LWJGL — Java bindings for OpenGL/Vulkan
- FXGL — JavaFX game engine
- KorGE — Kotlin multiplatform engine

### Haxe
- HaxeFlixel — Haxe 2D framework
- Heaps — Shiro Games' Haxe engine
- OpenFL — Flash-style API in Haxe
- Kha — low-level Haxe multimedia

### Other languages
- Flame — Flutter game engine (Dart)
- DragonRuby Game Toolkit — Ruby 2D, commercial
- Gosu — Ruby/C++ 2D library

### No-code & low-code makers
- GDevelop — open no-code game maker
- Construct 3 — browser no-code engine
- RPG Maker — classic JRPG maker
- Clickteam Fusion — event-based 2D maker
- Stencyl — block-based 2D maker
- GameSalad — drag-and-drop maker
- Buildbox — no-code 2D/3D maker
- Adventure Game Studio — point-and-click adventure maker
- Visionaire Studio — point-and-click engine
- RPG in a Box — voxel game maker
- Rosebud AI — prompt-to-game AI builder

### UGC platforms
- Roblox Studio — Luau games on Roblox
- Unreal Editor for Fortnite — Verse games inside Fortnite
- Minecraft Bedrock Add-ons — Script API mods (JS)

### Fantasy consoles & retro
- PICO-8 — Lua fantasy console
- Picotron — PICO-8 creator's fantasy workstation
- TIC-80 — open fantasy computer
- Pyxel — Python retro engine
- WASM-4 — Wasm fantasy console
- Voxatron — voxel fantasy console
- uxn — tiny VM, Varvara ecosystem
- Decker — HyperCard-like multimedia sketchpad
- Bitsy — tiny pixel narrative games
- Playdate SDK — Lua/C for Playdate
- Pulp — Playdate web game maker
- GB Studio — Game Boy games, no code
- NESmaker — NES games without assembly
- GBDK-2020 — C dev kit for Game Boy
- SGDK — Sega Genesis C dev kit
- devkitPro — Nintendo homebrew toolchains

### Interactive fiction & visual novels
- Twine — branching hypertext stories
- Ink (inkle) — narrative scripting language
- Inform 7 — natural-language parser IF
- TADS — text adventure authoring system
- ChoiceScript — choose-your-own-path games
- Yarn Spinner — dialogue for Unity/Godot
- Quest — browser text adventure maker
- Adventuron — retro text adventures
- Ren'Py — Python visual novel engine
- TyranoBuilder — no-code visual novels
- Monogatari — web visual novel engine
- articy:draft — narrative design tool

### Physics, audio & content tools
- Box2D — 2D physics engine (C)
- Jolt Physics — fast 3D physics (C++)
- PhysX — NVIDIA physics SDK
- Rapier — Rust 2D/3D physics, JS too
- Bullet — classic 3D physics (C++)
- Matter.js — JS 2D physics
- FMOD — game audio middleware
- Wwise — game audio middleware
- Tiled — tile map editor
- LDtk — modern 2D level editor
- Aseprite — pixel-art and animation editor
- Spine — 2D skeletal animation
- Blender — open 3D creation suite

### Online services & platform SDKs
- Steamworks SDK — Steam achievements, multiplayer, workshop
- Epic Online Services — free cross-platform game services
- PlayFab — Azure game backend
- Nakama — open-source game server (Go)
- Colyseus — Node multiplayer framework
- Photon — hosted multiplayer networking
- Microsoft GDK — Xbox and PC SDK
## 18. Backend frameworks

### JavaScript & TypeScript
- Express — minimal Node web framework
- Fastify — fast schema-based Node framework
- NestJS — Angular-style structured Node backend
- Koa — Express team's minimal successor
- Hono — tiny edge-first framework, any runtime
- Elysia — Bun-first ergonomic framework
- AdonisJS — Laravel-like Node framework
- hapi — configuration-centric Node framework
- Nitro — UnJS server toolkit, deploy anywhere
- Meteor — full-stack realtime JS platform
- Sails.js — Rails-like Node MVC
- Feathers — realtime REST and WebSocket APIs
- LoopBack — IBM's API framework; low activity
- Moleculer — Node microservices framework
- Encore — TS/Go backend framework with infra
- Effect — typed functional effects for TS
- Oak — Deno middleware framework
- Wasp — full-stack DSL: React, Node, Prisma

### Python
- Django — batteries-included web framework
- Flask — micro web framework
- FastAPI — type-hinted async APIs
- Litestar — performant ASGI framework
- Starlette — lightweight ASGI toolkit
- Django REST Framework — REST APIs on Django
- Django Ninja — FastAPI-style APIs on Django
- Sanic — async Python web server
- Tornado — async networking framework
- Pyramid — flexible Python web framework
- Bottle — single-file micro framework
- Falcon — minimal REST framework
- Quart — async Flask-compatible API
- aiohttp — async HTTP client and server
- Robyn — Python framework on Rust runtime

### Go
- net/http — Go standard library server
- Gin — popular fast Go router
- Echo — minimalist Go framework
- Fiber — Express-inspired Go framework
- chi — lightweight idiomatic router
- gorilla/mux — classic Go router
- Beego — full MVC Go framework
- Huma — OpenAPI-first Go APIs
- Goa — design-first Go services
- go-zero — microservices framework with codegen
- Kratos (go-kratos) — Bilibili's Go microservices framework

### Rust
- Axum — Tokio's ergonomic web framework
- Actix Web — fast actor-based framework
- Rocket — ergonomic Rust web framework
- Poem — full-featured Rust framework
- Warp — filter-based Rust framework
- Salvo — simple powerful Rust framework
- Loco — Rails-like Rust framework
- Pavex — compile-time-checked Rust framework

### Java & JVM
- Spring Boot — dominant Java framework
- Quarkus — Kubernetes-native Java, fast startup
- Micronaut — compile-time DI JVM framework
- Helidon — Oracle's microservices framework
- Jakarta EE — enterprise Java standard
- Javalin — lightweight Java/Kotlin framework
- Vert.x — reactive JVM toolkit
- Dropwizard — opinionated REST services
- Play Framework — reactive Scala/Java framework
- Ktor — Kotlin async framework (JetBrains)
- http4k — functional Kotlin HTTP toolkit
- http4s — functional Scala HTTP
- ZIO — Scala effect system and ecosystem
- Akka — actor toolkit; BSL license since 2022
- Apache Pekko — Apache-licensed Akka fork
- Grails — Groovy convention framework

### C# and .NET
- ASP.NET Core — Microsoft's web framework
- FastEndpoints — REPR-pattern .NET APIs
- ServiceStack — code-first .NET services
- ABP Framework — modular .NET app framework
- Orleans — virtual actors for distributed apps
- Aspire — .NET cloud app orchestration (ex-.NET Aspire)
- Giraffe — functional F# on ASP.NET Core

### PHP
- Laravel — elegant full-stack PHP framework
- Symfony — reusable components, enterprise PHP
- CodeIgniter — lightweight PHP framework
- Yii — high-performance PHP framework
- CakePHP — convention-over-configuration PHP
- Slim — PHP micro framework
- Laminas — enterprise PHP (formerly Zend Framework)
- Phalcon — PHP framework as C extension
- Tempest — modern PHP framework, new 2025
- Swoole — async coroutine PHP runtime
- Hyperf — coroutine framework on Swoole

### Ruby
- Ruby on Rails — convention-over-configuration full stack
- Sinatra — minimal Ruby DSL
- Hanami — modular Ruby framework
- Roda — routing-tree Ruby toolkit
- Grape — REST API DSL for Ruby
- Rage — fiber-based Ruby API framework

### Elixir, Erlang & Gleam
- Phoenix — Elixir web framework
- Ash Framework — declarative Elixir app framework
- Cowboy — Erlang HTTP server
- Wisp — Gleam web framework

### Swift
- Vapor — Swift server framework
- Hummingbird — lightweight Swift server

### C, C++ & Zig
- Drogon — fast C++ web framework
- Crow — Flask-like C++ framework
- Oat++ — C++ web framework
- Zap (Zig) — web framework on facil.io
- Jetzig — Zig MVC web framework

### Haskell & OCaml
- Servant — type-level Haskell APIs
- Yesod — type-safe Haskell web framework
- IHP — batteries-included Haskell framework
- Scotty — Sinatra-like Haskell framework
- Dream — tidy OCaml web framework

### Clojure
- Ring (Clojure) — HTTP abstraction for Clojure
- Reitit — fast data-driven router
- Biff — batteries-included Clojure web framework

### Other languages
- Kemal — Sinatra-like Crystal framework
- Lucky — type-safe Crystal framework
- Prologue — Nim web framework
- Mojolicious — real-time Perl framework
- Dancer2 — lightweight Perl framework
- OpenResty — Nginx plus LuaJIT platform
- Lapis — Lua/MoonScript web framework
- Dart Frog — minimal Dart backend (Very Good Ventures)
- Serverpod — Dart backend for Flutter apps
- Plumber — turn R code into APIs
- Genie.jl — Julia full-stack framework
- vibe.d — D async web framework
- veb — V's built-in web framework
- Hunchentoot — Common Lisp web server

### APIs & RPC
- GraphQL — typed query language for APIs
- gRPC — HTTP/2 RPC with Protobuf
- Protocol Buffers — Google's schema serialization
- Connect RPC — browser-friendly gRPC (Buf)
- tRPC — end-to-end typesafe TS APIs
- oRPC — typesafe TS RPC with OpenAPI output
- ts-rest — typed REST contracts for TS
- OpenAPI — REST API description standard
- TypeSpec — Microsoft's API description language
- Apache Thrift — cross-language RPC
- Cap'n Proto — zero-copy RPC and serialization
- Apollo Server — Node GraphQL server
- GraphQL Yoga — Node GraphQL server (The Guild)
- Pothos — code-first TS GraphQL schemas
- PostGraphile — instant GraphQL from Postgres (Node)
- Strawberry — type-hinted Python GraphQL
- gqlgen — schema-first Go GraphQL
- async-graphql — Rust GraphQL server

### Background jobs & workflows
- Temporal — durable workflow execution, many SDKs
- Cadence — Uber's workflow engine, Temporal ancestor
- Inngest — event-driven durable functions
- Trigger.dev — background jobs for TS
- Hatchet — distributed task queue on Postgres
- Restate — durable execution runtime
- DBOS — durable workflows in Postgres
- Celery — Python distributed task queue
- RQ — simple Redis queue for Python
- Sidekiq — Ruby background jobs on Redis
- Solid Queue — Rails 8 database-backed jobs
- BullMQ — Redis queues for Node
- Graphile Worker — Postgres job queue for Node
- pg-boss — Postgres job queue for Node
- Oban — Elixir jobs on Postgres
- Hangfire — .NET background jobs
- River — Go jobs on Postgres
- Asynq — Go jobs on Redis
- Apache Airflow — Python data pipeline scheduler
- Prefect — Python workflow orchestration
- Dagster — Python data asset orchestration

### Web servers & proxies
- Nginx — web server and reverse proxy
- Caddy — auto-HTTPS web server (Go)
- Apache HTTP Server — classic web server
- Traefik — cloud-native reverse proxy
- HAProxy — high-performance load balancer
- Envoy — service proxy for meshes
- Pingora — Cloudflare's Rust proxy framework
- Gunicorn — Python WSGI server
- Uvicorn — Python ASGI server
- Granian — Rust-based Python app server
- Puma — Ruby web server
- FrankenPHP — modern PHP app server on Caddy
- RoadRunner — Go-based PHP app server

### Distributed runtimes
- Dapr — portable distributed app runtime, any language

## 19. Backend-as-a-service & app services

### BaaS
- Firebase — Google's app backend suite
- Supabase — Postgres BaaS: auth, storage, realtime
- Appwrite — open-source self-hostable BaaS
- PocketBase — single-file Go backend on SQLite
- Convex — reactive TS backend and database
- Nhost — Postgres plus GraphQL BaaS
- Parse Platform — open-source BaaS, ex-Facebook
- AWS Amplify — AWS full-stack app platform
- Hasura — instant GraphQL/REST on databases
- Directus — data platform on any SQL DB
- Backendless — visual BaaS with UI builder
- Trailbase — single-binary Rust BaaS on SQLite
- Manifest — backend from one YAML file

### Auth
- Auth0 — hosted identity platform (Okta)
- Clerk — drop-in auth with UI components
- Better Auth — TS auth library; joined Vercel 2026
- Auth.js — formerly NextAuth; maintained by Better Auth
- Lucia — deprecated 2025; now an auth guide
- Keycloak — open-source identity server (Java)
- Ory Kratos — headless identity APIs (Go)
- SuperTokens — open-source auth
- WorkOS — enterprise SSO and SCIM APIs
- Stytch — passwordless auth APIs
- Zitadel — open-source identity platform
- authentik — self-hosted identity provider
- Logto — open-source auth for SaaS
- Kinde — auth plus feature flags, billing
- FusionAuth — self-hostable customer identity
- Hanko — passkey-first authentication
- OpenAuth — standards-based TS auth server (SST)
- Passport.js — Node auth strategies
- Devise — Rails authentication

### Payments & billing
- Stripe — payments, billing, checkout APIs
- Paddle — merchant of record for software
- Lemon Squeezy — merchant of record; Stripe-owned
- Polar — open-source developer payments, merchant of record
- RevenueCat — in-app subscriptions SDK
- Adyen — enterprise payments platform
- PayPal — payments, including Braintree
- Lago — open-source usage-based billing

### Email, messaging & push
- Resend — developer email API
- React Email — build emails with React
- MJML — responsive email markup
- SendGrid — Twilio's email API
- Postmark — transactional email
- Mailgun — email API
- Amazon SES — cheap bulk email
- Twilio — SMS, voice, WhatsApp APIs
- Novu — open-source notification infrastructure
- Knock — notification workflows API
- OneSignal — push, email, in-app messaging
- Firebase Cloud Messaging — free push for Android, iOS, web
- APNs — Apple Push Notification service
- ntfy — simple HTTP pub-sub push notifications
- Listmonk — self-hosted newsletter manager

### Search
- Algolia — hosted instant search
- Meilisearch — open-source instant search (Rust)
- Typesense — open-source typo-tolerant search
- Elasticsearch — distributed search and analytics
- OpenSearch — open fork of Elasticsearch
- Apache Solr — Lucene-based search server
- Tantivy — Rust search library
- Orama — in-browser and edge search (JS)
- Pagefind — static site search
- Fuse.js — fuzzy search in JS
- FlexSearch — fast full-text JS search

### Files, media & storage
- Amazon S3 — object storage standard
- Cloudflare R2 — S3-compatible, no egress fees
- Backblaze B2 — cheap object storage
- MinIO — self-hosted S3-compatible storage
- Garage — lightweight self-hosted distributed S3
- SeaweedFS — distributed file and object store
- UploadThing — file uploads for TS apps
- Uppy — JS file upload UI
- tus — resumable upload protocol
- Cloudinary — image/video transform CDN
- Mux — video streaming API

### CMS & content
- WordPress — most-used CMS, PHP
- Drupal — enterprise PHP CMS
- Joomla — PHP CMS
- Ghost — Node publishing and newsletters
- Strapi — open-source Node headless CMS
- Payload — TS headless CMS; Figma-owned since 2025
- Sanity — structured content platform
- Contentful — enterprise headless CMS
- Storyblok — visual headless CMS
- Prismic — headless CMS with slices
- Hygraph — GraphQL-native CMS (formerly GraphCMS)
- Keystatic — git-based CMS
- Decap CMS — git-based CMS (formerly Netlify CMS)
- Sveltia CMS — Decap-compatible modern git CMS
- TinaCMS — git-backed visual CMS
- KeystoneJS — TS CMS and app framework
- Craft CMS — flexible PHP CMS
- Statamic — Laravel flat-file CMS
- Kirby — file-based PHP CMS
- Grav — flat-file PHP CMS
- Umbraco — .NET CMS
- Wagtail — Django CMS
- Builder.io — visual headless CMS with AI

### E-commerce
- Shopify — hosted commerce platform
- Hydrogen — Shopify's headless React framework
- WooCommerce — WordPress commerce
- Magento Open Source — PHP commerce (Adobe Commerce)
- BigCommerce — hosted commerce platform
- Medusa — open-source TS commerce
- Saleor — GraphQL Python commerce
- Vendure — TS headless commerce
- Sylius — Symfony commerce
- PrestaShop — PHP open-source shop
- Spree Commerce — Rails commerce

## 20. Databases

### Relational
- PostgreSQL — default open relational DB
- MySQL — popular open relational DB
- MariaDB — MySQL community fork
- SQLite — embedded file database
- Microsoft SQL Server — Microsoft's relational DB
- Oracle Database — enterprise relational DB
- CockroachDB — distributed Postgres-compatible SQL
- YugabyteDB — distributed Postgres-compatible SQL
- TiDB — distributed MySQL-compatible SQL
- Vitess — MySQL sharding, YouTube origin
- PlanetScale — managed Vitess MySQL and Postgres
- Neon — serverless Postgres; Databricks-owned
- Amazon Aurora — AWS MySQL/Postgres-compatible DB
- Cloud Spanner — Google's global SQL
- Gel — graph-relational on Postgres (ex-EdgeDB); cloud shut down
- Multigres — Vitess-style Postgres scaling (Supabase), alpha
- Turso — SQLite rewrite in Rust, plus cloud
- libSQL — open-contribution SQLite fork
- Cloudflare D1 — serverless SQLite on Workers
- rqlite — distributed SQLite over Raft
- Litestream — stream SQLite backups to S3
- Dolt — Git-versioned SQL database
- H2 — embedded Java SQL database

### Postgres extensions
- pgvector — vector search in Postgres
- TimescaleDB — time-series Postgres (Tiger Data)
- ParadeDB — Elastic-style search in Postgres
- PostGIS — geospatial Postgres
- Citus — distributed Postgres extension

### Analytics
- DuckDB — embedded analytical SQL
- ClickHouse — fast columnar analytics
- Snowflake — cloud data warehouse
- BigQuery — Google serverless warehouse
- Materialize — incrementally updated SQL views
- RisingWave — streaming SQL database

### Document & wide-column
- MongoDB — leading document database
- Couchbase — document DB with mobile sync
- Apache CouchDB — HTTP/JSON DB, multi-master sync
- RavenDB — .NET-friendly document DB
- Amazon DynamoDB — serverless key-value/document store
- Cloud Firestore — Firebase's document DB
- Azure Cosmos DB — multi-model global DB
- FerretDB — MongoDB API on Postgres
- RethinkDB — realtime document DB, community-run
- ArangoDB — multi-model graph/document DB
- SurrealDB — multi-model DB with SQL-like queries
- Apache Cassandra — wide-column distributed DB
- ScyllaDB — C++ Cassandra-compatible DB
- Fauna — serverless document DB; shut down 2025

### Key-value & cache
- Redis — in-memory data store; AGPL again
- Valkey — Linux Foundation Redis fork
- Memcached — classic memory cache
- Dragonfly — multi-threaded Redis-compatible store
- Garnet — Microsoft's Redis-compatible cache
- Upstash — serverless Redis, vectors, queues
- etcd — consistent config store (Kubernetes)
- FoundationDB — ordered transactional KV (Apple)
- RocksDB — embedded LSM KV (Meta)
- LMDB — memory-mapped embedded KV
- BadgerDB — embedded Go KV
- Deno KV — built-in KV for Deno

### Graph
- Neo4j — leading graph database (Cypher)
- Memgraph — in-memory Cypher graph DB
- NebulaGraph — distributed graph DB
- JanusGraph — scalable graph on Cassandra/HBase
- Dgraph — distributed GraphQL-native graph DB
- TypeDB — strongly typed knowledge graph
- FalkorDB — graph DB, RedisGraph successor
- Amazon Neptune — managed graph DB
- Kùzu — embedded graph DB; archived Oct 2025

### Time-series
- InfluxDB — time-series DB
- QuestDB — fast SQL time-series DB
- TDengine — IoT time-series DB
- GreptimeDB — cloud-native observability DB

### Vector
- Pinecone — managed vector DB
- Weaviate — open-source vector DB
- Qdrant — Rust vector search engine
- Milvus — scalable vector DB
- Chroma — embedding DB for AI apps
- LanceDB — embedded multimodal vector DB
- turbopuffer — serverless vector/text search on S3
- Vespa — search and vector serving engine
- sqlite-vec — vector search SQLite extension
- Faiss — Meta's similarity search library

### Mobile, browser & embedded
- Realm — mobile DB; Atlas Device Sync ended 2025
- ObjectBox — on-device object DB with sync
- Isar — Flutter NoSQL DB; unmaintained
- Hive (Flutter) — key-value store; continued as Hive CE
- MMKV — Tencent's fast mobile key-value store
- LiteDB — embedded .NET NoSQL
- lowdb — tiny JSON-file DB (JS)
- PGlite — Postgres in Wasm, browser and Node
- SQLite Wasm — official SQLite browser build
- IndexedDB — browser built-in database
- Dexie.js — friendly IndexedDB wrapper

### Specialized
- Datomic — immutable Clojure DB, now free
- XTDB — bitemporal SQL database
- KurrentDB — event store (formerly EventStoreDB)
- TigerBeetle — financial transactions DB
- SpacetimeDB — database plus server for multiplayer

### Database tools
- DBeaver — universal database client
- TablePlus — native database GUI
- Beekeeper Studio — open SQL editor
- DataGrip — JetBrains database IDE
- pgAdmin — Postgres admin GUI
- Adminer — single-file PHP DB admin
- phpMyAdmin — classic MySQL web admin
- Bytebase — database DevOps, schema changes

## 21. ORMs, query builders & migrations

### JavaScript & TypeScript
- Prisma — schema-first TS ORM
- Drizzle — SQL-like TS ORM
- TypeORM — decorator-based TS ORM
- Sequelize — classic Node ORM
- MikroORM — data-mapper TS ORM
- Kysely — type-safe SQL query builder
- Knex — SQL query builder
- Objection.js — Knex-based ORM; low activity
- Mongoose (MongoDB ODM) — schemas for MongoDB
- ZenStack — Prisma plus access control

### Python
- SQLAlchemy — Python SQL toolkit and ORM
- SQLModel — SQLAlchemy plus Pydantic
- Peewee — small expressive ORM
- Tortoise ORM — async Django-like ORM
- Pony ORM — generator-based queries
- Piccolo — async ORM with admin
- Alembic — SQLAlchemy migrations
- Beanie — async MongoDB ODM

### Go
- GORM — popular Go ORM
- sqlc — generate Go from SQL
- Ent — Meta's entity framework for Go
- sqlx (Go) — extensions to database/sql
- Bun (uptrace) — SQL-first Go ORM
- pgx — Postgres driver and toolkit
- goose — Go/SQL migrations
- Atlas — database schema as code

### Rust
- Diesel — compile-time-checked ORM
- SeaORM — async dynamic ORM
- SQLx (Rust) — async compile-checked SQL
- rusqlite — SQLite bindings
- Toasty — Tokio's ORM, early preview

### JVM
- Hibernate — JPA ORM standard
- jOOQ — typesafe SQL DSL
- MyBatis — SQL mapper
- Exposed — Kotlin SQL framework (JetBrains)
- SQLDelight — typesafe Kotlin from SQL
- Room — Android SQLite persistence
- Flyway — SQL migrations
- Liquibase — database change management

### .NET
- Entity Framework Core — Microsoft's .NET ORM
- Dapper — micro-ORM by Stack Overflow
- NHibernate — .NET Hibernate port
- linq2db — LINQ-to-SQL toolkit
- Marten — Postgres document DB and event store

### Other languages
- Eloquent — Laravel's ActiveRecord ORM (PHP)
- Doctrine — PHP data mapper ORM
- Active Record — Rails ORM (Ruby)
- Sequel — Ruby SQL toolkit
- ROM — Ruby Object Mapper
- Ecto — Elixir data mapping and queries
- GRDB — Swift SQLite toolkit
- Fluent — Vapor's Swift ORM
- SQLite.swift — typesafe Swift SQLite
- Drift — reactive Dart/Flutter SQLite
- HoneySQL — Clojure SQL as data

## 22. Realtime, messaging & local-first sync

### Realtime transport & services
- ws — fast Node WebSocket library
- Socket.IO — WebSockets with fallbacks, rooms (JS)
- uWebSockets.js — very fast WebSocket server
- SignalR — .NET realtime hubs
- Action Cable — Rails WebSockets
- AnyCable — fast Action Cable server in Go
- Laravel Reverb — first-party Laravel WebSocket server
- Centrifugo — scalable realtime messaging server (Go)
- Mercure — SSE-based realtime hub
- Pusher Channels — hosted pub/sub WebSockets
- Ably — realtime messaging platform
- PubNub — realtime messaging network
- Liveblocks — multiplayer presence, comments, documents
- PartyKit — multiplayer servers; Cloudflare-owned
- Durable Objects — Cloudflare stateful edge objects
- Rivet — open-source stateful actors
- Hocuspocus — Yjs collaboration backend (Tiptap)

### Audio, video & P2P
- WebRTC — browser P2P audio, video, data
- LiveKit — open WebRTC SFU for audio and video
- Daily — WebRTC video API
- Agora — realtime voice/video SDKs
- mediasoup — Node WebRTC SFU
- Jitsi — open video meetings, embeddable
- PeerJS — simple WebRTC peers (JS)
- Pion — Go WebRTC implementation
- libp2p — modular P2P networking
- Iroh — Rust P2P QUIC connections by key
- Pear — Holepunch's P2P app runtime

### Message brokers & streaming
- Apache Kafka — distributed event log
- Redpanda — Kafka-compatible C++ streaming
- RabbitMQ — classic message broker
- NATS — lightweight messaging, JetStream
- Apache Pulsar — multi-tenant messaging and streaming
- ZeroMQ — brokerless messaging library
- Eclipse Mosquitto — MQTT broker
- EMQX — scalable MQTT broker
- Amazon SQS — managed queues
- Google Cloud Pub/Sub — managed pub/sub

### Local-first & sync engines
- Yjs — CRDT framework for collaboration (JS)
- Automerge — JSON-like CRDT documents
- Loro — fast CRDT library with rich text
- Zero — query-driven Postgres sync (Rocicorp)
- Replicache — sync framework; free, maintenance mode
- ElectricSQL — Postgres sync to clients
- PowerSync — Postgres/Mongo/MySQL to SQLite sync
- InstantDB — realtime relational client DB
- Jazz — local-first framework with CRDTs, auth
- Triplit — open-sourced; team joined Supabase 2025
- LiveStore — event-sourced reactive SQLite
- TinyBase — reactive JS store with sync
- RxDB — offline-first reactive JS DB
- PouchDB — CouchDB-syncing browser DB
- WatermelonDB — offline-first React Native DB
- Evolu — privacy-first local-first, E2E encrypted
- TanStack DB — reactive client collections, live queries
- Ditto — P2P mesh sync SDK
- Fireproof — local-first embedded document DB
## 23. AI & LLM app frameworks

### Agent frameworks
- LangChain — LLM app building blocks (Python/TS)
- LangGraph — stateful graph agents (Python/TS)
- LlamaIndex — RAG and document agents (Python/TS)
- CrewAI — role-based multi-agent teams (Python)
- Microsoft Agent Framework — merged Semantic Kernel + AutoGen, 1.0 2026
- Semantic Kernel — superseded by Microsoft Agent Framework
- AutoGen — superseded by Microsoft Agent Framework
- OpenAI Agents SDK — OpenAI's lightweight agent SDK (Python/TS)
- Claude Agent SDK — Anthropic's agent harness SDK (Python/TS)
- Google ADK — Agent Development Kit (Python, Java, Go)
- Pydantic AI — type-safe Python agents
- Mastra — TypeScript agents, workflows, RAG
- Vercel AI SDK — TS toolkit for AI UIs
- Agno — Python agents (formerly Phidata)
- smolagents — Hugging Face code agents (Python)
- Strands Agents — AWS model-driven agent SDK (Python)
- Letta — stateful agents (formerly MemGPT)
- Haystack — deepset's Python LLM pipelines
- DSPy — program LLMs, optimize prompts (Python)
- Genkit — Google's AI app framework (TS, Go)
- Spring AI — AI for Spring apps (Java)
- LangChain4j — LLM framework for Java
- Koog — JetBrains Kotlin agent framework
- Rig — Rust LLM app framework

### Structured output & prompting
- Instructor — structured outputs via Pydantic
- BAML — typed prompt-function DSL
- Outlines — constrained generation (Python)
- Guidance — Microsoft's controlled generation (Python)

### Protocols & agent UI
- MCP — Model Context Protocol for tools
- FastMCP — Pythonic MCP servers
- A2A — Agent2Agent protocol
- AG-UI — agent-to-UI event protocol
- OpenAI Apps SDK — apps inside ChatGPT, MCP-based
- CopilotKit — in-app copilots for React
- assistant-ui — React chat UI components
- Chainlit — Python chat app UI
- Open WebUI — self-hosted chat interface
- LibreChat — open multi-model chat app

### Model APIs & gateways
- OpenAI API — GPT models, Responses API
- Claude API — Anthropic's models API
- Gemini API — Google's models API
- Mistral AI — European models API
- DeepSeek API — low-cost reasoning models
- xAI API — Grok models
- Cohere — enterprise embeddings and rerank
- Amazon Bedrock — AWS hosted models
- Google Vertex AI — Google Cloud ML platform
- Azure AI Foundry — Microsoft model platform
- Groq — fast LPU inference
- Together AI — open-model inference
- Fireworks AI — fast open-model inference
- Replicate — run models by API
- fal — fast media-generation APIs
- Cloudflare Workers AI — models at the edge
- OpenRouter — one API, many models
- LiteLLM — unified LLM gateway proxy (Python)

### Voice & speech
- ElevenLabs — voice synthesis and voice agents
- Deepgram — speech-to-text APIs
- AssemblyAI — speech AI APIs
- Pipecat — voice agent pipelines (Python)
- LiveKit Agents — realtime voice agents (Python/TS)
- Vapi — hosted voice agents

### Local & on-device inference
- Ollama — run local LLMs easily
- llama.cpp — C++ LLM inference
- LM Studio — desktop app for local models
- vLLM — high-throughput LLM serving (Python)
- SGLang — fast structured LLM serving
- MLX — Apple silicon array framework
- MLC LLM — compile LLMs for any device
- WebLLM — LLMs in browser via WebGPU
- Transformers.js — Hugging Face models in JS
- ONNX Runtime — cross-platform inference
- LiteRT — on-device ML (formerly TensorFlow Lite)
- ExecuTorch — PyTorch on mobile and edge
- MediaPipe — on-device vision, audio, LLM tasks
- llamafile — single-file LLM executables (Mozilla)

### ML frameworks
- PyTorch — leading deep-learning framework
- TensorFlow — Google's ML framework
- JAX — composable transforms on accelerators
- Keras — high-level multi-backend deep learning
- scikit-learn — classic Python ML
- Hugging Face Transformers — pretrained model library (Python)

### RAG, data & memory
- Unstructured — document parsing for LLMs
- Docling — IBM document conversion (Python)
- Marker — PDF to Markdown (Python)
- Firecrawl — websites to LLM-ready data
- Crawl4AI — open LLM-friendly crawler (Python)
- Mem0 — memory layer for agents
- Zep — temporal knowledge-graph memory

### Browser agents & sandboxes
- Browser Use — LLM-driven browser automation (Python)
- Stagehand — AI browser automation SDK (TS)
- Browserbase — headless browsers for agents
- E2B — code sandboxes for agents
- Daytona — sandboxes for AI-generated code

### Visual LLM builders
- Dify — open LLM app platform
- Flowise — drag-and-drop LLM flows
- Langflow — visual LLM flow builder

### LLM observability & evals
- Langfuse — open LLM tracing and evals
- LangSmith — LangChain tracing and evals
- Helicone — LLM proxy observability
- Arize Phoenix — open LLM tracing
- Braintrust — evals and logging
- Opik — Comet's open LLM evals
- Promptfoo — LLM evals and red-teaming
- Logfire — Pydantic's observability platform

## 24. Bots & messaging platforms

### Telegram
- Telegram Bot API — official HTTP bot API
- Telegram Mini Apps — web apps inside Telegram
- TDLib — Telegram client library (C++)
- aiogram — async Python bot framework
- python-telegram-bot — popular Python wrapper
- pyTelegramBotAPI — simple sync/async Python bots
- Telethon — Python MTProto client, userbots
- Pyrogram — Python MTProto client; unmaintained
- grammY — TypeScript bot framework
- Telegraf — Node bot framework
- teloxide — Rust bot framework
- Telebot (Go) — Go bot framework

### Discord & Slack
- discord.js — Node Discord library
- discord.py — Python Discord library
- Serenity — Rust Discord library
- JDA — Java Discord API
- Discord Activities — embedded app SDK for games
- Slack Bolt — Slack app framework (JS, Python, Java)

### Other chat platforms
- WhatsApp Business Platform — official WhatsApp Cloud API
- whatsapp-web.js — unofficial WhatsApp Web automation (Node)
- Baileys — unofficial WhatsApp WebSocket library (TS)
- Messenger Platform — Meta Messenger bots
- LINE Messaging API — LINE bots
- signal-cli — Signal from the command line
- Microsoft 365 Agents Toolkit — Teams apps (ex-Teams Toolkit)
- Bot Framework — Microsoft's legacy bot SDK
- Matrix — open decentralized chat protocol
- maubot — Python Matrix bot framework
- XMPP — open messaging protocol
- Hubot — GitHub's classic chat bot (Node)

### Conversational AI platforms
- Rasa — open conversational AI framework (Python)
- Botpress — chatbot platform
- Dialogflow — Google conversational agents
- Amazon Lex — AWS chatbots
- Microsoft Copilot Studio — low-code agents
- Alexa Skills Kit — Alexa voice apps

### Open social protocols
- ActivityPub — fediverse protocol (Mastodon)
- AT Protocol — Bluesky's protocol
- Nostr — relay-based social protocol

## 25. Browser extensions & plugin platforms

### Browser extensions
- WebExtensions API — cross-browser extensions, Manifest V3
- WXT — Vite-based extension framework (TS)
- Plasmo — React extension framework
- CRXJS — Vite plugin for extensions
- Safari Web Extensions — Safari extension packaging
- Tampermonkey — userscript manager
- Violentmonkey — open userscript manager
- Bookmarklets — JS snippets as bookmarks

### Editor & IDE extensions
- VS Code Extension API — extend VS Code and forks
- IntelliJ Platform SDK — JetBrains IDE plugins
- Neovim plugins — Lua plugins for Neovim
- Emacs packages — Emacs Lisp extensions
- Zed extensions — Wasm extensions for Zed

### Productivity & desktop
- Obsidian plugins — TS plugins for Obsidian
- Logseq plugins — JS plugins for Logseq
- Raycast extensions — React extensions for Raycast
- Alfred workflows — macOS launcher automations
- Hammerspoon — macOS automation in Lua
- SwiftBar — macOS menu bar from scripts
- xbar — menu bar scripts (formerly BitBar)
- Übersicht — macOS desktop widgets in JSX
- Scriptable — iOS automation in JavaScript
- Tasker — Android automation
- Stream Deck SDK — Elgato key plugins
- Zellij plugins — Wasm terminal multiplexer plugins

### Business platforms
- Google Apps Script — JS scripts for Google Workspace
- Office Add-ins — Office.js web add-ins
- Atlassian Forge — Jira/Confluence apps
- Salesforce Platform — Apex and Lightning Web Components
- Shopify apps — extend Shopify stores
- Figma plugins — Figma plugins and widgets (TS)
- Adobe UXP — Photoshop and InDesign plugins

### Creative & audio plugins
- Blender add-ons — Python Blender extensions
- VST3 SDK — Steinberg audio plugins (C++)
- CLAP (audio) — open audio plugin standard
- nih-plug — Rust audio plugins

### Game modding
- Fabric — lightweight Minecraft mod loader (Java)
- NeoForge — Minecraft mod loader (Forge fork)
- Paper — Minecraft server plugins (Java)

## 26. Low-code, no-code & AI app builders

### Internal tools & admin
- Retool — internal tools builder
- Appsmith — open-source internal tools
- Budibase — open low-code apps
- ToolJet — open internal tools
- Windmill — scripts to apps and workflows
- Superblocks — internal tools platform
- Refine — React framework for admin apps
- React Admin — admin frontends on REST/GraphQL
- Filament (Laravel) — Laravel admin panels (PHP)
- AdminJS — Node auto admin panel
- Forest Admin — admin backend on your DB

### Spreadsheet-databases
- Airtable — spreadsheet-database apps
- NocoDB — Airtable-like UI on SQL
- Baserow — open no-code database
- Teable — Postgres-backed Airtable alternative
- Grist — relational spreadsheet
- Notion — docs plus databases as light apps
- Coda — docs as apps

### No-code app builders
- Bubble — no-code web apps
- Webflow — visual websites and CMS
- Framer — design-first websites
- WeWeb — no-code frontends on any backend
- Plasmic — visual React builder
- Glide — apps from spreadsheets
- Softr — apps on Airtable and databases
- Adalo — no-code mobile apps
- FlutterFlow — visual Flutter apps
- Draftbit — visual React Native apps
- Thunkable — no-code mobile apps
- MIT App Inventor — block-based Android/iOS apps
- Microsoft Power Apps — low-code business apps
- Google AppSheet — no-code apps from data
- OutSystems — enterprise low-code
- Mendix — enterprise low-code (Siemens)
- Zoho Creator — low-code business apps
- Claris FileMaker — database apps for teams
- Microsoft Access — legacy desktop database apps
- Xano — no-code scalable backend
- Wix Studio — website builder for agencies
- Squarespace — website builder
- Carrd — one-page sites

### Automation
- n8n — fair-code workflow automation
- Zapier — app-to-app automations
- Make — visual automation (formerly Integromat)
- IFTTT — simple consumer automations
- Pipedream — code-level integration workflows
- Activepieces — open-source Zapier alternative
- Power Automate — Microsoft workflow automation
- Node-RED — flow-based wiring for IoT and APIs

### AI app builders
- Lovable — prompt-to-full-stack web apps
- Bolt.new — StackBlitz's in-browser AI builder
- v0 — Vercel's AI app and UI builder
- Replit — cloud IDE with AI Agent
- Base44 — AI app builder; Wix-owned
- Rocket.new — AI web and mobile builder
- Firebase Studio — Google's AI full-stack workspace
- Google AI Studio — Gemini prompt-to-app builder
- Claude Artifacts — AI-built apps inside Claude
- Figma Make — prompt-to-app in Figma
- Google Stitch — AI UI designs to code
- GitHub Spark — natural-language micro apps
- Rork — AI React Native app builder

## 27. Notebooks & data apps

### Notebooks
- Jupyter — notebooks and JupyterLab
- Google Colab — hosted Jupyter with GPUs
- marimo — reactive Python notebooks and apps
- Observable — JS notebooks and Observable Framework
- Pluto.jl — reactive Julia notebooks
- Livebook — Elixir notebooks and apps
- Deepnote — collaborative data notebooks
- Hex (notebooks) — collaborative notebooks and data apps
- Quarto — publish notebooks to docs, sites
- Clerk (Clojure) — live notebooks
- Voilà — Jupyter notebooks as apps
- Evidence — BI reports from SQL plus Markdown

### Python & R data apps
- Streamlit — Python scripts to data apps
- Gradio — ML demos and apps in Python
- Dash — Plotly's Python analytical web apps
- Panel — HoloViz Python dashboards
- Shiny (R) — R web apps
- Shiny for Python — Shiny reactivity in Python
- Taipy — Python data apps and pipelines
- Vizro — low-code Dash dashboards (McKinsey)
- Datasette — publish SQLite as web app

### BI & dashboards
- Metabase — open BI and dashboards
- Apache Superset — open BI platform
- Redash — SQL dashboards; low activity
- Lightdash — dbt-native BI
- Looker Studio — Google's free dashboards
- Power BI — Microsoft BI
- Tableau — Salesforce visual analytics

## 28. Embedded & IoT

### Platforms & SDKs
- Arduino — beginner microcontroller platform
- PlatformIO — embedded build and IDE tooling
- ESP-IDF — Espressif's ESP32 framework (C)
- Raspberry Pi Pico SDK — C/C++ for RP2040/RP2350
- STM32CubeIDE — ST's STM32 IDE and HAL
- nRF Connect SDK — Nordic's Zephyr-based SDK
- Flipper Zero apps — C apps for Flipper Zero

### RTOS
- Zephyr — Linux Foundation RTOS
- FreeRTOS — ubiquitous small RTOS (AWS)
- Mbed OS — Arm's IoT OS; end of life July 2026
- RIOT — IoT operating system
- Apache NuttX — POSIX-like RTOS
- Eclipse ThreadX — RTOS (formerly Azure RTOS)

### Languages on microcontrollers
- MicroPython — Python for microcontrollers
- CircuitPython — Adafruit's beginner-friendly MicroPython
- Embassy — async Rust embedded framework
- RTIC — real-time concurrency for Rust
- esp-hal — Rust HAL for ESP32
- TinyGo — Go for microcontrollers and Wasm
- Embedded Swift — Swift subset for microcontrollers
- Nerves — Elixir embedded Linux
- Toit — managed language for ESP32
- Moddable SDK — modern JavaScript for microcontrollers
- Espruino — JavaScript interpreter for MCUs
- Johnny-Five — JS robotics; low activity
- MakeCode — Microsoft blocks/JS for micro:bit

### Embedded GUI
- LVGL — open embedded graphics library (C)
- TouchGFX — ST's embedded GUI framework
- emWin — SEGGER's embedded GUI

### Embedded Linux
- Yocto Project — custom embedded Linux builds
- Buildroot — simple embedded Linux builds
- OpenWrt — router Linux distribution
- balena — IoT fleet deployment

### Smart home & IoT cloud
- Home Assistant — open home automation (Python)
- openHAB — vendor-neutral home automation (Java)
- ESPHome — YAML firmware for ESP devices
- Tasmota — open firmware for ESP devices
- Zigbee2MQTT — Zigbee devices to MQTT
- Matter — cross-vendor smart-home standard
- MQTT — lightweight IoT pub/sub protocol
- AWS IoT Core — managed device connectivity
- Azure IoT Hub — Microsoft device cloud
- Particle — cellular IoT platform
- Blynk — IoT app builder
- Edge Impulse — TinyML on devices

### Robotics & simulation
- ROS 2 — Robot Operating System
- Gazebo — robot simulator
- Wokwi — online Arduino/ESP32 simulator

## 29. TV, car, wearables & XR

### TV
- tvOS — Apple TV apps in SwiftUI
- Compose for TV — Android TV and Google TV UI
- React Native tvOS — React Native for Apple TV, Android TV
- Roku SDK — BrightScript and SceneGraph
- Tizen — Samsung TV web/native apps
- webOS TV — LG TV web apps
- Vega OS — Fire TV's React Native OS
- Lightning JS — TV app framework (RDK)
- Google Cast SDK — cast to Chromecast

### Car
- CarPlay — iPhone apps on car screens
- Android Auto — Car App Library templates
- Android Automotive OS — Android built into cars
- Automotive Grade Linux — open car OS
- QNX — automotive and embedded RTOS

### Wearables
- watchOS — Apple Watch apps in SwiftUI
- Wear OS — Compose for Wear OS
- Garmin Connect IQ — Monkey C watch apps
- PebbleOS — open-sourced 2025, new watches
- Zepp OS — Amazfit watch apps in JS

### XR
- visionOS — Apple Vision Pro apps
- RealityKit — Apple 3D/AR rendering
- ARKit — Apple augmented reality
- Reality Composer Pro — visionOS scene editor
- ARCore — Google's AR SDK
- Android XR — Jetpack XR SDK
- Meta Spatial SDK — native Kotlin apps for Quest
- OpenXR — cross-vendor XR API standard
- WebXR — VR/AR in browsers
- A-Frame — declarative WebXR in HTML
- StereoKit — C# mixed-reality library
- Lens Studio — Snap AR lenses and Spectacles

## 30. WebAssembly

### Runtimes
- Wasmtime — Bytecode Alliance runtime (Rust)
- Wasmer — runtime plus package registry
- WasmEdge — CNCF cloud and edge runtime
- WAMR — WebAssembly Micro Runtime
- wazero — zero-dependency Go runtime
- WASI — WebAssembly system interface (0.3 async)

### Frameworks & platforms
- Spin — Fermyon's Wasm serverless framework
- wasmCloud — distributed Wasm apps (CNCF)
- Extism — cross-language Wasm plugin framework

### Toolchains
- Emscripten — C/C++ to Wasm
- wasm-bindgen — Rust–JS interop
- AssemblyScript — TypeScript-like language for Wasm
- Binaryen — Wasm optimizer and compiler infrastructure
- jco — JS tooling for Wasm components
- Javy — JS to Wasm (Shopify)
- Swift SDK for Wasm — Swift compiled to Wasm (SwiftWasm)
- Kotlin/Wasm — Kotlin to Wasm GC

### Languages & systems in the browser
- Pyodide — CPython in Wasm
- ruby.wasm — CRuby in Wasm
- CheerpJ — Java apps in the browser
- WebContainers — Node.js in the browser (StackBlitz)
- WordPress Playground — WordPress in browser via Wasm
- v86 — x86 emulator in the browser
- ffmpeg.wasm — FFmpeg in the browser

## 31. Runtimes & engines

### JavaScript
- Node.js — the server JS runtime
- Deno — secure TS-first runtime
- Bun — fast all-in-one JS runtime; Anthropic-owned
- workerd — Cloudflare Workers runtime, open source
- LLRT — AWS low-latency Lambda JS runtime
- V8 — Google's JS engine
- JavaScriptCore — WebKit's JS engine
- QuickJS — tiny embeddable JS engine
- Hermes — React Native's JS engine
- Boa — Rust JS engine

### Other languages
- CPython — reference Python
- PyPy — JIT Python
- OpenJDK — open Java runtime and JDK
- GraalVM — polyglot JVM, native images
- .NET — cross-platform runtime (ex-.NET Core)
- Mono — handed to WineHQ in 2024
- BEAM — Erlang/Elixir virtual machine
- LuaJIT — fast Lua JIT
- JRuby — Ruby on the JVM

## 32. Build tools, bundlers & linters

### JavaScript bundlers
- Vite — dev server and bundler; Rolldown in v8
- Vite+ — VoidZero unified toolchain; beta Aug 2026
- Rolldown — Rust Rollup-compatible bundler
- Rollup — ES module bundler
- webpack — veteran configurable bundler
- Rspack — Rust webpack-compatible bundler
- Rsbuild — Rspack-based build tool
- esbuild — fast Go bundler
- Turbopack — Next.js Rust bundler
- Parcel — zero-config bundler
- Farm — Rust Vite-compatible bundler
- tsdown — library bundler on Rolldown
- tsup — TS library bundler; tsdown suggested
- Metro — React Native bundler
- Trunk — Rust Wasm web bundler
- Gulp — JS task runner, legacy

### Compilers, linters & formatters
- TypeScript 7 (tsgo) — Go-native compiler, ~10x faster; stable 2026
- SWC — Rust JS/TS compiler
- Babel — JS transpiler
- Oxc — Rust JS parser, Oxlint, Oxfmt
- Biome — Rust JS linter and formatter (ex-Rome)
- ESLint — pluggable JS linter
- Prettier — opinionated code formatter
- Ruff — Rust Python linter and formatter (Astral)
- ty — Astral's fast Python type checker
- mypy — Python type checker
- Pyright — Microsoft's Python type checker

### Monorepos & build systems
- Turborepo — JS monorepo task runner
- Nx — monorepo build system
- moon — polyglot monorepo tool
- Bazel — Google's hermetic build system
- Buck2 — Meta's build system
- Pants — Python-friendly build system
- Gradle — JVM and Android builds
- Maven — classic Java builds
- CMake — C/C++ build generator
- Meson — fast C/C++ build system
- Xmake — Lua-based C/C++ build
- GNU Make — classic build tool
- Just — command runner
- Task — YAML task runner (go-task)
- Changesets — monorepo versioning and changelogs

## 33. Package managers & environments

### JavaScript
- npm — default Node package manager
- pnpm — disk-efficient package manager
- Yarn — Meta-born package manager
- JSR — modern TS-first registry
- vlt — new JS package manager and registry

### Python
- pip — standard installer
- uv — Astral's fast package manager
- Poetry — dependency and packaging tool
- PDM — PEP-compliant manager
- Hatch — Python project manager
- pipx — install Python CLI apps
- conda — cross-language package manager
- pixi — conda-based project manager
- pyenv — Python version manager

### Other languages
- Cargo — Rust builds and packages
- Go modules — Go dependency system
- NuGet — .NET packages
- Composer — PHP packages
- Bundler — Ruby gem dependencies
- Hex (hex.pm) — Elixir/Erlang packages
- pub.dev — Dart/Flutter packages
- Swift Package Manager — Swift packages
- CocoaPods — iOS deps; trunk read-only Dec 2026
- Carthage — decentralized iOS deps; low activity
- vcpkg — Microsoft's C/C++ packages
- Conan — C/C++ package manager
- opam — OCaml packages
- Cabal — Haskell packages
- Quicklisp — Common Lisp libraries
- LuaRocks — Lua packages
- CPAN — Perl modules
- CRAN — R packages
- Nimble — Nim packages

### System & toolchains
- Homebrew — macOS/Linux packages
- MacPorts — macOS ports
- Nix — reproducible packages and environments
- Devbox — Nix-powered dev environments
- mise — tool versions, env, tasks
- asdf — multi-language version manager
- nvm — Node version manager
- Volta — JS toolchain manager; unmaintained
- rustup — Rust toolchain installer
- SDKMAN! — JVM SDK manager
- Chocolatey — Windows packages
- winget — Windows Package Manager
- Scoop — Windows command-line installer
- Dev Containers — containerized dev environments spec

## 34. Testing & QA

### Unit testing
- Jest — JS testing framework
- Vitest — Vite-native JS test runner
- Mocha — flexible JS test framework
- Jasmine — BDD JS testing
- node:test — Node's built-in test runner
- pytest — Python testing
- Hypothesis — property-based Python testing
- JUnit — Java testing standard
- Kotest — Kotlin testing
- xUnit.net — .NET testing
- NUnit — .NET testing
- RSpec — Ruby BDD testing
- Minitest — Ruby's built-in testing
- PHPUnit — PHP testing
- Pest — elegant PHP testing
- Testify — Go assertions and mocks
- Ginkgo — Go BDD testing
- cargo-nextest — faster Rust test runner
- GoogleTest — C++ testing
- Catch2 — C++ testing
- XCTest — Apple testing framework
- Swift Testing — modern Swift test framework
- ExUnit — Elixir testing
- QuickCheck — original property testing (Haskell)
- fast-check — JS property-based testing

### Browser & E2E
- Playwright — cross-browser automation and testing
- Cypress — in-browser E2E testing
- Selenium — WebDriver browser automation
- WebdriverIO — WebDriver/BiDi test framework (JS)
- Puppeteer — Chrome automation (JS)
- Testing Library — user-centric DOM tests
- MSW — Mock Service Worker API mocking
- Storybook — UI component workshop
- Chromatic — visual tests for Storybook
- Percy — visual review (BrowserStack)

### Mobile
- Appium — cross-platform mobile automation
- Detox — React Native E2E tests
- Maestro — simple YAML mobile UI tests
- Espresso — Android UI tests
- XCUITest — iOS UI tests
- Patrol — Flutter native E2E tests

### API, load & contracts
- Postman — API client and testing
- Bruno — offline git-friendly API client
- Insomnia — API client (Kong)
- Hoppscotch — open web API client
- Hurl — HTTP tests in plain text
- Pact — consumer-driven contract testing
- k6 — Grafana load testing in JS
- Locust — Python load testing
- Apache JMeter — classic load testing
- Gatling — load testing as code
- Artillery — Node load testing

### Infra & quality
- Testcontainers — throwaway Docker deps in tests
- Stryker — mutation testing
- ZAP (OWASP) — open web security scanner
- BrowserStack — real-device cloud testing
- Sauce Labs — cloud testing
- Firebase Test Lab — Android/iOS device tests

## 35. Packaging, distribution & app stores

### Desktop packaging & updates
- electron-builder — package and update Electron apps
- Electron Forge — Electron build pipeline
- PyInstaller — bundle Python apps
- Nuitka — compile Python to binaries
- py2app — macOS Python app bundles
- Briefcase — BeeWare's native packaging
- cx_Freeze — freeze Python scripts
- jpackage — JDK native installers
- Conveyor — desktop packaging with auto-updates (Hydraulic)
- Velopack — installers and updates (Squirrel successor)
- Sparkle — macOS app auto-updates
- Apple notarization — notarytool signing checks
- MSIX — modern Windows packaging
- WiX Toolset — Windows MSI installers
- Inno Setup — Windows installer builder
- NSIS — scriptable Windows installers
- Flatpak — sandboxed Linux apps
- Snap — Canonical's Linux packages
- AppImage — single-file Linux apps

### Binaries & containers
- Docker — container images
- Podman — daemonless containers
- GoReleaser — release Go binaries
- dist — release Rust and other binaries (cargo-dist)
- Node SEA — Node single executable apps
- Burrito — Elixir single binaries

### Mobile delivery
- Fastlane — mobile build and release automation
- Expo EAS — cloud builds, updates, submissions
- Shorebird — Flutter code push
- TestFlight — iOS beta testing
- Firebase App Distribution — pre-release builds to testers
- Microsoft App Center — retired March 2025

### App stores
- Apple App Store — iOS/iPadOS/visionOS store
- Mac App Store — macOS store
- Google Play — Android store
- Microsoft Store — Windows store
- Steam — PC games store
- Epic Games Store — PC games store
- itch.io — indie games marketplace
- GOG — DRM-free games store
- Huawei AppGallery — HarmonyOS/Android store
- Samsung Galaxy Store — Samsung devices store
- Amazon Appstore — Fire devices; Android version ended 2025
- F-Droid — free software Android repository
- Flathub — Flatpak app store
- Chrome Web Store — Chrome extensions
- Firefox Add-ons — Firefox extensions (AMO)
- Open VSX — open VS Code extension registry
- Meta Horizon Store — Quest apps
- Setapp — Mac app subscription bundle
- AltStore PAL — alternative EU iOS marketplace

## 36. Hosting, deployment & CI

### Platforms
- Vercel — frontend cloud, Next.js home
- Netlify — Jamstack hosting
- Cloudflare Workers — edge compute; now recommended over Pages
- Render — simple PaaS
- Railway — instant deploys with databases
- Fly.io — apps near users on Machines
- Heroku — original git-push PaaS
- DigitalOcean — droplets and App Platform
- Koyeb — serverless containers and GPUs
- Northflank — containers, jobs, databases
- Deno Deploy — edge Deno hosting
- Val Town — hosted TS functions
- Modal — serverless Python and GPUs
- Hugging Face Spaces — ML demo hosting
- GitHub Pages — free static hosting
- Laravel Cloud — managed Laravel hosting
- Bunny.net — CDN and edge scripting
- Fastly Compute — Wasm edge compute

### Hyperscalers
- AWS Lambda — serverless functions
- AWS Fargate — serverless containers
- Google Cloud Run — serverless containers
- Azure App Service — managed web apps
- Hetzner — cheap dedicated and cloud servers

### Self-hosting & orchestration
- Coolify — self-hosted Heroku/Netlify alternative
- Dokploy — self-hosted PaaS
- CapRover — self-hosted PaaS
- Dokku — Docker mini-Heroku
- Kamal — deploy containers to any server
- Kubernetes — container orchestration
- Nomad — HashiCorp workload scheduler

### Infrastructure as code
- Terraform — HashiCorp IaC
- OpenTofu — open fork of Terraform
- Pulumi — IaC in real languages
- AWS CDK — AWS IaC in code
- SST — full-stack apps on AWS/Cloudflare
- Serverless Framework — serverless deploys

### Networking & tunnels
- Tailscale — private WireGuard mesh, Funnel publishing
- Cloudflare Tunnel — expose local services securely
- ngrok — tunnels to localhost

### CI/CD
- GitHub Actions — GitHub CI/CD
- GitLab CI/CD — GitLab pipelines
- CircleCI — hosted CI
- Buildkite — hybrid CI
- Jenkins — classic self-hosted CI
- Woodpecker CI — lightweight open CI
- Dagger — CI pipelines as code
- Bitrise — mobile CI/CD
- Codemagic — Flutter and mobile CI
- Xcode Cloud — Apple's CI/CD

## 37. Observability, analytics & feature flags

### Errors & APM
- Sentry — error and performance monitoring
- GlitchTip — open Sentry-compatible tracker
- Datadog — full observability SaaS
- New Relic — APM platform
- Honeycomb — high-cardinality tracing
- Bugsnag — error monitoring (SmartBear)
- Firebase Crashlytics — mobile crash reports
- LogRocket — session replay, frontend monitoring

### Open observability
- OpenTelemetry — vendor-neutral telemetry standard
- Prometheus — metrics and alerting
- Grafana — dashboards for everything
- Loki — Grafana log aggregation
- Jaeger — distributed tracing
- SigNoz — open OTel-native APM
- VictoriaMetrics — fast metrics storage
- Kibana — Elastic dashboards
- Fluent Bit — lightweight log shipper
- Vector — Datadog's observability data pipeline
- Better Stack — logs, uptime, incidents
- Axiom — event data and logs

### Uptime
- Uptime Kuma — self-hosted uptime monitor
- Healthchecks.io — cron job monitoring
- Checkly — synthetic monitoring as code

### Product analytics
- PostHog — open product analytics suite
- Mixpanel — event analytics
- Amplitude — product analytics
- Google Analytics 4 — web analytics
- Plausible — privacy-friendly analytics
- Umami — open web analytics
- Matomo — self-hosted analytics
- Fathom — privacy-first analytics
- Hotjar — heatmaps and recordings
- Microsoft Clarity — free heatmaps and replays
- Segment — customer data pipeline (Twilio)
- RudderStack — open customer data platform

### Feature flags & experiments
- LaunchDarkly — feature flag platform
- Statsig — flags and experiments; OpenAI-owned
- GrowthBook — open flags and A/B tests
- Unleash — open feature flags
- Flagsmith — open flags and remote config
- OpenFeature — vendor-neutral feature flag API

## 38. IDEs & AI coding agents

### IDEs & editors
- VS Code — Microsoft's extensible editor
- Visual Studio — full .NET/C++ IDE
- JetBrains IDEs — IntelliJ, PyCharm, WebStorm, Rider and more
- Android Studio — Android IDE
- Zed — fast collaborative Rust editor
- Cursor — AI-first VS Code fork
- Windsurf — AI IDE; Cognition-owned

### AI coding agents
- Claude Code — Anthropic's agentic coding CLI
- OpenAI Codex — OpenAI's coding agent
- GitHub Copilot — AI pair programmer and agent
- Gemini CLI — Google's terminal coding agent
- Google Antigravity — Google's agent-first IDE
- Jules — Google's async coding agent
- Kiro — AWS spec-driven AI IDE
- Aider — terminal AI pair programmer
- Cline — VS Code coding agent
- Roo Code — Cline-derived VS Code agent
- opencode — open terminal coding agent
- Amp — Sourcegraph-born coding agent
- Devin — Cognition's autonomous software engineer

## Item counts

| # | Section | Items |
|---|---|---|
| 1 | Languages | 119 |
| 2 | Desktop GUI by language | 107 |
| 3 | Apple native (macOS, iOS, iPadOS) | 49 |
| 4 | Windows native | 16 |
| 5 | Linux & other desktop OS native | 27 |
| 6 | Web-tech desktop wrappers | 30 |
| 7 | Web frontend frameworks (JavaScript/TypeScript) | 72 |
| 8 | Web UI in non-JS languages | 56 |
| 9 | CSS, styling & component libraries | 99 |
| 10 | Frontend state, data & forms (JS/TS) | 47 |
| 11 | Charts, maps & data viz | 49 |
| 12 | Editors: rich text, code & canvas (JS) | 30 |
| 13 | Web graphics, animation & media | 65 |
| 14 | Mobile native & cross-platform | 44 |
| 15 | TUI frameworks | 47 |
| 16 | CLI frameworks | 72 |
| 17 | Game engines & game tech | 126 |
| 18 | Backend frameworks | 178 |
| 19 | Backend-as-a-service & app services | 111 |
| 20 | Databases | 107 |
| 21 | ORMs, query builders & migrations | 55 |
| 22 | Realtime, messaging & local-first sync | 57 |
| 23 | AI & LLM app frameworks | 105 |
| 24 | Bots & messaging platforms | 39 |
| 25 | Browser extensions & plugin platforms | 39 |
| 26 | Low-code, no-code & AI app builders | 62 |
| 27 | Notebooks & data apps | 28 |
| 28 | Embedded & IoT | 48 |
| 29 | TV, car, wearables & XR | 31 |
| 30 | WebAssembly | 24 |
| 31 | Runtimes & engines | 19 |
| 32 | Build tools, bundlers & linters | 42 |
| 33 | Package managers & environments | 47 |
| 34 | Testing & QA | 58 |
| 35 | Packaging, distribution & app stores | 50 |
| 36 | Hosting, deployment & CI | 49 |
| 37 | Observability, analytics & feature flags | 41 |
| 38 | IDEs & AI coding agents | 20 |
| | **Total** | **2,265** |
