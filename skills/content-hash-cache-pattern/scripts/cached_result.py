"""Cache completed JSON results by content and processing identity; no extraction."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile


def digest(path):
    sha = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            sha.update(chunk)
    return sha.hexdigest()


def cache_identity(source, *, extractor, version, options, schema):
    if not all(isinstance(x, str) and x.strip() for x in (extractor, version, schema)):
        raise ValueError("Extractor, version and schema must be nonempty strings")
    if not isinstance(options, dict):
        raise ValueError("Options must be a JSON object")
    identity = {"source_sha256": digest(source), "extractor": extractor,
                "version": version, "options": options, "schema": schema}
    # Snapshot options; caller mutation cannot silently change the key.
    return json.loads(json.dumps(identity, sort_keys=True, allow_nan=False))


def cache_path(cache_dir, identity):
    raw = json.dumps(identity, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return Path(cache_dir) / (hashlib.sha256(raw.encode()).hexdigest() + ".json")


def reject_constant(value):
    raise ValueError("Nonstandard JSON constant: " + value)


def load_cached(cache_dir, identity):
    try:
        entry = json.loads(cache_path(cache_dir, identity).read_text(encoding="utf-8"),
                           parse_constant=reject_constant)
        if (isinstance(entry, dict) and entry.get("identity") == identity
                and entry.get("status") == "completed" and entry.get("payload") is not None):
            return entry["payload"]
    except (FileNotFoundError, UnicodeError, ValueError):
        pass
    return None


def store_cached(cache_dir, identity, payload):
    if payload is None:
        raise ValueError("None is a cache miss, not a completed result")
    raw = json.dumps({"identity": identity, "status": "completed", "payload": payload},
                     ensure_ascii=False, allow_nan=False)
    destination = cache_path(cache_dir, identity)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=destination.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def self_check():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        source = root / "one.txt"
        source.write_bytes(b"same")
        params = dict(extractor="ocr", version="1", options={"lang": "en"}, schema="1")
        identity = cache_identity(source, **params)
        source.rename(root / "moved.txt")
        source = root / "moved.txt"
        assert cache_identity(source, **params) == identity
        for field, value in (("version", "2"), ("options", {"lang": "fr"}), ("schema", "2")):
            assert cache_identity(source, **(params | {field: value})) != identity
        params["options"]["lang"] = "changed"
        assert identity["options"]["lang"] == "en"
        source.write_bytes(b"different")
        assert cache_identity(source, **params) != identity
        cache = root / "cache"
        store_cached(cache, identity, {"pages": [{"text": "hello", "page": 1}]})
        original = cache_path(cache, identity).read_bytes()
        assert load_cached(cache, identity)["pages"][0]["text"] == "hello"
        try:
            store_cached(cache, identity, {"bad": float("nan")})
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid JSON accepted")
        assert cache_path(cache, identity).read_bytes() == original
        from unittest.mock import patch
        with patch("os.replace", side_effect=OSError("Injected replacement failure")):
            try:
                store_cached(cache, identity, "new result")
            except OSError:
                pass
            else:
                raise AssertionError("Replacement failure ignored")
        assert cache_path(cache, identity).read_bytes() == original
        assert list(cache.iterdir()) == [cache_path(cache, identity)]
        cache_path(cache, identity).write_text("broken", encoding="utf-8")
        assert load_cached(cache, identity) is None
        cache_path(cache, identity).write_text(json.dumps(
            {"identity": identity, "status": "completed", "payload": float("nan")}),
            encoding="utf-8")
        assert load_cached(cache, identity) is None
        store_cached(cache, identity, "valid")
        entry = json.loads(cache_path(cache, identity).read_text())
        entry["identity"]["version"] = "wrong"
        cache_path(cache, identity).write_text(json.dumps(entry), encoding="utf-8")
        assert load_cached(cache, identity) is None
    print("Cache identity, reuse, invalidation and preservation checks passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true", required=True)
    parser.parse_args()
    self_check()
