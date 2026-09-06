from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "hot_theme_pullback"
SCENARIOS = {
    "fixed_d5_close": 5,
    "fixed_d10_close": 10,
    "fixed_d20_close": 20,
}
LATEST_ROOT = ROOT / "output" / "latest" / "research_backtest"
EVENTS_PATH = LATEST_ROOT / "hot_theme_pullback_published_signal_events_latest.csv"
SUMMARY_PATH = LATEST_ROOT / "hot_theme_pullback_published_signal_summary_latest.csv"
ANOMALY_PATH = (
    LATEST_ROOT / "hot_theme_pullback_published_signal_anomaly_candidates_latest.csv"
)
MANIFEST_PATH = LATEST_ROOT / "hot_theme_pullback_published_signal_manifest_latest.csv"
SOURCE_MANIFEST_NAME = "daily_published_model_snapshot_manifest.csv"
SOURCE_ARTIFACT_ID = "model_signals_for_report"
SOURCE_PURPOSE = "as_published_daily_model_snapshot"
SOURCE_SIGNAL_REQUIRED_COLUMNS = {
    "signal_date",
    "stock_id",
    "stock_name",
    "model_id",
    "model_score",
}
SOURCE_MANIFEST_REQUIRED_COLUMNS = {
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "pipeline_commit_sha",
    "artifact_id",
    "snapshot_path",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
}
REVISION_POLICY = "latest_revision_per_report_date_artifact"
FULL_REPLAY_BLOCKER = "blocked_missing_point_in_time_hot_theme_labels"
BOOLEAN_CONTRACT_FIELDS = {
    "events": (
        "return_valid",
        "right_censored",
        "primary_metric_included",
        "anomaly_candidate_flag",
        "formal_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "research_only",
    ),
    "summary": (
        "primary_metrics_retain_unresolved_candidates",
        "sensitivity_is_corrected_primary",
        "formal_use_allowed",
    ),
    "manifest": (
        "production_condition_recalculated",
        "formal_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "promotion_evidence_allowed",
        "production_change",
    ),
}
EVENT_ARTIFACT_COLUMNS = (
    "artifact_version",
    "model_id",
    "signal_event_key",
    "signal_date",
    "stock_id",
    "stock_name",
    "model_score",
    "model_rank",
    "report_bucket_memberships",
    "source_signal_row_count",
    "source_signal_row_sha256s",
    "source_signal_row_set_sha256",
    "snapshot_report_date",
    "snapshot_revision",
    "snapshot_revision_policy",
    "snapshot_path",
    "snapshot_sha256",
    "snapshot_manifest_row_sha256",
    "snapshot_pipeline_commit_sha",
    "scenario_id",
    "horizon_sessions",
    "entry_price_basis",
    "exit_price_basis",
    "price_source_path",
    "price_source_sha256",
    "entry_date",
    "entry_open_price",
    "exit_date",
    "exit_close_price",
    "entry_price_row_sha256",
    "exit_price_row_sha256",
    "return_valid",
    "right_censored",
    "invalid_reason",
    "gross_return_pct",
    "return_outcome",
    "primary_metric_included",
    "anomaly_candidate_flag",
    "anomaly_candidate_kinds",
    "anomaly_disposition",
    "formal_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "operation_contract_status",
    "full_historical_condition_replay_status",
    "research_only",
    "event_row_canonical_sha256",
)
SUMMARY_ARTIFACT_COLUMNS = (
    "artifact_version",
    "model_id",
    "analysis_scope",
    "scenario_id",
    "horizon_sessions",
    "entry_basis",
    "exit_basis",
    "signal_event_count",
    "mature_count",
    "right_censored_count",
    "invalid_count",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "high_return_threshold_pct",
    "high_return_hit_rate_pct",
    "loss_rate_pct",
    "anomaly_candidate_count",
    "unresolved_anomaly_count",
    "primary_metrics_retain_unresolved_candidates",
    "candidate_exclusion_sensitivity_count",
    "candidate_exclusion_sensitivity_win_rate_pct",
    "candidate_exclusion_sensitivity_avg_return_pct",
    "sensitivity_is_corrected_primary",
    "formal_use_allowed",
    "operation_contract_status",
    "full_historical_condition_replay_status",
    "research_status",
)
MANIFEST_FRAME_COLUMNS = (
    "artifact_version",
    "model_id",
    "producer_path",
    "producer_canonical_sha256",
    "evidence_basis",
    "production_condition_recalculated",
    "snapshot_revision_policy",
    "source_manifest_path",
    "source_manifest_sha256",
    "selected_snapshot_count",
    "selected_snapshot_date_min",
    "selected_snapshot_date_max",
    "selected_snapshot_bundle_sha256",
    "price_input_file_count",
    "price_input_bundle_sha256",
    "signal_event_count",
    "scenario_event_count",
    "events_row_set_sha256",
    "summary_row_set_sha256",
    "anomaly_candidate_count",
    "effective_anomaly_blocker_count",
    "semantic_version_binding_status",
    "full_historical_condition_replay_status",
    "operation_contract_status",
    "formal_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "promotion_evidence_allowed",
    "production_change",
)
MANIFEST_ARTIFACT_COLUMNS = MANIFEST_FRAME_COLUMNS + (
    "events_path",
    "events_file_sha256",
    "events_row_count",
    "summary_path",
    "summary_file_sha256",
    "summary_row_count",
    "anomalies_path",
    "anomalies_file_sha256",
    "anomalies_row_count",
    "evidence_payload_bundle_sha256",
)


def _text(value: Any) -> str:
    if value is None:
        return ""
    result = str(value).strip()
    return "" if result.lower() == "nan" else result


def _date(value: Any) -> str:
    text = "" if value is None else str(value)
    if len(text) != 8 or not text.isdigit():
        return ""
    try:
        parsed = datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return ""
    return text if parsed.strftime("%Y%m%d") == text else ""


def _code(value: Any) -> str:
    value_text = _text(value)
    if value_text.endswith(".0") and value_text[:-2].isdigit():
        value_text = value_text[:-2]
    return value_text.zfill(4) if value_text.isdigit() and len(value_text) < 4 else value_text


def _true(value: Any) -> bool:
    return _text(value).lower() in {"true", "1", "1.0", "yes", "y"}


def _canonical_text_sha256(path: Path) -> str:
    decoded = path.read_bytes().decode("utf-8-sig")
    payload = decoded.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    values.pop("event_row_canonical_sha256", None)
    normalized = {str(key): _text(value) for key, value in values.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _row_set_sha256(values: list[str]) -> str:
    payload = "\n".join(sorted(_text(value) for value in values if _text(value))) + "\n"
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def _published_hash_candidates(path: Path) -> set[str]:
    raw = path.read_bytes()
    lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(payload).hexdigest() for payload in (raw, lf, crlf)}


def _revision_number(value: Any) -> int:
    revision = _text(value).lower()
    if revision.startswith("r") and revision[1:].isdigit():
        return int(revision[1:])
    raise RuntimeError(f"invalid snapshot revision: {value!r}")


def _read_csv_frame(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing CSV: {path.as_posix()}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def _exact_header_errors(
    artifact_name: str,
    frame: pd.DataFrame,
    expected_columns: tuple[str, ...],
) -> list[str]:
    observed_columns = tuple(str(column) for column in frame.columns)
    if observed_columns == expected_columns:
        return []
    expected_set = set(expected_columns)
    observed_set = set(observed_columns)
    missing = [column for column in expected_columns if column not in observed_set]
    extra = [column for column in observed_columns if column not in expected_set]
    errors: list[str] = []
    if missing:
        errors.append(f"{artifact_name} artifact header missing columns: {missing}")
    if extra:
        errors.append(
            f"{artifact_name} artifact header has unexpected columns: {extra}"
        )
    if not missing and not extra:
        errors.append(
            f"{artifact_name} artifact header column order mismatch: "
            f"expected={list(expected_columns)}; observed={list(observed_columns)}"
        )
    return errors


def _display_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _path(root: Path, value: Any) -> Path:
    path = Path(_text(value))
    return path if path.is_absolute() else root / path


def _close(left: Any, right: Any, tolerance: float = 1e-7) -> bool:
    try:
        return math.isclose(float(left), float(right), rel_tol=0, abs_tol=tolerance)
    except (TypeError, ValueError):
        return _text(left) == _text(right)


def _load_price(path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing price history: {path.as_posix()}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {"date", "open", "high", "low", "close"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"price history missing required columns: {path.as_posix()}; {missing}"
        )
    if frame.empty:
        raise RuntimeError(f"empty price history: {path.as_posix()}")
    frame = frame.copy()
    frame["date"] = frame["date"].map(_date)
    parsed_dates = pd.to_datetime(frame["date"], format="%Y%m%d", errors="coerce")
    if frame["date"].eq("").any() or parsed_dates.isna().any():
        raise RuntimeError(f"price history contains invalid date: {path.as_posix()}")
    if frame["date"].duplicated(keep=False).any():
        duplicates = sorted(
            set(frame.loc[frame["date"].duplicated(keep=False), "date"].astype(str))
        )
        raise RuntimeError(
            f"price history contains duplicate date: {path.as_posix()}; {duplicates}"
        )
    for column in ["open", "high", "low", "close"]:
        numeric = pd.to_numeric(frame[column], errors="coerce")
        if (
            numeric.isna().any()
            or not numeric.map(math.isfinite).all()
            or (numeric <= 0).any()
        ):
            raise RuntimeError(
                f"price history contains invalid required price: "
                f"{path.as_posix()}; column={column}"
            )
        frame[column] = numeric
    return frame.sort_values("date").reset_index(drop=True)


def _source_manifest_path(manifest: pd.DataFrame, root: Path) -> Path:
    if "source_manifest_path" not in manifest.columns:
        raise RuntimeError("research manifest missing source_manifest_path")
    values = sorted({_text(value) for value in manifest["source_manifest_path"] if _text(value)})
    if len(values) != 1:
        raise RuntimeError(
            f"research manifest must bind exactly one source manifest: observed={values}"
        )
    path = _path(root, values[0]).resolve()
    if path.name != SOURCE_MANIFEST_NAME:
        raise RuntimeError(f"unexpected source manifest filename: {path.name}")
    approved_root = (
        root / "output" / "history" / "daily_model_snapshots"
    ).resolve()
    if path.parent != approved_root:
        raise RuntimeError(
            f"source manifest is outside registered snapshot root: {path.as_posix()}"
        )
    if not path.is_file():
        raise RuntimeError(f"missing source manifest: {path.as_posix()}")
    if "source_manifest_sha256" not in manifest.columns:
        raise RuntimeError("research manifest missing source_manifest_sha256")
    expected_sha = _canonical_text_sha256(path)
    if not manifest["source_manifest_sha256"].astype(str).eq(expected_sha).all():
        raise RuntimeError("source manifest canonical SHA mismatch")
    return path


def _rebuild_source_bases(
    source_manifest_path: Path,
    root: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    source_manifest = _read_csv_frame(source_manifest_path)
    missing = sorted(SOURCE_MANIFEST_REQUIRED_COLUMNS - set(source_manifest.columns))
    if missing:
        raise RuntimeError(f"snapshot manifest missing columns: {missing}")
    scoped = source_manifest[
        source_manifest["artifact_id"].astype(str).eq(SOURCE_ARTIFACT_ID)
        & source_manifest["purpose"].astype(str).eq(SOURCE_PURPOSE)
    ].copy()
    if scoped.empty:
        raise RuntimeError("snapshot manifest contains no formal model signal rows")
    scoped["snapshot_report_date"] = scoped["snapshot_report_date"].map(_date)
    scoped["_revision_number"] = scoped["snapshot_revision"].map(_revision_number)
    if scoped["snapshot_report_date"].eq("").any():
        raise RuntimeError("snapshot manifest has invalid report dates")
    if scoped.duplicated(["snapshot_report_date", "_revision_number"]).any():
        raise RuntimeError("snapshot manifest has duplicate report-date revisions")

    approved_snapshot_root = source_manifest_path.parent.resolve()
    selected: list[dict[str, Any]] = []
    for report_date, revisions in scoped.groupby("snapshot_report_date", sort=True):
        ordered = revisions.sort_values("_revision_number")
        actual = ordered["_revision_number"].astype(int).tolist()
        expected = list(range(1, len(ordered) + 1))
        if actual != expected:
            raise RuntimeError(
                f"snapshot revision chain is not contiguous: "
                f"date={report_date}; revisions={actual}"
            )
        prior_sha = ""
        seen_declared_sha: set[str] = set()
        seen_canonical_sha: set[str] = set()
        chosen: dict[str, Any] | None = None
        for _, manifest_row in ordered.iterrows():
            revision_number = int(manifest_row["_revision_number"])
            declared_sha = _text(manifest_row["snapshot_sha256"]).lower()
            if len(declared_sha) != 64 or any(
                character not in "0123456789abcdef" for character in declared_sha
            ):
                raise RuntimeError(
                    f"invalid snapshot SHA: date={report_date}; "
                    f"revision={manifest_row['snapshot_revision']}"
                )
            supersedes = _text(manifest_row["supersedes_snapshot_sha256"]).lower()
            if revision_number == 1 and supersedes:
                raise RuntimeError(
                    f"r1 supersedes hash must be empty: date={report_date}"
                )
            if revision_number > 1 and supersedes != prior_sha:
                raise RuntimeError(
                    f"snapshot supersession mismatch: date={report_date}; "
                    f"revision={manifest_row['snapshot_revision']}"
                )
            snapshot_path = _path(root, manifest_row["snapshot_path"]).resolve()
            try:
                snapshot_path.relative_to(approved_snapshot_root)
            except ValueError as exc:
                raise RuntimeError(
                    f"snapshot escaped registered root: {snapshot_path.as_posix()}"
                ) from exc
            snapshot = _read_csv_frame(snapshot_path)
            if declared_sha not in _published_hash_candidates(snapshot_path):
                raise RuntimeError(f"snapshot SHA mismatch: {snapshot_path.as_posix()}")
            canonical_sha = _canonical_text_sha256(snapshot_path)
            if declared_sha in seen_declared_sha or canonical_sha in seen_canonical_sha:
                raise RuntimeError(
                    f"duplicate snapshot payload revision: "
                    f"date={report_date}; revision={manifest_row['snapshot_revision']}"
                )
            try:
                row_count = int(_text(manifest_row["row_count"]))
                column_count = int(_text(manifest_row["column_count"]))
            except ValueError as exc:
                raise RuntimeError(
                    f"invalid snapshot dimensions: {snapshot_path.as_posix()}"
                ) from exc
            if row_count != len(snapshot):
                raise RuntimeError(f"snapshot row count mismatch: {snapshot_path.as_posix()}")
            if column_count != len(snapshot.columns):
                raise RuntimeError(
                    f"snapshot column count mismatch: {snapshot_path.as_posix()}"
                )
            missing_signal = sorted(
                SOURCE_SIGNAL_REQUIRED_COLUMNS - set(snapshot.columns)
            )
            if missing_signal:
                raise RuntimeError(
                    f"signal snapshot missing columns: {snapshot_path}; {missing_signal}"
                )
            manifest_values = {
                key: manifest_row[key]
                for key in source_manifest.columns
                if not key.startswith("_")
            }
            manifest_values["snapshot_revision_policy"] = REVISION_POLICY
            chosen = {
                "report_date": report_date,
                "revision": _text(manifest_row["snapshot_revision"]),
                "path": snapshot_path,
                "canonical_sha": canonical_sha,
                "pipeline_commit_sha": _text(manifest_row["pipeline_commit_sha"]),
                "manifest_row_sha": _canonical_row_sha256(manifest_values),
                "snapshot": snapshot,
            }
            prior_sha = declared_sha
            seen_declared_sha.add(declared_sha)
            seen_canonical_sha.add(canonical_sha)
        if chosen is None:
            raise RuntimeError(f"no selected snapshot revision: date={report_date}")
        selected.append(chosen)

    bases: dict[str, dict[str, Any]] = {}
    for revision in selected:
        snapshot = revision["snapshot"]
        target = snapshot[snapshot["model_id"].astype(str).eq(MODEL_ID)].copy()
        if target.empty:
            continue
        target["_signal_date"] = target["signal_date"].map(_date)
        target["_stock_id"] = target["stock_id"].map(_code)
        if target["_signal_date"].eq("").any() or target["_stock_id"].eq("").any():
            raise RuntimeError(
                f"invalid model signal identity: {revision['path'].as_posix()}"
            )
        if not target["_signal_date"].eq(revision["report_date"]).all():
            raise RuntimeError(
                f"signal date differs from snapshot report date: "
                f"{revision['path'].as_posix()}"
            )
        for (signal_date, stock_id), rows in target.groupby(
            ["_signal_date", "_stock_id"], sort=True
        ):
            sort_columns = [
                column for column in ["report_bucket", "model_rank"] if column in rows
            ]
            ordered = rows.sort_values(sort_columns) if sort_columns else rows
            representative = ordered.iloc[0]
            source_hashes = sorted(
                _canonical_row_sha256(row) for _, row in rows.iterrows()
            )
            report_buckets = (
                rows["report_bucket"].tolist() if "report_bucket" in rows else []
            )
            event_key = f"{MODEL_ID}|{signal_date}|{stock_id}"
            if event_key in bases:
                raise RuntimeError(f"duplicate rebuilt signal event key: {event_key}")
            bases[event_key] = {
                "signal_event_key": event_key,
                "signal_date": signal_date,
                "stock_id": stock_id,
                "stock_name": _text(representative.get("stock_name", "")),
                "model_score": _text(representative.get("model_score", "")),
                "model_rank": _text(representative.get("model_rank", "")),
                "report_bucket_memberships": "|".join(
                    sorted({_text(value) for value in report_buckets if _text(value)})
                ),
                "source_signal_row_count": str(len(rows)),
                "source_signal_row_sha256s": "|".join(source_hashes),
                "source_signal_row_set_sha256": _row_set_sha256(source_hashes),
                "snapshot_report_date": revision["report_date"],
                "snapshot_revision": revision["revision"],
                "snapshot_revision_policy": REVISION_POLICY,
                "snapshot_path_resolved": revision["path"],
                "snapshot_sha256": revision["canonical_sha"],
                "snapshot_manifest_row_sha256": revision["manifest_row_sha"],
                "snapshot_pipeline_commit_sha": revision["pipeline_commit_sha"],
            }
    stats = {
        "selected_snapshot_count": len(selected),
        "selected_snapshot_date_min": min(
            revision["report_date"] for revision in selected
        ),
        "selected_snapshot_date_max": max(
            revision["report_date"] for revision in selected
        ),
        "selected_snapshot_hashes": sorted(
            {revision["canonical_sha"] for revision in selected}
        ),
    }
    return bases, stats


def _required_columns() -> dict[str, set[str]]:
    return {
        "events": {
            "model_id",
            "signal_event_key",
            "signal_date",
            "stock_id",
            "stock_name",
            "model_score",
            "model_rank",
            "report_bucket_memberships",
            "source_signal_row_count",
            "source_signal_row_sha256s",
            "source_signal_row_set_sha256",
            "snapshot_report_date",
            "snapshot_revision",
            "snapshot_revision_policy",
            "snapshot_path",
            "snapshot_sha256",
            "snapshot_manifest_row_sha256",
            "snapshot_pipeline_commit_sha",
            "scenario_id",
            "horizon_sessions",
            "entry_price_basis",
            "exit_price_basis",
            "price_source_path",
            "price_source_sha256",
            "entry_date",
            "entry_open_price",
            "exit_date",
            "exit_close_price",
            "entry_price_row_sha256",
            "exit_price_row_sha256",
            "return_valid",
            "right_censored",
            "invalid_reason",
            "gross_return_pct",
            "return_outcome",
            "primary_metric_included",
            "anomaly_candidate_flag",
            "anomaly_candidate_kinds",
            "anomaly_disposition",
            "formal_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "research_only",
            "operation_contract_status",
            "full_historical_condition_replay_status",
            "event_row_canonical_sha256",
        },
        "summary": {
            "model_id",
            "scenario_id",
            "horizon_sessions",
            "signal_event_count",
            "mature_count",
            "right_censored_count",
            "invalid_count",
            "unique_stock_count",
            "win_count",
            "neutral_count",
            "failure_count",
            "win_rate_pct",
            "neutral_rate_pct",
            "failure_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "high_return_hit_rate_pct",
            "loss_rate_pct",
            "anomaly_candidate_count",
            "unresolved_anomaly_count",
            "primary_metrics_retain_unresolved_candidates",
            "candidate_exclusion_sensitivity_count",
            "candidate_exclusion_sensitivity_win_rate_pct",
            "candidate_exclusion_sensitivity_avg_return_pct",
            "sensitivity_is_corrected_primary",
            "formal_use_allowed",
            "operation_contract_status",
            "full_historical_condition_replay_status",
            "research_status",
        },
        "manifest": {
            "model_id",
            "producer_path",
            "producer_canonical_sha256",
            "evidence_basis",
            "production_condition_recalculated",
            "snapshot_revision_policy",
            "source_manifest_path",
            "source_manifest_sha256",
            "selected_snapshot_count",
            "selected_snapshot_date_min",
            "selected_snapshot_date_max",
            "selected_snapshot_bundle_sha256",
            "price_input_file_count",
            "price_input_bundle_sha256",
            "signal_event_count",
            "scenario_event_count",
            "events_row_set_sha256",
            "summary_row_set_sha256",
            "anomaly_candidate_count",
            "effective_anomaly_blocker_count",
            "semantic_version_binding_status",
            "operation_contract_status",
            "full_historical_condition_replay_status",
            "formal_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "promotion_evidence_allowed",
            "production_change",
        },
    }


def validate_frames(
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomalies: pd.DataFrame,
    manifest: pd.DataFrame,
    *,
    root: Path = ROOT,
    manifest_is_bound_artifact: bool = False,
) -> list[str]:
    errors: list[str] = []
    expected_headers = {
        "events": EVENT_ARTIFACT_COLUMNS,
        "summary": SUMMARY_ARTIFACT_COLUMNS,
        "anomalies": EVENT_ARTIFACT_COLUMNS,
        "manifest": (
            MANIFEST_ARTIFACT_COLUMNS
            if manifest_is_bound_artifact
            else MANIFEST_FRAME_COLUMNS
        ),
    }
    for name, frame in {
        "events": events,
        "summary": summary,
        "anomalies": anomalies,
        "manifest": manifest,
    }.items():
        errors.extend(_exact_header_errors(name, frame, expected_headers[name]))
    if errors:
        return errors
    if len(manifest) != 1:
        errors.append(f"manifest must contain exactly one row: observed={len(manifest)}")
        return errors
    if events.empty or summary.empty:
        errors.append("events and summary must be non-empty")
        return errors
    frames = {"events": events, "summary": summary, "manifest": manifest}
    token_errors: list[str] = []
    for surface, fields in BOOLEAN_CONTRACT_FIELDS.items():
        frame = frames[surface]
        for field in fields:
            invalid = sorted(
                {
                    "" if value is None else str(value)
                    for value in frame[field]
                    if ("" if value is None else str(value))
                    not in {"True", "False"}
                }
            )
            if invalid:
                token_errors.append(
                    f"{surface} {field} must use exact True/False tokens: "
                    f"observed={invalid}"
                )
    if token_errors:
        errors.extend(token_errors)
        return errors
    if not events["model_id"].astype(str).eq(MODEL_ID).all():
        errors.append("events contain a different model_id")
    if not summary["model_id"].astype(str).eq(MODEL_ID).all():
        errors.append("summary contains a different model_id")
    if not manifest["model_id"].astype(str).eq(MODEL_ID).all():
        errors.append("manifest contains a different model_id")
    if events.duplicated(["signal_event_key", "scenario_id"]).any():
        errors.append("duplicate signal/scenario rows")

    try:
        source_manifest = _source_manifest_path(manifest, root)
        expected_bases, source_stats = _rebuild_source_bases(source_manifest, root)
    except (OSError, RuntimeError, UnicodeDecodeError, ValueError) as exc:
        errors.append(str(exc))
        return errors
    observed_keys = set(events["signal_event_key"].astype(str))
    expected_keys = set(expected_bases)
    if observed_keys != expected_keys:
        errors.append(
            "published signal membership mismatch: "
            f"missing={sorted(expected_keys - observed_keys)}; "
            f"extra={sorted(observed_keys - expected_keys)}"
        )
    source_fields = [
        "signal_event_key",
        "signal_date",
        "stock_id",
        "stock_name",
        "model_score",
        "model_rank",
        "report_bucket_memberships",
        "source_signal_row_count",
        "source_signal_row_sha256s",
        "source_signal_row_set_sha256",
        "snapshot_report_date",
        "snapshot_revision",
        "snapshot_revision_policy",
        "snapshot_sha256",
        "snapshot_manifest_row_sha256",
        "snapshot_pipeline_commit_sha",
    ]
    for signal_key in sorted(observed_keys & expected_keys):
        expected_base = expected_bases[signal_key]
        part = events[events["signal_event_key"].astype(str).eq(signal_key)]
        for field in source_fields:
            observed_values = {_text(value) for value in part[field]}
            expected_value = _text(expected_base[field])
            if observed_values != {expected_value}:
                errors.append(
                    f"signal {signal_key} source field {field} mismatch: "
                    f"observed={sorted(observed_values)} expected={expected_value!r}"
                )
        for snapshot_value in part["snapshot_path"]:
            if _path(root, snapshot_value).resolve() != expected_base[
                "snapshot_path_resolved"
            ]:
                errors.append(f"signal {signal_key} snapshot path mismatch")

    expected_scenarios = set(SCENARIOS)
    for signal_key, part in events.groupby("signal_event_key"):
        observed = set(part["scenario_id"].astype(str))
        if observed != expected_scenarios:
            errors.append(
                f"signal event does not contain every fixed scenario: {signal_key}; "
                f"observed={sorted(observed)}"
            )

    price_cache: dict[str, pd.DataFrame] = {}
    for index, row in events.iterrows():
        scenario = _text(row["scenario_id"])
        if scenario not in SCENARIOS:
            errors.append(f"event {index} has unsupported scenario: {scenario}")
            continue
        horizon = SCENARIOS[scenario]
        try:
            observed_horizon = int(float(row["horizon_sessions"]))
        except (TypeError, ValueError):
            observed_horizon = -1
        if observed_horizon != horizon:
            errors.append(f"event {index} horizon differs from scenario")
        if _text(row["entry_price_basis"]) != "next_trading_day_open":
            errors.append(f"event {index} has invalid entry basis")
        if _text(row["exit_price_basis"]) != f"d{horizon}_close":
            errors.append(f"event {index} has invalid exit basis")
        if _true(row["formal_use_allowed"]):
            errors.append(f"event {index} improperly allows formal use")
        if _true(row["anomaly_candidate_flag"]) and not _true(
            row["primary_metric_included"]
        ):
            errors.append(f"event {index} excludes unresolved candidate from primary")
        if _true(row["approved_for_daily"]):
            errors.append(f"event {index} improperly allows daily approval")
        if _true(row["presentation_allowed"]):
            errors.append(f"event {index} improperly allows presentation")
        if not _true(row["research_only"]):
            errors.append(f"event {index} must remain research only")
        if _text(row["operation_contract_status"]) != "decision_required":
            errors.append(f"event {index} operation contract is not fail closed")
        if _text(row["full_historical_condition_replay_status"]) != FULL_REPLAY_BLOCKER:
            errors.append(f"event {index} full replay blocker mismatch")
        expected_hash = _canonical_row_sha256(row)
        if _text(row["event_row_canonical_sha256"]) != expected_hash:
            errors.append(f"event {index} canonical row hash mismatch")

        expected_price_path = (
            root / "data" / "stock_price_history" / f"{_code(row['stock_id'])}.csv"
        ).resolve()
        price_path = _path(root, row["price_source_path"]).resolve()
        if price_path != expected_price_path:
            errors.append(f"event {index} price source path mismatch")
        if not price_path.is_file():
            errors.append(f"event {index} price source is missing")
            continue
        if _text(row["price_source_sha256"]) != _canonical_text_sha256(price_path):
            errors.append(f"event {index} price source hash mismatch")
        cache_key = price_path.as_posix()
        if cache_key not in price_cache:
            try:
                price_cache[cache_key] = _load_price(price_path)
            except (OSError, RuntimeError, UnicodeDecodeError, ValueError) as exc:
                errors.append(str(exc))
                continue
        price = price_cache[cache_key]
        future = price[price["date"].astype(str) > _date(row["signal_date"])].reset_index(
            drop=True
        )
        if future.empty:
            censored_checks = {
                "return_valid": "False",
                "right_censored": "True",
                "invalid_reason": "missing_next_trading_day",
                "entry_date": "",
                "entry_open_price": "",
                "exit_date": "",
                "exit_close_price": "",
                "gross_return_pct": "",
                "return_outcome": "not_mature",
                "primary_metric_included": "False",
            }
            for field, expected in censored_checks.items():
                if _text(row[field]) != expected:
                    errors.append(
                        f"event {index} no-next-day field {field} mismatch"
                    )
            continue
        entry = future.iloc[0]
        if _date(row["entry_date"]) != _text(entry["date"]):
            errors.append(f"event {index} entry date mismatch")
        if not _close(row["entry_open_price"], entry["open"]):
            errors.append(f"event {index} entry price mismatch")
        if _text(row["entry_price_row_sha256"]) != _canonical_row_sha256(entry):
            errors.append(f"event {index} entry price-row hash mismatch")
        if len(future) < horizon:
            censored_checks = {
                "return_valid": "False",
                "right_censored": "True",
                "invalid_reason": f"right_censored_before_d{horizon}",
                "exit_date": "",
                "exit_close_price": "",
                "exit_price_row_sha256": "",
                "gross_return_pct": "",
                "return_outcome": "not_mature",
                "primary_metric_included": "False",
            }
            for field, expected in censored_checks.items():
                if _text(row[field]) != expected:
                    errors.append(
                        f"event {index} right-censored field {field} mismatch"
                    )
            continue
        exit_row = future.iloc[horizon - 1]
        if _date(row["exit_date"]) != _text(exit_row["date"]):
            errors.append(f"event {index} exit date mismatch")
        if not _close(row["exit_close_price"], exit_row["close"]):
            errors.append(f"event {index} exit price mismatch")
        if _text(row["exit_price_row_sha256"]) != _canonical_row_sha256(exit_row):
            errors.append(f"event {index} exit price-row hash mismatch")
        expected_return = (float(exit_row["close"]) / float(entry["open"]) - 1.0) * 100
        if not _close(row["gross_return_pct"], expected_return):
            errors.append(f"event {index} return formula mismatch")
        expected_outcome = (
            "win" if expected_return > 0 else "failure" if expected_return < 0 else "neutral"
        )
        if _text(row["return_outcome"]) != expected_outcome:
            errors.append(f"event {index} outcome mismatch")
        mature_checks = {
            "return_valid": "True",
            "right_censored": "False",
            "invalid_reason": "",
            "primary_metric_included": "True",
        }
        for field, expected in mature_checks.items():
            if _text(row[field]) != expected:
                errors.append(f"event {index} mature field {field} mismatch")

    independently_flagged_indexes: set[Any] = set()
    expected_anomaly_kinds: dict[Any, str] = {}
    for scenario_id in SCENARIOS:
        part = events[
            events["scenario_id"].astype(str).eq(scenario_id)
            & events["return_valid"].map(_true)
        ]
        values = pd.to_numeric(part["gross_return_pct"], errors="coerce").dropna()
        if values.empty:
            continue
        q1 = float(values.quantile(0.25))
        q3 = float(values.quantile(0.75))
        iqr = q3 - q1
        absolute_total = float(values.abs().sum())
        for event_index, value in values.items():
            triggers: list[str] = []
            if abs(float(value)) >= 30.0:
                triggers.append("absolute_return_30pct")
            if iqr > 0 and (
                float(value) < q1 - 6 * iqr or float(value) > q3 + 6 * iqr
            ):
                triggers.append("six_iqr_distance")
            if (
                len(values) >= 10
                and absolute_total > 0
                and abs(float(value)) / absolute_total >= 0.10
            ):
                triggers.append("absolute_contribution_10pct")
            if triggers:
                independently_flagged_indexes.add(event_index)
                expected_anomaly_kinds[event_index] = "|".join(triggers)
    for event_index, row in events.iterrows():
        expected_flag = event_index in independently_flagged_indexes
        if _true(row["anomaly_candidate_flag"]) != expected_flag:
            errors.append(f"event {event_index} anomaly candidate flag mismatch")
        expected_kinds = expected_anomaly_kinds.get(event_index, "")
        if _text(row["anomaly_candidate_kinds"]) != expected_kinds:
            errors.append(f"event {event_index} anomaly trigger kinds mismatch")
        expected_disposition = (
            "unresolved_anomaly_candidate" if expected_flag else "not_triggered"
        )
        if _text(row["anomaly_disposition"]) != expected_disposition:
            errors.append(f"event {event_index} anomaly disposition mismatch")

    expected_anomaly_hashes = set(
        events.loc[list(independently_flagged_indexes), "event_row_canonical_sha256"].astype(
            str
        )
    )
    observed_anomaly_hashes = (
        set(anomalies["event_row_canonical_sha256"].astype(str))
        if "event_row_canonical_sha256" in anomalies.columns
        else set()
    )
    if list(anomalies.columns) != list(events.columns):
        errors.append("anomaly artifact schema differs from event artifact")
    if (
        expected_anomaly_hashes != observed_anomaly_hashes
        or len(anomalies) != len(independently_flagged_indexes)
    ):
        errors.append("anomaly artifact does not match flagged event rows")
    elif list(anomalies.columns) == list(events.columns):
        expected_anomaly_rows = events.loc[
            list(independently_flagged_indexes)
        ].sort_values("event_row_canonical_sha256").reset_index(drop=True)
        observed_anomaly_rows = anomalies.sort_values(
            "event_row_canonical_sha256"
        ).reset_index(drop=True)
        for row_number, (expected_row, observed_row) in enumerate(
            zip(
                expected_anomaly_rows.to_dict(orient="records"),
                observed_anomaly_rows.to_dict(orient="records"),
            ),
            start=2,
        ):
            for field in events.columns:
                if _text(observed_row.get(field)) != _text(expected_row.get(field)):
                    errors.append(
                        f"anomaly row {row_number} field {field} differs "
                        "from canonical event row"
                    )
    if not anomalies.empty:
        if not anomalies["anomaly_disposition"].astype(str).eq(
            "unresolved_anomaly_candidate"
        ).all():
            errors.append("numerical candidates received a final disposition")
        if not anomalies["primary_metric_included"].map(_true).all():
            errors.append("anomaly artifact excludes candidates from primary metrics")

    if len(summary) != len(SCENARIOS):
        errors.append(
            f"summary row count mismatch: observed={len(summary)} "
            f"expected={len(SCENARIOS)}"
        )
    for scenario_id, horizon in SCENARIOS.items():
        event_part = events[events["scenario_id"].astype(str).eq(scenario_id)]
        mature = event_part[event_part["return_valid"].map(_true)]
        returns = pd.to_numeric(mature["gross_return_pct"], errors="coerce").dropna()
        sensitivity = mature[~mature["anomaly_candidate_flag"].map(_true)]
        sensitivity_returns = pd.to_numeric(
            sensitivity["gross_return_pct"], errors="coerce"
        ).dropna()
        summary_part = summary[summary["scenario_id"].astype(str).eq(scenario_id)]
        if len(summary_part) != 1:
            errors.append(f"summary must have one row for {scenario_id}")
            continue
        row = summary_part.iloc[0]
        wins = int((returns > 0).sum())
        neutral = int((returns == 0).sum())
        failures = int((returns < 0).sum())
        checks = {
            "horizon_sessions": horizon,
            "signal_event_count": len(expected_bases),
            "mature_count": len(returns),
            "right_censored_count": int(
                event_part["right_censored"].map(_true).sum()
            ),
            "invalid_count": int(
                (
                    ~event_part["return_valid"].map(_true)
                    & ~event_part["right_censored"].map(_true)
                ).sum()
            ),
            "unique_stock_count": mature["stock_id"].nunique(),
            "win_count": wins,
            "neutral_count": neutral,
            "failure_count": failures,
            "anomaly_candidate_count": int(
                mature["anomaly_candidate_flag"].map(_true).sum()
            ),
            "unresolved_anomaly_count": int(
                mature["anomaly_candidate_flag"].map(_true).sum()
            ),
            "candidate_exclusion_sensitivity_count": len(sensitivity_returns),
        }
        for column, expected in checks.items():
            if int(float(row[column])) != expected:
                errors.append(f"summary {scenario_id} {column} mismatch")
        metric_checks = {
            "win_rate_pct": wins / len(returns) * 100 if len(returns) else "",
            "neutral_rate_pct": (
                neutral / len(returns) * 100 if len(returns) else ""
            ),
            "failure_rate_pct": (
                failures / len(returns) * 100 if len(returns) else ""
            ),
            "avg_return_pct": returns.mean() if len(returns) else "",
            "median_return_pct": returns.median() if len(returns) else "",
            "high_return_hit_rate_pct": (
                int((returns >= 10.0).sum()) / len(returns) * 100
                if len(returns)
                else ""
            ),
            "loss_rate_pct": (
                failures / len(returns) * 100 if len(returns) else ""
            ),
            "candidate_exclusion_sensitivity_win_rate_pct": (
                int((sensitivity_returns > 0).sum())
                / len(sensitivity_returns)
                * 100
                if len(sensitivity_returns)
                else ""
            ),
            "candidate_exclusion_sensitivity_avg_return_pct": (
                sensitivity_returns.mean() if len(sensitivity_returns) else ""
            ),
        }
        for column, expected in metric_checks.items():
            if not _close(row[column], expected):
                errors.append(f"summary {scenario_id} {column} mismatch")
        if not _true(row["primary_metrics_retain_unresolved_candidates"]):
            errors.append(f"summary {scenario_id} does not retain unresolved candidates")
        if _true(row["sensitivity_is_corrected_primary"]):
            errors.append(f"summary {scenario_id} mislabels sensitivity as primary")
        if _true(row["formal_use_allowed"]):
            errors.append(f"summary {scenario_id} improperly allows formal use")
        if _text(row["operation_contract_status"]) != "decision_required":
            errors.append(f"summary {scenario_id} operation contract mismatch")
        if _text(row["full_historical_condition_replay_status"]) != FULL_REPLAY_BLOCKER:
            errors.append(f"summary {scenario_id} full replay blocker mismatch")
        if _text(row["research_status"]) != (
            "published_signal_exact_replay_research_only"
        ):
            errors.append(f"summary {scenario_id} research status mismatch")

    manifest_row = manifest.iloc[0]
    if _text(manifest_row["producer_path"]) != (
        "scripts/build_hot_theme_pullback_research.py"
    ):
        errors.append("manifest producer path mismatch")
    producer_path = _path(root, manifest_row["producer_path"]).resolve()
    if not producer_path.is_file() or _text(
        manifest_row["producer_canonical_sha256"]
    ) != _canonical_text_sha256(producer_path):
        errors.append("manifest producer canonical SHA mismatch")
    if _text(manifest_row["evidence_basis"]) != "as_published_formal_signal_membership":
        errors.append("manifest has wrong evidence basis")
    if _true(manifest_row["production_condition_recalculated"]):
        errors.append("manifest falsely claims condition recalculation")
    if _text(manifest_row["snapshot_revision_policy"]) != REVISION_POLICY:
        errors.append("manifest snapshot revision policy mismatch")
    if _path(root, manifest_row["source_manifest_path"]).resolve() != source_manifest:
        errors.append("manifest source path mismatch")
    source_stat_checks = {
        "selected_snapshot_count": source_stats["selected_snapshot_count"],
        "selected_snapshot_date_min": source_stats["selected_snapshot_date_min"],
        "selected_snapshot_date_max": source_stats["selected_snapshot_date_max"],
    }
    for column, expected in source_stat_checks.items():
        if _text(manifest_row[column]) != _text(expected):
            errors.append(f"manifest {column} mismatch")
    expected_snapshot_bundle = _row_set_sha256(
        sorted(
            {
                _text(base["snapshot_sha256"])
                for base in expected_bases.values()
            }
        )
    )
    if _text(manifest_row["selected_snapshot_bundle_sha256"]) != (
        expected_snapshot_bundle
    ):
        errors.append("manifest selected snapshot bundle mismatch")
    price_hashes = sorted(
        {
            _text(value)
            for value in events["price_source_sha256"]
            if _text(value)
        }
    )
    if int(float(manifest_row["price_input_file_count"])) != len(price_hashes):
        errors.append("manifest price input file count mismatch")
    if _text(manifest_row["price_input_bundle_sha256"]) != _row_set_sha256(
        price_hashes
    ):
        errors.append("manifest price input bundle mismatch")
    if int(float(manifest_row["signal_event_count"])) != events[
        "signal_event_key"
    ].nunique():
        errors.append("manifest signal event count mismatch")
    if int(float(manifest_row["scenario_event_count"])) != len(events):
        errors.append("manifest scenario event count mismatch")
    if _text(manifest_row["events_row_set_sha256"]) != _row_set_sha256(
        events["event_row_canonical_sha256"].astype(str).tolist()
    ):
        errors.append("manifest event row-set hash mismatch")
    summary_hash = _row_set_sha256(
        [_canonical_row_sha256(row) for _, row in summary.iterrows()]
    )
    if _text(manifest_row["summary_row_set_sha256"]) != summary_hash:
        errors.append("manifest summary row-set hash mismatch")
    anomaly_count = len(expected_anomaly_hashes)
    if int(float(manifest_row["anomaly_candidate_count"])) != anomaly_count:
        errors.append("manifest anomaly candidate count mismatch")
    if int(float(manifest_row["effective_anomaly_blocker_count"])) != anomaly_count:
        errors.append("manifest anomaly blocker count mismatch")
    if _text(manifest_row["semantic_version_binding_status"]) != (
        "published_pipeline_commit_only_no_current_ast_binding"
    ):
        errors.append("manifest semantic binding status mismatch")
    if _text(manifest_row["operation_contract_status"]) != "decision_required":
        errors.append("manifest operation contract mismatch")
    if _text(manifest_row["full_historical_condition_replay_status"]) != (
        FULL_REPLAY_BLOCKER
    ):
        errors.append("manifest full replay blocker mismatch")
    for field in [
        "formal_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "promotion_evidence_allowed",
        "production_change",
    ]:
        if _true(manifest_row[field]):
            errors.append(f"manifest improperly enables {field}")
    return errors


def validate_files(
    events_path: Path = EVENTS_PATH,
    summary_path: Path = SUMMARY_PATH,
    anomaly_path: Path = ANOMALY_PATH,
    manifest_path: Path = MANIFEST_PATH,
    *,
    root: Path = ROOT,
) -> list[str]:
    artifact_paths = {
        "events": events_path.resolve(),
        "summary": summary_path.resolve(),
        "anomalies": anomaly_path.resolve(),
    }
    try:
        frames = {
            "events": _read_csv_frame(events_path),
            "summary": _read_csv_frame(summary_path),
            "anomalies": _read_csv_frame(anomaly_path),
            "manifest": _read_csv_frame(manifest_path),
        }
    except (OSError, RuntimeError, UnicodeDecodeError, ValueError) as exc:
        return [str(exc)]
    errors: list[str] = []
    manifest_frame = frames["manifest"]
    if len(manifest_frame) != 1:
        return [
            f"manifest must contain exactly one row: observed={len(manifest_frame)}"
        ]
    manifest_row = manifest_frame.iloc[0]
    required_payload_fields = {"evidence_payload_bundle_sha256"}
    for key in artifact_paths:
        required_payload_fields.update(
            {f"{key}_path", f"{key}_file_sha256", f"{key}_row_count"}
        )
    missing = sorted(required_payload_fields - set(manifest_frame.columns))
    if missing:
        errors.append(f"manifest missing payload binding fields: {missing}")
    else:
        observed_payload_hashes: list[str] = []
        for key, path in artifact_paths.items():
            expected_sha = _canonical_text_sha256(path)
            observed_payload_hashes.append(expected_sha)
            if _path(root, manifest_row[f"{key}_path"]).resolve() != path:
                errors.append(f"manifest {key} artifact path mismatch")
            if _text(manifest_row[f"{key}_file_sha256"]) != expected_sha:
                errors.append(f"manifest {key} artifact file SHA mismatch")
            try:
                observed_count = int(float(manifest_row[f"{key}_row_count"]))
            except (TypeError, ValueError):
                observed_count = -1
            if observed_count != len(frames[key]):
                errors.append(f"manifest {key} artifact row count mismatch")
        expected_bundle = _row_set_sha256(observed_payload_hashes)
        if _text(manifest_row["evidence_payload_bundle_sha256"]) != expected_bundle:
            errors.append("manifest evidence payload bundle SHA mismatch")
    errors.extend(
        validate_frames(
            frames["events"],
            frames["summary"],
            frames["anomalies"],
            frames["manifest"],
            root=root,
            manifest_is_bound_artifact=True,
        )
    )
    return errors


def main() -> int:
    errors = validate_files()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("hot_theme_pullback research validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
