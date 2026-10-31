#!/usr/bin/env python3
"""Generate ISAC_6G.pdf from ISAC_6G_Analysis.md.

Lightweight Markdown -> PDF renderer using fpdf2. Supports headings,
paragraphs, bullet/numbered lists, blockquotes, fenced code blocks,
GitHub-style tables, and inline **bold** / *italic* / `code`.
Not a full Markdown engine -- tailored to this document's structure.
"""
import os
import re
import sys

from fpdf import FPDF

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "ISAC_6G_Analysis.md")
OUT = os.path.join(ROOT, "ISAC_6G.pdf")

# Theme colours (match the site)
INK = (28, 36, 51)
SOFT = (75, 86, 104)
BRAND = (37, 99, 235)
BRAND3 = (124, 58, 237)
LINE = (210, 216, 228)
CODE_BG = (238, 241, 246)
TH_BG = (238, 243, 255)


_UNICODE_MAP = {
    "—": "-", "–": "-", "’": "'", "‘": "'", "“": '"', "”": '"', "…": "...",
    "≤": "<=", "≥": ">=", "×": "x", "•": "-", "→": "->", "←": "<-",
    "↔": "<->", "◄": "<", "►": ">", "├": "|", "└": "|", "│": "|",
    "─": "-", "┴": "|", "┬": "|", "▼": "v", "▲": "^", "°": "deg",
    "±": "+/-", "≈": "~", "™": "(TM)", "®": "(R)", "©": "(c)",
    "\u00a0": " ", "\u2011": "-", "\u2212": "-",
}


def sanitize(text):
    """Map characters outside latin-1 to safe ASCII equivalents."""
    for k, v in _UNICODE_MAP.items():
        text = text.replace(k, v)
    # drop anything still non-latin-1
    return text.encode("latin-1", "replace").decode("latin-1").replace("?", "")


def strip_inline(text):
    """Remove markdown inline markers and sanitize for plain rendering."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return sanitize(text)


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*SOFT)
        self.cell(0, 8, f"Telcodex.io  -  ISAC 6G Analysis  -  Page {self.page_no()}",
                  align="C")


def write_inline(pdf, text, size=10.5, color=SOFT, lh=5.3):
    """Render a line with **bold**, *italic*, `code` segments via write()."""
    text = sanitize(text)
    pdf.set_text_color(*color)
    # tokenize into (style, chunk)
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]*\))")
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            pdf.set_font("Helvetica", "", size)
            pdf.set_text_color(*color)
            pdf.write(lh, text[pos:m.start()])
        tok = m.group(0)
        if tok.startswith("**"):
            pdf.set_font("Helvetica", "B", size)
            pdf.set_text_color(*INK)
            pdf.write(lh, tok[2:-2])
        elif tok.startswith("`"):
            pdf.set_font("Courier", "", size - 0.5)
            pdf.set_text_color(*BRAND3)
            pdf.write(lh, tok[1:-1])
        elif tok.startswith("["):
            lm = re.match(r"\[([^\]]+)\]\(([^)]*)\)", tok)
            pdf.set_font("Helvetica", "U", size)
            pdf.set_text_color(*BRAND)
            pdf.write(lh, lm.group(1))
        else:  # *italic*
            pdf.set_font("Helvetica", "I", size)
            pdf.set_text_color(*color)
            pdf.write(lh, tok[1:-1])
        pos = m.end()
    if pos < len(text):
        pdf.set_font("Helvetica", "", size)
        pdf.set_text_color(*color)
        pdf.write(lh, text[pos:])
    pdf.ln(lh + 0.6)


def parse_table(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(lines[i])
        i += 1
    header = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    body = []
    for r in rows[2:]:
        body.append([strip_inline(c.strip())
                     for c in r.strip().strip("|").split("|")])
    return header, body, i


def render_table(pdf, header, body):
    header = [strip_inline(h) for h in header]
    # column widths proportional to content, capped to page width
    epw = pdf.epw
    ncol = len(header)
    raw = []
    for c in range(ncol):
        maxlen = len(header[c])
        for row in body:
            if c < len(row):
                maxlen = max(maxlen, min(len(row[c]), 40))
        raw.append(max(maxlen, 3))
    total = sum(raw)
    widths = [epw * w / total for w in raw]

    line_h = 5.0
    pdf.ln(1)

    def draw_row(cells, is_head):
        # compute needed height
        pdf.set_font("Helvetica", "B" if is_head else "", 8.6)
        heights = []
        for c in range(ncol):
            txt = sanitize(cells[c]) if c < len(cells) else ""
            nlines = pdf.multi_cell(widths[c], line_h, txt, dry_run=True,
                                    output="LINES")
            heights.append(max(1, len(nlines)))
        rh = max(heights) * line_h
        if pdf.get_y() + rh > pdf.page_break_trigger:
            pdf.add_page()
            draw_row(header, True)
        x0 = pdf.get_x()
        y0 = pdf.get_y()
        for c in range(ncol):
            txt = sanitize(cells[c]) if c < len(cells) else ""
            x = pdf.get_x()
            y = pdf.get_y()
            if is_head:
                pdf.set_fill_color(*TH_BG)
                pdf.set_text_color(*INK)
            else:
                pdf.set_fill_color(255, 255, 255)
                pdf.set_text_color(*SOFT)
            pdf.rect(x, y, widths[c], rh)
            pdf.multi_cell(widths[c], line_h, txt, border=0, align="L",
                           fill=is_head, max_line_height=line_h)
            pdf.set_xy(x + widths[c], y)
        pdf.set_xy(x0, y0 + rh)

    draw_row(header, True)
    for row in body:
        pdf.set_font("Helvetica", "", 8.6)
        draw_row(row, False)
    pdf.ln(2)


def render_code(pdf, code_lines):
    pdf.ln(1)
    pdf.set_font("Courier", "", 8)
    pdf.set_fill_color(*CODE_BG)
    pdf.set_text_color(*INK)
    for ln in code_lines:
        safe = sanitize(ln)
        pdf.cell(0, 4.4, "  " + safe, fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)


def main():
    if not os.path.exists(SRC):
        print("Source not found:", SRC)
        sys.exit(1)
    with open(SRC, "r", encoding="utf-8") as f:
        md = f.read().replace("\r\n", "\n")
    lines = md.split("\n")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.set_margins(16, 16, 16)
    pdf.add_page()

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            render_code(pdf, buf)
            continue

        if s.startswith("|") and i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|-: "):
            header, body, i = parse_table(lines, i)
            render_table(pdf, header, body)
            continue

        if s.startswith("#"):
            m = re.match(r"(#{1,6})\s+(.*)", s)
            level = len(m.group(1))
            text = strip_inline(m.group(2))
            pdf.ln(2)
            if level == 1:
                pdf.set_font("Helvetica", "B", 18)
                pdf.set_text_color(*INK)
                pdf.multi_cell(0, 8, text)
                pdf.set_draw_color(*BRAND)
                pdf.set_line_width(0.6)
                y = pdf.get_y() + 1
                pdf.line(pdf.l_margin, y, pdf.l_margin + pdf.epw, y)
                pdf.ln(3)
            elif level == 2:
                pdf.set_font("Helvetica", "B", 13.5)
                pdf.set_text_color(*BRAND)
                pdf.multi_cell(0, 6.5, text)
                pdf.ln(1)
            elif level == 3:
                pdf.set_font("Helvetica", "B", 11.5)
                pdf.set_text_color(*BRAND3)
                pdf.multi_cell(0, 6, text)
                pdf.ln(0.5)
            else:
                pdf.set_font("Helvetica", "B", 10.5)
                pdf.set_text_color(*INK)
                pdf.multi_cell(0, 5.5, text)
            i += 1
            continue

        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            text = " ".join(x for x in buf if x)
            x = pdf.l_margin
            pdf.set_draw_color(*BRAND)
            pdf.set_line_width(1.2)
            y_start = pdf.get_y()
            pdf.set_x(x + 4)
            pdf.set_font("Helvetica", "I", 10)
            start_y = pdf.get_y()
            pdf.multi_cell(pdf.epw - 4, 5.1, strip_inline(text))
            pdf.line(x + 1, start_y, x + 1, pdf.get_y())
            pdf.ln(2)
            continue

        if re.match(r"^---+$", s):
            pdf.ln(1)
            pdf.set_draw_color(*LINE)
            pdf.set_line_width(0.2)
            y = pdf.get_y()
            pdf.line(pdf.l_margin, y, pdf.l_margin + pdf.epw, y)
            pdf.ln(3)
            i += 1
            continue

        if re.match(r"^[-*]\s+", s):
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i])
                pdf.set_x(pdf.l_margin + 3)
                pdf.set_font("Helvetica", "", 10.5)
                pdf.set_text_color(*BRAND)
                pdf.write(5.3, "-  ")
                write_inline(pdf, item, lh=5.3)
                i += 1
            pdf.ln(1)
            continue

        if re.match(r"^\d+\.\s+", s):
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                num = re.match(r"^\s*(\d+)\.\s+(.*)", lines[i])
                pdf.set_x(pdf.l_margin + 3)
                pdf.set_font("Helvetica", "B", 10.5)
                pdf.set_text_color(*BRAND)
                pdf.write(5.3, f"{num.group(1)}.  ")
                write_inline(pdf, num.group(2), lh=5.3)
                i += 1
            pdf.ln(1)
            continue

        # paragraph: gather until blank or block
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(#|>|\||```|---+$|[-*]\s|\d+\.\s)", lines[i]):
            buf.append(lines[i])
            i += 1
        write_inline(pdf, " ".join(x.strip() for x in buf), lh=5.3)
        pdf.ln(0.8)

    pdf.output(OUT)
    print("Wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
