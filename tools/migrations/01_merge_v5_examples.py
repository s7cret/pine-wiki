#!/usr/bin/env python3
"""Z-01: reassemble line-fragmented v5 examples, retaining their exact code."""
import argparse
from copy import deepcopy
import json
import re

from catalog_io import ROOT, load_catalog, save_catalog

VERSION_DIRECTIVE = re.compile(r"^\s*//\s*@version\s*=\s*\d+\s*$")


def merge_items(items):
    if len(items) <= 1 or any("\n" in item["code"] for item in items):
        return items
    groups = []
    for item in items:
        if not groups or VERSION_DIRECTIVE.fullmatch(item["code"]):
            groups.append([])
        groups[-1].append(item)
    merged = []
    for group in groups:
        # Preserve every field of the first element, not only the source record.
        item = deepcopy(group[0])
        item["code"] = "\n".join(fragment["code"] for fragment in group)
        merged.append(item)
    return merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=str, default=str(ROOT))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    catalog, wrapper = load_catalog(args.root, 5)
    before = sum(len(e["examples"].get("items", [])) for e in catalog["entries"])
    changed = 0
    for entry in catalog["entries"]:
        items = entry["examples"].get("items", [])
        merged = merge_items(items)
        if merged != items:
            entry["examples"]["items"] = merged
            changed += 1
    if changed:
        save_catalog(catalog, wrapper, args.dry_run)
    after = sum(len(e["examples"].get("items", [])) for e in catalog["entries"])
    print(json.dumps({"changed_entries": changed, "items_before": before,
                      "items_after": after, "dry_run": args.dry_run}))


if __name__ == "__main__":
    main()
