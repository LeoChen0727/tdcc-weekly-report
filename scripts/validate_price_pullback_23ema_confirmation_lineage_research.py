"""Independent, input-bound 23EMA confirmation provenance research validation.

No producer or production business function is imported or executed.  Matching
saved operation fields does not establish economic-unit comparability, official
first-publication PIT, actual fills, or promotion evidence.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

PREFIX = "price_pullback_23ema_confirmation_lineage_research_v1_"
MODEL_ID = "price_pullback_23ema"
DECISION_REF = "2f1374ff78376ced98e142a9632b227845507dd6"
ACTIVE_REF = "ea8ae537480b27f166e64c3fc8350cb73e53c2b4"
OUTCOME_REF = "7db2863af59c88ca419baba1c8a7f709a2e0aff2"
SIGNAL_DATE = "20260703"
ACTIVE_DATE = "20260706"
TERMINAL_DATE = "20261002"
ENTRY_OPEN_UTC = datetime(2026, 7, 6, 1, 0, tzinfo=timezone.utc)
CAPTURE_RUN_ID = 28739879860
CAPTURE_CREATED_AT = "2026-07-05T11:53:37Z"
REPOSITORY = "LeoChen0727/tdcc-weekly-report"
SECTION_PATH = "output/latest/daily_price_pullback_23ema_operation_section_latest.csv"
RANK_PATH = "output/latest/daily_candidate_model_signals_for_report_latest.csv"
AUDIT_PATH = "output/latest/daily_price_pullback_23ema_operation_evidence_audit_latest.csv"
TARGET_REASON = "close_prev20_high_break_next_open"
STOP_REASON = "sustained_close_below_lower_ma20_ema23_4pct_4d"
VERSION = PREFIX.removesuffix("_")
ROW_COLUMNS = [
    "model_id", "artifact_version", "signal_date", "stock_id", "report_line",
    "model_rank", "display_rank", "model_rank_overall", "confirmed_buy_rank_eligible",
    "confirmation_ref", "confirmation_artifact_sha256", "confirmation_row_sha256",
    "rank_source_sha256", "rank_source_row_sha256", "decision_price_sha256", "decision_target_price",
    "active_ref", "active_artifact_sha256", "active_row_sha256", "active_price_sha256",
    "entry_date", "entry_price", "saved_active_state", "replayed_active_state", "target_price",
    "terminal_ref", "terminal_artifact_sha256", "terminal_row_sha256", "terminal_price_sha256",
    "saved_terminal_state", "replayed_terminal_state", "terminal_target_price", "exit_date", "exit_reason",
    "rule_lineage_status", "economic_unit_status", "return_evidence_allowed", "promotion_allowed",
]
FALSE_MANIFEST_CLAIMS = (
    "actual_broker_execution_proven", "original_first_publication_proven", "full_research_window_PIT_proven",
    "production_adapter_consumed_prior_confirmation_proven", "economic_unit_comparability_proven",
    "return_evidence_allowed", "promotion_allowed", "original_primary_metrics_modified",
    "legacy_producer_executed", "production_or_latest_artifacts_written",
)
SUMMARY_BASIS = "frozen_source_lineage_rule_consistency_not_model_performance"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_row_sha256(row: dict[str, Any]) -> str:
    return digest(json.dumps(row, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":")).encode("utf-8"))


def truth(value: Any) -> bool:
    return value is True or str(value).strip().lower() in {"true", "1"}


def number(value: Any) -> float | None:
    try:
        result = float(value)
    except (ValueError, TypeError):
        return None
    return result if math.isfinite(result) else None


def same_number(left: Any, right: Any, *, tolerance: float = 1e-8) -> bool:
    a, b = number(left), number(right)
    return (a is None and b is None or a is not None and b is not None
            and math.isclose(a, b, rel_tol=1e-10, abs_tol=tolerance))


def csv_rows(raw: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))


def identity(row: dict[str, Any]) -> tuple[str, str, str, str]:
    return (str(row.get("model_id", "")), str(row.get("signal_date", "")),
            str(row.get("stock_id", "")), str(row.get("report_line") or row.get("report_bucket", "")))


def saved_sections(raw: bytes, section: str) -> dict[tuple[str, str, str, str], dict[str, str]]:
    """Two saved views must describe the same operation, not two trades."""
    grouped: dict[tuple[str, str, str, str], dict[str, dict[str, str]]] = {}
    for row in csv_rows(raw):
        if (row.get("model_id") != MODEL_ID or row.get("signal_date") != SIGNAL_DATE
                or row.get("row_type") != "data" or row.get("pdf_section") != section):
            continue
        view = row.get("pdf_view", "")
        if view not in {"highlight", "full"}:
            raise ValueError("saved operation has an unknown PDF view")
        views = grouped.setdefault(identity(row), {})
        if view in views:
            raise ValueError("duplicate saved operation identity/view")
        views[view] = row
    result = {}
    ignored = {"pdf_view", "display_order"}
    for key, views in grouped.items():
        if set(views) != {"highlight", "full"}:
            raise ValueError("saved operation is missing one of its two views")
        comparable = lambda r: {k: v for k, v in r.items() if k not in ignored}
        if comparable(views["highlight"]) != comparable(views["full"]):
            raise ValueError("saved operation views conflict on operation fields")
        result[key] = views["full"]
    return result


def price_frame(raw: bytes) -> pd.DataFrame:
    records = csv_rows(raw)
    if not records:
        raise ValueError("empty price source")
    dates = [r["date"] for r in records]
    if len(dates) != len(set(dates)):
        raise ValueError("duplicate source stock/date")
    frame = pd.DataFrame(records)
    for col in ("open", "high", "low", "close"):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    frame = frame.dropna(subset=["date", "open", "high", "low", "close"])
    frame = frame.sort_values("date").reset_index(drop=True)
    frame["ma20"] = frame["close"].rolling(20, min_periods=20).mean()
    frame["ema23"] = frame["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return frame


def replay_position(frame: pd.DataFrame, signal_date: str, as_of_date: str) -> dict[str, Any]:
    """Literal close-confirmed rule; target first and no realized D20 expiry."""
    signal_positions = frame.index[frame["date"].eq(signal_date)].tolist()
    asof_positions = frame.index[frame["date"].le(as_of_date)].tolist()
    if not signal_positions or not asof_positions:
        raise ValueError("source has no exact signal row or as-of row")
    signal = signal_positions[0]
    asof = asof_positions[-1]
    entry = signal + 1
    target = number(frame.iloc[max(0, signal - 20):signal]["high"].max()) if signal else None
    base = {"target_price": target, "entry_date": "", "entry_price": None,
            "exit_date": "", "exit_price": None, "exit_reason": "",
            "confirmation_date": "", "confirmation_day": None,
            "stop_confirmed_days": 0}
    if entry >= len(frame) or asof < entry:
        return {**base, "state": "pending_next_open_entry"}
    base.update(entry_date=str(frame.iloc[entry]["date"]), entry_price=number(frame.iloc[entry]["open"]))
    streak = 0
    for pos in range(entry, min(asof, entry + 19) + 1):
        row = frame.iloc[pos]
        close = number(row["close"])
        references = [v for k in ("ma20", "ema23")
                      if (v := number(row[k])) is not None and v > 0]
        stop = min(references) * .96 if references else None
        reason = ""
        if target is not None and close is not None and close > target:
            reason = TARGET_REASON
        else:
            streak = streak + 1 if close is not None and stop is not None and close <= stop else 0
            if streak >= 4:
                reason = STOP_REASON
        if reason:
            pending = pos == asof
            next_row = frame.iloc[pos + 1] if pos + 1 <= asof else None
            state = ("target_exit_pending_next_open" if reason == TARGET_REASON
                     else "stop_exit_pending_next_open") if pending else "exited"
            return {**base, "state": state, "exit_reason": reason,
                    "confirmation_date": str(row["date"]), "confirmation_day": pos - entry + 1,
                    "stop_confirmed_days": streak,
                    "exit_date": str(next_row["date"]) if next_row is not None else "",
                    "exit_price": number(next_row["open"]) if next_row is not None else None}
    return {**base, "state": "expired_d20_no_active_tracking" if asof >= entry + 19 else "active_operation",
            "stop_confirmed_days": streak}


def validate_capture(capture: dict[str, Any], *, server_metadata: dict[str, Any] | None = None) -> list[str]:
    errors = []
    run_id = capture.get("run_id", capture.get("id"))
    created_at = capture.get("server_created_at", capture.get("created_at", ""))
    head_sha = capture.get("head_sha", capture.get("head_commit", ""))
    if str(run_id) != str(CAPTURE_RUN_ID) or head_sha != DECISION_REF or created_at != CAPTURE_CREATED_AT:
        errors.append("capture server identity/head/date differs from the fixed Pages receipt")
    if capture.get("status") != "completed" or capture.get("conclusion") != "success":
        errors.append("capture receipt has no completed successful conclusion")
    try:
        created = datetime.fromisoformat(str(created_at).replace("Z", "+00:00"))
        if created.tzinfo is None or created >= ENTRY_OPEN_UTC:
            errors.append("capture is not independently dated before the next-open entry")
    except ValueError:
        errors.append("capture server created_at is not a valid timezone-aware timestamp")
    if server_metadata is not None:
        for key, expected in (("id", CAPTURE_RUN_ID), ("head_sha", DECISION_REF), ("created_at", CAPTURE_CREATED_AT)):
            if server_metadata.get(key) != expected:
                errors.append(f"GitHub server metadata mismatch: {key}")
        if server_metadata.get("conclusion") != "success" or server_metadata.get("status") != "completed":
            errors.append("GitHub capture run has no completed successful conclusion")
        for key in ("event", "html_url"):
            if capture.get(key) != server_metadata.get(key):
                errors.append(f"GitHub server metadata mismatch: {key}")
    return errors


def github_capture_metadata() -> dict[str, Any]:
    raw = subprocess.run(["gh", "api", f"repos/{REPOSITORY}/actions/runs/{CAPTURE_RUN_ID}"],
                         check=True, capture_output=True).stdout
    return json.loads(raw)


def git_sources(repo: Path, manifest: dict[str, Any]) -> dict[tuple[str, str], bytes]:
    records = manifest["source_files"]
    queries = [f"{r['ref']}:{r['path']}" for r in records]
    if len(queries) != len(set(queries)):
        raise ValueError("duplicate manifest source identity")
    payload = subprocess.run(["git", "--no-replace-objects", "cat-file", "--batch"], cwd=repo,
                             input=("\n".join(queries) + "\n").encode(), check=True,
                             capture_output=True).stdout
    result = {}
    offset = 0
    for record in records:
        end = payload.index(b"\n", offset)
        header = payload[offset:end].split()
        if len(header) != 3:
            raise ValueError(f"missing source Git blob: {record['path']}")
        oid, kind, size_text = header
        size = int(size_text)
        raw = payload[end + 1:end + 1 + size]
        if (kind != b"blob" or oid.decode() != record["git_blob"] or size != int(record["bytes"])
                or digest(raw) != record["sha256"]):
            raise ValueError(f"canonical source bytes/hash mismatch: {record['ref']}:{record['path']}")
        result[record["ref"], record["path"]] = raw
        offset = end + size + 2
    if offset != len(payload):
        raise ValueError("source batch contains unbound trailing bytes")
    return result


def _source_index(raw: bytes) -> dict[tuple[str, str, str, str], dict[str, str]]:
    result = {}
    for row in csv_rows(raw):
        if row.get("model_id") != MODEL_ID or row.get("signal_date") != SIGNAL_DATE:
            continue
        key = identity(row)
        if key in result:
            raise ValueError("duplicate source model/signal/stock/report-line identity")
        result[key] = row
    return result


def _check_binding(row: dict[str, str], prefix: str, ref: str, artifact: bytes,
                   source_row: dict[str, str], errors: list[str]) -> None:
    key = identity(row)
    if row.get(f"{prefix}_ref") != ref:
        errors.append(f"{key}: {prefix} reference mismatch")
    if row.get(f"{prefix}_artifact_sha256") != digest(artifact):
        errors.append(f"{key}: {prefix} artifact SHA mismatch")
    if row.get(f"{prefix}_row_sha256") != canonical_row_sha256(source_row):
        errors.append(f"{key}: {prefix} canonical source row SHA mismatch")


def validate_source_rows(rows: list[dict[str, str]], sources: dict[tuple[str, str], bytes]) -> list[str]:
    """Bind saved confirmed/ranking/active/audit rows and independently replay."""
    errors: list[str] = []
    confirmed_raw = sources[DECISION_REF, SECTION_PATH]
    active_raw = sources[ACTIVE_REF, SECTION_PATH]
    rank_raw = sources[DECISION_REF, RANK_PATH]
    terminal_raw = sources[OUTCOME_REF, AUDIT_PATH]
    confirmed = saved_sections(confirmed_raw, "confirmed_operation")
    active = saved_sections(active_raw, "active_operation")
    ranks, terminal = _source_index(rank_raw), _source_index(terminal_raw)
    observed = [identity(r) for r in rows]
    if len(rows) != 53 or len(set(observed)) != 53 or set(observed) != set(confirmed):
        errors.append("research rows must retain exactly the 53 saved confirmed stock/line identities")
    if set(active) != set(confirmed):
        errors.append("saved active cohort is not exactly the original saved confirmed cohort")
    if set(ranks) != set(confirmed):
        errors.append("saved model ranking cohort differs from original confirmed cohort")
    for row in rows:
        key = identity(row)
        if key not in confirmed or key not in active or key not in ranks or key not in terminal:
            errors.append(f"{key}: saved confirmation/ranking/active/terminal row is missing")
            continue
        origin, saved_active, rank, saved_terminal = confirmed[key], active[key], ranks[key], terminal[key]
        if not truth(origin.get("buy_rank_eligible")) or origin.get("row_action_status") != "confirmed_buy_candidate":
            errors.append(f"{key}: original saved confirmed row was not buy-rank eligible")
        if not truth(origin.get("approved_for_daily")) or not truth(origin.get("operation_module_approved_for_daily")):
            errors.append(f"{key}: original confirmation lacks its saved operation approval")
        if not truth(row.get("confirmed_buy_rank_eligible")):
            errors.append(f"{key}: research row loses original confirmed buy-rank eligibility")
        _check_binding(row, "confirmation", DECISION_REF, confirmed_raw, origin, errors)
        _check_binding(row, "active", ACTIVE_REF, active_raw, saved_active, errors)
        _check_binding(row, "terminal", OUTCOME_REF, terminal_raw, saved_terminal, errors)
        if (row.get("rank_source_sha256") != digest(rank_raw)
                or row.get("rank_source_row_sha256") != canonical_row_sha256(rank)):
            errors.append(f"{key}: ranking source artifact/row SHA mismatch")
        for col in ("model_rank", "display_rank", "model_rank_overall"):
            if row.get(col, "") != rank.get(col, ""):
                errors.append(f"{key}: saved ranking field {col} mismatch")
        if origin.get("operation_asof_date") != SIGNAL_DATE or saved_active.get("operation_asof_date") != ACTIVE_DATE:
            errors.append(f"{key}: confirmation or saved-active operation date mismatch")
        if saved_terminal.get("operation_asof_date") != TERMINAL_DATE:
            errors.append(f"{key}: saved terminal audit date mismatch")
        path = f"data/stock_price_history/{row['stock_id']}.csv"
        decision_price_raw = sources[DECISION_REF, path]
        active_price_raw, terminal_price_raw = sources[ACTIVE_REF, path], sources[OUTCOME_REF, path]
        if row.get("decision_price_sha256") != digest(decision_price_raw):
            errors.append(f"{key}: decision raw price SHA mismatch")
        if row.get("active_price_sha256") != digest(active_price_raw):
            errors.append(f"{key}: saved-active raw price SHA mismatch")
        if row.get("terminal_price_sha256") != digest(terminal_price_raw):
            errors.append(f"{key}: terminal raw price SHA mismatch")
        early = replay_position(price_frame(active_price_raw), SIGNAL_DATE, ACTIVE_DATE)
        late = replay_position(price_frame(terminal_price_raw), SIGNAL_DATE, TERMINAL_DATE)
        decision_prices = price_frame(decision_price_raw)
        signal_position = decision_prices.index[decision_prices["date"].eq(SIGNAL_DATE)].tolist()[0]
        decision_target = number(decision_prices.iloc[max(0, signal_position - 20):signal_position]["high"].max())
        if (not same_number(row.get("decision_target_price"), decision_target)
                or not same_number(decision_target, early["target_price"])):
            errors.append(f"{key}: decision-version target differs from its saved-active target")
        for field in ("entry_date",):
            if row.get(field) != early[field] or saved_active.get(field) != early[field]:
                errors.append(f"{key}: independently replayed next-open {field} mismatch")
        if (not same_number(row.get("entry_price"), early["entry_price"])
                or not same_number(saved_active.get("entry_price"), early["entry_price"], tolerance=.00500001)):
            errors.append(f"{key}: independently replayed next-open entry price mismatch")
        if not same_number(row.get("target_price"), early["target_price"]):
            errors.append(f"{key}: active-version previous-20-high target mismatch")
        if not same_number(row.get("terminal_target_price"), late["target_price"]):
            errors.append(f"{key}: terminal-version previous-20-high target mismatch")
        if not same_number(saved_active.get("target_price"), early["target_price"], tolerance=.00500001):
            errors.append(f"{key}: saved-active previous-20-high target mismatch")
        active_state = saved_active.get("row_action_status", "")
        terminal_state = saved_terminal.get("audit_status", "")
        if (row.get("saved_active_state") != active_state or row.get("replayed_active_state") != early["state"]
                or active_state != early["state"]):
            errors.append(f"{key}: saved-active state disagrees with independent replay")
        if (row.get("saved_terminal_state") != terminal_state or row.get("replayed_terminal_state") != late["state"]
                or terminal_state != late["state"]):
            errors.append(f"{key}: saved-terminal state disagrees with independent replay")
        if row.get("exit_date", "") != late["exit_date"] or row.get("exit_reason", "") != late["exit_reason"]:
            errors.append(f"{key}: independent terminal exit date/reason mismatch")
        if (saved_terminal.get("exit_date", "") != late["exit_date"]
                or saved_terminal.get("exit_reason", "") != late["exit_reason"]):
            errors.append(f"{key}: terminal source audit exit date/reason mismatch")
        if late["state"] == "expired_d20_no_active_tracking":
            if row.get("exit_date") or row.get("exit_reason") or number(row.get("exit_price")) is not None:
                errors.append(f"{key}: D20 expiry is incorrectly represented as a realized exit")
        if row.get("economic_unit_status") != "unverified" or truth(row.get("return_evidence_allowed")) or truth(row.get("promotion_allowed")):
            errors.append(f"{key}: operation provenance is inflated into economic-return or promotion evidence")
        if row.get("rule_lineage_status") != "frozen_confirmed_active_terminal_rule_consistent":
            errors.append(f"{key}: unexpected rule lineage status")
        if row.get("artifact_version") != VERSION:
            errors.append(f"{key}: artifact version mismatch")
    return errors


def validate_summary(rows: list[dict[str, str]], summary: list[dict[str, str]]) -> list[str]:
    expected: dict[str, Any] = {
        "cohort_rows": len(rows),
        "confirmed_buy_rank_eligible_rows": sum(truth(r.get("confirmed_buy_rank_eligible")) for r in rows),
        "matched_next_open_entry_rows": len(rows), "source_row_hash_bound_rows": len(rows),
        "return_evidence_allowed": "False", "promotion_allowed": "False",
    }
    for field, prefix in (("saved_active_state", "first_active_"),
                          ("saved_terminal_state", "terminal_"), ("report_line", "line_")):
        expected.update({prefix + name: count for name, count in Counter(r[field] for r in rows).items()})
    observed = {r.get("metric", ""): r for r in summary}
    errors = []
    if len(observed) != len(summary) or set(observed) != set(expected):
        errors.append("summary count/boundary metrics are missing, duplicated, or expanded into performance claims")
    for key, value in expected.items():
        row = observed.get(key, {})
        if row.get("value") != str(value) or row.get("basis") != SUMMARY_BASIS:
            errors.append(f"summary metric/basis mismatch: {key}")
    return errors


def validate(artifact_root: Path, *, repo_root: Path,
             server_metadata: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads((artifact_root / (PREFIX + "manifest.json")).read_text(encoding="utf-8-sig"))
        expected_names = {PREFIX + "rows.csv", PREFIX + "summary.csv"}
        output_records = manifest["output_files"]
        output_hashes = {r["path"]: r for r in output_records}
        if len(output_records) != 2 or set(output_hashes) != expected_names:
            errors.append("manifest must bind exactly rows.csv and summary.csv")
        for name in expected_names:
            raw = (artifact_root / name).read_bytes()
            record = output_hashes.get(name, {})
            if digest(raw) != record.get("sha256") or len(raw) != record.get("bytes"):
                errors.append(f"published artifact SHA mismatch: {name}")
        refs = manifest.get("refs", {})
        if refs != {"decision_ref": DECISION_REF, "active_ref": ACTIVE_REF, "outcome_ref": OUTCOME_REF}:
            errors.append("fixed decision/active/outcome source references mismatch")
        errors.extend(validate_capture(manifest["github_capture"], server_metadata=server_metadata))
        rows = csv_rows((artifact_root / (PREFIX + "rows.csv")).read_bytes())
        if (manifest.get("schema_version") != 1 or manifest.get("artifact_version") != VERSION
                or manifest.get("model_id") != MODEL_ID or manifest.get("columns") != ROW_COLUMNS
                or not rows or list(rows[0]) != ROW_COLUMNS):
            errors.append("versioned confirmation research schema/column contract mismatch")
        for flag in FALSE_MANIFEST_CLAIMS:
            if manifest.get(flag) is not False:
                errors.append(f"unproven manifest claim must remain false: {flag}")
        if (manifest.get("evidence_type") != "frozen_source_confirmed_lifecycle_implementation_consistency"
                or manifest.get("source_confirmed_mapping_proven") is not True):
            errors.append("manifest evidence type exceeds or loses its bounded confirmed source mapping")
        cohort_keys = sorted([r["signal_date"], r["stock_id"], r["report_line"]] for r in rows)
        if manifest.get("cohort_keys_sha256") != digest(json.dumps(cohort_keys, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()):
            errors.append("cohort canonical identity SHA mismatch")
        sources = git_sources(repo_root, manifest)
        errors.extend(validate_source_rows(rows, sources))
        summary = csv_rows((artifact_root / (PREFIX + "summary.csv")).read_bytes())
        errors.extend(validate_summary(rows, summary))
    except (OSError, ValueError, KeyError, TypeError, IndexError, subprocess.CalledProcessError) as exc:
        errors.append(f"cannot validate pinned confirmation lineage: {type(exc).__name__}: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="獨立核對23EMA保存confirmed→active→terminal的來源鏈與正式規則；不證明PIT、經濟報酬或promotion。")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--verify-github-capture", action="store_true")
    args = parser.parse_args(argv)
    try:
        metadata = github_capture_metadata() if args.verify_github_capture else None
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: GitHub capture server metadata unavailable: {type(exc).__name__}: {exc}")
        return 1
    errors = validate(args.artifact_root, repo_root=args.repo_root, server_metadata=metadata)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    capture_note = "GitHub server metadata已獨立核對" if metadata is not None else "GitHub server metadata未另外查詢"
    print(f"23EMA confirmation provenance數值與來源核對通過；{capture_note}；PIT/economic units/return evidence/promotion仍未證明。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
