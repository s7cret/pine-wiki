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
    args = parser.parse_args()
    output = args.output or args.root / "docs" / "v5-example-audit.json"
    v5, _ = load_catalog(args.root, 5)
    v6, _ = load_catalog(args.root, 6)
    selected = {e["id"] for e in v5["entries"] if len(e["examples"].get("items", [])) > 1
                and all("\n" not in i["code"] for i in e["examples"]["items"])}
    if output.exists():
        selected.update(r["entry_id"] for r in json.loads(output.read_text("utf-8"))["entries"])
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
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report["counts"]))


if __name__ == "__main__":
    main()
