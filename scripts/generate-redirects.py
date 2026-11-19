#!/usr/bin/env python3
"""
Genera pàgines de redirecció estàtiques a partir de data/redirects.yaml.

GitHub Pages no permet 301 reals, així que escrivim un index.html per a cada
URL antiga amb canonical + meta refresh + JS cap a la pàgina nova.
Aquests fitxers es copien a docs/ en fer el build de Hugo.

Ús:
    python3 scripts/generate-redirects.py

Els fitxers generats contenen el marcador "<!-- generated-redirect -->";
el script els esborra i els reescriu a cada execució (idempotent).
"""

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "redirects.yaml"
STATIC = ROOT / "static"
BASE = "https://machiroku.com"
MARKER = "<!-- generated-redirect -->"

LANGS = {"ca": "ca", "es": "es", "en": "en"}

TEMPLATE = """<!DOCTYPE html>
{MARKER}
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Redirigint… | Machiroku</title>
  <link rel="canonical" href="{base}{to}">
  <meta http-equiv="refresh" content="0; url={base}{to}">
  <script>window.location.replace("{base}{to}");</script>
  <style>
    body {{ font-family: sans-serif; text-align: center; padding: 50px; background: #f8f7ef; color: #1a1a1a; }}
    a {{ color: #8b1a1a; }}
  </style>
</head>
<body>
  <h1>Pàgina traslladada</h1>
  <p>Aquesta adreça ha canviat. <a href="{base}{to}">Continua a la pàgina nova</a>.</p>
</body>
</html>
"""


def lang_for(to: str) -> str:
    parts = [p for p in to.split("/") if p]
    return LANGS.get(parts[0], "ca") if parts else "ca"


def main() -> None:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    redirects = data["redirects"]

    # Neteja de redireccions generades anteriorment
    removed = 0
    for old in STATIC.rglob("index.html"):
        try:
            if MARKER in old.read_text(encoding="utf-8", errors="ignore"):
                old.unlink()
                removed += 1
        except OSError:
            pass

    written = 0
    for r in redirects:
        src = r["from"]
        dst = r["to"]
        if not (src.startswith("/") and src.endswith("/")):
            raise SystemExit(f"URL origen no vàlida (ha de començar i acabar amb /): {src}")
        if not (dst.startswith("/") and dst.endswith("/")):
            raise SystemExit(f"URL destí no vàlida (ha de començar i acabar amb /): {dst}")

        out = STATIC / src.strip("/") / "index.html"
        if out.exists() and MARKER not in out.read_text(encoding="utf-8", errors="ignore"):
            raise SystemExit(f"REFUSAT: {out} ja existeix i no és una redirecció generada")

        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            TEMPLATE.format(MARKER=MARKER, lang=lang_for(dst), base=BASE, to=dst),
            encoding="utf-8",
        )
        written += 1

    print(f"Redireccions generades: {written} (esborrades {removed})")


if __name__ == "__main__":
    main()
