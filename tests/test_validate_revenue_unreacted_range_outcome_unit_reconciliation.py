from __future__ import annotations

import ast
import json
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_revenue_unreacted_range_outcome_unit_reconciliation as producer
import validate_revenue_unreacted_range_outcome_unit_reconciliation as validator


def fixture():
    dates = pd.bdate_range("2025-01-01", periods=21).strftime("%Y%m%d").tolist()
    raw = pd.DataFrame({"date": dates, "close": ["100"] * 10 + ["10.2"] * 11}).to_csv(index=False).encode()
    resolutions = pd.DataFrame(columns=["stock_id", "resume_date", "exchange_ratio", "resolution_id", "root_cause_status"])
    old = pd.DataFrame([dict(episode_key="variant|4763|20250101|1", condition_variant_id="variant", stock_id="4763",
                            first_breakout_date=dates[0], first_breakout_d20_return_pct="-89.8000", launch_date="frozen",
                            qualifying_source_revenue_anomaly_candidate_flag="True", unresolved_price_path_candidate_flag="True")])
    events = [dict(event_id="split", stock_id="4763", effective_date=dates[10], new_shares_per_old_share="10")]
    detail = producer.reconcile(old, {"4763": producer.prepare_prices(raw, "4763", resolutions)}, resolutions, events)
    return old, detail, {"4763": raw}, resolutions, events


def test_independent_decimal_replay_accepts_synthetic_split():
    old, detail, prices, resolutions, events = fixture()
    validator.verify_detail(old, detail, prices, resolutions, events)
    validator.verify_comparison(detail, producer.comparison(detail))


@pytest.mark.parametrize("column,value", [("unit_reconciled_d20_return_pct", "3"), ("unit_added_share_factor", "1"),
                                          ("unit_d20_date", "20250201"), ("unit_raw_d0_close", "99"),
                                          ("unit_added_action_ids", ""), ("launch_date", "new"),
                                          ("unit_anomaly_disposition", "verified_data_error")])
def test_independent_validator_rejects_detail_mutations(column, value):
    old, detail, prices, resolutions, events = fixture()
    detail.loc[0, column] = value
    with pytest.raises(ValueError):
        validator.verify_detail(old, detail, prices, resolutions, events)


def test_independent_validator_rejects_missing_or_duplicate_rows():
    old, detail, prices, resolutions, events = fixture()
    with pytest.raises(ValueError):
        validator.verify_detail(old, detail.iloc[0:0], prices, resolutions, events)
    with pytest.raises(ValueError):
        validator.verify_detail(old, pd.concat([detail, detail]), prices, resolutions, events)


@pytest.mark.parametrize("field,value", [("episode_count", "0"), ("mean_pct", "999"),
                                        ("mean_pct", "nan"), ("mean_pct", "inf"), ("mean_pct", "-inf"),
                                        ("promotion_evidence_allowed", "true"), ("metric_basis", "corrected_performance")])
def test_independent_validator_rejects_metric_or_claim_drift(field, value):
    _, detail, _, _, _ = fixture()
    metrics = producer.comparison(detail)
    metrics.loc[0, field] = value
    with pytest.raises(ValueError):
        validator.verify_comparison(detail, metrics)


def test_validator_has_no_producer_business_import():
    tree = ast.parse((ROOT / "scripts/validate_revenue_unreacted_range_outcome_unit_reconciliation.py").read_text(encoding="utf-8"))
    modules = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    assert "build_revenue_unreacted_range_outcome_unit_reconciliation" not in modules
    assert "revenue_unreacted_range_source_first_condition_audit" not in modules


def test_official_evidence_contract_is_independently_verified():
    config = json.loads((ROOT / producer.CONFIG).read_text(encoding="utf-8"))
    validator.check_config(config)
    config["events"][0]["new_shares_per_old_share"] = "100"
    with pytest.raises(ValueError, match="unapproved"):
        validator.check_config(config)


def test_rehashed_report_cannot_add_contradictory_formal_claim():
    report = (ROOT / validator.OUTPUTS["report"]).read_bytes()
    manifest = json.loads((ROOT / validator.OUTPUTS["manifest"]).read_text(encoding="utf-8"))
    changed = report + "\n本研究已正式可用。\n".encode("utf-8")
    manifest["output_sha256"][validator.OUTPUTS["report"]] = validator.sha(changed)
    assert manifest["output_sha256"][validator.OUTPUTS["report"]] == validator.sha(changed)
    with pytest.raises(ValueError, match="report exact"):
        validator.verify_report(changed, 20430, manifest["changed_row_count"])
    validator.verify_report(report, 20430, manifest["changed_row_count"])


def test_published_artifacts_independent_raw_replay_when_materialized():
    assert (ROOT / validator.OUTPUTS["manifest"]).is_file(), "published six-artifact family is required; missing artifacts fail closed"
    assert validator.validate(ROOT)["rows"] == 20430
