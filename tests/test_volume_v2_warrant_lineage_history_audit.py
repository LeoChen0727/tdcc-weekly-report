from __future__ import annotations

import sys
import subprocess
from decimal import Decimal
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_volume_v2_warrant_lineage_history_audit as builder  # noqa: E402
import validate_volume_v2_warrant_lineage_history_audit as validator  # noqa: E402


def test_canonical_text_sha_is_bom_and_line_ending_independent() -> None:
    lf = "欄位,值\n股票,2330\n".encode("utf-8")
    crlf_with_bom = b"\xef\xbb\xbf" + lf.replace(b"\n", b"\r\n")

    assert builder.sha256_bytes(lf) == builder.sha256_bytes(crlf_with_bom)
    assert validator.sha256_bytes(lf) == validator.sha256_bytes(crlf_with_bom)
    assert builder.sha256_bytes(lf) == validator.sha256_bytes(lf)
    assert not builder.manifest_v1_sha256_candidates(
        lf
    ) & builder.manifest_v1_sha256_candidates(crlf_with_bom)
    assert not validator.manifest_v1_sha256_candidates(
        lf
    ) & validator.manifest_v1_sha256_candidates(crlf_with_bom)


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.strip()


def _formal_frame(report_date: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "signal_date": report_date,
                "report_line": "mainstream",
                "model_id": "volume_range_breakout_v2_high_position_volume_attack",
                "stock_id": "2330",
                "source_row_index": "volume_breakout:0",
                "warrant_flow_signal": "",
                "base_model_score": "50.0",
                "operation_score": "0.0",
                "tdcc_score": "0.0",
                "pattern_score": "0.0",
                "risk_penalty": "0.0",
                "final_rank_score": "50.0",
                "model_rank": "1",
            }
        ]
    )


def _write_current_sources(
    root: Path,
    report_date: str,
    *,
    watch_score: str = "1",
    candidate_score: str = "1",
) -> None:
    latest = root / "output" / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    _formal_frame(report_date).to_csv(
        latest / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame(
        [
            {
                "signal_date": report_date,
                "stock_id": "2330",
                "warrant_flow_signal": "",
                "score": watch_score,
                "rank": "1",
                "tdcc_status": "",
                "false_breakout_risk": "False",
            }
        ]
    ).to_csv(
        latest / "volume_breakout_watch_latest.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "warrant_flow_signal": "",
                "score": candidate_score,
                "rank": "1",
            }
        ]
    ).to_csv(latest / "all_candidates_latest.csv", index=False, lineterminator="\n")
    pd.DataFrame([{"stock_id": "2330", "warrant_flow_signal": ""}]).to_csv(
        latest / "warrant_flow_latest.csv",
        index=False,
        lineterminator="\n",
    )


def _manifest_row(root: Path, report_date: str) -> dict[str, str]:
    snapshot_path = (
        "output/history/daily_model_snapshots/"
        f"daily_candidate_model_signals_for_report_{report_date}.csv"
    )
    payload = (root / snapshot_path).read_bytes()
    return {
        "snapshot_report_date": report_date,
        "pipeline_commit_sha": "0" * 40,
        "artifact_id": "model_signals_for_report",
        "source_path": builder.FORMAL_SOURCE_PATH,
        "snapshot_path": snapshot_path,
        "snapshot_sha256": sorted(builder.manifest_v1_sha256_candidates(payload))[0],
        "row_count": "1",
    }


def _setup_dynamic_repo(
    root: Path,
    *,
    current_watch_score: str = "1",
    current_candidate_score: str = "1",
) -> None:
    (root / "scripts").mkdir(parents=True)
    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    (root / builder.PRODUCTION_CODE_PATH).write_text(
        "def append_volume_breakout_signals():\n"
        "    score_source = {}\n"
        "    score_source.update(row.to_dict())\n"
        "    score_source['warrant_flow_signal'] = authoritative_warrant_signal\n",
        encoding="utf-8",
        newline="\n",
    )
    _write_current_sources(root, "20260717")
    _formal_frame("20260717").to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv",
        index=False,
        lineterminator="\n",
    )
    pd.DataFrame([_manifest_row(root, "20260717")]).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv",
        index=False,
        lineterminator="\n",
    )
    _git(root, "init")
    _git(root, "config", "user.name", "test")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "core.autocrlf", "false")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "historical snapshot")
    _write_current_sources(
        root,
        "20260718",
        watch_score=current_watch_score,
        candidate_score=current_candidate_score,
    )


def _validate_generated_audit(root: Path, audit: pd.DataFrame, target: Path) -> None:
    csv_path = target / "audit.csv"
    md_path = target / "audit.md"
    docs_csv_path = target / "audit-docs.csv"
    docs_md_path = target / "audit-docs.md"
    builder.write_audit_artifacts(
        audit,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert validator.validate(
        root,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    ) == []


def test_new_day_current_audit_transitions_to_immutable_history_with_parity(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)

    current = builder.build_audit_dataframe(root)
    current_row = current[current["snapshot_report_date"].eq("20260718")].iloc[0]
    assert current_row["paired_source_resolution"] == builder.CURRENT_SOURCE_RESOLUTION
    assert current_row["formal_row_disposition"] == "verified_clean"
    assert current_row["evidence_status"] == "complete"
    _validate_generated_audit(root, current, tmp_path / "current")

    snapshot_dir = root / "output" / "history" / "daily_model_snapshots"
    current_formal = root / builder.FORMAL_SOURCE_PATH
    published_snapshot = (
        snapshot_dir / "daily_candidate_model_signals_for_report_20260718.csv"
    )
    published_snapshot.write_bytes(current_formal.read_bytes())
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest = pd.concat(
        [manifest, pd.DataFrame([_manifest_row(root, "20260718")])],
        ignore_index=True,
    )
    manifest.to_csv(manifest_path, index=False, lineterminator="\n")

    pending = builder.build_audit_dataframe(root)
    pending_row = pending[pending["snapshot_report_date"].eq("20260718")].iloc[0]
    assert (
        pending_row["paired_source_resolution"]
        == builder.PUBLISHED_PENDING_SOURCE_RESOLUTION
    )
    _validate_generated_audit(root, pending, tmp_path / "pending")

    _git(root, "add", ".")
    _git(root, "commit", "-m", "publish new snapshot")
    historical = builder.build_audit_dataframe(root)
    historical_row = historical[
        historical["snapshot_report_date"].eq("20260718")
    ].iloc[0]
    assert historical_row["paired_source_resolution"] in {
        "manifest_pipeline_commit_exact_source_blob",
        "snapshot_history_exact_blob_fallback",
    }
    _validate_generated_audit(root, historical, tmp_path / "historical")

    parity_fields = (
        "formal_row_sha256",
        "watch_row_sha256",
        "candidate_row_sha256",
        "official_warrant_row_sha256",
        "production_code_sha256",
        "formal_snapshot_sha256",
        "watch_artifact_sha256",
        "candidate_artifact_sha256",
        "official_warrant_artifact_sha256",
        "formal_row_disposition",
        "evidence_status",
    )
    for field in parity_fields:
        assert current_row[field] == pending_row[field] == historical_row[field]


def test_quarantined_dynamic_audit_is_valid_evidence_artifact(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(
        root,
        current_watch_score="9",
        current_candidate_score="1",
    )

    audit = builder.build_audit_dataframe(root)
    row = audit[audit["snapshot_report_date"].eq("20260718")].iloc[0]
    assert row["formal_row_disposition"] == "quarantined"
    assert row["evidence_status"] == "complete"
    _validate_generated_audit(root, audit, tmp_path / "quarantined")


def test_unreplayable_dynamic_audit_is_valid_fail_closed_artifact(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    _setup_dynamic_repo(root)
    formal_path = root / builder.FORMAL_SOURCE_PATH
    formal = pd.read_csv(formal_path, dtype=str, keep_default_na=False)
    formal.loc[0, "final_rank_score"] = "not-a-number"
    formal.to_csv(formal_path, index=False, lineterminator="\n")

    audit = builder.build_audit_dataframe(root)
    row = audit[audit["snapshot_report_date"].eq("20260718")].iloc[0]
    assert row["formal_row_disposition"] == "unreplayable"
    assert row["evidence_status"] == "incomplete"
    _validate_generated_audit(root, audit, tmp_path / "unreplayable")


def test_builder_reconstructs_all_dynamic_volume_v2_sources(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    sources = builder.build_audit_sources(ROOT, builder.manifest_rows(ROOT))
    expected_dates = tuple(source["report_date"] for source in sources)
    expected_rows = sum(
        len(builder.volume_v2_formal_rows(source["formal_payload"], builder.FORMAL_SOURCE_PATH))
        for source in sources
    )

    assert len(audit) == expected_rows
    assert tuple(audit["snapshot_report_date"].drop_duplicates()) == expected_dates
    assert set(audit["formal_row_disposition"]) == {"verified_clean"}
    assert int(audit["watch_disposition"].eq("superseded_advisory_snapshot").sum()) == 1
    assert audit.loc[
        audit["candidate_row_present"].eq("False"), "counterfactual_score_context"
    ].eq("{}").all()
    assert audit.loc[
        audit["official_warrant_row_present"].eq("True"),
        "official_warrant_row_sha256",
    ].str.fullmatch(r"[0-9a-f]{64}").all()
    assert int(audit["watch_candidate_score_collision"].eq("True").sum()) == 0
    assert int(audit["watch_candidate_rank_collision"].eq("True").sum()) == 0
    assert set(audit["replay_status"]) == {"resolved"}
    assert set(audit["rank_replay_status"]) == {"resolved"}
    assert int(audit["formal_row_disposition"].eq("quarantined").sum()) == 0
    assert int(audit["formal_row_disposition"].eq("superseded").sum()) == 0
    absent = audit[audit["candidate_row_present"].eq("False")]
    assert set(absent["counterfactual_score_context"]) == {"{}"}
    rounding_gap = pd.to_numeric(
        audit["published_component_replay_rounding_gap"], errors="raise"
    ).abs()
    assert float(rounding_gap.max()) <= 0.3

    collision = audit[audit["watch_disposition"].eq("superseded_advisory_snapshot")].iloc[0]
    assert collision["snapshot_report_date"] == "20260716"
    assert collision["stock_id"] == "6505"
    assert collision["model_id"] == "volume_range_breakout_v2_high_position_volume_attack"
    assert collision["watch_warrant_signal"] == "call_put_bullish"
    assert collision["candidate_warrant_signal"] == "call_strong_inflow"
    assert collision["official_warrant_signal"] == "call_strong_inflow"
    assert collision["formal_warrant_signal"] == "call_strong_inflow"
    assert collision["watch_source_score"] == "99.0"
    assert collision["candidate_source_score"] == "99.0"
    assert collision["watch_source_rank"] == ""
    assert collision["candidate_source_rank"] == ""
    assert collision["collision_fields"] == "warrant_flow_signal"
    assert collision["published_counterfactual_collision_fields"] == ""
    assert collision["published_warrant_basis_signal"] == "call_strong_inflow"
    assert collision["warrant_bonus_points"] == "0"
    assert collision["base_model_score_delta"] == "0"
    assert collision["tdcc_score_delta"] == "0"
    assert collision["risk_penalty_delta"] == "0"
    assert collision["score_delta"] == "0"
    assert collision["rank_delta"] == "0"
    assert collision["published_final_rank_score"] == "73.0"
    assert collision["published_model_rank"] == "1"
    assert collision["formal_row_disposition"] == "verified_clean"
    assert collision["impact_scope"] == "watch_only_no_formal_score_or_rank_effect"

    output_csv = tmp_path / "output.csv"
    output_md = tmp_path / "output.md"
    docs_csv = tmp_path / "docs.csv"
    docs_md = tmp_path / "docs.md"
    builder.write_audit_artifacts(audit, output_csv, output_md, docs_csv, docs_md)

    assert output_csv.read_bytes() == docs_csv.read_bytes()
    assert output_md.read_bytes() == docs_md.read_bytes()


def test_dispatcher_source_mode_distinguishes_legacy_and_canonical_order() -> None:
    legacy = b"""
def append_volume_breakout_signals():
    score_source = {}
    score_source.update(row.to_dict())
"""
    canonical = b"""
def append_volume_breakout_signals():
    score_source = {}
    score_source.update(row.to_dict())
    score_source[\"warrant_flow_signal\"] = authoritative_warrant_signal
"""
    explicit_allowlist = b"""
def append_volume_breakout_signals():
    score_source = {field: candidate_values[field] for field in candidate_fields}
    score_source.update({field: watch_values[field] for field in watch_fields})
    score_source[\"warrant_flow_signal\"] = authoritative_warrant_signal
"""

    assert builder.dispatcher_warrant_source_mode(legacy) == "legacy_watch_overrides_candidate"
    assert (
        builder.dispatcher_warrant_source_mode(canonical)
        == "canonical_candidate_after_watch_merge"
    )
    assert (
        builder.dispatcher_warrant_source_mode(explicit_allowlist)
        == "canonical_candidate_explicit_allowlist"
    )


def test_three_collision_fields_replay_complete_component_delta() -> None:
    candidate = pd.Series(
        {
            "warrant_flow_signal": "no_signal",
            "tdcc_judgement": "mild_accumulation",
            "false_breakout_risk": "False",
        }
    )
    watch = pd.Series(
        {
            "warrant_flow_signal": "call_inflow",
            "tdcc_status": "distribution_warning",
            "false_breakout_risk": "True",
        }
    )
    published, canonical = builder.build_collision_contexts(
        candidate,
        watch,
        "legacy_watch_overrides_candidate",
    )
    formal = pd.Series(
        {
            "base_model_score": "62.0",
            "operation_score": "5.0",
            "tdcc_score": "3.0",
            "pattern_score": "4.0",
            "risk_penalty": "12.0",
            "final_rank_score": "62.0",
        }
    )

    replay = builder.replay_collision_components(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )
    independent = validator.independent_component_replay(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )

    assert builder.collision_field_names(published, canonical) == builder.COLLISION_FIELDS
    assert replay["counterfactual_base"] == Decimal("74")
    assert replay["counterfactual_tdcc"] == Decimal("7")
    assert replay["counterfactual_risk"] == Decimal("2")
    assert replay["counterfactual_final"] == Decimal("88")
    assert replay["final_delta"] == Decimal("26")
    assert independent["canonical_base"] == replay["counterfactual_base"]
    assert independent["canonical_tdcc"] == replay["counterfactual_tdcc"]
    assert independent["canonical_risk"] == replay["counterfactual_risk"]
    assert independent["canonical_final"] == replay["counterfactual_final"]


def test_component_replay_clamps_counterfactual_base_and_final() -> None:
    candidate = pd.Series({"tdcc_judgement": "mild_accumulation"})
    watch = pd.Series({"tdcc_status": "distribution_warning"})
    published, canonical = builder.build_collision_contexts(
        candidate,
        watch,
        "legacy_watch_overrides_candidate",
    )
    formal = pd.Series(
        {
            "base_model_score": "92.0",
            "operation_score": "0.0",
            "tdcc_score": "0.0",
            "pattern_score": "0.0",
            "risk_penalty": "6.0",
            "final_rank_score": "86.0",
        }
    )

    replay = builder.replay_collision_components(
        formal,
        "volume_range_breakout_v2_low_position_volume_attack",
        published,
        canonical,
    )

    assert replay["counterfactual_base"] == Decimal("100")
    assert replay["counterfactual_final"] == Decimal("100")


def test_counterfactual_rank_tie_break_ignores_published_rank() -> None:
    frame = pd.DataFrame(
        [
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "1",
                "stock_id": "6505",
                "source_row_index": "volume_breakout:9",
                "replay_status": "resolved",
            },
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "3",
                "stock_id": "2332",
                "source_row_index": "volume_breakout:8",
                "replay_status": "resolved",
            },
            {
                "counterfactual_final_rank_score": "80.0",
                "published_model_rank": "2",
                "stock_id": "2332",
                "source_row_index": "volume_breakout:2",
                "replay_status": "resolved",
            },
        ]
    )

    assert builder.counterfactual_rank_order(frame, frame.index) == [2, 1, 0]


def test_validator_accepts_fresh_deterministic_artifacts(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    _validate_generated_audit(ROOT, audit, tmp_path / "fresh")


def test_daily_model_pr_workflow_rebuilds_and_pins_history_audit() -> None:
    workflow = (
        ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml"
    ).read_text(encoding="utf-8")

    assert "python scripts/build_volume_v2_warrant_lineage_history_audit.py" in workflow
    assert "python scripts/validate_volume_v2_warrant_lineage_history_audit.py" in workflow
    assert "tests/test_volume_v2_warrant_lineage_history_audit.py" in workflow
    for governed_path in (
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "docs/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
        "docs/latest/volume_v2_warrant_lineage_history_audit_latest.md",
        "output/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
        "output/latest/volume_v2_warrant_lineage_history_audit_latest.md",
    ):
        assert governed_path in workflow


def test_production_workflows_build_current_audit_then_rebuild_after_snapshot_publish() -> None:
    build_command = "python scripts/build_volume_v2_warrant_lineage_history_audit.py"
    validate_command = "python scripts/validate_volume_v2_warrant_lineage_history_audit.py"
    publish_command = "python scripts/update_daily_published_model_snapshots.py"

    daily = (ROOT / ".github/workflows/daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    candidate_index = daily.index("python scripts/build_daily_candidate_model_layer.py")
    first_build = daily.index(build_command, candidate_index)
    first_validate = daily.index(validate_command, first_build)
    operation_index = daily.index(
        "python scripts/build_daily_volume_breakout_operation_section.py",
        first_validate,
    )
    publish_index = daily.index(publish_command, operation_index)
    second_build = daily.index(build_command, publish_index)
    second_validate = daily.index(validate_command, second_build)
    assert candidate_index < first_build < first_validate < operation_index
    assert publish_index < second_build < second_validate

    warrant = (ROOT / ".github/workflows/warrant_flow.yml").read_text(
        encoding="utf-8"
    )
    candidate_index = warrant.index("python scripts/build_daily_candidate_model_layer.py")
    first_build = warrant.index(build_command, candidate_index)
    first_validate = warrant.index(validate_command, first_build)
    publish_index = warrant.index(publish_command, first_validate)
    second_build = warrant.index(build_command, publish_index)
    second_validate = warrant.index(validate_command, second_build)
    assert candidate_index < first_build < first_validate < publish_index
    assert publish_index < second_build < second_validate
    assert "git add output/latest/volume_v2_warrant_lineage_history_audit_latest.*" in warrant
    assert "git add docs/latest/volume_v2_warrant_lineage_history_audit_latest.*" in warrant


def test_validator_rejects_tampered_formal_disposition(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    target = audit[
        audit["snapshot_report_date"].eq("20260716") & audit["stock_id"].eq("6505")
    ].index
    assert len(target) == 1
    audit.loc[target[0], "formal_row_disposition"] = "superseded"

    csv_path = tmp_path / "audit.csv"
    docs_csv_path = tmp_path / "audit_docs.csv"
    payload = audit.to_csv(index=False, lineterminator="\n").encode("utf-8")
    csv_path.write_bytes(payload)
    docs_csv_path.write_bytes(payload)
    md_path = tmp_path / "audit.md"
    docs_md_path = tmp_path / "audit_docs.md"
    md_payload = builder.render_markdown(builder.build_audit_dataframe(ROOT)).encode("utf-8")
    md_path.write_bytes(md_payload)
    docs_md_path.write_bytes(md_payload)

    errors = validator.validate(
        ROOT,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert any("formal_row_disposition mismatch" in error for error in errors)


def test_validator_rejects_tampered_component_replay(tmp_path: Path) -> None:
    audit = builder.build_audit_dataframe(ROOT)
    target = audit[
        audit["snapshot_report_date"].eq("20260716") & audit["stock_id"].eq("6505")
    ].index
    assert len(target) == 1
    audit.loc[target[0], "counterfactual_base_model_score"] = "999.0"

    csv_path = tmp_path / "audit.csv"
    docs_csv_path = tmp_path / "audit_docs.csv"
    payload = audit.to_csv(index=False, lineterminator="\n").encode("utf-8")
    csv_path.write_bytes(payload)
    docs_csv_path.write_bytes(payload)
    md_path = tmp_path / "audit.md"
    docs_md_path = tmp_path / "audit_docs.md"
    md_payload = builder.render_markdown(builder.build_audit_dataframe(ROOT)).encode("utf-8")
    md_path.write_bytes(md_payload)
    docs_md_path.write_bytes(md_payload)

    errors = validator.validate(
        ROOT,
        csv_path,
        md_path,
        docs_csv_path,
        docs_md_path,
    )
    assert any("counterfactual_base_model_score mismatch" in error for error in errors)
