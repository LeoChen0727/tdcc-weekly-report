from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys

import pandas as pd


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/volume_breakout")

REQUIRED_FILES = [
    LATEST_DIR / "volume_breakout_watch_latest.csv",
    LATEST_DIR / "volume_breakout_watch_latest.md",
    LATEST_DIR / "volume_breakout_backtest_latest.csv",
    LATEST_DIR / "volume_breakout_backtest_latest.md",
    LATEST_DIR / "volume_breakout_chatgpt_packet_latest.md",
    HISTORY_DIR / "volume_breakout_event_log.csv",
]

LATEST_ONLY_REQUIRED_FILES = [
    LATEST_DIR / "volume_breakout_watch_latest.csv",
    LATEST_DIR / "volume_breakout_watch_latest.md",
    LATEST_DIR / "volume_breakout_chatgpt_packet_latest.md",
]

WATCH_REQUIRED_COLUMNS = [
    "signal_date",
    "advisory_score_as_of",
    "advisory_score_source_artifact",
    "advisory_score_source_sha256",
    "stock_id",
    "stock_name",
    "volume_breakout_type",
    "volume_watch_scope",
    "volume_breakout_priority",
    "selection_status",
    "risk_flags",
    "next_volume_breakout_confirmation",
    "advisory_volume_breakout_score",
    "advisory_volume_breakout_rank",
]

FORBIDDEN_WATCH_COLUMNS = {
    "call_warrant_count",
    "put_warrant_count",
    "score",
    "rank",
    "volume_breakout_score",
    "volume_breakout_rank",
}

BACKTEST_REQUIRED_COLUMNS = [
    "group_name",
    "group_value",
    "sample_count",
    "mature_d5_count",
    "avg_return_d5",
    "win_rate_d5",
    "sample_status",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def line_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(text.splitlines())


def check_multiline_markdown(path: Path) -> None:
    if line_count(path) <= 5:
        fail(f"{path} is suspiciously short or single-line")


def check_csv(path: Path, required_columns: list[str], allow_empty: bool = False) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        fail(f"{path} missing columns: {missing}")
    if not allow_empty and df.empty:
        fail(f"{path} has no rows")
    return df


def forbidden_watch_columns(columns: list[str]) -> list[str]:
    return sorted(
        column
        for column in columns
        if column.startswith("warrant_") or column in FORBIDDEN_WATCH_COLUMNS
    )


def advisory_as_of_matches_signal_date(watch: pd.DataFrame) -> bool:
    if watch.empty:
        return True
    if not {"signal_date", "advisory_score_as_of"} <= set(watch.columns):
        return False
    signal_dates = watch["signal_date"].astype(str).str.strip()
    advisory_as_of = watch["advisory_score_as_of"].astype(str).str.strip()
    return bool((advisory_as_of != "").all() and advisory_as_of.equals(signal_dates))


def canonical_text_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()


def advisory_source_lineage_errors(
    watch: pd.DataFrame, root: Path = Path(".")
) -> list[str]:
    errors: list[str] = []
    required = {
        "stock_id",
        "advisory_score_source_artifact",
        "advisory_score_source_sha256",
    }
    if not required <= set(watch.columns):
        return ["volume breakout watch advisory source lineage columns are missing"]
    for row_number, row in enumerate(watch.to_dict("records"), start=2):
        artifact_text = str(row.get("advisory_score_source_artifact", "")).strip()
        expected_sha = str(row.get("advisory_score_source_sha256", "")).strip()
        if not artifact_text:
            errors.append(f"row={row_number} advisory score source artifact is blank")
            continue
        artifact = Path(artifact_text)
        if not artifact.is_absolute():
            artifact = root / artifact
        if not artifact.is_file():
            errors.append(
                f"row={row_number} advisory score source artifact is missing: {artifact_text}"
            )
            continue
        actual_sha = canonical_text_sha256(artifact)
        if expected_sha != actual_sha:
            errors.append(
                "row="
                f"{row_number} advisory score source SHA mismatch: "
                f"stock_id={row.get('stock_id', '')} expected={expected_sha} actual={actual_sha}"
            )
    return errors


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate volume breakout watch and optional backtest outputs.")
    parser.add_argument(
        "--latest-only",
        action="store_true",
        help="Validate only latest daily watch outputs. Backtest files are checked only if present.",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    required_files = LATEST_ONLY_REQUIRED_FILES if args.latest_only else REQUIRED_FILES

    for path in required_files:
        if not path.exists():
            fail(f"missing required file: {path}")
        if path.suffix.lower() == ".md":
            check_multiline_markdown(path)

    watch = check_csv(LATEST_DIR / "volume_breakout_watch_latest.csv", WATCH_REQUIRED_COLUMNS, allow_empty=True)
    forbidden_lineage_columns = forbidden_watch_columns(watch.columns.tolist())
    if forbidden_lineage_columns:
        fail(
            "volume breakout watch must not mirror warrant or generic candidate "
            f"score/rank lineage fields: {forbidden_lineage_columns}"
        )
    if not watch.empty:
        if not advisory_as_of_matches_signal_date(watch):
            fail(
                "volume breakout watch advisory_score_as_of must be nonblank and "
                "equal signal_date for every row"
            )
        source_lineage_errors = advisory_source_lineage_errors(watch)
        if source_lineage_errors:
            fail(source_lineage_errors[0])
    backtest = pd.DataFrame()
    events = pd.DataFrame()
    should_check_backtest = not args.latest_only or (
        (LATEST_DIR / "volume_breakout_backtest_latest.csv").exists()
        and (HISTORY_DIR / "volume_breakout_event_log.csv").exists()
    )
    if should_check_backtest:
        backtest = check_csv(LATEST_DIR / "volume_breakout_backtest_latest.csv", BACKTEST_REQUIRED_COLUMNS, allow_empty=False)
        events = check_csv(HISTORY_DIR / "volume_breakout_event_log.csv", ["event_date", "stock_id", "volume_breakout_type", "mature_d5"], allow_empty=False)

    if not watch.empty:
        valid_priorities = {"A_bottom_volume_attack", "B_bottom_volume_attack_with_risk"}
        bad = sorted(set(watch["volume_breakout_priority"]) - valid_priorities)
        if bad:
            fail(f"invalid volume_breakout_priority values: {bad}")
        bad_types = sorted(set(watch["volume_breakout_type"]) - {"bottom_volume_attack"})
        if bad_types:
            fail(f"invalid volume_breakout_type values: {bad_types}")
        bad_status = sorted(set(watch["selection_status"]) - {"selected"})
        if bad_status:
            fail(f"invalid selection_status values: {bad_status}")

    if not backtest.empty and "sample_status" in backtest.columns:
        bad_status = sorted(set(backtest["sample_status"]) - {"ok", "insufficient_sample", "pending_only", "data_missing", ""})
        if bad_status:
            fail(f"invalid sample_status values: {bad_status}")

    print(f"Volume breakout validation passed: watch_rows={len(watch)}, backtest_rows={len(backtest)}, event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
