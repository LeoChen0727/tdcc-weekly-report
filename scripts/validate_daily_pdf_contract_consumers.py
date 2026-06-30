from __future__ import annotations

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
MODEL_EMPTY_STATE_TEXT = "本日無股票推薦"


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


def approved_pdf_contract_model_ids(model_rows: Iterable[dict[str, str]]) -> set[str]:
    return {
        row.get("model_id", "")
        for row in model_rows
        if row.get("model_id", "")
        and bool_value(row, "approved_for_daily_pdf")
        and row.get("pdf_visibility", "") in DISPLAY_MODEL_VISIBILITIES
    }


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
    roster_required = display_roster_model_ids(registry_rows, parameter_rows, readiness_rows)
    required = contract_required | roster_required
    if not required:
        errors.append("Daily PDF has no contract-approved display model roster")
        return errors
    for model_id in sorted(required - available):
        errors.append(f"Daily PDF display roster missing required model_id: {model_id}")
    return errors


def validate_renderer_fixed_model_table_contract(source_paths: Iterable[Path] = (RENDERER,)) -> list[str]:
    errors: list[str] = []
    skip_re = re.compile(r"if\s+not\s+(?:ranked_rows|line_rows)\s*:\s*\n\s*continue")
    for path in source_paths:
        if not path.exists():
            errors.append(f"missing daily PDF renderer path: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if MODEL_EMPTY_STATE_TEXT not in text:
            errors.append(f"daily PDF renderer missing zero-candidate text: {MODEL_EMPTY_STATE_TEXT}")
        if skip_re.search(text):
            errors.append(
                "daily PDF renderer must not skip a model section when a model has zero candidate rows: "
                f"{rel(path)}"
            )
    return errors


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


def validate() -> tuple[
    list[str],
    set[str],
    set[str],
    list[EventFieldUsage],
    list[dict[str, str]],
    list[dict[str, str]],
]:
    errors = validate_required_contracts()
    if errors:
        return errors, set(), set(), [], [], []

    model_rows = load_csv_rows(STOCK_MODEL_CONTRACT)
    event_rows = load_csv_rows(EVENT_CATALYST_CONTRACT)
    registry_rows = load_csv_rows(DAILY_MODEL_REGISTRY)
    parameter_rows = load_csv_rows(DAILY_MODEL_PARAMETERS)
    readiness_rows = load_csv_rows(DAILY_MODEL_READINESS)
    used_model_ids = model_ids_from_report_outputs()
    required_display_model_ids = (
        approved_pdf_contract_model_ids(model_rows)
        | display_roster_model_ids(registry_rows, parameter_rows, readiness_rows)
    )
    event_usages = discover_event_field_usages(event_rows)

    errors.extend(validate_model_ids(used_model_ids, model_rows))
    errors.extend(
        validate_required_display_model_coverage(
            used_model_ids,
            model_rows,
            registry_rows,
            parameter_rows,
            readiness_rows,
        )
    )
    errors.extend(validate_event_field_usages(event_usages, event_rows))
    errors.extend(validate_private_pdf_rules())
    errors.extend(validate_renderer_fixed_model_table_contract())
    errors.extend(validate_research_recommendations_not_direct_pdf_inputs())
    return errors, used_model_ids, required_display_model_ids, event_usages, model_rows, event_rows


def main() -> int:
    errors, used_model_ids, required_display_model_ids, event_usages, model_rows, event_rows = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    approved_daily_models = sorted(row["model_id"] for row in model_rows if bool_value(row, "approved_for_daily_pdf"))
    approved_event_rows = [row for row in event_rows if bool_value(row, "approved_for_daily_pdf")]
    used_event_fields = sorted({usage.field_name for usage in event_usages})
    output_state = "present" if CHATGPT_OUTPUT_ROOT.exists() else "not_present"

    print("daily PDF contract consumer validation passed")
    print(f"stock_model_contract={rel(STOCK_MODEL_CONTRACT)}")
    print(f"event_catalyst_contract={rel(EVENT_CATALYST_CONTRACT)}")
    print("daily_contract_approved_model_ids=" + ";".join(approved_daily_models))
    print(
        "daily_required_display_model_ids="
        + (";".join(sorted(required_display_model_ids)) if required_display_model_ids else "none")
    )
    print("daily_used_model_ids=" + (";".join(sorted(used_model_ids)) if used_model_ids else "none"))
    print(f"daily_event_contract_approved_rows={len(approved_event_rows)}")
    print("daily_used_event_fields=" + (";".join(used_event_fields) if used_event_fields else "none"))
    print(f"chatgpt_side_outputs_official={output_state}")
    print("blocked_contract_fields=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
