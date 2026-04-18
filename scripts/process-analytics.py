import json
import sys
from datetime import datetime, timezone

# Seccions de Machiroku
SECTION_MAP = {
    'inici':           'Inici',
    'oferta':          'Oferta gastronòmica',
    'reserves':        'Reserves',
    'sobre-nosaltres': 'Sobre nosaltres',
    'contacte':        'Contacte',
    'admin':           'Admin',
    'legals':          'Avís legal',
    'privacitat':      'Privacitat',
    'cookies':         'Cookies',
}

def safe_get(data, key, default=None):
    if data is None:
        return default
    return data.get(key, default)

def extract_lang(path):
    """Extreu l'idioma d'una URL de Machiroku.
    Producció: /ca/inici/ → ca
    Staging:   /machiroku-web/ca/inici/ → ca
    """
    parts = [p for p in path.strip('/').split('/') if p]
    if parts and parts[0] in ('ca', 'es', 'en'):
        return parts[0]
    if len(parts) >= 2 and parts[1] in ('ca', 'es', 'en'):
        return parts[1]
    return 'ca'

def extract_section(path):
    """Extreu la secció principal d'una URL de Machiroku.
    Producció: /ca/oferta/ → oferta
    Staging:   /machiroku-web/ca/oferta/ → oferta
    """
    if not path:
        return 'inici'
    parts = [p for p in path.strip('/').split('/') if p]
    # Producció: /lang/seccio/
    if parts and parts[0] in ('ca', 'es', 'en'):
        return parts[1] if len(parts) >= 2 else 'inici'
    # Staging: /machiroku-web/lang/seccio/
    if len(parts) >= 3:
        return parts[2]
    elif len(parts) == 2:
        return parts[1]
    return 'inici'

def main():
    if len(sys.argv) < 5:
        print("Ús: process-analytics.py <input.json> <output.json> <start> <end>")
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2]
    start_date  = sys.argv[3]
    end_date    = sys.argv[4]

    try:
        with open(input_file) as f:
            content = f.read().strip()
        if not content:
            print("⚠️  Fitxer d'entrada buit, generant analytics buit.")
            raw = {}
        else:
            raw = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"❌ JSON invàlid: {e}")
        sys.exit(1)

    # Hits: estructura GoatCounter v0:
    #   {hits: [{path, stats: [{day, hourly, daily}], total, total_unique}]}
    hits_data = safe_get(raw, "hits_data") or {}
    hits = safe_get(hits_data, "hits") or []

    by_lang    = {}
    by_section = {}
    total      = 0
    hits_by_day = {}

    for path_item in hits:
        path    = path_item.get("path", "")
        lang    = extract_lang(path)
        section = extract_section(path)

        for stat in path_item.get("stats", []):
            date  = (stat.get("day") or "")[:10]
            count = stat.get("daily", 0)
            if not count:
                continue
            total += count
            by_lang[lang]       = by_lang.get(lang, 0) + count
            by_section[section] = by_section.get(section, 0) + count
            if date:
                hits_by_day[date] = hits_by_day.get(date, 0) + count

    hits_by_day_list = [{"date": k, "count": v} for k, v in sorted(hits_by_day.items())]

    # Browsers, systems, sizes, locations
    # Estructura: {browsers: [{id, browser, stats: [{day, hourly, daily}], total}]}
    browsers_raw  = safe_get(safe_get(raw, "browsers")  or {}, "browsers")  or []
    systems_raw   = safe_get(safe_get(raw, "systems")   or {}, "systems")   or []
    sizes_raw     = safe_get(safe_get(raw, "sizes")     or {}, "sizes")     or []
    locations_raw = safe_get(safe_get(raw, "locations") or {}, "locations") or []

    def norm_items(items):
        out = []
        for item in items:
            name = (item.get("browser") or item.get("system") or item.get("size") or
                    item.get("location") or item.get("id") or "Desconegut")
            count = sum(s.get("daily", 0) for s in item.get("stats", []))
            if not count:
                count = item.get("total", 0)
            if count > 0:
                out.append({"name": name, "id": item.get("id", name), "count": count})
        return sorted(out, key=lambda x: x["count"], reverse=True)

    output = {
        "generated":   datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "period":      {"start": start_date, "end": end_date},
        "total":       total,
        "hits_by_day": hits_by_day_list,
        "by_lang":     by_lang,
        "by_section":  by_section,
        "browsers":    norm_items(browsers_raw),
        "systems":     norm_items(systems_raw),
        "sizes":       norm_items(sizes_raw),
        "locations":   norm_items(locations_raw),
    }

    import os
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Analytics processats: {total} visites")
    print(f"   Idiomes: {by_lang}")
    print(f"   Seccions: {by_section}")

if __name__ == "__main__":
    main()
