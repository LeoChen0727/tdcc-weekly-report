from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from daily_snapshot_revision_utils import (  # noqa: E402
    normalize_revision_manifest_schema,
    select_latest_snapshot_revisions,
    snapshot_file_sha256_candidates,
)
from model_research_artifact_guard import (  # noqa: E402
    load_ownership_rules,
    model_owned_artifact_guard,
    validate_changed_paths,
)
from tracking_utils import normalize_code, safe_str, write_csv  # noqa: E402


ROOT = SCRIPT_DIR.parent
MODEL_ID = "pullback_short_reclaim"
PRODUCER = "scripts/build_pullback_short_reclaim_research.py"
ARTIFACT_ID = "model_signals_for_report"
ARTIFACT_VERSION = "pullback_short_reclaim_published_signal_replay_v1"
SNAPSHOT_REVISION_POLICY = "latest_revision_per_report_date_artifact"
HORIZONS = (5, 10, 20)
ANOMALY_CANDIDATE_ABS_RETURN_PCT = 80.0
ENTRY_RULE = "signal_date_next_trading_day_open"
OPERATION_CONTRACT_STATUS = "decision_required"
FORMAL_USE_ALLOWED = False
REQUIRED_ROOT_CHECKS = (
    "identity_dedup_non_overlap",
    "formal_operation_replay",
    "point_in_time_and_trading_calendar",
    "raw_source_lineage_and_hash",
    "units_formula_and_adjustment_basis",
    "authoritative_business_event_history",
    "independent_source_corroboration",
    "reproducible_evidence_reference",
)
SIGNAL_SEMANTIC_COLUMNS = (
    "signal_date",
    "stock_id",
    "model_id",
    "entry_basis",
    "model_score",
    "main_condition_met",
    "score_components",
    "risk_penalty_tags",
    "next_confirmation",
    "model_main_conditions",
    "model_add_score_items",
    "model_forbidden_veto",
    "model_operation_guidance",
    "selection_semantics",
)
EVENTS_FILENAME = "pullback_short_reclaim_published_signal_replay_events_latest.csv"
SUMMARY_FILENAME = "pullback_short_reclaim_published_signal_replay_summary_latest.csv"
ANOMALIES_FILENAME = (
    "pullback_short_reclaim_published_signal_replay_anomaly_candidates_latest.csv"
)
ANOMALY_COLUMNS = (
    "artifact_version",
    "anomaly_candidate_id",
    "signal_event_id",
    "model_id",
    "signal_date",
    "stock_id",
    "horizon",
    "realized_return_pct",
    "statistical_trigger_method",
    "statistical_trigger_threshold_pct",
    "statistical_trigger_status",
    "final_disposition",
    "primary_metric_policy",
    "promotion_policy",
    "required_root_checks",
    "completed_root_checks",
    "missing_root_checks",
    "snapshot_sha256",
    "source_row_sha256",
    "price_source_sha256",
    "price_source_immutability_status",
    "retained_in_primary_metrics",
    "formal_use_allowed",
    "promotion_evidence_allowed",
    "operation_contract_status",
    "generated_at",
)


@dataclass(frozen=True)
class ReplayBundle:
    events: pd.DataFrame
    summary: pd.DataFrame
    anomalies: pd.DataFrame


def canonical_file_sha256(path: Path) -> str:
    payload = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(payload).hexdigest()


def raw_file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {str(key): safe_str(values[key]) for key in sorted(values)}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def aggregate_sha256(values: list[str]) -> str:
    payload = "\n".join(sorted(set(values))).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _is_sha(value: Any, length: int) -> bool:
    return re.fullmatch(rf"[0-9a-f]{{{length}}}", safe_str(value).lower()) is not None


def _bool_text(value: bool) -> str:
    return "True" if value else "False"


def _date(value: Any) -> str:
    text = "" if value is None else str(value)
    if len(text) != 8 or not text.isdigit():
        return ""
    try:
        parsed = datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return ""
    return text if parsed.strftime("%Y%m%d") == text else ""


def _outcome(value: float) -> str:
    if value > 0:
        return "win"
    if value < 0:
        return "failure"
    return "neutral"


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _manifest_metadata(manifest_path: Path) -> dict[tuple[str, str], dict[str, str]]:
    try:
        manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    except Exception as exc:
        raise RuntimeError(f"failed to read snapshot manifest: {manifest_path}") from exc
    manifest = normalize_revision_manifest_schema(
        manifest,
        source=manifest_path.as_posix(),
    )
    required = {
        "snapshot_report_date",
        "snapshot_revision",
        "artifact_id",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
        "column_count",
        "pipeline_commit_sha",
        "source_path",
        "purpose",
    }
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise RuntimeError(f"snapshot manifest missing columns: {missing}")
    selected = manifest[manifest["artifact_id"].astype(str).eq(ARTIFACT_ID)].copy()
    metadata: dict[tuple[str, str], dict[str, str]] = {}
    for _, row in selected.iterrows():
        report_date = _date(row.get("snapshot_report_date", ""))
        revision = safe_str(row.get("snapshot_revision", ""))
        key = (report_date, revision)
        if not report_date:
            raise RuntimeError("snapshot manifest contains invalid report date")
        if not revision:
            raise RuntimeError("snapshot manifest contains blank revision")
        if key in metadata:
            raise RuntimeError(f"duplicate snapshot manifest key: {key}")
        metadata[key] = {str(column): safe_str(row.get(column, "")) for column in row.index}
    return metadata


def _validate_snapshot_frame(
    frame: pd.DataFrame,
    metadata: dict[str, str],
    *,
    report_date: str,
    revision: str,
) -> None:
    try:
        expected_rows = int(metadata["row_count"])
        expected_columns = int(metadata["column_count"])
    except (KeyError, TypeError, ValueError) as exc:
        raise RuntimeError(
            f"invalid row_count/column_count for {report_date}/{revision}"
        ) from exc
    if len(frame) != expected_rows or len(frame.columns) != expected_columns:
        raise RuntimeError(
            "snapshot row/column count mismatch: "
            f"report_date={report_date} revision={revision} "
            f"expected={expected_rows}x{expected_columns} "
            f"actual={len(frame)}x{len(frame.columns)}"
        )
    if not _is_sha(metadata.get("pipeline_commit_sha", ""), 40):
        raise RuntimeError(
            f"invalid pipeline_commit_sha for {report_date}/{revision}"
        )
    if metadata.get("source_path") != (
        "output/latest/daily_candidate_model_signals_for_report_latest.csv"
    ):
        raise RuntimeError(
            f"unexpected model signal source_path for {report_date}/{revision}"
        )
    if metadata.get("purpose") != "as_published_daily_model_snapshot":
        raise RuntimeError(
            f"unexpected snapshot purpose for {report_date}/{revision}"
        )


def _price_source_path_text(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _load_price_history(stock_id: str, price_dir: Path) -> tuple[pd.DataFrame, str, str]:
    path = price_dir / f"{stock_id}.csv"
    if not path.is_file():
        return pd.DataFrame(), _price_source_path_text(path), ""
    try:
        raw = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        raise RuntimeError(f"failed to read price history: {path}") from exc
    required = {"date", "open", "close"}
    missing = sorted(required - set(raw.columns))
    if missing:
        raise RuntimeError(f"price history missing columns: stock_id={stock_id} {missing}")
    work = raw.copy()
    work["_date"] = work["date"].map(_date)
    if work["_date"].eq("").any():
        raise RuntimeError(f"price history contains invalid date: stock_id={stock_id}")
    if work["_date"].duplicated().any():
        duplicates = sorted(work.loc[work["_date"].duplicated(False), "_date"].unique())
        raise RuntimeError(
            f"price history contains duplicate dates: stock_id={stock_id} dates={duplicates}"
        )
    work["_open"] = pd.to_numeric(work["open"], errors="coerce")
    work["_close"] = pd.to_numeric(work["close"], errors="coerce")
    work = work.sort_values("_date").reset_index(drop=True)
    return work, _price_source_path_text(path), raw_file_sha256(path)


def _price_row_sha256(row: pd.Series) -> str:
    return canonical_row_sha256(
        {column: row[column] for column in row.index if not str(column).startswith("_")}
    )


def _blank_forward(status: str) -> dict[str, Any]:
    values: dict[str, Any] = {
        "entry_date": "",
        "entry_open_price": "",
        "entry_price_row_sha256": "",
        "overall_maturity_status": status,
    }
    for horizon in HORIZONS:
        values.update(
            {
                f"d{horizon}_maturity_status": status,
                f"d{horizon}_exit_date": "",
                f"d{horizon}_exit_close_price": "",
                f"d{horizon}_exit_price_row_sha256": "",
                f"d{horizon}_return_pct": "",
                f"d{horizon}_outcome": "",
                f"d{horizon}_anomaly_candidate": "False",
            }
        )
    return values


def _forward_replay(price: pd.DataFrame, signal_date: str) -> dict[str, Any]:
    if price.empty:
        return _blank_forward("missing_price_history")
    future = price[price["_date"].astype(str).gt(signal_date)].reset_index(drop=True)
    if future.empty:
        return _blank_forward("no_forward_price")
    entry = future.iloc[0]
    entry_price = float(entry["_open"]) if pd.notna(entry["_open"]) else math.nan
    values: dict[str, Any] = {
        "entry_date": safe_str(entry["_date"]),
        "entry_open_price": round(entry_price, 6) if math.isfinite(entry_price) else "",
        "entry_price_row_sha256": _price_row_sha256(entry),
        "overall_maturity_status": "not_mature",
    }
    mature_count = 0
    for horizon in HORIZONS:
        status = "not_mature"
        exit_date = ""
        exit_price: float | str = ""
        exit_row_sha = ""
        realized: float | str = ""
        outcome = ""
        anomaly = False
        if len(future) >= horizon:
            exit_row = future.iloc[horizon - 1]
            exit_date = safe_str(exit_row["_date"])
            exit_row_sha = _price_row_sha256(exit_row)
            close_price = (
                float(exit_row["_close"]) if pd.notna(exit_row["_close"]) else math.nan
            )
            if not math.isfinite(entry_price) or entry_price <= 0:
                status = "invalid_entry_price"
            elif not math.isfinite(close_price) or close_price <= 0:
                status = "invalid_exit_price"
            else:
                status = "mature"
                mature_count += 1
                exit_price = round(close_price, 6)
                result = (close_price / entry_price - 1.0) * 100.0
                realized = round(result, 6)
                outcome = _outcome(result)
                anomaly = abs(result) >= ANOMALY_CANDIDATE_ABS_RETURN_PCT
        values.update(
            {
                f"d{horizon}_maturity_status": status,
                f"d{horizon}_exit_date": exit_date,
                f"d{horizon}_exit_close_price": exit_price,
                f"d{horizon}_exit_price_row_sha256": exit_row_sha,
                f"d{horizon}_return_pct": realized,
                f"d{horizon}_outcome": outcome,
                f"d{horizon}_anomaly_candidate": _bool_text(anomaly),
            }
        )
    if mature_count == len(HORIZONS):
        values["overall_maturity_status"] = "mature_d20"
    elif mature_count:
        values["overall_maturity_status"] = "partially_mature"
    elif any(
        values[f"d{horizon}_maturity_status"].startswith("invalid_")
        for horizon in HORIZONS
    ):
        values["overall_maturity_status"] = "invalid_price"
    return values


def _semantic_sha(row: pd.Series) -> str:
    payload = {column: safe_str(row.get(column, "")) for column in SIGNAL_SEMANTIC_COLUMNS}
    payload["stock_id"] = normalize_code(payload["stock_id"])
    payload["signal_date"] = _date(payload["signal_date"])
    return canonical_row_sha256(payload)


def _build_anomalies(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if events.empty:
        return pd.DataFrame(columns=ANOMALY_COLUMNS[:-1])
    canonical = events[events["primary_metric_included"].astype(str).eq("True")]
    for _, event in canonical.iterrows():
        for horizon in HORIZONS:
            if safe_str(event.get(f"d{horizon}_anomaly_candidate")) != "True":
                continue
            candidate_id = hashlib.sha256(
                f"{event['signal_event_id']}|d{horizon}".encode("utf-8")
            ).hexdigest()
            rows.append(
                {
                    "artifact_version": ARTIFACT_VERSION,
                    "anomaly_candidate_id": candidate_id,
                    "signal_event_id": event["signal_event_id"],
                    "model_id": MODEL_ID,
                    "signal_date": event["signal_date"],
                    "stock_id": event["stock_id"],
                    "horizon": f"D+{horizon}",
                    "realized_return_pct": event[f"d{horizon}_return_pct"],
                    "statistical_trigger_method": "abs_realized_return_ge_threshold",
                    "statistical_trigger_threshold_pct": ANOMALY_CANDIDATE_ABS_RETURN_PCT,
                    "statistical_trigger_status": "anomaly_candidate",
                    "final_disposition": "unresolved_anomaly_candidate",
                    "primary_metric_policy": "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only",
                    "promotion_policy": "blocked_pending_root_cause",
                    "required_root_checks": ";".join(REQUIRED_ROOT_CHECKS),
                    "completed_root_checks": "",
                    "missing_root_checks": ";".join(REQUIRED_ROOT_CHECKS),
                    "snapshot_sha256": event["snapshot_sha256"],
                    "source_row_sha256": event["source_row_sha256"],
                    "price_source_sha256": event["price_source_sha256"],
                    "price_source_immutability_status": "mutable_current_file_unpinned",
                    "retained_in_primary_metrics": "True",
                    "formal_use_allowed": "False",
                    "promotion_evidence_allowed": "False",
                    "operation_contract_status": OPERATION_CONTRACT_STATUS,
                }
            )
    return pd.DataFrame(rows, columns=ANOMALY_COLUMNS[:-1])


def _pct(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 6) if denominator else ""


def _build_summary(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    canonical = events[events["primary_metric_included"].astype(str).eq("True")].copy()
    snapshot_shas = canonical["snapshot_sha256"].astype(str).tolist() if not canonical.empty else []
    price_shas = [
        value
        for value in canonical.get("price_source_sha256", pd.Series(dtype=str)).astype(str)
        if value
    ]
    common = {
        "artifact_version": ARTIFACT_VERSION,
        "model_id": MODEL_ID,
        "snapshot_revision_policy": SNAPSHOT_REVISION_POLICY,
        "entry_rule": ENTRY_RULE,
        "exit_rule": "fixed_future_close_research_comparison",
        "stop_rule": "undefined_decision_required",
        "published_source_row_count": len(events),
        "unique_signal_event_count": len(canonical),
        "duplicate_presentation_row_count": len(events) - len(canonical),
        "snapshot_report_count": int(canonical["snapshot_report_date"].nunique()) if not canonical.empty else 0,
        "report_date_min": safe_str(canonical["snapshot_report_date"].min()) if not canonical.empty else "",
        "report_date_max": safe_str(canonical["snapshot_report_date"].max()) if not canonical.empty else "",
        "source_snapshot_set_sha256": aggregate_sha256(snapshot_shas),
        "source_price_set_sha256": aggregate_sha256(price_shas),
        "primary_metric_basis": "unique_signal_event_including_unresolved_anomaly_candidates",
        "primary_retains_unresolved_anomaly_candidates": "True",
        "excluded_anomaly_candidate_count": 0,
        "right_censoring_policy": "per_horizon_incomplete_forward_price_excluded_from_horizon_metrics",
        "sensitivity_analysis_basis": "excluding_unresolved_anomaly_candidates_sensitivity_only",
        "sensitivity_is_corrected_primary": "False",
        "price_source_formal_lineage_status": "mutable_current_files_unpinned_block_formal_use",
        "formal_use_allowed": "False",
        "trade_eligible": "False",
        "promotion_evidence_allowed": "False",
        "operation_contract_status": OPERATION_CONTRACT_STATUS,
        "interpretation_status": "research_only_operation_decision_required",
        "generated_at": generated_at,
    }
    rows: list[dict[str, Any]] = []
    for horizon in HORIZONS:
        status_col = f"d{horizon}_maturity_status"
        return_col = f"d{horizon}_return_pct"
        outcome_col = f"d{horizon}_outcome"
        mature = canonical[canonical[status_col].astype(str).eq("mature")].copy()
        returns = pd.to_numeric(mature[return_col], errors="coerce")
        if returns.isna().any():
            raise RuntimeError(f"mature D+{horizon} row has a blank/non-numeric return")
        wins = int(mature[outcome_col].astype(str).eq("win").sum())
        neutrals = int(mature[outcome_col].astype(str).eq("neutral").sum())
        failures = int(mature[outcome_col].astype(str).eq("failure").sum())
        anomaly_count = int(
            mature[f"d{horizon}_anomaly_candidate"].astype(str).eq("True").sum()
        )
        sensitivity = mature[
            ~mature[f"d{horizon}_anomaly_candidate"].astype(str).eq("True")
        ].copy()
        sensitivity_returns = pd.to_numeric(
            sensitivity[return_col], errors="coerce"
        )
        sensitivity_wins = int(
            sensitivity[outcome_col].astype(str).eq("win").sum()
        )
        sensitivity_neutrals = int(
            sensitivity[outcome_col].astype(str).eq("neutral").sum()
        )
        sensitivity_failures = int(
            sensitivity[outcome_col].astype(str).eq("failure").sum()
        )
        right_censored_statuses = {
            "not_mature",
            "no_forward_price",
            "missing_price_history",
        }
        right_censored_count = int(
            canonical[status_col].astype(str).isin(right_censored_statuses).sum()
        )
        invalid_price_count = int(
            canonical[status_col].astype(str).str.startswith("invalid_").sum()
        )
        promotion_blockers = [
            "operation_contract_decision_required",
            "mutable_price_source_unpinned",
            "market_calendar_proof_missing",
        ]
        if anomaly_count:
            promotion_blockers.append("unresolved_anomaly_candidate")
        row = dict(common)
        row.update(
            {
                "horizon": f"D+{horizon}",
                "holding_trading_rows": horizon,
                "signal_event_count": len(canonical),
                "mature_count": len(mature),
                "not_mature_count": len(canonical) - len(mature),
                "right_censored_count": right_censored_count,
                "invalid_price_count": invalid_price_count,
                "win_count": wins,
                "neutral_count": neutrals,
                "failure_count": failures,
                "win_rate_pct": _pct(wins, len(mature)),
                "neutral_rate_pct": _pct(neutrals, len(mature)),
                "failure_rate_pct": _pct(failures, len(mature)),
                "average_return_pct": round(float(returns.mean()), 6) if len(returns) else "",
                "median_return_pct": round(float(returns.median()), 6) if len(returns) else "",
                "unresolved_anomaly_candidate_count": anomaly_count,
                "sensitivity_sample_count": len(sensitivity),
                "sensitivity_excluded_anomaly_candidate_count": anomaly_count,
                "sensitivity_win_count": sensitivity_wins,
                "sensitivity_neutral_count": sensitivity_neutrals,
                "sensitivity_failure_count": sensitivity_failures,
                "sensitivity_win_rate_pct": _pct(
                    sensitivity_wins, len(sensitivity)
                ),
                "sensitivity_average_return_pct": round(
                    float(sensitivity_returns.mean()), 6
                )
                if len(sensitivity_returns)
                else "",
                "sensitivity_median_return_pct": round(
                    float(sensitivity_returns.median()), 6
                )
                if len(sensitivity_returns)
                else "",
                "promotion_blockers": ";".join(promotion_blockers),
            }
        )
        rows.append(row)
    return pd.DataFrame(rows)


def build_replay(
    *,
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
    through_date: str = "",
    generated_at: str | None = None,
) -> ReplayBundle:
    snapshot_dir = Path(snapshot_dir)
    manifest_path = Path(manifest_path)
    price_dir = Path(price_dir)
    if through_date and not _date(through_date):
        raise RuntimeError(f"invalid through_date: {through_date!r}")
    metadata_index = _manifest_metadata(manifest_path)
    revisions = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        through_date=through_date,
        manifest_path=manifest_path,
        repository_root=snapshot_dir.parents[2] if len(snapshot_dir.parents) >= 3 else snapshot_dir.parent,
    )
    if not revisions:
        raise RuntimeError("manifest contains no model_signals_for_report revisions")
    manifest_sha = canonical_file_sha256(manifest_path)
    producer_sha = raw_file_sha256(Path(__file__))
    price_cache: dict[str, tuple[pd.DataFrame, str, str]] = {}
    rows: list[dict[str, Any]] = []

    for revision in revisions:
        if _date(revision.report_date) != revision.report_date:
            raise RuntimeError(
                f"selected snapshot has invalid report date: {revision.report_date!r}"
            )
        metadata = metadata_index.get((revision.report_date, revision.revision))
        if metadata is None:
            raise RuntimeError(
                f"selected snapshot has no exact manifest metadata: {revision.report_date}/{revision.revision}"
            )
        if safe_str(metadata.get("snapshot_path")) != revision.path_text:
            raise RuntimeError("selected snapshot path differs from manifest metadata")
        if safe_str(metadata.get("snapshot_sha256")).lower() != revision.snapshot_sha256:
            raise RuntimeError("selected snapshot SHA differs from manifest metadata")
        if revision.snapshot_sha256 not in snapshot_file_sha256_candidates(revision.path):
            raise RuntimeError("selected snapshot SHA failed exact replay verification")
        try:
            snapshot = pd.read_csv(revision.path, dtype=str, keep_default_na=False)
        except Exception as exc:
            raise RuntimeError(f"failed to read selected snapshot: {revision.path}") from exc
        _validate_snapshot_frame(
            snapshot,
            metadata,
            report_date=revision.report_date,
            revision=revision.revision,
        )
        required_columns = {"signal_date", "stock_id", "model_id", "entry_basis"}
        missing = sorted(required_columns - set(snapshot.columns))
        if missing:
            raise RuntimeError(f"published model signal snapshot missing columns: {missing}")
        target = snapshot[snapshot["model_id"].astype(str).eq(MODEL_ID)].copy()
        target_count = len(target)
        for source_position, (frame_index, source_row) in enumerate(target.iterrows(), start=1):
            signal_date = _date(source_row.get("signal_date", ""))
            stock_id = normalize_code(source_row.get("stock_id", ""))
            if not signal_date or signal_date != revision.report_date:
                raise RuntimeError(
                    "published signal_date must equal snapshot_report_date: "
                    f"report_date={revision.report_date} row={frame_index + 1}"
                )
            if not stock_id:
                raise RuntimeError(
                    f"published pullback signal has blank stock_id: {revision.path_text}"
                )
            if safe_str(source_row.get("entry_basis")) != "signal_date_next_open":
                raise RuntimeError(
                    f"published pullback signal has unexpected entry_basis: {stock_id}/{signal_date}"
                )
            if stock_id not in price_cache:
                price_cache[stock_id] = _load_price_history(stock_id, price_dir)
            price, price_path, price_sha = price_cache[stock_id]
            replay = _forward_replay(price, signal_date)
            candidate_horizons = [
                f"D+{horizon}"
                for horizon in HORIZONS
                if replay[f"d{horizon}_anomaly_candidate"] == "True"
            ]
            rows.append(
                {
                    "artifact_version": ARTIFACT_VERSION,
                    "model_id": MODEL_ID,
                    "source_artifact_id": ARTIFACT_ID,
                    "snapshot_revision_policy": SNAPSHOT_REVISION_POLICY,
                    "snapshot_report_date": revision.report_date,
                    "snapshot_revision": revision.revision,
                    "snapshot_path": revision.path_text,
                    "snapshot_sha256": revision.snapshot_sha256,
                    "snapshot_manifest_sha256": manifest_sha,
                    "snapshot_pipeline_commit_sha": metadata["pipeline_commit_sha"],
                    "snapshot_total_row_count": len(snapshot),
                    "snapshot_total_column_count": len(snapshot.columns),
                    "snapshot_target_model_row_count": target_count,
                    "snapshot_csv_row_number": int(frame_index) + 2,
                    "target_model_row_ordinal": source_position,
                    "published_source_row_index": safe_str(source_row.get("source_row_index", "")),
                    "source_row_sha256": canonical_row_sha256(source_row),
                    "signal_semantic_sha256": _semantic_sha(source_row),
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "stock_name": safe_str(source_row.get("stock_name", "")),
                    "report_line": safe_str(source_row.get("report_line", "")),
                    "report_bucket": safe_str(source_row.get("report_bucket", "")),
                    "model_score": safe_str(source_row.get("model_score", "")),
                    "published_entry_basis": safe_str(source_row.get("entry_basis", "")),
                    "entry_rule": ENTRY_RULE,
                    "price_source_path": price_path,
                    "price_source_sha256": price_sha,
                    "price_source_sha256_basis": "raw_file_bytes",
                    "price_source_immutability_status": "mutable_current_file_unpinned",
                    "trading_calendar_status": "stock_price_row_sequence_only_no_market_calendar_proof",
                    "realized_price_basis": "next_open_to_fixed_future_close_no_intraday_high_low",
                    "return_cost_basis": "raw_return_before_costs_slippage_and_tax",
                    "statistical_trigger_status": "anomaly_candidate" if candidate_horizons else "not_triggered",
                    "anomaly_candidate_horizons": ";".join(candidate_horizons),
                    "anomaly_disposition": "unresolved_anomaly_candidate" if candidate_horizons else "not_applicable",
                    "anomaly_primary_metric_policy": "retained_in_primary_metrics",
                    "formal_use_allowed": "False",
                    "trade_eligible": "False",
                    "promotion_evidence_allowed": "False",
                    "operation_contract_status": OPERATION_CONTRACT_STATUS,
                    "operation_use_status": "research_outcome_replay_only_no_operation_contract",
                    "producer_source_sha256": producer_sha,
                    **replay,
                }
            )

    events = pd.DataFrame(rows)
    if events.empty:
        raise RuntimeError(f"latest snapshots contain no {MODEL_ID} rows")
    events = events.sort_values(
        ["signal_date", "stock_id", "snapshot_csv_row_number"]
    ).reset_index(drop=True)
    events["signal_event_id"] = events.apply(
        lambda row: hashlib.sha256(
            f"{MODEL_ID}|{row['signal_date']}|{row['stock_id']}".encode("utf-8")
        ).hexdigest(),
        axis=1,
    )
    for _, group in events.groupby("signal_event_id", sort=False):
        if group["signal_semantic_sha256"].nunique(dropna=False) != 1:
            first = group.iloc[0]
            raise RuntimeError(
                "duplicate published presentation rows disagree on signal semantics: "
                f"signal_date={first['signal_date']} stock_id={first['stock_id']}"
            )
        ordered_indices = list(group.sort_values("snapshot_csv_row_number").index)
        count = len(ordered_indices)
        for ordinal, index in enumerate(ordered_indices, start=1):
            events.at[index, "source_duplicate_ordinal"] = ordinal
            events.at[index, "source_duplicate_count"] = count
            events.at[index, "identity_disposition"] = (
                "canonical_signal_event"
                if ordinal == 1
                else "duplicate_report_presentation_row"
            )
            events.at[index, "primary_metric_included"] = _bool_text(ordinal == 1)
    events["source_duplicate_ordinal"] = events["source_duplicate_ordinal"].astype(int)
    events["source_duplicate_count"] = events["source_duplicate_count"].astype(int)

    timestamp = generated_at or _now_text()
    events["generated_at"] = timestamp
    anomalies = _build_anomalies(events)
    anomalies["generated_at"] = timestamp
    summary = _build_summary(events, timestamp)
    return ReplayBundle(events=events, summary=summary, anomalies=anomalies)


def _replay_output_paths(output_dir: Path) -> tuple[Path, Path, Path]:
    output_dir = Path(output_dir)
    return (
        output_dir / EVENTS_FILENAME,
        output_dir / SUMMARY_FILENAME,
        output_dir / ANOMALIES_FILENAME,
    )


def _preflight_model_owned_outputs(
    *, repository_root: Path, output_paths: tuple[Path, ...]
) -> None:
    root = repository_root.resolve()
    planned_paths: list[str] = []
    for output_path in output_paths:
        resolved = output_path.resolve()
        try:
            planned_paths.append(resolved.relative_to(root).as_posix())
        except ValueError as exc:
            raise RuntimeError(
                f"model-owned output path must stay within repository root: {resolved}"
            ) from exc
    registry_path = root / "config/model_research_artifact_ownership.csv"
    rules = load_ownership_rules(registry_path)
    errors = validate_changed_paths(MODEL_ID, PRODUCER, planned_paths, rules)
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise RuntimeError(
            f"model-owned artifact ownership preflight failed:\n{details}"
        )


def write_replay(bundle: ReplayBundle, output_dir: Path) -> tuple[Path, Path, Path]:
    events_path, summary_path, anomalies_path = _replay_output_paths(output_dir)
    write_csv(bundle.events, events_path)
    write_csv(bundle.summary, summary_path)
    write_csv(bundle.anomalies, anomalies_path)
    return events_path, summary_path, anomalies_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build pullback_short_reclaim exact published-signal research replay."
    )
    parser.add_argument(
        "--snapshot-dir",
        type=Path,
        default=ROOT / "output/history/daily_model_snapshots",
    )
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument(
        "--price-dir", type=Path, default=ROOT / "data/stock_price_history"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output/latest/research_backtest",
    )
    parser.add_argument("--through-date", default="")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    manifest_path = args.manifest or (
        args.snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    )
    planned_output_paths = _replay_output_paths(args.output_dir)
    registry_path = ROOT / "config/model_research_artifact_ownership.csv"
    sentinel_registry_path = ROOT / "config/model_research_protected_sentinels.csv"
    _preflight_model_owned_outputs(
        repository_root=ROOT,
        output_paths=planned_output_paths,
    )
    bundle = build_replay(
        snapshot_dir=args.snapshot_dir,
        manifest_path=manifest_path,
        price_dir=args.price_dir,
        through_date=args.through_date,
    )
    with model_owned_artifact_guard(
        MODEL_ID,
        PRODUCER,
        root=ROOT,
        registry_path=registry_path,
        sentinel_registry_path=sentinel_registry_path,
    ):
        paths = write_replay(bundle, args.output_dir)
    print("pullback_short_reclaim published-signal research replay built")
    print(f"source_rows={len(bundle.events)}")
    print(f"unique_signal_events={int(bundle.summary.iloc[0]['unique_signal_event_count'])}")
    for path in paths:
        print(path.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
