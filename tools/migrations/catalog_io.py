"""Small stdlib helpers for lossless catalog wrappers and ordered JSON updates."""
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]


def load_catalog(root, version):
    path = Path(root) / f"catalog-v{version}.js"
    raw = path.read_bytes().decode("utf-8")
    marker = f"window.PINE_CATALOG[{version}]="
    before, separator, after = raw.partition(marker)
    if not separator:
        raise ValueError(f"Unexpected catalog wrapper: {path}")
    whitespace = after[:len(after) - len(after.lstrip())]
    data, end = json.JSONDecoder().raw_decode(after.lstrip())
    suffix = after.lstrip()[end:]
    if suffix.strip() != ";":
        raise ValueError(f"Unexpected trailing catalog content: {path}")
    return data, (path, before + separator + whitespace, suffix, raw)


def save_catalog(data, wrapper, dry_run=False):
    path, prefix, suffix, previous = wrapper
    updated = prefix + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + suffix
    if updated == previous:
        return False
    if not dry_run:
        path.write_bytes(updated.encode("utf-8"))
    return True


def nonempty_text(text):
    return isinstance(text, dict) and any(str(text.get(k) or "").strip() for k in ("ru", "en", "original"))
