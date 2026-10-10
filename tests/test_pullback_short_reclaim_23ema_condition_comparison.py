"""Fail-closed regression tests for the frozen reclaim feature comparison."""
from __future__ import annotations

import ast
import copy
from decimal import Decimal
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_pullback_short_reclaim_23ema_condition_comparison as producer
import validate_pullback_short_reclaim_23ema_condition_comparison as validator


@pytest.fixture(scope="module")
def comparison_sources():
    return validator.load_sources(ROOT)


@pytest.fixture(scope="module")
def comparison_bundle(comparison_sources):
    """Build only this new comparison in memory, reusing immutable blob reads."""
    def reader(root, commit, path, expected_sha256=None):
        if commit == validator.SOURCE_COMMIT:
            keys = [key for key, spec in validator.SOURCE_ARTIFACTS.items() if spec["path"] == path]
            assert len(keys) == 1
            payload = comparison_sources[keys[0]]
        else:
            assert commit == validator.SNAPSHOT_COMMIT
            payload = comparison_sources["snapshots"][path]
        if expected_sha256 is not None:
            assert validator._sha(payload) == expected_sha256
        return payload
    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(producer, "read_git_blob", reader)
        return producer.build_bundle(ROOT)


@pytest.fixture(scope="module")
def comparison_references(comparison_sources, comparison_bundle):
    rows, receipts, columns = validator.verify_detail(comparison_sources, comparison_bundle[0])
    return rows, receipts, columns, *validator.expected_tables(rows)


def test_comparison_independent_bundle_success(comparison_sources, comparison_bundle):
    result = validator.validate_bundle(ROOT, *comparison_bundle, sources=comparison_sources)
    assert result == {
        "source_rows": 3020, "unique_signal_events": 2992, "context_schema_primary_count": 1846,
        "snapshot_count": 32, "summary_rows": 630, "feature_rows": 4860,
        "original_cells_and_unresolved_anomalies_retained": True, "formal_use_allowed": False,
    }


def test_comparison_frozen_columns_dates_and_partial_basis_unchanged(comparison_sources, comparison_bundle):
    original = validator._csv(comparison_sources["detail"])
    detail = comparison_bundle[0]
    pd.testing.assert_frame_equal(detail.loc[:, original.columns], original)
    primary = detail[detail.primary_metric_included.eq("True")]
    assert len(primary) == 2992
    assert primary.context_schema_available.value_counts().to_dict() == {"True": 1846, "False": 1146}
    assert len(detail.loc[detail.context_schema_available.eq("False")]) == 1151
    assert set(primary["signal_date"].str[:6]) == {"202606", "202607", "202608", "202609"}
    target = detail.loc[detail.stock_id.eq("5904")].iloc[0]
    assert target["d20_return_pct"] == "-88.270677"
    assert target["d20_share_unit_return_pct"] == "17.293233"
    assert target["anomaly_disposition"] == "unresolved_anomaly_candidate"
    assert target["entry_date"] == "20260714" and target["d20_exit_date"] == "20260819"
    assert target["d5_share_factor"] == "1" and target["d10_share_factor"] == "1"


@pytest.mark.parametrize("column,value", [
    ("entry_date", "20260715"), ("d20_return_pct", "0"), ("d20_share_unit_return_pct", "0"),
    ("source_row_sha256", "0" * 64), ("snapshot_csv_row_number", "2"),
    ("primary_metric_included", "False"), ("stock_id", "9999"),
    ("formal_use_allowed", "True"), ("cash_flow_status", "complete"),
    ("anomaly_disposition", "verified_real_extreme"),
])
def test_comparison_original_cell_tamper_rejected(comparison_sources, comparison_bundle, column, value):
    detail = comparison_bundle[0].copy(deep=True)
    index = detail.index[detail.stock_id.eq("5904")][0]
    detail.at[index, column] = value
    with pytest.raises(ValueError, match="original frozen cells"):
        validator.verify_detail(comparison_sources, detail)


@pytest.mark.parametrize("column,where,value", [
    ("context_schema_available", "old", "True"), ("tdcc_positive_state", "old", "recorded_false"),
    ("obv_positive_state", "old", "recorded_false"), ("feature_return_20d", "old", "5"),
    ("feature_price_pullback_signal_date", "new", "20990101"),
    ("tdcc_positive_state", "unavailable", "recorded_false"),
    ("comparison_version", "old", "promoted"),
])
def test_comparison_joined_feature_tamper_rejected(comparison_sources, comparison_bundle, column, where, value):
    detail = comparison_bundle[0].copy(deep=True)
    if where == "unavailable":
        index = detail.index[detail.context_schema_available.eq("True") & detail.feature_price_pullback_tdcc_history_available.eq("False")][0]
    else:
        index = detail.index[detail.context_schema_available.eq("True" if where == "new" else "False")][0]
    detail.at[index, column] = value
    with pytest.raises(ValueError, match="published feature/state/date"):
        validator.verify_detail(comparison_sources, detail)


def test_comparison_source_and_snapshot_tamper_rejected(comparison_sources, comparison_bundle):
    sources = dict(comparison_sources)
    sources["detail"] += b"\n"
    with pytest.raises(ValueError, match="immutable source SHA"):
        validator.verify_detail(sources, comparison_bundle[0])
    sources = dict(comparison_sources)
    sources["snapshots"] = dict(sources["snapshots"])
    path = sorted(sources["snapshots"])[0]
    sources["snapshots"][path] += b"\n"
    with pytest.raises(ValueError, match="CSV row width|lineage SHA"):
        validator.verify_detail(sources, comparison_bundle[0])
    del sources["snapshots"][path]
    with pytest.raises(ValueError, match="snapshot population"):
        validator.verify_detail(sources, comparison_bundle[0])


def test_comparison_legacy_crlf_identity_is_not_guessed(comparison_sources):
    first = validator._csv(comparison_sources["detail"]).iloc[0]
    raw = comparison_sources["snapshots"][first.snapshot_path]
    lf = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    assert first.snapshot_sha256 == validator._sha(lf.replace(b"\n", b"\r\n"))
    assert first.snapshot_sha256 != validator._sha(lf)


@pytest.mark.parametrize("field,value", [
    ("signal_count", 2991), ("mature_count", 2240), ("win_count", 0),
    ("average_return_pct", "999"), ("median_return_pct", "999"),
    ("win_rate_pct", "100"), ("high_return_ge10_count", 0),
    ("tail_loss_le_minus10_rate_pct", "100"), ("unresolved_retained_count", 100),
    ("formal_use_allowed", "True"),
])
def test_comparison_summary_metrics_tamper_rejected(comparison_bundle, comparison_references, field, value):
    summary = comparison_bundle[1].copy(deep=True)
    summary.at[0, field] = value
    with pytest.raises(ValueError, match="summary"):
        validator._verify_table(summary, comparison_references[3], "summary")


def test_comparison_full_and_same_schema_denominators_are_separate(comparison_bundle, comparison_references):
    summary = comparison_bundle[1]
    subset = summary.loc[summary.period.eq("all") & summary.horizon.eq(5) & summary.metric_basis.eq("raw_primary")]
    assert int(subset.loc[subset.group_id.eq("baseline_all"), "signal_count"].iloc[0]) == 2992
    assert int(subset.loc[subset.group_id.eq("baseline_context_schema"), "signal_count"].iloc[0]) == 1846
    altered = summary.copy(deep=True)
    index = subset.index[subset.group_id.eq("baseline_context_schema")][0]
    altered.at[index, "signal_count"] = 2992
    with pytest.raises(ValueError, match="population"):
        validator._verify_table(altered, comparison_references[3], "summary")


def test_comparison_exhaustive_table_rows_and_order(comparison_bundle, comparison_references):
    for index, expected in ((1, comparison_references[3]), (2, comparison_references[4])):
        frame = comparison_bundle[index]
        with pytest.raises(ValueError, match="exhaustive"):
            validator._verify_table(frame.iloc[:-1], expected, "table")
        duplicate = frame.copy(deep=True)
        duplicate.iloc[1] = duplicate.iloc[0]
        with pytest.raises(ValueError, match="population"):
            validator._verify_table(duplicate, expected, "table")


@pytest.mark.parametrize("field,value", [
    ("state_count", 9999), ("band_count", 0), ("state_rate_pct", "100"),
    ("outcome_band", "cleaned"), ("feature_state", "verified_false"),
    ("promotion_evidence_allowed", "True"),
])
def test_comparison_feature_table_tamper_rejected(comparison_bundle, comparison_references, field, value):
    features = comparison_bundle[2].copy(deep=True)
    features.at[0, field] = value
    with pytest.raises(ValueError, match="features"):
        validator._verify_table(features, comparison_references[4], "features")


def test_comparison_unknown_and_recorded_false_are_not_equivalent():
    event = {"signal_date": "20260703"}
    row = {
        "return_20d": "10", "price_pullback_signal_date": "20260703",
        "price_pullback_tdcc_history_available": "False", "price_pullback_high_thresholds_up": "False",
        "price_pullback_obv_above_ma20": "False", "price_pullback_rsi14": "60", "price_pullback_macd_hist": "0.1",
    }
    fields = validator.feature_values(event, row, True)
    assert fields["tdcc_positive_state"] == "unknown"
    assert fields["obv_positive_state"] == "recorded_false"
    assert fields["technical_quality_state"] == "pass"
    row["price_pullback_tdcc_history_available"] = "True"
    assert validator.feature_values(event, row, True)["tdcc_positive_state"] == "recorded_false"
    row["price_pullback_obv_above_ma20"] = ""
    assert validator.feature_values(event, row, True)["obv_positive_state"] == "unknown"
    assert validator.feature_values(event, row, False)["technical_quality_state"] == "unknown"


@pytest.mark.parametrize("ret20,rsi,macd,expected", [
    ("5", "60", "0.000001", ("pass", "pass")),
    ("25", "60", "0", ("pass", "recorded_false")),
    ("25.000001", "59.999999", "1", ("recorded_false", "recorded_false")),
    ("4.999999", "", "1", ("recorded_false", "unknown")),
    ("NaN", "60", "NaN", ("unknown", "unknown")),
])
def test_comparison_feature_numeric_boundaries(ret20, rsi, macd, expected):
    row = dict(zip(validator.FEATURE_FIELDS, (ret20, "20260703", "True", "True", "True", rsi, macd)))
    result = validator.feature_values({"signal_date": "20260703"}, row, True)
    assert (result["ret20_5_25_state"], result["technical_quality_state"]) == expected


def test_comparison_return_thresholds_censoring_and_sensitivity_are_descriptive():
    rows = []
    for index, value in enumerate(("-10", "-0.000001", "0", "9.999999", "10")):
        rows.append({"stock_id": str(index), "signal_date": "20260703", "d5_maturity_status": "mature",
                     "d5_return_pct": value, "d5_share_unit_return_pct": value,
                     "d5_anomaly_candidate": "True" if index == 0 else "False",
                     "d5_comparison_anomaly_candidate": "True" if index == 0 else "False"})
    rows.append({"stock_id": "censored", "signal_date": "20260703", "d5_maturity_status": "not_mature",
                 "d5_return_pct": "", "d5_share_unit_return_pct": "", "d5_anomaly_candidate": "False",
                 "d5_comparison_anomaly_candidate": "False"})
    metrics = validator.return_metrics(rows, 5, "raw_primary")
    assert metrics["signal_count"] == 6 and metrics["mature_count"] == 5 and metrics["immature_count"] == 1
    assert metrics["win_count"] == 2 and metrics["neutral_count"] == 1 and metrics["failure_count"] == 2
    assert metrics["high_return_ge10_count"] == 1 and metrics["tail_loss_le_minus10_count"] == 1
    assert metrics["unresolved_retained_count"] == 1
    assert metrics["average_return_pct"] == Decimal("1.9999996")
    sensitivity = validator.return_metrics(rows, 5, "raw_original_candidate_exclusion_sensitivity")
    assert sensitivity["mature_count"] == 4 and sensitivity["excluded_candidate_count"] == 1
    assert validator.return_metrics(rows, 5, "partial_share_unit_supplement")["unresolved_retained_count"] == 1
    rows.append({"stock_id": "new-review", "signal_date": "20260703", "d5_maturity_status": "mature",
                 "d5_return_pct": "55", "d5_share_unit_return_pct": "55", "d5_anomaly_candidate": "False",
                 "d5_comparison_anomaly_candidate": "True"})
    sensitivity = validator.return_metrics(rows, 5, "raw_original_candidate_exclusion_sensitivity")
    assert sensitivity["mature_count"] == 5 and sensitivity["retained_review_candidate_count"] == 1


@pytest.mark.parametrize("key,value", [
    ("source_commit", "0" * 40), ("snapshot_commit", "0" * 40),
    ("formal_use_allowed", True), ("first_publication_pit_proven", True),
    ("total_return_complete", True), ("numerical_disposition_changed", True),
    ("context_schema_primary_count", 2992), ("non_overlapping_trades_proven", True),
])
def test_comparison_manifest_boundary_tamper_rejected(comparison_bundle, comparison_sources, comparison_references, monkeypatch, key, value):
    # Row/table checkers already have dedicated mutation tests. Isolate manifest pins here.
    rows, receipts, columns = comparison_references[:3]
    monkeypatch.setattr(validator, "verify_detail", lambda sources, detail: (rows, receipts, columns))
    monkeypatch.setattr(validator, "expected_tables", lambda rows: comparison_references[3:])
    monkeypatch.setattr(validator, "_verify_table", lambda *args: None)
    manifest = copy.deepcopy(comparison_bundle[3])
    manifest[key] = value
    with pytest.raises(ValueError, match="manifest immutable"):
        validator.validate_bundle(ROOT, *comparison_bundle[:3], manifest, sources=comparison_sources)


def test_comparison_validator_has_no_business_import():
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "__import__"}
    assert all(not module.startswith(("build_", "scripts", "model_", "price_pullback", "daily_model")) for module in imports)


def test_comparison_unsafe_source_paths_fail_closed():
    for path in ("../data.csv", "/data.csv", "data/../x.csv", "data\\x.csv", "-x"):
        with pytest.raises(ValueError, match="safe path"):
            validator._read_blob(ROOT, validator.SOURCE_COMMIT, path)
        with pytest.raises(RuntimeError, match="safe regular-blob"):
            producer.read_git_blob(ROOT, producer.SOURCE_COMMIT, path)


def test_comparison_actual_artifact_bytes_validate(comparison_sources, monkeypatch):
    monkeypatch.setattr(validator, "load_sources", lambda root: comparison_sources)
    result = validator.validate(ROOT)
    assert result["source_rows"] == 3020 and result["summary_rows"] == 630 and result["feature_rows"] == 4860


def test_comparison_new_anomaly_candidates_stay_primary(comparison_bundle, comparison_sources):
    detail, summary = comparison_bundle[:2]
    original = validator._csv(comparison_sources["detail"])
    for horizon in validator.HORIZONS:
        prefix = f"d{horizon}"
        pd.testing.assert_series_equal(detail[prefix + "_anomaly_candidate"], original[prefix + "_anomaly_candidate"])
        mask = detail[prefix + "_comparison_anomaly_candidate"].eq("True") & detail.primary_metric_included.eq("True")
        assert mask.any()
        assert set(detail.loc[mask, prefix + "_comparison_anomaly_disposition"]) == {"unresolved_anomaly_candidate"}
        baseline = summary.loc[summary.period.eq("all") & summary.horizon.eq(horizon) & summary.metric_basis.eq("raw_primary") & summary.group_id.eq("baseline_all")].iloc[0]
        assert int(baseline.retained_review_candidate_count) == int(mask.sum())
    candidate_index = detail.index[detail.d5_comparison_anomaly_candidate.eq("True")][0]
    changed = detail.copy(deep=True)
    changed.at[candidate_index, "d5_comparison_anomaly_disposition"] = "verified_real_extreme"
    with pytest.raises(ValueError, match="published feature/state/date"):
        validator.verify_detail(comparison_sources, changed)


def test_comparison_feature_denominators_include_same_schema_populations(comparison_bundle):
    features, summary = comparison_bundle[2], comparison_bundle[1]
    for population, group in (("all", "baseline_all"), ("context_schema", "baseline_context_schema"), ("tdcc_available", "baseline_tdcc_available")):
        selected = features.loc[features.period.eq("all") & features.horizon.eq(5) & features.metric_basis.eq("raw_primary")
                                & features.population_basis.eq(population) & features.feature.eq("tdcc_positive")]
        counts = selected.groupby("outcome_band").agg(band_count=("band_count", "first"), state_count=("state_count", "sum"))
        assert counts.band_count.tolist() == counts.state_count.tolist()
        reference = summary.loc[summary.period.eq("all") & summary.horizon.eq(5) & summary.metric_basis.eq("raw_primary") & summary.group_id.eq(group)].iloc[0]
        assert int(counts.band_count.sum()) == int(reference.mature_count)


def test_comparison_immutable_output_lf_rules():
    rules = set((ROOT / ".gitattributes").read_text(encoding="utf-8").splitlines())
    assert {path + " text eol=lf" for path in validator.OUTPUTS.values()}.issubset(rules)
