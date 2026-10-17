#!/usr/bin/env python3
"""Remove only unreferenced history text records; preserve JSON and JS order."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data_integrity import text_references

ROOT = Path(__file__).resolve().parents[2]


def load_history(root, shard):
    path = root / f"history-{shard}.js"
    original = path.read_bytes().decode("utf-8")
    marker = f'window.PINE_HISTORY["{shard}"]='
    prefix, separator, payload = original.partition(marker)
    if not separator:
        raise ValueError(f"Unexpected history wrapper: {path}")
    whitespace = payload[:len(payload) - len(payload.lstrip())]
    data, end = json.JSONDecoder().raw_decode(payload.lstrip())
    suffix = payload.lstrip()[end:]
    if suffix.strip() != ";":
        raise ValueError(f"Unexpected trailing history content: {path}")
    return data, (path, prefix + separator + whitespace, suffix)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    loaded = {shard: load_history(args.root, shard) for shard in "0123456789abcdef"}
    removals = {}
    # Validate every shard before writing any of them. A dangling reference is
    # a separate data error; never turn it into an apparent successful cleanup.
    for shard, (data, _) in loaded.items():
        used = {ref for ref, _ in text_references(data)}
        missing = used - data["texts"].keys()
        if missing:
            raise ValueError(f"history-{shard}: missing text references: {sorted(missing)}")
        removals[shard] = sorted(data["texts"].keys() - used)
    for shard, (data, wrapper) in loaded.items():
        if not removals[shard]:
            continue
        for ref in removals[shard]:
            del data["texts"][ref]
        if not args.dry_run:
            path, prefix, suffix = wrapper
            path.write_bytes((prefix + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + suffix).encode("utf-8"))
    print(json.dumps({"removed": {shard: len(ids) for shard, ids in removals.items()},
                      "total_removed": sum(map(len, removals.values())), "dry_run": args.dry_run}))


if __name__ == "__main__":
    main()
