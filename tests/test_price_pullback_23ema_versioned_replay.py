from __future__ import annotations

import json
import csv
import gzip
from datetime import date, timedelta

import pytest

import scripts.build_price_pullback_23ema_versioned_replay as producer
from scripts import validate_price_pullback_23ema_versioned_replay as validator


def forward():
    return [{"day": day, "date": f"d{day:02d}", "open": 100.0, "close": 100.0,
             "ma20": 90.0, "ema23": 90.0} for day in range(1, 22)]


def test_equal_target_differs_between_ge_and_gt():
    trace = forward(); trace[0]["close"] = 150.0
    assert validator.replay_legacy(trace, 100, 150)["target_day"] == 1
    assert validator.replay_legacy(trace, 100, 150, "strict_gt_legacy_refs")["target_day"] is None


def test_simultaneous_reference_hits_are_legacy_unresolved_formal_target_first():
    # Function-level reference matrix; not claimed as an observed OHLC tape.
    trace = forward()
    for row in trace[:4]: row.update(close=90.0, ma20=120.0, ema23=120.0)
    trace[3]["close"] = 110.0
    old = validator.replay_legacy(trace, 100, 105)
    formal = validator.replay_formal(trace, 100, 105)
    assert old["exit_reason"] == "same_day_unresolved"
    assert old["realized_return_pct"] is None
    assert formal["exit_reason"] == "close_prev20_high_break_next_open"
    assert formal["stop_confirmed_days"] == 3


def test_d20_target_uses_d21_open_and_no_trigger_is_only_legacy_close_exit():
    trace = forward(); trace[19]["close"] = 151.0; trace[20]["open"] = 160.0
    result = validator.replay_legacy(trace, 100, 150)
    assert result["exit_date"] == "d21"
    assert result["exit_price"] == 160
    assert result["realized_return_pct"] == pytest.approx(60)
    ordinary = forward(); ordinary[19]["close"] = 95.0
    assert validator.replay_legacy(ordinary, 100, 150)["exit_reason"] == "d20_close"
    assert validator.replay_formal(ordinary, 100, 150)["state"] == "expired_d20_no_active_tracking"
    assert validator.replay_formal(ordinary, 100, 150)["realized_return_pct"] is None


def test_stop_streak_resets_before_four_consecutive_closes():
    trace = forward()
    for index in [0, 1, 2, 4, 5, 6, 7]: trace[index].update(close=90.0, ma20=100.0, ema23=100.0)
    trace[8]["open"] = 80.0
    result = validator.replay_legacy(trace, 100, 200)
    assert result["stop_day"] == 8
    assert result["exit_date"] == "d09"
    assert result["realized_return_pct"] == pytest.approx(-20)


def test_missing_d21_prevents_legacy_maturity_and_formal_realized_target_exit():
    trace = forward()[:20]; trace[-1]["close"] = 160
    assert not validator.replay_legacy(trace, 100, 150)["mature"]
    formal = validator.replay_formal(trace, 100, 150)
    assert formal["state"] == "target_exit_pending_next_open"
    assert formal["realized_return_pct"] is None


def test_invalid_stop_reference_resets_formal_streak_instead_of_filling():
    trace = forward()
    for row in trace[:8]: row.update(close=90.0, ma20=100.0, ema23=100.0)
    trace[3].update(ma20=None, ema23=None)
    assert validator.replay_formal(trace, 100, 200)["realized_days"] == 8
    assert not validator.replay_legacy(trace, 100, 200)["mature"]


def test_diagnostic_incomplete_tape_retains_censoring_without_formal_position_claim():
    trace = forward()[:5]
    diagnostic = producer.replay_formal_adapter(trace, 200)
    independent = validator.replay_formal(trace, 100, 200)
    assert diagnostic["state"] == "right_censored"
    assert independent["state"] == "active_operation"
    assert diagnostic["exit_date"] == ""
    assert independent["realized_return_pct"] is None


def lifecycle_row(trade, position, variant="legacy_ge", stock="1001"):
    trace = forward(); trace[3]["close"] = 160
    return {"rule_variant": variant, "stock_id": stock, "stock_day_position": str(position),
            "new_global_index": str(position), "trade_id": trade, "trace_json": json.dumps(trace),
            "entry_price": "100", "target_price": "150"}


def test_active_suppresses_until_exit_equality_with_stock_and_variant_isolation():
    rows = [lifecycle_row("a", 10), lifecycle_row("b", 14), lifecycle_row("c", 15),
            lifecycle_row("other_stock", 14, stock="1002"), lifecycle_row("other_variant", 14, variant="strict_gt_legacy_refs")]
    result = validator.expected_lifecycle(rows)
    assert result["a"]["exit_stock_day_position"] == 15
    assert not result["b"]["accepted_trade"]
    assert result["b"]["suppressed_by_trade_id"] == "a"
    assert result["c"]["accepted_trade"]
    assert result["other_stock"]["accepted_trade"]
    assert result["other_variant"]["accepted_trade"]


def test_metrics_keep_unresolved_and_missing_tie_in_primary_denominator():
    rows = [{"realized_return_pct": "10", "outcome_bucket": "win", "anomaly_status": "unresolved_anomaly_candidate"},
            {"realized_return_pct": "-5", "outcome_bucket": "failure", "anomaly_status": "none"},
            {"realized_return_pct": "", "outcome_bucket": "same_day_unresolved", "anomaly_status": "none"}]
    result = validator.metrics(rows)
    assert result["n"] == 3 and result["finite_return_count"] == 2 and result["missing_return_count"] == 1
    assert result["unresolved_candidate_count"] == 1
    assert result["mean_return_pct"] == pytest.approx(2.5)
    assert result["high_return_hit_rate_pct"] == pytest.approx(100 / 3)


def test_row_hash_order_pinned_ast_and_artifact_numeric_bindings(tmp_path):
    assert validator.canonical_row_sha256({"b": "2", "a": "1"}) == validator.canonical_row_sha256({"a": "1", "b": "2"})
    assert validator.canonical_row_sha256({"a": "1"}) != validator.canonical_row_sha256({"a": "2"})
    a = validator.source_ast_sha256(b"def f(x):\n    return x + 1\n", ["f"])
    assert a == validator.source_ast_sha256(b"def f(x):\n  return x+1\n", ["f"])
    assert a != validator.source_ast_sha256(b"def f(x):\n    return x + 2\n", ["f"])
    trace = forward()
    for row in trace:
        row["date"] = (date(2025, 12, 1) + timedelta(days=row["day"] - 1)).strftime("%Y%m%d")
    ledger = []
    for variant in validator.VARIANTS:
        result = validator.replay_legacy(trace, 100, 200, variant)
        ledger.append({"rule_variant": variant, "trade_id": variant, "signal_id": "signal1", "stock_id": "1001",
                       "signal_date": "20251128", "stock_day_position": 40, "stock_work_rows": 100, "new_global_index": 40,
                       "gate_eligible": True, "accepted_trade": True, "mature": True, "primary_included": True,
                       "selector_status": "legacy_gate_eligible", "trace_json": json.dumps(trace),
                       "formal_adapter_trace_json": json.dumps(trace),
                       "formal_adapter_result_json": json.dumps({"state": "expired_d20_no_active_tracking", "exit_date": "", "exit_reason": ""}),
                       "formal_target_price": 200, "target_price": 200, "entry_price": 100,
                       "formal_position_status": "not_formal_position", "pre_effective_from": True,
                       "fullselectorparity_not_proven": True, "pit_status": "unknown_original_publication",
                       "publication_available_at": "", "suppressed_by_trade_id": "", "exit_stock_day_position": 60,
                       "lifecycle_status": "exited", "anomaly_status": "no_candidate_trigger",
                       **{feature: True for feature in validator.FEATURES}, **result})
    summaries, comparisons = [], []
    for variant in validator.VARIANTS:
        selected = [r for r in ledger if r["rule_variant"] == variant]
        for basis in validator.BASES:
            stat = validator.metrics(selected)
            summaries.append({"rule_variant": variant, "basis": basis, "eligible_signal_count": 1,
                              "suppressed_signal_count": 0, "immature_signal_count": 0, "left_censored_count": 0,
                              "promotion_allowed": False, "original_1161_ledger_restored": False, **stat})
            for group in ("high_return_upper_quartile", "negative_return", "matched_single_feature"):
                cohort = [] if group == "negative_return" else selected
                for feature in validator.FEATURES:
                    comparisons.append({"rule_variant": variant, "basis": basis, "group": group, "feature": feature,
                                        "cohort_n": len(cohort), "known_n": len(cohort), "unknown_n": 0,
                                        "feature_true_pct_of_known": 100 if cohort else None,
                                        "buy_sell_holding_basis": "same_accepted_trade_cohort_no_signal_reselection",
                                        **validator.metrics(cohort, high_cut=stat["high_return_threshold_pct"])})
    hashes = {}
    values = {"ledger": ledger, "summary": summaries, "feature_comparison": comparisons,
              "pit_coverage": [{"pit_status": "unknown_original_publication", "promotion_allowed": False}],
              "parity": [{"status": "not_proven"}]}
    for name, rows in values.items():
        path = tmp_path / (validator.PREFIX + name + ".csv")
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
        if name == "ledger":
            compressed = path.with_suffix(".csv.gz")
            compressed.write_bytes(gzip.compress(path.read_bytes(), mtime=0))
            path.unlink()
            path = compressed
        hashes[path.name] = validator.digest(path.read_bytes())
    manifest = {"source_ref": validator.SOURCE_REF, "semantic_ref": validator.SEMANTIC_REF, "formal_ref": validator.SOURCE_REF,
                "signal_start": "20251128", "signal_end": "20260602", "data_ceiling": "20260703", "output_hashes": hashes,
                **{k: False for k in ("promotion_allowed", "original_1161_ledger_restored", "original_primary_metrics_modified",
                                      "original_publication_version_verified", "formal_signal_selector_parity_proven",
                                      "formal_model_backtest_parity_or_anomaly_disposition_proven")}}
    manifest_path = tmp_path / (validator.PREFIX + "manifest.json")
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    assert validator.validate(tmp_path) == []
    summary_path = tmp_path / (validator.PREFIX + "summary.csv")
    summary_path.write_bytes(summary_path.read_bytes() + b"\n")
    assert any("artifact SHA mismatch" in e for e in validator.validate(tmp_path))
    manifest["output_hashes"][summary_path.name] = validator.digest(summary_path.read_bytes())
    manifest["promotion_allowed"] = True
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    assert any("unproven manifest claim" in e for e in validator.validate(tmp_path))


def neutral_producer_guard(monkeypatch):
    monkeypatch.setattr(producer, "load_ownership_rules", lambda path: [])
    monkeypatch.setattr(producer, "validate_changed_paths", lambda *args: [])
    monkeypatch.setattr(producer, "git", lambda *args: b"")
    monkeypatch.setattr(producer, "protected_snapshot", lambda path: {})


def test_source_reader_binds_canonical_blobs_without_archive_eol_conversion(tmp_path, monkeypatch):
    source = b"date,close\n20260101,100\n"
    path = "data/stock_price_history/1001.csv"
    blob_id = "a" * 40
    monkeypatch.setattr(producer, "git", lambda *args: f"100644 blob {blob_id}\t{path}\n".encode())
    def cat_file(command, **kwargs):
        assert command == ["git", "--no-replace-objects", "cat-file", "--batch"]
        assert kwargs["input"] == (blob_id + "\n").encode()
        return f"{blob_id} blob {len(source)}\n".encode() + source + b"\n"
    monkeypatch.setattr(producer.subprocess, "check_output", cat_file)
    blobs, records = producer.read_git_inputs(tmp_path)
    assert blobs == {path: source}
    assert records == [{"path": path, "git_blob": blob_id,
                        "sha256": validator.digest(source), "bytes": len(source)}]
    assert records[0]["sha256"] != validator.digest(source.replace(b"\n", b"\r\n"))


def test_writer_compresses_ledger_deterministically_and_binds_stored_bytes(tmp_path):
    result = {key: [{"stock_id": "1001", "value": "測試"}]
              for key in ("ledger", "pit_coverage", "parity", "summary", "feature_comparison")}
    result["manifest"] = {"promotion_allowed": False}
    first, second = tmp_path / "first", tmp_path / "second"
    hashes = producer.write_outputs(first, result)
    assert hashes == producer.write_outputs(second, result)
    name = producer.PREFIX + "ledger.csv.gz"
    payload = (first / name).read_bytes()
    assert payload[4:8] == b"\x00" * 4
    assert gzip.decompress(payload).decode("utf-8") == "stock_id,value\n1001,測試\n"
    assert hashes[name] == validator.digest(payload)
    assert validator.read_csv(first / name) == result["ledger"]
    assert not (first / (producer.PREFIX + "ledger.csv")).exists()


def create_guard_outputs(output_root):
    output_root.mkdir()
    for name in producer.OUTPUT_NAMES:
        with (output_root / name).open("xb") as stream:
            stream.write(name.encode("utf-8"))


def test_producer_guard_requires_new_exclusive_six_outputs_and_rejects_seventh(tmp_path, monkeypatch):
    neutral_producer_guard(monkeypatch)
    repo_root = tmp_path / "repo_not_materialized"
    output_root = tmp_path / "six_outputs"
    with producer.model_owned_artifact_guard(repo_root, output_root) as receipt:
        create_guard_outputs(output_root)
    assert set(producer.output_snapshot(output_root)) == set(producer.OUTPUT_NAMES)
    assert receipt["protected_sentinel_before_sha256"] == receipt["protected_sentinel_after_sha256"]
    with pytest.raises(ValueError, match="refuses to overwrite an existing artifact"):
        with producer.model_owned_artifact_guard(repo_root, output_root):
            pytest.fail("existing versioned artifacts must reject entry")

    extra_root = tmp_path / "seventh_output"
    with pytest.raises(RuntimeError, match="model-owned output scope changed outside six artifacts"):
        with producer.model_owned_artifact_guard(repo_root, extra_root):
            create_guard_outputs(extra_root)
            (extra_root / "another_model.csv").write_bytes(b"forbidden output")


@pytest.mark.parametrize("mutation", ["repository", "protected"])
def test_producer_guard_rejects_repository_or_protected_snapshot_drift(tmp_path, monkeypatch, mutation):
    neutral_producer_guard(monkeypatch)
    if mutation == "repository":
        statuses = iter([b"", b" M config/protected.csv\n"])
        monkeypatch.setattr(producer, "git", lambda *args: next(statuses))
        expected_error = "repository changed during diagnostic producer"
    else:
        snapshots = iter([{"protected.csv": {"git_blob": "before"}},
                          {"protected.csv": {"git_blob": "after"}}])
        monkeypatch.setattr(producer, "protected_snapshot", lambda path: next(snapshots))
        expected_error = "protected mature-model artifacts changed during replay"
    with pytest.raises(RuntimeError, match=expected_error):
        with producer.model_owned_artifact_guard(tmp_path / "repo_not_materialized", tmp_path / "outputs"):
            create_guard_outputs(tmp_path / "outputs")
