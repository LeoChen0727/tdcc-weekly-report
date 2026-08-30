from __future__ import annotations

import ast
from pathlib import Path
import shutil
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_revenue_unreacted_range_frozen_rule_launch_evidence as producer  # noqa: E402
import validate_revenue_unreacted_range_frozen_rule_launch_evidence as validator  # noqa: E402


ARTIFACT_PATHS = (
    validator.DETAIL_RELATIVE_PATH,
    validator.MATRIX_RELATIVE_PATH,
    validator.MANIFEST_RELATIVE_PATH,
)


def _artifact_fixture(tmp_path: Path) -> Path:
    for relative_path in ARTIFACT_PATHS:
        target = tmp_path / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative_path, target)
    return tmp_path


def _canonical_lf(payload: bytes) -> bytes:
    canonical = payload.replace(b"\r\n", b"\n")
    assert b"\r" not in canonical
    return canonical


def test_committed_artifacts_match_producer_and_independent_replay() -> None:
    assert producer.check_artifacts(ROOT) == []
    assert validator.validate(artifact_root=ROOT, source_root=ROOT) == []


def test_independent_validator_does_not_import_producer_or_production_semantics() -> None:
    syntax = ast.parse(
        (SCRIPTS / "validate_revenue_unreacted_range_frozen_rule_launch_evidence.py")
        .read_text(encoding="utf-8")
    )
    imported: set[str] = set()
    for node in ast.walk(syntax):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    forbidden = {
        "build_revenue_unreacted_range_frozen_rule_launch_evidence",
        "build_daily_revenue_unreacted_range_operation_section",
        "build_daily_candidate_model_layer",
    }
    assert imported.isdisjoint(forbidden)


def test_manifest_states_truthful_provisional_evidence_without_permissions() -> None:
    manifest = pd.read_csv(
        ROOT / validator.MANIFEST_RELATIVE_PATH,
        dtype=str,
        keep_default_na=False,
    ).iloc[0]
    assert manifest["launch_evidence_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    assert manifest["gross_chronological_status"] == "positive_all_thirds"
    assert manifest["transaction_cost_status"] == "robust_declared_grid"
    assert manifest["relative_edge_status"] == "weak_and_time_unstable"
    assert manifest["regime_coverage_status"] == "limited_no_range_or_high_risk"
    assert manifest["evidence_permission_status"] == "evidence_only_no_permission_grant"
    assert manifest["anomaly_operation_count"] == "9"
    assert manifest["verified_real_extreme_count"] == "8"
    assert manifest["verified_data_error_repaired_count"] == "1"
    assert manifest["effective_anomaly_blocker_count"] == "0"
    for permission in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        assert manifest[permission] == "False"


def test_frozen_sample_dates_buckets_benchmark_and_monthly_revenue_scope() -> None:
    detail = pd.read_csv(
        ROOT / validator.DETAIL_RELATIVE_PATH,
        dtype=str,
        keep_default_na=False,
    )
    assert len(detail) == 53
    assert detail["source_operation_key"].is_unique
    assert detail["chronological_bucket_id"].value_counts().to_dict() == {
        "chronological_third_1_early_18": 18,
        "chronological_third_2_middle_18": 18,
        "chronological_third_3_late_17": 17,
    }
    assert detail["benchmark_entry_date"].equals(detail["entry_date"])
    assert detail["benchmark_exit_date"].equals(detail["exit_date"])
    assert set(detail["benchmark_exact_date_coverage"]) == {"True"}
    assert detail["benchmark_index_code"].value_counts().to_dict() == {
        "TWSE": 52,
        "TPEX": 1,
    }
    assert detail["entry_market_regime"].value_counts().to_dict() == {
        "strong_bull": 31,
        "mild_bull": 11,
        "correction": 11,
    }
    assert set(detail["financial_statement_scope"]) == {
        validator.FINANCIAL_STATEMENT_SCOPE
    }
    assert not {
        "eps",
        "gross_margin",
        "operating_margin",
        "operating_income",
        "non_operating_income",
        "net_income",
    }.intersection({column.lower() for column in detail.columns})


def test_declared_cost_grid_and_sparse_control_are_not_overstated() -> None:
    matrix = pd.read_csv(
        ROOT / validator.MATRIX_RELATIVE_PATH,
        dtype=str,
        keep_default_na=False,
    )
    costs = matrix.loc[matrix["analysis_family"].eq("transaction_cost")]
    assert list(costs["group_id"]) == [
        "declared_cost_slippage_0bp_each_side",
        "declared_cost_slippage_10bp_each_side",
        "declared_cost_slippage_25bp_each_side",
    ]
    assert list(costs["avg_return_pct"]) == ["14.2238", "13.9956", "13.6541"]
    assert list(costs["median_return_pct"]) == ["8.7685", "8.5512", "8.2261"]
    stress = costs.iloc[-1]
    assert stress["positive_rate_pct"] == "73.5849"
    control = matrix.loc[
        matrix["analysis_family"].eq(
            "same_date_source_low_control_sensitivity_summary"
        )
    ].iloc[0]
    assert control["group_count"] == "7"
    assert control["sample_count"] == "10"
    assert control["comparator_sample_count"] == "11"
    assert control["status"] == "sensitivity_sparse_not_independent"
    assert control["avg_difference_pct_points"] == "-13.3660"
    assert control["median_difference_pct_points"] == "0.8096"


def test_crlf_transport_is_equivalent_for_all_committed_artifacts(tmp_path: Path) -> None:
    artifact_root = _artifact_fixture(tmp_path)
    for relative_path in ARTIFACT_PATHS:
        path = artifact_root / relative_path
        path.write_bytes(_canonical_lf(path.read_bytes()).replace(b"\n", b"\r\n"))
    assert validator.validate(artifact_root=artifact_root, source_root=ROOT) == []


def test_source_crlf_transport_keeps_canonical_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "frozen_source.csv"
    payload = _canonical_lf((ROOT / validator.SOURCE_RELATIVE_PATH).read_bytes())
    source.write_bytes(payload.replace(b"\n", b"\r\n"))
    monkeypatch.setattr(validator, "SOURCE_RELATIVE_PATH", source)
    frame = validator._read_frozen_source(ROOT)
    assert len(frame) > validator.EXPECTED_OPERATION_COUNT


@pytest.mark.parametrize("relative_path", ARTIFACT_PATHS)
def test_independent_validator_rejects_non_eol_artifact_tamper(
    tmp_path: Path, relative_path: Path
) -> None:
    artifact_root = _artifact_fixture(tmp_path)
    path = artifact_root / relative_path
    payload = _canonical_lf(path.read_bytes())
    assert b"revenue_unreacted_range" in payload
    path.write_bytes(payload.replace(b"revenue_unreacted_range", b"revenue_unreacted_rangf", 1))
    errors = validator.validate(artifact_root=artifact_root, source_root=ROOT)
    assert errors
    assert any("mismatch" in error or "drift" in error for error in errors)


def test_frozen_source_rejects_non_eol_tamper(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "frozen_source.csv"
    payload = _canonical_lf((ROOT / validator.SOURCE_RELATIVE_PATH).read_bytes())
    source.write_bytes(payload.replace(b"revenue_unreacted_range", b"revenue_unreacted_rangf", 1))
    monkeypatch.setattr(validator, "SOURCE_RELATIVE_PATH", source)
    with pytest.raises(RuntimeError, match="canonical LF SHA drift"):
        validator._read_frozen_source(ROOT)


def test_independent_validator_rejects_lone_cr_and_missing_member(tmp_path: Path) -> None:
    artifact_root = _artifact_fixture(tmp_path)
    detail_path = artifact_root / validator.DETAIL_RELATIVE_PATH
    detail_path.write_bytes(_canonical_lf(detail_path.read_bytes()).replace(b"\n", b"\r"))
    errors = validator.validate(artifact_root=artifact_root, source_root=ROOT)
    assert any("unsupported lone CR" in error for error in errors)

    artifact_root = _artifact_fixture(tmp_path / "missing")
    (artifact_root / validator.MATRIX_RELATIVE_PATH).unlink()
    errors = validator.validate(artifact_root=artifact_root, source_root=ROOT)
    assert any("missing or unsafe" in error for error in errors)
