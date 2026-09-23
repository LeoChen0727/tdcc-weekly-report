from __future__ import annotations

import ast
import hashlib
from io import BytesIO
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

import build_revenue_unreacted_range_projection_v3 as producer
import validate_revenue_unreacted_range_projection_v3 as validator


def _csv(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _parse(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(BytesIO(payload), dtype=str, keep_default_na=False)


def _detail(rows) -> pd.DataFrame:
    result = []
    for key, stock, value, candidate in rows:
        row = dict.fromkeys(validator.replay.SOURCE_DETAIL_COLUMNS, "")
        row.update(
            generated_at="2026-09-23", episode_key=key, stock_id=stock,
            condition_variant_id="absolute_strong",
            monthly_revenue_history_blob_sha256="c" * 64,
            episode_status="launch_within_active_horizon",
            first_breakout_d20_return_pct=str(value),
            qualifying_source_revenue_anomaly_candidate_flag=str(candidate).lower(),
            unresolved_price_path_candidate_flag="false",
        )
        result.append(row)
    return pd.DataFrame(result, columns=validator.replay.SOURCE_DETAIL_COLUMNS)


@pytest.fixture
def synthetic_bundle(monkeypatch):
    old = _detail([("same", "1111", 10, False), ("removed", "2222", -5, False)])
    new = _detail([("same", "1111", 20, False), ("added", "3333", 100, True)])
    frame = pd.DataFrame([
        ["20260710", "10", "11", "9", "10", "100", "1"],
        ["20260713", "11", "12", "10", "11", "120", "1.2"],
    ], columns=validator.replay.PRICE_INPUT_COLUMNS)
    old_prices = {"1111": frame.iloc[1:].copy(), "2222": frame.copy()}
    new_prices = {"1111": frame.copy(), "2222": frame.copy()}
    fields = {
        "model_id": "revenue_unreacted_range", "artifact_version": validator.VERSION,
        "cutoff_date": validator.CUTOFF,
        "v2_source_commit": validator.V2_SOURCE_COMMIT,
        "v3_source_commit": validator.V3_SOURCE_COMMIT,
        "candidate_status": "not_adopted_pending_review",
        "historical_availability_status": "current_version_replay_not_first_publication_PIT",
        **validator.FLAGS,
    }
    monkeypatch.setattr(
        validator, "_source_evidence", lambda _root: (fields, old, new, old_prices, new_prices)
    )
    prices = producer.price_diff(old_prices, new_prices)
    episodes = producer.episode_diff(old, new)
    comparison = producer.comparison(old, new)
    artifacts = {
        validator.OUTPUTS["detail"]: _csv(new),
        validator.OUTPUTS["price_diff"]: _csv(prices),
        validator.OUTPUTS["episode_diff"]: _csv(episodes),
        validator.OUTPUTS["comparison"]: _csv(comparison),
        validator.OUTPUTS["report"]: producer.report(fields, prices, episodes, comparison),
    }
    manifest = {"generated_at": "2026-09-23T12:00:00+08:00", **fields}
    for name, relative in validator.OUTPUTS.items():
        if name != "manifest":
            manifest[name + "_bytes_sha256"] = hashlib.sha256(artifacts[relative]).hexdigest()
    artifacts[validator.OUTPUTS["manifest"]] = _csv(pd.DataFrame([manifest]))
    return artifacts, old, new, old_prices, new_prices


def _rebind(artifacts, name):
    manifest = _parse(artifacts[validator.OUTPUTS["manifest"]])
    manifest.loc[0, name + "_bytes_sha256"] = hashlib.sha256(artifacts[validator.OUTPUTS[name]]).hexdigest()
    artifacts[validator.OUTPUTS["manifest"]] = _csv(manifest)


def test_validator_has_no_producer_imports() -> None:
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imported = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    imported.update(alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names)
    assert "build_revenue_unreacted_range_projection_v3" not in imported
    assert "revenue_unreacted_range_source_first_condition_audit" not in imported
    assert "revenue_unreacted_range_source_snapshot_projection" not in imported


def test_independent_replay_diff_and_primary_sensitivity_contract(synthetic_bundle) -> None:
    artifacts, *_ = synthetic_bundle
    assert validator.validate(artifacts=artifacts) == []
    comparison = _parse(artifacts[validator.OUTPUTS["comparison"]])
    candidate = comparison.loc[comparison.source_version.eq("v3_candidate")]
    assert candidate.episode_count.tolist() == ["2", "1"]
    assert candidate.unresolved_candidate_count.tolist() == ["1", "0"]
    assert candidate.first_breakout_d20_mean_pct.tolist() == ["60.0", "20.0"]
    assert candidate.formal_model_use_allowed.tolist() == ["false", "false"]


@pytest.mark.parametrize("name", tuple(validator.OUTPUTS))
def test_missing_each_of_six_artifacts_fails_closed(synthetic_bundle, name) -> None:
    artifacts, *_ = synthetic_bundle
    del artifacts[validator.OUTPUTS[name]]
    assert validator.validate(artifacts=artifacts) == ["v3 requires exactly six declared artifacts"]


def test_default_validation_requires_physical_files(tmp_path) -> None:
    assert any("artifact is missing" in error for error in validator.validate(tmp_path))


@pytest.mark.parametrize("name", ["detail", "price_diff", "episode_diff", "comparison", "report"])
def test_artifact_byte_mutation_fails_before_source_replay(synthetic_bundle, monkeypatch, name) -> None:
    artifacts, *_ = synthetic_bundle
    artifacts[validator.OUTPUTS[name]] += b"\n"
    monkeypatch.setattr(validator, "_source_evidence", lambda _root: pytest.fail("tampered artifact reached replay"))
    assert any("bytes SHA-256 mismatch" in error for error in validator.validate(artifacts=artifacts))


@pytest.mark.parametrize("mutation", ["source", "flags", "detail", "price_diff", "episode_diff", "comparison", "report"])
def test_rebound_hashes_do_not_bypass_independent_evidence(synthetic_bundle, mutation) -> None:
    artifacts, *_ = synthetic_bundle
    name = "manifest" if mutation in {"source", "flags"} else mutation
    frame = None if name == "report" else _parse(artifacts[validator.OUTPUTS[name]])
    if mutation == "source":
        frame.loc[0, "v3_source_commit"] = "e" * 40
    elif mutation == "flags":
        frame.loc[0, "formal_model_use_allowed"] = "true"
    elif mutation == "detail":
        frame.loc[0, "first_breakout_d20_return_pct"] = "999"
    elif mutation in {"price_diff", "episode_diff"}:
        frame = frame.iloc[1:].copy()
    elif mutation == "comparison":
        frame.loc[0, "metric_basis"] = "corrected_primary"
    elif mutation == "report":
        artifacts[validator.OUTPUTS[name]] = artifacts[validator.OUTPUTS[name]].replace(
            "不是正式買賣策略的實現報酬或正式勝率".encode(), "正式勝率".encode()
        )
    if frame is not None:
        artifacts[validator.OUTPUTS[name]] = _csv(frame)
    if name != "manifest":
        _rebind(artifacts, name)
    assert validator.validate(artifacts=artifacts)


def test_independent_price_diff_distinguishes_format_from_economic_change(synthetic_bundle) -> None:
    _, _, _, old, _ = synthetic_bundle
    new = {stock: frame.copy() for stock, frame in old.items()}
    new["1111"]["close"] = "11.0"
    expected = validator._expected_price_diff(old, new).set_index("stock_id")
    assert expected.loc["1111", "change_class"] == "numeric_format_only"
    assert expected.loc["1111", "shared_raw_ohlcv_changed_date_count"] == 0
    new["1111"]["close"] = "12.0"
    expected = validator._expected_price_diff(old, new).set_index("stock_id")
    assert expected.loc["1111", "change_class"] == "shared_raw_ohlcv_changed_requires_review"
    assert expected.loc["1111", "shared_changed_date_count"] == 1


def test_bom_crlf_artifact_transport_preserves_serialized_hashes(synthetic_bundle) -> None:
    artifacts, *_ = synthetic_bundle
    transported = {path: b"\xef\xbb\xbf" + payload.replace(b"\n", b"\r\n") for path, payload in artifacts.items()}
    assert validator.validate(artifacts=transported) == []


def test_published_v3_candidate_passes_full_independent_replay() -> None:
    if not all((ROOT / relative).is_file() for relative in validator.OUTPUTS.values()):
        sparse = subprocess.run(
            ["git", "-C", str(ROOT), "config", "--bool", "core.sparseCheckout"],
            capture_output=True, text=True, check=False, timeout=30,
        )
        if sparse.returncode == 0 and sparse.stdout.strip() == "true":
            pytest.skip("sparse local checkout has no published v3 artifact family; not a full replay pass")
    assert validator.validate(ROOT) == []
