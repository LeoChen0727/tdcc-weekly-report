from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from datetime import datetime
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable

try:
    from model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )
except ModuleNotFoundError:  # Imported as scripts.<module> in focused tests.
    from scripts.model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_research.py"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_actual_recommendation_replay_v1"
SOURCE_ARTIFACT_ID = "model_signals_for_report"
SOURCE_PURPOSE = "as_published_daily_model_snapshot"
REVISION_POLICY = "latest_valid_revision_per_report_date"
HORIZONS = (5, 10, 20)
HIGH_RETURN_THRESHOLD_PCT = Decimal("10")
ANOMALY_ABS_RETURN_THRESHOLD_PCT = Decimal("80")
DETAIL_ARTIFACT_NAME = (
    "tdcc_stealth_accumulation_actual_recommendation_replay_detail_v1.csv"
)
SUMMARY_ARTIFACT_NAME = (
    "tdcc_stealth_accumulation_actual_recommendation_replay_summary_v1.csv"
)

MANIFEST_REQUIRED_COLUMNS = {
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "daily_pdf_ready",
    "artifact_id",
    "source_path",
    "snapshot_path",
    "source_sha256",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
}
SIGNAL_REQUIRED_COLUMNS = {"signal_date", "stock_id", "model_id"}
PRICE_REQUIRED_COLUMNS = {"date", "open", "close"}

DETAIL_FIELDS = [
    "artifact_version", "model_id", "event_id", "signal_event_id",
    "source_presentation_count", "source_presentation_ordinal",
    "source_presentation_row_sha256s", "source_presentation_surfaces",
    "identity_disposition", "primary_metric_included", "source_manifest_path",
    "source_manifest_sha256", "source_artifact_id", "snapshot_report_date",
    "snapshot_revision", "snapshot_revision_policy", "snapshot_path",
    "snapshot_sha256", "snapshot_canonical_sha256", "snapshot_row_count",
    "snapshot_column_count", "pipeline_commit_sha", "source_row_number",
    "published_source_row_sha256", "signal_date", "stock_id", "stock_name",
    "report_line", "report_bucket", "model_score", "model_rank", "display_rank",
    "selection_semantics", "published_entry_basis", "main_condition_met",
    "published_tdcc_price_phase", "published_tdcc_status",
    "production_semantic_sha256", "semantic_binding_status",
    "phase_classifier_status", "full_historical_selector_replay_status",
    "research_entry_basis", "entry_date", "entry_open_price",
    "entry_price_row_sha256", "price_source_path", "price_source_sha256",
    "price_source_canonical_sha256", "price_observation_date_max",
    "forward_window_status", "exit_d5_date", "exit_d5_close_price",
    "exit_d5_price_row_sha256", "return_d5_pct", "exit_d10_date",
    "exit_d10_close_price", "exit_d10_price_row_sha256", "return_d10_pct",
    "exit_d20_date", "exit_d20_close_price", "exit_d20_price_row_sha256",
    "return_d20_pct", "anomaly_candidate", "anomaly_trigger_codes",
    "anomaly_disposition", "retained_in_primary", "formal_use",
    "trade_eligible", "promotion_evidence_allowed", "operation_decision_status",
    "price_source_immutability_status",
]

SUMMARY_FIELDS = [
    "artifact_version", "model_id", "horizon", "entry_basis", "exit_basis",
    "source_artifact_id", "snapshot_revision_policy", "source_manifest_path",
    "source_manifest_sha256", "detail_artifact_sha256",
    "manifest_revision_row_count", "selected_snapshot_count",
    "snapshot_report_date_min", "snapshot_report_date_max",
    "source_presentation_row_count", "actual_recommendation_row_count",
    "unique_signal_event_count", "duplicate_source_presentation_count",
    "evaluated_count", "right_censored_count", "invalid_price_count", "win_count",
    "neutral_count", "failure_count", "win_rate_pct", "neutral_rate_pct",
    "failure_rate_pct", "average_return_pct", "median_return_pct",
    "high_return_hit_count", "high_return_hit_rate_pct", "loss_count",
    "loss_rate_pct", "unresolved_anomaly_candidate_count",
    "sensitivity_analysis_basis", "sensitivity_is_corrected_primary",
    "sensitivity_evaluated_count", "sensitivity_excluded_anomaly_candidate_count",
    "sensitivity_win_count", "sensitivity_neutral_count",
    "sensitivity_failure_count", "sensitivity_win_rate_pct",
    "sensitivity_average_return_pct", "sensitivity_median_return_pct",
    "primary_metric_basis", "anomaly_candidate_policy", "phase_classifier_status",
    "full_historical_selector_replay_status", "semantic_binding_status",
    "production_semantic_sha256", "price_source_formal_lineage_status",
    "formal_use", "trade_eligible", "promotion_evidence_allowed",
    "operation_decision_status",
    "promotion_status", "promotion_blockers", "evidence_status",
]


@dataclass(frozen=True)
class SnapshotRevision:
    report_date: str
    revision: str
    revision_number: int
    path: Path
    path_text: str
    snapshot_sha256: str
    canonical_sha256: str
    row_count: int
    column_count: int
    pipeline_commit_sha: str
    rows: tuple[dict[str, str], ...]
    fieldnames: tuple[str, ...]


@dataclass(frozen=True)
class PriceHistory:
    path: Path
    path_text: str
    raw_sha256: str
    canonical_sha256: str
    rows: tuple[dict[str, str], ...]


def _text(value: Any) -> str:
    return "" if value is None else str(value).replace("\ufeff", "").strip()


def _normalize_date(value: Any) -> str:
    text = _text(value)
    if re.fullmatch(r"[0-9]{8}", text) is None:
        return ""
    try:
        parsed = datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return ""
    return text if parsed.strftime("%Y%m%d") == text else ""


def _normalize_stock_id(value: Any) -> str:
    text = _text(value)
    if re.fullmatch(r"[0-9]+\.0", text):
        text = text[:-2]
    if re.fullmatch(r"[0-9]{4,6}", text) is None:
        raise RuntimeError(f"invalid Taiwan stock_id: {value!r}")
    return text


def _is_sha256(value: Any) -> bool:
    return re.fullmatch(r"[0-9a-f]{64}", _text(value).lower()) is not None


def _canonical_text_bytes(payload: bytes) -> bytes:
    text = payload.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def _canonical_sha256(payload: bytes) -> str:
    return hashlib.sha256(_canonical_text_bytes(payload)).hexdigest()


def _published_hash_candidates(payload: bytes) -> set[str]:
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(candidate).hexdigest() for candidate in (payload, lf, crlf)}


def _row_sha256(row: dict[str, Any]) -> str:
    normalized = {str(key): _text(value) for key, value in row.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _read_csv_payload(payload: bytes, source: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
        fieldnames = list(reader.fieldnames or [])
        rows = [{key: _text(value) for key, value in row.items()} for row in reader]
    except (UnicodeDecodeError, csv.Error) as exc:
        raise RuntimeError(f"failed to read CSV {source}: {exc}") from exc
    if not fieldnames:
        raise RuntimeError(f"CSV has no header: {source}")
    return fieldnames, rows


def _read_csv_file(path: Path) -> tuple[bytes, list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise RuntimeError(f"missing CSV: {path.as_posix()}")
    payload = path.read_bytes()
    fieldnames, rows = _read_csv_payload(payload, path.as_posix())
    return payload, fieldnames, rows


def _relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise RuntimeError(
            f"path must stay under repository_root: {path.resolve().as_posix()}"
        ) from exc


def _require_canonical_manifest_path(
    manifest_path: Path, repository_root: Path
) -> Path:
    root = repository_root.resolve()
    expected = (
        root
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    ).resolve()
    observed = manifest_path.resolve()
    if observed != expected:
        raise RuntimeError(
            "manifest_path must resolve to the canonical daily snapshot manifest: "
            f"expected={expected.as_posix()} observed={observed.as_posix()}"
        )
    return observed


def _resolve_snapshot_path(path_text: str, repository_root: Path) -> Path:
    normalized = path_text.replace("\\", "/")
    candidate = Path(normalized)
    if candidate.is_absolute() or not normalized or any(
        part in {"", ".", ".."} for part in normalized.split("/")
    ):
        raise RuntimeError(f"unsafe snapshot_path: {path_text!r}")
    path = (repository_root / candidate).resolve()
    approved_root = (
        repository_root / "output" / "history" / "daily_model_snapshots"
    ).resolve()
    try:
        path.relative_to(approved_root)
    except ValueError as exc:
        raise RuntimeError(f"snapshot_path escapes approved root: {path_text}") from exc
    return path


def _parse_positive_int(value: Any, label: str) -> int:
    text = _text(value)
    if re.fullmatch(r"[0-9]+", text) is None:
        raise RuntimeError(f"{label} must be a non-negative integer: {text!r}")
    return int(text)


def _decimal(value: Any, label: str) -> Decimal:
    try:
        number = Decimal(_text(value))
    except InvalidOperation as exc:
        raise RuntimeError(f"{label} is not numeric: {value!r}") from exc
    if not number.is_finite() or number <= 0:
        raise RuntimeError(f"{label} must be finite and positive: {value!r}")
    return number


def _format_decimal(value: Decimal) -> str:
    rounded = value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    if rounded == 0:
        rounded = Decimal("0")
    return f"{rounded:.6f}"


def _revision_number(value: Any) -> int:
    match = re.fullmatch(r"r([1-9][0-9]*)", _text(value))
    if match is None:
        raise RuntimeError(f"invalid snapshot_revision: {_text(value)!r}")
    return int(match.group(1))


def _expected_snapshot_name(
    report_date: str,
    revision: str,
    snapshot_sha256: str,
    revision_reason: str,
) -> set[str]:
    names = {
        f"daily_candidate_model_signals_for_report_{report_date}_{revision}_{snapshot_sha256[:12]}.csv"
    }
    if revision == "r1" and revision_reason == "legacy_v1_manifest":
        names.add(f"daily_candidate_model_signals_for_report_{report_date}.csv")
    return names


def load_latest_revisions(
    manifest_path: Path,
    repository_root: Path,
) -> tuple[list[SnapshotRevision], dict[str, Any]]:
    manifest_path = _require_canonical_manifest_path(
        manifest_path, repository_root
    )
    manifest_payload, fieldnames, manifest_rows = _read_csv_file(manifest_path)
    missing = sorted(MANIFEST_REQUIRED_COLUMNS - set(fieldnames))
    if missing:
        raise RuntimeError(f"snapshot manifest missing columns: {missing}")
    scoped = [row for row in manifest_rows if row["artifact_id"] == SOURCE_ARTIFACT_ID]
    if not scoped:
        raise RuntimeError("snapshot manifest has no model_signals_for_report rows")

    groups: dict[str, list[dict[str, str]]] = {}
    for row in scoped:
        report_date = _normalize_date(row["snapshot_report_date"])
        if not report_date:
            raise RuntimeError("snapshot manifest contains invalid snapshot_report_date")
        if row["purpose"] != SOURCE_PURPOSE:
            raise RuntimeError(f"{report_date}: unexpected snapshot purpose")
        main_price_date = _normalize_date(row["main_price_date"])
        if not main_price_date or main_price_date != report_date:
            raise RuntimeError(f"{report_date}: main_price_date mismatch")
        if row["report_ready"].lower() != "true" or row["daily_pdf_ready"].lower() != "true":
            raise RuntimeError(f"{report_date}: published snapshot readiness is not true")
        if re.fullmatch(r"[0-9a-f]{40}", row["pipeline_commit_sha"].lower()) is None:
            raise RuntimeError(f"{report_date}: invalid pipeline_commit_sha")
        groups.setdefault(report_date, []).append(row)

    latest: list[SnapshotRevision] = []
    for report_date in sorted(groups):
        ordered = sorted(
            groups[report_date],
            key=lambda row: _revision_number(row["snapshot_revision"]),
        )
        observed = [_revision_number(row["snapshot_revision"]) for row in ordered]
        expected = list(range(1, len(ordered) + 1))
        if observed != expected or len(set(observed)) != len(observed):
            raise RuntimeError(
                f"{report_date}: non-contiguous or duplicate revision chain {observed}"
            )
        prior_sha = ""
        seen_manifest_sha: set[str] = set()
        seen_canonical_sha: set[str] = set()
        selected: SnapshotRevision | None = None
        for index, row in enumerate(ordered):
            revision = row["snapshot_revision"]
            revision_number = observed[index]
            snapshot_sha = row["snapshot_sha256"].lower()
            source_sha = row["source_sha256"].lower()
            if not _is_sha256(snapshot_sha) or source_sha != snapshot_sha:
                raise RuntimeError(f"{report_date}/{revision}: source/snapshot SHA contract failed")
            supersedes = row["supersedes_snapshot_sha256"].lower()
            if revision_number == 1 and supersedes:
                raise RuntimeError(f"{report_date}/r1: supersedes_snapshot_sha256 must be empty")
            if revision_number > 1:
                if supersedes != prior_sha:
                    raise RuntimeError(
                        f"{report_date}/{revision}: supersedes_snapshot_sha256 mismatch"
                    )
                if not row["revision_reason"]:
                    raise RuntimeError(f"{report_date}/{revision}: revision_reason is required")
            path = _resolve_snapshot_path(row["snapshot_path"], repository_root)
            if path.name not in _expected_snapshot_name(
                report_date, revision, snapshot_sha, row["revision_reason"]
            ):
                raise RuntimeError(f"{report_date}/{revision}: snapshot path identity mismatch")
            payload, snapshot_fields, snapshot_rows = _read_csv_file(path)
            if snapshot_sha not in _published_hash_candidates(payload):
                raise RuntimeError(f"{report_date}/{revision}: snapshot SHA-256 mismatch")
            canonical_sha = _canonical_sha256(payload)
            if snapshot_sha in seen_manifest_sha or canonical_sha in seen_canonical_sha:
                raise RuntimeError(f"{report_date}/{revision}: duplicate payload revision")
            expected_rows = _parse_positive_int(row["row_count"], "row_count")
            expected_columns = _parse_positive_int(row["column_count"], "column_count")
            if expected_rows != len(snapshot_rows):
                raise RuntimeError(f"{report_date}/{revision}: snapshot row_count mismatch")
            if expected_columns != len(snapshot_fields):
                raise RuntimeError(f"{report_date}/{revision}: snapshot column_count mismatch")
            missing_signal = sorted(SIGNAL_REQUIRED_COLUMNS - set(snapshot_fields))
            if missing_signal:
                raise RuntimeError(
                    f"{report_date}/{revision}: signal snapshot missing columns {missing_signal}"
                )
            for source_row_number, signal_row in enumerate(snapshot_rows, start=2):
                signal_date = _normalize_date(signal_row.get("signal_date"))
                if not signal_date:
                    raise RuntimeError(
                        f"{report_date}/{revision}: invalid signal_date at row "
                        f"{source_row_number}"
                    )
                if signal_date != report_date:
                    raise RuntimeError(
                        f"{report_date}/{revision}: signal_date mismatch at row "
                        f"{source_row_number}"
                    )
            selected = SnapshotRevision(
                report_date=report_date,
                revision=revision,
                revision_number=revision_number,
                path=path,
                path_text=_relative_path(path, repository_root),
                snapshot_sha256=snapshot_sha,
                canonical_sha256=canonical_sha,
                row_count=len(snapshot_rows),
                column_count=len(snapshot_fields),
                pipeline_commit_sha=row["pipeline_commit_sha"].lower(),
                rows=tuple(snapshot_rows),
                fieldnames=tuple(snapshot_fields),
            )
            prior_sha = snapshot_sha
            seen_manifest_sha.add(snapshot_sha)
            seen_canonical_sha.add(canonical_sha)
        if selected is None:
            raise RuntimeError(f"{report_date}: no selected snapshot revision")
        latest.append(selected)

    stats = {
        "manifest_sha256": _canonical_sha256(manifest_payload),
        "manifest_path": _relative_path(manifest_path, repository_root),
        "manifest_revision_row_count": len(scoped),
    }
    return latest, stats


def _load_price_history(
    stock_id: str,
    price_dir: Path,
    repository_root: Path,
) -> PriceHistory:
    path = (price_dir / f"{stock_id}.csv").resolve()
    payload, fieldnames, rows = _read_csv_file(path)
    missing = sorted(PRICE_REQUIRED_COLUMNS - set(fieldnames))
    if missing:
        raise RuntimeError(f"{path.as_posix()}: price history missing columns {missing}")
    normalized: list[dict[str, str]] = []
    seen_dates: set[str] = set()
    for row in rows:
        date = _normalize_date(row.get("date"))
        if not date or date in seen_dates:
            raise RuntimeError(f"{path.as_posix()}: invalid or duplicate price date")
        _decimal(row.get("open"), f"{stock_id}/{date}/open")
        _decimal(row.get("close"), f"{stock_id}/{date}/close")
        copied = dict(row)
        copied["date"] = date
        normalized.append(copied)
        seen_dates.add(date)
    normalized.sort(key=lambda row: row["date"])
    if not normalized:
        raise RuntimeError(f"{path.as_posix()}: empty price history")
    return PriceHistory(
        path=path,
        path_text=_relative_path(path, repository_root),
        raw_sha256=hashlib.sha256(payload).hexdigest(),
        canonical_sha256=_canonical_sha256(payload),
        rows=tuple(normalized),
    )


def _event_id(snapshot_sha: str, row_sha: str) -> str:
    payload = f"{ARTIFACT_VERSION}|{MODEL_ID}|{snapshot_sha}|{row_sha}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _signal_event_id(signal_date: str, stock_id: str) -> str:
    payload = f"{ARTIFACT_VERSION}|{MODEL_ID}|{signal_date}|{stock_id}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _empty_forward_fields() -> dict[str, str]:
    fields = {
        "entry_date": "",
        "entry_open_price": "",
        "entry_price_row_sha256": "",
        "forward_window_status": "no_future_trading_day",
    }
    for horizon in HORIZONS:
        fields.update(
            {
                f"exit_d{horizon}_date": "",
                f"exit_d{horizon}_close_price": "",
                f"exit_d{horizon}_price_row_sha256": "",
                f"return_d{horizon}_pct": "",
            }
        )
    return fields


def _forward_fields(history: PriceHistory, signal_date: str) -> dict[str, str]:
    result = _empty_forward_fields()
    future = [row for row in history.rows if row["date"] > signal_date]
    if not future:
        return result
    entry = future[0]
    entry_open = _decimal(entry["open"], f"{entry['date']}/entry_open")
    result.update(
        {
            "entry_date": entry["date"],
            "entry_open_price": _format_decimal(entry_open),
            "entry_price_row_sha256": _row_sha256(entry),
            "forward_window_status": (
                "ready" if len(future) >= max(HORIZONS) else "partial_forward_window"
            ),
        }
    )
    for horizon in HORIZONS:
        if len(future) < horizon:
            continue
        exit_row = future[horizon - 1]
        exit_close = _decimal(exit_row["close"], f"{exit_row['date']}/exit_close")
        realized = (exit_close / entry_open - Decimal("1")) * Decimal("100")
        result.update(
            {
                f"exit_d{horizon}_date": exit_row["date"],
                f"exit_d{horizon}_close_price": _format_decimal(exit_close),
                f"exit_d{horizon}_price_row_sha256": _row_sha256(exit_row),
                f"return_d{horizon}_pct": _format_decimal(realized),
            }
        )
    return result


def build_detail_rows(
    manifest_path: Path,
    price_dir: Path,
    repository_root: Path,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    revisions, stats = load_latest_revisions(manifest_path, repository_root)
    price_cache: dict[str, PriceHistory] = {}
    detail: list[dict[str, str]] = []
    seen_event_ids: set[str] = set()
    for revision in revisions:
        for source_row_number, source_row in enumerate(revision.rows, start=2):
            if source_row.get("model_id") != MODEL_ID:
                continue
            signal_date = _normalize_date(source_row.get("signal_date"))
            if signal_date != revision.report_date:
                raise RuntimeError(
                    f"{revision.report_date}/{revision.revision}: target signal_date mismatch"
                )
            stock_id = _normalize_stock_id(source_row.get("stock_id"))
            row_sha = _row_sha256(source_row)
            event_id = _event_id(revision.canonical_sha256, row_sha)
            if event_id in seen_event_ids:
                raise RuntimeError(f"duplicate published target row: {event_id}")
            seen_event_ids.add(event_id)
            if stock_id not in price_cache:
                price_cache[stock_id] = _load_price_history(
                    stock_id, price_dir, repository_root
                )
            price = price_cache[stock_id]
            event = {
                "artifact_version": ARTIFACT_VERSION,
                "model_id": MODEL_ID,
                "event_id": event_id,
                "signal_event_id": _signal_event_id(signal_date, stock_id),
                "source_presentation_count": "",
                "source_presentation_ordinal": "",
                "source_presentation_row_sha256s": "",
                "source_presentation_surfaces": "",
                "identity_disposition": "",
                "primary_metric_included": "",
                "source_manifest_path": stats["manifest_path"],
                "source_manifest_sha256": stats["manifest_sha256"],
                "source_artifact_id": SOURCE_ARTIFACT_ID,
                "snapshot_report_date": revision.report_date,
                "snapshot_revision": revision.revision,
                "snapshot_revision_policy": REVISION_POLICY,
                "snapshot_path": revision.path_text,
                "snapshot_sha256": revision.snapshot_sha256,
                "snapshot_canonical_sha256": revision.canonical_sha256,
                "snapshot_row_count": str(revision.row_count),
                "snapshot_column_count": str(revision.column_count),
                "pipeline_commit_sha": revision.pipeline_commit_sha,
                "source_row_number": str(source_row_number),
                "published_source_row_sha256": row_sha,
                "signal_date": signal_date,
                "stock_id": stock_id,
                "stock_name": source_row.get("stock_name", ""),
                "report_line": source_row.get("report_line", ""),
                "report_bucket": source_row.get("report_bucket", ""),
                "model_score": source_row.get("model_score", ""),
                "model_rank": source_row.get("model_rank", ""),
                "display_rank": source_row.get("display_rank", ""),
                "selection_semantics": source_row.get("selection_semantics", ""),
                "published_entry_basis": source_row.get("entry_basis", ""),
                "main_condition_met": source_row.get("main_condition_met", ""),
                "published_tdcc_price_phase": source_row.get("tdcc_price_phase", ""),
                "published_tdcc_status": source_row.get("tdcc_status", ""),
                "production_semantic_sha256": "",
                "semantic_binding_status": (
                    "pipeline_commit_only_model_semantic_sha_unavailable"
                ),
                "phase_classifier_status": "unresolved_not_replayed",
                "full_historical_selector_replay_status": "unavailable",
                "research_entry_basis": "next_trading_day_open_after_published_signal",
                "price_source_path": price.path_text,
                "price_source_sha256": price.raw_sha256,
                "price_source_canonical_sha256": price.canonical_sha256,
                "price_observation_date_max": price.rows[-1]["date"],
                "anomaly_candidate": "False",
                "anomaly_trigger_codes": "",
                "anomaly_disposition": "not_anomaly_candidate",
                "retained_in_primary": "True",
                "formal_use": "False",
                "trade_eligible": "False",
                "promotion_evidence_allowed": "False",
                "operation_decision_status": "required_before_formal_use",
                "price_source_immutability_status": "mutable_current_file_unpinned",
            }
            event.update(_forward_fields(price, signal_date))
            detail.append({field: _text(event.get(field, "")) for field in DETAIL_FIELDS})
    detail.sort(
        key=lambda row: (
            row["snapshot_report_date"], row["stock_id"], row["report_line"],
            row["report_bucket"], row["event_id"],
        )
    )
    stats["selected_snapshot_count"] = len(revisions)
    stats["snapshot_dates"] = [revision.report_date for revision in revisions]
    return detail, stats


def apply_signal_identity_dedup(detail: list[dict[str, str]]) -> None:
    groups: dict[str, list[dict[str, str]]] = {}
    for row in detail:
        groups.setdefault(row["signal_event_id"], []).append(row)
    semantic_fields = (
        "signal_date",
        "stock_id",
        "model_score",
        "selection_semantics",
        "published_entry_basis",
        "main_condition_met",
        "published_tdcc_price_phase",
        "published_tdcc_status",
    )
    for rows in groups.values():
        ordered = sorted(
            rows,
            key=lambda row: (
                row["report_line"],
                row["report_bucket"],
                row["source_row_number"],
                row["event_id"],
            ),
        )
        semantic_values = {
            tuple(row[field] for field in semantic_fields) for row in ordered
        }
        if len(semantic_values) != 1:
            first = ordered[0]
            raise RuntimeError(
                "cross-surface presentation rows disagree on signal semantics: "
                f"signal_date={first['signal_date']} stock_id={first['stock_id']}"
            )
        row_hashes = ";".join(
            sorted(row["published_source_row_sha256"] for row in ordered)
        )
        surfaces = ";".join(
            sorted(
                f"{row['report_line']}|{row['report_bucket']}" for row in ordered
            )
        )
        for ordinal, row in enumerate(ordered, start=1):
            primary = ordinal == 1
            row["source_presentation_count"] = str(len(ordered))
            row["source_presentation_ordinal"] = str(ordinal)
            row["source_presentation_row_sha256s"] = row_hashes
            row["source_presentation_surfaces"] = surfaces
            row["identity_disposition"] = (
                "canonical_signal_event"
                if primary
                else "duplicate_source_presentation"
            )
            row["primary_metric_included"] = "True" if primary else "False"
            row["retained_in_primary"] = "True" if primary else "False"


def apply_anomaly_candidates(detail: list[dict[str, str]]) -> None:
    primary = [row for row in detail if row["primary_metric_included"] == "True"]
    triggers: dict[str, set[str]] = {
        row["signal_event_id"]: set() for row in primary
    }
    for horizon in HORIZONS:
        field = f"return_d{horizon}_pct"
        observed: list[tuple[str, Decimal]] = []
        for row in primary:
            if not row[field]:
                continue
            value = Decimal(row[field])
            event_id = row["signal_event_id"]
            observed.append((event_id, value))
            if abs(value) >= ANOMALY_ABS_RETURN_THRESHOLD_PCT:
                triggers[event_id].add(f"abs_return_ge_80_pct:d{horizon}")
        total_abs = sum((abs(value) for _, value in observed), Decimal("0"))
        if len(observed) >= 3 and total_abs > 0:
            for event_id, value in observed:
                if abs(value) / total_abs > Decimal("0.5"):
                    triggers[event_id].add(
                        f"return_contribution_gt_50pct:d{horizon}"
                    )
    for row in detail:
        row_triggers = triggers.get(row["signal_event_id"], set())
        if row_triggers:
            row["anomaly_candidate"] = "True"
            row["anomaly_trigger_codes"] = ";".join(sorted(row_triggers))
            row["anomaly_disposition"] = "unresolved_anomaly_candidate"
        row["retained_in_primary"] = row["primary_metric_included"]


def _rate(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return ""
    return _format_decimal(Decimal(numerator) * Decimal("100") / Decimal(denominator))


def _mean(values: list[Decimal]) -> str:
    if not values:
        return ""
    return _format_decimal(sum(values, Decimal("0")) / Decimal(len(values)))


def _median(values: list[Decimal]) -> str:
    if not values:
        return ""
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return _format_decimal(ordered[middle])
    return _format_decimal((ordered[middle - 1] + ordered[middle]) / Decimal("2"))


def build_summary_rows(
    detail: list[dict[str, str]],
    stats: dict[str, Any],
    detail_artifact_sha256: str,
) -> list[dict[str, str]]:
    primary = [row for row in detail if row["primary_metric_included"] == "True"]
    anomaly_count = sum(row["anomaly_candidate"] == "True" for row in primary)
    blockers = [
        "phase_classifier_unresolved",
        "full_historical_selector_replay_unavailable",
        "model_semantic_sha_unavailable_from_snapshot_contract",
        "formal_operation_decision_required",
        "mutable_price_source_unpinned",
    ]
    if not detail:
        blockers.append("no_published_tdcc_stealth_signal_rows")
    if anomaly_count:
        blockers.append("unresolved_anomaly_candidates_require_root_cause_disposition")
    dates = list(stats["snapshot_dates"])
    summary: list[dict[str, str]] = []
    for horizon in HORIZONS:
        evaluated = [row for row in primary if row[f"return_d{horizon}_pct"]]
        values = [Decimal(row[f"return_d{horizon}_pct"]) for row in evaluated]
        sensitivity_rows = [
            row for row in evaluated if row["anomaly_candidate"] != "True"
        ]
        sensitivity_values = [
            Decimal(row[f"return_d{horizon}_pct"]) for row in sensitivity_rows
        ]
        wins = sum(value > 0 for value in values)
        neutral = sum(value == 0 for value in values)
        failures = sum(value < 0 for value in values)
        high_returns = sum(value >= HIGH_RETURN_THRESHOLD_PCT for value in values)
        sensitivity_wins = sum(value > 0 for value in sensitivity_values)
        sensitivity_neutral = sum(value == 0 for value in sensitivity_values)
        sensitivity_failures = sum(value < 0 for value in sensitivity_values)
        row = {
            "artifact_version": ARTIFACT_VERSION,
            "model_id": MODEL_ID,
            "horizon": f"d{horizon}",
            "entry_basis": "next_trading_day_open_after_published_signal",
            "exit_basis": f"fixed_d{horizon}_trading_day_close_after_signal",
            "source_artifact_id": SOURCE_ARTIFACT_ID,
            "snapshot_revision_policy": REVISION_POLICY,
            "source_manifest_path": stats["manifest_path"],
            "source_manifest_sha256": stats["manifest_sha256"],
            "detail_artifact_sha256": detail_artifact_sha256,
            "manifest_revision_row_count": str(stats["manifest_revision_row_count"]),
            "selected_snapshot_count": str(stats["selected_snapshot_count"]),
            "snapshot_report_date_min": min(dates) if dates else "",
            "snapshot_report_date_max": max(dates) if dates else "",
            "source_presentation_row_count": str(len(detail)),
            "actual_recommendation_row_count": str(len(primary)),
            "unique_signal_event_count": str(len(primary)),
            "duplicate_source_presentation_count": str(len(detail) - len(primary)),
            "evaluated_count": str(len(values)),
            "right_censored_count": str(len(primary) - len(values)),
            "invalid_price_count": "0",
            "win_count": str(wins),
            "neutral_count": str(neutral),
            "failure_count": str(failures),
            "win_rate_pct": _rate(wins, len(values)),
            "neutral_rate_pct": _rate(neutral, len(values)),
            "failure_rate_pct": _rate(failures, len(values)),
            "average_return_pct": _mean(values),
            "median_return_pct": _median(values),
            "high_return_hit_count": str(high_returns),
            "high_return_hit_rate_pct": _rate(high_returns, len(values)),
            "loss_count": str(failures),
            "loss_rate_pct": _rate(failures, len(values)),
            "unresolved_anomaly_candidate_count": str(anomaly_count),
            "sensitivity_analysis_basis": (
                "excluding_unresolved_anomaly_candidates_sensitivity_only"
            ),
            "sensitivity_is_corrected_primary": "False",
            "sensitivity_evaluated_count": str(len(sensitivity_values)),
            "sensitivity_excluded_anomaly_candidate_count": str(
                len(values) - len(sensitivity_values)
            ),
            "sensitivity_win_count": str(sensitivity_wins),
            "sensitivity_neutral_count": str(sensitivity_neutral),
            "sensitivity_failure_count": str(sensitivity_failures),
            "sensitivity_win_rate_pct": _rate(
                sensitivity_wins, len(sensitivity_values)
            ),
            "sensitivity_average_return_pct": _mean(sensitivity_values),
            "sensitivity_median_return_pct": _median(sensitivity_values),
            "primary_metric_basis": "including_unresolved_anomaly_candidates",
            "anomaly_candidate_policy": (
                "statistical_trigger_only_retained_in_primary_pending_root_cause"
            ),
            "phase_classifier_status": "unresolved_not_replayed",
            "full_historical_selector_replay_status": "unavailable",
            "semantic_binding_status": (
                "pipeline_commit_only_model_semantic_sha_unavailable"
            ),
            "production_semantic_sha256": "",
            "price_source_formal_lineage_status": (
                "mutable_current_files_unpinned_block_formal_use"
            ),
            "formal_use": "False",
            "trade_eligible": "False",
            "promotion_evidence_allowed": "False",
            "operation_decision_status": "required_before_formal_use",
            "promotion_status": "blocked",
            "promotion_blockers": ";".join(blockers),
            "evidence_status": (
                "no_actual_recommendation_rows"
                if not detail
                else "actual_recommendation_performance_research_only"
            ),
        }
        summary.append({field: _text(row.get(field, "")) for field in SUMMARY_FIELDS})
    return summary


def _csv_bytes(rows: Iterable[dict[str, str]], fieldnames: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def _preflight_model_owned_outputs(
    *, repository_root: Path, output_paths: Iterable[Path]
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
    registry_path = root / "config" / "model_research_artifact_ownership.csv"
    rules = load_ownership_rules(registry_path)
    errors = validate_changed_paths(MODEL_ID, PRODUCER, planned_paths, rules)
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise RuntimeError(
            f"model-owned artifact ownership preflight failed:\n{details}"
        )


def produce(
    *,
    repository_root: Path,
    manifest_path: Path,
    price_dir: Path,
    detail_path: Path,
    summary_path: Path,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    repository_root = repository_root.resolve()
    if detail_path.name != DETAIL_ARTIFACT_NAME or summary_path.name != SUMMARY_ARTIFACT_NAME:
        raise RuntimeError("output filenames must match the model-owned v1 artifact allowlist")
    if detail_path.resolve() == summary_path.resolve():
        raise RuntimeError("detail and summary output paths must be distinct")
    detail, stats = build_detail_rows(
        manifest_path.resolve(), price_dir.resolve(), repository_root
    )
    apply_signal_identity_dedup(detail)
    apply_anomaly_candidates(detail)
    detail_payload = _csv_bytes(detail, DETAIL_FIELDS)
    detail_sha = hashlib.sha256(detail_payload).hexdigest()
    summary = build_summary_rows(detail, stats, detail_sha)
    summary_payload = _csv_bytes(summary, SUMMARY_FIELDS)
    detail_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    detail_path.write_bytes(detail_payload)
    summary_path.write_bytes(summary_payload)
    return detail, summary


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Replay exact as-published tdcc_stealth_accumulation recommendations; "
            "this does not replay the unresolved historical phase classifier."
        )
    )
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--price-dir", type=Path)
    parser.add_argument("--detail-output", type=Path)
    parser.add_argument("--summary-output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    root = args.repository_root.resolve()
    manifest = args.manifest or (
        root
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    price_dir = args.price_dir or root / "data" / "stock_price_history"
    artifact_dir = root / "output" / "research" / MODEL_ID
    detail = args.detail_output or artifact_dir / DETAIL_ARTIFACT_NAME
    summary = args.summary_output or artifact_dir / SUMMARY_ARTIFACT_NAME
    registry_path = root / "config" / "model_research_artifact_ownership.csv"
    sentinel_registry_path = root / "config" / "model_research_protected_sentinels.csv"
    _preflight_model_owned_outputs(
        repository_root=root,
        output_paths=(detail, summary),
    )
    with model_owned_artifact_guard(
        MODEL_ID,
        PRODUCER,
        root=root,
        registry_path=registry_path,
        sentinel_registry_path=sentinel_registry_path,
    ):
        produce(
            repository_root=root,
            manifest_path=manifest,
            price_dir=price_dir,
            detail_path=detail,
            summary_path=summary,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
