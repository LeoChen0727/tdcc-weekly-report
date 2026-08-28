from __future__ import annotations

from pathlib import Path

import pytest

from scripts.validate_repo_production_inventory import (
    REVENUE_READINESS_FORMAL_SYNC_PRODUCER,
    REVENUE_READINESS_FORMAL_SYNC_PRODUCER_TOKEN,
    REVENUE_READINESS_LEGACY_BUILDER,
    REVENUE_READINESS_FORMAL_SYNC_PUSH,
    validate_revenue_readiness_formal_sync_workflow_text,
)


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/revenue_unreacted_range_readiness_formal_sync.yml"
SPEC = ROOT / "docs/specs/revenue_unreacted_range_readiness_formal_sync_v1.md"
TEXT = WORKFLOW.read_text(encoding="utf-8")
SPEC_TEXT = SPEC.read_text(encoding="utf-8")


def test_current_workflow_passes_fail_closed_inventory_guard() -> None:
    assert validate_revenue_readiness_formal_sync_workflow_text(TEXT) == []


def test_target_branch_is_never_checked_out_or_executed() -> None:
    assert 'ref: "${{ inputs.target_branch }}"' not in TEXT
    assert "ref: ${{ inputs.target_branch }}" not in TEXT
    assert "ref: main" in TEXT
    assert 'ref: "${{ inputs.expected_main_sha }}"' in TEXT
    assert TEXT.count("persist-credentials: false") == 2
    assert "git merge-base" not in TEXT
    assert (
        "READINESS_SYNC_TARGET_BRANCH: "
        "codex/revenue-unreacted-range-readiness-formal-sync-3a-v1-20260828"
    ) in TEXT


def test_exact_producer_blocker_four_disabled_meanings_and_versioned_counts() -> None:
    assert (
        TEXT.count(f"python -B {REVENUE_READINESS_FORMAL_SYNC_PRODUCER}")
        == 1
    )
    assert REVENUE_READINESS_LEGACY_BUILDER not in TEXT
    assert TEXT.count(REVENUE_READINESS_FORMAL_SYNC_PRODUCER_TOKEN) == 2
    assert REVENUE_READINESS_FORMAL_SYNC_PRODUCER_TOKEN in SPEC_TEXT
    for token in (
        "registered monthly and\nsource validators",
        "tests/test_revenue_unreacted_range_forward_holdout_v2.py",
        "tests/test_sync_revenue_unreacted_range_operation_readiness.py",
        "A fuzzy `-k` expression is forbidden",
        "test_current_canonical_sources_build_exact_disabled_revenue_row",
    ):
        assert token in SPEC_TEXT
    assert (
        "anomaly_disposition_blockers=9; unresolved_anomalies=9; "
        "forward_holdout_v2_mature=0/20; formal_adapter=not_started"
    ) in TEXT
    for token in (
        "exception_id=revenue_unreacted_range_readiness_formal_sync_3a_v1_20260828",
        "authorization_reference=user_authorized_3A_3C_20260828",
        "contract_version=revenue_readiness_sync_3a_v1_20260828",
        "formal_model_use_allowed=False",
        "approved_for_daily=False",
        "presentation_allowed=False",
        "production_allowed=False",
    ):
        assert token in TEXT
        assert token in SPEC_TEXT


def test_builder_runtime_dependencies_are_explicit() -> None:
    assert (
        "python -m pip install --disable-pip-version-check pandas requests tabulate"
        in TEXT
    )


def test_committed_phase_remote_identity_and_key_cleanup_are_final() -> None:
    marker = "- name: Push only validated commit to inert codex target"
    before, final = TEXT.split(marker, 1)
    assert "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY" not in before
    assert TEXT.count("git push ") == 1
    assert REVENUE_READINESS_FORMAL_SYNC_PUSH in final
    assert TEXT.count("--phase committed") == 2
    assert "remote_main_before" in final
    assert "remote_target_before" in final
    assert "remote_main_after" in final
    assert "remote_target_after" in final
    assert '[ "$remote_target_after" = "$SYNC_COMMIT_SHA" ]' in final
    assert "trap 'rm -f \"$key\"' EXIT" in final
    assert "rm -f \"$key\"" in final
    assert "trap - EXIT" in final
    assert "\n      - name:" not in final
    assert "\n      - uses:" not in final


def test_exact_four_bundle_and_clean_state_are_revalidated() -> None:
    paths = (
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/model_operation_readiness_latest.md",
        "docs/latest/model_operation_readiness_latest.csv",
        "docs/latest/model_operation_readiness_latest.md",
    )
    for path in paths:
        assert TEXT.count(path) >= 4
    assert "sha256sum --check SHA256SUMS" in TEXT
    assert "find \"$bundle\" -type f -printf '%P\\n' | sort" in TEXT
    assert TEXT.count("git status --porcelain=v1 -z --untracked-files=all") == 2


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    (
        (
            lambda text: text.replace(
                REVENUE_READINESS_FORMAL_SYNC_PUSH,
                REVENUE_READINESS_FORMAL_SYNC_PUSH + "\n          git push origin HEAD:extra",
            ),
            "exactly one git push",
        ),
        (
            lambda text: text + "\n      - name: Unexpected post-push step\n        run: true\n",
            "final workflow step",
        ),
        (
            lambda text: text.replace(
                "- name: Push only validated commit to inert codex target",
                "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: early\n      "
                "- name: Push only validated commit to inert codex target",
            ),
            "exposes deploy key before final push step",
        ),
        (
            lambda text: text.replace(
                "READINESS_SYNC_TARGET_BRANCH: "
                "codex/revenue-unreacted-range-readiness-formal-sync-3a-v1-20260828",
                "READINESS_SYNC_TARGET_BRANCH: codex/arbitrary-target",
            ),
            "target is not exact and immutable",
        ),
        (
            lambda text: text.replace(
                'ref: "${{ inputs.expected_main_sha }}"',
                'ref: "${{ inputs.target_branch }}"',
            ),
            "must never checkout target code",
        ),
        (
            lambda text: text.replace("sha256sum --check SHA256SUMS", "true"),
            "independently verify bundle hashes",
        ),
        (
            lambda text: text.replace(
                f"python -B {REVENUE_READINESS_FORMAL_SYNC_PRODUCER}",
                f"python -B {REVENUE_READINESS_LEGACY_BUILDER}",
            ),
            "legacy broad readiness builder",
        ),
        (
            lambda text: text.replace(
                REVENUE_READINESS_FORMAL_SYNC_PRODUCER_TOKEN,
                "producer=mutated.py",
                1,
            ),
            "exact producer token",
        ),
        (
            lambda text: text.replace("trap 'rm -f \"$key\"' EXIT", "true"),
            "fail-closed key cleanup",
        ),
        (
            lambda text: text.replace(
                "anomaly_disposition_blockers=9; ",
                "",
            ),
            "exact builder blocker",
        ),
        (
            lambda text: text.replace(
                REVENUE_READINESS_FORMAL_SYNC_PUSH,
                REVENUE_READINESS_FORMAL_SYNC_PUSH.replace(
                    "git push ", "git push --force "
                ),
            ),
            "non-force push",
        ),
    ),
)
def test_workflow_guard_rejects_security_boundary_mutations(
    mutation,
    expected_error: str,
) -> None:
    errors = validate_revenue_readiness_formal_sync_workflow_text(mutation(TEXT))
    assert any(expected_error in error for error in errors), errors


def test_workflow_does_not_invoke_forbidden_surfaces() -> None:
    for token in (
        "run_chatgpt_daily_" + "report_entrypoint",
        "daily_full_" + "pipeline",
        "gh workflow run",
        "clasp ",
    ):
        assert token not in TEXT.lower()
    assert "\n  schedule:" not in TEXT
    assert "\n  push:" not in TEXT
