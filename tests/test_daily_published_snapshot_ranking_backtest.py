from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_published_snapshot_ranking_backtest as builder  # noqa: E402
import validate_daily_published_snapshot_ranking_backtest as validator  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def manifest_row(report_date: str, artifact_id: str, snapshot_path: Path) -> dict[str, str]:
    df = pd.read_csv(snapshot_path, dtype=str)
    return {
        "snapshot_report_date": report_date,
        "generated_at": "2026-06-16 18:00:00 Asia/Taipei",
        "pipeline_commit_sha": "test-sha",
        "main_price_date": report_date,
        "report_ready": "True",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
        "artifact_id": artifact_id,
        "source_path": (
            "output/latest/daily_candidate_model_signals_for_report_latest.csv"
            if artifact_id == "model_signals_for_report"
            else "output/latest/daily_volume_breakout_operation_section_latest.csv"
        ),
        "snapshot_path": snapshot_path.as_posix(),
        "source_sha256": builder.canonical_text_sha256(snapshot_path),
        "snapshot_sha256": builder.canonical_text_sha256(snapshot_path),
        "row_count": str(len(df)),
        "column_count": str(len(df.columns)),
        "purpose": "as_published_daily_model_snapshot",
    }


def lineage_audit_row(
    formal_row: pd.Series | dict[str, str],
    formal_snapshot_path: Path,
    *,
    disposition: str = "verified_clean",
    evidence_status: str = "complete",
    paired_source_resolution: str = "current_worktree_exact_source_files",
) -> dict[str, str]:
    values = formal_row.to_dict() if isinstance(formal_row, pd.Series) else dict(formal_row)
    signal_date = str(values.get("signal_date", ""))
    return {
        "snapshot_report_date": signal_date,
        "signal_date": signal_date,
        "model_id": str(values.get("model_id", "")),
        "stock_id": str(values.get("stock_id", "")),
        "formal_row_sha256": builder.canonical_row_sha256(values),
        "formal_snapshot_sha256": builder.canonical_text_sha256(formal_snapshot_path),
        "paired_source_resolution": paired_source_resolution,
        "production_code_sha256": "1" * 64,
        "watch_artifact_sha256": "2" * 64,
        "candidate_artifact_sha256": "3" * 64,
        "official_warrant_artifact_sha256": "4" * 64,
        "formal_row_disposition": disposition,
        "evidence_status": evidence_status,
    }


def formal_snapshot_index_for(
    formal_row: pd.Series | dict[str, str], formal_snapshot_path: Path
) -> dict[tuple[str, str, str], list[dict[str, str]]]:
    values = formal_row.to_dict() if isinstance(formal_row, pd.Series) else dict(formal_row)
    key = (
        builder.normalize_date(values.get("signal_date", "")),
        str(values.get("model_id", "")),
        builder.normalize_code(values.get("stock_id", "")),
    )
    return {
        key: [
            {
                "formal_row_sha256": builder.canonical_row_sha256(values),
                "formal_snapshot_sha256": builder.canonical_text_sha256(
                    formal_snapshot_path
                ),
                "formal_snapshot_path": formal_snapshot_path.as_posix(),
            }
        ]
    }


def write_price_history(price_dir: Path) -> None:
    write_csv(
        price_dir / "1234.csv",
        [
            {"date": "20260615", "open": "90", "high": "95", "low": "89", "close": "94"},
            {"date": "20260616", "open": "100", "high": "110", "low": "95", "close": "105"},
            {"date": "20260617", "open": "106", "high": "112", "low": "101", "close": "108"},
            {"date": "20260618", "open": "109", "high": "115", "low": "102", "close": "110"},
            {"date": "20260619", "open": "111", "high": "116", "low": "103", "close": "112"},
            {"date": "20260622", "open": "113", "high": "118", "low": "104", "close": "114"},
            {"date": "20260623", "open": "114", "high": "119", "low": "105", "close": "115"},
            {"date": "20260624", "open": "115", "high": "120", "low": "106", "close": "116"},
            {"date": "20260625", "open": "116", "high": "121", "low": "107", "close": "117"},
            {"date": "20260626", "open": "117", "high": "122", "low": "108", "close": "118"},
            {"date": "20260629", "open": "118", "high": "123", "low": "109", "close": "119"},
        ],
    )
    write_csv(
        price_dir / "5678.csv",
        [
            {"date": "20260615", "open": "50", "high": "52", "low": "49", "close": "51"},
            {"date": "20260616", "open": "50", "high": "51", "low": "46", "close": "47"},
            {"date": "20260617", "open": "47", "high": "48", "low": "44", "close": "45"},
            {"date": "20260618", "open": "45", "high": "46", "low": "42", "close": "43"},
        ],
    )


def write_snapshot_fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    report_date = "20260615"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    price_dir = tmp_path / "data" / "stock_price_history"

    signals = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    operations = snapshot_dir / f"daily_volume_breakout_operation_section_{report_date}.csv"
    manifest = snapshot_dir / "daily_published_model_snapshot_manifest.csv"

    write_csv(
        signals,
        [
            {
                "signal_date": report_date,
                "stock_id": "1234",
                "stock_name": "Alpha",
                "model_id": "volume_range_breakout",
                "model_name_zh": "放量攻擊模型",
                "model_score": "91",
                "display_rank": "1",
                "model_rank": "1",
                "report_line": "mainstream",
                "report_bucket": "mainstream",
                "effective_mainstream_label": "core_mainstream",
            },
            {
                "signal_date": report_date,
                "stock_id": "5678",
                "stock_name": "Beta",
                "model_id": "hot_theme_pullback",
                "model_name_zh": "熱門族群回檔模型",
                "model_score": "73",
                "display_rank": "12",
                "model_rank": "12",
                "report_line": "non_mainstream",
                "report_bucket": "non_mainstream",
                "effective_mainstream_label": "non_mainstream",
            },
        ],
    )
    write_csv(
        operations,
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "stock_id": "1234",
                "stock_name": "Alpha",
                "signal_date": report_date,
                "confirmation_date": "",
                "display_order": "1",
                "research_score": "91",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "stock_id": "1234",
                "stock_name": "Alpha",
                "signal_date": report_date,
                "confirmation_date": "",
                "display_order": "1",
                "research_score": "91",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "row_type": "data",
                "stock_id": "5678",
                "stock_name": "Beta",
                "signal_date": report_date,
                "confirmation_date": report_date,
                "display_order": "2",
                "research_score": "73",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
            },
        ],
    )
    write_csv(manifest, [manifest_row(report_date, "model_signals_for_report", signals), manifest_row(report_date, "volume_breakout_operation_section", operations)])
    write_price_history(price_dir)
    return manifest, snapshot_dir, price_dir


def test_published_snapshot_ranking_backtest_uses_date_stamped_snapshots(tmp_path: Path) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)

    summary, events = builder.build_daily_published_snapshot_ranking_backtest(
        manifest_path=manifest,
        snapshot_root=snapshot_dir,
        price_dir=price_dir,
        generated_at="2026-06-16 18:00:00 Asia/Taipei",
    )

    model_events = events[events["source_artifact"].eq("model_signals_for_report")]
    assert len(model_events) == 2
    assert set(model_events["mainstream_segment"]) == {"mainstream", "non_mainstream"}
    assert set(model_events["score_decile"]) == {"score_90_100", "score_70_80"}
    assert set(model_events["rank_bucket"]) == {"rank_001_005", "rank_011_020"}
    assert set(model_events["ranking_evaluation_eligible"]) == {"True"}
    assert set(model_events["trade_eligible"]) == {"False"}

    operation_events = events[events["source_artifact"].eq("volume_breakout_operation_section")]
    assert len(operation_events) == 2
    pending = operation_events[operation_events["operation_section"].eq("pending_confirmation")]
    confirmed = operation_events[operation_events["operation_section"].eq("confirmed_operation")]
    assert set(operation_events["ranking_evaluation_eligible"]) == {"False"}
    assert set(pending["trade_eligible"]) == {"False"}
    assert set(confirmed["trade_eligible"]) == {"True"}

    volume_sections = summary[summary["segment_type"].eq("volume_operation_section")]
    assert "volume_range_breakout|active_operation" in set(volume_sections["segment_value"])
    assert set(summary["advisory_only"]) == {"True"}


def rewrite_fixture_volume_rows_as_v2(
    manifest: Path,
    snapshot_dir: Path,
    *,
    first_disposition: str,
) -> Path:
    report_date = "20260615"
    model_id = "volume_range_breakout_v2_high_position_volume_attack"
    signals_path = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    operations_path = snapshot_dir / f"daily_volume_breakout_operation_section_{report_date}.csv"

    signals = pd.read_csv(signals_path, dtype=str, keep_default_na=False)
    signals.loc[signals["stock_id"].isin(["1234", "5678"]), "model_id"] = model_id
    signals.to_csv(signals_path, index=False, encoding="utf-8", lineterminator="\n")
    operations = pd.read_csv(operations_path, dtype=str, keep_default_na=False)
    operations.loc[operations["stock_id"].isin(["1234", "5678"]), "model_id"] = model_id
    operations.to_csv(operations_path, index=False, encoding="utf-8", lineterminator="\n")
    write_csv(
        manifest,
        [
            manifest_row(report_date, "model_signals_for_report", signals_path),
            manifest_row(report_date, "volume_breakout_operation_section", operations_path),
        ],
    )

    lineage_path = snapshot_dir.parent.parent / "volume_v2_lineage.csv"
    formal_rows = pd.read_csv(signals_path, dtype=str, keep_default_na=False).set_index(
        "stock_id", drop=False
    )
    write_csv(
        lineage_path,
        [
            lineage_audit_row(
                formal_rows.loc["1234"],
                signals_path,
                disposition=first_disposition,
            ),
            lineage_audit_row(formal_rows.loc["5678"], signals_path),
        ],
    )
    return lineage_path


def test_snapshot_canonical_hash_normalizes_bom_crlf_and_lone_cr(tmp_path: Path) -> None:
    paths = [tmp_path / "lf.csv", tmp_path / "bom_crlf.csv", tmp_path / "cr.csv"]
    paths[0].write_bytes(b"a,b\n1,2\n")
    paths[1].write_bytes(b"\xef\xbb\xbfa,b\r\n1,2\r\n")
    paths[2].write_bytes(b"a,b\r1,2\r")

    hashes = {builder.canonical_text_sha256(path) for path in paths}

    assert len(hashes) == 1
    hashes.pop()
    manifest_hashes = [
        builder.published_manifest_v1_sha256_candidates(path) for path in paths
    ]
    assert manifest_hashes[0] & manifest_hashes[2]
    assert not manifest_hashes[0] & manifest_hashes[1]
    for path in paths:
        for manifest_hash in builder.published_manifest_v1_sha256_candidates(path):
            assert builder.validate_snapshot_row(
                pd.Series(
                    {
                        "snapshot_path": path.as_posix(),
                        "snapshot_sha256": manifest_hash,
                        "row_count": "1",
                        "column_count": "2",
                    }
                ),
                snapshot_root=tmp_path,
            ) == []


def test_volume_v2_non_clean_events_are_retained_but_excluded_from_research_metrics(
    tmp_path: Path,
) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)
    lineage_path = rewrite_fixture_volume_rows_as_v2(
        manifest,
        snapshot_dir,
        first_disposition="quarantined",
    )

    summary, events = builder.build_daily_published_snapshot_ranking_backtest(
        manifest_path=manifest,
        snapshot_root=snapshot_dir,
        price_dir=price_dir,
        lineage_audit_path=lineage_path,
        generated_at="2026-06-16 18:00:00 Asia/Taipei",
    )

    quarantined = events[
        events["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")
        & events["stock_id"].eq("1234")
    ]
    assert len(quarantined) == 2
    assert set(quarantined["lineage_gate_status"]) == {"non_clean_excluded"}
    assert set(quarantined["lineage_formal_row_disposition"]) == {"quarantined"}
    assert set(quarantined["summary_evidence_eligible"]) == {"False"}
    assert set(quarantined["lineage_gate_pass_for_promotion_evidence"]) == {"False"}
    assert set(quarantined["ranking_evaluation_eligible"]) == {"False"}
    assert set(quarantined["trade_eligible"]) == {"False"}

    clean_confirmed = events[
        events["source_artifact"].eq("volume_breakout_operation_section")
        & events["stock_id"].eq("5678")
    ]
    assert set(clean_confirmed["lineage_gate_status"]) == {"verified_clean"}
    assert set(clean_confirmed["trade_eligible"]) == {"True"}

    exclusions = summary[summary["segment_type"].eq("lineage_exclusion")]
    assert int(exclusions["sample_size"].astype(int).sum()) == 2
    assert set(exclusions["evaluated_d1_count"].astype(int)) == {0}
    model_signal_summary = summary[
        summary["segment_type"].eq("model_overall")
        & summary["source_artifact"].eq("model_signals_for_report")
        & summary["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")
    ]
    assert len(model_signal_summary) == 1
    assert int(model_signal_summary.iloc[0]["sample_size"]) == 1
    assert int(model_signal_summary.iloc[0]["lineage_excluded_count"]) == 1
    assert validator.validate_volume_v2_lineage(events) == []

    invalid = events.copy()
    invalid.loc[
        invalid["lineage_gate_status"].eq("non_clean_excluded"),
        "ranking_evaluation_eligible",
    ] = "True"
    assert any(
        "ranking_evaluation_eligible=False" in error
        for error in validator.validate_volume_v2_lineage(invalid)
    )


@pytest.mark.parametrize(
    "paired_source_resolution",
    [
        "current_worktree_exact_source_files",
        "manifest_pipeline_commit_exact_source_blob",
        "snapshot_history_exact_blob_fallback",
    ],
)
def test_volume_v2_verified_clean_requires_exact_current_or_history_row_hash(
    tmp_path: Path,
    paired_source_resolution: str,
) -> None:
    formal_path = tmp_path / "formal.csv"
    formal_row = {
        "signal_date": "20260716",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "stock_id": "6505",
        "warrant_flow_signal": "call_inflow",
        "final_rank_score": "80",
        "model_rank": "1",
    }
    write_csv(formal_path, [formal_row])
    lineage_path = tmp_path / "lineage.csv"
    write_csv(
        lineage_path,
        [
            lineage_audit_row(
                formal_row,
                formal_path,
                paired_source_resolution=paired_source_resolution,
            )
        ],
    )
    audit_index, audit_sha = builder.load_volume_v2_lineage_audit(lineage_path)

    payload = builder.volume_v2_lineage_payload(
        signal_date="20260716",
        model_id=formal_row["model_id"],
        stock_id="6505",
        audit_index=audit_index,
        formal_snapshot_index=formal_snapshot_index_for(formal_row, formal_path),
        audit_path=lineage_path,
        audit_sha256=audit_sha,
    )

    assert payload["lineage_gate_status"] == "verified_clean"
    assert payload["summary_evidence_eligible"] == "True"
    assert payload["lineage_gate_pass_for_promotion_evidence"] == "True"
    assert payload["lineage_formal_row_sha256"] == payload["lineage_observed_formal_row_sha256"]
    assert payload["lineage_formal_snapshot_sha256"] == payload["lineage_observed_formal_snapshot_sha256"]
    assert payload["lineage_paired_source_resolution"] == paired_source_resolution


@pytest.mark.parametrize(
    ("field", "changed_value"),
    [
        ("warrant_flow_signal", "put_inflow"),
        ("final_rank_score", "79"),
        ("model_rank", "2"),
    ],
)
def test_volume_v2_same_key_changed_warrant_score_or_rank_fails_hash_gate(
    tmp_path: Path,
    field: str,
    changed_value: str,
) -> None:
    formal_path = tmp_path / "formal.csv"
    audited_row = {
        "signal_date": "20260716",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "stock_id": "6505",
        "warrant_flow_signal": "call_inflow",
        "final_rank_score": "80",
        "model_rank": "1",
    }
    write_csv(formal_path, [audited_row])
    lineage_path = tmp_path / "lineage.csv"
    write_csv(lineage_path, [lineage_audit_row(audited_row, formal_path)])
    audit_index, audit_sha = builder.load_volume_v2_lineage_audit(lineage_path)
    changed_row = dict(audited_row)
    changed_row[field] = changed_value
    write_csv(formal_path, [changed_row])

    payload = builder.volume_v2_lineage_payload(
        signal_date="20260716",
        model_id=audited_row["model_id"],
        stock_id="6505",
        audit_index=audit_index,
        formal_snapshot_index=formal_snapshot_index_for(changed_row, formal_path),
        audit_path=lineage_path,
        audit_sha256=audit_sha,
    )

    assert payload["lineage_gate_status"] == "non_clean_excluded"
    assert payload["lineage_formal_row_disposition"] == "hash_mismatch"
    assert payload["summary_evidence_eligible"] == "False"
    assert payload["lineage_gate_pass_for_promotion_evidence"] == "False"


@pytest.mark.parametrize(
    ("field", "stale_value"),
    [
        ("formal_snapshot_sha256", "0" * 64),
        ("watch_artifact_sha256", "stale"),
        ("paired_source_resolution", "legacy_key_only_resolution"),
    ],
)
def test_volume_v2_stale_snapshot_or_source_lineage_fails_closed(
    tmp_path: Path,
    field: str,
    stale_value: str,
) -> None:
    formal_path = tmp_path / "formal.csv"
    formal_row = {
        "signal_date": "20260716",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "stock_id": "6505",
        "warrant_flow_signal": "call_inflow",
        "final_rank_score": "80",
        "model_rank": "1",
    }
    write_csv(formal_path, [formal_row])
    audit_row = lineage_audit_row(formal_row, formal_path)
    audit_row[field] = stale_value
    lineage_path = tmp_path / "lineage.csv"
    write_csv(lineage_path, [audit_row])
    audit_index, audit_sha = builder.load_volume_v2_lineage_audit(lineage_path)

    payload = builder.volume_v2_lineage_payload(
        signal_date="20260716",
        model_id=formal_row["model_id"],
        stock_id="6505",
        audit_index=audit_index,
        formal_snapshot_index=formal_snapshot_index_for(formal_row, formal_path),
        audit_path=lineage_path,
        audit_sha256=audit_sha,
    )

    assert payload["lineage_gate_status"] == "non_clean_excluded"
    assert payload["summary_evidence_eligible"] == "False"
    assert payload["lineage_gate_pass_for_promotion_evidence"] == "False"


def test_volume_v2_changed_formal_snapshot_cannot_enter_ranking_trade_or_summary(
    tmp_path: Path,
) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)
    lineage_path = rewrite_fixture_volume_rows_as_v2(
        manifest,
        snapshot_dir,
        first_disposition="verified_clean",
    )
    report_date = "20260615"
    signals_path = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    operations_path = snapshot_dir / f"daily_volume_breakout_operation_section_{report_date}.csv"
    signals = pd.read_csv(signals_path, dtype=str, keep_default_na=False)
    signals.loc[signals["stock_id"].eq("1234"), "model_score"] = "999"
    signals.to_csv(signals_path, index=False, encoding="utf-8", lineterminator="\n")
    write_csv(
        manifest,
        [
            manifest_row(report_date, "model_signals_for_report", signals_path),
            manifest_row(report_date, "volume_breakout_operation_section", operations_path),
        ],
    )

    summary, events = builder.build_daily_published_snapshot_ranking_backtest(
        manifest_path=manifest,
        snapshot_root=snapshot_dir,
        price_dir=price_dir,
        lineage_audit_path=lineage_path,
        generated_at="2026-06-16 18:00:00 Asia/Taipei",
    )

    volume_events = events[events["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")]
    assert set(volume_events["lineage_gate_status"]) == {"non_clean_excluded"}
    assert set(volume_events["ranking_evaluation_eligible"]) == {"False"}
    assert set(volume_events["trade_eligible"]) == {"False"}
    assert set(volume_events["summary_evidence_eligible"]) == {"False"}
    assert summary[
        summary["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")
        & ~summary["segment_type"].eq("lineage_exclusion")
    ].empty


@pytest.mark.parametrize("disposition", ["superseded", "quarantined", "unreplayable"])
def test_volume_v2_non_clean_dispositions_fail_closed_for_promotion_evidence(
    tmp_path: Path,
    disposition: str,
) -> None:
    formal_path = tmp_path / "formal.csv"
    formal_row = {
        "signal_date": "20260716",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "stock_id": "6505",
        "warrant_flow_signal": "call_inflow",
        "final_rank_score": "80",
        "model_rank": "1",
    }
    write_csv(formal_path, [formal_row])
    lineage_path = tmp_path / "lineage.csv"
    write_csv(
        lineage_path,
        [
            lineage_audit_row(
                formal_row,
                formal_path,
                disposition=disposition,
            )
        ],
    )
    audit_index, audit_sha = builder.load_volume_v2_lineage_audit(lineage_path)

    payload = builder.volume_v2_lineage_payload(
        signal_date="20260716",
        model_id="volume_range_breakout_v2_high_position_volume_attack",
        stock_id="6505",
        audit_index=audit_index,
        formal_snapshot_index=formal_snapshot_index_for(formal_row, formal_path),
        audit_path=lineage_path,
        audit_sha256=audit_sha,
    )

    assert payload["lineage_gate_status"] == "non_clean_excluded"
    assert payload["summary_evidence_eligible"] == "False"
    assert payload["lineage_gate_pass_for_promotion_evidence"] == "False"


def test_volume_v2_uncovered_research_row_is_explicitly_excluded(tmp_path: Path) -> None:
    lineage_path = tmp_path / "missing.csv"
    audit_index, audit_sha = builder.load_volume_v2_lineage_audit(lineage_path)

    payload = builder.volume_v2_lineage_payload(
        signal_date="20260708",
        model_id="volume_range_breakout_v2_low_position_volume_attack",
        stock_id="6637",
        audit_index=audit_index,
        formal_snapshot_index={},
        audit_path=lineage_path,
        audit_sha256=audit_sha,
    )

    assert payload["lineage_gate_status"] == "uncovered_fail_closed"
    assert payload["lineage_formal_row_disposition"] == "uncovered"
    assert payload["summary_evidence_eligible"] == "False"
    assert payload["lineage_gate_pass_for_promotion_evidence"] == "False"


def test_published_snapshot_manifest_hash_mismatch_blocks_build(tmp_path: Path) -> None:
    manifest, snapshot_dir, price_dir = write_snapshot_fixture(tmp_path)
    manifest_df = pd.read_csv(manifest, dtype=str)
    manifest_df.loc[0, "snapshot_sha256"] = "bad"
    manifest_df.to_csv(manifest, index=False, encoding="utf-8", lineterminator="\n")

    with pytest.raises(RuntimeError, match="snapshot_sha256 mismatch"):
        builder.build_daily_published_snapshot_ranking_backtest(
            manifest_path=manifest,
            snapshot_root=snapshot_dir,
            price_dir=price_dir,
            generated_at="2026-06-16 18:00:00 Asia/Taipei",
        )
