#!/usr/bin/env python3
"""Z-03: remove empty editorial texts; add explicit cross-version hints."""
import argparse
from copy import deepcopy
import json

from catalog_io import ROOT, load_catalog, nonempty_text, save_catalog

# Reviewed correspondences within the existing family graph. No positional or
# fuzzy matching: RSI overloads and variadic groups are deliberately excluded.
RENAMED_PARAMETERS = {
    **{(f"functions:math.{name}", "x"): "number" for name in
       ("abs", "log", "log10", "sqrt", "sign", "exp", "ceil", "floor")},
    **{(f"functions:math.{name}", "x"): "angle" for name in ("asin", "acos", "atan")},
    ("functions:fixnan", "x"): "source",
    ("functions:ta.cum", "x"): "source",
    ("functions:ta.cross", "x"): "source1",
    ("functions:ta.cross", "y"): "source2",
}
EMPTY_REMARKS = "e3b0c44298fc1c14"


def donor_for(catalogs, version, entry, parameter):
    family = entry["family"]["id"]
    target_names = [parameter["name"]]
    renamed = RENAMED_PARAMETERS.get((family, parameter["name"]))
    if renamed:
        target_names.append(renamed)
    for donor_version in range(version + 1, 7):
        # Prefer the literal parameter name before the reviewed rename.
        for target_name in target_names:
            candidates = []
            for donor in catalogs[donor_version]["entries"]:
                if donor["family"]["id"] != family or donor["category"] != entry["category"]:
                    continue
                for param in donor["parameters"]:
                    if param["name"] == target_name and nonempty_text(catalogs[donor_version]["texts"].get(param.get("description"))):
                        candidates.append((donor, param))
            if candidates:
                # Multiple overloads are safe only when their actual texts agree.
                texts = {json.dumps(catalogs[donor_version]["texts"][p["description"]], sort_keys=True) for _, p in candidates}
                if len(texts) != 1:
                    return None
                donor, param = candidates[0]
                return {"version": donor_version, "entry_id": donor["id"],
                        "parameter": param["name"], "text": param["description"],
                        "sources": deepcopy(donor["sources"])}
    return None


def clear_empty_references(value, empty_ids):
    """Empty examples.note uses the same placeholder as result.description."""
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, str) and item in empty_ids:
                value[key] = None
            else:
                clear_empty_references(item, empty_ids)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, str) and item in empty_ids:
                value[index] = None
            else:
                clear_empty_references(item, empty_ids)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    loaded = {v: load_catalog(args.root, v) for v in range(1, 7)}
    catalogs = {v: data for v, (data, _) in loaded.items()}
    # Keep donors frozen during the migration; no hint is used as primary proof.
    originals = deepcopy(catalogs)
    stats = {"changed_catalogs": [], "hints_added": {}, "missing_marked": {}, "texts_removed": {}}
    for version, catalog in catalogs.items():
        hints = missing = 0
        empty_ids = {ref for ref, text in catalog["texts"].items()
                     if ref != EMPTY_REMARKS and text.get("basis") and not nonempty_text(text)}
        for entry in catalog["entries"]:
            for parameter in entry["parameters"]:
                if nonempty_text(catalog["texts"].get(parameter.get("description"))):
                    continue
                parameter["description"] = None
                if parameter.get("description_hint"):
                    continue
                hint = donor_for(originals, version, entry, parameter)
                if hint:
                    donor_text = originals[hint["version"]]["texts"][hint["text"]]
                    previous = catalog["texts"].get(hint["text"])
                    if previous is not None and previous != donor_text:
                        raise ValueError(f"Conflicting text ID {hint['text']} in v{version}")
                    catalog["texts"][hint["text"]] = deepcopy(donor_text)
                    parameter["description_hint"] = hint
                    parameter.pop("description_missing", None)
                    hints += 1
                elif not parameter.get("description_missing"):
                    parameter["description_missing"] = True
                    missing += 1
        clear_empty_references(catalog["entries"], empty_ids)
        for ref in empty_ids:
            del catalog["texts"][ref]
        if catalog != originals[version]:
            save_catalog(catalog, loaded[version][1], args.dry_run)
            stats["changed_catalogs"].append(version)
        stats["hints_added"][version] = hints
        stats["missing_marked"][version] = missing
        stats["texts_removed"][version] = len(empty_ids)
    stats["dry_run"] = args.dry_run
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
