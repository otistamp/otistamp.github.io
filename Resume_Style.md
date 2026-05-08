# Resume Style Guide

## Concept

Terminal-inspired layout with a vertical split. Left panel mimics a dark terminal sidebar
(Catppuccin Mocha); right panel is the main content pane in a light complement
(Catppuccin Latte). Font throughout is Inconsolata.

---

## Font

**Inconsolata**
- Use for all text: headings, body, labels
- Recommended weights: 400 (body), 600 (section labels / company names), 700 (name / title)

---

## Layout

Two-column vertical split, approximately 30% left / 70% right.

**Left panel** - Catppuccin Mocha (dark)
Contains: name, title, contact info, summary, strengths, technology summary, education

**Right panel** - Catppuccin Latte (light)
Contains: experience (all roles, reverse chronological)

---

## Catppuccin Mocha Palette (left panel)

| Role              | Name       | Hex       |
|-------------------|------------|-----------|
| Panel background  | Base       | #1e1e2e   |
| Section bg / alt  | Mantle     | #181825   |
| Borders / dividers| Surface0   | #313244   |
| Muted text        | Subtext0   | #a6adc8   |
| Body text         | Text       | #cdd6f4   |
| Name / headings   | Lavender   | #b4befe   |
| Section labels    | Mauve      | #cba6f7   |
| Accent / links    | Blue       | #89b4fa   |
| Bullet markers    | Teal       | #94e2d5   |
| Contact links     | Peach      | #fab387   |
| Active role date  | Green      | #a6e3a1   |

---

## Catppuccin Latte Palette (right panel)

| Role              | Name       | Hex       |
|-------------------|------------|-----------|
| Panel background  | Base       | #eff1f5   |
| Section bg / alt  | Mantle     | #e6e9ef   |
| Borders / dividers| Surface0   | #ccd0da   |
| Muted text        | Subtext0   | #6c6f85   |
| Body text         | Text       | #4c4f69   |
| Company names     | Blue       | #1e66f5   |
| Job titles        | Mauve      | #8839ef   |
| Date ranges       | Subtext0   | #6c6f85   |
| Bullet markers    | Teal       | #179299   |
| Active role "Present" | Green  | #40a02b   |
| Contact links     | Peach      | #fe640b   |

---

## Typography Scale

| Element           | Size  | Weight | Color (Mocha)     | Color (Latte)     |
|-------------------|-------|--------|-------------------|-------------------|
| Name              | 24pt  | 700    | Lavender #b4befe  | -                 |
| Title (tagline)   | 11pt  | 400    | Mauve #cba6f7     | -                 |
| Section label     | 9pt   | 600    | Mauve #cba6f7     | Mauve #8839ef     |
| Company name      | 11pt  | 600    | -                 | Blue #1e66f5      |
| Job title         | 10pt  | 600    | -                 | Mauve #8839ef     |
| Date / location   | 9pt   | 400    | Subtext0 #a6adc8  | Subtext0 #6c6f85  |
| Body / bullets    | 9pt   | 400    | Text #cdd6f4      | Text #4c4f69      |

---

## Spacing Notes

- Consistent left padding inside each panel: 16-20pt
- Section label: small-caps or letter-spaced uppercase
- Thin horizontal rule between sections using Surface0 color of the respective panel
- Bullet marker: use panel Teal color; indent body text 10pt from marker
- Role separator (between jobs on right panel): 1px rule in Surface0 #ccd0da
