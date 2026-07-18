from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tdcc_dataset_contract import build_dataset_manifest, write_dataset_manifest


def main() -> int:
    try:
        manifest = build_dataset_manifest()
        latest_path, versioned_path = write_dataset_manifest(manifest)
    except Exception as exc:
        print(f"TDCC_DATASET_MANIFEST_ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "TDCC dataset manifest built: "
        f"dataset_id={manifest['dataset_id']} signal_date={manifest['signal_date']} "
        f"snapshots={manifest['snapshot_count']}"
    )
    print(f"Saved: {latest_path.as_posix()}")
    print(f"Saved: {versioned_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
