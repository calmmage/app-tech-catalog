"""Build index.html: the four lists in lists/ parsed into one searchable page."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
L = ROOT / "lists"
REPO = "https://github.com/calmmage/app-tech-catalog"


def norm(s):
    s = re.sub(r"\(.*?\)", "", s.lower())
    s = re.sub(r"[`*_\"']", "", s)
    return re.sub(r"[^a-z0-9+#.]+", "", s).strip(".")


def split_dash(s):
    parts = re.split(r" — | – ", s, maxsplit=1)
    return parts[0].strip(), (parts[1].strip() if len(parts) > 1 else "")


def parse_sectioned(path, skip=("Contents", "Item counts")):
    """'## N. Section' → '### Sub' → '- Name — note'."""
    sections, sec, sub = [], None, None
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            title = re.sub(r"^\d+\.\s*", "", line[3:]).strip()
            if title in skip:
                sec = None
                continue
            sec = {"title": title, "groups": []}
            sections.append(sec)
            sub = None
        elif line.startswith("### ") and sec is not None:
            sub = {"title": line[4:].strip(), "items": []}
            sec["groups"].append(sub)
        elif line.startswith("- ") and sec is not None and not line.startswith("- ["):
            if sub is None:
                sub = {"title": "", "items": []}
                sec["groups"].append(sub)
            name, note = split_dash(line[2:])
            sub["items"].append([name, note])
    return sections


def parse_a1(path):
    sections, sec = [], None
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            title = re.sub(r"\s+—\s+\d+$", "", line[3:]).strip()
            sec = {"title": title, "groups": [{"title": "", "items": []}]}
            sections.append(sec)
        elif line.startswith("- ") and sec is not None:
            body = line[2:].strip()
            m = re.match(r"(.*?)\s+\((.*)\)$", body)
            name, note = (m.group(1), m.group(2)) if m else (body, "")
            sec["groups"][0]["items"].append([name, note])
    return sections


URLISH = re.compile(r"^(https?://|[a-z0-9-]+\.[a-z]{2,}(/|$))", re.I)


def parse_a3(path):
    batches, batch, cat = [], None, None
    for line in path.read_text().splitlines():
        if line.startswith("# Batch"):
            batch = {"title": line[2:].strip(), "cats": []}
            batches.append(batch)
        elif line.startswith("## ") and batch is not None:
            m = re.match(r"## (\d+)\. (.*?)(?: — ([SCWIN ]+))?$", line)
            if not m:
                continue
            cat = {"n": int(m.group(1)), "title": m.group(2).strip(),
                   "tags": (m.group(3) or "").split(), "picks": []}
            batch["cats"].append(cat)
        elif line.startswith("- **") and cat is not None:
            m = re.match(r"- \*\*(.+?)\*\*\s*(.*)$", line)
            if not m:
                continue
            name, rest = m.group(1), re.sub(r"^[—–-]\s*", "", m.group(2))
            parts = [p.strip() for p in rest.split(" · ") if p.strip()]
            link = ""
            if parts and URLISH.match(parts[-1]):
                link = parts.pop()
                if not link.startswith("http"):
                    link = "https://" + link
            cat["picks"].append([name, " · ".join(parts), link])
    return batches


a0 = parse_sectioned(L / "a0-direct.md")
a1 = parse_a1(L / "a1-petr-words.md")
a2 = parse_sectioned(L / "a2-spec-catalog.md")
a3 = parse_a3(L / "a3-app-types.md")

# All names, merged across the four lists
names = {}


def add(name, note, src, where):
    key = norm(name)
    if not key:
        return
    row = names.setdefault(key, {"name": name, "note": note, "src": set(), "where": where})
    row["src"].add(src)
    if not row["note"] and note:
        row["note"] = note


for sec in a2:
    for g in sec["groups"]:
        for n, note in g["items"]:
            add(n, note, 2, sec["title"])
for sec in a0:
    for g in sec["groups"]:
        for n, note in g["items"]:
            add(n, note, 0, sec["title"])
for b in a3:
    for c in b["cats"]:
        for n, note, _ in c["picks"]:
            add(n, note, 3, c["title"])
for sec in a1:
    for n, note in sec["groups"][0]["items"]:
        parts = n.split(" - ", 1)
        bare = parts[1] if len(parts) == 2 else parts[0]
        add(bare, note or (parts[0] if len(parts) == 2 else ""), 1, sec["title"])

all_names = sorted(
    ([r["name"], r["note"], "".join(str(s) for s in sorted(r["src"])), r["where"]] for r in names.values()),
    key=lambda r: r[0].lower().lstrip("@.").lstrip(),
)

count = lambda secs: sum(len(g["items"]) for s in secs for g in s["groups"])
stats = {
    "a0": count(a0), "a1": count(a1), "a2": count(a2),
    "a3": sum(len(c["picks"]) for b in a3 for c in b["cats"]),
    "types": sum(len(b["cats"]) for b in a3),
    "names": len(all_names),
}

data = {"a2": a2, "a3": a3, "names": all_names, "stats": stats, "repo": REPO,
        "story": (ROOT / "story.md").read_text()}
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

page = (ROOT / "page.html").read_text()
page = page.replace("/*DATA*/null", blob)
for k, v in stats.items():
    page = page.replace("{{" + k + "}}", f"{v:,}")
(ROOT / "artifact.html").write_text(page)  # claude.ai wraps it in its own skeleton
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Every way to build an app: 128 app types with picks, 2,265 frameworks, 3,810 names.">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<style>[hidden]{display:none!important}body{margin:0}</style>
"""
title_end = page.index("</style>") + len("</style>")
(ROOT / "index.html").write_text(head + page[:title_end] + "\n</head>\n<body>\n" + page[title_end:] + "\n</body>\n</html>\n")
print(stats, f"{len(page)/1024:.0f} KB")
