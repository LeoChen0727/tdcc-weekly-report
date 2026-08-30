from __future__ import annotations

import argparse
import csv
import ast
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
STOCK_MODEL_CONTRACT = ROOT / "config" / "stock_model_contract_registry.csv"
EVENT_CATALYST_CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"

RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
MODEL_LAYER = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
CHATGPT_OUTPUT_ROOT = ROOT / "chatgpt_side_outputs_official"

DAILY_MODEL_SIGNALS = ROOT / "output/latest/daily_candidate_model_signals_for_report_latest.csv"
DAILY_MODEL_REGISTRY = ROOT / "output/latest/daily_report_model_registry_latest.csv"
DAILY_MODEL_PARAMETERS = ROOT / "output/latest/daily_candidate_model_parameters_latest.csv"
DAILY_MODEL_READINESS = ROOT / "output/latest/model_operation_readiness_latest.csv"
W_BOTTOM_OPERATION_ARTIFACTS = {
    "w_bottom_right_side": ROOT / "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
    "neckline_volume_breakout_confirmation": (
        ROOT / "output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
    ),
}
VOLUME_BREAKOUT_V2_MODEL_IDS = (
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
)
OPERATION_ROW_METRIC_REQUIRED_COLUMNS = {
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
}
PDF_OPERATION_ADAPTER_ARTIFACTS = {
    **{
        model_id: ROOT / "output/latest/daily_volume_breakout_operation_section_latest.csv"
        for model_id in VOLUME_BREAKOUT_V2_MODEL_IDS
    },
    **W_BOTTOM_OPERATION_ARTIFACTS,
    "price_pullback_23ema": ROOT / "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
}
PDF_OPERATION_RENDERER_TOKENS = {
    "volume_range_breakout_v2_low_position_volume_attack": (
        "VOLUME_BREAKOUT_V2_LOW_MODEL_ID",
        "daily_volume_breakout_operation_section_latest.csv",
        "render_volume_range_breakout_operation_section",
    ),
    "volume_range_breakout_v2_mid_position_momentum_attack": (
        "VOLUME_BREAKOUT_V2_MID_MODEL_ID",
        "daily_volume_breakout_operation_section_latest.csv",
        "render_volume_range_breakout_operation_section",
    ),
    "volume_range_breakout_v2_high_position_volume_attack": (
        "VOLUME_BREAKOUT_V2_HIGH_MODEL_ID",
        "daily_volume_breakout_operation_section_latest.csv",
        "render_volume_range_breakout_operation_section",
    ),
    "w_bottom_right_side": (
        "W_BOTTOM_RIGHT_SIDE_MODEL_ID",
        "daily_w_bottom_right_side_operation_section_latest.csv",
        "render_w_bottom_operation_section",
    ),
    "neckline_volume_breakout_confirmation": (
        "W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID",
        "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
        "render_w_bottom_operation_section",
    ),
    "price_pullback_23ema": (
        "PRICE_PULLBACK_MODEL_ID",
        "daily_price_pullback_23ema_operation_section_latest.csv",
        "render_price_pullback_operation_section",
    ),
}
W_BOTTOM_OPERATION_REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "row_type",
    "display_order",
    "operation_asof_date",
    "report_line",
    "report_line_memberships",
    "operation_status",
    "row_action_status",
    "buy_rank_eligible",
    "stock_display",
    "entry_rule_id",
    "entry_basis_zh",
    "stop_loss_rule_id",
    "exit_rule_id",
    "planned_holding_days",
} | OPERATION_ROW_METRIC_REQUIRED_COLUMNS
W_BOTTOM_OPERATION_REQUIRED_SECTIONS = {"confirmed_operation", "active_operation"}
W_BOTTOM_OPERATION_REQUIRED_VIEWS = {"highlight", "full"}
PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "row_type",
    "display_order",
    "operation_asof_date",
    "report_line",
    "report_line_memberships",
    "operation_status",
    "row_action_status",
    "buy_rank_eligible",
    "stock_display",
    "operation_quality_zh",
    "operation_status_zh",
    "signal_date",
    "entry_rule_id",
    "entry_basis_zh",
    "stop_loss_rule_id",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
    "operation_age_days",
    "rank_reason_zh",
    "risk_tags_zh",
} | OPERATION_ROW_METRIC_REQUIRED_COLUMNS
VOLUME_OPERATION_REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "row_type",
    "display_order",
    "operation_asof_date",
    "operation_status",
    "row_action_status",
    "buy_rank_eligible",
    "stock_display",
    "entry_rule_id",
    "entry_basis_zh",
    "stop_loss_rule_id",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
} | OPERATION_ROW_METRIC_REQUIRED_COLUMNS
PDF_OPERATION_REQUIRED_SECTIONS = {"confirmed_operation", "active_operation"}
PDF_OPERATION_REQUIRED_VIEWS = {"highlight", "full"}
PDF_OPERATION_REQUIRED_COLUMNS_BY_MODEL = {
    **{model_id: VOLUME_OPERATION_REQUIRED_COLUMNS for model_id in VOLUME_BREAKOUT_V2_MODEL_IDS},
    "w_bottom_right_side": W_BOTTOM_OPERATION_REQUIRED_COLUMNS,
    "neckline_volume_breakout_confirmation": W_BOTTOM_OPERATION_REQUIRED_COLUMNS,
    "price_pullback_23ema": PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS,
}
PDF_OPERATION_ALLOWED_SECTIONS_BY_MODEL = {
    **{
        model_id: {
            "confirmed_operation",
            "confirmed_unranked_operation",
            "pending_confirmation",
            "active_operation",
        }
        for model_id in VOLUME_BREAKOUT_V2_MODEL_IDS
    },
    "w_bottom_right_side": PDF_OPERATION_REQUIRED_SECTIONS,
    "neckline_volume_breakout_confirmation": PDF_OPERATION_REQUIRED_SECTIONS,
    "price_pullback_23ema": PDF_OPERATION_REQUIRED_SECTIONS,
}


def allowed_model_ids_for_operation_artifact(model_id: str, path: Path) -> set[str]:
    if model_id in VOLUME_BREAKOUT_V2_MODEL_IDS and path.name == "daily_volume_breakout_operation_section_latest.csv":
        return set(VOLUME_BREAKOUT_V2_MODEL_IDS)
    return {model_id}

DAILY_MODEL_OUTPUTS = (
    DAILY_MODEL_SIGNALS,
    DAILY_MODEL_REGISTRY,
)

DAILY_EVENT_OUTPUTS = (
    ROOT / "output/latest/all_candidates_latest.csv",
    ROOT / "output/latest/daily_candidate_model_signals_for_report_latest.csv",
)

DAILY_PDF_SOURCE_PATHS = (
    RENDERER,
    ENTRYPOINT,
)

WORD_RE_TEMPLATE = r"(?<![A-Za-z0-9_]){}(?![A-Za-z0-9_])"
SCORE_CONTEXT_RE = re.compile(
    r"\b(score|scores|scoring|weighted|bonus|penalty|formula|calculation|calculate|calc|component)\b"
)
SCORE_NAME_RE = re.compile(r"\b[A-Za-z0-9_]*_score\b")
RANKING_CONTEXT_RE = re.compile(r"\b(rank|ranking|sort_values|sort_index|order|ascending|descending)\b")
RANKING_NAME_RE = re.compile(r"\b(rank_[A-Za-z0-9_]*|[A-Za-z0-9_]*_rank)\b")
REASON_CONTEXT_RE = re.compile(
    r"\b(reason|why_selected|recommend|recommended|recommendation|buy|sell|judgment|action|operation_note|next_confirmation)\b"
)

PRIVATE_PDF_RULE_PATTERNS = {
    r"\bcompute_action_decision\b": "PDF renderer must not compute old action decisions",
    r"\baction_decision_utils\b": "PDF renderer must not import old action decision helpers",
    r"\bdaily_model_parameter_recommendations_latest\.csv\b": (
        "PDF renderer must not read research recommendation outputs directly"
    ),
    r"\bdaily_model_parameter_research_latest\.csv\b": (
        "PDF renderer must not read research parameter outputs directly"
    ),
    r"\bresearch_backtest\b": "PDF renderer must not consume research/backtest lane outputs directly",
    r"\bgenerate_repo_chatgpt_side_reports\.py\b": "PDF renderer must not use retired helper report generator paths",
    r"\bpdf_side_(?:score|ranking|rank|buy|sell|judgment|reason)\b": (
        "PDF renderer must not define private PDF-side scoring/ranking/judgment rules"
    ),
}

FORBIDDEN_RESEARCH_RECOMMENDATION_COLUMNS = {
    "condition_function",
    "score_function",
    "score_profile_id",
    "model_score",
    "model_rank",
    "display_rank",
    "pdf_visibility",
    "model_registry_order",
    "model_registry_active",
    "report_line_applicability",
}

DISPLAY_MODEL_VISIBILITIES = {"pdf_core_model", "pdf_specialty_section"}
REVENUE_UNREACTED_RANGE_MODEL_ID = "revenue_unreacted_range"
REVENUE_PRODUCTION_PERMISSION_FIELDS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
)
VALIDATION_PHASE_FULL = "full"
VALIDATION_PHASE_RUNTIME = "runtime"
VALIDATION_PHASES = (VALIDATION_PHASE_FULL, VALIDATION_PHASE_RUNTIME)
MODEL_EMPTY_STATE_TEXT = "本日無股票推薦"
OPERATION_ACTIVE_EMPTY_STATE_TEXT = "目前無操作中追蹤列"
OPERATION_CONFIRMED_BUY_TABLE_TITLE = "本日可買 / 已確認買入候選"
OPERATION_ACTIVE_TABLE_TITLE = "操作中"
FORBIDDEN_RENDERER_MODEL_STATUS_SUMMARY_TOKENS = (
    "append_model_status_table",
    "build_model_status_table",
    "模型狀態 / PDF整合",
    "本日表格狀態",
)
FORBIDDEN_OPERATION_HIGHLIGHT_EMPTY_STATE_TOKENS = (
    "目前無已確認操作",
    "DAILY_HIGHLIGHT_VOLUME_EMPTY_CONFIRMED_POLICY",
    "should_render_highlight_confirmed_empty_table",
)
REQUIRED_RENDERER_MODEL_ORDER_TOKENS = (
    "PDF_PRESENTATION_MODEL_ORDER_OVERRIDES",
    "VOLUME_BREAKOUT_V2_LOW_MODEL_ID: 1.0",
    "VOLUME_BREAKOUT_V2_MID_MODEL_ID: 1.05",
    "VOLUME_BREAKOUT_V2_HIGH_MODEL_ID] = 1.08",
    "W_BOTTOM_RIGHT_SIDE_MODEL_ID: 1.1",
    "W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID: 1.2",
    "PRICE_PULLBACK_MODEL_ID: 1.3",
)
REQUIRED_OPERATION_HIGHLIGHT_CONTRACT_TOKENS = (
    "OPERATION_TABLE_MODEL_IDS",
    "W_BOTTOM_OPERATION_TABLE_MODEL_IDS",
    "W_BOTTOM_OPERATION_INPUT_KEYS",
    "PRICE_PULLBACK_OPERATION_INPUT_KEY",
    "VOLUME_BREAKOUT_V2_LOW_MODEL_ID",
    "VOLUME_BREAKOUT_V2_MID_MODEL_ID",
    "VOLUME_BREAKOUT_V2_HIGH_MODEL_ID",
    "daily_w_bottom_right_side_operation_section_latest.csv",
    "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
    "daily_price_pullback_23ema_operation_section_latest.csv",
    "render_w_bottom_operation_section",
    "render_price_pullback_operation_section",
    "w_bottom_operation_frame",
    "price_pullback_operation_frame",
    "pdf_integrated_daily_adapter",
    "OPERATION_HIGHLIGHT_TABLE_CONTRACT = \"confirmed_buy_then_active_only\"",
    "OPERATION_CONFIRMED_BUY_TABLE_TITLE = \"本日可買 / 已確認買入候選\"",
    "OPERATION_ACTIVE_TABLE_TITLE = \"操作中\"",
    "OPERATION_ACTIVE_EMPTY_STATE_TEXT = \"目前無操作中追蹤列\"",
    "W_BOTTOM_RIGHT_SIDE_MODEL_ID",
    "W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID",
    "PRICE_PULLBACK_MODEL_ID",
)
REQUIRED_OPERATION_HIGHLIGHT_DISPLAY_LIMIT_TOKENS = (
    "OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS = 10",
    "OPERATION_HIGHLIGHT_ROW_LIMITS",
    '"active_operation": OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS',
    "def operation_highlight_row_limit(",
    "def limit_operation_rows_for_pdf_view(",
    "return limit_operation_rows_for_pdf_view(selected, pdf_view, pdf_section)",
)
FORBIDDEN_OPERATION_HIGHLIGHT_DISPLAY_LIMIT_TOKENS = (
    "VOLUME_OPERATION_HIGHLIGHT_LIMITS",
    "W_BOTTOM_OPERATION_HIGHLIGHT_LIMITS",
    '"confirmed_operation": 10',
    "'confirmed_operation': 10",
    '"active_operation": 5',
    "'active_operation': 5",
    '"active_operation": None',
    "'active_operation': None",
)
REQUIRED_STOCK_MODEL_HEADER_LAYOUT_TOKENS = (
    'PDF_MODEL_TITLE_BLUE = "#1f4e79"',
    "MODEL_H1 = ParagraphStyle(",
    "MODEL_H2 = ParagraphStyle(",
    "MODEL_SUMMARY_NUMBER_RE = re.compile(",
    'OPERATION_MODEL_SAMPLING_TEXT = "取樣：已確認欄位股票精華版全部列出，操作中欄位股票精華版最多列出十檔股票。"',
    "def operation_model_summary_lines(",
    "def append_stock_model_summary_lines(",
    "def append_stock_model_title(",
    "STOCK_MODEL_SECTION_TABLE_START_MIN_ROOM = 168 * mm",
    "def append_stock_model_section_start(",
    "CondPageBreak(STOCK_MODEL_SECTION_TABLE_START_MIN_ROOM)",
    "append_stock_model_title(story, model_name, level=1)",
    "append_stock_model_section_start(story, model_name, level=2)",
    "append_stock_model_description_lines(story, desc)",
)
FORBIDDEN_STOCK_MODEL_HEADER_LAYOUT_TOKENS = (
    "story.append(Paragraph(model_name, H1))",
    "story.append(Paragraph(model_name, H2))",
    "story.append(para(desc, BODY_SMALL))",
    "story.append(para(operation_model_summary_text(inputs, model_id), BODY_SMALL))",
)
REQUIRED_OPERATION_SECTION_PAGEBREAK_TOKENS = (
    "OPERATION_SECTION_TABLE_START_MIN_ROOM = 88 * mm",
    "OPERATION_SECTION_SHORT_TABLE_START_MIN_ROOM = 48 * mm",
    "OPERATION_SECTION_SHORT_TABLE_MAX_ROWS = 3",
    "def operation_section_table_start_min_room(",
    "def append_section_label_with_table(",
    "CondPageBreak(operation_section_table_start_min_room(table_flowable))",
    "append_section_label_with_table(\n        story,\n        OPERATION_CONFIRMED_BUY_TABLE_TITLE,",
    "append_section_label_with_table(\n        story,\n        OPERATION_ACTIVE_TABLE_TITLE,",
)
FORBIDDEN_OPERATION_SECTION_PAGEBREAK_TOKENS = (
    "story.append(keep_with_next(Paragraph(escape_html(label), H2)))",
    "story.append(Paragraph(OPERATION_CONFIRMED_BUY_TABLE_TITLE, H2))",
    "story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))",
    'story.append(Paragraph("已確認但未通過買入排名門檻", H2))',
    'story.append(Paragraph("待確認", H2))',
)


@dataclass(frozen=True)
class EventFieldUsage:
    field_name: str
    path: str
    context: str
    line_no: int | None = None
    line: str = ""


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "").strip() for key, value in row.items()} for row in csv.DictReader(fh)]


def csv_header(path: Path) -> list[str]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        try:
            return [str(column or "").strip() for column in next(reader)]
        except StopIteration:
            return []


def bool_value(row: dict[str, str], column: str) -> bool:
    return row.get(column, "").strip().lower() == "true"


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def remove_field_name(line: str, field_name: str) -> str:
    return re.sub(WORD_RE_TEMPLATE.format(re.escape(field_name.lower())), " ", line.lower())


def source_contexts(line: str, field_name: str) -> set[str]:
    context_line = remove_field_name(line, field_name)
    contexts: set[str] = set()
    if SCORE_CONTEXT_RE.search(context_line) or SCORE_NAME_RE.search(context_line):
        contexts.add("score")
    if RANKING_CONTEXT_RE.search(context_line) or RANKING_NAME_RE.search(context_line):
        contexts.add("ranking")
    if REASON_CONTEXT_RE.search(context_line):
        contexts.add("reason")
    if not contexts:
        contexts.add("source_reference")
    return contexts


def model_ids_from_report_outputs(paths: Iterable[Path] = DAILY_MODEL_OUTPUTS) -> set[str]:
    model_ids: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            if "model_id" not in (reader.fieldnames or []):
                continue
            for row in reader:
                model_id = str(row.get("model_id") or "").strip()
                if model_id:
                    model_ids.add(model_id)
    return model_ids


def rows_by_model_id(rows: Iterable[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("model_id", ""): row for row in rows if row.get("model_id", "")}


def dormant_registry_only_model_ids(
    reported_model_ids: Iterable[str],
    signal_model_ids: Iterable[str],
    registry_rows: Iterable[dict[str, str]],
    model_rows: Iterable[dict[str, str]],
    readiness_rows: Iterable[dict[str, str]],
) -> set[str]:
    """Return exact renderer-suppressed roster metadata, never signal rows."""

    reported = set(reported_model_ids)
    signals = set(signal_model_ids)
    if (
        REVENUE_UNREACTED_RANGE_MODEL_ID not in reported
        or REVENUE_UNREACTED_RANGE_MODEL_ID in signals
        or not any(
            row.get("model_id", "") == REVENUE_UNREACTED_RANGE_MODEL_ID
            for row in registry_rows
        )
    ):
        return set()

    contract_rows = [
        row
        for row in model_rows
        if row.get("model_id", "") == REVENUE_UNREACTED_RANGE_MODEL_ID
    ]
    readiness_matches = [
        row
        for row in readiness_rows
        if row.get("model_id", "") == REVENUE_UNREACTED_RANGE_MODEL_ID
    ]
    if len(contract_rows) != 1 or len(readiness_matches) != 1:
        return set()
    if bool_value(contract_rows[0], "approved_for_daily_pdf"):
        return set()

    readiness = readiness_matches[0]
    if any(bool_value(readiness, field) for field in REVENUE_PRODUCTION_PERMISSION_FIELDS):
        return set()
    if readiness.get("pdf_integration_status", "") == "pdf_integrated_daily_adapter":
        return set()
    return {REVENUE_UNREACTED_RANGE_MODEL_ID}


def approved_pdf_contract_model_ids(model_rows: Iterable[dict[str, str]]) -> set[str]:
    return {
        row.get("model_id", "")
        for row in model_rows
        if row.get("model_id", "")
        and bool_value(row, "approved_for_daily_pdf")
        and row.get("pdf_visibility", "") in DISPLAY_MODEL_VISIBILITIES
    }


def readiness_pdf_display_model_ids(
    parameter_rows: Iterable[dict[str, str]],
    readiness_rows: Iterable[dict[str, str]],
) -> set[str]:
    parameters = rows_by_model_id(parameter_rows)
    model_ids: set[str] = set()
    for row in readiness_rows:
        model_id = row.get("model_id", "")
        if not model_id:
            continue
        visibility = parameters.get(model_id, {}).get("pdf_visibility", "")
        if visibility not in DISPLAY_MODEL_VISIBILITIES:
            continue
        presentation_allowed = row.get("presentation_allowed", "").strip().lower() in {"true", "1", "yes", "y"}
        pdf_integrated = row.get("pdf_integration_status", "") == "pdf_integrated_daily_adapter"
        if presentation_allowed or pdf_integrated:
            model_ids.add(model_id)
    return model_ids


def display_roster_model_ids(
    registry_rows: Iterable[dict[str, str]],
    parameter_rows: Iterable[dict[str, str]],
    readiness_rows: Iterable[dict[str, str]],
) -> set[str]:
    parameters = rows_by_model_id(parameter_rows)
    readiness = rows_by_model_id(readiness_rows)
    model_ids: set[str] = set()
    for row in registry_rows:
        model_id = row.get("model_id", "")
        if not model_id:
            continue
        active_text = row.get("model_registry_active", "true").strip().lower()
        if active_text not in {"true", "1", "yes", "y"}:
            continue
        applicability = row.get("report_line_applicability", "both")
        if applicability not in {"both", "mainstream", "non_mainstream"}:
            continue
        parameter = parameters.get(model_id, {})
        readiness_row = readiness.get(model_id, {})
        visibility = parameter.get("pdf_visibility") or row.get("pdf_visibility", "")
        presentation_allowed = (
            readiness_row.get("presentation_allowed", "").strip().lower() in {"true", "1", "yes", "y"}
        )
        if visibility in DISPLAY_MODEL_VISIBILITIES or presentation_allowed:
            model_ids.add(model_id)
    return model_ids


def validate_required_display_model_coverage(
    available_model_ids: Iterable[str],
    model_rows: Iterable[dict[str, str]],
    registry_rows: Iterable[dict[str, str]],
    parameter_rows: Iterable[dict[str, str]],
    readiness_rows: Iterable[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    available = set(available_model_ids)
    contract_required = approved_pdf_contract_model_ids(model_rows)
    readiness_required = readiness_pdf_display_model_ids(parameter_rows, readiness_rows)
    roster_required = display_roster_model_ids(registry_rows, parameter_rows, readiness_rows)
    registry_required = contract_required | readiness_required
    for model_id in sorted(registry_required - roster_required):
        errors.append(f"Daily PDF display registry missing required model_id: {model_id}")
    required = contract_required | readiness_required | roster_required
    if not required:
        errors.append("Daily PDF has no contract-approved display model roster")
        return errors
    for model_id in sorted(required - available):
        errors.append(f"Daily PDF display roster missing required model_id: {model_id}")
    return errors


def function_string_literals(path: Path, function_name: str) -> set[str]:
    if not path.exists():
        return set()
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig", errors="replace"), filename=str(path))
    except SyntaxError:
        return set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name:
            return {
                child.value
                for child in ast.walk(node)
                if isinstance(child, ast.Constant) and isinstance(child.value, str)
            }
    return set()


def validate_operation_row_metric_renderer_contract(path: Path = RENDERER) -> list[str]:
    errors: list[str] = []
    function_name = "operation_row_performance_label"
    literals = function_string_literals(path, function_name)
    if not literals:
        return [f"daily PDF renderer missing {function_name}: {rel(path)}"]

    required = {
        "row_metric_status",
        "row_metric_label_zh",
        "row_metric_sample_size",
        "row_metric_win_rate_zh",
        "row_metric_neutral_rate_zh",
        "row_metric_failure_rate_zh",
        "row_metric_avg_return_zh",
        "unavailable_no_approved_add_score_metric",
        "ready",
    }
    forbidden = {
        "win_rate_zh",
        "neutral_rate_zh",
        "failure_rate_zh",
        "avg_return_zh",
        "technical_package",
        "pdf_bonus_combo",
        "pdf_combo",
        "row_level_combo",
        "add_score_combo",
    }
    missing = sorted(required - literals)
    if missing:
        errors.append(
            "daily PDF operation row metric renderer must consume the model-owned row_metric contract: missing "
            + ";".join(missing)
        )
    legacy = sorted(forbidden & literals)
    if legacy:
        errors.append(
            "daily PDF operation row metric renderer must not fall back to baseline or legacy metric prefixes: "
            + ";".join(legacy)
        )
    return errors


def validate_renderer_fixed_model_table_contract(source_paths: Iterable[Path] = (RENDERER,)) -> list[str]:
    errors: list[str] = []
    skip_re = re.compile(r"if\s+not\s+(?:ranked_rows|line_rows)\s*:\s*\n\s*continue")
    confirmed_limit_re = re.compile(r"['\"]confirmed_operation['\"]\s*:\s*(\d+)")
    active_limit_re = re.compile(r"['\"]active_operation['\"]\s*:\s*(\d+)")
    active_none_re = re.compile(r"['\"]active_operation['\"]\s*:\s*None")
    for path in source_paths:
        if not path.exists():
            errors.append(f"missing daily PDF renderer path: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if MODEL_EMPTY_STATE_TEXT not in text:
            errors.append(f"daily PDF renderer missing zero-candidate text: {MODEL_EMPTY_STATE_TEXT}")
        for forbidden in FORBIDDEN_RENDERER_MODEL_STATUS_SUMMARY_TOKENS:
            if forbidden in text:
                errors.append(
                    "daily PDF renderer must not render technical model/PDF integration status summary tables: "
                    f"{forbidden} in {rel(path)}"
                )
        for forbidden in FORBIDDEN_OPERATION_HIGHLIGHT_EMPTY_STATE_TOKENS:
            if forbidden in text:
                errors.append(
                    "daily PDF operation-oriented highlight tables must keep empty states inside the two main tables: "
                    f"forbidden {forbidden} in {rel(path)}"
                )
        for required in REQUIRED_RENDERER_MODEL_ORDER_TOKENS:
            if required not in text:
                errors.append(
                    "daily PDF renderer must keep W-bottom model sections immediately after volume attack: "
                    f"missing {required} in {rel(path)}"
                )
        for required in REQUIRED_OPERATION_HIGHLIGHT_CONTRACT_TOKENS:
            if required not in text:
                errors.append(
                    "daily PDF renderer must keep operation-oriented model highlight tables as confirmed-buy then active only: "
                    f"missing {required} in {rel(path)}"
                )
        for required in REQUIRED_OPERATION_HIGHLIGHT_DISPLAY_LIMIT_TOKENS:
            if required not in text:
                errors.append(
                    "daily PDF renderer must keep highlight operation display limits as confirmed-all and active-max-10: "
                    f"missing {required} in {rel(path)}"
                )
        for forbidden in FORBIDDEN_OPERATION_HIGHLIGHT_DISPLAY_LIMIT_TOKENS:
            if forbidden in text:
                errors.append(
                    "daily PDF renderer must not keep legacy operation highlight row caps: "
                    f"forbidden {forbidden} in {rel(path)}"
                )
        for match in confirmed_limit_re.finditer(text):
            errors.append(
                "daily PDF renderer must not cap highlight confirmed_operation rows: "
                f"{match.group(0)} in {rel(path)}"
            )
        for match in active_limit_re.finditer(text):
            limit = int(match.group(1))
            if limit != 10:
                errors.append(
                    "daily PDF renderer must cap highlight active_operation rows at exactly 10: "
                    f"{match.group(0)} in {rel(path)}"
                )
        for match in active_none_re.finditer(text):
            errors.append(
                "daily PDF renderer must not leave highlight active_operation rows uncapped: "
                f"{match.group(0)} in {rel(path)}"
            )
        for required in REQUIRED_STOCK_MODEL_HEADER_LAYOUT_TOKENS:
            if required not in text:
                errors.append(
                    "daily PDF stock model header layout must keep blue model titles, split summary paragraphs, "
                    f"and red numeric markup: missing {required} in {rel(path)}"
                )
        for forbidden in FORBIDDEN_STOCK_MODEL_HEADER_LAYOUT_TOKENS:
            if forbidden in text:
                errors.append(
                    "daily PDF stock model header layout must not collapse model titles/descriptions back to "
                    f"generic single-paragraph rendering: forbidden {forbidden} in {rel(path)}"
                )
        for required in REQUIRED_OPERATION_SECTION_PAGEBREAK_TOKENS:
            if required not in text:
                errors.append(
                    "daily PDF operation section labels must reserve table-start room through the shared "
                    f"section-label-with-table helper: missing {required} in {rel(path)}"
                )
        for forbidden in FORBIDDEN_OPERATION_SECTION_PAGEBREAK_TOKENS:
            if forbidden in text:
                errors.append(
                    "daily PDF operation section labels must not be appended separately from their tables: "
                    f"forbidden {forbidden} in {rel(path)}"
                )
        if skip_re.search(text):
            errors.append(
                "daily PDF renderer must not skip a model section when a model has zero candidate rows: "
                f"{rel(path)}"
            )
    return errors


def split_tokens(value: str) -> set[str]:
    return {part.strip() for part in re.split(r"[|,;]", str(value or "")) if part.strip()}


def renderer_text_for_operation_contract(source_paths: Iterable[Path]) -> tuple[str, list[str]]:
    chunks: list[str] = []
    errors: list[str] = []
    for path in source_paths:
        if not path.exists():
            errors.append(f"missing daily PDF renderer path for operation adapter contract: {rel(path)}")
            continue
        chunks.append(path.read_text(encoding="utf-8-sig", errors="replace"))
    return "\n".join(chunks), errors


def validate_pdf_integrated_operation_adapter_contract(
    readiness_rows: Iterable[dict[str, str]],
    *,
    source_paths: Iterable[Path] = (RENDERER,),
    artifact_paths: dict[str, Path] | None = None,
    renderer_tokens: dict[str, tuple[str, ...]] | None = None,
    required_columns_by_model: dict[str, set[str]] | None = None,
    allowed_sections_by_model: dict[str, set[str]] | None = None,
    required_model_ids: set[str] | None = None,
    require_renderer_contract: bool = True,
) -> list[str]:
    errors: list[str] = []
    artifacts = artifact_paths if artifact_paths is not None else PDF_OPERATION_ADAPTER_ARTIFACTS
    tokens_by_model = renderer_tokens if renderer_tokens is not None else PDF_OPERATION_RENDERER_TOKENS
    required_columns = (
        required_columns_by_model if required_columns_by_model is not None else PDF_OPERATION_REQUIRED_COLUMNS_BY_MODEL
    )
    allowed_sections = (
        allowed_sections_by_model if allowed_sections_by_model is not None else PDF_OPERATION_ALLOWED_SECTIONS_BY_MODEL
    )
    renderer_text = ""
    if require_renderer_contract:
        renderer_text, renderer_errors = renderer_text_for_operation_contract(source_paths)
        errors.extend(renderer_errors)

    readiness_by_model = rows_by_model_id(readiness_rows)
    target_model_ids = {
        row.get("model_id", "")
        for row in readiness_rows
        if row.get("model_id", "") and row.get("pdf_integration_status", "") == "pdf_integrated_daily_adapter"
    }
    target_model_ids.update(required_model_ids or set())
    integrated_rows: list[dict[str, str]] = []
    for model_id in sorted(target_model_ids):
        ready = readiness_by_model.get(model_id, {})
        if not ready:
            errors.append(f"PDF operation adapter readiness row missing for {model_id}")
            continue
        integrated_rows.append(ready)
    for ready in integrated_rows:
        model_id = ready.get("model_id", "")
        if ready.get("pdf_integration_status", "") != "pdf_integrated_daily_adapter":
            errors.append(
                f"PDF operation adapter must be pdf_integrated_daily_adapter before renderer use: {model_id}"
            )
        path = artifacts.get(model_id)
        if path is None:
            errors.append(
                "PDF-integrated operation model missing dedicated adapter contract artifact mapping: "
                f"{model_id}"
            )
            continue
        if require_renderer_contract:
            missing_tokens = [token for token in tokens_by_model.get(model_id, ()) if token not in renderer_text]
            if model_id not in tokens_by_model:
                errors.append(
                    "PDF-integrated operation model missing renderer-consumption token contract: "
                    f"{model_id}"
                )
            elif missing_tokens:
                errors.append(
                    "PDF-integrated operation model is not consumed from its dedicated adapter by renderer: "
                    f"{model_id} missing " + ";".join(missing_tokens)
                )
        readiness_sections = split_tokens(ready.get("daily_adapter_sections", ""))
        missing_readiness_sections = sorted(PDF_OPERATION_REQUIRED_SECTIONS - readiness_sections)
        if missing_readiness_sections:
            errors.append(
                f"PDF operation adapter readiness missing required sections for {model_id}: "
                + ";".join(missing_readiness_sections)
            )
        header = set(csv_header(path))
        if not header:
            errors.append(f"missing PDF operation adapter artifact: {rel(path)}")
            continue
        missing_columns = sorted(required_columns.get(model_id, set()) - header)
        if missing_columns:
            errors.append(
                f"PDF operation adapter artifact missing required columns for {model_id}: "
                + ";".join(missing_columns)
            )
        rows = load_csv_rows(path)
        if not rows:
            errors.append(f"PDF operation adapter artifact has no rows: {rel(path)}")
            continue
        allowed_artifact_models = allowed_model_ids_for_operation_artifact(model_id, path)
        present_models = {row.get("model_id", "") for row in rows if row.get("model_id", "")}
        unexpected_models = sorted(present_models - allowed_artifact_models)
        if unexpected_models:
            errors.append(
                f"PDF operation adapter artifact mixes model_ids for {model_id}: "
                + ";".join(unexpected_models)
            )
        model_rows = [row for row in rows if row.get("model_id", "") == model_id]
        if not model_rows:
            errors.append(
                f"PDF operation adapter artifact has no rows for required model_id {model_id}: "
                f"{rel(path)}"
            )
            continue
        metric_sections = {"confirmed_operation", "confirmed_unranked_operation", "active_operation"}
        for row_index, row in enumerate(model_rows, start=2):
            if row.get("row_type", "") != "data" or row.get("pdf_section", "") not in metric_sections:
                continue
            status = row.get("row_metric_status", "")
            if status not in {"ready", "unavailable_no_approved_add_score_metric"}:
                errors.append(
                    f"PDF operation adapter row {row_index} has invalid row_metric_status for {model_id}: "
                    f"{status or 'blank'}"
                )
                continue
            if status == "ready":
                required_payload = {
                    "row_metric_label_zh",
                    "row_metric_sample_size",
                    "row_metric_win_rate_zh",
                    "row_metric_neutral_rate_zh",
                    "row_metric_failure_rate_zh",
                    "row_metric_avg_return_zh",
                }
                missing_payload = sorted(column for column in required_payload if not row.get(column, ""))
                if missing_payload:
                    errors.append(
                        f"PDF operation adapter ready row {row_index} has incomplete row_metric payload for "
                        f"{model_id}: " + ";".join(missing_payload)
                    )
        sections = {row.get("pdf_section", "") for row in model_rows if row.get("pdf_section", "")}
        extra_sections = sorted(sections - allowed_sections.get(model_id, PDF_OPERATION_REQUIRED_SECTIONS))
        if extra_sections:
            errors.append(
                f"PDF operation adapter exposes PDF-forbidden sections for {model_id}: "
                + ";".join(extra_sections)
            )
        missing_sections = sorted(PDF_OPERATION_REQUIRED_SECTIONS - sections)
        if missing_sections:
            errors.append(
                f"PDF operation adapter missing required sections for {model_id}: "
                + ";".join(missing_sections)
            )
        views = {row.get("pdf_view", "") for row in model_rows if row.get("pdf_view", "")}
        missing_views = sorted(PDF_OPERATION_REQUIRED_VIEWS - views)
        if missing_views:
            errors.append(
                f"PDF operation adapter missing required pdf_view rows for {model_id}: "
                + ";".join(missing_views)
            )
        for view in sorted(PDF_OPERATION_REQUIRED_VIEWS):
            for section in sorted(PDF_OPERATION_REQUIRED_SECTIONS):
                if not any(row.get("pdf_view", "") == view and row.get("pdf_section", "") == section for row in rows):
                    errors.append(
                        f"PDF operation adapter missing {view}/{section} row for {model_id}: {rel(path)}"
                    )
    return errors


def validate_w_bottom_operation_adapter_contract(readiness_rows: Iterable[dict[str, str]]) -> list[str]:
    return validate_pdf_integrated_operation_adapter_contract(
        readiness_rows,
        artifact_paths=dict(W_BOTTOM_OPERATION_ARTIFACTS),
        required_columns_by_model={
            model_id: W_BOTTOM_OPERATION_REQUIRED_COLUMNS for model_id in W_BOTTOM_OPERATION_ARTIFACTS
        },
        allowed_sections_by_model={
            model_id: W_BOTTOM_OPERATION_REQUIRED_SECTIONS for model_id in W_BOTTOM_OPERATION_ARTIFACTS
        },
        required_model_ids=set(W_BOTTOM_OPERATION_ARTIFACTS),
    )


def event_rows_by_field(event_rows: Iterable[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in event_rows:
        field_name = row.get("field_name", "")
        if field_name:
            grouped.setdefault(field_name, []).append(row)
    return grouped


def matching_event_rows(usage: EventFieldUsage, event_rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    rows = [row for row in event_rows if row.get("field_name", "") == usage.field_name]
    exact = [row for row in rows if row.get("source_file", "").replace("\\", "/") == usage.path]
    return exact or rows


def discover_event_field_usages(
    event_rows: Iterable[dict[str, str]],
    source_paths: Iterable[Path] = DAILY_PDF_SOURCE_PATHS,
    output_paths: Iterable[Path] = DAILY_EVENT_OUTPUTS,
) -> list[EventFieldUsage]:
    field_names = sorted(
        {row.get("field_name", "") for row in event_rows if row.get("field_name", "")},
        key=len,
        reverse=True,
    )
    usages: list[EventFieldUsage] = []

    for path in source_paths:
        if not path.exists():
            continue
        try:
            lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
        except OSError:
            continue
        for line_no, line in enumerate(lines, start=1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            lowered = line.lower()
            for field_name in field_names:
                if re.search(WORD_RE_TEMPLATE.format(re.escape(field_name.lower())), lowered):
                    for context in source_contexts(line, field_name):
                        usages.append(EventFieldUsage(field_name, rel(path), context, line_no, line.strip()))

    for path in output_paths:
        if path.suffix.lower() != ".csv":
            continue
        for column in csv_header(path):
            if column in field_names:
                usages.append(EventFieldUsage(column, rel(path), "csv_header"))

    return sorted(set(usages), key=lambda item: (item.path, item.field_name, item.context, item.line_no or 0))


def validate_required_contracts() -> list[str]:
    errors: list[str] = []
    if not STOCK_MODEL_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(STOCK_MODEL_CONTRACT)}")
    if not EVENT_CATALYST_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(EVENT_CATALYST_CONTRACT)}")
    return errors


def validate_model_ids(used_model_ids: Iterable[str], model_rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_model = {row.get("model_id", ""): row for row in model_rows if row.get("model_id", "")}
    for model_id in sorted(set(used_model_ids)):
        row = by_model.get(model_id)
        if row is None:
            errors.append(f"Daily PDF uses model_id not in stock model contract: {model_id}")
            continue
        if not bool_value(row, "approved_for_daily_pdf"):
            errors.append(f"Daily PDF uses model_id not approved_for_daily_pdf=true: {model_id}")
    return errors


def validate_event_field_usages(usages: Iterable[EventFieldUsage], event_rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    rows_by_field = event_rows_by_field(event_rows)
    for usage in usages:
        if usage.field_name not in rows_by_field:
            errors.append(f"Daily PDF uses event/catalyst field missing from contract: {usage.field_name}")
            continue
        rows = matching_event_rows(usage, event_rows)
        if not any(bool_value(row, "approved_for_daily_pdf") for row in rows):
            errors.append(
                f"Daily PDF uses event/catalyst field not approved_for_daily_pdf=true: "
                f"{usage.field_name} at {usage.path}"
            )
        if not any("daily_pdf" in split_semicolon(row.get("allowed_consumers", "")) for row in rows):
            errors.append(f"Daily PDF field lacks daily_pdf consumer approval: {usage.field_name} at {usage.path}")
        if usage.context == "score":
            if not any(bool_value(row, "score_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    f"Daily PDF uses disclosure-only or score_allowed=false event/catalyst field in score context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "ranking":
            if not any(bool_value(row, "ranking_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    f"Daily PDF uses disclosure-only or ranking_allowed=false event/catalyst field in ranking context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "reason":
            if not any(bool_value(row, "reason_text_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    f"Daily PDF uses disclosure-only or reason_text_allowed=false event/catalyst field in reason text context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
            if any("no_reason" in row.get("degraded_behavior", "").lower() for row in rows):
                errors.append(
                    f"Daily PDF may strengthen a degraded event/catalyst source in reason text: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
    return errors


def validate_private_pdf_rules(source_paths: Iterable[Path] = DAILY_PDF_SOURCE_PATHS) -> list[str]:
    errors: list[str] = []
    for path in source_paths:
        if not path.exists():
            errors.append(f"missing daily PDF source path: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for pattern, message in PRIVATE_PDF_RULE_PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f"{message}: {rel(path)} matches {pattern}")
    return errors


def string_list_assignment(path: Path, assignment_name: str) -> set[str]:
    if not path.exists():
        return set()
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig", errors="replace"), filename=str(path))
    except SyntaxError:
        return set()

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == assignment_name for target in node.targets):
            continue
        if not isinstance(node.value, (ast.List, ast.Tuple)):
            return set()
        values: set[str] = set()
        for item in node.value.elts:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                values.add(item.value)
        return values
    return set()


def validate_research_recommendations_not_direct_pdf_inputs() -> list[str]:
    errors: list[str] = []
    for path in (RENDERER, ENTRYPOINT):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if "daily_model_parameter_recommendations_latest.csv" in text:
            errors.append(f"daily PDF source directly reads research recommendations: {rel(path)}")
        if "daily_model_parameter_research_latest.csv" in text:
            errors.append(f"daily PDF source directly reads research parameter research: {rel(path)}")

    if MODEL_LAYER.exists():
        text = MODEL_LAYER.read_text(encoding="utf-8-sig", errors="replace")
        if "MODEL_PARAMETER_RECOMMENDATIONS" in text:
            recommendation_columns = string_list_assignment(MODEL_LAYER, "RECOMMENDATION_COLUMNS")
            forbidden = sorted(recommendation_columns & FORBIDDEN_RESEARCH_RECOMMENDATION_COLUMNS)
            if forbidden:
                errors.append(
                    "model layer allows research recommendations to overwrite production baseline fields: "
                    + ";".join(forbidden)
                )
        if "MODEL_PARAMETER_RECOMMENDATIONS" in text and "RECOMMENDATION_COLUMNS" not in text:
            errors.append(
                "model layer reads research recommendations without an advisory column allowlist: "
                f"{rel(MODEL_LAYER)}"
            )
        if "research_only_not_pdf_core" not in text:
            errors.append(
                "model layer must preserve research-only visibility instead of writing research recommendations "
                f"directly into production PDF core: {rel(MODEL_LAYER)}"
            )
    return errors


def validate(phase: str = VALIDATION_PHASE_FULL) -> tuple[
    list[str],
    set[str],
    set[str],
    list[EventFieldUsage],
    list[dict[str, str]],
    list[dict[str, str]],
]:
    if phase not in VALIDATION_PHASES:
        raise ValueError(f"unsupported daily PDF consumer validation phase: {phase}")

    errors: list[str] = []
    if not STOCK_MODEL_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(STOCK_MODEL_CONTRACT)}")
    if phase == VALIDATION_PHASE_FULL and not EVENT_CATALYST_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(EVENT_CATALYST_CONTRACT)}")
    if errors:
        return errors, set(), set(), [], [], []

    model_rows = load_csv_rows(STOCK_MODEL_CONTRACT)
    event_rows = load_csv_rows(EVENT_CATALYST_CONTRACT) if phase == VALIDATION_PHASE_FULL else []
    registry_rows = load_csv_rows(DAILY_MODEL_REGISTRY)
    parameter_rows = load_csv_rows(DAILY_MODEL_PARAMETERS)
    readiness_rows = load_csv_rows(DAILY_MODEL_READINESS)
    reported_model_ids = model_ids_from_report_outputs()
    signal_model_ids = model_ids_from_report_outputs((DAILY_MODEL_SIGNALS,))
    dormant_registry_ids = dormant_registry_only_model_ids(
        reported_model_ids,
        signal_model_ids,
        registry_rows,
        model_rows,
        readiness_rows,
    )
    used_model_ids = reported_model_ids - dormant_registry_ids
    effective_registry_rows = [
        row
        for row in registry_rows
        if row.get("model_id", "") not in dormant_registry_ids
    ]
    required_display_model_ids = (
        approved_pdf_contract_model_ids(model_rows)
        | display_roster_model_ids(
            effective_registry_rows,
            parameter_rows,
            readiness_rows,
        )
    )
    event_usages = discover_event_field_usages(event_rows) if phase == VALIDATION_PHASE_FULL else []

    errors.extend(validate_model_ids(used_model_ids, model_rows))
    errors.extend(
        validate_required_display_model_coverage(
            used_model_ids,
            model_rows,
            effective_registry_rows,
            parameter_rows,
            readiness_rows,
        )
    )
    if phase == VALIDATION_PHASE_FULL:
        errors.extend(validate_event_field_usages(event_usages, event_rows))
        errors.extend(validate_private_pdf_rules())
        errors.extend(validate_renderer_fixed_model_table_contract())
        errors.extend(validate_operation_row_metric_renderer_contract())
    errors.extend(
        validate_pdf_integrated_operation_adapter_contract(
            readiness_rows,
            required_model_ids=set(W_BOTTOM_OPERATION_ARTIFACTS),
            require_renderer_contract=phase == VALIDATION_PHASE_FULL,
        )
    )
    if phase == VALIDATION_PHASE_FULL:
        errors.extend(validate_research_recommendations_not_direct_pdf_inputs())
    return errors, used_model_ids, required_display_model_ids, event_usages, model_rows, event_rows


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate daily PDF contract consumers.")
    parser.add_argument(
        "--phase",
        choices=VALIDATION_PHASES,
        default=VALIDATION_PHASE_FULL,
        help="runtime checks current model approvals, display roster, and data adapter consistency only",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors, used_model_ids, required_display_model_ids, event_usages, model_rows, event_rows = validate(args.phase)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    approved_daily_models = sorted(row["model_id"] for row in model_rows if bool_value(row, "approved_for_daily_pdf"))

    print("daily PDF contract consumer validation passed")
    print(f"validation_phase={args.phase}")
    print(f"stock_model_contract={rel(STOCK_MODEL_CONTRACT)}")
    print("daily_contract_approved_model_ids=" + ";".join(approved_daily_models))
    print(
        "daily_required_display_model_ids="
        + (";".join(sorted(required_display_model_ids)) if required_display_model_ids else "none")
    )
    print("daily_used_model_ids=" + (";".join(sorted(used_model_ids)) if used_model_ids else "none"))
    if args.phase == VALIDATION_PHASE_FULL:
        approved_event_rows = [row for row in event_rows if bool_value(row, "approved_for_daily_pdf")]
        used_event_fields = sorted({usage.field_name for usage in event_usages})
        output_state = "present" if CHATGPT_OUTPUT_ROOT.exists() else "not_present"
        print(f"event_catalyst_contract={rel(EVENT_CATALYST_CONTRACT)}")
        print(f"daily_event_contract_approved_rows={len(approved_event_rows)}")
        print("daily_used_event_fields=" + (";".join(used_event_fields) if used_event_fields else "none"))
        print(f"chatgpt_side_outputs_official={output_state}")
        print("blocked_contract_fields=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
