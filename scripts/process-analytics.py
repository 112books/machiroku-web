import json
import sys
from datetime import datetime

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

def extract_section(path):
    """Extreu la secció principal d'una URL de Machiroku.
    /machiroku-web/ca/oferta/ → oferta
    /machiroku-web/es/reserves/ → reserves
    """
    if not path:
        return 'inici'
    parts = [p for p in path.strip('/').split('/') if p]
    # Estructura: machiroku-web / lang / seccio
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

    # Hits
    hits_data = safe_get(raw, "hits_data") or {}
    hits = safe_get(hits_data, "hits") or []

    # Totals per idioma i secció
    by_lang    = {}
    by_section = {}
    total      = 0

    for day in hits:
        for stat in safe_get(day, "stats") or []:
            path  = safe_get(stat, "path", "")
            count = safe_get(stat, "count", 0)
            total += count

            # Idioma: /machiroku-web/ca/ → ca
            parts = [p for p in path.strip('/').split('/') if p]
            lang = parts[1] if len(parts) >= 2 and parts[1] in ('ca', 'es', 'en') else 'ca'
            by_lang[lang] = by_lang.get(lang, 0) + count

            # Secció
            section = extract_section(path)
            by_section[section] = by_section.get(section, 0) + count

    # Hits per dia
    hits_by_day = {}
    for day in hits:
        date = (day.get("day") or "")[:10]
        if not date:
            continue
        day_total = sum(s.get("count", 0) for s in day.get("stats", []))
        if day_total > 0:
            hits_by_day[date] = hits_by_day.get(date, 0) + day_total

    hits_by_day_list = [{"date": k, "count": v} for k, v in sorted(hits_by_day.items())]

    # La resta
    browsers_raw  = safe_get(safe_get(raw, "browsers")  or {}, "browsers")  or []
    systems_raw   = safe_get(safe_get(raw, "systems")   or {}, "systems")   or []
    sizes_raw     = safe_get(safe_get(raw, "sizes")     or {}, "sizes")     or []
    locations_raw = safe_get(safe_get(raw, "locations") or {}, "locations") or []

    def norm_items(items):
        out = []
        for item in items:
            name = item.get("browser") or item.get("system") or item.get("size") or item.get("location") or item.get("id") or "Desconegut"
            count = sum(s.get("count", 0) for s in item.get("stats", [])) or item.get("count", 0)
            if count > 0:
                out.append({"name": name, "id": name, "count": count})
        return sorted(out, key=lambda x: x["count"], reverse=True)

    output = {
        "generated":   datetime.utcnow().isoformat() + "Z",
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
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Analytics processats: {total} visites")
    print(f"   Idiomes: {by_lang}")
    print(f"   Seccions: {by_section}")

if __name__ == "__main__":
    main()
