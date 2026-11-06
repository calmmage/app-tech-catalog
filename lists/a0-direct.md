# App Tech Catalog

Every way to build an app: languages, GUI toolkits, TUI/CLI, web, mobile, macOS native, Electron & co, game engines, backends, data, tooling, distribution.
Format: `Name — language · note`. Sections are grouped by what you are building.

---

## 1. Languages

### Mainstream
- JavaScript — web, Node, everywhere
- TypeScript — typed JavaScript
- Python
- Java
- Kotlin — Android, JVM, multiplatform
- Swift — Apple platforms, also Linux/Windows
- Objective-C — legacy Apple
- C
- C++
- C#
- Go
- Rust
- Dart — Flutter
- PHP
- Ruby
- SQL

### Systems / performance
- Zig
- Odin
- Nim
- V
- Crystal — Ruby-like, compiled
- D
- Carbon — experimental C++ successor
- Hare
- C3
- Jai — closed beta
- Vale
- Mojo — Python-like, for AI/perf
- Hylo — formerly Val
- Inko
- Pony
- Ada / SPARK
- Fortran
- Free Pascal
- Delphi (Object Pascal)
- Assembly — x86-64, ARM64, RISC-V

### JVM / .NET family
- Scala
- Groovy
- Clojure
- F#
- VB.NET

### Functional
- Haskell
- OCaml
- ReasonML
- ReScript
- Elm
- PureScript
- Elixir
- Erlang
- Gleam — BEAM + JS targets
- LFE — Lisp Flavoured Erlang
- Roc
- Unison
- Koka
- Idris
- Agda
- Lean 4
- Rocq — formerly Coq
- F*
- Futhark — GPU arrays
- Grain — WebAssembly
- MoonBit — WebAssembly-first

### Lisps
- Common Lisp — SBCL, LispWorks
- Scheme — Guile, Chez, Chicken, Gambit
- Racket
- ClojureScript
- Emacs Lisp
- Janet
- Fennel — Lisp → Lua
- Hy — Lisp → Python

### Scripting / embeddable
- Lua
- Luau — Roblox
- Teal — typed Lua
- MoonScript
- Perl
- Raku
- Tcl
- Wren
- Squirrel
- AngelScript
- Haxe
- Io
- Red / Rebol
- Starlark

### Shells
- Bash
- Zsh
- Fish
- PowerShell
- Nushell
- Elvish
- Oils (OSH / YSH)
- xonsh
- AWK

### Data / science
- R
- Julia
- MATLAB
- GNU Octave
- Wolfram Language
- SAS
- Cython
- Codon — compiled Python
- Taichi
- Triton — GPU kernels
- Halide
- Chapel

### Array languages
- APL (Dyalog)
- J
- K / q (kdb+)
- BQN
- Uiua

### Logic
- Prolog (SWI-Prolog)
- Mercury
- Datalog / Soufflé

### Old-school & rapid-app languages
- COBOL
- Smalltalk — Pharo, Squeak
- Eiffel
- Forth
- Factor
- FreeBASIC
- QB64
- PureBasic
- B4X — B4A / B4i / B4J
- Xojo
- LiveCode
- Visual Basic 6 / VBA
- AutoHotkey
- AutoIt
- AppleScript
- ActionScript 3 — Adobe AIR

### Compile-to-JS
- CoffeeScript
- Civet
- LiveScript
- Imba
- Mint
- Fable — F# → JS
- Scala.js
- Kotlin/JS
- js_of_ocaml / Melange
- GopherJS

### GPU / shader
- GLSL
- HLSL
- WGSL
- Metal Shading Language
- CUDA
- OpenCL
- Slang

### Game-engine scripting
- GDScript — Godot
- Blueprints — Unreal visual scripting
- Verse — Fortnite UEFN

### Narrative / interactive fiction
- Ink
- Inform 7
- Yarn — Yarn Spinner
- ChoiceScript
- Twine story formats — Harlowe, SugarCube

### Smart contracts
- Solidity
- Vyper
- Move
- Cairo

### Hardware description
- Verilog / SystemVerilog
- VHDL
- Chisel

### Config / infra languages
- Nix
- HCL
- CUE
- Dhall
- Jsonnet
- Pkl

### Visual / block programming
- Scratch
- Snap!
- Blockly
- MIT App Inventor
- Kodular
- LabVIEW (G)

---

## 2. Prototyping & mockups
- Figma
- Penpot — open source
- Sketch — macOS
- Framer
- ProtoPie
- Origami Studio
- Principle
- Axure RP
- Balsamiq
- Adobe XD — maintenance mode
- Lunacy
- Whimsical
- Excalidraw
- tldraw
- Uizard
- Google Stitch
- v0
- Lovable
- Bolt.new
- Claude Artifacts
- Rive — interactive animation
- Spline — 3D for web
- LottieFiles
- Storybook
- Ladle
- Histoire — Vue/Svelte stories
- Anima — design → code
- Locofy — design → code
- Builder.io — visual CMS / design → code
- Plasmic — visual React builder

---

## 3. Desktop GUI — by language

### Rust
- Iced — Elm architecture, wgpu; powers COSMIC desktop
- egui / eframe — immediate mode
- Slint — declarative DSL; also C++, JS, Python
- Dioxus — React-like; desktop, web, mobile
- GPUI — Zed editor's GPU UI framework
- Xilem / Masonry — Linebender, Druid successor
- Druid — archived
- Floem — from the Lapce editor
- Makepad — GPU, live-coded design
- Freya — Dioxus + Skia
- Vizia — reactive; audio plugin UIs
- Relm4 — Elm-style on GTK4
- gtk4-rs / gtk-rs
- fltk-rs
- Kas
- Ribir
- libcosmic — System76 toolkit on Iced
- cxx-qt — Qt from Rust (KDAB)
- native-windows-gui
- objc2 / cacao — AppKit from Rust
- Blitz — HTML/CSS renderer (Dioxus)
- winit — windowing
- Wry / Tao — Tauri's webview and window libs

### C / C++
- Qt Widgets
- Qt Quick / QML
- GTK
- wxWidgets
- FLTK
- Dear ImGui
- Nuklear
- microui
- raygui
- Clay — layout library
- NanoGUI
- RmlUi — HTML/CSS-like UI for games
- Ultimate++
- JUCE — audio apps and plugins
- Nana
- Elements (cycfi)
- IUP
- libui-ng
- Sciter — HTML/CSS engine for desktop
- Ultralight — lightweight HTML UI
- Noesis GUI — XAML for games
- CopperSpice — Qt fork
- saucer — modern C++ webview
- webview/webview — tiny cross-platform webview

### Go
- Fyne
- Gio
- Wails — Go + web UI
- Cogent Core
- giu — Dear ImGui wrapper
- gotk4 — GTK4 bindings
- walk — Windows
- DarwinKit — AppKit from Go (formerly MacDriver)
- Energy — Go + CEF
- Lorca — Chrome as UI, archived

### Python
- Tkinter
- CustomTkinter
- ttkbootstrap
- PySide6 — Qt for Python
- PyQt6
- wxPython
- Kivy / KivyMD
- BeeWare Toga
- Dear PyGui
- Flet — Flutter under the hood
- NiceGUI — browser-rendered
- pywebview
- Eel
- PySimpleGUI — went commercial
- PyGObject — GTK
- PyObjC — Cocoa
- rumps — macOS menu bar apps
- Gooey — argparse → GUI
- Enaml
- Remi
- Rio

### .NET (C# / F#)
- WPF
- WinForms
- WinUI 3
- UWP — legacy
- Avalonia
- Uno Platform
- .NET MAUI
- Eto.Forms
- GtkSharp / Gir.Core
- Blazor Hybrid
- Photino.NET
- Xamarin.Forms — end of life 2024
- Fabulous — F# MVU

### JVM
- JavaFX (OpenJFX)
- Swing
- SWT
- Compose Multiplatform Desktop — Kotlin
- TornadoFX — Kotlin + JavaFX, archived
- Seesaw — Clojure Swing

### JavaScript / TypeScript (non-browser native)
- React Native for macOS
- React Native for Windows
- NodeGui — Qt
- Sciter.js

### Dart
- Flutter desktop — macOS, Windows, Linux

### Other languages
- Nim — NiGui, nimx, owlkettle (GTK4)
- Zig — capy, dvui, zgui
- Odin — vendor:microui, raylib
- Haskell — monomer, gi-gtk, threepenny-gui
- OCaml — lablgtk3
- Elixir — Scenic, Elixir Desktop, :wx
- Clojure — cljfx, HumbleUI
- Racket — racket/gui
- Common Lisp — McCLIM, LTK, LispWorks CAPI
- D — DlangUI, GtkD
- V — V UI
- Julia — GLMakie, Gtk4.jl, Blink.jl
- Swift (cross-platform) — SwiftCrossUI, Adwaita for Swift
- Tcl — Tk
- Lua — IUP, wxLua
- Pascal — Lazarus LCL, Delphi VCL, Delphi FireMonkey
- Smalltalk — Pharo Spec2
- Perl — Perl/Tk, Prima
- Ruby — Glimmer DSLs, Shoes, ruby-gnome
- PHP — NativePHP (Electron/Tauri)
- Haxe — HaxeUI

---

## 4. Web-tech desktop wrappers (Electron & co)
- Electron
- Electron Forge
- electron-builder
- electron-vite
- electron-updater
- Electron Fiddle
- Tauri — Rust core, system webview; v2 adds mobile
- Wails — Go
- Neutralinojs
- NW.js
- Electrobun — Bun + system webview
- Socket Runtime
- Pake — wrap any website via Tauri
- Nativefier — archived
- CEF — Chromium Embedded Framework
- WebView2 — Windows
- WKWebView — macOS / iOS
- WebKitGTK — Linux
- Capacitor Electron — community
- Fluid — macOS site-specific browser
- Unite — macOS web apps
- WebCatalog
- PWA install — "Add to Dock" / "Install app"

---

## 5. macOS & Apple native

### UI frameworks
- SwiftUI
- AppKit
- UIKit — iOS/iPadOS
- Mac Catalyst — iPad app on Mac
- Cocoa (Objective-C)
- Interface Builder — storyboards / XIB
- MenuBarExtra — SwiftUI menu bar apps
- WidgetKit
- App Intents — Shortcuts, Siri, Spotlight
- App Extensions — Share, Finder Sync, Quick Look, Safari
- Live Activities / Dynamic Island
- App Clips

### Graphics, ML, media
- Metal
- Core Animation
- Core Graphics
- Core Image
- SpriteKit — 2D games
- SceneKit — 3D, soft-deprecated 2025
- RealityKit
- ARKit
- GameplayKit
- AVFoundation
- Vision
- Core ML
- Create ML
- Foundation Models — on-device LLM (2025)

### Data & architecture
- SwiftData
- Core Data
- CloudKit
- GRDB — SQLite
- Combine
- The Composable Architecture (TCA)
- RxSwift

### Tooling
- Xcode
- Swift Package Manager
- CocoaPods — winding down
- Carthage
- Tuist
- XcodeGen
- Swift Playgrounds
- Sparkle — auto-updates outside the App Store
- Fastlane

### Scripting, menu bar & automation
- AppleScript
- JXA — JavaScript for Automation
- Shortcuts
- Automator
- Hammerspoon — Lua
- SwiftBar
- xbar (formerly BitBar)
- Übersicht — desktop widgets
- Raycast extensions — React/TS
- Alfred workflows
- Platypus — script → .app
- swiftDialog
- Keyboard Maestro
- BetterTouchTool
- Karabiner-Elements
- launchd agents — background jobs
- .NET for macOS — Xamarin.Mac successor

### Other Apple targets
- iOS / iPadOS — SwiftUI, UIKit
- watchOS — SwiftUI
- tvOS
- visionOS — SwiftUI + RealityKit
- CarPlay

---

## 6. Windows native
- Win32 API
- MFC
- ATL / WTL
- C++/WinRT
- Windows App SDK
- XAML Islands
- DirectX / Direct2D
- windows-rs — Rust
- PowerShell + WPF/WinForms
- AutoHotkey GUIs
- HTA — legacy HTML Applications
- PowerToys Command Palette extensions
- Rainmeter — desktop widgets

---

## 7. Linux native
- GTK4
- libadwaita
- Qt / KDE Frameworks
- Kirigami — KDE convergent UI
- Granite — elementary OS
- GJS — GNOME JavaScript
- Vala
- Blueprint — GTK UI markup
- Cambalache — UI designer
- Glade — legacy
- GNOME Builder
- Workbench — GTK playground
- EFL — Enlightenment
- Motif
- Xlib / XCB
- smithay-client-toolkit — Wayland
- Waybar
- AGS — Aylur's GTK Shell
- eww — widgets
- Quickshell — QML shell widgets
- Conky
- Plasma widgets (plasmoids)
- GNOME Shell extensions
- zenity / YAD / kdialog — script dialogs

---

## 8. Mobile — native
- Swift + SwiftUI — iOS
- UIKit — iOS
- Kotlin + Jetpack Compose — Android
- Android Views (XML layouts)
- Java — Android
- Android NDK — C/C++
- Material 3
- Jetpack — Room, Navigation, WorkManager, Hilt
- Glance — Android widgets
- Compose for Wear OS
- Compose for TV

## 9. Mobile — cross-platform
- React Native
- Expo
- Expo Router
- Expo EAS — builds & updates
- Flutter
- Kotlin Multiplatform
- Compose Multiplatform — iOS + Android
- .NET MAUI
- Uno Platform
- Avalonia (mobile)
- Ionic
- Capacitor
- Apache Cordova
- NativeScript
- Lynx — ByteDance
- Tamagui
- React Native Web
- Skip — SwiftUI → Android
- Tauri v2 mobile
- Dioxus mobile
- Titanium SDK
- Solar2D
- Framework7
- Onsen UI
- Quasar
- uni-app
- Taro
- Hotwire Native
- Unity as a Library
- Codename One — Java
- Xamarin — end of life

### React Native ecosystem
- NativeWind
- gluestack UI (formerly NativeBase)
- React Native Paper
- Reanimated
- React Native Skia
- Unistyles
- React Navigation

### Flutter ecosystem
- Riverpod
- Bloc
- Provider
- GetX
- go_router
- Drift
- Isar
- Hive
- Flame — 2D games

---

## 10. Web frontend

### UI libraries
- React
- Vue
- Angular
- Svelte
- Solid
- Preact
- Qwik
- Lit — Web Components
- Stencil
- FAST — Microsoft Web Components
- Alpine.js
- htmx
- Datastar
- _hyperscript
- Hotwire — Turbo + Stimulus
- Unpoly
- Ember
- Backbone
- Knockout
- Mithril
- Inferno
- Marko
- Riot
- Aurelia
- Hyperapp
- VanJS
- Arrow.js
- petite-vue
- jQuery
- Vanilla Web Components
- Million.js
- Mitosis — write once, compile to frameworks
- Ext JS
- OpenUI5 / SAPUI5
- Polymer — legacy

### Meta-frameworks / full-stack JS
- Next.js
- Nuxt
- SvelteKit
- SolidStart
- React Router v7 (Remix)
- TanStack Start
- Astro
- Qwik City
- Analog — Angular
- Gatsby
- RedwoodJS / RedwoodSDK
- Blitz.js
- Waku
- Vike
- Fresh — Deno
- Enhance
- Meteor
- Wasp — full-stack DSL
- T3 Stack

### Web UI in non-JS languages
- Leptos — Rust
- Yew — Rust
- Dioxus web — Rust
- Sycamore — Rust
- Perseus — Rust
- go-app — Go
- Vugu — Go
- Vecty — Go
- templ — Go
- gomponents — Go
- Blazor WebAssembly — C#
- Blazor Server — C#
- Bolero — F#
- Fable + Elmish — F#
- Feliz — F#
- Laminar — Scala.js
- Tyrian — Scala.js
- Compose for Web (Kotlin/Wasm)
- Kobweb — Kotlin
- KVision — Kotlin
- Reagent — ClojureScript
- re-frame — ClojureScript
- UIx — ClojureScript
- Halogen — PureScript
- Lustre — Gleam
- Jaspr — Dart
- Flutter Web — Dart
- Phoenix LiveView — Elixir
- Laravel Livewire — PHP
- Inertia.js — Laravel/Rails + SPA
- StimulusReflex — Rails
- Django Unicorn — Python
- Vaadin — Java
- GWT — Java
- JSF / PrimeFaces — Java
- Apache Wicket — Java
- Seaside — Smalltalk

### Python data / quick web apps
- Streamlit
- Gradio
- Dash (Plotly)
- Panel (HoloViz)
- Shiny for Python
- Reflex
- Mesop
- FastHTML
- Solara
- Taipy
- Anvil
- Voilà
- PyScript
- Pyodide

### R / Julia web apps
- Shiny (R)
- Genie.jl / Stipple
- Pluto.jl

### Static sites & docs
- Hugo
- Jekyll
- Eleventy
- Zola
- Hexo
- Pelican
- Lume
- Bridgetown
- Middleman
- Nikola
- Hakyll
- mdBook
- MkDocs / Material for MkDocs
- Sphinx
- Docusaurus
- VitePress
- Starlight
- Nextra
- Fumadocs
- Mintlify
- GitBook
- Quarto
- Jupyter Book
- Observable Framework
- Evidence
- Slidev
- reveal.js
- Marp

### CSS & styling
- Tailwind CSS
- UnoCSS
- Bootstrap
- Bulma
- Foundation
- Pico CSS
- Open Props
- Sass
- Less
- PostCSS
- Lightning CSS
- CSS Modules
- styled-components
- Emotion
- vanilla-extract
- Panda CSS
- StyleX
- Stitches

### Component libraries
- shadcn/ui
- Radix UI
- Base UI
- Headless UI
- Ark UI
- React Aria / React Spectrum
- MUI
- Chakra UI
- Mantine
- Ant Design
- Fluent UI
- Carbon
- Blueprint
- Semantic UI
- PrimeReact / PrimeVue / PrimeNG
- Vuetify
- Quasar
- Element Plus
- Naive UI
- Angular Material
- daisyUI
- Flowbite
- HeroUI (formerly NextUI)
- Park UI
- Kobalte — Solid
- Melt UI / Bits UI — Svelte
- Skeleton — Svelte
- Web Awesome (formerly Shoelace)
- Spectrum Web Components
- Material Web
- Kendo UI
- DevExtreme
- Syncfusion

### State, data fetching, routing, forms
- Redux / Redux Toolkit
- Zustand
- Jotai
- Recoil — archived
- MobX
- XState
- Valtio
- Pinia
- Vuex
- NgRx
- Effector
- Nanostores
- Preact Signals
- Legend State
- TanStack Query
- SWR
- Apollo Client
- urql
- Relay
- tRPC
- TanStack Router
- React Router
- Vue Router
- React Hook Form
- Formik
- TanStack Form
- Zod
- Valibot
- Yup
- ArkType

### Tables, drag-and-drop, editors
- AG Grid
- TanStack Table
- Handsontable
- Glide Data Grid
- MUI X Data Grid
- dnd kit
- Pragmatic drag and drop
- SortableJS
- react-dnd
- Tiptap
- ProseMirror
- Lexical
- Slate
- Plate
- Quill
- CKEditor
- TinyMCE
- Editor.js
- BlockNote
- Milkdown
- CodeMirror
- Monaco Editor

### Animation
- Motion (formerly Framer Motion)
- GSAP
- Anime.js
- Lottie
- Rive runtime
- React Spring
- AutoAnimate
- View Transitions API

### 2D / 3D / canvas
- Three.js
- React Three Fiber
- Babylon.js
- PlayCanvas
- A-Frame
- PixiJS
- Konva
- Fabric.js
- Paper.js
- p5.js
- tldraw SDK
- Excalidraw (embed)
- React Flow (xyflow)
- Cytoscape.js
- Sigma.js
- Mermaid

### Charts & maps
- D3
- Chart.js
- ECharts
- Plotly.js
- Recharts
- visx
- Observable Plot
- Vega / Vega-Lite
- Highcharts
- ApexCharts
- Nivo
- uPlot
- Tremor
- deck.gl
- Mapbox GL JS
- MapLibre
- Leaflet
- OpenLayers
- CesiumJS

---

## 11. Browser extensions & plugin platforms
- WebExtensions API (Manifest V3)
- Plasmo
- WXT
- CRXJS
- Extension.js
- web-ext — Firefox
- Safari Web Extensions
- VS Code extensions
- JetBrains plugins
- Zed extensions
- Neovim plugins — Lua
- Emacs packages — Elisp
- Sublime Text plugins — Python
- Obsidian plugins
- Figma plugins
- Raycast extensions
- Alfred workflows
- Slack apps
- Discord Activities
- Notion integrations
- Shopify apps
- Office Add-ins (Office.js)
- Google Workspace add-ons
- Telegram Mini Apps
- WeChat Mini Programs
- Alipay Mini Programs
- Stream Deck plugins
- Home Assistant integrations
- Chrome DevTools extensions

---

## 12. TUI frameworks (terminal UIs)

### Go
- Bubble Tea — Elm architecture (Charm)
- Lip Gloss — styling (Charm)
- Bubbles — components (Charm)
- Huh — forms (Charm)
- Glamour — markdown rendering (Charm)
- tview
- tcell
- termui
- gocui
- termbox-go
- pterm

### Rust
- Ratatui
- crossterm
- termion
- termwiz
- Cursive
- tui-realm
- iocraft — React-like
- r3bl_tui
- inquire — prompts
- dialoguer — prompts
- indicatif — progress bars
- console

### Python
- Textual
- Rich
- prompt_toolkit
- urwid
- curses
- blessed
- npyscreen
- asciimatics
- PyTermGUI
- pyTermTk
- py_cui
- picotui
- Questionary
- InquirerPy
- tqdm — progress bars
- alive-progress

### JavaScript / TypeScript
- Ink — React for terminals
- Ink UI
- Pastel — Ink app framework
- OpenTUI — powers opencode
- Blessed
- neo-blessed
- blessed-contrib — dashboards
- react-blessed
- Terminal-kit
- @clack/prompts
- Inquirer.js
- Enquirer
- prompts
- chalk
- ora — spinners
- listr2 — task lists
- cli-progress

### C / C++
- ncurses
- PDCurses
- notcurses
- FTXUI
- termbox2
- Turbo Vision (tvision)
- FINAL CUT
- ImTui — Dear ImGui in terminal
- CDK — Curses Development Kit
- newt
- dialog
- whiptail

### .NET
- Terminal.Gui
- Spectre.Console
- Consolonia — Avalonia in terminal
- Sharprompt

### JVM
- Lanterna
- JLine
- Jexer
- Mosaic — Jetpack Compose for terminal (Kotlin)
- Kotter — Kotlin

### Others
- Brick — Haskell
- vty — Haskell
- Notty / Nottui — OCaml
- Minttea — OCaml Bubble Tea port
- Ratatouille — Elixir
- Owl — Elixir CLI toolkit
- TTY toolkit (tty-prompt…) — Ruby
- Laravel Prompts — PHP
- php-tui — PHP
- SwiftTUI — Swift
- TermKit — Swift
- illwill — Nim
- libvaxis — Zig
- Term.jl — Julia
- TerminalUserInterfaces.jl — Julia
- Curses::UI — Perl
- gum — shell scripts (Charm)
- fzf — fuzzy picker for any script

---

## 13. CLI frameworks (argument parsing, commands)

### Rust
- clap
- argh
- pico-args
- bpaf

### Go
- Cobra
- Fang — Cobra starter kit (Charm)
- urfave/cli
- Kong
- Kingpin
- pflag

### Python
- Click
- Typer
- argparse
- Cyclopts
- docopt
- Python Fire
- Cleo
- Cement

### JavaScript / TypeScript
- Commander.js
- yargs
- oclif
- citty
- cac
- meow
- Clipanion
- Gluegun
- Cliffy — Deno

### JVM
- picocli
- JCommander
- Clikt — Kotlin
- kotlinx-cli

### .NET
- System.CommandLine
- CommandLineParser
- Spectre.Console.Cli
- Cocona

### Ruby / PHP
- Thor
- OptionParser
- dry-cli
- GLI
- Symfony Console
- Laravel Zero

### C / C++
- CLI11
- cxxopts
- argparse (C++)
- Boost.Program_options
- getopt

### Others
- Swift Argument Parser
- optparse-applicative — Haskell
- Cmdliner — OCaml
- cligen — Nim
- zig-clap — Zig

---

## 14. Game engines & frameworks

### Big general engines
- Unity — C#
- Unreal Engine — C++ / Blueprints
- Godot — GDScript / C#
- Redot — Godot fork
- GameMaker — GML
- Defold — Lua
- Cocos Creator — TS
- Cocos2d-x — C++
- CryEngine
- O3DE — Open 3D Engine
- Stride — C#
- Flax — C# / C++
- Unigine
- Source 2 / s&box — C#
- Wicked Engine

### Rust
- Bevy — ECS
- Fyrox
- macroquad
- miniquad
- ggez
- Piston
- Notan
- Tetra
- Comfy
- nannou — creative coding
- wgpu

### C / C++ libraries
- raylib
- SDL (SDL3)
- SFML
- Allegro
- sokol
- bgfx
- Ogre
- Irrlicht
- Magnum
- Diligent Engine
- The Forge
- Filament — rendering
- Hazel — educational

### Lua
- LÖVE
- Solar2D
- Gideros
- Roblox Studio — Luau

### JavaScript / TypeScript (web games)
- Phaser
- PixiJS
- Babylon.js
- PlayCanvas
- Three.js
- Excalibur.js
- KAPLAY (Kaboom successor)
- melonJS
- Kontra
- LittleJS
- Wonderland Engine — WebXR
- Needle Engine

### Python
- Pygame / pygame-ce
- Arcade
- Pyglet
- Panda3D
- Ursina
- Pyxel — retro

### JVM
- libGDX
- jMonkeyEngine
- KorGE — Kotlin
- LWJGL

### .NET
- MonoGame
- FNA
- Nez
- Raylib-cs
- Silk.NET

### Go / Zig / others
- Ebitengine — Go
- Pixel — Go
- G3N — Go
- Mach — Zig
- Heaps — Haxe
- HaxeFlixel — Haxe
- OpenFL — Haxe
- Kha — Haxe
- Armory3D — Haxe + Blender
- Ceramic — Haxe

### No-code / low-code game makers
- Construct 3
- GDevelop
- Buildbox
- Stencyl
- Clickteam Fusion
- RPG Maker
- GB Studio — Game Boy games
- Adventure Game Studio
- Bitsy

### Visual novels & interactive fiction
- Ren'Py
- TyranoBuilder
- Naninovel — Unity
- Twine
- Ink / Inky
- Inform 7
- Yarn Spinner
- ChoiceScript

### Fantasy consoles
- PICO-8
- Picotron
- TIC-80
- WASM-4

### Platforms inside other games
- Fortnite UEFN — Verse
- Minecraft mods — Fabric, NeoForge
- Roblox

---

## 15. Graphics APIs & low-level rendering
- OpenGL
- OpenGL ES
- Vulkan
- Metal
- DirectX 12
- WebGL
- WebGPU
- Dawn — WebGPU in C++
- ANGLE
- MoltenVK — Vulkan on Mac
- Skia
- Impeller — Flutter renderer
- Cairo
- NanoVG
- Blend2D
- Vello — GPU 2D (Rust)
- femtovg
- tiny-skia
- GLFW

---

## 16. Creative coding & audio apps
- Processing
- openFrameworks
- Cinder
- TouchDesigner
- vvvv
- Max/MSP
- Pure Data
- Hydra — live visuals
- Shadertoy
- Sonic Pi
- TidalCycles
- Strudel
- SuperCollider
- Csound
- ChucK
- Faust
- VCV Rack
- iPlug2 — audio plugins
- DPF — audio plugins
- nih-plug — Rust audio plugins
- Web Audio API
- Tone.js
- Elementary Audio

---

## 17. Backend frameworks

### JavaScript / TypeScript
- Express
- Fastify
- Koa
- Hapi
- NestJS
- Hono
- Elysia — Bun
- AdonisJS
- Sails
- LoopBack
- Feathers
- Nitro / h3
- Oak — Deno

### Python
- Django
- Django REST Framework
- Django Ninja
- Flask
- FastAPI
- Starlette
- Litestar
- Sanic
- Tornado
- aiohttp
- Pyramid
- Bottle
- Falcon
- Quart
- Robyn
- BlackSheep
- CherryPy
- Uvicorn / Gunicorn / Granian — servers

### Ruby
- Ruby on Rails
- Sinatra
- Hanami
- Roda
- Grape

### PHP
- Laravel
- Symfony
- CodeIgniter
- CakePHP
- Yii
- Slim
- Laminas
- Phalcon
- WordPress
- Drupal
- Statamic
- FrankenPHP — server
- RoadRunner — server
- Swoole

### Go
- net/http
- Gin
- Echo
- Fiber
- Chi
- Gorilla Mux
- Beego
- Buffalo
- Iris
- Encore
- Huma
- Goa
- go-kit
- Kratos
- go-zero

### Rust
- Axum
- Actix Web
- Rocket
- Warp
- Poem
- Salvo
- Loco — Rails-like
- Pavex
- Spin — Fermyon, Wasm

### JVM
- Spring Boot
- Quarkus
- Micronaut
- Helidon
- Vert.x
- Javalin
- Dropwizard
- Play Framework
- Jakarta EE
- Ktor — Kotlin
- http4k — Kotlin
- Pekko HTTP / Akka HTTP — Scala
- ZIO HTTP — Scala
- http4s — Scala

### .NET
- ASP.NET Core
- Minimal APIs
- FastEndpoints
- Carter
- Orleans — actors
- ServiceStack
- Giraffe — F#
- Saturn — F#
- Falco — F#

### Elixir / Erlang / Gleam
- Phoenix
- Ash Framework
- Plug
- Cowboy
- Wisp — Gleam

### Others
- Vapor — Swift
- Hummingbird — Swift
- Serverpod — Dart
- Dart Frog — Dart
- Shelf — Dart
- Kemal — Crystal
- Lucky — Crystal
- Jester — Nim
- Prologue — Nim
- Zap — Zig
- http.zig — Zig
- Ring — Clojure
- Pedestal — Clojure
- Biff — Clojure
- Yesod — Haskell
- Servant — Haskell
- Scotty — Haskell
- IHP — Haskell
- Dream — OCaml
- Mojolicious — Perl
- Dancer2 — Perl
- Catalyst — Perl
- Drogon — C++
- Crow — C++
- Oat++ — C++
- cpp-httplib — C++
- Boost.Beast — C++
- Mongoose — C
- OpenResty — Lua + Nginx
- Lapis — Lua
- Plumber — R
- Genie.jl — Julia
- veb (vweb) — V
- Hunchentoot — Common Lisp

---

## 18. Backend-as-a-service, CMS, auth, payments

### BaaS & instant backends
- Firebase
- Supabase
- Appwrite
- PocketBase — single Go binary
- Convex
- Nhost
- Parse Platform
- AWS Amplify
- Hasura
- PostgREST
- InstantDB
- Triplit
- Jazz
- Xata

### Headless CMS
- Strapi
- Payload CMS
- Directus
- Sanity
- Contentful
- KeystoneJS
- Ghost
- Decap CMS
- TinaCMS

### Auth
- Clerk
- Auth0
- WorkOS
- Better Auth
- Auth.js (NextAuth)
- Kinde
- Stytch
- Ory
- Keycloak
- SuperTokens
- Firebase Auth
- Supabase Auth
- Passkeys / WebAuthn

### Payments & subscriptions
- Stripe
- Paddle
- Lemon Squeezy
- Polar
- RevenueCat — mobile subscriptions
- StoreKit 2 — Apple
- Google Play Billing

---

## 19. Databases

### Relational
- PostgreSQL
- MySQL
- MariaDB
- SQLite
- libSQL / Turso
- DuckDB
- SQL Server
- Oracle
- CockroachDB
- YugabyteDB
- TiDB
- Neon — serverless Postgres
- PlanetScale

### Document / key-value
- MongoDB
- CouchDB
- PouchDB
- Couchbase
- Redis
- Valkey
- Dragonfly
- KeyDB
- Memcached
- DynamoDB
- Firestore
- FoundationDB
- etcd

### Wide-column / analytics / time series
- Cassandra
- ScyllaDB
- ClickHouse
- TimescaleDB
- InfluxDB
- QuestDB
- Apache Druid
- Apache Pinot
- Snowflake
- BigQuery

### Multi-model / graph
- SurrealDB
- Gel (formerly EdgeDB)
- Neo4j
- ArangoDB
- Dgraph
- Memgraph

### Search
- Elasticsearch
- OpenSearch
- Meilisearch
- Typesense
- Algolia

### Vector
- pgvector
- Qdrant
- Weaviate
- Pinecone
- Milvus
- Chroma
- LanceDB

### Embedded / on-device
- Realm — deprecated
- ObjectBox
- RxDB
- WatermelonDB
- IndexedDB
- Dexie.js
- LevelDB
- RocksDB
- LMDB
- sled — Rust
- redb — Rust

---

## 20. ORMs & query builders
- Prisma — TS
- Drizzle — TS
- TypeORM — TS
- Sequelize — JS
- Kysely — TS
- Knex — JS
- MikroORM — TS
- SQLAlchemy — Python
- SQLModel — Python
- Django ORM — Python
- Peewee — Python
- Tortoise ORM — Python
- Active Record — Ruby
- Sequel — Ruby
- Eloquent — PHP
- Doctrine — PHP
- GORM — Go
- sqlc — Go
- Ent — Go
- sqlx — Go
- Bun — Go
- Diesel — Rust
- SeaORM — Rust
- SQLx — Rust
- Hibernate — Java
- jOOQ — Java
- MyBatis — Java
- Exposed — Kotlin
- Entity Framework Core — C#
- Dapper — C#
- Ecto — Elixir
- Room — Android
- Drift — Dart

---

## 21. APIs, realtime, messaging, jobs
- REST / OpenAPI
- GraphQL
- gRPC
- Connect RPC
- tRPC
- JSON-RPC
- Protocol Buffers
- Cap'n Proto
- Apache Thrift
- Apache Avro
- WebSockets
- Socket.IO
- Server-Sent Events
- WebRTC
- WebTransport
- MQTT
- Apollo Server
- GraphQL Yoga
- Pothos
- Strawberry — Python GraphQL
- gqlgen — Go GraphQL
- async-graphql — Rust
- Phoenix Channels
- SignalR
- Centrifugo
- Pusher
- Ably
- PartyKit
- Soketi
- NATS
- Apache Kafka
- RabbitMQ
- Redis Streams
- ZeroMQ
- Temporal
- Inngest
- Trigger.dev
- BullMQ
- Celery
- Sidekiq
- Oban

## 22. Local-first & sync
- Yjs
- Automerge
- Loro
- Liveblocks
- Zero (Rocicorp)
- Replicache
- ElectricSQL
- PowerSync
- TinyBase
- ShareDB
- Evolu

---

## 23. AI / LLM app frameworks
- Claude Agent SDK
- OpenAI Agents SDK
- Google ADK
- Vercel AI SDK
- Mastra
- LangChain
- LangGraph
- LlamaIndex
- Haystack
- DSPy
- Pydantic AI
- Semantic Kernel
- AutoGen
- CrewAI
- smolagents
- Agno
- Letta
- Instructor
- Outlines
- Guidance
- BAML
- LiteLLM
- MCP SDKs / FastMCP
- assistant-ui
- CopilotKit
- Chainlit
- Open WebUI
- Ollama
- llama.cpp
- vLLM
- MLX — Apple Silicon
- LM Studio
- Hugging Face Transformers
- Transformers.js
- ONNX Runtime
- Langfuse — tracing

## 24. Bots & chat apps
- aiogram — Telegram, Python
- python-telegram-bot
- pyTelegramBotAPI
- Telethon — Telegram user API
- Pyrogram
- grammY — Telegram, TS
- Telegraf — Telegram, JS
- teloxide — Telegram, Rust
- telebot — Telegram, Go
- discord.js
- discord.py
- Pycord
- Serenity — Discord, Rust
- Poise — Discord, Rust
- JDA — Discord, Java
- Discord.Net
- Slack Bolt
- Microsoft Bot Framework
- Botpress
- Rasa
- WhatsApp Cloud API
- Baileys — WhatsApp
- whatsapp-web.js
- Matrix SDKs
- Mastodon.py

---

## 25. Low-code / no-code / AI app builders
- Bubble
- Webflow
- Framer Sites
- FlutterFlow
- Adalo
- Glide
- Softr
- Thunkable
- Draftbit
- Wix Studio
- Squarespace
- WordPress + Elementor
- WeWeb
- Xano — no-code backend
- Noodl
- Power Apps
- OutSystems
- Mendix
- AppSheet
- Airtable Interfaces
- Notion
- Lovable
- Bolt.new
- v0
- Replit Agent
- Base44
- Google AI Studio apps

### Internal tools & admin panels
- Retool
- Appsmith
- ToolJet
- Budibase
- Jet Admin
- React Admin
- Refine
- AdminJS
- Django Admin
- Filament — Laravel
- Laravel Nova
- ActiveAdmin / Avo — Rails
- Grafana
- Metabase
- Apache Superset
- Redash

### Automation & workflows
- n8n
- Zapier
- Make
- Node-RED
- Pipedream
- Windmill
- Activepieces

### Notebooks, spreadsheets & office scripting
- Jupyter
- marimo
- Observable
- Hex
- Deepnote
- Google Colab
- Google Apps Script
- Excel VBA
- Office Scripts
- Airtable scripting
- LibreOffice Basic

---

## 26. Embedded, IoT & hardware UI
- LVGL
- TouchGFX
- Embedded Wizard
- Qt for MCUs
- Slint (embedded)
- emWin
- µGFX
- Arduino
- PlatformIO
- ESP-IDF
- ESPHome
- MicroPython
- CircuitPython
- Zephyr RTOS
- FreeRTOS
- Embassy — async Rust embedded
- RTIC — Rust
- TinyGo
- Espruino
- Nerves — Elixir
- Raspberry Pi + Qt/PyQt kiosk

## 27. TV, car, wearables, XR
- Android TV / Google TV
- Fire TV
- Roku SceneGraph — BrightScript
- Samsung Tizen
- LG webOS
- Lightning.js — TV apps in JS
- Android Auto
- Android Automotive OS
- Wear OS
- Garmin Connect IQ — Monkey C
- OpenXR
- WebXR
- Meta Spatial SDK
- Unity XR Interaction Toolkit
- Snap Lens Studio
- TikTok Effect House

## 28. Blockchain dApps
- Hardhat
- Foundry
- ethers.js
- viem
- wagmi
- RainbowKit
- thirdweb
- Anchor — Solana
- solana-web3.js

---

## 29. WebAssembly
- Emscripten
- wasm-bindgen / wasm-pack
- AssemblyScript
- WASI
- Wasmtime
- Wasmer
- WasmEdge
- Extism — Wasm plugins
- Uno Platform WASM
- Kotlin/Wasm

---

## 30. Runtimes, build tools, package managers

### JavaScript
- Node.js
- Deno
- Bun
- Vite
- Webpack
- Rollup
- Rolldown
- esbuild
- SWC
- Babel
- Parcel
- Turbopack
- Rspack
- Rsbuild
- Farm
- tsup
- tsdown
- unbuild
- Nx
- Turborepo
- Lerna
- npm
- pnpm
- Yarn
- Biome
- Oxc / oxlint
- ESLint
- Prettier

### Python
- uv
- pip
- Poetry
- PDM
- Hatch
- conda
- pixi
- Ruff
- PyInstaller
- Nuitka
- Briefcase — BeeWare packaging
- py2app
- cx_Freeze

### Native & polyglot
- Cargo
- cargo-dist
- Go modules
- GoReleaser
- Maven
- Gradle
- sbt
- Mill
- Bazel
- Buck2
- Pants
- CMake
- Meson
- Ninja
- Make
- xmake
- Premake
- Zig build system
- vcpkg
- Conan
- Nix
- Homebrew
- just
- Task (Taskfile)
- mise
- asdf

---

## 31. Desktop packaging & distribution
- DMG / create-dmg
- .pkg installers
- Notarization (notarytool)
- Sparkle
- Squirrel
- MSIX
- WiX Toolset
- Inno Setup
- NSIS
- AppImage
- Flatpak / Flathub
- Snap / Snapcraft
- Homebrew Cask
- winget
- Chocolatey
- Scoop

## 32. App stores & channels
- App Store (iOS)
- Mac App Store
- TestFlight
- Google Play
- Microsoft Store
- Steam
- itch.io
- Epic Games Store
- F-Droid
- Setapp
- Chrome Web Store
- Firefox Add-ons
- Firebase App Distribution
- Codemagic
- Bitrise

---

## 33. Testing
- Vitest
- Jest
- Mocha
- Playwright
- Cypress
- Puppeteer
- Selenium
- WebdriverIO
- Testing Library
- Chromatic
- pytest
- Hypothesis
- RSpec
- Minitest
- JUnit
- Kotest
- xUnit
- NUnit
- XCTest
- Swift Testing
- Espresso
- Detox
- Maestro
- Appium
- cargo-nextest
- proptest
- testify — Go
- Ginkgo — Go
- k6 — load testing
- Locust — load testing

## 34. Hosting, deploy & infra
- Vercel
- Netlify
- Cloudflare Workers / Pages
- Fly.io
- Railway
- Render
- Heroku
- DigitalOcean App Platform
- AWS Lambda
- AWS ECS / Fargate
- AWS Elastic Beanstalk
- Google Cloud Run
- Google App Engine
- Firebase Hosting
- Azure App Service
- Deno Deploy
- Modal
- Koyeb
- Northflank
- Coolify
- Dokku
- CapRover
- Kamal
- Hetzner
- GitHub Pages
- Val Town
- Replit Deployments
- Docker
- Podman
- Kubernetes
- Nomad
- SST
- Serverless Framework
- Pulumi
- Terraform / OpenTofu
- Ansible
- GitHub Actions
- GitLab CI

## 35. Observability & analytics
- Sentry
- PostHog
- Datadog
- Grafana + Prometheus
- OpenTelemetry
- Honeycomb
- Better Stack
- LogRocket
- Firebase Crashlytics
- Bugsnag
- Mixpanel
- Amplitude
- Plausible
- Umami
- Healthchecks.io

## 36. Generated output: email, PDF, docs
- React Email
- MJML
- Maizzle
- Typst
- LaTeX
- WeasyPrint
- react-pdf
- Pandoc
