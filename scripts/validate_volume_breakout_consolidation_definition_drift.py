from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
OPERATION_UTILS = ROOT / "scripts" / "volume_breakout_operation_utils.py"
PATTERN_CLASSIFIER = ROOT / "scripts" / "build_volume_breakout_pattern_classification.py"
V2_CLOSE_ONLY = ROOT / "scripts" / "build_volume_range_breakout_v2_close_only_confirmation_audit.py"
V2_CLOSE_ONLY_VALIDATOR = ROOT / "scripts" / "validate_volume_range_breakout_v2_close_only_confirmation_audit.py"
LIFECYCLE_INVENTORY = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
V2_SUMMARY = ROOT / "output" / "latest" / "research_backtest" / "volume_range_breakout_v2_close_only_confirmation_audit_latest.csv"
V2_DETAIL = ROOT / "output" / "latest" / "research_backtest" / "volume_range_breakout_v2_close_only_confirmation_audit_detail_latest.csv"

BASE_SHAPE_ID = "width40_gt40_non_consolidation"
BASE_SHAPE_DEFINITION = "range_width_40_pct > 40"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def require_contains(path: Path, text: str, needles: list[str]) -> None:
    for needle in needles:
        if needle not in text:
            fail(f"{path} missing expected definition text: {needle}")


def validate_known_legacy_definitions() -> None:
    operation_text = read_text(OPERATION_UTILS)
    require_contains(
        OPERATION_UTILS,
        operation_text,
        [
            "width40 = safe_float(row.get(\"range_width_40_pct\"))",
            "elif width40 <= 25:",
            "elif width40 <= 40:",
            "consolidation_type = \"non_consolidation\"",
        ],
    )

    pattern_text = read_text(PATTERN_CLASSIFIER)
    require_contains(
        PATTERN_CLASSIFIER,
        pattern_text,
        [
            "def consolidation_dimension(row: pd.Series)",
            "width60 = safe_float(row.get(\"range_width_60_pct\"))",
            "width60 <= 30",
            "width20 <= 18",
        ],
    )


def validate_v2_isolation() -> None:
    v2_text = read_text(V2_CLOSE_ONLY)
    validator_text = read_text(V2_CLOSE_ONLY_VALIDATOR)
    require_contains(
        V2_CLOSE_ONLY,
        v2_text,
        [
            f"BASE_SHAPE_ID = \"{BASE_SHAPE_ID}\"",
            f"BASE_SHAPE_DEFINITION = \"{BASE_SHAPE_DEFINITION}\"",
            "source[\"v2_base_shape_id\"].astype(str).eq(BASE_SHAPE_ID)",
        ],
    )
    forbidden = [
        "source[\"consolidation_type\"].astype(str).eq(\"non_consolidation\")",
        "Candidate population: `consolidation_type=non_consolidation`",
    ]
    for needle in forbidden:
        if needle in v2_text or needle in validator_text:
            fail(f"v2 close-only path still consumes legacy consolidation label: {needle}")
    require_contains(
        V2_CLOSE_ONLY_VALIDATOR,
        validator_text,
        [
            "source_work[\"range_width_40_pct\"].gt(40)",
            f"BASE_SHAPE_DEFINITION",
        ],
    )


def validate_legacy_owner_not_deleted() -> None:
    if not LIFECYCLE_INVENTORY.exists():
        fail(f"missing lifecycle inventory: {LIFECYCLE_INVENTORY}")
    inv = pd.read_csv(LIFECYCLE_INVENTORY, dtype=str, keep_default_na=False)
    row = inv[inv.get("path", pd.Series(dtype=str)).astype(str).eq("scripts/build_volume_breakout_pattern_classification.py")]
    if row.empty:
        fail("pattern classifier must remain in lifecycle inventory before deletion or cleanup is discussed")
    owner_text = "|".join(row.astype(str).agg("|".join, axis=1).tolist())
    for expected in ["research_backtest", "active"]:
        if expected not in owner_text:
            fail(f"pattern classifier lifecycle inventory must show {expected}")


def validate_v2_outputs() -> None:
    for path in [V2_SUMMARY, V2_DETAIL]:
        if not path.exists():
            fail(f"missing v2 output: {path}")
    summary = pd.read_csv(V2_SUMMARY, dtype=str, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(V2_DETAIL, dtype=str, keep_default_na=False, low_memory=False)
    if set(summary["base_shape_id"].astype(str)) != {BASE_SHAPE_ID}:
        fail("v2 summary must expose the explicit base_shape_id")
    if set(summary["base_shape_definition"].astype(str)) != {BASE_SHAPE_DEFINITION}:
        fail("v2 summary must expose the explicit base_shape_definition")
    if "v2_base_shape_match_flag" not in detail.columns:
        fail("v2 detail must expose v2_base_shape_match_flag for legacy-label audit")
    if detail["v2_base_shape_match_flag"].astype(str).eq("True").sum() == 0:
        fail("v2 detail must contain events matching the explicit base shape")


def main() -> int:
    validate_known_legacy_definitions()
    validate_v2_isolation()
    validate_legacy_owner_not_deleted()
    validate_v2_outputs()
    print("volume breakout consolidation definition drift validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
