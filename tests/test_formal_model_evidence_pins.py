from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_approved_operation_patterns import build_approval  # noqa: E402
from formal_model_evidence import evidence_pin_for_model  # noqa: E402
from validate_formal_model_evidence_pins import validate  # noqa: E402


def test_formal_model_evidence_pins_validate() -> None:
    assert validate() == []


def test_approved_operation_rows_carry_exact_evidence_pins() -> None:
    approval = build_approval("2026-07-12 00:00:00 Asia/Taipei")
    assert len(approval) == 6
    for _, row in approval.iterrows():
        pin = evidence_pin_for_model(str(row["model_id"]), str(row["approval_version"]))
        assert row["evidence_artifact_version"] == pin.evidence_version
        assert row["evidence_canonical_sha256"] == pin.canonical_sha256
        assert row["evidence_pin_source"] == pin.evidence_path


def test_price_pullback_pin_uses_promoted_spec_not_mutable_latest() -> None:
    pin = evidence_pin_for_model("price_pullback_23ema", "price_pullback_23ema_operation_v1_20260703")
    assert pin.evidence_path == "docs/specs/price_pullback_23ema_operation_candidate_spec.md"
    assert "latest" not in pin.evidence_path


def test_revenue_pin_uses_immutable_frozen_rule_launch_manifest() -> None:
    pin = evidence_pin_for_model(
        "revenue_unreacted_range",
        "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830",
    )
    assert pin.evidence_path == (
        "config/approved_operation_evidence/"
        "revenue_unreacted_range_source_mid_falling_"
        "frozen_rule_launch_evidence_v1_20260830_manifest.csv"
    )
    assert pin.evidence_version == (
        "revenue_unreacted_range_source_mid_falling_"
        "frozen_rule_launch_evidence_v1_20260830"
    )
    assert pin.canonical_sha256 == (
        "4890147988797f8d0e7a27777d400514b423b679f108565675309ec2e83161fb"
    )
