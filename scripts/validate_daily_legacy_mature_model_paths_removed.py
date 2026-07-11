from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEPRECATED_FUNCTION_SENTINEL = "deprecated_no_production_function"

CANONICAL_OPERATION_MODEL_IDS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
    "price_pullback_23ema",
}

DEPRECATED_FORMAL_MODEL_IDS = {
    "volume_range_breakout",
    "near_high_neckline_challenge",
    "platform_strengthening",
}

FORBIDDEN_FORMAL_MODEL_ID_ALIASES = DEPRECATED_FORMAL_MODEL_IDS | {
    "w_bottom",
    "w_bottom_right",
    "w_bottom_right_low_early_entry",
    "w_bottom_early_entry",
    "w_bottom_right_side_research",
    "price_pullback",
    "ema23_pullback",
    "price_pullback_23ema_research",
}

FORMAL_MODEL_ID_CSVS = (
    ROOT / "config" / "daily_model_condition_spec.csv",
    ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv",
    ROOT / "config" / "daily_pdf_semantic_golden_cases.csv",
    ROOT / "output" / "latest" / "daily_report_model_registry_latest.csv",
    ROOT / "output" / "latest" / "model_operation_readiness_latest.csv",
    ROOT / "output" / "latest" / "daily_candidate_model_signals_latest.csv",
    ROOT / "output" / "latest" / "daily_candidate_model_signals_for_report_latest.csv",
    ROOT / "output" / "latest" / "approved_operation_patterns_latest.csv",
    ROOT / "output" / "latest" / "model_contract_parity_latest.csv",
    ROOT / "output" / "latest" / "daily_w_bottom_right_side_operation_section_latest.csv",
    ROOT / "output" / "latest" / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
    ROOT / "output" / "latest" / "daily_price_pullback_23ema_operation_section_latest.csv",
    ROOT / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv",
    ROOT / "output" / "latest" / "research_backtest" / "daily_model_research_parity_latest.csv",
)

PACKET_TEXTS = (
    ROOT / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt",
    ROOT / "output" / "latest" / "CHATGPT_DAILY_REPORT_PACKET.txt",
    ROOT / "docs" / "latest" / "chatgpt_daily_report_packet_latest.txt",
)

FORBIDDEN_SOURCE_SNIPPETS = {
    ROOT / "scripts" / "build_daily_candidate_model_layer.py": (
        "def cond_neckline_challenge(",
        "def cond_platform_strength(",
        "def score_neckline_challenge(",
        "def score_platform_strength(",
        '"near_high_neckline_challenge": ScoreProfile',
        '"platform_strengthening": ScoreProfile',
        'ModelSpec(\n            "near_high_neckline_challenge"',
        'ModelSpec(\n            "platform_strengthening"',
    ),
    ROOT / "scripts" / "audit_daily_candidate_model_selection_correctness.py": (
        'elif model == "near_high_neckline_challenge"',
        'elif model == "platform_strengthening"',
    ),
    ROOT / "scripts" / "build_daily_w_bottom_operation_sections.py": (
        "RESEARCH_LATEST_DIR",
        "research_backtest",
        "preview",
    ),
    ROOT / "scripts" / "build_daily_price_pullback_23ema_operation_section.py": (
        "RESEARCH_LATEST_DIR",
        "research_backtest",
        "preview",
    ),
}

EXPECTED_ADAPTER_MODELS = {
    ROOT / "output" / "latest" / "daily_w_bottom_right_side_operation_section_latest.csv": {
        "w_bottom_right_side",
    },
    ROOT / "output" / "latest" / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv": {
        "neckline_volume_breakout_confirmation",
    },
    ROOT / "output" / "latest" / "daily_price_pullback_23ema_operation_section_latest.csv": {
        "price_pullback_23ema",
    },
    ROOT / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv": {
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
        "volume_range_breakout_v2_high_position_volume_attack",
    },
}


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{k or "": str(v or "").strip() for k, v in row.items()} for row in csv.DictReader(fh)]


def validate_registry_deprecations() -> list[str]:
    errors: list[str] = []
    rows = read_rows(ROOT / "config" / "stock_model_contract_registry.csv")
    by_model = {row.get("model_id", ""): row for row in rows}
    for model_id in sorted(DEPRECATED_FORMAL_MODEL_IDS - {"volume_range_breakout"}):
        row = by_model.get(model_id)
        if row is None:
            errors.append(f"stock_model_contract_registry missing deprecated audit row for {model_id}")
            continue
        if row.get("pdf_visibility") != "deprecated_not_pdf_core":
            errors.append(f"{model_id} must remain deprecated_not_pdf_core in stock_model_contract_registry")
        for col in ("condition_function", "score_function", "score_profile_id"):
            if row.get(col) != DEPRECATED_FUNCTION_SENTINEL:
                errors.append(f"{model_id} registry {col} must be {DEPRECATED_FUNCTION_SENTINEL}")
        for col in (
            "approved_for_daily_pdf",
            "approved_for_tdcc_weekly_pdf",
            "approved_for_individual_pdf",
            "research_baseline_required",
            "promotion_required",
        ):
            if row.get(col) != "false":
                errors.append(f"{model_id} registry {col} must be false")
    return errors


def validate_formal_csvs() -> list[str]:
    errors: list[str] = []
    for path in FORMAL_MODEL_ID_CSVS:
        if not path.exists():
            continue
        for index, row in enumerate(read_rows(path), start=2):
            model_id = row.get("model_id", "")
            if model_id in FORBIDDEN_FORMAL_MODEL_ID_ALIASES:
                errors.append(f"{rel(path)}:{index} must not contain legacy or alias model_id={model_id}")
            if path.name == "approved_operation_patterns_latest.csv":
                if model_id in CANONICAL_OPERATION_MODEL_IDS and row.get("approved_for_daily") != "True":
                    errors.append(f"{rel(path)}:{index} canonical operation model {model_id} must be approved_for_daily=True")
            if path.name.endswith("_operation_section_latest.csv") and row.get("row_type") != "empty_state":
                if row.get("approved_for_daily") != "True" or row.get("operation_module_approved_for_daily") != "True":
                    errors.append(f"{rel(path)}:{index} operation data row must be backed by approved daily operation module")
    return errors


def validate_adapter_model_sets() -> list[str]:
    errors: list[str] = []
    for path, expected in EXPECTED_ADAPTER_MODELS.items():
        if not path.exists():
            errors.append(f"missing operation adapter: {rel(path)}")
            continue
        rows = read_rows(path)
        models = {row.get("model_id", "") for row in rows if row.get("model_id", "")}
        unexpected = sorted(models - expected)
        missing = sorted(expected - models)
        if unexpected:
            errors.append(f"{rel(path)} contains unexpected model_ids: {unexpected}")
        if missing:
            errors.append(f"{rel(path)} missing expected model_ids: {missing}")
    return errors


def validate_source_snippets() -> list[str]:
    errors: list[str] = []
    for path, snippets in FORBIDDEN_SOURCE_SNIPPETS.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for snippet in snippets:
            if snippet in text:
                errors.append(f"{rel(path)} contains forbidden legacy mature-model snippet: {snippet}")
    return errors


def validate_packet_texts() -> list[str]:
    errors: list[str] = []
    forbidden_lines = {f"model_id: {model_id}" for model_id in FORBIDDEN_FORMAL_MODEL_ID_ALIASES}
    for path in PACKET_TEXTS:
        if not path.exists():
            continue
        for index, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
            if line.strip() in forbidden_lines:
                errors.append(f"{rel(path)}:{index} must not expose legacy mature model packet line {line.strip()!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_registry_deprecations())
    errors.extend(validate_formal_csvs())
    errors.extend(validate_adapter_model_sets())
    errors.extend(validate_source_snippets())
    errors.extend(validate_packet_texts())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("legacy mature model path removal validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
