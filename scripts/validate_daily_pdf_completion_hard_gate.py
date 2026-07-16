from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import validate_chatgpt_daily_report_new_conversation_replay as replay  # noqa: E402
from scripts import validate_daily_pdf_contract_consumers as pdf_consumers  # noqa: E402
DAILY_FULL_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
DAILY_MODEL_PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
DAILY_PDF_REPLAY_PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_pdf_replay_pr_validation.yml"
COMPLETION_GATE = ROOT / "scripts" / "validate_daily_pdf_completion_hard_gate.py"
REPLAY_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_daily_report_new_conversation_replay.py"
RENDERED_MODEL_REGRESSION_CONTRACT = ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv"
DAILY_MODEL_READINESS = ROOT / "output" / "latest" / "model_operation_readiness_latest.csv"
DAILY_MODEL_SIGNALS = ROOT / "output" / "latest" / "daily_candidate_model_signals_for_report_latest.csv"
STOCK_THEME_TAXONOMY = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"

STATIC_COMPLETION_GATE_COMMAND = "python scripts/validate_daily_pdf_completion_hard_gate.py"
DAILY_FULL_OUTPUT_GATE_COMMAND = (
    "python scripts/validate_daily_pdf_completion_hard_gate.py "
    "--require-output-dir chatgpt_side_outputs_new_conversation_replay"
)
PR_OUTPUT_GATE_COMMAND = (
    "python scripts/validate_daily_pdf_completion_hard_gate.py "
    "--require-output-dir chatgpt_side_outputs_pr_validation"
)
REPLAY_COMMAND = "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py"

REQUIRED_STATIC_VALIDATORS = (
    "python scripts/validate_chatgpt_side_pdf_contract.py",
    "python scripts/validate_daily_pdf_shared_path_isolation.py",
    "python scripts/validate_daily_pdf_contract_consumers.py",
    "python scripts/validate_daily_pdf_role_manifest_contract.py",
    "python scripts/validate_pdf_production_inventory.py",
)
REQUIRED_PR_VALIDATORS = (
    "python scripts/validate_repo_production_inventory.py",
    "python scripts/validate_daily_pdf_contract_consumers.py",
    "python scripts/validate_daily_pdf_role_manifest_contract.py",
    "python scripts/validate_daily_pdf_shared_path_isolation.py",
    "python scripts/validate_daily_production_boundaries.py",
    "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
)
REQUIRED_REGRESSION_MODEL_IDS = set(pdf_consumers.PDF_OPERATION_ADAPTER_ARTIFACTS)
HIGHLIGHT_ROLE_REPORT_LINES = {
    "mainstream_highlight": "mainstream",
    "non_mainstream_highlight": "non_mainstream",
}
OPERATION_MODEL_DISPLAY_NAMES = {
    "volume_range_breakout_v2_low_position_volume_attack": "低位放量攻擊模型",
    "volume_range_breakout_v2_mid_position_momentum_attack": "中位動能放量攻擊模型",
    "volume_range_breakout_v2_high_position_volume_attack": "高位階放量攻擊模型",
    "w_bottom_right_side": "W底右側模型",
    "neckline_volume_breakout_confirmation": "W底頸線帶量突破確認模型",
    "price_pullback_23ema": "23EMA回檔模型",
}
OPERATION_SECTION_TITLES = {
    "confirmed_operation": "本日可買 / 已確認買入候選",
    "active_operation": "操作中",
}
OPERATION_SECTION_EMPTY_TEXT = {
    "confirmed_operation": "本日無股票推薦",
    "active_operation": "目前無操作中追蹤列",
}
HIGHLIGHT_OPERATION_SECTIONS = ("confirmed_operation", "active_operation")
OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS = ("買入：", "賣出：", "停損：", "基礎模型績效：", "勝：", "和：", "敗：")
RENDERED_STOCK_ID_SAMPLE_SIZE = 3


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def normalized_repo_artifact(path: Path | str) -> str:
    text = str(path).replace("\\", "/").strip()
    if not text:
        return ""
    path_obj = Path(text)
    if path_obj.is_absolute():
        return rel(path_obj).replace("\\", "/")
    return text.lstrip("./")


PDF_OPERATION_ADAPTER_SOURCE_ARTIFACTS = {
    model_id: normalized_repo_artifact(path)
    for model_id, path in pdf_consumers.PDF_OPERATION_ADAPTER_ARTIFACTS.items()
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8-sig", errors="replace")


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def boolish(value: str) -> bool:
    return str(value or "").strip().lower() in {"true", "1", "yes", "y"}


def compact_text(value: object) -> str:
    return replay.compact_contract_text(value)


def split_tokens(value: object) -> set[str]:
    return {
        token.strip()
        for token in str(value or "").replace(";", "|").replace(",", "|").split("|")
        if token.strip()
    }


def load_stock_report_line_memberships() -> dict[str, set[str]]:
    by_stock: dict[str, set[str]] = {}
    source_paths = (DAILY_MODEL_SIGNALS, STOCK_THEME_TAXONOMY)
    for path in source_paths:
        for row in load_csv_rows(path):
            stock_id = stock_id_from_operation_row(row)
            if not stock_id:
                continue
            lines = by_stock.setdefault(stock_id, set())
            for col in ("report_line", "report_bucket"):
                value = str(row.get(col, "") or "").strip()
                if value in {"mainstream", "non_mainstream"}:
                    lines.add(value)
            for col in ("report_line_memberships", "taxonomy_report_line_memberships"):
                for token in split_tokens(row.get(col, "")):
                    if token in {"mainstream", "non_mainstream"}:
                        lines.add(token)
            truth_cols = (
                ("mainstream_report_eligible", "mainstream"),
                ("taxonomy_mainstream_report_eligible", "mainstream"),
                ("non_mainstream_report_eligible", "non_mainstream"),
                ("taxonomy_non_mainstream_report_eligible", "non_mainstream"),
            )
            for col, line in truth_cols:
                if boolish(row.get(col, "")):
                    lines.add(line)
    return by_stock


def row_matches_report_line(
    row: dict[str, str],
    report_line: str,
    stock_report_lines: dict[str, set[str]] | None = None,
) -> bool:
    raw_report_line = str(row.get("report_line", "") or "").strip()
    memberships = split_tokens(row.get("report_line_memberships", ""))
    if raw_report_line in {report_line, "both"}:
        return True
    if raw_report_line:
        return report_line in memberships or "both" in memberships
    if memberships:
        return report_line in memberships or "both" in memberships
    stock_id = stock_id_from_operation_row(row)
    if stock_id and stock_report_lines is not None and stock_id in stock_report_lines:
        return report_line in stock_report_lines[stock_id]
    return True


def stock_id_from_operation_row(row: dict[str, str]) -> str:
    stock_id = str(row.get("stock_id", "") or "").strip()
    if stock_id:
        return stock_id.removesuffix(".0")
    stock_display = str(row.get("stock_display", "") or "").strip()
    if not stock_display:
        return ""
    return stock_display.split()[0].removesuffix(".0")


def model_display_name(model_id: str, rows: Iterable[dict[str, str]]) -> str:
    for row in rows:
        text = str(row.get("model_name_zh", "") or "").strip()
        if text:
            return text
    return OPERATION_MODEL_DISPLAY_NAMES.get(model_id, model_id)


def operation_table_title(model_name: str, section: str) -> str:
    return f"{model_name} - {OPERATION_SECTION_TITLES[section]}"


def operation_rows_for_rendered_section(
    rows: Iterable[dict[str, str]],
    section: str,
    report_line: str,
    stock_report_lines: dict[str, set[str]] | None = None,
) -> list[dict[str, str]]:
    matched: list[dict[str, str]] = []
    for row in rows:
        if str(row.get("pdf_view", "") or "").strip() != "highlight":
            continue
        if str(row.get("pdf_section", "") or "").strip() != section:
            continue
        if str(row.get("row_type", "") or "").strip() != "data":
            continue
        if not row_matches_report_line(row, report_line, stock_report_lines):
            continue
        if section == "confirmed_operation":
            if str(row.get("row_action_status", "") or "").strip() != "confirmed_buy_candidate":
                continue
            if not boolish(row.get("buy_rank_eligible", "")):
                continue
        elif section == "active_operation":
            if str(row.get("operation_status", "") or "").strip() != "active_operation":
                continue
            if boolish(row.get("buy_rank_eligible", "")):
                continue
        matched.append(row)

    def sort_key(row: dict[str, str]) -> tuple[float, str]:
        try:
            display_order = float(str(row.get("display_order", "") or "").strip())
        except ValueError:
            display_order = 999999.0
        return display_order, stock_id_from_operation_row(row)

    return sorted(matched, key=sort_key)


def operation_empty_state_rows(
    rows: Iterable[dict[str, str]],
    section: str,
    report_line: str,
    stock_report_lines: dict[str, set[str]] | None = None,
) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if str(row.get("pdf_view", "") or "").strip() == "highlight"
        and str(row.get("pdf_section", "") or "").strip() == section
        and str(row.get("row_type", "") or "").strip() == "empty_state"
        and row_matches_report_line(row, report_line, stock_report_lines)
    ]


def validate_operation_adapter_pdf_text(
    role_to_compact_text: dict[str, str],
    adapter_rows_by_model: dict[str, list[dict[str, str]]],
    required_model_ids: Iterable[str] | None = None,
    stock_report_lines: dict[str, set[str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    model_ids = sorted(required_model_ids or adapter_rows_by_model)
    for model_id in model_ids:
        rows = adapter_rows_by_model.get(model_id, [])
        if not rows:
            errors.append(f"PDF operation adapter has no rows for model_id={model_id}")
            continue
        model_name = model_display_name(model_id, rows)
        for role, report_line in HIGHLIGHT_ROLE_REPORT_LINES.items():
            compact_pdf_text = role_to_compact_text.get(role, "")
            if not compact_pdf_text:
                errors.append(f"{role}: missing compact PDF text for operation adapter validation")
                continue
            if compact_text(model_name) not in compact_pdf_text:
                errors.append(f"{role}: missing operation model title for {model_id}: {model_name}")
            for token in OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS:
                if compact_text(token) not in compact_pdf_text:
                    errors.append(f"{role}: missing operation model summary token for {model_id}: {token}")
            for section in HIGHLIGHT_OPERATION_SECTIONS:
                title = operation_table_title(model_name, section)
                compact_title = compact_text(title)
                if compact_title not in compact_pdf_text:
                    errors.append(f"{role}: missing operation table title for {model_id}/{section}: {title}")

                data_rows = operation_rows_for_rendered_section(rows, section, report_line, stock_report_lines)
                if data_rows:
                    stock_ids = [
                        stock_id_from_operation_row(row)
                        for row in data_rows[:RENDERED_STOCK_ID_SAMPLE_SIZE]
                    ]
                    for stock_id in [stock_id for stock_id in stock_ids if stock_id]:
                        if stock_id not in compact_pdf_text:
                            errors.append(f"{role}: missing rendered stock_id={stock_id} for {model_id}/{section}")
                    continue

                empty_text = OPERATION_SECTION_EMPTY_TEXT[section]
                if compact_text(empty_text) not in compact_pdf_text:
                    errors.append(f"{role}: missing empty-state text for {model_id}/{section}: {empty_text}")
    return errors


def compact_pdf_text_by_role(role_map: dict[str, Path]) -> tuple[dict[str, str], list[str]]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency is installed in CI.
        return {}, [f"pypdf import failed for operation adapter PDF text validation: {exc}"]

    errors: list[str] = []
    role_to_compact_text: dict[str, str] = {}
    for role, path in role_map.items():
        try:
            reader = PdfReader(str(path))
            role_to_compact_text[role] = compact_text("\n".join(page.extract_text() or "" for page in reader.pages))
        except Exception as exc:
            errors.append(f"{role}: pypdf text extraction failed for operation adapter validation: {path}: {exc}")
    return role_to_compact_text, errors


def validate_operation_adapter_pdf_presence(role_map: dict[str, Path]) -> list[str]:
    role_to_text, errors = compact_pdf_text_by_role(role_map)
    if errors:
        return errors
    adapter_rows_by_model = {
        model_id: load_csv_rows(path)
        for model_id, path in pdf_consumers.PDF_OPERATION_ADAPTER_ARTIFACTS.items()
    }
    return validate_operation_adapter_pdf_text(
        role_to_text,
        adapter_rows_by_model,
        required_model_ids=pdf_consumers.PDF_OPERATION_ADAPTER_ARTIFACTS,
        stock_report_lines=load_stock_report_line_memberships(),
    )


def validate_semantic_manifest_adapter_sources(
    rows: Iterable[dict[str, str]],
    expected_artifacts: dict[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    expected = expected_artifacts or PDF_OPERATION_ADAPTER_SOURCE_ARTIFACTS
    for index, row in enumerate(rows, start=2):
        model_id = str(row.get("model_id", "") or "").strip()
        if not model_id:
            continue
        section = str(row.get("pdf_section", "") or "").strip()
        if not section:
            errors.append(f"semantic manifest row {index} missing pdf_section for {model_id}")
            continue
        expected_source = expected.get(model_id)
        if not expected_source:
            errors.append(
                "semantic manifest row "
                f"{index} uses model_id without a formal PDF operation adapter contract: {model_id}"
            )
            continue
        observed_source = normalized_repo_artifact(row.get("source_artifact", ""))
        if observed_source != expected_source:
            errors.append(
                f"semantic manifest row {index} for {model_id}/{section} must use dedicated adapter "
                f"{expected_source}, observed={observed_source or '<missing>'}"
            )
    return errors


def require_literals(text: str, literals: Iterable[str], context: str) -> list[str]:
    errors: list[str] = []
    for literal in literals:
        if literal not in text:
            errors.append(f"{context} missing required completion hard-gate literal: {literal!r}")
    return errors


def require_ordered(text: str, literals: Iterable[str], context: str) -> list[str]:
    errors: list[str] = []
    cursor = -1
    for literal in literals:
        index = text.find(literal, cursor + 1)
        if index < 0:
            errors.append(f"{context} missing ordered completion hard-gate literal: {literal!r}")
            continue
        if index <= cursor:
            errors.append(f"{context} completion hard-gate order is invalid at literal: {literal!r}")
        cursor = index
    return errors


def validate_workflow_gates() -> list[str]:
    errors: list[str] = []
    for path in (
        DAILY_FULL_WORKFLOW,
        DAILY_MODEL_PR_WORKFLOW,
        DAILY_PDF_REPLAY_PR_WORKFLOW,
        COMPLETION_GATE,
        REPLAY_VALIDATOR,
    ):
        if not path.exists():
            errors.append(f"missing required daily PDF completion hard-gate file: {rel(path)}")

    if DAILY_FULL_WORKFLOW.exists():
        text = read_text(DAILY_FULL_WORKFLOW)
        errors.extend(require_literals(text, REQUIRED_STATIC_VALIDATORS, rel(DAILY_FULL_WORKFLOW)))
        errors.extend(
            require_literals(
                text,
                (
                    STATIC_COMPLETION_GATE_COMMAND,
                    REPLAY_COMMAND,
                    "PDF replay output_dir=chatgpt_side_outputs_new_conversation_replay",
                    "--output-dir chatgpt_side_outputs_new_conversation_replay",
                    DAILY_FULL_OUTPUT_GATE_COMMAND,
                ),
                rel(DAILY_FULL_WORKFLOW),
            )
        )
        errors.extend(
            require_ordered(
                text,
                (
                    "- name: Replay ChatGPT-side daily PDF new conversation",
                    REPLAY_COMMAND,
                    DAILY_FULL_OUTPUT_GATE_COMMAND,
                    "- name: Dispatch and wait for GitHub Pages deploy",
                ),
                rel(DAILY_FULL_WORKFLOW),
            )
        )

    if DAILY_MODEL_PR_WORKFLOW.exists():
        text = read_text(DAILY_MODEL_PR_WORKFLOW)
        errors.extend(require_literals(text, REQUIRED_PR_VALIDATORS, rel(DAILY_MODEL_PR_WORKFLOW)))
        errors.extend(
            require_literals(
                text,
                (
                    STATIC_COMPLETION_GATE_COMMAND,
                    "tests/test_daily_pdf_completion_hard_gate.py",
                ),
                rel(DAILY_MODEL_PR_WORKFLOW),
            )
        )

    if DAILY_PDF_REPLAY_PR_WORKFLOW.exists():
        text = read_text(DAILY_PDF_REPLAY_PR_WORKFLOW)
        errors.extend(
            require_literals(
                text,
                (
                    "python scripts/validate_repo_production_inventory.py",
                    "python scripts/validate_daily_pdf_contract_consumers.py",
                    "python scripts/validate_daily_pdf_shared_path_isolation.py",
                    "python scripts/validate_daily_production_boundaries.py",
                    STATIC_COMPLETION_GATE_COMMAND,
                    REPLAY_COMMAND,
                    "PDF replay output_dir=chatgpt_side_outputs_pr_validation",
                    "--output-dir chatgpt_side_outputs_pr_validation",
                    PR_OUTPUT_GATE_COMMAND,
                    "chatgpt_side_outputs_pr_validation/*.pdf",
                    "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json",
                    "chatgpt_side_outputs_pr_validation/chatgpt_daily_pdf_semantic_manifest.csv",
                    "if-no-files-found: error",
                ),
                rel(DAILY_PDF_REPLAY_PR_WORKFLOW),
            )
        )
        errors.extend(
            require_ordered(
                text,
                (
                    "- name: Replay ChatGPT-side daily PDF new conversation",
                    REPLAY_COMMAND,
                    PR_OUTPUT_GATE_COMMAND,
                    "- name: Upload PR daily PDF replay evidence",
                ),
                rel(DAILY_PDF_REPLAY_PR_WORKFLOW),
            )
        )
    return errors


def validate_regression_contract() -> list[str]:
    errors: list[str] = []
    if not RENDERED_MODEL_REGRESSION_CONTRACT.exists():
        return [f"missing rendered model regression contract: {rel(RENDERED_MODEL_REGRESSION_CONTRACT)}"]
    rows = replay.read_rendered_model_regression_contract(RENDERED_MODEL_REGRESSION_CONTRACT)
    if not rows:
        errors.append(f"rendered model regression contract has no active rows: {rel(RENDERED_MODEL_REGRESSION_CONTRACT)}")
        return errors
    model_ids = {row.get("model_id", "").strip() for row in rows if row.get("model_id", "").strip()}
    missing = sorted(REQUIRED_REGRESSION_MODEL_IDS - model_ids)
    if missing:
        errors.append("rendered model regression contract missing PDF operation model_ids: " + ";".join(missing))
    roles = {row.get("pdf_role", "").strip() for row in rows if row.get("pdf_role", "").strip()}
    for role in ("mainstream_highlight", "non_mainstream_highlight"):
        if role not in roles:
            errors.append(f"rendered model regression contract missing digest role: {role}")
    summary_tokens = {compact_text(token) for token in OPERATION_MODEL_SUMMARY_REQUIRED_TOKENS}
    for model_id in sorted(REQUIRED_REGRESSION_MODEL_IDS):
        for role in ("mainstream_highlight", "non_mainstream_highlight"):
            candidates = [
                row
                for row in rows
                if row.get("model_id", "").strip() == model_id
                and row.get("pdf_role", "").strip() == role
                and row.get("report_date", "").strip() == "*"
            ]
            if not candidates:
                errors.append(f"rendered model regression contract missing wildcard summary row: {model_id}/{role}")
                continue
            required_text = ""
            for row in candidates:
                required_text += "".join(compact_text(token) for token in split_tokens(row.get("required_text_tokens", "")))
            missing_tokens = sorted(token for token in summary_tokens if token not in required_text)
            if missing_tokens:
                errors.append(
                    f"rendered model regression contract missing operation summary tokens for {model_id}/{role}: "
                    + ";".join(missing_tokens)
                )
    return errors


def rows_by_model_id(rows: Iterable[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row.get("model_id", "").strip(): row for row in rows if row.get("model_id", "").strip()}


def validate_readiness_pdf_consistency() -> list[str]:
    errors: list[str] = []
    readiness_rows = load_csv_rows(DAILY_MODEL_READINESS)
    if not readiness_rows:
        return [f"missing or empty model operation readiness artifact: {rel(DAILY_MODEL_READINESS)}"]

    by_model = rows_by_model_id(readiness_rows)
    for model_id in sorted(REQUIRED_REGRESSION_MODEL_IDS):
        row = by_model.get(model_id)
        if row is None:
            errors.append(f"PDF operation model missing readiness row: {model_id}")
            continue
        if row.get("pdf_integration_status", "") != "pdf_integrated_daily_adapter":
            errors.append(
                f"PDF operation model is not marked pdf_integrated_daily_adapter in readiness: {model_id}"
            )
        if not boolish(row.get("presentation_allowed", "")):
            errors.append(f"PDF operation model is not presentation_allowed in readiness: {model_id}")
        if not boolish(row.get("approved_for_daily", "")):
            errors.append(f"PDF operation model is not approved_for_daily in readiness: {model_id}")

    for row in readiness_rows:
        model_id = row.get("model_id", "").strip()
        status = row.get("pdf_integration_status", "").strip()
        presentation_allowed = boolish(row.get("presentation_allowed", ""))
        if presentation_allowed and status != "pdf_integrated_daily_adapter":
            errors.append(
                f"presentation_allowed model must be pdf_integrated_daily_adapter: {model_id}"
            )
        if status == "pdf_integrated_daily_adapter" and not presentation_allowed:
            errors.append(
                f"pdf_integrated_daily_adapter model must be presentation_allowed: {model_id}"
            )

    errors.extend(
        pdf_consumers.validate_pdf_integrated_operation_adapter_contract(
            readiness_rows,
            required_model_ids=set(pdf_consumers.PDF_OPERATION_ADAPTER_ARTIFACTS),
        )
    )
    return errors


def manifest_pdf_paths(output_dir: Path, manifest: dict) -> tuple[list[Path], list[str]]:
    errors: list[str] = []
    outputs = manifest.get("pdf_outputs")
    if not isinstance(outputs, list):
        return [], ["runtime manifest pdf_outputs must be a list of role/path objects"]
    paths: list[Path] = []
    for index, output in enumerate(outputs, start=1):
        if not isinstance(output, dict):
            errors.append(f"runtime manifest pdf_outputs[{index}] must be an object")
            continue
        raw_path = str(output.get("path", "")).strip()
        if not raw_path:
            errors.append(f"runtime manifest pdf_outputs[{index}] missing path")
            continue
        path = Path(raw_path).expanduser()
        if not path.is_absolute():
            path = output_dir / path
        paths.append(path.resolve())
    return paths, errors


def validate_output_dir(output_dir: Path) -> list[str]:
    output_dir = output_dir.expanduser().resolve()
    manifest, errors = replay.read_runtime_manifest(output_dir)
    if errors:
        return errors
    assert manifest is not None

    required_manifest_fields = (
        "manifest_type",
        "source_ref",
        "source_commit_sha",
        "clean_source_commit_sha",
        "main_price_date",
        "freshness_path",
        "readme_path",
        "packet_path",
        "pdf_count",
        "pdf_paths",
        "pdf_outputs",
        "output_dir",
        "semantic_manifest_path",
    )
    for field in required_manifest_fields:
        if field not in manifest or manifest.get(field) in ("", None):
            errors.append(f"runtime manifest missing completion field: {field}")
    if manifest.get("manifest_type") != "chatgpt_daily_report_runtime_manifest":
        errors.append("runtime manifest_type must be chatgpt_daily_report_runtime_manifest")
    if manifest.get("pdf_count") != len(replay.EXPECTED_PDF_ROLES):
        errors.append("runtime manifest pdf_count must match the six official daily PDFs")

    paths, path_errors = manifest_pdf_paths(output_dir, manifest)
    errors.extend(path_errors)
    if paths:
        role_map, role_errors = replay.role_to_pdf_paths_from_manifest(manifest, paths)
        errors.extend(role_errors)
        if sorted(role_map) != sorted(replay.EXPECTED_PDF_ROLES):
            errors.append("runtime manifest role map does not cover every official daily PDF role")
        emitted_pdfs = sorted(path.resolve() for path in output_dir.glob("*.pdf"))
        if sorted(paths) != emitted_pdfs:
            errors.append("daily PDF output directory must contain exactly the manifest-listed six PDFs")
        errors.extend(replay.validate_pdf_files_open(paths))
        if not errors:
            errors.extend(replay.validate_pdf_highlight_layout_contract(paths, output_dir))
            main_price_date = str(manifest.get("main_price_date", "")).strip()
            if main_price_date:
                errors.extend(replay.validate_rendered_model_regression_contract(paths, main_price_date, output_dir))
                errors.extend(replay.validate_semantic_manifest_contract(output_dir, main_price_date))
                semantic_rows, semantic_read_errors = replay.read_semantic_manifest(output_dir, manifest)
                if not semantic_read_errors:
                    errors.extend(validate_semantic_manifest_adapter_sources(semantic_rows))
            errors.extend(validate_operation_adapter_pdf_presence(role_map))
    return errors


def validate(require_output_dirs: Iterable[Path] = ()) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_workflow_gates())
    errors.extend(validate_regression_contract())
    errors.extend(validate_readiness_pdf_consistency())
    for output_dir in require_output_dirs:
        errors.extend(validate_output_dir(output_dir))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate daily PDF completion hard gates.")
    parser.add_argument(
        "--require-output-dir",
        type=Path,
        action="append",
        default=[],
        help="Require a replay output directory with six PDFs, runtime manifest, and text regression pass.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(args.require_output_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily PDF completion hard-gate validation passed")
    print(
        "validated_workflows="
        f"{rel(DAILY_FULL_WORKFLOW)};"
        f"{rel(DAILY_MODEL_PR_WORKFLOW)};"
        f"{rel(DAILY_PDF_REPLAY_PR_WORKFLOW)}"
    )
    print(f"validated_readiness={rel(DAILY_MODEL_READINESS)}")
    if args.require_output_dir:
        print("validated_output_dirs=" + ";".join(str(path) for path in args.require_output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
