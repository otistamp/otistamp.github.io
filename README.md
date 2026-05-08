# resume

A code-driven resume built with HTML/CSS and rendered to PDF via WeasyPrint. Designed as a terminal-inspired two-column layout using the [Catppuccin](https://github.com/catppuccin/catppuccin) Mocha (dark) and Latte (light) palettes with Inconsolata as the typeface.

## Setup

**System dependency** (macOS):

```bash
brew install pango
```

**Python dependencies:**

```bash
uv sync
```

## Usage

Render to PDF:

```bash
uv run python render_resume.py
```

Output: `resume.pdf`. The script warns if content overflows past one page.

Live preview in browser (faster for design iteration):

```bash
uv run python -m http.server 8767
```

Then open `http://localhost:8767/index.html`. For color reference, open `http://localhost:8767/palette.html`.

## Structure

```
index.html         # Source — all content and styles live here
render_resume.py   # HTML → PDF via WeasyPrint
palette.html       # Color swatch reference for both Catppuccin palettes
Resume_Base.md     # Job-agnostic content source (keep in sync with HTML)
Resume_Style.md    # Design spec: color roles, typography scale, spacing
```

Job-specific variant files (`Resume_<Company>.md`) are gitignored and kept local only.

## Creating a job-specific variant

1. Create `Resume_<Company>.md` locally (it will not be committed)
2. Write a targeted summary and note any bullet tweaks
3. Before rendering, apply the summary override in `index.html`
4. Render and save the output PDF under a descriptive name

## Design

The full Catppuccin Mocha and Latte palettes are available as CSS variables in `resume.html` (`--mocha-*` and `--latte-*`). See `Resume_Style.md` for the current color role assignments.
