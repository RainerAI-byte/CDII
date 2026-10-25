from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable,
    ListItem, HRFlowable
)
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "U04_E08_sintesis.md"
OUTPUT = ROOT / "reports" / "U04_E08_sintesis.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="DocTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=20, leading=25, alignment=TA_CENTER, spaceAfter=18,
    textColor=colors.HexColor("#183153")
))
styles.add(ParagraphStyle(
    name="H1Custom", parent=styles["Heading1"], fontSize=15, leading=19,
    spaceBefore=15, spaceAfter=8, keepWithNext=True,
    textColor=colors.HexColor("#183153")
))
styles.add(ParagraphStyle(
    name="H2Custom", parent=styles["Heading2"], fontSize=11.5, leading=15,
    spaceBefore=10, spaceAfter=5, keepWithNext=True,
    textColor=colors.HexColor("#28527A")
))
styles.add(ParagraphStyle(
    name="BodyCustom", parent=styles["BodyText"], fontSize=9.3,
    leading=13.3, spaceAfter=7
))
styles.add(ParagraphStyle(
    name="SmallCustom", parent=styles["BodyText"], fontSize=8,
    leading=10, textColor=colors.HexColor("#555555"), spaceAfter=5
))

def inline_markup(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(
        r"(https://github\.com/[^\s]+)",
        r'<link href="\1" color="#1769AA">\1</link>', text
    )
    return text

def footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#D6DEE8"))
    canvas.line(2 * cm, 1.55 * cm, width - 2 * cm, 1.55 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(2 * cm, 1.1 * cm, "INF-8239 · U04.E08 · Expediente de gobernanza")
    canvas.drawRightString(width - 2 * cm, 1.1 * cm, f"Página {doc.page}")
    canvas.restoreState()

lines = SOURCE.read_text(encoding="utf-8-sig").splitlines()
story = []
paragraph_buffer = []
bullet_buffer = []
first_title = True

def flush_paragraph():
    global paragraph_buffer
    if paragraph_buffer:
        content = " ".join(x.strip() for x in paragraph_buffer).strip()
        if content:
            story.append(Paragraph(inline_markup(content), styles["BodyCustom"]))
        paragraph_buffer = []

def flush_bullets():
    global bullet_buffer
    if bullet_buffer:
        items = [
            ListItem(Paragraph(inline_markup(item), styles["BodyCustom"]),
                     leftIndent=10)
            for item in bullet_buffer
        ]
        story.append(ListFlowable(
            items, bulletType="bullet", start="circle",
            leftIndent=18, bulletFontSize=7, spaceAfter=7
        ))
        bullet_buffer = []

for raw in lines:
    line = raw.strip()
    if not line:
        flush_paragraph()
        flush_bullets()
        continue
    if line == "---":
        flush_paragraph()
        flush_bullets()
        story.append(HRFlowable(
            width="100%", thickness=0.6,
            color=colors.HexColor("#D6DEE8"), spaceBefore=4, spaceAfter=8
        ))
        continue
    if line.startswith("# "):
        flush_paragraph()
        flush_bullets()
        heading = line[2:].strip()
        if first_title:
            story.append(Paragraph(inline_markup(heading), styles["DocTitle"]))
            first_title = False
        else:
            story.append(Paragraph(inline_markup(heading), styles["H1Custom"]))
        continue
    if line.startswith("## "):
        flush_paragraph()
        flush_bullets()
        story.append(Paragraph(inline_markup(line[3:].strip()), styles["H2Custom"]))
        continue
    if line.startswith("- "):
        flush_paragraph()
        bullet_buffer.append(line[2:].strip())
        continue
    if re.match(r"^\d+\.\s", line):
        flush_paragraph()
        bullet_buffer.append(re.sub(r"^\d+\.\s", "", line))
        continue
    flush_bullets()
    paragraph_buffer.append(line)

flush_paragraph()
flush_bullets()

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4,
    rightMargin=2 * cm, leftMargin=2 * cm,
    topMargin=1.8 * cm, bottomMargin=2 * cm,
    title="U04.E08 — Expediente de gobernanza y DSS responsable",
    author="INF-8239 Ciencia de Datos II"
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)

print(f"PDF generado: {OUTPUT}")
print(f"Fuente editable: {SOURCE}")
print(f"Tamaño PDF: {OUTPUT.stat().st_size:,} bytes")
