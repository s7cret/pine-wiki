"""Shared stdlib invariants for the catalog/history JSON schema."""
import re


TEXT_ID = re.compile(r"[0-9a-f]{16}")
EMPTY_REMARKS = "e3b0c44298fc1c14"
ROLES = ("api", "construct", "part", "detail", "technical")
# These fields are literal identifiers, code, source metadata, or raw prose,
# never references to the localized text pool. In particular a future entry
# or family with a hex-looking ID must not create a false missing-text error.
LITERAL_FIELDS = frozenset({
    "id", "entry_id", "entry_ids", "parameter", "name", "key", "domain_key",
    "representative_id", "same_concept_ids", "anchor_ids", "parents",
    "original_family", "sha256", "snapshot_id", "source_record_ids", "clause_ids",
    "description_hashes", "url", "label", "artifact", "code", "template",
    "syntax", "signatures", "types", "return_types", "parameters", "requiredness",
    "values", "quote", "ru", "en", "original", "synonyms", "search_terms",
})


def text_references(document):
    """Yield (text ID, path) throughout the document, excluding its text pool.

    Outside documented literal fields, exact 16-character lowercase hex
    scalars are text references. Lookup does not depend on pool membership,
    so unknown hashes are reported as dangling links as well.
    Traverse all nested fields rather than an allowlist: supplements, previous
    descriptions, related notes, and default-contract evidence also hold links.
    Dictionary keys are identities, not references. Text-pool keys must never
    count as references to themselves.
    """
    def walk(value, path):
        if isinstance(value, dict):
            for key, child in value.items():
                if not path and key == "texts":
                    continue
                # Catalog parameters are objects containing description links;
                # history parameters are literal names. Only skip the latter.
                if key == "parameters" and isinstance(child, list) and all(isinstance(item, str) for item in child):
                    continue
                if key in LITERAL_FIELDS and key != "parameters":
                    continue
                yield from walk(child, path + (str(key),))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                yield from walk(child, path + (str(index),))
        elif isinstance(value, str) and TEXT_ID.fullmatch(value):
            yield value, ".".join(path)
    yield from walk(document, ())


def has_text(value):
    return isinstance(value, dict) and any(str(value.get(k) or "").strip() for k in ("ru", "en", "original"))


def text_pool_errors(document, label):
    pool = document["texts"]
    references = list(text_references(document))
    used = {ref for ref, _ in references}
    for ref, path in references:
        if ref not in pool:
            yield f"{label}: missing text {ref} ({path})"
    for ref in sorted(pool.keys() - used):
        yield f"{label}: orphan text {ref}"
    for ref, item in pool.items():
        # This schema's empty remarks sentinel is intentional; no other pooled
        # text may be empty, including records without an editorial basis.
        if ref != EMPTY_REMARKS and not has_text(item):
            yield f"{label}: empty text {ref}"


def catalog_aggregates(catalog):
    entries = catalog["entries"]
    role_keys = {role: {e["structure"]["key"] for e in entries if e["structure"]["role"] == role} for role in ROLES}
    structure = {role: len(keys) for role, keys in role_keys.items()}
    structure.update(records=len(entries),
                     original_records=sum(not e["structure"]["generated"] for e in entries),
                     added_records=sum(e["structure"]["generated"] for e in entries),
                     parameters=sum(len(e["parameters"]) for e in entries))
    counts = {"records": len(entries), "public_records": sum(not e["technical"] for e in entries),
              "technical_records": sum(e["technical"] for e in entries),
              "elements": len(role_keys["api"]) + len(role_keys["construct"]),
              "technical_elements": len(role_keys["technical"]),
              "categories": {category: {
                  "records": sum(e["category"] == category for e in entries),
                  "elements": len({e["structure"]["key"] for e in entries if e["category"] == category})
              } for category in {e["category"] for e in entries}}}
    return counts, structure


def family_version_aggregate(entries):
    """Combine all overloads; comparing each record to the union is incorrect."""
    parameters = [p for entry in entries for p in entry["parameters"]]
    names = {p["name"] for p in parameters}
    return {
        "parameters": sorted(names),
        "types": {name: sorted({t for p in parameters if p["name"] == name for t in p["types"]}) for name in names},
        "requiredness": {name: sorted({p.get("state", "unknown") for p in parameters if p["name"] == name}) for name in names},
        "return_types": sorted({t for entry in entries for t in entry["result"]["types"]})
    }


def normalized_history_aggregate(version):
    # Order in the stored arrays is presentational. Preserve duplicates when
    # sorting, so accidental duplicate aggregate values still fail validation.
    return {"parameters": sorted(version["parameters"]),
            "types": {name: sorted(values) for name, values in version["types"].items()},
            "requiredness": {name: sorted(values) for name, values in version["requiredness"].items()},
            "return_types": sorted(version["return_types"])}
