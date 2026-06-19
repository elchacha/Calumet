#!/usr/bin/env python
"""Build the standalone field-catalog viewer (catalog.html) by embedding the per-object
JSON into the viewer template.

This is the quick test bench for the HTML/JS template; the production equivalent is
com.calumet.sftool.metadata.fieldcatalog.FieldCatalogHtml (kept in sync with this logic).

Usage:
    python docs/field-catalog/embed.py <fieldCatalogDir> [viewerHtml]

  <fieldCatalogDir> : folder holding index.json + <Object>.json
                      (e.g. C:\\Tool\\Calumet\\orgs\\<org>\\fieldCatalog)
  [viewerHtml]      : viewer template (default: index.html next to this script)

Writes <fieldCatalogDir>/catalog.html (self-contained, data embedded).
"""
import json, os, glob, sys

if len(sys.argv) < 2:
    print("usage: python docs/field-catalog/embed.py <fieldCatalogDir> [viewerHtml]")
    raise SystemExit(2)

catalog_dir = sys.argv[1]
viewer = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

index_path = os.path.join(catalog_dir, "index.json")
if not os.path.exists(index_path):
    print("index.json not found in", catalog_dir, "- run field_catalog first")
    raise SystemExit(1)

tpl = open(viewer, encoding="utf-8").read()
index = json.load(open(index_path, encoding="utf-8"))
objects = [json.load(open(f, encoding="utf-8"))
           for f in sorted(glob.glob(os.path.join(catalog_dir, "*.json")))
           if os.path.basename(f) != "index.json"]

# escape </ so the embedded JSON cannot close the <script> tag
payload = json.dumps({"index": index, "objects": objects}, ensure_ascii=False).replace("</", "<\\/")
out = os.path.join(catalog_dir, "catalog.html")
open(out, "w", encoding="utf-8").write(
    tpl.replace("</body>", f'<script>window.__CATALOG__={payload};</script>\n</body>', 1))
print("regenerated", out, "| objects:", len(objects))
