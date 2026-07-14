from __future__ import annotations

import math
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_operation_lag_bucket_audit"
ARTIFACT_VERSION = "operation_lag_bucket_v1_20260714"
SOURCE_OPERATION_ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
SOURCE_OPERATION_ARTIFACT_VERSION = "rearmed_operation_grid_v1_20260713"
SOURCE_CONDITION_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_CONDITION_ARTIFACT_VERSION = "source_first_condition_v2_20260714"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
GRID_ID = (
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|"
    "d30|none_no_stop_reference"
)
PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "excluding_unresolved_anomaly_candidates_sensitivity"
DISCOVERY_HORIZON_DAYS = 126

PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"
SOURCE_OPERATION_DETAIL_CSV = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv"
)
SOURCE_CONDITION_DETAIL_CSV = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv"
)

LATEST_BUCKETS = {
    "latest_lag_d0_20": (0, 20),
    "latest_lag_d21_40": (21, 40),
    "latest_lag_d41_60": (41, 60),
    "latest_lag_d61_90": (61, 90),
    "latest_lag_d91_126": (91, 126),
}
FIRST_BUCKETS = {
    "first_lag_d0_20": (0, 20),
    "first_lag_d21_40": (21, 40),
    "first_lag_d41_60": (41, 60),
    "first_lag_d61_90": (61, 90),
    "first_lag_d91_126": (91, 126),
    "first_lag_d127_plus": (127, None),
}
LATEST_WATCH_BUCKETS = {
    "latest_watch_d0_60": (0, 60),
    "latest_watch_d61_126": (61, 126),
}


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _same_number(observed: object, expected: float | None, tolerance: float = 0.00011) -> bool:
    value = _number(observed)
    if expected is None:
        return value is None
    return value is not None and math.isclose(value, expected, abs_tol=tolerance)


def _rate(count: int, total: int) -> float | None:
    return count / total * 100.0 if total else None


def _stat(series: pd.Series, kind: str) -> float | None:
    values = pd.to_numeric(series, errors="coerce").dropna()
    if values.empty:
        return None
    if kind == "mean":
        return float(values.mean())
    if kind == "median":
        return float(values.median())
    if kind == "p10":
        return float(values.quantile(0.10))
    if kind == "p90":
        return float(values.quantile(0.90))
    raise ValueError(kind)


def _bucket(value: int, buckets: dict[str, tuple[int, int | None]]) -> str:
    for bucket_id, (lower, upper) in buckets.items():
        if value >= lower and (upper is None or value <= upper):
            return bucket_id
    return ""


def _price_indices(stock_id: str, cache: dict[str, dict[str, int]]) -> dict[str, int]:
    if stock_id in cache:
        return cache[stock_id]
    path = PRICE_HISTORY_DIR / f"{stock_id}.csv"
    if not path.is_file():
        return {}
    dates = pd.read_csv(path, usecols=["date"], dtype={"date": str}, keep_default_na=False)[
        "date"
    ]
    dates = dates.astype(str).str.replace(r"\D", "", regex=True).str[:8]
    dates = dates.loc[dates.str.fullmatch(r"\d{8}")].drop_duplicates().sort_values(
        kind="mergesort"
    )
    cache[stock_id] = {date: index for index, date in enumerate(dates.tolist())}
    return cache[stock_id]


def _overlap_pair_count(detail: pd.DataFrame) -> int:
    overlaps = 0
    for _stock_id, stock in detail.groupby("stock_id", sort=False):
        previous_exit = ""
        for row in stock.sort_values("entry_date", kind="mergesort").itertuples(index=False):
            if previous_exit and str(row.entry_date) <= previous_exit:
                overlaps += 1
            previous_exit = max(previous_exit, str(row.exit_date))
    return overlaps


def _governance(frame: pd.DataFrame, name: str, errors: list[str]) -> None:
    expected = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_operation_artifact_id": SOURCE_OPERATION_ARTIFACT_ID,
        "source_operation_artifact_version": SOURCE_OPERATION_ARTIFACT_VERSION,
        "source_condition_artifact_id": SOURCE_CONDITION_ARTIFACT_ID,
        "source_condition_artifact_version": SOURCE_CONDITION_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "grid_id": GRID_ID,
    }
    for column, value in expected.items():
        if set(frame[column].astype(str)) != {value}:
            errors.append(f"operation lag bucket {name} governance drift: {column}")
    if _boolish(frame["approved_for_daily"]).any():
        errors.append(f"operation lag bucket {name} must remain research-only")
    if _boolish(frame["production_change"]).any():
        errors.append(f"operation lag bucket {name} must not change production")


def _validate_detail_lineage(
    detail: pd.DataFrame,
    operations: pd.DataFrame,
    episodes: pd.DataFrame,
    errors: list[str],
) -> None:
    operation_keys = set(
        zip(
            operations["episode_key"].astype(str),
            operations["stock_id"].astype(str),
            operations["trigger_date"].astype(str),
            operations["entry_date"].astype(str),
        )
    )
    detail_keys = set(
        zip(
            detail["episode_key"].astype(str),
            detail["stock_id"].astype(str),
            detail["trigger_date"].astype(str),
            detail["entry_date"].astype(str),
        )
    )
    if operation_keys != detail_keys:
        errors.append("operation lag bucket detail does not exactly cover the adopted source grid")
    episode_lookup = episodes.set_index("episode_key", drop=False)
    date_cache: dict[str, dict[str, int]] = {}
    for row in detail.itertuples(index=False):
        if row.episode_key not in episode_lookup.index:
            errors.append(f"operation lag bucket source episode is missing: {row.episode_key}")
            continue
        source = episode_lookup.loc[row.episode_key]
        periods = str(source["qualifying_revenue_periods"]).split("|")
        source_dates = str(source["qualifying_source_dates"]).split("|")
        trade_dates = str(source["qualifying_trade_dates"]).split("|")
        try:
            sequence_indices = [
                int(value) for value in str(source["qualifying_sequence_indices"]).split("|")
            ]
        except ValueError:
            errors.append(f"operation lag bucket source sequence is invalid: {row.episode_key}")
            continue
        if not (
            periods == str(row.qualifying_revenue_periods).split("|")
            and source_dates == str(row.qualifying_source_dates).split("|")
            and trade_dates == str(row.qualifying_trade_dates).split("|")
            and sequence_indices
            == [int(value) for value in str(row.qualifying_sequence_indices).split("|")]
        ):
            errors.append(f"operation lag bucket copied lineage drift: {row.episode_key}")
            continue
        indices = _price_indices(str(row.stock_id), date_cache)
        trigger_index = indices.get(str(row.trigger_date))
        if trigger_index is None:
            errors.append(
                f"operation lag bucket trigger date is absent from price history: "
                f"{row.stock_id}/{row.trigger_date}"
            )
            continue
        asof_positions = [
            position
            for position, (trade_date, sequence_index) in enumerate(
                zip(trade_dates, sequence_indices)
            )
            if trade_date <= str(row.trigger_date) and sequence_index <= trigger_index
        ]
        if not asof_positions:
            errors.append(f"operation lag bucket has no as-of source: {row.episode_key}")
            continue
        position = asof_positions[-1]
        latest_lag = trigger_index - sequence_indices[position]
        first_lag = trigger_index - sequence_indices[0]
        expected_future = len(periods) - position - 1
        checks = (
            (str(row.episode_first_qualifying_revenue_period), periods[0], "first period"),
            (str(row.episode_first_qualifying_source_date), source_dates[0], "first source date"),
            (str(row.episode_first_qualifying_trade_date), trade_dates[0], "first trade date"),
            (str(row.asof_latest_qualifying_revenue_period), periods[position], "as-of period"),
            (str(row.asof_latest_qualifying_source_date), source_dates[position], "as-of source date"),
            (str(row.asof_latest_qualifying_trade_date), trade_dates[position], "as-of trade date"),
            (
                str(row.final_episode_latest_qualifying_trade_date),
                trade_dates[-1],
                "final episode trade date",
            ),
            (str(row.latest_source_lag_bucket), _bucket(latest_lag, LATEST_BUCKETS), "latest bucket"),
            (
                str(row.latest_watch_segment),
                _bucket(latest_lag, LATEST_WATCH_BUCKETS),
                "latest watch segment",
            ),
            (str(row.first_source_lag_bucket), _bucket(first_lag, FIRST_BUCKETS), "first bucket"),
        )
        for observed, expected, label in checks:
            if observed != expected:
                errors.append(f"operation lag bucket {label} drift: {row.episode_key}")
        if int(row.latest_source_to_trigger_trading_days) != latest_lag:
            errors.append(f"operation lag bucket latest lag drift: {row.episode_key}")
        if int(row.first_source_to_trigger_trading_days) != first_lag:
            errors.append(f"operation lag bucket first lag drift: {row.episode_key}")
        if int(row.future_qualifying_update_ignored_count) != expected_future:
            errors.append(f"operation lag bucket future-update count drift: {row.episode_key}")
        if _bool_value(row.final_episode_latest_after_trigger_flag) != (expected_future > 0):
            errors.append(f"operation lag bucket future-update flag drift: {row.episode_key}")
        if not _bool_value(row.time_travel_guard_passed):
            errors.append(f"operation lag bucket time-travel guard is false: {row.episode_key}")
        if trade_dates[position] > str(row.trigger_date):
            errors.append(f"operation lag bucket consumed a future revenue update: {row.episode_key}")
        if latest_lag < 0 or latest_lag > DISCOVERY_HORIZON_DAYS:
            errors.append(f"operation lag bucket latest lag exceeds active horizon: {row.episode_key}")


def _validate_summary(summary: pd.DataFrame, detail: pd.DataFrame, errors: list[str]) -> None:
    expected_keys: set[tuple[str, str, str]] = set()
    for analysis_basis in (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS):
        expected_keys.add((analysis_basis, "latest_qualifying_source_asof_trigger", "all"))
        expected_keys.update(
            (analysis_basis, "latest_qualifying_source_asof_trigger", bucket)
            for bucket in LATEST_BUCKETS
        )
        expected_keys.add((analysis_basis, "episode_first_qualifying_source", "all"))
        expected_keys.update(
            (analysis_basis, "episode_first_qualifying_source", bucket)
            for bucket in FIRST_BUCKETS
        )
        expected_keys.add(
            (
                analysis_basis,
                "latest_qualifying_source_watch_horizon_comparison",
                "all",
            )
        )
        expected_keys.update(
            (
                analysis_basis,
                "latest_qualifying_source_watch_horizon_comparison",
                bucket,
            )
            for bucket in LATEST_WATCH_BUCKETS
        )
    observed_keys = set(
        zip(
            summary["analysis_basis"].astype(str),
            summary["lag_basis_id"].astype(str),
            summary["lag_bucket_id"].astype(str),
        )
    )
    if observed_keys != expected_keys or summary.duplicated(
        ["analysis_basis", "lag_basis_id", "lag_bucket_id"]
    ).any():
        errors.append("operation lag bucket summary coverage drift")
        return
    analysis_parts = {
        PRIMARY_ANALYSIS_BASIS: detail,
        SENSITIVITY_ANALYSIS_BASIS: detail.loc[
            ~_boolish(detail["source_anomaly_candidate_flag"])
            & ~_boolish(detail["operation_return_review_candidate_flag"])
        ],
    }
    overlap_count = _overlap_pair_count(detail)
    for row in summary.itertuples(index=False):
        overall = analysis_parts[str(row.analysis_basis)]
        if row.lag_bucket_id == "all":
            part = overall
        elif row.lag_basis_id == "latest_qualifying_source_asof_trigger":
            part = overall.loc[
                overall["latest_source_lag_bucket"].astype(str).eq(str(row.lag_bucket_id))
            ]
        elif row.lag_basis_id == "latest_qualifying_source_watch_horizon_comparison":
            part = overall.loc[
                overall["latest_watch_segment"].astype(str).eq(str(row.lag_bucket_id))
            ]
        else:
            part = overall.loc[
                overall["first_source_lag_bucket"].astype(str).eq(str(row.lag_bucket_id))
            ]
        outcomes = part["return_outcome"].astype(str)
        wins = int(outcomes.eq("win").sum())
        neutral = int(outcomes.eq("neutral").sum())
        failures = int(outcomes.eq("failure").sum())
        total = len(part)
        overall_wins = int(overall["return_outcome"].astype(str).eq("win").sum())
        expected = {
            "operation_count": total,
            "unique_stock_count": part["stock_id"].nunique(),
            "win_count": wins,
            "neutral_count": neutral,
            "failure_count": failures,
            "source_anomaly_candidate_count": int(
                _boolish(part["source_anomaly_candidate_flag"]).sum()
            ),
            "operation_return_review_candidate_count": int(
                _boolish(part["operation_return_review_candidate_flag"]).sum()
            ),
            "future_qualifying_update_ignored_operation_count": int(
                pd.to_numeric(
                    part["future_qualifying_update_ignored_count"], errors="coerce"
                ).gt(0).sum()
            ),
        }
        for column, value in expected.items():
            if int(getattr(row, column)) != int(value):
                errors.append(
                    f"operation lag bucket summary count drift: "
                    f"{row.analysis_basis}/{row.lag_bucket_id}/{column}"
                )
        numerical = {
            "win_rate_pct": _rate(wins, total),
            "neutral_rate_pct": _rate(neutral, total),
            "failure_rate_pct": _rate(failures, total),
            "avg_return_pct": _stat(part["realized_return_pct"], "mean"),
            "median_return_pct": _stat(part["realized_return_pct"], "median"),
            "p10_return_pct": _stat(part["realized_return_pct"], "p10"),
            "p90_return_pct": _stat(part["realized_return_pct"], "p90"),
            "return_ge20_rate_pct": _rate(
                int(_boolish(part["realized_return_ge20"]).sum()), total
            ),
            "delta_vs_overall_win_rate_pct_points": (
                (_rate(wins, total) or 0.0) - (_rate(overall_wins, len(overall)) or 0.0)
                if total
                else None
            ),
            "delta_vs_overall_avg_return_pct_points": (
                (_stat(part["realized_return_pct"], "mean") or 0.0)
                - (_stat(overall["realized_return_pct"], "mean") or 0.0)
                if total
                else None
            ),
        }
        for column, value in numerical.items():
            if not _same_number(getattr(row, column), value):
                errors.append(
                    f"operation lag bucket summary metric drift: "
                    f"{row.analysis_basis}/{row.lag_bucket_id}/{column}"
                )
        if int(row.same_stock_overlap_pair_count) != overlap_count:
            errors.append("operation lag bucket summary overlap count drift")
        if int(row.unclassified_operation_count) != 0:
            errors.append("operation lag bucket summary reports unclassified operations")
    for analysis_basis, overall in analysis_parts.items():
        for lag_basis_id, buckets in (
            ("latest_qualifying_source_asof_trigger", LATEST_BUCKETS),
            ("episode_first_qualifying_source", FIRST_BUCKETS),
            (
                "latest_qualifying_source_watch_horizon_comparison",
                LATEST_WATCH_BUCKETS,
            ),
        ):
            rows = summary.loc[
                summary["analysis_basis"].eq(analysis_basis)
                & summary["lag_basis_id"].eq(lag_basis_id)
                & summary["lag_bucket_id"].isin(buckets)
            ]
            if int(pd.to_numeric(rows["operation_count"], errors="coerce").sum()) != len(
                overall
            ):
                errors.append(
                    f"operation lag bucket partition does not conserve rows: "
                    f"{analysis_basis}/{lag_basis_id}"
                )


def validate() -> list[str]:
    errors: list[str] = []
    paths = (
        LATEST_CSV,
        DETAIL_CSV,
        LATEST_MD,
        HISTORY_CSV,
        DOCS_CSV,
        DOCS_MD,
        SOURCE_OPERATION_DETAIL_CSV,
        SOURCE_CONDITION_DETAIL_CSV,
    )
    for path in paths:
        if not path.is_file():
            errors.append(f"operation lag bucket artifact is missing: {path}")
    if errors:
        return errors
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "trigger_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "exit_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    operations = pd.read_csv(
        SOURCE_OPERATION_DETAIL_CSV,
        dtype={"stock_id": str, "trigger_date": str, "entry_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    operations = operations.loc[
        operations["grid_id"].astype(str).eq(GRID_ID) & _boolish(operations["return_valid"])
    ].copy()
    episodes = pd.read_csv(
        SOURCE_CONDITION_DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    episodes = episodes.loc[
        episodes["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    _governance(summary, "summary", errors)
    _governance(detail, "detail", errors)
    if detail.duplicated(["episode_key", "stock_id", "trigger_date", "entry_date"]).any():
        errors.append("operation lag bucket detail contains duplicate operations")
    if not _boolish(detail["same_stock_non_overlap_applied"]).all():
        errors.append("operation lag bucket non-overlap flag is not universal")
    if _overlap_pair_count(detail) != 0:
        errors.append("operation lag bucket contains overlapping same-stock operations")
    if not pd.to_numeric(
        detail["future_qualifying_update_ignored_count"], errors="coerce"
    ).gt(0).any():
        errors.append("operation lag bucket no longer exercises the future-update regression guard")
    _validate_detail_lineage(detail, operations, episodes, errors)
    _validate_summary(summary, detail, errors)
    if LATEST_CSV.read_bytes() != HISTORY_CSV.read_bytes() or LATEST_CSV.read_bytes() != DOCS_CSV.read_bytes():
        errors.append("operation lag bucket summary mirrors drift")
    if LATEST_MD.read_bytes() != DOCS_MD.read_bytes():
        errors.append("operation lag bucket markdown mirror drift")
    markdown = LATEST_MD.read_text(encoding="utf-8")
    for token in (
        "營收轉強後發動時間差績效稽核",
        "逐筆只採用 trigger 當日以前已知的最後一筆合格營收",
        "0-20、21-40、41-60、61-90、91-126",
        "127 日以上桶",
        "60 個交易日列為下一輪 research-only 觀察期限候選",
        "61 至 126 日待查交易",
        "Primary 保留所有待查數字",
        "EPS、毛利率、營益率、營業利益、業外、淨利與年報欄位未納入",
    ):
        if token not in markdown:
            errors.append(f"operation lag bucket markdown omits required explanation: {token}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue_unreacted_range operation lag bucket audit validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
