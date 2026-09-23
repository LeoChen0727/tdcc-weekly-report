"""Independent validator tests plus mandatory real six-artifact regression."""
from __future__ import annotations

import ast
from copy import deepcopy
import csv
import gzip
import importlib.util
import io
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
STEM = "tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation"
sys.path.insert(0, str(ROOT / "scripts"))


def module(prefix):
    spec = importlib.util.spec_from_file_location("tdcc_ca_" + prefix + "_test", ROOT / f"scripts/{prefix}_{STEM}.py")
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


@pytest.fixture(scope="module")
def validator(): return module("validate")


@pytest.fixture
def synthetic(monkeypatch):
    p = module("build")
    cfg = p.load_contract(ROOT)
    trade = dict(profile="common_12", strategy="trend_8", partition="training", trade_id="synthetic:8422:D20:S0", signal_date="20251102", stock_id="8422", horizon="20", slippage_bps="0", entry_date="20251103", exit_date="20251201", shares="1000", entry_open="241.5", exit_close="23.9", entry_cash="241844.1375", net_return_pct="-90.181", primary_row_retained="True", anomaly_candidate="True", formal_use="False", promotion_evidence_allowed="False")
    raw = gzip.compress(p.csv_payload(list(trade), [trade]), mtime=0)
    cfg["source_trade_count"] = 1
    cfg["source_trades"] = {"path": "synthetic", "bytes": len(raw), "sha256": p.digest(raw)}
    monkeypatch.setattr(p, "load_contract", lambda root: cfg)
    monkeypatch.setattr(p, "source_trades", lambda *args: raw)
    return cfg, p.build(ROOT), raw


def rebind(payloads, name, data):
    result = dict(payloads); result[name] = data
    path = STEM + "_source_manifest_v1.json"
    manifest = json.loads(result[path])
    import hashlib
    manifest["artifacts"][name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    result[path] = json.dumps(manifest, ensure_ascii=False).encode("utf-8")
    return result


def mutate_csv(payloads, suffix, field, value):
    name = STEM + "_" + suffix
    compressed = suffix.endswith(".gz")
    raw = gzip.decompress(payloads[name]) if compressed else payloads[name]
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    rows = list(reader); rows[0][field] = value
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, reader.fieldnames, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    raw = out.getvalue().encode("utf-8")
    return rebind(payloads, name, gzip.compress(raw, mtime=0) if compressed else raw)


def test_independent_contract_verifies_archived_official_facts(validator):
    cfg = validator.contract(ROOT)
    assert cfg["events"][2]["share_factor"] == "0.27658171"


def test_validator_has_no_producer_or_business_function_import():
    tree = ast.parse((ROOT / f"scripts/validate_{STEM}.py").read_text(encoding="utf-8"))
    imports = [a.name for node in ast.walk(tree) if isinstance(node, ast.Import) for a in node.names]
    imports += [node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    assert all(not name.startswith(("build_", "scripts.build_", "daily_candidate", "model_")) for name in imports)


def test_synthetic_artifacts_independently_reconcile(validator, synthetic):
    cfg, payloads, raw = synthetic
    assert validator.validate_payloads(ROOT, cfg, payloads, raw) == 1


@pytest.mark.parametrize("field,value", [("theoretical_exit_shares", "1000"), ("known_action_gross_price_proxy_pct", "100"), ("known_action_costed_proxy_pct", "0"), ("verified_total_return_pct", "0"), ("corporate_action_coverage_complete", "True"), ("entry_date", "20251104"), ("anomaly_candidate", "False"), ("source_trade_row_sha256", "0" * 64)])
def test_rehashed_semantic_tamper_rejected(validator, synthetic, field, value):
    cfg, payloads, raw = synthetic
    bad = mutate_csv(payloads, "positions_v1.csv.gz", field, value)
    with pytest.raises(ValueError): validator.validate_payloads(ROOT, cfg, bad, raw)


def test_summary_wrong_denominator_and_lost_blocked_row_rejected(validator, synthetic):
    cfg, payloads, raw = synthetic
    bad = mutate_csv(payloads, "summary_v1.csv", "theoretical_gross_proxy_samples", "2")
    with pytest.raises(ValueError, match="summary"):
        validator.validate_payloads(ROOT, cfg, bad, raw)
    name = STEM + "_blocked_v1.csv.gz"
    header = gzip.decompress(payloads[name]).splitlines(keepends=True)[0]
    bad = rebind(payloads, name, gzip.compress(header, mtime=0))
    with pytest.raises(ValueError, match="rows"):
        validator.validate_payloads(ROOT, cfg, bad, raw)


def test_source_artifact_and_report_tamper_rejected(validator, synthetic):
    cfg, payloads, raw = synthetic
    with pytest.raises(ValueError, match="source bytes"):
        validator.validate_payloads(ROOT, cfg, payloads, raw + b"x")
    bad = dict(payloads); bad[STEM + "_report_v1.md"] += b"changed"
    with pytest.raises(ValueError, match="binding"):
        validator.validate_payloads(ROOT, cfg, bad, raw)
    name = STEM + "_report_v1.md"
    with pytest.raises(ValueError, match="caveats"):
        validator.validate_payloads(ROOT, cfg, rebind(payloads, name, b"success"), raw)


def test_missing_extra_artifacts_and_duplicate_json_fail_closed(validator, synthetic):
    cfg, payloads, raw = synthetic
    for bad in ({k: v for k, v in payloads.items() if not k.endswith("report_v1.md")}, {**payloads, "other.csv": b"x"}):
        with pytest.raises(ValueError, match="six"):
            validator.validate_payloads(ROOT, cfg, bad, raw)
    with pytest.raises(ValueError, match="duplicate"):
        validator.read_json(b'{"a":1,"a":1}')


@pytest.mark.parametrize("contradiction", ["pit", "formal"])
def test_rehashed_report_with_retained_keywords_cannot_reverse_conclusion(validator, synthetic, contradiction):
    cfg, payloads, raw = synthetic
    name = STEM + "_report_v1.md"
    prose = payloads[name].decode("utf-8")
    changed = prose.replace("不證明首次發布 PIT", "已證明首次發布 PIT") if contradiction == "pit" else prose + "\n此模型已正式可用。\n"
    with pytest.raises(ValueError, match="approved narrative"):
        validator.validate_payloads(ROOT, cfg, rebind(payloads, name, changed.encode("utf-8")), raw)


def test_published_six_full_frozen_trade_population_is_mandatory(validator):
    # No skip: repository PR/main CI must contain all six published artifacts.
    assert validator.validate(ROOT) == 305673
