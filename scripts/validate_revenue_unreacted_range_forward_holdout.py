from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
import math
import numbers
from pathlib import Path
import re
from typing import Mapping

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_holdout"
ARTIFACT_VERSION = "forward_holdout_v1_20260811"
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"

PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
PR462_PROJECTED_EPISODE_ROW_COUNT = 19569
PR462_PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260803"
HOLDOUT_START_DATE = "20260804"
SOURCE_PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
SOURCE_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
PRIMARY_VARIANT_ID = "source_mid_falling"
CHALLENGER_VARIANT_IDS = (
    "source_low_falling",
    "source_low_or_mid_falling_union",
)
ALL_VARIANT_IDS = (PRIMARY_VARIANT_ID, *CHALLENGER_VARIANT_IDS)
CONFIRMATION_VARIANT_ID = "delayed_next_close_continuation_bonus"
LIFECYCLE_POLICY_ID = "rearm_after_realized_exit_next_trade_day"
BASE_CONFIRMATION_RULE_ID = "close_cross_prev20_and_ma60_gt_ma120"
CONFIRMATION_RULE_ID = "next_trading_day_close_above_trigger_close"
ENTRY_RULE_ID = "next_day_close_confirmed_following_trading_day_open"
STOP_POLICY_ID = "none_no_stop_reference"
EXIT_RULE_ID = "fixed_d30_close"
HOLDING_DAYS = 30
HOLDING_SESSION_INDEX_OFFSET = 29
WATCH_HORIZON_TRADING_DAYS = 60
OPERATION_RETURN_REVIEW_THRESHOLD_PCT = 80.0

RULE_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_rule_v1"
RULE_CONTRACT = {
    "model_id": MODEL_ID,
    "source_variant_id": SOURCE_VARIANT_ID,
    "primary_variant_id": PRIMARY_VARIANT_ID,
    "challenger_variant_ids": list(CHALLENGER_VARIANT_IDS),
    "position_buckets": {
        "source_low_falling": "low_pos_le40",
        "source_mid_falling": "mid_pos_40_75",
        "source_low_or_mid_falling_union": "low_pos_le40|mid_pos_40_75",
    },
    "shape_bucket": "falling",
    "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
    "base_confirmation_rule_id": BASE_CONFIRMATION_RULE_ID,
    "confirmation_variant_id": CONFIRMATION_VARIANT_ID,
    "confirmation_rule_id": CONFIRMATION_RULE_ID,
    "entry_rule_id": ENTRY_RULE_ID,
    "entry_price_basis": "analysis_open",
    "holding_days": HOLDING_DAYS,
    "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
    "holding_session_contract": "inclusive_entry_session_count_30_exit_offset_29",
    "stop_policy_id": STOP_POLICY_ID,
    "exit_rule_id": EXIT_RULE_ID,
    "exit_price_basis": "analysis_close",
    "lifecycle_policy_id": LIFECYCLE_POLICY_ID,
    "same_stock_non_overlap": "entry_after_prior_realized_exit_next_trading_day",
    "anomaly_policy": "primary_retains_unresolved_candidates_sensitivity_excludes",
    "financial_statement_scope": (
        "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
        "non_operating_income_net_income_excluded"
    ),
}
DATA_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_data_v1"
DATA_CONTRACT = {
    "training_cutoff_date": TRAINING_CUTOFF_DATE,
    "bridge_start_date": BRIDGE_START_DATE,
    "bridge_end_date": BRIDGE_END_DATE,
    "holdout_start_date": HOLDOUT_START_DATE,
    "source_projection_artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
    "source_projection_artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
    "pr462_projected_episode_row_count": PR462_PROJECTED_EPISODE_ROW_COUNT,
    "pr462_projected_episode_semantic_sha256": (
        PR462_PROJECTED_EPISODE_SEMANTIC_SHA256
    ),
    "source_artifact_id": SOURCE_ARTIFACT_ID,
    "source_artifact_version": SOURCE_ARTIFACT_VERSION,
    "append_only_history": True,
    "research_only": True,
    "formal_model_use_allowed": False,
    "approved_for_daily": False,
    "presentation_allowed": False,
    "promotion_evidence_allowed": False,
    "production_change": False,
}

MONTHLY_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
FALSE_FLAG_COLUMNS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "promotion_evidence_allowed",
    "production_change",
)
METRIC_COLUMNS = (
    "event_count",
    "mature_count",
    "right_censored_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "return_ge20_count",
    "loss_count",
    "same_stock_overlap_pair_count",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")

DEFAULT_PATHS = {
    "manifest": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_manifest_latest.csv",
    "detail": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_event_detail_latest.csv",
    "summary": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_maturity_status_latest.csv",
    "comparison": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_comparison_latest.csv",
    "anomaly": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_anomaly_sensitivity_latest.csv",
    "manifest_history": ROOT / f"output/history/research/{ARTIFACT_ID}_manifest.csv",
    "detail_history": ROOT / f"output/history/research/{ARTIFACT_ID}_event_detail.csv",
    "summary_history": ROOT / f"output/history/research/{ARTIFACT_ID}_maturity_status.csv",
    "comparison_history": ROOT / f"output/history/research/{ARTIFACT_ID}_comparison.csv",
    "anomaly_history": ROOT / f"output/history/research/{ARTIFACT_ID}_anomaly_sensitivity.csv",
    "source_manifest": ROOT / "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
}


def _bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _strict_bool(value: object, *, label: str) -> bool:
    token = str(value).strip().lower()
    if token in {"true", "1", "yes"}:
        return True
    if token in {"false", "0", "no"}:
        return False
    raise RuntimeError(f"{label} is not canonical boolean text")


def _date(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    return text.zfill(4) if text.isdigit() else text


def _number(value: object) -> float:
    result = pd.to_numeric(value, errors="coerce")
    return float(result) if pd.notna(result) else math.nan


def _equal_number(left: object, right: object, tolerance: float = 0.00011) -> bool:
    left_number = _number(left)
    right_number = _number(right)
    if not np.isfinite(left_number) and not np.isfinite(right_number):
        return True
    return bool(
        np.isfinite(left_number)
        and np.isfinite(right_number)
        and math.isclose(left_number, right_number, abs_tol=tolerance)
    )


def _canonical_numeric_text(text: str) -> str | None:
    candidate = text.strip()
    if not re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        candidate,
    ):
        return None
    unsigned = candidate.lstrip("+-")
    integer_part = re.split(r"[eE]", unsigned, maxsplit=1)[0].split(".", maxsplit=1)[0]
    if len(integer_part) > 1 and integer_part.startswith("0"):
        return None
    if len(integer_part) > 18:
        return None
    try:
        number = Decimal(candidate)
    except InvalidOperation:
        return None
    if not number.is_finite():
        return None
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _canonical_value(value: object) -> str:
    if value is None or (
        not isinstance(value, (list, dict, tuple)) and pd.isna(value)
    ):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        if not math.isfinite(float(value)):
            return ""
        return format(float(value), ".15g")
    text_value = str(value).strip()
    if text_value.lower() in {"true", "false"}:
        return text_value.lower()
    numeric = _canonical_numeric_text(text_value)
    return numeric if numeric is not None else text_value


def _json_sha(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode(
            "utf-8"
        )
    ).hexdigest()


RULE_CANONICAL_SHA256 = _json_sha(RULE_CONTRACT)
DATA_CONTRACT_SHA256 = _json_sha(DATA_CONTRACT)


def _frame_sha(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = [
        [_canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _json_sha([CANONICAL_LINEAGE_VERSION, columns, rows])


def _mapping_sha(mapping: Mapping[str, object]) -> str:
    payload = [
        [str(key), _canonical_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) != "generated_at"
    ]
    return _json_sha([CANONICAL_LINEAGE_VERSION, payload])


def _source_numeric_text(text: str) -> str | None:
    candidate = text.strip()
    if not re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        candidate,
    ):
        return None
    unsigned = candidate.lstrip("+-")
    integer_part = re.split(r"[eE]", unsigned, maxsplit=1)[0].split(".", maxsplit=1)[0]
    if len(integer_part) > 1 and integer_part.startswith("0"):
        return None
    try:
        number = Decimal(candidate)
    except InvalidOperation:
        return None
    if not number.is_finite():
        return None
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _source_value(value: object) -> str:
    if value is None or (not isinstance(value, (str, bytes)) and pd.isna(value)):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (numbers.Integral, numbers.Real, Decimal)):
        number = float(value)
        if not np.isfinite(number):
            return ""
        numeric = _source_numeric_text(str(value))
        return numeric if numeric is not None else str(value).strip()
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    numeric = _source_numeric_text(text)
    return numeric if numeric is not None else text


def _source_mapping_sha(mapping: Mapping[str, object]) -> str:
    payload = [
        [str(key), _source_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) != "generated_at"
    ]
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _source_table_sha(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = sorted(
        [[_source_value(row[column]) for column in columns] for _, row in frame.iterrows()]
    )
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _normalize_source(source_detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "artifact_id",
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "episode_start_trade_date",
        "qualifying_update_count",
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_cross_market_resolution_ids",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        "qualifying_source_revenue_anomaly_candidate_flags",
        "qualifying_source_revenue_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        *MONTHLY_LINEAGE_COLUMNS,
    }
    missing = sorted(required - set(source_detail.columns))
    if missing:
        raise RuntimeError(f"source detail missing columns: {missing}")
    source = source_detail.loc[
        source_detail["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty:
        raise RuntimeError("source detail has no pre-registered source variant")
    if not source["artifact_id"].astype(str).eq(SOURCE_ARTIFACT_ID).all():
        raise RuntimeError("source artifact id drift")
    if not source["artifact_version"].astype(str).eq(SOURCE_ARTIFACT_VERSION).all():
        raise RuntimeError("source artifact version drift")
    if source["episode_key"].astype(str).duplicated().any():
        raise RuntimeError("source detail has duplicate episode keys")
    source["stock_id"] = source["stock_id"].map(
        lambda value: str(value)[:-2]
        if str(value).endswith(".0") and str(value)[:-2].isdigit()
        else str(value).strip()
    )
    slice_sha = _source_table_sha(source)
    source["source_first_canonical_row_sha256"] = source.apply(
        lambda row: _source_mapping_sha(row.to_dict()), axis=1
    )
    source["source_first_selected_slice_canonical_sha256"] = slice_sha
    return source.reset_index(drop=True)


def _normalize_prices(
    daily_by_stock: Mapping[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    result: dict[str, pd.DataFrame] = {}
    for raw_stock_id, raw in daily_by_stock.items():
        stock_id = _stock_id(raw_stock_id)
        frame = raw.copy()
        if "date" not in frame.columns:
            raise RuntimeError(f"price input missing date: {stock_id}")
        frame["date"] = frame["date"].map(_date)
        if frame["date"].eq("").any() or frame["date"].duplicated().any():
            raise RuntimeError(f"price input has invalid or duplicate dates: {stock_id}")
        frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
        for basis in ("open", "high", "low", "close"):
            analysis = f"analysis_{basis}"
            if analysis not in frame.columns:
                if basis not in frame.columns:
                    raise RuntimeError(f"price input missing {analysis}: {stock_id}")
                frame[analysis] = pd.to_numeric(frame[basis], errors="coerce")
            frame[analysis] = pd.to_numeric(frame[analysis], errors="coerce")
        close = frame["analysis_close"]
        if "ma60" not in frame.columns:
            frame["ma60"] = close.rolling(60, min_periods=60).mean()
        if "ma120" not in frame.columns:
            frame["ma120"] = close.rolling(120, min_periods=120).mean()
        if "operation_ma20" not in frame.columns:
            frame["operation_ma20"] = close.rolling(20, min_periods=20).mean()
        if "operation_ema23" not in frame.columns:
            frame["operation_ema23"] = close.ewm(span=23, adjust=False).mean()
        if "analysis_ema23" not in frame.columns:
            frame["analysis_ema23"] = close.ewm(span=23, adjust=False).mean()
        if "cross_breakout_prev20" not in frame.columns:
            previous_high = close.shift(1).rolling(20, min_periods=20).max()
            breakout = close.gt(previous_high)
            frame["cross_breakout_prev20"] = breakout & ~breakout.shift(
                1, fill_value=False
            ).astype(bool)
        result[stock_id] = frame
    if not result:
        raise RuntimeError("price input is empty")
    return result


def _price_lineage(
    prices: Mapping[str, pd.DataFrame],
) -> tuple[str, str, int, int]:
    rows = [
        {"stock_id": stock_id, "price_canonical_sha256": _frame_sha(frame)}
        for stock_id, frame in sorted(prices.items())
    ]
    return (
        _frame_sha(pd.DataFrame(rows)),
        "|".join(
            f"{row['stock_id']}:{row['price_canonical_sha256']}" for row in rows
        ),
        len(rows),
        sum(len(frame) for frame in prices.values()),
    )


def _training_lineage(source_manifest: pd.DataFrame) -> dict[str, object]:
    if len(source_manifest) != 1:
        raise RuntimeError("training source manifest must contain exactly one row")
    row = source_manifest.iloc[0]
    expected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
    }
    for column, value in expected.items():
        if str(row.get(column, "")).strip() != value:
            raise RuntimeError(f"training source projection drift: {column}")
    try:
        row_count = int(row.get("projected_episode_row_count", ""))
    except (TypeError, ValueError) as exc:
        raise RuntimeError(
            "training projected episode row count is invalid"
        ) from exc
    if row_count != PR462_PROJECTED_EPISODE_ROW_COUNT:
        raise RuntimeError(
            "PR462 projected episode row count drift: "
            f"expected={PR462_PROJECTED_EPISODE_ROW_COUNT} observed={row_count}"
        )
    semantic_sha = str(row.get("projected_episode_semantic_sha256", "")).strip().lower()
    if semantic_sha != PR462_PROJECTED_EPISODE_SEMANTIC_SHA256:
        raise RuntimeError("PR462 projected episode semantic SHA-256 drift")
    if not _bool(row.get("research_only", False)):
        raise RuntimeError("training source projection must remain research-only")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if column not in source_manifest.columns or _bool(row.get(column, False)):
            raise RuntimeError(
                f"training source projection formal consumer flag drift: {column}"
            )
    return {
        "training_source_projection_semantic_sha256": semantic_sha,
        "training_source_projected_episode_row_count": row_count,
        "training_source_manifest_canonical_sha256": _frame_sha(source_manifest),
    }


def _anchor_features(frame: pd.DataFrame, index: int) -> dict[str, object]:
    close = _number(frame.at[index, "analysis_close"])
    prior = frame.iloc[max(0, index - 120) : index]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    observed = bool(
        len(prior) == 120
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close)
    )
    high = float(prior_high.max()) if observed else math.nan
    low = float(prior_low.min()) if observed else math.nan
    observed = bool(observed and np.isfinite(high) and np.isfinite(low) and high > low)
    position = (close - low) / (high - low) * 100.0 if observed else math.nan
    position_bucket = (
        "low_pos_le40"
        if observed and position <= 40.0
        else "mid_pos_40_75"
        if observed and position <= 75.0
        else "high_pos_gt75"
        if observed
        else "insufficient_history"
    )
    return20 = math.nan
    if index >= 20:
        close20 = _number(frame.at[index - 20, "analysis_close"])
        if np.isfinite(close) and np.isfinite(close20) and close20 > 0:
            return20 = (close / close20 - 1.0) * 100.0
    recent = pd.to_numeric(
        frame.iloc[max(0, index - 22) : index + 1]["analysis_close"], errors="coerce"
    )
    range23 = (
        (float(recent.max()) / float(recent.min()) - 1.0) * 100.0
        if len(recent) == 23 and recent.notna().all() and float(recent.min()) > 0
        else math.nan
    )
    ema_now = _number(frame.at[index, "analysis_ema23"]) if index >= 5 else math.nan
    ema_prior = _number(frame.at[index - 5, "analysis_ema23"]) if index >= 5 else math.nan
    slope = (
        (ema_now / ema_prior - 1.0) * 100.0
        if np.isfinite(ema_now) and np.isfinite(ema_prior) and ema_prior > 0
        else math.nan
    )
    if not all(np.isfinite(value) for value in (return20, range23, slope)):
        shape = "insufficient_history"
    elif return20 > 5.0 and slope > 0.0:
        shape = "rising"
    elif return20 < -5.0 and slope < 0.0:
        shape = "falling"
    elif abs(return20) <= 5.0 and range23 <= 15.0:
        shape = "consolidation"
    else:
        shape = "mixed_or_turn"
    return {
        "source_position_120d_pct": round(position, 4) if np.isfinite(position) else "",
        "source_shape_return20_pct": round(return20, 4) if np.isfinite(return20) else "",
        "source_shape_range23_pct": round(range23, 4) if np.isfinite(range23) else "",
        "source_shape_ema23_slope5_pct": round(slope, 4) if np.isfinite(slope) else "",
        "source_position_bucket": position_bucket,
        "source_shape_bucket": shape,
        "source_position_shape_cell_id": (
            f"{position_bucket}__{shape}"
            if position_bucket != "insufficient_history" and shape != "insufficient_history"
            else "insufficient_history"
        ),
    }


def _lineage(episode: pd.Series, frame: pd.DataFrame) -> list[dict[str, object]]:
    names = (
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_cross_market_resolution_ids",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        "qualifying_source_revenue_anomaly_candidate_flags",
    )
    lists = {
        name: [part.strip() for part in str(episode[name]).split("|") if part.strip()]
        for name in names
    }
    lengths = {len(values) for values in lists.values()}
    lengths.add(int(episode["qualifying_update_count"]))
    if len(lengths) != 1 or not lists[names[0]]:
        raise RuntimeError(f"source point-in-time lineage is not aligned: {episode['episode_key']}")
    date_index = {str(date): int(index) for index, date in frame["date"].items()}
    rows: list[dict[str, object]] = []
    for values in zip(*(lists[name] for name in names), strict=True):
        (
            period,
            source_date,
            resolution,
            row_sha,
            table_date,
            trade_date,
            sequence,
            anomaly_flag,
        ) = values
        source_date = _date(source_date)
        table_date = _date(table_date)
        trade_date = _date(trade_date)
        if not source_date or not table_date or not trade_date:
            raise RuntimeError("source point-in-time date lineage is incomplete")
        sequence_index = int(sequence)
        if not SHA256_PATTERN.fullmatch(str(row_sha).lower()):
            raise RuntimeError("source point-in-time row SHA is invalid")
        first_available = next(
            (str(date) for date in frame["date"] if str(date) >= source_date), ""
        )
        if trade_date not in date_index or date_index[trade_date] != sequence_index:
            raise RuntimeError("source point-in-time sequence/date lineage drift")
        if first_available != trade_date or source_date > trade_date:
            raise RuntimeError("source point-in-time availability uses future information")
        rows.append(
            {
                "period": period,
                "source_date": source_date,
                "resolution": resolution,
                "row_sha": str(row_sha).lower(),
                "table_date": table_date,
                "trade_date": trade_date,
                "sequence_index": sequence_index,
                "source_anomaly_candidate_flag": _strict_bool(
                    anomaly_flag,
                    label=(
                        "source point-in-time anomaly flag/"
                        f"{episode['episode_key']}/{row_sha}"
                    ),
                ),
            }
        )
    if [row["sequence_index"] for row in rows] != sorted(
        {row["sequence_index"] for row in rows}
    ):
        raise RuntimeError("source point-in-time sequence is not strictly increasing")
    if _strict_bool(
        episode["qualifying_source_revenue_anomaly_candidate_flag"],
        label="source episode aggregate anomaly flag",
    ) != any(bool(row["source_anomaly_candidate_flag"]) for row in rows):
        raise RuntimeError("source point-in-time anomaly flag aggregate drift")
    if "start_source_revenue_anomaly_candidate_flag" in episode.index and (
        _strict_bool(
            episode["start_source_revenue_anomaly_candidate_flag"],
            label="source episode-start anomaly flag",
        )
        != bool(rows[0]["source_anomaly_candidate_flag"])
    ):
        raise RuntimeError("source point-in-time episode-start anomaly flag drift")
    return rows


def _operation(frame: pd.DataFrame, trigger: int) -> dict[str, object]:
    confirmation = trigger + 1
    entry = confirmation + 1
    trigger_close = _number(frame.at[trigger, "analysis_close"])
    confirmation_close = _number(frame.at[confirmation, "analysis_close"])
    base = {
        "trigger_index": trigger,
        "trigger_date": str(frame.at[trigger, "date"]),
        "trigger_close": round(trigger_close, 8),
        "confirmation_index": confirmation,
        "confirmation_date": str(frame.at[confirmation, "date"]),
        "confirmation_close": round(confirmation_close, 8),
        "entry_index": entry,
        "planned_exit_index": entry + HOLDING_SESSION_INDEX_OFFSET,
        "planned_exit_date": "",
        "exit_index": "",
        "exit_date": "",
        "exit_price": "",
        "return_valid": False,
        "right_censored": True,
        "realized_return_pct": "",
        "return_outcome": "",
        "realized_return_ge20": False,
        "operation_return_review_candidate_flag": False,
    }
    if entry >= len(frame):
        return {
            **base,
            "entry_date": "",
            "entry_price": "",
            "operation_status": "right_censored_before_entry",
            "blocked": len(frame) - 1,
        }
    entry_price = _number(frame.at[entry, "analysis_open"])
    base.update({"entry_date": str(frame.at[entry, "date"]), "entry_price": round(entry_price, 8)})
    exit_index = entry + HOLDING_SESSION_INDEX_OFFSET
    if exit_index >= len(frame):
        return {
            **base,
            "operation_status": f"right_censored_before_d{HOLDING_DAYS}",
            "blocked": len(frame) - 1,
        }
    exit_price = _number(frame.at[exit_index, "analysis_close"])
    realized = (exit_price / entry_price - 1.0) * 100.0
    outcome = "win" if realized > 1e-9 else "failure" if realized < -1e-9 else "neutral"
    return {
        **base,
        "planned_exit_date": str(frame.at[exit_index, "date"]),
        "exit_index": exit_index,
        "exit_date": str(frame.at[exit_index, "date"]),
        "exit_price": round(exit_price, 8),
        "return_valid": True,
        "right_censored": False,
        "realized_return_pct": round(realized, 4),
        "return_outcome": outcome,
        "realized_return_ge20": realized >= 20.0,
        "operation_return_review_candidate_flag": abs(realized) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
        "entry_date": str(frame.at[entry, "date"]),
        "entry_price": round(entry_price, 8),
        "operation_status": "mature_operation",
        "blocked": exit_index,
    }


def _expected_window(
    source: pd.DataFrame,
    prices: Mapping[str, pd.DataFrame],
    *,
    start_date: str,
    end_date: str,
) -> list[dict[str, object]]:
    expected: list[dict[str, object]] = []
    for raw_stock_id, episodes in source.groupby("stock_id", sort=False):
        stock_id = _stock_id(raw_stock_id)
        frame = prices.get(stock_id)
        if frame is None or frame.empty:
            continue
        date_index = {str(date): int(index) for index, date in frame["date"].items()}
        start_matches = frame.index[frame["date"].astype(str).ge(start_date)]
        end_matches = frame.index[frame["date"].astype(str).le(end_date)]
        if not len(start_matches) or not len(end_matches):
            continue
        window_start = int(start_matches[0])
        window_end = int(end_matches[-1])
        triggers: list[int] = []
        for index in range(window_start, window_end + 1):
            ma60 = _number(frame.at[index, "ma60"])
            ma120 = _number(frame.at[index, "ma120"])
            if not (_bool(frame.at[index, "cross_breakout_prev20"]) and np.isfinite(ma60) and np.isfinite(ma120) and ma60 > ma120):
                continue
            if index + 1 >= len(frame):
                continue
            trigger_close = _number(frame.at[index, "analysis_close"])
            confirmation_close = _number(frame.at[index + 1, "analysis_close"])
            if np.isfinite(trigger_close) and np.isfinite(confirmation_close) and confirmation_close > trigger_close:
                triggers.append(index)
        blocked = window_start - 1
        for _, episode in episodes.sort_values(
            ["episode_start_trade_date", "episode_key"], kind="mergesort"
        ).iterrows():
            episode_lineage = _lineage(episode, frame)
            start = max(
                date_index[_date(episode["episode_start_trade_date"])],
                window_start,
                blocked + 1,
            )
            end = min(
                max(row["sequence_index"] for row in episode_lineage) + WATCH_HORIZON_TRADING_DAYS,
                window_end,
            )
            for trigger in triggers:
                if trigger < start or trigger <= blocked:
                    continue
                if trigger > end:
                    break
                operation = _operation(frame, trigger)
                blocked = max(blocked, int(operation.pop("blocked")))
                trigger_date = str(frame.at[trigger, "date"])
                available = [
                    row
                    for row in episode_lineage
                    if int(row["sequence_index"]) <= trigger
                    and str(row["source_date"]) <= trigger_date
                    and str(row["trade_date"]) <= trigger_date
                    and str(row["table_date"]) <= trigger_date
                ]
                if not available:
                    raise RuntimeError("source as-of point-in-time row is missing at trigger")
                asof = available[-1]
                lag = trigger - int(asof["sequence_index"])
                if lag <= WATCH_HORIZON_TRADING_DAYS:
                    features = _anchor_features(frame, int(asof["sequence_index"]))
                    position = str(features["source_position_bucket"])
                    shape = str(features["source_shape_bucket"])
                    low = position == "low_pos_le40" and shape == "falling"
                    mid = position == "mid_pos_40_75" and shape == "falling"
                    if low or mid:
                        source_candidate = bool(asof["source_anomaly_candidate_flag"])
                        price_candidate = _bool(episode["unresolved_price_path_candidate_flag"])
                        return_candidate = _bool(operation["operation_return_review_candidate_flag"])
                        event_key = "|".join(
                            (
                                LIFECYCLE_POLICY_ID,
                                CONFIRMATION_VARIANT_ID,
                                stock_id,
                                str(episode["episode_key"]),
                                str(operation["trigger_date"]),
                            )
                        )
                        expected.append(
                            {
                                "event_key": event_key,
                                "stock_id": stock_id,
                                "stock_name": str(episode["stock_name"]),
                                "episode_key": str(episode["episode_key"]),
                                "variant_id": PRIMARY_VARIANT_ID if mid else CHALLENGER_VARIANT_IDS[0],
                                "primary_variant_member": mid,
                                "low_falling_member": low,
                                "low_or_mid_falling_union_member": True,
                                "source_asof_date": asof["source_date"],
                                "source_asof_trade_date": asof["trade_date"],
                                "source_asof_revenue_period": asof["period"],
                                "source_asof_row_canonical_sha256": asof["row_sha"],
                                "source_asof_canonical_source_table_date": asof["table_date"],
                                "source_asof_sequence_index": asof["sequence_index"],
                                "source_to_trigger_trading_days": lag,
                                "future_qualifying_update_ignored_count": len(episode_lineage) - len(available),
                                **features,
                                **operation,
                                "anomaly_candidate_flag": source_candidate or price_candidate or return_candidate,
                                "source_anomaly_candidate_flag": source_candidate,
                                "unresolved_price_path_candidate_flag": price_candidate,
                            }
                        )
                if _bool(operation["right_censored"]):
                    break
    return expected


def _membership(detail: pd.DataFrame, variant_id: str) -> pd.Series:
    column = {
        PRIMARY_VARIANT_ID: "primary_variant_member",
        CHALLENGER_VARIANT_IDS[0]: "low_falling_member",
        CHALLENGER_VARIANT_IDS[1]: "low_or_mid_falling_union_member",
    }[variant_id]
    return detail[column].map(_bool)


def _overlap_count(detail: pd.DataFrame) -> int:
    count = 0
    for _, stock in detail.groupby("stock_id", sort=False):
        prior_exit = -1
        for row in stock.sort_values("trigger_index", kind="mergesort").itertuples(index=False):
            entry = int(row.entry_index)
            if prior_exit >= 0 and entry <= prior_exit:
                count += 1
            prior_exit = max(
                prior_exit,
                entry if _bool(row.right_censored) else int(row.exit_index),
            )
    return count


def _metrics(part: pd.DataFrame) -> dict[str, object]:
    mature = part.loc[part["return_valid"].map(_bool)]
    returns = pd.to_numeric(mature["realized_return_pct"], errors="coerce").dropna()
    outcomes = mature["return_outcome"].astype(str)
    count = len(mature)
    return {
        "event_count": len(part),
        "mature_count": count,
        "right_censored_count": int(part["right_censored"].map(_bool).sum()),
        "win_count": int(outcomes.eq("win").sum()),
        "neutral_count": int(outcomes.eq("neutral").sum()),
        "failure_count": int(outcomes.eq("failure").sum()),
        "win_rate_pct": round(float(outcomes.eq("win").mean()) * 100.0, 4) if count else "",
        "average_return_pct": round(float(returns.mean()), 4) if len(returns) else "",
        "median_return_pct": round(float(returns.median()), 4) if len(returns) else "",
        "p10_return_pct": round(float(returns.quantile(0.10)), 4) if len(returns) else "",
        "p90_return_pct": round(float(returns.quantile(0.90)), 4) if len(returns) else "",
        "return_ge20_count": int(returns.ge(20.0).sum()),
        "loss_count": int(returns.lt(0.0).sum()),
        "same_stock_overlap_pair_count": _overlap_count(part),
    }


def _check_metric_row(
    row: pd.Series,
    expected: Mapping[str, object],
    *,
    label: str,
    errors: list[str],
) -> None:
    for column in METRIC_COLUMNS:
        if column not in row.index:
            errors.append(f"{label} missing metric column: {column}")
        elif not _equal_number(row[column], expected[column]):
            errors.append(f"{label} metric drift: {column}")


def _validate_capture_surfaces(
    frames: Mapping[str, pd.DataFrame],
    *,
    expected_capture_id: str,
    errors: list[str],
) -> None:
    common = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "capture_id": expected_capture_id,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
    }
    for label, frame in frames.items():
        missing = sorted({*common, "artifact_row_key"} - set(frame.columns))
        if missing:
            errors.append(f"{label} capture surface missing columns: {missing}")
            continue
        if frame["artifact_row_key"].astype(str).eq("").any():
            errors.append(f"{label} capture surface has blank artifact_row_key")
        if frame["artifact_row_key"].astype(str).duplicated().any():
            errors.append(f"{label} capture surface has duplicate artifact_row_key")
        for column, expected in common.items():
            observed = set(frame[column].astype(str).str.strip())
            if frame.empty:
                continue
            if observed != {str(expected)}:
                errors.append(f"{label} capture-envelope parity drift: {column}")


def validate_history_surfaces(
    current_frames: Mapping[str, pd.DataFrame],
    history_frames: Mapping[str, pd.DataFrame],
) -> list[str]:
    """Validate append-only structure and current-capture parity only.

    Historical rows are not replayed because their original input bundles are not
    part of this validator invocation.
    """

    errors: list[str] = []
    expected_names = set(current_frames)
    if set(history_frames) != expected_names:
        errors.append(
            "history surface set drift: "
            f"expected={sorted(expected_names)} observed={sorted(history_frames)}"
        )
        return errors
    manifest = current_frames["manifest"]
    if len(manifest) != 1 or "capture_id" not in manifest.columns:
        return ["history validation requires one current manifest capture"]
    current_capture_id = str(manifest.iloc[0]["capture_id"]).strip()
    for label in sorted(expected_names):
        current = current_frames[label]
        history = history_frames[label]
        if list(history.columns) != list(current.columns):
            errors.append(f"{label} history schema drift")
            continue
        required = {"capture_id", "artifact_row_key"}
        missing = sorted(required - set(history.columns))
        if missing:
            errors.append(f"{label} history missing structural keys: {missing}")
            continue
        if history[list(required)].astype(str).eq("").any().any():
            errors.append(f"{label} history has blank structural key")
        if history.duplicated(["capture_id", "artifact_row_key"]).any():
            errors.append(f"{label} history has duplicate capture/artifact row keys")
            continue
        persisted = history.loc[
            history["capture_id"].astype(str).eq(current_capture_id)
        ].copy()
        current_keys = set(current["artifact_row_key"].astype(str))
        persisted_keys = set(persisted["artifact_row_key"].astype(str))
        if persisted_keys != current_keys:
            errors.append(f"{label} history current-capture row presence drift")
            continue
        current_index = current.set_index("artifact_row_key", drop=False)
        persisted_index = persisted.set_index("artifact_row_key", drop=False)
        for key in sorted(current_keys):
            if _mapping_sha(current_index.loc[key].to_dict()) != _mapping_sha(
                persisted_index.loc[key].to_dict()
            ):
                errors.append(
                    f"{label} history current-capture semantic parity drift: {key}"
                )
    return errors


def validate_frames(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    comparison: pd.DataFrame,
    anomaly: pd.DataFrame,
    *,
    source_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    source_manifest: pd.DataFrame,
    history_frames: Mapping[str, pd.DataFrame] | None = None,
) -> list[str]:
    """Independently replay the frozen forward-holdout contract."""

    errors: list[str] = []
    frames = {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
    }
    for label, frame in frames.items():
        if "research_only" not in frame.columns or not frame["research_only"].map(_bool).all():
            errors.append(f"{label} must remain research-only")
        for column in FALSE_FLAG_COLUMNS:
            if column not in frame.columns or frame[column].map(_bool).any():
                errors.append(f"{label} formal consumer flag must remain false: {column}")
    if len(manifest) != 1:
        errors.append("manifest must contain exactly one row")
        return errors
    manifest_row = manifest.iloc[0]
    for column, expected in (
        ("preregistration_merge_commit", PREREGISTRATION_MERGE_COMMIT),
        ("training_cutoff_date", TRAINING_CUTOFF_DATE),
        ("bridge_start_date", BRIDGE_START_DATE),
        ("bridge_end_date", BRIDGE_END_DATE),
        ("holdout_start_date", HOLDOUT_START_DATE),
        ("artifact_row_key", "manifest"),
        ("rule_canonical_sha256", RULE_CANONICAL_SHA256),
        ("data_contract_sha256", DATA_CONTRACT_SHA256),
        ("holdout_status", "holdout_accumulating"),
    ):
        if column not in manifest.columns or str(manifest_row[column]).strip() != expected:
            errors.append(f"manifest preregistration/rule/cutoff drift: {column}")
    for column in ("ranking_consumption_allowed", "pdf_consumption_allowed"):
        if column not in manifest.columns or _bool(manifest_row[column]):
            errors.append(f"manifest formal consumer flag must remain false: {column}")

    try:
        training_lineage = _training_lineage(source_manifest)
        source = _normalize_source(source_detail)
        prices = _normalize_prices(daily_by_stock)
        observed = max(str(frame["date"].iloc[-1]) for frame in prices.values())
        if observed < HOLDOUT_START_DATE:
            raise RuntimeError(
                f"price observation ends before holdout start: {observed}"
            )
        if set(source["artifact_id"].astype(str)) != {SOURCE_ARTIFACT_ID}:
            raise RuntimeError("source artifact id drift")
        if set(source["artifact_version"].astype(str)) != {SOURCE_ARTIFACT_VERSION}:
            raise RuntimeError("source artifact version drift")
        current_monthly_lineage: dict[str, str] = {}
        for column in MONTHLY_LINEAGE_COLUMNS:
            values = {
                str(value).strip().lower()
                for value in source[column]
                if str(value).strip()
            }
            if len(values) != 1 or not SHA256_PATTERN.fullmatch(next(iter(values), "")):
                raise RuntimeError(
                    f"source monthly-revenue lineage is not one canonical SHA-256: {column}"
                )
            current_monthly_lineage[column] = next(iter(values))
        for column in (
            "qualifying_source_dates",
            "qualifying_canonical_source_table_dates",
            "qualifying_trade_dates",
        ):
            tokens = [
                _date(token)
                for value in source[column]
                for token in str(value).split("|")
                if str(token).strip()
            ]
            if any(not token for token in tokens):
                raise RuntimeError(f"source lineage has an invalid date: {column}")
            if any(token > observed for token in tokens):
                raise RuntimeError(
                    f"source lineage exceeds observation cutoff: {column}"
                )
        expected = _expected_window(
            source, prices, start_date=HOLDOUT_START_DATE, end_date=observed
        )
        bridge = _expected_window(
            source,
            prices,
            start_date=BRIDGE_START_DATE,
            end_date=min(BRIDGE_END_DATE, observed),
        ) if observed >= BRIDGE_START_DATE else []
    except Exception as exc:  # validation boundary reports input defects as evidence
        errors.append(f"point-in-time source/price replay failed: {exc}")
        return errors

    source_sha = _frame_sha(source)
    price_sha, price_sha_set, price_stock_count, price_row_count = _price_lineage(prices)
    capture_envelope = {
        "artifact_version": ARTIFACT_VERSION,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": observed,
        "source_detail_canonical_sha256": source_sha,
        "price_input_canonical_sha256": price_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    expected_capture_id = _json_sha(capture_envelope)
    manifest_lineage = {
        "capture_id": expected_capture_id,
        "observed_through_date": observed,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_row_count": len(source),
        "source_detail_canonical_sha256": source_sha,
        "price_input_stock_count": price_stock_count,
        "price_input_row_count": price_row_count,
        "price_input_stock_canonical_sha256s": price_sha_set,
        "price_input_canonical_sha256": price_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    for column, expected_value in manifest_lineage.items():
        if _canonical_value(manifest_row.get(column, "")) != _canonical_value(
            expected_value
        ):
            errors.append(f"manifest capture-envelope lineage drift: {column}")
    _validate_capture_surfaces(
        frames,
        expected_capture_id=expected_capture_id,
        errors=errors,
    )
    detail_lineage = {
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_canonical_sha256": source_sha,
        "price_input_canonical_sha256": price_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    for column, expected_value in detail_lineage.items():
        if column not in detail.columns:
            errors.append(f"detail capture-envelope lineage missing: {column}")
            continue
        if detail.empty:
            continue
        observed_values = {
            _canonical_value(value) for value in detail[column]
        }
        if observed_values != {_canonical_value(expected_value)}:
            errors.append(f"detail capture-envelope lineage drift: {column}")

    if detail["event_key"].astype(str).duplicated().any():
        errors.append("detail has duplicate event keys")
    if detail["trigger_date"].astype(str).lt(HOLDOUT_START_DATE).any():
        errors.append("bridge period leaked before holdout start")
    expected_by_key = {str(row["event_key"]): row for row in expected}
    actual_keys = set(detail["event_key"].astype(str))
    if actual_keys != set(expected_by_key):
        errors.append("holdout event completeness/bridge/as-of replay drift")
    row_columns = (
        "stock_id",
        "stock_name",
        "episode_key",
        "variant_id",
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_revenue_period",
        "source_asof_row_canonical_sha256",
        "source_asof_canonical_source_table_date",
        "source_position_bucket",
        "source_shape_bucket",
        "source_position_shape_cell_id",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "planned_exit_date",
        "exit_date",
        "operation_status",
        "return_outcome",
    )
    numeric_columns = (
        "source_asof_sequence_index",
        "source_to_trigger_trading_days",
        "future_qualifying_update_ignored_count",
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "trigger_index",
        "trigger_close",
        "confirmation_index",
        "confirmation_close",
        "entry_index",
        "planned_exit_index",
        "exit_index",
        "entry_price",
        "exit_price",
        "realized_return_pct",
    )
    bool_columns = (
        "primary_variant_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "return_valid",
        "right_censored",
        "realized_return_ge20",
        "operation_return_review_candidate_flag",
        "anomaly_candidate_flag",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    )
    for _, row in detail.iterrows():
        key = str(row.get("event_key", ""))
        expected_row = expected_by_key.get(key)
        if expected_row is None:
            continue
        if str(row.get("artifact_row_key", "")) != key:
            errors.append(f"detail artifact/event key drift: {key}")
        for column in row_columns:
            if str(row.get(column, "")) != str(expected_row.get(column, "")):
                errors.append(f"detail point-in-time/timing drift: {key}/{column}")
        for column in numeric_columns:
            if not _equal_number(row.get(column, ""), expected_row.get(column, "")):
                errors.append(f"detail D+2/D+30 numeric replay drift: {key}/{column}")
        for column in bool_columns:
            if _bool(row.get(column, "")) != _bool(expected_row.get(column, "")):
                errors.append(f"detail anomaly/censor/member drift: {key}/{column}")
        if str(row.get("confirmation_variant_id", "")) != CONFIRMATION_VARIANT_ID:
            errors.append(f"detail confirmation contract drift: {key}")
        if str(row.get("entry_price_basis", "")) != "analysis_open":
            errors.append(f"detail D+2 entry basis drift: {key}")
        if str(row.get("exit_price_basis", "")) != "analysis_close":
            errors.append(f"detail D+30 exit basis drift: {key}")
        if not _equal_number(row.get("holding_session_index_offset", ""), 29):
            errors.append(f"detail D+30 holding offset must remain 29: {key}")
        if str(row.get("stop_policy_id", "")) != STOP_POLICY_ID:
            errors.append(f"detail stop policy drift: {key}")
        trigger_date = str(row.get("trigger_date", ""))
        for column in (
            "source_asof_date",
            "source_asof_trade_date",
            "source_asof_canonical_source_table_date",
        ):
            if str(row.get(column, "")) > trigger_date:
                errors.append(f"detail future source as-of leakage: {key}/{column}")
        if _number(row.get("source_asof_sequence_index", "")) > _number(
            row.get("trigger_index", "")
        ):
            errors.append(f"detail future source sequence leakage: {key}")
        if not _bool(row.get("primary_metric_included", False)):
            errors.append(f"detail anomaly candidate must remain in primary metric: {key}")
        expected_sensitivity = not _bool(row.get("anomaly_candidate_flag", False))
        if _bool(row.get("sensitivity_metric_included", False)) != expected_sensitivity:
            errors.append(f"detail anomaly sensitivity inclusion drift: {key}")
        if _bool(row.get("right_censored", False)) and (
            _bool(row.get("return_valid", False))
            or np.isfinite(_number(row.get("realized_return_pct", "")))
            or str(row.get("return_outcome", "")).strip()
        ):
            errors.append(f"right-censored row entered mature metrics: {key}")
        if "event_row_canonical_sha256" in row.index:
            mapping = row.drop(labels=["event_row_canonical_sha256"]).to_dict()
            if str(row["event_row_canonical_sha256"]).strip() != _mapping_sha(mapping):
                errors.append(f"detail event row canonical SHA drift: {key}")

    overlap = _overlap_count(detail)
    if overlap:
        errors.append(f"same-stock overlap/rearm prior exit violation: {overlap}")

    if int(_number(manifest_row.get("bridge_excluded_signal_count", -1))) != len(bridge):
        errors.append("manifest bridge exclusion count drift")
    if int(_number(manifest_row.get("holdout_event_count", -1))) != len(detail):
        errors.append("manifest holdout event count drift")
    mature_total = int(detail["return_valid"].map(_bool).sum())
    if int(_number(manifest_row.get("mature_event_count", -1))) != mature_total:
        errors.append("manifest mature/right-censored count drift")

    for surface_label, frame in (("summary", summary), ("comparison", comparison)):
        if len(frame) != len(ALL_VARIANT_IDS):
            errors.append(f"{surface_label} row multiplicity drift")
            continue
        if frame["variant_id"].astype(str).duplicated().any():
            errors.append(f"{surface_label} duplicate variant business key")
            continue
        if set(frame["variant_id"].astype(str)) != set(ALL_VARIANT_IDS):
            errors.append(f"{surface_label} primary/challenger variant set drift")
            continue
        if not frame.apply(
            lambda row: str(row.get("artifact_row_key", ""))
            == str(row.get("variant_id", "")),
            axis=1,
        ).all():
            errors.append(f"{surface_label} artifact/business key drift")
            continue
        for variant_id in ALL_VARIANT_IDS:
            part = detail.loc[_membership(detail, variant_id)]
            expected_metrics = _metrics(part)
            row = frame.loc[frame["variant_id"].astype(str).eq(variant_id)].iloc[0]
            _check_metric_row(
                row,
                expected_metrics,
                label=f"{surface_label}/{variant_id}",
                errors=errors,
            )
            if str(row.get("holdout_status", "")) != "holdout_accumulating":
                errors.append(f"{surface_label} holdout status drift: {variant_id}")

    expected_anomaly_keys = {
        (variant_id, basis)
        for variant_id in ALL_VARIANT_IDS
        for basis in (
            "primary_candidate_retaining",
            "excluding_unresolved_anomaly_candidates_sensitivity",
        )
    }
    actual_anomaly_keys = set(
        zip(anomaly["variant_id"].astype(str), anomaly["analysis_basis"].astype(str))
    )
    anomaly_business_keys = list(
        zip(anomaly["variant_id"].astype(str), anomaly["analysis_basis"].astype(str))
    )
    if len(anomaly) != len(expected_anomaly_keys):
        errors.append("anomaly row multiplicity drift")
    elif len(set(anomaly_business_keys)) != len(anomaly_business_keys):
        errors.append("anomaly duplicate variant/analysis business key")
    elif actual_anomaly_keys != expected_anomaly_keys:
        errors.append("anomaly primary/sensitivity surface key drift")
    elif not anomaly.apply(
        lambda row: str(row.get("artifact_row_key", ""))
        == f"{row.get('variant_id', '')}|{row.get('analysis_basis', '')}",
        axis=1,
    ).all():
        errors.append("anomaly artifact/business key drift")
    else:
        for variant_id, basis in sorted(expected_anomaly_keys):
            part = detail.loc[_membership(detail, variant_id)]
            candidates = part["anomaly_candidate_flag"].map(_bool)
            basis_part = part if basis == "primary_candidate_retaining" else part.loc[~candidates]
            row = anomaly.loc[
                anomaly["variant_id"].astype(str).eq(variant_id)
                & anomaly["analysis_basis"].astype(str).eq(basis)
            ].iloc[0]
            _check_metric_row(
                row,
                _metrics(basis_part),
                label=f"anomaly/{variant_id}/{basis}",
                errors=errors,
            )
            expected_excluded = 0 if basis == "primary_candidate_retaining" else int(candidates.sum())
            if not _equal_number(row.get("excluded_anomaly_candidate_count", ""), expected_excluded):
                errors.append(f"anomaly primary retention/sensitivity drift: {variant_id}/{basis}")
    if history_frames is not None:
        errors.extend(validate_history_surfaces(frames, history_frames))
    return errors


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype={"stock_id": str, "trigger_date": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )


def _load_explicit_price_inputs(directory: Path) -> dict[str, pd.DataFrame]:
    if not directory.is_dir():
        raise RuntimeError(f"explicit price input directory is missing: {directory}")
    output: dict[str, pd.DataFrame] = {}
    for path in sorted(directory.glob("*.csv")):
        frame = _read_csv(path)
        if "stock_id" in frame.columns:
            stock_ids = sorted({_stock_id(value) for value in frame["stock_id"]})
            if len(stock_ids) != 1:
                raise RuntimeError(
                    f"explicit price input must contain one stock identity: {path}"
                )
            stock_id = stock_ids[0]
        else:
            stock_id = _stock_id(path.stem)
        if not stock_id or stock_id in output:
            raise RuntimeError(f"explicit price input stock identity is invalid: {path}")
        output[stock_id] = frame
    if not output:
        raise RuntimeError("explicit price input directory contains no CSV inputs")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the independent revenue forward holdout replay"
    )
    for name, path in DEFAULT_PATHS.items():
        parser.add_argument(f"--{name.replace('_', '-')}", type=Path, default=path)
    parser.add_argument(
        "--source-detail",
        type=Path,
        required=True,
        help="Explicit source-detail evidence used by the capture",
    )
    parser.add_argument(
        "--price-input-directory",
        type=Path,
        required=True,
        help="Directory containing one explicit normalized price CSV per stock",
    )
    args = parser.parse_args()
    source = _read_csv(args.source_detail)
    daily = _load_explicit_price_inputs(args.price_input_directory)
    errors = validate_frames(
        _read_csv(args.manifest),
        _read_csv(args.detail),
        _read_csv(args.summary),
        _read_csv(args.comparison),
        _read_csv(args.anomaly),
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=_read_csv(args.source_manifest),
        history_frames={
            name: _read_csv(getattr(args, f"{name}_history"))
            for name in ("manifest", "detail", "summary", "comparison", "anomaly")
        },
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: revenue_unreacted_range forward holdout independently validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
