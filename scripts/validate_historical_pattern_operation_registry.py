from __future__ import annotations

from pathlib import Path

import pandas as pd


LATEST_DIR = Path("output/latest")
RESEARCH_HISTORY_DIR = Path("output/history/research")

REGISTRY_CSV = LATEST_DIR / "historical_pattern_operation_registry_latest.csv"
REGISTRY_MD = LATEST_DIR / "historical_pattern_operation_registry_latest.md"
DETAIL_HISTORY_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
REGISTRY_HISTORY_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_registry.csv"

REQUIRED_REGISTRY_COLUMNS = {
    "model_id",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "pattern_name_zh",
    "entry_rule_zh",
    "stop_loss_rule_zh",
    "hold_rule_zh",
    "exit_rule_zh",
    "sample_size",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_holding_days",
    "profit_factor",
    "best_for_market_regime",
    "risk_notes_zh",
    "confidence_status",
    "approved_for_daily",
    "out_of_sample_pass",
    "generated_at",
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "event_date",
    "stock_id",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_reason",
    "return_pct",
    "out_of_sample",
}

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def check_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md":
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.splitlines()) < 10:
            fail(f"{path} is suspiciously short")


def main() -> int:
    for path in [REGISTRY_CSV, REGISTRY_MD, DETAIL_HISTORY_CSV, REGISTRY_HISTORY_CSV]:
        check_file(path)

    registry = read_csv(REGISTRY_CSV)
    detail = read_csv(DETAIL_HISTORY_CSV)
    if registry.empty:
        fail(f"{REGISTRY_CSV} has no rows")
    if detail.empty:
        fail(f"{DETAIL_LATEST_CSV} has no rows")

    missing_registry = sorted(REQUIRED_REGISTRY_COLUMNS - set(registry.columns))
    if missing_registry:
        fail(f"{REGISTRY_CSV} missing columns: {missing_registry}")
    missing_detail = sorted(REQUIRED_DETAIL_COLUMNS - set(detail.columns))
    if missing_detail:
        fail(f"{DETAIL_HISTORY_CSV} missing columns: {missing_detail}")

    forbidden = sorted((set(registry.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"historical operation research must not emit production decision fields: {forbidden}")

    models = set(registry["model_id"])
    if models != {"volume_range_breakout"}:
        fail(f"unexpected model_id values: {sorted(models)}")

    statuses = set(registry["model_hit_status"])
    expected_status = {"current_model_hit", "research_relaxed_not_current_model"}
    bad_status = sorted(statuses - expected_status)
    if bad_status:
        fail(f"unexpected model_hit_status values: {bad_status}")

    approved = set(registry["approved_for_daily"].astype(str).str.lower())
    if approved - {"false"}:
        fail("research registry must not approve patterns for daily production directly")

    relaxed = registry[registry["model_hit_status"] == "research_relaxed_not_current_model"]
    if not relaxed.empty and set(relaxed["approved_for_daily"].astype(str).str.lower()) != {"false"}:
        fail("research-only relaxed rows must keep approved_for_daily=False")

    valid_confidence = {"low", "medium", "high"}
    bad_confidence = sorted(set(registry["confidence_status"]) - valid_confidence)
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")

    sample_size = pd.to_numeric(registry["sample_size"], errors="coerce")
    if sample_size.isna().any() or (sample_size <= 0).any():
        fail("sample_size must be positive for every registry row")

    print(
        "historical pattern operation registry validation passed "
        f"registry_rows={len(registry)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
