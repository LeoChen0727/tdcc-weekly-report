from __future__ import annotations

import csv
import io
import subprocess
from pathlib import Path

import pytest

from scripts.validate_revenue_unreacted_range_readiness_formal_sync_v2 import (
    ALLOWED_PATHS,
    EXPECTED_FIELDS,
    MARKDOWN_COMPARE_FIELDS,
    _validate_csv_semantics,
    _validate_markdown_semantics,
    _validate_phase,
    validate,
)


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = (
    ROOT
    / "scripts/validate_revenue_unreacted_range_readiness_formal_sync_v2.py"
)
FIELDS = (
    "generated_at",
    "model_id",
    "model_name_zh",
    "parity_status",
    "blocker",
    "operation_module_status",
    "daily_adapter_status",
    "formal_model_use_allowed",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "production_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "registry_current_model_pattern_count",
    "daily_adapter_row_count",
    "daily_adapter_data_row_count",
    "daily_adapter_sections",
    "status_note_zh",
)
STATUS_NOTE = (
    "九筆 anomaly disposition 與 disabled formal adapter preparation 均已完成；"
    "八筆 verified_real_extreme 保留於 Primary，6177 的衍生 attribution data "
    "error 已完成固定規則修復重跑；目前 promotion blocker 僅為 forward "
    "holdout v2 成熟度 0/20。"
)


def revenue_row(*, current: bool) -> dict[str, str]:
    row = {field: "" for field in FIELDS}
    row.update(
        {
            "generated_at": "new-time" if current else "base-time",
            "model_id": "revenue_unreacted_range",
            "model_name_zh": "營收爆發但股價尚未反應模型",
            "parity_status": "research_matrix_complete",
            "blocker": (
                "forward_holdout_v2_mature=0/20"
                if current
                else "legacy blocker"
            ),
            "operation_module_status": (
                "disabled_adapter_preparation_validated"
                if current
                else "research_matrix_complete_formal_adapter_not_started"
            ),
            "daily_adapter_status": (
                "disabled_no_runtime_artifact" if current else "not_started"
            ),
            "formal_model_use_allowed": "False",
            "approved_for_daily": "False",
            "approval_status": "not_started",
            "operation_module_id": (
                "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
                if current
                else ""
            ),
            "presentation_allowed": "False",
            "production_allowed": "False",
            "operation_directive_level": "no_operation_directive",
            "pdf_integration_status": "not_started",
            "packet_integration_status": "not_started",
            "registry_current_model_pattern_count": "0",
            "daily_adapter_row_count": "0",
            "daily_adapter_data_row_count": "0",
            "status_note_zh": STATUS_NOTE if current else "legacy note",
        }
    )
    return row


def other_row(*, generated_at: str = "base-time") -> dict[str, str]:
    row = {field: "" for field in FIELDS}
    row.update(
        {
            "generated_at": generated_at,
            "model_id": "other_model",
            "model_name_zh": "其他模型",
            "parity_status": "production_parity",
            "blocker": "none",
            "operation_module_status": "approved_operation_v1",
            "daily_adapter_status": "ready",
            "approved_for_daily": "True",
            "approval_status": "approved",
            "presentation_allowed": "True",
            "operation_directive_level": "approved_daily_operation_guidance",
            "pdf_integration_status": "pdf_integrated_daily_adapter",
            "packet_integration_status": "packet_integrated_daily_adapter",
        }
    )
    return row


def csv_bytes(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def markdown_bytes(rows: list[dict[str, str]]) -> bytes:
    header = "| " + " | ".join(MARKDOWN_COMPARE_FIELDS) + " |"
    separator = "| " + " | ".join("---" for _ in MARKDOWN_COMPARE_FIELDS) + " |"
    data_rows = [
        "| "
        + " | ".join(row.get(field, "") for field in MARKDOWN_COMPARE_FIELDS)
        + " |"
        for row in rows
    ]
    return (
        "# Model Operation Readiness\n\n## Status Table\n\n"
        + "\n".join([header, separator, *data_rows])
        + "\n"
    ).encode("utf-8")


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    return completed.stdout.strip()


def write_mirrors(repo: Path, csv_data: bytes, markdown_data: bytes) -> None:
    payloads = {
        "output/latest/model_operation_readiness_latest.csv": csv_data,
        "output/latest/model_operation_readiness_latest.md": markdown_data,
        "docs/latest/model_operation_readiness_latest.csv": csv_data,
        "docs/latest/model_operation_readiness_latest.md": markdown_data,
    }
    assert set(payloads) == ALLOWED_PATHS
    for logical_path, payload in payloads.items():
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


def initialized_sync_repo(tmp_path: Path) -> tuple[Path, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "Codex Test")
    git(repo, "config", "user.email", "codex-test@example.invalid")
    base_rows = [other_row(), revenue_row(current=False)]
    write_mirrors(repo, csv_bytes(base_rows), markdown_bytes(base_rows))
    git(repo, "add", "--", ".")
    git(repo, "commit", "-m", "base")
    base_sha = git(repo, "rev-parse", "HEAD")
    current_rows = [other_row(generated_at="unchanged-time"), revenue_row(current=True)]
    write_mirrors(repo, csv_bytes(current_rows), markdown_bytes(current_rows))
    return repo, base_sha


def test_exact_v2_row_and_markdown_pass() -> None:
    base = csv_bytes([other_row(), revenue_row(current=False)])
    current_rows = [other_row(generated_at="other-time"), revenue_row(current=True)]
    current = csv_bytes(current_rows)
    assert _validate_csv_semantics(base, current) == []
    assert _validate_markdown_semantics(markdown_bytes(current_rows), current) == []


def test_rejects_reuse_after_v2_authorization_is_consumed() -> None:
    consumed = csv_bytes([other_row(), revenue_row(current=True)])
    errors = _validate_csv_semantics(consumed, consumed)
    assert any("authorization is already consumed" in error for error in errors)


@pytest.mark.parametrize(
    ("field", "value"),
    (
        ("blocker", "anomaly_disposition_blockers=1"),
        ("operation_module_status", "formal_adapter_not_started"),
        ("daily_adapter_status", "ready"),
        ("operation_module_id", "wrong_module"),
        ("formal_model_use_allowed", "True"),
        ("approved_for_daily", "True"),
        ("presentation_allowed", "True"),
        ("production_allowed", "True"),
        ("daily_adapter_row_count", "1"),
        ("daily_adapter_data_row_count", "1"),
        ("daily_adapter_sections", "confirmed_operation"),
    ),
)
def test_rejects_readiness_or_permission_drift(field: str, value: str) -> None:
    base = csv_bytes([other_row(), revenue_row(current=False)])
    row = revenue_row(current=True)
    row[field] = value
    errors = _validate_csv_semantics(base, csv_bytes([other_row(), row]))
    assert any(field in error for error in errors), errors


def test_rejects_anomaly_closure_note_drift_without_reclassifying_sources() -> None:
    base = csv_bytes([other_row(), revenue_row(current=False)])
    row = revenue_row(current=True)
    row["status_note_zh"] = "forward holdout only"
    errors = _validate_csv_semantics(base, csv_bytes([other_row(), row]))
    assert any("verified_real_extreme" in error for error in errors)
    assert any("6177" in error for error in errors)


def test_rejects_non_revenue_drift_and_revenue_only_permission_leak() -> None:
    base = csv_bytes([other_row(), revenue_row(current=False)])
    changed_other = other_row(generated_at="allowed-new-time")
    changed_other["blocker"] = "changed"
    changed_other["formal_model_use_allowed"] = "False"
    errors = _validate_csv_semantics(
        base,
        csv_bytes([changed_other, revenue_row(current=True)]),
    )
    assert "non-revenue readiness rows drifted beyond generated_at" in errors
    assert any("revenue-only" in error for error in errors)


def test_rejects_markdown_csv_semantic_drift() -> None:
    rows = [other_row(), revenue_row(current=True)]
    csv_data = csv_bytes(rows)
    markdown_rows = [other_row(), revenue_row(current=True)]
    markdown_rows[1]["production_allowed"] = "True"
    errors = _validate_markdown_semantics(markdown_bytes(markdown_rows), csv_data)
    assert any("production_allowed disagrees" in error for error in errors)
    assert any("production_allowed must remain False" in error for error in errors)


def test_dedicated_validator_does_not_reimplement_source_business_gates() -> None:
    source = VALIDATOR.read_text(encoding="utf-8")
    for forbidden in (
        "anomaly_disposition_registry",
        "validate_revenue_unreacted_range_anomaly_dispositions.py",
        "validate_revenue_unreacted_range_operation_adapter.py",
        "revenue_unreacted_range_operation_adapter.py",
        "forward_holdout_v2_manifest",
        "pandas",
    ):
        assert forbidden not in source


def test_full_working_tree_phase_passes_exact_four(tmp_path: Path) -> None:
    repo, base_sha = initialized_sync_repo(tmp_path)
    assert validate(repo, base_sha, "working-tree") == []


def test_staged_phase_passes_exact_four_and_rejects_unstaged(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_sync_repo(tmp_path)
    git(repo, "add", "--", *sorted(ALLOWED_PATHS))
    assert _validate_phase(repo, base_sha, "staged") == []
    one_path = repo / sorted(ALLOWED_PATHS)[0]
    one_path.write_bytes(one_path.read_bytes() + b"unstaged\n")
    errors = _validate_phase(repo, base_sha, "staged")
    assert any("only staged tracked modifications" in error for error in errors)


def test_committed_phase_requires_one_direct_child_and_clean_status(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_sync_repo(tmp_path)
    git(repo, "add", "--", *sorted(ALLOWED_PATHS))
    git(repo, "commit", "-m", "sync")
    assert _validate_phase(repo, base_sha, "committed") == []
    extra = repo / "unexpected.txt"
    extra.write_text("unexpected\n", encoding="utf-8")
    errors = _validate_phase(repo, base_sha, "committed")
    assert any("must be clean" in error for error in errors)


def test_committed_phase_rejects_an_extra_committed_path(tmp_path: Path) -> None:
    repo, base_sha = initialized_sync_repo(tmp_path)
    (repo / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")
    git(repo, "add", "--", *sorted(ALLOWED_PATHS), "unexpected.txt")
    git(repo, "commit", "-m", "sync with extra path")
    errors = _validate_phase(repo, base_sha, "committed")
    assert any("unexpected=['unexpected.txt']" in error for error in errors)


def test_phase_rejects_subset_or_extra_path(tmp_path: Path) -> None:
    repo, base_sha = initialized_sync_repo(tmp_path)
    (repo / sorted(ALLOWED_PATHS)[0]).write_bytes(b"base replacement\n")
    extra = repo / "unexpected.txt"
    extra.write_text("unexpected\n", encoding="utf-8")
    errors = _validate_phase(repo, base_sha, "working-tree")
    assert any("exactly the four readiness mirrors" in error for error in errors)


def test_expected_field_fixture_covers_contract() -> None:
    assert EXPECTED_FIELDS["blocker"] == "forward_holdout_v2_mature=0/20"
    assert EXPECTED_FIELDS["daily_adapter_row_count"] == "0"
    assert EXPECTED_FIELDS["daily_adapter_data_row_count"] == "0"
