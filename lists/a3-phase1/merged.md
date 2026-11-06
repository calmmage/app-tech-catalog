# Approach 3 · Phase 1 merged — categories of apps

240 categories from 5 lenses → 128 distinct, by Petr's rule: «not what can be IN type 1. instead what can BE type 1».
Lens tags: **S** structured · **C** community · **W** wild internet · **I** Instagram saves · **N** Petr's notes. Public lens files: `structured.md`, `community.md`, `wild.md`; Instagram and notes lenses are private.

## Batch 1 — Desktop & OS
1. Platform-native desktop toolkit — S C N
2. Cross-platform native-widget wrapper — S C
3. Self-drawn / GPU cross-platform GUI — S C
4. Immediate-mode GUI — S C
5. Game engine as GUI toolkit — W
6. Bundled-browser shell (Electron-style) — S C
7. System-webview shell (Tauri-style) — S C N
8. RAD visual form designer — C
9. Shared core + native shells — C
10. Menu bar / tray utility — S C W N
11. Notch app — W
12. Summon-anywhere command (launcher, hotkey palette) — S C N
13. Desktop widget / glanceable — S C
14. Desktop pet / cursor-side buddy — W I
15. Ambient juice layer over work (sound, animation, haptics on work events) — N
16. Home-cooked tool for one / own-it replacement for a paid product — W I
17. Kiosk / single-app locked device (incl. kid-proof) — S I N
18. Whole OS as the product (distro) — I
19. Boot-sector app — W

## Batch 2 — Terminal, files, scripts, services
20. One-shot CLI — S C N
21. Prompt wizard / REPL / one-paste installer — S C N
22. Full-screen TUI — S C N
23. SSH-served app — S W
24. Agent-first CLI (made for agents to call) — W
25. Plain file as the app (Markdown/outline is data and UI) — N
26. Spreadsheet / hosted table as the app (Sheets, Notion, Airtable) — S C W N
27. Notebook — S
28. OS automation recipe (Shortcuts, AppleScript) — S C I N
29. Visual workflow automation (n8n-style) — S C N
30. Scheduled background job / daemon — S N
31. Trigger-only / serverless / edge function — S W
32. Headless API / library / MCP server (users are code or agents) — S I N W
33. Git-forge app (README, Issues, Actions are the app) — W
34. Smart contract + dApp — S
35. Live instrument console (hardware data → gauges, rolling plots) — N

## Batch 3 — Web
36. Static site — S C
37. Client-rendered SPA — S C
38. Full-stack meta-framework — C
39. Server-rendered MVC monolith — C
40. HTML-over-the-wire / hypermedia — S C
41. Script → web UI (Streamlit-style) — S C
42. Installable PWA — S C N
43. WASM-compiled app — S C
44. Canvas / GPU / 3D web scene — S I N
45. Embeddable widget — S
46. Single-file HTML tool / artifact shared by link — C W I N
47. Whole OS in one HTML file — W
48. App in a link or QR code — W
49. Multi-tab app (tabs talk to each other) — I
50. Agent-readable site (llms.txt) — I
51. Full-stack SaaS from a starter template — I N
52. Self-hosted on my own machine (tailnet / tunnel, no deploy) — I N
53. Publish pipeline: one note → site, newsletter, channels — N
54. Copy-paste component & effect registry — I
55. Reference-cloned design — I
56. Fake-door landing page (complaint-mined) — I
57. Infinite canvas board — N

## Batch 4 — Browser, mobile, messengers, hosts
58. Browser extension (incl. bridged to an agent) — S C I N
59. Userscript / bookmarklet / in-page layer on someone else's site — S C I N
60. Native mobile app — S C I
61. Cross-platform compiled mobile — S C
62. Hybrid webview mobile — S C
63. Phone home-screen widget as the main surface — W N
64. Super-app mini app (Telegram Mini App, WeChat) — S C W N
65. Personal chat bot (1:1) — S C N
66. Bot inside other people's chats (group, guest, inline) — N
67. Userbot (acting as my own account) — N
68. Email / SMS as the interface — S W N
69. Voice-first / dial-in / smart-speaker app — S C W N
70. One-card-at-a-time review queue — N
71. Daily digest (push report) — I N
72. Plugin inside a host app (editor, notes, Figma, Office) — S C W I N
73. Audio / creative-tool plugin (VST, Blender add-on) — S C

## Batch 5 — AI-native
74. Talking to an agent is the app (personal agent, messenger contact) — C W I N
75. App inside AI chat (MCP Apps, Apps SDK) — S C W I
76. Agent skill folder as the app — W I N
77. Mod / hook / skin for an agent harness — I N
78. Agent fleet / org chart / long-running build loop — I N
79. Agent-to-agent network (friends' agents trade updates) — N
80. Persona council / simulated experts — I
81. Middleware proxy between agent and model — I
82. Generated-per-click app — W
83. LLM as the backend — W
84. Neural-rendered computer — W
85. Agent-composed native UI (generative UI) — W
86. Self-rewriting app — W
87. Malleable software — W
88. Prompt-to-app generator — C W
89. On-device / tiny edge model as the product — W I
90. Personal search over my own data / second brain — I N
91. Scheduled pipeline + self-rebuilding dashboard — I
92. Node-graph / natural-language generation pipeline — W I
93. AI media workshop / content factory — I N

## Batch 6 — Games, media, odd runtimes
94. Editor-centric game engine — S C N
95. Code-first game framework / browser game or toy — S C N
96. No-code game maker — C
97. Fantasy console — S C W
98. Interactive fiction / narrative engine — S C
99. Inside another game (mods, UGC platforms, redstone computers) — S C W
100. Daily puzzle with work woven in — N
101. Learning sandbox game for kids — I
102. Creative coding & live coding — S C W
103. Node-based visual patching — C
104. Rendered show: video or podcast from code — I N
105. Interactive show (pauses for buttons, form, chat) — N
106. Input-scrubbed AI video (fake 3D) — I
107. Diagram / board compiled from code — I
108. App inside a PDF — W
109. App inside a font — W
110. CSS-only computer — W
111. Type-checker program — W
112. Database / SQL as the runtime — W

## Batch 7 — Devices, hardware, networks
113. Microcontroller firmware — S
114. Embedded screen HMI / cheap touchscreen gadget — S C W
115. Wearable / watch app — S
116. TV & car screens — S C N
117. XR / spatial / AR overlay — S C I N
118. HUD glasses app — W
119. Ambient e-ink / LED display — W
120. Receipt-printer app — W
121. Odd-input handheld (Playdate, Flipper Zero) — W
122. Physical input for software (dials, cards) — I
123. Embodied robot / smart toy — I
124. Room as the computer — W
125. Local-first sync app — C W I
126. Bluetooth mesh app — W
127. Serverless peer-to-peer app — W
128. Protocol-native app (AT Protocol, Nostr) — W

## Merged or dropped
- Same shape, merged: launcher into summon-anywhere; "apps whose users are agents" into headless API/MCP; "browser extension bridged to an agent" into browser extension; "messenger contact as the app" into talking to an agent; "local-first native desktop utility" split between home-cooked tool and local-first sync; stylized generative visuals into node-graph pipeline; voice-driven home and TV into voice-first.
- Dropped as content, not shape («those are still emoji + text combos»): "Asymmetric co-op game", "Small indie game with one twist" (I).
