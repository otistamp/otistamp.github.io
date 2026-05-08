#!/usr/bin/env python3
"""Render resume.html to PDF using WeasyPrint."""

import sys
from pathlib import Path

try:
    from weasyprint import HTML
except ImportError:
    print("WeasyPrint not installed. Run: uv add weasyprint")
    sys.exit(1)

src = Path(__file__).parent / "index.html"
out = Path(__file__).parent / "resume.pdf"

doc = HTML(filename=str(src)).render()
pages = len(doc.pages)
doc.write_pdf(str(out))
print(f"Rendered: {out} ({pages} page{'s' if pages != 1 else ''})")
if pages > 1:
    print(f"WARNING: {pages} pages — content overflows")
