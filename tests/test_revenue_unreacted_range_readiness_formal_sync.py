from __future__ import annotations

import csv
import io
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_revenue_unreacted_range_readiness_formal_sync import (  # noqa: E402
    ALLOWED_PATHS,
    EXPECTED_BLOCKER,
    EXPECTED_HOLDOUT_ARTIFACT_VERSION,
    EXPECTED_PROMOTION_DECISION_ID,
    _validate_phase,
    validate_canonical_disabled_sources,
    validate_markdown_semantics,
    validate_semantics,
)


FIELDS = [
    "generated_at",
    "model_id",
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
]


def encoded(
    rows: list[dict[str, str]],
    fields: list[str] | None = None,
) -> bytes:
    selected_fields = fields or FIELDS
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=selected_fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(
        [{field: row.get(field, "") for field in selected_fields} for row in rows]
    )
    return stream.getvalue().encode()


def other(timestamp: str = "old") -> dict[str, str]:
    return {
        **dict.fromkeys(FIELDS, ""),
        "generated_at": timestamp,
        "model_id": "other",
        "approved_for_daily": "True",
        "presentation_allowed": "True",
    }


def revenue() -> dict[str, str]:
    return {
        **dict.fromkeys(FIELDS, ""),
        "generated_at": "new",
        "model_id": "revenue_unreacted_range",
        "parity_status": "research_matrix_complete",
        "blocker": EXPECTED_BLOCKER,
        "operation_module_status": (
            "research_matrix_complete_formal_adapter_not_started"
        ),
        "daily_adapter_status": "not_started",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "presentation_allowed": "False",
        "production_allowed": "False",
        "operation_directive_level": "no_operation_directive",
        "pdf_integration_status": "not_started",
        "packet_integration_status": "not_started",
    }


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def canonical_rows() -> tuple[dict[str, str], dict[str, str], list[dict[str, str]]]:
    promotion = {
        "model_id": "revenue_unreacted_range",
        "decision_id": EXPECTED_PROMOTION_DECISION_ID,
        "combined_exclusion_candidate_count": "9",
        "forward_holdout_first_interpretation_min_mature": "20",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "production_change": "False",
    }
    holdout = {
        "model_id": "revenue_unreacted_range",
        "artifact_version": EXPECTED_HOLDOUT_ARTIFACT_VERSION,
        "capture_id": "capture-v1",
        "artifact_row_key": "manifest",
        "primary_mature_count": "0",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "production_change": "False",
    }
    anomalies = [
        {
            "model_id": "revenue_unreacted_range",
            "operation_key": f"operation-{index}",
            "final_disposition": "unresolved_anomaly_candidate",
        }
        for index in range(9)
    ]
    return promotion, holdout, anomalies


def write_canonical_sources(
    repo: Path,
    promotion: dict[str, str],
    holdout: dict[str, str],
    anomalies: list[dict[str, str]],
) -> None:
    write_csv(
        repo / "config/revenue_unreacted_range_promotion_preparation_registry.csv",
        [promotion],
    )
    write_csv(
        repo
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv",
        [holdout],
    )
    write_csv(
        repo
        / "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
        anomalies,
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


def initialized_repo(tmp_path: Path) -> tuple[Path, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    for path in sorted(ALLOWED_PATHS):
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"base:{path}\n", encoding="utf-8")
    git(repo, "add", "--", ".")
    git(repo, "commit", "-m", "base")
    return repo, git(repo, "rev-parse", "HEAD")


def change_all_four(repo: Path) -> None:
    for path in sorted(ALLOWED_PATHS):
        target = repo / path
        target.write_text(f"changed:{path}\n", encoding="utf-8")


def test_accepts_only_timestamp_drift_for_non_revenue_and_disabled_revenue() -> None:
    assert validate_semantics(
        encoded([other()]),
        encoded([other("new"), revenue()]),
    ) == []


def test_accepts_only_canonical_permission_schema_extension_for_non_revenue() -> None:
    legacy_fields = [
        field
        for field in FIELDS
        if field not in {"formal_model_use_allowed", "production_allowed"}
    ]
    assert validate_semantics(
        encoded([other()], legacy_fields),
        encoded([other("new"), revenue()]),
    ) == []


def test_rejects_non_revenue_business_drift() -> None:
    changed = other("new")
    changed["approved_for_daily"] = "False"
    assert "non-revenue readiness rows drifted beyond generated_at" in validate_semantics(
        encoded([other()]),
        encoded([changed, revenue()]),
    )


def test_rejects_revenue_permission_or_exact_builder_blocker_drift() -> None:
    row = revenue()
    row["presentation_allowed"] = "True"
    row["blocker"] = (
        "unresolved_anomalies=9; forward_holdout_v2_mature=0/20; "
        "formal_adapter=not_started"
    )
    errors = validate_semantics(encoded([other()]), encoded([other("new"), row]))
    assert any("presentation_allowed must remain False" in error for error in errors)
    assert any("exact revenue_readiness_sync_3a_v1_20260828 blocker" in error for error in errors)


@pytest.mark.parametrize(
    "field_name",
    (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ),
)
def test_rejects_missing_or_true_committed_revenue_permission_fields(
    field_name: str,
) -> None:
    missing_fields = [field for field in FIELDS if field != field_name]
    missing_errors = validate_semantics(
        encoded([other()]),
        encoded([other("new"), revenue()], missing_fields),
    )
    assert any("missing required permission columns" in error for error in missing_errors)

    unsafe = revenue()
    unsafe[field_name] = "True"
    true_errors = validate_semantics(
        encoded([other()]),
        encoded([other("new"), unsafe]),
    )
    assert any(f"{field_name} must remain False" in error for error in true_errors)


@pytest.mark.parametrize("alias_value", ("True", "False"))
def test_rejects_non_revenue_permission_alias_drift(alias_value: str) -> None:
    changed = other("new")
    changed["production_allowed"] = alias_value
    errors = validate_semantics(
        encoded([other()]),
        encoded([changed, revenue()]),
    )
    assert any(
        "production_allowed is revenue-only" in error
        for error in errors
    )


def markdown_status(
    revenue_row: dict[str, str],
    fields: list[str] | None = None,
    *,
    other_rows: list[dict[str, str]] | None = None,
) -> bytes:
    selected_fields = fields or FIELDS
    rows = [*(other_rows or []), revenue_row]
    row_lines = "".join(
        f"| {' | '.join(row.get(field, '') for field in selected_fields)} |\n"
        for row in rows
    )
    return (
        "# Model Operation Readiness\n\n"
        "## Status Table\n\n"
        f"| {' | '.join(selected_fields)} |\n"
        f"| {' | '.join('---' for _ in selected_fields)} |\n"
        f"{row_lines}"
    ).encode()


def test_markdown_requires_all_four_false_permission_fields() -> None:
    assert validate_markdown_semantics(
        markdown_status(revenue(), other_rows=[other()])
    ) == []
    missing_fields = [
        field for field in FIELDS if field != "production_allowed"
    ]
    assert any(
        "missing required permission columns" in error
        for error in validate_markdown_semantics(
            markdown_status(revenue(), missing_fields)
        )
    )
    unsafe = revenue()
    unsafe["formal_model_use_allowed"] = "True"
    assert any(
        "formal_model_use_allowed must remain False" in error
        for error in validate_markdown_semantics(markdown_status(unsafe))
    )


@pytest.mark.parametrize("alias_value", ("True", "False"))
def test_markdown_rejects_non_revenue_permission_alias(alias_value: str) -> None:
    aliased = other()
    aliased["formal_model_use_allowed"] = alias_value

    assert any(
        "formal_model_use_allowed is revenue-only" in error
        for error in validate_markdown_semantics(
            markdown_status(revenue(), other_rows=[aliased])
        )
    )


def test_rejects_missing_duplicate_or_blank_model_id() -> None:
    assert any(
        "exactly one" in error
        for error in validate_semantics(encoded([other()]), encoded([other("new")]))
    )
    assert any(
        "exactly one" in error
        for error in validate_semantics(
            encoded([other()]),
            encoded([other("new"), revenue(), revenue()]),
        )
    )
    blank = other("new")
    blank["model_id"] = ""
    assert any(
        "blank model_id" in error
        for error in validate_semantics(
            encoded([other()]),
            encoded([blank, revenue()]),
        )
    )


def test_canonical_one_shot_evidence_accepts_exact_nine_and_zero_of_twenty(
    tmp_path: Path,
) -> None:
    promotion, holdout, anomalies = canonical_rows()
    write_canonical_sources(tmp_path, promotion, holdout, anomalies)
    assert validate_canonical_disabled_sources(tmp_path) == []


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("blank_anomaly_key", "blank operation_key"),
        ("duplicate_anomaly_key", "duplicate operation_key"),
        ("duplicate_holdout_identity", "duplicate versioned identities"),
        ("permission_true", "production_change must remain False"),
        ("wrong_anomaly_count", "exact 9 distinct unresolved rows"),
        ("mature_count", "mature count must remain 0"),
    ),
)
def test_canonical_one_shot_evidence_rejects_identity_count_and_permission_mutations(
    tmp_path: Path,
    mutation: str,
    message: str,
) -> None:
    promotion, holdout, anomalies = canonical_rows()
    holdout_rows = [holdout]
    if mutation == "blank_anomaly_key":
        anomalies[0]["operation_key"] = ""
    elif mutation == "duplicate_anomaly_key":
        anomalies[1]["operation_key"] = anomalies[0]["operation_key"]
    elif mutation == "duplicate_holdout_identity":
        holdout_rows.append(dict(holdout))
    elif mutation == "permission_true":
        promotion["production_change"] = "True"
    elif mutation == "wrong_anomaly_count":
        anomalies.pop()
    elif mutation == "mature_count":
        holdout["primary_mature_count"] = "1"
    write_csv(
        tmp_path
        / "config/revenue_unreacted_range_promotion_preparation_registry.csv",
        [promotion],
    )
    write_csv(
        tmp_path
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv",
        holdout_rows,
    )
    write_csv(
        tmp_path
        / "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
        anomalies,
    )
    assert any(
        message in error
        for error in validate_canonical_disabled_sources(tmp_path)
    )


def test_working_tree_phase_requires_exact_four_and_no_staged_or_untracked_paths(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_repo(tmp_path)
    change_all_four(repo)
    assert _validate_phase(repo, base_sha, "working-tree") == []

    extra = repo / "unexpected.txt"
    extra.write_text("unexpected\n", encoding="utf-8")
    errors = _validate_phase(repo, base_sha, "working-tree")
    assert any("unexpected=['unexpected.txt']" in error for error in errors)

    extra.unlink()
    git(repo, "add", "--", sorted(ALLOWED_PATHS)[0])
    errors = _validate_phase(repo, base_sha, "working-tree")
    assert "working-tree sync must not contain staged changes" in errors


def test_staged_phase_rejects_subset_unstaged_and_untracked_mutations(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_repo(tmp_path)
    change_all_four(repo)
    git(repo, "add", "--", *sorted(ALLOWED_PATHS))
    assert _validate_phase(repo, base_sha, "staged") == []

    one_path = repo / sorted(ALLOWED_PATHS)[0]
    one_path.write_text("unstaged mutation\n", encoding="utf-8")
    errors = _validate_phase(repo, base_sha, "staged")
    assert any("no unstaged or untracked changes" in error for error in errors)

    git(repo, "add", "--", sorted(ALLOWED_PATHS)[0])
    git(repo, "reset", "--", sorted(ALLOWED_PATHS)[-1])
    errors = _validate_phase(repo, base_sha, "staged")
    assert any("missing=" in error for error in errors)


def test_committed_phase_requires_one_direct_child_exact_four_and_clean_status(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_repo(tmp_path)
    change_all_four(repo)
    git(repo, "add", "--", *sorted(ALLOWED_PATHS))
    git(repo, "commit", "-m", "sync")
    assert _validate_phase(repo, base_sha, "committed") == []

    (repo / "untracked.txt").write_text("unexpected\n", encoding="utf-8")
    errors = _validate_phase(repo, base_sha, "committed")
    assert "committed sync worktree and index must be clean" in errors
    (repo / "untracked.txt").unlink()

    (repo / sorted(ALLOWED_PATHS)[0]).write_text("second commit\n", encoding="utf-8")
    git(repo, "add", "--", sorted(ALLOWED_PATHS)[0])
    git(repo, "commit", "-m", "second")
    errors = _validate_phase(repo, base_sha, "committed")
    assert "committed sync must be exactly one direct child of base_sha" in errors
