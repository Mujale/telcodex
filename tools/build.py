#!/usr/bin/env python3
"""Pre-render Markdown into each topic page's HTML at build time.

For every page that declares  window.PAGE = { md: "<file>.md", key: "<key>" },
this reads the markdown, renders it to HTML, and injects it into the page's
<article id="doc"> ... </article> block. It also pre-renders the "On this page"
TOC and the "Related topics" block, so the content is present in the static
HTML with no JavaScript required (best for SEO/crawlers).

The page.js engine still runs in the browser: if a #doc already contains
pre-rendered content it leaves it in place, so JS is pure progressive enhancement.

Run:  python tools/build.py
Re-run after editing any .md file.
"""
import os
import re
import html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# topic registry (mirrors TOPICS in assets/page.js, for Related links)
TOPICS = [
    ("standardization", "standardization.html", "Standardization & Timeline", "Release 20 vs 21 and the approved 6G freeze dates."),
    ("features",        "features.html",        "6G Features",                "Sub-THz, AI-native radio, ISAC, ambient IoT and more."),
    ("architecture",    "architecture.html",    "Network Architecture",       "How the RAN and core evolve for 6G, with diagrams."),
    ("ran",             "ran.html",             "6G RAN",                     "The radio access network: spectrum, air interface, MIMO."),
    ("core",            "core.html",            "6G Core",                    "The next-generation core and service-based architecture."),
    ("management",      "management.html",      "Network Management",         "Intent-driven, AI-assisted, closed-loop operation."),
]
TOPIC_BY_KEY = {t[0]: t for t in TOPICS}


# ---------------- Markdown renderer (mirrors assets/page.js) ----------------
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s):
    s = esc(s)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img alt="\1" src="\2" />', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def render_table(rows):
    def cells(r):
        return [c.strip() for c in r.strip().strip("|").split("|")]
    head = cells(rows[0])
    out = ['<div class="table-wrap"><table><thead><tr>']
    out += ["<th>" + inline(h) + "</th>" for h in head]
    out.append("</tr></thead><tbody>")
    for r in rows[2:]:
        if not r.strip():
            continue
        out.append("<tr>" + "".join("<td>" + inline(c) + "</td>" for c in cells(r)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def is_sep(s):
    return bool(re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", s)) and "-" in s


def md_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, i = [], 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if re.match(r"^\s*$", line):
            i += 1
            continue
        if re.match(r"^\s*---\s*$", line):
            out.append("<hr/>")
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            lv = len(h.group(1))
            out.append(f"<h{lv}>{inline(h.group(2))}</h{lv}>")
            i += 1
            continue
        if re.match(r"^\s*>\s?", line):
            buf = []
            while i < n and re.match(r"^\s*>\s?", lines[i]):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + md_to_html("\n".join(buf)) + "</blockquote>")
            continue
        if "|" in line and i + 1 < n and is_sep(lines[i + 1]):
            buf = [line, lines[i + 1]]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append(render_table(buf))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            buf = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                i += 1
                while (i < n and lines[i].strip() and re.match(r"^\s+", lines[i])
                       and not re.match(r"^\s*[-*]\s+", lines[i])
                       and not re.match(r"^\s*\d+\.\s+", lines[i])):
                    item += " " + lines[i].strip()
                    i += 1
                buf.append("<li>" + inline(item) + "</li>")
            out.append("<ul>" + "".join(buf) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            buf = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                i += 1
                while (i < n and lines[i].strip() and re.match(r"^\s+", lines[i])
                       and not re.match(r"^\s*[-*]\s+", lines[i])
                       and not re.match(r"^\s*\d+\.\s+", lines[i])):
                    item += " " + lines[i].strip()
                    i += 1
                buf.append("<li>" + inline(item) + "</li>")
            out.append("<ol>" + "".join(buf) + "</ol>")
            continue
        buf = [line]
        i += 1
        while (i < n and lines[i].strip()
               and not re.match(r"^(#{1,6})\s", lines[i])
               and not re.match(r"^\s*[-*]\s+", lines[i])
               and not re.match(r"^\s*\d+\.\s+", lines[i])
               and not re.match(r"^\s*>", lines[i])
               and not re.match(r"^\s*---\s*$", lines[i])
               and "|" not in lines[i]):
            buf.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


def build_toc(doc_html):
    """Add ids to <h2> and return (doc_html_with_ids, toc_html)."""
    idx = [0]
    toc = []

    def repl(m):
        sid = f"sec-{idx[0]}"
        text = re.sub(r"<[^>]+>", "", m.group(1))
        toc.append(f'<a href="#{sid}">{text}</a>')
        idx[0] += 1
        return f'<h2 id="{sid}">{m.group(1)}</h2>'

    doc_html = re.sub(r"<h2>(.*?)</h2>", repl, doc_html, flags=re.S)
    toc_html = "".join(toc) if toc else '<span style="font-size:13px;color:var(--ink-faint)">—</span>'
    return doc_html, toc_html


def related_html(key):
    picks = [t for t in TOPICS if t[0] != key][:3]
    cards = "".join(
        f'<a href="{url}"><strong>{title}</strong><span>{blurb}</span></a>'
        for (_k, url, title, blurb) in picks
    )
    return f'<div class="related"><h4>Related topics</h4><div class="cards">{cards}</div></div>'


# ---------------- Page processing ----------------
PAGE_RE = re.compile(r"window\.PAGE\s*=\s*\{([^}]*)\}")


def parse_page_config(html_text):
    m = PAGE_RE.search(html_text)
    if not m:
        return None
    cfg = m.group(1)
    md = re.search(r'md\s*:\s*"([^"]+)"', cfg)
    key = re.search(r'key\s*:\s*"([^"]+)"', cfg)
    return (md.group(1) if md else None, key.group(1) if key else None)


DOC_RE = re.compile(r'(<article class="doc" id="doc">)(.*?)(</article>)', re.S)
TOC_RE = re.compile(r'(<nav class="toc" id="toc">)(.*?)(</nav>)', re.S)


def process(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    cfg = parse_page_config(text)
    if not cfg:
        return False, "no window.PAGE"
    md_file, key = cfg
    if not md_file:
        return False, "no md (static page)"
    md_path = os.path.join(ROOT, md_file)
    if not os.path.exists(md_path):
        return False, f"missing {md_file}"
    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()

    doc_html = md_to_html(md)
    doc_html, toc_html = build_toc(doc_html)
    if key and key in TOPIC_BY_KEY:
        doc_html += "\n" + related_html(key)

    # mark as prerendered so page.js can skip re-fetching
    new_doc = r'\1' + "\n<!-- prerendered -->\n" + doc_html.replace("\\", r"\\") + "\n\\3"
    if not DOC_RE.search(text):
        return False, "no #doc block"
    text = DOC_RE.sub(lambda m: m.group(1) + "\n<!-- prerendered -->\n" + doc_html + "\n" + m.group(3), text, count=1)

    # pre-fill TOC too
    if TOC_RE.search(text):
        text = TOC_RE.sub(lambda m: m.group(1) + toc_html + m.group(3), text, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True, f"rendered {md_file}" + (f" (+related)" if key in TOPIC_BY_KEY else "")


def main():
    pages = [p for p in os.listdir(ROOT) if p.endswith(".html")]
    print("Pre-rendering markdown into pages...\n")
    for p in sorted(pages):
        ok, msg = process(os.path.join(ROOT, p))
        flag = "OK " if ok else "-- "
        print(f"  {flag}{p}: {msg}")
    print("\nDone. Re-run after editing any .md file.")


if __name__ == "__main__":
    main()
