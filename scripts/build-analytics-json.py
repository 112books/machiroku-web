import json
import sys
from datetime import datetime, timezone

def load(path):
    try:
        with open(path) as f:
            content = f.read().strip()
        if not content or content == "null":
            print(f"WARN: {path} buit o null", file=sys.stderr)
            return None
        parsed = json.loads(content)
        # Debug: mostra estructura del primer element per diagnosticar canvis d'API
        for key, val in (parsed.items() if isinstance(parsed, dict) else []):
            if isinstance(val, list) and val:
                print(f"DEBUG {path} → {key}[0] keys: {list(val[0].keys())}", file=sys.stderr)
                break
        return parsed
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"WARN: JSON invalid a {path}: {e}", file=sys.stderr)
        return None

start = sys.argv[1] if len(sys.argv) > 1 else ""
end   = sys.argv[2] if len(sys.argv) > 2 else ""

data = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "period": {"start": start, "end": end},
    "hits_data":  load("/tmp/hits.json"),
    "browsers":   load("/tmp/browsers.json"),
    "systems":    load("/tmp/systems.json"),
    "sizes":      load("/tmp/sizes.json"),
    "locations":  load("/tmp/locations.json"),
}

with open("/tmp/raw_all.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON generat correctament")
