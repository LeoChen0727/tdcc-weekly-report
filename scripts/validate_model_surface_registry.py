from __future__ import annotations

import ast
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_CSV = ROOT / "config" / "model_surface_registry.csv"
STOCK_MODEL_CONTRACT = ROOT / "config" / "stock_model_contract_registry.csv"
EVENT_CATALYST_CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"

REQUIRED_COLUMNS = [
    "surface_id",
    "surface_name",
    "surface_type",
    "selection_level",
    "owning_lane",
    "supporting_lanes",
    "formal_contract_file",
    "primary_source_file",
    "implementation_sources",
    "consumer_surfaces",
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
    "stock_entry_signal",
    "research_parity_status",
    "promotion_required",
    "effective_from",
    "deprecated_after",
    "change_reason",
    "notes",
]

BOOLEAN_COLUMNS = [
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
    "stock_entry_signal",
    "promotion_required",
]

STOCK_CONTRACT_APPROVAL_COLUMNS = [
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
    "promotion_required",
]

ALLOWED_SURFACE_TYPES = {
    "stock_entry_model",
    "tdcc_stock_entry_model",
    "tdcc_specialty_stock_model",
    "tdcc_weekly_ranking_model",
    "theme_fund_rotation_model",
    "event_catalyst_overlay_surface",
}

ALLOWED_SELECTION_LEVELS = {
    "individual_stock",
    "tdcc_weekly_report",
    "theme_group",
    "candidate_overlay",
}

ALLOWED_CONTRACT_SENTINELS = {
    "pending_review",
    "pending_tdcc_ranking_contract",
    "pending_theme_model_contract",
    "not_applicable",
}

ALLOWED_PARITY_STATUSES = {
    "ok",
    "warning_research_variant_only",
    "research_backtest_advisory_only",
    "pending_backtest_optimization",
    "disclosure_only_not_ranked",
    "pending_review",
}

BOOL_VALUES = {"true", "false"}
SURFACE_ID_RE = re.compile(r"^[a-z0-9_]+$")
MODEL_ID_CONSTANT_RE = re.compile(r"(^MODEL_ID$|_MODEL_ID$)")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
STOCK_SURFACE_TYPES = {"stock_entry_model", "tdcc_stock_entry_model", "tdcc_specialty_stock_model"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_csv_rows(path: Path) -> tuple[list[dict[str, str]], list[str], list[str]]:
    if not path.exists():
        return [], [], [f"missing CSV: {rel(path)}"]
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = [{key: str(value or "").strip() for key, value in row.items()} for row in reader]
        return rows, list(reader.fieldnames or []), []


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def validate_schema(fieldnames: list[str]) -> list[str]:
    if fieldnames != REQUIRED_COLUMNS:
        return ["model surface registry header must match required columns exactly: " + ",".join(REQUIRED_COLUMNS)]
    return []


def validate_path_list(surface_id: str, column: str, value: str) -> list[str]:
    errors: list[str] = []
    for item in split_semicolon(value):
        if item in ALLOWED_CONTRACT_SENTINELS:
            continue
        item_path = Path(item)
        if item_path.is_absolute():
            errors.append(f"{surface_id} {column} must be repo-relative: {item}")
            continue
        if ".." in item_path.parts:
            errors.append(f"{surface_id} {column} must not traverse outside repo: {item}")
            continue
        if not (ROOT / item).exists():
            errors.append(f"{surface_id} {column} path does not exist: {item}")
    return errors


def validate_rows(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if not rows:
        return ["model surface registry is empty"]

    seen: set[str] = set()
    for line_no, row in enumerate(rows, start=2):
        surface_id = row.get("surface_id", "")
        if not surface_id:
            errors.append(f"row {line_no} has empty surface_id")
            continue
        if not SURFACE_ID_RE.match(surface_id):
            errors.append(f"{surface_id} must use lowercase snake_case surface_id")
        if surface_id in seen:
            errors.append(f"duplicate surface_id: {surface_id}")
        seen.add(surface_id)

        for column in REQUIRED_COLUMNS:
            if not row.get(column, ""):
                errors.append(f"{surface_id} has empty required field: {column}")

        surface_type = row.get("surface_type", "")
        if surface_type not in ALLOWED_SURFACE_TYPES:
            errors.append(f"{surface_id} has invalid surface_type: {surface_type}")

        selection_level = row.get("selection_level", "")
        if selection_level not in ALLOWED_SELECTION_LEVELS:
            errors.append(f"{surface_id} has invalid selection_level: {selection_level}")

        for column in BOOLEAN_COLUMNS:
            value = row.get(column, "")
            if value not in BOOL_VALUES:
                errors.append(f"{surface_id} {column} must be true/false, got {value!r}")

        parity_status = row.get("research_parity_status", "")
        if parity_status not in ALLOWED_PARITY_STATUSES:
            errors.append(f"{surface_id} has invalid research_parity_status: {parity_status}")

        effective_from = row.get("effective_from", "")
        if effective_from and effective_from != "pending_review" and not DATE_RE.match(effective_from):
            errors.append(f"{surface_id} effective_from must be YYYY-MM-DD or pending_review")

        deprecated_after = row.get("deprecated_after", "")
        if deprecated_after and deprecated_after not in {"none", "pending_review"} and not DATE_RE.match(deprecated_after):
            errors.append(f"{surface_id} deprecated_after must be YYYY-MM-DD, none, or pending_review")

        errors.extend(validate_path_list(surface_id, "formal_contract_file", row.get("formal_contract_file", "")))
        errors.extend(validate_path_list(surface_id, "primary_source_file", row.get("primary_source_file", "")))
        errors.extend(validate_path_list(surface_id, "implementation_sources", row.get("implementation_sources", "")))

        if surface_type in STOCK_SURFACE_TYPES and row.get("stock_entry_signal") != "true":
            errors.append(f"{surface_id} stock model surface must have stock_entry_signal=true")
        if surface_type not in STOCK_SURFACE_TYPES and row.get("stock_entry_signal") != "false":
            errors.append(f"{surface_id} non-stock model surface must have stock_entry_signal=false")

    return errors


def collect_declared_script_model_ids() -> tuple[dict[str, set[str]], list[str]]:
    ids_by_path: dict[str, set[str]] = {}
    errors: list[str] = []
    for path in sorted((ROOT / "scripts").glob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig"))
        except SyntaxError as exc:
            errors.append(f"could not parse script for model ids: {rel(path)}:{exc.lineno}: {exc.msg}")
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            if not isinstance(node.value, ast.Constant) or not isinstance(node.value.value, str):
                continue
            model_id = str(node.value.value).strip()
            if not model_id:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name) and MODEL_ID_CONSTANT_RE.search(target.id):
                    ids_by_path.setdefault(rel(path), set()).add(model_id)

    return ids_by_path, errors


def validate_declared_script_model_ids(surface_rows: list[dict[str, str]]) -> list[str]:
    ids_by_path, errors = collect_declared_script_model_ids()
    surface_ids = {row.get("surface_id", "") for row in surface_rows}
    for path, model_ids in sorted(ids_by_path.items()):
        for model_id in sorted(model_ids):
            if model_id not in surface_ids:
                errors.append(f"script-declared model_id missing from model surface registry: {model_id} ({path})")
    return errors


def validate_stock_contract_alignment(surface_rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    stock_rows, stock_fields, stock_errors = load_csv_rows(STOCK_MODEL_CONTRACT)
    errors.extend(stock_errors)
    if errors:
        return errors

    missing_stock_cols = sorted({"model_id", *STOCK_CONTRACT_APPROVAL_COLUMNS} - set(stock_fields))
    if missing_stock_cols:
        return [f"stock model contract missing columns: {missing_stock_cols}"]

    surfaces = {row.get("surface_id", ""): row for row in surface_rows}
    stock_model_ids = {row["model_id"] for row in stock_rows if row.get("model_id")}
    for stock in stock_rows:
        model_id = stock.get("model_id", "")
        surface = surfaces.get(model_id)
        if surface is None:
            errors.append(f"model surface registry missing stock contract model_id: {model_id}")
            continue
        if surface.get("formal_contract_file") != rel(STOCK_MODEL_CONTRACT):
            errors.append(f"{model_id} must reference {rel(STOCK_MODEL_CONTRACT)}")
        if surface.get("surface_type") not in STOCK_SURFACE_TYPES:
            errors.append(f"{model_id} stock contract row has non-stock surface_type={surface.get('surface_type')!r}")
        for column in STOCK_CONTRACT_APPROVAL_COLUMNS:
            if surface.get(column) != stock.get(column):
                errors.append(
                    f"{model_id} surface {column}={surface.get(column)!r} "
                    f"does not match stock contract {stock.get(column)!r}"
                )

    for surface in surface_rows:
        surface_id = surface.get("surface_id", "")
        if surface.get("formal_contract_file") == rel(STOCK_MODEL_CONTRACT) and surface_id not in stock_model_ids:
            errors.append(f"{surface_id} references stock model contract but is not in that contract")

    group = surfaces.get("group_fund_rotation")
    if group is None:
        errors.append("model surface registry must include group_fund_rotation")
    else:
        if group.get("surface_type") != "theme_fund_rotation_model":
            errors.append("group_fund_rotation must be classified as theme_fund_rotation_model")
        if group.get("formal_contract_file") == rel(STOCK_MODEL_CONTRACT):
            errors.append("group_fund_rotation must not reference stock_model_contract_registry.csv")
        if group.get("stock_entry_signal") != "false":
            errors.append("group_fund_rotation must not be a stock entry signal")

    tdcc_ranking = surfaces.get("tdcc_weekly_ranking_formula")
    if tdcc_ranking is None:
        errors.append("model surface registry must include tdcc_weekly_ranking_formula")
    else:
        if tdcc_ranking.get("surface_type") != "tdcc_weekly_ranking_model":
            errors.append("tdcc_weekly_ranking_formula must be classified as tdcc_weekly_ranking_model")
        if tdcc_ranking.get("selection_level") != "tdcc_weekly_report":
            errors.append("tdcc_weekly_ranking_formula must use selection_level=tdcc_weekly_report")
        if tdcc_ranking.get("formal_contract_file") == rel(STOCK_MODEL_CONTRACT):
            errors.append("tdcc_weekly_ranking_formula must not reference stock_model_contract_registry.csv")
        if tdcc_ranking.get("stock_entry_signal") != "false":
            errors.append("tdcc_weekly_ranking_formula must not be a stock entry signal")
        if tdcc_ranking.get("approved_for_tdcc_weekly_pdf") != "true":
            errors.append("tdcc_weekly_ranking_formula must be approved for TDCC weekly PDF use")
        if tdcc_ranking.get("approved_for_daily_pdf") != "false":
            errors.append("tdcc_weekly_ranking_formula must not be approved for daily PDF use")
        if "scripts/build_tdcc_weekly_ranking_backtest.py" not in split_semicolon(
            tdcc_ranking.get("implementation_sources", "")
        ):
            errors.append("tdcc_weekly_ranking_formula must list the research/backtest implementation source")

    event = surfaces.get("event_catalyst_overlay")
    if event is None:
        errors.append("model surface registry must include event_catalyst_overlay")
    else:
        if event.get("formal_contract_file") != rel(EVENT_CATALYST_CONTRACT):
            errors.append(f"event_catalyst_overlay must reference {rel(EVENT_CATALYST_CONTRACT)}")
        if event.get("stock_entry_signal") != "false":
            errors.append("event_catalyst_overlay must not be a stock entry signal")

    return errors


def validate() -> list[str]:
    rows, fieldnames, errors = load_csv_rows(REGISTRY_CSV)
    errors.extend(validate_schema(fieldnames))
    if errors:
        return errors
    errors.extend(validate_rows(rows))
    errors.extend(validate_declared_script_model_ids(rows))
    errors.extend(validate_stock_contract_alignment(rows))
    return errors


def main() -> int:
    rows, _, _ = load_csv_rows(REGISTRY_CSV)
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    tdcc_surfaces = sorted(
        row["surface_id"]
        for row in rows
        if row.get("approved_for_tdcc_weekly_pdf") == "true"
    )
    tdcc_stock_model_surfaces = sorted(
        row["surface_id"]
        for row in rows
        if row.get("approved_for_tdcc_weekly_pdf") == "true"
        and row.get("formal_contract_file") == rel(STOCK_MODEL_CONTRACT)
    )
    non_stock_surfaces = sorted(
        row["surface_id"]
        for row in rows
        if row.get("stock_entry_signal") == "false"
    )
    print("model surface registry validation passed")
    print(f"registry={rel(REGISTRY_CSV)}")
    print(f"validated_surfaces={len(rows)}")
    print(f"tdcc_weekly_pdf_surfaces={tdcc_surfaces}")
    print(f"tdcc_weekly_stock_model_surfaces={tdcc_stock_model_surfaces}")
    print(f"non_stock_surfaces={non_stock_surfaces}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
