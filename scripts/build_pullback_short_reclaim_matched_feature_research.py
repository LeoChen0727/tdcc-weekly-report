"""Build frozen same-signal-date feature diagnostics; never a formal strategy."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import fnmatch
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterator

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
from model_research_artifact_guard import (  # noqa: E402
    _dirty_snapshot,
    changed_during_run,
    load_ownership_rules,
    load_protected_sentinels,
    validate_changed_paths,
)


ROOT = SCRIPT_DIR.parent
MODEL_ID = "pullback_short_reclaim"
OWNER_ID = "pullback_short_reclaim_matched_feature_research"
VERSION = OWNER_ID + "_v1"
PRODUCER = "scripts/build_pullback_short_reclaim_matched_feature_research.py"
VALIDATOR = "scripts/validate_pullback_short_reclaim_matched_feature_research.py"
SOURCE_COMMIT = "f4e71df3ffcf2982bcc1dc6972599717d461d082"
SOURCE_PREFIX = (
    "output/research/pullback_short_reclaim/"
    "pullback_short_reclaim_23ema_condition_comparison_v1_"
)
SOURCE_ARTIFACTS = {
    "detail": {
        "path": SOURCE_PREFIX + "detail.csv",
        "raw_sha256": "34a3a327a980b1caba4aa54f510f80cfb40a48034e9268cff5de804e653144e4",
    },
    "manifest": {
        "path": SOURCE_PREFIX + "manifest.json",
        "raw_sha256": "82936597ae0e8e61c45aac92aa6049a10c35eecc2a30a31d3116600dd7f247f9",
    },
}
OUTPUT_PREFIX = (
    "output/research/pullback_short_reclaim/"
    "pullback_short_reclaim_matched_feature_research_v1_"
)
OUTPUTS = {
    "metrics": OUTPUT_PREFIX + "metrics.csv",
    "features": OUTPUT_PREFIX + "features.csv",
    "audit": OUTPUT_PREFIX + "audit.csv",
    "manifest": OUTPUT_PREFIX + "manifest.json",
}
HORIZONS = (5, 10, 20)
OUTCOME_BANDS = ("high_ge10", "middle_0_to_lt10", "loss_lt0")
FEATURES = {
    "return_20d": "feature_return_20d",
    "rsi14": "feature_price_pullback_rsi14",
    "macd_hist": "feature_price_pullback_macd_hist",
    "model_score": "model_score",
}
FEATURE_ROW_TYPES = (
    "period_event_equal_outcome_band",
    "signal_date_outcome_band",
    "signal_date_high_loss_contrast",
    "period_date_equal_high_loss_contrast",
)
AUDIT_TYPES = (
    "source_identity_summary",
    "source_duplicate_identity",
    "period_concentration",
    "period_stock_interval_overlap",
    "review_candidate_union_contribution",
    "review_candidate_event",
)
METRICS_COLUMNS = (
    "artifact_version",
    "model_id",
    "period",
    "horizon",
    "metric_basis",
    "return_cost_basis",
    "aggregation_basis",
    "signal_count",
    "mature_count",
    "immature_count",
    "unique_stock_count",
    "signal_date_count",
    "win_count",
    "win_rate_pct",
    "neutral_count",
    "neutral_rate_pct",
    "failure_count",
    "failure_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "high_return_ge10_count",
    "high_return_ge10_rate_pct",
    "loss_count",
    "loss_rate_pct",
    "tail_loss_le_minus10_count",
    "tail_loss_le_minus10_rate_pct",
    "source_anomaly_candidate_count",
    "comparison_anomaly_candidate_count",
    "union_review_candidate_event_count",
    "primary_retains_unresolved_candidates",
    "sensitivity_is_corrected_primary",
    "first_publication_pit_proven",
    "first_publication_pit_status",
    "total_return_complete",
    "formal_use_allowed",
    "trade_eligible",
    "promotion_evidence_allowed",
    "operation_contract_status",
)
FEATURES_COLUMNS = (
    "artifact_version",
    "model_id",
    "period",
    "signal_date",
    "horizon",
    "feature_id",
    "source_field",
    "row_type",
    "outcome_band",
    "aggregation_basis",
    "population_count",
    "value_count",
    "missing_value_count",
    "q1",
    "median",
    "q3",
    "iqr",
    "high_value_count",
    "loss_value_count",
    "high_median",
    "loss_median",
    "high_minus_loss_median",
    "paired_signal_date_count",
    "paired_status",
    "positive_difference_count",
    "zero_difference_count",
    "negative_difference_count",
    "positive_difference_rate_pct",
    "negative_difference_rate_pct",
    "feature_scale_note",
    "primary_retains_unresolved_candidates",
    "first_publication_pit_proven",
    "formal_use_allowed",
    "promotion_evidence_allowed",
)
AUDIT_COLUMNS = (
    "artifact_version",
    "model_id",
    "period",
    "horizon",
    "audit_type",
    "audit_key",
    "signal_date",
    "stock_id",
    "signal_event_id",
    "report_line",
    "identity_disposition",
    "source_duplicate_count",
    "entry_date",
    "exit_date",
    "maturity_status",
    "return_pct",
    "signal_count",
    "mature_count",
    "unique_stock_count",
    "signal_date_count",
    "largest_signal_date",
    "largest_signal_date_count",
    "largest_signal_date_share_pct",
    "repeated_stock_count",
    "repeated_stock_signal_count",
    "overlap_pair_count",
    "overlap_stock_count",
    "overlap_eligible_event_count",
    "overlap_not_assessed_event_count",
    "boundary_touch_pair_count",
    "overlap_interval_basis",
    "overlap_interpretation",
    "source_row_count",
    "canonical_signal_event_count",
    "source_duplicate_group_count",
    "source_duplicate_extra_row_count",
    "canonical_same_stock_signal_date_group_count",
    "canonical_same_stock_signal_date_event_count",
    "canonical_same_stock_signal_date_cross_report_line_group_count",
    "review_candidate_union_event_count",
    "review_candidate_mature_count",
    "review_candidate_return_sum_pct",
    "review_candidate_average_point_contribution_pct",
    "primary_return_sum_pct",
    "review_candidate_share_of_primary_return_sum_pct",
    "primary_average_return_pct",
    "candidate_exclusion_sensitivity_average_return_pct",
    "candidate_exclusion_sensitivity_delta_pct",
    "review_candidate_disposition",
    "review_candidate_reason",
    "audit_status",
    "primary_retains_unresolved_candidates",
    "sensitivity_is_corrected_primary",
    "first_publication_pit_proven",
    "formal_use_allowed",
    "promotion_evidence_allowed",
    "operation_contract_status",
)
SOURCE_REQUIRED_COLUMNS = {
    "signal_event_id",
    "signal_date",
    "stock_id",
    "report_line",
    "model_score",
    "entry_date",
    "primary_metric_included",
    "formal_use_allowed",
    "trade_eligible",
    "promotion_evidence_allowed",
    "first_publication_pit_proven",
    "total_return_complete",
    "price_source_immutability_status",
    "trading_calendar_status",
    "return_cost_basis",
    "identity_disposition",
    "source_duplicate_count",
    "source_duplicate_ordinal",
    *FEATURES.values(),
    *(
        f"d{horizon}_{suffix}"
        for horizon in HORIZONS
        for suffix in (
            "maturity_status",
            "exit_date",
            "return_pct",
            "outcome",
            "anomaly_candidate",
            "comparison_anomaly_candidate",
            "comparison_anomaly_disposition",
            "comparison_anomaly_reason",
        )
    ),
}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _git(root: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        raise RuntimeError(completed.stderr.decode("utf-8", errors="replace").strip())
    return completed.stdout


def read_git_blob(
    root: Path,
    commit: str,
    path: str,
    expected_sha256: str,
) -> bytes:
    payload = _git(root, "show", f"{commit}:{path}")
    observed = sha256(payload)
    if observed != expected_sha256:
        raise RuntimeError(
            f"fixed source raw SHA-256 mismatch: {path} observed={observed} "
            f"expected={expected_sha256}"
        )
    return payload


def _text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    return str(value).strip()


def _fmt(value: float | None) -> str:
    if value is None or not math.isfinite(value):
        return ""
    return f"{value:.6f}"


def _pct(numerator: int, denominator: int) -> str:
    return _fmt(numerator / denominator * 100.0) if denominator else ""


def _numeric_values(frame: pd.DataFrame, field: str) -> pd.Series:
    raw = frame[field].map(_text)
    present = raw[raw.ne("")]
    values = pd.to_numeric(present, errors="raise").astype(float)
    if not all(math.isfinite(value) for value in values):
        raise RuntimeError(f"non-finite numeric feature: {field}")
    return values


def _distribution(values: pd.Series | list[float]) -> dict[str, str]:
    series = pd.Series(values, dtype=float)
    if series.empty:
        return {"q1": "", "median": "", "q3": "", "iqr": ""}
    q1 = float(series.quantile(0.25, interpolation="linear"))
    median = float(series.quantile(0.5, interpolation="linear"))
    q3 = float(series.quantile(0.75, interpolation="linear"))
    return {
        "q1": _fmt(q1),
        "median": _fmt(median),
        "q3": _fmt(q3),
        "iqr": _fmt(q3 - q1),
    }


def _periods(frame: pd.DataFrame) -> list[str]:
    return ["all", *sorted(frame["signal_date"].str[:6].unique())]


def _period_frame(frame: pd.DataFrame, period: str) -> pd.DataFrame:
    return frame if period == "all" else frame[frame["signal_date"].str.startswith(period)]


def _band_mask(returns: pd.Series, band: str) -> pd.Series:
    if band == "high_ge10":
        return returns.ge(10)
    if band == "middle_0_to_lt10":
        return returns.ge(0) & returns.lt(10)
    if band == "loss_lt0":
        return returns.lt(0)
    raise RuntimeError(f"unknown outcome band: {band}")


def _feature_scale_note(feature_id: str) -> str:
    if feature_id == "macd_hist":
        return "raw_macd_hist_scale_differs_by_stock_no_cross_stock_threshold_or_recommendation"
    return "continuous_published_snapshot_value_descriptive_only"


def load_source(root: Path = ROOT) -> tuple[pd.DataFrame, dict[str, Any]]:
    root = Path(root)
    payloads = {
        key: read_git_blob(root, SOURCE_COMMIT, spec["path"], spec["raw_sha256"])
        for key, spec in SOURCE_ARTIFACTS.items()
    }
    try:
        source_manifest = json.loads(payloads["manifest"].decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("fixed source manifest is not valid UTF-8 JSON") from exc
    if source_manifest.get("artifact_version") != (
        "pullback_short_reclaim_23ema_condition_comparison_v1"
    ):
        raise RuntimeError("fixed source manifest artifact_version mismatch")
    if source_manifest.get("model_id") != MODEL_ID:
        raise RuntimeError("fixed source manifest model_id mismatch")
    if source_manifest.get("output_sha256", {}).get(
        SOURCE_ARTIFACTS["detail"]["path"]
    ) != SOURCE_ARTIFACTS["detail"]["raw_sha256"]:
        raise RuntimeError("fixed source manifest detail SHA binding mismatch")
    if source_manifest.get("return_cost_basis") != (
        "original_before_costs_slippage_and_tax"
    ):
        raise RuntimeError("fixed source manifest return cost basis mismatch")
    for field in (
        "first_publication_pit_proven",
        "formal_use_allowed",
        "promotion_evidence_allowed",
        "total_return_complete",
        "non_overlapping_trades_proven",
    ):
        if source_manifest.get(field) is not False:
            raise RuntimeError(f"fixed source manifest {field} must remain false")

    detail = pd.read_csv(
        io.BytesIO(payloads["detail"]),
        dtype=str,
        keep_default_na=False,
    )
    missing = sorted(SOURCE_REQUIRED_COLUMNS - set(detail.columns))
    if missing:
        raise RuntimeError(f"fixed source detail missing required columns: {missing}")
    if len(detail) != 3020:
        raise RuntimeError("fixed source detail row count mismatch")
    if set(detail["model_id"].map(_text)) != {MODEL_ID}:
        raise RuntimeError("fixed source detail contains another model")
    canonical = detail[detail["primary_metric_included"].eq("True")].copy()
    if len(canonical) != 2992 or canonical["signal_event_id"].nunique() != 2992:
        raise RuntimeError("fixed source canonical event population mismatch")
    if canonical["signal_event_id"].duplicated().any():
        raise RuntimeError("fixed source canonical signal_event_id must be unique")
    if canonical["signal_date"].map(
        lambda value: bool(re.fullmatch(r"\d{8}", value))
    ).eq(False).any():
        raise RuntimeError("fixed source contains invalid signal_date")
    for field in (
        "formal_use_allowed",
        "trade_eligible",
        "promotion_evidence_allowed",
        "first_publication_pit_proven",
        "total_return_complete",
    ):
        if set(canonical[field].map(_text)) != {"False"}:
            raise RuntimeError(f"fixed source {field} must remain false")
    if set(canonical["return_cost_basis"].map(_text)) != {
        "raw_return_before_costs_slippage_and_tax"
    }:
        raise RuntimeError("fixed source detail return cost basis mismatch")
    if set(canonical["identity_disposition"].map(_text)) != {
        "canonical_signal_event"
    }:
        raise RuntimeError("fixed source canonical identity disposition mismatch")
    duplicate_counts = pd.to_numeric(
        canonical["source_duplicate_count"], errors="raise"
    ).astype(int)
    duplicate_ordinals = pd.to_numeric(
        canonical["source_duplicate_ordinal"], errors="raise"
    ).astype(int)
    if not duplicate_counts.isin((1, 2)).all() or not duplicate_ordinals.eq(1).all():
        raise RuntimeError("fixed source duplicate identity lineage mismatch")
    if int(duplicate_counts.gt(1).sum()) != 28 or int(
        (duplicate_counts - 1).sum()
    ) != 28:
        raise RuntimeError("fixed source duplicate lineage count mismatch")
    if set(canonical["price_source_immutability_status"].map(_text)) != {
        "mutable_current_file_unpinned"
    }:
        raise RuntimeError("fixed source price lineage disclosure mismatch")
    if set(canonical["trading_calendar_status"].map(_text)) != {
        "stock_price_row_sequence_only_no_market_calendar_proof"
    }:
        raise RuntimeError("fixed source trading-calendar disclosure mismatch")
    union_mask = pd.Series(False, index=canonical.index)
    for horizon in HORIZONS:
        union_mask |= canonical[f"d{horizon}_comparison_anomaly_candidate"].eq("True")
    if int(union_mask.sum()) != 8:
        raise RuntimeError("fixed source review-candidate event union must remain exactly 8")
    for horizon in HORIZONS:
        prefix = f"d{horizon}"
        candidate_mask = canonical[prefix + "_comparison_anomaly_candidate"].eq("True")
        if set(
            canonical.loc[
                candidate_mask,
                prefix + "_comparison_anomaly_disposition",
            ].map(_text)
        ) != {"unresolved_anomaly_candidate"}:
            raise RuntimeError(
                f"fixed source D{horizon} review candidates must remain unresolved"
            )
        if set(
            canonical.loc[
                ~candidate_mask,
                prefix + "_comparison_anomaly_disposition",
            ].map(_text)
        ) != {"not_flagged_by_this_review"}:
            raise RuntimeError(
                f"fixed source D{horizon} non-candidate disposition mismatch"
            )
        mature = canonical[canonical[prefix + "_maturity_status"].eq("mature")]
        returns = pd.to_numeric(
            mature[prefix + "_return_pct"], errors="raise"
        ).astype(float)
        if not all(math.isfinite(value) for value in returns):
            raise RuntimeError(f"fixed source D{horizon} mature return is non-finite")
    return canonical.reset_index(drop=True), source_manifest


def review_candidate_ids(canonical: pd.DataFrame) -> set[str]:
    mask = pd.Series(False, index=canonical.index)
    for horizon in HORIZONS:
        mask |= canonical[f"d{horizon}_comparison_anomaly_candidate"].eq("True")
    result = set(canonical.loc[mask, "signal_event_id"].map(_text))
    if len(result) != 8:
        raise RuntimeError("review-candidate event union must remain exactly 8")
    return result


def build_metrics(canonical: pd.DataFrame) -> pd.DataFrame:
    union_ids = review_candidate_ids(canonical)
    rows: list[dict[str, Any]] = []
    for period in _periods(canonical):
        population = _period_frame(canonical, period)
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            mature = population[population[prefix + "_maturity_status"].eq("mature")]
            returns = pd.to_numeric(
                mature[prefix + "_return_pct"], errors="raise"
            ).astype(float)
            count = len(mature)
            wins = int(returns.gt(0).sum())
            neutral = int(returns.eq(0).sum())
            failure = int(returns.lt(0).sum())
            high = int(returns.ge(10).sum())
            loss = failure
            tail = int(returns.le(-10).sum())
            rows.append(
                {
                    "artifact_version": VERSION,
                    "model_id": MODEL_ID,
                    "period": period,
                    "horizon": horizon,
                    "metric_basis": "raw_primary_including_unresolved",
                    "return_cost_basis": "raw_return_before_costs_slippage_and_tax",
                    "aggregation_basis": "unique_signal_event_equal_weight",
                    "signal_count": len(population),
                    "mature_count": count,
                    "immature_count": len(population) - count,
                    "unique_stock_count": mature["stock_id"].nunique(),
                    "signal_date_count": mature["signal_date"].nunique(),
                    "win_count": wins,
                    "win_rate_pct": _pct(wins, count),
                    "neutral_count": neutral,
                    "neutral_rate_pct": _pct(neutral, count),
                    "failure_count": failure,
                    "failure_rate_pct": _pct(failure, count),
                    "average_return_pct": _fmt(float(returns.mean())) if count else "",
                    "median_return_pct": _fmt(float(returns.median())) if count else "",
                    "high_return_ge10_count": high,
                    "high_return_ge10_rate_pct": _pct(high, count),
                    "loss_count": loss,
                    "loss_rate_pct": _pct(loss, count),
                    "tail_loss_le_minus10_count": tail,
                    "tail_loss_le_minus10_rate_pct": _pct(tail, count),
                    "source_anomaly_candidate_count": int(
                        mature[prefix + "_anomaly_candidate"].eq("True").sum()
                    ),
                    "comparison_anomaly_candidate_count": int(
                        mature[prefix + "_comparison_anomaly_candidate"].eq("True").sum()
                    ),
                    "union_review_candidate_event_count": int(
                        population["signal_event_id"].isin(union_ids).sum()
                    ),
                    "primary_retains_unresolved_candidates": "True",
                    "sensitivity_is_corrected_primary": "False",
                    "first_publication_pit_proven": "False",
                    "first_publication_pit_status": "unknown_not_proven",
                    "total_return_complete": "False",
                    "formal_use_allowed": "False",
                    "trade_eligible": "False",
                    "promotion_evidence_allowed": "False",
                    "operation_contract_status": "decision_required",
                }
            )
    return pd.DataFrame(rows, columns=METRICS_COLUMNS)


def _feature_base(
    *,
    period: str,
    signal_date: str,
    horizon: int,
    feature_id: str,
    row_type: str,
    outcome_band: str,
    aggregation_basis: str,
) -> dict[str, Any]:
    row = {column: "" for column in FEATURES_COLUMNS}
    row.update(
        {
            "artifact_version": VERSION,
            "model_id": MODEL_ID,
            "period": period,
            "signal_date": signal_date,
            "horizon": horizon,
            "feature_id": feature_id,
            "source_field": FEATURES[feature_id],
            "row_type": row_type,
            "outcome_band": outcome_band,
            "aggregation_basis": aggregation_basis,
            "feature_scale_note": _feature_scale_note(feature_id),
            "primary_retains_unresolved_candidates": "True",
            "first_publication_pit_proven": "False",
            "formal_use_allowed": "False",
            "promotion_evidence_allowed": "False",
        }
    )
    return row


def _band_feature_row(
    frame: pd.DataFrame,
    returns: pd.Series,
    *,
    period: str,
    signal_date: str,
    horizon: int,
    feature_id: str,
    band: str,
    row_type: str,
    aggregation_basis: str,
) -> dict[str, Any]:
    band_rows = frame.loc[_band_mask(returns, band)]
    values = _numeric_values(band_rows, FEATURES[feature_id])
    row = _feature_base(
        period=period,
        signal_date=signal_date,
        horizon=horizon,
        feature_id=feature_id,
        row_type=row_type,
        outcome_band=band,
        aggregation_basis=aggregation_basis,
    )
    row.update(
        {
            "population_count": len(band_rows),
            "value_count": len(values),
            "missing_value_count": len(band_rows) - len(values),
            **_distribution(values),
            "paired_status": "not_applicable",
        }
    )
    return row


def _date_contrast_row(
    frame: pd.DataFrame,
    returns: pd.Series,
    *,
    period: str,
    signal_date: str,
    horizon: int,
    feature_id: str,
) -> tuple[dict[str, Any], float | None]:
    high_rows = frame.loc[_band_mask(returns, "high_ge10")]
    loss_rows = frame.loc[_band_mask(returns, "loss_lt0")]
    high_values = _numeric_values(high_rows, FEATURES[feature_id])
    loss_values = _numeric_values(loss_rows, FEATURES[feature_id])
    high_median = float(high_values.median()) if len(high_values) else None
    loss_median = float(loss_values.median()) if len(loss_values) else None
    delta = (
        high_median - loss_median
        if high_median is not None and loss_median is not None
        else None
    )
    if high_median is None and loss_median is None:
        status = "missing_high_and_loss_values"
    elif high_median is None:
        status = "missing_high_values"
    elif loss_median is None:
        status = "missing_loss_values"
    else:
        status = "paired_both_bands_present"
    row = _feature_base(
        period=period,
        signal_date=signal_date,
        horizon=horizon,
        feature_id=feature_id,
        row_type="signal_date_high_loss_contrast",
        outcome_band="high_ge10_minus_loss_lt0",
        aggregation_basis="within_signal_date_median_difference",
    )
    row.update(
        {
            "population_count": len(frame),
            "high_value_count": len(high_values),
            "loss_value_count": len(loss_values),
            "high_median": _fmt(high_median),
            "loss_median": _fmt(loss_median),
            "high_minus_loss_median": _fmt(delta),
            "paired_signal_date_count": 1 if delta is not None else 0,
            "paired_status": status,
            "positive_difference_count": int(delta is not None and delta > 0),
            "zero_difference_count": int(delta is not None and delta == 0),
            "negative_difference_count": int(delta is not None and delta < 0),
            "positive_difference_rate_pct": (
                _fmt(100.0 if delta > 0 else 0.0) if delta is not None else ""
            ),
            "negative_difference_rate_pct": (
                _fmt(100.0 if delta < 0 else 0.0) if delta is not None else ""
            ),
        }
    )
    return row, delta


def build_features(canonical: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    periods = _periods(canonical)
    for period in periods:
        population = _period_frame(canonical, period)
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            mature = population[population[prefix + "_maturity_status"].eq("mature")]
            returns = pd.to_numeric(mature[prefix + "_return_pct"], errors="raise").astype(float)
            for feature_id in FEATURES:
                for band in OUTCOME_BANDS:
                    rows.append(
                        _band_feature_row(
                            mature,
                            returns,
                            period=period,
                            signal_date="",
                            horizon=horizon,
                            feature_id=feature_id,
                            band=band,
                            row_type="period_event_equal_outcome_band",
                            aggregation_basis="event_equal_within_period",
                        )
                    )
                date_deltas: list[float] = []
                paired_high_count = 0
                paired_loss_count = 0
                mature_dates = sorted(mature["signal_date"].unique())
                for signal_date in mature_dates:
                    day = mature[mature["signal_date"].eq(signal_date)]
                    day_returns = pd.to_numeric(
                        day[prefix + "_return_pct"], errors="raise"
                    ).astype(float)
                    _, delta = _date_contrast_row(
                        day,
                        day_returns,
                        period=signal_date[:6],
                        signal_date=signal_date,
                        horizon=horizon,
                        feature_id=feature_id,
                    )
                    if delta is not None:
                        high_values = _numeric_values(
                            day.loc[_band_mask(day_returns, "high_ge10")],
                            FEATURES[feature_id],
                        )
                        loss_values = _numeric_values(
                            day.loc[_band_mask(day_returns, "loss_lt0")],
                            FEATURES[feature_id],
                        )
                        date_deltas.append(delta)
                        paired_high_count += len(high_values)
                        paired_loss_count += len(loss_values)
                distribution = _distribution(date_deltas)
                summary = _feature_base(
                    period=period,
                    signal_date="",
                    horizon=horizon,
                    feature_id=feature_id,
                    row_type="period_date_equal_high_loss_contrast",
                    outcome_band="high_ge10_minus_loss_lt0",
                    aggregation_basis="signal_date_equal_weight_of_paired_date_median_differences",
                )
                summary.update(
                    {
                        "population_count": len(mature),
                        "value_count": len(date_deltas),
                        "missing_value_count": len(mature_dates) - len(date_deltas),
                        **distribution,
                        "high_value_count": paired_high_count,
                        "loss_value_count": paired_loss_count,
                        "high_minus_loss_median": distribution["median"],
                        "paired_signal_date_count": len(date_deltas),
                        "paired_status": (
                            "paired_dates_available"
                            if date_deltas
                            else "no_paired_signal_dates"
                        ),
                        "positive_difference_count": sum(
                            value > 0 for value in date_deltas
                        ),
                        "zero_difference_count": sum(
                            value == 0 for value in date_deltas
                        ),
                        "negative_difference_count": sum(
                            value < 0 for value in date_deltas
                        ),
                        "positive_difference_rate_pct": _pct(
                            sum(value > 0 for value in date_deltas),
                            len(date_deltas),
                        ),
                        "negative_difference_rate_pct": _pct(
                            sum(value < 0 for value in date_deltas),
                            len(date_deltas),
                        ),
                    }
                )
                rows.append(summary)

    for signal_date in sorted(canonical["signal_date"].unique()):
        population = canonical[canonical["signal_date"].eq(signal_date)]
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            mature = population[population[prefix + "_maturity_status"].eq("mature")]
            returns = pd.to_numeric(mature[prefix + "_return_pct"], errors="raise").astype(float)
            for feature_id in FEATURES:
                for band in OUTCOME_BANDS:
                    rows.append(
                        _band_feature_row(
                            mature,
                            returns,
                            period=signal_date[:6],
                            signal_date=signal_date,
                            horizon=horizon,
                            feature_id=feature_id,
                            band=band,
                            row_type="signal_date_outcome_band",
                            aggregation_basis="event_equal_within_signal_date",
                        )
                    )
                contrast, _ = _date_contrast_row(
                    mature,
                    returns,
                    period=signal_date[:6],
                    signal_date=signal_date,
                    horizon=horizon,
                    feature_id=feature_id,
                )
                rows.append(contrast)
    result = pd.DataFrame(rows, columns=FEATURES_COLUMNS)
    return result.sort_values(
        ["row_type", "period", "signal_date", "horizon", "feature_id", "outcome_band"],
        kind="stable",
    ).reset_index(drop=True)


def _audit_base(
    *,
    period: str,
    horizon: int,
    audit_type: str,
    audit_key: str,
) -> dict[str, Any]:
    row = {column: "" for column in AUDIT_COLUMNS}
    row.update(
        {
            "artifact_version": VERSION,
            "model_id": MODEL_ID,
            "period": period,
            "horizon": horizon,
            "audit_type": audit_type,
            "audit_key": audit_key,
            "primary_retains_unresolved_candidates": "True",
            "sensitivity_is_corrected_primary": "False",
            "first_publication_pit_proven": "False",
            "formal_use_allowed": "False",
            "promotion_evidence_allowed": "False",
            "operation_contract_status": "decision_required",
        }
    )
    return row


def _overlap_counts(mature: pd.DataFrame, horizon: int) -> tuple[int, int, int]:
    overlap_pairs = 0
    boundary_touch_pairs = 0
    overlap_stocks: set[str] = set()
    exit_field = f"d{horizon}_exit_date"
    for stock_id, group in mature.groupby("stock_id", sort=True):
        intervals = sorted(
            (
                _text(row["entry_date"]),
                _text(row[exit_field]),
                _text(row["signal_event_id"]),
            )
            for _, row in group.iterrows()
        )
        for entry_date, exit_date, _ in intervals:
            if not re.fullmatch(r"\d{8}", entry_date) or not re.fullmatch(
                r"\d{8}", exit_date
            ):
                raise RuntimeError("mature event has invalid overlap interval date")
            if entry_date > exit_date:
                raise RuntimeError("mature event overlap interval is reversed")
        for index, (left_entry, left_exit, _) in enumerate(intervals):
            for right_entry, right_exit, _ in intervals[index + 1 :]:
                if left_entry <= right_exit and right_entry <= left_exit:
                    overlap_pairs += 1
                    overlap_stocks.add(_text(stock_id))
                    if left_exit == right_entry or right_exit == left_entry:
                        boundary_touch_pairs += 1
    return overlap_pairs, len(overlap_stocks), boundary_touch_pairs


def build_audit(canonical: pd.DataFrame) -> pd.DataFrame:
    union_ids = review_candidate_ids(canonical)
    rows: list[dict[str, Any]] = []
    duplicate_counts = pd.to_numeric(
        canonical["source_duplicate_count"], errors="raise"
    ).astype(int)
    duplicate_events = canonical.loc[duplicate_counts.gt(1)].copy()
    stock_date_sizes = canonical.groupby(["signal_date", "stock_id"], sort=True).size()
    multi_identity_keys = stock_date_sizes[stock_date_sizes.gt(1)].index
    cross_report_line_groups = 0
    for signal_date, stock_id in multi_identity_keys:
        group = canonical[
            canonical["signal_date"].eq(signal_date)
            & canonical["stock_id"].eq(stock_id)
        ]
        if group["report_line"].nunique() > 1:
            cross_report_line_groups += 1

    identity_summary = _audit_base(
        period="all",
        horizon=0,
        audit_type="source_identity_summary",
        audit_key="all|source_identity_summary",
    )
    identity_summary["horizon"] = ""
    identity_summary.update(
        {
            "signal_count": len(canonical),
            "source_row_count": 3020,
            "canonical_signal_event_count": len(canonical),
            "source_duplicate_group_count": len(duplicate_events),
            "source_duplicate_extra_row_count": int((duplicate_counts - 1).sum()),
            "canonical_same_stock_signal_date_group_count": len(multi_identity_keys),
            "canonical_same_stock_signal_date_event_count": int(
                stock_date_sizes[stock_date_sizes.gt(1)].sum()
            ),
            "canonical_same_stock_signal_date_cross_report_line_group_count": (
                cross_report_line_groups
            ),
            "audit_status": (
                "canonical_signal_event_identity_preserved_no_second_dedup_"
                "same_stock_date_cross_report_line_identity_reported"
            ),
        }
    )
    rows.append(identity_summary)
    for _, event in duplicate_events.sort_values(
        ["signal_date", "stock_id", "report_line", "signal_event_id"],
        kind="stable",
    ).iterrows():
        duplicate_row = _audit_base(
            period=_text(event["signal_date"])[:6],
            horizon=0,
            audit_type="source_duplicate_identity",
            audit_key=_text(event["signal_event_id"]),
        )
        duplicate_row["horizon"] = ""
        duplicate_row.update(
            {
                "signal_date": _text(event["signal_date"]),
                "stock_id": _text(event["stock_id"]),
                "signal_event_id": _text(event["signal_event_id"]),
                "report_line": _text(event["report_line"]),
                "identity_disposition": _text(event["identity_disposition"]),
                "source_duplicate_count": _text(event["source_duplicate_count"]),
                "source_duplicate_group_count": 1,
                "source_duplicate_extra_row_count": (
                    int(_text(event["source_duplicate_count"])) - 1
                ),
                "audit_status": (
                    "source_duplicate_identity_already_canonicalized_upstream_"
                    "canonical_event_retained_no_second_dedup"
                ),
            }
        )
        rows.append(duplicate_row)

    for period in _periods(canonical):
        population = _period_frame(canonical, period)
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            mature = population[population[prefix + "_maturity_status"].eq("mature")]
            returns = pd.to_numeric(
                mature[prefix + "_return_pct"], errors="raise"
            ).astype(float)
            date_counts = mature["signal_date"].value_counts()
            if len(date_counts):
                largest_count = int(date_counts.max())
                largest_date = sorted(
                    str(date)
                    for date, count in date_counts.items()
                    if int(count) == largest_count
                )[0]
            else:
                largest_count = 0
                largest_date = ""
            concentration = _audit_base(
                period=period,
                horizon=horizon,
                audit_type="period_concentration",
                audit_key=f"{period}|D{horizon}|concentration",
            )
            concentration.update(
                {
                    "signal_count": len(population),
                    "mature_count": len(mature),
                    "unique_stock_count": mature["stock_id"].nunique(),
                    "signal_date_count": mature["signal_date"].nunique(),
                    "largest_signal_date": largest_date,
                    "largest_signal_date_count": largest_count,
                    "largest_signal_date_share_pct": _pct(largest_count, len(mature)),
                    "review_candidate_union_event_count": int(
                        population["signal_event_id"].isin(union_ids).sum()
                    ),
                    "audit_status": "descriptive_date_concentration_not_oos",
                }
            )
            rows.append(concentration)

            stock_counts = mature["stock_id"].value_counts()
            repeated = stock_counts[stock_counts.gt(1)]
            (
                overlap_pair_count,
                overlap_stock_count,
                boundary_touch_pair_count,
            ) = _overlap_counts(mature, horizon)
            overlap = _audit_base(
                period=period,
                horizon=horizon,
                audit_type="period_stock_interval_overlap",
                audit_key=f"{period}|D{horizon}|stock_interval_overlap",
            )
            overlap.update(
                {
                    "signal_count": len(population),
                    "mature_count": len(mature),
                    "unique_stock_count": mature["stock_id"].nunique(),
                    "signal_date_count": mature["signal_date"].nunique(),
                    "repeated_stock_count": len(repeated),
                    "repeated_stock_signal_count": int(repeated.sum()),
                    "overlap_pair_count": overlap_pair_count,
                    "overlap_stock_count": overlap_stock_count,
                    "overlap_eligible_event_count": len(mature),
                    "overlap_not_assessed_event_count": len(population) - len(mature),
                    "boundary_touch_pair_count": boundary_touch_pair_count,
                    "overlap_interval_basis": (
                        "mature_parseable_entry_to_fixed_horizon_exit_closed_interval"
                    ),
                    "overlap_interpretation": (
                        "conservative_inclusive_date_intersection_not_actual_position_conflict"
                    ),
                    "review_candidate_union_event_count": int(
                        population["signal_event_id"].isin(union_ids).sum()
                    ),
                    "audit_status": (
                        "mature_parseable_intervals_only_immature_unassessed_"
                        "inclusive_boundary_touch_conservative_not_position_conflict_"
                        "market_calendar_unproven_non_overlapping_trades_not_proven"
                    ),
                }
            )
            rows.append(overlap)

            candidates = mature[mature["signal_event_id"].isin(union_ids)]
            candidate_returns = pd.to_numeric(
                candidates[prefix + "_return_pct"], errors="raise"
            ).astype(float)
            sensitivity = mature[~mature["signal_event_id"].isin(union_ids)]
            sensitivity_returns = pd.to_numeric(
                sensitivity[prefix + "_return_pct"], errors="raise"
            ).astype(float)
            primary_sum = float(returns.sum()) if len(returns) else 0.0
            candidate_sum = (
                float(candidate_returns.sum()) if len(candidate_returns) else 0.0
            )
            primary_average = float(returns.mean()) if len(returns) else None
            sensitivity_average = (
                float(sensitivity_returns.mean()) if len(sensitivity_returns) else None
            )
            contribution = _audit_base(
                period=period,
                horizon=horizon,
                audit_type="review_candidate_union_contribution",
                audit_key=f"{period}|D{horizon}|review_candidate_union_contribution",
            )
            contribution.update(
                {
                    "signal_count": len(population),
                    "mature_count": len(mature),
                    "unique_stock_count": mature["stock_id"].nunique(),
                    "signal_date_count": mature["signal_date"].nunique(),
                    "review_candidate_union_event_count": int(
                        population["signal_event_id"].isin(union_ids).sum()
                    ),
                    "review_candidate_mature_count": len(candidates),
                    "review_candidate_return_sum_pct": _fmt(candidate_sum),
                    "review_candidate_average_point_contribution_pct": (
                        _fmt(candidate_sum / len(mature)) if len(mature) else ""
                    ),
                    "primary_return_sum_pct": _fmt(primary_sum),
                    "review_candidate_share_of_primary_return_sum_pct": (
                        _fmt(candidate_sum / primary_sum * 100.0)
                        if not math.isclose(primary_sum, 0.0, abs_tol=1e-12)
                        else ""
                    ),
                    "primary_average_return_pct": _fmt(primary_average),
                    "candidate_exclusion_sensitivity_average_return_pct": _fmt(
                        sensitivity_average
                    ),
                    "candidate_exclusion_sensitivity_delta_pct": (
                        _fmt(sensitivity_average - primary_average)
                        if sensitivity_average is not None and primary_average is not None
                        else ""
                    ),
                    "review_candidate_disposition": (
                        "unresolved_anomaly_candidate_union_retained_in_primary"
                    ),
                    "review_candidate_reason": (
                        "union_of_d5_d10_d20_comparison_anomaly_candidates_retained_in_primary"
                    ),
                    "audit_status": (
                        "candidate_exclusion_is_sensitivity_only_not_corrected_primary"
                    ),
                }
            )
            rows.append(contribution)

    union_events = canonical[canonical["signal_event_id"].isin(union_ids)].sort_values(
        ["signal_date", "stock_id", "signal_event_id"], kind="stable"
    )
    for _, event in union_events.iterrows():
        for horizon in HORIZONS:
            prefix = f"d{horizon}"
            candidate_at_horizon = _text(
                event[prefix + "_comparison_anomaly_candidate"]
            ) == "True"
            event_row = _audit_base(
                period=_text(event["signal_date"])[:6],
                horizon=horizon,
                audit_type="review_candidate_event",
                audit_key=f"{event['signal_event_id']}|D{horizon}",
            )
            event_row.update(
                {
                    "signal_date": _text(event["signal_date"]),
                    "stock_id": _text(event["stock_id"]),
                    "signal_event_id": _text(event["signal_event_id"]),
                    "report_line": _text(event["report_line"]),
                    "identity_disposition": _text(event["identity_disposition"]),
                    "source_duplicate_count": _text(event["source_duplicate_count"]),
                    "entry_date": _text(event["entry_date"]),
                    "exit_date": _text(event[prefix + "_exit_date"]),
                    "maturity_status": _text(event[prefix + "_maturity_status"]),
                    "return_pct": _text(event[prefix + "_return_pct"]),
                    "review_candidate_union_event_count": 8,
                    "review_candidate_reason": (
                        _text(event[prefix + "_comparison_anomaly_reason"])
                        if candidate_at_horizon
                        else "union_candidate_triggered_at_another_horizon"
                    ),
                    "review_candidate_disposition": (
                        _text(event[prefix + "_comparison_anomaly_disposition"])
                        if candidate_at_horizon
                        else "union_candidate_triggered_at_another_horizon"
                    ),
                    "audit_status": (
                        "retained_primary_review_candidate_event"
                        if _text(event[prefix + "_maturity_status"]) == "mature"
                        else "retained_primary_union_event_not_mature_for_horizon"
                    ),
                }
            )
            rows.append(event_row)
    return pd.DataFrame(rows, columns=AUDIT_COLUMNS)


def _snapshot_coverage(source_manifest: dict[str, Any]) -> dict[str, Any]:
    coverage: dict[str, dict[str, list[str]]] = {}
    for receipt in source_manifest.get("snapshots", []):
        match = re.search(r"(\d{8})", _text(receipt.get("path")))
        if not match:
            raise RuntimeError("fixed source manifest snapshot date is missing")
        signal_date = match.group(1)
        month = signal_date[:6]
        bucket = coverage.setdefault(month, {"snapshot_dates": [], "context_schema_dates": []})
        bucket["snapshot_dates"].append(signal_date)
        if receipt.get("context_schema_available") is True:
            bucket["context_schema_dates"].append(signal_date)
    return coverage


def build_bundle(
    repository_root: Path = ROOT,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    root = Path(repository_root)
    canonical, source_manifest = load_source(root)
    metrics = build_metrics(canonical)
    features = build_features(canonical)
    audit = build_audit(canonical)
    csv_outputs = {
        OUTPUTS["metrics"]: csv_bytes(metrics),
        OUTPUTS["features"]: csv_bytes(features),
        OUTPUTS["audit"]: csv_bytes(audit),
    }
    manifest = {
        "artifact_version": VERSION,
        "model_id": MODEL_ID,
        "owner_id": OWNER_ID,
        "producer_path": PRODUCER,
        "validator_path": VALIDATOR,
        "source_commit": SOURCE_COMMIT,
        "source_artifacts": SOURCE_ARTIFACTS,
        "source_artifact_version": source_manifest["artifact_version"],
        "source_row_count": 3020,
        "unique_signal_event_count": 2992,
        "source_duplicate_group_count": 28,
        "source_duplicate_extra_row_count": 28,
        "canonical_same_stock_signal_date_group_count": 0,
        "canonical_same_stock_signal_date_cross_report_line_group_count": 0,
        "identity_policy": (
            "preserve_canonical_signal_event_id_and_report_line_no_second_dedup"
        ),
        "union_review_candidate_event_count": 8,
        "periods": _periods(canonical),
        "horizons": list(HORIZONS),
        "features": FEATURES,
        "outcome_bands": list(OUTCOME_BANDS),
        "feature_row_types": list(FEATURE_ROW_TYPES),
        "audit_types": list(AUDIT_TYPES),
        "metrics_schema": list(METRICS_COLUMNS),
        "features_schema": list(FEATURES_COLUMNS),
        "audit_schema": list(AUDIT_COLUMNS),
        "quantile_method": "pandas_linear_interpolation",
        "metric_weighting": "unique_signal_event_equal_weight",
        "metric_population": "all_primary_metric_included_unique_signal_events",
        "cross_population_comparison_warning": (
            "do_not_compare_as_improvement_against_complete_schema_or_other_population_metrics"
        ),
        "source_manifest_return_cost_basis": (
            "original_before_costs_slippage_and_tax"
        ),
        "return_cost_basis": "raw_return_before_costs_slippage_and_tax",
        "date_contrast_weighting": "signal_date_equal_weight_of_within_date_median_differences",
        "snapshot_coverage": _snapshot_coverage(source_manifest),
        "period_analysis_status": (
            "same_sample_month_diagnostics_not_complete_month_or_independent_oos"
        ),
        "review_candidate_policy": (
            "eight_event_union_retained_in_primary_exclusion_sensitivity_not_corrected"
        ),
        "macd_scale_policy": "raw_cross_stock_scale_not_comparable_for_threshold_or_recommendation",
        "price_source_formal_lineage_status": "mutable_current_files_unpinned_block_formal_use",
        "trading_calendar_status": "stock_price_row_sequence_only_no_market_calendar_proof",
        "non_overlapping_trades_proven": False,
        "overlap_eligibility": "mature_events_with_parseable_entry_and_exit_dates_only",
        "overlap_interval_basis": (
            "entry_date_to_fixed_horizon_exit_date_closed_interval"
        ),
        "overlap_interpretation": (
            "inclusive_endpoint_touch_is_conservative_date_intersection_"
            "not_actual_position_conflict"
        ),
        "immature_overlap_status": "not_assessed_not_non_overlapping",
        "entry_exit_changed": False,
        "first_publication_pit_proven": False,
        "first_publication_pit_status": "unknown_not_proven",
        "total_return_complete": False,
        "formal_use_allowed": False,
        "trade_eligible": False,
        "promotion_evidence_allowed": False,
        "operation_contract_status": "decision_required",
        "output_sha256": {
            path: sha256(payload) for path, payload in csv_outputs.items()
        },
    }
    return metrics, features, audit, manifest


def protected_snapshot(root: Path) -> dict[str, Any]:
    sentinels = load_protected_sentinels(
        root / "config/model_research_protected_sentinels.csv"
    )
    patterns = [sentinel.artifact_glob for sentinel in sentinels] + [
        spec["path"] for spec in SOURCE_ARTIFACTS.values()
    ]

    def matches(path: str) -> bool:
        return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)

    maps: list[dict[str, str]] = []
    for command in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z")):
        mapping: dict[str, str] = {}
        for entry in _git(root, *command).decode().split("\0"):
            if entry:
                metadata, path = entry.split("\t", 1)
                if matches(path):
                    mapping[path] = metadata
        maps.append(mapping)
    paths = set(maps[0]) | set(maps[1])
    for pattern in patterns:
        paths.update(
            path.relative_to(root).as_posix()
            for path in root.glob(pattern)
            if path.is_file()
        )
    for sentinel in sentinels:
        if sentinel.required and not any(
            fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in paths
        ):
            raise RuntimeError("missing protected sentinel: " + sentinel.sentinel_id)
    return {
        "tree": maps[0],
        "index": maps[1],
        "physical": {
            path: sha256((root / path).read_bytes())
            for path in paths
            if (root / path).is_file()
        },
    }


@contextmanager
def model_owned_artifact_guard(root: Path) -> Iterator[None]:
    rules = load_ownership_rules(root / "config/model_research_artifact_ownership.csv")
    errors = validate_changed_paths(OWNER_ID, PRODUCER, list(OUTPUTS.values()), rules)
    if errors:
        raise RuntimeError("unregistered matched-feature outputs: " + "; ".join(errors))
    before = _dirty_snapshot(root)
    protected = protected_snapshot(root)
    index_before = _git(root, "ls-files", "--stage", "-z")
    head_before = _git(root, "rev-parse", "HEAD")
    try:
        yield
    finally:
        changed = set(changed_during_run(root, before)) - set(OUTPUTS.values())
        if (
            changed
            or protected_snapshot(root) != protected
            or _git(root, "ls-files", "--stage", "-z") != index_before
            or _git(root, "rev-parse", "HEAD") != head_before
        ):
            raise RuntimeError("matched-feature research changed protected/out-of-scope paths")


def write_bundle(
    bundle: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, Any]],
    repository_root: Path = ROOT,
) -> None:
    root = Path(repository_root).resolve()
    metrics, features, audit, manifest = bundle
    payloads = {
        OUTPUTS["metrics"]: csv_bytes(metrics),
        OUTPUTS["features"]: csv_bytes(features),
        OUTPUTS["audit"]: csv_bytes(audit),
    }
    if manifest.get("output_sha256") != {
        path: sha256(payload) for path, payload in payloads.items()
    }:
        raise RuntimeError("matched-feature output hash mismatch")
    payloads[OUTPUTS["manifest"]] = canonical_json(manifest) + b"\n"
    with model_owned_artifact_guard(root):
        for relative, payload in payloads.items():
            target = root / relative
            if not target.resolve().is_relative_to(root) or any(
                path.is_symlink() for path in (target, *target.parents) if path != root
            ):
                raise RuntimeError("unsafe matched-feature output path")
            if target.exists() and target.read_bytes() != payload:
                raise RuntimeError("immutable matched-feature output already differs")
        for relative, payload in payloads.items():
            target = root / relative
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as handle:
                    handle.write(payload)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    write_bundle(build_bundle(args.repo_root), args.repo_root)
    print("回檔後短線轉強同訊號日連續特徵研究已產出；僅供研究，不是正式模型或 PDF 輸入。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
