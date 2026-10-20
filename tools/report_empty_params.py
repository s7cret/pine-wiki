#!/usr/bin/env python3
"""CSV of missing source descriptions, optionally only those without a hint."""
import argparse
import csv
from pathlib import Path
import sys
from semantic_contracts import meaningful_text
from content_provenance import classify_content

sys.path.insert(0, str(Path(__file__).resolve().parent / "migrations"))
from catalog_io import ROOT, load_catalog, nonempty_text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, help="UTF-8 CSV destination; default: stdout")
    parser.add_argument("--without-hint", action="store_true")
    args = parser.parse_args()
    rows = []
    for version in range(1, 7):
        catalog, _ = load_catalog(args.root, version)
        for entry in catalog["entries"]:
            for parameter in entry["parameters"]:
                if meaningful_text(catalog["texts"].get(parameter.get("description"))):
                    continue
                if args.without_hint and parameter.get("description_hint"):
                    continue
                rows.append((version, entry["name"], parameter["name"], entry["id"], parameter.get('description_content_status','physically_empty'), bool(parameter.get('description_hint')), bool(parameter.get('description_supplement')), classify_content(catalog['texts'].get(parameter.get('description'),{}))))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        stream = args.output.open("w", encoding="utf-8", newline="")
    else:
        sys.stdout.reconfigure(encoding="utf-8", newline="")
        stream = sys.stdout
    try:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("version", "function", "parameter", "entry_id", "description_status", "has_neighbor_hint", "has_editorial_supplement", "main_content_origin"))
        writer.writerows(rows)
    finally:
        if args.output:
            stream.close()


if __name__ == "__main__":
    main()
