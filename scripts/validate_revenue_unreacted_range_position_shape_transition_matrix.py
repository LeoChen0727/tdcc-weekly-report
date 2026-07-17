from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_position_shape_transition_matrix"
ARTIFACT_VERSION = "position_shape_transition_matrix_v1_20260717"
SOURCE_OPERATION_LAG_ARTIFACT_ID = (
    "revenue_unreacted_range_operation_lag_bucket_audit"
)
SOURCE_OPERATION_LAG_ARTIFACT_VERSION = "operation_lag_bucket_v1_20260714"
SOURCE_REARMED_ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
SOURCE_REARMED_ARTIFACT_VERSION = "rearmed_operation_grid_v1_20260713"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
ADOPTED_GRID_ID = (
    "rearm_after_realized_exit_next_trade_day|"
    "delayed_next_close_continuation_bonus|d30|none_no_stop_reference"
)
PRICE_HISTORY_CUTOFF_DATE = "20260713"

# These hashes bind the business rows after deterministic normalization and exclude
# mutable generated_at timestamps. They are intentionally duplicated here so this
# validator does not import the producer it independently verifies.
PINNED_OPERATION_LAG_SEMANTIC_SHA256 = (
    "04e627169d6a2198d2f523bc52067e93a36d7d73f81155214cd38e2ea5e35600"
)
PINNED_REARMED_SEMANTIC_SHA256 = (
    "e7b20554d93dbe71abc3dd683691bc710e1f941b73a83ae12fd48057423eb643"
)

PINNED_OPERATION_COUNT = 955
PINNED_UNIQUE_STOCK_COUNT = 602
PINNED_WIN_COUNT = 535
PINNED_NEUTRAL_COUNT = 7
PINNED_FAILURE_COUNT = 413
PINNED_AVG_RETURN_PCT = 9.1232
PINNED_MEDIAN_RETURN_PCT = 2.0
PINNED_P10_RETURN_PCT = -14.8248
PINNED_P90_RETURN_PCT = 45.3562
PINNED_RETURN_GE20_COUNT = 201
PINNED_SOURCE_ANOMALY_COUNT = 90
PINNED_OPERATION_RETURN_REVIEW_COUNT = 25
PINNED_UNRESOLVED_PRICE_PATH_COUNT = 1
PINNED_SENSITIVITY_COUNT = 841

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = (
    "excluding_unresolved_anomaly_candidates_sensitivity"
)
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)

ANCHORS = (
    (
        10,
        "revenue_available",
        "asof_latest_qualifying_trade_date",
        "latest qualifying monthly-revenue availability mapped to its first trading date",
    ),
    (
        20,
        "pre_breakout_week_close",
        "derived_trigger_index_minus_5",
        "close five trading sessions before the adopted trigger",
    ),
    (
        30,
        "formal_confirmation_close",
        "confirmation_date",
        "formal delayed next-close continuation confirmation",
    ),
)
ANCHOR_IDS = tuple(row[1] for row in ANCHORS)
PINNED_ANCHOR_COVERAGE = {
    "revenue_available": 462,
    "pre_breakout_week_close": 513,
    "formal_confirmation_close": 551,
}
POSITION_BUCKETS = ("low_pos_le40", "mid_pos_40_75", "high_pos_gt75")
SHAPE_BUCKETS = ("consolidation", "rising", "falling", "mixed_or_turn")
CELL_IDS = tuple(
    f"{position}__{shape}"
    for position in POSITION_BUCKETS
    for shape in SHAPE_BUCKETS
) + ("insufficient_history",)

FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
POSITION_POLICY = (
    "anchor adjusted close positioned within the adjusted analysis-high/analysis-low "
    "range of exactly 120 prior trading sessions, excluding the anchor"
)
SHAPE_POLICY = (
    "revenue-model-owned descriptive shape: adjusted close return from t-20 to anchor; "
    "adjusted-close range across the 23 sessions ending at anchor; EMA23 through anchor "
    "with five-session slope"
)

OPERATION_KEY_COLUMNS = (
    "episode_key",
    "stock_id",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
)
OPERATION_LAG_CANONICAL_COLUMNS = (
    "model_id",
    "artifact_id",
    "artifact_version",
    "source_variant_id",
    "grid_id",
    "episode_key",
    "stock_id",
    "asof_latest_qualifying_source_date",
    "asof_latest_qualifying_trade_date",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "latest_source_to_trigger_trading_days",
    "first_source_to_trigger_trading_days",
    "realized_return_pct",
    "return_outcome",
    "realized_return_ge20",
    "source_anomaly_candidate_flag",
    "operation_return_review_candidate_flag",
    "time_travel_guard_passed",
    "same_stock_non_overlap_applied",
)
REARMED_CANONICAL_COLUMNS = (
    "artifact_id",
    "artifact_version",
    "grid_id",
    "episode_key",
    "stock_id",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "return_valid",
    "realized_return_pct",
    "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "operation_return_review_candidate_flag",
)
CANONICAL_DATE_COLUMNS = {
    "asof_latest_qualifying_source_date",
    "asof_latest_qualifying_trade_date",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
}
CANONICAL_INTEGER_COLUMNS = {
    "latest_source_to_trigger_trading_days",
    "first_source_to_trigger_trading_days",
}
CANONICAL_FLOAT_COLUMNS = {"realized_return_pct"}
CANONICAL_BOOL_COLUMNS = {
    "realized_return_ge20",
    "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "operation_return_review_candidate_flag",
    "time_travel_guard_passed",
    "same_stock_non_overlap_applied",
    "return_valid",
}

SOURCE_RELATIVE_PATHS = {
    "operation_lag": (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv"
    ),
    "rearmed": (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv"
    ),
    "price_dir": "data/stock_price_history",
    "resolution": "config/revenue_unreacted_range_price_comparability_resolution.csv",
}
ARTIFACT_RELATIVE_PATHS = {
    "summary": (
        "output/latest/research_backtest/"
        f"{ARTIFACT_ID}_latest.csv"
    ),
    "detail": (
        "output/latest/research_backtest/"
        f"{ARTIFACT_ID}_detail_latest.csv"
    ),
    "transition": (
        "output/latest/research_backtest/"
        f"{ARTIFACT_ID}_transition_latest.csv"
    ),
    "markdown": (
        "output/latest/research_backtest/"
        f"{ARTIFACT_ID}_latest.md"
    ),
    "summary_history": f"output/history/research/{ARTIFACT_ID}.csv",
    "transition_history": f"output/history/research/{ARTIFACT_ID}_transition.csv",
    "summary_docs": f"docs/latest/{ARTIFACT_ID}_latest.csv",
    "transition_docs": f"docs/latest/{ARTIFACT_ID}_transition_latest.csv",
    "markdown_docs": f"docs/latest/{ARTIFACT_ID}_latest.md",
}


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    return text[:-2] if text.endswith(".0") and text[:-2].isdigit() else text


def _date_text(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _same_number(
    observed: object,
    expected: float | int | str | None,
    *,
    tolerance: float = 0.00011,
) -> bool:
    observed_number = _number(observed)
    expected_number = _number(expected)
    if expected_number is None:
        return observed_number is None
    return observed_number is not None and math.isclose(
        observed_number, expected_number, abs_tol=tolerance
    )


def _rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator * 100.0 if denominator else None


def _stat(values: pd.Series, kind: str) -> float | None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return None
    if kind == "mean":
        return float(numeric.mean())
    if kind == "median":
        return float(numeric.median())
    if kind == "p10":
        return float(numeric.quantile(0.10))
    if kind == "p90":
        return float(numeric.quantile(0.90))
    if kind == "min":
        return float(numeric.min())
    if kind == "max":
        return float(numeric.max())
    raise ValueError(kind)


def _top_abs_share(values: pd.Series, count: int) -> float | None:
    numeric = pd.to_numeric(values, errors="coerce").dropna().abs()
    denominator = float(numeric.sum())
    if numeric.empty or denominator <= 0:
        return None
    return float(numeric.nlargest(count).sum()) / denominator * 100.0


def _sha256(path: Path) -> str:
    """Hash canonical CSV text bytes without checkout-specific EOL drift."""

    payload = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(payload).hexdigest()


def _canonical_semantic_sha256(
    frame: pd.DataFrame,
    columns: tuple[str, ...],
    *,
    filter_rearmed_grid: bool,
) -> str:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical source is missing columns: {missing}")
    canonical = frame.loc[:, columns].copy()
    if filter_rearmed_grid:
        canonical = canonical.loc[
            canonical["grid_id"].astype(str).eq(ADOPTED_GRID_ID)
            & _boolish(canonical["return_valid"])
        ].copy()
    else:
        canonical = canonical.loc[
            canonical["grid_id"].astype(str).eq(ADOPTED_GRID_ID)
        ].copy()
    if canonical.empty:
        raise RuntimeError("canonical source is empty")
    canonical["stock_id"] = canonical["stock_id"].map(_stock_id)
    for column in columns:
        if column in CANONICAL_DATE_COLUMNS:
            canonical[column] = canonical[column].map(_date_text)
        elif column in CANONICAL_INTEGER_COLUMNS:
            numeric = pd.to_numeric(canonical[column], errors="coerce")
            if numeric.isna().any() or not np.isclose(numeric, numeric.round()).all():
                raise RuntimeError(f"canonical integer column is invalid: {column}")
            canonical[column] = numeric.round().astype("int64").astype(str)
        elif column in CANONICAL_FLOAT_COLUMNS:
            numeric = pd.to_numeric(canonical[column], errors="coerce")
            if numeric.isna().any():
                raise RuntimeError(f"canonical float column is invalid: {column}")
            canonical[column] = numeric.map(lambda value: f"{float(value):.8f}")
        elif column in CANONICAL_BOOL_COLUMNS:
            canonical[column] = canonical[column].map(
                lambda value: "true" if _bool_value(value) else "false"
            )
        else:
            canonical[column] = canonical[column].astype(str).str.strip()
    canonical = canonical.sort_values(
        [
            "stock_id",
            "entry_date",
            "episode_key",
            "trigger_date",
            "confirmation_date",
            "exit_date",
        ],
        kind="mergesort",
    ).reset_index(drop=True)
    payload = canonical.to_csv(index=False, lineterminator="\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _overlap_pair_count(frame: pd.DataFrame) -> int:
    count = 0
    for _stock, rows in frame.groupby("stock_id", sort=False):
        prior_exit = ""
        for row in rows.sort_values("entry_date", kind="mergesort").itertuples(
            index=False
        ):
            if prior_exit and str(row.entry_date) <= prior_exit:
                count += 1
            prior_exit = max(prior_exit, str(row.exit_date))
    return count


def _read_source_frames(
    source_root: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, str, str, str, str]:
    lag_path = source_root / SOURCE_RELATIVE_PATHS["operation_lag"]
    rearmed_path = source_root / SOURCE_RELATIVE_PATHS["rearmed"]
    if not lag_path.is_file():
        raise RuntimeError(f"operation-lag source is missing: {lag_path}")
    if not rearmed_path.is_file():
        raise RuntimeError(f"rearmed source is missing: {rearmed_path}")
    lag = pd.read_csv(
        lag_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    rearmed = pd.read_csv(
        rearmed_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    lag_file_sha = _sha256(lag_path)
    rearmed_file_sha = _sha256(rearmed_path)
    lag_semantic_sha = _canonical_semantic_sha256(
        lag, OPERATION_LAG_CANONICAL_COLUMNS, filter_rearmed_grid=False
    )
    rearmed_semantic_sha = _canonical_semantic_sha256(
        rearmed, REARMED_CANONICAL_COLUMNS, filter_rearmed_grid=True
    )
    return (
        lag,
        rearmed,
        lag_file_sha,
        rearmed_file_sha,
        lag_semantic_sha,
        rearmed_semantic_sha,
    )


def _prepare_source(lag: pd.DataFrame, rearmed: pd.DataFrame) -> pd.DataFrame:
    required_lag = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "source_variant_id",
        "grid_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "asof_latest_qualifying_source_date",
        "asof_latest_qualifying_trade_date",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "latest_source_to_trigger_trading_days",
        "first_source_to_trigger_trading_days",
        "realized_return_pct",
        "return_outcome",
        "realized_return_ge20",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
        "time_travel_guard_passed",
        "same_stock_non_overlap_applied",
    }
    missing = sorted(required_lag - set(lag.columns))
    if missing:
        raise RuntimeError(f"operation-lag source is missing columns: {missing}")
    source = lag.loc[lag["grid_id"].astype(str).eq(ADOPTED_GRID_ID)].copy()
    source["stock_id"] = source["stock_id"].map(_stock_id)
    for column in CANONICAL_DATE_COLUMNS:
        source[column] = source[column].map(_date_text)
        if source[column].eq("").any():
            raise RuntimeError(f"operation-lag source has invalid {column}")
    governance = {
        "model_id": MODEL_ID,
        "artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
        "artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "grid_id": ADOPTED_GRID_ID,
    }
    for column, expected in governance.items():
        if set(source[column].astype(str)) != {expected}:
            raise RuntimeError(f"operation-lag source governance drift: {column}")
    if source.duplicated(list(OPERATION_KEY_COLUMNS)).any():
        raise RuntimeError("operation-lag source contains duplicate operations")
    if not _boolish(source["time_travel_guard_passed"]).all():
        raise RuntimeError("operation-lag time-travel guard failed")
    if not _boolish(source["same_stock_non_overlap_applied"]).all():
        raise RuntimeError("operation-lag non-overlap flag failed")
    source["realized_return_pct"] = pd.to_numeric(
        source["realized_return_pct"], errors="coerce"
    )
    if source["realized_return_pct"].isna().any():
        raise RuntimeError("operation-lag source has invalid return")
    expected_outcome = np.where(
        source["realized_return_pct"].gt(0),
        "win",
        np.where(source["realized_return_pct"].lt(0), "failure", "neutral"),
    )
    if not source["return_outcome"].astype(str).eq(expected_outcome).all():
        raise RuntimeError("operation-lag return outcome drift")
    if not _boolish(source["realized_return_ge20"]).eq(
        source["realized_return_pct"].ge(20)
    ).all():
        raise RuntimeError("operation-lag return >=20 flag drift")
    source["source_anomaly_candidate_flag"] = _boolish(
        source["source_anomaly_candidate_flag"]
    )
    source["operation_return_review_candidate_flag"] = _boolish(
        source["operation_return_review_candidate_flag"]
    )
    source["operation_key"] = source.loc[:, OPERATION_KEY_COLUMNS].astype(str).agg(
        "|".join, axis=1
    )
    if source["operation_key"].duplicated().any():
        raise RuntimeError("operation key is not unique")
    if _overlap_pair_count(source):
        raise RuntimeError("operation-lag source contains same-stock overlap")

    required_rearmed = {
        "artifact_id",
        "artifact_version",
        "grid_id",
        "return_valid",
        "realized_return_pct",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "operation_return_review_candidate_flag",
        *OPERATION_KEY_COLUMNS,
    }
    missing = sorted(required_rearmed - set(rearmed.columns))
    if missing:
        raise RuntimeError(f"rearmed source is missing columns: {missing}")
    lineage = rearmed.loc[
        rearmed["grid_id"].astype(str).eq(ADOPTED_GRID_ID)
        & _boolish(rearmed["return_valid"])
    ].copy()
    if set(lineage["artifact_id"].astype(str)) != {SOURCE_REARMED_ARTIFACT_ID}:
        raise RuntimeError("rearmed artifact id drift")
    if set(lineage["artifact_version"].astype(str)) != {
        SOURCE_REARMED_ARTIFACT_VERSION
    }:
        raise RuntimeError("rearmed artifact version drift")
    lineage["stock_id"] = lineage["stock_id"].map(_stock_id)
    for column in ("trigger_date", "confirmation_date", "entry_date", "exit_date"):
        lineage[column] = lineage[column].map(_date_text)
    if lineage.duplicated(list(OPERATION_KEY_COLUMNS)).any():
        raise RuntimeError("rearmed source contains duplicate mature operations")
    compare = [
        *OPERATION_KEY_COLUMNS,
        "realized_return_pct",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
    ]
    joined = source.loc[:, compare].merge(
        lineage.loc[:, compare],
        on=list(OPERATION_KEY_COLUMNS),
        how="outer",
        suffixes=("_lag", "_rearmed"),
        indicator=True,
        validate="one_to_one",
    )
    if not joined["_merge"].eq("both").all():
        raise RuntimeError("operation-lag and rearmed keys differ")
    if (
        pd.to_numeric(joined["realized_return_pct_lag"], errors="coerce")
        - pd.to_numeric(joined["realized_return_pct_rearmed"], errors="coerce")
    ).abs().gt(0.0001).any():
        raise RuntimeError("operation-lag and rearmed returns differ")
    for column in (
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
    ):
        if not _boolish(joined[f"{column}_lag"]).eq(
            _boolish(joined[f"{column}_rearmed"])
        ).all():
            raise RuntimeError(f"operation-lag and rearmed {column} differ")
    unresolved = lineage.loc[
        :, [*OPERATION_KEY_COLUMNS, "unresolved_price_path_candidate_flag"]
    ].copy()
    unresolved["unresolved_price_path_candidate_flag"] = _boolish(
        unresolved["unresolved_price_path_candidate_flag"]
    )
    source = source.merge(
        unresolved,
        on=list(OPERATION_KEY_COLUMNS),
        how="left",
        validate="one_to_one",
    )
    if source["unresolved_price_path_candidate_flag"].isna().any():
        raise RuntimeError("unresolved price-path lineage is incomplete")
    source["unresolved_price_path_candidate_flag"] = source[
        "unresolved_price_path_candidate_flag"
    ].astype(bool)
    source["combined_exclusion_candidate_flag"] = (
        source["source_anomaly_candidate_flag"]
        | source["operation_return_review_candidate_flag"]
        | source["unresolved_price_path_candidate_flag"]
    )
    source["sensitivity_included"] = ~source[
        "combined_exclusion_candidate_flag"
    ]
    return source.sort_values(["stock_id", "entry_date"], kind="mergesort").reset_index(
        drop=True
    )


def _validate_pinned_source(
    source: pd.DataFrame,
    lag_semantic_sha: str,
    rearmed_semantic_sha: str,
    errors: list[str],
) -> None:
    if lag_semantic_sha != PINNED_OPERATION_LAG_SEMANTIC_SHA256:
        errors.append(
            "operation-lag semantic SHA drift: "
            f"{lag_semantic_sha}/{PINNED_OPERATION_LAG_SEMANTIC_SHA256}"
        )
    if rearmed_semantic_sha != PINNED_REARMED_SEMANTIC_SHA256:
        errors.append(
            "rearmed semantic SHA drift: "
            f"{rearmed_semantic_sha}/{PINNED_REARMED_SEMANTIC_SHA256}"
        )
    outcomes = source["return_outcome"].astype(str)
    checks = {
        "operation_count": (len(source), PINNED_OPERATION_COUNT),
        "unique_stock_count": (source["stock_id"].nunique(), PINNED_UNIQUE_STOCK_COUNT),
        "win_count": (int(outcomes.eq("win").sum()), PINNED_WIN_COUNT),
        "neutral_count": (int(outcomes.eq("neutral").sum()), PINNED_NEUTRAL_COUNT),
        "failure_count": (int(outcomes.eq("failure").sum()), PINNED_FAILURE_COUNT),
        "return_ge20_count": (
            int(source["realized_return_pct"].ge(20).sum()),
            PINNED_RETURN_GE20_COUNT,
        ),
        "source_anomaly_candidate_count": (
            int(source["source_anomaly_candidate_flag"].sum()),
            PINNED_SOURCE_ANOMALY_COUNT,
        ),
        "operation_return_review_candidate_count": (
            int(source["operation_return_review_candidate_flag"].sum()),
            PINNED_OPERATION_RETURN_REVIEW_COUNT,
        ),
        "unresolved_price_path_candidate_count": (
            int(source["unresolved_price_path_candidate_flag"].sum()),
            PINNED_UNRESOLVED_PRICE_PATH_COUNT,
        ),
        "sensitivity_operation_count": (
            int(source["sensitivity_included"].sum()),
            PINNED_SENSITIVITY_COUNT,
        ),
    }
    for label, (actual, expected) in checks.items():
        if actual != expected:
            errors.append(f"pinned source {label} drift: {actual}/{expected}")
    numerical = {
        "average": (source["realized_return_pct"].mean(), PINNED_AVG_RETURN_PCT),
        "median": (source["realized_return_pct"].median(), PINNED_MEDIAN_RETURN_PCT),
        "p10": (source["realized_return_pct"].quantile(0.10), PINNED_P10_RETURN_PCT),
        "p90": (source["realized_return_pct"].quantile(0.90), PINNED_P90_RETURN_PCT),
    }
    for label, (actual, expected) in numerical.items():
        if not math.isclose(float(actual), expected, abs_tol=0.00011):
            errors.append(f"pinned source {label} drift: {actual}/{expected}")


def _load_resolutions(path: Path) -> pd.DataFrame:
    if not path.is_file():
        return pd.DataFrame(
            columns=["stock_id", "resume_date", "exchange_ratio", "resolution_id"]
        )
    frame = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
    required = {
        "stock_id",
        "resume_date",
        "exchange_ratio",
        "resolution_id",
        "root_cause_status",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"price resolution is missing columns: {missing}")
    frame = frame.loc[
        frame["root_cause_status"].astype(str).eq(
            "verified_non_comparable_raw_price_scale"
        )
    ].copy()
    frame["stock_id"] = frame["stock_id"].map(_stock_id)
    frame["resume_date"] = frame["resume_date"].map(_date_text)
    frame["exchange_ratio"] = pd.to_numeric(
        frame["exchange_ratio"], errors="coerce"
    )
    if frame["exchange_ratio"].isna().any() or frame["exchange_ratio"].le(0).any():
        raise RuntimeError("price resolution exchange ratio is invalid")
    return frame


def _load_adjusted_price(
    stock_id: str,
    price_dir: Path,
    resolutions: pd.DataFrame,
) -> pd.DataFrame:
    path = price_dir / f"{stock_id}.csv"
    if not path.is_file():
        raise RuntimeError(f"price history is missing: {path}")
    frame = pd.read_csv(path, low_memory=False)
    required = {"date", "open", "high", "low", "close"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"price history {stock_id} is missing columns: {missing}")
    frame["date"] = frame["date"].map(_date_text)
    frame = frame.loc[
        frame["date"].str.fullmatch(r"\d{8}")
        & frame["date"].le(PRICE_HISTORY_CUTOFF_DATE)
    ].copy()
    frame = frame.sort_values("date", kind="mergesort").drop_duplicates(
        "date", keep="last"
    )
    for column in ("open", "high", "low", "close"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["close"]).reset_index(drop=True)
    frame["adjustment_factor"] = 1.0
    for event in resolutions.loc[resolutions["stock_id"].eq(stock_id)].itertuples(
        index=False
    ):
        frame.loc[
            frame["date"].lt(str(event.resume_date)), "adjustment_factor"
        ] *= 1.0 / float(event.exchange_ratio)
    for column in ("open", "high", "low", "close"):
        frame[f"analysis_{column}"] = frame[column] * frame["adjustment_factor"]
    frame["analysis_ema23"] = frame["analysis_close"].ewm(
        span=23, adjust=False, min_periods=23
    ).mean()
    frame["sequence_index"] = np.arange(len(frame), dtype=int)
    if frame.empty or frame["date"].duplicated().any():
        raise RuntimeError(f"adjusted price history is empty or duplicated: {stock_id}")
    return frame


def _position_bucket(value: float) -> str:
    if value <= 40:
        return "low_pos_le40"
    if value <= 75:
        return "mid_pos_40_75"
    return "high_pos_gt75"


def _anchor_features(price: pd.DataFrame, index: int) -> dict[str, object]:
    close = _number(price.at[index, "analysis_close"])
    close_value = float(close) if close is not None else math.nan
    prior = price.iloc[max(0, index - 120) : index]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    position_observed = bool(
        len(prior) == 120
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close_value)
    )
    high = float(prior_high.max()) if position_observed else math.nan
    low = float(prior_low.min()) if position_observed else math.nan
    position_observed = bool(
        position_observed
        and np.isfinite(high)
        and np.isfinite(low)
        and high > low
    )
    position = (
        (close_value - low) / (high - low) * 100.0
        if position_observed
        else math.nan
    )
    position_bucket = (
        _position_bucket(position) if position_observed else "insufficient_history"
    )

    return20 = math.nan
    range23 = math.nan
    ema_slope5 = math.nan
    if index >= 20:
        close20 = _number(price.at[index - 20, "analysis_close"])
        if close20 is not None and close20 > 0 and np.isfinite(close_value):
            return20 = (close_value / close20 - 1.0) * 100.0
    recent = pd.to_numeric(
        price.iloc[max(0, index - 22) : index + 1]["analysis_close"],
        errors="coerce",
    )
    if len(recent) == 23 and recent.notna().all() and float(recent.min()) > 0:
        range23 = (float(recent.max()) / float(recent.min()) - 1.0) * 100.0
    if index >= 5:
        ema_now = _number(price.at[index, "analysis_ema23"])
        ema_prior = _number(price.at[index - 5, "analysis_ema23"])
        if ema_now is not None and ema_prior is not None and ema_prior > 0:
            ema_slope5 = (ema_now / ema_prior - 1.0) * 100.0
    shape_observed = bool(
        np.isfinite(return20) and np.isfinite(range23) and np.isfinite(ema_slope5)
    )
    if not shape_observed:
        shape_bucket = "insufficient_history"
    elif return20 > 5 and ema_slope5 > 0:
        shape_bucket = "rising"
    elif return20 < -5 and ema_slope5 < 0:
        shape_bucket = "falling"
    elif abs(return20) <= 5 and range23 <= 15:
        shape_bucket = "consolidation"
    else:
        shape_bucket = "mixed_or_turn"
    classification_observed = position_observed and shape_observed
    cell_id = (
        f"{position_bucket}__{shape_bucket}"
        if classification_observed
        else "insufficient_history"
    )
    return {
        "anchor_adjusted_close": close_value,
        "position_prior_session_count": len(prior),
        "position_window_start_date": str(prior["date"].iloc[0]) if len(prior) else "",
        "position_window_end_date": str(prior["date"].iloc[-1]) if len(prior) else "",
        "position_prior_adjusted_high": high,
        "position_prior_adjusted_low": low,
        "position_120d_pct": position,
        "position_observed": position_observed,
        "position_bucket": position_bucket,
        "shape_return20_pct": return20,
        "shape_range23_pct": range23,
        "shape_ema23_slope5_pct": ema_slope5,
        "shape_observed": shape_observed,
        "shape_bucket": shape_bucket,
        "classification_observed": classification_observed,
        "position_shape_cell_id": cell_id,
    }


def _expected_detail(
    source: pd.DataFrame,
    source_root: Path,
) -> pd.DataFrame:
    price_dir = source_root / SOURCE_RELATIVE_PATHS["price_dir"]
    resolutions = _load_resolutions(source_root / SOURCE_RELATIVE_PATHS["resolution"])
    anchor_meta = {
        anchor_id: (order, date_rule, definition)
        for order, anchor_id, date_rule, definition in ANCHORS
    }
    rows: list[dict[str, object]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    for operation in source.itertuples(index=False):
        stock_id = str(operation.stock_id)
        if stock_id not in price_cache:
            price_cache[stock_id] = _load_adjusted_price(
                stock_id, price_dir, resolutions
            )
        price = price_cache[stock_id]
        date_index = {
            str(date): int(index) for index, date in price["date"].items()
        }
        named_dates = {
            "revenue": str(operation.asof_latest_qualifying_trade_date),
            "trigger": str(operation.trigger_date),
            "confirmation": str(operation.confirmation_date),
            "entry": str(operation.entry_date),
            "exit": str(operation.exit_date),
        }
        missing = [name for name, date in named_dates.items() if date not in date_index]
        if missing:
            raise RuntimeError(
                f"anchor dates are absent from price history: {operation.operation_key}/{missing}"
            )
        revenue_index = date_index[named_dates["revenue"]]
        trigger_index = date_index[named_dates["trigger"]]
        confirmation_index = date_index[named_dates["confirmation"]]
        entry_index = date_index[named_dates["entry"]]
        exit_index = date_index[named_dates["exit"]]
        preweek_index = trigger_index - 5
        if preweek_index < 0:
            raise RuntimeError(f"trigger lacks five prior sessions: {operation.operation_key}")
        if revenue_index > trigger_index:
            raise RuntimeError(f"revenue anchor is after trigger: {operation.operation_key}")
        if confirmation_index != trigger_index + 1:
            raise RuntimeError(f"confirmation offset drift: {operation.operation_key}")
        if entry_index != confirmation_index + 1:
            raise RuntimeError(f"entry offset drift: {operation.operation_key}")
        if exit_index < entry_index:
            raise RuntimeError(f"exit precedes entry: {operation.operation_key}")
        if str(operation.asof_latest_qualifying_source_date) > named_dates["revenue"]:
            raise RuntimeError(
                f"source date is after mapped revenue date: {operation.operation_key}"
            )
        source_before_preweek = revenue_index <= preweek_index
        chronology_id = (
            "source_before_or_on_preweek"
            if source_before_preweek
            else "latest_source_arrived_after_preweek_before_or_on_trigger"
        )
        semantics = (
            "chronological_source_to_preweek_to_confirmation"
            if source_before_preweek
            else "labeled_anchor_comparison_not_chronological_latest_source_after_preweek"
        )
        anchor_indices = {
            "revenue_available": revenue_index,
            "pre_breakout_week_close": preweek_index,
            "formal_confirmation_close": confirmation_index,
        }
        for anchor_id, anchor_index in anchor_indices.items():
            order, rule, definition = anchor_meta[anchor_id]
            features = _anchor_features(price, anchor_index)
            rows.append(
                {
                    "operation_key": str(operation.operation_key),
                    "episode_key": str(operation.episode_key),
                    "stock_id": stock_id,
                    "stock_name": str(operation.stock_name),
                    "asof_latest_qualifying_source_date": str(
                        operation.asof_latest_qualifying_source_date
                    ),
                    "asof_latest_qualifying_trade_date": str(
                        operation.asof_latest_qualifying_trade_date
                    ),
                    "trigger_date": str(operation.trigger_date),
                    "confirmation_date": str(operation.confirmation_date),
                    "entry_date": str(operation.entry_date),
                    "exit_date": str(operation.exit_date),
                    "latest_source_to_trigger_trading_days": int(
                        operation.latest_source_to_trigger_trading_days
                    ),
                    "first_source_to_trigger_trading_days": int(
                        operation.first_source_to_trigger_trading_days
                    ),
                    "realized_return_pct": float(operation.realized_return_pct),
                    "return_outcome": str(operation.return_outcome),
                    "realized_return_ge20": float(operation.realized_return_pct) >= 20,
                    "source_anomaly_candidate_flag": bool(
                        operation.source_anomaly_candidate_flag
                    ),
                    "operation_return_review_candidate_flag": bool(
                        operation.operation_return_review_candidate_flag
                    ),
                    "unresolved_price_path_candidate_flag": bool(
                        operation.unresolved_price_path_candidate_flag
                    ),
                    "combined_exclusion_candidate_flag": bool(
                        operation.combined_exclusion_candidate_flag
                    ),
                    "primary_included": True,
                    "sensitivity_included": bool(operation.sensitivity_included),
                    "anchor_order": order,
                    "anchor_id": anchor_id,
                    "anchor_date_rule": rule,
                    "anchor_definition": definition,
                    "anchor_date": str(price.at[anchor_index, "date"]),
                    "anchor_sequence_index": anchor_index,
                    "preweek_date": str(price.at[preweek_index, "date"]),
                    "source_to_preweek_trading_days": preweek_index - revenue_index,
                    "preweek_to_trigger_trading_days": trigger_index - preweek_index,
                    "trigger_to_confirmation_trading_days": (
                        confirmation_index - trigger_index
                    ),
                    "confirmation_to_entry_trading_days": entry_index - confirmation_index,
                    "source_before_or_on_preweek_flag": source_before_preweek,
                    "anchor_chronology_id": chronology_id,
                    "comparison_sequence_semantics": semantics,
                    **features,
                }
            )
    return pd.DataFrame(rows).sort_values(
        ["stock_id", "entry_date", "anchor_order"], kind="mergesort"
    ).reset_index(drop=True)


def _governance_errors(
    frame: pd.DataFrame,
    name: str,
    expected_lineage: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    expected = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_operation_lag_artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
        "source_operation_lag_artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "grid_id": ADOPTED_GRID_ID,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        "price_basis": "adjusted_analysis_ohlc_only",
        **expected_lineage,
    }
    for column, value in expected.items():
        if column not in frame:
            errors.append(f"{name} is missing governance column: {column}")
        elif set(frame[column].astype(str)) != {value}:
            errors.append(f"{name} governance drift: {column}")
    for column in (
        "approved_for_daily",
        "formal_model_use_allowed",
        "production_change",
        "presentation_allowed",
    ):
        if column not in frame:
            errors.append(f"{name} is missing formal-use flag: {column}")
        elif _boolish(frame[column]).any():
            errors.append(f"{name} must keep {column}=False")
    if "promotion_readiness" not in frame or set(
        frame["promotion_readiness"].astype(str)
    ) != {"research_only_not_promotion_evidence"}:
        errors.append(f"{name} promotion readiness drift")
    return errors


def _compare_detail(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    lineage: dict[str, str],
) -> list[str]:
    errors = _governance_errors(actual, "detail", lineage)
    required = set(expected.columns)
    missing = sorted(required - set(actual.columns))
    if missing:
        errors.append(f"detail is missing independently recomputed columns: {missing}")
        return errors
    if len(actual) != PINNED_OPERATION_COUNT * len(ANCHORS):
        errors.append(
            f"detail row count drift: {len(actual)}/{PINNED_OPERATION_COUNT * len(ANCHORS)}"
        )
    if actual.duplicated(["operation_key", "anchor_id"]).any():
        errors.append("detail contains duplicate operation anchors")
    left = actual.copy()
    left["stock_id"] = left["stock_id"].map(_stock_id)
    keys = ["operation_key", "anchor_id"]
    joined = expected.merge(
        left,
        on=keys,
        how="outer",
        suffixes=("_expected", "_actual"),
        indicator=True,
        validate="one_to_one",
    )
    if not joined["_merge"].eq("both").all():
        errors.append("detail operation-anchor membership differs from source replay")
        return errors
    bool_columns = {
        "realized_return_ge20",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "combined_exclusion_candidate_flag",
        "primary_included",
        "sensitivity_included",
        "source_before_or_on_preweek_flag",
        "position_observed",
        "shape_observed",
        "classification_observed",
    }
    numeric_columns = {
        "latest_source_to_trigger_trading_days",
        "first_source_to_trigger_trading_days",
        "realized_return_pct",
        "anchor_order",
        "anchor_sequence_index",
        "source_to_preweek_trading_days",
        "preweek_to_trigger_trading_days",
        "trigger_to_confirmation_trading_days",
        "confirmation_to_entry_trading_days",
        "anchor_adjusted_close",
        "position_prior_session_count",
        "position_prior_adjusted_high",
        "position_prior_adjusted_low",
        "position_120d_pct",
        "shape_return20_pct",
        "shape_range23_pct",
        "shape_ema23_slope5_pct",
    }
    string_columns = required - bool_columns - numeric_columns - set(keys)
    for column in sorted(string_columns):
        expected_values = joined[f"{column}_expected"].fillna("").astype(str)
        actual_values = joined[f"{column}_actual"].fillna("").astype(str)
        mismatches = int((~expected_values.eq(actual_values)).sum())
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    for column in sorted(bool_columns):
        mismatches = int(
            (~_boolish(joined[f"{column}_expected"]).eq(
                _boolish(joined[f"{column}_actual"])
            )).sum()
        )
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    for column in sorted(numeric_columns):
        mismatches = sum(
            not _same_number(expected_value, actual_value)
            for expected_value, actual_value in zip(
                joined[f"{column}_expected"], joined[f"{column}_actual"]
            )
        )
        if mismatches:
            errors.append(f"detail {column} drift rows={mismatches}")
    observed_coverage = (
        left.loc[_boolish(left["classification_observed"])]
        .groupby("anchor_id")["operation_key"]
        .nunique()
        .to_dict()
    )
    if observed_coverage != PINNED_ANCHOR_COVERAGE:
        errors.append(
            f"detail anchor coverage drift: {observed_coverage}/{PINNED_ANCHOR_COVERAGE}"
        )
    chronological = left["source_before_or_on_preweek_flag"].map(_bool_value)
    expected_semantics = np.where(
        chronological,
        "chronological_source_to_preweek_to_confirmation",
        "labeled_anchor_comparison_not_chronological_latest_source_after_preweek",
    )
    if not left["comparison_sequence_semantics"].astype(str).eq(
        expected_semantics
    ).all():
        errors.append("detail chronological transition labels are not source<=preweek exact")
    return errors


def _performance_metrics(part: pd.DataFrame) -> dict[str, float | int | None]:
    returns = pd.to_numeric(part["realized_return_pct"], errors="coerce")
    outcomes = part["return_outcome"].astype(str)
    total = len(part)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    failures = int(outcomes.eq("failure").sum())
    ge20 = int(returns.ge(20).sum())
    le_minus20 = int(returns.le(-20).sum())
    return {
        "operation_count": total,
        "unique_stock_count": int(part["stock_id"].nunique()),
        "unique_episode_count": int(part["episode_key"].nunique()),
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failures,
        "win_rate_pct": _rate(wins, total),
        "neutral_rate_pct": _rate(neutral, total),
        "failure_rate_pct": _rate(failures, total),
        "avg_return_pct": _stat(returns, "mean"),
        "median_return_pct": _stat(returns, "median"),
        "p10_return_pct": _stat(returns, "p10"),
        "p90_return_pct": _stat(returns, "p90"),
        "min_return_pct": _stat(returns, "min"),
        "max_return_pct": _stat(returns, "max"),
        "return_ge20_count": ge20,
        "return_ge20_rate_pct": _rate(ge20, total),
        "return_le_minus20_count": le_minus20,
        "return_le_minus20_rate_pct": _rate(le_minus20, total),
        "top1_abs_return_share_pct": _top_abs_share(returns, 1),
        "top5_abs_return_share_pct": _top_abs_share(returns, 5),
        "avg_latest_source_to_trigger_trading_days": _stat(
            part["latest_source_to_trigger_trading_days"], "mean"
        ),
        "median_latest_source_to_trigger_trading_days": _stat(
            part["latest_source_to_trigger_trading_days"], "median"
        ),
        "avg_first_source_to_trigger_trading_days": _stat(
            part["first_source_to_trigger_trading_days"], "mean"
        ),
        "median_first_source_to_trigger_trading_days": _stat(
            part["first_source_to_trigger_trading_days"], "median"
        ),
        "avg_source_to_preweek_trading_days": _stat(
            part["source_to_preweek_trading_days"], "mean"
        ),
        "median_source_to_preweek_trading_days": _stat(
            part["source_to_preweek_trading_days"], "median"
        ),
        "source_before_or_on_preweek_count": int(
            _boolish(part["source_before_or_on_preweek_flag"]).sum()
        ),
        "source_anomaly_candidate_count": int(
            _boolish(part["source_anomaly_candidate_flag"]).sum()
        ),
        "operation_return_review_candidate_count": int(
            _boolish(part["operation_return_review_candidate_flag"]).sum()
        ),
        "unresolved_price_path_candidate_count": int(
            _boolish(part["unresolved_price_path_candidate_flag"]).sum()
        ),
        "combined_exclusion_candidate_count": int(
            _boolish(part["combined_exclusion_candidate_flag"]).sum()
        ),
    }


def _validate_metrics(
    row: object,
    expected: dict[str, float | int | None],
    label: str,
    errors: list[str],
) -> None:
    for column, value in expected.items():
        observed = getattr(row, column)
        if not _same_number(observed, value):
            errors.append(f"{label} metric drift: {column}")


def _compare_summary(
    summary: pd.DataFrame,
    expected_detail: pd.DataFrame,
    lineage: dict[str, str],
) -> list[str]:
    errors = _governance_errors(summary, "summary", lineage)
    required_keys = {
        (basis, anchor, cell)
        for basis in ANALYSIS_BASES
        for anchor in ANCHOR_IDS
        for cell in CELL_IDS
    }
    observed_keys = set(
        zip(
            summary["analysis_basis"].astype(str),
            summary["anchor_id"].astype(str),
            summary["position_shape_cell_id"].astype(str),
        )
    )
    if observed_keys != required_keys or summary.duplicated(
        ["analysis_basis", "anchor_id", "position_shape_cell_id"]
    ).any():
        errors.append("summary must contain exactly 12 cells plus insufficient per basis/anchor")
        return errors
    parts = {
        PRIMARY_ANALYSIS_BASIS: expected_detail,
        SENSITIVITY_ANALYSIS_BASIS: expected_detail.loc[
            _boolish(expected_detail["sensitivity_included"])
        ],
    }
    for row in summary.itertuples(index=False):
        basis = parts[str(row.analysis_basis)]
        anchor = basis.loc[basis["anchor_id"].eq(str(row.anchor_id))]
        part = anchor.loc[
            anchor["position_shape_cell_id"].eq(str(row.position_shape_cell_id))
        ]
        expected_count = int(basis["operation_key"].nunique())
        observed_count = int(_boolish(anchor["classification_observed"]).sum())
        prefix = f"summary {row.analysis_basis}/{row.anchor_id}/{row.position_shape_cell_id}"
        if int(row.analysis_basis_operation_count) != expected_count:
            errors.append(f"{prefix} analysis-basis count drift")
        if int(row.anchor_classification_observed_count) != observed_count:
            errors.append(f"{prefix} observed coverage count drift")
        if not _same_number(
            row.anchor_classification_coverage_pct, _rate(observed_count, len(anchor))
        ):
            errors.append(f"{prefix} observed coverage rate drift")
        if not _same_number(row.cell_share_of_anchor_pct, _rate(len(part), len(anchor))):
            errors.append(f"{prefix} cell share drift")
        _validate_metrics(row, _performance_metrics(part), prefix, errors)
        if int(row.same_stock_overlap_pair_count) != 0:
            errors.append(f"{prefix} overlap count must be zero")
        if str(row.position_policy) != POSITION_POLICY:
            errors.append(f"{prefix} position policy drift")
        if str(row.shape_policy) != SHAPE_POLICY:
            errors.append(f"{prefix} shape policy drift")
    for basis, detail in parts.items():
        for anchor in ANCHOR_IDS:
            rows = summary.loc[
                summary["analysis_basis"].eq(basis)
                & summary["anchor_id"].eq(anchor)
            ]
            if int(pd.to_numeric(rows["operation_count"], errors="coerce").sum()) != int(
                detail["operation_key"].nunique()
            ):
                errors.append(f"summary cells do not conserve operations: {basis}/{anchor}")
    return errors


def _operation_transitions(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for operation_key, group in detail.groupby("operation_key", sort=False):
        anchors = group.set_index("anchor_id", drop=False)
        if set(anchors.index) != set(ANCHOR_IDS) or len(anchors) != len(ANCHOR_IDS):
            raise RuntimeError(f"transition anchors are incomplete: {operation_key}")
        first = anchors.loc["revenue_available"]
        row: dict[str, object] = {
            "operation_key": operation_key,
            "episode_key": str(first["episode_key"]),
            "stock_id": str(first["stock_id"]),
            "realized_return_pct": first["realized_return_pct"],
            "return_outcome": str(first["return_outcome"]),
            "latest_source_to_trigger_trading_days": first[
                "latest_source_to_trigger_trading_days"
            ],
            "first_source_to_trigger_trading_days": first[
                "first_source_to_trigger_trading_days"
            ],
            "source_to_preweek_trading_days": first["source_to_preweek_trading_days"],
            "source_before_or_on_preweek_flag": first[
                "source_before_or_on_preweek_flag"
            ],
            "anchor_chronology_id": str(first["anchor_chronology_id"]),
            "comparison_sequence_semantics": str(
                first["comparison_sequence_semantics"]
            ),
            "source_anomaly_candidate_flag": first[
                "source_anomaly_candidate_flag"
            ],
            "operation_return_review_candidate_flag": first[
                "operation_return_review_candidate_flag"
            ],
            "unresolved_price_path_candidate_flag": first[
                "unresolved_price_path_candidate_flag"
            ],
            "combined_exclusion_candidate_flag": first[
                "combined_exclusion_candidate_flag"
            ],
            "sensitivity_included": first["sensitivity_included"],
        }
        for anchor_id in ANCHOR_IDS:
            anchor = anchors.loc[anchor_id]
            row[f"{anchor_id}_position_bucket"] = str(anchor["position_bucket"])
            row[f"{anchor_id}_shape_bucket"] = str(anchor["shape_bucket"])
            row[f"{anchor_id}_cell_id"] = str(anchor["position_shape_cell_id"])
        row["position_transition_id"] = ">".join(
            str(row[f"{anchor_id}_position_bucket"]) for anchor_id in ANCHOR_IDS
        )
        row["shape_transition_id"] = ">".join(
            str(row[f"{anchor_id}_shape_bucket"]) for anchor_id in ANCHOR_IDS
        )
        row["position_shape_transition_id"] = ">".join(
            str(row[f"{anchor_id}_cell_id"]) for anchor_id in ANCHOR_IDS
        )
        row["full_three_anchor_observed"] = all(
            row[f"{anchor_id}_cell_id"] != "insufficient_history"
            for anchor_id in ANCHOR_IDS
        )
        rows.append(row)
    return pd.DataFrame(rows)


def _compare_transition(
    transition: pd.DataFrame,
    expected_detail: pd.DataFrame,
    lineage: dict[str, str],
) -> list[str]:
    errors = _governance_errors(transition, "transition", lineage)
    operations = _operation_transitions(expected_detail)
    parts = {
        PRIMARY_ANALYSIS_BASIS: operations,
        SENSITIVITY_ANALYSIS_BASIS: operations.loc[
            _boolish(operations["sensitivity_included"])
        ],
    }
    key_columns = [
        "anchor_chronology_id",
        "comparison_sequence_semantics",
        "position_transition_id",
        "shape_transition_id",
        "position_shape_transition_id",
    ]
    expected_keys: set[tuple[str, str, str, str, str, str, str]] = set()
    expected_parts: dict[
        tuple[str, str, str, str, str, str, str], pd.DataFrame
    ] = {}
    for basis, part in parts.items():
        overall_key = (
            basis,
            "overall_state_comparison",
            "all",
            "all_anchor_comparison_sequences",
            "all",
            "all",
            "all",
        )
        expected_keys.add(overall_key)
        expected_parts[overall_key] = part
        complete = part.loc[_boolish(part["full_three_anchor_observed"])]
        for keys, group in complete.groupby(key_columns, sort=False, dropna=False):
            row_type = (
                "chronological_transition"
                if str(keys[0]) == "source_before_or_on_preweek"
                else "nonchronological_anchor_state_sequence"
            )
            key = (basis, row_type, *(str(value) for value in keys))
            expected_keys.add(key)
            expected_parts[key] = group
    observed_keys = {
        (
            str(row.analysis_basis),
            str(row.row_type),
            str(row.anchor_chronology_id),
            str(row.comparison_sequence_semantics),
            str(row.position_transition_id),
            str(row.shape_transition_id),
            str(row.position_shape_transition_id),
        )
        for row in transition.itertuples(index=False)
    }
    if observed_keys != expected_keys or transition.duplicated(
        ["analysis_basis", "row_type", *key_columns]
    ).any():
        errors.append("transition membership differs from independent replay")
        return errors
    for row in transition.itertuples(index=False):
        key = (
            str(row.analysis_basis),
            str(row.row_type),
            str(row.anchor_chronology_id),
            str(row.comparison_sequence_semantics),
            str(row.position_transition_id),
            str(row.shape_transition_id),
            str(row.position_shape_transition_id),
        )
        part = expected_parts[key]
        label = "transition " + "/".join(key)
        _validate_metrics(row, _performance_metrics(part), label, errors)
        full_observed = int(_boolish(part["full_three_anchor_observed"]).sum())
        if int(row.full_three_anchor_observed_count) != full_observed:
            errors.append(f"{label} full-three-anchor count drift")
        if not _same_number(
            row.full_three_anchor_observed_rate_pct,
            _rate(full_observed, len(part)),
        ):
            errors.append(f"{label} full-three-anchor rate drift")
        if int(row.same_stock_overlap_pair_count) != 0:
            errors.append(f"{label} overlap count must be zero")
    non_overall = transition.loc[
        transition["row_type"].isin(
            ["chronological_transition", "nonchronological_anchor_state_sequence"]
        )
    ]
    chronological = non_overall["anchor_chronology_id"].eq(
        "source_before_or_on_preweek"
    )
    if not non_overall.loc[chronological, "comparison_sequence_semantics"].eq(
        "chronological_source_to_preweek_to_confirmation"
    ).all():
        errors.append("source<=preweek transitions lack the exact chronological label")
    if not non_overall.loc[~chronological, "comparison_sequence_semantics"].eq(
        "labeled_anchor_comparison_not_chronological_latest_source_after_preweek"
    ).all():
        errors.append("source-after-preweek rows are incorrectly called chronological")
    for basis, part in parts.items():
        grouped = transition.loc[
            transition["analysis_basis"].eq(basis)
            & transition["row_type"].isin(
                ["chronological_transition", "nonchronological_anchor_state_sequence"]
            )
        ]
        expected_complete = int(_boolish(part["full_three_anchor_observed"]).sum())
        if int(pd.to_numeric(grouped["operation_count"], errors="coerce").sum()) != len(
            part.loc[_boolish(part["full_three_anchor_observed"])]
        ):
            errors.append(
                "transition groups do not conserve complete three-anchor operations: "
                f"{basis}/{int(pd.to_numeric(grouped['operation_count'], errors='coerce').sum())}/"
                f"{expected_complete}"
            )
    return errors


def _validate_mirrors_and_markdown(paths: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    for name, path in paths.items():
        if not path.is_file():
            errors.append(f"artifact is missing: {name}={path}")
    if errors:
        return errors
    if not (
        paths["summary"].read_bytes()
        == paths["summary_history"].read_bytes()
        == paths["summary_docs"].read_bytes()
    ):
        errors.append("summary latest/history/docs mirrors drift")
    if not (
        paths["transition"].read_bytes()
        == paths["transition_history"].read_bytes()
        == paths["transition_docs"].read_bytes()
    ):
        errors.append("transition latest/history/docs mirrors drift")
    if paths["markdown"].read_bytes() != paths["markdown_docs"].read_bytes():
        errors.append("markdown latest/docs mirrors drift")
    markdown = paths["markdown"].read_text(encoding="utf-8")
    for token in (
        "research_only",
        "120",
        "asof_latest_qualifying_trade_date",
        "chronological transition",
        "adjusted analysis price",
        "anomaly candidates",
        "財報",
    ):
        if token not in markdown:
            errors.append(f"markdown omits required explanation: {token}")
    return errors


def validate(
    *,
    artifact_root: Path = ROOT,
    source_root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    artifact_root = artifact_root.resolve()
    source_root = source_root.resolve()
    paths = {
        name: artifact_root / relative
        for name, relative in ARTIFACT_RELATIVE_PATHS.items()
    }
    errors.extend(_validate_mirrors_and_markdown(paths))
    if errors:
        return errors
    try:
        (
            lag,
            rearmed,
            lag_file_sha,
            rearmed_file_sha,
            lag_semantic_sha,
            rearmed_semantic_sha,
        ) = _read_source_frames(source_root)
        source = _prepare_source(lag, rearmed)
    except (RuntimeError, ValueError, KeyError, pd.errors.ParserError) as exc:
        return [str(exc)]
    _validate_pinned_source(source, lag_semantic_sha, rearmed_semantic_sha, errors)
    if errors:
        return errors
    lineage = {
        "source_operation_lag_detail_sha256": lag_file_sha,
        "source_operation_lag_semantic_sha256": lag_semantic_sha,
        "source_rearmed_detail_sha256": rearmed_file_sha,
        "source_rearmed_semantic_sha256": rearmed_semantic_sha,
    }
    try:
        expected_detail = _expected_detail(source, source_root)
        summary = pd.read_csv(paths["summary"], keep_default_na=False, low_memory=False)
        detail = pd.read_csv(
            paths["detail"],
            dtype={"stock_id": str},
            keep_default_na=False,
            low_memory=False,
        )
        transition = pd.read_csv(
            paths["transition"], keep_default_na=False, low_memory=False
        )
        errors.extend(_compare_detail(detail, expected_detail, lineage))
        errors.extend(_compare_summary(summary, expected_detail, lineage))
        errors.extend(_compare_transition(transition, expected_detail, lineage))
    except (RuntimeError, ValueError, KeyError, AttributeError, pd.errors.ParserError) as exc:
        errors.append(str(exc))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Independently validate the revenue position/shape transition matrix."
        )
    )
    parser.add_argument(
        "--artifact-root",
        type=Path,
        default=ROOT,
        help="Repository root containing generated matrix artifacts.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=ROOT,
        help="Repository root containing source baseline and stock price history.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(
        artifact_root=args.artifact_root,
        source_root=args.source_root,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue_unreacted_range position/shape transition matrix validation passed: "
        f"operations={PINNED_OPERATION_COUNT} stocks={PINNED_UNIQUE_STOCK_COUNT} "
        f"sensitivity={PINNED_SENSITIVITY_COUNT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
