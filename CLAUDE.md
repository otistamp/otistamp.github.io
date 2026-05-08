# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Rendering the PDF

```bash
uv run python render_resume.py
```

Output is `resume.pdf`. The script prints the page count and warns if content overflows past 1 page — keep it at 1 page.

To preview in a browser (faster iteration than re-rendering to PDF):

```bash
uv run python -m http.server 8767
# then open http://localhost:8767/index.html
```

WeasyPrint requires Pango/GObject system libraries. On macOS install via Homebrew: `brew install pango`.

## File structure

- `index.html` — single source of truth for content and CSS. Edit this to change layout, colors, or copy.
- `render_resume.py` — renders `index.html` → `resume.pdf` via WeasyPrint.
- `Resume_Base.md` — job-agnostic markdown copy of the resume content. Keep in sync with `index.html` when updating copy.
- `Resume_Style.md` — design reference: color role assignments for both palettes, typography scale, spacing notes.
- `palette.html` — standalone color swatch page showing all Catppuccin Mocha and Latte colors rendered in-palette for visual reference when tweaking.
- `Resume_<Company>.md` — job-specific variant files (gitignored, local only). Document summary overrides and interview notes. Do not commit these.

## Design system

Two-column vertical split (30% left / 70% right). Font is Inconsolata committed at `fonts/Inconsolata.ttf`.

Full Catppuccin Mocha (left panel) and Latte (right panel) palettes are defined as CSS variables in `index.html` — all 26 colors each. Reference `Resume_Style.md` for which variable maps to which element. When changing a color, update the `var(--mocha-*)` or `var(--latte-*)` reference in the relevant CSS rule; no hex codes needed inline.

**Do not use em dashes** in any resume markdown or HTML content - use a spaced hyphen ` - ` instead.

## Job-specific variants

`Resume_Base.md` holds neutral content. Job-specific files (`Resume_<Company>.md`) are gitignored and kept local only - document summary overrides, bullet tweaks, and interview notes there. Do not modify the base or commit variants.

When targeting a specific role, apply the variant's summary override directly in `index.html` before rendering.
