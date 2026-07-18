from __future__ import annotations

import argparse

from tdcc_stock_history_utils import normalize_code, write_tdcc_stock_history_files
from tdcc_weekly_data_readiness import ensure_weekly_data_ready, load_readiness, taipei_today


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build per-stock TDCC weekly history CSV files.")
    parser.add_argument(
        "--stock-id",
        action="append",
        default=None,
        help="Optional stock id to build. Can be repeated. Default: build every stock.",
    )
    parser.add_argument(
        "--use-existing-readiness",
        action="store_true",
        help="Use the readiness artifact created earlier in the same official weekly run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.use_existing_readiness:
        load_readiness()
    else:
        ensure_weekly_data_ready(as_of_date=taipei_today())
    limit = {normalize_code(x) for x in args.stock_id} if args.stock_id else None
    manifest = write_tdcc_stock_history_files(limit)
    print(f"Saved TDCC stock history files: {len(manifest)}")
    print("Saved manifest: output/latest/tdcc_stock_history_manifest.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
