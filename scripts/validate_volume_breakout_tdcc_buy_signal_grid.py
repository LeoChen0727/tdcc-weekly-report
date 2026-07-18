from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_tdcc_buy_signal_grid import (  # noqa: E402
    BEST_CSV,
    DETAIL_HISTORY_CSV,
    DOCS_LATEST_DIR,
    EVENT_COLUMNS,
    GRID_COLUMNS,
    GRID_CSV,
    GRID_MD,
    MAX_TDCC_SIGNAL_AGE_DAYS,
    MODEL_ID,
    OVERLAY_MODEL_ID,
    PROPOSAL_MD,
    REGISTRY_CSV,
    RESEARCH_ID,
    SIGNAL_UNIVERSE_ID,
)
from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract  # noqa: E402


REQUIRED_FEATURE_SCOPES = {
    "tdcc_only",
    "tdcc_event_filter",
    "tdcc_price_position",
    "tdcc_attack_method",
    "tdcc_volume_ratio",
    "tdcc_consolidation",
    "tdcc_attack_position",
}

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def check_exists(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md" and len(path.read_text(encoding="utf-8", errors="replace").splitlines()) < 10:
        fail(f"{path} is suspiciously short")


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def validate_mirror(path: Path) -> None:
    mirror = DOCS_LATEST_DIR / path.name
    check_exists(mirror)
    if path.read_bytes() != mirror.read_bytes():
        fail(f"docs/latest mirror differs for {path.name}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def truthy(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "1.0", "yes", "y", "t"})


def numeric_required(df: pd.DataFrame, column: str) -> pd.Series:
    values = pd.to_numeric(df[column], errors="coerce")
    if values.isna().any():
        fail(f"{column} contains non-numeric values")
    return values


def validate_events(events: pd.DataFrame) -> None:
    if events.empty:
        fail(f"{DETAIL_HISTORY_CSV} has no rows")
    missing = sorted(set(EVENT_COLUMNS) - set(events.columns))
    if missing:
        fail(f"{DETAIL_HISTORY_CSV} missing columns: {missing}")
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"event artifact must not emit production decision fields: {forbidden}")

    if set(events["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"unexpected event model_id values: {sorted(set(events['model_id']))}")
    if set(events["overlay_model_id"].astype(str)) != {OVERLAY_MODEL_ID}:
        fail("event overlay_model_id mismatch")
    if set(events["research_id"].astype(str)) != {RESEARCH_ID}:
        fail("event research_id mismatch")
    if set(events["signal_universe_id"].astype(str)) != {SIGNAL_UNIVERSE_ID}:
        fail("event signal_universe_id mismatch")
    if set(events["event_filter_id"].astype(str)) != {"current_model_hit_all"}:
        fail("events must use current_model_hit_all as the unique signal universe")
    if set(events["model_hit_status"].astype(str)) != {"current_model_hit"}:
        fail("events must only contain current_model_hit rows")
    if not false_only(events["approved_for_daily"]):
        fail("events approved_for_daily must remain false")

    list_types = set(events["tdcc_list_type"].astype(str))
    if "no_tdcc" not in list_types:
        fail("events must include no_tdcc baseline rows")
    if not ({"weekly_increase", "consecutive_accumulation"} & list_types):
        fail("events must include at least one TDCC as-of list type")

    key_cols = ["event_date", "stock_id", "pattern_id", "tdcc_list_type"]
    dupes = events.duplicated(key_cols).sum()
    if dupes:
        fail(f"events contain duplicated event/pattern/tdcc_list rows: {dupes}")

    dates = pd.to_datetime(events["event_date"], format="%Y%m%d", errors="coerce")
    if dates.isna().any():
        fail("event_date has invalid values")
    span_days = int((dates.max() - dates.min()).days)
    if span_days < 250:
        fail(f"event date span is too short for one-year research: {span_days} days")

    tdcc_events = events[events["tdcc_list_type"].astype(str).ne("no_tdcc")].copy()
    if tdcc_events.empty:
        fail("TDCC as-of matched events are empty")
    signal_dates = pd.to_datetime(tdcc_events["tdcc_signal_date"], format="%Y%m%d", errors="coerce")
    event_dates = pd.to_datetime(tdcc_events["event_date"], format="%Y%m%d", errors="coerce")
    if signal_dates.isna().any():
        fail("TDCC events must have valid tdcc_signal_date")
    if (signal_dates > event_dates).any():
        fail("TDCC grid contains future leak: tdcc_signal_date > event_date")
    ages = numeric_required(tdcc_events, "tdcc_signal_age_days")
    if (ages < 0).any() or (ages > MAX_TDCC_SIGNAL_AGE_DAYS).any():
        fail(f"tdcc_signal_age_days must be between 0 and {MAX_TDCC_SIGNAL_AGE_DAYS}")
    ranks = numeric_required(tdcc_events, "tdcc_rank")
    if (ranks < 1).any() or (ranks > 50).any():
        fail("tdcc_rank must be numeric between 1 and 50")


def validate_grid(grid: pd.DataFrame, best: pd.DataFrame, registry: pd.DataFrame) -> None:
    if grid.empty:
        fail(f"{GRID_CSV} has no rows")
    missing = sorted(set(GRID_COLUMNS) - set(grid.columns))
    if missing:
        fail(f"{GRID_CSV} missing columns: {missing}")
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"grid artifact must not emit production decision fields: {forbidden}")
    if set(grid["model_id"].astype(str)) != {MODEL_ID}:
        fail("grid model_id mismatch")
    if set(grid["overlay_model_id"].astype(str)) != {OVERLAY_MODEL_ID}:
        fail("grid overlay_model_id mismatch")
    if set(grid["research_id"].astype(str)) != {RESEARCH_ID}:
        fail("grid research_id mismatch")
    if set(grid["signal_universe_id"].astype(str)) != {SIGNAL_UNIVERSE_ID}:
        fail("grid signal_universe_id mismatch")
    if not false_only(grid["approved_for_daily"]):
        fail("TDCC buy-signal grid must not approve production directly")

    list_types = set(grid["tdcc_list_type"].astype(str))
    if "no_tdcc" not in list_types:
        fail("grid must include no_tdcc baseline rows")
    if not ({"weekly_increase", "consecutive_accumulation"} & list_types):
        fail("grid must include TDCC list-type rows")

    missing_scopes = sorted(REQUIRED_FEATURE_SCOPES - set(grid["tdcc_feature_scope"].astype(str)))
    if missing_scopes:
        fail(f"grid missing required TDCC feature scopes: {missing_scopes}")

    sample = numeric_required(grid, "sample_size")
    if (sample <= 0).any():
        fail("sample_size must be positive")
    for col in ["win_rate", "avg_return", "median_return", "research_score"]:
        numeric_required(grid, col)

    candidates = grid[truthy(grid["approved_for_daily_candidate"])]
    if candidates.empty:
        fail("expected at least one approved_for_daily_candidate research row")
    if set(candidates["candidate_status"]) != {"promotion_candidate"}:
        fail("approved_for_daily_candidate rows must be promotion_candidate only")
    if set(candidates["out_of_sample_pass"].astype(str).str.lower()) != {"true"}:
        fail("promotion candidates must pass out-of-sample check")

    if best.empty:
        fail(f"{BEST_CSV} has no rows")
    key_cols = ["tdcc_list_type", "rank_bucket", "tdcc_feature_scope", "tdcc_feature_id", "pattern_id"]
    best_keys = set(map(tuple, best[key_cols].astype(str).to_numpy()))
    grid_keys = set(map(tuple, grid[key_cols].astype(str).to_numpy()))
    if not best_keys.issubset(grid_keys):
        fail("best candidates must be a subset of grid rows")
    if not false_only(best["approved_for_daily"]):
        fail("best candidates approved_for_daily must remain false")
    approved_best = best[truthy(best["approved_for_daily_candidate"])]
    if not approved_best.empty and set(approved_best["candidate_status"]) != {"promotion_candidate"}:
        fail("approved_for_daily_candidate best rows must be promotion_candidate only")
    tdcc_watch = best[best["tdcc_list_type"].astype(str).ne("no_tdcc")]
    if tdcc_watch.empty:
        fail("best candidates should include TDCC watch rows for review")
    if len(registry) != len(grid):
        fail("evidence registry must mirror grid row count")


def main() -> int:
    for path in [DETAIL_HISTORY_CSV, GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        check_exists(path)
    for path in [GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        validate_mirror(path)

    events = read_csv(DETAIL_HISTORY_CSV)
    grid = read_csv(GRID_CSV)
    best = read_csv(BEST_CSV)
    registry = read_csv(REGISTRY_CSV)

    contract = load_research_tdcc_dataset_contract()
    for label, frame in [("events", events), ("grid", grid), ("best", best), ("registry", registry)]:
        values = sorted({value for value in frame.get("source_tdcc_dataset_id", pd.Series(dtype=str)).astype(str) if value})
        if values != [contract.dataset_id]:
            fail(f"{label} source_tdcc_dataset_id mismatch: expected {contract.dataset_id}, got {values}")

    validate_events(events)
    validate_grid(grid, best, registry)

    print(
        "volume breakout TDCC buy signal grid validation passed "
        f"event_rows={len(events)} grid_rows={len(grid)} best_rows={len(best)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
