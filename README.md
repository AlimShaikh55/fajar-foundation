# Fajar Foundation website

Plain HTML/CSS/JS. No build step needed to host it: upload this folder to GitHub Pages as is.

## Before going live: fill these in
Search the HTML for `class="placeholder"` (shown with a dashed yellow highlight).

1. **CIN**: in the footer of every page and on transparency.html. Easiest: edit `CIN = ...` in build.py and run `python3 build.py`.
2. **Team photos**: add `assets/img/team/alim.jpg`, `kartik.jpg`, `nitin.jpg` (portrait, about 800×1000 px). Until then, initials are shown.
3. **Bios** for Kartik and Nitin on about.html. Review Alim's bio too.
4. **Logo**: the pinwheel is drawn in code. To use your real logo, replace the SVG in `PINWHEEL` in build.py and `assets/img/favicon.svg`.
5. **Certificate of Incorporation**: add the PDF to `assets/docs/` and link it on transparency.html.
6. When 12A, 80G or CSR-1 come through, update transparency.html and get-involved.html.

## Editing
Each page's content lives in build.py (shared header and footer). Edit there, run `python3 build.py`, and the HTML files regenerate.
Or edit the .html files directly if you don't plan to use the script.

## Deploy on GitHub Pages
1. Push the contents of this folder to the repo root.
2. Settings → Pages → Deploy from branch → main / root.
3. For fajarfoundation.org, add a `CNAME` file containing the domain and point DNS to GitHub Pages.
