from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_revenue_unreacted_range_outcome_unit_reconciliation as subject


def fixture(*, stock="4763", action_date="20250115", ratio="10", prior=False):
    dates = pd.bdate_range("2025-01-01", periods=25).strftime("%Y%m%d").tolist()
    prices = pd.DataFrame({"date": dates, "close": ["100" if date < action_date else "10.2" for date in dates]})
    resolutions = pd.DataFrame(columns=["stock_id", "resume_date", "exchange_ratio", "resolution_id", "root_cause_status"])
    if prior:
        resolutions.loc[0] = [stock, action_date, ratio, "old", "verified_non_comparable_raw_price_scale"]
    frame = subject.prepare_prices(prices.to_csv(index=False).encode(), stock, resolutions)
    old = (frame.iloc[20].analysis_close / frame.iloc[0].analysis_close - 1) * 100
    detail = pd.DataFrame([dict(episode_key="v|" + stock + "|20250101|1", condition_variant_id="v", stock_id=stock,
                               first_breakout_date=dates[0], first_breakout_d20_return_pct=f"{old:.4f}",
                               episode_status="original_status", launch_date="original_launch",
                               qualifying_source_revenue_anomaly_candidate_flag="True", unresolved_price_path_candidate_flag="True")])
    events = [dict(event_id="new", stock_id=stock, effective_date=action_date, new_shares_per_old_share=ratio)]
    return detail, {stock: frame}, resolutions, events, prices.to_csv(index=False).encode()


def test_split_reconciles_without_mutating_any_old_column_or_flag():
    detail, prices, resolutions, events, _ = fixture()
    result = subject.reconcile(detail, prices, resolutions, events)
    assert result.loc[:, detail.columns].equals(detail)
    assert float(result.iloc[0].unit_reconciled_d20_return_pct) == pytest.approx(2)
    assert result.iloc[0].unit_anomaly_disposition == "unresolved_anomaly_candidate"
    assert result.iloc[0].unit_added_action_ids == "new"


def test_existing_normalized_actions_not_applied_twice():
    detail, prices, resolutions, events, _ = fixture(prior=True)
    with pytest.raises(RuntimeError, match="already normalized"):
        subject.reconcile(detail, prices, resolutions, events)
    result = subject.reconcile(detail, prices, resolutions, [])
    assert float(result.iloc[0].unit_reconciled_d20_return_pct) == pytest.approx(2)
    assert result.iloc[0].unit_existing_action_ids == "old"


@pytest.mark.parametrize("offset,expected", [(0, False), (20, True), (21, False)])
def test_action_interval_is_start_exclusive_end_inclusive(offset, expected):
    detail, prices, resolutions, events, _ = fixture()
    events[0]["effective_date"] = prices["4763"].iloc[offset].date
    result = subject.reconcile(detail, prices, resolutions, events)
    assert bool(result.iloc[0].unit_added_action_ids) is expected


def test_immature_and_no_breakout_are_not_invented():
    detail, prices, resolutions, events, _ = fixture()
    detail["first_breakout_d20_return_pct"] = ""
    result = subject.reconcile(detail, prices, resolutions, events)
    assert result.iloc[0].unit_reconciliation_status == "no_mature_d20_observation"
    assert result.iloc[0].unit_reconciled_d20_return_pct == ""


def test_original_outcome_must_reconcile_before_any_new_adjustment():
    detail, prices, resolutions, events, _ = fixture()
    detail["first_breakout_d20_return_pct"] = "999"
    with pytest.raises(RuntimeError, match="original outcome mismatch"):
        subject.reconcile(detail, prices, resolutions, events)


def test_duplicate_episodes_fail_closed():
    detail, prices, resolutions, events, _ = fixture()
    with pytest.raises(RuntimeError, match="identity"):
        subject.reconcile(pd.concat([detail, detail]), prices, resolutions, events)


def test_comparison_retains_candidates_primary_and_separates_sensitivity():
    detail, prices, resolutions, events, _ = fixture()
    result = subject.comparison(subject.reconcile(detail, prices, resolutions, events))
    assert set(result[result.metric_basis.eq("primary_all_rows")].episode_count) == {"1"}
    assert set(result[result.metric_basis.eq("candidate_exclusion_sensitivity_only")].episode_count) == {"0"}
    assert set(result.promotion_evidence_allowed) == {"false"}


def test_embedded_official_receipts_verify_offline():
    config = json.loads((ROOT / subject.CONFIG).read_text(encoding="utf-8"))
    assert subject.validate_actions(config, ROOT)[0]["new_shares_per_old_share"] == "10"


@pytest.mark.parametrize("key,value", [("new_shares_per_old_share", "0"), ("new_shares_per_old_share", "NaN"),
                                       ("effective_date", "20250629"), ("stock_id", "8291"),
                                       ("verification_status", "pending_receipt")])
def test_unapproved_event_or_ratio_fails(key, value):
    config = json.loads((ROOT / subject.CONFIG).read_text(encoding="utf-8"))
    config["events"][0][key] = value
    with pytest.raises(RuntimeError):
        subject.validate_actions(config, ROOT)


def test_embedded_receipt_mutation_fails():
    config = json.loads((ROOT / subject.CONFIG).read_text(encoding="utf-8"))
    config["documents"]["twse_4763_20250606"]["sha256"] = "0" * 64
    with pytest.raises(RuntimeError, match="receipt SHA"):
        subject.validate_actions(config, ROOT)


def test_writer_exact_six_immutable_files(tmp_path, monkeypatch):
    monkeypatch.setattr(subject, "OUTPUTS", {key: key + ".csv" for key in subject.OUTPUTS})
    payloads = {value: b"data\n" for value in subject.OUTPUTS.values()}
    with pytest.raises(RuntimeError, match="exactly six"):
        subject.write_outputs(tmp_path, {**payloads, "extra.csv": b"extra"})
    subject.write_outputs(tmp_path, payloads)
    subject.write_outputs(tmp_path, payloads)
    changed = copy.deepcopy(payloads)
    changed[subject.OUTPUTS["detail"]] = b"changed\n"
    with pytest.raises(RuntimeError, match="immutable"):
        subject.write_outputs(tmp_path, changed)
    assert (tmp_path / subject.OUTPUTS["detail"]).read_bytes() == b"data\n"


def test_guard_rejects_unregistered_output_before_build(tmp_path):
    registry = tmp_path / "config/model_research_artifact_ownership.csv"
    registry.parent.mkdir()
    registry.write_text("owner_model_id,producer,artifact_glob,artifact_class,change_policy,formal_evidence_status\nother,other.py,other.csv,model_research_output,model_owned_write,research_only\n")
    with pytest.raises(RuntimeError, match="unregistered"):
        with subject.model_owned_artifact_guard(tmp_path):
            pytest.fail("guard must reject before entering")


@pytest.mark.parametrize("protected_drift,changed", [(True, []), (False, ["output/latest/model_operation_readiness_latest.csv"])])
def test_guard_detects_protected_or_out_of_scope_changes(monkeypatch, tmp_path, protected_drift, changed):
    monkeypatch.setattr(subject, "load_ownership_rules", lambda _: [])
    monkeypatch.setattr(subject, "validate_changed_paths", lambda *args: [])
    monkeypatch.setattr(subject, "_dirty_snapshot", lambda _: {})
    monkeypatch.setattr(subject, "changed_during_run", lambda *args: changed)
    snapshots = iter([{"protected": "old"}, {"protected": "new" if protected_drift else "old"}])
    monkeypatch.setattr(subject, "protected_snapshot", lambda _: next(snapshots))
    with pytest.raises(RuntimeError, match="protected/out-of-scope"):
        with subject.model_owned_artifact_guard(tmp_path):
            pass
