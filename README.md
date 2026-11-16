# Gale AI — website

Static site for Gale AI (AI call analytics for sales teams and contact centers), rebuilt from the old Tilda site in a new design.
Hosted on GitHub Pages.

## Edit & rebuild

```bash
python3 _build/build.py
```

- `_build/kit.py` — layout (header, footer) and page components
- `_build/pages_*.py` — page content (cases, partners, contact center, VN)
- `_build/src/landing-*.html` — hand-designed main pages (RU `/`, EN `/en/`)
- `_build/data/` — content pulled from the old Tilda pages (blog, privacy policy)
- `assets/` — styles and images

Generated pages are committed, so GitHub Pages serves them as-is.
