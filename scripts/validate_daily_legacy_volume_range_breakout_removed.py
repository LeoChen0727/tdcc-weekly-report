from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_MODEL_ID = "volume_range_breakout"
V2_MODEL_IDS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
}

FORMAL_MODEL_ID_CSVS = (
    ROOT / "config" / "stock_model_contract_registry.csv",
    ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv",
    ROOT / "config" / "daily_pdf_semantic_golden_cases.csv",
    ROOT / "output" / "latest" / "daily_report_model_registry_latest.csv",
    ROOT / "output" / "latest" / "model_operation_readiness_latest.csv",
    ROOT / "output" / "latest" / "daily_candidate_model_signals_for_report_latest.csv",
    ROOT / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv",
    ROOT / "output" / "latest" / "approved_operation_patterns_latest.csv",
    ROOT / "output" / "latest" / "model_contract_parity_latest.csv",
    ROOT / "output" / "latest" / "research_backtest" / "daily_model_research_parity_latest.csv",
)
PACKET_TEXTS = (
    ROOT / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt",
    ROOT / "output" / "latest" / "CHATGPT_DAILY_REPORT_PACKET.txt",
    ROOT / "docs" / "latest" / "chatgpt_daily_report_packet_latest.txt",
)

FORBIDDEN_SOURCE_SNIPPETS = {
    ROOT / "scripts" / "build_daily_candidate_model_layer.py": (
        'def score_volume_breakout(',
        "VOLUME_RANGE_BREAKOUT_MAIN_CONDITIONS_ZH",
        '"volume_breakout_range": "volume_range_breakout"',
        'ModelSpec(\n            "volume_range_breakout"',
        '"profile=volume_range_breakout":',
        '"volume_range_breakout": ScoreProfile',
        '"model_id": "volume_range_breakout"',
    ),
    ROOT / "scripts" / "build_approved_operation_patterns.py": (
        'MODEL_ID = "volume_range_breakout"',
        "volume_breakout_operation_v1_20260615",
        "volume_breakout_confirmed_operation_v1",
        "def positive_rank_rows(",
        "def approval_row(",
    ),
    ROOT / "scripts" / "build_model_operation_readiness.py": (
        'VOLUME_MODEL_ID = "volume_range_breakout"',
        "deprecated_replaced_by_volume_range_breakout_v2",
        "legacy_isolated",
    ),
    ROOT / "build_chatgpt_daily_report_packet.py": (
        "model_id: volume_range_breakout",
        '.eq("volume_range_breakout")',
        ".eq('volume_range_breakout')",
    ),
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
        rows = list(csv.DictReader(fh))
    return [{k or "": v for k, v in row.items()} for row in rows]


def validate_formal_csvs() -> list[str]:
    errors: list[str] = []
    for path in FORMAL_MODEL_ID_CSVS:
        if not path.exists():
            continue
        rows = read_rows(path)
        for index, row in enumerate(rows, start=2):
            if str(row.get("model_id", "")).strip() == LEGACY_MODEL_ID:
                errors.append(f"{rel(path)}:{index} must not contain legacy model_id={LEGACY_MODEL_ID}")
            if path.name == "stock_model_contract_registry.csv":
                for col in ("condition_function", "score_function", "score_profile_id"):
                    if str(row.get(col, "")).strip() in {
                        "cond_volume_breakout",
                        "score_volume_breakout",
                        LEGACY_MODEL_ID,
                    }:
                        errors.append(f"{rel(path)}:{index} contains legacy {col}={row.get(col)}")
            if path.name == "approved_operation_patterns_latest.csv":
                text = ",".join(str(value) for value in row.values())
                if "volume_breakout_operation_v1_20260615" in text or "volume_breakout_confirmed_operation_v1" in text:
                    errors.append(f"{rel(path)}:{index} contains legacy v1 approval evidence")
    return errors


def validate_required_v2_rows() -> list[str]:
    errors: list[str] = []
    registry = read_rows(ROOT / "config" / "stock_model_contract_registry.csv")
    registry_ids = {row.get("model_id", "") for row in registry}
    missing = sorted(V2_MODEL_IDS - registry_ids)
    if missing:
        errors.append(f"stock_model_contract_registry missing v2 volume models: {missing}")

    readiness = read_rows(ROOT / "output" / "latest" / "model_operation_readiness_latest.csv")
    readiness_ids = {row.get("model_id", "") for row in readiness}
    missing = sorted(V2_MODEL_IDS - readiness_ids)
    if missing:
        errors.append(f"model_operation_readiness_latest missing v2 volume models: {missing}")

    approval = read_rows(ROOT / "output" / "latest" / "approved_operation_patterns_latest.csv")
    approval_ids = {row.get("model_id", "") for row in approval}
    missing = sorted(V2_MODEL_IDS - approval_ids)
    if missing:
        errors.append(f"approved_operation_patterns_latest missing v2 volume models: {missing}")
    return errors


def validate_source_snippets() -> list[str]:
    errors: list[str] = []
    for path, snippets in FORBIDDEN_SOURCE_SNIPPETS.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for snippet in snippets:
            if snippet in text:
                errors.append(f"{rel(path)} contains forbidden legacy snippet: {snippet}")
    return errors


def validate_packet_texts() -> list[str]:
    errors: list[str] = []
    forbidden_line = f"model_id: {LEGACY_MODEL_ID}"
    for path in PACKET_TEXTS:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for index, line in enumerate(lines, start=1):
            if line.strip() == forbidden_line:
                errors.append(f"{rel(path)}:{index} must not expose legacy packet {forbidden_line}")
    return errors


def validate_background_registry() -> list[str]:
    path = ROOT / "config" / "daily_model_background_data_registry.csv"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = [line for line in text.splitlines() if line.startswith("volume_breakout_operation_research_outputs,")]
    if len(lines) != 1:
        return [f"{rel(path)} must contain exactly one legacy v1 research cleanup row"]
    line = lines[0]
    required = (
        "legacy_v1_research_archive_only",
        "deprecated_candidate",
        "review_for_research_backtest_cleanup_then_delete_or_quarantine",
        "do not use as production gate score ranking PDF metric operation adapter approved_operation evidence",
    )
    return [f"{rel(path)} legacy row missing required cleanup marker: {token}" for token in required if token not in line]


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_formal_csvs())
    errors.extend(validate_required_v2_rows())
    errors.extend(validate_source_snippets())
    errors.extend(validate_packet_texts())
    errors.extend(validate_background_registry())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("legacy volume_range_breakout v1 removal validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
