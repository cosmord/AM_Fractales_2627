#!/usr/bin/env python3
"""Rebuild every derived deliverable from the specs in this repository.

Usage:
    python scripts/rebuild_artifacts.py

Requires: numpy, sympy, matplotlib, reportlab, python-pptx, Pillow.
"""
from __future__ import annotations

import json
import os
import runpy
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


def run_scripts():
    for name in ("Newton.py", "Halley.py", "Chebyshev.py"):
        print("running", name, flush=True)
        subprocess.check_call([sys.executable, name])


def build_pdf():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    with open("memoria/memoria_spec.json", encoding="utf-8") as fh:
        spec = json.load(fh)
    styles = getSampleStyleSheet()
    story = []
    for el in spec.get("elements", []):
        kind = el.get("type")
        if kind == "heading":
            story.append(Paragraph(el.get("text", ""), styles["Heading" + str(min(max(int(el.get("level", 1)), 1), 3))]))
        elif kind == "paragraph":
            story.append(Paragraph(el.get("text", ""), styles["BodyText"]))
            story.append(Spacer(1, 6))
        elif kind == "table":
            rows = el.get("rows", [])
            if not rows:
                continue
            table = Table(rows, repeatRows=1 if el.get("header", True) else 0)
            style = [("GRID", (0, 0), (-1, -1), 0.5, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP")]
            if el.get("header", True):
                style += [("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                          ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
            table.setStyle(TableStyle(style))
            story.append(table)
            story.append(Spacer(1, 10))
        elif kind == "image":
            img = Image(el["path"], width=float(el.get("width", 400)))
            img.drawHeight = img.drawWidth * img.imageHeight / img.imageWidth
            story.append(img)
            story.append(Spacer(1, 10))
        elif kind == "pagebreak":
            story.append(PageBreak())

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 9)
        canvas.drawCentredString(A4[0] / 2, 0.5 * inch, "Page " + str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate("memoria/memoria.pdf", pagesize=A4,
                            title=spec.get("title", ""), author=spec.get("author", ""))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("built memoria/memoria.pdf")


def build_pptx():
    import copy
    from pptx import Presentation  # pyright: ignore[reportMissingImports]
    from pptx.dml.color import RGBColor  # pyright: ignore[reportMissingImports]
    from pptx.enum.shapes import MSO_SHAPE  # pyright: ignore[reportMissingImports]
    from pptx.util import Inches, Pt  # pyright: ignore[reportMissingImports]

    LAYOUTS = {"title": 0, "title_content": 1, "section": 2, "two_content": 3, "title_only": 5, "blank": 6}
    SHAPES = {"rectangle": MSO_SHAPE.RECTANGLE, "rounded_rectangle": MSO_SHAPE.ROUNDED_RECTANGLE,
              "oval": MSO_SHAPE.OVAL, "diamond": MSO_SHAPE.DIAMOND}
    with open("presentacion/deck_spec.json", encoding="utf-8") as fh:
        spec = json.load(fh)
    prs = Presentation()
    if spec.get("slide_size", "16:9") == "16:9":
        prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    for s in spec["slides"]:
        slide = prs.slides.add_slide(prs.slide_layouts[LAYOUTS.get(s.get("layout"), 1)])
        if s.get("background"):
            slide.background.fill.solid()
            slide.background.fill.fore_color.rgb = RGBColor.from_string(s["background"])
        if s.get("slide_number"):
            for ph in slide.slide_layout.placeholders:
                if ph.placeholder_format.idx == 12:
                    slide.shapes._spTree.append(copy.deepcopy(ph._element))
        if s.get("title") is not None and slide.shapes.title is not None:
            slide.shapes.title.text = s["title"]
        if s.get("subtitle") is not None:
            for ph in slide.placeholders:
                if ph.placeholder_format.idx == 1:
                    ph.text = s["subtitle"]
                    break
        if s.get("bullets"):
            body = next((p for p in slide.placeholders if p.placeholder_format.idx != 0), None)
            if body is None:
                body = slide.shapes.add_textbox(Inches(.5), Inches(1.5), Inches(9), Inches(5))
            body.text_frame.clear()
            for i, item in enumerate(s["bullets"]):
                item = {"text": item} if isinstance(item, str) else item
                para = body.text_frame.paragraphs[0] if i == 0 else body.text_frame.add_paragraph()
                para.level = int(item.get("level", 0))
                run = para.add_run()
                run.text = item.get("text", "")
                if item.get("size"):
                    run.font.size = Pt(item["size"])
                if item.get("bold") is not None:
                    run.font.bold = item["bold"]
                if item.get("font"):
                    run.font.name = item["font"]
                if item.get("color"):
                    run.font.color.rgb = RGBColor.from_string(item["color"])
        for img in s.get("images", []):
            kw = {}
            if img.get("width"):
                kw["width"] = Inches(img["width"])
            slide.shapes.add_picture(img["path"], Inches(img.get("left", 1)), Inches(img.get("top", 1)), **kw)
        for tbl in s.get("tables", []):
            rows = tbl["rows"]
            shape = slide.shapes.add_table(len(rows), len(rows[0]), Inches(tbl.get("left", 1)),
                                           Inches(tbl.get("top", 2)), Inches(tbl.get("width", 6)),
                                           Inches(tbl.get("height", 2)))
            for r, row in enumerate(rows):
                for c, val in enumerate(row):
                    shape.table.cell(r, c).text = str(val)
        for shp in s.get("shapes", []):
            shape = slide.shapes.add_shape(SHAPES.get(shp.get("type", "rectangle"), MSO_SHAPE.RECTANGLE),
                                           Inches(shp.get("left", 1)), Inches(shp.get("top", 1)),
                                           Inches(shp.get("width", 2)), Inches(shp.get("height", 1)))
            if shp.get("fill"):
                shape.fill.solid()
                shape.fill.fore_color.rgb = RGBColor.from_string(shp["fill"])
            if shp.get("text"):
                shape.text_frame.text = shp["text"]
                if shp.get("text_color"):
                    shape.text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor.from_string(shp["text_color"])
        if s.get("notes"):
            slide.notes_slide.notes_text_frame.text = s["notes"]
    # Styling applied after creation, same as the classroom deck.
    for idx in (0, len(prs.slides) - 1):
        for shape in prs.slides[idx].shapes:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.color.rgb = RGBColor(0xE6, 0xED, 0xF7)
    for idx in (2, 3, 4, 6):
        for shape in prs.slides[idx].shapes:
            if shape.is_placeholder and shape.placeholder_format.idx == 1:
                shape.width = Inches(7.2)
    for shape in prs.slides[5].shapes:
        if shape.shape_type == 13:
            shape.top = Inches(1.7)
    prs.save("presentacion/presentacion.pptx")
    print("built presentacion/presentacion.pptx")


def build_zip():
    files = ["README_entrega.md", "memoria/memoria.pdf", "presentacion/presentacion.pptx",
             "Newton.py", "Halley.py", "Chebyshev.py",
             "imaxes/fractal_Newton.png", "imaxes/fractal_Halley.png", "imaxes/fractal_Chebyshev.png"]
    with zipfile.ZipFile("entrega_AM.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel in files:
            zf.write(rel, rel)
    with zipfile.ZipFile("entrega_AM.zip") as zf:
        assert zf.testzip() is None
    print("built entrega_AM.zip")


if __name__ == "__main__":
    run_scripts()
    build_pdf()
    build_pptx()
    build_zip()
    print("done")
