#!/usr/bin/env python3
"""Z-11: register saved requiredness discrepancies without resolving them."""
import argparse
from copy import deepcopy
import hashlib
import json

from catalog_io import ROOT, load_catalog, save_catalog


def issue_for(catalog, entry, parameter):
    version = catalog["version"]
    identity = entry["id"] + "\0" + parameter["name"]
    issue_id = f"SOURCE.CONFLICT.V{version}.PARAMETER_REQUIREDNESS." + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12].upper()
    metadata = parameter.get("metadata_state")
    prose = parameter.get("prose_state")
    return {
        "id": issue_id,
        "versions": [version],
        "type": "source_conflict",
        "status": "recorded_source_caveat",
        "entry_id": entry["id"],
        "parameter": parameter["name"],
        "metadata_state": metadata,
        "prose_state": prose,
        "source_snapshot": catalog["snapshot"],
        "reviewed_on": "2026-10-17",
        "review": {
            "status": "snapshot_provenance_and_bilingual_summary_checked",
            "current_behavior_status": "not_revalidated",
            "runtime_validation": False,
            "source_revision_rechecked_online": False,
            "linked_clauses_checked": 0,
            "missing_linked_clauses": 0,
            "scope": {
                "ru": "Сопоставлены сохранённые metadata_state и prose_state параметра. Исходные страницы и поведение Pine заново не проверялись.",
                "en": "The parameter's saved metadata_state and prose_state were compared. Source pages and Pine behavior were not revalidated."
            }
        },
        "title": {
            "ru": f"Обязательность {entry['name']}({parameter['name']}): расхождение разметки",
            "en": f"{entry['name']}({parameter['name']}): requiredness metadata discrepancy"
        },
        "summary": {
            "ru": f"В сохранённой карточке {entry['id']} параметр {parameter['name']} имеет metadata_state={metadata}, prose_state={prose} и state=conflict. Эти значения описывают расхождение двух представлений источника в каталоге, а не установленный конфликт правил языка.",
            "en": f"In saved entry {entry['id']}, parameter {parameter['name']} has metadata_state={metadata}, prose_state={prose}, and state=conflict. This records disagreement between two source representations in the catalog, not a confirmed contradiction in language rules."
        },
        "effect": {
            "ru": "Статус conflict сохранён. Описание необязательного аргумента может относиться к функции в целом, а метаданные обязательности — к отдельной перегрузке; без проверки исходного контекста обязательность не переопределяется.",
            "en": "The conflict status is retained. Optional-argument prose may describe the function overall while requiredness metadata describes a particular overload; requiredness is not overridden without checking the source context."
        },
        "sources": deepcopy(entry["sources"]),
        "origin": [{"artifact": f"catalog-v{version}.js", "field": "entries[].parameters[]",
                    "id": entry["id"], "parameter": parameter["name"], "snapshot": catalog["snapshot"]}]
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    counts = {}
    for version in range(1, 7):
        catalog, wrapper = load_catalog(args.root, version)
        issues = catalog.setdefault("source_issues", [])
        covered = {(i.get("entry_id"), i.get("parameter")) for i in issues}
        added = 0
        for entry in catalog["entries"]:
            for parameter in entry["parameters"]:
                if parameter.get("state") != "conflict" or (entry["id"], parameter["name"]) in covered:
                    continue
                issues.append(issue_for(catalog, entry, parameter))
                covered.add((entry["id"], parameter["name"]))
                added += 1
        if added:
            save_catalog(catalog, wrapper, args.dry_run)
        counts[version] = added
    print(json.dumps({"issues_added": counts, "dry_run": args.dry_run}))


if __name__ == "__main__":
    main()
