from __future__ import annotations

import hashlib
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_daily_published_model_snapshots as update_snapshots  # noqa: E402
import validate_daily_published_model_snapshots as validate_snapshots  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def rewrite_with_crlf(path: Path) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))


def repository_file(repository_root: Path, path_text: object) -> Path:
    path = Path(str(path_text))
    return path if path.is_absolute() else repository_root / path


def write_minimal_latest_artifacts(latest_dir: Path, report_date: str = "20260615") -> None:
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": report_date,
                "report_ready": "True",
                "warrant_ready": "True",
                "warrant_source_status": "ok",
                "warrant_daily_publish_allowed": "True",
                "warrant_pdf_visibility": "visible",
                "warrant_model_effect_allowed": "True",
                "warrant_pdf_effect_allowed": "True",
                "daily_pdf_ready": "True",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        [
            {
                "signal_date": report_date,
                "stock_id": "6153",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_score": "70.0",
                "base_model_score": "55.0",
                "operation_score": "6.0",
                "tdcc_score": "4.0",
                "pattern_score": "8.0",
                "risk_penalty": "3.0",
                "final_rank_score": "70.0",
                "rank_reason_zh": "test evidence",
            }
        ],
    )
    write_csv(
        latest_dir / "all_candidates_latest.csv",
        [
            {
                "date": report_date,
                "signal_date": report_date,
                "main_price_date": report_date,
                "stock_id": "6153",
                "stock_name": "test stock",
                "category": "pattern",
                "candidate_source_type": "individual_quality_candidate",
                "candidate_line": "pattern_watch",
                "candidate_line_group": "individual_pattern_watch",
                "source_row_index": "0",
                "close": "101",
                "ema23": "100",
                "ma20": "100",
                "distance_to_ema23_pct": "1.0",
                "gap_ema23_pct": "1.0",
                "platform_low": "95",
                "short_platform_low": "96",
                "previous_20d_low": "94",
                "low_20": "94",
                "ma5_turning_up_flag": "False",
                "ma10_turning_up_flag": "False",
                "volume_ratio": "1.2",
                "return_20d": "5.0",
                "latest_revenue_yoy": "10.0",
                "cumulative_revenue_yoy": "8.0",
                "off_60d_low_pct": "12.0",
                "tdcc_judgement": "mild_accumulation",
                "tdcc_accumulation_signal": "True",
                "warrant_flow_signal": "neutral",
                "false_breakout_risk": "False",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_summary_for_report_latest.csv",
        [
            {
                "signal_date": report_date,
                "report_line": "mainstream",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_report_model_registry_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_registry_order": "1",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_candidate_model_parameters_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_volume_breakout_operation_section_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "buy_rank_eligible": "False",
                "operation_asof_date": report_date,
                "selected_trigger_id": "",
                "operation_score": "6.0",
                "tdcc_score": "4.0",
                "pattern_score": "8.0",
                "risk_penalty": "3.0",
                "final_rank_score": "70.0",
                "entry_rule_id": "pending_confirmation",
                "stop_loss_rule_id": "signal_low_stop_after_confirmation",
                "stop_loss_price": "",
                "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
                "planned_holding_days": "10",
            }
        ],
    )
    write_csv(
        latest_dir / "daily_volume_breakout_operation_evidence_audit_latest.csv",
        [
            {
                "model_id": "volume_range_breakout",
                "operation_asof_date": report_date,
                "stock_id": "6153",
                "signal_date": report_date,
                "selected_trigger_id": "",
                "selected_confirmation_date": "",
                "operation_lifecycle_state": "pending_confirmation",
                "audit_status": "candidate_evaluated",
                "included_in_daily_adapter": "False",
                "tdcc_list_type": "",
                "rank_bucket": "",
                "classification_id": "",
                "attack_method": "",
                "price_position_type": "",
                "evidence_confluence_scope": "",
                "evidence_confluence_id": "",
                "evidence_sample_size": "",
                "evidence_win_rate": "",
                "evidence_avg_return": "",
                "evidence_median_return": "",
                "evidence_out_of_sample_pass": "",
                "ranking_research_score": "",
                "reason": "",
                "generated_at": "2026-06-16 08:00:00 Asia/Taipei",
            }
        ],
    )
    for name, model_id in [
        ("daily_w_bottom_right_side_operation_section_latest.csv", "w_bottom_right_side"),
        (
            "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
            "neckline_volume_breakout_confirmation",
        ),
    ]:
        write_csv(
            latest_dir / name,
            [
                {
                    "model_id": model_id,
                    "pdf_view": "highlight",
                    "pdf_section": "confirmed_operation",
                    "row_type": "empty_state",
                    "buy_rank_eligible": "False",
                    "row_action_status": "empty_state",
                    "entry_rule_id": "right_low_signal_next_open"
                    if model_id == "w_bottom_right_side"
                    else "close_ge_1pct_within_3_sessions_next_open",
                    "stop_loss_rule_id": "w_structure_low_close_stop"
                    if model_id == "w_bottom_right_side"
                    else "no_fixed_stop_loss_20d_operation_rule",
                    "stop_loss_price": "",
                    "exit_rule_id": "d20_gain10_else_d40_close"
                    if model_id == "w_bottom_right_side"
                    else "tp10_close_win_5pct_pullback_neutral_else_20d_close_loss",
                    "planned_holding_days": "40" if model_id == "w_bottom_right_side" else "20",
                }
            ],
        )


def test_daily_published_model_snapshot_builder_and_validator_use_report_date(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    manifest_rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    assert set(manifest_rows["artifact_id"]) == {
        "all_candidates_source_rows",
        "data_freshness",
        "model_parameters",
        "model_registry",
        "model_signals_for_report",
        "model_summary_for_report",
        "neckline_volume_breakout_confirmation_operation_section",
        "volume_breakout_operation_evidence_audit",
        "volume_breakout_operation_section",
        "w_bottom_right_side_operation_section",
    }
    assert set(manifest_rows["snapshot_report_date"]) == {"20260615"}
    assert set(manifest_rows["snapshot_revision"]) == {"r1"}
    assert set(manifest_rows["supersedes_snapshot_sha256"]) == {""}
    assert set(manifest_rows["revision_reason"]) == {"initial_publish"}
    assert all(
        not Path(value).is_absolute()
        and "\\" not in str(value)
        and str(value).startswith("output/latest/")
        for value in manifest_rows["source_path"]
    )
    assert all(
        not Path(value).is_absolute()
        and "\\" not in str(value)
        and str(value).startswith("output/history/daily_model_snapshots/")
        for value in manifest_rows["snapshot_path"]
    )
    signal_row = manifest_rows[
        manifest_rows["artifact_id"].eq("model_signals_for_report")
    ].iloc[0]
    candidate_row = manifest_rows[
        manifest_rows["artifact_id"].eq("all_candidates_source_rows")
    ].iloc[0]
    assert Path(signal_row["snapshot_path"]).name == (
        "daily_candidate_model_signals_for_report_20260615_r1_"
        f"{signal_row['snapshot_sha256'][:12]}.csv"
    )
    assert Path(candidate_row["snapshot_path"]).name == (
        f"all_candidates_20260615_r1_{candidate_row['snapshot_sha256'][:12]}.csv"
    )
    assert repository_file(tmp_path, signal_row["snapshot_path"]).exists()
    assert repository_file(tmp_path, candidate_row["snapshot_path"]).exists()
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_warrant_formal_sync_updates_only_selected_snapshot_families(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"
    selected_ids = {
        "data_freshness",
        "model_signals_for_report",
        "all_candidates_source_rows",
        "model_summary_for_report",
    }
    protected_ids = {
        "model_registry",
        "model_parameters",
        "volume_breakout_operation_section",
        "volume_breakout_operation_evidence_audit",
        "w_bottom_right_side_operation_section",
        "neckline_volume_breakout_confirmation_operation_section",
    }
    write_minimal_latest_artifacts(latest_dir, report_date=report_date)
    initial_manifest = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="full-build-sha",
    )
    manifest_before = pd.read_csv(manifest_path, dtype=str).fillna("")
    protected_before = (
        manifest_before[manifest_before["artifact_id"].isin(protected_ids)]
        .sort_values("artifact_id")
        .reset_index(drop=True)
    )
    protected_snapshot_bytes = {
        row["artifact_id"]: repository_file(tmp_path, row["snapshot_path"]).read_bytes()
        for _, row in protected_before.iterrows()
    }
    selected_r1_paths = {
        row["artifact_id"]: repository_file(tmp_path, row["snapshot_path"])
        for _, row in manifest_before[manifest_before["artifact_id"].isin(selected_ids)].iterrows()
    }
    selected_r1_bytes = {
        artifact_id: path.read_bytes() for artifact_id, path in selected_r1_paths.items()
    }

    freshness = pd.read_csv(latest_dir / "data_freshness_latest.csv", dtype=str)
    freshness.loc[0, "warrant_source_status"] = "ok_refreshed"
    freshness.to_csv(
        latest_dir / "data_freshness_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    signals = pd.read_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv", dtype=str
    )
    signals.loc[0, "model_score"] = "72.0"
    signals.to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    candidates = pd.read_csv(latest_dir / "all_candidates_latest.csv", dtype=str)
    candidates.loc[0, "warrant_flow_signal"] = "call_inflow"
    candidates.to_csv(
        latest_dir / "all_candidates_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    summary = pd.read_csv(
        latest_dir / "daily_candidate_model_summary_for_report_latest.csv", dtype=str
    )
    summary.loc[0, "model_name_zh"] = "放量攻擊模型正式同步"
    summary.to_csv(
        latest_dir / "daily_candidate_model_summary_for_report_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    manifest_rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="warrant-formal-sync-sha",
        artifact_ids=selected_ids,
        revision_reason="warrant_formal_sync",
    )

    assert set(manifest_rows["artifact_id"]) == selected_ids
    assert set(manifest_rows["snapshot_revision"]) == {"r2"}
    assert set(manifest_rows["revision_reason"]) == {"warrant_formal_sync"}
    manifest_after = pd.read_csv(manifest_path, dtype=str).fillna("")
    selected_after = manifest_after[manifest_after["artifact_id"].isin(selected_ids)]
    assert len(selected_after) == len(selected_ids) * 2
    assert set(selected_after["snapshot_revision"]) == {"r1", "r2"}
    protected_after = (
        manifest_after[manifest_after["artifact_id"].isin(protected_ids)]
        .sort_values("artifact_id")
        .reset_index(drop=True)
    )
    pd.testing.assert_frame_equal(protected_before, protected_after)
    for _, row in protected_after.iterrows():
        assert repository_file(tmp_path, row["snapshot_path"]).read_bytes() == (
            protected_snapshot_bytes[row["artifact_id"]]
        )
    for artifact_id, path in selected_r1_paths.items():
        assert path.exists()
        assert path.read_bytes() == selected_r1_bytes[artifact_id]
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_targeted_snapshot_selection_fails_closed_on_empty_or_unknown_ids(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    write_minimal_latest_artifacts(latest_dir)

    with pytest.raises(RuntimeError, match="selection must not be empty"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "output" / "history" / "daily_model_snapshots",
            manifest_path=(
                tmp_path
                / "output"
                / "history"
                / "daily_model_snapshots"
                / "daily_published_model_snapshot_manifest.csv"
            ),
            artifact_ids=set(),
        )
    with pytest.raises(RuntimeError, match="unknown daily snapshot artifact ids"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "history",
            manifest_path=tmp_path / "history" / "manifest.csv",
            artifact_ids={"not_registered"},
        )


@pytest.mark.parametrize(
    ("manifest_payload", "expected_message"),
    [
        (b"\xff\xfe\x00\x00", "manifest is unreadable"),
        (
            (",".join(update_snapshots.MANIFEST_COLUMNS) + "\n").encode("utf-8"),
            "manifest has no data rows",
        ),
    ],
)
def test_existing_unreadable_or_header_only_manifest_fails_without_lineage_loss(
    tmp_path: Path,
    manifest_payload: bytes,
    expected_message: str,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    protected_snapshot = snapshot_dir / "data_freshness_20260614.csv"
    protected_snapshot.write_bytes(b"immutable historical payload\n")
    manifest_path.write_bytes(manifest_payload)
    before_files = {
        path.name: path.read_bytes()
        for path in snapshot_dir.iterdir()
        if path.is_file()
    }

    with pytest.raises(RuntimeError, match=expected_message):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
        )

    after_files = {
        path.name: path.read_bytes()
        for path in snapshot_dir.iterdir()
        if path.is_file()
    }
    assert after_files == before_files
    assert not update_snapshots.manifest_publication_lock_path(manifest_path).exists()
    assert not list(snapshot_dir.glob(".*.tmp"))


@pytest.mark.parametrize("removed_column", ["row_count", "revision_reason"])
def test_existing_manifest_with_unapproved_partial_schema_fails_without_rewrite(
    tmp_path: Path,
    removed_column: str,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
    )

    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    assert removed_column in manifest.columns
    manifest.drop(columns=[removed_column]).to_csv(
        manifest_path,
        index=False,
        lineterminator="\n",
    )
    corrupted_manifest = manifest_path.read_bytes()
    before_snapshots = {
        path.name: path.read_bytes()
        for path in snapshot_dir.glob("*.csv")
        if path != manifest_path
    }

    with pytest.raises(RuntimeError, match="unapproved daily snapshot manifest schema"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
        )

    assert manifest_path.read_bytes() == corrupted_manifest
    assert {
        path.name: path.read_bytes()
        for path in snapshot_dir.glob("*.csv")
        if path != manifest_path
    } == before_snapshots
    assert not update_snapshots.manifest_publication_lock_path(manifest_path).exists()
    assert not list(snapshot_dir.glob(".*.tmp"))


def test_manifest_lock_collision_fails_closed_and_keeps_unknown_lock(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    lock_path = update_snapshots.manifest_publication_lock_path(manifest_path)
    unknown_lock = b"unknown stale or concurrent owner\n"
    lock_path.write_bytes(unknown_lock)

    with pytest.raises(RuntimeError, match="publication lock already exists"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
        )

    assert lock_path.read_bytes() == unknown_lock
    assert not manifest_path.exists()
    assert not list(snapshot_dir.glob("data_freshness_20260615_r1_*.csv"))
    assert not list(snapshot_dir.glob(".*.tmp"))


def test_manifest_cas_detects_bypass_writer_and_rolls_back_promoted_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    external_manifest = b"external writer bypassed publication lock\n"
    real_replace = update_snapshots.os.replace
    injected = False

    def replace_then_mutate_manifest(source: Path | str, target: Path | str) -> None:
        nonlocal injected
        real_replace(source, target)
        target_path = Path(target)
        if (
            not injected
            and target_path != manifest_path
            and target_path.name.startswith("data_freshness_20260615_r1_")
        ):
            injected = True
            manifest_path.write_bytes(external_manifest)

    monkeypatch.setattr(update_snapshots.os, "replace", replace_then_mutate_manifest)
    with pytest.raises(RuntimeError, match="manifest changed since planning"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
        )

    assert injected
    assert manifest_path.read_bytes() == external_manifest
    assert not list(snapshot_dir.glob("data_freshness_20260615_r1_*.csv"))
    assert not update_snapshots.manifest_publication_lock_path(manifest_path).exists()
    assert not list(snapshot_dir.glob(".*.tmp"))


def test_targeted_snapshot_sync_does_not_repair_excluded_operation_drift(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir)
    initial_manifest = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="full-build-sha",
    )
    target = repository_file(
        tmp_path,
        initial_manifest[
            initial_manifest["artifact_id"].eq("volume_breakout_operation_section")
        ].iloc[0]["snapshot_path"]
    )
    target_before = target.read_bytes()
    operation_source = latest_dir / "daily_volume_breakout_operation_section_latest.csv"
    operation = pd.read_csv(operation_source, dtype=str)
    operation.loc[0, "model_id"] = "drifted_operation_model"
    operation.to_csv(
        operation_source,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="warrant-formal-sync-sha",
        artifact_ids={"data_freshness"},
    )

    assert target.read_bytes() == target_before
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )


def test_targeted_snapshot_sync_preserves_protected_legacy_manifest_identity(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    initial_manifest = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="full-build-sha",
    )

    protected_id = "volume_breakout_operation_section"
    protected_row = initial_manifest[
        initial_manifest["artifact_id"].eq(protected_id)
    ].iloc[0]
    protected_snapshot = repository_file(tmp_path, protected_row["snapshot_path"])
    protected_snapshot_before = protected_snapshot.read_bytes()

    legacy_manifest = pd.read_csv(
        manifest_path,
        dtype=str,
        keep_default_na=False,
    ).drop(columns=list(update_snapshots.REVISION_MANIFEST_COLUMNS))
    protected_mask = legacy_manifest["artifact_id"].eq(protected_id)
    legacy_manifest.loc[
        protected_mask,
        list(update_snapshots.WARRANT_LINEAGE_MANIFEST_COLUMNS),
    ] = ""
    legacy_manifest.to_csv(
        manifest_path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    canonical_before = update_snapshots.normalize_known_manifest_schema(
        pd.read_csv(manifest_path, dtype=str, keep_default_na=False),
        context="test legacy mature manifest before targeted sync",
    )
    protected_before = canonical_before[
        canonical_before["artifact_id"].eq(protected_id)
    ].to_dict("records")

    freshness_path = latest_dir / "data_freshness_latest.csv"
    freshness = pd.read_csv(freshness_path, dtype=str, keep_default_na=False)
    freshness.loc[0, "warrant_source_status"] = "ok_revised"
    freshness.to_csv(
        freshness_path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="warrant-formal-sync-sha",
        artifact_ids={"data_freshness"},
        revision_reason="warrant_formal_sync",
    )

    current_manifest = pd.read_csv(
        manifest_path,
        dtype=str,
        keep_default_na=False,
    )
    protected_after = current_manifest[
        current_manifest["artifact_id"].eq(protected_id)
    ].to_dict("records")
    assert protected_after == protected_before
    assert protected_snapshot.read_bytes() == protected_snapshot_before
    assert list(current_manifest.columns) == update_snapshots.MANIFEST_COLUMNS
    assert len(current_manifest) == len(initial_manifest) + 1
    selected_revisions = current_manifest[
        current_manifest["artifact_id"].eq("data_freshness")
    ]["snapshot_revision"].tolist()
    assert selected_revisions == ["r1", "r2"]


def test_current_manifest_blank_warrant_lineage_is_not_legacy_defaulted() -> None:
    row = {column: "" for column in update_snapshots.MANIFEST_COLUMNS}
    row.update(
        {
            "snapshot_report_date": "20260615",
            "snapshot_revision": "r1",
            "revision_reason": "initial_publish",
            "warrant_ready": "True",
            "artifact_id": "volume_breakout_operation_section",
        }
    )

    normalized = update_snapshots.normalize_known_manifest_schema(
        pd.DataFrame([row], columns=update_snapshots.MANIFEST_COLUMNS),
        context="test current mature manifest blank lineage",
    )

    for column in update_snapshots.WARRANT_LINEAGE_MANIFEST_COLUMNS:
        assert normalized.iloc[0][column] == ""


def test_daily_published_model_snapshot_hashes_tolerate_windows_crlf_checkout(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    manifest = pd.read_csv(manifest_path, dtype=str)
    for _, row in manifest.iterrows():
        rewrite_with_crlf(repository_file(tmp_path, row["source_path"]))
        rewrite_with_crlf(repository_file(tmp_path, row["snapshot_path"]))

    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_legacy_crlf_raw_manifest_hash_is_preserved_and_reused_from_lf_checkout(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    freshness_mask = manifest["artifact_id"].eq("data_freshness")
    row = manifest.loc[freshness_mask].iloc[0]
    versioned_path = repository_file(tmp_path, row["snapshot_path"])
    artifact = update_snapshots.ARTIFACTS_BY_ID["data_freshness"]
    legacy_path = snapshot_dir / update_snapshots.legacy_snapshot_name(
        artifact,
        "20260615",
    )
    versioned_path.replace(legacy_path)
    lf_payload = legacy_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    legacy_crlf_hash = hashlib.sha256(lf_payload.replace(b"\n", b"\r\n")).hexdigest()
    manifest.loc[freshness_mask, "snapshot_path"] = legacy_path.as_posix()
    manifest.loc[freshness_mask, "source_sha256"] = legacy_crlf_hash
    manifest.loc[freshness_mask, "snapshot_sha256"] = legacy_crlf_hash
    manifest.loc[freshness_mask, "revision_reason"] = (
        update_snapshots.LEGACY_REVISION_REASON
    )
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []
    reused = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
    )
    assert reused.iloc[0]["snapshot_revision"] == "r1"
    assert reused.iloc[0]["snapshot_sha256"] == legacy_crlf_hash
    assert repository_file(tmp_path, reused.iloc[0]["snapshot_path"]) == legacy_path


def test_daily_published_model_snapshot_builder_requires_reason_before_writing_r2(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    initial = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    section_path = latest_dir / "daily_volume_breakout_operation_section_latest.csv"
    section = pd.read_csv(section_path, dtype=str)
    section.loc[0, "stock_id"] = "9999"
    section.to_csv(section_path, index=False, encoding="utf-8", lineterminator="\n")

    manifest_before = manifest_path.read_bytes()
    snapshot_paths_before = sorted(path.name for path in snapshot_dir.glob("*.csv"))
    with pytest.raises(RuntimeError, match="revision_reason is required"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            generated_at="2026-06-16 09:00:00 Asia/Taipei",
            commit_sha="test-sha-2",
        )
    assert manifest_path.read_bytes() == manifest_before
    assert sorted(path.name for path in snapshot_dir.glob("*.csv")) == snapshot_paths_before

    revised = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        revision_reason="explicit_operation_correction",
    )
    initial_row = initial[
        initial["artifact_id"].eq("volume_breakout_operation_section")
    ].iloc[0]
    revised_row = revised[
        revised["artifact_id"].eq("volume_breakout_operation_section")
    ].iloc[0]
    assert revised_row["snapshot_revision"] == "r2"
    assert revised_row["supersedes_snapshot_sha256"] == initial_row["snapshot_sha256"]
    assert repository_file(tmp_path, initial_row["snapshot_path"]).exists()
    assert Path(initial_row["snapshot_path"]) != Path(revised_row["snapshot_path"])
    assert pd.read_csv(
        repository_file(tmp_path, revised_row["snapshot_path"]), dtype=str
    ).loc[0, "stock_id"] == "9999"


def test_snapshot_publish_copy_failure_leaves_no_final_or_temporary_orphan(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    original_copyfile = update_snapshots.shutil.copyfile
    copy_count = 0

    def fail_second_copy(source: Path, target: Path) -> str:
        nonlocal copy_count
        copy_count += 1
        if copy_count == 2:
            raise OSError("injected snapshot copy failure")
        return original_copyfile(source, target)

    monkeypatch.setattr(update_snapshots.shutil, "copyfile", fail_second_copy)
    with pytest.raises(OSError, match="injected snapshot copy failure"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )

    assert not manifest_path.exists()
    assert list(snapshot_dir.glob("*.csv")) == []
    assert list(snapshot_dir.glob("*.tmp")) == []
    assert not update_snapshots.manifest_publication_lock_path(manifest_path).exists()


def test_snapshot_publish_manifest_replace_failure_rolls_back_promoted_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    original_replace = update_snapshots.os.replace

    def fail_manifest_replace(source: Path, target: Path) -> None:
        if Path(target) == manifest_path:
            raise OSError("injected manifest replace failure")
        original_replace(source, target)

    monkeypatch.setattr(update_snapshots.os, "replace", fail_manifest_replace)
    with pytest.raises(OSError, match="injected manifest replace failure"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )

    assert not manifest_path.exists()
    assert list(snapshot_dir.glob("*.csv")) == []
    assert list(snapshot_dir.glob("*.tmp")) == []
    assert not update_snapshots.manifest_publication_lock_path(manifest_path).exists()


def test_daily_published_model_snapshot_builder_appends_status_revision_idempotently(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")

    initial = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    freshness_path = latest_dir / "data_freshness_latest.csv"
    freshness = pd.read_csv(freshness_path, dtype=str)
    freshness.loc[0, "warrant_source_status"] = "ok_refreshed"
    freshness.to_csv(freshness_path, index=False, encoding="utf-8", lineterminator="\n")

    revised = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
        revision_reason="warrant_formal_sync",
    )

    initial_row = initial[initial["artifact_id"].eq("data_freshness")].iloc[0]
    revised_row = revised.iloc[0]
    assert revised_row["snapshot_revision"] == "r2"
    assert revised_row["supersedes_snapshot_sha256"] == initial_row["snapshot_sha256"]
    assert revised_row["revision_reason"] == "warrant_formal_sync"
    assert pd.read_csv(repository_file(tmp_path, initial_row["snapshot_path"]), dtype=str).loc[
        0, "warrant_source_status"
    ] == "ok"
    assert pd.read_csv(repository_file(tmp_path, revised_row["snapshot_path"]), dtype=str).loc[
        0, "warrant_source_status"
    ] == "ok_refreshed"

    manifest_before_idempotent = manifest_path.read_bytes()
    repeated = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 10:00:00 Asia/Taipei",
        commit_sha="test-sha-3",
        artifact_ids={"data_freshness"},
    )
    assert repeated.iloc[0]["snapshot_revision"] == "r2"
    assert manifest_path.read_bytes() == manifest_before_idempotent


def test_legacy_v1_manifest_is_normalized_without_moving_or_overwriting_snapshot(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"
    write_minimal_latest_artifacts(latest_dir, report_date=report_date)
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    legacy_paths: dict[str, Path] = {}
    for index, row in manifest.iterrows():
        artifact = update_snapshots.ARTIFACTS_BY_ID[row["artifact_id"]]
        legacy_path = snapshot_dir / update_snapshots.legacy_snapshot_name(
            artifact,
            report_date,
        )
        repository_file(tmp_path, row["snapshot_path"]).replace(legacy_path)
        manifest.loc[index, "snapshot_path"] = legacy_path.as_posix()
        legacy_paths[row["artifact_id"]] = legacy_path
    manifest = manifest.drop(
        columns=[
            "snapshot_revision",
            "supersedes_snapshot_sha256",
            "revision_reason",
        ]
    )
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    legacy_freshness_bytes = legacy_paths["data_freshness"].read_bytes()

    reused = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
    )
    assert reused.iloc[0]["snapshot_revision"] == "r1"
    assert reused.iloc[0]["revision_reason"] == "legacy_v1_manifest"
    assert repository_file(tmp_path, reused.iloc[0]["snapshot_path"]) == (
        legacy_paths["data_freshness"]
    )
    assert legacy_paths["data_freshness"].read_bytes() == legacy_freshness_bytes

    freshness_path = latest_dir / "data_freshness_latest.csv"
    freshness = pd.read_csv(freshness_path, dtype=str)
    freshness.loc[0, "warrant_source_status"] = "ok_revised"
    freshness.to_csv(freshness_path, index=False, encoding="utf-8", lineterminator="\n")
    revised = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 10:00:00 Asia/Taipei",
        commit_sha="test-sha-3",
        artifact_ids={"data_freshness"},
        revision_reason="warrant_formal_sync",
    )
    assert revised.iloc[0]["snapshot_revision"] == "r2"
    assert revised.iloc[0]["supersedes_snapshot_sha256"] == reused.iloc[0][
        "snapshot_sha256"
    ]
    assert legacy_paths["data_freshness"].read_bytes() == legacy_freshness_bytes
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_snapshot_validator_rejects_revision_gap_and_broken_supersedes_chain(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    freshness_path = latest_dir / "data_freshness_latest.csv"
    freshness = pd.read_csv(freshness_path, dtype=str)
    freshness.loc[0, "warrant_source_status"] = "ok_revised"
    freshness.to_csv(freshness_path, index=False, encoding="utf-8", lineterminator="\n")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
        revision_reason="warrant_formal_sync",
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    r2_mask = manifest["artifact_id"].eq("data_freshness") & manifest[
        "snapshot_revision"
    ].eq("r2")
    manifest.loc[r2_mask, "snapshot_revision"] = "r3"
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    gap_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("revision sequence must be continuous" in error for error in gap_errors)

    manifest.loc[r2_mask, "snapshot_revision"] = "r2"
    manifest.loc[r2_mask, "supersedes_snapshot_sha256"] = "0" * 64
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    chain_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("must equal the prior revision" in error for error in chain_errors)

    r1_sha = manifest.loc[
        manifest["artifact_id"].eq("data_freshness")
        & manifest["snapshot_revision"].eq("r1"),
        "snapshot_sha256",
    ].iloc[0]
    manifest.loc[r2_mask, "supersedes_snapshot_sha256"] = r1_sha
    manifest.loc[r2_mask, "revision_reason"] = ""
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    reason_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("revision_reason is required" in error for error in reason_errors)


def test_snapshot_validator_checks_all_revision_hashes_and_current_max_revision(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    initial = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    freshness_path = latest_dir / "data_freshness_latest.csv"
    freshness = pd.read_csv(freshness_path, dtype=str)
    freshness.loc[0, "warrant_source_status"] = "ok_revised"
    freshness.to_csv(freshness_path, index=False, encoding="utf-8", lineterminator="\n")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
        revision_reason="warrant_formal_sync",
    )
    initial_freshness = initial[initial["artifact_id"].eq("data_freshness")].iloc[0]
    initial_freshness_path = repository_file(
        tmp_path, initial_freshness["snapshot_path"]
    )
    initial_payload = initial_freshness_path.read_bytes()
    initial_freshness_path.write_text(
        "tampered\n",
        encoding="utf-8",
    )
    errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("r1: snapshot_sha256 does not match snapshot file" in error for error in errors)

    initial_freshness_path.write_bytes(initial_payload)
    current = pd.read_csv(freshness_path, dtype=str)
    current.loc[0, "warrant_source_status"] = "unpublished_drift"
    current.to_csv(freshness_path, index=False, encoding="utf-8", lineterminator="\n")
    errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("max revision does not match current source" in error for error in errors)


def test_snapshot_validator_does_not_apply_current_schema_to_historical_revision(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    historical_mask = manifest["artifact_id"].eq("model_signals_for_report")
    historical_row = manifest.loc[historical_mask].iloc[0]
    versioned_path = repository_file(tmp_path, historical_row["snapshot_path"])
    historical = pd.read_csv(versioned_path, dtype=str)
    historical = historical.drop(columns=["base_model_score"])
    artifact = update_snapshots.ARTIFACTS_BY_ID["model_signals_for_report"]
    legacy_path = snapshot_dir / update_snapshots.legacy_snapshot_name(
        artifact,
        "20260615",
    )
    historical.to_csv(legacy_path, index=False, encoding="utf-8", lineterminator="\n")
    versioned_path.unlink()
    historical_hash = update_snapshots.sha256_file(legacy_path)
    manifest.loc[historical_mask, "snapshot_path"] = legacy_path.as_posix()
    manifest.loc[historical_mask, "snapshot_sha256"] = historical_hash
    manifest.loc[historical_mask, "source_sha256"] = historical_hash
    manifest.loc[historical_mask, "row_count"] = str(len(historical))
    manifest.loc[historical_mask, "column_count"] = str(len(historical.columns))
    manifest.loc[historical_mask, "revision_reason"] = (
        update_snapshots.LEGACY_REVISION_REASON
    )
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    write_minimal_latest_artifacts(latest_dir, report_date="20260616")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-17 08:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
    )

    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_snapshot_validator_rejects_unreferenced_versioned_file(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    signal_row = rows[rows["artifact_id"].eq("model_signals_for_report")].iloc[0]
    source = repository_file(tmp_path, signal_row["snapshot_path"])
    orphan = snapshot_dir / (
        "daily_candidate_model_signals_for_report_20260615_"
        f"r99_{signal_row['snapshot_sha256'][:12]}.csv"
    )
    orphan.write_bytes(source.read_bytes())

    errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any(
        "unreferenced versioned daily snapshot file is forbidden" in error
        and orphan.as_posix() in error
        for error in errors
    )


def test_snapshot_cli_accepts_revision_reason() -> None:
    args = update_snapshots.parse_args(
        ["--artifact-id", "data_freshness", "--revision-reason", "warrant_formal_sync"]
    )
    assert args.artifact_id == ["data_freshness"]
    assert args.revision_reason == "warrant_formal_sync"


def test_daily_published_model_snapshot_builder_rejects_not_ready_freshness(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "warrant_ready": "False",
                "warrant_source_status": "failed",
                "warrant_daily_publish_allowed": "False",
                "warrant_pdf_visibility": "blocked_unavailable",
                "warrant_model_effect_allowed": "False",
                "warrant_pdf_effect_allowed": "False",
                "daily_pdf_ready": "True",
            }
        ],
    )

    with pytest.raises(RuntimeError, match="warrant_ready must be True before publishing model snapshots"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "history",
            manifest_path=tmp_path / "history" / "manifest.csv",
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )


def test_daily_published_model_snapshot_builder_allows_bounded_warrant_grace(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    write_csv(
        latest_dir / "data_freshness_latest.csv",
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "warrant_ready": "False",
                "warrant_source_status": "warning_grace",
                "warrant_daily_publish_allowed": "True",
                "warrant_pdf_visibility": "hidden_unavailable",
                "warrant_model_effect_allowed": "False",
                "warrant_pdf_effect_allowed": "False",
                "daily_pdf_ready": "True",
            }
        ],
    )

    manifest_rows = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    freshness_row = manifest_rows[manifest_rows["artifact_id"] == "data_freshness"].iloc[0]
    assert freshness_row["warrant_ready"] == "False"
    assert freshness_row["warrant_pdf_visibility"] == "hidden_unavailable"


def test_daily_published_model_snapshot_builder_rejects_wrong_model_signal_date(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    signals = pd.read_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        dtype=str,
    )
    signals.loc[0, "signal_date"] = "20260612"
    signals.to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    with pytest.raises(RuntimeError, match="signal_date must match report date 20260615"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=tmp_path / "output" / "history" / "daily_model_snapshots",
            manifest_path=(
                tmp_path
                / "output"
                / "history"
                / "daily_model_snapshots"
                / "daily_published_model_snapshot_manifest.csv"
            ),
            generated_at="2026-06-16 08:00:00 Asia/Taipei",
            commit_sha="test-sha",
        )


def test_legacy_absolute_c_paths_relocate_without_rewriting_manifest_identity(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    for column in ("source_path", "snapshot_path"):
        manifest[column] = manifest[column].map(
            lambda value: f"C:/retired-runner/repository/{value}"
        )
    identity_columns = [
        "artifact_id",
        "snapshot_revision",
        "source_path",
        "snapshot_path",
        "source_sha256",
        "snapshot_sha256",
    ]
    before = manifest[identity_columns].copy()
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    reused = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"data_freshness"},
    )
    after = pd.read_csv(manifest_path, dtype=str).fillna("")

    pd.testing.assert_frame_equal(before, after[identity_columns])
    assert reused.iloc[0]["snapshot_path"].startswith(
        "C:/retired-runner/repository/output/history/daily_model_snapshots/"
    )
    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    ) == []


def test_legacy_absolute_path_without_approved_tail_fails_closed(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
    )
    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    mask = manifest["artifact_id"].eq("data_freshness")
    filename = Path(manifest.loc[mask, "snapshot_path"].iloc[0]).name
    manifest.loc[mask, "snapshot_path"] = f"C:/retired-runner/arbitrary/{filename}"
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
    )
    assert any("does not end in the approved path" in error for error in errors)
    with pytest.raises(RuntimeError, match="does not end in the approved path"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
        )


def test_publisher_and_validator_reject_canonical_duplicate_fake_r2(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"
    write_minimal_latest_artifacts(latest_dir, report_date=report_date)
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
        artifact_ids={"data_freshness"},
    )

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    r1 = manifest.iloc[0].copy()
    r1_versioned = repository_file(tmp_path, r1["snapshot_path"])
    lf_payload = r1_versioned.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf_payload = lf_payload.replace(b"\n", b"\r\n")
    legacy_path = snapshot_dir / f"data_freshness_{report_date}.csv"
    legacy_path.write_bytes(crlf_payload)
    r1_versioned.unlink()
    legacy_raw_sha = hashlib.sha256(crlf_payload).hexdigest()
    canonical_sha = hashlib.sha256(lf_payload).hexdigest()
    manifest.loc[0, "snapshot_path"] = legacy_path.as_posix()
    manifest.loc[0, "source_sha256"] = legacy_raw_sha
    manifest.loc[0, "snapshot_sha256"] = legacy_raw_sha
    manifest.loc[0, "revision_reason"] = update_snapshots.LEGACY_REVISION_REASON

    artifact = update_snapshots.ARTIFACTS_BY_ID["data_freshness"]
    r2_path = snapshot_dir / update_snapshots.snapshot_name(
        artifact,
        report_date,
        "r2",
        canonical_sha,
    )
    r2_path.write_bytes(lf_payload)
    r2 = manifest.iloc[0].copy()
    r2["snapshot_revision"] = "r2"
    r2["supersedes_snapshot_sha256"] = legacy_raw_sha
    r2["revision_reason"] = "fake_line_ending_revision"
    r2["snapshot_path"] = (
        update_snapshots.SNAPSHOT_REPOSITORY_PATH / r2_path.name
    ).as_posix()
    r2["source_sha256"] = canonical_sha
    r2["snapshot_sha256"] = canonical_sha
    pd.concat([manifest, r2.to_frame().T], ignore_index=True).to_csv(
        manifest_path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
    )
    assert any("canonical duplicate payload revision is forbidden" in error for error in errors)
    with pytest.raises(RuntimeError, match="canonical duplicate payload revision is forbidden"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
            revision_reason="must_not_publish",
        )


def test_publisher_rejects_r3_that_repeats_r1_canonical_payload(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    initial = update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
    )
    r1_payload = repository_file(
        tmp_path, initial.iloc[0]["snapshot_path"]
    ).read_bytes()

    source = latest_dir / "data_freshness_latest.csv"
    frame = pd.read_csv(source, dtype=str)
    frame.loc[0, "warrant_source_status"] = "ok_revised"
    frame.to_csv(source, index=False, encoding="utf-8", lineterminator="\n")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
        revision_reason="real_r2",
    )
    manifest_before = manifest_path.read_bytes()
    source.write_bytes(r1_payload)

    with pytest.raises(RuntimeError, match="canonical duplicate payload revision"):
        update_snapshots.build_daily_published_model_snapshots(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            artifact_ids={"data_freshness"},
            revision_reason="fake_r3_reversion",
        )
    assert manifest_path.read_bytes() == manifest_before


def test_scoped_validator_requires_only_requested_current_artifacts_but_full_chain(
    tmp_path: Path,
) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    selected_ids = {"model_signals_for_report", "all_candidates_source_rows"}
    write_minimal_latest_artifacts(latest_dir, report_date="20260615")
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 08:00:00 Asia/Taipei",
        commit_sha="test-sha",
        artifact_ids=selected_ids,
    )

    signals_path = latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    signals = pd.read_csv(signals_path, dtype=str)
    signals.loc[0, "model_score"] = "71.0"
    signals.to_csv(
        signals_path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )
    update_snapshots.build_daily_published_model_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        generated_at="2026-06-16 09:00:00 Asia/Taipei",
        commit_sha="test-sha-2",
        artifact_ids={"model_signals_for_report"},
        revision_reason="scoped_formal_sync",
    )

    assert validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids=selected_ids,
    ) == []
    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    historical_r1 = manifest[
        manifest["artifact_id"].eq("model_signals_for_report")
        & manifest["snapshot_revision"].eq("r1")
    ].iloc[0]
    historical_path = repository_file(tmp_path, historical_r1["snapshot_path"])
    historical_payload = historical_path.read_bytes()
    historical_path.write_text("tampered historical revision\n", encoding="utf-8")
    historical_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids=selected_ids,
    )
    assert any(
        "model_signals_for_report/r1" in error
        and "snapshot_sha256 does not match" in error
        for error in historical_errors
    )
    historical_path.write_bytes(historical_payload)
    full_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
    )
    assert any("manifest missing current" in error for error in full_errors)
    missing_selected_errors = validate_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        artifact_ids={"data_freshness"},
    )
    assert any("data_freshness" in error for error in missing_selected_errors)

    args = validate_snapshots.parse_args(
        [
            "--artifact-id",
            "model_signals_for_report",
            "--artifact-id",
            "all_candidates_source_rows",
        ]
    )
    assert args.artifact_id == [
        "model_signals_for_report",
        "all_candidates_source_rows",
    ]


def test_model_signal_snapshot_contract_keeps_volume_v2_score_columns_required() -> None:
    expected = {
        "base_model_score",
        "operation_score",
        "tdcc_score",
        "pattern_score",
        "risk_penalty",
        "final_rank_score",
        "rank_reason_zh",
    }
    artifact = update_snapshots.ARTIFACTS_BY_ID["model_signals_for_report"]
    assert expected <= set(artifact.required_columns)
