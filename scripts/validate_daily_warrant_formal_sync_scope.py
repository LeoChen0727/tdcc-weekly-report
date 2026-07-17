from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from decimal import Decimal, InvalidOperation
from fnmatch import fnmatchcase
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "daily_warrant_formal_sync_scope_v3"
ALLOWED_MUTABLE_MODEL_IDS = frozenset(
    {
        "hot_theme_pullback",
        "neckline_volume_breakout_confirmation",
        "pullback_short_reclaim",
        "revenue_unreacted_range",
        "tdcc_stealth_accumulation",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
        "w_bottom_right_side",
    }
)
BULLISH_WARRANT_SIGNALS = frozenset(
    {"call_inflow", "call_strong_inflow", "call_put_bullish"}
)
WARRANT_BONUS_BY_MODEL = {
    "hot_theme_pullback": "5",
    "neckline_volume_breakout_confirmation": "4",
    "pullback_short_reclaim": "4",
    "revenue_unreacted_range": "3",
    "tdcc_stealth_accumulation": "2",
    "volume_range_breakout_v2_low_position_volume_attack": "2",
    "volume_range_breakout_v2_mid_position_momentum_attack": "2",
    "w_bottom_right_side": "3",
}
STOCK_LEVEL_CANDIDATE_PROJECTED_MODEL_IDS = frozenset(
    {
        "volume_range_breakout_v2_high_position_volume_attack",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
    }
)
NON_CANDIDATE_WARRANT_EXEMPT_MODEL_IDS = frozenset(
    {"tdcc_short_term_continuation_d5_d10"}
)
FORMAL_SIGNAL_ARTIFACTS = (
    "output/latest/daily_candidate_model_signals_latest.csv",
    "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv",
)
LATEST_SIGNAL_ARTIFACTS = FORMAL_SIGNAL_ARTIFACTS[:2]
ALL_CANDIDATES_ARTIFACT = "output/latest/all_candidates_latest.csv"
WARRANT_FLOW_ARTIFACT = "output/latest/warrant_flow_latest.csv"
MODEL_PARAMETERS_ARTIFACT = "output/latest/daily_candidate_model_parameters_latest.csv"
FRONTPAGE_UNIQUE_ARTIFACT = "output/latest/daily_candidate_frontpage_unique_latest.csv"
STAGED_ALLOWED_PATTERNS = (
    "output/latest/warrant_daily_raw_latest.csv",
    "output/latest/warrant_daily_fetch_latest.md",
    "output/latest/warrant_source_status_latest.*",
    "output/latest/warrant_flow_latest.*",
    "output/latest/warrant_flow_merge_latest.md",
    "output/latest/all_candidates_latest.*",
    "output/latest/stock_monitor_latest.md",
    "output/latest/data_freshness_latest.*",
    "output/latest/chatgpt_indicator_usage_guide_latest.md",
    "output/latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt",
    "output/latest/theme_event_watch_latest.*",
    "output/latest/daily_candidate_model_parameters_latest.*",
    "output/latest/daily_candidate_model_signals_latest.*",
    "output/latest/daily_candidate_model_signals_for_report_latest.*",
    "output/latest/daily_candidate_frontpage_unique_latest.*",
    "output/latest/daily_candidate_same_model_repeat_latest.*",
    "output/latest/daily_candidate_model_layer_packet_latest.md",
    "output/latest/daily_candidate_model_layer_validation_latest.*",
    "output/latest/daily_candidate_model_selection_audit_latest.*",
    "output/latest/daily_candidate_pipeline_integrity_audit_latest.*",
    "output/latest/daily_candidate_group_rotation_latest.*",
    "output/latest/daily_report_model_registry_latest.*",
    "output/latest/daily_candidate_model_summary_for_report_latest.*",
    "output/debug/warrant_fetch_debug_latest.*",
    "output/history/warrant_daily/*",
    "output/history/warrant_flow/*",
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv",
    "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv",
    "output/history/daily_model_snapshots/data_freshness_*.csv",
    "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv",
    "output/history/daily_model_snapshots/all_candidates_*.csv",
    "output/history/daily_model_snapshots/daily_candidate_model_summary_for_report_*.csv",
    "docs/latest/daily_candidate_model_*",
    "docs/latest/daily_candidate_frontpage_unique_latest.*",
    "docs/latest/daily_candidate_same_model_repeat_latest.*",
    "docs/latest/daily_candidate_pipeline_integrity_audit_latest.*",
    "docs/latest/daily_candidate_group_rotation_latest.*",
    "docs/latest/daily_report_model_registry_latest.*",
    "docs/latest/theme_event_watch_latest.*",
    "docs/latest/chatgpt_indicator_usage_guide_latest.md",
    "docs/latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt",
)
WARRANT_CANDIDATE_FIELDS = frozenset(
    {
        "warrant_flow_signal",
        "warrant_flow_score",
        "warrant_flow_warning",
        "call_turnover",
        "put_turnover",
        "call_put_turnover_ratio",
        "call_turnover_change_1d",
        "call_turnover_change_5d",
        "low_float_call_spike_count",
        "top_issuer",
        "warrant_note",
    }
)
WARRANT_SOURCE_TO_CANDIDATE_FIELDS = {
    "warrant_flow_signal": "warrant_flow_signal",
    "warrant_flow_score": "warrant_flow_score",
    "warrant_flow_warning": "warrant_flow_warning",
    "call_turnover": "call_turnover",
    "put_turnover": "put_turnover",
    "call_put_turnover_ratio": "call_put_turnover_ratio",
    "call_turnover_change_1d": "call_turnover_change_1d",
    "call_turnover_change_5d": "call_turnover_change_5d",
    "low_float_call_spike_count": "low_float_call_spike_count",
    "top_issuer": "top_issuer",
    "note": "warrant_note",
}
WARRANT_NUMERIC_CANDIDATE_FIELDS = frozenset(
    {
        "warrant_flow_score",
        "call_turnover",
        "put_turnover",
        "call_put_turnover_ratio",
        "call_turnover_change_1d",
        "call_turnover_change_5d",
        "low_float_call_spike_count",
    }
)
WARRANT_PRESENTATION_FIELDS = frozenset(
    {
        "frontpage_display_allowed",
        "frontpage_duplicate_reason",
        "frontpage_duplicate_reason_zh",
        "warrant_flow_signal",
        "warrant_flow_signal_zh",
        "why_selected_human_zh",
        "why_selected_zh",
        "why_selected",
    }
)
WARRANT_SCORE_AND_RANK_FIELDS = frozenset(
    {
        "base_model_score",
        "display_rank",
        "display_rank_new_signal",
        "display_rank_repeated_signal",
        "final_rank_score",
        "merged_score_components",
        "model_rank",
        "model_rank_new_signal",
        "model_rank_overall",
        "model_rank_repeated_signal",
        "model_score",
        "primary_model_rank",
        "primary_model_score",
        "score_components",
        "score_components_zh",
    }
)
WARRANT_MUTABLE_FIELDS = WARRANT_PRESENTATION_FIELDS | WARRANT_SCORE_AND_RANK_FIELDS
WARRANT_NUMERIC_SCORE_FIELDS = (
    "base_model_score",
    "final_rank_score",
    "model_score",
)
FRONTPAGE_REASON_ZH = {
    "": "",
    "not_pdf_core_model": "非PDF核心模型",
    "same_model_repeat_moved_to_persistence_table": "同模型重複進榜，移至延續表",
    "duplicate_stock_already_shown_on_frontpage": "首頁已列示",
}
WARRANT_EXPLANATION_FIELDS = frozenset(
    {
        "score_components",
        "score_components_zh",
        "merged_score_components",
        "why_selected_human_zh",
        "why_selected_zh",
        "why_selected",
    }
)
IDENTITY_FIELD_CANDIDATES = (
    "signal_date",
    "report_line",
    "report_bucket",
    "source_row_index",
    "stock_id",
    "model_id",
)


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _text(value: object) -> str:
    return str(value or "").strip()


def _date_text(value: object) -> str:
    digits = "".join(character for character in _text(value) if character.isdigit())
    return digits[:8] if len(digits) >= 8 else ""


def _canonical_warrant_value(column: str, value: object) -> str:
    normalized = _text(value)
    if normalized.lower() in {"", "<na>", "nan", "none", "null"}:
        return ""
    if column == "warrant_flow_signal":
        return normalized.lower()
    if column not in WARRANT_NUMERIC_CANDIDATE_FIELDS:
        return normalized
    try:
        number = Decimal(normalized)
    except InvalidOperation:
        return normalized
    if not number.is_finite():
        return normalized
    if number == 0:
        return "0"
    return format(number.normalize(), "f")


def _decimal(value: object) -> Decimal | None:
    normalized = _text(value)
    if not normalized:
        return None
    try:
        number = Decimal(normalized)
    except InvalidOperation:
        return None
    return number if number.is_finite() else None


def _clamp_score(value: Decimal) -> Decimal:
    return max(Decimal("0"), min(Decimal("100"), value))


def _strip_warrant_explanation(value: object) -> str:
    normalized = _text(value)
    normalized = re.sub(
        r"(?i)warrant bullish\s*\+[0-9]+(?:\.[0-9]+)?",
        "",
        normalized,
    )
    normalized = re.sub(
        r"權證偏多\s*\+[0-9]+(?:\.[0-9]+)?",
        "",
        normalized,
    )
    normalized = normalized.replace("權證偏多。", "")
    previous = None
    while previous != normalized:
        previous = normalized
        normalized = re.sub(r"\|\s*\|", "|", normalized)
        normalized = re.sub(r"/\s*/", "/", normalized)
    normalized = re.sub(r"^\s*[|/]\s*|\s*[|/]\s*$", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def _candidate_warrant_projection(row: dict[str, str]) -> dict[str, str]:
    return {
        column: _canonical_warrant_value(column, row.get(column))
        for column in WARRANT_CANDIDATE_FIELDS
    }


def _official_warrant_projection(row: dict[str, str]) -> dict[str, str]:
    return {
        candidate_column: _canonical_warrant_value(
            candidate_column,
            row.get(source_column),
        )
        for source_column, candidate_column in WARRANT_SOURCE_TO_CANDIDATE_FIELDS.items()
    }


def _source_key(row: dict[str, str]) -> tuple[str, str]:
    source_row_index = _text(row.get("source_row_index"))
    raw_stock_id = _text(row.get("stock_id"))
    stock_id = raw_stock_id.zfill(4) if raw_stock_id else ""
    return source_row_index, stock_id


def _report_line(row: dict[str, str]) -> str:
    return _text(row.get("report_line")) or _text(row.get("report_bucket"))


def _signal_key(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    source_row_index, stock_id = _source_key(row)
    return (
        _text(row.get("signal_date")),
        _report_line(row),
        source_row_index,
        stock_id,
        _text(row.get("model_id")),
    )


def _read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = list(reader.fieldnames or [])
        rows = [
            {column: _text(row.get(column)) for column in columns}
            for row in reader
        ]
    return columns, rows


def validate_warrant_bonus_parameter_contract(root: Path) -> list[str]:
    errors: list[str] = []
    if ALLOWED_MUTABLE_MODEL_IDS != frozenset(WARRANT_BONUS_BY_MODEL):
        errors.append("warrant bonus model allowlist does not match pinned bonus contract")
        return errors
    path = root / MODEL_PARAMETERS_ARTIFACT
    if not path.is_file():
        return [f"missing formal model parameter artifact: {MODEL_PARAMETERS_ARTIFACT}"]
    columns, rows = _read_rows(path)
    required = {"model_id", "warrant_bullish_bonus"}
    missing = sorted(required - set(columns))
    if missing:
        return [
            "formal model parameter artifact missing warrant bonus columns: "
            + ",".join(missing)
        ]
    by_model: dict[str, str] = {}
    for row in rows:
        model_id = _text(row.get("model_id"))
        if not model_id:
            continue
        if model_id in by_model:
            errors.append(f"duplicate formal model parameter row: {model_id}")
            continue
        by_model[model_id] = _canonical_warrant_value(
            "warrant_flow_score",
            row.get("warrant_bullish_bonus"),
        )
    for model_id, expected_bonus in WARRANT_BONUS_BY_MODEL.items():
        if by_model.get(model_id) != expected_bonus:
            errors.append(
                "formal model warrant bonus parameter mismatch: "
                f"model_id={model_id} expected={expected_bonus} "
                f"actual={by_model.get(model_id, '<missing>')}"
            )
    for model_id, bonus in sorted(by_model.items()):
        if model_id not in WARRANT_BONUS_BY_MODEL and bonus not in {"", "0"}:
            errors.append(
                "unapproved formal model has nonzero warrant bonus: "
                f"model_id={model_id} bonus={bonus}"
            )
    return errors


def validate_warrant_bonus_marker(
    row: dict[str, str],
    relative_path: str,
) -> list[str]:
    model_id = _text(row.get("model_id"))
    signal = _text(row.get("warrant_flow_signal")).lower()
    components = [part.strip() for part in _text(row.get("score_components")).split("|")]
    observed_markers = [
        part for part in components if part.lower().startswith("warrant bullish +")
    ]
    expected_bonus = WARRANT_BONUS_BY_MODEL.get(model_id)
    expected_markers = (
        [f"warrant bullish +{expected_bonus}"]
        if expected_bonus and signal in BULLISH_WARRANT_SIGNALS
        else []
    )
    if observed_markers != expected_markers:
        return [
            "formal signal warrant bonus marker mismatch "
            f"{relative_path}: model_id={model_id} stock_id={_source_key(row)[1]} "
            f"signal={signal!r} expected={expected_markers} actual={observed_markers}"
        ]
    return []


def validate_warrant_score_delta(
    before_rows: object,
    after_rows: object,
) -> list[str]:
    """Prove that the only numeric score change is the pinned warrant bonus.

    Scores are persisted after a 0..100 clamp.  For a newly added bonus the
    forward clamped relation is exact; for a removed bonus the reverse clamped
    relation is exact even when the old score was saturated at 100.
    """

    errors: list[str] = []
    if not isinstance(before_rows, list) or not isinstance(after_rows, list):
        return ["warrant formal sync mutable score rows must be arrays"]

    def index_rows(
        rows: list[object],
        label: str,
    ) -> dict[tuple[str, ...], dict[str, Any]]:
        indexed: dict[tuple[str, ...], dict[str, Any]] = {}
        for raw_row in rows:
            if not isinstance(raw_row, dict):
                errors.append(f"warrant {label} mutable score row must be an object")
                continue
            identity = raw_row.get("identity")
            if not isinstance(identity, list) or not all(isinstance(item, str) for item in identity):
                errors.append(f"warrant {label} mutable score row has invalid identity")
                continue
            key = tuple(identity)
            if key in indexed:
                errors.append(f"warrant {label} mutable score row has duplicate identity: {key}")
                continue
            indexed[key] = raw_row
        return indexed

    before_by_key = index_rows(before_rows, "before")
    after_by_key = index_rows(after_rows, "after")
    if set(before_by_key) != set(after_by_key):
        errors.append("warrant mutable score identity membership drift")
        return errors

    for key in sorted(before_by_key):
        before = before_by_key[key]
        after = after_by_key[key]
        model_id = _text(before.get("model_id"))
        if model_id != _text(after.get("model_id")):
            errors.append(f"warrant mutable score model_id drift key={key}")
            continue
        bonus_text = WARRANT_BONUS_BY_MODEL.get(model_id)
        if bonus_text is None:
            errors.append(f"warrant mutable score row has unapproved model_id key={key}")
            continue
        bonus = Decimal(bonus_text)
        before_signal = _text(before.get("warrant_flow_signal")).lower()
        after_signal = _text(after.get("warrant_flow_signal")).lower()
        before_effect = bonus if before_signal in BULLISH_WARRANT_SIGNALS else Decimal("0")
        after_effect = bonus if after_signal in BULLISH_WARRANT_SIGNALS else Decimal("0")
        delta = after_effect - before_effect

        if _text(before.get("non_warrant_score_components")) != _text(
            after.get("non_warrant_score_components")
        ):
            errors.append(f"non-warrant score components drift key={key}")

        before_scores = before.get("scores")
        after_scores = after.get("scores")
        if not isinstance(before_scores, dict) or not isinstance(after_scores, dict):
            errors.append(f"warrant mutable score row missing scores key={key}")
            continue
        for column in WARRANT_NUMERIC_SCORE_FIELDS:
            before_text = _text(before_scores.get(column))
            after_text = _text(after_scores.get(column))
            if not before_text and not after_text:
                continue
            if not before_text or not after_text:
                errors.append(
                    f"warrant score field presence drift key={key} column={column}"
                )
                continue
            before_value = _decimal(before_text)
            after_value = _decimal(after_text)
            if before_value is None or after_value is None:
                errors.append(
                    f"warrant score field is not finite numeric key={key} column={column}"
                )
                continue
            if delta > 0 and before_value == 0:
                errors.append(
                    "warrant score delta is not provable across lower clamp boundary "
                    f"key={key} column={column}"
                )
                continue
            if delta < 0 and before_value == 100:
                errors.append(
                    "warrant score delta is not provable across upper clamp boundary "
                    f"key={key} column={column}"
                )
                continue
            if delta >= 0:
                expected_after = _clamp_score(before_value + delta)
                valid = after_value == expected_after
                expected_text = str(expected_after)
            else:
                expected_before = _clamp_score(after_value - delta)
                valid = before_value == expected_before
                expected_text = f"reverse_before={expected_before}"
            if not valid:
                errors.append(
                    "warrant score delta mismatch "
                    f"key={key} column={column} before={before_value} after={after_value} "
                    f"bonus_delta={delta} expected={expected_text}"
                )
    return errors


def validate_frontpage_uniqueness(
    root: Path,
    report_columns: list[str],
    report_rows: list[dict[str, str]],
) -> list[str]:
    """Independently recompute report front-page representatives and consumer rows."""

    errors: list[str] = []
    required = {
        "signal_date",
        "report_bucket",
        "stock_id",
        "model_id",
        "model_group",
        "same_model_repeat_status",
        "model_score",
        "model_rank",
        "frontpage_display_allowed",
        "frontpage_duplicate_reason",
        "frontpage_duplicate_reason_zh",
    }
    missing = sorted(required - set(report_columns))
    if missing:
        return ["report frontpage contract columns missing: " + ",".join(missing)]

    indexed_rows: list[tuple[tuple[str, str, str, str, str], dict[str, str]]] = []
    core_groups: dict[tuple[str, str], list[tuple[tuple[str, str, str, str, str], dict[str, str]]]] = {}
    for row in report_rows:
        key = _signal_key(row)
        indexed_rows.append((key, row))
        report_bucket = _text(row.get("report_bucket"))
        report_line = _text(row.get("report_line"))
        if report_line and report_line != report_bucket:
            errors.append(
                f"report frontpage bucket/line mismatch key={key} "
                f"report_bucket={report_bucket!r} report_line={report_line!r}"
            )
        repeat = _text(row.get("same_model_repeat_status")) == "repeated_same_model_signal"
        is_core = _text(row.get("model_group")) == "pdf_core_model"
        if is_core and not repeat:
            core_groups.setdefault((report_bucket, key[3]), []).append((key, row))

    winner_keys: set[tuple[str, str, str, str, str]] = set()
    for members in core_groups.values():
        def sort_key(item: tuple[tuple[str, str, str, str, str], dict[str, str]]) -> tuple[Any, ...]:
            key, row = item
            score = _decimal(row.get("model_score"))
            rank = _decimal(row.get("model_rank"))
            return (
                -(score if score is not None else Decimal("-999")),
                rank if rank is not None else Decimal("999999"),
                _text(row.get("model_id")),
                key,
            )

        winner_keys.add(sorted(members, key=sort_key)[0][0])

    winner_rows: dict[tuple[str, str, str], dict[str, str]] = {}
    for key, row in indexed_rows:
        repeat = _text(row.get("same_model_repeat_status")) == "repeated_same_model_signal"
        is_core = _text(row.get("model_group")) == "pdf_core_model"
        if repeat:
            expected_allowed = "False"
            expected_reason = "same_model_repeat_moved_to_persistence_table"
        elif not is_core:
            expected_allowed = "False"
            expected_reason = "not_pdf_core_model"
        elif key in winner_keys:
            expected_allowed = "True"
            expected_reason = ""
            winner_rows[(key[0], _text(row.get("report_bucket")), key[3])] = row
        else:
            expected_allowed = "False"
            expected_reason = "duplicate_stock_already_shown_on_frontpage"
        expected_zh = FRONTPAGE_REASON_ZH[expected_reason]
        observed = (
            _text(row.get("frontpage_display_allowed")),
            _text(row.get("frontpage_duplicate_reason")),
            _text(row.get("frontpage_duplicate_reason_zh")),
        )
        expected = (expected_allowed, expected_reason, expected_zh)
        if observed != expected:
            errors.append(
                f"report frontpage representative mismatch key={key} "
                f"expected={expected} actual={observed}"
            )

    artifact_path = root / FRONTPAGE_UNIQUE_ARTIFACT
    if not artifact_path.is_file():
        return errors + [f"missing frontpage consumer artifact: {FRONTPAGE_UNIQUE_ARTIFACT}"]
    front_columns, front_rows = _read_rows(artifact_path)
    required_front_columns = {
        "signal_date",
        "report_bucket",
        "stock_id",
        "primary_model_id",
        "primary_model_score",
        "primary_model_rank",
    }
    if winner_rows:
        missing_front = sorted(required_front_columns - set(front_columns))
        if missing_front:
            return errors + [
                "frontpage consumer artifact columns missing: " + ",".join(missing_front)
            ]

    actual_winners: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in front_rows:
        raw_stock_id = _text(row.get("stock_id"))
        consumer_key = (
            _text(row.get("signal_date")),
            _text(row.get("report_bucket")),
            raw_stock_id.zfill(4) if raw_stock_id else "",
        )
        if consumer_key in actual_winners:
            errors.append(f"frontpage consumer artifact duplicate identity: {consumer_key}")
            continue
        actual_winners[consumer_key] = row
    for key in sorted(set(winner_rows) - set(actual_winners)):
        errors.append(f"frontpage representative missing from consumer artifact: {key}")
    for key in sorted(set(actual_winners) - set(winner_rows)):
        errors.append(f"frontpage consumer artifact has unexpected representative: {key}")
    for key in sorted(set(winner_rows) & set(actual_winners)):
        expected_row = winner_rows[key]
        actual_row = actual_winners[key]
        if _text(actual_row.get("primary_model_id")) != _text(expected_row.get("model_id")):
            errors.append(f"frontpage consumer primary model mismatch key={key}")
        for consumer_column, report_column in (
            ("primary_model_score", "model_score"),
            ("primary_model_rank", "model_rank"),
        ):
            actual_value = _decimal(actual_row.get(consumer_column))
            expected_value = _decimal(expected_row.get(report_column))
            if actual_value is None or expected_value is None or actual_value != expected_value:
                errors.append(
                    f"frontpage consumer numeric mismatch key={key} column={consumer_column}"
                )
    return errors


def validate_model_rank_contract(
    columns: list[str],
    rows: list[dict[str, str]],
    relative_path: str,
    *,
    report_artifact: bool,
) -> list[str]:
    """Independently recompute formal per-model and report display ranks."""

    errors: list[str] = []
    required = {
        "report_bucket",
        "stock_id",
        "model_id",
        "model_score",
        "model_rank",
    }
    if report_artifact:
        required.update(
            {
                "report_line",
                "display_rank",
                "same_model_repeat_status",
                "same_model_consecutive_days",
                "same_model_appear_count_10d",
                "model_rank_overall",
                "model_rank_new_signal",
                "model_rank_repeated_signal",
                "display_rank_new_signal",
                "display_rank_repeated_signal",
            }
        )
    missing = sorted(required - set(columns))
    if missing:
        return [
            f"formal rank contract columns missing {relative_path}: " + ",".join(missing)
        ]

    def score_value(row: dict[str, str]) -> Decimal:
        value = _decimal(row.get("model_score"))
        return value if value is not None else Decimal("-999999")

    def rank_value(row: dict[str, str]) -> Decimal:
        value = _decimal(row.get("model_rank"))
        return value if value is not None else Decimal("999999")

    groups: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        bucket = _text(row.get("report_bucket"))
        report_line = _text(row.get("report_line"))
        if report_artifact and report_line != bucket:
            errors.append(
                f"formal rank report bucket/line mismatch {relative_path}: "
                f"stock_id={_source_key(row)[1]} model_id={_text(row.get('model_id'))}"
            )
        groups.setdefault((bucket, _text(row.get("model_id"))), []).append(row)

    for group_key, members in sorted(groups.items()):
        ordered = sorted(
            members,
            key=lambda row: (
                -score_value(row),
                _source_key(row)[1],
                _text(row.get("source_row_index")),
            ),
        )
        for expected_rank, row in enumerate(ordered, start=1):
            observed_rank = _decimal(row.get("model_rank"))
            if observed_rank != Decimal(expected_rank):
                errors.append(
                    f"formal model rank mismatch {relative_path}: group={group_key} "
                    f"stock_id={_source_key(row)[1]} expected={expected_rank} "
                    f"actual={_text(row.get('model_rank'))!r}"
                )

    if not report_artifact:
        return errors

    for row in rows:
        model_rank = _text(row.get("model_rank"))
        if _text(row.get("model_rank_overall")) != model_rank:
            errors.append(
                f"report model_rank_overall mismatch {relative_path}: "
                f"stock_id={_source_key(row)[1]} model_id={_text(row.get('model_id'))}"
            )
        if _text(row.get("display_rank")) != model_rank:
            errors.append(
                f"report display_rank mismatch {relative_path}: "
                f"stock_id={_source_key(row)[1]} model_id={_text(row.get('model_id'))}"
            )

    status_contracts = (
        (
            "new_model_signal",
            "model_rank_new_signal",
            "display_rank_new_signal",
            "新進榜",
        ),
        (
            "repeated_same_model_signal",
            "model_rank_repeated_signal",
            "display_rank_repeated_signal",
            "連續榜",
        ),
    )
    for status, rank_column, display_column, display_prefix in status_contracts:
        status_groups: dict[tuple[str, str], list[dict[str, str]]] = {}
        for row in rows:
            if _text(row.get("same_model_repeat_status")) == status:
                status_groups.setdefault(
                    (_text(row.get("report_bucket")), _text(row.get("model_id"))),
                    [],
                ).append(row)
            elif _text(row.get(rank_column)) or _text(row.get(display_column)):
                errors.append(
                    f"report inactive rank field must be blank {relative_path}: "
                    f"stock_id={_source_key(row)[1]} column={rank_column}"
                )

        for group_key, members in sorted(status_groups.items()):
            if status == "new_model_signal":
                ordered = sorted(
                    members,
                    key=lambda row: (
                        -score_value(row),
                        rank_value(row),
                        _source_key(row)[1],
                    ),
                )
            else:
                ordered = sorted(
                    members,
                    key=lambda row: (
                        -(
                            _decimal(row.get("same_model_consecutive_days"))
                            or Decimal("0")
                        ),
                        -(
                            _decimal(row.get("same_model_appear_count_10d"))
                            or Decimal("0")
                        ),
                        -score_value(row),
                        rank_value(row),
                        _source_key(row)[1],
                    ),
                )
            for expected_rank, row in enumerate(ordered, start=1):
                expected_display = f"{display_prefix} #{expected_rank}"
                if _decimal(row.get(rank_column)) != Decimal(expected_rank):
                    errors.append(
                        f"report status rank mismatch {relative_path}: group={group_key} "
                        f"status={status} stock_id={_source_key(row)[1]} "
                        f"expected={expected_rank} actual={_text(row.get(rank_column))!r}"
                    )
                if _text(row.get(display_column)) != expected_display:
                    errors.append(
                        f"report status display rank mismatch {relative_path}: group={group_key} "
                        f"status={status} stock_id={_source_key(row)[1]} "
                        f"expected={expected_display!r} actual={_text(row.get(display_column))!r}"
                    )
    return errors


def build_scope_snapshot(root: Path) -> tuple[dict[str, Any], list[str]]:
    artifacts: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    candidate_path = root / ALL_CANDIDATES_ARTIFACT
    if not candidate_path.is_file():
        errors.append(f"missing warrant source artifact: {ALL_CANDIDATES_ARTIFACT}")
    else:
        candidate_columns, candidate_rows = _read_rows(candidate_path)
        non_warrant_columns = [
            column for column in candidate_columns if column not in WARRANT_CANDIDATE_FIELDS
        ]
        missing_warrant_columns = sorted(WARRANT_CANDIDATE_FIELDS - set(candidate_columns))
        if missing_warrant_columns:
            errors.append(
                "all_candidates missing governed warrant columns: "
                + ",".join(missing_warrant_columns)
            )
        canonical_rows = [
            json.dumps(
                {column: row.get(column, "") for column in non_warrant_columns},
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            for row in candidate_rows
        ]
        canonical_rows.sort()
        artifacts[ALL_CANDIDATES_ARTIFACT] = {
            "columns": candidate_columns,
            "non_warrant_columns": non_warrant_columns,
            "total_row_count": len(candidate_rows),
            "protected_row_count": len(candidate_rows),
            "protected_sha256": _canonical_sha256(
                {"columns": non_warrant_columns, "rows": canonical_rows}
            ),
        }

    signal_data: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for relative_path in FORMAL_SIGNAL_ARTIFACTS:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing formal signal artifact: {relative_path}")
            continue

        columns, rows = _read_rows(path)
        if "model_id" not in columns:
            errors.append(f"formal signal artifact missing model_id: {relative_path}")
            continue
        signal_data[relative_path] = (columns, rows)

    latest_raw_rows = signal_data.get(LATEST_SIGNAL_ARTIFACTS[0], ([], []))[1]
    mutable_signal_dates = sorted(
        {_text(row.get("signal_date")) for row in latest_raw_rows if _text(row.get("signal_date"))}
    )
    mutable_signal_date_set = set(mutable_signal_dates)

    for relative_path in FORMAL_SIGNAL_ARTIFACTS:
        if relative_path not in signal_data:
            continue
        columns, rows = signal_data[relative_path]

        identity_columns = [
            column for column in IDENTITY_FIELD_CANDIDATES if column in columns
        ]
        required_identity_columns = {"signal_date", "stock_id", "model_id"}
        has_report_dimension = "report_line" in columns or "report_bucket" in columns
        if not required_identity_columns.issubset(identity_columns) or not has_report_dimension:
            errors.append(f"formal signal identity columns missing: {relative_path}")
            continue

        identity_rows: list[str] = []
        protected_rows: list[str] = []
        protected_model_ids: set[str] = set()
        mutable_row_count = 0
        mutable_score_rows: list[dict[str, Any]] = []
        for normalized in rows:
            identity_rows.append(
                json.dumps(
                    {column: normalized.get(column, "") for column in identity_columns},
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            model_id = normalized["model_id"]
            is_current_row = (
                _text(normalized.get("signal_date")) in mutable_signal_date_set
            )
            is_current_mutable_row = (
                model_id in ALLOWED_MUTABLE_MODEL_IDS and is_current_row
            )
            protected_normalized = dict(normalized)
            if is_current_mutable_row:
                mutable_row_count += 1
                mutable_fields = WARRANT_MUTABLE_FIELDS
                if relative_path == LATEST_SIGNAL_ARTIFACTS[0]:
                    non_warrant_components = [
                        part.strip()
                        for part in _text(normalized.get("score_components")).split("|")
                        if part.strip()
                        and not part.strip().lower().startswith("warrant bullish +")
                    ]
                    mutable_score_rows.append(
                        {
                            "identity": list(_signal_key(normalized)),
                            "model_id": model_id,
                            "warrant_flow_signal": _text(
                                normalized.get("warrant_flow_signal")
                            ).lower(),
                            "non_warrant_score_components": " | ".join(
                                non_warrant_components
                            ),
                            "scores": {
                                column: _text(normalized.get(column))
                                for column in WARRANT_NUMERIC_SCORE_FIELDS
                            },
                        }
                    )
            elif is_current_row:
                protected_model_ids.add(model_id or "__blank__")
                mutable_fields = WARRANT_PRESENTATION_FIELDS
            else:
                protected_model_ids.add(model_id or "__blank__")
                mutable_fields = frozenset()
            for column in mutable_fields:
                if column in protected_normalized:
                    if column in WARRANT_EXPLANATION_FIELDS:
                        protected_normalized[column] = _strip_warrant_explanation(
                            protected_normalized[column]
                        )
                    else:
                        protected_normalized[column] = ""
            protected_rows.append(
                json.dumps(
                    protected_normalized,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )

        identity_rows.sort()
        protected_rows.sort()
        mutable_score_rows.sort(key=lambda row: row["identity"])
        protected_payload = {"columns": columns, "rows": protected_rows}
        artifacts[relative_path] = {
            "columns": columns,
            "identity_columns": identity_columns,
            "identity_row_count": len(identity_rows),
            "identity_sha256": _canonical_sha256(
                {"columns": identity_columns, "rows": identity_rows}
            ),
            "total_row_count": len(rows),
            "mutable_row_count": mutable_row_count,
            "mutable_score_rows": mutable_score_rows,
            "protected_row_count": len(protected_rows),
            "protected_model_ids": sorted(protected_model_ids),
            "protected_sha256": _canonical_sha256(protected_payload),
        }

    aggregate_payload = {
        path: {
            "columns": record["columns"],
            "protected_row_count": record["protected_row_count"],
            "protected_sha256": record["protected_sha256"],
            "identity_row_count": record.get("identity_row_count"),
            "identity_sha256": record.get("identity_sha256"),
        }
        for path, record in sorted(artifacts.items())
    }
    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "allowed_mutable_model_ids": sorted(ALLOWED_MUTABLE_MODEL_IDS),
        "mutable_signal_dates": mutable_signal_dates,
        "artifact_count": len(artifacts),
        "aggregate_sha256": _canonical_sha256(aggregate_payload),
        "artifacts": artifacts,
    }
    return snapshot, errors


def compare_scope_snapshots(before: dict[str, Any], after: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if before.get("schema_version") != SCHEMA_VERSION:
        errors.append("warrant formal sync scope snapshot schema_version mismatch")
    expected_mutable = sorted(ALLOWED_MUTABLE_MODEL_IDS)
    if before.get("allowed_mutable_model_ids") != expected_mutable:
        errors.append("warrant formal sync scope snapshot allowed_mutable_model_ids mismatch")
    if before.get("mutable_signal_dates") != after.get("mutable_signal_dates"):
        errors.append("warrant formal sync mutable_signal_dates drift")

    before_artifacts = before.get("artifacts")
    after_artifacts = after.get("artifacts")
    if not isinstance(before_artifacts, dict):
        errors.append("warrant formal sync scope before snapshot artifacts must be an object")
        before_artifacts = {}
    if not isinstance(after_artifacts, dict):
        errors.append("warrant formal sync scope after snapshot artifacts must be an object")
        after_artifacts = {}

    for relative_path in sorted(set(before_artifacts) | set(after_artifacts)):
        if relative_path not in before_artifacts:
            errors.append(f"protected formal signal artifact added: {relative_path}")
            continue
        if relative_path not in after_artifacts:
            errors.append(f"protected formal signal artifact removed: {relative_path}")
            continue
        before_record = before_artifacts[relative_path]
        after_record = after_artifacts[relative_path]
        if before_record.get("columns") != after_record.get("columns"):
            errors.append(f"formal signal schema drift outside warrant sync scope: {relative_path}")
        if relative_path == ALL_CANDIDATES_ARTIFACT:
            if before_record.get("non_warrant_columns") != after_record.get("non_warrant_columns"):
                errors.append("all_candidates non-warrant schema drift")
            if before_record.get("protected_row_count") != after_record.get("protected_row_count"):
                errors.append("all_candidates non-warrant row-count drift")
            if before_record.get("protected_sha256") != after_record.get("protected_sha256"):
                errors.append("all_candidates non-warrant content drift")
            continue
        if before_record.get("identity_row_count") != after_record.get("identity_row_count"):
            errors.append(f"formal signal identity row-count drift: {relative_path}")
        if before_record.get("identity_sha256") != after_record.get("identity_sha256"):
            errors.append(f"formal signal identity membership drift: {relative_path}")
        if before_record.get("protected_row_count") != after_record.get("protected_row_count"):
            errors.append(f"formal signal protected row-count drift: {relative_path}")
        if before_record.get("protected_sha256") != after_record.get("protected_sha256"):
            errors.append(f"formal signal non-warrant semantic hash drift: {relative_path}")

    before_raw = before_artifacts.get(LATEST_SIGNAL_ARTIFACTS[0], {})
    after_raw = after_artifacts.get(LATEST_SIGNAL_ARTIFACTS[0], {})
    if isinstance(before_raw, dict) and isinstance(after_raw, dict):
        errors.extend(
            validate_warrant_score_delta(
                before_raw.get("mutable_score_rows"),
                after_raw.get("mutable_score_rows"),
            )
        )

    return errors


def validate_staged_path_list(paths: list[str]) -> list[str]:
    errors: list[str] = []
    for raw_path in paths:
        path = raw_path.strip().replace("\\", "/")
        if not path:
            continue
        if not any(fnmatchcase(path, pattern) for pattern in STAGED_ALLOWED_PATTERNS):
            errors.append(f"warrant formal sync staged path is outside allowlist: {path}")
    return errors


def staged_paths(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    return [item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def validate_current_projection(root: Path) -> tuple[list[str], dict[str, int]]:
    errors = validate_warrant_bonus_parameter_contract(root)
    metrics = {
        "candidate_rows": 0,
        "warrant_rows": 0,
        "raw_signal_rows": 0,
        "report_signal_rows": 0,
        "history_signal_rows": 0,
    }
    candidate_path = root / ALL_CANDIDATES_ARTIFACT
    if not candidate_path.is_file():
        return [f"missing warrant source artifact: {ALL_CANDIDATES_ARTIFACT}"], metrics

    candidate_columns, candidate_rows = _read_rows(candidate_path)
    required_candidate_columns = {
        "source_row_index",
        "stock_id",
        *WARRANT_CANDIDATE_FIELDS,
    }
    missing_candidate_columns = sorted(required_candidate_columns - set(candidate_columns))
    if missing_candidate_columns:
        errors.append(
            "all_candidates warrant projection columns missing: "
            + ",".join(missing_candidate_columns)
        )
        return errors, metrics

    candidate_by_key: dict[tuple[str, str], dict[str, str]] = {}
    candidate_signals_by_stock: dict[str, set[str]] = {}
    for row in candidate_rows:
        key = _source_key(row)
        if not all(key):
            errors.append(f"all_candidates has incomplete warrant projection key: {key}")
            continue
        if key in candidate_by_key:
            errors.append(f"all_candidates has duplicate warrant projection key: {key}")
            continue
        projection = _candidate_warrant_projection(row)
        signal = projection["warrant_flow_signal"]
        candidate_by_key[key] = projection
        candidate_signals_by_stock.setdefault(key[1], set()).add(signal)
    metrics["candidate_rows"] = len(candidate_by_key)
    if not candidate_by_key:
        errors.append("all_candidates warrant projection has no rows")
    candidate_by_stock: dict[str, str] = {}
    for stock_id, signals in sorted(candidate_signals_by_stock.items()):
        if len(signals) != 1:
            errors.append(
                f"all_candidates has inconsistent warrant signals for stock_id={stock_id}: "
                + ",".join(sorted(signals))
            )
            continue
        candidate_by_stock[stock_id] = next(iter(signals))

    warrant_path = root / WARRANT_FLOW_ARTIFACT
    warrant_by_stock: dict[str, dict[str, str]] = {}
    warrant_dates: set[str] = set()
    if not warrant_path.is_file():
        errors.append(f"missing official warrant projection artifact: {WARRANT_FLOW_ARTIFACT}")
    else:
        warrant_columns, warrant_rows = _read_rows(warrant_path)
        missing_warrant_columns = sorted(
            {"date", "stock_id", *WARRANT_SOURCE_TO_CANDIDATE_FIELDS}
            - set(warrant_columns)
        )
        if missing_warrant_columns:
            errors.append(
                "official warrant projection columns missing: "
                + ",".join(missing_warrant_columns)
            )
        else:
            for row in warrant_rows:
                raw_stock_id = _text(row.get("stock_id"))
                stock_id = raw_stock_id.zfill(4) if raw_stock_id else ""
                date_value = _date_text(row.get("date"))
                if not stock_id:
                    errors.append("official warrant projection has blank stock_id")
                    continue
                if not date_value:
                    errors.append(f"official warrant projection has invalid date for stock_id={stock_id}")
                else:
                    warrant_dates.add(date_value)
                if stock_id in warrant_by_stock:
                    errors.append(f"official warrant projection has duplicate stock_id={stock_id}")
                    continue
                warrant_by_stock[stock_id] = _official_warrant_projection(row)
    metrics["warrant_rows"] = len(warrant_by_stock)
    if not warrant_by_stock:
        errors.append("official warrant projection has no rows")
    if len(warrant_dates) != 1:
        errors.append(
            "official warrant projection must have exactly one valid date: "
            f"{sorted(warrant_dates)}"
        )
    candidate_dates = {
        _date_text(
            row.get("main_price_date")
            or row.get("signal_date")
            or row.get("date")
        )
        for row in candidate_rows
    }
    candidate_dates.discard("")
    if len(candidate_dates) != 1:
        errors.append(
            "all_candidates must have exactly one valid formal date: "
            f"{sorted(candidate_dates)}"
        )
    if len(warrant_dates) == 1 and len(candidate_dates) == 1 and warrant_dates != candidate_dates:
        errors.append(
            "official warrant projection date does not match all_candidates date: "
            f"warrant={next(iter(warrant_dates))} candidates={next(iter(candidate_dates))}"
        )
    empty_projection = {column: "" for column in WARRANT_CANDIDATE_FIELDS}
    for source_key, candidate_projection in candidate_by_key.items():
        expected_projection = warrant_by_stock.get(source_key[1], empty_projection)
        for column in sorted(WARRANT_CANDIDATE_FIELDS):
            expected_value = expected_projection[column]
            actual_value = candidate_projection[column]
            if actual_value != expected_value:
                errors.append(
                    "all_candidates warrant projection mismatch: "
                    f"source_key={source_key} column={column} "
                    f"expected={expected_value!r} actual={actual_value!r}"
                )

    signal_rows_by_path: dict[str, dict[tuple[str, str, str, str, str], dict[str, str]]] = {}
    signal_columns_by_path: dict[str, list[str]] = {}
    required_signal_columns = {
        "signal_date",
        "source_row_index",
        "stock_id",
        "model_id",
        "model_score",
        "model_rank",
        "warrant_flow_signal",
    }
    for relative_path in LATEST_SIGNAL_ARTIFACTS:
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing latest formal signal artifact: {relative_path}")
            continue
        columns, rows = _read_rows(path)
        signal_columns_by_path[relative_path] = columns
        missing_columns = sorted(required_signal_columns - set(columns))
        if missing_columns:
            errors.append(
                f"latest formal signal artifact missing columns {relative_path}: "
                + ",".join(missing_columns)
            )
            continue
        rows_by_key: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
        for row in rows:
            signal_key = _signal_key(row)
            if not all(signal_key):
                errors.append(
                    f"latest formal signal artifact has incomplete identity {relative_path}: "
                    f"{signal_key}"
                )
                continue
            if signal_key in rows_by_key:
                errors.append(
                    f"latest formal signal artifact has duplicate identity {relative_path}: "
                    f"{signal_key}"
                )
                continue
            rows_by_key[signal_key] = row
            if relative_path == LATEST_SIGNAL_ARTIFACTS[0]:
                errors.extend(validate_warrant_bonus_marker(row, relative_path))
            source_key = _source_key(row)
            candidate_projection = candidate_by_key.get(source_key)
            expected_signal = (
                candidate_projection.get("warrant_flow_signal")
                if candidate_projection is not None
                else None
            )
            actual_signal = _text(row.get("warrant_flow_signal")).lower()
            if expected_signal is None:
                model_id = _text(row.get("model_id"))
                if model_id in NON_CANDIDATE_WARRANT_EXEMPT_MODEL_IDS and not actual_signal:
                    continue
                if (
                    model_id in STOCK_LEVEL_CANDIDATE_PROJECTED_MODEL_IDS
                    and re.fullmatch(r"volume_breakout:[0-9]+", source_key[0])
                ):
                    expected_signal = candidate_by_stock.get(source_key[1])
                if expected_signal is None:
                    errors.append(
                        f"formal signal row has no all_candidates warrant source {relative_path}: "
                        f"{signal_key}"
                    )
                    continue
            if actual_signal != expected_signal:
                errors.append(
                    f"formal signal warrant projection mismatch {relative_path}: "
                    f"{signal_key} expected={expected_signal!r} actual={actual_signal!r}"
                )
        signal_rows_by_path[relative_path] = rows_by_key

    raw_by_key = signal_rows_by_path.get(LATEST_SIGNAL_ARTIFACTS[0], {})
    report_by_key = signal_rows_by_path.get(LATEST_SIGNAL_ARTIFACTS[1], {})
    metrics["raw_signal_rows"] = len(raw_by_key)
    metrics["report_signal_rows"] = len(report_by_key)
    errors.extend(
        validate_model_rank_contract(
            signal_columns_by_path.get(LATEST_SIGNAL_ARTIFACTS[0], []),
            list(raw_by_key.values()),
            LATEST_SIGNAL_ARTIFACTS[0],
            report_artifact=False,
        )
    )
    errors.extend(
        validate_model_rank_contract(
            signal_columns_by_path.get(LATEST_SIGNAL_ARTIFACTS[1], []),
            list(report_by_key.values()),
            LATEST_SIGNAL_ARTIFACTS[1],
            report_artifact=True,
        )
    )
    raw_signal_dates = {key[0] for key in raw_by_key}
    report_signal_dates = {key[0] for key in report_by_key}
    expected_formal_date = (
        next(iter(candidate_dates))
        if len(candidate_dates) == 1 and candidate_dates == warrant_dates
        else ""
    )
    for label, observed_dates in (
        ("raw formal signals", raw_signal_dates),
        ("report formal signals", report_signal_dates),
    ):
        if len(observed_dates) > 1:
            errors.append(f"{label} have multiple signal dates: {sorted(observed_dates)}")
        if observed_dates and expected_formal_date and observed_dates != {expected_formal_date}:
            errors.append(
                f"{label} date must equal formal warrant/candidate date "
                f"{expected_formal_date}: observed={sorted(observed_dates)}"
            )
    for key in sorted(set(raw_by_key) - set(report_by_key)):
        errors.append(f"raw formal signal row missing from report signals: {key}")
    for key in sorted(set(report_by_key) - set(raw_by_key)):
        errors.append(f"report signal row missing from raw formal signals: {key}")
    for key in sorted(set(raw_by_key) & set(report_by_key)):
        raw = raw_by_key[key]
        row = report_by_key[key]
        parity_columns = {
            "warrant_flow_signal",
            *(
                (WARRANT_SCORE_AND_RANK_FIELDS | WARRANT_PRESENTATION_FIELDS)
                & set(raw)
                & set(row)
            ),
        }
        for column in sorted(parity_columns):
            if _text(row.get(column)) != _text(raw.get(column)):
                errors.append(
                    f"raw/report warrant formal sync mismatch key={key} column={column}"
                )

    errors.extend(
        validate_frontpage_uniqueness(
            root,
            signal_columns_by_path.get(LATEST_SIGNAL_ARTIFACTS[1], []),
            list(report_by_key.values()),
        )
    )

    current_signal_dates = raw_signal_dates
    report_by_history_key: dict[tuple[str, str, str, str], dict[str, str]] = {}
    for key, row in report_by_key.items():
        history_key = (key[0], key[1], key[3], key[4])
        if history_key in report_by_history_key:
            errors.append(f"report formal signal has duplicate history identity: {history_key}")
            continue
        report_by_history_key[history_key] = row

    history_path = root / FORMAL_SIGNAL_ARTIFACTS[2]
    history_by_key: dict[tuple[str, str, str, str], dict[str, str]] = {}
    if not history_path.is_file():
        errors.append(f"missing formal signal history artifact: {FORMAL_SIGNAL_ARTIFACTS[2]}")
    else:
        history_columns, history_rows = _read_rows(history_path)
        required_history_columns = {"signal_date", "stock_id", "model_id", "model_score", "model_rank"}
        missing_history_columns = sorted(required_history_columns - set(history_columns))
        has_history_report_dimension = "report_line" in history_columns or "report_bucket" in history_columns
        if missing_history_columns or not has_history_report_dimension:
            errors.append(
                "formal signal history parity columns missing: "
                + ",".join(missing_history_columns or ["report_line_or_report_bucket"])
            )
        else:
            for row in history_rows:
                signal_date = _text(row.get("signal_date"))
                if signal_date not in current_signal_dates:
                    continue
                raw_stock_id = _text(row.get("stock_id"))
                stock_id = raw_stock_id.zfill(4) if raw_stock_id else ""
                history_key = (
                    signal_date,
                    _report_line(row),
                    stock_id,
                    _text(row.get("model_id")),
                )
                if not all(history_key):
                    errors.append(f"formal signal history has incomplete identity: {history_key}")
                    continue
                if history_key in history_by_key:
                    errors.append(f"formal signal history has duplicate identity: {history_key}")
                    continue
                history_by_key[history_key] = row

    metrics["history_signal_rows"] = len(history_by_key)
    for key in sorted(set(report_by_history_key) - set(history_by_key)):
        errors.append(f"report formal signal row missing from current history: {key}")
    for key in sorted(set(history_by_key) - set(report_by_history_key)):
        errors.append(f"current history row missing from report formal signals: {key}")
    for key in sorted(set(report_by_history_key) & set(history_by_key)):
        report_row = report_by_history_key[key]
        history_row = history_by_key[key]
        parity_columns = (
            WARRANT_SCORE_AND_RANK_FIELDS
            & set(report_row)
            & set(history_row)
        )
        for column in sorted(parity_columns):
            if _text(report_row.get(column)) != _text(history_row.get(column)):
                errors.append(f"report/history formal signal mismatch key={key} column={column}")

    return errors, metrics


def _write_snapshot(path: Path, snapshot: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fail closed when warrant formal sync changes models without approved warrant "
            "score effects or leaves source/signal/report warrant projections inconsistent."
        )
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write-snapshot", type=Path)
    action.add_argument("--compare-snapshot", type=Path)
    action.add_argument("--validate-staged", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()

    root = args.repo_root.resolve()
    if args.validate_staged:
        try:
            paths = staged_paths(root)
        except (OSError, subprocess.CalledProcessError) as exc:
            print(f"ERROR: unable to inspect staged warrant formal sync paths: {exc}")
            return 1
        staged_errors = validate_staged_path_list(paths)
        if staged_errors:
            for error in staged_errors:
                print(f"ERROR: {error}")
            return 1
        print(f"warrant formal sync staged path validation passed: staged_paths={len(paths)}")
        return 0

    snapshot, errors = build_scope_snapshot(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    if args.write_snapshot is not None:
        _write_snapshot(args.write_snapshot, snapshot)
        print(
            "warrant formal sync scope snapshot captured "
            f"artifacts={snapshot['artifact_count']} "
            f"aggregate_sha256={snapshot['aggregate_sha256']}"
        )
        return 0

    projection_errors, metrics = validate_current_projection(root)
    if projection_errors:
        for error in projection_errors:
            print(f"ERROR: {error}")
        return 1

    try:
        before = json.loads(args.compare_snapshot.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: unable to read warrant formal sync scope snapshot: {exc}")
        return 1

    compare_errors = compare_scope_snapshots(before, snapshot)
    if compare_errors:
        for error in compare_errors:
            print(f"ERROR: {error}")
        return 1

    print(f"warrant_formal_sync_scope_before_sha256={before.get('aggregate_sha256', '')}")
    print(f"warrant_formal_sync_scope_after_sha256={snapshot['aggregate_sha256']}")
    for relative_path, record in sorted(snapshot["artifacts"].items()):
        if relative_path == ALL_CANDIDATES_ARTIFACT:
            print(
                "warrant_formal_sync_scope_artifact "
                f"path={relative_path} protected_rows={record['protected_row_count']} "
                f"protected_sha256={record['protected_sha256']}"
            )
            continue
        print(
            "warrant_formal_sync_scope_artifact "
            f"path={relative_path} protected_rows={record['protected_row_count']} "
            f"mutable_rows={record['mutable_row_count']} "
            f"identity_sha256={record['identity_sha256']} "
            f"protected_sha256={record['protected_sha256']}"
        )
    print(
        "warrant_projection "
        f"candidate_rows={metrics['candidate_rows']} "
        f"warrant_rows={metrics['warrant_rows']} "
        f"raw_signal_rows={metrics['raw_signal_rows']} "
        f"report_signal_rows={metrics['report_signal_rows']} "
        f"history_signal_rows={metrics['history_signal_rows']}"
    )
    print("warrant formal sync scope and projection validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
