#!/usr/bin/env python3
"""Reproduce the v5/v6 comparison without changing catalogs (stdlib only)."""
import argparse
import collections
import difflib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "migrations"))
from catalog_io import ROOT, load_catalog

MERGE_MANIFEST = Path(__file__).resolve().parent / 'migrations' / 'v5_example_merge_manifest.json'


def selected_entries(catalog):
    # This immutable input was reconstructed from the pre-migration catalog,
    # not from the generated audit. It works before and after line merging.
    manifest = json.loads(MERGE_MANIFEST.read_text(encoding='utf-8'))
    ids = manifest['entry_ids']
    if manifest.get('schema_version') != 1 or not ids or len(ids) != len(set(ids)):
        raise ValueError('Invalid v5 example merge manifest')
    selected = set(ids)
    missing = selected - {e['id'] for e in catalog['entries']}
    if missing:
        raise ValueError('Merged v5 entries missing from catalog: ' + ', '.join(sorted(missing)))
    return selected


def normalized(code, trailing_space=False):
    lines = []
    for line in code.splitlines():
        if not line.strip():
            continue
        if re.fullmatch(r"\s*//\s*@version\s*=\s*\d+\s*", line):
            line = "//@version=N"
        lines.append(line.rstrip() if trailing_space else line)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true", help="Compare the regenerated audit without writing files")
    args = parser.parse_args()
    output = args.output or args.root / "docs" / "v5-example-audit.json"
    v5, _ = load_catalog(args.root, 5)
    v6, _ = load_catalog(args.root, 6)
    selected = selected_entries(v5)
    records = []
    for entry in v5["entries"]:
        if entry["id"] not in selected:
            continue
        code = "\n".join(i["code"] for i in entry["examples"]["items"])
        candidates = [(e, i["code"]) for e in v6["entries"]
                      if (e["name"], e["category"]) == (entry["name"], entry["category"])
                      for i in e["examples"].get("items", [])]
        exact = next(((e, c) for e, c in candidates if normalized(c) == normalized(code)), None)
        trailing = next(((e, c) for e, c in candidates if normalized(c, True) == normalized(code, True)), None)
        record = {"entry_id": entry["id"], "name": entry["name"], "category": entry["category"]}
        if exact:
            record.update(comparison="same_except_version_and_empty_lines", donor_entry_id=exact[0]["id"])
        elif trailing:
            record.update(comparison="trailing_whitespace_only", donor_entry_id=trailing[0]["id"])
        elif candidates:
            donor, other = max(candidates, key=lambda p: difflib.SequenceMatcher(None, normalized(code, True), normalized(p[1], True)).ratio())
            record.update(comparison="reviewed_difference", donor_entry_id=donor["id"],
                          diff="\n".join(difflib.unified_diff(normalized(code, True).splitlines(),
                               normalized(other, True).splitlines(), fromfile="v5", tofile="v6", lineterm="")))
        else:
            record["comparison"] = "no_v6_example"
        records.append(record)
    report = {"normalization": "Ignore only standalone @version values and empty lines; additionally classify trailing whitespace separately. Preserve indentation and internal whitespace.",
              "counts": dict(collections.Counter(r["comparison"] for r in records)), "entries": records}
    rendered = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode('utf-8')
    if args.check:
        if not output.exists() or output.read_bytes() != rendered:
            raise SystemExit('V5 example audit is missing or stale: ' + str(output))
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(rendered)
    print(json.dumps(report["counts"]))


if __name__ == "__main__":
    main()
