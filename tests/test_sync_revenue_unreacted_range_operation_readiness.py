from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_revenue_unreacted_range_operation_readiness as syncer  # noqa: E402


def readiness_row(model_id: str) -> dict[str, str]:
    row = {field_name: "" for field_name in syncer.LEGACY_COLUMNS}
    row.update(
        {
            "generated_at": "committed-time",
            "model_id": model_id,
            "model_name_zh": "營收模型" if model_id == syncer.MODEL_ID else "其他模型",
            "parity_status": "stale" if model_id == syncer.MODEL_ID else "production_parity",
            "blocker": "stale blocker" if model_id == syncer.MODEL_ID else "unchanged blocker",
            "operation_module_status": "baseline_only_no_validated_operation_module",
            "daily_adapter_status": "not_started",
            "approved_for_daily": "False" if model_id == syncer.MODEL_ID else "True",
            "approval_status": "not_started",
            "presentation_allowed": "False" if model_id == syncer.MODEL_ID else "True",
            "operation_directive_level": "no_operation_directive",
            "pdf_integration_status": "not_started",
            "packet_integration_status": "not_started",
            "registry_pattern_count": "0",
            "registry_current_model_pattern_count": "0",
            "registry_best_sample_size": "0",
            "daily_adapter_row_count": "0",
            "daily_adapter_data_row_count": "0",
            "status_note_zh": "保留原值",
        }
    )
    return row


def revenue_summary() -> dict[str, str | int]:
    return {
        "parity_status": "research_matrix_complete",
        "blocker": (
            "anomaly_disposition_blockers=9; unresolved_anomalies=9; "
            "forward_holdout_v2_mature=0/20; formal_adapter=not_started"
        ),
        "operation_module_status": (
            "research_matrix_complete_formal_adapter_not_started"
        ),
        "daily_adapter_status": "not_started",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "operation_module_id": "",
        "approval_version": "",
        "presentation_allowed": "False",
        "production_allowed": "False",
        "operation_directive_level": "no_operation_directive",
        "pdf_integration_status": "not_started",
        "packet_integration_status": "not_started",
        "registry_pattern_count": 1,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": "source_mid_falling",
        "registry_best_sample_size": 53,
        "registry_best_win_rate": "77.3585",
        "registry_best_median_return": "9.4077",
        "daily_adapter_row_count": 0,
        "daily_adapter_data_row_count": 0,
        "daily_adapter_sections": "",
        "status_note_zh": "僅月營收；正式權限維持關閉。",
    }


def legacy_readiness() -> pd.DataFrame:
    return pd.DataFrame(
        [
            readiness_row("other_model"),
            readiness_row(syncer.MODEL_ID),
            readiness_row("second_other_model"),
        ],
        columns=syncer.LEGACY_COLUMNS,
    )


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def test_build_replaces_only_revenue_and_keeps_non_revenue_fields_exact() -> None:
    base = legacy_readiness()
    expected_non_revenue = base[
        ~base["model_id"].eq(syncer.MODEL_ID)
    ].reset_index(drop=True)

    actual = syncer.build_revenue_only_readiness(
        base,
        revenue_summary(),
        generated_at="new-revenue-time",
    )

    assert tuple(actual.columns) == syncer.TARGET_COLUMNS
    assert actual["model_id"].tolist() == base["model_id"].tolist()
    actual_non_revenue = actual[
        ~actual["model_id"].eq(syncer.MODEL_ID)
    ].reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual_non_revenue[list(syncer.LEGACY_COLUMNS)],
        expected_non_revenue,
    )
    assert actual_non_revenue["generated_at"].eq("committed-time").all()
    for field_name in syncer.REVENUE_PERMISSION_COLUMNS:
        assert actual_non_revenue[field_name].eq("").all()

    revenue = actual[actual["model_id"].eq(syncer.MODEL_ID)].iloc[0]
    assert revenue["generated_at"] == "new-revenue-time"
    assert revenue["model_name_zh"] == "營收模型"
    for field_name, expected in revenue_summary().items():
        assert revenue[field_name] == str(expected)


def test_build_accepts_only_canonical_extended_disabled_source() -> None:
    base = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="first-time",
    )
    rebuilt = syncer.build_revenue_only_readiness(
        base,
        revenue_summary(),
        generated_at="second-time",
    )
    non_revenue = rebuilt[~rebuilt["model_id"].eq(syncer.MODEL_ID)]
    assert non_revenue["generated_at"].eq("committed-time").all()
    assert rebuilt.loc[
        rebuilt["model_id"].eq(syncer.MODEL_ID), "generated_at"
    ].item() == "second-time"

    unsafe = base.copy()
    unsafe.loc[unsafe["model_id"].eq(syncer.MODEL_ID), "production_allowed"] = "True"
    with pytest.raises(RuntimeError, match="production_allowed must be explicit False"):
        syncer.build_revenue_only_readiness(
            unsafe,
            revenue_summary(),
            generated_at="unsafe",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("duplicate", "duplicate model_id"),
        ("blank", "blank model_id"),
        ("schema", "schema drift"),
        ("noncanonical_bool", "non-canonical values"),
    ),
)
def test_build_fails_closed_on_identity_or_schema_drift(
    mutation: str,
    message: str,
) -> None:
    base = legacy_readiness()
    if mutation == "duplicate":
        base.loc[2, "model_id"] = "other_model"
    elif mutation == "blank":
        base.loc[2, "model_id"] = ""
    elif mutation == "schema":
        base["unexpected"] = ""
    elif mutation == "noncanonical_bool":
        base.loc[0, "approved_for_daily"] = "true"

    with pytest.raises(RuntimeError, match=message):
        syncer.build_revenue_only_readiness(
            base,
            revenue_summary(),
            generated_at="new-time",
        )


def test_build_fails_closed_on_same_model_summary_schema_drift() -> None:
    incomplete = revenue_summary()
    incomplete.pop("blocker")
    with pytest.raises(RuntimeError, match="summary schema drift"):
        syncer.build_revenue_only_readiness(
            legacy_readiness(),
            incomplete,
            generated_at="new-time",
        )


def test_committed_source_treats_crlf_as_diagnostic_and_semantic_drift_as_error(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    source = repo / "source.csv"
    source.write_bytes(b"key,value\nrow,one\n")
    git(repo, "add", "source.csv")
    git(repo, "commit", "-m", "source")

    source.write_bytes(b"key,value\r\nrow,one\r\n")
    committed, diagnostic = syncer._committed_semantic_source(
        repo,
        "source.csv",
        csv_source=True,
    )
    assert committed == b"key,value\nrow,one\n"
    assert diagnostic is not None
    assert "diagnostic only" in diagnostic

    source.write_bytes(b"key,value\nrow,two\n")
    with pytest.raises(RuntimeError, match="semantic drift from HEAD"):
        syncer._committed_semantic_source(
            repo,
            "source.csv",
            csv_source=True,
        )


def test_load_committed_inputs_rejects_committed_output_docs_mirror_drift(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    csv_data = legacy_readiness().to_csv(index=False, lineterminator="\n").encode()
    drifted_csv = csv_data.replace(b"unchanged blocker", b"drifted blocker", 1)
    for logical_path in syncer.READINESS_MIRROR_RELS:
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if logical_path == syncer.DOCS_CSV_REL:
            path.write_bytes(drifted_csv)
        elif logical_path.endswith(".csv"):
            path.write_bytes(csv_data)
        else:
            path.write_text("# committed readiness\n", encoding="utf-8")
    for logical_path in syncer.CANONICAL_SOURCE_RELS:
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("model_id\nrevenue_unreacted_range\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "drifted mirrors")

    with pytest.raises(RuntimeError, match="output/docs readiness CSV mirrors differ"):
        syncer.load_committed_inputs(repo)


def test_write_scope_is_exact_four_byte_paired_mirrors(tmp_path: Path) -> None:
    readiness = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="new-time",
    )
    syncer.write_readiness_mirrors(
        tmp_path,
        readiness,
        generated_at="new-time",
    )

    written = {
        path.relative_to(tmp_path).as_posix()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    assert written == set(syncer.READINESS_MIRROR_RELS)
    assert (
        tmp_path / syncer.OUT_CSV_REL
    ).read_bytes() == (tmp_path / syncer.DOCS_CSV_REL).read_bytes()
    markdown = (tmp_path / syncer.OUT_MD_REL).read_bytes()
    assert markdown == (tmp_path / syncer.DOCS_MD_REL).read_bytes()
    text = markdown.decode("utf-8")
    assert "| formal_model_use_allowed |" in text
    assert "| production_allowed |" in text
    status_row = next(
        line for line in text.splitlines() if f"| {syncer.MODEL_ID} |" in line
    )
    assert status_row.count("False") >= 4


def test_current_canonical_sources_build_exact_disabled_revenue_row() -> None:
    base = pd.read_csv(ROOT / syncer.OUT_CSV_REL, dtype=str).fillna("")
    promotion = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    anomalies = pd.read_csv(
        ROOT / syncer.ANOMALY_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL,
        dtype=str,
    ).fillna("")
    detail = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL,
        dtype=str,
    ).fillna("")
    holdout_summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL,
        dtype=str,
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL,
        dtype=str,
    ).fillna("")
    source_projection_manifest = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL,
        dtype=str,
    ).fillna("")
    summary = syncer.summarize_revenue_promotion_readiness(
        promotion,
        anomalies,
        holdout,
        holdout_detail=detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        source_projection_manifest=source_projection_manifest,
    )

    readiness = syncer.build_revenue_only_readiness(
        base,
        summary,
        generated_at="deterministic-test-time",
    )
    revenue = readiness[readiness["model_id"].eq(syncer.MODEL_ID)].iloc[0]
    assert revenue["blocker"] == (
        "anomaly_disposition_blockers=9; unresolved_anomalies=9; "
        "forward_holdout_v2_mature=0/20; formal_adapter=not_started"
    )
    assert revenue["parity_status"] == "research_matrix_complete"
    assert revenue["formal_model_use_allowed"] == "False"
    assert revenue["approved_for_daily"] == "False"
    assert revenue["presentation_allowed"] == "False"
    assert revenue["production_allowed"] == "False"


def test_import_does_not_load_legacy_cross_model_builder() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            "-c",
            (
                "import sys; sys.path.insert(0, 'scripts'); "
                "import sync_revenue_unreacted_range_operation_readiness; "
                "assert 'build_model_operation_readiness' not in sys.modules"
            ),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0, result.stderr


def test_full_v2_gate_rejects_bad_rule_canonical_sha() -> None:
    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    holdout.loc[0, "rule_canonical_sha256"] = "0" * 64
    with pytest.raises(RuntimeError, match="rule_canonical_sha256 drift"):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            holdout,
            holdout_detail=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
            ).fillna(""),
            holdout_summary=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
            ).fillna(""),
            replay_source=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
            ).fillna(""),
            source_projection_manifest=pd.read_csv(
                ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
            ).fillna(""),
        )


def test_full_v2_gate_rejects_self_consistent_forged_mature_row_before_d30(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    price_path = repo / syncer.PRICE_HISTORY_DIR_REL / "2330.csv"
    price_path.parent.mkdir(parents=True)
    price_path.write_text(
        "date,open,close\n"
        "20260831,100,100\n"
        "20260901,110,110\n",
        encoding="utf-8",
        newline="\n",
    )
    resolution_path = repo / syncer.PRICE_RESOLUTION_REL
    resolution_path.parent.mkdir(parents=True, exist_ok=True)
    resolution_path.write_bytes((ROOT / syncer.PRICE_RESOLUTION_REL).read_bytes())
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "registered price evidence")

    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    manifest = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
    ).fillna("")
    source_projection_manifest = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
    ).fillna("")

    manifest.loc[0, "observed_through_date"] = "20260901"
    manifest.loc[0, "holdout_status"] = "holdout_accumulating"
    manifest.loc[0, "holdout_event_count"] = "1"
    manifest.loc[0, "mature_event_count"] = "1"
    manifest.loc[0, "right_censored_event_count"] = "0"
    manifest.loc[0, "primary_mature_count"] = "1"
    manifest.loc[0, "primary_right_censored_count"] = "0"
    manifest_row = manifest.iloc[0]
    capture_envelope = {
        "artifact_version": syncer.REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "rule_canonical_sha256": syncer.RULE_CANONICAL_SHA256,
        "data_contract_sha256": syncer.DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": syncer.PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": "20260901",
        "source_detail_canonical_sha256": manifest_row[
            "source_detail_canonical_sha256"
        ],
        "price_input_canonical_sha256": manifest_row[
            "price_input_canonical_sha256"
        ],
        **{
            field_name: manifest_row[field_name]
            for field_name in syncer.MONTHLY_LINEAGE_COLUMNS
        },
        "training_source_projection_semantic_sha256": (
            syncer.PROJECTED_EPISODE_SEMANTIC_SHA256
        ),
        "training_source_projected_episode_row_count": (
            syncer.PROJECTED_EPISODE_ROW_COUNT
        ),
        "training_source_manifest_canonical_sha256": (
            syncer.SELECTED_V2_MANIFEST_CANONICAL_SHA256
        ),
    }
    capture_id = syncer._canonical_json_sha256(capture_envelope)
    manifest.loc[0, "capture_id"] = capture_id

    detail_columns = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, nrows=0
    ).columns
    event = {column: "" for column in detail_columns}
    for column in detail_columns:
        if column in manifest.columns:
            event[column] = str(manifest.loc[0, column])
    event.update(
        {
            "capture_id": capture_id,
            "artifact_row_key": "forged|2330|20260831",
            "event_key": "forged|2330|20260831",
            "variant_id": syncer.PRIMARY_VARIANT_ID,
            "candidate_variant_id": syncer.PRIMARY_VARIANT_ID,
            "primary_variant_member": "True",
            "low_falling_member": "False",
            "low_or_mid_falling_union_member": "True",
            "lifecycle_policy_id": "rearm_after_realized_exit_next_trade_day",
            "confirmation_variant_id": "delayed_next_close_continuation_bonus",
            "holding_days": "30",
            "holding_session_index_offset": "29",
            "stop_policy_id": "none_no_stop_reference",
            "stock_id": "2330",
            "stock_name": "台積電",
            "episode_key": "forged-episode",
            "source_asof_date": "20260828",
            "source_asof_trade_date": "20260828",
            "source_asof_canonical_source_table_date": "20260828",
            "trigger_index": "0",
            "trigger_date": "20260831",
            "trigger_close": "100",
            "confirmation_index": "1",
            "confirmation_date": "20260901",
            "confirmation_close": "110",
            "entry_index": "2",
            "entry_price_basis": "analysis_open",
            "entry_date": "20260902",
            "entry_price": "110",
            "planned_exit_index": "31",
            "planned_exit_date": "20261013",
            "exit_index": "31",
            "exit_date": "20261013",
            "exit_price": "121",
            "exit_price_basis": "analysis_close",
            "exit_reason": "fixed_d30_close",
            "return_valid": "True",
            "right_censored": "False",
            "realized_return_pct": "10",
            "return_outcome": "win",
            "realized_return_ge20": "False",
            "operation_return_review_candidate_flag": "False",
            "operation_status": "mature_operation",
            "anomaly_candidate_flag": "False",
            "source_anomaly_candidate_flag": "False",
            "unresolved_price_path_candidate_flag": "False",
            "primary_metric_included": "True",
            "sensitivity_metric_included": "True",
            "same_stock_non_overlap_applied": "True",
            "financial_statement_scope": (
                syncer.REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE
            ),
            "research_only": "True",
            "formal_model_use_allowed": "False",
            "approved_for_daily": "False",
            "presentation_allowed": "False",
            "promotion_evidence_allowed": "False",
            "production_change": "False",
        }
    )
    event["event_row_canonical_sha256"] = syncer._canonical_mapping_sha256(
        {
            key: value
            for key, value in event.items()
            if key != "event_row_canonical_sha256"
        }
    )
    detail = pd.DataFrame([event], columns=detail_columns)
    assert detail.loc[0, "event_row_canonical_sha256"] == (
        syncer._canonical_mapping_sha256(
            detail.drop(columns=["event_row_canonical_sha256"]).iloc[0].to_dict()
        )
    )

    summary["holdout_status"] = "holdout_accumulating"
    for column in ("event_count", "mature_count", "right_censored_count"):
        summary[column] = "0"
    primary = summary["variant_id"].eq(syncer.PRIMARY_VARIANT_ID)
    summary.loc[primary, "event_count"] = "1"
    summary.loc[primary, "mature_count"] = "1"

    with pytest.raises(
        RuntimeError,
        match=r"independently replayed D\+2 entry and D\+30",
    ):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            manifest,
            holdout_detail=detail,
            holdout_summary=summary,
            replay_source=replay_source,
            source_projection_manifest=source_projection_manifest,
            repo_root=repo,
        )


def test_registered_price_gate_recomputes_mature_exit_and_realized_return() -> None:
    dates = pd.bdate_range("2026-08-31", periods=32).strftime("%Y%m%d").tolist()
    price = pd.DataFrame(
        {
            "date": dates,
            "analysis_open": [100.0] * 32,
            "analysis_close": [100.0, 101.0, *([100.0] * 28), 110.0, 120.0],
        }
    )
    event = {
        "price_input_canonical_sha256": "a" * 64,
        "holding_days": "30",
        "holding_session_index_offset": "29",
        "stock_id": "2330",
        "trigger_index": "0",
        "trigger_date": dates[0],
        "trigger_close": "100",
        "confirmation_index": "1",
        "confirmation_date": dates[1],
        "confirmation_close": "101",
        "entry_index": "2",
        "entry_price_basis": "analysis_open",
        "entry_date": dates[2],
        "entry_price": "100",
        "planned_exit_index": "31",
        "planned_exit_date": dates[31],
        "exit_index": "31",
        "exit_date": dates[31],
        "exit_price": "120",
        "exit_price_basis": "analysis_close",
        "exit_reason": "fixed_d30_close",
        "return_valid": "True",
        "right_censored": "False",
        "realized_return_pct": "20",
        "return_outcome": "win",
        "realized_return_ge20": "False",
        "operation_return_review_candidate_flag": "False",
        "operation_status": "mature_operation",
    }
    detail = pd.DataFrame([event])
    syncer._validate_detail_maturity_against_registered_prices(
        detail,
        observed_through=dates[-1],
        registered_prices={"2330": price},
        manifest_price_sha="a" * 64,
    )

    forged_return = detail.copy()
    forged_return.loc[0, "realized_return_pct"] = "19"
    with pytest.raises(RuntimeError, match=r"realized_return_pct.*disagrees"):
        syncer._validate_detail_maturity_against_registered_prices(
            forged_return,
            observed_through=dates[-1],
            registered_prices={"2330": price},
            manifest_price_sha="a" * 64,
        )


def test_markdown_status_table_must_match_canonical_csv_non_revenue_cells() -> None:
    readiness = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="new-time",
    )
    markdown = syncer.render_markdown(readiness, generated_at="new-time")
    syncer.validate_markdown_status_table_matches_csv(
        markdown,
        readiness,
        source_name="memory.md",
    )
    drifted = readiness.copy()
    drifted.loc[drifted["model_id"].eq("other_model"), "blocker"] = "drifted"
    with pytest.raises(RuntimeError, match="disagrees with canonical CSV"):
        syncer.validate_markdown_status_table_matches_csv(
            markdown,
            drifted,
            source_name="memory.md",
        )
