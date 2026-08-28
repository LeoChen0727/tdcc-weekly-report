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
