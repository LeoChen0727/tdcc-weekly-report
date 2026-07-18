from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tdcc_dataset_contract import (
    LATEST_MANIFEST_JSON,
    build_dataset_manifest,
    load_tdcc_dataset_manifest,
    versioned_manifest_path,
)


VOLATILE_FIELDS = {"generated_at", "producer"}


def stable_manifest(value: dict[str, Any]) -> dict[str, Any]:
    return {key: item for key, item in value.items() if key not in VOLATILE_FIELDS}


def validate() -> list[str]:
    errors: list[str] = []
    try:
        actual = load_tdcc_dataset_manifest(LATEST_MANIFEST_JSON)
    except Exception as exc:
        return [str(exc)]
    try:
        expected = build_dataset_manifest(
            generated_at=str(actual.get("generated_at", "")),
            producer={str(key): str(value) for key, value in dict(actual.get("producer", {})).items()},
        )
    except Exception as exc:
        return [str(exc)]

    if stable_manifest(actual) != stable_manifest(expected):
        errors.append("latest TDCC dataset manifest does not match canonical snapshot contents")
    versioned_path = versioned_manifest_path(actual["signal_date"])
    if not versioned_path.exists():
        errors.append(f"versioned TDCC dataset manifest is missing: {versioned_path.as_posix()}")
    else:
        try:
            versioned = json.loads(versioned_path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"cannot read versioned TDCC dataset manifest: {exc}")
        else:
            if versioned != actual:
                errors.append("latest and versioned TDCC dataset manifests are not byte-equivalent JSON values")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("TDCC dataset manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    manifest = load_tdcc_dataset_manifest()
    print(
        "TDCC dataset manifest validation passed: "
        f"dataset_id={manifest['dataset_id']} signal_date={manifest['signal_date']} "
        f"snapshots={manifest['snapshot_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
