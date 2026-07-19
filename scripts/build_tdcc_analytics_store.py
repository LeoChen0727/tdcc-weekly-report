from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tdcc_analytics_store import DEFAULT_OUTPUT_DIR, build_analytics_store
from tdcc_dataset_contract import LATEST_MANIFEST_JSON


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the derived TDCC Parquet and DuckDB analytics store."
    )
    parser.add_argument("--source-manifest", type=Path, default=LATEST_MANIFEST_JSON)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = build_analytics_store(
            source_manifest_path=args.source_manifest,
            output_dir=args.output_dir,
        )
    except Exception as exc:
        print(f"TDCC_ANALYTICS_BUILD_ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "TDCC analytics store built: "
        f"dataset_id={manifest['source_tdcc_dataset_id']} "
        f"signal_date={manifest['signal_date']} "
        f"snapshots={manifest['history_snapshot_count']} rows={manifest['row_count']}"
    )
    for artifact in manifest["artifacts"].values():
        print(f"Saved: {artifact['path']}")
    print(f"Saved: {(args.output_dir / 'tdcc_analytics_manifest_latest.json').as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
