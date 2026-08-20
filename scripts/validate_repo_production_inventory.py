from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
PR_SAFE_BASE_GUARD_WORKFLOW = ".github/workflows/individual_stock_pr_validation.yml"
PR_SAFE_BASE_GUARD_SCRIPT = "scripts/validate_repo_production_inventory.py"
PR_SAFE_REPOSITORY = "LeoChen0727/tdcc-weekly-report"
PR_SAFE_CHECKOUT_ACTION = (
    "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803"
)
PR_SAFE_SETUP_PYTHON_ACTION = (
    "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1"
)
PR_SAFE_EXPECTED_ACTION_USES = (
    PR_SAFE_CHECKOUT_ACTION,
    PR_SAFE_SETUP_PYTHON_ACTION,
    PR_SAFE_CHECKOUT_ACTION,
)
PR_SAFE_GUARD_JOB_ID = "pr-safe-base-audit-runner"
PR_SAFE_GUARD_JOB_NAME = "pr-safe-trust-root-self-change-guard"
PR_SAFE_GUARD_JOB_RUNS_ON = "ubuntu-latest"
PR_SAFE_GUARD_JOB_TIMEOUT_MINUTES = "10"
PR_SAFE_GUARD_JOB_IF_BLOCK = (
    "    if: >-",
    "      github.event_name == 'pull_request_target' &&",
    "      github.event.pull_request.base.ref == 'main' &&",
    "      github.event.pull_request.base.repo.full_name == github.repository",
)
PR_SAFE_GUARD_STEP_NAMES = (
    "Checkout pull request base only",
    "Fetch pull request head object without checkout",
    "Validate trust-root self-change from base code",
)
PR_SAFE_REQUIRED_CHECK_CONTEXT = "individual-stock-pr-validation"
PR_SAFE_TARGET_SKIP_CHECK_NAME = (
    "individual-stock-pr-validation-pull-request-target-skip"
)
PR_SAFE_REGULAR_JOB_NAME_EXPRESSION = (
    "${{ github.event_name == 'pull_request' && "
    "'individual-stock-pr-validation' || "
    "'individual-stock-pr-validation-pull-request-target-skip' }}"
)
PR_SAFE_READ_ONLY_PERMISSIONS = {"contents": "read"}
PR_STATIC_DEPENDENCY_STEP_NAME = "Install PR static validation dependencies"
PR_STATIC_DEPENDENCY_COMMAND = (
    "python -m pip install --disable-pip-version-check pytest pandas requests "
    "PyYAML==6.0.2 pypdf"
)
PR_STATIC_VALIDATION_STEP_NAME = "Validate repository static contracts"
PR_STATIC_VALIDATION_COMMANDS = (
    "python scripts/validate_apps_script_workflow_triggers.py",
    "python scripts/validate_repo_production_inventory.py",
    "python scripts/validate_repo_file_lifecycle_inventory.py",
    "python scripts/validate_repo_hidden_coupling_audit.py",
    "python scripts/validate_daily_model_background_data_registry.py",
    "python scripts/validate_repo_semantic_integrity.py",
    "python scripts/validate_repo_code_isolation_policy.py",
    "python scripts/validate_model_research_workflow_isolation.py",
    "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    "python scripts/validate_daily_pdf_role_manifest_contract.py",
    "python scripts/validate_pdf_production_inventory.py --phase prebuild",
    "python scripts/validate_daily_production_boundaries.py",
)
PR_SAFE_AUTHORIZATION_PATH = (
    "config/daily_model_pr_safe_self_migration_authorizations.csv"
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH = (
    "config/repo_file_lifecycle_semantic_migrations.csv"
)
PR_SAFE_TRUST_ROOT_APPROVAL_LABEL = "trust-root-maintenance-approved"
PR_SAFE_TRUST_ROOT_PATHS = frozenset(
    {
        ".github/workflows/individual_stock_pr_validation.yml",
        "scripts/validate_repo_production_inventory.py",
        "scripts/validate_repo_advanced_integrity_pr_safe.py",
        "scripts/validate_daily_published_model_snapshots_pr_safe.py",
        "config/daily_model_pr_safe_self_migration_authorizations.csv",
        "config/repo_file_lifecycle_semantic_migrations.csv",
    }
)

PR_SAFE_LEGACY_REPLAY_IMMUTABLE_PATHS = frozenset(
    {
        PR_SAFE_BASE_GUARD_WORKFLOW,
        PR_SAFE_BASE_GUARD_SCRIPT,
        PR_SAFE_AUTHORIZATION_PATH,
        PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
    }
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_COLUMNS = (
    "migration_id",
    "status",
    "approval_reference",
    "row_path",
    "column",
    "base_value_sha256",
    "current_value_sha256",
    "added_values",
    "removed_values",
    "scope",
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_STATUS = "preauthorized"
PR_SAFE_LIFECYCLE_AUTHORIZATION_SCOPE = "pr462_research_lifecycle_only"
PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS = frozenset(
    {
        ("scripts/build_model_data_independence_audit.py", "reads_artifact"),
        ("scripts/build_revenue_unreacted_range_research.py", "reads_artifact"),
    }
)
PR_SAFE_AUTHORIZATION_COLUMNS = (
    "migration_id",
    "status",
    "approval_reference",
    "base_helper_sha256",
    "current_helper_sha256",
    "current_test_sha256",
    "changed_paths",
)
PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID = (
    "additive-research-validation-registration-pr-safe-v4"
)
PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID = (
    "input_bound_in_process_independent_validator"
)
PR_SAFE_INPUT_BOUND_VALIDATOR_STAGE_A_MIGRATION_ID = (
    "input-bound-validator-pr-safe-control-plane-stage-a-v1"
)
PR_SAFE_ADVANCED_HELPER = "scripts/validate_repo_advanced_integrity_pr_safe.py"
PR_SAFE_ADVANCED_TEST = "tests/test_repo_advanced_integrity_pr_safe.py"
PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY = "config/repo_file_lifecycle_inventory.csv"
PR_SAFE_AUTHORIZED_STAGE1_PATHS = frozenset(
    {
        PR_SAFE_ADVANCED_HELPER,
        PR_SAFE_ADVANCED_TEST,
        PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY,
    }
)
PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS = frozenset(
    {
        ".github/workflows/research_backtest_pipeline.yml",
        "config/apps_script_research_dispatch_inputs.csv",
        "config/repo_file_lifecycle_inventory.csv",
        "scripts/validate_apps_script_workflow_triggers.py",
        PR_SAFE_ADVANCED_HELPER,
        "tests/test_daily_production_boundaries.py",
        PR_SAFE_ADVANCED_TEST,
    }
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID = (
    "local-validation-replay-advanced-integrity-pr-safe-v2"
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS = frozenset(
    {PR_SAFE_ADVANCED_HELPER, PR_SAFE_ADVANCED_TEST}
)
PR_SAFE_ADVANCED_BASE_LIFECYCLE_INVENTORY_SHA256 = (
    "45eae9722c4d8587ff483a8e550eb5054cc8a6ab26a836d7f8f80e30a9c3a3d7"
)
PR_SAFE_ADVANCED_CURRENT_LIFECYCLE_INVENTORY_SHA256 = (
    "69831c7ef8b922ddb763af94cbf4df694ee2d981c7a7d475567f67587ed07ce5"
)
PR_SAFE_INPUT_BOUND_BASE_LIFECYCLE_INVENTORY_SHA256 = (
    "99daaa3785f949b5efce848e7e8bcbe4a79ae08aad15ce5d008f1e3cc994327d"
)
PR_SAFE_INPUT_BOUND_CURRENT_LIFECYCLE_INVENTORY_SHA256 = (
    "6bd6d3c81eccbcfb929112ad713de7130d02829f9e46832055b88c4bd8be1e29"
)
PR_SAFE_SNAPSHOT_MIGRATION_ID = "daily-full-checkpoint-replay-snapshot-pr-safe-v1"
PR_SAFE_SNAPSHOT_HELPER = "scripts/validate_daily_published_model_snapshots_pr_safe.py"
PR_SAFE_SNAPSHOT_TEST = "tests/test_daily_published_model_snapshots_pr_safe.py"
PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY = "config/repo_file_lifecycle_inventory.csv"
PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS = frozenset(
    {
        PR_SAFE_SNAPSHOT_HELPER,
        PR_SAFE_SNAPSHOT_TEST,
        PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY,
    }
)
PR_SAFE_SNAPSHOT_SELF_STRICT_SURFACES = frozenset({PR_SAFE_SNAPSHOT_HELPER})
PR_SAFE_SNAPSHOT_BASE_CONTENT_REF_SHA = (
    "6a37e30797006397146bdbc6d29c51560c48ef9a"
)
PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256 = (
    "745dd9582fc1d272615c57990ac6173157c33120e7da51e787dd3122e8c16532"
)
PR_SAFE_SNAPSHOT_BASE_TEST_SHA256 = (
    "85e192cb342cd135cc3a368be701abe39945a7c07c34ecd3d5271b040f092651"
)
PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256 = (
    "9021ef2f921514d1bc781aaf4adec87a9a573630153a9a4d28536dc35daf0bf3"
)
PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256 = (
    "05d47d133b2afe0654c1c9755c632ecafdd6b12e5f9311d05a12c105b835d641"
)
PR_SAFE_SNAPSHOT_BASE_LIFECYCLE_INVENTORY_SHA256 = (
    "88fb62d8b1ea278b52939a433f1cdf210cdf081fe89a287739d8900f5d286e88"
)
PR_SAFE_SNAPSHOT_CURRENT_LIFECYCLE_INVENTORY_SHA256 = (
    "45eae9722c4d8587ff483a8e550eb5054cc8a6ab26a836d7f8f80e30a9c3a3d7"
)
PR_SAFE_SNAPSHOT_REQUIRED_MODE = "100644"
PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS = (
    PR_SAFE_AUTHORIZED_STAGE1_PATHS
    | PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS
    | PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID = (
    "local-validation-replay-f-routing-portable-test-v2"
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_CONTENT_REF_SHA = (
    "fef0cd7787643ce4d4f53d5890e8c1b9ed3f193d"
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES = frozenset(
    {"config/repo_production_inventory.csv"}
)
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH = {
    "config/git_worktree_materialization_contract.csv": (
        "2dd3c88177059831bb8ad88745d6aa4d9a0991ec1d69f64fb0d4c506a5b332a8"
    ),
    "config/repo_file_lifecycle_inventory.csv": (
        "adf32adc13882d556d2c54595ca49241df36f8c30e2528cb4f4411aad55974b5"
    ),
    "config/repo_production_inventory.csv": (
        "675f8d6abdd5bbcc7f911739ee1d3f9439353cfc6375b415070f4da4ce7dd533"
    ),
    "scripts/git_worktree_safety.py": (
        "926b33cc3e7716d1ac9a7ec4f716e6ddb78c3f16058604a92088c1699e58e760"
    ),
    "scripts/run_local_daily_full_validation_replay.py": None,
    "scripts/validate_git_worktree_safety.py": (
        "84bdcb07691a8ee1384d23d61d1e6658533591412b694d577a47cae9c2cde2bc"
    ),
    "scripts/validate_local_daily_full_validation_replay.py": None,
    "tests/test_git_worktree_safety.py": (
        "1c880196af21e7b2bde7fc2aa989c7aa2762822ee1585344239305278d80f1ce"
    ),
}
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_SHA256_BY_PATH = {
    "config/git_worktree_materialization_contract.csv": (
        "8c3505199bee61e045bfee06c80b51802c203b0da2a9f8d62c384049e48515f3"
    ),
    "config/repo_file_lifecycle_inventory.csv": (
        "99daaa3785f949b5efce848e7e8bcbe4a79ae08aad15ce5d008f1e3cc994327d"
    ),
    "config/repo_production_inventory.csv": (
        "4f155b6568f60646608ed8c0be596ceb9ba4521afb2e0da82d8b2deea2c9d89b"
    ),
    "scripts/git_worktree_safety.py": (
        "8113a2a6c8de90c57696ea8bc6f8ed883d83e10e2f6e3268030828faf2d91828"
    ),
    "scripts/run_local_daily_full_validation_replay.py": (
        "2293c0eae889e7a494a14187afb61d9d2093ae4d8eca9471775f704e28c7be63"
    ),
    "scripts/validate_git_worktree_safety.py": (
        "bdb16b6550bbf3ba70a8822af28c5cf2e34fdc7bb807b11729d86064d864808b"
    ),
    "scripts/validate_local_daily_full_validation_replay.py": (
        "65cbd4bc2273d01484b33aa844282afcc66db00820439d52b446618e4886ea2f"
    ),
    "tests/test_git_worktree_safety.py": (
        "b9c8c69fefb86ab02ba8cf21542730f63ae94e32b865035427c8225493167cf3"
    ),
}
PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS = frozenset(
    PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_ID = (
    "daily-full-checkpoint-replay-20260807-v1"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES = frozenset(
    {".github/workflows/daily_full_pipeline.yml"}
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": (
        "09bf4b8e3fd5fcc1861f132015c758fd25c4574584efcf257881385cf719d67e"
    ),
    ".github/workflows/daily_full_validation_replay_20260807.yml": None,
    "config/repo_file_lifecycle_inventory.csv": (
        "69831c7ef8b922ddb763af94cbf4df694ee2d981c7a7d475567f67587ed07ce5"
    ),
    "config/repo_production_inventory.csv": (
        "359a3419a6ad7e043d9649a0efe89e1b4ed40365d1640f7d3d8fa06909f6092a"
    ),
    "scripts/daily_full_validation_replay_checkpoint.py": None,
    "scripts/run_daily_full_validation_replay.py": None,
    "scripts/validate_daily_full_validation_replay.py": None,
    "scripts/validate_repo_file_lifecycle_inventory.py": (
        "81030020cd36377676a1c11c6827a67ecbc09d3edf1f152ad6269ff3cdcdd882"
    ),
    "tests/test_daily_full_validation_replay.py": None,
}
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": (
        "8a1b02295fb3e78420952fda03de86007b1ae0bd48033dea4467aec5085e42e3"
    ),
    ".github/workflows/daily_full_validation_replay_20260807.yml": (
        "9ba1da323f7aa4ed0501e702abbd14d511cf697138c247bdb92e033f43a96831"
    ),
    "config/repo_file_lifecycle_inventory.csv": (
        "adf32adc13882d556d2c54595ca49241df36f8c30e2528cb4f4411aad55974b5"
    ),
    "config/repo_production_inventory.csv": (
        "675f8d6abdd5bbcc7f911739ee1d3f9439353cfc6375b415070f4da4ce7dd533"
    ),
    "scripts/daily_full_validation_replay_checkpoint.py": (
        "d6f02d338095bcf6c9d6cafd0df53e26a974a380dbe5dd24e0c5fcd01a88b348"
    ),
    "scripts/run_daily_full_validation_replay.py": (
        "94707cb4029487f3c119970c7ef2a2476442e7926a70a20f0d8dcede9b602703"
    ),
    "scripts/validate_daily_full_validation_replay.py": (
        "4ec1e81b5781c91d0f0b0a9eec754f29c125c79b4e6c20e04e4474a1fe69ec3b"
    ),
    "scripts/validate_repo_file_lifecycle_inventory.py": (
        "bbdd0793bab756c04d5536ef7c9aaec75569a9f78ad5eaa3deff012e49e71aab"
    ),
    "tests/test_daily_full_validation_replay.py": (
        "b2e5f48050a7d14b964348511655e1e1e2ef89e11899fe2715945d4fe47a3ee7"
    ),
}
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS = frozenset(
    PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_PATH = (
    "config/repo_file_lifecycle_inventory.csv"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_OVERLAP_ROW = (
    "scripts/validate_repo_production_inventory.py"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PRE_STAGE_F_LIFECYCLE_SHA256 = (
    "45eae9722c4d8587ff483a8e550eb5054cc8a6ab26a836d7f8f80e30a9c3a3d7"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STAGE_F_LIFECYCLE_SHA256 = (
    "69831c7ef8b922ddb763af94cbf4df694ee2d981c7a7d475567f67587ed07ce5"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BRANCH_LIFECYCLE_SHA256 = (
    "b297a44b3e898e6f896893607b6e88d62b0fe3c2aefb57aa463caef3ed384429"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_INTEGRATED_LIFECYCLE_SHA256 = (
    "e4e7ae5fa26c90545ddcd8f12aae8a5c0a343e2657d44f081b4c7b3088ae3c1a"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_ANCHOR = (
    "      - name: Build volume attack theme layer\n"
)
PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_INSERTION = """      - name: Create failure-safe immutable pre-step41 checkpoint
        shell: bash
        run: |
          set -euo pipefail
          python -B scripts/run_daily_full_validation_replay.py capture-production-checkpoint \\
            --repo-root . \\
            --runner-temp "$RUNNER_TEMP/daily-full-pre-step41-checkpoint-work" \\
            --replay-date "$EXPECTED_MAIN_PRICE_DATE" \\
            --source-sha "$GITHUB_SHA" \\
            --run-id "$GITHUB_RUN_ID" \\
            --bundle-dir "$RUNNER_TEMP/daily-full-pre-step41-checkpoint"

      - name: Upload failure-safe immutable pre-step41 checkpoint
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: daily-full-pre-step41-checkpoint-${{ github.run_id }}-${{ github.run_attempt }}
          path: ${{ runner.temp }}/daily-full-pre-step41-checkpoint/
          if-no-files-found: error
          retention-days: 30

"""
PR_SAFE_RETAINED_AUTHORIZATION_ROWS = (
    {
        "migration_id": "additive-research-validation-registration-pr-safe-v1",
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_pr_safe_stage0_control_plane_trust_root_20260803"
        ),
        "base_helper_sha256": (
            "72f79f37dd8a4ece163f9f6e3c7f299f3243c8c44b66442c992bc54f38126315"
        ),
        "current_helper_sha256": (
            "b09d8063512dad3c771789e8e546ab4c1541b5f1b1ca8cb59a1bfcfb3c35982a"
        ),
        "current_test_sha256": (
            "72e308d5e8757878958ba21529298001c1888a72e9e837ed9d6057c3d8e2f50b"
        ),
        "changed_paths": f"{PR_SAFE_ADVANCED_HELPER};{PR_SAFE_ADVANCED_TEST}",
    },
    {
        "migration_id": "additive-research-validation-registration-pr-safe-v2",
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_stage1_v2_preauthorization_20260803"
        ),
        "base_helper_sha256": (
            "72f79f37dd8a4ece163f9f6e3c7f299f3243c8c44b66442c992bc54f38126315"
        ),
        "current_helper_sha256": (
            "5a05baa9d505152c5bacf456116be4c896db08e55a14a37c1d46074a810a8e8c"
        ),
        "current_test_sha256": (
            "557d085bfa04221a9dc0bf826b783f8de1fa9b6e026bdcba181d2d1f836fd234"
        ),
        "changed_paths": f"{PR_SAFE_ADVANCED_HELPER};{PR_SAFE_ADVANCED_TEST}",
    },
)
PR_SAFE_CONSUMED_AUTHORIZATION_ROWS = (
    {
        "migration_id": "additive-research-validation-registration-pr-safe-v3",
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_stage1_v3_collision_free_fixture_preauthorization_20260803"
        ),
        "base_helper_sha256": (
            "5a05baa9d505152c5bacf456116be4c896db08e55a14a37c1d46074a810a8e8c"
        ),
        "current_helper_sha256": (
            "bfc01dc51857f2944b88475d4ae8f460fc930a7c0ea75b1f1345b9e7e44d463c"
        ),
        "current_test_sha256": (
            "d99d14062787e06360e9956b645851c2b84a01ec7c4c55a48fd6c2fcb519defe"
        ),
        "changed_paths": f"{PR_SAFE_ADVANCED_HELPER};{PR_SAFE_ADVANCED_TEST}",
    },
)
PR_SAFE_REGULAR_BLOB_MODES = frozenset({"100644", "100755"})
PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE = re.compile(
    r"(?im)(?:^|[{,])\s*['\"]?(?:checks|statuses)['\"]?\s*:\s*"
    r"['\"]?write['\"]?(?![A-Za-z0-9_-])|"
    r"^\s*permissions\s*:\s*['\"]?write-all['\"]?(?![A-Za-z0-9_-])"
)
DAILY_WORKFLOW = ".github/workflows/daily_full_pipeline.yml"
PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY = "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY"
PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION = (
    "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
)
PRODUCTION_ARTIFACT_WRITE_SSH_KEY = (
    f"ssh-key: {PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION}"
)
PRODUCTION_ARTIFACT_PERSIST_CREDENTIALS = "persist-credentials: true"
PRODUCTION_ARTIFACT_WRITE_PREFLIGHT_NAME = (
    "Require production artifact write deploy key"
)
PRODUCTION_ARTIFACT_WRITE_SECRET_GUARD = (
    'if [ -z "${PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}" ]; then'
)
ARTIFACT_PUSH_JOB_MARKERS = (
    "git commit",
    "git push",
    "ci_push_with_retry.sh",
)

REQUIRED_COLUMNS = {
    "path",
    "kind",
    "owner",
    "status",
    "purpose",
    "allowed_workflows",
    "allowed_stage_patterns",
}

VALID_KINDS = {"python", "test_python", "workflow", "executable_script"}
VALID_STATUSES = {"active", "manual_diagnostic", "legacy_deprecated"}

VALID_OWNERS = {
    "daily_production",
    "research_backtest",
    "tdcc_weekly",
    "individual_stock",
    "catalyst_event",
    "market_risk",
    "warrant",
    "official_price_data",
    "current_holdings",
    "diagnostics",
    "repo_infrastructure",
}

WORKFLOW_ALLOWED_OWNERS = {
    ".github/workflows/current_holdings_pattern.yml": {"current_holdings", "repo_infrastructure"},
    ".github/workflows/daily_full_pipeline.yml": {
        "daily_production",
        "official_price_data",
        "warrant",
        "catalyst_event",
        "market_risk",
        "repo_infrastructure",
    },
    ".github/workflows/daily_full_validation_replay_20260807.yml": {
        "daily_production",
        "official_price_data",
        "warrant",
        "catalyst_event",
        "market_risk",
        "repo_infrastructure",
    },
    ".github/workflows/daily_pdf_replay_pr_validation.yml": {
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/daily_model_maintenance_pr_validation.yml": {
        "daily_production",
        "research_backtest",
        "repo_infrastructure",
    },
    ".github/workflows/debug_tpex_fetch.yml": {"diagnostics", "official_price_data", "repo_infrastructure"},
    ".github/workflows/diagnose_stock_selection.yml": {
        "diagnostics",
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/event_catalyst_update.yml": {
        "catalyst_event",
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/historical_structured_source_replay.yml": {
        "official_price_data",
        "market_risk",
        "warrant",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_data_refresh.yml": {
        "individual_stock",
        "official_price_data",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_pr_validation.yml": {
        "daily_production",
        "individual_stock",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_report.yml": {
        "individual_stock",
        "official_price_data",
        "repo_infrastructure",
    },
    ".github/workflows/official_price_backfill.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/official_price_fetch.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/pages.yml": {"repo_infrastructure"},
    ".github/workflows/repair_daily_price_range.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_one_daily_price.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_recent_daily_price_gaps.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/research_backtest_pipeline.yml": {
        "research_backtest",
        "market_risk",
        "daily_production",
        "tdcc_weekly",
        "catalyst_event",
        "repo_infrastructure",
    },
    ".github/workflows/signal_performance_tracker.yml": {"research_backtest", "repo_infrastructure"},
    ".github/workflows/tdcc_history_backfill.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/tdcc_weekly_pr_validation.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/tdcc_weekly.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/test_tdcc_trend.yml": {"tdcc_weekly", "diagnostics", "repo_infrastructure"},
    ".github/workflows/volume_v2_advisory_lineage_refresh.yml": {
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/warrant_flow.yml": {
        "catalyst_event",
        "daily_production",
        "official_price_data",
        "repo_infrastructure",
        "warrant",
    },
    ".github/workflows/weekly_theme_review.yml": {
        "catalyst_event",
        "daily_production",
        "repo_infrastructure",
    },
}

FORBIDDEN_WORKFLOW_SNIPPETS = {
    ".github/workflows/daily_full_pipeline.yml": {
        "daily pipeline must not run TDCC weekly report builders": (
            "python scripts/build_tdcc_weekly_candidate_reports.py",
            "python scripts/build_tdcc_signal_effectiveness_report.py",
        ),
        "daily pipeline must not stage TDCC weekly PDF outputs": (
            "git add output/latest/tdcc_weekly_",
            "git add docs/latest/tdcc_weekly_",
        ),
        "daily pipeline must not stage research source/config changes": (
            "git add config/",
            "git add scripts/",
            "git add .github/workflows/",
        ),
    },
    ".github/workflows/research_backtest_pipeline.yml": {
        "research pipeline must not mutate production config or source": (
            "git add config/",
            "git add scripts/",
            "git add .github/workflows/",
        ),
        "research pipeline must not run daily production PDF entrypoints": (
            "python scripts/run_chatgpt_daily_report_entrypoint.py",
            "python scripts/generate_chatgpt_side_daily_reports.py",
            "python build_chatgpt_daily_report_packet.py",
            "python build_chatgpt_daily_report_rules.py",
        ),
        "research pipeline must not stage full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
    ".github/workflows/tdcc_weekly.yml": {
        "TDCC weekly pipeline must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC weekly pipeline must not run daily PDF entrypoints": (
            "python scripts/run_chatgpt_daily_report_entrypoint.py",
            "python scripts/generate_chatgpt_side_daily_reports.py",
            "python build_chatgpt_daily_report_packet.py",
        ),
        "TDCC weekly pipeline must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/tdcc_history_backfill.yml": {
        "TDCC history backfill must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC history backfill must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": {
        "TDCC monthly history gap repair must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC monthly history gap repair must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/warrant_flow.yml": {
        "warrant flow must not stage source or workflow files": (
            "git add scripts/",
            "git add .github/workflows/",
            "git add build_warrant_flow_latest.py",
            "git add merge_warrant_flow_into_candidates.py",
            "git add build_data_freshness_latest.py",
        ),
    },
    ".github/workflows/individual_stock_report.yml": {
        "individual stock report must not publish full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
    ".github/workflows/individual_stock_data_refresh.yml": {
        "individual stock data refresh must not publish full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
    ".github/workflows/individual_stock_pr_validation.yml": {
        "individual stock PR validation must remain read-only": (
            "contents: write",
            "git add ",
            "git commit",
            "git push",
            "actions/upload-pages-artifact",
            "actions/deploy-pages",
        ),
    },
    ".github/workflows/tdcc_weekly_pr_validation.yml": {
        "TDCC weekly PR validation must remain read-only": (
            "contents: write",
            "git add ",
            "git commit",
            "git push",
            "actions/upload-pages-artifact",
            "actions/deploy-pages",
        ),
    },
}

REQUIRED_WORKFLOW_COMMANDS = {
    DAILY_WORKFLOW: (
        "python scripts/validate_pdf_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
    ),
    ".github/workflows/historical_structured_source_replay.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/replay_historical_structured_sources.py",
        "python scripts/validate_historical_structured_source_replay.py",
        "python scripts/validate_historical_source_replay_staged_paths.py",
    ),
    ".github/workflows/research_backtest_pipeline.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_research_production_boundaries.py",
        "python scripts/validate_model_research_workflow_isolation.py",
    ),
    ".github/workflows/daily_model_maintenance_pr_validation.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/validate_model_research_workflow_isolation.py",
    ),
    ".github/workflows/daily_pdf_replay_pr_validation.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
    ),
    ".github/workflows/tdcc_weekly.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_tdcc_report_contract_consumers.py",
    ),
    ".github/workflows/tdcc_history_backfill.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/tdcc_weekly_pr_validation.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
    ),
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
    ),
    ".github/workflows/individual_stock_report.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/individual_stock_data_refresh.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/individual_stock_pr_validation.yml": (
        *PR_STATIC_VALIDATION_COMMANDS,
        "python scripts/validate_individual_pdf_contract_consumers.py",
    ),
    ".github/workflows/warrant_flow.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/repair_recent_daily_price_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_recent_structured_source_repair_workflow.py",
    ),
    ".github/workflows/volume_v2_advisory_lineage_refresh.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python -B scripts/validate_repo_file_lifecycle_inventory.py",
        "python -B scripts/validate_daily_production_boundaries.py",
        "python -B scripts/validate_model_data_independence.py",
        "python -B scripts/validate_repo_code_isolation_policy.py",
        "python -B scripts/run_volume_v2_advisory_lineage_refresh.py",
        "python -B scripts/validate_volume_breakout_watch.py --latest-only",
        "python -B scripts/validate_volume_attack_theme_layer.py",
        "python -B scripts/validate_daily_canonical_field_lineage.py",
        "python -B scripts/validate_daily_warrant_formal_sync_scope.py",
        "python -B scripts/validate_volume_v2_advisory_lineage_refresh.py",
    ),
}

PYTHON_INVOKE_RE = re.compile(r"\bpython(?:3)?\s+([A-Za-z0-9_./\\-]+\.py)")
REQUIRED_WORKFLOW_PYTHON_TARGET_RE = re.compile(
    r"\bpython(?:3)?\s+(?:-[A-Za-z]+\s+)*"
    r"([A-Za-z0-9_./\\-]+\.py)"
)
SHELL_INVOKE_RE = re.compile(r"\b(?:bash|sh)\s+([A-Za-z0-9_./\\-]+\.sh)")

EXECUTABLE_SCRIPT_SUFFIXES = {
    ".bat",
    ".cmd",
    ".gs",
    ".js",
    ".mjs",
    ".pl",
    ".ps1",
    ".rb",
    ".sh",
    ".ts",
    ".tsx",
}

ACTIVE_GUIDANCE_ROOT_FILES = {
    "AGENTS.md",
    "README.md",
}

ACTIVE_GUIDANCE_PREFIXES = (
    "docs/latest/",
    "output/latest/",
    "rules/",
)

ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES = {
    ".md",
    ".txt",
}

FORBIDDEN_GUIDANCE_COMMANDS = {
    r"\bpython(?:3)?\s+scripts/generate_chatgpt_side_daily_reports\.py\b": (
        "active guidance must point users to scripts/run_chatgpt_daily_report_entrypoint.py, "
        "not the renderer CLI"
    ),
    r"\bpython(?:3)?\s+generate_repo_chatgpt_side_reports\.py\b": (
        "active guidance must not point users to the retired OneDrive/helper report generator"
    ),
    r"\bpython(?:3)?\s+scripts/generate_daily_market_pdf\.py\b": (
        "active guidance must not point users to retired daily market PDF generator"
    ),
    r"\bpython(?:3)?\s+scripts/validate_daily_market_report\.py\b": (
        "active guidance must not point users to retired daily market PDF validator"
    ),
    r"\bpython(?:3)?\s+build_daily_market_report_artifacts\.py\b": (
        "active guidance must not present repo market artifacts as the formal daily PDF entrypoint"
    ),
}


@dataclass(frozen=True)
class InventoryRow:
    path: str
    kind: str
    owner: str
    status: str
    purpose: str
    allowed_workflows: tuple[str, ...]
    allowed_stage_patterns: tuple[str, ...]


def run_git_ls_files(pattern: str) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", pattern],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def tracked_python_paths() -> set[str]:
    tracked = {
        path
        for path in run_git_ls_files("*.py")
        if path.startswith("scripts/") or "/" not in path
        if (ROOT / path).exists()
    }
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for pattern in ("*.py", "scripts/**/*.py")
        for path in ROOT.glob(pattern)
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_test_python_paths() -> set[str]:
    tracked = {path for path in run_git_ls_files("*.py") if path.startswith("tests/") if (ROOT / path).exists()}
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "tests").glob("**/*.py")
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_executable_script_paths() -> set[str]:
    tracked = {
        path
        for path in run_git_ls_files("*")
        if Path(path).suffix in EXECUTABLE_SCRIPT_SUFFIXES
        if (ROOT / path).exists()
    }
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.glob("**/*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix in EXECUTABLE_SCRIPT_SUFFIXES
    }
    return tracked | working_tree


def tracked_workflow_paths() -> set[str]:
    tracked = {
        *run_git_ls_files(".github/workflows/*.yml"),
        *run_git_ls_files(".github/workflows/*.yaml"),
    }
    tracked = {path for path in tracked if (ROOT / path).exists()}
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for pattern in (".github/workflows/*.yml", ".github/workflows/*.yaml")
        for path in ROOT.glob(pattern)
    }
    return tracked | working_tree


def tracked_guidance_text_paths() -> set[str]:
    tracked: set[str] = set()
    for path in run_git_ls_files("*"):
        if not (ROOT / path).exists():
            continue
        suffix = Path(path).suffix.lower()
        if suffix not in {".md", ".txt"}:
            continue
        if path in ACTIVE_GUIDANCE_ROOT_FILES:
            tracked.add(path)
            continue
        if path.startswith(ACTIVE_GUIDANCE_PREFIXES):
            tracked.add(path)
            continue
        if path.startswith("docs/") and path.count("/") == 1 and suffix in ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES:
            tracked.add(path)
    return tracked


def split_semicolon(value: str) -> tuple[str, ...]:
    return tuple(part.strip().replace("\\", "/") for part in value.split(";") if part.strip())


def load_inventory(errors: list[str]) -> dict[str, InventoryRow]:
    rows_by_path: dict[str, InventoryRow] = {}
    if not INVENTORY.exists():
        errors.append("missing repo production inventory: config/repo_production_inventory.csv")
        return rows_by_path

    with INVENTORY.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            errors.append("repo production inventory is empty")
            return rows_by_path
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            errors.append(f"repo production inventory missing columns: {sorted(missing)}")
            return rows_by_path

        for line_no, row in enumerate(reader, start=2):
            path = (row.get("path") or "").strip().replace("\\", "/")
            if not path:
                errors.append(f"inventory row {line_no} has empty path")
                continue
            if path in rows_by_path:
                errors.append(f"inventory path listed more than once: {path}")
                continue
            inventory_row = InventoryRow(
                path=path,
                kind=(row.get("kind") or "").strip(),
                owner=(row.get("owner") or "").strip(),
                status=(row.get("status") or "").strip(),
                purpose=(row.get("purpose") or "").strip(),
                allowed_workflows=split_semicolon(row.get("allowed_workflows") or ""),
                allowed_stage_patterns=split_semicolon(row.get("allowed_stage_patterns") or ""),
            )
            rows_by_path[path] = inventory_row

    return rows_by_path


def read_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8", errors="replace")


def normalize_invoked_python_path(path: str) -> str:
    normalized = path.strip().strip("'\"").replace("\\", "/")
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def workflow_invocations(workflow_path: str) -> set[str]:
    text = read_text(workflow_path)
    invoked = {normalize_invoked_python_path(match.group(1)) for match in PYTHON_INVOKE_RE.finditer(text)}
    invoked.update(normalize_invoked_python_path(match.group(1)) for match in SHELL_INVOKE_RE.finditer(text))
    return invoked


def workflow_job_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    in_jobs = False
    current_name = ""
    current_lines: list[str] = []

    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        if not in_jobs:
            if stripped == "jobs:":
                in_jobs = True
            continue
        if stripped and not line.startswith((" ", "\t")):
            break

        match = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", stripped)
        if match:
            if current_name:
                blocks[current_name] = "".join(current_lines)
            current_name = match.group(1)
            current_lines = [line]
        elif current_name:
            current_lines.append(line)

    if current_name:
        blocks[current_name] = "".join(current_lines)
    return blocks


def workflow_has_pull_request_trigger(text: str) -> bool:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^on:\s*(?:pull_request|\[[^]]*\bpull_request\b[^]]*\])\s*$", line):
            return True
        if line.strip() != "on:" or line.startswith((" ", "\t")):
            continue
        for trigger_line in lines[index + 1 :]:
            if trigger_line and not trigger_line.startswith((" ", "\t")):
                break
            if re.match(r"^  pull_request:\s*$", trigger_line):
                return True
        return False
    return False


def workflow_call_declared_secrets(text: str) -> set[str]:
    secrets: set[str] = set()
    in_workflow_call = False
    in_secrets = False

    for line in text.splitlines():
        if line == "  workflow_call:":
            in_workflow_call = True
            in_secrets = False
            continue
        if not in_workflow_call:
            continue
        if re.match(r"^  \S", line):
            break
        if line == "    secrets:":
            in_secrets = True
            continue
        if not in_secrets:
            continue
        if re.match(r"^    \S", line):
            in_secrets = False
            continue
        match = re.match(r"^      ([A-Za-z0-9_]+):\s*$", line)
        if match:
            secrets.add(match.group(1))

    return secrets


def local_reusable_workflow_path(job_block: str) -> str:
    match = re.search(
        r"^    uses:\s+\./(\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml)\s*$",
        job_block,
        flags=re.MULTILINE,
    )
    return match.group(1) if match else ""


def workflow_job_mapping(job_block: str, section: str) -> dict[str, str]:
    lines = job_block.splitlines()
    section_line = f"    {section}:"
    mapping: dict[str, str] = {}
    in_section = False
    for line in lines:
        if not in_section:
            if line == section_line:
                in_section = True
            continue
        if re.match(r"^    \S", line):
            break
        match = re.match(r"^      ([A-Za-z0-9_]+):\s*(.*?)\s*$", line)
        if match:
            mapping[match.group(1)] = match.group(2).strip("'\"")
    return mapping


def is_registered_reusable_writer_job(
    job_block: str,
    rows_by_path: dict[str, InventoryRow],
) -> bool:
    called_path = local_reusable_workflow_path(job_block)
    called_row = rows_by_path.get(called_path)
    if not called_path or called_row is None or not called_row.allowed_stage_patterns:
        return False
    called_text = read_text(called_path)
    return workflow_call_declared_secrets(called_text) == {
        PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY
    }


def validate_reusable_writer_delegate(
    workflow_path: str,
    job_name: str,
    block: str,
    errors: list[str],
) -> None:
    secrets = workflow_job_mapping(block, "secrets")
    expected = {
        PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    }
    if secrets != expected:
        errors.append(
            f"{workflow_path} reusable writer job {job_name} must pass exactly "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} and no other secrets"
        )


def workflow_step_blocks(job_block: str) -> list[str]:
    blocks: list[str] = []
    in_steps = False
    current_lines: list[str] = []

    for line in job_block.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        if not in_steps:
            if stripped == "    steps:":
                in_steps = True
            continue

        if re.match(r"^      -\s+", stripped):
            if current_lines:
                blocks.append("".join(current_lines))
            current_lines = [line]
        elif current_lines:
            current_lines.append(line)

    if current_lines:
        blocks.append("".join(current_lines))
    return blocks


def workflow_step_name(step_block: str) -> str:
    match = re.search(r"^      - name:\s*(.+?)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def canonical_workflow_step_text(step_block: str) -> str:
    normalized = step_block.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in normalized.strip().split("\n"))


def validate_regular_pr_static_validation_step(text: str) -> list[str]:
    errors: list[str] = []
    jobs = workflow_job_blocks(text)
    regular_job = jobs.get("individual-stock-pr-validation", "")
    if not regular_job:
        return ["regular individual-stock PR validation job is missing"]

    steps = workflow_step_blocks(regular_job)
    dependency_steps = [
        (index, step)
        for index, step in enumerate(steps)
        if workflow_step_name(step) == PR_STATIC_DEPENDENCY_STEP_NAME
    ]
    static_steps = [
        (index, step)
        for index, step in enumerate(steps)
        if workflow_step_name(step) == PR_STATIC_VALIDATION_STEP_NAME
    ]
    if len(dependency_steps) != 1:
        errors.append("pull_request job must contain exactly one PR static dependency step")
    if len(static_steps) != 1:
        errors.append("pull_request job must contain exactly one repository static validation step")
    if len(dependency_steps) != 1 or len(static_steps) != 1:
        return errors

    dependency_index, dependency_step = dependency_steps[0]
    static_index, static_step = static_steps[0]
    if dependency_index >= static_index:
        errors.append("PR static validation dependencies must be installed before validation")

    expected_dependency = canonical_workflow_step_text(
        "      - name: "
        f"{PR_STATIC_DEPENDENCY_STEP_NAME}\n"
        f"        run: {PR_STATIC_DEPENDENCY_COMMAND}\n"
    )
    if canonical_workflow_step_text(dependency_step) != expected_dependency:
        errors.append("PR static dependency step must match the exact unconditional contract")

    expected_static = canonical_workflow_step_text(
        "      - name: "
        f"{PR_STATIC_VALIDATION_STEP_NAME}\n"
        "        run: |\n"
        + "".join(f"          {command}\n" for command in PR_STATIC_VALIDATION_COMMANDS)
    )
    if canonical_workflow_step_text(static_step) != expected_static:
        errors.append(
            "repository static validation step must match the exact unconditional command contract"
        )
    if workflow_step_condition(static_step):
        errors.append("repository static validation step must not have an if condition")
    if re.search(r"^        continue-on-error\s*:", static_step, flags=re.MULTILINE):
        errors.append("repository static validation step must fail closed")

    audit_job = jobs.get("pr-safe-base-audit-runner", "")
    if PR_STATIC_VALIDATION_STEP_NAME in audit_job:
        errors.append("pull_request_target base-owned runner must not contain the PR-head static step")
    if "ref: ${{ github.event.pull_request.head.sha }}" in audit_job:
        errors.append("pull_request_target base-owned runner must not checkout the PR head SHA")
    if "git checkout " in audit_job or "git switch " in audit_job:
        errors.append("pull_request_target base-owned runner must not transition to PR-head code")
    return errors


def workflow_job_scalar_values(job_block: str, key: str) -> tuple[str, ...]:
    return tuple(
        match.group(1).strip("'\"")
        for match in re.finditer(
            rf"^    {re.escape(key)}:\s*(.*?)\s*$",
            job_block,
            flags=re.MULTILINE,
        )
    )


def workflow_job_multiline_block(
    job_block: str,
    key: str,
) -> tuple[tuple[str, ...], list[str]]:
    lines = job_block.splitlines()
    indexes = [
        index
        for index, line in enumerate(lines)
        if re.match(rf"^    {re.escape(key)}:\s*", line)
    ]
    if len(indexes) != 1:
        return (), [f"audit runner must contain exactly one {key} field"]
    block = [lines[indexes[0]]]
    for line in lines[indexes[0] + 1 :]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 4:
            break
        block.append(line.rstrip())
    return tuple(block), []


def canonical_workflow_job_header_sha256(
    job_block: str,
) -> tuple[str, list[str]]:
    lines = job_block.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    indexes = [index for index, line in enumerate(lines) if line == "    steps:"]
    if len(indexes) != 1:
        return "", ["audit runner must contain exactly one steps mapping"]
    header_lines = [line.rstrip() for line in lines[: indexes[0]]]
    while header_lines and not header_lines[0]:
        header_lines.pop(0)
    while header_lines and not header_lines[-1]:
        header_lines.pop()
    payload = ("\n".join(header_lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest(), []


def canonical_workflow_step_sha256(step_block: str) -> str:
    normalized = step_block.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    payload = ("\n".join(lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def workflow_step_mapping(step_block: str, section: str) -> dict[str, str]:
    lines = step_block.splitlines()
    section_line = f"        {section}:"
    mapping: dict[str, str] = {}
    in_section = False

    for line in lines:
        if not in_section:
            if line == section_line:
                in_section = True
            continue
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 8:
            break
        match = re.match(r"^          ([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            mapping[match.group(1)] = match.group(2)
    return mapping


def workflow_exact_mapping(
    text: str,
    section: str,
    *,
    section_indent: int,
    entry_indent: int,
) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    section_line = f"{' ' * section_indent}{section}:"
    indexes = [index for index, line in enumerate(lines) if line == section_line]
    if len(indexes) != 1:
        return {}, [
            f"workflow must contain exactly one {section} mapping at indent "
            f"{section_indent}"
        ]

    mapping: dict[str, str] = {}
    errors: list[str] = []
    for line in lines[indexes[0] + 1 :]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= section_indent:
            break
        match = re.fullmatch(
            rf" {{{entry_indent}}}([A-Za-z0-9_-]+):\s*(.*?)\s*",
            line,
        )
        if not match:
            errors.append(f"{section} mapping contains malformed entry: {line.strip()}")
            continue
        key = match.group(1)
        if key in mapping:
            errors.append(f"{section} mapping contains duplicate key: {key}")
            continue
        mapping[key] = match.group(2).strip("'\"")
    return mapping, errors


def workflow_action_uses(text: str) -> tuple[tuple[str, ...], list[str]]:
    refs: list[str] = []
    errors: list[str] = []
    for line in text.splitlines():
        if not re.match(r"^\s+(?:-\s+)?uses\s*:", line):
            continue
        match = re.fullmatch(r"\s+(?:-\s+)?uses:\s*(.*?)\s*", line)
        if not match or not match.group(1):
            errors.append(f"workflow contains malformed uses entry: {line.strip()}")
            continue
        refs.append(match.group(1).strip("'\""))
    return tuple(refs), errors


def workflow_step_uses(step_block: str) -> str:
    match = re.search(r"^        uses:\s*([^\s#]+)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def workflow_step_condition(step_block: str) -> str:
    match = re.search(r"^        if:\s*(.+?)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def workflow_step_with_values(
    step_block: str,
) -> tuple[dict[str, str | tuple[str, ...]], list[str]]:
    lines = step_block.splitlines()
    values: dict[str, str | tuple[str, ...]] = {}
    errors: list[str] = []
    try:
        start = lines.index("        with:") + 1
    except ValueError:
        return values, ["workflow step lacks an exact with mapping"]

    index = start
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 8:
            break
        match = re.fullmatch(r" {10}([A-Za-z0-9_-]+):\s*(.*?)\s*", line)
        if not match:
            errors.append(f"workflow with mapping has malformed line: {line.strip()}")
            index += 1
            continue
        key, raw_value = match.groups()
        if key in values:
            errors.append(f"workflow with mapping repeats key: {key}")
        if raw_value in {"|", ">"}:
            block_values: list[str] = []
            index += 1
            while index < len(lines):
                block_line = lines[index]
                block_indent = len(block_line) - len(block_line.lstrip(" "))
                if block_line.strip() and block_indent <= 10:
                    break
                if block_line.strip():
                    if block_indent != 12:
                        errors.append(
                            f"workflow block value has unexpected indentation: {key}"
                        )
                    block_values.append(block_line.strip())
                index += 1
            values[key] = tuple(block_values)
            continue
        values[key] = raw_value.strip("'\"")
        index += 1
    return values, errors


def workflow_trigger_paths(text: str, trigger: str) -> tuple[tuple[str, ...], list[str]]:
    lines = text.splitlines()
    trigger_line = f"  {trigger}:"
    indexes = [index for index, line in enumerate(lines) if line == trigger_line]
    if len(indexes) != 1:
        return (), [f"workflow must contain exactly one {trigger} trigger mapping"]
    paths_indexes: list[int] = []
    for index in range(indexes[0] + 1, len(lines)):
        line = lines[index]
        if line and not line.startswith("    "):
            break
        if line == "    paths:":
            paths_indexes.append(index)
    if len(paths_indexes) != 1:
        return (), [f"{trigger} must contain exactly one paths mapping"]
    paths: list[str] = []
    for line in lines[paths_indexes[0] + 1 :]:
        if line and not line.startswith("      "):
            break
        match = re.fullmatch(r" {6}-\s*['\"]?(.+?)['\"]?\s*", line)
        if match:
            paths.append(match.group(1).strip("'\""))
        elif line.strip():
            return (), [f"{trigger} paths contains malformed entry: {line.strip()}"]
    return tuple(paths), []


def validate_pr_safe_base_guard_workflow_text(text: str) -> list[str]:
    errors: list[str] = []
    target_headers = list(
        re.finditer(r"^  pull_request_target:\s*$", text, flags=re.MULTILINE)
    )
    if len(target_headers) != 1:
        errors.append("workflow must declare pull_request_target exactly once")
    else:
        tail = text[target_headers[0].end() :]
        next_section = re.search(
            r"^(?:[A-Za-z_][^:\n]*|  [A-Za-z_][^:\n]*):",
            tail,
            flags=re.MULTILINE,
        )
        target_block = tail[: next_section.start()] if next_section else tail
        if re.search(r"^    paths(?:-ignore)?:", target_block, flags=re.MULTILINE):
            errors.append("pull_request_target trust-root guard must not use a paths filter")
        target_types = re.findall(
            r"^    types:\s*(.*?)\s*$",
            target_block,
            flags=re.MULTILINE,
        )
        if target_types != ["[opened, synchronize, reopened, edited]"]:
            errors.append("pull_request_target event types must match the closed set")

    action_uses, action_errors = workflow_action_uses(text)
    errors.extend(action_errors)
    if action_uses != PR_SAFE_EXPECTED_ACTION_USES:
        errors.append("workflow uses entries must match the pinned base-only action set")

    global_permissions, permission_errors = workflow_exact_mapping(
        text,
        "permissions",
        section_indent=0,
        entry_indent=2,
    )
    errors.extend(permission_errors)
    if global_permissions != PR_SAFE_READ_ONLY_PERMISSIONS:
        errors.append("workflow permissions must contain exactly contents: read")

    jobs = workflow_job_blocks(text)
    regular_job = jobs.get("individual-stock-pr-validation", "")
    if not regular_job:
        errors.append("regular individual-stock PR validation job is missing")
    else:
        regular_names = re.findall(
            r"^    name:\s*(.*?)\s*$",
            regular_job,
            flags=re.MULTILINE,
        )
        if regular_names != [PR_SAFE_REGULAR_JOB_NAME_EXPRESSION]:
            errors.append(
                "regular job name must preserve the pull_request required context and "
                "use a distinct pull_request_target skip name"
            )
        if workflow_job_scalar_values(regular_job, "timeout-minutes") != ("30",):
            errors.append(
                "regular individual-stock PR validation job must use timeout-minutes: 30"
            )
    errors.extend(validate_regular_pr_static_validation_step(text))

    guard_job = jobs.get(PR_SAFE_GUARD_JOB_ID, "")
    if not guard_job:
        return [*errors, "base-owned trust-root self-change guard job is missing"]
    if workflow_job_scalar_values(guard_job, "name") != (PR_SAFE_GUARD_JOB_NAME,):
        errors.append("trust-root guard job name must match its non-required context")
    if workflow_job_scalar_values(guard_job, "runs-on") != (
        PR_SAFE_GUARD_JOB_RUNS_ON,
    ):
        errors.append("trust-root guard must run on ubuntu-latest")
    if workflow_job_scalar_values(guard_job, "timeout-minutes") != (
        PR_SAFE_GUARD_JOB_TIMEOUT_MINUTES,
    ):
        errors.append("trust-root guard must use timeout-minutes: 10")
    guard_if, guard_if_errors = workflow_job_multiline_block(guard_job, "if")
    errors.extend(guard_if_errors)
    if guard_if != PR_SAFE_GUARD_JOB_IF_BLOCK:
        errors.append("trust-root guard if condition must match the base-owned contract")
    guard_permissions, guard_permission_errors = workflow_exact_mapping(
        guard_job,
        "permissions",
        section_indent=4,
        entry_indent=6,
    )
    errors.extend(guard_permission_errors)
    if guard_permissions != PR_SAFE_READ_ONLY_PERMISSIONS:
        errors.append("trust-root guard permissions must contain exactly contents: read")

    steps = workflow_step_blocks(guard_job)
    if tuple(workflow_step_name(step) for step in steps) != PR_SAFE_GUARD_STEP_NAMES:
        errors.append("trust-root guard steps must match the exact ordered contract")
        return errors

    expected_checkout = canonical_workflow_step_text(
        "      - name: Checkout pull request base only\n"
        f"        uses: {PR_SAFE_CHECKOUT_ACTION}\n"
        "        with:\n"
        "          ref: ${{ github.event.pull_request.base.sha }}\n"
        "          fetch-depth: 1\n"
        "          persist-credentials: false\n"
    )
    expected_fetch = canonical_workflow_step_text(
        "      - name: Fetch pull request head object without checkout\n"
        "        env:\n"
        "          PR_NUMBER: ${{ github.event.pull_request.number }}\n"
        "          HEAD_SHA: ${{ github.event.pull_request.head.sha }}\n"
        "        shell: bash\n"
        "        run: |\n"
        "          set -euo pipefail\n"
        "          test -n \"$PR_NUMBER\"\n"
        "          test -n \"$HEAD_SHA\"\n"
        "          LOCAL_HEAD_REF=\"refs/remotes/origin/pr-safe-head\"\n"
        "          git fetch --no-tags --depth=1 origin "
        "\"+refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF\"\n"
        "          test \"$(git rev-parse \"$LOCAL_HEAD_REF\")\" = \"$HEAD_SHA\"\n"
    )
    expected_validate = canonical_workflow_step_text(
        "      - name: Validate trust-root self-change from base code\n"
        "        env:\n"
        "          BASE_SHA: ${{ github.event.pull_request.base.sha }}\n"
        "          HEAD_SHA: ${{ github.event.pull_request.head.sha }}\n"
        "          BASE_REPOSITORY: ${{ github.event.pull_request.base.repo.full_name }}\n"
        "          HEAD_REPOSITORY: ${{ github.event.pull_request.head.repo.full_name }}\n"
        "          MAINTAINER_APPROVED: "
        "${{ contains(github.event.pull_request.labels.*.name, "
        "'trust-root-maintenance-approved') }}\n"
        "        shell: bash\n"
        "        run: |\n"
        "          set -euo pipefail\n"
        "          python scripts/validate_repo_production_inventory.py \\\n"
        "            --validate-pr-trust-root-change \\\n"
        "            --base-sha \"$BASE_SHA\" \\\n"
        "            --head-sha \"$HEAD_SHA\" \\\n"
        "            --base-repository \"$BASE_REPOSITORY\" \\\n"
        "            --head-repository \"$HEAD_REPOSITORY\" \\\n"
        "            --maintainer-approved \"$MAINTAINER_APPROVED\"\n"
    )
    observed_steps = tuple(canonical_workflow_step_text(step) for step in steps)
    if observed_steps != (expected_checkout, expected_fetch, expected_validate):
        errors.append("trust-root guard steps must match the base-only command contract")

    forbidden_fragments = (
        "continue-on-error:",
        "actions/upload-artifact@",
        "secrets.",
        "runs-on: self-hosted",
        "git checkout ",
        "git switch ",
        "git reset ",
        "git clean ",
        "git show ",
        "github.event.pull_request.head.ref",
        "pr-safe-control-plane-audit-manifest",
    )
    for fragment in forbidden_fragments:
        if fragment in guard_job:
            errors.append(f"trust-root guard contains forbidden fragment: {fragment}")
    return errors


def is_checkout_step(step_block: str) -> bool:
    return bool(
        re.search(
            r"^        uses:\s*actions/checkout@[^\s#]+\s*$",
            step_block,
            flags=re.MULTILINE,
        )
    )


def is_valid_writer_secret_preflight(step_block: str) -> bool:
    if workflow_step_name(step_block) != PRODUCTION_ARTIFACT_WRITE_PREFLIGHT_NAME:
        return False
    if not re.search(r"^        shell:\s*bash\s*$", step_block, flags=re.MULTILINE):
        return False
    env = workflow_step_mapping(step_block, "env")
    if (
        env.get(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
        != PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    ):
        return False
    stripped_lines = {line.strip() for line in step_block.splitlines()}
    return (
        PRODUCTION_ARTIFACT_WRITE_SECRET_GUARD in stripped_lines
        and "exit 1" in stripped_lines
    )


def is_artifact_push_job(block: str) -> bool:
    return any(marker in block for marker in ARTIFACT_PUSH_JOB_MARKERS)


def validate_artifact_push_job(
    workflow_path: str,
    job_name: str,
    block: str,
    errors: list[str],
) -> None:
    steps = workflow_step_blocks(block)
    checkout_steps = [
        (index, step)
        for index, step in enumerate(steps)
        if is_checkout_step(step)
    ]
    if not checkout_steps:
        errors.append(f"{workflow_path} writer job {job_name} must checkout the repository")

    keyed_checkout_steps = [
        (index, step)
        for index, step in checkout_steps
        if workflow_step_mapping(step, "with").get("ssh-key")
        == PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    ]
    if not keyed_checkout_steps:
        errors.append(
            f"{workflow_path} writer job {job_name} must use "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} as actions/checkout ssh-key"
        )

    authenticated_checkout_steps = [
        (index, step)
        for index, step in keyed_checkout_steps
        if workflow_step_mapping(step, "with").get("persist-credentials") == "true"
    ]
    if keyed_checkout_steps and not authenticated_checkout_steps:
        errors.append(
            f"{workflow_path} writer job {job_name} must set persist-credentials: true "
            "in the same actions/checkout step as the deploy key"
        )

    preflight_indices = [
        index
        for index, step in enumerate(steps)
        if is_valid_writer_secret_preflight(step)
    ]
    if not preflight_indices:
        errors.append(
            f"{workflow_path} writer job {job_name} must fail closed when "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} is empty"
        )
    elif checkout_steps and min(preflight_indices) >= min(index for index, _ in checkout_steps):
        errors.append(
            f"{workflow_path} writer job {job_name} must check the deploy key "
            "before actions/checkout"
        )


def validate_production_artifact_writer_auth(
    rows_by_path: dict[str, InventoryRow],
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    for workflow_path in sorted(workflow_paths):
        row = rows_by_path.get(workflow_path)
        text = read_text(workflow_path)
        job_blocks = workflow_job_blocks(text)
        artifact_push_jobs = {
            job_name: block
            for job_name, block in job_blocks.items()
            if is_artifact_push_job(block)
        }
        is_registered_writer = bool(row is not None and row.allowed_stage_patterns)
        writer_jobs = artifact_push_jobs if is_registered_writer else {}
        reusable_writer_jobs = {
            job_name: block
            for job_name, block in job_blocks.items()
            if is_registered_reusable_writer_job(block, rows_by_path)
        }

        if is_registered_writer and not artifact_push_jobs:
            errors.append(
                f"{workflow_path} has allowed_stage_patterns but no artifact push job"
            )

        for job_name, block in writer_jobs.items():
            validate_artifact_push_job(workflow_path, job_name, block, errors)
        for job_name, block in reusable_writer_jobs.items():
            validate_reusable_writer_delegate(workflow_path, job_name, block, errors)

        for job_name, block in job_blocks.items():
            if (
                job_name not in writer_jobs
                and job_name not in reusable_writer_jobs
                and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY in block
            ):
                errors.append(
                    f"{workflow_path} non-writer job {job_name} must not use "
                    f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}"
                )

        writer_secret_count = sum(
            block.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            for block in writer_jobs.values()
        )
        reusable_writer_secret_count = sum(
            block.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            for block in reusable_writer_jobs.values()
        )
        reusable_secret_declaration_count = int(
            is_registered_writer
            and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY
            in workflow_call_declared_secrets(text)
        )
        if (
            text.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            != writer_secret_count
            + reusable_writer_secret_count
            + reusable_secret_declaration_count
        ):
            errors.append(
                f"{workflow_path} must scope secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} "
                "to artifact push jobs only"
            )
        if workflow_has_pull_request_trigger(text) and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY in text:
            errors.append(
                f"{workflow_path} pull_request workflow must not use "
                f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}"
            )


def validate_inventory_coverage(
    rows_by_path: dict[str, InventoryRow],
    python_paths: set[str],
    test_python_paths: set[str],
    executable_script_paths: set[str],
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    expected = python_paths | test_python_paths | executable_script_paths | workflow_paths
    actual = set(rows_by_path)

    for path in sorted(expected - actual):
        errors.append(f"tracked executable/test/workflow path missing owner inventory: {path}")
    for path in sorted(actual - expected):
        errors.append(f"inventory lists untracked or out-of-scope path: {path}")


def validate_inventory_rows(rows_by_path: dict[str, InventoryRow], errors: list[str]) -> None:
    for row in rows_by_path.values():
        if row.kind not in VALID_KINDS:
            errors.append(f"{row.path} has invalid inventory kind: {row.kind}")
        if row.kind == "test_python" and not row.path.startswith("tests/"):
            errors.append(f"{row.path} has test_python kind but is not under tests/")
        if row.kind == "executable_script" and Path(row.path).suffix not in EXECUTABLE_SCRIPT_SUFFIXES:
            errors.append(f"{row.path} has executable_script kind but unsupported suffix")
        if row.owner not in VALID_OWNERS:
            errors.append(f"{row.path} has invalid or empty owner: {row.owner}")
        if row.status not in VALID_STATUSES:
            errors.append(f"{row.path} has invalid status: {row.status}")
        if not row.purpose:
            errors.append(f"{row.path} has empty purpose")
        if row.kind == "workflow" and row.path not in WORKFLOW_ALLOWED_OWNERS:
            errors.append(f"workflow has no allowed-owner boundary rule: {row.path}")
        if row.status == "legacy_deprecated" and row.allowed_workflows:
            errors.append(f"deprecated path must not list allowed workflows: {row.path}")


def validate_workflow_invocations(rows_by_path: dict[str, InventoryRow], workflow_paths: set[str], errors: list[str]) -> None:
    for workflow_path in sorted(workflow_paths):
        workflow_row = rows_by_path.get(workflow_path)
        if workflow_row is None:
            continue
        allowed_owners = WORKFLOW_ALLOWED_OWNERS.get(workflow_path, set())
        invoked_paths = workflow_invocations(workflow_path)

        for invoked_path in sorted(invoked_paths):
            if not (
                invoked_path.startswith("scripts/")
                or invoked_path.startswith("tests/")
                or invoked_path.startswith("docs/")
                or "/" not in invoked_path
            ):
                continue
            invoked_row = rows_by_path.get(invoked_path)
            if invoked_row is None:
                errors.append(f"{workflow_path} invokes Python path without inventory owner: {invoked_path}")
                continue
            if invoked_row.status == "legacy_deprecated":
                errors.append(f"{workflow_path} invokes deprecated Python path: {invoked_path}")
            if invoked_row.owner not in allowed_owners:
                errors.append(
                    f"{workflow_path} invokes {invoked_path} owned by {invoked_row.owner}; "
                    f"allowed owners are {sorted(allowed_owners)}"
                )
            if invoked_row.allowed_workflows and workflow_path not in invoked_row.allowed_workflows:
                errors.append(
                    f"{workflow_path} invokes {invoked_path}, but inventory allowed_workflows="
                    f"{list(invoked_row.allowed_workflows)}"
                )


def required_workflow_python_targets(text: str) -> frozenset[str]:
    return frozenset(
        match.group(1).replace("\\", "/").removeprefix("./")
        for match in REQUIRED_WORKFLOW_PYTHON_TARGET_RE.finditer(text)
    )


def workflow_contains_required_command(
    workflow_text: str,
    command: str,
) -> bool:
    return re.search(
        rf"(?m)^[ \t]*{re.escape(command)}(?=$|[ \t\r\\])",
        workflow_text,
    ) is not None


def validate_required_workflow_commands(
    workflow_path: str,
    workflow_text: str,
    command_list: tuple[str, ...],
    errors: list[str],
) -> None:
    for command in command_list:
        if not workflow_contains_required_command(workflow_text, command):
            errors.append(f"{workflow_path} must run {command}")


def validate_workflow_snippets(errors: list[str]) -> None:
    for workflow_path, command_list in REQUIRED_WORKFLOW_COMMANDS.items():
        if not (ROOT / workflow_path).exists():
            continue
        validate_required_workflow_commands(
            workflow_path,
            read_text(workflow_path),
            command_list,
            errors,
        )
        if workflow_path == PR_SAFE_BASE_GUARD_WORKFLOW:
            errors.extend(validate_regular_pr_static_validation_step(read_text(workflow_path)))

    for workflow_path, grouped_snippets in FORBIDDEN_WORKFLOW_SNIPPETS.items():
        if not (ROOT / workflow_path).exists():
            continue
        text = read_text(workflow_path)
        for label, snippets in grouped_snippets.items():
            for snippet in snippets:
                if snippet in text:
                    errors.append(f"{workflow_path}: {label}: forbidden snippet found: {snippet}")


def validate_allowed_stage_patterns(rows_by_path: dict[str, InventoryRow], errors: list[str]) -> None:
    for row in rows_by_path.values():
        if row.kind != "workflow":
            continue
        text = read_text(row.path)
        for pattern in row.allowed_stage_patterns:
            if pattern and pattern not in text:
                errors.append(f"{row.path} inventory allowed_stage_patterns missing from workflow text: {pattern}")


def validate_active_guidance_commands(errors: list[str]) -> None:
    for rel_path in sorted(tracked_guidance_text_paths()):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, message in FORBIDDEN_GUIDANCE_COMMANDS.items():
            if re.search(pattern, text):
                errors.append(f"{message}: {rel_path} matches {pattern}")


def canonical_blob_sha256(payload: bytes) -> str:
    canonical = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(canonical).hexdigest()


def build_daily_full_checkpoint_replay_integrated_lifecycle_inventory(
    pre_stage_f_payload: bytes,
    stage_f_payload: bytes,
    replay_branch_payload: bytes,
) -> bytes | None:
    expected_hashes = (
        PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PRE_STAGE_F_LIFECYCLE_SHA256,
        PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STAGE_F_LIFECYCLE_SHA256,
        PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BRANCH_LIFECYCLE_SHA256,
    )
    payloads = (pre_stage_f_payload, stage_f_payload, replay_branch_payload)
    if tuple(canonical_blob_sha256(payload) for payload in payloads) != expected_hashes:
        return None

    parsed: list[tuple[list[str], list[dict[str, str]], bytes]] = []
    for payload in payloads:
        canonical = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        try:
            reader = csv.DictReader(
                io.StringIO(canonical.decode("utf-8-sig"), newline="")
            )
            fieldnames = list(reader.fieldnames or ())
            rows = [dict(row) for row in reader]
        except (UnicodeError, csv.Error):
            return None
        if (
            not fieldnames
            or any(None in row for row in rows)
            or any(not row.get("path", "").strip() for row in rows)
            or len({row["path"] for row in rows}) != len(rows)
        ):
            return None
        parsed.append((fieldnames, rows, canonical))

    base_fields, base_rows, _base_canonical = parsed[0]
    stage_f_fields, stage_f_rows, _stage_f_canonical = parsed[1]
    replay_fields, replay_rows, replay_canonical = parsed[2]
    if base_fields != stage_f_fields or base_fields != replay_fields:
        return None

    base_by_path = {row["path"]: row for row in base_rows}
    stage_f_by_path = {row["path"]: row for row in stage_f_rows}
    replay_by_path = {row["path"]: row for row in replay_rows}
    overlap_path = PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_OVERLAP_ROW
    if set(base_by_path) != set(stage_f_by_path) or overlap_path not in base_by_path:
        return None
    stage_f_changed = {
        path for path in base_by_path if base_by_path[path] != stage_f_by_path[path]
    }
    if stage_f_changed != {overlap_path}:
        return None

    base_overlap = base_by_path[overlap_path]
    stage_f_overlap = stage_f_by_path[overlap_path]
    replay_overlap = replay_by_path.get(overlap_path)
    if replay_overlap is None:
        return None
    stage_f_columns = {
        column
        for column in base_fields
        if base_overlap[column] != stage_f_overlap[column]
    }
    replay_overlap_columns = {
        column
        for column in base_fields
        if base_overlap[column] != replay_overlap[column]
    }
    if stage_f_columns != {"imported_by"}:
        return None
    if replay_overlap_columns != {"called_by_workflow"}:
        return None

    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=base_fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(replay_rows)
    if output.getvalue().encode("utf-8") != replay_canonical:
        return None

    merged_rows = [dict(row) for row in replay_rows]
    merged_overlap = next(row for row in merged_rows if row["path"] == overlap_path)
    merged_overlap["imported_by"] = stage_f_overlap["imported_by"]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=base_fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(merged_rows)
    integrated = output.getvalue().encode("utf-8")
    if canonical_blob_sha256(integrated) != (
        PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_INTEGRATED_LIFECYCLE_SHA256
    ):
        return None
    return integrated


def pr_safe_migration_contract_for_paths(
    changed_paths: set[str],
    *,
    base_helper_sha256: str | None = None,
    current_helper_sha256: str | None = None,
    current_test_sha256: str | None = None,
    target_id: str | None = None,
) -> tuple[str, str, str, frozenset[str]] | None:
    del base_helper_sha256, current_helper_sha256, current_test_sha256
    contracts = (
        (
            PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS,
        ),
        (
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
        ),
        (
            PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_AUTHORIZED_STAGE1_PATHS,
        ),
        (
            PR_SAFE_SNAPSHOT_MIGRATION_ID,
            PR_SAFE_SNAPSHOT_HELPER,
            PR_SAFE_SNAPSHOT_TEST,
            PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
        ),
    )
    matches = [
        contract
        for contract in contracts
        if changed_paths == contract[3]
        and (target_id is None or target_id == contract[0])
    ]
    return matches[0] if len(matches) == 1 else None


def _pr_safe_repo_ref_is_ancestor(
    repository_root: Path,
    ancestor: str,
    descendant: str,
) -> bool:
    try:
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, descendant],
            cwd=repository_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


def _pr_safe_repo_blob(
    repository_root: Path,
    ref: str,
    path: str,
) -> bytes | None:
    try:
        result = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            cwd=repository_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout if result.returncode == 0 else None


def _pr_safe_repo_raw_blob_sha256(
    repository_root: Path,
    ref: str,
    path: str,
) -> str | None:
    payload = _pr_safe_repo_blob(repository_root, ref, path)
    return None if payload is None else hashlib.sha256(payload).hexdigest()


def _pr_safe_repo_blob_mode(
    repository_root: Path,
    ref: str,
    path: str,
) -> str | None:
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-z", ref, "--", path],
            cwd=repository_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    entries = [entry for entry in result.stdout.split(b"\0") if entry]
    if len(entries) != 1 or b"\t" not in entries[0]:
        return None
    metadata, raw_path = entries[0].split(b"\t", 1)
    fields = metadata.decode("ascii", errors="replace").split()
    try:
        observed_path = raw_path.decode("utf-8").replace("\\", "/")
    except UnicodeError:
        return None
    if len(fields) != 3 or fields[1] != "blob" or observed_path != path:
        return None
    return fields[0]


def _pr_safe_repo_exact_modified_paths(
    repository_root: Path,
    base_ref: str,
    head_ref: str,
    expected_paths: frozenset[str],
) -> bool:
    try:
        result = subprocess.run(
            [
                "git",
                "diff",
                "--name-status",
                "-z",
                "--find-renames",
                "--find-copies",
                "--diff-filter=ACDMRT",
                f"{base_ref}...{head_ref}",
                "--",
            ],
            cwd=repository_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    if result.returncode != 0:
        return False
    fields = result.stdout.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 2 != 0:
        return False
    observed_paths: list[str] = []
    for index in range(0, len(fields), 2):
        if fields[index] != b"M":
            return False
        try:
            path = fields[index + 1].decode("utf-8").replace("\\", "/")
        except UnicodeError:
            return False
        observed_paths.append(path)
    return (
        len(observed_paths) == len(set(observed_paths))
        and frozenset(observed_paths) == expected_paths
    )


def _pr_safe_repo_exact_change_statuses(
    repository_root: Path,
    base_ref: str,
    head_ref: str,
    expected_status_by_path: dict[str, str],
) -> bool:
    if not expected_status_by_path or any(
        status not in {"A", "M"} for status in expected_status_by_path.values()
    ):
        return False
    try:
        result = subprocess.run(
            [
                "git",
                "diff",
                "--name-status",
                "-z",
                "--find-renames",
                "--find-copies",
                "--diff-filter=ACDMRT",
                f"{base_ref}...{head_ref}",
                "--",
            ],
            cwd=repository_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    if result.returncode != 0:
        return False
    fields = result.stdout.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 2 != 0:
        return False
    observed_status_by_path: dict[str, str] = {}
    for index in range(0, len(fields), 2):
        try:
            status = fields[index].decode("ascii")
            path = fields[index + 1].decode("utf-8").replace("\\", "/")
        except UnicodeError:
            return False
        if status not in {"A", "M"} or path in observed_status_by_path:
            return False
        observed_status_by_path[path] = status
    return observed_status_by_path == expected_status_by_path


def is_preauthorized_local_validation_replay_routing_migration(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> bool:
    normalized_paths = {str(path).replace("\\", "/") for path in changed_paths}
    normalized_strict = {
        str(path).replace("\\", "/") for path in strict_surface_changes
    }
    if normalized_paths != PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS:
        return False
    if normalized_strict != PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES:
        return False
    if not re.fullmatch(r"[0-9a-f]{40}", str(base_ref)):
        return False

    root = Path(repository_root).resolve()
    if not _pr_safe_repo_ref_is_ancestor(
        root,
        PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_CONTENT_REF_SHA,
        base_ref,
    ):
        return False
    if not _pr_safe_repo_ref_is_ancestor(root, base_ref, head_ref):
        return False

    for path in sorted(PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS):
        base_blob = _pr_safe_repo_blob(root, base_ref, path)
        target_blob = _pr_safe_repo_blob(root, head_ref, path)
        expected_base_sha = (
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH[path]
        )
        if expected_base_sha is None:
            if (
                base_blob is not None
                or _pr_safe_repo_blob_mode(root, base_ref, path) is not None
            ):
                return False
        elif (
            base_blob is None
            or canonical_blob_sha256(base_blob) != expected_base_sha
            or _pr_safe_repo_blob_mode(root, base_ref, path) != "100644"
        ):
            return False
        if (
            target_blob is None
            or canonical_blob_sha256(target_blob)
            != PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_SHA256_BY_PATH[path]
            or _pr_safe_repo_blob_mode(root, head_ref, path) != "100644"
        ):
            return False
    return True


def is_preauthorized_daily_full_checkpoint_replay_migration(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> bool:
    normalized_paths = {str(path).replace("\\", "/") for path in changed_paths}
    normalized_strict = {
        str(path).replace("\\", "/") for path in strict_surface_changes
    }
    if normalized_paths == PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS:
        return is_preauthorized_local_validation_replay_routing_migration(
            base_ref,
            normalized_paths,
            normalized_strict,
            repository_root=repository_root,
            head_ref=head_ref,
        )
    if normalized_paths == PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS:
        if normalized_strict != PR_SAFE_SNAPSHOT_SELF_STRICT_SURFACES:
            return False
        if not re.fullmatch(r"[0-9a-f]{40}", str(base_ref)):
            return False
        root = Path(repository_root).resolve()
        if not _pr_safe_repo_ref_is_ancestor(
            root,
            PR_SAFE_SNAPSHOT_BASE_CONTENT_REF_SHA,
            base_ref,
        ):
            return False
        if not _pr_safe_repo_ref_is_ancestor(root, base_ref, head_ref):
            return False
        authorization_payload = _pr_safe_repo_blob(
            root,
            base_ref,
            PR_SAFE_AUTHORIZATION_PATH,
        )
        if authorization_payload is None:
            return False
        errors = validate_pr_safe_control_plane_delta(
            normalized_paths,
            base_helper=_pr_safe_repo_blob(root, base_ref, PR_SAFE_SNAPSHOT_HELPER),
            base_test=_pr_safe_repo_blob(root, base_ref, PR_SAFE_SNAPSHOT_TEST),
            current_helper=_pr_safe_repo_blob(root, head_ref, PR_SAFE_SNAPSHOT_HELPER),
            current_test=_pr_safe_repo_blob(root, head_ref, PR_SAFE_SNAPSHOT_TEST),
            authorization_payload=authorization_payload,
        )
        if errors:
            return False
        base_lifecycle_inventory = _pr_safe_repo_blob(
            root,
            base_ref,
            PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY,
        )
        current_lifecycle_inventory = _pr_safe_repo_blob(
            root,
            head_ref,
            PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY,
        )
        if (
            base_lifecycle_inventory is None
            or canonical_blob_sha256(base_lifecycle_inventory)
            != PR_SAFE_SNAPSHOT_BASE_LIFECYCLE_INVENTORY_SHA256
            or current_lifecycle_inventory is None
            or canonical_blob_sha256(current_lifecycle_inventory)
            != PR_SAFE_SNAPSHOT_CURRENT_LIFECYCLE_INVENTORY_SHA256
        ):
            return False
        for ref in (base_ref, head_ref):
            for path in sorted(PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS):
                if _pr_safe_repo_blob_mode(root, ref, path) != PR_SAFE_SNAPSHOT_REQUIRED_MODE:
                    return False
        return True
    if normalized_paths != PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS:
        return False
    if normalized_strict != PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES:
        return False
    if not re.fullmatch(r"[0-9a-f]{40}", str(base_ref)):
        return False

    root = Path(repository_root).resolve()
    if not _pr_safe_repo_ref_is_ancestor(
        root,
        PR_SAFE_SNAPSHOT_BASE_CONTENT_REF_SHA,
        base_ref,
    ):
        return False
    if not _pr_safe_repo_ref_is_ancestor(root, base_ref, head_ref):
        return False

    base_blobs: dict[str, bytes | None] = {}
    current_blobs: dict[str, bytes] = {}
    for path in sorted(PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS):
        base_blob = _pr_safe_repo_blob(root, base_ref, path)
        current_blob = _pr_safe_repo_blob(root, head_ref, path)
        expected_base_sha = PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH[
            path
        ]
        if expected_base_sha is None:
            if base_blob is not None or _pr_safe_repo_blob_mode(root, base_ref, path) is not None:
                return False
        else:
            if base_blob is None or canonical_blob_sha256(base_blob) != expected_base_sha:
                return False
            if _pr_safe_repo_blob_mode(root, base_ref, path) != "100644":
                return False
        if current_blob is None:
            return False
        if canonical_blob_sha256(current_blob) != (
            PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH[path]
        ):
            return False
        if _pr_safe_repo_blob_mode(root, head_ref, path) != "100644":
            return False
        base_blobs[path] = base_blob
        current_blobs[path] = current_blob

    workflow_path = ".github/workflows/daily_full_pipeline.yml"
    base_workflow_blob = base_blobs[workflow_path]
    if base_workflow_blob is None:
        return False
    try:
        base_workflow = base_workflow_blob.decode("utf-8-sig")
        current_workflow = current_blobs[workflow_path].decode("utf-8-sig")
    except UnicodeError:
        return False
    base_workflow = base_workflow.replace("\r\n", "\n").replace("\r", "\n")
    current_workflow = current_workflow.replace("\r\n", "\n").replace("\r", "\n")
    anchor = PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_ANCHOR
    insertion = PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_INSERTION
    if base_workflow.count(anchor) != 1 or insertion in base_workflow:
        return False
    if current_workflow.count(anchor) != 1 or current_workflow.count(insertion) != 1:
        return False
    return current_workflow == base_workflow.replace(anchor, insertion + anchor, 1)
























def parse_pr_safe_authorizations(payload: bytes) -> tuple[list[dict[str, str]], list[str]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    except UnicodeError as exc:
        return [], [f"cannot decode PR-safe authorization ledger: {exc}"]
    if tuple(reader.fieldnames or ()) != PR_SAFE_AUTHORIZATION_COLUMNS:
        return [], ["PR-safe authorization ledger header mismatch"]
    rows: list[dict[str, str]] = []
    try:
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                return [], [
                    f"PR-safe authorization ledger row has extra fields: {line_number}"
                ]
            rows.append({str(key): str(value or "") for key, value in row.items()})
    except csv.Error as exc:
        return [], [f"cannot parse PR-safe authorization ledger: {exc}"]
    migration_ids = [row.get("migration_id", "").strip() for row in rows]
    if any(not migration_id for migration_id in migration_ids) or len(
        migration_ids
    ) != len(set(migration_ids)):
        return [], ["PR-safe authorization migration ids must be nonblank and unique"]
    return rows, []


def validate_pr_safe_authorization_history(
    rows: list[dict[str, str]],
) -> list[str]:
    retained = list(PR_SAFE_RETAINED_AUTHORIZATION_ROWS)
    if any(
        row.get("migration_id", "").strip() == PR_SAFE_SNAPSHOT_MIGRATION_ID
        for row in rows
    ):
        retained.extend(PR_SAFE_CONSUMED_AUTHORIZATION_ROWS)
    if rows[: len(retained)] != retained:
        return [
            "PR-safe authorization history must retain the exact append-only prefix"
        ]
    return []


def parse_pr_safe_lifecycle_authorizations(
    payload: bytes,
) -> tuple[list[dict[str, str]], list[str]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    except UnicodeError as exc:
        return [], [f"cannot decode lifecycle authorization ledger: {exc}"]
    if tuple(reader.fieldnames or ()) != PR_SAFE_LIFECYCLE_AUTHORIZATION_COLUMNS:
        return [], ["lifecycle authorization ledger header mismatch"]

    rows: list[dict[str, str]] = []
    errors: list[str] = []
    try:
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                errors.append(
                    "lifecycle authorization ledger row has extra fields: "
                    f"{line_number}"
                )
                continue
            normalized = {str(key): str(value or "").strip() for key, value in row.items()}
            rows.append(normalized)
    except csv.Error as exc:
        return [], [f"cannot parse lifecycle authorization ledger: {exc}"]

    migration_ids = [row.get("migration_id", "") for row in rows]
    if any(not migration_id for migration_id in migration_ids) or len(
        migration_ids
    ) != len(set(migration_ids)):
        errors.append("lifecycle authorization migration ids must be nonblank and unique")

    observed_targets: list[tuple[str, str]] = []
    for row in rows:
        target = (
            row.get("row_path", "").replace("\\", "/"),
            row.get("column", ""),
        )
        observed_targets.append(target)
        if row.get("status", "") != PR_SAFE_LIFECYCLE_AUTHORIZATION_STATUS:
            errors.append(
                "lifecycle authorization status must be preauthorized: "
                + row.get("migration_id", "")
            )
        if row.get("scope", "") != PR_SAFE_LIFECYCLE_AUTHORIZATION_SCOPE:
            errors.append(
                "lifecycle authorization scope mismatch: "
                + row.get("migration_id", "")
            )
        if not row.get("approval_reference", ""):
            errors.append(
                "lifecycle authorization lacks approval_reference: "
                + row.get("migration_id", "")
            )
        for field in ("base_value_sha256", "current_value_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", row.get(field, "")):
                errors.append(
                    f"lifecycle authorization {field} is not canonical SHA-256: "
                    + row.get("migration_id", "")
                )
        added_values = [
            value for value in row.get("added_values", "").split(";") if value
        ]
        removed_values = [
            value for value in row.get("removed_values", "").split(";") if value
        ]
        if added_values != sorted(set(added_values)):
            errors.append(
                "lifecycle authorization added_values must be sorted and unique: "
                + row.get("migration_id", "")
            )
        if removed_values != sorted(set(removed_values)):
            errors.append(
                "lifecycle authorization removed_values must be sorted and unique: "
                + row.get("migration_id", "")
            )
        if not added_values and not removed_values:
            errors.append(
                "lifecycle authorization must describe a semantic delta: "
                + row.get("migration_id", "")
            )
        if set(added_values) & set(removed_values):
            errors.append(
                "lifecycle authorization added/removed values overlap: "
                + row.get("migration_id", "")
            )

    if len(observed_targets) != len(set(observed_targets)):
        errors.append("lifecycle authorization targets must be unique")
    if set(observed_targets) != PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS:
        errors.append("lifecycle authorization target set mismatch")
    return rows, errors


def validate_pr_safe_control_plane_delta(
    changed_paths: set[str],
    *,
    base_helper: bytes | None,
    base_test: bytes | None = None,
    current_helper: bytes | None,
    current_test: bytes | None,
    authorization_payload: bytes,
    changed_workflow_blobs: dict[str, bytes | None] | None = None,
    target_id: str | None = None,
) -> list[str]:
    errors: list[str] = []
    immutable_changes = sorted(
        changed_paths & PR_SAFE_LEGACY_REPLAY_IMMUTABLE_PATHS
    )
    if immutable_changes:
        errors.append(
            "legacy replay shim may not modify its base-owned trust root: "
            + ", ".join(immutable_changes)
        )

    for path, payload in sorted((changed_workflow_blobs or {}).items()):
        if payload is None:
            continue
        try:
            workflow_text = payload.decode("utf-8-sig")
        except UnicodeError:
            errors.append(f"cannot decode changed workflow for spoof audit: {path}")
            continue
        if PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE.search(workflow_text):
            errors.append(
                "changed workflow requests checks/statuses write permission: " + path
            )

    protected_changes = changed_paths & PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS
    if not protected_changes:
        return errors
    if base_helper is None or current_helper is None or current_test is None:
        errors.append("preauthorized replay helper/test blobs must all exist")
        return errors
    contract = pr_safe_migration_contract_for_paths(
        changed_paths,
        base_helper_sha256=canonical_blob_sha256(base_helper),
        current_helper_sha256=canonical_blob_sha256(current_helper),
        current_test_sha256=canonical_blob_sha256(current_test),
        target_id=target_id,
    )
    if contract is None:
        errors.append(
            "PR-safe helper migration must change exactly the preauthorized paths"
        )
        return errors
    migration_id, _helper_path, _test_path, authorized_paths = contract

    authorizations, authorization_errors = parse_pr_safe_authorizations(
        authorization_payload
    )
    errors.extend(authorization_errors)
    errors.extend(validate_pr_safe_authorization_history(authorizations))
    matching = [
        row
        for row in authorizations
        if row.get("migration_id", "").strip() == migration_id
    ]
    if len(matching) != 1:
        errors.append(
            "base authorization ledger must contain exactly one matching replay migration"
        )
        return errors
    authorization = matching[0]
    observed_paths = {
        path.strip()
        for path in authorization.get("changed_paths", "").split(";")
        if path.strip()
    }
    expected = {
        "base_helper_sha256": canonical_blob_sha256(base_helper),
        "current_helper_sha256": canonical_blob_sha256(current_helper),
        "current_test_sha256": canonical_blob_sha256(current_test),
    }
    if authorization.get("status", "").strip() != "preauthorized":
        errors.append("replay migration authorization status is not preauthorized")
    if not authorization.get("approval_reference", "").strip():
        errors.append("replay migration authorization lacks approval_reference")
    if observed_paths != authorized_paths:
        errors.append("replay migration authorization changed_paths mismatch")
    for field, observed in expected.items():
        if authorization.get(field, "").strip() != observed:
            errors.append(f"PR-safe migration authorization {field} mismatch")

    if migration_id in {
        PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID,
        PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
        PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID,
    }:
        marker = migration_id.encode("utf-8")
        if marker in base_helper:
            errors.append("replay migration was already consumed by the base helper")
        if marker not in current_helper:
            errors.append("replay migration id is absent from the current helper")
    elif migration_id == PR_SAFE_SNAPSHOT_MIGRATION_ID:
        snapshot_expected = {
            "base_helper_sha256": PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256,
            "current_helper_sha256": PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256,
            "current_test_sha256": PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256,
        }
        for field, expected_sha in snapshot_expected.items():
            if expected[field] != expected_sha:
                errors.append(f"snapshot replay shim pinned {field} mismatch")
        if base_test is None:
            errors.append("snapshot replay shim base test blob must exist")
        elif canonical_blob_sha256(base_test) != PR_SAFE_SNAPSHOT_BASE_TEST_SHA256:
            errors.append("snapshot replay shim pinned base_test_sha256 mismatch")
    else:
        errors.append(f"unsupported retained replay migration id: {migration_id}")
    return errors


def validate_pr_safe_advanced_lifecycle_inventory_delta(
    base_payload: bytes | None,
    current_payload: bytes | None,
) -> list[str]:
    errors: list[str] = []
    if base_payload is None:
        errors.append("advanced helper preauthorization base lifecycle blob is missing")
    elif canonical_blob_sha256(base_payload) != (
        PR_SAFE_ADVANCED_BASE_LIFECYCLE_INVENTORY_SHA256
    ):
        errors.append("advanced helper preauthorization base lifecycle SHA mismatch")
    if current_payload is None:
        errors.append("advanced helper preauthorization current lifecycle blob is missing")
    elif canonical_blob_sha256(current_payload) != (
        PR_SAFE_ADVANCED_CURRENT_LIFECYCLE_INVENTORY_SHA256
    ):
        errors.append("advanced helper preauthorization current lifecycle SHA mismatch")
    return errors


def validate_pr_safe_input_bound_lifecycle_inventory_delta(
    base_payload: bytes | None,
    current_payload: bytes | None,
) -> list[str]:
    errors: list[str] = []
    if base_payload is None:
        errors.append("input-bound preauthorization base lifecycle blob is missing")
    elif canonical_blob_sha256(base_payload) != (
        PR_SAFE_INPUT_BOUND_BASE_LIFECYCLE_INVENTORY_SHA256
    ):
        errors.append("input-bound preauthorization base lifecycle SHA mismatch")
    if current_payload is None:
        errors.append("input-bound preauthorization current lifecycle blob is missing")
    elif canonical_blob_sha256(current_payload) != (
        PR_SAFE_INPUT_BOUND_CURRENT_LIFECYCLE_INVENTORY_SHA256
    ):
        errors.append("input-bound preauthorization current lifecycle SHA mismatch")
    return errors


def git_output_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {message}")
    return result.stdout


def git_blob_at_ref(ref: str, path: str) -> bytes | None:
    try:
        return git_output_bytes("show", f"{ref}:{path}")
    except RuntimeError:
        return None


def parse_git_name_status_entries_z(
    payload: bytes,
) -> tuple[dict[str, str], list[str]]:
    fields = payload.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    entries: dict[str, str] = {}
    errors: list[str] = []
    index = 0
    while index < len(fields):
        try:
            status = fields[index].decode("ascii")
        except UnicodeError:
            errors.append("git name-status output contains a non-ASCII status")
            break
        index += 1
        if not re.fullmatch(r"[ACDMRT][0-9]*", status):
            errors.append(f"git name-status output has unsupported status: {status!r}")
            break
        path_count = 2 if status[0] in {"R", "C"} else 1
        if index + path_count > len(fields):
            errors.append(f"git name-status output is truncated after status {status}")
            break
        for raw_path in fields[index : index + path_count]:
            try:
                path = raw_path.decode("utf-8").replace("\\", "/")
            except UnicodeError:
                errors.append(
                    f"git name-status output contains a non-UTF-8 path for {status}"
                )
                continue
            if not path:
                errors.append(f"git name-status output has a blank path for {status}")
            elif path in entries:
                errors.append(f"git name-status output repeats a path: {path}")
            else:
                entries[path] = status
        index += path_count
    return entries, errors


def parse_git_name_status_z(payload: bytes) -> tuple[set[str], list[str]]:
    entries, errors = parse_git_name_status_entries_z(payload)
    return set(entries), errors


def git_tree_entry_at_ref(ref: str, path: str) -> tuple[str, str, str, str] | None:
    payload = git_output_bytes("ls-tree", "-z", ref, "--", path)
    entries = [entry for entry in payload.split(b"\0") if entry]
    if not entries:
        return None
    if len(entries) != 1 or b"\t" not in entries[0]:
        raise RuntimeError(f"git ls-tree returned ambiguous evidence for {ref}:{path}")
    metadata, raw_path = entries[0].split(b"\t", 1)
    metadata_fields = metadata.decode("ascii").split()
    if len(metadata_fields) != 3:
        raise RuntimeError(f"git ls-tree returned malformed metadata for {ref}:{path}")
    try:
        observed_path = raw_path.decode("utf-8").replace("\\", "/")
    except UnicodeError as exc:
        raise RuntimeError(f"git ls-tree returned a non-UTF-8 path for {ref}:{path}") from exc
    mode, object_type, object_id = metadata_fields
    return mode, object_type, object_id, observed_path


def validate_pr_trust_root_change(
    base_sha: str,
    head_sha: str,
    *,
    base_repository: str = "",
    head_repository: str = "",
    maintainer_approved: str = "",
) -> list[str]:
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base_sha):
        return [f"invalid base SHA: {base_sha!r}"]
    if not re.fullmatch(r"[0-9a-fA-F]{40}", head_sha):
        return [f"invalid head SHA: {head_sha!r}"]

    errors: list[str] = []
    try:
        checkout_sha = git_output_bytes("rev-parse", "HEAD").decode("ascii").strip()
        if checkout_sha.lower() != base_sha.lower():
            errors.append(
                "base-owned guard checkout does not match pull request base SHA: "
                f"checkout={checkout_sha} base={base_sha}"
            )
        diff_payload = git_output_bytes(
            "diff",
            "--name-status",
            "-z",
            "--no-renames",
            "--diff-filter=ACDMRT",
            base_sha,
            head_sha,
            "--",
        )
    except (OSError, RuntimeError, UnicodeError) as exc:
        return [*errors, f"cannot inspect base-owned trust-root diff: {exc}"]

    changed_entries, diff_errors = parse_git_name_status_entries_z(diff_payload)
    errors.extend(diff_errors)
    trust_changes = sorted(set(changed_entries) & PR_SAFE_TRUST_ROOT_PATHS)
    if not trust_changes:
        return errors

    if (
        base_repository != PR_SAFE_REPOSITORY
        or head_repository != PR_SAFE_REPOSITORY
        or base_repository != head_repository
    ):
        errors.append("trust-root maintenance must originate from the same repository")
    if maintainer_approved != "true":
        errors.append(
            "trust-root maintenance requires the explicit "
            f"{PR_SAFE_TRUST_ROOT_APPROVAL_LABEL} label"
        )

    for path in trust_changes:
        status = changed_entries[path]
        if status != "M":
            errors.append(
                f"trust-root path must remain an in-place modification: {path} status={status}"
            )
        try:
            base_entry = git_tree_entry_at_ref(base_sha, path)
            head_entry = git_tree_entry_at_ref(head_sha, path)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        if base_entry is None or head_entry is None:
            errors.append(f"trust-root path must exist in base and head: {path}")
            continue
        base_mode, base_type, _base_oid, base_path = base_entry
        head_mode, head_type, _head_oid, head_path = head_entry
        if (
            base_path != path
            or head_path != path
            or base_mode != "100644"
            or head_mode != "100644"
            or base_type != "blob"
            or head_type != "blob"
        ):
            errors.append(
                "trust-root path must remain a 100644 regular blob: "
                f"path={path} base={base_mode}/{base_type}/{base_path} "
                f"head={head_mode}/{head_type}/{head_path}"
            )

    if PR_SAFE_BASE_GUARD_WORKFLOW in trust_changes:
        try:
            workflow_payload = git_blob_at_ref(head_sha, PR_SAFE_BASE_GUARD_WORKFLOW)
            if workflow_payload is None:
                errors.append("trust-root guard workflow head blob is missing")
            else:
                workflow_text = workflow_payload.decode("utf-8-sig")
                errors.extend(validate_pr_safe_base_guard_workflow_text(workflow_text))
        except (OSError, RuntimeError, UnicodeError) as exc:
            errors.append(f"cannot validate trust-root guard workflow head blob: {exc}")
    return errors


def validate_pr_safe_exact_migration_blob_modes(
    changed_paths: set[str],
    base_sha: str,
    head_sha: str,
) -> list[str]:
    contract = pr_safe_migration_contract_for_paths(changed_paths)
    if contract is None or contract[0] != PR_SAFE_SNAPSHOT_MIGRATION_ID:
        return []

    errors: list[str] = []
    for ref_label, ref in (("base", base_sha), ("head", head_sha)):
        for path in sorted(PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS):
            try:
                entry = git_tree_entry_at_ref(ref, path)
            except RuntimeError as exc:
                errors.append(str(exc))
                continue
            if entry is None:
                errors.append(
                    f"snapshot preauthorization path is missing from {ref_label}: {path}"
                )
                continue
            mode, object_type, _object_id, observed_path = entry
            if (
                mode != PR_SAFE_SNAPSHOT_REQUIRED_MODE
                or object_type != "blob"
                or observed_path != path
            ):
                errors.append(
                    "snapshot preauthorization requires exact regular blob mode: "
                    f"ref={ref_label} path={path} mode={mode} type={object_type} "
                    f"observed_path={observed_path}"
                )
    return errors
















def validate_pr_safe_base_guard_repository_invariants(
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    write_permission_owners: list[str] = []
    for path in sorted(workflow_paths):
        try:
            text = (ROOT / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read workflow for PR-safe collision audit: {path}: {exc}")
            continue
        if PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE.search(text):
            write_permission_owners.append(path)

    if write_permission_owners:
        errors.append(
            "audit-only workflows may not request checks/statuses write permission: "
            + ", ".join(write_permission_owners)
        )
    try:
        guard_text = (ROOT / PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return
    if "pull_request_target:" not in guard_text:
        errors.append("base-owned PR-safe audit workflow must use pull_request_target")
    if "actions/github-script" in guard_text:
        errors.append("audit-only PR-safe workflow may not use actions/github-script")
    errors.extend(validate_pr_safe_base_guard_workflow_text(guard_text))


def validate() -> list[str]:
    errors: list[str] = []
    rows_by_path = load_inventory(errors)
    python_paths = tracked_python_paths()
    test_python_paths = tracked_test_python_paths()
    executable_script_paths = tracked_executable_script_paths()
    workflow_paths = tracked_workflow_paths()

    if rows_by_path:
        validate_inventory_coverage(
            rows_by_path,
            python_paths,
            test_python_paths,
            executable_script_paths,
            workflow_paths,
            errors,
        )
        validate_inventory_rows(rows_by_path, errors)
        validate_workflow_invocations(rows_by_path, workflow_paths, errors)
        validate_allowed_stage_patterns(rows_by_path, errors)
        validate_production_artifact_writer_auth(rows_by_path, workflow_paths, errors)

    validate_workflow_snippets(errors)
    validate_active_guidance_commands(errors)
    validate_pr_safe_base_guard_repository_invariants(workflow_paths, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--validate-pr-trust-root-change",
        action="store_true",
    )
    parser.add_argument("--base-sha", default="")
    parser.add_argument("--head-sha", default="")
    parser.add_argument("--base-repository", default="")
    parser.add_argument("--head-repository", default="")
    parser.add_argument("--maintainer-approved", default="")
    args = parser.parse_args(argv or [])
    if args.validate_pr_trust_root_change:
        errors = validate_pr_trust_root_change(
            args.base_sha.strip(),
            args.head_sha.strip(),
            base_repository=args.base_repository.strip(),
            head_repository=args.head_repository.strip(),
            maintainer_approved=args.maintainer_approved.strip(),
        )
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("base-owned PR trust-root change validation passed")
        print(f"head_sha={args.head_sha.strip()}")
        return 0

    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    python_count = len(tracked_python_paths())
    test_python_count = len(tracked_test_python_paths())
    executable_script_count = len(tracked_executable_script_paths())
    workflow_count = len(tracked_workflow_paths())
    print("repo production inventory validation passed")
    print(f"validated_python_paths={python_count}")
    print(f"validated_test_python_paths={test_python_count}")
    print(f"validated_executable_scripts={executable_script_count}")
    print(f"validated_workflows={workflow_count}")
    print(f"inventory={INVENTORY.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
