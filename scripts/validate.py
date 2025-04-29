#!/usr/bin/env python3
"""validate.py – reiner JSON-Schema-Check

Usage:
    python scripts/validate.py  [--file fragenkatalog.json] [--schema schema.json]

Exit-Codes:
    0 → Datei erfüllt Schema
    1 → Schema-Verletzung oder Datei nicht gefunden
"""

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator, ValidationError


def load_json(path: Path):
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Datei nicht gefunden: {path}")
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description="Validiert fragenkatalog.json gegen schema.json")
    ap.add_argument("--file", default="fragenkatalog.json", help="Pfad zur Fragen-JSON")
    ap.add_argument("--schema", default="schema.json", help="Pfad zum JSON-Schema")
    args = ap.parse_args()

    data   = load_json(Path(args.file))
    schema = load_json(Path(args.schema))

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(data))

    if errors:
        print("❌ Schema-Verletzungen:\n")
        for err in errors:
            loc = " → ".join(str(p) for p in err.path)
            print(f"* {loc}: {err.message}")
        sys.exit(1)

    print("✅ JSON entspricht dem Schema.")
    sys.exit(0)


if __name__ == "__main__":
    main()
