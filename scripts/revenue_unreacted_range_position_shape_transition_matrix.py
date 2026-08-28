from __future__ import annotations

from datetime import datetime
import hashlib
import math
from pathlib import Path
from typing import Mapping
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from revenue_unreacted_range_operation_lag_bucket_audit import (
    ARTIFACT_VERSION as SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
)
from revenue_unreacted_range_rearmed_operation_grid import (
    ARTIFACT_VERSION as SOURCE_REARMED_ARTIFACT_VERSION,
)
from revenue_unreacted_range_source_first_condition_audit import load_stock_price


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_position_shape_transition_matrix"
V1_ARTIFACT_VERSION = "position_shape_transition_matrix_v1_20260717"
V2_ARTIFACT_VERSION = "position_shape_transition_matrix_v2_20260822"
V3_ARTIFACT_VERSION = "position_shape_transition_matrix_v3_20260829"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION
SOURCE_OPERATION_LAG_ARTIFACT_ID = "revenue_unreacted_range_operation_lag_bucket_audit"
SOURCE_REARMED_ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
V2_SOURCE_OPERATION_LAG_ARTIFACT_VERSION = "operation_lag_bucket_v2_20260822"
V2_SOURCE_REARMED_ARTIFACT_VERSION = "rearmed_operation_grid_v2_20260822"
V3_SOURCE_OPERATION_LAG_ARTIFACT_VERSION = "operation_lag_bucket_v3_20260829"
V3_SOURCE_REARMED_ARTIFACT_VERSION = "rearmed_operation_grid_v3_20260829"


def versions_for_operation_lag_artifact(
    source_artifact_version: object,
) -> tuple[str, str]:
    version = str(source_artifact_version).strip()
    mapping = {
        SOURCE_OPERATION_LAG_ARTIFACT_VERSION: (
            V1_ARTIFACT_VERSION,
            SOURCE_REARMED_ARTIFACT_VERSION,
        ),
        V2_SOURCE_OPERATION_LAG_ARTIFACT_VERSION: (
            V2_ARTIFACT_VERSION,
            V2_SOURCE_REARMED_ARTIFACT_VERSION,
        ),
        V3_SOURCE_OPERATION_LAG_ARTIFACT_VERSION: (
            V3_ARTIFACT_VERSION,
            V3_SOURCE_REARMED_ARTIFACT_VERSION,
        ),
    }
    if version not in mapping:
        raise RuntimeError(
            f"unsupported operation-lag artifact version: {version or '<empty>'}"
        )
    return mapping[version]
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
ADOPTED_GRID_ID = (
    "rearm_after_realized_exit_next_trade_day|"
    "delayed_next_close_continuation_bonus|d30|none_no_stop_reference"
)
PRICE_HISTORY_CUTOFF_DATE = "20260713"

PINNED_OPERATION_LAG_SEMANTIC_SHA256 = (
    "04e627169d6a2198d2f523bc52067e93a36d7d73f81155214cd38e2ea5e35600"
)
PINNED_REARMED_SEMANTIC_SHA256 = (
    "e7b20554d93dbe71abc3dd683691bc710e1f941b73a83ae12fd48057423eb643"
)
PINNED_PRIMARY_OPERATION_COUNT = 955
PINNED_PRIMARY_UNIQUE_STOCK_COUNT = 602
PINNED_PRIMARY_WIN_COUNT = 535
PINNED_PRIMARY_NEUTRAL_COUNT = 7
PINNED_PRIMARY_FAILURE_COUNT = 413
PINNED_PRIMARY_AVG_RETURN_PCT = 9.1232
PINNED_PRIMARY_MEDIAN_RETURN_PCT = 2.0
PINNED_PRIMARY_RETURN_GE20_COUNT = 201
PINNED_SOURCE_ANOMALY_CANDIDATE_COUNT = 90
PINNED_OPERATION_RETURN_REVIEW_CANDIDATE_COUNT = 25
PINNED_SENSITIVITY_OPERATION_COUNT = 841

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "excluding_unresolved_anomaly_candidates_sensitivity"
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)

POSITION_BUCKETS = (
    (10, "low_pos_le40"),
    (20, "mid_pos_40_75"),
    (30, "high_pos_gt75"),
)
SHAPE_BUCKETS = (
    (10, "consolidation"),
    (20, "rising"),
    (30, "falling"),
    (40, "mixed_or_turn"),
)
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
ANCHOR_IDS = tuple(anchor[1] for anchor in ANCHORS)

POSITION_POLICY = (
    "anchor adjusted close positioned within the adjusted analysis-high/analysis-low range "
    "of exactly 120 prior trading sessions, excluding the anchor"
)
SHAPE_POLICY = (
    "revenue-model-owned descriptive shape: adjusted close return from t-20 to anchor; "
    "adjusted-close range across the 23 sessions ending at anchor; EMA23 through anchor "
    "with five-session slope"
)
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
ANOMALY_POLICY = (
    "primary retains source, unresolved price-path, and operation-return review candidates; "
    "sensitivity excludes their union without assigning a final anomaly disposition"
)
SAMPLE_POLICY = "sample_count_disclosed_not_used_as_automatic_rejection"

SOURCE_OPERATION_LAG_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv"
)
SOURCE_REARMED_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv"
)
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
PRICE_RESOLUTION_CSV = ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"

DEFAULT_OUTPUT_RELATIVE_PATHS = {
    "summary_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv",
    "detail_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv",
    "transition_latest": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_transition_latest.csv"
    ),
    "markdown_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md",
    "summary_history": f"output/history/research/{ARTIFACT_ID}.csv",
    "transition_history": f"output/history/research/{ARTIFACT_ID}_transition.csv",
    "summary_docs": f"docs/latest/{ARTIFACT_ID}_latest.csv",
    "transition_docs": f"docs/latest/{ARTIFACT_ID}_transition_latest.csv",
    "markdown_docs": f"docs/latest/{ARTIFACT_ID}_latest.md",
}

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


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


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


def _number(value: object) -> float:
    number = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(number) if pd.notna(number) else math.nan


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _metric(values: pd.Series, method: str) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return ""
    if method == "mean":
        value = numeric.mean()
    elif method == "median":
        value = numeric.median()
    elif method == "p10":
        value = numeric.quantile(0.10)
    elif method == "p90":
        value = numeric.quantile(0.90)
    elif method == "min":
        value = numeric.min()
    elif method == "max":
        value = numeric.max()
    else:
        raise ValueError(f"unsupported metric method: {method}")
    return round(float(value), 4)


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
        raise RuntimeError(f"position/shape canonical source is missing columns: {missing}")
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
        raise RuntimeError("position/shape canonical source is empty")
    canonical["stock_id"] = canonical["stock_id"].map(_stock_id)
    for column in columns:
        if column in CANONICAL_DATE_COLUMNS:
            canonical[column] = canonical[column].map(_date_text)
        elif column in CANONICAL_INTEGER_COLUMNS:
            numeric = pd.to_numeric(canonical[column], errors="coerce")
            if numeric.isna().any() or not np.isclose(numeric, numeric.round()).all():
                raise RuntimeError(
                    f"position/shape canonical integer column is invalid: {column}"
                )
            canonical[column] = numeric.round().astype("int64").astype(str)
        elif column in CANONICAL_FLOAT_COLUMNS:
            numeric = pd.to_numeric(canonical[column], errors="coerce")
            if numeric.isna().any():
                raise RuntimeError(
                    f"position/shape canonical float column is invalid: {column}"
                )
            canonical[column] = numeric.map(lambda value: f"{float(value):.8f}")
        elif column in CANONICAL_BOOL_COLUMNS:
            canonical[column] = canonical[column].map(
                lambda value: "true" if _bool_value(value) else "false"
            )
        else:
            canonical[column] = canonical[column].astype(str).str.strip()
    canonical = canonical.sort_values(
        ["stock_id", "entry_date", "episode_key", "trigger_date", "confirmation_date", "exit_date"],
        kind="mergesort",
    ).reset_index(drop=True)
    if canonical.astype(str).apply(
        lambda column: column.str.contains(r"[\t\r\n]", regex=True).any()
    ).any():
        raise RuntimeError("position/shape canonical source contains control separators")
    payload = canonical.to_csv(index=False, lineterminator="\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def canonical_operation_lag_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_semantic_sha256(
        frame,
        OPERATION_LAG_CANONICAL_COLUMNS,
        filter_rearmed_grid=False,
    )


def canonical_rearmed_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_semantic_sha256(
        frame,
        REARMED_CANONICAL_COLUMNS,
        filter_rearmed_grid=True,
    )


def _top_abs_share(values: pd.Series, count: int) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna().abs()
    total = float(numeric.sum())
    if not len(numeric) or total <= 0:
        return ""
    return round(float(numeric.nlargest(count).sum()) / total * 100.0, 4)


def _overlap_pair_count(frame: pd.DataFrame) -> int:
    count = 0
    for _stock_id, stock in frame.groupby("stock_id", sort=False):
        ordered = stock.sort_values("entry_date", kind="mergesort")
        prior_exit = ""
        for row in ordered.itertuples(index=False):
            if prior_exit and str(row.entry_date) <= prior_exit:
                count += 1
            prior_exit = max(prior_exit, str(row.exit_date))
    return count


def _load_operation_lag_detail(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"position/shape operation-lag detail is missing: {path}")
    return pd.read_csv(
        path,
        dtype={
            "stock_id": str,
            "trigger_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "exit_date": str,
            "asof_latest_qualifying_source_date": str,
            "asof_latest_qualifying_trade_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )


def _prepare_operation_lag_detail(
    frame: pd.DataFrame,
    *,
    enforce_pinned_baseline: bool,
    expected_artifact_version: str = SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
) -> pd.DataFrame:
    required = {
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
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"position/shape source detail is missing columns: {missing}")
    source = frame.copy()
    source["stock_id"] = source["stock_id"].map(_stock_id)
    for column in (
        "asof_latest_qualifying_source_date",
        "asof_latest_qualifying_trade_date",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
    ):
        source[column] = source[column].map(_date_text)
        if source[column].eq("").any():
            raise RuntimeError(f"position/shape source has invalid {column}")
    source = source.loc[source["grid_id"].astype(str).eq(ADOPTED_GRID_ID)].copy()
    if source.empty:
        raise RuntimeError("position/shape adopted source grid is empty")
    if set(source["model_id"].astype(str)) != {MODEL_ID}:
        raise RuntimeError("position/shape source model drift")
    if set(source["artifact_id"].astype(str)) != {SOURCE_OPERATION_LAG_ARTIFACT_ID}:
        raise RuntimeError("position/shape source artifact drift")
    if set(source["artifact_version"].astype(str)) != {expected_artifact_version}:
        raise RuntimeError("position/shape source artifact version drift")
    if set(source["source_variant_id"].astype(str)) != {SOURCE_VARIANT_ID}:
        raise RuntimeError("position/shape source variant drift")
    if source.duplicated(list(OPERATION_KEY_COLUMNS)).any():
        raise RuntimeError("position/shape source contains duplicate operations")
    if not _boolish(source["time_travel_guard_passed"]).all():
        raise RuntimeError("position/shape source time-travel guard failed")
    if not _boolish(source["same_stock_non_overlap_applied"]).all():
        raise RuntimeError("position/shape source non-overlap flag failed")
    source["realized_return_pct"] = pd.to_numeric(
        source["realized_return_pct"], errors="coerce"
    )
    if source["realized_return_pct"].isna().any():
        raise RuntimeError("position/shape source has invalid realized returns")
    computed_outcome = np.where(
        source["realized_return_pct"].gt(0.0),
        "win",
        np.where(source["realized_return_pct"].lt(0.0), "failure", "neutral"),
    )
    if not source["return_outcome"].astype(str).eq(computed_outcome).all():
        raise RuntimeError("position/shape source return outcome drift")
    if not _boolish(source["realized_return_ge20"]).eq(
        source["realized_return_pct"].ge(20.0)
    ).all():
        raise RuntimeError("position/shape source return >=20 flag drift")
    source["source_anomaly_candidate_flag"] = _boolish(
        source["source_anomaly_candidate_flag"]
    )
    source["operation_return_review_candidate_flag"] = _boolish(
        source["operation_return_review_candidate_flag"]
    )
    source["unresolved_price_path_candidate_flag"] = False
    source["combined_exclusion_candidate_flag"] = (
        source["source_anomaly_candidate_flag"]
        | source["unresolved_price_path_candidate_flag"]
        | source["operation_return_review_candidate_flag"]
    )
    source["primary_included"] = True
    source["sensitivity_included"] = ~source["combined_exclusion_candidate_flag"]
    source["operation_key"] = source.loc[:, OPERATION_KEY_COLUMNS].astype(str).agg(
        "|".join, axis=1
    )
    if source["operation_key"].duplicated().any():
        raise RuntimeError("position/shape operation key is not unique")
    overlap_count = _overlap_pair_count(source)
    if overlap_count:
        raise RuntimeError(f"position/shape source operations overlap: {overlap_count}")

    _ = enforce_pinned_baseline
    return source.sort_values(["stock_id", "entry_date"], kind="mergesort").reset_index(
        drop=True
    )


def _validate_pinned_baseline(source: pd.DataFrame) -> None:
    outcomes = source["return_outcome"].astype(str)
    checks = {
        "operation_count": (len(source), PINNED_PRIMARY_OPERATION_COUNT),
        "unique_stock_count": (
            source["stock_id"].nunique(),
            PINNED_PRIMARY_UNIQUE_STOCK_COUNT,
        ),
        "win_count": (int(outcomes.eq("win").sum()), PINNED_PRIMARY_WIN_COUNT),
        "neutral_count": (
            int(outcomes.eq("neutral").sum()),
            PINNED_PRIMARY_NEUTRAL_COUNT,
        ),
        "failure_count": (
            int(outcomes.eq("failure").sum()),
            PINNED_PRIMARY_FAILURE_COUNT,
        ),
        "return_ge20_count": (
            int(source["realized_return_pct"].ge(20.0).sum()),
            PINNED_PRIMARY_RETURN_GE20_COUNT,
        ),
        "source_anomaly_candidate_count": (
            int(source["source_anomaly_candidate_flag"].sum()),
            PINNED_SOURCE_ANOMALY_CANDIDATE_COUNT,
        ),
        "unresolved_price_path_candidate_count": (
            int(source["unresolved_price_path_candidate_flag"].sum()),
            1,
        ),
        "operation_return_review_candidate_count": (
            int(source["operation_return_review_candidate_flag"].sum()),
            PINNED_OPERATION_RETURN_REVIEW_CANDIDATE_COUNT,
        ),
        "sensitivity_operation_count": (
            int(source["sensitivity_included"].sum()),
            PINNED_SENSITIVITY_OPERATION_COUNT,
        ),
    }
    for label, (actual, expected) in checks.items():
        if actual != expected:
            raise RuntimeError(
                f"position/shape pinned baseline {label} drift: {actual}/{expected}"
            )
    average = round(float(source["realized_return_pct"].mean()), 4)
    median = round(float(source["realized_return_pct"].median()), 4)
    if average != PINNED_PRIMARY_AVG_RETURN_PCT:
        raise RuntimeError(
            f"position/shape pinned baseline average drift: {average}/"
            f"{PINNED_PRIMARY_AVG_RETURN_PCT}"
        )
    if median != PINNED_PRIMARY_MEDIAN_RETURN_PCT:
        raise RuntimeError(
            f"position/shape pinned baseline median drift: {median}/"
            f"{PINNED_PRIMARY_MEDIAN_RETURN_PCT}"
        )


def _load_rearmed_detail(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"position/shape rearmed detail is missing: {path}")
    usecols = [
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
    ]
    return pd.read_csv(
        path,
        usecols=usecols,
        dtype={column: str for column in OPERATION_KEY_COLUMNS},
        keep_default_na=False,
        low_memory=False,
    )


def _validate_rearmed_lineage(
    source: pd.DataFrame,
    rearmed: pd.DataFrame,
    *,
    expected_artifact_version: str = SOURCE_REARMED_ARTIFACT_VERSION,
) -> pd.DataFrame:
    required = {
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
    missing = sorted(required - set(rearmed.columns))
    if missing:
        raise RuntimeError(f"position/shape rearmed lineage is missing columns: {missing}")
    lineage = rearmed.loc[
        rearmed["grid_id"].astype(str).eq(ADOPTED_GRID_ID)
        & _boolish(rearmed["return_valid"])
    ].copy()
    if set(lineage["artifact_id"].astype(str)) != {SOURCE_REARMED_ARTIFACT_ID}:
        raise RuntimeError("position/shape rearmed artifact drift")
    if set(lineage["artifact_version"].astype(str)) != {expected_artifact_version}:
        raise RuntimeError("position/shape rearmed artifact version drift")
    lineage["stock_id"] = lineage["stock_id"].map(_stock_id)
    for column in ("trigger_date", "confirmation_date", "entry_date", "exit_date"):
        lineage[column] = lineage[column].map(_date_text)
    if lineage.duplicated(list(OPERATION_KEY_COLUMNS)).any():
        raise RuntimeError("position/shape rearmed lineage contains duplicate mature operations")
    compare_columns = [
        *OPERATION_KEY_COLUMNS,
        "realized_return_pct",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
    ]
    joined = source.loc[:, compare_columns].merge(
        lineage.loc[:, compare_columns],
        on=list(OPERATION_KEY_COLUMNS),
        how="outer",
        suffixes=("_lag", "_rearmed"),
        indicator=True,
        validate="one_to_one",
    )
    if not joined["_merge"].eq("both").all():
        raise RuntimeError("position/shape operation-lag/rearmed lineage key drift")
    left_return = pd.to_numeric(joined["realized_return_pct_lag"], errors="coerce")
    right_return = pd.to_numeric(joined["realized_return_pct_rearmed"], errors="coerce")
    if (left_return - right_return).abs().gt(0.0001).any():
        raise RuntimeError("position/shape operation-lag/rearmed return drift")
    for column in (
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
    ):
        if not _boolish(joined[f"{column}_lag"]).eq(
            _boolish(joined[f"{column}_rearmed"])
        ).all():
            raise RuntimeError(f"position/shape operation-lag/rearmed {column} drift")
    unresolved = lineage.loc[
        :, [*OPERATION_KEY_COLUMNS, "unresolved_price_path_candidate_flag"]
    ].copy()
    unresolved["unresolved_price_path_candidate_flag"] = _boolish(
        unresolved["unresolved_price_path_candidate_flag"]
    )
    enriched = source.drop(columns=["unresolved_price_path_candidate_flag"]).merge(
        unresolved,
        on=list(OPERATION_KEY_COLUMNS),
        how="left",
        validate="one_to_one",
    )
    if enriched["unresolved_price_path_candidate_flag"].isna().any():
        raise RuntimeError("position/shape unresolved price-path lineage is incomplete")
    enriched["unresolved_price_path_candidate_flag"] = enriched[
        "unresolved_price_path_candidate_flag"
    ].astype(bool)
    enriched["combined_exclusion_candidate_flag"] = (
        enriched["source_anomaly_candidate_flag"]
        | enriched["unresolved_price_path_candidate_flag"]
        | enriched["operation_return_review_candidate_flag"]
    )
    enriched["sensitivity_included"] = ~enriched["combined_exclusion_candidate_flag"]
    return enriched.sort_values(["stock_id", "entry_date"], kind="mergesort").reset_index(
        drop=True
    )


def _load_price_resolutions(path: Path) -> pd.DataFrame:
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
        raise RuntimeError(f"position/shape price resolution is missing columns: {missing}")
    frame = frame.loc[
        frame["root_cause_status"].astype(str).eq(
            "verified_non_comparable_raw_price_scale"
        )
    ].copy()
    frame["stock_id"] = frame["stock_id"].map(_stock_id)
    frame["resume_date"] = frame["resume_date"].map(_date_text)
    frame["exchange_ratio"] = pd.to_numeric(frame["exchange_ratio"], errors="coerce")
    return frame


def _normalize_price_frame(frame: pd.DataFrame, stock_id: str) -> pd.DataFrame:
    required = {"date", "analysis_open", "analysis_high", "analysis_low", "analysis_close"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"position/shape adjusted price frame is missing for {stock_id}: {missing}"
        )
    stock = frame.copy()
    stock["date"] = stock["date"].map(_date_text)
    stock = stock.loc[
        stock["date"].str.fullmatch(r"\d{8}")
        & stock["date"].le(PRICE_HISTORY_CUTOFF_DATE)
    ].copy()
    stock = stock.sort_values("date", kind="mergesort").reset_index(drop=True)
    if stock.empty:
        raise RuntimeError(f"position/shape adjusted price frame is empty: {stock_id}")
    if stock["date"].duplicated().any():
        raise RuntimeError(f"position/shape adjusted price dates are duplicated: {stock_id}")
    for column in ("analysis_open", "analysis_high", "analysis_low", "analysis_close"):
        stock[column] = pd.to_numeric(stock[column], errors="coerce")
    stock["analysis_ema23"] = stock["analysis_close"].ewm(
        span=23, adjust=False, min_periods=23
    ).mean()
    stock["stock_sequence_index"] = np.arange(len(stock), dtype=int)
    return stock


def load_adjusted_daily_by_stock(
    stock_ids: list[str] | tuple[str, ...] | set[str],
    *,
    price_history_dir: Path | str = PRICE_HISTORY_DIR,
    price_resolution_path: Path | str | None = None,
) -> dict[str, pd.DataFrame]:
    price_dir = Path(price_history_dir)
    resolution_path = (
        Path(price_resolution_path)
        if price_resolution_path is not None
        else price_dir.parents[1]
        / "config/revenue_unreacted_range_price_comparability_resolution.csv"
    )
    resolutions = _load_price_resolutions(resolution_path)
    output: dict[str, pd.DataFrame] = {}
    for stock_id in sorted({_stock_id(value) for value in stock_ids}):
        path = price_dir / f"{stock_id}.csv"
        if not path.is_file():
            raise RuntimeError(f"position/shape price history is missing: {path}")
        stock = load_stock_price(
            stock_id,
            path,
            resolutions,
            observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
        )
        factor = pd.to_numeric(stock["analysis_price_adjustment_factor"], errors="coerce")
        for source_column, target_column in (
            ("open", "analysis_open"),
            ("high", "analysis_high"),
            ("low", "analysis_low"),
        ):
            stock[target_column] = pd.to_numeric(
                stock[source_column], errors="coerce"
            ) * factor
        output[stock_id] = _normalize_price_frame(stock, stock_id)
    return output


def _position_bucket(value: float) -> str:
    if value <= 40.0:
        return "low_pos_le40"
    if value <= 75.0:
        return "mid_pos_40_75"
    return "high_pos_gt75"


def _anchor_features(stock: pd.DataFrame, anchor_index: int) -> dict[str, object]:
    close = _number(stock.at[anchor_index, "analysis_close"])
    prior = stock.iloc[max(0, anchor_index - 120) : anchor_index]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    position_observed = bool(
        len(prior) == 120
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close)
    )
    high = float(prior_high.max()) if position_observed else math.nan
    low = float(prior_low.min()) if position_observed else math.nan
    position_observed = bool(position_observed and np.isfinite(high) and np.isfinite(low) and high > low)
    position = (close - low) / (high - low) * 100.0 if position_observed else math.nan
    position_bucket = _position_bucket(position) if position_observed else "insufficient_history"

    return20 = math.nan
    range23 = math.nan
    ema23_slope5 = math.nan
    if anchor_index >= 20:
        close20 = _number(stock.at[anchor_index - 20, "analysis_close"])
        if np.isfinite(close) and np.isfinite(close20) and close20 > 0:
            return20 = (close / close20 - 1.0) * 100.0
    recent = pd.to_numeric(
        stock.iloc[max(0, anchor_index - 22) : anchor_index + 1]["analysis_close"],
        errors="coerce",
    )
    if len(recent) == 23 and recent.notna().all() and float(recent.min()) > 0:
        range23 = (float(recent.max()) / float(recent.min()) - 1.0) * 100.0
    if anchor_index >= 5:
        ema_now = _number(stock.at[anchor_index, "analysis_ema23"])
        ema_prior = _number(stock.at[anchor_index - 5, "analysis_ema23"])
        if np.isfinite(ema_now) and np.isfinite(ema_prior) and ema_prior > 0:
            ema23_slope5 = (ema_now / ema_prior - 1.0) * 100.0
    shape_observed = bool(
        np.isfinite(return20) and np.isfinite(range23) and np.isfinite(ema23_slope5)
    )
    if not shape_observed:
        shape_bucket = "insufficient_history"
    elif return20 > 5.0 and ema23_slope5 > 0.0:
        shape_bucket = "rising"
    elif return20 < -5.0 and ema23_slope5 < 0.0:
        shape_bucket = "falling"
    elif abs(return20) <= 5.0 and range23 <= 15.0:
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
        "anchor_adjusted_close": round(close, 8) if np.isfinite(close) else "",
        "position_prior_session_count": len(prior),
        "position_window_start_date": str(prior["date"].iloc[0]) if len(prior) else "",
        "position_window_end_date": str(prior["date"].iloc[-1]) if len(prior) else "",
        "position_prior_adjusted_high": round(high, 8) if np.isfinite(high) else "",
        "position_prior_adjusted_low": round(low, 8) if np.isfinite(low) else "",
        "position_120d_pct": round(position, 4) if np.isfinite(position) else "",
        "position_observed": position_observed,
        "position_bucket": position_bucket,
        "shape_return20_pct": round(return20, 4) if np.isfinite(return20) else "",
        "shape_range23_pct": round(range23, 4) if np.isfinite(range23) else "",
        "shape_ema23_slope5_pct": (
            round(ema23_slope5, 4) if np.isfinite(ema23_slope5) else ""
        ),
        "shape_observed": shape_observed,
        "shape_bucket": shape_bucket,
        "classification_observed": classification_observed,
        "position_shape_cell_id": cell_id,
    }


def _anchor_context(operation: pd.Series, stock: pd.DataFrame) -> dict[str, object]:
    date_index = {str(date): int(index) for index, date in stock["date"].items()}
    named_dates = {
        "revenue": str(operation["asof_latest_qualifying_trade_date"]),
        "trigger": str(operation["trigger_date"]),
        "confirmation": str(operation["confirmation_date"]),
        "entry": str(operation["entry_date"]),
        "exit": str(operation["exit_date"]),
    }
    missing = [name for name, date in named_dates.items() if date not in date_index]
    if missing:
        raise RuntimeError(
            f"position/shape anchor dates are absent from price history: "
            f"{operation['stock_id']}/{operation['operation_key']}/{missing}"
        )
    revenue_index = date_index[named_dates["revenue"]]
    trigger_index = date_index[named_dates["trigger"]]
    confirmation_index = date_index[named_dates["confirmation"]]
    entry_index = date_index[named_dates["entry"]]
    exit_index = date_index[named_dates["exit"]]
    preweek_index = trigger_index - 5
    if preweek_index < 0:
        raise RuntimeError(
            f"position/shape trigger lacks five prior sessions: {operation['operation_key']}"
        )
    if revenue_index > trigger_index:
        raise RuntimeError(
            f"position/shape latest source is after trigger: {operation['operation_key']}"
        )
    if confirmation_index != trigger_index + 1:
        raise RuntimeError(
            f"position/shape delayed confirmation offset drift: {operation['operation_key']}"
        )
    if entry_index != confirmation_index + 1:
        raise RuntimeError(
            f"position/shape next-open entry offset drift: {operation['operation_key']}"
        )
    if exit_index < entry_index:
        raise RuntimeError(f"position/shape exit precedes entry: {operation['operation_key']}")
    source_date = str(operation["asof_latest_qualifying_source_date"])
    if source_date > named_dates["revenue"]:
        raise RuntimeError(
            f"position/shape official revenue source date is after mapped trade date: "
            f"{operation['operation_key']}"
        )
    source_before_preweek = revenue_index <= preweek_index
    chronology_id = (
        "source_before_or_on_preweek"
        if source_before_preweek
        else "latest_source_arrived_after_preweek_before_or_on_trigger"
    )
    return {
        "revenue_index": revenue_index,
        "preweek_index": preweek_index,
        "trigger_index": trigger_index,
        "confirmation_index": confirmation_index,
        "entry_index": entry_index,
        "exit_index": exit_index,
        "preweek_date": str(stock.at[preweek_index, "date"]),
        "source_to_preweek_trading_days": preweek_index - revenue_index,
        "preweek_to_trigger_trading_days": trigger_index - preweek_index,
        "trigger_to_confirmation_trading_days": confirmation_index - trigger_index,
        "confirmation_to_entry_trading_days": entry_index - confirmation_index,
        "source_before_or_on_preweek_flag": source_before_preweek,
        "anchor_chronology_id": chronology_id,
        "comparison_sequence_semantics": (
            "chronological_source_to_preweek_to_confirmation"
            if source_before_preweek
            else "labeled_anchor_comparison_not_chronological_latest_source_after_preweek"
        ),
    }


def _build_detail(
    source: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    *,
    generated_at: str,
    source_operation_lag_detail_sha256: str,
    source_operation_lag_semantic_sha256: str,
    source_rearmed_detail_sha256: str,
    source_rearmed_semantic_sha256: str,
) -> pd.DataFrame:
    normalized_daily = {
        _stock_id(stock_id): _normalize_price_frame(frame, _stock_id(stock_id))
        for stock_id, frame in daily_by_stock.items()
    }
    rows: list[dict[str, object]] = []
    anchor_metadata = {anchor_id: (order, date_rule, definition) for order, anchor_id, date_rule, definition in ANCHORS}
    for _, operation in source.iterrows():
        stock_id = str(operation["stock_id"])
        stock = normalized_daily.get(stock_id)
        if stock is None:
            raise RuntimeError(f"position/shape adjusted price history is missing: {stock_id}")
        context = _anchor_context(operation, stock)
        anchor_indices = {
            "revenue_available": int(context["revenue_index"]),
            "pre_breakout_week_close": int(context["preweek_index"]),
            "formal_confirmation_close": int(context["confirmation_index"]),
        }
        for anchor_id in ANCHOR_IDS:
            anchor_index = anchor_indices[anchor_id]
            anchor_order, anchor_date_rule, anchor_definition = anchor_metadata[anchor_id]
            features = _anchor_features(stock, anchor_index)
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": MODEL_ID,
                    "artifact_id": ARTIFACT_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "source_operation_lag_artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
                    "source_operation_lag_artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
                    "source_operation_lag_detail_sha256": source_operation_lag_detail_sha256,
                    "source_operation_lag_semantic_sha256": source_operation_lag_semantic_sha256,
                    "source_rearmed_artifact_id": SOURCE_REARMED_ARTIFACT_ID,
                    "source_rearmed_artifact_version": SOURCE_REARMED_ARTIFACT_VERSION,
                    "source_rearmed_detail_sha256": source_rearmed_detail_sha256,
                    "source_rearmed_semantic_sha256": source_rearmed_semantic_sha256,
                    "source_variant_id": SOURCE_VARIANT_ID,
                    "grid_id": ADOPTED_GRID_ID,
                    "operation_key": str(operation["operation_key"]),
                    "episode_key": str(operation["episode_key"]),
                    "stock_id": stock_id,
                    "stock_name": str(operation["stock_name"]),
                    "asof_latest_qualifying_source_date": str(
                        operation["asof_latest_qualifying_source_date"]
                    ),
                    "asof_latest_qualifying_trade_date": str(
                        operation["asof_latest_qualifying_trade_date"]
                    ),
                    "trigger_date": str(operation["trigger_date"]),
                    "confirmation_date": str(operation["confirmation_date"]),
                    "entry_date": str(operation["entry_date"]),
                    "exit_date": str(operation["exit_date"]),
                    "latest_source_to_trigger_trading_days": int(
                        _number(operation["latest_source_to_trigger_trading_days"])
                    ),
                    "first_source_to_trigger_trading_days": int(
                        _number(operation["first_source_to_trigger_trading_days"])
                    ),
                    "realized_return_pct": round(
                        float(operation["realized_return_pct"]), 4
                    ),
                    "return_outcome": str(operation["return_outcome"]),
                    "realized_return_ge20": bool(
                        float(operation["realized_return_pct"]) >= 20.0
                    ),
                    "source_anomaly_candidate_flag": bool(
                        operation["source_anomaly_candidate_flag"]
                    ),
                    "operation_return_review_candidate_flag": bool(
                        operation["operation_return_review_candidate_flag"]
                    ),
                    "unresolved_price_path_candidate_flag": bool(
                        operation["unresolved_price_path_candidate_flag"]
                    ),
                    "combined_exclusion_candidate_flag": bool(
                        operation["combined_exclusion_candidate_flag"]
                    ),
                    "primary_included": True,
                    "sensitivity_included": bool(operation["sensitivity_included"]),
                    "anchor_order": anchor_order,
                    "anchor_id": anchor_id,
                    "anchor_date_rule": anchor_date_rule,
                    "anchor_definition": anchor_definition,
                    "anchor_date": str(stock.at[anchor_index, "date"]),
                    "anchor_sequence_index": anchor_index,
                    **{
                        key: value
                        for key, value in context.items()
                        if not key.endswith("_index")
                    },
                    **features,
                    "position_policy": POSITION_POLICY,
                    "shape_policy": SHAPE_POLICY,
                    "price_basis": "adjusted_analysis_ohlc_only",
                    "price_history_cutoff_date": PRICE_HISTORY_CUTOFF_DATE,
                    "condition_role": "research_stratification_not_model_gate",
                    "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                    "approved_for_daily": False,
                    "presentation_allowed": False,
                    "formal_model_use_allowed": False,
                    "production_change": False,
                    "promotion_readiness": "research_only_not_promotion_evidence",
                }
            )
    detail = pd.DataFrame(rows)
    expected_rows = len(source) * len(ANCHORS)
    if len(detail) != expected_rows:
        raise RuntimeError(
            f"position/shape detail does not conserve anchors: {len(detail)}/{expected_rows}"
        )
    if detail.duplicated(["operation_key", "anchor_id"]).any():
        raise RuntimeError("position/shape detail contains duplicate operation anchors")
    return detail.sort_values(
        ["stock_id", "entry_date", "anchor_order"], kind="mergesort"
    ).reset_index(drop=True)


def _performance_metrics(part: pd.DataFrame) -> dict[str, object]:
    realized = pd.to_numeric(part["realized_return_pct"], errors="coerce")
    outcomes = part["return_outcome"].astype(str)
    count = len(part)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    failures = int(outcomes.eq("failure").sum())
    ge20 = int(realized.ge(20.0).sum())
    le_minus20 = int(realized.le(-20.0).sum())
    return {
        "operation_count": count,
        "unique_stock_count": int(part["stock_id"].nunique()),
        "unique_episode_count": int(part["episode_key"].nunique()),
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failures,
        "win_rate_pct": _rate(wins, count),
        "neutral_rate_pct": _rate(neutral, count),
        "failure_rate_pct": _rate(failures, count),
        "avg_return_pct": _metric(realized, "mean"),
        "median_return_pct": _metric(realized, "median"),
        "p10_return_pct": _metric(realized, "p10"),
        "p90_return_pct": _metric(realized, "p90"),
        "min_return_pct": _metric(realized, "min"),
        "max_return_pct": _metric(realized, "max"),
        "return_ge20_count": ge20,
        "return_ge20_rate_pct": _rate(ge20, count),
        "return_le_minus20_count": le_minus20,
        "return_le_minus20_rate_pct": _rate(le_minus20, count),
        "top1_abs_return_share_pct": _top_abs_share(realized, 1),
        "top5_abs_return_share_pct": _top_abs_share(realized, 5),
        "avg_latest_source_to_trigger_trading_days": _metric(
            part["latest_source_to_trigger_trading_days"], "mean"
        ),
        "median_latest_source_to_trigger_trading_days": _metric(
            part["latest_source_to_trigger_trading_days"], "median"
        ),
        "avg_first_source_to_trigger_trading_days": _metric(
            part["first_source_to_trigger_trading_days"], "mean"
        ),
        "median_first_source_to_trigger_trading_days": _metric(
            part["first_source_to_trigger_trading_days"], "median"
        ),
        "avg_source_to_preweek_trading_days": _metric(
            part["source_to_preweek_trading_days"], "mean"
        ),
        "median_source_to_preweek_trading_days": _metric(
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


def _analysis_parts(detail: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        PRIMARY_ANALYSIS_BASIS: detail.copy(),
        SENSITIVITY_ANALYSIS_BASIS: detail.loc[
            _boolish(detail["sensitivity_included"])
        ].copy(),
    }


def _build_cell_summary(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    cell_specs: list[tuple[int, str, str, str]] = []
    cell_order = 0
    for position_order, position_bucket in POSITION_BUCKETS:
        for shape_order, shape_bucket in SHAPE_BUCKETS:
            cell_order += 1
            cell_specs.append(
                (
                    position_order * 100 + shape_order,
                    position_bucket,
                    shape_bucket,
                    f"{position_bucket}__{shape_bucket}",
                )
            )
    cell_specs.append((9999, "insufficient_history", "insufficient_history", "insufficient_history"))
    anchor_lookup = {anchor_id: (order, rule, definition) for order, anchor_id, rule, definition in ANCHORS}
    for analysis_basis, basis_detail in _analysis_parts(detail).items():
        for anchor_id in ANCHOR_IDS:
            anchor = basis_detail.loc[basis_detail["anchor_id"].eq(anchor_id)].copy()
            anchor_order, anchor_rule, anchor_definition = anchor_lookup[anchor_id]
            observed_count = int(_boolish(anchor["classification_observed"]).sum())
            for order, position_bucket, shape_bucket, cell_id in cell_specs:
                part = anchor.loc[anchor["position_shape_cell_id"].eq(cell_id)].copy()
                common = detail.iloc[0]
                rows.append(
                    {
                        "generated_at": str(common["generated_at"]),
                        "model_id": MODEL_ID,
                        "artifact_id": ARTIFACT_ID,
                        "artifact_version": ARTIFACT_VERSION,
                        "source_operation_lag_artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
                        "source_operation_lag_artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
                        "source_operation_lag_detail_sha256": str(
                            common["source_operation_lag_detail_sha256"]
                        ),
                        "source_operation_lag_semantic_sha256": str(
                            common["source_operation_lag_semantic_sha256"]
                        ),
                        "source_rearmed_detail_sha256": str(
                            common["source_rearmed_detail_sha256"]
                        ),
                        "source_rearmed_semantic_sha256": str(
                            common["source_rearmed_semantic_sha256"]
                        ),
                        "source_variant_id": SOURCE_VARIANT_ID,
                        "grid_id": ADOPTED_GRID_ID,
                        "analysis_basis": analysis_basis,
                        "anchor_order": anchor_order,
                        "anchor_id": anchor_id,
                        "anchor_date_rule": anchor_rule,
                        "anchor_definition": anchor_definition,
                        "cell_order": order,
                        "position_bucket": position_bucket,
                        "shape_bucket": shape_bucket,
                        "position_shape_cell_id": cell_id,
                        "analysis_basis_operation_count": int(
                            basis_detail["operation_key"].nunique()
                        ),
                        "anchor_classification_observed_count": observed_count,
                        "anchor_classification_coverage_pct": _rate(observed_count, len(anchor)),
                        "cell_share_of_anchor_pct": _rate(len(part), len(anchor)),
                        **_performance_metrics(part),
                        "same_stock_overlap_pair_count": 0,
                        "position_policy": POSITION_POLICY,
                        "shape_policy": SHAPE_POLICY,
                        "price_basis": "adjusted_analysis_ohlc_only",
                        "price_history_cutoff_date": PRICE_HISTORY_CUTOFF_DATE,
                        "condition_role": "research_stratification_not_model_gate",
                        "sample_policy": SAMPLE_POLICY,
                        "anomaly_policy": ANOMALY_POLICY,
                        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                        "approved_for_daily": False,
                        "presentation_allowed": False,
                        "formal_model_use_allowed": False,
                        "production_change": False,
                        "promotion_readiness": "research_only_not_promotion_evidence",
                    }
                )
            classified = sum(
                int(anchor["position_shape_cell_id"].eq(spec[3]).sum()) for spec in cell_specs
            )
            if classified != len(anchor):
                raise RuntimeError(
                    f"position/shape cells do not conserve operations: "
                    f"{analysis_basis}/{anchor_id}/{classified}/{len(anchor)}"
                )
    return pd.DataFrame(rows).sort_values(
        ["analysis_basis", "anchor_order", "cell_order"], kind="mergesort"
    ).reset_index(drop=True)


def _operation_transitions(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for operation_key, group in detail.groupby("operation_key", sort=False):
        by_anchor = group.set_index("anchor_id", drop=False)
        if set(by_anchor.index) != set(ANCHOR_IDS) or len(by_anchor) != len(ANCHOR_IDS):
            raise RuntimeError(f"position/shape transition anchors are incomplete: {operation_key}")
        first = by_anchor.loc["revenue_available"]
        row = {
            "operation_key": operation_key,
            "episode_key": str(first["episode_key"]),
            "stock_id": str(first["stock_id"]),
            "stock_name": str(first["stock_name"]),
            "trigger_date": str(first["trigger_date"]),
            "confirmation_date": str(first["confirmation_date"]),
            "entry_date": str(first["entry_date"]),
            "exit_date": str(first["exit_date"]),
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
            "comparison_sequence_semantics": str(first["comparison_sequence_semantics"]),
            "source_anomaly_candidate_flag": first["source_anomaly_candidate_flag"],
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
            anchor = by_anchor.loc[anchor_id]
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


def _transition_summary_row(
    *,
    detail: pd.DataFrame,
    analysis_basis: str,
    row_type: str,
    part: pd.DataFrame,
    chronology_id: str,
    comparison_semantics: str,
    position_transition_id: str,
    shape_transition_id: str,
    position_shape_transition_id: str,
) -> dict[str, object]:
    common = detail.iloc[0]
    first = (
        part.iloc[0]
        if not part.empty and row_type != "overall_state_comparison"
        else None
    )
    row: dict[str, object] = {
        "generated_at": str(common["generated_at"]),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_operation_lag_artifact_id": SOURCE_OPERATION_LAG_ARTIFACT_ID,
        "source_operation_lag_artifact_version": SOURCE_OPERATION_LAG_ARTIFACT_VERSION,
        "source_operation_lag_detail_sha256": str(
            common["source_operation_lag_detail_sha256"]
        ),
        "source_operation_lag_semantic_sha256": str(
            common["source_operation_lag_semantic_sha256"]
        ),
        "source_rearmed_detail_sha256": str(common["source_rearmed_detail_sha256"]),
        "source_rearmed_semantic_sha256": str(
            common["source_rearmed_semantic_sha256"]
        ),
        "source_variant_id": SOURCE_VARIANT_ID,
        "grid_id": ADOPTED_GRID_ID,
        "analysis_basis": analysis_basis,
        "row_type": row_type,
        "anchor_chronology_id": chronology_id,
        "comparison_sequence_semantics": comparison_semantics,
        "position_transition_id": position_transition_id,
        "shape_transition_id": shape_transition_id,
        "position_shape_transition_id": position_shape_transition_id,
    }
    for anchor_id in ANCHOR_IDS:
        row[f"{anchor_id}_position_bucket"] = (
            str(first[f"{anchor_id}_position_bucket"]) if first is not None else "all"
        )
        row[f"{anchor_id}_shape_bucket"] = (
            str(first[f"{anchor_id}_shape_bucket"]) if first is not None else "all"
        )
        row[f"{anchor_id}_cell_id"] = (
            str(first[f"{anchor_id}_cell_id"]) if first is not None else "all"
        )
    full_observed = int(_boolish(part["full_three_anchor_observed"]).sum())
    row.update(
        {
            "full_three_anchor_observed_count": full_observed,
            "full_three_anchor_observed_rate_pct": _rate(full_observed, len(part)),
            **_performance_metrics(part),
            "same_stock_overlap_pair_count": 0,
            "position_policy": POSITION_POLICY,
            "shape_policy": SHAPE_POLICY,
            "price_basis": "adjusted_analysis_ohlc_only",
            "price_history_cutoff_date": PRICE_HISTORY_CUTOFF_DATE,
            "condition_role": "research_stratification_not_model_gate",
            "sample_policy": SAMPLE_POLICY,
            "anomaly_policy": ANOMALY_POLICY,
            "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
            "approved_for_daily": False,
            "presentation_allowed": False,
            "formal_model_use_allowed": False,
            "production_change": False,
            "promotion_readiness": "research_only_not_promotion_evidence",
        }
    )
    return row


def _build_transition_summary(detail: pd.DataFrame) -> pd.DataFrame:
    operations = _operation_transitions(detail)
    rows: list[dict[str, object]] = []
    for analysis_basis, part in {
        PRIMARY_ANALYSIS_BASIS: operations.copy(),
        SENSITIVITY_ANALYSIS_BASIS: operations.loc[
            _boolish(operations["sensitivity_included"])
        ].copy(),
    }.items():
        rows.append(
            _transition_summary_row(
                detail=detail,
                analysis_basis=analysis_basis,
                row_type="overall_state_comparison",
                part=part,
                chronology_id="all",
                comparison_semantics="all_anchor_comparison_sequences",
                position_transition_id="all",
                shape_transition_id="all",
                position_shape_transition_id="all",
            )
        )
        complete = part.loc[_boolish(part["full_three_anchor_observed"])].copy()
        group_columns = [
            "anchor_chronology_id",
            "comparison_sequence_semantics",
            "position_transition_id",
            "shape_transition_id",
            "position_shape_transition_id",
        ]
        detailed_count = 0
        for keys, transition in complete.groupby(group_columns, sort=False, dropna=False):
            row_type = (
                "chronological_transition"
                if str(keys[0]) == "source_before_or_on_preweek"
                else "nonchronological_anchor_state_sequence"
            )
            rows.append(
                _transition_summary_row(
                    detail=detail,
                    analysis_basis=analysis_basis,
                    row_type=row_type,
                    part=transition,
                    chronology_id=str(keys[0]),
                    comparison_semantics=str(keys[1]),
                    position_transition_id=str(keys[2]),
                    shape_transition_id=str(keys[3]),
                    position_shape_transition_id=str(keys[4]),
                )
            )
            detailed_count += len(transition)
        if detailed_count != len(complete):
            raise RuntimeError(
                f"position/shape detailed state sequences do not conserve complete anchors: "
                f"{analysis_basis}/{detailed_count}/{len(complete)}"
            )
    return pd.DataFrame(rows).sort_values(
        ["analysis_basis", "row_type", "operation_count", "position_shape_transition_id"],
        ascending=[True, False, False, True],
        kind="mergesort",
    ).reset_index(drop=True)


def build_position_shape_transition_matrix(
    operation_lag_detail: pd.DataFrame | None = None,
    *,
    operation_lag_detail_path: Path | str | None = None,
    rearmed_detail: pd.DataFrame | None = None,
    rearmed_detail_path: Path | str | None = None,
    price_history_dir: Path | str = PRICE_HISTORY_DIR,
    price_resolution_path: Path | str | None = None,
    daily_by_stock: Mapping[str, pd.DataFrame] | None = None,
    generated_at: str | None = None,
    enforce_pinned_baseline: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if operation_lag_detail is not None and operation_lag_detail_path is not None:
        raise ValueError("supply operation_lag_detail or operation_lag_detail_path, not both")
    source_path = Path(operation_lag_detail_path or SOURCE_OPERATION_LAG_DETAIL_CSV)
    source_sha = ""
    if operation_lag_detail is None:
        operation_lag_detail = _load_operation_lag_detail(source_path)
        source_sha = _sha256(source_path)
    source_versions = set(
        operation_lag_detail["artifact_version"].astype(str).str.strip()
    )
    if len(source_versions) != 1:
        raise RuntimeError("position/shape operation-lag version is not constant")
    source_operation_lag_version = next(iter(source_versions))
    selected_artifact_version, expected_rearmed_artifact_version = (
        versions_for_operation_lag_artifact(source_operation_lag_version)
    )
    v1_baseline = (
        enforce_pinned_baseline
        and source_operation_lag_version == SOURCE_OPERATION_LAG_ARTIFACT_VERSION
    )
    source_semantic_sha = canonical_operation_lag_semantic_sha256(operation_lag_detail)
    if (
        v1_baseline
        and source_semantic_sha != PINNED_OPERATION_LAG_SEMANTIC_SHA256
    ):
        raise RuntimeError(
            f"position/shape source semantic SHA drift: {source_semantic_sha}/"
            f"{PINNED_OPERATION_LAG_SEMANTIC_SHA256}"
        )
    source = _prepare_operation_lag_detail(
        operation_lag_detail,
        enforce_pinned_baseline=v1_baseline,
        expected_artifact_version=source_operation_lag_version,
    )

    if rearmed_detail is not None and rearmed_detail_path is not None:
        raise ValueError("supply rearmed_detail or rearmed_detail_path, not both")
    rearmed_sha = ""
    if rearmed_detail is None:
        lineage_path = Path(rearmed_detail_path or SOURCE_REARMED_DETAIL_CSV)
        rearmed_detail = _load_rearmed_detail(lineage_path)
        rearmed_sha = _sha256(lineage_path)
    rearmed_semantic_sha = canonical_rearmed_semantic_sha256(rearmed_detail)
    if v1_baseline and rearmed_semantic_sha != PINNED_REARMED_SEMANTIC_SHA256:
        raise RuntimeError(
            f"position/shape rearmed semantic SHA drift: {rearmed_semantic_sha}/"
            f"{PINNED_REARMED_SEMANTIC_SHA256}"
        )
    source = _validate_rearmed_lineage(
        source,
        rearmed_detail,
        expected_artifact_version=expected_rearmed_artifact_version,
    )
    if v1_baseline:
        _validate_pinned_baseline(source)

    if daily_by_stock is None:
        daily_by_stock = load_adjusted_daily_by_stock(
            set(source["stock_id"]),
            price_history_dir=price_history_dir,
            price_resolution_path=price_resolution_path,
        )
    generated = generated_at or _now_text()
    detail = _build_detail(
        source,
        daily_by_stock,
        generated_at=generated,
        source_operation_lag_detail_sha256=source_sha,
        source_operation_lag_semantic_sha256=source_semantic_sha,
        source_rearmed_detail_sha256=rearmed_sha,
        source_rearmed_semantic_sha256=rearmed_semantic_sha,
    )
    if v1_baseline:
        expected_coverage = {
            "revenue_available": 462,
            "pre_breakout_week_close": 513,
            "formal_confirmation_close": 551,
        }
        observed = (
            detail.loc[_boolish(detail["classification_observed"])]
            .groupby("anchor_id")["operation_key"]
            .nunique()
            .to_dict()
        )
        if observed != expected_coverage:
            raise RuntimeError(
                f"position/shape pinned anchor coverage drift: {observed}/{expected_coverage}"
            )
    summary = _build_cell_summary(detail)
    transition = _build_transition_summary(detail)
    for frame in (summary, detail, transition):
        frame.loc[:, "artifact_version"] = selected_artifact_version
        frame.loc[:, "source_operation_lag_artifact_version"] = (
            source_operation_lag_version
        )
    detail.loc[:, "source_rearmed_artifact_version"] = (
        expected_rearmed_artifact_version
    )
    return summary, detail, transition


def resolve_output_paths(
    *,
    output_root: Path | str = ROOT,
    output_paths: Mapping[str, Path | str] | None = None,
) -> dict[str, Path]:
    root = Path(output_root)
    resolved = {
        key: root / relative for key, relative in DEFAULT_OUTPUT_RELATIVE_PATHS.items()
    }
    if output_paths:
        unknown = sorted(set(output_paths) - set(resolved))
        if unknown:
            raise ValueError(f"unknown position/shape output path keys: {unknown}")
        for key, path in output_paths.items():
            resolved[key] = Path(path)
    return resolved


def _markdown_table(frame: pd.DataFrame, columns: list[str], limit: int = 30) -> str:
    if frame.empty:
        return "_No rows._"
    view = frame.loc[:, columns].head(limit).astype(str)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for record in view.itertuples(index=False, name=None):
        lines.append("| " + " | ".join(value.replace("|", "/") for value in record) + " |")
    return "\n".join(lines)


def _markdown(summary: pd.DataFrame, transition: pd.DataFrame) -> str:
    primary = summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)]
    coverage = primary.drop_duplicates("anchor_id")
    transitions = transition.loc[
        transition["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & ~transition["row_type"].eq("overall_state_comparison")
    ].sort_values("operation_count", ascending=False, kind="mergesort")
    lines = [
        "# 營收改善但股價尚未反應：三錨點位階與型態轉換矩陣",
        "",
        f"- generated_at: `{summary['generated_at'].iloc[0]}`",
        f"- model_id: `{MODEL_ID}`",
        f"- artifact_version: `{summary['artifact_version'].iloc[0]}`",
        f"- adopted_grid: `{ADOPTED_GRID_ID}`",
        "- 狀態：`research_only`；分類不是正式模型 gate、ranking、PDF 或 promotion evidence。",
        "- 位階：anchor 前 120 個交易日，不含 anchor；低位 <=40%、中位 >40%~75%、高位 >75%。",
        "- 型態：本 revenue 模型自有定義，分盤整、上升、下降、混合／轉折。",
        "- 財報欄位全部排除；本 artifact 僅使用 PIT 月營收來源與 adjusted analysis price。",
        "- `asof_latest_qualifying_trade_date` 可能晚於突破前一週；此時只作標籤順序比較，不宣稱 chronological transition。",
        "- primary 保留 anomaly candidates；候選排除只另列 sensitivity。",
        "",
        "## 三錨點覆蓋",
        "",
        _markdown_table(
            coverage,
            [
                "anchor_id",
                "analysis_basis_operation_count",
                "anchor_classification_observed_count",
                "anchor_classification_coverage_pct",
            ],
            limit=10,
        ),
        "",
        "## 主要錨點狀態序列",
        "",
        _markdown_table(
            transitions,
            [
                "row_type",
                "anchor_chronology_id",
                "comparison_sequence_semantics",
                "position_transition_id",
                "shape_transition_id",
                "operation_count",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "p10_return_pct",
                "p90_return_pct",
                "return_ge20_rate_pct",
            ],
        ),
        "",
    ]
    return "\n".join(lines)


def write_position_shape_transition_matrix(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    transition: pd.DataFrame,
    *,
    output_root: Path | str = ROOT,
    output_paths: Mapping[str, Path | str] | None = None,
) -> dict[str, Path]:
    paths = resolve_output_paths(output_root=output_root, output_paths=output_paths)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(
        paths["summary_latest"], index=False, encoding="utf-8-sig", lineterminator="\n"
    )
    detail.to_csv(
        paths["detail_latest"], index=False, encoding="utf-8-sig", lineterminator="\n"
    )
    transition.to_csv(
        paths["transition_latest"], index=False, encoding="utf-8-sig", lineterminator="\n"
    )
    paths["summary_history"].write_bytes(paths["summary_latest"].read_bytes())
    paths["summary_docs"].write_bytes(paths["summary_latest"].read_bytes())
    paths["transition_history"].write_bytes(paths["transition_latest"].read_bytes())
    paths["transition_docs"].write_bytes(paths["transition_latest"].read_bytes())
    markdown = _markdown(summary, transition)
    paths["markdown_latest"].write_text(markdown, encoding="utf-8", newline="\n")
    paths["markdown_docs"].write_bytes(paths["markdown_latest"].read_bytes())
    return paths


if __name__ == "__main__":
    raise SystemExit(
        "Use scripts/build_revenue_unreacted_range_research.py with the model-owned "
        "position/shape transition stage"
    )
