#!/usr/bin/env python3
"""Gera canvas-bundle.html: o canvas inteiro (manifesto + todas as telas) num único arquivo.
Use para publicar como artefato no Claude app, mandar para um cliente ou abrir sem servidor.
Uso: python .ai/design/canvas/bundle.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, "manifest.js"), encoding="utf-8").read()
m = re.search(r"window\.CANVAS\s*=\s*(\{.*\})\s*;?\s*$", src, re.S)
if not m:
    raise SystemExit("manifest.js inválido")
# o manifesto é JS (pode ter comentários/chaves sem aspas): avaliamos de forma segura via conversão simples
js = re.sub(r"//[^\n]*", "", m.group(1))
js = re.sub(r"([{,]\s*)([A-Za-z_][\w]*)\s*:", r'\1"\2":', js)
js = re.sub(r",\s*([}\]])", r"\1", js)
manifest = json.loads(js)
for sc in manifest.get("screens", []):
    path = os.path.join(ROOT, sc.get("file", ""))
    if os.path.isfile(path):
        sc["html"] = open(path, encoding="utf-8").read()
html = open(os.path.join(ROOT, "canvas.html"), encoding="utf-8").read()
inject = "<script>window.CANVAS_BUNDLED=true;window.CANVAS=" + json.dumps(manifest, ensure_ascii=False).replace("</", "<\\/") + ";</script>\n"
html = html.replace("<script>\n/* ---", inject + "<script>\n/* ---", 1)
out = os.path.join(ROOT, "canvas-bundle.html")
open(out, "w", encoding="utf-8").write(html)
print(f"Gerado: {out} ({len(html)//1024} KB, {len(manifest.get('screens', []))} telas)")
