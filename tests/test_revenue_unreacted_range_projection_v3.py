from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_revenue_unreacted_range_projection_v3 as subject
import revenue_unreacted_range_projection_source_io as source_io


def prices(dates, *, close="10", ratio="1"):
    return pd.DataFrame([[date, "10", "11", "9", close, "1000", ratio] for date in dates], columns=subject.PRICE_INPUT_COLUMNS)


def detail(**changes):
    row = dict(generated_at="old", monthly_revenue_history_blob_sha256="old", condition_variant_id="variant", episode_key="variant|1234|20260101|1", stock_id="1234",
               episode_status="launch_within_active_horizon", first_breakout_d20_return_pct="30", qualifying_source_revenue_anomaly_candidate_flag="True", unresolved_price_path_candidate_flag="False")
    row.update(changes)
    return pd.DataFrame([row])


def test_price_diff_distinguishes_added_calendar_and_derived_ratio():
    old = {"1234": prices(["20260102", "20260103"])}
    new = {"1234": prices(["20260101", "20260102", "20260103"], ratio="2")}
    row = subject.price_diff(old, new).iloc[0]
    assert row.added_date_count == 1
    assert row.shared_raw_ohlcv_changed_date_count == 0
    assert row.shared_volume_ratio_changed_date_count == 2
    assert row.change_class == "historical_rows_added|shared_volume_ratio_changed"


def test_raw_ohlcv_change_is_review_candidate_not_data_error():
    row = subject.price_diff({"1234": prices(["20260101"])}, {"1234": prices(["20260101"], close="100")}).iloc[0]
    assert row.shared_raw_ohlcv_changed_date_count == 1
    assert row.change_class == "shared_raw_ohlcv_changed_requires_review"
    assert "verified_data_error" not in row.change_class


def test_numeric_representation_is_not_a_raw_price_change():
    row = subject.price_diff({"1234": prices(["20260101"])}, {"1234": prices(["20260101"], close="10.0")}).iloc[0]
    assert row.shared_raw_ohlcv_changed_date_count == 0
    assert row.change_class == "numeric_format_only"


def test_episode_diff_ignores_only_transport_provenance_not_semantic_fields():
    old = detail()
    assert subject.episode_diff(old, detail(generated_at="new", monthly_revenue_history_blob_sha256="new")).empty
    changed = subject.episode_diff(old, detail(first_breakout_d20_return_pct="31"))
    assert changed.iloc[0].changed_columns == "first_breakout_d20_return_pct"
    assert changed.iloc[0].old_row_sha256 != changed.iloc[0].new_row_sha256


def test_episode_diff_preserves_added_and_removed_keys():
    diff = subject.episode_diff(detail(), detail(episode_key="variant|1234|20260102|1"))
    assert set(diff.change_class) == {"added_episode", "removed_episode"}


def test_episode_duplicates_fail_closed():
    with pytest.raises(RuntimeError, match="identity drift"):
        subject.episode_diff(pd.concat([detail(), detail()]), detail())


def test_primary_retains_unresolved_candidates_and_sensitivity_is_separate():
    rows = subject.comparison(detail(), detail())
    assert set(rows.loc[rows.metric_basis.eq("primary_all_rows"), "episode_count"]) == {1}
    assert set(rows.loc[rows.metric_basis.eq("candidate_exclusion_sensitivity_only"), "episode_count"]) == {0}
    assert set(rows.loc[rows.metric_basis.eq("candidate_exclusion_sensitivity_only"), "unresolved_candidate_count"]) == {0}
    assert set(rows.promotion_evidence_allowed) == {"false"}
    assert set(rows.metric_interpretation) == {"retrospective_close_observation_not_formal_operation_win_rate"}


def test_source_cutoff_occurs_before_price_comparison():
    payloads = {source_io.PRICE_PREFIX + "1234.csv": prices(["20260713", "20260714"]).to_csv(index=False).encode()}
    frames = subject.cutoff_prices(payloads, {"1234"})
    assert frames["1234"].date.tolist() == ["20260713"]


@pytest.mark.parametrize("mutation", ["extra", "missing"])
def test_writer_exact_six_files(tmp_path, mutation):
    payloads = {path: b"test" for path in subject.OUTPUTS.values()}
    if mutation == "extra": payloads["output/latest/model_operation_readiness_latest.csv"] = b"bad"
    else: payloads.pop(subject.OUTPUTS["detail"])
    with pytest.raises(RuntimeError, match="exactly six"):
        subject.write_outputs(tmp_path, payloads)
    assert not list(tmp_path.iterdir())


def test_writer_never_replaces_existing_version(tmp_path):
    payloads = {path: b"first" for path in subject.OUTPUTS.values()}
    subject.write_outputs(tmp_path, payloads)
    changed = {path: b"second" for path in subject.OUTPUTS.values()}
    with pytest.raises(RuntimeError, match="immutable"):
        subject.write_outputs(tmp_path, changed)
    assert all((tmp_path / path).read_bytes() == b"first" for path in payloads)


@pytest.mark.parametrize("outside_change", ["sentinel", "foreign_artifact"])
def test_model_owned_guard_rejects_protected_or_unowned_changes(monkeypatch, tmp_path, outside_change):
    state = {"value": "before"}
    monkeypatch.setattr(subject, "load_ownership_rules", lambda path: [])
    monkeypatch.setattr(subject, "validate_changed_paths", lambda *args: [])
    monkeypatch.setattr(subject, "_dirty_snapshot", lambda root: {})
    monkeypatch.setattr(subject, "protected_snapshot", lambda root: {"tree": {}, "physical": {}, "value": state["value"]})
    monkeypatch.setattr(subject, "changed_during_run", lambda *args: ["output/latest/foreign.csv"] if outside_change == "foreign_artifact" else [])
    with pytest.raises(RuntimeError, match="outside its six-artifact"):
        with subject.model_owned_artifact_guard(tmp_path):
            if outside_change == "sentinel": state["value"] = "changed"


def test_git_loader_is_read_only_and_requires_full_revision(monkeypatch, tmp_path):
    calls = []
    def fail(root, *args, **kwargs):
        calls.append(args)
        raise RuntimeError("missing")
    monkeypatch.setattr(source_io, "_git", fail)
    with pytest.raises(RuntimeError, match="full commit"):
        source_io.ensure_source_commit(tmp_path, "main")
    with pytest.raises(RuntimeError, match="missing"):
        source_io.ensure_source_commit(tmp_path, source_io.V2_SOURCE_COMMIT)
    assert calls == [("rev-parse", "--verify", source_io.V2_SOURCE_COMMIT + "^{commit}")]


def test_git_blob_batch_rejects_wrong_identity(monkeypatch, tmp_path):
    def git(root, *args, **kwargs):
        if args[0] == "rev-parse": return (source_io.V2_SOURCE_COMMIT + "\n").encode()
        if args[0] == "ls-tree": return b"100644 blob " + b"a" * 40 + b"\tinput.csv\0"
        return b"b" * 40 + b" blob 3\nabc\n"
    monkeypatch.setattr(source_io, "_git", git)
    with pytest.raises(RuntimeError, match="identity mismatch"):
        source_io.read_git_payloads(tmp_path, source_io.V2_SOURCE_COMMIT, ("input.csv",))
