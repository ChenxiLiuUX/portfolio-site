# Chenxi Liu — Portfolio site

Plain HTML and CSS. No build step, no framework.

## Files

- `index.html` — home: hero, project cards, impact, about
- `case-parallel-chatbot.html` — research-led case study
- `case-maya-migrate.html` — decision-led case study
- `case-parallel-admin.html` — decision-led case study
- `case-shopify-audits.html` — before/after case study (Peace Out, Winky Lux)
- `styles.css` — the design system. Every color, size, and space comes from tokens here.
- `images/` — photos and project images (keep them under ~200 KB each)
- `design-system.html` — documentation for the system (not linked from the site)

## Preview

Open `index.html` in a browser, or run a local server from this folder:

    python3 -m http.server 8000

then visit http://localhost:8000

## Before publishing

- Replace every `.todo` span (dashed highlight) with real content. Search the files for `class="todo"`.
- Replace `.media` and `.card__media` placeholders with exported images, and give each a real `alt`.
- Fill in metrics as results come in (the `—` values).
- Add your resume as `resume.pdf` in this folder (the nav link and the About button both point to it).
- Confirm with each client what can be shown publicly.

## Rules

Use the tokens in `styles.css`. Don't add per-page colors or one-off sizes; extend the system instead and document the change in `design-system.html`.
