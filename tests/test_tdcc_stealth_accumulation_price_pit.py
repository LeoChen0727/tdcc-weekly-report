from __future__ import annotations

import ast
import copy
import csv
import hashlib
import io
import sys
from types import SimpleNamespace
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_tdcc_stealth_accumulation_price_pit as validator  # noqa: E402


PIPELINE = "a" * 40
EARLIER = "b" * 40


def csv_bytes(rows: list[dict]) -> bytes:
    fields = list(dict.fromkeys(k for row in rows for k in row))
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


class MemorySources:
    def __init__(self):
        self.data = {}
        self.times = {PIPELINE: "2026-07-01T05:29:39Z", EARLIER: "2026-06-30T06:45:08Z"}

    def add(self, commit: str, path: str, rows: list[dict]) -> list[dict]:
        key = f"{commit}:{path}"
        self.data[key] = csv_bytes(rows)
        return [{"source": key, "row_number": i, "row": r, "row_sha256": validator.row_digest(r)} for i, r in enumerate(validator.parse_rows(self.data[key]), 2)]

    def read(self, key: str) -> bytes:
        return self.data[key]

    def rows(self, key: str) -> list[dict]:
        return validator.parse_rows(self.data[key])

    def paths(self, commit: str, prefix: str) -> list[str]:
        return [k.split(":", 1)[1] for k in self.data if k.startswith(f"{commit}:{prefix}/")]

    def commit_time(self, commit: str) -> str:
        return self.times[commit]

    def manifest(self) -> dict:
        result = {}
        for key, payload in self.data.items():
            commit, path = key.split(":", 1)
            result[key] = {"commit": commit, "path": path, "sha256": validator.digest(payload), "bytes": len(payload),
                           "git_blob_oid": hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest(),
                           "url": f"https://github.com/LeoChen0727/tdcc-weekly-report/blob/{commit}/{path}"}
        return result


def enum_fixture(explicit: bool = False):
    sources = MemorySources()
    stock = "3653" if explicit else "8358"
    category = "revenue_breakout_low_response" if explicit else "revenue_pullback"
    snapshot = {"stock_id": stock, "date": "20260717", "category": category,
                "tdcc_date": "20260703", "tdcc_accumulation_signal": "mild_accumulation"}
    candidate = {**snapshot, "tdcc_accumulation_signal": "mild_accumulation" if explicit else ""}
    if explicit:
        candidate.update(tdcc_400_change_sum="0.47", tdcc_1000_change_sum="0.89", tdcc_400_up_weeks="1", tdcc_1000_up_weeks="1", tdcc_weeks_used="3")
    candidate_ref = sources.add(PIPELINE, validator.CANDIDATE_PATHS[category], [candidate])[0]
    trend_ref = sources.add(PIPELINE, "output/latest/tdcc_trend_debug_latest.csv", [{"stock_id": stock,
        "tdcc_accumulation_signal": "distribution_warning" if explicit else "mild_accumulation",
        "tdcc_history_dates": "20260430,20260508,20260515"}])[0]
    chosen = candidate_ref if explicit else trend_ref
    functions = [{"source": f"{PIPELINE}:build_all_candidates_latest.py", "name": n}
                 for n in ("merge_tdcc", "merge_without_duplicate_columns", "infer_tdcc_signal_from_numbers", "deduplicate_candidates")]
    functions.append({"source": f"{PIPELINE}:tdcc_trend_utils.py", "name": "classify_accumulation"})
    lineage = {"candidate_source_row": candidate_ref, "trend_debug_row": trend_ref,
               "branch": "existing_candidate_enum_preserved" if explicit else "blank_candidate_enum_filled_from_trend_debug",
               "selected_source": chosen["source"], "selected_enum": "mild_accumulation", "snapshot_tdcc_date": "20260703",
               "enum_window_dates": trend_ref["row"]["tdcc_history_dates"], "producer_functions": functions,
               "runtime_invocation_evidence": "not_recorded", "event_time_availability": "unproven_original_input_filed_at_not_present"}
    if explicit:
        functions.extend([{"source": f"{PIPELINE}:tdcc_trend_utils.py", "name": "load_tdcc_history_trend"},
                          {"source": f"{PIPELINE}:build_revenue_breakout_low_response.py", "name": "build_revenue_breakout_low_response_candidates"}])
        history = []
        selected = []
        for date, p400, p1000 in (("20260618", "68.44", "58.89"), ("20260626", "67.90", "60.26"), ("20260703", "68.91", "59.78"), ("20260709", "1", "1")):
            path = f"output/history/tdcc/tdcc_holder_ratio_{date}.csv"
            ref = sources.add(PIPELINE, path, [{"date": date, "code": "0001" if date == "20260709" else stock, "over_400_pct": p400, "over_1000_pct": p1000}])[0]
            selected.append(path)
            if date != "20260709":
                history.append(ref)
        lineage.update(history_rows=history, selected_history_paths=selected, missing_history_dates=["20260709"], enum_window_dates="20260618,20260626,20260703")
        lineage["history_recomputed_metrics"] = {"tdcc_400_change_sum": "0.47", "tdcc_1000_change_sum": "0.89", "tdcc_400_up_weeks": 1, "tdcc_1000_up_weeks": 1}
    return sources, {"snapshot_row": {"row": snapshot}, "v2_detail": {"row": {"snapshot_pipeline_commit_sha": PIPELINE}},
                     "enum_lineage": lineage, "enum_source_branch": lineage["branch"], "enum_window_dates": lineage["enum_window_dates"]}


def test_validator_has_no_producer_or_business_imports():
    imports = [n for n in ast.walk(ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))) if isinstance(n, (ast.Import, ast.ImportFrom))]
    names = {n.module.split(".")[0] for n in imports if isinstance(n, ast.ImportFrom)}
    names |= {a.name.split(".")[0] for n in imports if isinstance(n, ast.Import) for a in n.names}
    assert names <= {"__future__", "argparse", "ast", "csv", "hashlib", "io", "json", "re", "subprocess", "collections", "datetime", "decimal", "pathlib"}


def test_producer_full_checkout_requires_registered_protected_sentinel_guard():
    source = (ROOT / "scripts/audit_tdcc_stealth_accumulation_price_pit.py").read_text(encoding="utf-8")
    guard = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == "output_guard")
    branch = next(n for n in guard.body if isinstance(n, ast.If))
    assert ast.unparse(branch.test) == "not sparse"
    call = branch.body[0].items[0].context_expr
    assert call.func.id == "model_owned_artifact_guard"
    assert {k.arg for k in call.keywords} == {"root", "registry_path", "sentinel_registry_path"}
    assert isinstance(branch.body[-1], ast.Return)
    assert any(isinstance(n, ast.Try) and n.finalbody for n in guard.body)


@pytest.mark.parametrize("field", ["sha256", "git_blob_oid", "bytes"])
def test_manifest_tampering_is_rejected(field):
    sources = MemorySources()
    sources.add(PIPELINE, "source.csv", [{"stock_id": "8358"}])
    manifest = sources.manifest()
    validator.verify_manifest(manifest, sources)
    manifest[next(iter(manifest))][field] = -1 if field == "bytes" else "0" * 64
    with pytest.raises(ValueError, match="mismatch"):
        validator.verify_manifest(manifest, sources)


@pytest.mark.parametrize("field,value", [("row_sha256", "0" * 64), ("row_number", 1), ("row", {"stock_id": "8261"})])
def test_nested_raw_row_tampering_is_rejected(field, value):
    sources = MemorySources()
    ref = sources.add(PIPELINE, "source.csv", [{"stock_id": "8358"}])[0]
    validator.verify_references({"nested": [ref]}, sources.manifest(), sources)
    ref[field] = value
    with pytest.raises(ValueError):
        validator.verify_references({"nested": [ref]}, sources.manifest(), sources)


def test_missing_required_enum_producer_function_fails():
    sources, record = enum_fixture()
    validator.verify_enum(record, sources)
    record["enum_lineage"]["producer_functions"] = [r for r in record["enum_lineage"]["producer_functions"] if r["name"] != "infer_tdcc_signal_from_numbers"]
    with pytest.raises(ValueError, match="missing required producer function"):
        validator.verify_enum(record, sources)


def test_3653_preserves_candidate_enum_despite_conflicting_debug():
    sources, record = enum_fixture(explicit=True)
    validator.verify_enum(record, sources)
    record["enum_lineage"]["selected_source"] = record["enum_lineage"]["trend_debug_row"]["source"]
    with pytest.raises(ValueError, match="enum selected source"):
        validator.verify_enum(record, sources)


def test_holder_date_cannot_replace_enum_history_window():
    sources, record = enum_fixture()
    record["enum_lineage"]["enum_window_dates"] = "20260703"
    record["enum_window_dates"] = "20260703"
    with pytest.raises(ValueError, match="history window"):
        validator.verify_enum(record, sources)


def test_explicit_history_does_not_invent_missing_stock_week():
    sources, record = enum_fixture(explicit=True)
    record["enum_lineage"]["missing_history_dates"] = []
    with pytest.raises(ValueError, match="missing TDCC history dates"):
        validator.verify_enum(record, sources)


def test_selector_difference_is_recomputed_not_trusted():
    record = {"pipeline_candidate_row": {"row": {"volume_ratio": "1.2"}}, "snapshot_row": {"row": {"volume_ratio": "1.3"}},
              "pipeline_selector_input_differences": {}, "selector_input_differences": 0, "pipeline_common_field_differences": {}}
    with pytest.raises(ValueError, match="selector input comparison"):
        validator.verify_selector_comparison(record, {"volume_ratio"})


def test_late_generated_metadata_does_not_imply_lookahead():
    sources = MemorySources()
    row = {"stock_id": "8358", "date": "20260630", "category": "revenue_pullback", "volume_ratio": "1.64"}
    earlier = sources.add(EARLIER, "output/latest/all_candidates_latest.csv", [row])[0]
    replay = {"snapshot_generated_at": "2026-07-01 13:49:33 Asia/Taipei", "entry_date": "20260701", "candidate_signal_date": "20260630", "snapshot_pipeline_commit_sha": PIPELINE}
    record = {"v2_detail": {"row": replay}, "snapshot_row": {"row": row}, "pipeline_commit_time": sources.times[PIPELINE], "generated_after_entry_open": True, "pipeline_after_entry_open": True,
              "pit": {"signal_close": "2026-06-30T13:30:00+08:00", "research_entry_open": "2026-07-01T09:00:00+08:00", "generated_after_signal_close": True,
                      "original_publication_time_proven": False, "metadata_is_first_publication_or_input_filed_at": False,
                      "earlier_selector_evidence": earlier, "matching_commit_time": sources.times[EARLIER], "matching_before_entry_open": True}}
    validator.verify_timing(record, sources, {"volume_ratio"})
    record["pit"]["original_publication_time_proven"] = True
    with pytest.raises(ValueError, match="metadata cannot prove"):
        validator.verify_timing(record, sources, {"volume_ratio"})


def test_population_keeps_cross_category_signal_weighting_separate():
    row = {"stock_id": "8358", "candidate_signal_date": "20260630", "snapshot_report_date": "20260630", "entry_date": "20260701",
           "snapshot_generated_at": "2026-07-01 08:30:00 Asia/Taipei", "snapshot_path": "snapshot.csv", "snapshot_row_number": "214"}
    rows = [row, {**row, "snapshot_row_number": "354"}]
    expected = validator.population_expected(rows)
    assert expected["generated_calendar_date_after_signal_date"] == 2
    assert expected["generated_after_entry_open"] == 0
    assert expected["same_stock_signal_duplicate_groups"] == 1 and expected["duplicate_group_rows"] == 2
    assert expected["snapshot_identity_duplicate_groups"] == 0
    expected["interpretation"] = "metadata_temporal_comparison_not_event_time_PIT_or_trade_eligibility_verdict"
    validator.verify_population(expected, rows)
    expected["interpretation"] = "confirmed_lookahead"
    with pytest.raises(ValueError, match="must not be a look-ahead verdict"):
        validator.verify_population(expected, rows)


def test_8358_two_categories_require_distinct_source_row_identity():
    sources = MemorySources()
    path = "output/history/daily_model_snapshots/all_candidates_20260630.csv"
    raw = [{"stock_id": "8358", "date": "20260630", "category": c} for c in ("revenue_pullback", "pullback_rebound")]
    refs = sources.add(validator.SOURCE_COMMIT, path, raw)
    pipeline = sources.add(PIPELINE, "output/latest/all_candidates_latest.csv", raw)[0]
    detail = [{"stock_id": "8358", "candidate_signal_date": "20260630", "snapshot_path": path, "snapshot_row_number": str(r["row_number"]),
               "snapshot_row_sha256": r["row_sha256"], "snapshot_sha256": validator.digest(sources.read(r["source"])), "snapshot_pipeline_commit_sha": PIPELINE} for r in refs]
    identities = [{k: r[k] for k in ("snapshot_path", "snapshot_row_number", "snapshot_row_sha256")} for r in detail]
    record = {"v2_detail": {"row": detail[0]}, "snapshot_row": refs[0], "pipeline_candidate_row": pipeline,
              "snapshot_digest_audit": validator.expected_snapshot_digest(sources.read(refs[0]["source"]), detail[0]["snapshot_sha256"]),
              "same_stock_signal_rows": 2, "same_stock_signal_identities": identities, "same_stock_signal_categories": "revenue_pullback;pullback_rebound"}
    validator.verify_identity(record, detail, sources)
    record["same_stock_signal_rows"] = 1
    with pytest.raises(ValueError, match="identity count"):
        validator.verify_identity(record, detail, sources)


def test_function_reference_is_checked_against_actual_source_segment():
    sources = MemorySources()
    key = f"{PIPELINE}:producer.py"
    sources.data[key] = b"def classify():\n    return 'mild'\n"
    ref = {"source": key, "name": "classify", "line": 1, "end_line": 2,
           "function_sha256": validator.digest(b"def classify():\n    return 'mild'")}
    validator.verify_references(ref, sources.manifest(), sources)
    ref["function_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="function hash"):
        validator.verify_references(ref, sources.manifest(), sources)


def test_csv_json_parity_rejects_performance_or_disposition_edit():
    observations = [{**dict.fromkeys(validator.CSV_FIELDS, ""), "observation_id": code, "stock_id": stock, "gross_return_pct": str(i), "disposition": "unresolved_anomaly_candidate", "retained_in_primary": True, "formal_use": False}
                    for i, (code, (stock, _)) in enumerate(validator.EXPECTED_OBSERVATIONS.items())]
    audit = {"observations": observations, "code_baseline_commit": PIPELINE}
    report = " ".join([validator.MODEL_ID, PIPELINE, validator.ARTIFACT_COMMIT, validator.SOURCE_COMMIT,
                       "unresolved_anomaly_candidate", "全部留在既有主結果", "不發布修正績效", "按訊號列加權", "不能直接認定前視偏誤",
                       "formal_operation_replay", "formal_use=False", "promotion_evidence_allowed=False", *[str(v) for r in observations for v in r.values()]])
    validator.verify_presentations(audit, csv_bytes(observations), report)
    corrupted = copy.deepcopy(observations)
    corrupted[0]["gross_return_pct"] = "99"
    with pytest.raises(ValueError, match="CSV/JSON"):
        validator.verify_presentations(audit, csv_bytes(corrupted), report)


def test_report_must_not_drop_the_unresolved_primary_conclusion():
    with pytest.raises(ValueError, match="report research conclusion missing"):
        rows = [{**dict.fromkeys(validator.CSV_FIELDS, ""), "observation_id": str(i), "gross_return_pct": "1", "disposition": "unresolved_anomaly_candidate", "retained_in_primary": True, "formal_use": False} for i in range(6)]
        validator.verify_presentations({"observations": rows, "code_baseline_commit": PIPELINE}, csv_bytes(rows), "已發布修正績效")


@pytest.mark.parametrize("corruption", ["missing_snapshot_row_number", "extra_column", "duplicate_column"])
def test_csv_requires_exact_complete_schema(corruption):
    rows = [{**dict.fromkeys(validator.CSV_FIELDS, ""), "observation_id": str(i)} for i in range(6)]
    if corruption == "missing_snapshot_row_number":
        for row in rows:
            del row["snapshot_row_number"]
    elif corruption == "extra_column":
        for row in rows:
            row["unexpected"] = ""
    payload = csv_bytes(rows)
    if corruption == "duplicate_column":
        payload = payload.replace(b"observation_id,", b"observation_id,observation_id,", 1)
    with pytest.raises(ValueError, match="exact column contract"):
        validator.verify_presentations({"observations": rows}, payload, "")


@pytest.mark.parametrize("status", ["pass", "verified", "verified_commit_row_lineage"])
def test_eight_checks_reject_overclaimed_external_status(status):
    record = {"disposition": "unresolved_anomaly_candidate", "retained_in_primary": True,
              "formal_use": False, "trade_eligible": False, "promotion_evidence_allowed": False,
              "checks": [{"check": n, "status": validator.EXPECTED_CHECK_STATUSES[n]} for n in validator.REQUIRED_CHECKS]}
    validator.verify_disposition(record)
    next(r for r in record["checks"] if r["check"] == "authoritative_business_event_history")["status"] = status
    with pytest.raises(ValueError, match="eight-check status/order"):
        validator.verify_disposition(record)


@pytest.mark.parametrize("changed", ["csv", "md"])
def test_companion_hash_tampering_is_rejected(changed):
    payloads = {"csv": b"original csv\n", "md": b"original report\n"}
    audit = {"companion_sha256": {k: validator.digest(v) for k, v in payloads.items()}}
    validator.verify_companions(audit, payloads["csv"], payloads["md"])
    payloads[changed] += b"tampered"
    with pytest.raises(ValueError, match="companion artifact hash"):
        validator.verify_companions(audit, payloads["csv"], payloads["md"])


def test_v2_digest_discrepancy_is_reproduced_without_changing_prices():
    row = {"stock_id": "8261", "entry_open_price": "176", "return_d10_pct": "85.795455",
           "large_return_observation_codes": "", "large_return_spotcheck_status": ""}
    old_digest = validator.digest(csv_bytes([row]))
    annotated = {**row, "large_return_observation_codes": "d10_max_observed_return", "large_return_spotcheck_status": "unresolved"}
    evidence = validator.embedded_digest_expected(csv_bytes([annotated]), [{"detail_artifact_sha256": old_digest}])
    assert evidence["embedded_hash_mismatch"] is True
    assert evidence["pre_observation_reconstruction_matches_embedded"] is True
    assert evidence["annotation_rows"] == 1 and evidence["old_artifact_modified"] is False
    changed_price = {**annotated, "entry_open_price": "177"}
    changed = validator.embedded_digest_expected(csv_bytes([changed_price]), [{"detail_artifact_sha256": old_digest}])
    assert changed["pre_observation_reconstruction_matches_embedded"] is False


def test_legacy_snapshot_crlf_digest_is_distinct_from_exact_raw_git_hash():
    raw = b"stock_id,price\n8261,176\n"
    recorded = validator.digest(raw.replace(b"\n", b"\r\n"))
    evidence = validator.expected_snapshot_digest(raw, recorded)
    assert evidence["matching_bases"] == ["crlf"]
    assert evidence["raw_bytes_match"] is False
    assert evidence["sha256_by_basis"]["raw_git_bytes"] == validator.digest(raw)
    with pytest.raises(ValueError, match="all declared line-ending bases"):
        validator.expected_snapshot_digest(raw.replace(b"176", b"177"), recorded)
    with pytest.raises(ValueError, match="all declared line-ending bases"):
        validator.expected_snapshot_digest(b"\xef\xbb\xbf" + raw, recorded)


@pytest.mark.parametrize("module_path", ["scripts/audit_tdcc_stealth_accumulation_price_pit.py", "scripts/validate_tdcc_stealth_accumulation_price_pit.py"])
@pytest.mark.parametrize("mutation", ["crlf_only", "modified_content", "added_bom", "untracked", "bare_cr"])
def test_checkout_transport_never_hides_uncommitted_content(module_path, mutation, tmp_path, monkeypatch):
    tree = ast.parse((ROOT / module_path).read_text(encoding="utf-8"))
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "read_audit_payload")
    namespace = {"Path": Path, "subprocess": validator.subprocess}
    exec(compile(ast.Module(body=[node], type_ignores=[]), module_path, "exec"), namespace)
    raw = b"stock_id,price\n8261,176\n"
    actual = raw.replace(b"\n", b"\r\n")
    if mutation == "modified_content":
        actual = actual.replace(b"176", b"177")
    elif mutation == "added_bom":
        actual = b"\xef\xbb\xbf" + actual
    elif mutation == "bare_cr":
        actual = raw.replace(b"\n", b"\r")
    (tmp_path / "audit.csv").write_bytes(actual)
    monkeypatch.setattr(validator.subprocess, "run", lambda *a, **k: SimpleNamespace(
        returncode=1 if mutation == "untracked" else 0, stdout=raw))
    observed = namespace["read_audit_payload"](tmp_path, "audit.csv")
    assert observed == (raw if mutation == "crlf_only" else actual)
