# Portfolio — project notes

Handoff for any future session. Read this first, then `README.md`.

## How the site is built

- `tools/build_pages.py` holds all page content and generates `index.html` and the four `case-*.html` pages. Edit content there, then run it from the `tools` folder: `python3 build_pages.py`.
- `tools/build_preview.py` bundles everything into one self-contained `portfolio-preview.html` (used for the claude.ai preview link). It is a derived file, so it isn't stored in this folder.
- `styles.css` is the design system. `design-system.html` documents it.
- Don't hand-edit the generated HTML pages; the next build overwrites them.

## Decisions so far

- **Name on the site:** Chenxi Liu. Role on every project: Lead product designer. Hero says "UX designer".
- **Type:** Space Mono for the site name, hero name, section headings, project titles, and numbers. Plus Jakarta Sans for everything else. Project titles and section headings are uppercase via CSS; the hero statement is sentence case.
- **Color:** light neutral background, near-black ink, vermilion accent (#B8361A) for links and hover only, bright vermilion (#F0583A) for fills and rules, never as text. Dark ink panel for About.
- **Buttons:** solid ink button for primary actions ("Read case study", "Download resume"). Outline button for secondary ("LinkedIn").
- **Home page:** hero (name + statement), Work (four cards; "Read case study" is the only link on each card), Impact (four figures), About (dark panel with grayscale photo, resume and LinkedIn buttons). Nav: Work, About, Download resume. No header name on the home page.
- **Project order and titles:**
  1. Years of Consultant Expertise Made Interactive (Parallel chatbot)
  2. Designing an Internal Operating System (Parallel admin tool)
  3. Two Beauty Brands, Two Different UX Strategies (Peace Out + Winky Lux audits, one combined case study)
  4. Maya Migrate
- **Project card covers:** 1600 × 1200, light gray (#E6E9EC) background, one tightly cropped real screen centered with a 3px ink border. Cards keep a 4:3 image on phones so nothing is cropped. Chatbot cover = the chat entry panel (word cloud + book-a-call). Admin cover = Overview, last 7 days: header, KPIs, meeting mix, client status (no sidebar). Audits cover = my Peace Out concern-first navigation mockup (option A); may become a split cover with a Winky Lux family-grid mockup later.
- **Case-study figures:** real screens get the `media-img` style (full width, ink border). Chatbot hero figure = full v2 hero; admin first figure = full Overview.
- **Case study structure:** summary (role, team, timeline, problem, outcome), context, core story, design, results and what's next, looking back.
- **Confidentiality:** no participant or stakeholder names, no budgets or rates, nothing from Winky Lux's internal brand book or the agency's internal procedure vocabulary.

## Facts to keep straight

- Chatbot: Chenxi designed v1, ran a moderated study of it with 3 participants plus a survey, found 6 ranked frictions, wrote the approved v2 scope. 2026.
- Admin tool: review found ~16 of 328 recorded calls had usable analysis, 75 of 96 chatbot conversations were cold; 23 findings (8 high, 11 medium, 4 polish). v3 designed; v4 will follow the agency's operating procedure.
- Audits: Peace Out 15 findings (9 major), July 2026. Winky Lux 19 findings, August 2026. 34 total. Winky Lux lip page: ~60 tiles to ~25 choices (a recommendation, not a measured result).

## Source images

- Chatbot hero: embedded in Parallel_Chatbot_v2_Scope.pdf (page 4).
- Peace Out mockups: embedded in PeaceOut_UX_UI_Review.pdf (concern-first nav on page 2, product page on page 3, current header on page 5). Extract with `pdfimages -png`.
- Admin screens: Figma file NRFjA4yDfO6P3B3Q3b8bVY (Parallel Designs). Export frames as PNG at 2x and upload; the container can't download from Figma directly.

## Still to do

- Impact section: confirm figures with the founder (replace "Live"; label "60 → 25" as a recommendation).
- Results on every case study: add data as the founder provides it.
- Maya Migrate case study: team, timeline, reflection (waiting on source material).
- Winky Lux "after" image caption: add a mockup or remove the pair.
- Project card cover still needed: Maya Migrate (phone screens).
- Optional: a Winky Lux family-grid mockup ("8 flavors, from $18") to fill the Winky Lux after image and make the audits cover a split.
- Admin figures still needed: Checkpoints rear view (Figma node 975-2465) and By client (975-2189); remaining figures on other case studies.
- Add `resume.pdf` to this folder.
- Deploy (GitHub Pages or Netlify), likely via Claude Code.
