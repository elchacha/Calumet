#!/usr/bin/env python
"""
Generate a fully self-contained HowToStart.html from index.html.

index.html (the docs-site version) links ../shared.css and ../littlechaman-mascot.png.
Those assets do not exist at the Calumet release root, so for the release we inline:
  - the shared.css :root{} block (the only part index.html actually uses), and
  - the mascot image as a base64 data URI.

Single source of truth = index.html. Re-run this after editing index.html.
Output: HowToStart.html (next to index.html). Used by the release-builder (step 13).
"""
import base64
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent          # docs/starting/
DOCS = HERE.parent                               # docs/

src_html   = (HERE / "index.html").read_text(encoding="utf-8")
shared_css = (DOCS / "shared.css").read_text(encoding="utf-8")
mascot_b64 = base64.b64encode((DOCS / "littlechaman-mascot.png").read_bytes()).decode("ascii")

# 1. Inline the :root{} variables in place of the shared.css <link>.
root_match = re.search(r":root\{[^}]*\}", shared_css)
if not root_match:
    raise SystemExit("Could not find :root{} block in shared.css")
inline_style = "<style>" + root_match.group(0) + "</style>"
out = src_html.replace('<link rel="stylesheet" href="../shared.css">', inline_style)

# 2. Inline the mascot as a data URI.
out = out.replace('src="../littlechaman-mascot.png"',
                  'src="data:image/png;base64,' + mascot_b64 + '"')

# 3. The "back to documentation" link is meaningless standalone -> drop it.
out = re.sub(r'\s*<a class="gs-back"[^>]*>.*?</a>', "", out, flags=re.S)

(HERE / "HowToStart.html").write_text(out, encoding="utf-8")
print("Wrote", HERE / "HowToStart.html",
      "(" + str(len(out) // 1024) + " KB)")
