from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_buy_signal_grid import (  # noqa: E402
    BEST_CSV,
    DETAIL_HISTORY_CSV,
    DOCS_LATEST_DIR,
    GRID_COLUMNS,
    GRID_CSV,
    GRID_MD,
    MIN_CANDIDATE_SAMPLE,
    MODEL_ID,
    PROPOSAL_MD,
    REGISTRY_CSV,
    RESEARCH_ID,
    SIGNAL_UNIVERSE_ID,
)


REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "event_date",
    "stock_id",
    "entry_date",
    "exit_date",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "out_of_sample",
    "source_signal_universe_id",
}

REQUIRED_FEATURE_SCOPES = {
    "all_current_model_hits",
    "event_filter",
    "price_position",
    "attack_method",
    "volume_ratio",
    "consolidation",
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


def check_exists(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md" and len(path.read_text(encoding="utf-8", errors="replace").splitlines()) < 8:
        fail(f"{path} is suspiciously short")


def truthy(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "1.0", "yes", "y", "t"})


def numeric(df: pd.DataFrame, column: str) -> pd.Series:
    out = pd.to_numeric(df[column], errors="coerce")
    if out.isna().any():
        fail(f"{column} contains non-numeric values")
    return out


def validate_mirror(path: Path) -> None:
    mirror = DOCS_LATEST_DIR / path.name
    check_exists(mirror)
    if path.read_bytes() != mirror.read_bytes():
        fail(f"docs/latest mirror differs for {path.name}")


def validate_detail(detail: pd.DataFrame) -> None:
    if detail.empty:
        fail(f"{DETAIL_HISTORY_CSV} has no rows")
    missing = sorted(REQUIRED_DETAIL_COLUMNS - set(detail.columns))
    if missing:
        fail(f"{DETAIL_HISTORY_CSV} missing columns: {missing}")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"detail artifact must not emit production decision fields: {forbidden}")
    if set(detail["model_id"]) != {MODEL_ID}:
        fail(f"unexpected detail model_id values: {sorted(set(detail['model_id']))}")
    if set(detail["model_hit_status"]) != {"current_model_hit"}:
        fail(f"detail must only contain current_model_hit rows: {sorted(set(detail['model_hit_status']))}")
    if set(detail["event_filter_id"]) != {"current_model_hit_all"}:
        fail("detail must use current_model_hit_all as the unique signal universe to avoid double-counting")
    if set(detail["source_signal_universe_id"]) != {SIGNAL_UNIVERSE_ID}:
        fail("detail source_signal_universe_id mismatch")
    dupes = detail.duplicated(["event_date", "stock_id", "pattern_id"]).sum()
    if dupes:
        fail(f"detail contains duplicated signal/pattern rows: {dupes}")
    dates = pd.to_datetime(detail["event_date"], format="%Y%m%d", errors="coerce")
    if dates.isna().any():
        fail("detail event_date has invalid values")
    span_days = int((dates.max() - dates.min()).days)
    if span_days < 250:
        fail(f"detail date span is too short for one-year research: {span_days} days")


def validate_grid(grid: pd.DataFrame, best: pd.DataFrame, registry: pd.DataFrame) -> None:
    if grid.empty:
        fail(f"{GRID_CSV} has no rows")
    missing = sorted(set(GRID_COLUMNS) - set(grid.columns))
    if missing:
        fail(f"{GRID_CSV} missing columns: {missing}")
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"grid artifact must not emit production decision fields: {forbidden}")
    if set(grid["model_id"]) != {MODEL_ID}:
        fail(f"unexpected grid model_id values: {sorted(set(grid['model_id']))}")
    if set(grid["research_id"]) != {RESEARCH_ID}:
        fail(f"unexpected research_id values: {sorted(set(grid['research_id']))}")
    if set(grid["signal_universe_id"]) != {SIGNAL_UNIVERSE_ID}:
        fail(f"unexpected signal_universe_id values: {sorted(set(grid['signal_universe_id']))}")
    if set(grid["approved_for_daily"].astype(str).str.lower()) != {"false"}:
        fail("buy-signal grid must not approve production directly")
    scopes = set(grid["feature_group_scope"])
    missing_scopes = sorted(REQUIRED_FEATURE_SCOPES - scopes)
    if missing_scopes:
        fail(f"grid missing required feature group scopes: {missing_scopes}")

    sample = numeric(grid, "sample_size")
    if (sample <= 0).any():
        fail("sample_size must be positive")
    numeric(grid, "win_rate")
    numeric(grid, "avg_return")
    numeric(grid, "median_return")
    numeric(grid, "research_score")

    candidates = grid[truthy(grid["approved_for_daily_candidate"])]
    if candidates.empty:
        fail("expected at least one approved_for_daily_candidate research row")
    if set(candidates["candidate_status"]) != {"promotion_candidate"}:
        fail("approved_for_daily_candidate rows must be promotion_candidate only")
    if (pd.to_numeric(candidates["sample_size"], errors="coerce") < MIN_CANDIDATE_SAMPLE).any():
        fail("promotion candidates below minimum sample size")
    if (pd.to_numeric(candidates["win_rate"], errors="coerce") < 50).any():
        fail("promotion candidates below 50% win rate")
    if (pd.to_numeric(candidates["avg_return"], errors="coerce") <= 0).any():
        fail("promotion candidates must have positive average return")
    if (pd.to_numeric(candidates["median_return"], errors="coerce") <= 0).any():
        fail("promotion candidates must have positive median return")
    if set(candidates["out_of_sample_pass"].astype(str).str.lower()) != {"true"}:
        fail("promotion candidates must pass out-of-sample check")

    if best.empty:
        fail(f"{BEST_CSV} has no rows")
    key_cols = ["feature_group_scope", "feature_group_id", "pattern_id"]
    best_keys = set(map(tuple, best[key_cols].astype(str).to_numpy()))
    grid_candidate_keys = set(map(tuple, candidates[key_cols].astype(str).to_numpy()))
    if not best_keys.issubset(grid_candidate_keys):
        fail("best candidates must be a subset of grid promotion candidates")
    if len(registry) != len(grid):
        fail("evidence registry must mirror grid row count")


def main() -> int:
    for path in [DETAIL_HISTORY_CSV, GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        check_exists(path)
    for path in [GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        validate_mirror(path)

    detail = read_csv(DETAIL_HISTORY_CSV)
    grid = read_csv(GRID_CSV)
    best = read_csv(BEST_CSV)
    registry = read_csv(REGISTRY_CSV)

    validate_detail(detail)
    validate_grid(grid, best, registry)

    print(
        "volume breakout buy signal grid validation passed "
        f"detail_rows={len(detail)} grid_rows={len(grid)} best_rows={len(best)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
