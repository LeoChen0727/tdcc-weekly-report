from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

try:
    from scripts import detect_daily_model_pr_validation_scope as pr_scope
except ModuleNotFoundError:  # Direct execution from the scripts directory.
    import detect_daily_model_pr_validation_scope as pr_scope


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config/model_research_workflow_entrypoints.csv"
OWNERSHIP_REGISTRY = ROOT / "config/model_research_artifact_ownership.csv"
WORKFLOW = ROOT / ".github/workflows/research_backtest_pipeline.yml"
PR_VALIDATION_WORKFLOW = ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml"

REQUIRED_COLUMNS = {
    "workflow_path",
    "workflow_input",
    "model_id",
    "producer",
    "latest_stage_glob",
    "history_stage_glob",
    "docs_stage_glob",
    "default_enabled",
    "formal_sync_allowed",
}

FORBIDDEN_WORKFLOW_SCRIPTS = {
    "scripts/build_daily_model_parameter_research.py",
    "scripts/build_daily_w_bottom_operation_sections.py",
    "scripts/build_daily_price_pullback_23ema_operation_section.py",
    "scripts/build_model_operation_readiness.py",
    "scripts/build_approved_operation_patterns.py",
    "scripts/update_daily_published_model_snapshots.py",
}

FORBIDDEN_STAGE_SNIPPETS = {
    "git add output/history/research/ || true",
    "git add output/history/daily_model_snapshots/",
    "git add output/latest/model_operation_readiness_latest",
    "git add output/latest/approved_operation_patterns_latest",
    "git add output/latest/daily_w_bottom_",
    "git add output/latest/daily_neckline_",
    "git add output/latest/daily_price_pullback_23ema_",
    "git add output/latest/daily_volume_breakout_",
}

SHARED_DATA_INPUT = "run_shared_model_research_data_refresh"
SHARED_DATA_COMMANDS = {
    "python scripts/build_monthly_revenue_point_in_time_panel.py",
    "python scripts/build_daily_model_signal_background_features.py",
}
SHARED_DATA_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/monthly_revenue_point_in_time_panel_latest.* || true",
    "git add output/history/research/monthly_revenue_point_in_time_panel.csv || true",
    "git add output/latest/research_backtest/daily_model_signal_background_feature_panel_latest.* || true",
    "git add output/latest/research_backtest/daily_model_background_feature_catalog_latest.* || true",
}

BACKGROUND_REGISTRY_STRUCTURE_COMMAND = (
    "python scripts/validate_daily_model_background_data_registry.py --structure-only"
)
BACKGROUND_REGISTRY_FULL_COMMAND = (
    "python scripts/validate_daily_model_background_data_registry.py"
)
COMMIT_STEP_MARKER = "- name: Commit research and backtest outputs"
DEPLOY_KEY_STEP_NAME = "Require production artifact write deploy key"
CHECKOUT_STEP_NAME = "Checkout repository"
CHECKOUT_FETCH_DEPTH = "2"
SETUP_PYTHON_STEP_NAME = "Set up Python"
SYNC_TARGET_BRANCH_STEP_NAME = "Synchronize target branch before research"
SYNC_TARGET_BRANCH_COMMAND = 'git pull --ff-only origin "$TARGET_BRANCH"'
SYNC_TARGET_BRANCH_RUN_SHA256 = (
    "d798aca85bff30d0ac9ba49204e14bd79e35d7350e1a154a252b3e8eee7824ff"
)
PY_YAML_INSTALL_STEP_NAME = "Install pinned workflow contract parser"
PY_YAML_INSTALL_COMMAND = (
    "python -m pip install --disable-pip-version-check --no-input PyYAML==6.0.2"
)
RESEARCH_PREFLIGHT_STEP_NAME = "Validate Apps Script workflow triggers"
NON_MODEL_ARTIFACT_VALIDATION_STEP_NAME = (
    "Validate existing registered artifacts before non-model research"
)
NON_MODEL_ARTIFACT_VALIDATION_STEP_IF = (
    "${{ env.MODEL_RESEARCH_SELECTED != 'true' }}"
)
INSTALL_DEPENDENCIES_STEP_NAME = "Install dependencies"
INSTALL_DEPENDENCIES_STEP_IF = "${{ env.ANY_RESEARCH_SELECTED == 'true' }}"
REVENUE_BUILD_STEP_NAME = "Build model-owned revenue lag and strength research"
REVENUE_BUILD_STEP_IF = (
    "${{ github.event.inputs.run_revenue_unreacted_range_research == 'true' && "
    "github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_rebaseline_only "
    "!= 'true' && github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only "
    "!= 'true' && github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_supersede_only "
    "!= 'true' }}"
)
PUBLISH_STEP_NAME = "Commit research and backtest outputs"
PUBLISH_STEP_IF = (
    "${{ env.ANY_RESEARCH_SELECTED == 'true' && github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_rebaseline_only "
    "!= 'true' && github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only "
    "!= 'true' && github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_supersede_only "
    "!= 'true' }}"
)
POST_RUN_STEP_NAME = "Validate post-run model research contracts"
POST_RUN_STEP_IF = "${{ env.MODEL_RESEARCH_SELECTED == 'true' }}"
POST_RUN_RUN_SHA256 = (
    "92c33c29b61d045e838237d5e979102cef083542b62809e62a08b2012461ee0d"
)
POST_RUN_SENTINEL = "$RUNNER_TEMP/model-research-post-run-validation.pass"
RESEARCH_JOB_NAME = "research-backtest-pipeline"
RESEARCH_JOB_KEYS = frozenset({"runs-on", "env", "steps"})
RESEARCH_JOB_RUNNER = "ubuntu-latest"
RESEARCH_JOB_ENV_SHA256 = (
    "4933468887500747b18ae732aecac5991abf238514359c60eb050ffa311e6261"
)
PY_YAML_INSTALL_RUN_SHA256 = (
    "145c750702e5fc9867791c24a695b1e8becf145aa9fd0bf0d23069d07f5a46bf"
)
RESEARCH_PREFLIGHT_RUN_SHA256 = (
    "547fdcbcc8a02a23a3d40d9c3ce6bbb33c332189af6a8fef1c427064b0d6e6cc"
)
RESEARCH_PREFLIGHT_STEP_SHA256 = (
    "81692b57897d5d582dee95598e018d36ba9561d14dc04567ade28d898aeceeb8"
)
FORBIDDEN_SHELL_ENV_KEYS = frozenset({"BASH_ENV", "ENV"})
FORBIDDEN_CROSS_STEP_STATE_CHANNELS = frozenset({"GITHUB_ENV", "GITHUB_PATH"})
RESEARCH_JOB_STEP_CONTROL_SHA256 = (
    "43f8f0f808f62fcb4996db0de35ef3e700c1c80ca3566792a01ac125bfc4d167"
)
BOOTSTRAP_STEP_NAMES = (
    DEPLOY_KEY_STEP_NAME,
    CHECKOUT_STEP_NAME,
    SETUP_PYTHON_STEP_NAME,
    SYNC_TARGET_BRANCH_STEP_NAME,
    PY_YAML_INSTALL_STEP_NAME,
    RESEARCH_PREFLIGHT_STEP_NAME,
    NON_MODEL_ARTIFACT_VALIDATION_STEP_NAME,
    INSTALL_DEPENDENCIES_STEP_NAME,
)
BOOTSTRAP_STEP_MAPPING_SHA256 = {
    DEPLOY_KEY_STEP_NAME: (
        "87663af618fc1daf8ab346c87fb92d2b9374fbe8930ba1b53e44f4454aaded58"
    ),
    CHECKOUT_STEP_NAME: (
        "91b50d21141d82e199db7c155f372e5e38f87f47234cd911630cac53e3aabb98"
    ),
    SETUP_PYTHON_STEP_NAME: (
        "7fa739195c725b3acaf8e302eebec0ee273401d322190d801eddd6ae96275a83"
    ),
    NON_MODEL_ARTIFACT_VALIDATION_STEP_NAME: (
        "b7397161067b820108ebb62aa3600edf5241d71ef5c7ac7f4ab389d4765491c6"
    ),
    INSTALL_DEPENDENCIES_STEP_NAME: (
        "5150d9a1ad1775f64157bb121ae3d8f046cccb548bfedcf03f97944904ed4dc7"
    ),
}

REVENUE_WORKFLOW_INPUT = "run_revenue_unreacted_range_research"
REVENUE_PROJECTION_CHAIN_STAGE_INPUT = (
    "run_revenue_unreacted_range_source_snapshot_projection_chain_only"
)
REVENUE_PROJECTION_REBASELINE_STAGE_INPUT = (
    "run_revenue_unreacted_range_source_snapshot_projection_rebaseline_only"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_INPUT = (
    "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only"
)
REVENUE_PROJECTION_SUPERSEDE_STAGE_INPUT = (
    "run_revenue_unreacted_range_source_snapshot_projection_supersede_only"
)
REVENUE_PROJECTION_SUPERSEDE_IDENTITY_INPUTS = (
    "expected_base_sha",
    "expected_head_sha",
    "confirmation",
)
REVENUE_FORWARD_HOLDOUT_STAGE_INPUT = (
    "run_revenue_unreacted_range_forward_holdout_only"
)
REVENUE_PRODUCER = "scripts/build_revenue_unreacted_range_research.py"
REVENUE_FULL_BUILD_COMMAND = f"python {REVENUE_PRODUCER}"
REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage forward_holdout"
)
REVENUE_FORWARD_HOLDOUT_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_* || true",
    "git add output/history/research/"
    "revenue_unreacted_range_forward_holdout_* || true",
    "git add docs/latest/revenue_unreacted_range_forward_holdout_* || true",
}
REVENUE_FULL_STAGE_COMMANDS = {
    "git add output/latest/research_backtest/revenue_unreacted_range_* || true",
    "git add output/history/research/revenue_unreacted_range_* || true",
    "git add docs/latest/revenue_unreacted_range_* || true",
}
REVENUE_PROJECTION_CHAIN_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage source_snapshot_projection_chain"
)
REVENUE_PROJECTION_REBASELINE_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage source_snapshot_projection_rebaseline"
)
REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS = (
    "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py "
    "--projection-manifest output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py "
    "--manifest output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv "
    "--projected-detail output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff.py "
    "--v1-manifest output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv "
    "--v1-detail output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv "
    "--v2-manifest output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv "
    "--v2-detail output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv "
    "--diff-summary output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_"
    "diff_summary.csv --diff-detail output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_"
    "diff_detail.csv",
)
REVENUE_PROJECTION_REBASELINE_AUDIT_COMMANDS = (
    "python scripts/build_model_data_independence_audit.py",
    "python scripts/validate_model_data_independence.py",
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND = (
    "python scripts/build_model_data_independence_audit.py "
    "--normalize-existing-csv-line-endings-only"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_VALIDATOR_COMMANDS = (
    "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    "python scripts/validate_model_data_independence.py",
)
REVENUE_PROJECTION_SUPERSEDE_BUILD_COMMAND = (
    f"{REVENUE_FULL_BUILD_COMMAND} --stage "
    "source_snapshot_projection_supersede_and_chain"
)
REVENUE_PROJECTION_SUPERSEDE_STEP_NAME = (
    "Supersede revenue source projection v2 and rebuild downstream research chain"
)
REVENUE_PROJECTION_SUPERSEDE_STEP_IF = (
    "${{ github.event.inputs.run_revenue_unreacted_range_research == 'true' && "
    "github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_supersede_only "
    "== 'true' && github.ref_type == 'branch' && github.ref_name != 'main' }}"
)
REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME = (
    "Validate revenue projection supersede exact75 artifact closure"
)
REVENUE_PROJECTION_SUPERSEDE_STAGE_STEP_NAME = (
    "Stage validated revenue projection supersede exact75 artifacts"
)
REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME = (
    "Commit validated revenue projection supersede exact75 artifacts"
)
REVENUE_PROJECTION_SUPERSEDE_IDENTITY_FILE = (
    "$RUNNER_TEMP/revenue-projection-supersede-exact75-validated-identity.tsv"
)
REVENUE_PROJECTION_SUPERSEDE_TRUSTED_CANDIDATE_COMMIT = (
    "4bcaa07123ef4a000c187dc2f19caefbec4cf252"
)
REVENUE_PROJECTION_SUPERSEDE_CODE_ROOT_SHA = (
    "2315df2367b6b475ed4f4aa2fe8b260617854991"
)
REVENUE_PROJECTION_SUPERSEDE_CONFIRMATION = (
    "supersede_revenue_source_snapshot_projection_v2"
)
REVENUE_PROJECTION_SUPERSEDE_RUN_BODY = "\n".join(
    (
        "set -euo pipefail",
        REVENUE_PROJECTION_SUPERSEDE_BUILD_COMMAND,
        "python scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
        "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
        REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS[2],
        "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py",
        "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
        "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
        "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "python scripts/build_model_data_independence_audit.py",
        "python scripts/validate_model_data_independence.py",
    )
)
REVENUE_PROJECTION_REBASELINE_COMMANDS = (
    REVENUE_PROJECTION_REBASELINE_BUILD_COMMAND,
    *REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS,
    *REVENUE_PROJECTION_REBASELINE_AUDIT_COMMANDS,
)
REVENUE_PROJECTION_REBASELINE_STEP_IF = (
    "${{ github.event.inputs.run_revenue_unreacted_range_research == 'true' && "
    "github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_rebaseline_only "
    "== 'true' && github.ref_type == 'branch' && github.ref_name != 'main' }}"
)
REVENUE_PROJECTION_REBASELINE_PRECHECK_STEP_NAME = (
    "Validate immutable revenue projection v1 before rebaseline"
)
REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS = (
    (
        "Build revenue source projection v2 rebaseline candidate",
        REVENUE_PROJECTION_REBASELINE_BUILD_COMMAND,
    ),
    (
        "Validate rebaseline source-first audit against projection v2",
        REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS[0],
    ),
    (
        "Validate revenue source projection v2 rebaseline candidate",
        REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS[1],
    ),
    (
        "Validate revenue source projection v1 to v2 diff",
        REVENUE_PROJECTION_REBASELINE_VALIDATOR_COMMANDS[2],
    ),
    (
        "Build rebaseline model data independence audit",
        REVENUE_PROJECTION_REBASELINE_AUDIT_COMMANDS[0],
    ),
    (
        "Validate rebaseline model data independence audit",
        REVENUE_PROJECTION_REBASELINE_AUDIT_COMMANDS[1],
    ),
)
REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME = (
    "Validate revenue rebaseline exact17 artifact closure"
)
REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME = (
    "Stage validated revenue rebaseline exact17 artifacts"
)
REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME = (
    "Commit validated revenue rebaseline exact17 artifacts"
)
REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE = (
    "$RUNNER_TEMP/revenue-rebaseline-exact17-validated-identity.tsv"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF = (
    "${{ github.event.inputs.run_revenue_unreacted_range_research == 'true' && "
    "github.event.inputs."
    "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only "
    "== 'true' && github.ref_type == 'branch' && github.ref_name != 'main' }}"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND_STEPS = (
    (
        "Normalize revenue projection candidate audit CSV line endings",
        REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND,
    ),
    (
        "Validate repaired revenue projection candidate audit CSVs",
        "\n".join(REVENUE_PROJECTION_CANDIDATE_REPAIR_VALIDATOR_COMMANDS),
    ),
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME = (
    "Validate revenue candidate repair exact2 artifact closure"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME = (
    "Stage validated revenue candidate repair exact2 artifacts"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME = (
    "Commit validated revenue candidate repair exact2 artifacts"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_IDENTITY_FILE = (
    "$RUNNER_TEMP/revenue-candidate-repair-exact2-validated-identity.tsv"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT = (
    "4bcaa07123ef4a000c187dc2f19caefbec4cf252"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_RUN_ATTEMPT_GUARD = (
    'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
    '"$GITHUB_RUN_ATTEMPT" != "1" ]]; then'
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_DISPATCH_HEAD_GUARD = (
    'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
    '"$(git rev-parse HEAD)" != "$GITHUB_SHA" ]]; then'
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_CODE_PARENT_GUARD = (
    'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
    '"$(git rev-parse HEAD^)" != '
    f'"{REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT}" ]]; then'
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES = "41824"
REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256 = (
    "2ff7e9c3140f0540ffb0238ba0937893b03de39bd2bcd5d84559b53a649685be"
)
# These digests lock the two non-trivial shell contracts without relying on
# substring presence. They are recalculated only when the audited shell bodies
# intentionally change alongside focused mutation coverage.
REVENUE_PROJECTION_REBASELINE_PRECHECK_RUN_SHA256 = (
    "54d9e4fb9ec8ebf223d202477fa7b27d310f4a09b85e52375f5531be0305c9df"
)
REVENUE_PROJECTION_REBASELINE_CLOSURE_RUN_SHA256 = (
    "8e043894954deef5bc7ca49b20d5566ca4f8791562193c9f89b79846635ef7b5"
)
REVENUE_PROJECTION_REBASELINE_STAGE_RUN_SHA256 = (
    "65481f4d297be68035faf9e59b2b39645b8235a5635d42da09bdfcb9c6055c9b"
)
REVENUE_PROJECTION_REBASELINE_COMMIT_RUN_SHA256 = (
    "a0d11a38ce1ff41e9c7a23551f080a4a68000a1d2b47931322c47693746d69f3"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_RUN_SHA256 = (
    "2f1dc9b0d65b713f8639dd1dd1f5c46b28eb4ead4f4825456e22cfbeac3e6d5a"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_RUN_SHA256 = (
    "eaf19f5f5a95c7d4488af06950ea39ccb0c7a6e108050eb1e7ce995dcaedc985"
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_RUN_SHA256 = (
    "4cc4bbb5ef0c70529bf41e81c5f17fb40944e26114112ae6e1f40a29192389f4"
)
REVENUE_PROJECTION_REBASELINE_V1_CANONICAL_PATHS = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest.csv",
    "docs/latest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
)
REVENUE_PROJECTION_REBASELINE_V1_IDENTITIES = (
    (
        REVENUE_PROJECTION_REBASELINE_V1_CANONICAL_PATHS[0],
        "148157",
        "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e",
    ),
    (
        REVENUE_PROJECTION_REBASELINE_V1_CANONICAL_PATHS[1],
        "26633382",
        "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a",
    ),
    (
        REVENUE_PROJECTION_REBASELINE_V1_CANONICAL_PATHS[2],
        "148157",
        "cee652015f334b9d3b464b4703a2199f2652845e0daa3dcffeef8ab2978700db",
    ),
    (
        REVENUE_PROJECTION_REBASELINE_V1_CANONICAL_PATHS[3],
        "148157",
        "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e",
    ),
)
REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS = (
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_archive_evidence_v1_20260731.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_summary.csv",
    "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_detail.csv",
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_latest.csv",
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv",
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_latest.md",
    "output/history/research/"
    "revenue_unreacted_range_source_first_condition_audit.csv",
    "docs/latest/revenue_unreacted_range_source_first_condition_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_source_first_condition_audit_latest.md",
    "output/latest/model_data_independence_audit_latest.csv",
    "output/latest/model_data_independence_audit_latest.md",
    "docs/latest/model_data_independence_audit_latest.csv",
    "docs/latest/model_data_independence_audit_latest.md",
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS = (
    "output/latest/model_data_independence_audit_latest.csv",
    "docs/latest/model_data_independence_audit_latest.csv",
)
REVENUE_PROJECTION_SUPERSEDE_CODE_PATHS = (
    ".github/workflows/research_backtest_pipeline.yml",
    "config/apps_script_research_dispatch_inputs.csv",
    "config/daily_model_background_data_registry.csv",
    "config/daily_model_data_sharing_migrations.csv",
    "config/daily_model_data_sharing_registry.csv",
    "config/repo_file_lifecycle_inventory.csv",
    "config/repo_production_inventory.csv",
    "config/report_artifact_lineage.csv",
    "scripts/build_revenue_unreacted_range_research.py",
    "scripts/revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "scripts/revenue_unreacted_range_lag_strength_matrix.py",
    "scripts/revenue_unreacted_range_launch_timing_feature_audit.py",
    "scripts/revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    "scripts/revenue_unreacted_range_operation_lag_bucket_audit.py",
    "scripts/revenue_unreacted_range_position_shape_transition_matrix.py",
    "scripts/revenue_unreacted_range_rearmed_operation_grid.py",
    "scripts/revenue_unreacted_range_source_snapshot_projection.py",
    "scripts/validate_apps_script_workflow_triggers.py",
    "scripts/validate_model_research_workflow_isolation.py",
    "scripts/validate_repo_file_lifecycle_inventory.py",
    "scripts/validate_repo_production_inventory.py",
    "scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "scripts/validate_revenue_unreacted_range_lag_strength_matrix.py",
    "scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py",
    "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    "scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
    "scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
    "scripts/validate_revenue_unreacted_range_promotion_preparation.py",
    "scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
    "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    "tests/test_daily_production_boundaries.py",
    "tests/test_model_data_independence.py",
    "tests/test_model_research_workflow_isolation.py",
    "tests/test_repo_file_lifecycle_inventory.py",
    "tests/test_repo_production_inventory.py",
    "tests/test_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "tests/test_revenue_unreacted_range_lag_strength_matrix.py",
    "tests/test_revenue_unreacted_range_launch_timing_feature_audit.py",
    "tests/test_revenue_unreacted_range_operation_lag_bucket_audit.py",
    "tests/test_revenue_unreacted_range_position_shape_transition_matrix.py",
    "tests/test_revenue_unreacted_range_rearmed_operation_grid.py",
    "tests/test_revenue_unreacted_range_source_snapshot_projection.py",
    "tests/test_validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    "tests/test_validate_revenue_unreacted_range_promotion_preparation.py",
)
REVENUE_PROJECTION_SUPERSEDE_ALLOWED_PATHS = (
    "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_detail_latest.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest.csv",
    "docs/latest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_supersede_evidence_v2_20260822.csv",
    "docs/latest/revenue_unreacted_range_forward_confirmation_feature_audit_feature_contrast_latest.csv",
    "docs/latest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.md",
    "docs/latest/revenue_unreacted_range_forward_confirmation_feature_audit_operation_return_review_latest.csv",
    "docs/latest/revenue_unreacted_range_lag_strength_matrix_latest.csv",
    "docs/latest/revenue_unreacted_range_lag_strength_matrix_latest.md",
    "docs/latest/revenue_unreacted_range_launch_timing_feature_audit_feature_contrast_latest.csv",
    "docs/latest/revenue_unreacted_range_launch_timing_feature_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_launch_timing_feature_audit_latest.md",
    "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
    "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast_latest.csv",
    "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.md",
    "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation_latest.csv",
    "docs/latest/revenue_unreacted_range_operation_lag_bucket_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_operation_lag_bucket_audit_latest.md",
    "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_latest.csv",
    "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_latest.md",
    "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_transition_latest.csv",
    "docs/latest/revenue_unreacted_range_rearmed_operation_grid_latest.csv",
    "docs/latest/revenue_unreacted_range_rearmed_operation_grid_latest.md",
    "docs/latest/revenue_unreacted_range_rearmed_operation_grid_operation_return_review_latest.csv",
    "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit.csv",
    "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit_feature_contrast.csv",
    "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit_operation_return_review.csv",
    "output/history/research/revenue_unreacted_range_lag_strength_matrix.csv",
    "output/history/research/revenue_unreacted_range_launch_timing_feature_audit.csv",
    "output/history/research/revenue_unreacted_range_launch_timing_feature_audit_feature_contrast.csv",
    "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit.csv",
    "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_detail.csv",
    "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast.csv",
    "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation.csv",
    "output/history/research/revenue_unreacted_range_operation_lag_bucket_audit.csv",
    "output/history/research/revenue_unreacted_range_position_shape_transition_matrix.csv",
    "output/history/research/revenue_unreacted_range_position_shape_transition_matrix_transition.csv",
    "output/history/research/revenue_unreacted_range_rearmed_operation_grid.csv",
    "output/history/research/revenue_unreacted_range_rearmed_operation_grid_operation_return_review.csv",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_event_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_feature_contrast_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_operation_return_review_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_lag_strength_matrix_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_lag_strength_matrix_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_lag_strength_matrix_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_feature_contrast_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_transition_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_latest.md",
    "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_operation_return_review_latest.csv",
    "output/latest/model_data_independence_audit_latest.csv",
    "output/latest/model_data_independence_audit_latest.md",
    "docs/latest/model_data_independence_audit_latest.csv",
    "docs/latest/model_data_independence_audit_latest.md",
)
REVENUE_PROJECTION_SUPERSEDE_IMMUTABLE_PATHS = (
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_archive_evidence_v1_20260731.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_summary.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_detail.csv",
)
REVENUE_PROJECTION_SUPERSEDE_LITERAL_GIT_ADD = (
    "git --no-replace-objects add -- \\\n  "
    + " \\\n  ".join(REVENUE_PROJECTION_SUPERSEDE_ALLOWED_PATHS)
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS = tuple(
    path
    for path in REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS
    if path not in REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS
)
REVENUE_PROJECTION_REBASELINE_LITERAL_GIT_ADD = "git add -- \\\n  " + " \\\n  ".join(
    REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS
)
REVENUE_PROJECTION_CANDIDATE_REPAIR_LITERAL_GIT_ADD = "git add -- \\\n  " + " \\\n  ".join(
    REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS
)
REVENUE_PROJECTION_REBASELINE_EXPECTED_PATH_OCCURRENCES = (
    10,
    10,
    8,
    14,
    12,
    10,
    10,
    6,
    6,
    6,
    6,
    6,
    6,
    12,
    10,
    12,
    10,
)
REVENUE_PROJECTION_REBASELINE_FORBIDDEN_COMPANION_INPUTS = (
    "run_market_timing",
    "run_weekly_surge",
    "run_explosive_volume",
    "run_surge_model",
    "run_signal_performance",
    "run_volume_breakout",
    "run_catalyst_performance",
    "run_msci_rebalance",
    "run_tdcc_signal_performance",
    "run_tdcc_short_term_edge",
    "run_short_term_specialty_packet",
    "run_shared_model_research_data_refresh",
    "run_price_pullback_23ema_research",
    "run_volume_range_breakout_v2_research",
)
REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS = {
    "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
    "python scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py",
    "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py",
    "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
    "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
    "python scripts/validate_revenue_unreacted_range_position_shape_transition_matrix.py",
    "python scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    "python scripts/validate_revenue_unreacted_range_promotion_preparation.py --require-source-artifacts",
}

PUBLISH_COMMIT = 'git commit -m "Update research backtest outputs"'
PUBLISH_PUSH = 'git push origin "HEAD:$TARGET_BRANCH"'
REVENUE_REBASELINE_COMMIT = (
    'git commit -m "Update revenue projection v2 rebaseline candidate artifacts"'
)
REVENUE_CANDIDATE_REPAIR_COMMIT = (
    'git commit -m "Repair revenue projection v2 candidate audit CSV line endings"'
)
REVENUE_SUPERSEDE_COMMIT = (
    'git --no-replace-objects commit -m '
    '"Supersede revenue source projection v2 research canonical artifacts"'
)
REVENUE_SUPERSEDE_PUSH = (
    'git --no-replace-objects push origin "HEAD:$TARGET_BRANCH"'
)
PUBLISH_FAIL_CLOSED_SHELL = "set -euo pipefail"
PUBLISH_NO_CHANGE_GUARD = (
    "if git diff --cached --quiet; then\n"
    'echo "No changes to commit"\n'
    "exit 0\n"
    "fi"
)
FORBIDDEN_PUBLISH_REWRITE = re.compile(
    r"^git\s+(?:pull|fetch|rebase|merge|reset|checkout|switch)(?:\s|$)"
)


@dataclass(frozen=True)
class WorkflowEntrypoint:
    workflow_path: str
    workflow_input: str
    model_id: str
    producer: str
    latest_stage_glob: str
    history_stage_glob: str
    docs_stage_glob: str
    default_enabled: bool
    formal_sync_allowed: bool


class _UniqueKeyBaseLoader(yaml.BaseLoader):
    """String-preserving loader that rejects duplicate semantic mapping keys."""


def _construct_unique_mapping(
    loader: _UniqueKeyBaseLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    if not isinstance(node, yaml.MappingNode):
        raise yaml.constructor.ConstructorError(
            None,
            None,
            "expected a mapping node",
            node.start_mark,
        )
    mapping: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key == "<<":
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "YAML merge keys are forbidden in the research workflow contract",
                key_node.start_mark,
            )
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable mapping key",
                key_node.start_mark,
            ) from exc
        if duplicate:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate semantic key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyBaseLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _semantic_workflow_mapping(text: str) -> tuple[dict[object, object] | None, list[str]]:
    try:
        tokens = yaml.scan(text, Loader=_UniqueKeyBaseLoader)
        for token in tokens:
            if isinstance(
                token,
                (yaml.tokens.AnchorToken, yaml.tokens.AliasToken, yaml.tokens.TagToken),
            ):
                return None, [
                    "research workflow YAML anchors, aliases, and explicit tags are "
                    f"forbidden: token={type(token).__name__} line={token.start_mark.line + 1}"
                ]
        parsed = yaml.load(text, Loader=_UniqueKeyBaseLoader)
    except yaml.YAMLError as exc:
        return None, [f"research workflow YAML semantic parse failed: {exc}"]
    if not isinstance(parsed, dict):
        return None, ["research workflow YAML root must be a semantic mapping"]
    return parsed, []


def _mapping_defaults_run_shell(mapping: dict[object, object]) -> bool:
    defaults = mapping.get("defaults")
    if not isinstance(defaults, dict):
        return False
    run_defaults = defaults.get("run")
    return isinstance(run_defaults, dict) and "shell" in run_defaults


def _as_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized not in {"true", "false"}:
        raise ValueError(f"invalid boolean value: {value}")
    return normalized == "true"


def load_registry(path: Path = REGISTRY) -> list[WorkflowEntrypoint]:
    if not path.is_file():
        raise RuntimeError(f"missing model research workflow registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
            raise RuntimeError("model research workflow registry schema is incomplete")
        rows = list(reader)
    if not rows:
        raise RuntimeError("model research workflow registry is empty")
    return [
        WorkflowEntrypoint(
            workflow_path=row["workflow_path"].strip(),
            workflow_input=row["workflow_input"].strip(),
            model_id=row["model_id"].strip(),
            producer=row["producer"].strip(),
            latest_stage_glob=row["latest_stage_glob"].strip(),
            history_stage_glob=row["history_stage_glob"].strip(),
            docs_stage_glob=row["docs_stage_glob"].strip(),
            default_enabled=_as_bool(row["default_enabled"]),
            formal_sync_allowed=_as_bool(row["formal_sync_allowed"]),
        )
        for row in rows
    ]


def load_model_owned_producers(path: Path = OWNERSHIP_REGISTRY) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, str] = {}
    for row in rows:
        if row.get("change_policy", "").strip() != "model_owned_write":
            continue
        model_id = row.get("owner_model_id", "").strip()
        producer = row.get("producer", "").strip()
        previous = result.setdefault(model_id, producer)
        if previous != producer:
            raise RuntimeError(f"model has multiple model-owned producers: {model_id}")
    return result


def workflow_input_defaults(text: str) -> dict[str, str]:
    match = re.search(r"(?ms)^    inputs:\s*\n(?P<body>.*?)(?=^permissions:)", text)
    if not match:
        return {}
    body = match.group("body")
    rows: dict[str, str] = {}
    input_matches = list(
        re.finditer(r"(?m)^      (?P<name>[A-Za-z0-9_]+):\s*$", body)
    )
    for index, input_match in enumerate(input_matches):
        block_end = (
            input_matches[index + 1].start()
            if index + 1 < len(input_matches)
            else len(body)
        )
        input_body = body[input_match.end() : block_end]
        default_match = re.search(
            r'(?m)^        default:\s*(?:(?:"(?P<quoted>true|false)")|'
            r"(?P<plain>true|false))\s*$",
            input_body,
        )
        if default_match:
            rows[input_match.group("name")] = (
                default_match.group("quoted") or default_match.group("plain")
            )
    return rows


def workflow_input_types(text: str) -> dict[str, str]:
    match = re.search(r"(?ms)^    inputs:\s*\n(?P<body>.*?)(?=^permissions:)", text)
    if not match:
        return {}
    body = match.group("body")
    rows: dict[str, str] = {}
    input_matches = list(
        re.finditer(r"(?m)^      (?P<name>[A-Za-z0-9_]+):\s*$", body)
    )
    for index, input_match in enumerate(input_matches):
        block_end = (
            input_matches[index + 1].start()
            if index + 1 < len(input_matches)
            else len(body)
        )
        input_body = body[input_match.end() : block_end]
        type_match = re.search(r"(?m)^        type:\s*(?P<type>[A-Za-z0-9_-]+)\s*$", input_body)
        if type_match:
            rows[input_match.group("name")] = type_match.group("type")
    return rows


def workflow_step_blocks(text: str) -> list[str]:
    return [block for block in re.split(r"(?m)^      - name: ", text)[1:] if block.strip()]


def _normalized_shell_block(block: str) -> str:
    return "\n".join(line.strip() for line in block.splitlines() if line.strip())


def _shell_array_values(block: str, variable: str) -> tuple[str, ...]:
    match = re.search(
        rf"(?ms)^\s*{re.escape(variable)}=\(\s*\n(?P<body>.*?)^\s*\)\s*$",
        block,
    )
    if not match:
        return ()
    return tuple(
        line.strip()
        for line in match.group("body").splitlines()
        if line.strip()
    )


def _named_step_blocks(blocks: list[str], name: str) -> list[str]:
    return [
        block
        for block in blocks
        if block.splitlines() and block.splitlines()[0].strip() == name
    ]


def _step_run_body(block: str) -> str | None:
    lines = block.splitlines()
    run_indices = [
        index
        for index, line in enumerate(lines)
        if line == "        run: |"
    ]
    if len(run_indices) != 1:
        return None
    run_index = run_indices[0]
    body_lines: list[str] = []
    for line in lines[run_index + 1 :]:
        if not line.strip():
            body_lines.append("")
            continue
        if not line.startswith("          "):
            return None
        body_lines.append(line[10:])
    while body_lines and not body_lines[-1]:
        body_lines.pop()
    return "\n".join(body_lines)


def _step_run_sha256(block: str) -> str | None:
    body = _step_run_body(block)
    if body is None:
        return None
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _step_block_sha256(block: str) -> str:
    return hashlib.sha256(block.rstrip().encode("utf-8")).hexdigest()


def _semantic_step_run_body(step: dict[object, object]) -> str | None:
    run = step.get("run")
    if not isinstance(run, str):
        return None
    return run.rstrip("\n")


def _semantic_step_run_sha256(step: dict[object, object]) -> str | None:
    run = _semantic_step_run_body(step)
    if run is None:
        return None
    return hashlib.sha256(run.encode("utf-8")).hexdigest()


def _semantic_mapping_sha256(mapping: dict[object, object]) -> str:
    try:
        canonical = json.dumps(mapping, sort_keys=True, separators=(",", ":"))
    except (TypeError, ValueError):
        return ""
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _semantic_step_control_sha256(steps: list[dict[object, object]]) -> str:
    control_keys = ("name", "if", "uses", "shell", "continue-on-error")
    control_manifest = [
        {key: step[key] for key in control_keys if key in step}
        for step in steps
    ]
    try:
        canonical = json.dumps(
            control_manifest,
            sort_keys=True,
            separators=(",", ":"),
        )
    except (TypeError, ValueError):
        return ""
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def validate_unmasked_step_contracts(text: str, blocks: list[str]) -> list[str]:
    errors: list[str] = []
    workflow_mapping, yaml_errors = _semantic_workflow_mapping(text)
    errors.extend(yaml_errors)
    if workflow_mapping is None:
        return errors

    if _mapping_defaults_run_shell(workflow_mapping):
        errors.append(
            "research workflow must not override defaults.run.shell because it can "
            "mask a failing validator or side-effect guard"
        )
    if "defaults" in workflow_mapping:
        errors.append(
            "research workflow must not define workflow-level defaults because run "
            "shell or working-directory drift can redirect every validator and "
            "side-effect guard"
        )
    if "env" in workflow_mapping:
        errors.append(
            "research workflow must not define workflow-level env because it can "
            "inject shell startup state into every validator and side-effect guard"
        )
    for key in ("if", "shell", "continue-on-error"):
        if key in workflow_mapping:
            errors.append(
                f"research workflow must not define top-level {key} metadata: "
                f"actual={workflow_mapping[key]!r}"
            )

    jobs = workflow_mapping.get("jobs")
    if not isinstance(jobs, dict):
        errors.append("research workflow jobs must be a semantic mapping")
        return errors
    if set(jobs) != {RESEARCH_JOB_NAME}:
        errors.append(
            "research workflow jobs must contain exactly the single protected research "
            f"job: actual={sorted(map(str, jobs))}"
        )
    job = jobs.get(RESEARCH_JOB_NAME)
    if not isinstance(job, dict):
        errors.append(
            "research workflow job must retain its exact semantic mapping key: "
            f"{RESEARCH_JOB_NAME}"
        )
        return errors
    if set(job) != RESEARCH_JOB_KEYS:
        errors.append(
            "research workflow job semantic keys must remain exact to forbid container, "
            "service, defaults, and alternate-runtime injection: "
            f"actual={sorted(map(str, job))}"
        )
    if job.get("runs-on") != RESEARCH_JOB_RUNNER:
        errors.append(
            "research workflow job runner must remain exact: "
            f"actual={job.get('runs-on')!r}"
        )
    if _mapping_defaults_run_shell(job):
        errors.append(
            "research workflow job must not override defaults.run.shell because it can "
            "mask a failing validator or side-effect guard"
        )
    for key in ("if", "shell", "continue-on-error"):
        if key in job:
            errors.append(
                f"research workflow job must not define {key} metadata: "
                f"actual={job[key]!r}"
            )
    job_env = job.get("env")
    if not isinstance(job_env, dict):
        errors.append("research workflow job env must remain a semantic mapping")
    else:
        forbidden_job_env = sorted(FORBIDDEN_SHELL_ENV_KEYS.intersection(job_env))
        if forbidden_job_env:
            errors.append(
                "research workflow job env must not define shell startup injection "
                f"keys: actual={forbidden_job_env}"
            )
        job_env_digest = hashlib.sha256(
            json.dumps(job_env, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        if job_env_digest != RESEARCH_JOB_ENV_SHA256:
            errors.append(
                "research workflow job env drift can skip validators or redirect publish: "
                f"actual_sha256={job_env_digest}"
            )

    semantic_steps = job.get("steps")
    if not isinstance(semantic_steps, list) or not all(
        isinstance(step, dict) for step in semantic_steps
    ):
        errors.append("research workflow steps must be a semantic list of mappings")
        return errors

    step_control_digest = _semantic_step_control_sha256(semantic_steps)
    if step_control_digest != RESEARCH_JOB_STEP_CONTROL_SHA256:
        errors.append(
            "research workflow step control plane drift can activate an unvalidated "
            "writer or reorder the rebaseline execution chain: "
            f"actual_sha256={step_control_digest}"
        )

    for index, step in enumerate(semantic_steps):
        run = step.get("run")
        if run is not None and not isinstance(run, str):
            errors.append(
                "research workflow run must remain a decoded semantic scalar: "
                f"step={step.get('name', index)!r}"
            )
        elif isinstance(run, str):
            forbidden_channels = sorted(
                channel
                for channel in FORBIDDEN_CROSS_STEP_STATE_CHANNELS
                if channel in run
            )
            if forbidden_channels:
                errors.append(
                    "research workflow run must not write or reference cross-step shell "
                    "state channels: "
                    f"step={step.get('name', index)!r} actual={forbidden_channels}"
                )

        step_env = step.get("env")
        if step_env is None:
            continue
        if not isinstance(step_env, dict):
            errors.append(
                "research workflow step env must remain a semantic mapping: "
                f"step={step.get('name', index)!r}"
            )
            continue
        forbidden_step_env = sorted(FORBIDDEN_SHELL_ENV_KEYS.intersection(step_env))
        if forbidden_step_env:
            errors.append(
                "research workflow step env must not define shell startup injection "
                f"keys: step={step.get('name', index)!r} actual={forbidden_step_env}"
            )

    critical_contracts = (
        (
            DEPLOY_KEY_STEP_NAME,
            None,
            "deploy-key precondition",
            {"name", "shell", "env", "run"},
        ),
        (
            CHECKOUT_STEP_NAME,
            None,
            "repository checkout",
            {"name", "uses", "with"},
        ),
        (
            SETUP_PYTHON_STEP_NAME,
            None,
            "Python runtime setup",
            {"name", "uses", "with"},
        ),
        (
            SYNC_TARGET_BRANCH_STEP_NAME,
            None,
            "target branch synchronization",
            {"name", "run"},
        ),
        (
            PY_YAML_INSTALL_STEP_NAME,
            None,
            "pinned PyYAML install",
            {"name", "run"},
        ),
        (
            RESEARCH_PREFLIGHT_STEP_NAME,
            None,
            "research preflight",
            {"name", "env", "run"},
        ),
        (
            NON_MODEL_ARTIFACT_VALIDATION_STEP_NAME,
            NON_MODEL_ARTIFACT_VALIDATION_STEP_IF,
            "non-model artifact validation skip guard",
            {"name", "if", "run"},
        ),
        (
            INSTALL_DEPENDENCIES_STEP_NAME,
            INSTALL_DEPENDENCIES_STEP_IF,
            "research dependency installation",
            {"name", "if", "run"},
        ),
        (
            REVENUE_BUILD_STEP_NAME,
            REVENUE_BUILD_STEP_IF,
            "revenue build",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_REBASELINE_PRECHECK_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_STEP_IF,
            "revenue rebaseline immutable v1 precheck",
            {"name", "if", "run"},
        ),
        *(
            (
                step_name,
                REVENUE_PROJECTION_REBASELINE_STEP_IF,
                step_name,
                {"name", "if", "run"},
            )
            for step_name, _command in REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS
        ),
        *(
            (
                step_name,
                REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF,
                step_name,
                {"name", "if", "run"},
            )
            for step_name, _command in REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND_STEPS
        ),
        (
            REVENUE_PROJECTION_SUPERSEDE_STEP_NAME,
            REVENUE_PROJECTION_SUPERSEDE_STEP_IF,
            "revenue projection supersede producer and validator chain",
            {"name", "if", "run"},
        ),
        (
            POST_RUN_STEP_NAME,
            POST_RUN_STEP_IF,
            "post-run research validation",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME,
            REVENUE_PROJECTION_SUPERSEDE_STEP_IF,
            "revenue projection supersede exact75 closure",
            {"name", "if", "env", "run"},
        ),
        (
            REVENUE_PROJECTION_SUPERSEDE_STAGE_STEP_NAME,
            REVENUE_PROJECTION_SUPERSEDE_STEP_IF,
            "revenue projection supersede exact75 staging",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME,
            REVENUE_PROJECTION_SUPERSEDE_STEP_IF,
            "revenue projection supersede exact75 commit",
            {"name", "if", "env", "run"},
        ),
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF,
            "revenue candidate repair exact2 closure",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF,
            "revenue candidate repair exact2 staging",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF,
            "revenue candidate repair exact2 commit",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_STEP_IF,
            "revenue rebaseline exact17 closure",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_STEP_IF,
            "revenue rebaseline exact17 staging",
            {"name", "if", "run"},
        ),
        (
            REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_STEP_IF,
            "revenue rebaseline exact17 commit",
            {"name", "if", "run"},
        ),
        (
            PUBLISH_STEP_NAME,
            PUBLISH_STEP_IF,
            "research publish",
            {"name", "if", "env", "run"},
        ),
    )
    critical_steps_by_name: dict[str, dict[object, object]] = {}
    for step_name, expected_if, label, expected_keys in critical_contracts:
        matching = [
            step for step in semantic_steps if step.get("name") == step_name
        ]
        if len(matching) != 1:
            errors.append(
                f"{label} step must appear exactly once with its named runtime contract: "
                f"observed={len(matching)}"
            )
            continue
        step = matching[0]
        critical_steps_by_name[step_name] = step
        if set(step) != expected_keys:
            errors.append(
                f"{label} step semantic metadata keys drifted: "
                f"expected={sorted(expected_keys)} actual={sorted(map(str, step))}"
            )
        if expected_if is None:
            if "if" in step:
                errors.append(
                    f"{label} step must not define an if condition: actual={step['if']!r}"
                )
        elif step.get("if") != expected_if:
            errors.append(
                f"{label} step must retain its exact fail-closed if condition: "
                f"actual={step.get('if')!r}"
            )
        if "shell" in step and "shell" not in expected_keys:
            errors.append(
                f"{label} step must not override the GitHub Actions fail-closed shell"
            )
        if "continue-on-error" in step:
            errors.append(
                f"{label} step must not define continue-on-error: "
                f"actual={step['continue-on-error']!r}"
            )

    for step_name, expected_digest in BOOTSTRAP_STEP_MAPPING_SHA256.items():
        step = critical_steps_by_name.get(step_name)
        if step is not None and _semantic_mapping_sha256(step) != expected_digest:
            errors.append(
                "research rebaseline bootstrap step must retain its exact semantic "
                f"metadata and body: step={step_name!r}"
            )

    checkout_step = critical_steps_by_name.get(CHECKOUT_STEP_NAME)
    checkout_with = checkout_step.get("with") if checkout_step is not None else None
    if not isinstance(checkout_with, dict) or (
        checkout_with.get("fetch-depth") != CHECKOUT_FETCH_DEPTH
    ):
        errors.append(
            "repository checkout must retain fetch-depth 2 so the authorized repair "
            "parent and pinned baseline blobs are available"
        )

    observed_bootstrap_names = tuple(
        step.get("name") for step in semantic_steps[: len(BOOTSTRAP_STEP_NAMES)]
    )
    if observed_bootstrap_names != BOOTSTRAP_STEP_NAMES:
        errors.append(
            "research rebaseline bootstrap steps must occupy the exact leading order: "
            f"actual={observed_bootstrap_names}"
        )

    sync_step = critical_steps_by_name.get(SYNC_TARGET_BRANCH_STEP_NAME)
    if sync_step is not None and (
        _semantic_step_run_body(sync_step) != SYNC_TARGET_BRANCH_COMMAND
        or _semantic_step_run_sha256(sync_step) != SYNC_TARGET_BRANCH_RUN_SHA256
    ):
        errors.append(
            "target branch synchronization must retain its exact single-command "
            "fail-closed fast-forward contract"
        )

    install_step = critical_steps_by_name.get(PY_YAML_INSTALL_STEP_NAME)
    if install_step is not None and (
        _semantic_step_run_body(install_step) != PY_YAML_INSTALL_COMMAND
        or _semantic_step_run_sha256(install_step) != PY_YAML_INSTALL_RUN_SHA256
    ):
        errors.append(
            "pinned PyYAML install must retain its exact single-command parser bootstrap"
        )

    preflight_step = critical_steps_by_name.get(RESEARCH_PREFLIGHT_STEP_NAME)
    if preflight_step is not None and (
        _semantic_step_run_sha256(preflight_step) != RESEARCH_PREFLIGHT_RUN_SHA256
    ):
        errors.append(
            "research preflight run body must retain its exact fail-closed dispatch guards"
        )
    if preflight_step is not None and (
        _semantic_mapping_sha256(preflight_step) != RESEARCH_PREFLIGHT_STEP_SHA256
    ):
        errors.append(
            "research preflight step must retain its exact env and run contract"
        )
    if preflight_step is not None:
        preflight_body = _semantic_step_run_body(preflight_step) or ""
        supersede_code_paths = _shell_array_values(
            preflight_body,
            "REVENUE_SUPERSEDE_CODE_PATHS",
        )
        if supersede_code_paths != REVENUE_PROJECTION_SUPERSEDE_CODE_PATHS:
            errors.append(
                "revenue projection supersede preflight must bind the exact44 literal "
                f"code paths: actual={list(supersede_code_paths)}"
            )
        required_code_identity_snippets = (
            f'REVENUE_SUPERSEDE_CODE_ROOT_SHA="{REVENUE_PROJECTION_SUPERSEDE_CODE_ROOT_SHA}"',
            'REVENUE_SUPERSEDE_SHALLOW_STATE="$(git --no-replace-objects rev-parse --is-shallow-repository)"',
            'git --no-replace-objects fetch --no-tags --unshallow origin "$TARGET_BRANCH"',
            'read -r -a REVENUE_SUPERSEDE_PARENT_FIELDS <<< "$(git --no-replace-objects rev-list --parents -n 1 "$REVENUE_SUPERSEDE_EXPECTED_HEAD_SHA")"',
            '"${REVENUE_SUPERSEDE_PARENT_FIELDS[1]}" != "$REVENUE_SUPERSEDE_EXPECTED_BASE_SHA"',
            "code head must have expected_base_sha as its exact sole direct parent.",
            'git --no-replace-objects rev-parse "$REVENUE_SUPERSEDE_CODE_ROOT_SHA^{commit}"',
            'git --no-replace-objects merge-base --is-ancestor "$REVENUE_SUPERSEDE_CODE_ROOT_SHA" "$REVENUE_SUPERSEDE_EXPECTED_HEAD_SHA"',
            "git --no-replace-objects diff --name-only --no-renames "
            '"$REVENUE_SUPERSEDE_CODE_ROOT_SHA" '
            '"$REVENUE_SUPERSEDE_EXPECTED_HEAD_SHA"',
            "Revenue source snapshot projection supersede cumulative code changed-path "
            "exact44 allowlist mismatch.",
            "git --no-replace-objects diff --name-status --no-renames "
            '"$REVENUE_SUPERSEDE_CODE_ROOT_SHA" '
            '"$REVENUE_SUPERSEDE_EXPECTED_HEAD_SHA"',
            "Revenue source snapshot projection supersede code commit status count "
            "mismatch.",
            "$'M\\t'\"${REVENUE_SUPERSEDE_CODE_PATHS[$index]}\"",
            "Revenue source snapshot projection supersede code commit requires exact "
            "modified-only status",
        )
        missing_code_identity = [
            snippet
            for snippet in required_code_identity_snippets
            if snippet not in preflight_body
        ]
        if missing_code_identity:
            errors.append(
                "revenue projection supersede preflight code-commit identity closure "
                f"is incomplete: missing={missing_code_identity}"
            )
    sync_install_preflight_steps = (sync_step, install_step, preflight_step)
    if all(step is not None for step in sync_install_preflight_steps):
        sync_install_preflight_indices = [
            next(
                index
                for index, candidate in enumerate(semantic_steps)
                if candidate is step
            )
            for step in sync_install_preflight_steps
        ]
        if sync_install_preflight_indices != list(
            range(
                sync_install_preflight_indices[0],
                sync_install_preflight_indices[0]
                + len(sync_install_preflight_indices),
            )
        ):
            errors.append(
                "target branch synchronization, pinned PyYAML parser install, and "
                "self-validating research preflight must be consecutive in exact order"
            )

    protected_step_names = [REVENUE_PROJECTION_REBASELINE_PRECHECK_STEP_NAME]
    protected_step_names.extend(
        step_name for step_name, _command in REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS
    )
    protected_indices: list[int] = []
    for step_name in protected_step_names:
        step = critical_steps_by_name.get(step_name)
        if step is not None:
            protected_indices.append(
                next(index for index, candidate in enumerate(semantic_steps) if candidate is step)
            )
    if len(protected_indices) == len(protected_step_names):
        if protected_indices != list(
            range(protected_indices[0], protected_indices[0] + len(protected_indices))
        ):
            errors.append(
                "revenue rebaseline producer, validators, audit, and exact17 identity "
                "preconditions must be contiguous and retain their exact order"
            )

    for step_name, command in REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS:
        step = critical_steps_by_name.get(step_name)
        if step is not None and _semantic_step_run_body(step) != command:
            errors.append(
                f"{step_name} must be an unconditional single-command fail-closed step: "
                f"expected={command!r} actual={_semantic_step_run_body(step)!r}"
            )

    repair_command_step_names = [
        step_name
        for step_name, _command in REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND_STEPS
    ]
    repair_command_indices = [
        next(index for index, candidate in enumerate(semantic_steps) if candidate is step)
        for step_name in repair_command_step_names
        if (step := critical_steps_by_name.get(step_name)) is not None
    ]
    if len(repair_command_indices) == len(repair_command_step_names):
        if repair_command_indices != list(
            range(repair_command_indices[0], repair_command_indices[0] + len(repair_command_indices))
        ):
            errors.append(
                "revenue candidate repair normalize and validator steps must be "
                "contiguous and retain their exact order"
            )
    for step_name, command in REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND_STEPS:
        step = critical_steps_by_name.get(step_name)
        if step is not None and _semantic_step_run_body(step) != command:
            errors.append(
                f"{step_name} must be an unconditional single-command fail-closed step: "
                f"expected={command!r} actual={_semantic_step_run_body(step)!r}"
            )

    supersede_step = critical_steps_by_name.get(REVENUE_PROJECTION_SUPERSEDE_STEP_NAME)
    if supersede_step is not None and (
        _semantic_step_run_body(supersede_step)
        != REVENUE_PROJECTION_SUPERSEDE_RUN_BODY
    ):
        errors.append(
            "revenue projection supersede producer and validator chain must retain its "
            "exact fail-closed order without forward holdout or promotion preparation"
        )

    for step_name, expected_digest, label in (
        (
            REVENUE_PROJECTION_REBASELINE_PRECHECK_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_PRECHECK_RUN_SHA256,
            "immutable v1 precheck",
        ),
        (
            REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_CLOSURE_RUN_SHA256,
            "exact17 validated identity closure",
        ),
        (
            REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
            REVENUE_PROJECTION_REBASELINE_STAGE_RUN_SHA256,
            "exact17 working and index identity staging",
        ),
    ):
        step = critical_steps_by_name.get(step_name)
        if step is not None and _semantic_step_run_sha256(step) != expected_digest:
            errors.append(
                f"revenue rebaseline {label} run body drifted from its exact fail-closed contract"
            )

    post_run_step = critical_steps_by_name.get(POST_RUN_STEP_NAME)
    if post_run_step is not None and (
        _semantic_step_run_sha256(post_run_step) != POST_RUN_RUN_SHA256
    ):
        errors.append(
            "post-run research validation run body must retain its exact read-only "
            "validator sequence"
        )

    rebaseline_commit_step = critical_steps_by_name.get(
        REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME
    )
    if rebaseline_commit_step is not None and (
        _semantic_step_run_sha256(rebaseline_commit_step)
        != REVENUE_PROJECTION_REBASELINE_COMMIT_RUN_SHA256
    ):
        errors.append(
            "revenue rebaseline dedicated commit run body drifted from its exact "
            "fail-closed contract"
        )

    for step_name, expected_digest, label in (
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_RUN_SHA256,
            "exact2 validated identity closure",
        ),
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_RUN_SHA256,
            "exact2 working and index identity staging",
        ),
        (
            REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
            REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_RUN_SHA256,
            "exact2 dedicated commit",
        ),
    ):
        step = critical_steps_by_name.get(step_name)
        if step is not None and _semantic_step_run_sha256(step) != expected_digest:
            errors.append(
                f"revenue candidate repair {label} run body drifted from its exact "
                "fail-closed contract"
            )

    closure_chain_names = (
        POST_RUN_STEP_NAME,
        REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME,
        REVENUE_PROJECTION_SUPERSEDE_STAGE_STEP_NAME,
        REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
        REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
        REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        PUBLISH_STEP_NAME,
    )
    closure_chain_indices: list[int] = []
    for step_name in closure_chain_names:
        step = critical_steps_by_name.get(step_name)
        if step is not None:
            closure_chain_indices.append(
                next(index for index, candidate in enumerate(semantic_steps) if candidate is step)
            )
    if len(closure_chain_indices) == len(closure_chain_names):
        if closure_chain_indices != list(
            range(
                closure_chain_indices[0],
                closure_chain_indices[0] + len(closure_chain_indices),
            )
        ):
            errors.append(
                "post-run validators, supersede exact75 closure chain, repair exact2 "
                "closure chain, rebaseline exact17 closure chain, and mode-skipped "
                "generic publish must be consecutive in exact order"
            )
    return errors


def validate_publish_block(text: str, blocks: list[str]) -> list[str]:
    errors: list[str] = []
    shell_lines = [line.strip() for line in text.splitlines()]
    commit_lines = [
        line
        for line in shell_lines
        if line.startswith(("git commit ", "git --no-replace-objects commit "))
    ]
    push_lines = [
        line
        for line in shell_lines
        if line.startswith(("git push ", "git --no-replace-objects push "))
    ]
    observed_publish_blocks = [
        block
        for block in blocks
        if any(
            line.strip().startswith(
                (
                    "git commit ",
                    "git push ",
                    "git --no-replace-objects commit ",
                    "git --no-replace-objects push ",
                )
            )
            or "ci_push_with_retry.sh" in line
            for line in block.splitlines()
        )
    ]
    generic_blocks = _named_step_blocks(blocks, PUBLISH_STEP_NAME)
    rebaseline_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
    )
    repair_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
    )
    supersede_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME,
    )
    expected_publish_blocks = [
        *supersede_blocks,
        *repair_blocks,
        *rebaseline_blocks,
        *generic_blocks,
    ]
    if (
        len(generic_blocks) != 1
        or len(rebaseline_blocks) != 1
        or len(repair_blocks) != 1
        or len(supersede_blocks) != 1
        or len(observed_publish_blocks) != 4
        or {id(block) for block in observed_publish_blocks}
        != {id(block) for block in expected_publish_blocks}
    ):
        errors.append(
            "research workflow must contain exactly one generic, one supersede, one "
            "candidate repair, and one rebaseline commit/push block: "
            f"observed={len(observed_publish_blocks)}"
        )

    if commit_lines != [
        REVENUE_SUPERSEDE_COMMIT,
        REVENUE_CANDIDATE_REPAIR_COMMIT,
        REVENUE_REBASELINE_COMMIT,
        PUBLISH_COMMIT,
    ]:
        errors.append(
            "research workflow commit commands must be exact supersede, candidate "
            f"repair, rebaseline, then generic commits: observed={commit_lines}"
        )

    if push_lines != [
        REVENUE_SUPERSEDE_PUSH,
        PUBLISH_PUSH,
        PUBLISH_PUSH,
        PUBLISH_PUSH,
    ]:
        errors.append(
            "research workflow must contain exactly four direct fail-closed pushes: "
            f"observed={push_lines}"
        )

    if "ci_push_with_retry.sh" in text:
        errors.append("research workflow must not retry or rebase after validation")

    if len(generic_blocks) == 1:
        generic_block = _normalized_shell_block(generic_blocks[0])
        if PUBLISH_FAIL_CLOSED_SHELL not in generic_block:
            errors.append("research workflow publish block missing fail-closed shell mode")
        if "set +e" in generic_block:
            errors.append("research workflow publish block must not mask shell failure")
        if PUBLISH_NO_CHANGE_GUARD not in generic_block:
            errors.append("research workflow publish block missing staged no-change exit guard")
        else:
            shell_position = generic_block.find(PUBLISH_FAIL_CLOSED_SHELL)
            guard_position = generic_block.index(PUBLISH_NO_CHANGE_GUARD)
            commit_position = generic_block.find(PUBLISH_COMMIT)
            push_position = generic_block.find(PUBLISH_PUSH)
            if not (shell_position < guard_position < commit_position < push_position):
                errors.append(
                    "research workflow publish order must be fail-closed shell, staged guard, "
                    "commit, then direct push"
                )
        for line in generic_block.splitlines():
            if FORBIDDEN_PUBLISH_REWRITE.match(line):
                errors.append(
                    "research workflow publish block must not rewrite or resynchronize the target branch: "
                    f"{line}"
                )

    if len(rebaseline_blocks) == 1:
        rebaseline_block = _normalized_shell_block(rebaseline_blocks[0])
        if PUBLISH_FAIL_CLOSED_SHELL not in rebaseline_block:
            errors.append(
                "revenue rebaseline dedicated commit block missing fail-closed shell mode"
            )
        if "set +e" in rebaseline_block:
            errors.append(
                "revenue rebaseline dedicated commit block must not mask shell failure"
            )
        commit_position = rebaseline_block.find(REVENUE_REBASELINE_COMMIT)
        push_position = rebaseline_block.find(PUBLISH_PUSH)
        if not (0 <= commit_position < push_position):
            errors.append(
                "revenue rebaseline dedicated publish order must be exact commit then "
                "direct push"
            )
        for line in rebaseline_block.splitlines():
            if FORBIDDEN_PUBLISH_REWRITE.match(line):
                errors.append(
                    "revenue rebaseline dedicated commit block must not rewrite or "
                    f"resynchronize the target branch: {line}"
                )

    if len(repair_blocks) == 1:
        repair_block = _normalized_shell_block(repair_blocks[0])
        if PUBLISH_FAIL_CLOSED_SHELL not in repair_block:
            errors.append(
                "revenue candidate repair dedicated commit block missing fail-closed shell mode"
            )
        if "set +e" in repair_block:
            errors.append(
                "revenue candidate repair dedicated commit block must not mask shell failure"
            )
        commit_position = repair_block.find(REVENUE_CANDIDATE_REPAIR_COMMIT)
        push_position = repair_block.find(PUBLISH_PUSH)
        if not (0 <= commit_position < push_position):
            errors.append(
                "revenue candidate repair dedicated publish order must be exact commit "
                "then direct push"
            )
        for line in repair_block.splitlines():
            if FORBIDDEN_PUBLISH_REWRITE.match(line):
                errors.append(
                    "revenue candidate repair dedicated commit block must not rewrite "
                    f"or resynchronize the target branch: {line}"
                )

    if len(supersede_blocks) == 1:
        supersede_block = _normalized_shell_block(supersede_blocks[0])
        if PUBLISH_FAIL_CLOSED_SHELL not in supersede_block:
            errors.append(
                "revenue projection supersede dedicated commit block missing fail-closed shell mode"
            )
        if "set +e" in supersede_block:
            errors.append(
                "revenue projection supersede dedicated commit block must not mask shell failure"
            )
        commit_position = supersede_block.find(REVENUE_SUPERSEDE_COMMIT)
        push_position = supersede_block.find(REVENUE_SUPERSEDE_PUSH)
        if not (0 <= commit_position < push_position):
            errors.append(
                "revenue projection supersede dedicated publish order must be exact "
                "commit then direct deploy-key push"
            )

    return errors


def validate_pr_workflow_text(text: str, rows: list[WorkflowEntrypoint]) -> list[str]:
    errors: list[str] = []
    if not rows:
        errors.append("daily model PR validation requires registered model namespaces")
    trigger = text.split("\njobs:", 1)[0]
    lines = trigger.splitlines()
    try:
        pull_request_index = lines.index("  pull_request:")
    except ValueError:
        errors.append("daily model PR validation must trigger on every pull request")
    else:
        nested = []
        for line in lines[pull_request_index + 1 :]:
            if not line.strip():
                continue
            if len(line) - len(line.lstrip()) <= 2:
                break
            nested.append(line.strip())
        if nested:
            errors.append(
                "daily model PR validation pull_request trigger must remain unfiltered"
            )
    for literal in (
        "  workflow_dispatch:",
        "  scope:",
        "python scripts/detect_daily_model_pr_validation_scope.py",
        "  daily-model-maintenance-pr-validation:",
    ):
        if literal not in text:
            errors.append(f"daily model PR validation missing scope contract: {literal}")
    for row in rows:
        for path in (
            row.producer,
            f"tests/test_{row.model_id}_scope_probe.py",
        ):
            try:
                domains = pr_scope.domains_for_path(path)
            except pr_scope.ScopeDetectionError as exc:
                errors.append(
                    f"registered model namespace is not routed by PR scope: {path}: {exc}"
                )
                continue
            research_domains = set(domains) - {pr_scope.REPO_CURRENT_CONTRACTS}
            if (
                pr_scope.REPO_CURRENT_CONTRACTS not in domains
                or not research_domains
            ):
                errors.append(
                    f"registered model namespace is not routed to core and research: {path}"
                )
    return errors


def validate_workflow_text(
    text: str,
    rows: list[WorkflowEntrypoint],
    model_owned_producers: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    defaults = workflow_input_defaults(text)
    input_types = workflow_input_types(text)
    blocks = workflow_step_blocks(text)
    errors.extend(validate_unmasked_step_contracts(text, blocks))
    errors.extend(validate_publish_block(text, blocks))
    stripped_lines = [line.strip() for line in text.splitlines()]
    any_selected_line = next(
        (line for line in text.splitlines() if "ANY_RESEARCH_SELECTED:" in line),
        "",
    )
    model_selected_line = next(
        (line for line in text.splitlines() if "MODEL_RESEARCH_SELECTED:" in line),
        "",
    )

    if "run_model_parameter_research" in text:
        errors.append("legacy cross-model workflow input is forbidden: run_model_parameter_research")
    if 'git pull --rebase --autostash origin "$TARGET_BRANCH" || true' in text:
        errors.append("research workflow must not pull or ignore sync failure after producers run")
    pre_run_sync = 'git pull --ff-only origin "$TARGET_BRANCH"'
    if pre_run_sync not in text:
        errors.append("research workflow missing fail-closed pre-run branch synchronization")
    branch_sync_lines = [
        line.strip()
        for line in text.splitlines()
        if FORBIDDEN_PUBLISH_REWRITE.match(line.strip())
    ]
    if branch_sync_lines != [pre_run_sync]:
        errors.append(
            "research workflow must contain exactly one pre-run ff-only synchronization and no "
            f"post-validation branch rewrite: observed={branch_sync_lines}"
        )
    for name, default in sorted(defaults.items()):
        if default != "false":
            errors.append(f"research workflow input must default false: {name}={default}")
    for script in sorted(FORBIDDEN_WORKFLOW_SCRIPTS):
        if f"python {script}" in text:
            errors.append(f"research workflow must not invoke formal or cross-model producer: {script}")
    for snippet in sorted(FORBIDDEN_STAGE_SNIPPETS):
        if snippet in text:
            errors.append(f"research workflow contains forbidden broad/formal stage path: {snippet}")

    if defaults.get(SHARED_DATA_INPUT) != "false":
        errors.append(f"missing opt-in shared objective data input with false default: {SHARED_DATA_INPUT}")
    if f"github.event.inputs.{SHARED_DATA_INPUT} == 'true'" not in any_selected_line:
        errors.append(f"shared objective data input missing from ANY_RESEARCH_SELECTED: {SHARED_DATA_INPUT}")
    shared_blocks = [
        block for block in blocks if all(command in block for command in SHARED_DATA_COMMANDS)
    ]
    if len(shared_blocks) != 1:
        errors.append("shared objective data refresh must appear in exactly one workflow step")
    elif f"github.event.inputs.{SHARED_DATA_INPUT} == 'true'" not in shared_blocks[0]:
        errors.append("shared objective data refresh has wrong workflow input condition")
    for command in SHARED_DATA_STAGE_COMMANDS:
        if command not in text:
            errors.append(f"shared objective data stage allowlist missing from workflow: {command}")

    stage_inputs = (
        REVENUE_FORWARD_HOLDOUT_STAGE_INPUT,
        REVENUE_PROJECTION_CHAIN_STAGE_INPUT,
        REVENUE_PROJECTION_REBASELINE_STAGE_INPUT,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_INPUT,
        REVENUE_PROJECTION_SUPERSEDE_STAGE_INPUT,
    )
    for stage_input in stage_inputs:
        if defaults.get(stage_input) != "false":
            errors.append(
                "missing opt-in revenue stage input with false default: "
                f"{stage_input}"
            )
        if any(row.workflow_input == stage_input for row in rows):
            errors.append(
                "revenue stage mode must not be registered as a second producer "
                f"entrypoint: {stage_input}"
            )
        stage_input_condition = f"github.event.inputs.{stage_input} == 'true'"
        if (
            stage_input_condition in any_selected_line
            or stage_input_condition in model_selected_line
        ):
            errors.append(
                "revenue stage mode must require the primary revenue workflow input "
                f"instead of selecting research independently: {stage_input}"
            )
    for stage_input in (
        REVENUE_PROJECTION_REBASELINE_STAGE_INPUT,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_INPUT,
        REVENUE_PROJECTION_SUPERSEDE_STAGE_INPUT,
    ):
        if input_types.get(stage_input) != "boolean":
            errors.append(
                "revenue source projection protected stage input must use "
                f"workflow_dispatch type boolean: {stage_input}"
            )

    holdout_requires_primary = (
        'if [[ "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then'
    )
    mutually_exclusive_modes = (
        'if [[ "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" && '
        '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" ]]; then'
    )
    rebaseline_requires_primary = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then'
    )
    rebaseline_exclusive_modes = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
        '( "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" ) ]]; then'
    )
    rebaseline_forbids_other_research = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
        '"$REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED" == "true" ]]; then'
    )
    rebaseline_requires_branch = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
        '( "$REVENUE_REBASELINE_REF_TYPE" != "branch" || '
        '"$TARGET_BRANCH" == "main" ) ]]; then'
    )
    repair_requires_primary = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then'
    )
    repair_exclusive_modes = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
        '( "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" ) ]]; then'
    )
    repair_forbids_other_research = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
        '"$REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED" == "true" ]]; then'
    )
    repair_requires_branch = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
        '( "$REVENUE_REBASELINE_REF_TYPE" != "branch" || '
        '"$TARGET_BRANCH" == "main" ) ]]; then'
    )
    supersede_requires_primary = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then'
    )
    supersede_exclusive_modes = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && '
        '( "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" || '
        '"$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" ) ]]; then'
    )
    supersede_forbids_other_research = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && '
        '"$REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED" == "true" ]]; then'
    )
    supersede_requires_dispatch_branch = (
        'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && '
        '( "$GITHUB_EVENT_NAME" != "workflow_dispatch" || '
        '"$REVENUE_REBASELINE_REF_TYPE" != "branch" || '
        '"$TARGET_BRANCH" == "main" ) ]]; then'
    )
    if holdout_requires_primary not in text:
        errors.append(
            "revenue forward holdout stage must fail closed unless the primary revenue "
            "workflow input is selected"
        )
    if mutually_exclusive_modes not in text:
        errors.append(
            "revenue forward holdout and source projection chain stage modes must be "
            "mutually exclusive"
        )
    if rebaseline_requires_primary not in text:
        errors.append(
            "revenue source projection rebaseline stage must fail closed unless the "
            "primary revenue workflow input is selected"
        )
    if rebaseline_exclusive_modes not in text:
        errors.append(
            "revenue source projection rebaseline stage must be mutually exclusive "
            "with forward holdout and projection chain modes"
        )
    if rebaseline_forbids_other_research not in text:
        errors.append(
            "revenue source projection rebaseline stage must forbid every other "
            "research input"
        )
    if rebaseline_requires_branch not in text:
        errors.append(
            "revenue source projection rebaseline stage must require a non-main "
            "branch ref"
        )
    if repair_requires_primary not in text:
        errors.append(
            "revenue source projection candidate repair must fail closed unless the "
            "primary revenue workflow input is selected"
        )
    if repair_exclusive_modes not in text:
        errors.append(
            "revenue source projection candidate repair must be mutually exclusive "
            "with forward holdout, projection chain, and rebaseline modes"
        )
    if repair_forbids_other_research not in text:
        errors.append(
            "revenue source projection candidate repair must forbid every other "
            "research input"
        )
    if repair_requires_branch not in text:
        errors.append(
            "revenue source projection candidate repair must require a non-main "
            "branch ref"
        )
    for snippet, message in (
        (
            supersede_requires_primary,
            "revenue projection supersede must require the primary revenue input",
        ),
        (
            supersede_exclusive_modes,
            "revenue projection supersede must be mutually exclusive with every other revenue stage mode",
        ),
        (
            supersede_forbids_other_research,
            "revenue projection supersede must forbid every other research input",
        ),
        (
            supersede_requires_dispatch_branch,
            "revenue projection supersede must require workflow_dispatch on a non-main branch",
        ),
        (
            'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && "$GITHUB_RUN_ATTEMPT" != "1" ]]; then',
            "revenue projection supersede must reject workflow retry attempts",
        ),
        (
            f'if [[ "$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" && "$REVENUE_SUPERSEDE_CONFIRMATION" != "{REVENUE_PROJECTION_SUPERSEDE_CONFIRMATION}" ]]; then',
            "revenue projection supersede must require its exact confirmation token",
        ),
    ):
        if snippet not in text:
            errors.append(message)
    for identity_input in REVENUE_PROJECTION_SUPERSEDE_IDENTITY_INPUTS:
        if input_types.get(identity_input) != "string":
            errors.append(
                "revenue projection supersede identity input must use workflow_dispatch "
                f"type string: {identity_input}"
            )
    if REVENUE_PROJECTION_CANDIDATE_REPAIR_RUN_ATTEMPT_GUARD not in text:
        errors.append(
            "revenue source projection candidate repair must reject workflow retry "
            "attempts"
        )
    if REVENUE_PROJECTION_CANDIDATE_REPAIR_DISPATCH_HEAD_GUARD not in text:
        errors.append(
            "revenue source projection candidate repair must require synchronized "
            "HEAD to equal the dispatch SHA"
        )
    if REVENUE_PROJECTION_CANDIDATE_REPAIR_CODE_PARENT_GUARD not in text:
        errors.append(
            "revenue source projection candidate repair must require the single "
            "authorized code commit above its pinned baseline"
        )
    other_research_line = next(
        (
            line
            for line in text.splitlines()
            if "REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED:" in line
        ),
        "",
    )
    observed_companion_inputs = tuple(
        re.findall(r"github\.event\.inputs\.([A-Za-z0-9_]+) == 'true'", other_research_line)
    )
    if observed_companion_inputs != REVENUE_PROJECTION_REBASELINE_FORBIDDEN_COMPANION_INPUTS:
        errors.append(
            "revenue source projection rebaseline companion-input guard drift: "
            f"actual={list(observed_companion_inputs)}"
        )

    revenue_blocks = [
        block
        for block in blocks
        if REVENUE_PROJECTION_CHAIN_BUILD_COMMAND in block
        or REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND in block
    ]
    if len(revenue_blocks) != 1:
        errors.append(
            "revenue holdout, projection-chain, and full commands must appear together "
            "in exactly one non-rebaseline workflow step"
        )
    else:
        revenue_block = revenue_blocks[0]
        revenue_lines = [line.strip() for line in revenue_block.splitlines()]
        holdout_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_FORWARD_HOLDOUT_STAGE_INPUT}'
            ' }}" == "true" ]]; then'
        )
        projection_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_PROJECTION_CHAIN_STAGE_INPUT}'
            ' }}" == "true" ]]; then'
        )
        try:
            holdout_index = revenue_lines.index(holdout_if)
            holdout_fi_index = revenue_lines.index("fi", holdout_index + 1)
            projection_index = revenue_lines.index(
                projection_if, holdout_fi_index + 1
            )
            else_index = revenue_lines.index("else", projection_index + 1)
            fi_index = revenue_lines.index("fi", else_index + 1)
        except ValueError:
            errors.append(
                "revenue holdout and source projection stage modes are missing their "
                "guarded stage/full branches"
            )
        else:
            holdout_python = {
                line for line in revenue_lines[holdout_index + 1 : holdout_fi_index]
                if line.startswith("python ")
            }
            projection_python = {
                line for line in revenue_lines[projection_index + 1 : else_index]
                if line.startswith("python ")
            }
            full_python = {
                line for line in revenue_lines[else_index + 1 : fi_index]
                if line.startswith("python ")
            }
            expected_holdout_python = {
                REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND,
            }
            if holdout_python != expected_holdout_python:
                errors.append(
                    "revenue forward holdout stage mode must contain only its model-owned "
                    "producer stage with persisted independent replay: "
                    f"actual={sorted(holdout_python)}"
                )
            expected_projection_python = {
                REVENUE_PROJECTION_CHAIN_BUILD_COMMAND,
                *REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS,
            }
            if projection_python != expected_projection_python:
                errors.append(
                    "revenue source projection chain stage mode must contain only its "
                    "existing producer stage and cutoff-chain validators: "
                    f"actual={sorted(projection_python)}"
                )
            if REVENUE_FULL_BUILD_COMMAND not in full_python:
                errors.append(
                    "revenue full research branch must retain the existing producer"
                )
            if REVENUE_PROJECTION_CHAIN_BUILD_COMMAND in full_python:
                errors.append(
                    "revenue full research branch must not replace the full producer with "
                    "the source projection chain stage"
                )
            if REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND in full_python:
                errors.append(
                    "revenue full research branch must not replace the full producer with "
                    "the forward holdout stage"
                )
            if REVENUE_PROJECTION_REBASELINE_BUILD_COMMAND in full_python:
                errors.append(
                    "revenue full research branch must not replace the full producer "
                    "with the source projection rebaseline stage"
                )
        revenue_condition = f"github.event.inputs.{REVENUE_WORKFLOW_INPUT} == 'true'"
        if revenue_condition not in revenue_block:
            errors.append(
                "revenue stage modes must remain nested under the "
                "primary revenue workflow input"
            )

    rebaseline_precheck_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_REBASELINE_PRECHECK_STEP_NAME,
    )
    rebaseline_closure_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
    )
    rebaseline_stage_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
    )
    rebaseline_commit_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
    )
    repair_closure_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
    )
    repair_stage_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
    )
    repair_commit_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
    )
    supersede_closure_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME,
    )
    supersede_stage_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_SUPERSEDE_STAGE_STEP_NAME,
    )
    supersede_commit_blocks = _named_step_blocks(
        blocks,
        REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME,
    )
    if len(rebaseline_precheck_blocks) == 1:
        precheck_body = _step_run_body(rebaseline_precheck_blocks[0]) or ""
        for path, expected_bytes, expected_sha256 in (
            REVENUE_PROJECTION_REBASELINE_V1_IDENTITIES
        ):
            for token in (path, expected_bytes, expected_sha256):
                if token not in precheck_body:
                    errors.append(
                        "revenue source projection rebaseline immutable v1 precheck "
                        f"bytes/SHA identity drift: missing={token}"
                    )
    if len(rebaseline_closure_blocks) == 1:
        closure_body = _step_run_body(rebaseline_closure_blocks[0]) or ""
        closure_paths = _shell_array_values(
            closure_body,
            "REVENUE_REBASELINE_ALLOWED_PATHS",
        )
        if closure_paths != REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS:
            errors.append(
                "revenue source projection rebaseline final closure must guard the "
                "exact seventeen changed or untracked artifact paths: "
                f"actual={list(closure_paths)}"
            )
        for path, expected_bytes, expected_sha256 in (
            REVENUE_PROJECTION_REBASELINE_V1_IDENTITIES
        ):
            for token in (path, expected_bytes, expected_sha256):
                if token not in closure_body:
                    errors.append(
                        "revenue source projection rebaseline immutable v1 postcheck "
                        f"bytes/SHA identity drift: missing={token}"
                    )
        for snippet in (
            f'test "$(cat "{POST_RUN_SENTINEL}")" = "pass"',
            "git status --porcelain=v1 --untracked-files=all",
            '"${#REVENUE_REBASELINE_CHANGED_PATHS[@]}" -ne "${#REVENUE_REBASELINE_ALLOWED_PATHS[@]}"',
            "Revenue source snapshot projection rebaseline worktree-path allowlist mismatch",
            f'REVENUE_REBASELINE_IDENTITY_FILE="{REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE}"',
            "validated_bytes=",
            "validated_sha256=",
            '>> "$REVENUE_REBASELINE_IDENTITY_FILE"',
        ):
            if snippet not in closure_body:
                errors.append(
                    "revenue source projection rebaseline exact17 validated identity "
                    f"closure is incomplete: {snippet}"
                )
    if len(rebaseline_stage_blocks) == 1:
        stage_body = _step_run_body(rebaseline_stage_blocks[0]) or ""
        stage_paths = _shell_array_values(
            stage_body,
            "REVENUE_REBASELINE_ALLOWED_PATHS",
        )
        if stage_paths != REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS:
            errors.append(
                "revenue source projection rebaseline staging step must contain only "
                "its exact seventeen artifact paths: "
                f"actual={list(stage_paths)}"
            )
        identity_snippets = (
            f'REVENUE_REBASELINE_IDENTITY_FILE="{REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE}"',
            "mapfile -t REVENUE_REBASELINE_VALIDATED_IDENTITIES",
            'working_bytes="$(wc -c < "$path"',
            'working_sha256="$(sha256sum "$path"',
            "Revenue rebaseline artifact drifted after validation",
            "git status --porcelain=v1 --untracked-files=all",
            "Revenue source snapshot projection rebaseline pre-stage worktree-path allowlist mismatch",
            REVENUE_PROJECTION_REBASELINE_LITERAL_GIT_ADD,
            "mapfile -t REVENUE_REBASELINE_STAGED_PATHS < <(git diff --cached --name-only)",
            "Revenue source snapshot projection rebaseline staged-path allowlist mismatch",
            'staged_bytes="$(git cat-file -s ":$path")"',
            'staged_sha256="$(git show ":$path" | sha256sum',
            "Revenue rebaseline staged artifact identity mismatch",
        )
        missing_identity_snippets = [
            snippet for snippet in identity_snippets if snippet not in stage_body
        ]
        if missing_identity_snippets:
            errors.append(
                "revenue source projection rebaseline staging step lacks fail-closed "
                "working/index identity closure: "
                f"missing={missing_identity_snippets}"
            )
        if 'git add -- "${REVENUE_REBASELINE_ALLOWED_PATHS[@]}"' in stage_body:
            errors.append(
                "revenue source projection rebaseline staging must use seventeen "
                "literal pathspecs, never an array-expanded git add"
            )
        observed_positions = [stage_body.find(snippet) for snippet in identity_snippets]
        if not missing_identity_snippets and observed_positions != sorted(observed_positions):
            errors.append(
                "revenue source projection rebaseline staging must compare validated "
                "working identities before exact staging and index identities after staging"
            )
    if len(rebaseline_commit_blocks) == 1:
        dedicated_commit_body = _step_run_body(rebaseline_commit_blocks[0]) or ""
        dedicated_commit_paths = _shell_array_values(
            dedicated_commit_body,
            "REVENUE_REBASELINE_ALLOWED_PATHS",
        )
        if dedicated_commit_paths != REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS:
            errors.append(
                "revenue source projection rebaseline dedicated commit must contain "
                "only its exact seventeen artifact paths: "
                f"actual={list(dedicated_commit_paths)}"
            )
        dedicated_commit_snippets = (
            PUBLISH_FAIL_CLOSED_SHELL,
            f'REVENUE_REBASELINE_IDENTITY_FILE="{REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE}"',
            "mapfile -t REVENUE_REBASELINE_VALIDATED_IDENTITIES",
            "mapfile -t REVENUE_REBASELINE_STAGED_PATHS < <(git diff --cached --name-only)",
            "Revenue rebaseline pre-commit staged-path allowlist mismatch",
            "if ! git diff --quiet; then",
            "git ls-files --others --exclude-standard",
            'REVENUE_REBASELINE_PRE_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'staged_bytes="$(git cat-file -s ":$path")"',
            'staged_sha256="$(git show ":$path" | sha256sum',
            "Revenue rebaseline pre-commit staged artifact identity mismatch",
            REVENUE_REBASELINE_COMMIT,
            'REVENUE_REBASELINE_POST_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'git rev-parse "$REVENUE_REBASELINE_POST_COMMIT_HEAD^"',
            "git diff --name-only --no-renames",
            "Revenue rebaseline committed-path allowlist mismatch",
            'committed_bytes="$(git cat-file -s "$REVENUE_REBASELINE_POST_COMMIT_HEAD:$path")"',
            'committed_sha256="$(git show "$REVENUE_REBASELINE_POST_COMMIT_HEAD:$path"',
            "Revenue rebaseline committed artifact identity mismatch",
            "git status --porcelain=v1 --untracked-files=all",
            "Revenue rebaseline worktree or index is not clean after commit",
            PUBLISH_PUSH,
        )
        missing_commit_snippets = [
            snippet
            for snippet in dedicated_commit_snippets
            if snippet not in dedicated_commit_body
        ]
        if missing_commit_snippets:
            errors.append(
                "revenue source projection rebaseline dedicated commit lacks exact17 "
                "staged/index identity closure: "
                f"missing={missing_commit_snippets}"
            )
        dedicated_commit_lines = [
            line.strip()
            for line in dedicated_commit_body.splitlines()
            if line.strip()
        ]
        if f"done\n{REVENUE_REBASELINE_COMMIT}" not in dedicated_commit_body:
            errors.append(
                "revenue rebaseline dedicated commit must execute exact git commit as "
                "the next side effect after its final pre-commit index identity loop"
            )
        observed_positions = [
            dedicated_commit_body.find(snippet)
            for snippet in dedicated_commit_snippets
        ]
        if not missing_commit_snippets and observed_positions != sorted(observed_positions):
            errors.append(
                "revenue rebaseline dedicated commit identity, commit-object, clean "
                "status, and push guards must retain exact fail-closed order"
            )
        if not dedicated_commit_lines or dedicated_commit_lines[-1] != PUBLISH_PUSH:
            errors.append(
                "revenue rebaseline dedicated direct push must be the final command"
            )
        if any(line.startswith("git add ") for line in dedicated_commit_lines):
            errors.append(
                "revenue rebaseline dedicated commit must not modify or stage after "
                "index identity validation"
            )

    if len(repair_closure_blocks) == 1:
        repair_closure_body = _step_run_body(repair_closure_blocks[0]) or ""
        repair_paths = _shell_array_values(
            repair_closure_body,
            "REVENUE_CANDIDATE_REPAIR_PATHS",
        )
        unchanged_paths = _shell_array_values(
            repair_closure_body,
            "REVENUE_CANDIDATE_REPAIR_UNCHANGED_PATHS",
        )
        if repair_paths != REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS:
            errors.append(
                "revenue candidate repair closure must guard the exact two CSV mirrors: "
                f"actual={list(repair_paths)}"
            )
        if unchanged_paths != REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS:
            errors.append(
                "revenue candidate repair closure must preserve the other exact15 "
                f"rebaseline artifacts: actual={list(unchanged_paths)}"
            )
        repair_closure_snippets = (
            f'test "$(cat "{POST_RUN_SENTINEL}")" = "pass"',
            f'REVENUE_CANDIDATE_REPAIR_BASE_COMMIT="{REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT}"',
            'git merge-base --is-ancestor "$REVENUE_CANDIDATE_REPAIR_BASE_COMMIT" HEAD',
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_BYTES="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES}"',
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_SHA256="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256}"',
            "git status --porcelain=v1 --untracked-files=all",
            "Revenue candidate repair changed-path exact2 allowlist mismatch",
            'base_blob="$(git rev-parse "$REVENUE_CANDIDATE_REPAIR_BASE_COMMIT:$path")"',
            'head_blob="$(git rev-parse "HEAD:$path")"',
            'index_blob="$(git rev-parse ":$path")"',
            'working_blob="$(git hash-object "$path")"',
            "Revenue candidate repair changed a protected exact15 artifact",
            'cmp -s "${REVENUE_CANDIDATE_REPAIR_PATHS[0]}" "${REVENUE_CANDIDATE_REPAIR_PATHS[1]}"',
            f'REVENUE_CANDIDATE_REPAIR_IDENTITY_FILE="{REVENUE_PROJECTION_CANDIDATE_REPAIR_IDENTITY_FILE}"',
            "Revenue candidate repair postimage identity mismatch",
            '>> "$REVENUE_CANDIDATE_REPAIR_IDENTITY_FILE"',
        )
        missing = [
            snippet
            for snippet in repair_closure_snippets
            if snippet not in repair_closure_body
        ]
        if missing:
            errors.append(
                "revenue candidate repair exact2 closure is incomplete: "
                f"missing={missing}"
            )

    if len(repair_stage_blocks) == 1:
        repair_stage_body = _step_run_body(repair_stage_blocks[0]) or ""
        repair_stage_paths = _shell_array_values(
            repair_stage_body,
            "REVENUE_CANDIDATE_REPAIR_PATHS",
        )
        if repair_stage_paths != REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS:
            errors.append(
                "revenue candidate repair staging must contain only its exact two CSV "
                f"paths: actual={list(repair_stage_paths)}"
            )
        repair_stage_snippets = (
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_BYTES="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES}"',
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_SHA256="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256}"',
            f'REVENUE_CANDIDATE_REPAIR_IDENTITY_FILE="{REVENUE_PROJECTION_CANDIDATE_REPAIR_IDENTITY_FILE}"',
            "Revenue candidate repair pre-stage changed-path allowlist mismatch",
            'working_bytes="$(wc -c < "$path"',
            'working_sha256="$(sha256sum "$path"',
            REVENUE_PROJECTION_CANDIDATE_REPAIR_LITERAL_GIT_ADD,
            "mapfile -t REVENUE_CANDIDATE_REPAIR_STAGED_PATHS < <(git diff --cached --name-only)",
            "Revenue candidate repair staged-path exact2 allowlist mismatch",
            "if ! git diff --quiet; then",
            'staged_bytes="$(git cat-file -s ":$path")"',
            'staged_sha256="$(git show ":$path" | sha256sum',
            "Revenue candidate repair staged artifact identity mismatch",
        )
        missing = [
            snippet
            for snippet in repair_stage_snippets
            if snippet not in repair_stage_body
        ]
        if missing:
            errors.append(
                "revenue candidate repair staging lacks exact working/index identity "
                f"closure: missing={missing}"
            )
        if 'git add -- "${REVENUE_CANDIDATE_REPAIR_PATHS[@]}"' in repair_stage_body:
            errors.append(
                "revenue candidate repair staging must use two literal pathspecs, "
                "never an array-expanded git add"
            )

    if len(repair_commit_blocks) == 1:
        repair_commit_body = _step_run_body(repair_commit_blocks[0]) or ""
        repair_commit_paths = _shell_array_values(
            repair_commit_body,
            "REVENUE_CANDIDATE_REPAIR_PATHS",
        )
        repair_commit_unchanged_paths = _shell_array_values(
            repair_commit_body,
            "REVENUE_CANDIDATE_REPAIR_UNCHANGED_PATHS",
        )
        if repair_commit_paths != REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS:
            errors.append(
                "revenue candidate repair commit must contain only its exact two CSV "
                f"paths: actual={list(repair_commit_paths)}"
            )
        if (
            repair_commit_unchanged_paths
            != REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS
        ):
            errors.append(
                "revenue candidate repair commit must preserve the other exact15 "
                f"rebaseline artifacts: actual={list(repair_commit_unchanged_paths)}"
            )
        repair_commit_snippets = (
            PUBLISH_FAIL_CLOSED_SHELL,
            f'REVENUE_CANDIDATE_REPAIR_BASE_COMMIT="{REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT}"',
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_BYTES="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES}"',
            f'REVENUE_CANDIDATE_REPAIR_EXPECTED_SHA256="{REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256}"',
            f'REVENUE_CANDIDATE_REPAIR_IDENTITY_FILE="{REVENUE_PROJECTION_CANDIDATE_REPAIR_IDENTITY_FILE}"',
            "mapfile -t REVENUE_CANDIDATE_REPAIR_STAGED_PATHS < <(git diff --cached --name-only)",
            "Revenue candidate repair pre-commit staged-path allowlist mismatch",
            "if ! git diff --quiet; then",
            "git ls-files --others --exclude-standard",
            'REVENUE_CANDIDATE_REPAIR_PRE_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'staged_bytes="$(git cat-file -s ":$path")"',
            'staged_sha256="$(git show ":$path" | sha256sum',
            "Revenue candidate repair pre-commit staged artifact identity mismatch",
            REVENUE_CANDIDATE_REPAIR_COMMIT,
            'REVENUE_CANDIDATE_REPAIR_POST_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'git rev-parse "$REVENUE_CANDIDATE_REPAIR_POST_COMMIT_HEAD^"',
            "git diff --name-only --no-renames",
            "Revenue candidate repair committed-path exact2 allowlist mismatch",
            'committed_bytes="$(git cat-file -s "$REVENUE_CANDIDATE_REPAIR_POST_COMMIT_HEAD:$path")"',
            'committed_sha256="$(git show "$REVENUE_CANDIDATE_REPAIR_POST_COMMIT_HEAD:$path"',
            "Revenue candidate repair committed artifact identity mismatch",
            'committed_blob="$(git rev-parse "$REVENUE_CANDIDATE_REPAIR_POST_COMMIT_HEAD:$path")"',
            "Revenue candidate repair commit changed a protected exact15 artifact",
            "git status --porcelain=v1 --untracked-files=all",
            "Revenue candidate repair worktree or index is not clean after commit",
            PUBLISH_PUSH,
        )
        missing = [
            snippet
            for snippet in repair_commit_snippets
            if snippet not in repair_commit_body
        ]
        if missing:
            errors.append(
                "revenue candidate repair dedicated commit lacks exact2 staged and "
                f"post-commit identity closure: missing={missing}"
            )
        repair_commit_lines = [
            line.strip()
            for line in repair_commit_body.splitlines()
            if line.strip()
        ]
        if f"done\n{REVENUE_CANDIDATE_REPAIR_COMMIT}" not in repair_commit_body:
            errors.append(
                "revenue candidate repair commit must be the next side effect after "
                "its final pre-commit index identity loop"
            )
        if not repair_commit_lines or repair_commit_lines[-1] != PUBLISH_PUSH:
            errors.append(
                "revenue candidate repair direct push must be the final command"
            )
        if any(line.startswith("git add ") for line in repair_commit_lines):
            errors.append(
                "revenue candidate repair dedicated commit must not modify or stage "
                "after index identity validation"
            )

    supersede_bodies: dict[str, str] = {}
    for label, step_blocks in (
        ("closure", supersede_closure_blocks),
        ("stage", supersede_stage_blocks),
        ("commit", supersede_commit_blocks),
    ):
        if len(step_blocks) == 1:
            supersede_bodies[label] = _step_run_body(step_blocks[0]) or ""

    for label, body in supersede_bodies.items():
        allowed_paths = _shell_array_values(body, "REVENUE_SUPERSEDE_ALLOWED_PATHS")
        if allowed_paths != REVENUE_PROJECTION_SUPERSEDE_ALLOWED_PATHS:
            errors.append(
                "revenue projection supersede "
                f"{label} must bind the exact75 literal artifact paths: "
                f"actual_count={len(allowed_paths)}"
            )
        if re.search(r"\bgit (?!--no-replace-objects\b|ls-remote\b)", body):
            errors.append(
                "revenue projection supersede identity and side-effect Git commands "
                f"must use --no-replace-objects: step={label}"
            )
        if "GITHUB_TOKEN" in body or "ci_push_with_retry.sh" in body:
            errors.append(
                "revenue projection supersede must use only the deploy-key checkout and "
                f"direct push without token fallback or retry: step={label}"
            )

    supersede_closure_body = supersede_bodies.get("closure", "")
    if supersede_closure_body:
        immutable_paths = _shell_array_values(
            supersede_closure_body,
            "REVENUE_SUPERSEDE_IMMUTABLE_PATHS",
        )
        if immutable_paths != REVENUE_PROJECTION_SUPERSEDE_IMMUTABLE_PATHS:
            errors.append(
                "revenue projection supersede closure must preserve immutable exact7 "
                f"candidate artifacts: actual={list(immutable_paths)}"
            )
        required_closure_snippets = (
            f'test "$(cat "{POST_RUN_SENTINEL}")" = "pass"',
            f'REVENUE_SUPERSEDE_TRUSTED_CANDIDATE_COMMIT="{REVENUE_PROJECTION_SUPERSEDE_TRUSTED_CANDIDATE_COMMIT}"',
            'if [[ "$(git --no-replace-objects rev-parse --is-shallow-repository)" == "true" ]]; then',
            'git --no-replace-objects fetch --no-tags --unshallow origin "$TARGET_BRANCH"',
            "git --no-replace-objects merge-base --is-ancestor",
            "Revenue projection supersede mutated an immutable v1/v2/diff artifact",
            "latest manifest is not byte-identical to immutable v2",
            "docs manifest is not byte-identical to immutable v2",
            "latest detail is not byte-identical to immutable v2",
            "Revenue projection supersede changed-path exact75 allowlist mismatch",
            f'REVENUE_SUPERSEDE_IDENTITY_FILE="{REVENUE_PROJECTION_SUPERSEDE_IDENTITY_FILE}"',
            'test "$(wc -l < "$REVENUE_SUPERSEDE_IDENTITY_FILE"',
            '= "75"',
        )
        missing = [
            snippet
            for snippet in required_closure_snippets
            if snippet not in supersede_closure_body
        ]
        if missing:
            errors.append(
                "revenue projection supersede exact75 closure is incomplete: "
                f"missing={missing}"
            )

    supersede_stage_body = supersede_bodies.get("stage", "")
    if supersede_stage_body:
        required_stage_snippets = (
            f'REVENUE_SUPERSEDE_IDENTITY_FILE="{REVENUE_PROJECTION_SUPERSEDE_IDENTITY_FILE}"',
            "Revenue projection supersede pre-stage changed-path exact75 allowlist mismatch",
            "Revenue projection supersede artifact drifted after validation",
            REVENUE_PROJECTION_SUPERSEDE_LITERAL_GIT_ADD,
            "git --no-replace-objects diff --cached --name-only",
            "Revenue projection supersede staged-path exact75 allowlist mismatch",
            "git --no-replace-objects cat-file -s",
            "git --no-replace-objects show",
            "Revenue projection supersede staged artifact identity mismatch",
        )
        missing = [
            snippet
            for snippet in required_stage_snippets
            if snippet not in supersede_stage_body
        ]
        if missing:
            errors.append(
                "revenue projection supersede exact75 literal staging is incomplete: "
                f"missing={missing}"
            )
        if 'git --no-replace-objects add -- "${REVENUE_SUPERSEDE_ALLOWED_PATHS[@]}"' in supersede_stage_body:
            errors.append(
                "revenue projection supersede staging must use exact75 literal pathspecs, "
                "never an array-expanded git add"
            )

    supersede_commit_body = supersede_bodies.get("commit", "")
    if supersede_commit_body:
        immutable_paths = _shell_array_values(
            supersede_commit_body,
            "REVENUE_SUPERSEDE_IMMUTABLE_PATHS",
        )
        if immutable_paths != REVENUE_PROJECTION_SUPERSEDE_IMMUTABLE_PATHS:
            errors.append(
                "revenue projection supersede commit must preserve immutable exact7 "
                f"candidate artifacts: actual={list(immutable_paths)}"
            )
        required_commit_snippets = (
            f'REVENUE_SUPERSEDE_IDENTITY_FILE="{REVENUE_PROJECTION_SUPERSEDE_IDENTITY_FILE}"',
            "Revenue projection supersede pre-commit HEAD moved from expected_head_sha",
            "Revenue projection supersede pre-commit staged-path exact75 allowlist mismatch",
            "Revenue projection supersede pre-commit staged artifact identity mismatch",
            "git ls-remote --exit-code origin",
            "Revenue projection supersede remote branch moved before artifact commit",
            REVENUE_SUPERSEDE_COMMIT,
            "git --no-replace-objects rev-list --parents -n 1",
            "git --no-replace-objects rev-list --count",
            "unique direct child of expected_head_sha",
            "Revenue projection supersede committed-path exact75 allowlist mismatch",
            "Revenue projection supersede committed artifact identity mismatch",
            "artifact commit changed an immutable v1/v2/diff artifact",
            "Revenue projection supersede remote branch moved before the direct push",
            REVENUE_SUPERSEDE_PUSH,
        )
        missing = [
            snippet
            for snippet in required_commit_snippets
            if snippet not in supersede_commit_body
        ]
        if missing:
            errors.append(
                "revenue projection supersede exact75 dedicated commit is incomplete: "
                f"missing={missing}"
            )
        supersede_commit_lines = [
            line.strip()
            for line in supersede_commit_body.splitlines()
            if line.strip()
        ]
        if not supersede_commit_lines or supersede_commit_lines[-1] != REVENUE_SUPERSEDE_PUSH:
            errors.append(
                "revenue projection supersede direct deploy-key push must be the final command"
            )
        if any(
            line.startswith(("git add ", "git --no-replace-objects add "))
            for line in supersede_commit_lines
        ):
            errors.append(
                "revenue projection supersede dedicated commit must not stage after "
                "exact75 index validation"
            )

    if text.count(REVENUE_PROJECTION_SUPERSEDE_IDENTITY_FILE) != 3:
        errors.append(
            "revenue projection supersede identity file must be written once after "
            "validation and read by exact75 staging and dedicated commit"
        )

    for path, expected_count in zip(
        REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS,
        REVENUE_PROJECTION_REBASELINE_EXPECTED_PATH_OCCURRENCES,
        strict=True,
    ):
        if text.count(path) != expected_count:
            errors.append(
                "revenue source projection rebaseline exact17 path occurrence drift: "
                f"path={path} expected={expected_count} actual={text.count(path)}"
            )
    if text.count(REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE) != 3:
        errors.append(
            "revenue source projection rebaseline identity file must be written once "
            "after validation and read by exact17 staging and dedicated commit"
        )
    if text.count(REVENUE_PROJECTION_CANDIDATE_REPAIR_IDENTITY_FILE) != 3:
        errors.append(
            "revenue candidate repair identity file must be written once after "
            "validation and read by exact2 staging and dedicated commit"
        )
    if text.count(POST_RUN_SENTINEL) != 4:
        errors.append(
            "post-run validator sentinel must be written once and consumed once by each "
            "protected supersede/repair/rebaseline identity closure"
        )

    commit_step_name = COMMIT_STEP_MARKER.removeprefix("- name: ")
    commit_blocks = [
        block
        for block in blocks
        if block.splitlines() and block.splitlines()[0].strip() == commit_step_name
    ]
    if len(commit_blocks) != 1:
        errors.append("research artifact commit step must appear exactly once")
    else:
        commit_lines = [line.strip() for line in commit_blocks[0].splitlines()]
        revenue_stage_if = (
            'if [[ "${{ github.event.inputs.'
            f'{REVENUE_WORKFLOW_INPUT}'
            ' }}" == "true" ]]; then'
        )
        holdout_stage_if = (
            'if [[ "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" ]]; then'
        )
        full_stage_elif = (
            'elif [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" != "true" ]]; then'
        )
        try:
            revenue_stage_index = commit_lines.index(revenue_stage_if)
            holdout_stage_index = commit_lines.index(
                holdout_stage_if, revenue_stage_index + 1
            )
            full_stage_index = commit_lines.index(
                full_stage_elif, holdout_stage_index + 1
            )
            stage_fi_index = commit_lines.index("fi", full_stage_index + 1)
        except ValueError:
            errors.append(
                "revenue forward holdout commit staging must be nested under the "
                "primary revenue artifact stage"
            )
        else:
            holdout_stage_commands = {
                line
                for line in commit_lines[
                    holdout_stage_index + 1 : full_stage_index
                ]
                if line.startswith("git add ")
            }
            full_stage_commands = {
                line
                for line in commit_lines[full_stage_index + 1 : stage_fi_index]
                if line.startswith("git add ")
            }
            if holdout_stage_commands != REVENUE_FORWARD_HOLDOUT_STAGE_COMMANDS:
                errors.append(
                    "revenue forward holdout commit stage must contain only its exact "
                    "latest/history/docs artifact prefixes: "
                    f"actual={sorted(holdout_stage_commands)}"
                )
            if full_stage_commands != REVENUE_FULL_STAGE_COMMANDS:
                errors.append(
                    "revenue full research commit stage must retain its existing "
                    "latest/history/docs artifact prefixes: "
                    f"actual={sorted(full_stage_commands)}"
                )

    volume_source = "python scripts/build_volume_breakout_confirmed_operation_backtest.py"
    volume_v2 = "python scripts/build_volume_range_breakout_v2_research.py"
    if volume_source in text and volume_v2 in text and text.index(volume_source) > text.index(volume_v2):
        errors.append("volume breakout source refresh must precede the model-owned v2 producer")

    registry_models = {row.model_id: row.producer for row in rows}
    if registry_models != model_owned_producers:
        errors.append(
            "workflow registry must cover every model_owned_write producer exactly: "
            f"workflow={registry_models}; ownership={model_owned_producers}"
        )

    inputs = [row.workflow_input for row in rows]
    producers = [row.producer for row in rows]
    if len(inputs) != len(set(inputs)):
        errors.append("duplicate workflow_input in model research workflow registry")
    if len(producers) != len(set(producers)):
        errors.append("duplicate producer in model research workflow registry")

    for row in rows:
        if row.workflow_path != ".github/workflows/research_backtest_pipeline.yml":
            errors.append(f"unsupported workflow path for model research entrypoint: {row.workflow_path}")
        if row.default_enabled:
            errors.append(f"model research workflow input must be opt-in: {row.workflow_input}")
        if row.formal_sync_allowed:
            errors.append(f"model research workflow must not perform formal sync: {row.workflow_input}")
        if defaults.get(row.workflow_input) != "false":
            errors.append(f"missing opt-in workflow input with false default: {row.workflow_input}")
        if f"github.event.inputs.{row.workflow_input} == 'true'" not in any_selected_line:
            errors.append(f"workflow input missing from ANY_RESEARCH_SELECTED: {row.workflow_input}")
        if f"github.event.inputs.{row.workflow_input} == 'true'" not in model_selected_line:
            errors.append(f"workflow input missing from MODEL_RESEARCH_SELECTED: {row.workflow_input}")

        command = f"python {row.producer}"
        producer_blocks = [block for block in blocks if command in block]
        expected_producer_block_count = 3 if row.producer == REVENUE_PRODUCER else 1
        if len(producer_blocks) != expected_producer_block_count:
            errors.append(
                "model-owned producer must appear in its exact workflow step count: "
                f"{row.producer}; expected={expected_producer_block_count} "
                f"actual={len(producer_blocks)}"
            )
        else:
            condition = f"github.event.inputs.{row.workflow_input} == 'true'"
            for block in producer_blocks:
                if condition not in block:
                    errors.append(
                        f"model-owned producer has wrong workflow input condition: {row.producer}"
                    )
                other_producers = sorted(
                    producer
                    for producer in producers
                    if producer != row.producer and f"python {producer}" in block
                )
                if other_producers:
                    errors.append(
                        f"model-owned workflow step mixes producers: {row.model_id}; "
                        f"others={other_producers}"
                    )
                mixed_shared_commands = sorted(
                    shared_command
                    for shared_command in SHARED_DATA_COMMANDS
                    if shared_command in block
                )
                if mixed_shared_commands:
                    errors.append(
                        f"model-owned workflow step contains shared data refresh: "
                        f"{row.model_id}; commands={mixed_shared_commands}"
                    )

        for stage_glob in (row.latest_stage_glob, row.history_stage_glob, row.docs_stage_glob):
            stage_command = f"git add {stage_glob} || true"
            if stage_command not in text:
                errors.append(f"model-owned stage allowlist missing from workflow: {stage_command}")

    shared_positions = [text.index(command) for command in SHARED_DATA_COMMANDS if command in text]
    model_positions = [
        text.index(f"python {row.producer}")
        for row in rows
        if f"python {row.producer}" in text
    ]
    if shared_positions and model_positions:
        shared_first = min(shared_positions)
        model_first = min(model_positions)
        if shared_first > model_first:
            errors.append("shared objective data refresh must precede model-owned producers")
    if model_positions and pre_run_sync in text and text.index(pre_run_sync) > min(model_positions):
        errors.append("target branch synchronization must precede model-owned producers")

    structure_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == BACKGROUND_REGISTRY_STRUCTURE_COMMAND
    ]
    full_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == BACKGROUND_REGISTRY_FULL_COMMAND
    ]
    producer_line_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if any(line == f"python {row.producer}" for row in rows)
    ]
    commit_positions = [
        index
        for index, line in enumerate(stripped_lines)
        if line == COMMIT_STEP_MARKER
    ]
    structure_blocks = [
        block
        for block in blocks
        if BACKGROUND_REGISTRY_STRUCTURE_COMMAND in {
            line.strip() for line in block.splitlines()
        }
    ]
    full_blocks = [
        block
        for block in blocks
        if BACKGROUND_REGISTRY_FULL_COMMAND in {
            line.strip() for line in block.splitlines()
        }
    ]
    if len(structure_positions) != 1 or len(structure_blocks) != 1:
        errors.append(
            "research workflow must run background registry structure-only validation "
            "exactly once before model producers"
        )
    if len(full_positions) != 2 or len(full_blocks) != 2:
        errors.append(
            "research workflow must run full background artifact validation exactly "
            "once for non-model research and once after model producers"
        )
    else:
        non_model_blocks = [
            block
            for block in full_blocks
            if "env.MODEL_RESEARCH_SELECTED != 'true'" in block
        ]
        post_model_blocks = [
            block
            for block in full_blocks
            if "env.MODEL_RESEARCH_SELECTED == 'true'" in block
        ]
        if len(non_model_blocks) != 1:
            errors.append(
                "existing registered artifacts full validation must be conditional on "
                "MODEL_RESEARCH_SELECTED != true"
            )
        if len(post_model_blocks) != 1:
            errors.append(
                "post-run full background artifact validation must be conditional on "
                "MODEL_RESEARCH_SELECTED == true"
            )
    if producer_line_positions:
        if not structure_positions or structure_positions[0] >= min(producer_line_positions):
            errors.append(
                "background registry structure-only validation must precede model-owned producers"
            )
        if not full_positions or max(full_positions) <= max(producer_line_positions):
            errors.append(
                "full background artifact validation must run after model-owned producers"
            )
        if not commit_positions or not full_positions or max(full_positions) >= min(commit_positions):
            errors.append(
                "full background artifact validation must pass before research artifacts are committed"
            )
    post_run_parity = "python scripts/validate_daily_model_research_parity.py"
    if model_positions and (
        post_run_parity not in text or text.index(post_run_parity) < max(model_positions)
    ):
        errors.append("daily model research parity validation must run after model-owned producers")

    return errors


def validate() -> list[str]:
    errors: list[str] = []
    try:
        rows = load_registry()
        model_owned_producers = load_model_owned_producers()
    except (OSError, RuntimeError, ValueError) as exc:
        return [str(exc)]
    if not WORKFLOW.is_file():
        return [f"missing research workflow: {WORKFLOW}"]
    errors.extend(validate_workflow_text(WORKFLOW.read_text(encoding="utf-8"), rows, model_owned_producers))
    if not PR_VALIDATION_WORKFLOW.is_file():
        errors.append(f"missing daily model PR validation workflow: {PR_VALIDATION_WORKFLOW}")
    else:
        errors.extend(validate_pr_workflow_text(PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8"), rows))
    for row in rows:
        if not (ROOT / row.producer).is_file():
            errors.append(f"missing model-owned workflow producer: {row.producer}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"model research workflow isolation validation passed: {WORKFLOW.relative_to(ROOT)}")
    print(f"validated_entrypoints={len(load_registry())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
