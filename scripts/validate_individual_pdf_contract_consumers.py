from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
STOCK_MODEL_CONTRACT = ROOT / "config" / "stock_model_contract_registry.csv"
EVENT_CATALYST_CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"

INDIVIDUAL_SOURCE_PATHS = (
    ROOT / "scripts" / "generate_individual_stock_report.py",
    ROOT / "scripts" / "build_individual_stock_chatgpt_packets.py",
    ROOT / "scripts" / "build_individual_stock_raw_data_index.py",
    ROOT / "scripts" / "validate_individual_stock_outputs.py",
)

INDIVIDUAL_OUTPUT_DIRS = (
    ROOT / "output/latest/individual_stock_reports",
    ROOT / "docs/latest/individual_stock_reports",
)

WORD_RE_TEMPLATE = r"(?<![A-Za-z0-9_]){}(?![A-Za-z0-9_])"
SCORE_CONTEXT_RE = re.compile(
    r"\b(score|scores|scoring|weighted|bonus|penalty|formula|calculation|calculate|calc|component)\b"
)
SCORE_NAME_RE = re.compile(r"\b[A-Za-z0-9_]*_score\b")
RANKING_CONTEXT_RE = re.compile(r"\b(rank|ranking|sort_values|sort_index|order|ascending|descending)\b")
RANKING_NAME_RE = re.compile(r"\b(rank_[A-Za-z0-9_]*|[A-Za-z0-9_]*_rank)\b")
REASON_CONTEXT_RE = re.compile(
    r"\b("
    r"reason|why_selected|recommend|recommended|recommendation|buy|sell|judgment|judgement|"
    r"action_summary|entry_strategy|final_decision|score_interpretation|thesis|operation"
    r")\b"
)

GENERIC_EVENT_FIELD_NAMES = {"summary", "notes", "importance", "source_url"}

PRIVATE_PDF_RULE_PATTERNS = {
    r"\bpdf_side_(?:score|scoring|rank|ranking|buy|sell|judgment|judgement|reason|recommendation?)\b": (
        "Individual PDF source must not define private PDF-side scoring/ranking/judgment rules"
    ),
    r"\bindividual_pdf_(?:score|scoring|rank|ranking|buy|sell|judgment|judgement)_rule\b": (
        "Individual PDF source must not define independent PDF-side action rules"
    ),
    r"\bchatgpt_side_outputs_official\b": (
        "Individual PDF source must not consume daily stock recommendation official PDF outputs"
    ),
    r"\btdcc_weekly_candidate_(?:highlight|full).*\.pdf\b": (
        "Individual PDF source must not consume or overwrite TDCC weekly report PDF outputs"
    ),
    r"\bresearch_backtest\b": "Individual PDF source must not consume research/backtest lane outputs directly",
    r"\bdaily_model_parameter_recommendations_latest\.csv\b": (
        "Individual PDF source must not consume research recommendation outputs directly"
    ),
    r"\bdaily_model_parameter_research_latest\.csv\b": (
        "Individual PDF source must not consume research parameter outputs directly"
    ),
}


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


def individual_output_csv_paths(root: Path = ROOT) -> list[Path]:
    paths: set[Path] = set()
    for directory in INDIVIDUAL_OUTPUT_DIRS:
        if directory.exists():
            paths.update(path for path in directory.glob("*.csv") if path.is_file())
    return sorted(paths)


def model_ids_from_individual_outputs(paths: Iterable[Path] | None = None) -> set[str]:
    model_ids: set[str] = set()
    for path in paths if paths is not None else individual_output_csv_paths():
        if path.suffix.lower() != ".csv":
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
    source_paths: Iterable[Path] = INDIVIDUAL_SOURCE_PATHS,
    output_paths: Iterable[Path] | None = None,
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
                if field_name in GENERIC_EVENT_FIELD_NAMES:
                    continue
                if re.search(WORD_RE_TEMPLATE.format(re.escape(field_name.lower())), lowered):
                    for context in source_contexts(line, field_name):
                        usages.append(EventFieldUsage(field_name, rel(path), context, line_no, line.strip()))

    for path in output_paths if output_paths is not None else individual_output_csv_paths():
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
            errors.append(f"Individual PDF uses model_id not in stock model contract: {model_id}")
            continue
        if not bool_value(row, "approved_for_individual_pdf"):
            errors.append(f"Individual PDF uses model_id not approved_for_individual_pdf=true: {model_id}")
    return errors


def validate_event_field_usages(usages: Iterable[EventFieldUsage], event_rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    rows_by_field = event_rows_by_field(event_rows)
    for usage in usages:
        if usage.field_name not in rows_by_field:
            errors.append(f"Individual PDF uses event/catalyst field missing from contract: {usage.field_name}")
            continue
        rows = matching_event_rows(usage, event_rows)
        if not any(bool_value(row, "approved_for_individual_pdf") for row in rows):
            errors.append(
                "Individual PDF uses event/catalyst field not approved_for_individual_pdf=true: "
                f"{usage.field_name} at {usage.path}"
            )
        if not any("individual_pdf" in split_semicolon(row.get("allowed_consumers", "")) for row in rows):
            errors.append(f"Individual PDF field lacks individual_pdf consumer approval: {usage.field_name}")
        if usage.context == "score":
            if not any(bool_value(row, "score_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    "Individual PDF uses disclosure-only or score_allowed=false event/catalyst field in score context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "ranking":
            if not any(bool_value(row, "ranking_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    "Individual PDF uses disclosure-only or ranking_allowed=false event/catalyst field in ranking context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "reason":
            if not any(bool_value(row, "reason_text_allowed") and not bool_value(row, "disclosure_only") for row in rows):
                errors.append(
                    "Individual PDF uses disclosure-only or reason_text_allowed=false event/catalyst field in reason text context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
            if any("no_reason" in row.get("degraded_behavior", "").lower() for row in rows):
                errors.append(
                    "Individual PDF may strengthen a degraded event/catalyst source in reason text: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
    return errors


def validate_private_pdf_rules(source_paths: Iterable[Path] = INDIVIDUAL_SOURCE_PATHS) -> list[str]:
    errors: list[str] = []
    for path in source_paths:
        if not path.exists():
            errors.append(f"missing individual PDF source path: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for pattern, message in PRIVATE_PDF_RULE_PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f"{message}: {rel(path)} matches {pattern}")
    return errors


def validate_action_display_boundary() -> list[str]:
    errors: list[str] = []
    packet_builder = ROOT / "scripts" / "build_individual_stock_chatgpt_packets.py"
    renderer = ROOT / "scripts" / "generate_individual_stock_report.py"
    if not packet_builder.exists():
        return [f"missing individual stock packet builder: {rel(packet_builder)}"]
    packet_text = packet_builder.read_text(encoding="utf-8-sig", errors="replace")
    if "## ACTION_DISPLAY" not in packet_text:
        errors.append("Individual PDF packet builder must emit ACTION_DISPLAY for PDF-visible report language")
    if "## ACTION_DECISION" not in packet_text:
        errors.append("Individual PDF packet builder must keep ACTION_DECISION as internal context")
    if renderer.exists():
        renderer_text = renderer.read_text(encoding="utf-8-sig", errors="replace")
        required_display_fields = [
            "action_rating_display_zh",
            "action_summary_zh",
            "entry_strategy_zh",
            "position_sizing_zh",
            "risk_control_zh",
            "final_decision_zh",
        ]
        for field_name in required_display_fields:
            if field_name not in renderer_text:
                errors.append(f"Individual PDF renderer does not consume ACTION_DISPLAY field: {field_name}")
    return errors


def validate() -> tuple[list[str], set[str], list[EventFieldUsage], list[dict[str, str]], list[dict[str, str]]]:
    errors = validate_required_contracts()
    if errors:
        return errors, set(), [], [], []

    model_rows = load_csv_rows(STOCK_MODEL_CONTRACT)
    event_rows = load_csv_rows(EVENT_CATALYST_CONTRACT)
    used_model_ids = model_ids_from_individual_outputs()
    event_usages = discover_event_field_usages(event_rows)

    errors.extend(validate_model_ids(used_model_ids, model_rows))
    errors.extend(validate_event_field_usages(event_usages, event_rows))
    errors.extend(validate_private_pdf_rules())
    errors.extend(validate_action_display_boundary())
    return errors, used_model_ids, event_usages, model_rows, event_rows


def main() -> int:
    errors, used_model_ids, event_usages, model_rows, event_rows = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    approved_individual_models = sorted(
        row["model_id"] for row in model_rows if bool_value(row, "approved_for_individual_pdf")
    )
    approved_event_rows = [row for row in event_rows if bool_value(row, "approved_for_individual_pdf")]
    used_event_fields = sorted({usage.field_name for usage in event_usages})

    print("individual PDF contract consumer validation passed")
    print(f"stock_model_contract={rel(STOCK_MODEL_CONTRACT)}")
    print(f"event_catalyst_contract={rel(EVENT_CATALYST_CONTRACT)}")
    print("individual_contract_approved_model_ids=" + (";".join(approved_individual_models) or "none"))
    print("individual_used_model_ids=" + (";".join(sorted(used_model_ids)) if used_model_ids else "none"))
    print(f"individual_event_contract_approved_rows={len(approved_event_rows)}")
    print("individual_used_event_fields=" + (";".join(used_event_fields) if used_event_fields else "none"))
    print("blocked_contract_fields=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
