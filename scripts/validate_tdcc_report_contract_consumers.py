from __future__ import annotations

import ast
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
STOCK_MODEL_CONTRACT = ROOT / "config" / "stock_model_contract_registry.csv"
EVENT_CATALYST_CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"

TDCC_SOURCE_GLOBS = (
    "scripts/build_tdcc_weekly_*.py",
    "scripts/build_tdcc_signal_*.py",
    "scripts/validate_tdcc_*.py",
)

TDCC_REPORT_MODEL_CSVS = (
    ROOT / "output/latest/tdcc_weekly_model_cross_summary_latest.csv",
    ROOT / "output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv",
    ROOT / "output/latest/tdcc_weekly_candidate_full_for_report_latest.csv",
)

TDCC_EVENT_OUTPUT_GLOBS = (
    "output/latest/tdcc_*.csv",
    "output/latest/tdcc_*.md",
)

TDCC_PUBLISHED_REPORT_DIRS = (
    ROOT / "docs/latest/published_reports/tdcc_weekly",
    ROOT / "output/latest/published_reports/tdcc_weekly",
)

MODEL_ALLOWLIST_NAME_RE = re.compile(r"ALLOWED.*MODEL|MODEL.*ALLOWED")
WORD_RE_TEMPLATE = r"(?<![A-Za-z0-9_]){}(?![A-Za-z0-9_])"
SCORE_CONTEXT_RE = re.compile(
    r"\b(score|scores|scoring|weighted|bonus|penalty|formula|calculation|calculate|calc|component)\b"
)
SCORE_NAME_RE = re.compile(r"\b[A-Za-z0-9_]*_score\b")
RANKING_CONTEXT_RE = re.compile(r"\b(rank|ranking|sort_values|sort_index|order|ascending|descending)\b")
RANKING_NAME_RE = re.compile(r"\b(rank_[A-Za-z0-9_]*|[A-Za-z0-9_]*_rank)\b")
REASON_CONTEXT_RE = re.compile(
    r"\b(reason|why_selected|recommended_usage|report_usage|operation_note|next_confirmation|risk_tags|note)\b"
)
GENERIC_EVENT_FIELD_NAMES = {"summary", "notes", "importance"}


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


def bool_value(row: dict[str, str], column: str) -> bool:
    return row.get(column, "").strip().lower() == "true"


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def csv_header(path: Path) -> list[str]:
    if not path.exists() or path.stat().st_size <= 0:
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        try:
            return [str(column or "").strip() for column in next(reader)]
        except StopIteration:
            return []


def tdcc_source_paths(root: Path = ROOT) -> list[Path]:
    paths: set[Path] = set()
    for pattern in TDCC_SOURCE_GLOBS:
        paths.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(paths)


def tdcc_event_output_paths(root: Path = ROOT) -> list[Path]:
    paths: set[Path] = set()
    for pattern in TDCC_EVENT_OUTPUT_GLOBS:
        paths.update(path for path in root.glob(pattern) if path.is_file())
    for directory in TDCC_PUBLISHED_REPORT_DIRS:
        if directory.exists():
            paths.update(path for path in directory.glob("*") if path.is_file())
    return sorted(paths)


def string_constants(node: ast.AST) -> set[str]:
    constants: set[str] = set()
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        constants.add(node.value)
        return constants
    for child in ast.iter_child_nodes(node):
        constants.update(string_constants(child))
    return constants


def assignment_target_names(node: ast.Assign | ast.AnnAssign) -> list[str]:
    targets: list[ast.AST]
    if isinstance(node, ast.Assign):
        targets = list(node.targets)
    else:
        targets = [node.target]
    names: list[str] = []
    for target in targets:
        if isinstance(target, ast.Name):
            names.append(target.id)
        elif isinstance(target, ast.Tuple):
            names.extend(item.id for item in target.elts if isinstance(item, ast.Name))
    return names


def model_ids_from_source_allowlists(paths: Iterable[Path]) -> set[str]:
    model_ids: set[str] = set()
    for path in paths:
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig", errors="replace"), filename=str(path))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            names = assignment_target_names(node)
            if not any(MODEL_ALLOWLIST_NAME_RE.search(name) for name in names):
                continue
            model_ids.update(string_constants(node.value))
    return model_ids


def model_ids_from_report_outputs(paths: Iterable[Path] = TDCC_REPORT_MODEL_CSVS) -> set[str]:
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


def discover_event_field_usages(
    event_rows: Iterable[dict[str, str]],
    source_paths: Iterable[Path] | None = None,
    output_paths: Iterable[Path] | None = None,
) -> list[EventFieldUsage]:
    field_names = sorted(
        {row.get("field_name", "") for row in event_rows if row.get("field_name", "")},
        key=len,
        reverse=True,
    )
    usages: list[EventFieldUsage] = []

    for path in source_paths if source_paths is not None else tdcc_source_paths():
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

    for path in output_paths if output_paths is not None else tdcc_event_output_paths():
        if path.suffix.lower() == ".csv":
            for column in csv_header(path):
                if column in field_names:
                    usages.append(EventFieldUsage(column, rel(path), "csv_header"))
            continue
        if path.suffix.lower() == ".md":
            try:
                text = path.read_text(encoding="utf-8-sig", errors="replace")
            except OSError:
                continue
            lowered = text.lower()
            for field_name in field_names:
                if field_name in GENERIC_EVENT_FIELD_NAMES:
                    continue
                if re.search(WORD_RE_TEMPLATE.format(re.escape(field_name.lower())), lowered):
                    usages.append(EventFieldUsage(field_name, rel(path), "markdown_text"))
            continue
        lowered_name = path.name.lower()
        for field_name in field_names:
            if field_name in GENERIC_EVENT_FIELD_NAMES:
                continue
            if field_name.lower() in lowered_name:
                usages.append(EventFieldUsage(field_name, rel(path), "published_path"))

    return sorted(set(usages), key=lambda item: (item.path, item.field_name, item.context, item.line_no or 0))


def validate_model_ids(used_model_ids: Iterable[str], model_rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_model = {row.get("model_id", ""): row for row in model_rows if row.get("model_id", "")}
    for model_id in sorted(set(used_model_ids)):
        row = by_model.get(model_id)
        if row is None:
            errors.append(f"TDCC weekly report uses model_id not in stock model contract: {model_id}")
            continue
        if not bool_value(row, "approved_for_tdcc_weekly_pdf"):
            errors.append(f"TDCC weekly report uses model_id not approved for TDCC weekly PDF: {model_id}")
    return errors


def event_rows_by_field(event_rows: Iterable[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in event_rows:
        field_name = row.get("field_name", "")
        if field_name:
            grouped.setdefault(field_name, []).append(row)
    return grouped


def validate_event_field_usages(usages: Iterable[EventFieldUsage], event_rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_field = event_rows_by_field(event_rows)
    for usage in usages:
        rows = by_field.get(usage.field_name, [])
        if not rows:
            errors.append(f"TDCC weekly report uses event/catalyst field missing from contract: {usage.field_name}")
            continue
        if any(not bool_value(row, "approved_for_tdcc_weekly_pdf") for row in rows):
            errors.append(
                f"TDCC weekly report uses event/catalyst field not approved_for_tdcc_weekly_pdf=true: "
                f"{usage.field_name} at {usage.path}"
            )
        if any("tdcc_weekly_pdf" not in split_semicolon(row.get("allowed_consumers", "")) for row in rows):
            errors.append(f"TDCC weekly report field lacks tdcc_weekly_pdf consumer approval: {usage.field_name}")
        if usage.context == "score":
            if any(bool_value(row, "disclosure_only") or not bool_value(row, "score_allowed") for row in rows):
                errors.append(
                    f"TDCC weekly report uses disclosure-only or score_allowed=false field in score context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "ranking":
            if any(bool_value(row, "disclosure_only") or not bool_value(row, "ranking_allowed") for row in rows):
                errors.append(
                    f"TDCC weekly report uses disclosure-only or ranking_allowed=false field in ranking context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
        if usage.context == "reason":
            if any(bool_value(row, "disclosure_only") or not bool_value(row, "reason_text_allowed") for row in rows):
                errors.append(
                    f"TDCC weekly report uses disclosure-only or reason_text_allowed=false field in reason text context: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
            if any("no_reason" in row.get("degraded_behavior", "").lower() for row in rows):
                errors.append(
                    f"TDCC weekly report may strengthen a degraded event/catalyst source in reason text: "
                    f"{usage.field_name} at {usage.path}:{usage.line_no or '-'}"
                )
    return errors


def validate_required_contracts() -> list[str]:
    errors: list[str] = []
    if not STOCK_MODEL_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(STOCK_MODEL_CONTRACT)}")
    if not EVENT_CATALYST_CONTRACT.exists():
        errors.append(f"missing required contract: {rel(EVENT_CATALYST_CONTRACT)}")
    return errors


def validate() -> tuple[list[str], set[str], list[EventFieldUsage], list[dict[str, str]], list[dict[str, str]]]:
    errors = validate_required_contracts()
    if errors:
        return errors, set(), [], [], []

    model_rows = load_csv_rows(STOCK_MODEL_CONTRACT)
    event_rows = load_csv_rows(EVENT_CATALYST_CONTRACT)
    source_paths = tdcc_source_paths()
    used_model_ids = model_ids_from_source_allowlists(source_paths) | model_ids_from_report_outputs()
    event_usages = discover_event_field_usages(event_rows, source_paths=source_paths)

    errors.extend(validate_model_ids(used_model_ids, model_rows))
    errors.extend(validate_event_field_usages(event_usages, event_rows))
    return errors, used_model_ids, event_usages, model_rows, event_rows


def main() -> int:
    errors, used_model_ids, event_usages, model_rows, event_rows = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    approved_event_rows = [row for row in event_rows if bool_value(row, "approved_for_tdcc_weekly_pdf")]
    used_event_fields = sorted({usage.field_name for usage in event_usages})
    contract_tdcc_models = sorted(row["model_id"] for row in model_rows if bool_value(row, "approved_for_tdcc_weekly_pdf"))
    print("tdcc report contract consumer validation passed")
    print(f"stock_model_contract={rel(STOCK_MODEL_CONTRACT)}")
    print(f"event_catalyst_contract={rel(EVENT_CATALYST_CONTRACT)}")
    print("tdcc_contract_approved_model_ids=" + ";".join(contract_tdcc_models))
    print("tdcc_used_model_ids=" + (";".join(sorted(used_model_ids)) if used_model_ids else "none"))
    print(f"tdcc_event_contract_approved_rows={len(approved_event_rows)}")
    print("tdcc_used_event_fields=" + (";".join(used_event_fields) if used_event_fields else "none"))
    print("blocked_contract_fields=none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
