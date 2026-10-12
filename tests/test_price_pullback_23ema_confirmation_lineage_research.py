from __future__ import annotations

import ast
import csv
import io
import subprocess
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

import scripts.validate_price_pullback_23ema_confirmation_lineage_research as validator
import scripts.build_price_pullback_23ema_confirmation_lineage_research as research_writer


def dates(count=90):
    day = date(2026, 6, 5)
    result = []
    while len(result) < count:
        if day.weekday() < 5:
            result.append(day.strftime("%Y%m%d"))
        day += timedelta(days=1)
    return result


def frame(count=45):
    return pd.DataFrame({"date": dates(count), "open": [100.] * count,
                         "high": [110.] * count, "low": [90.] * count,
                         "close": [100.] * count, "ma20": [100.] * count,
                         "ema23": [100.] * count})


def encoded(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def test_target_is_strict_and_pending_cannot_use_future_open():
    prices = frame()
    prices.loc[21, "close"] = 110
    prices.loc[22, "close"] = 110.01
    prices.loc[23, "open"] = 117
    exact = validator.replay_position(prices, "20260703", prices.iloc[21]["date"])
    assert exact["state"] == "active_operation"
    pending = validator.replay_position(prices, "20260703", prices.iloc[22]["date"])
    assert pending["state"] == "target_exit_pending_next_open"
    assert pending["exit_price"] is None
    assert pending["exit_date"] == ""
    exited = validator.replay_position(prices, "20260703", prices.iloc[23]["date"])
    assert exited["exit_price"] == 117
    assert exited["exit_date"] == prices.iloc[23]["date"]


def test_stop_requires_four_consecutive_closes_and_next_open():
    prices = frame()
    prices.loc[21:24, "close"] = 96
    prices.loc[25, "open"] = 93
    early = validator.replay_position(prices, "20260703", prices.iloc[23]["date"])
    assert early["state"] == "active_operation"
    assert early["stop_confirmed_days"] == 3
    result = validator.replay_position(prices, "20260703", prices.iloc[25]["date"])
    assert result["exit_reason"] == validator.STOP_REASON
    assert result["confirmation_day"] == 4
    assert result["exit_price"] == 93


def test_target_has_priority_over_fourth_stop_close():
    prices = frame()
    prices.loc[:20, "high"] = 105
    prices.loc[:, ["ma20", "ema23"]] = 200
    prices.loc[21:23, "close"] = 104
    prices.loc[24, "close"] = 106
    result = validator.replay_position(prices, "20260703", prices.iloc[25]["date"])
    assert result["exit_reason"] == validator.TARGET_REASON
    assert result["confirmation_day"] == 4
    assert result["stop_confirmed_days"] == 3


def test_a_non_stop_close_resets_the_stop_streak():
    prices = frame()
    prices.loc[21:23, "close"] = 95
    prices.loc[24, "close"] = 100
    prices.loc[25:28, "close"] = 95
    result = validator.replay_position(prices, "20260703", prices.iloc[29]["date"])
    assert result["exit_reason"] == validator.STOP_REASON
    assert result["confirmation_day"] == 8


def test_d20_expiry_has_no_realized_price_or_close_exit():
    prices = frame()
    prices.loc[40, "close"] = 109
    result = validator.replay_position(prices, "20260703", prices.iloc[40]["date"])
    assert result["state"] == "expired_d20_no_active_tracking"
    assert result["exit_date"] == ""
    assert result["exit_reason"] == ""
    assert result["exit_price"] is None


def test_price_frame_recomputes_references_without_lookahead():
    raw = [{"date": d, "open": "100", "high": "110", "low": "90", "close": "100"}
           for d in dates(45)]
    raw[-1]["close"] = "500"
    computed = validator.price_frame(encoded(raw))
    assert computed.iloc[21]["ma20"] == 100
    assert pd.isna(computed.iloc[21]["ema23"])
    assert computed.iloc[22]["ema23"] == 100
    assert computed.iloc[40]["ema23"] == 100


def test_duplicate_price_source_dates_are_not_silently_deduplicated():
    row = {"date": "20260703", "open": "100", "high": "110", "low": "90", "close": "100"}
    with pytest.raises(ValueError, match="duplicate source stock/date"):
        validator.price_frame(encoded([row, row]))


def capture():
    return {"run_id": validator.CAPTURE_RUN_ID, "head_sha": validator.DECISION_REF,
            "server_created_at": validator.CAPTURE_CREATED_AT,
            "conclusion": "success", "status": "completed"}


def test_future_capture_cannot_be_called_pre_entry_evidence():
    bad = capture()
    bad["server_created_at"] = "2026-07-06T01:00:00Z"
    errors = validator.validate_capture(bad)
    assert any("before the next-open entry" in error for error in errors)


def test_capture_compares_independent_server_head_and_timestamp():
    server = {"id": validator.CAPTURE_RUN_ID, "head_sha": validator.DECISION_REF,
              "created_at": validator.CAPTURE_CREATED_AT,
              "conclusion": "success", "status": "completed"}
    assert validator.validate_capture(capture(), server_metadata=server) == []
    server["head_sha"] = "wrong-head"
    assert any("head_sha" in error for error in validator.validate_capture(capture(), server_metadata=server))


def corpus():
    confirmed, active, ranks, audits, research = [], [], [], [], []
    price = encoded([{k: str(v) for k, v in row.items()} for row in frame(90).drop(columns=["ma20", "ema23"]).to_dict("records")])
    for i in range(53):
        stock = str(2000 + i)
        line = "mainstream" if i < 15 else "non_mainstream"
        rank = i + 1 if i < 15 else i - 14
        key = {"model_id": validator.MODEL_ID, "signal_date": validator.SIGNAL_DATE,
               "stock_id": stock, "report_line": line}
        saved = {**key, "row_type": "data", "pdf_section": "confirmed_operation",
                 "operation_asof_date": validator.SIGNAL_DATE,
                 "row_action_status": "confirmed_buy_candidate", "buy_rank_eligible": "True",
                 "approved_for_daily": "True", "operation_module_approved_for_daily": "True",
                 "entry_date": "", "entry_price": "", "target_price": "110"}
        later = {**saved, "pdf_section": "active_operation", "operation_asof_date": validator.ACTIVE_DATE,
                 "row_action_status": "active_operation", "buy_rank_eligible": "False",
                 "entry_date": validator.ACTIVE_DATE, "entry_price": "100"}
        for view in ("highlight", "full"):
            confirmed.append({**saved, "pdf_view": view})
            active.append({**later, "pdf_view": view})
        ranks.append({**key, "model_rank": str(rank), "display_rank": str(rank), "model_rank_overall": str(rank)})
        audits.append({**key, "operation_asof_date": validator.TERMINAL_DATE,
                       "audit_status": "expired_d20_no_active_tracking", "exit_date": "", "exit_reason": ""})
    confirmed_raw, active_raw, rank_raw, audit_raw = map(encoded, (confirmed, active, ranks, audits))
    sources = {(validator.DECISION_REF, validator.SECTION_PATH): confirmed_raw,
               (validator.ACTIVE_REF, validator.SECTION_PATH): active_raw,
               (validator.DECISION_REF, validator.RANK_PATH): rank_raw,
               (validator.OUTCOME_REF, validator.AUDIT_PATH): audit_raw}
    saved_confirmed = validator.saved_sections(confirmed_raw, "confirmed_operation")
    saved_active = validator.saved_sections(active_raw, "active_operation")
    for rank, terminal in zip(ranks, audits):
        key = validator.identity(rank)
        stock = rank["stock_id"]
        sources[validator.ACTIVE_REF, f"data/stock_price_history/{stock}.csv"] = price
        sources[validator.OUTCOME_REF, f"data/stock_price_history/{stock}.csv"] = price
        sources[validator.DECISION_REF, f"data/stock_price_history/{stock}.csv"] = price
        research.append({**rank, "artifact_version": validator.VERSION, "confirmed_buy_rank_eligible": "True",
                         "confirmation_ref": validator.DECISION_REF,
                         "confirmation_artifact_sha256": validator.digest(confirmed_raw),
                         "confirmation_row_sha256": validator.canonical_row_sha256(saved_confirmed[key]),
                         "rank_source_sha256": validator.digest(rank_raw),
                         "rank_source_row_sha256": validator.canonical_row_sha256(rank),
                         "decision_price_sha256": validator.digest(price), "decision_target_price": "110",
                         "active_ref": validator.ACTIVE_REF,
                         "active_artifact_sha256": validator.digest(active_raw),
                         "active_row_sha256": validator.canonical_row_sha256(saved_active[key]),
                         "active_price_sha256": validator.digest(price),
                         "entry_date": validator.ACTIVE_DATE, "entry_price": "100",
                         "target_price": "110", "terminal_target_price": "110", "saved_active_state": "active_operation",
                         "replayed_active_state": "active_operation",
                         "terminal_ref": validator.OUTCOME_REF,
                         "terminal_artifact_sha256": validator.digest(audit_raw),
                         "terminal_row_sha256": validator.canonical_row_sha256(terminal),
                         "terminal_price_sha256": validator.digest(price),
                         "saved_terminal_state": "expired_d20_no_active_tracking",
                         "replayed_terminal_state": "expired_d20_no_active_tracking",
                         "exit_date": "", "exit_reason": "", "economic_unit_status": "unverified",
                         "return_evidence_allowed": "False", "promotion_allowed": "False",
                         "rule_lineage_status": "frozen_confirmed_active_terminal_rule_consistent"})
    return research, sources


def test_exact_saved_cohort_and_source_arithmetic_pass():
    research, sources = corpus()
    assert validator.validate_source_rows(research, sources) == []


def test_research_source_row_hash_tamper_is_detected():
    research, sources = corpus()
    research[0]["active_row_sha256"] = "forged"
    assert any("canonical source row SHA" in error for error in validator.validate_source_rows(research, sources))


def test_original_false_buy_rank_cannot_be_promoted_by_research_metadata():
    research, sources = corpus()
    changed = validator.csv_rows(sources[validator.DECISION_REF, validator.SECTION_PATH])
    for row in changed:
        if row["stock_id"] == research[0]["stock_id"]:
            row["buy_rank_eligible"] = "False"
    raw = encoded(changed)
    sources[validator.DECISION_REF, validator.SECTION_PATH] = raw
    origin = validator.saved_sections(raw, "confirmed_operation")[validator.identity(research[0])]
    for row in research:
        row["confirmation_artifact_sha256"] = validator.digest(raw)
    research[0]["confirmation_row_sha256"] = validator.canonical_row_sha256(origin)
    assert any("was not buy-rank eligible" in error for error in validator.validate_source_rows(research, sources))


def test_conflicting_saved_pdf_views_fail_instead_of_choosing_one():
    research, sources = corpus()
    changed = validator.csv_rows(sources[validator.ACTIVE_REF, validator.SECTION_PATH])
    changed[0]["entry_price"] = "500"
    with pytest.raises(ValueError, match="views conflict"):
        validator.saved_sections(encoded(changed), "active_operation")


def test_saved_model_rank_tamper_does_not_become_buy_rank_proof():
    research, sources = corpus()
    research[0]["model_rank"] = "280"
    assert any("saved ranking field model_rank" in error for error in validator.validate_source_rows(research, sources))


def test_expiry_cannot_gain_a_realized_price_or_promotion_claim():
    research, sources = corpus()
    research[0]["exit_price"] = "109"
    research[0]["return_evidence_allowed"] = "True"
    errors = validator.validate_source_rows(research, sources)
    assert any("D20 expiry" in error for error in errors)
    assert any("economic-return or promotion" in error for error in errors)


def test_validator_does_not_import_a_producer_or_production_business_module():
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not any(name.startswith("scripts.") or "build_price_pullback" in name or "build_daily" in name for name in imports)


def test_terminal_target_does_not_overwrite_the_saved_active_target():
    research, sources = corpus()
    research[0]["terminal_target_price"] = "500"
    assert any("terminal-version previous-20-high" in error for error in validator.validate_source_rows(research, sources))


def test_decision_target_cannot_silently_use_later_price_version():
    research, sources = corpus()
    research[0]["decision_target_price"] = "109"
    assert any("decision-version target" in error for error in validator.validate_source_rows(research, sources))


def test_git_source_bytes_are_bound_to_the_canonical_blob_hash(monkeypatch):
    raw = b"a\n"
    record = {"ref": validator.DECISION_REF, "path": validator.SECTION_PATH,
              "git_blob": "fixed-oid", "bytes": len(raw), "sha256": validator.digest(raw)}
    payload = b"fixed-oid blob 2\na\n\n"
    monkeypatch.setattr(validator.subprocess, "run", lambda *a, **k: SimpleNamespace(stdout=payload))
    assert validator.git_sources(Path("."), {"source_files": [record]})[validator.DECISION_REF, validator.SECTION_PATH] == raw
    payload = b"fixed-oid blob 2\nb\n\n"
    with pytest.raises(ValueError, match="canonical source bytes/hash mismatch"):
        validator.git_sources(Path("."), {"source_files": [record]})


def summary_fixture(research):
    counts = {"cohort_rows": len(research), "confirmed_buy_rank_eligible_rows": len(research),
              "matched_next_open_entry_rows": len(research), "source_row_hash_bound_rows": len(research),
              "return_evidence_allowed": "False", "promotion_allowed": "False"}
    for field, prefix in (("saved_active_state", "first_active_"),
                          ("saved_terminal_state", "terminal_"), ("report_line", "line_")):
        counts.update({prefix + name: count for name, count in Counter(r[field] for r in research).items()})
    return [{"metric": k, "value": str(v), "basis": validator.SUMMARY_BASIS} for k, v in counts.items()]


def test_summary_tamper_or_performance_expansion_is_rejected():
    research, _ = corpus()
    summary = summary_fixture(research)
    assert validator.validate_summary(research, summary) == []
    summary[0]["value"] = "54"
    assert any("cohort_rows" in error for error in validator.validate_summary(research, summary))
    summary = summary_fixture(research)
    summary.append({"metric": "corrected_avg_return", "value": "3.0", "basis": validator.SUMMARY_BASIS})
    assert any("performance claims" in error for error in validator.validate_summary(research, summary))


def registered_fake_repository(tmp_path):
    repo = tmp_path / "registration-fixture"
    config = repo / "config"
    config.mkdir(parents=True)
    owners, shares = [], []
    for name in research_writer.OUTPUT_NAMES:
        path = "output/research/price_pullback_23ema/" + name
        owners.append({"artifact_glob": path, "producer": research_writer.PRODUCER,
                       "owner_model_id": research_writer.OWNER_ID, "change_policy": "model_owned_write"})
        shares.append({"registered_producers": research_writer.PRODUCER, "producer_write_scope": path,
                       "approved_consumer_models": research_writer.MODEL_ID})
    (config / "model_research_artifact_ownership.csv").write_bytes(encoded(owners))
    (config / "daily_model_data_sharing_registry.csv").write_bytes(encoded(shares))
    return repo, owners, shares


@pytest.mark.parametrize("change", ["missing_family", "wrong_writer", "foreign_consumer"])
def test_research_writer_requires_exact_registered_family_writer_consumer(tmp_path, change):
    repo, owners, shares = registered_fake_repository(tmp_path)
    research_writer.require_registration(repo)
    if change == "missing_family":
        owners = owners[1:]
    elif change == "wrong_writer":
        owners[0]["producer"] = "scripts/foreign_research_writer.py"
    else:
        shares[0]["approved_consumer_models"] = "foreign_model"
    (repo / "config/model_research_artifact_ownership.csv").write_bytes(encoded(owners))
    (repo / "config/daily_model_data_sharing_registry.csv").write_bytes(encoded(shares))
    with pytest.raises(ValueError, match="unregistered"):
        research_writer.require_registration(repo)


def test_research_writer_refuses_existing_bundle_before_sources_or_network(tmp_path, monkeypatch):
    repo = tmp_path / "empty-repository"
    repo.mkdir()
    output = tmp_path / "already-published"
    output.mkdir()
    sentinel = output / "retained.csv"
    original = b"immutable existing evidence\n"
    sentinel.write_bytes(original)
    def forbidden(*args, **kwargs):
        pytest.fail("existing evidence refusal must precede registration, source build, and network")
    monkeypatch.setattr(research_writer, "require_registration", forbidden)
    monkeypatch.setattr(research_writer, "capture_metadata", forbidden)
    monkeypatch.setattr(research_writer, "build", forbidden)
    monkeypatch.setattr(sys, "argv", ["research-writer", "--repo-root", str(repo), "--output-root", str(output),
                                     "--decision-ref", validator.DECISION_REF, "--active-ref", validator.ACTIVE_REF,
                                     "--outcome-ref", validator.OUTCOME_REF, "--capture-run-id", str(validator.CAPTURE_RUN_ID)])
    with pytest.raises(ValueError, match="immutable research root is not empty"):
        research_writer.main()
    assert sentinel.read_bytes() == original
    assert list(output.iterdir()) == [sentinel]


def test_research_writer_protected_signature_detects_other_model_artifact_drift(tmp_path):
    repo = tmp_path / "tiny-git-fixture"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True, capture_output=True)
    other = repo / "output/research/foreign_model/evidence.csv"
    other.parent.mkdir(parents=True)
    other.write_bytes(b"value\n1\n")
    subprocess.run(["git", "-C", str(repo), "add", "--", "output/research/foreign_model/evidence.csv"],
                   check=True, capture_output=True)
    before = research_writer.protected_signature(repo)
    other.write_bytes(b"value\n2\n")
    assert research_writer.protected_signature(repo) != before
