from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_actual_recommendation_replay_v1"
SOURCE_ARTIFACT_ID = "model_signals_for_report"
SOURCE_PURPOSE = "as_published_daily_model_snapshot"
REVISION_POLICY = "latest_valid_revision_per_report_date"
HORIZONS = (5, 10, 20)
DETAIL_ARTIFACT_NAME = (
    "tdcc_stealth_accumulation_actual_recommendation_replay_detail_v1.csv"
)
SUMMARY_ARTIFACT_NAME = (
    "tdcc_stealth_accumulation_actual_recommendation_replay_summary_v1.csv"
)
HIGH_RETURN_THRESHOLD_PCT = Decimal("10")
ANOMALY_ABS_RETURN_THRESHOLD_PCT = Decimal("80")

MANIFEST_REQUIRED_COLUMNS = {
    "snapshot_report_date", "snapshot_revision", "supersedes_snapshot_sha256",
    "revision_reason", "generated_at", "pipeline_commit_sha", "main_price_date",
    "report_ready", "daily_pdf_ready", "artifact_id", "source_path",
    "snapshot_path", "source_sha256", "snapshot_sha256", "row_count",
    "column_count", "purpose",
}
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


def _text(value: Any) -> str:
    return "" if value is None else str(value).replace("\ufeff", "").strip()


def _date(value: Any) -> str:
    text = _text(value)
    if re.fullmatch(r"[0-9]{8}", text) is None:
        return ""
    try:
        parsed = datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return ""
    return text if parsed.strftime("%Y%m%d") == text else ""


def _stock_id(value: Any) -> str:
    text = _text(value)
    if re.fullmatch(r"[0-9]+\.0", text):
        text = text[:-2]
    if re.fullmatch(r"[0-9]{4,6}", text) is None:
        raise RuntimeError(f"invalid stock_id: {value!r}")
    return text


def _canonical_bytes(payload: bytes) -> bytes:
    decoded = payload.decode("utf-8-sig")
    return decoded.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def _canonical_sha(payload: bytes) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _hash_candidates(payload: bytes) -> set[str]:
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(candidate).hexdigest() for candidate in (payload, lf, crlf)}


def _row_sha(row: dict[str, Any]) -> str:
    normalized = {str(key): _text(value) for key, value in row.items()}
    payload = json.dumps(normalized, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _read_csv(path: Path) -> tuple[bytes, list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise RuntimeError(f"missing CSV: {path.as_posix()}")
    payload = path.read_bytes()
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    fields = list(reader.fieldnames or [])
    if not fields:
        raise RuntimeError(f"CSV has no header: {path.as_posix()}")
    return payload, fields, [
        {key: _text(value) for key, value in row.items()} for row in reader
    ]


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise RuntimeError(f"path escapes repository root: {path.as_posix()}") from exc


def _require_canonical_manifest_path(manifest_path: Path, root: Path) -> Path:
    repository_root = root.resolve()
    expected = (
        repository_root
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


def _revision_number(value: Any) -> int:
    match = re.fullmatch(r"r([1-9][0-9]*)", _text(value))
    if match is None:
        raise RuntimeError(f"invalid snapshot revision: {value!r}")
    return int(match.group(1))


def _positive_decimal(value: Any, label: str) -> Decimal:
    try:
        number = Decimal(_text(value))
    except InvalidOperation as exc:
        raise RuntimeError(f"{label} is not numeric") from exc
    if not number.is_finite() or number <= 0:
        raise RuntimeError(f"{label} must be positive")
    return number


def _fmt(value: Decimal) -> str:
    rounded = value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    if rounded == 0:
        rounded = Decimal("0")
    return f"{rounded:.6f}"


def _event_id(snapshot_sha: str, row_sha: str) -> str:
    payload = f"{ARTIFACT_VERSION}|{MODEL_ID}|{snapshot_sha}|{row_sha}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _signal_event_id(signal_date: str, stock_id: str) -> str:
    payload = f"{ARTIFACT_VERSION}|{MODEL_ID}|{signal_date}|{stock_id}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _snapshot_path(path_text: str, root: Path) -> Path:
    normalized = path_text.replace("\\", "/")
    if not normalized or Path(normalized).is_absolute() or any(
        part in {"", ".", ".."} for part in normalized.split("/")
    ):
        raise RuntimeError(f"unsafe snapshot_path: {path_text!r}")
    path = (root / normalized).resolve()
    approved = (root / "output" / "history" / "daily_model_snapshots").resolve()
    try:
        path.relative_to(approved)
    except ValueError as exc:
        raise RuntimeError("snapshot_path escapes approved directory") from exc
    return path


def _expected_names(date: str, revision: str, sha: str, reason: str) -> set[str]:
    names = {
        f"daily_candidate_model_signals_for_report_{date}_{revision}_{sha[:12]}.csv"
    }
    if revision == "r1" and reason == "legacy_v1_manifest":
        names.add(f"daily_candidate_model_signals_for_report_{date}.csv")
    return names


def _load_selected_snapshots(
    root: Path,
    manifest_path: Path,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    manifest_path = _require_canonical_manifest_path(manifest_path, root)
    manifest_payload, fields, rows = _read_csv(manifest_path)
    missing = sorted(MANIFEST_REQUIRED_COLUMNS - set(fields))
    if missing:
        raise RuntimeError(f"manifest missing required columns: {missing}")
    scoped = [row for row in rows if row["artifact_id"] == SOURCE_ARTIFACT_ID]
    if not scoped:
        raise RuntimeError("manifest has no model_signals_for_report rows")
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in scoped:
        report_date = _date(row["snapshot_report_date"])
        if not report_date:
            raise RuntimeError("invalid manifest report date")
        if row["purpose"] != SOURCE_PURPOSE:
            raise RuntimeError(f"{report_date}: wrong purpose")
        main_price_date = _date(row["main_price_date"])
        if not main_price_date or main_price_date != report_date:
            raise RuntimeError(f"{report_date}: main_price_date mismatch")
        if row["report_ready"].lower() != "true" or row["daily_pdf_ready"].lower() != "true":
            raise RuntimeError(f"{report_date}: readiness false")
        if re.fullmatch(r"[0-9a-f]{40}", row["pipeline_commit_sha"].lower()) is None:
            raise RuntimeError(f"{report_date}: invalid pipeline commit")
        grouped.setdefault(report_date, []).append(row)

    selected: list[dict[str, Any]] = []
    for report_date in sorted(grouped):
        ordered = sorted(
            grouped[report_date], key=lambda row: _revision_number(row["snapshot_revision"])
        )
        numbers = [_revision_number(row["snapshot_revision"]) for row in ordered]
        if numbers != list(range(1, len(ordered) + 1)) or len(set(numbers)) != len(numbers):
            raise RuntimeError(f"{report_date}: invalid revision chain {numbers}")
        prior_sha = ""
        seen_snapshot_sha: set[str] = set()
        seen_canonical_sha: set[str] = set()
        chosen: dict[str, Any] | None = None
        for position, row in enumerate(ordered, start=1):
            revision = row["snapshot_revision"]
            sha = row["snapshot_sha256"].lower()
            if re.fullmatch(r"[0-9a-f]{64}", sha) is None or row["source_sha256"].lower() != sha:
                raise RuntimeError(f"{report_date}/{revision}: SHA contract failed")
            supersedes = row["supersedes_snapshot_sha256"].lower()
            if position == 1 and supersedes:
                raise RuntimeError(f"{report_date}/r1: unexpected supersedes hash")
            if position > 1 and supersedes != prior_sha:
                raise RuntimeError(f"{report_date}/{revision}: supersedes hash mismatch")
            if position > 1 and not row["revision_reason"]:
                raise RuntimeError(f"{report_date}/{revision}: revision reason missing")
            path = _snapshot_path(row["snapshot_path"], root)
            if path.name not in _expected_names(
                report_date, revision, sha, row["revision_reason"]
            ):
                raise RuntimeError(f"{report_date}/{revision}: path identity mismatch")
            payload, snapshot_fields, snapshot_rows = _read_csv(path)
            if sha not in _hash_candidates(payload):
                raise RuntimeError(f"{report_date}/{revision}: snapshot hash mismatch")
            canonical = _canonical_sha(payload)
            if sha in seen_snapshot_sha or canonical in seen_canonical_sha:
                raise RuntimeError(f"{report_date}/{revision}: duplicate payload revision")
            try:
                row_count = int(row["row_count"])
                column_count = int(row["column_count"])
            except ValueError as exc:
                raise RuntimeError(f"{report_date}/{revision}: invalid dimensions") from exc
            if row_count != len(snapshot_rows) or column_count != len(snapshot_fields):
                raise RuntimeError(f"{report_date}/{revision}: row/column count mismatch")
            if not {"signal_date", "stock_id", "model_id"}.issubset(snapshot_fields):
                raise RuntimeError(f"{report_date}/{revision}: signal schema incomplete")
            for source_row_number, signal_row in enumerate(snapshot_rows, start=2):
                signal_date = _date(signal_row.get("signal_date"))
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
            chosen = {
                "report_date": report_date,
                "revision": revision,
                "path": path,
                "path_text": _relative(path, root),
                "snapshot_sha": sha,
                "canonical_sha": canonical,
                "row_count": row_count,
                "column_count": column_count,
                "pipeline_commit_sha": row["pipeline_commit_sha"].lower(),
                "rows": snapshot_rows,
            }
            prior_sha = sha
            seen_snapshot_sha.add(sha)
            seen_canonical_sha.add(canonical)
        if chosen is None:
            raise RuntimeError(f"{report_date}: no chosen revision")
        selected.append(chosen)
    stats = {
        "manifest_path": _relative(manifest_path, root),
        "manifest_sha": _canonical_sha(manifest_payload),
        "revision_count": str(len(scoped)),
        "selected_count": str(len(selected)),
    }
    return selected, stats


def _load_price(root: Path, price_dir: Path, stock_id: str) -> dict[str, Any]:
    path = (price_dir / f"{stock_id}.csv").resolve()
    payload, fields, rows = _read_csv(path)
    if not {"date", "open", "close"}.issubset(fields):
        raise RuntimeError(f"{stock_id}: price schema incomplete")
    normalized: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        date = _date(row["date"])
        if not date or date in seen:
            raise RuntimeError(f"{stock_id}: invalid or duplicate price date")
        _positive_decimal(row["open"], f"{stock_id}/{date}/open")
        _positive_decimal(row["close"], f"{stock_id}/{date}/close")
        copy = dict(row)
        copy["date"] = date
        normalized.append(copy)
        seen.add(date)
    normalized.sort(key=lambda row: row["date"])
    if not normalized:
        raise RuntimeError(f"{stock_id}: empty price history")
    return {
        "path": path,
        "path_text": _relative(path, root),
        "raw_sha": hashlib.sha256(payload).hexdigest(),
        "canonical_sha": _canonical_sha(payload),
        "rows": normalized,
    }


def _forward(price: dict[str, Any], signal_date: str) -> dict[str, str]:
    result = {
        "entry_date": "", "entry_open_price": "", "entry_price_row_sha256": "",
        "forward_window_status": "no_future_trading_day",
    }
    for horizon in HORIZONS:
        result.update(
            {
                f"exit_d{horizon}_date": "",
                f"exit_d{horizon}_close_price": "",
                f"exit_d{horizon}_price_row_sha256": "",
                f"return_d{horizon}_pct": "",
            }
        )
    future = [row for row in price["rows"] if row["date"] > signal_date]
    if not future:
        return result
    entry = future[0]
    entry_open = _positive_decimal(entry["open"], "entry open")
    result.update(
        {
            "entry_date": entry["date"],
            "entry_open_price": _fmt(entry_open),
            "entry_price_row_sha256": _row_sha(entry),
            "forward_window_status": (
                "ready" if len(future) >= max(HORIZONS) else "partial_forward_window"
            ),
        }
    )
    for horizon in HORIZONS:
        if len(future) < horizon:
            continue
        exit_row = future[horizon - 1]
        exit_close = _positive_decimal(exit_row["close"], "exit close")
        realized = (exit_close / entry_open - Decimal("1")) * Decimal("100")
        result.update(
            {
                f"exit_d{horizon}_date": exit_row["date"],
                f"exit_d{horizon}_close_price": _fmt(exit_close),
                f"exit_d{horizon}_price_row_sha256": _row_sha(exit_row),
                f"return_d{horizon}_pct": _fmt(realized),
            }
        )
    return result


def _expected_detail(
    root: Path,
    manifest_path: Path,
    price_dir: Path,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    snapshots, stats = _load_selected_snapshots(root, manifest_path)
    prices: dict[str, dict[str, Any]] = {}
    events: list[dict[str, str]] = []
    seen_events: set[str] = set()
    for snapshot in snapshots:
        for source_row_number, source in enumerate(snapshot["rows"], start=2):
            if source["model_id"] != MODEL_ID:
                continue
            signal_date = _date(source["signal_date"])
            if signal_date != snapshot["report_date"]:
                raise RuntimeError(f"{snapshot['report_date']}: target signal date mismatch")
            stock_id = _stock_id(source["stock_id"])
            row_sha = _row_sha(source)
            event_id = _event_id(snapshot["canonical_sha"], row_sha)
            if event_id in seen_events:
                raise RuntimeError(f"duplicate target source row: {event_id}")
            seen_events.add(event_id)
            if stock_id not in prices:
                prices[stock_id] = _load_price(root, price_dir, stock_id)
            price = prices[stock_id]
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
                "source_manifest_sha256": stats["manifest_sha"],
                "source_artifact_id": SOURCE_ARTIFACT_ID,
                "snapshot_report_date": snapshot["report_date"],
                "snapshot_revision": snapshot["revision"],
                "snapshot_revision_policy": REVISION_POLICY,
                "snapshot_path": snapshot["path_text"],
                "snapshot_sha256": snapshot["snapshot_sha"],
                "snapshot_canonical_sha256": snapshot["canonical_sha"],
                "snapshot_row_count": str(snapshot["row_count"]),
                "snapshot_column_count": str(snapshot["column_count"]),
                "pipeline_commit_sha": snapshot["pipeline_commit_sha"],
                "source_row_number": str(source_row_number),
                "published_source_row_sha256": row_sha,
                "signal_date": signal_date,
                "stock_id": stock_id,
                "stock_name": source.get("stock_name", ""),
                "report_line": source.get("report_line", ""),
                "report_bucket": source.get("report_bucket", ""),
                "model_score": source.get("model_score", ""),
                "model_rank": source.get("model_rank", ""),
                "display_rank": source.get("display_rank", ""),
                "selection_semantics": source.get("selection_semantics", ""),
                "published_entry_basis": source.get("entry_basis", ""),
                "main_condition_met": source.get("main_condition_met", ""),
                "published_tdcc_price_phase": source.get("tdcc_price_phase", ""),
                "published_tdcc_status": source.get("tdcc_status", ""),
                "production_semantic_sha256": "",
                "semantic_binding_status": (
                    "pipeline_commit_only_model_semantic_sha_unavailable"
                ),
                "phase_classifier_status": "unresolved_not_replayed",
                "full_historical_selector_replay_status": "unavailable",
                "research_entry_basis": "next_trading_day_open_after_published_signal",
                "price_source_path": price["path_text"],
                "price_source_sha256": price["raw_sha"],
                "price_source_canonical_sha256": price["canonical_sha"],
                "price_observation_date_max": price["rows"][-1]["date"],
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
            event.update(_forward(price, signal_date))
            events.append({field: _text(event.get(field, "")) for field in DETAIL_FIELDS})

    events.sort(
        key=lambda row: (
            row["snapshot_report_date"], row["stock_id"], row["report_line"],
            row["report_bucket"], row["event_id"],
        )
    )
    groups: dict[str, list[dict[str, str]]] = {}
    for row in events:
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
        if len({tuple(row[field] for field in semantic_fields) for row in ordered}) != 1:
            raise RuntimeError("independent cross-surface signal semantics mismatch")
        row_hashes = ";".join(
            sorted(row["published_source_row_sha256"] for row in ordered)
        )
        surfaces = ";".join(
            sorted(
                f"{row['report_line']}|{row['report_bucket']}" for row in ordered
            )
        )
        for ordinal, row in enumerate(ordered, start=1):
            primary_row = ordinal == 1
            row["source_presentation_count"] = str(len(ordered))
            row["source_presentation_ordinal"] = str(ordinal)
            row["source_presentation_row_sha256s"] = row_hashes
            row["source_presentation_surfaces"] = surfaces
            row["identity_disposition"] = (
                "canonical_signal_event"
                if primary_row
                else "duplicate_source_presentation"
            )
            row["primary_metric_included"] = (
                "True" if primary_row else "False"
            )
            row["retained_in_primary"] = "True" if primary_row else "False"

    primary = [row for row in events if row["primary_metric_included"] == "True"]
    triggers: dict[str, set[str]] = {
        row["signal_event_id"]: set() for row in primary
    }
    for horizon in HORIZONS:
        field = f"return_d{horizon}_pct"
        observed = [
            (row["signal_event_id"], Decimal(row[field]))
            for row in primary
            if row[field]
        ]
        for event_id, value in observed:
            if abs(value) >= ANOMALY_ABS_RETURN_THRESHOLD_PCT:
                triggers[event_id].add(f"abs_return_ge_80_pct:d{horizon}")
        total_abs = sum((abs(value) for _, value in observed), Decimal("0"))
        if len(observed) >= 3 and total_abs > 0:
            for event_id, value in observed:
                if abs(value) / total_abs > Decimal("0.5"):
                    triggers[event_id].add(
                        f"return_contribution_gt_50pct:d{horizon}"
                    )
    for row in events:
        row_triggers = triggers.get(row["signal_event_id"], set())
        if row_triggers:
            row["anomaly_candidate"] = "True"
            row["anomaly_trigger_codes"] = ";".join(sorted(row_triggers))
            row["anomaly_disposition"] = "unresolved_anomaly_candidate"
        row["retained_in_primary"] = row["primary_metric_included"]
    stats["snapshot_dates"] = [snapshot["report_date"] for snapshot in snapshots]
    return events, stats


def _rate(count: int, total: int) -> str:
    return "" if total == 0 else _fmt(Decimal(count) * Decimal("100") / Decimal(total))


def _mean(values: list[Decimal]) -> str:
    return "" if not values else _fmt(sum(values, Decimal("0")) / Decimal(len(values)))


def _median(values: list[Decimal]) -> str:
    if not values:
        return ""
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return _fmt(ordered[middle])
    return _fmt((ordered[middle - 1] + ordered[middle]) / Decimal("2"))


def _expected_summary(
    detail: list[dict[str, str]],
    stats: dict[str, Any],
    detail_payload: bytes,
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
    dates = stats["snapshot_dates"]
    rows: list[dict[str, str]] = []
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
        high = sum(value >= HIGH_RETURN_THRESHOLD_PCT for value in values)
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
            "source_manifest_sha256": stats["manifest_sha"],
            "detail_artifact_sha256": hashlib.sha256(detail_payload).hexdigest(),
            "manifest_revision_row_count": stats["revision_count"],
            "selected_snapshot_count": stats["selected_count"],
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
            "high_return_hit_count": str(high),
            "high_return_hit_rate_pct": _rate(high, len(values)),
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
        rows.append({field: _text(row.get(field, "")) for field in SUMMARY_FIELDS})
    return rows


def _compare_rows(
    label: str,
    observed: list[dict[str, str]],
    expected: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    if len(observed) != len(expected):
        errors.append(f"{label} row count mismatch: observed={len(observed)} expected={len(expected)}")
        return errors
    for index, (actual, wanted) in enumerate(zip(observed, expected), start=2):
        for field in wanted:
            if _text(actual.get(field)) != _text(wanted.get(field)):
                errors.append(
                    f"{label} row {index} field {field} mismatch: "
                    f"observed={actual.get(field)!r} expected={wanted.get(field)!r}"
                )
                if len(errors) >= 20:
                    return errors
    return errors


def validate(
    *,
    repository_root: Path,
    manifest_path: Path,
    price_dir: Path,
    detail_path: Path,
    summary_path: Path,
) -> list[str]:
    errors: list[str] = []
    try:
        if detail_path.name != DETAIL_ARTIFACT_NAME or summary_path.name != SUMMARY_ARTIFACT_NAME:
            raise RuntimeError("artifact filenames are outside the model-owned v1 allowlist")
        detail_payload, detail_fields, detail_rows = _read_csv(detail_path)
        _, summary_fields, summary_rows = _read_csv(summary_path)
        if detail_fields != DETAIL_FIELDS:
            errors.append("detail schema does not exactly match v1 contract")
        if summary_fields != SUMMARY_FIELDS:
            errors.append("summary schema does not exactly match v1 contract")
        expected_detail, stats = _expected_detail(
            repository_root.resolve(), manifest_path.resolve(), price_dir.resolve()
        )
        expected_summary = _expected_summary(expected_detail, stats, detail_payload)
        errors.extend(_compare_rows("detail", detail_rows, expected_detail))
        errors.extend(_compare_rows("summary", summary_rows, expected_summary))
        if any(row.get("formal_use") != "False" for row in detail_rows + summary_rows):
            errors.append("formal_use must remain False")
        if any(row.get("trade_eligible") != "False" for row in detail_rows + summary_rows):
            errors.append("trade_eligible must remain False")
        if any(
            row.get("promotion_evidence_allowed") != "False"
            for row in detail_rows + summary_rows
        ):
            errors.append("promotion_evidence_allowed must remain False")
        if any(
            row.get("operation_decision_status") != "required_before_formal_use"
            for row in detail_rows + summary_rows
        ):
            errors.append("operation_decision_status must remain required_before_formal_use")
        if any(
            row.get("price_source_immutability_status")
            != "mutable_current_file_unpinned"
            for row in detail_rows
        ):
            errors.append("detail must preserve mutable current price-source blocker")
        if any(
            row.get("price_source_formal_lineage_status")
            != "mutable_current_files_unpinned_block_formal_use"
            for row in summary_rows
        ):
            errors.append("summary must preserve mutable price-source blocker")
        if any(
            row.get("retained_in_primary") != row.get("primary_metric_included")
            for row in detail_rows
        ):
            errors.append("retained_in_primary must follow identity-dedup primary membership")
        if any(
            row.get("anomaly_candidate") == "True"
            and row.get("primary_metric_included") == "True"
            and row.get("retained_in_primary") != "True"
            for row in detail_rows
        ):
            errors.append("unresolved anomaly candidates must remain in primary metrics")
        if any(row.get("promotion_status") != "blocked" for row in summary_rows):
            errors.append("promotion_status must remain blocked")
        if any(
            row.get("sensitivity_is_corrected_primary") != "False"
            for row in summary_rows
        ):
            errors.append("candidate-exclusion sensitivity cannot be corrected primary")
    except (
        OSError,
        RuntimeError,
        UnicodeDecodeError,
        csv.Error,
        InvalidOperation,
    ) as exc:
        errors.append(str(exc))
    return errors


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Independently validate TDCC stealth v1 replay")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--price-dir", type=Path)
    parser.add_argument("--detail", type=Path)
    parser.add_argument("--summary", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    root = args.repository_root.resolve()
    artifact_dir = root / "output" / "research" / MODEL_ID
    errors = validate(
        repository_root=root,
        manifest_path=args.manifest
        or root / "output" / "history" / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv",
        price_dir=args.price_dir or root / "data" / "stock_price_history",
        detail_path=args.detail or artifact_dir / DETAIL_ARTIFACT_NAME,
        summary_path=args.summary or artifact_dir / SUMMARY_ARTIFACT_NAME,
    )
    if errors:
        print("tdcc stealth accumulation research validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("tdcc stealth accumulation research validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
