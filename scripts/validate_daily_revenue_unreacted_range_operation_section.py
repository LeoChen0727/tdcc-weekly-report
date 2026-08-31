from __future__ import annotations

"""Independent validator for the formal revenue operation adapter.

This module intentionally does not import the producer or any model business
function. It validates the serialized contract, lifecycle evidence, canonical
row hashes, and append-only history proof from first principles.
"""

import argparse
import ast
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACT = (
    ROOT
    / "output"
    / "latest"
    / "daily_revenue_unreacted_range_operation_section_latest.csv"
)
DEFAULT_SOURCE_MODULE = (
    ROOT
    / "scripts"
    / "build_daily_revenue_unreacted_range_operation_section.py"
)

MODEL_ID = "revenue_unreacted_range"
MODEL_VARIANT_ID = "source_mid_falling"
MODEL_VARIANT_VERSION = "v2"
OPERATION_MODULE_ID = "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
ADAPTER_SCHEMA_VERSION = "revenue_unreacted_range_operation_section_schema_v2"
LIFECYCLE_CONTRACT_VERSION = "revenue_unreacted_range_lifecycle_v2"
ADAPTER_MODE = "formal_production"
APPROVAL_STATUS = "provisional_backtest_supported_oos_unconfirmed"
FORMAL_SIGNAL_EFFECTIVE_FROM = "20260831"
RULE_SPEC_ID = "revenue_unreacted_range_source_mid_falling_d30_v1"
RULE_CANONICAL_SHA256 = (
    "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
)
SELECTION_POLICY = "fixed_preselected_no_reselection"
HOLDOUT_USE_POLICY = "post_launch_monitoring_non_hard_no_tuning"
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only_EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
BASELINE_PERFORMANCE_STATUS = (
    "provisional_gross_historical_header_disclosure_only"
)
BASELINE_PERFORMANCE_SCOPE = (
    "whole_model_gross_historical_d2_open_to_d30_close"
)
BASELINE_PERFORMANCE_SOURCE = (
    "config/approved_operation_evidence/"
    "revenue_unreacted_range_source_mid_falling_"
    "frozen_rule_launch_evidence_v1_20260830_manifest.csv"
)
BASELINE_METRICS = {
    "sample_size": "53",
    "win_rate_zh": "77.3585%",
    "neutral_rate_zh": "0.0000%",
    "failure_rate_zh": "22.6415%",
    "avg_return_zh": "+14.8950%",
    "median_return_zh": "+9.4077%",
}

REPORT_LINES = ("mainstream", "non_mainstream")
ROW_ACTION_STATUS = {
    "pending_confirmation": "pending_confirmation",
    "confirmed_operation": "confirmed_buy_candidate",
    "confirmed_unranked_operation": "confirmed_not_buy_ranked",
    "active_operation": "active_operation",
}
EXPECTED_GROUPS = tuple(
    (view, report_line, section)
    for report_line in REPORT_LINES
    for view, sections in (
        ("highlight", ("confirmed_operation", "active_operation")),
        (
            "full",
            (
                "confirmed_operation",
                "confirmed_unranked_operation",
                "pending_confirmation",
                "active_operation",
            ),
        ),
    )
    for section in sections
)
HEX64 = re.compile(r"[0-9a-f]{64}")
DATE8 = re.compile(r"20[0-9]{6}")
HISTORY_NAME = re.compile(
    r"daily_revenue_unreacted_range_operation_section_"
    r"(?P<date>20[0-9]{6})_(?P<sha>[0-9a-f]{64})\.csv"
)

EXPECTED_COLUMNS = (
    "model_id",
    "model_name_zh",
    "model_variant_id",
    "model_variant_version",
    "operation_module_id",
    "adapter_schema_version",
    "lifecycle_contract_version",
    "adapter_mode",
    "approval_version",
    "approval_status",
    "formal_signal_effective_from",
    "rule_spec_id",
    "rule_canonical_sha256",
    "selection_policy",
    "holdout_use_policy",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "empty_text_zh",
    "operation_asof_date",
    "operation_source_date_status",
    "report_line",
    "report_line_memberships",
    "display_order",
    "operation_key",
    "stock_id",
    "stock_name",
    "stock_display",
    "rank_reason_zh",
    "risk_tags_zh",
    "taxonomy_status",
    "theme_mainstream_label",
    "primary_theme",
    "industry",
    "lifecycle_state",
    "operation_status",
    "operation_status_zh",
    "operation_quality",
    "operation_quality_zh",
    "row_action_status",
    "buy_rank_eligible",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "baseline_performance_status",
    "baseline_performance_scope",
    "baseline_performance_source",
    "row_metric_status",
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
    "operation_directive_level",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
    "source_revenue_period",
    "source_table_date",
    "source_trade_date",
    "source_sequence_index",
    "source_to_trigger_trading_days",
    "source_position_120d_pct",
    "source_shape_return20_pct",
    "source_shape_ema23_slope5_pct",
    "signal_date",
    "signal_sequence_index",
    "signal_close",
    "confirmation_date",
    "confirmation_sequence_index",
    "confirmation_close",
    "entry_date",
    "entry_sequence_index",
    "entry_price",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_loss_rule_id",
    "stop_loss_price",
    "stop_loss_label_zh",
    "stop_basis_zh",
    "planned_exit_sequence_index",
    "exit_date",
    "exit_price",
    "exit_rule_zh",
    "confirmation_rule_id",
    "entry_rule_id",
    "exit_rule_id",
    "stop_policy_id",
    "confirmation_offset_trading_days",
    "entry_offset_trading_days",
    "holding_days",
    "planned_holding_days",
    "operation_age_days",
    "holding_session_index_offset",
    "entry_price_basis",
    "exit_price_basis",
    "price_confirmation_basis",
    "same_stock_non_overlap_policy",
    "financial_statement_scope",
    "source_revenue_anomaly_candidate_flag",
    "source_artifacts",
    "monthly_revenue_source_row_sha256",
    "price_source_sha256",
    "taxonomy_source_row_sha256",
    "confirmed_history_artifact",
    "confirmed_history_row_sha256",
    "lifecycle_replay_sha256",
    "adapter_source_status",
    "adapter_note_zh",
    "generated_at",
    "row_canonical_sha256",
)

ROW_METRIC_PAYLOAD_COLUMNS = (
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
)
FORBIDDEN_SOURCE_PARTS = (
    "output/latest",
    "docs/latest",
    "research_backtest",
)
FIXED_FIELDS = {
    "model_id": MODEL_ID,
    "model_variant_id": MODEL_VARIANT_ID,
    "model_variant_version": MODEL_VARIANT_VERSION,
    "operation_module_id": OPERATION_MODULE_ID,
    "adapter_schema_version": ADAPTER_SCHEMA_VERSION,
    "lifecycle_contract_version": LIFECYCLE_CONTRACT_VERSION,
    "adapter_mode": ADAPTER_MODE,
    "approval_status": APPROVAL_STATUS,
    "formal_signal_effective_from": FORMAL_SIGNAL_EFFECTIVE_FROM,
    "rule_spec_id": RULE_SPEC_ID,
    "rule_canonical_sha256": RULE_CANONICAL_SHA256,
    "selection_policy": SELECTION_POLICY,
    "holdout_use_policy": HOLDOUT_USE_POLICY,
    "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
    "baseline_performance_status": BASELINE_PERFORMANCE_STATUS,
    "baseline_performance_scope": BASELINE_PERFORMANCE_SCOPE,
    "baseline_performance_source": BASELINE_PERFORMANCE_SOURCE,
    "formal_model_use_allowed": "True",
    "approved_for_daily": "True",
    "presentation_allowed": "True",
    "production_allowed": "True",
    "confirmation_rule_id": "d1_analysis_close_above_trigger_analysis_close",
    "entry_rule_id": "d2_analysis_open",
    "exit_rule_id": "d30_analysis_close_offset29",
    "stop_policy_id": "none_no_stop_reference",
    "confirmation_offset_trading_days": "1",
    "entry_offset_trading_days": "2",
    "holding_days": "30",
    "planned_holding_days": "30",
    "holding_session_index_offset": "29",
    "entry_price_basis": "analysis_open",
    "exit_price_basis": "analysis_close",
    "price_confirmation_basis": "analysis_close_only",
    "entry_basis_zh": "D+1 收盤高於訊號日收盤確認；D+2 開盤進場。",
    "same_stock_non_overlap_policy": (
        "entry_after_prior_realized_exit_next_trading_day"
    ),
    "adapter_source_status": (
        "objective_sources_recomputed_no_research_latest_input"
    ),
    "stop_loss_rule_id": "none_no_stop_reference",
    "stop_loss_price": "",
    "stop_loss_label_zh": "不設正式停損價",
    "stop_basis_zh": "不設停損；固定持有至 D+30 收盤。",
    "exit_rule_zh": (
        "進場後固定於 D+30（自進場日計第30個交易日）收盤出場。"
    ),
}


class ValidationError(RuntimeError):
    pass


def _clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_csv(path: Path) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    if not path.is_file():
        raise ValidationError(f"artifact does not exist: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        header = tuple(reader.fieldnames or ())
        if len(header) != len(set(header)):
            raise ValidationError(f"duplicate CSV columns: {path}")
        return header, [
            {key: _clean(value) for key, value in row.items() if key is not None}
            for row in reader
        ]


def _canonical_semantic_csv_bytes(payload: bytes, *, source_name: str) -> bytes:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValidationError(
            f"append-only history is not UTF-8: {source_name}"
        ) from exc
    records = list(csv.reader(io.StringIO(text, newline="")))
    if not records:
        raise ValidationError(f"append-only history is empty: {source_name}")
    header = tuple(records[0])
    if header != EXPECTED_COLUMNS:
        raise ValidationError(
            f"append-only history schema drift: {source_name}"
        )
    generated_at_index = header.index("generated_at")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    for row_number, record in enumerate(records[1:], start=2):
        if len(record) != len(header):
            raise ValidationError(
                "append-only history row width drift: "
                f"{source_name}/row={row_number}"
            )
        normalized = list(record)
        normalized[generated_at_index] = ""
        writer.writerow(normalized)
    return output.getvalue().encode("utf-8")


def _row_hash(row: Mapping[str, str]) -> str:
    payload = [
        [column, _clean(row.get(column, ""))]
        for column in EXPECTED_COLUMNS
        if column not in {"generated_at", "row_canonical_sha256"}
    ]
    return hashlib.sha256(
        json.dumps(
            payload, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _int(row: Mapping[str, str], field: str, *, row_number: int) -> int:
    token = _clean(row.get(field))
    try:
        return int(token)
    except ValueError as exc:
        raise ValidationError(
            f"row {row_number} has invalid integer {field}={token!r}"
        ) from exc


def _resolve_artifact_path(value: str) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else ROOT / candidate


def _validate_source_module(path: Path) -> None:
    if not path.is_file():
        raise ValidationError(f"producer source module does not exist: {path}")
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(path))
    imported_modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_modules.add(node.module or "")
    forbidden_imports = sorted(
        module
        for module in imported_modules
        if any(
            token in module.lower()
            for token in ("research", "backtest", "candidate_model_layer")
        )
    )
    if forbidden_imports:
        raise ValidationError(
            f"producer imports forbidden research/legacy modules: {forbidden_imports}"
        )
    required_tokens = (
        '"data" / "monthly_revenue_history"',
        '"data" / "stock_price_history"',
        '"config" / "stock_theme_map.csv"',
        "FORMAL_SIGNAL_EFFECTIVE_FROM = \"20260831\"",
    )
    missing = [token for token in required_tokens if token not in text]
    if missing:
        raise ValidationError(
            f"producer objective-source/effective-date declarations drifted: {missing}"
        )


def _validate_history_snapshot(path: Path) -> None:
    match = HISTORY_NAME.fullmatch(path.name)
    if match is None:
        raise ValidationError(f"invalid append-only history filename: {path}")
    payload = path.read_bytes()
    semantic_payload = _canonical_semantic_csv_bytes(
        payload,
        source_name=str(path),
    )
    actual_sha = hashlib.sha256(semantic_payload).hexdigest()
    if actual_sha != match.group("sha"):
        raise ValidationError(
            f"append-only history semantic content hash mismatch: {path}"
        )
    header, rows = _read_csv(path)
    if header != EXPECTED_COLUMNS:
        raise ValidationError(f"append-only history schema drift: {path}")
    if not rows:
        raise ValidationError(f"append-only history is empty: {path}")
    if any(row["generated_at"] for row in rows):
        raise ValidationError(
            f"append-only semantic history must blank generated_at: {path}"
        )
    if {row["operation_asof_date"] for row in rows} != {match.group("date")}:
        raise ValidationError(
            f"append-only history date/filename mismatch: {path}"
        )
    for row in rows:
        if row["row_canonical_sha256"] != _row_hash(row):
            raise ValidationError(
                f"append-only history contains row hash drift: {path}"
            )


def _validate_confirmed_proof(
    row: Mapping[str, str], *, current_asof: str, row_number: int
) -> None:
    proof_value = row["confirmed_history_artifact"]
    proof_hash = row["confirmed_history_row_sha256"]
    if not proof_value or not HEX64.fullmatch(proof_hash):
        raise ValidationError(
            f"row {row_number} active operation lacks immutable confirmed proof"
        )
    proof_path = _resolve_artifact_path(proof_value)
    _validate_history_snapshot(proof_path)
    _header, proof_rows = _read_csv(proof_path)
    matches = [
        proof
        for proof in proof_rows
        if proof["operation_key"] == row["operation_key"]
        and proof["operation_module_id"] == OPERATION_MODULE_ID
        and proof["row_type"] == "data"
        and proof["pdf_section"] == "confirmed_operation"
        and proof["buy_rank_eligible"] == "True"
        and proof["row_canonical_sha256"] == proof_hash
        and FORMAL_SIGNAL_EFFECTIVE_FROM
        <= proof["operation_asof_date"]
        < current_asof
    ]
    if not matches:
        raise ValidationError(
            f"row {row_number} active operation proof is not a prior buy-ranked confirmed row"
        )


def _validate_source_artifacts(row: Mapping[str, str], *, row_number: int) -> None:
    values = [
        part.strip().replace("\\", "/").lower()
        for part in row["source_artifacts"].split(";")
        if part.strip()
    ]
    if not values:
        raise ValidationError(f"row {row_number} has no source_artifacts")
    forbidden = [
        value
        for value in values
        if any(part in value for part in FORBIDDEN_SOURCE_PARTS)
    ]
    if forbidden:
        raise ValidationError(
            f"row {row_number} consumes forbidden research/latest input: {forbidden}"
        )


def validate_artifact(
    artifact: Path,
    *,
    source_module: Path = DEFAULT_SOURCE_MODULE,
    history_snapshot: Path | None = None,
) -> dict[str, int | str]:
    _validate_source_module(source_module)
    header, rows = _read_csv(artifact)
    if header != EXPECTED_COLUMNS:
        missing = sorted(set(EXPECTED_COLUMNS) - set(header))
        extra = sorted(set(header) - set(EXPECTED_COLUMNS))
        raise ValidationError(
            "formal adapter schema drift: "
            f"missing={missing} extra={extra} order_matches=False"
        )
    if not rows:
        raise ValidationError("formal adapter contains no rows")
    report_dates = {row["operation_asof_date"] for row in rows}
    if len(report_dates) != 1:
        raise ValidationError(
            f"formal adapter must contain exactly one operation_asof_date: {sorted(report_dates)}"
        )
    report_date = next(iter(report_dates))
    if not DATE8.fullmatch(report_date):
        raise ValidationError(f"invalid operation_asof_date={report_date!r}")

    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    data_identity: set[tuple[str, str, str, str]] = set()
    replay_hashes: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        for field, expected in {**FIXED_FIELDS, **BASELINE_METRICS}.items():
            if row[field] != expected:
                raise ValidationError(
                    f"row {row_number} fixed field drift {field}={row[field]!r}; expected {expected!r}"
                )
        if not HEX64.fullmatch(row["row_canonical_sha256"]):
            raise ValidationError(
                f"row {row_number} has invalid row_canonical_sha256"
            )
        if row["row_canonical_sha256"] != _row_hash(row):
            raise ValidationError(f"row {row_number} canonical row hash drift")
        if not HEX64.fullmatch(row["lifecycle_replay_sha256"]):
            raise ValidationError(
                f"row {row_number} has invalid lifecycle_replay_sha256"
            )
        replay_hashes.add(row["lifecycle_replay_sha256"])
        _validate_source_artifacts(row, row_number=row_number)
        group = (row["pdf_view"], row["report_line"], row["pdf_section"])
        if group not in EXPECTED_GROUPS:
            raise ValidationError(f"row {row_number} has forbidden PDF group {group}")
        grouped.setdefault(group, []).append(row)
        if row["report_line_memberships"] != row["report_line"]:
            raise ValidationError(
                f"row {row_number} report_line membership drift"
            )
        if row["row_type"] == "empty_state":
            if row["stock_id"] or row["operation_key"]:
                raise ValidationError(
                    f"row {row_number} empty state contains synthetic stock identity"
                )
            if row["buy_rank_eligible"] != "False":
                raise ValidationError(
                    f"row {row_number} empty state is buy-rank eligible"
                )
            if row["row_metric_status"] != "not_applicable_empty_state":
                raise ValidationError(
                    f"row {row_number} empty state row_metric_status drift"
                )
            if row["row_metric_selection_status"] != "empty_state":
                raise ValidationError(
                    f"row {row_number} empty state row metric selection drift"
                )
            if any(row[field] for field in ROW_METRIC_PAYLOAD_COLUMNS):
                raise ValidationError(
                    f"row {row_number} empty state has row-level metric payload"
                )
            continue
        if row["row_type"] != "data":
            raise ValidationError(
                f"row {row_number} invalid row_type={row['row_type']!r}"
            )
        if report_date < FORMAL_SIGNAL_EFFECTIVE_FROM:
            raise ValidationError(
                f"row {row_number} backfills a formal signal before {FORMAL_SIGNAL_EFFECTIVE_FROM}"
            )
        if row["signal_date"] < FORMAL_SIGNAL_EFFECTIVE_FROM:
            raise ValidationError(
                f"row {row_number} signal predates formal effective date"
            )
        if row["pdf_section"] == "confirmed_unranked_operation":
            raise ValidationError(
                f"row {row_number} confirmed_unranked is forbidden without ranking authorization"
            )
        if row["lifecycle_state"] != row["pdf_section"]:
            raise ValidationError(
                f"row {row_number} lifecycle section/state mismatch"
            )
        if row["row_action_status"] != ROW_ACTION_STATUS[row["pdf_section"]]:
            raise ValidationError(
                f"row {row_number} row_action_status/state mismatch"
            )
        expected_buy = (
            "True" if row["pdf_section"] == "confirmed_operation" else "False"
        )
        if row["buy_rank_eligible"] != expected_buy:
            raise ValidationError(
                f"row {row_number} buy_rank_eligible/state mismatch"
            )
        if row["row_metric_status"] != "unavailable_no_approved_add_score_metric":
            raise ValidationError(
                f"row {row_number} improperly exposes baseline as row-level metric"
            )
        if row["row_metric_selection_status"] != "baseline_not_permitted_in_operation_row":
            raise ValidationError(
                f"row {row_number} row metric selection status drift"
            )
        if any(row[field] for field in ROW_METRIC_PAYLOAD_COLUMNS):
            raise ValidationError(
                f"row {row_number} improperly uses gross baseline as stock-row metric"
            )
        identity = (
            row["pdf_view"],
            row["report_line"],
            row["pdf_section"],
            row["operation_key"],
        )
        if identity in data_identity:
            raise ValidationError(
                f"row {row_number} duplicates formal operation identity {identity}"
            )
        data_identity.add(identity)
        signal_index = _int(row, "signal_sequence_index", row_number=row_number)
        confirmation_index = _int(
            row, "confirmation_sequence_index", row_number=row_number
        )
        entry_index = _int(row, "entry_sequence_index", row_number=row_number)
        exit_index = _int(
            row, "planned_exit_sequence_index", row_number=row_number
        )
        if confirmation_index != signal_index + 1:
            raise ValidationError(f"row {row_number} is not D+1 confirmation")
        if entry_index != signal_index + 2:
            raise ValidationError(f"row {row_number} is not D+2 entry")
        if exit_index != entry_index + 29:
            raise ValidationError(f"row {row_number} is not D30 close exit")
        state = row["pdf_section"]
        if state == "pending_confirmation":
            if any(
                row[field]
                for field in (
                    "confirmation_date",
                    "confirmation_close",
                    "entry_date",
                    "entry_price",
                    "confirmed_history_artifact",
                    "confirmed_history_row_sha256",
                )
            ):
                raise ValidationError(
                    f"row {row_number} pending state contains future lifecycle values"
                )
        elif state == "confirmed_operation":
            if not row["confirmation_date"] or not row["confirmation_close"]:
                raise ValidationError(
                    f"row {row_number} confirmed state lacks D+1 close evidence"
                )
            if row["entry_date"] or row["entry_price"]:
                raise ValidationError(
                    f"row {row_number} confirmed state contains future D+2 entry"
                )
            if row["confirmed_history_artifact"] or row["confirmed_history_row_sha256"]:
                raise ValidationError(
                    f"row {row_number} confirmed state improperly self-proves history"
                )
        elif state == "active_operation":
            if not all(
                row[field]
                for field in (
                    "confirmation_date",
                    "confirmation_close",
                    "entry_date",
                    "entry_price",
                )
            ):
                raise ValidationError(
                    f"row {row_number} active state lacks close-confirmed D+2 entry evidence"
                )
            operation_age = _int(
                row, "operation_age_days", row_number=row_number
            )
            if not 1 <= operation_age <= 30:
                raise ValidationError(
                    f"row {row_number} active operation_age_days is outside 1..30"
                )
            _validate_confirmed_proof(
                row, current_asof=report_date, row_number=row_number
            )

    if set(grouped) != set(EXPECTED_GROUPS):
        raise ValidationError(
            "formal adapter PDF section coverage drift: "
            f"missing={sorted(set(EXPECTED_GROUPS) - set(grouped))}"
        )
    for group, group_rows in grouped.items():
        row_types = {row["row_type"] for row in group_rows}
        if "empty_state" in row_types and len(group_rows) != 1:
            raise ValidationError(
                f"PDF group mixes empty and data rows: {group}"
            )
        orders = sorted(_int(row, "display_order", row_number=0) for row in group_rows)
        if orders != list(range(1, len(group_rows) + 1)):
            raise ValidationError(f"PDF group display order is not contiguous: {group}")
    if len(replay_hashes) != 1:
        raise ValidationError(
            f"formal adapter contains multiple lifecycle replay hashes: {replay_hashes}"
        )
    for view in ("highlight", "full"):
        for report_line in REPORT_LINES:
            confirmed = {
                row["stock_id"]
                for row in grouped[(view, report_line, "confirmed_operation")]
                if row["row_type"] == "data"
            }
            active = {
                row["stock_id"]
                for row in grouped[(view, report_line, "active_operation")]
                if row["row_type"] == "data"
            }
            overlap = sorted(confirmed & active)
            if overlap:
                raise ValidationError(
                    f"same stock overlaps confirmed and active: {view}/{report_line}/{overlap}"
                )
    if report_date < FORMAL_SIGNAL_EFFECTIVE_FROM and any(
        row["row_type"] != "empty_state" for row in rows
    ):
        raise ValidationError("pre-effective artifact must be a full empty state")
    if history_snapshot is not None:
        _validate_history_snapshot(history_snapshot)
    return {
        "row_count": len(rows),
        "data_row_count": sum(row["row_type"] == "data" for row in rows),
        "empty_row_count": sum(
            row["row_type"] == "empty_state" for row in rows
        ),
        "operation_asof_date": report_date,
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Independently validate the formal revenue operation adapter."
        )
    )
    parser.add_argument("--artifact", type=Path, default=DEFAULT_ARTIFACT)
    parser.add_argument(
        "--source-module", type=Path, default=DEFAULT_SOURCE_MODULE
    )
    parser.add_argument("--history-snapshot", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        result = validate_artifact(
            args.artifact,
            source_module=args.source_module,
            history_snapshot=args.history_snapshot,
        )
    except ValidationError as exc:
        print(f"FAIL: {exc}")
        return 1
    print(
        "PASS: formal revenue operation adapter is independently valid "
        f"asof={result['operation_asof_date']} rows={result['row_count']} "
        f"data_rows={result['data_row_count']} "
        f"empty_rows={result['empty_row_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
