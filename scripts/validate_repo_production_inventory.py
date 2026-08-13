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
PR_SAFE_AUDIT_MANIFEST_SCHEMA_VERSION = 1
PR_SAFE_AUDIT_MODE = "base_owned_evidence_only"
PR_SAFE_AUDIT_MANIFEST_FILENAME = "pr-safe-control-plane-audit-manifest.json"
PR_SAFE_EXPECTED_WORKFLOW_REF = (
    f"{PR_SAFE_REPOSITORY}/{PR_SAFE_BASE_GUARD_WORKFLOW}@refs/heads/main"
)
PR_SAFE_ALLOWED_EVENT_ACTIONS = frozenset(
    {"opened", "synchronize", "reopened", "edited"}
)
PR_SAFE_CHECKOUT_ACTION = (
    "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803"
)
PR_SAFE_SETUP_PYTHON_ACTION = (
    "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1"
)
PR_SAFE_UPLOAD_ARTIFACT_ACTION = (
    "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02"
)
PR_SAFE_EXPECTED_ACTION_USES = (
    PR_SAFE_CHECKOUT_ACTION,
    PR_SAFE_SETUP_PYTHON_ACTION,
    PR_SAFE_CHECKOUT_ACTION,
    PR_SAFE_UPLOAD_ARTIFACT_ACTION,
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
PR_SAFE_AUDIT_STEP_NAMES = (
    "Checkout pull request base only",
    "Fetch pull request head object without checkout",
    "Validate PR head blobs and write audit-only manifest",
    "Record audit manifest SHA-256",
    "Upload audit-only evidence",
    "Fail runner when audit validator rejects",
)
PR_SAFE_AUDIT_STEP_SHA256 = (
    "1cf9ca3456324b5fc20d51705d37dee3f715e528fb912eb01cc4e7497925ecf9",
    "b90af382f61aaa0f33f4aa81515e392863444446342c505d4a3098c498b89fce",
    "e301e03e3c7c6e60231a199662fd297a706f007727cc9aa249135ddd9413fb7f",
    "26bade9c4c3b3a0e8e2fcb8b293f309e359efca4904eef8c853b0f3e3c8bed24",
    "8169e8d5635859dca2c93eef7e4221c23a1f3f92d9f92efddf3a3752f4156d2a",
    "39bd97385eabe276a77d3721ff8df61c3aa3d796a3d016755454bdce823ff845",
)
PR_SAFE_AUDIT_JOB_NAME = "pr-safe-base-audit-runner"
PR_SAFE_AUDIT_JOB_RUNS_ON = "ubuntu-latest"
PR_SAFE_AUDIT_JOB_TIMEOUT_MINUTES = "10"
PR_SAFE_AUDIT_JOB_IF_BLOCK = (
    "    if: >-",
    "      github.event_name == 'pull_request_target' &&",
    "      github.event.pull_request.base.ref == 'main' &&",
    "      github.event.pull_request.base.repo.full_name == github.repository",
)
PR_SAFE_AUDIT_JOB_HEADER_SHA256 = (
    "9b2aef41c5b06cdd3b1179b71f0773ebf2ff6ce56de801786990af27b4871806"
)
PR_SAFE_AUDIT_ARTIFACT_NAME = (
    "pr-safe-control-plane-audit-${{ github.run_id }}-${{ github.run_attempt }}"
)
PR_SAFE_AUDIT_ARTIFACT_PATHS = (
    "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json",
    "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256",
)
PR_SAFE_AUDIT_RETENTION_DAYS = "30"
PR_SAFE_AUTHORIZATION_PATH = (
    "config/daily_model_pr_safe_self_migration_authorizations.csv"
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH = (
    "config/repo_file_lifecycle_semantic_migrations.csv"
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
PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID = (
    "revenue-unreacted-range-forward-holdout-exact-target-v1"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_CONTENT_REF_SHA = (
    "77dbe2f8c0de91bd2d4a07141f0982446b9afb12"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER = (
    "scripts/validate_model_research_workflow_isolation.py"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_TEST = (
    "tests/test_model_research_workflow_isolation.py"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "aa0945c69d13ab0b562c57f8bf4638de47d8d785cfde8d604c056c647911da09",
    ".github/workflows/research_backtest_pipeline.yml": "787efe25c7703e1c344962c4b57677ac9201d27c30bc5bd3e3c53a2b754d8a36",
    "config/daily_model_background_data_registry.csv": "c82ad53052529ccd0a88239fd63655c2bfa4c87282622716254a197e5a9bdead",
    "config/daily_model_data_sharing_migrations.csv": "2e6b0c9a0efc7fe31db6a078c807cf7e1635b9dbda21142ebd8fb638742a99fe",
    "config/daily_model_data_sharing_registry.csv": "ec7ed00b38e2d13552bb362e992bff65317da0947d76dd116fa25be13d38a317",
    "config/daily_model_validator_independence.csv": "c124878ed83dfb1903879fbafcdce935a01f993c15d74761a2f98304da17e5d8",
    "config/repo_file_lifecycle_inventory.csv": "6bd6d3c81eccbcfb929112ad713de7130d02829f9e46832055b88c4bd8be1e29",
    "config/repo_production_inventory.csv": "4f155b6568f60646608ed8c0be596ceb9ba4521afb2e0da82d8b2deea2c9d89b",
    "config/report_artifact_lineage.csv": "23e9e63c1e30188bf2b388a895cceb58053acfa2a74592e2b40afc161904e39e",
    "docs/latest/model_data_independence_audit_latest.csv": "79c6603df08691024f4307ba4b33ae733950d3b1b3b57a21562aaef4634b96cb",
    "docs/latest/model_data_independence_audit_latest.md": "2497c0f5d7ae805825470b14b713bbacafc906f04fb2278b4746eaf1f920dcc8",
    "docs/latest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": None,
    "docs/latest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": None,
    "docs/latest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": None,
    "docs/latest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": None,
    "docs/latest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": None,
    "docs/specs/revenue_unreacted_range_forward_holdout.md": None,
    "output/history/research/revenue_unreacted_range_forward_holdout_anomaly_sensitivity.csv": None,
    "output/history/research/revenue_unreacted_range_forward_holdout_comparison.csv": None,
    "output/history/research/revenue_unreacted_range_forward_holdout_event_detail.csv": None,
    "output/history/research/revenue_unreacted_range_forward_holdout_manifest.csv": None,
    "output/history/research/revenue_unreacted_range_forward_holdout_maturity_status.csv": None,
    "output/latest/model_data_independence_audit_latest.csv": "79c6603df08691024f4307ba4b33ae733950d3b1b3b57a21562aaef4634b96cb",
    "output/latest/model_data_independence_audit_latest.md": "2497c0f5d7ae805825470b14b713bbacafc906f04fb2278b4746eaf1f920dcc8",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": None,
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": None,
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": None,
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": None,
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": None,
    "scripts/build_revenue_unreacted_range_research.py": "70430096dc7ee7781a94d62525db1d3a4e4555ce6b45737b06895eefbf739aed",
    "scripts/model_data_independence.py": "90f036e84780bb3077fe93e6127688de15a2157d73ae4f18f0aebaee28a2256b",
    "scripts/revenue_unreacted_range_forward_holdout.py": None,
    "scripts/validate_model_research_workflow_isolation.py": "912c59d6b0642f13b36480997af99c85ad51494e2dfcf6703225b159ae0278e6",
    "scripts/validate_revenue_unreacted_range_forward_holdout.py": None,
    "tests/test_daily_model_background_data_registry.py": "2530676b105129b6ad4a409741f46050228f695853f1aed0054be3b822b0f8b6",
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "322a8dab09ebcb7c913491868c3c1517dcdedf3b66ff847d3cd44c3160646db2",
    "tests/test_model_data_independence.py": "7420e424465eb7b97b6da6fcbf9ab7fd6a19bf09333f6eaabf33c78f6e36546b",
    "tests/test_model_research_artifact_ownership.py": "6e20d6d38e5977c5dc482bef305e18db40388a20efff8f0f01d57956d9b32b5e",
    "tests/test_model_research_workflow_isolation.py": "00305b86fbda9918864157189e96f694061528c21c0bb80d84dcc9549bf6991d",
    "tests/test_revenue_unreacted_range_forward_holdout.py": None,
    "tests/test_validate_revenue_unreacted_range_forward_holdout.py": None,
}
PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "d714ea85d7a47102186a6f2612eff9e1cc25efd3a50fbc3846e0f997c10ac405",
    ".github/workflows/research_backtest_pipeline.yml": "72297d14df7a39d290c13b7853ef2e6a30df3c5aa207fb73db4056ac4187c02a",
    "config/daily_model_background_data_registry.csv": "40e0dd17120e1340690fcaa87b1f4fb5192a023702d8a210cca929cb38ec6484",
    "config/daily_model_data_sharing_migrations.csv": "8c98df161fdb60297c93cb760baa365fb05a57d6c64e68d7653a6fbe9534fbf7",
    "config/daily_model_data_sharing_registry.csv": "15ba0fc062858943cb3a96b8a2d39be70b23000e4f6c5363182805e8e6e1a956",
    "config/daily_model_validator_independence.csv": "a76e2e232c9b063eb5e62a7f5a562610f305f9069fe20b6db583159e60d720d3",
    "config/repo_file_lifecycle_inventory.csv": "f68002587c18ca4463d80a9ba41859e6ca06b75872566242a2ce64a0fb230431",
    "config/repo_production_inventory.csv": "0273f04dc00d040b5890b3036fc10521b1c295e570aab9b48d7300914d47eac2",
    "config/report_artifact_lineage.csv": "6d8249ebfd7f28d0d11c0c6e6de3f5d6eea10d84de4f73998733b762657a15cb",
    "docs/latest/model_data_independence_audit_latest.csv": "a5039a5ebeaeb379bf424986462531e87cc9cfb9f4890c3a12b8cad9d52b3b97",
    "docs/latest/model_data_independence_audit_latest.md": "2f54c8060da9dfdfc91884257482612d1fb8f790f3b67bcbdcfc40be97af10d2",
    "docs/latest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": "5fb470b2b3f7571b10b13062393166365ebf469a05f776f10dc54156cc2f5421",
    "docs/latest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": "0c79a883dc39b005adbf8608d96815574c04616f3fcbc2bbf56ff5cb7af7576f",
    "docs/latest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": "6f5810eeb60ad61b9784f5eba483831570a7a586435d524aed8f2515e51cd703",
    "docs/latest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": "b50ed00d92c06e43b55a24c45db1206291ddc53c0791f8703fd8edb4a0ae8f6c",
    "docs/latest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": "5c41293c1b279cdccb4680f0c46dfe8b20d02d24d60a279cc587f0c33cbbe2a9",
    "docs/specs/revenue_unreacted_range_forward_holdout.md": "1302aa3dd88c896349bc782d91244f3f052b242233f64b4ffc8bfefde4b4bbdb",
    "output/history/research/revenue_unreacted_range_forward_holdout_anomaly_sensitivity.csv": "5fb470b2b3f7571b10b13062393166365ebf469a05f776f10dc54156cc2f5421",
    "output/history/research/revenue_unreacted_range_forward_holdout_comparison.csv": "0c79a883dc39b005adbf8608d96815574c04616f3fcbc2bbf56ff5cb7af7576f",
    "output/history/research/revenue_unreacted_range_forward_holdout_event_detail.csv": "6f5810eeb60ad61b9784f5eba483831570a7a586435d524aed8f2515e51cd703",
    "output/history/research/revenue_unreacted_range_forward_holdout_manifest.csv": "b50ed00d92c06e43b55a24c45db1206291ddc53c0791f8703fd8edb4a0ae8f6c",
    "output/history/research/revenue_unreacted_range_forward_holdout_maturity_status.csv": "5c41293c1b279cdccb4680f0c46dfe8b20d02d24d60a279cc587f0c33cbbe2a9",
    "output/latest/model_data_independence_audit_latest.csv": "a5039a5ebeaeb379bf424986462531e87cc9cfb9f4890c3a12b8cad9d52b3b97",
    "output/latest/model_data_independence_audit_latest.md": "2f54c8060da9dfdfc91884257482612d1fb8f790f3b67bcbdcfc40be97af10d2",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": "5fb470b2b3f7571b10b13062393166365ebf469a05f776f10dc54156cc2f5421",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": "0c79a883dc39b005adbf8608d96815574c04616f3fcbc2bbf56ff5cb7af7576f",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": "6f5810eeb60ad61b9784f5eba483831570a7a586435d524aed8f2515e51cd703",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": "b50ed00d92c06e43b55a24c45db1206291ddc53c0791f8703fd8edb4a0ae8f6c",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": "5c41293c1b279cdccb4680f0c46dfe8b20d02d24d60a279cc587f0c33cbbe2a9",
    "scripts/build_revenue_unreacted_range_research.py": "0e8fe73332a4894c069dfad9b85f2466c31a9bef10759404ea0b9f0a5b7e4101",
    "scripts/model_data_independence.py": "0142a9a26d502c947d8f061ef312f988be2edaac9cd6232b7d064db44c7dbd28",
    "scripts/revenue_unreacted_range_forward_holdout.py": "fcd8896fe633abc7a76e6bc2f7fee8ddfdc02a549538dba15a2524707135c5b5",
    "scripts/validate_model_research_workflow_isolation.py": "c9f5b0a2491136c9c0b4201d48a16674076fb964f39103f553dfcb93d28f97b4",
    "scripts/validate_revenue_unreacted_range_forward_holdout.py": "4c893613362be4d565ef4a67d35fa0820738a4c1d55a263d40045347327116d6",
    "tests/test_daily_model_background_data_registry.py": "f4a9bb4faebba075c5c4a2e7829dd97fbdb1a1ff270ddad28680a4e3fcdb5c83",
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "8eca7620ed1eb32abe10618ea1f76078e838643e5f34a79c2de2b6abe796967a",
    "tests/test_model_data_independence.py": "db757e1aa3ca092afe7c9071e3ee25e6875a68ba35696f59e14c58d11ca6ac28",
    "tests/test_model_research_artifact_ownership.py": "632f7a5eae05815211794495560ce344f020befdfa2f2cd2b7e717a9454b1124",
    "tests/test_model_research_workflow_isolation.py": "682d2083e8fb59c9e48f4e2778693305e4731a5d40b70688278804021bac7d9f",
    "tests/test_revenue_unreacted_range_forward_holdout.py": "75fe616e3af0b1bc4c6cf9000c7e6e3ab507bd4fdb9fa004e954891c971830e6",
    "tests/test_validate_revenue_unreacted_range_forward_holdout.py": "5d96e64ceb9dce37681d42430b3b6f6fa375d710cee3c14a303fd8cfd77f1ea4",
}
PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS = frozenset(
    PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID = (
    "revenue-unreacted-range-forward-holdout-replay-detail-exact-target-v1"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_CONTENT_REF_SHA = (
    "8e03b27fc65a2141701a4cad158d5c6c1f8b229b"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER = (
    "scripts/revenue_unreacted_range_forward_holdout.py"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TEST = (
    "tests/test_revenue_unreacted_range_forward_holdout.py"
)
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_SHA256_BY_PATH = {
    "config/daily_model_background_data_registry.csv": "40e0dd17120e1340690fcaa87b1f4fb5192a023702d8a210cca929cb38ec6484",
    "config/daily_model_data_sharing_migrations.csv": "8c98df161fdb60297c93cb760baa365fb05a57d6c64e68d7653a6fbe9534fbf7",
    "config/daily_model_data_sharing_registry.csv": "15ba0fc062858943cb3a96b8a2d39be70b23000e4f6c5363182805e8e6e1a956",
    "config/repo_file_lifecycle_inventory.csv": "f68002587c18ca4463d80a9ba41859e6ca06b75872566242a2ce64a0fb230431",
    "config/report_artifact_lineage.csv": "6d8249ebfd7f28d0d11c0c6e6de3f5d6eea10d84de4f73998733b762657a15cb",
    "docs/latest/model_data_independence_audit_latest.csv": "a5039a5ebeaeb379bf424986462531e87cc9cfb9f4890c3a12b8cad9d52b3b97",
    "docs/latest/model_data_independence_audit_latest.md": "2f54c8060da9dfdfc91884257482612d1fb8f790f3b67bcbdcfc40be97af10d2",
    "docs/latest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": None,
    "docs/specs/revenue_unreacted_range_forward_holdout.md": "1302aa3dd88c896349bc782d91244f3f052b242233f64b4ffc8bfefde4b4bbdb",
    "output/latest/model_data_independence_audit_latest.csv": "a5039a5ebeaeb379bf424986462531e87cc9cfb9f4890c3a12b8cad9d52b3b97",
    "output/latest/model_data_independence_audit_latest.md": "2f54c8060da9dfdfc91884257482612d1fb8f790f3b67bcbdcfc40be97af10d2",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": None,
    "scripts/build_revenue_unreacted_range_research.py": "0e8fe73332a4894c069dfad9b85f2466c31a9bef10759404ea0b9f0a5b7e4101",
    "scripts/revenue_unreacted_range_forward_holdout.py": "fcd8896fe633abc7a76e6bc2f7fee8ddfdc02a549538dba15a2524707135c5b5",
    "tests/test_daily_model_background_data_registry.py": "f4a9bb4faebba075c5c4a2e7829dd97fbdb1a1ff270ddad28680a4e3fcdb5c83",
    "tests/test_model_data_independence.py": "db757e1aa3ca092afe7c9071e3ee25e6875a68ba35696f59e14c58d11ca6ac28",
    "tests/test_model_research_artifact_ownership.py": "632f7a5eae05815211794495560ce344f020befdfa2f2cd2b7e717a9454b1124",
    "tests/test_revenue_unreacted_range_forward_holdout.py": "75fe616e3af0b1bc4c6cf9000c7e6e3ab507bd4fdb9fa004e954891c971830e6",
    "tests/test_validate_revenue_unreacted_range_forward_holdout.py": "5d96e64ceb9dce37681d42430b3b6f6fa375d710cee3c14a303fd8cfd77f1ea4",
}
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH = {
    "config/daily_model_background_data_registry.csv": "e161cd1826197072039a5f5f2aaebb7c97af31e9bc335529c936db600fbb2d08",
    "config/daily_model_data_sharing_migrations.csv": "6f82c52cb0799971621eafac0a676c2e1e7fdbdb65a6c1354a5a4fa86da2cd02",
    "config/daily_model_data_sharing_registry.csv": "7aa4fdde0f0ca9ea9aacb727ef060d89430018480b69d92dd6cf520695ef41d8",
    "config/repo_file_lifecycle_inventory.csv": "fc1fb68e6d4a4910e79386d23aed7837ce41ea9c738ad43a2992eef9c8f9e632",
    "config/report_artifact_lineage.csv": "e838d9c08c16aee1735811c3f93188407c7f09d0df574940c71b8d1ccb713566",
    "docs/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "docs/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "docs/latest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": "96ce91a25c845cbfcdadc3f6c72a3444efe3d3a8a57604685493e2c82dac863d",
    "docs/specs/revenue_unreacted_range_forward_holdout.md": "9f1f2b9e4eea895cd13012509495f13742b3bb8aabfa52cd96a74013e6a9be86",
    "output/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "output/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": "96ce91a25c845cbfcdadc3f6c72a3444efe3d3a8a57604685493e2c82dac863d",
    "scripts/build_revenue_unreacted_range_research.py": "70d549218cde2b7917bb13f54c8b41bd9e74c770896cdf4c43351bc2439df29b",
    "scripts/revenue_unreacted_range_forward_holdout.py": "11fb0878c6b9678c8321e7c6a460e5d06eb976a7f9dfd5d3dd3c9f851ea953c3",
    "tests/test_daily_model_background_data_registry.py": "ef4f0d9e3fbd3922430abc8b828d06a9ba7cd4c8eafaca005791fb1a90da124a",
    "tests/test_model_data_independence.py": "3a713e0ca5778f3d56772dc3fad6f0c5dcf0956cf446ded133eb970e4a16b5c6",
    "tests/test_model_research_artifact_ownership.py": "e071cc4ec6353a43648eae2d007569747150e5cc78759e6556e98c8748730144",
    "tests/test_revenue_unreacted_range_forward_holdout.py": "81b1dbfdedd95faf0f04058c0f7c78ae87cf291c1fc5653becafaa0ed9704e3c",
    "tests/test_validate_revenue_unreacted_range_forward_holdout.py": "8be89f425261ea8631524b07ef29d5ae43e329f0b2936c774b632fe925429595",
}
PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS = frozenset(
    PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_ID = (
    "revenue-unreacted-range-promotion-preparation-exact-target-v1"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_BASE_CONTENT_REF_SHA = (
    "6c6f43b6e2bf326ad4da550ec19b14e2675b9aab"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_HELPER = (
    "scripts/validate_model_research_workflow_isolation.py"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_TEST = (
    "tests/test_model_research_workflow_isolation.py"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "d714ea85d7a47102186a6f2612eff9e1cc25efd3a50fbc3846e0f997c10ac405",
    ".github/workflows/research_backtest_pipeline.yml": "72297d14df7a39d290c13b7853ef2e6a30df3c5aa207fb73db4056ac4187c02a",
    "config/daily_model_validator_independence.csv": "a76e2e232c9b063eb5e62a7f5a562610f305f9069fe20b6db583159e60d720d3",
    "config/repo_file_lifecycle_inventory.csv": "279a7a44a9f16962fe04cba11c8d4acfcab73c2811f44e6af508ba655c1ba619",
    "config/repo_production_inventory.csv": "7daee6c91eb11ffb9eba82af552f8dfa11792b8021492ba6907bfcc650dff434",
    "config/revenue_unreacted_range_anomaly_disposition_registry.csv": None,
    "config/revenue_unreacted_range_promotion_preparation_registry.csv": None,
    "docs/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "docs/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "docs/specs/revenue_unreacted_range_promotion_preparation_20260812.md": None,
    "output/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "output/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "scripts/model_data_independence.py": "0142a9a26d502c947d8f061ef312f988be2edaac9cd6232b7d064db44c7dbd28",
    "scripts/validate_model_research_workflow_isolation.py": "c9f5b0a2491136c9c0b4201d48a16674076fb964f39103f553dfcb93d28f97b4",
    "scripts/validate_revenue_unreacted_range_promotion_preparation.py": None,
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "8eca7620ed1eb32abe10618ea1f76078e838643e5f34a79c2de2b6abe796967a",
    "tests/test_daily_model_parameter_research.py": "9435cd06cada7de500032707a19a626110d5b39d5e2044a365f746877eb62526",
    "tests/test_daily_published_model_snapshots_pr_safe.py": "05d47d133b2afe0654c1c9755c632ecafdd6b12e5f9311d05a12c105b835d641",
    "tests/test_model_data_independence.py": "3a713e0ca5778f3d56772dc3fad6f0c5dcf0956cf446ded133eb970e4a16b5c6",
    "tests/test_model_research_workflow_isolation.py": "682d2083e8fb59c9e48f4e2778693305e4731a5d40b70688278804021bac7d9f",
    "tests/test_validate_revenue_unreacted_range_promotion_preparation.py": None,
}
PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "8e3ef3c072749dfcfd3be871a973f4983d79cb7823d485f200c84b6cd129ff25",
    ".github/workflows/research_backtest_pipeline.yml": "681117802a20c4fc5fb2c7bd143155bfd3bf2ddb3025c8a345fe29e281bb9099",
    "config/daily_model_validator_independence.csv": "1162da43004570b2836b86f7e0f58ef2f814bfc6e994b4c472de66b5d946c61a",
    "config/repo_file_lifecycle_inventory.csv": "471c77280afe9322df3df62e9c345abb432d28a40707cfa1d2650fadfa3db80c",
    "config/repo_production_inventory.csv": "e019a84107f263f77e0e4f7f9e014841ebdb470ad29d58fee91441d00258b17f",
    "config/revenue_unreacted_range_anomaly_disposition_registry.csv": "8d13efcce3feecf23231b53ec3e880cf82f72bfd4efcb9aaccc99eab18905ecc",
    "config/revenue_unreacted_range_promotion_preparation_registry.csv": "27251680b40c1f01a516f1243cefbd69282a120ae1f2b573cdc27b78ffea02b4",
    "docs/latest/model_data_independence_audit_latest.csv": "3b71b276152f93e50ca72c99a459627aa40c75abd15df3a2d9150aca6aab199e",
    "docs/latest/model_data_independence_audit_latest.md": "ebffaebdfec5a59dc89b742438a494fadebed90922748d2db672eaf21fdf5c6f",
    "docs/specs/revenue_unreacted_range_promotion_preparation_20260812.md": "3ab32414f4471952bef4e619703556068cd7e12d43439556d4a424559ac0008d",
    "output/latest/model_data_independence_audit_latest.csv": "3b71b276152f93e50ca72c99a459627aa40c75abd15df3a2d9150aca6aab199e",
    "output/latest/model_data_independence_audit_latest.md": "ebffaebdfec5a59dc89b742438a494fadebed90922748d2db672eaf21fdf5c6f",
    "scripts/model_data_independence.py": "031a7a013b9bf04f5b9a1b3c20b716094c2d9f48a1dcbfd851c57cb5cc0b124e",
    "scripts/validate_model_research_workflow_isolation.py": "9a75b27d0b061061ba946e697a666ebd7177ecd328f325413088e4d32713f8b8",
    "scripts/validate_revenue_unreacted_range_promotion_preparation.py": "5b151732eba84fd13c1d8d6631d9b1bd0df3352d37705b9d5efeff167298b8a0",
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "84ddebfcf48886cc9cec4daa4249977aaaf0e5d169edca8d9a1ba94d28e4bb64",
    "tests/test_daily_model_parameter_research.py": "32d7a95ce495953f5d85a02fc322bf320d275bbe381797a512fcb49486da862b",
    "tests/test_daily_published_model_snapshots_pr_safe.py": "36f10cb06865076ae950ad1e2e5783c42eb0a4a2f2d829ce746462e2f33cd226",
    "tests/test_model_data_independence.py": "fd3485916ca6741bc743d1b04d8e14502fcfd7fca878287953e0d49f59b7be65",
    "tests/test_model_research_workflow_isolation.py": "07f55055d31505ef7e5e0c5d6ade4dbe28b16db1d3e307576e33f8d4dc06f543",
    "tests/test_validate_revenue_unreacted_range_promotion_preparation.py": "74f295fd6f22d20c9048e3ad44cda034b392a683e531140bd0589eeee2ac4fdc",
}
PR_SAFE_REVENUE_PROMOTION_PREPARATION_PATHS = frozenset(
    PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_SHA256_BY_PATH
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_ID = (
    "revenue-unreacted-range-promotion-preparation-exact-target-v2"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_BASE_CONTENT_REF_SHA = (
    "8613b166cb86e91ef3a4f357a9f5ce40f2ec5da8"
)
PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "d714ea85d7a47102186a6f2612eff9e1cc25efd3a50fbc3846e0f997c10ac405",
    ".github/workflows/research_backtest_pipeline.yml": "72297d14df7a39d290c13b7853ef2e6a30df3c5aa207fb73db4056ac4187c02a",
    "config/daily_model_validator_independence.csv": "a76e2e232c9b063eb5e62a7f5a562610f305f9069fe20b6db583159e60d720d3",
    "config/repo_file_lifecycle_inventory.csv": "279a7a44a9f16962fe04cba11c8d4acfcab73c2811f44e6af508ba655c1ba619",
    "config/repo_production_inventory.csv": "7daee6c91eb11ffb9eba82af552f8dfa11792b8021492ba6907bfcc650dff434",
    "config/revenue_unreacted_range_anomaly_disposition_registry.csv": None,
    "config/revenue_unreacted_range_promotion_preparation_registry.csv": None,
    "docs/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "docs/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "docs/specs/revenue_unreacted_range_promotion_preparation_20260812.md": None,
    "output/latest/model_data_independence_audit_latest.csv": "21ff57d0f79fdcb861ad7284bbc46853ccbd47984a62ea7c05b9cd64ffeaf0fc",
    "output/latest/model_data_independence_audit_latest.md": "91aeff1b79e2a318b249354a56e33f88cff39d96d690d5b2413f9727cd8d8335",
    "scripts/model_data_independence.py": "0142a9a26d502c947d8f061ef312f988be2edaac9cd6232b7d064db44c7dbd28",
    "scripts/validate_model_research_workflow_isolation.py": "c9f5b0a2491136c9c0b4201d48a16674076fb964f39103f553dfcb93d28f97b4",
    "scripts/validate_revenue_unreacted_range_promotion_preparation.py": None,
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "8eca7620ed1eb32abe10618ea1f76078e838643e5f34a79c2de2b6abe796967a",
    "tests/test_daily_model_parameter_research.py": "9435cd06cada7de500032707a19a626110d5b39d5e2044a365f746877eb62526",
    "tests/test_daily_published_model_snapshots_pr_safe.py": "05d47d133b2afe0654c1c9755c632ecafdd6b12e5f9311d05a12c105b835d641",
    "tests/test_model_data_independence.py": "3a713e0ca5778f3d56772dc3fad6f0c5dcf0956cf446ded133eb970e4a16b5c6",
    "tests/test_model_research_workflow_isolation.py": "682d2083e8fb59c9e48f4e2778693305e4731a5d40b70688278804021bac7d9f",
    "tests/test_validate_revenue_unreacted_range_promotion_preparation.py": None,
}
PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_model_maintenance_pr_validation.yml": "8e3ef3c072749dfcfd3be871a973f4983d79cb7823d485f200c84b6cd129ff25",
    ".github/workflows/research_backtest_pipeline.yml": "681117802a20c4fc5fb2c7bd143155bfd3bf2ddb3025c8a345fe29e281bb9099",
    "config/daily_model_validator_independence.csv": "1162da43004570b2836b86f7e0f58ef2f814bfc6e994b4c472de66b5d946c61a",
    "config/repo_file_lifecycle_inventory.csv": "6822365492111e83297a16a930b58b120234ba68d24024762c5e2cd99873bacd",
    "config/repo_production_inventory.csv": "e019a84107f263f77e0e4f7f9e014841ebdb470ad29d58fee91441d00258b17f",
    "config/revenue_unreacted_range_anomaly_disposition_registry.csv": "8d13efcce3feecf23231b53ec3e880cf82f72bfd4efcb9aaccc99eab18905ecc",
    "config/revenue_unreacted_range_promotion_preparation_registry.csv": "27251680b40c1f01a516f1243cefbd69282a120ae1f2b573cdc27b78ffea02b4",
    "docs/latest/model_data_independence_audit_latest.csv": "3b71b276152f93e50ca72c99a459627aa40c75abd15df3a2d9150aca6aab199e",
    "docs/latest/model_data_independence_audit_latest.md": "ebffaebdfec5a59dc89b742438a494fadebed90922748d2db672eaf21fdf5c6f",
    "docs/specs/revenue_unreacted_range_promotion_preparation_20260812.md": "3ab32414f4471952bef4e619703556068cd7e12d43439556d4a424559ac0008d",
    "output/latest/model_data_independence_audit_latest.csv": "3b71b276152f93e50ca72c99a459627aa40c75abd15df3a2d9150aca6aab199e",
    "output/latest/model_data_independence_audit_latest.md": "ebffaebdfec5a59dc89b742438a494fadebed90922748d2db672eaf21fdf5c6f",
    "scripts/model_data_independence.py": "031a7a013b9bf04f5b9a1b3c20b716094c2d9f48a1dcbfd851c57cb5cc0b124e",
    "scripts/validate_model_research_workflow_isolation.py": "9a75b27d0b061061ba946e697a666ebd7177ecd328f325413088e4d32713f8b8",
    "scripts/validate_revenue_unreacted_range_promotion_preparation.py": "5b151732eba84fd13c1d8d6631d9b1bd0df3352d37705b9d5efeff167298b8a0",
    "tests/test_daily_model_maintenance_pr_validation_workflow.py": "84ddebfcf48886cc9cec4daa4249977aaaf0e5d169edca8d9a1ba94d28e4bb64",
    "tests/test_daily_model_parameter_research.py": "32d7a95ce495953f5d85a02fc322bf320d275bbe381797a512fcb49486da862b",
    "tests/test_daily_published_model_snapshots_pr_safe.py": "36f10cb06865076ae950ad1e2e5783c42eb0a4a2f2d829ce746462e2f33cd226",
    "tests/test_model_data_independence.py": "fd3485916ca6741bc743d1b04d8e14502fcfd7fca878287953e0d49f59b7be65",
    "tests/test_model_research_workflow_isolation.py": "07f55055d31505ef7e5e0c5d6ade4dbe28b16db1d3e307576e33f8d4dc06f543",
    "tests/test_validate_revenue_unreacted_range_promotion_preparation.py": "74f295fd6f22d20c9048e3ad44cda034b392a683e531140bd0589eeee2ac4fdc",
}
PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_PATHS = frozenset(
    PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID = (
    "daily-runtime-authority-containment-exact-target-v1"
)
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_CONTENT_REF_SHA = (
    "e7319ea8c3a29519358244c613830d33d80db7b8"
)
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER = (
    "scripts/validate_daily_production_boundaries.py"
)
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TEST = "tests/test_daily_production_boundaries.py"
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "8a1b02295fb3e78420952fda03de86007b1ae0bd48033dea4467aec5085e42e3",
    ".github/workflows/debug_tpex_fetch.yml": "e52e5d998cb5d4a266cdac49f1768f487c5a7b211b908d103fa1366b6ede138a",
    ".github/workflows/event_catalyst_update.yml": "0331223d91c56bf04b3360b63091d1b7b9a039ab7841353333681346706bbe9c",
    ".github/workflows/historical_structured_source_replay.yml": "3c88c42dd42c6e6646868c62ac3ff96669a60731c44bca5af6c9ec3fb1f19005",
    ".github/workflows/official_price_backfill.yml": "4e55af382a36ef2131b856faaecc04066416f27b6fc83cba034a1388549eea85",
    ".github/workflows/official_price_fetch.yml": "d4b8a50b7333daa51895504ae9b08249b46804ccf9f2b5b3ed7a777a8fad9613",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "f0d1acc2895b29138e852a33fb6b626ad3f3f66107cb8ac71058acc2e77c9d6a",
    ".github/workflows/warrant_flow.yml": "7a503e7524a392f06b0d8c22faacc2a7be957ba8b2ed87db130a11b0120800d6",
    "config/repo_file_lifecycle_inventory.csv": "fc1fb68e6d4a4910e79386d23aed7837ce41ea9c738ad43a2992eef9c8f9e632",
    "config/repo_production_inventory.csv": "0273f04dc00d040b5890b3036fc10521b1c295e570aab9b48d7300914d47eac2",
    "config/report_artifact_lineage.csv": "e838d9c08c16aee1735811c3f93188407c7f09d0df574940c71b8d1ccb713566",
    "config/runtime_file_lineage_contract.csv": "767c1c630f0bc5ff95c171c72555efc183e2348899542082960b13346439c99e",
    "scripts/daily_authority_release.py": None,
    "scripts/market_session_calendar.py": "23b8ea3e5fa8f3ac4bd25797f2686c3654d1e50e3912d054a2d062b9bc76eb1c",
    "scripts/repair_recent_daily_price_gaps.py": "d874861c85b6af7e6c4b1b84d31e9ef7e94627cde558c2db032386473fd95fab",
    "scripts/validate_daily_production_boundaries.py": "70c56bd57cc273ee1a7caa7ffcb935793c967cd7b127698e48411acd3b035010",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "46e89b21234aa2975b5d5426644581039fd8d3a27e2e17ce6f43982856e75b32",
    "scripts/validate_recent_structured_source_repair_workflow.py": "1f8ed03a16df3d18c5d0304d559122f36cbf4bd629382441bcfe28ccf667efa2",
    "tests/test_daily_authority_release.py": None,
    "tests/test_daily_production_boundaries.py": "361b937f8ad2b173ee48288bd499d4100797bbb88fd089b2e696a41ea5b486d3",
}
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "4bc3e52c69aba1d3dfda2074760a37f64af771c884ad147ad9356087dabe722b",
    ".github/workflows/debug_tpex_fetch.yml": "4167dcc0b6e1a563ea4ac17e2eaed8f84a894f8fc527ca86730f17fab525762b",
    ".github/workflows/event_catalyst_update.yml": "49888c3b5828cc0b6ff0126ccf5dcdd12db9656c2252a9efd7cca4e0875af278",
    ".github/workflows/historical_structured_source_replay.yml": "ef89646660b52954533b2a78412c1c67d56afb914adfa1300f687de93e04cd03",
    ".github/workflows/official_price_backfill.yml": "0b28a3134391cb7759259221972b6d14b134affbee1546c613d7020a15c6ea48",
    ".github/workflows/official_price_fetch.yml": "8b128b159007d66ded32862b183f9227238a3169f803e9bf9c3c521901c2a22b",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "7e6b7ccf8bcbe776d747c7526007aeda2e80d71b101161f521c4b70b91723c56",
    ".github/workflows/warrant_flow.yml": "a80b34fb274e0b5c4f007c3ae3c82f15470a427468053dca36f7eb81a546005b",
    "config/repo_file_lifecycle_inventory.csv": "3b6f5e7ff545a7ae5cab1fe3364fd17379a8daaaab2d6538b610bd95a1662a9b",
    "config/repo_production_inventory.csv": "0769a088ef4f1bb394bf33397a17307cbe7960d165fe56f2668cc88a24ae9fe2",
    "config/report_artifact_lineage.csv": "9b71464838e786a85cad3c85f37e83cc019fce0ff9cc22a9004981bfff46b155",
    "config/runtime_file_lineage_contract.csv": "e94d93888aa79a415ffa536c64f9029ba7f66a362f44f265a6765dfe7e6d42a1",
    "scripts/daily_authority_release.py": "b2895991d6b5d21443c07ffea78b6b4d8813ce883a595523baf4a8f1115fe6f8",
    "scripts/market_session_calendar.py": "529f117df989d5d8fb60a56fb444efbde3646e220bec4601aa2dbb124cceed28",
    "scripts/repair_recent_daily_price_gaps.py": "2dcab2ba980c8b394567d16cd2dbd9a8bcf2937863571ef1e0cb5e8970bbc0b1",
    "scripts/validate_daily_production_boundaries.py": "1df727afdf9a4579e0f908d1c886924d76699c2a0203249e6997d9c64610f60f",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "81c9225afb4e1c885d5f29cffa2f2bd97952546eaf6c237428f34b5357151ca8",
    "scripts/validate_recent_structured_source_repair_workflow.py": "5ff826ffd0ca207a686e0ed87ba710bd9315735a2c2dfb5d091a8dc9ed941676",
    "tests/test_daily_authority_release.py": "1659d68c1ed9d2b6f8251f76b607ba2dfd284045aadc08c87d306a88ca5911d4",
    "tests/test_daily_production_boundaries.py": "c6464e7afe88d9cbc786592bc4269415e9370774e111b55e0a226bb951453669",
}
PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS = frozenset(
    PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID = (
    "daily-runtime-recovery-architecture-exact-target-v1"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_CONTENT_REF_SHA = (
    "99271e96ce59b1651d327065480115a6a52887b8"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER = (
    "scripts/validate_recent_structured_source_repair_workflow.py"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TEST = (
    "tests/test_validate_recent_structured_source_repair_workflow.py"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "4bc3e52c69aba1d3dfda2074760a37f64af771c884ad147ad9356087dabe722b",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "7e6b7ccf8bcbe776d747c7526007aeda2e80d71b101161f521c4b70b91723c56",
    "config/repo_file_lifecycle_inventory.csv": "3b6f5e7ff545a7ae5cab1fe3364fd17379a8daaaab2d6538b610bd95a1662a9b",
    "config/repo_production_inventory.csv": "0769a088ef4f1bb394bf33397a17307cbe7960d165fe56f2668cc88a24ae9fe2",
    "config/report_artifact_lineage.csv": "9b71464838e786a85cad3c85f37e83cc019fce0ff9cc22a9004981bfff46b155",
    "scripts/daily_source_recovery_bundle.py": None,
    "scripts/repair_recent_daily_price_gaps.py": "2dcab2ba980c8b394567d16cd2dbd9a8bcf2937863571ef1e0cb5e8970bbc0b1",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "81c9225afb4e1c885d5f29cffa2f2bd97952546eaf6c237428f34b5357151ca8",
    "scripts/validate_recent_structured_source_repair_workflow.py": "5ff826ffd0ca207a686e0ed87ba710bd9315735a2c2dfb5d091a8dc9ed941676",
    "tests/test_daily_price_history_continuity.py": "7d6b99544893ccbf2c61c37db651a6651ceafddded6ed8450ac91ffb51b6f05c",
    "tests/test_daily_production_boundaries.py": "c6464e7afe88d9cbc786592bc4269415e9370774e111b55e0a226bb951453669",
    "tests/test_daily_source_recovery_bundle.py": None,
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "a4e5a43f76f179dee0034cf05783bf5b96619218df367fe09e6d7781cb98ad3d",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "eea49e7f70a4787a5a0aa065e60b59e3a795eeac9377c5d70255564a3e5cc36b",
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "8fc456bfbcb9701f0168a838cee9b5407112ab0ec634d582a3a1b3ca21480ea6",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "b8675aba39faeea26b0de8b7d377e1d344c8d7f8b63f4528a46c69434a39dce2",
    "config/repo_file_lifecycle_inventory.csv": "279a7a44a9f16962fe04cba11c8d4acfcab73c2811f44e6af508ba655c1ba619",
    "config/repo_production_inventory.csv": "7daee6c91eb11ffb9eba82af552f8dfa11792b8021492ba6907bfcc650dff434",
    "config/report_artifact_lineage.csv": "02d4da43c7aec79cb873c120f7040d20e96235fd2352f886a70c91e2c399c65d",
    "scripts/daily_source_recovery_bundle.py": "8b44388a53c66a72b3669409f53a32210264aaadd1a32ccc1ac326a0ad32b6ba",
    "scripts/repair_recent_daily_price_gaps.py": "35975f124172082180da7deedf5f23825c484be9feb7044894c8823bffdac2b5",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "95ce98d3f74c871e6f522b62368e8d0bfd22148186f590fc5fc59d40cf1a9c8c",
    "scripts/validate_recent_structured_source_repair_workflow.py": "149998534996ae05fff5de64a8e616ce0528017cf455f0189fbf1e807440356d",
    "tests/test_daily_price_history_continuity.py": "20d3f10fc69c0e2ada12ceb34c0ed0e7331d61343bb2335fc1ad6466d849c3aa",
    "tests/test_daily_production_boundaries.py": "80e72199372ed4ec71725f898f57d6f62214bc7285e86e5764df3b792cd586b1",
    "tests/test_daily_source_recovery_bundle.py": "ab888cd8edcf6cdf92ed2be12612ebd2f7de801a737c4e4561bfa5bf9bf8cce2",
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "6818e353e2f776a2b6bd6bc625ba2bfa864872c7747dc30a854939d67ee97671",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "153549586fa43eeedf93fc93dba1c78f4e8345f0ae2fe1c08310fb89568364f1",
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS = frozenset(
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_ID = (
    "daily-runtime-recovery-architecture-exact-target-v2"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_CONTENT_REF_SHA = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_CONTENT_REF_SHA
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_HELPER = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TEST = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TEST
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH,
    "scripts/validate_daily_production_boundaries.py": (
        "1df727afdf9a4579e0f908d1c886924d76699c2a0203249e6997d9c64610f60f"
    ),
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH,
    "scripts/validate_daily_production_boundaries.py": (
        "e043f3c6eb0bd0d2cf77333ff5461908d9a3f58a05336a7848486f77a6ca4ffe"
    ),
    "tests/test_daily_production_boundaries.py": (
        "168c3f1a1b5094f0336166571c5870e9a9760c44722ee5f34495a820aba1d3cc"
    ),
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_PATHS = frozenset(
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_ID = (
    "daily-runtime-recovery-architecture-exact-target-v3"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_CONTENT_REF_SHA = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_CONTENT_REF_SHA
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_HELPER = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_HELPER
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TEST = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TEST
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_SHA256_BY_PATH,
    ".github/workflows/daily_full_pipeline.yml": (
        "245f4e15a3e1aded0c1694c21d954e494b2f83dfecedc9ec5441c44c142fa906"
    ),
    "scripts/validate_daily_production_boundaries.py": (
        "1271234fbf38bbebfdb99617ccab239d466a29c0ed2f1eb1ece30cade55a668f"
    ),
    "scripts/validate_recent_structured_source_repair_workflow.py": (
        "aecb4ba2aa06e24c2b8d7c5bd097c489f2eaa89957233e6ccd571dc1dc20605b"
    ),
    "tests/test_daily_production_boundaries.py": (
        "d0cff54c9e57344856d4aad16c2286afda5d015aeccf6a0921dc9cbcb00c381e"
    ),
    "tests/test_validate_recent_structured_source_repair_workflow.py": (
        "5ba11898291dcbec297c7b4ea971ee713fb2a565ddf98e8f7bc5a5d61460bbce"
    ),
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_PATHS = frozenset(
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_ID = (
    "daily-runtime-recovery-architecture-exact-target-v4"
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_BASE_CONTENT_REF_SHA = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_CONTENT_REF_SHA
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_HELPER = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_HELPER
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TEST = (
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TEST
)
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_BASE_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_SHA256_BY_PATH,
    "tests/test_daily_production_boundaries.py": (
        "67a6e289a6222acb69ac26f9c7b06cc1671f9d68a80b56792dc30ee9fdffcbd2"
    ),
    "tests/test_validate_recent_structured_source_repair_workflow.py": (
        "55d2a01aa8c0cabc847658e8d12a951a6bcc7c7da1bbfdd64e551595ad46fad1"
    ),
}
PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_PATHS = frozenset(
    PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_ID = (
    "daily-runtime-integration-regressions-exact-target-v1"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_CONTENT_REF_SHA = (
    "fa75fe901b21f791107dd0c3d284e4263d241c05"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PULL_REQUEST_NUMBER = 539
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_REPOSITORY = PR_SAFE_REPOSITORY
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_RUN_ATTEMPT = 1
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_HELPER = (
    "scripts/validate_recent_structured_source_repair_workflow.py"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TEST = (
    "tests/test_validate_recent_structured_source_repair_workflow.py"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "245f4e15a3e1aded0c1694c21d954e494b2f83dfecedc9ec5441c44c142fa906",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "b8675aba39faeea26b0de8b7d377e1d344c8d7f8b63f4528a46c69434a39dce2",
    "config/repo_file_lifecycle_inventory.csv": "6822365492111e83297a16a930b58b120234ba68d24024762c5e2cd99873bacd",
    "fetch_official_daily_price.py": "ffcf29287057280c5f3d92e575ce222d8cf2bd8bfc8415d1645a277be5548f94",
    "scripts/daily_source_recovery_bundle.py": "8b44388a53c66a72b3669409f53a32210264aaadd1a32ccc1ac326a0ad32b6ba",
    "scripts/market_session_calendar.py": "529f117df989d5d8fb60a56fb444efbde3646e220bec4601aa2dbb124cceed28",
    "scripts/repair_recent_daily_price_gaps.py": "35975f124172082180da7deedf5f23825c484be9feb7044894c8823bffdac2b5",
    "scripts/run_daily_full_validation_replay.py": "cc594e9fc191cf004d8d98729a97220f694cb7d2bed67dde15858fe7e06a9686",
    "scripts/validate_daily_full_validation_replay.py": "298d45808fd414ed1816cac4375169c943cda47a5dd7ab13b1224890f80c14c4",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "95ce98d3f74c871e6f522b62368e8d0bfd22148186f590fc5fc59d40cf1a9c8c",
    "scripts/validate_recent_structured_source_repair_workflow.py": "aecb4ba2aa06e24c2b8d7c5bd097c489f2eaa89957233e6ccd571dc1dc20605b",
    "tests/test_daily_full_validation_replay.py": "aed958a6937aa570c829080787ae2ffd2c2e160ef133765e359228de532780f2",
    "tests/test_daily_production_boundaries.py": "67a6e289a6222acb69ac26f9c7b06cc1671f9d68a80b56792dc30ee9fdffcbd2",
    "tests/test_daily_source_recovery_bundle.py": "ab888cd8edcf6cdf92ed2be12612ebd2f7de801a737c4e4561bfa5bf9bf8cce2",
    "tests/test_market_session_calendar.py": "26138bc25094ce6ec334a2a40bd26cdce0ee85dfa35d52de4a4f6e749a8ec97f",
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "6818e353e2f776a2b6bd6bc625ba2bfa864872c7747dc30a854939d67ee97671",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "55d2a01aa8c0cabc847658e8d12a951a6bcc7c7da1bbfdd64e551595ad46fad1",
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "4b0b07ebd4e38f6383eaa5630638b17eee21e8e4c7685df1d6a386b54576151b",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "c71ce7cb531d48cb4f986b906e24c316ba86b9c22c0f8d1f72a9a8e0a79542ff",
    "config/repo_file_lifecycle_inventory.csv": "7de82d1d695b841f1212e36c9e3fedb44151685896fe2ca2881aa642c8d9de3f",
    "fetch_official_daily_price.py": "e0be065fce65e90ddfa42114f7e00c51abedc5229ae2c2682ce009fa8fd0acea",
    "scripts/daily_source_recovery_bundle.py": "d09c8a2c5e1fa3a1a0d12e99c63bfb2d6e6f415bacbf4ca15e424102cdb2531d",
    "scripts/market_session_calendar.py": "26e5c4819617c5d5b976b07b1b82068d83c5b7cf193cc750e9ed37c6c67801e9",
    "scripts/repair_recent_daily_price_gaps.py": "00b30cee68a969f354846e937523e4fc870e0f9dd62d06be954755dafcbdac76",
    "scripts/run_daily_full_validation_replay.py": "0ff9cfc5927312bfac6aa62b6dce237435461a86772a7b569c759ac0923c28e1",
    "scripts/validate_daily_full_validation_replay.py": "3278b57a5b745fd0f9612c4315fca0c4dcdccb5fa5ff59be8e19baa437cb71c7",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "f632ba3a0ceab60b6879193dbc57119595b8f4c5a8c2a0f72d9e280d370e7c91",
    "scripts/validate_recent_structured_source_repair_workflow.py": "b7bc22b49f552ab957cfcac73eeaf3974a00aeb6fb8037b3797c6c0e2b50cf4b",
    "tests/test_daily_full_validation_replay.py": "6edef65598a2cd090bf3b566d881a749b5ecee7d8fb231ee38ccea5a4a616bf5",
    "tests/test_daily_production_boundaries.py": "fd821d51597389b08d066064965695832f5d9a2b339239c7921d4b9e494e5360",
    "tests/test_daily_source_recovery_bundle.py": "9e60207bcd4e2152abbfc44ceaa5b74ae425d17e2a44ef5cceb23777215fc2ac",
    "tests/test_market_session_calendar.py": "338bfac554153f38c48fc8e64102cc7f759d7bce44b074a4e4a9f00f437a527b",
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "341e119fe4fa772136390bb007578e5071469e8ef4785e3a6546df60315428b2",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "5f1635e79b0ab4c1ad2c1314b8c72b7f273dbd23e51398a24444f5ec3999b0a1",
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PATHS = frozenset(
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_MODE_BY_PATH = {
    path: "100644" for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PATHS
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_OBJECT_TYPE_BY_PATH = {
    path: "blob" for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PATHS
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_ID = (
    "daily-runtime-integration-regressions-exact-target-v2"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_CONTENT_REF_SHA = (
    "c128cedaf36f1176d539539d580d014598cfc743"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_HELPER = (
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_HELPER
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TEST = (
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TEST
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "4b0b07ebd4e38f6383eaa5630638b17eee21e8e4c7685df1d6a386b54576151b",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "d7fc0adc10c6984957e973512b44bb61a5b4a4947915f2c2060ad8fa1def04f1",
    "config/repo_file_lifecycle_inventory.csv": "22c79ea3915ebe7c66bb1b2bdd8721e501db79715111dfd2e8073ef9d9029c6b",
    "fetch_official_daily_price.py": "cdf155d5bd78d19e16a14e9cc09aef22e535560d25feace8aa618b2ada26dca4",
    "scripts/daily_source_recovery_bundle.py": "d09c8a2c5e1fa3a1a0d12e99c63bfb2d6e6f415bacbf4ca15e424102cdb2531d",
    "scripts/market_session_calendar.py": "2e7fedb433adea4a7e417f4e1aa58f85bc55d12128e82e487d071b669d6bf3a2",
    "scripts/repair_recent_daily_price_gaps.py": "82f49361cafeea3506c0338ba16dbc509168bed5e549cd774dff9b4df25fd860",
    "scripts/run_daily_full_validation_replay.py": "0ff9cfc5927312bfac6aa62b6dce237435461a86772a7b569c759ac0923c28e1",
    "scripts/validate_daily_full_validation_replay.py": "3278b57a5b745fd0f9612c4315fca0c4dcdccb5fa5ff59be8e19baa437cb71c7",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "a7ee88cc0c4fa24bb344a6377d72122f9f7f2e464898b1bf462d8d3b18ea6b35",
    "scripts/validate_recent_structured_source_repair_workflow.py": "2b9ff401efe48ae2d51d0b25ff0263d1a3987cd5b0b67e80506408fccb0a3e6a",
    "tests/test_daily_full_validation_replay.py": "09d8e62f41dd69fa30192e6610c59d05b2e85b311a2ba573eeae384d83c94097",
    "tests/test_daily_production_boundaries.py": "6202fc24f60b06caecb73539a1d2ba3856ed852f27c83e03a13cf46709ac749f",
    "tests/test_daily_source_recovery_bundle.py": "863a29e2fde8e3ae8aaa93727371b53cdca01afeb8e2fd10b6acbb1679e96e8b",
    "tests/test_market_session_calendar.py": "e4395cfcb46bc8b1f0a5d007961b10c864dced030dcaa0ffa68ce283da44ac45",
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "ab7b648bd136afaa09d3701c82d05253167f3170bf23c358daffc0b5de923420",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "d3b02cb30b181f9521c785fb7f61a26038d9f1ced813831c031736a0e71ae620",
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_PATHS = frozenset(
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_RAW_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_RAW_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_MODE_BY_PATH = {
    path: "100644"
    for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_PATHS
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_OBJECT_TYPE_BY_PATH = {
    path: "blob"
    for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_PATHS
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_ID = (
    "daily-runtime-integration-regressions-exact-target-v3"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_CONTENT_REF_SHA = (
    "4909056fe11bb3667df355aa406ac6bd82528a10"
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_HELPER = (
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_HELPER
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TEST = (
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TEST
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_SHA256_BY_PATH = {
    ".github/workflows/daily_full_pipeline.yml": "4b0b07ebd4e38f6383eaa5630638b17eee21e8e4c7685df1d6a386b54576151b",
    ".github/workflows/repair_recent_daily_price_gaps.yml": "51b9863503985d3d18ff064d2a29705a13e7f97baa6fd5de4d91951d20c53841",
    "config/repo_file_lifecycle_inventory.csv": "22c79ea3915ebe7c66bb1b2bdd8721e501db79715111dfd2e8073ef9d9029c6b",
    "fetch_official_daily_price.py": "5eca761565de41cc3d765ff762f83c262e7afd4f8d4337b282155c263595de22",
    "scripts/daily_source_recovery_bundle.py": "d09c8a2c5e1fa3a1a0d12e99c63bfb2d6e6f415bacbf4ca15e424102cdb2531d",
    "scripts/market_session_calendar.py": "2e7fedb433adea4a7e417f4e1aa58f85bc55d12128e82e487d071b669d6bf3a2",
    "scripts/repair_recent_daily_price_gaps.py": "82f49361cafeea3506c0338ba16dbc509168bed5e549cd774dff9b4df25fd860",
    "scripts/run_daily_full_validation_replay.py": "0ff9cfc5927312bfac6aa62b6dce237435461a86772a7b569c759ac0923c28e1",
    "scripts/validate_daily_full_validation_replay.py": "3278b57a5b745fd0f9612c4315fca0c4dcdccb5fa5ff59be8e19baa437cb71c7",
    "scripts/validate_recent_daily_price_repair_staged_paths.py": "62a11d1694fa513d3f7ea927fb1de6fe30d0efa31b0557354227f5d9d61d872f",
    "scripts/validate_recent_structured_source_repair_workflow.py": "df28e2f36096e59ce88401df36d38beab7b4a15d400eb9e4afb1b11e7e525f59",
    "tests/test_daily_full_validation_replay.py": "09d8e62f41dd69fa30192e6610c59d05b2e85b311a2ba573eeae384d83c94097",
    "tests/test_daily_production_boundaries.py": "6202fc24f60b06caecb73539a1d2ba3856ed852f27c83e03a13cf46709ac749f",
    "tests/test_daily_source_recovery_bundle.py": "863a29e2fde8e3ae8aaa93727371b53cdca01afeb8e2fd10b6acbb1679e96e8b",
    "tests/test_market_session_calendar.py": "4ee299786f44ba82b6c9a5c254ced6f3c0f2bd13f1c69ffb45e1c86dbed9cf2a",
    "tests/test_validate_recent_daily_price_repair_staged_paths.py": "69384a69ee59096c3867afa7df381edc07739d4539b18ff38a060a4a7cb78ba3",
    "tests/test_validate_recent_structured_source_repair_workflow.py": "6477736164b2ef1e7129ec742496b0a7b5b83388161a1c051858ca271a50a52a",
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_PATHS = frozenset(
    PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_SHA256_BY_PATH
)
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_RAW_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_RAW_SHA256_BY_PATH = {
    **PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_SHA256_BY_PATH,
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_MODE_BY_PATH = {
    path: "100644"
    for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_PATHS
}
PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_OBJECT_TYPE_BY_PATH = {
    path: "blob"
    for path in PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_PATHS
}
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
PR_SAFE_TRIGGER_PATHS = tuple(sorted(PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS))
PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS = frozenset(
    {
        PR_SAFE_BASE_GUARD_WORKFLOW,
        PR_SAFE_BASE_GUARD_SCRIPT,
        PR_SAFE_AUTHORIZATION_PATH,
        PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
    }
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
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_pdf_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_model_research_workflow_isolation.py",
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
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
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
}

PYTHON_INVOKE_RE = re.compile(r"\bpython(?:3)?\s+([A-Za-z0-9_./\\-]+\.py)")
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
    trigger_paths, trigger_errors = workflow_trigger_paths(
        text,
        "pull_request_target",
    )
    errors.extend(trigger_errors)
    if trigger_paths != PR_SAFE_TRIGGER_PATHS:
        errors.append("pull_request_target paths must match the exact Stage1 path set")
    action_uses, action_errors = workflow_action_uses(text)
    errors.extend(action_errors)
    if action_uses != PR_SAFE_EXPECTED_ACTION_USES:
        errors.append("workflow uses entries must match the exact ordered pinned action set")

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
        regular_timeouts = re.findall(
            r"^    timeout-minutes:\s*(.*?)\s*$",
            regular_job,
            flags=re.MULTILINE,
        )
        if regular_timeouts != ["30"]:
            errors.append("regular individual-stock PR validation job must use timeout-minutes: 30")

    audit_job = jobs.get(PR_SAFE_AUDIT_JOB_NAME, "")
    if not audit_job:
        return [*errors, "base-owned PR-safe audit runner job is missing"]
    audit_header_sha256, audit_header_errors = canonical_workflow_job_header_sha256(
        audit_job
    )
    errors.extend(audit_header_errors)
    if audit_header_sha256 != PR_SAFE_AUDIT_JOB_HEADER_SHA256:
        errors.append("audit runner job header must match the exact canonical contract")
    if workflow_job_scalar_values(audit_job, "name") != (PR_SAFE_AUDIT_JOB_NAME,):
        errors.append("audit runner name must appear once and match its non-required context")
    if workflow_job_scalar_values(audit_job, "runs-on") != (
        PR_SAFE_AUDIT_JOB_RUNS_ON,
    ):
        errors.append("audit runner runs-on must appear once and equal ubuntu-latest")
    if workflow_job_scalar_values(audit_job, "timeout-minutes") != (
        PR_SAFE_AUDIT_JOB_TIMEOUT_MINUTES,
    ):
        errors.append("audit runner timeout-minutes must appear once and equal 10")
    audit_if_block, audit_if_errors = workflow_job_multiline_block(audit_job, "if")
    errors.extend(audit_if_errors)
    if audit_if_block != PR_SAFE_AUDIT_JOB_IF_BLOCK:
        errors.append("audit runner if condition must match the exact base-owned contract")
    audit_permissions, audit_permission_errors = workflow_exact_mapping(
        audit_job,
        "permissions",
        section_indent=4,
        entry_indent=6,
    )
    errors.extend(audit_permission_errors)
    if audit_permissions != PR_SAFE_READ_ONLY_PERMISSIONS:
        errors.append("audit runner permissions must contain exactly contents: read")
    if not re.search(
        r"^    timeout-minutes:\s*10\s*$",
        audit_job,
        flags=re.MULTILINE,
    ):
        errors.append("base-owned PR-safe audit runner must use timeout-minutes: 10")
    steps = workflow_step_blocks(audit_job)
    step_names = tuple(workflow_step_name(step) for step in steps)
    if step_names != PR_SAFE_AUDIT_STEP_NAMES:
        errors.append("audit runner steps must match the exact six-step ordered name contract")
    step_sha256 = tuple(canonical_workflow_step_sha256(step) for step in steps)
    if step_sha256 != PR_SAFE_AUDIT_STEP_SHA256:
        errors.append(
            "audit runner steps must match the exact canonical security contract"
        )
    audit_checkout_steps = [
        step for step in steps if workflow_step_uses(step).startswith("actions/checkout@")
    ]
    if len(audit_checkout_steps) != 1 or workflow_step_uses(
        audit_checkout_steps[0] if audit_checkout_steps else ""
    ) != PR_SAFE_CHECKOUT_ACTION:
        errors.append("audit runner must use exactly one pinned checkout step")

    upload_steps = [
        step
        for step in steps
        if workflow_step_uses(step).startswith("actions/upload-artifact@")
    ]
    if len(upload_steps) != 1:
        errors.append("audit runner must contain exactly one upload-artifact step")
        return errors
    upload_step = upload_steps[0]
    if workflow_step_uses(upload_step) != PR_SAFE_UPLOAD_ARTIFACT_ACTION:
        errors.append("audit evidence upload must use the pinned official action SHA")
    if workflow_step_name(upload_step) != "Upload audit-only evidence":
        errors.append("audit evidence upload step name mismatch")
    if workflow_step_condition(upload_step) != "always()":
        errors.append("audit evidence upload must use if: always()")
    with_values, with_errors = workflow_step_with_values(upload_step)
    errors.extend(with_errors)
    expected_with: dict[str, str | tuple[str, ...]] = {
        "name": PR_SAFE_AUDIT_ARTIFACT_NAME,
        "path": PR_SAFE_AUDIT_ARTIFACT_PATHS,
        "if-no-files-found": "error",
        "retention-days": PR_SAFE_AUDIT_RETENTION_DAYS,
    }
    if with_values != expected_with:
        errors.append("audit evidence upload with mapping must match the exact contract")
    required_sidecar_lines = (
        'manifest_name="$(basename "$AUDIT_MANIFEST")"',
        '(cd "$manifest_dir" && sha256sum "$manifest_name" > '
        '"${manifest_name}.sha256")',
    )
    if not all(line in audit_job for line in required_sidecar_lines):
        errors.append("audit SHA-256 sidecar must reference the manifest basename")
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


def validate_workflow_snippets(errors: list[str]) -> None:
    for workflow_path, command_list in REQUIRED_WORKFLOW_COMMANDS.items():
        if not (ROOT / workflow_path).exists():
            continue
        text = read_text(workflow_path)
        for command in command_list:
            if command not in text:
                errors.append(f"{workflow_path} must run {command}")

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
    revenue_profiles = pr_safe_revenue_forward_holdout_target_profiles(changed_paths)
    if target_id is not None:
        revenue_profiles = tuple(
            profile for profile in revenue_profiles if profile[0] == target_id
        )
    revenue_target = revenue_profiles[0] if len(revenue_profiles) == 1 else None
    observed_hashes = (
        base_helper_sha256,
        current_helper_sha256,
        current_test_sha256,
    )
    if revenue_profiles and all(observed_hashes):
        exact_profiles = [
            profile
            for profile in revenue_profiles
            if (
                profile[4][profile[2]],
                profile[5][profile[2]],
                profile[5][profile[3]],
            )
            == observed_hashes
        ]
        revenue_target = exact_profiles[0] if len(exact_profiles) == 1 else None
    if revenue_target is not None:
        return (
            revenue_target[0],
            revenue_target[2],
            revenue_target[3],
            revenue_target[6],
        )
    authority_profiles = pr_safe_daily_authority_containment_target_profiles(
        changed_paths
    )
    authority_target = authority_profiles[0] if authority_profiles else None
    if authority_profiles and all(observed_hashes):
        exact_profiles = [
            profile
            for profile in authority_profiles
            if (
                profile[4][profile[2]],
                profile[5][profile[2]],
                profile[5][profile[3]],
            )
            == observed_hashes
        ]
        authority_target = exact_profiles[0] if len(exact_profiles) == 1 else None
    if authority_target is not None:
        return (
            authority_target[0],
            authority_target[2],
            authority_target[3],
            authority_target[6],
        )
    if changed_paths == PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS:
        return (
            PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS,
        )
    if changed_paths == PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS:
        return (
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
        )
    if changed_paths == PR_SAFE_AUTHORIZED_STAGE1_PATHS:
        return (
            PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID,
            PR_SAFE_ADVANCED_HELPER,
            PR_SAFE_ADVANCED_TEST,
            PR_SAFE_AUTHORIZED_STAGE1_PATHS,
        )
    if changed_paths == PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS:
        return (
            PR_SAFE_SNAPSHOT_MIGRATION_ID,
            PR_SAFE_SNAPSHOT_HELPER,
            PR_SAFE_SNAPSHOT_TEST,
            PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
        )
    return None


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


def pr_safe_revenue_forward_holdout_target_profiles(
    changed_paths: set[str],
) -> tuple[tuple[
    str,
    str,
    str,
    str,
    dict[str, str | None],
    dict[str, str],
    frozenset[str],
], ...]:
    normalized_paths = frozenset(str(path).replace("\\", "/") for path in changed_paths)
    profiles = (
        (
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_CONTENT_REF_SHA,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_TEST,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS,
        ),
        (
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_CONTENT_REF_SHA,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TEST,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_SHA256_BY_PATH,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH,
            PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS,
        ),
        (
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_ID,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_BASE_CONTENT_REF_SHA,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_HELPER,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_TEST,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_BASE_SHA256_BY_PATH,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_SHA256_BY_PATH,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_PATHS,
        ),
        (
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_ID,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_BASE_CONTENT_REF_SHA,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_HELPER,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_TEST,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_BASE_SHA256_BY_PATH,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_SHA256_BY_PATH,
            PR_SAFE_REVENUE_PROMOTION_PREPARATION_PATHS,
        ),
    )
    return tuple(profile for profile in profiles if normalized_paths == profile[6])


def pr_safe_revenue_forward_holdout_target_profile(
    changed_paths: set[str],
    *,
    target_id: str | None = None,
) -> tuple[
    str,
    str,
    str,
    str,
    dict[str, str | None],
    dict[str, str],
    frozenset[str],
] | None:
    profiles = pr_safe_revenue_forward_holdout_target_profiles(changed_paths)
    if target_id is None:
        return profiles[0] if profiles else None
    return next((profile for profile in profiles if profile[0] == target_id), None)


def preauthorized_revenue_forward_holdout_target_profile(
    base_ref: str,
    changed_paths: set[str],
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
    target_id: str | None = None,
) -> tuple[
    str,
    str,
    str,
    str,
    dict[str, str | None],
    dict[str, str],
    frozenset[str],
] | None:
    if not re.fullmatch(r"[0-9a-f]{40}", str(base_ref)):
        return None
    profiles = pr_safe_revenue_forward_holdout_target_profiles(changed_paths)
    if target_id is not None:
        profiles = tuple(profile for profile in profiles if profile[0] == target_id)
    root = Path(repository_root).resolve()
    matching_profiles = []
    for profile in profiles:
        (
            _profile_target_id,
            base_content_ref_sha,
            _helper_path,
            _test_path,
            base_sha256_by_path,
            target_sha256_by_path,
            target_paths,
        ) = profile
        if (
            set(base_sha256_by_path) != target_paths
            or set(target_sha256_by_path) != target_paths
            or not _pr_safe_repo_ref_is_ancestor(root, base_content_ref_sha, base_ref)
            or not _pr_safe_repo_ref_is_ancestor(root, base_ref, head_ref)
        ):
            continue
        profile_matches = True
        for path in sorted(target_paths):
            base_blob = _pr_safe_repo_blob(root, base_ref, path)
            target_blob = _pr_safe_repo_blob(root, head_ref, path)
            expected_base_sha = base_sha256_by_path[path]
            expected_target_sha = target_sha256_by_path[path]
            if expected_base_sha is None:
                if (
                    base_blob is not None
                    or _pr_safe_repo_blob_mode(root, base_ref, path) is not None
                ):
                    profile_matches = False
                    break
            elif (
                base_blob is None
                or canonical_blob_sha256(base_blob) != expected_base_sha
                or _pr_safe_repo_blob_mode(root, base_ref, path) != "100644"
            ):
                profile_matches = False
                break
            if (
                target_blob is None
                or canonical_blob_sha256(target_blob) != expected_target_sha
                or _pr_safe_repo_blob_mode(root, head_ref, path) != "100644"
            ):
                profile_matches = False
                break
        if profile_matches:
            matching_profiles.append(profile)
    return matching_profiles[0] if len(matching_profiles) == 1 else None


def is_preauthorized_revenue_forward_holdout_target(
    base_ref: str,
    changed_paths: set[str],
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
    target_id: str | None = None,
) -> bool:
    return preauthorized_revenue_forward_holdout_target_profile(
        base_ref,
        changed_paths,
        repository_root=repository_root,
        head_ref=head_ref,
        target_id=target_id,
    ) is not None


def pr_safe_daily_authority_containment_target_profiles(
    changed_paths: set[str],
) -> tuple[tuple[
    str,
    str,
    str,
    str,
    dict[str, str | None],
    dict[str, str],
    frozenset[str],
], ...]:
    normalized_paths = frozenset(str(path).replace("\\", "/") for path in changed_paths)
    profiles = (
        (
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_ID,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_HELPER,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TEST,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_PATHS,
        ),
        (
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_ID,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_HELPER,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TEST,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_PATHS,
        ),
        (
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_ID,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_HELPER,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TEST,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PATHS,
        ),
        (
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_ID,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_HELPER,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TEST,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_PATHS,
        ),
        (
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_ID,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_HELPER,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TEST,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_PATHS,
        ),
        (
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TEST,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS,
        ),
        (
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TEST,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS,
        ),
        (
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_ID,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_CONTENT_REF_SHA,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_HELPER,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TEST,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_BASE_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_SHA256_BY_PATH,
            PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_PATHS,
        ),
    )
    return tuple(profile for profile in profiles if normalized_paths == profile[6])


def pr_safe_daily_authority_containment_target_profile(
    changed_paths: set[str],
    *,
    target_id: str | None = None,
) -> tuple[
    str,
    str,
    str,
    str,
    dict[str, str | None],
    dict[str, str],
    frozenset[str],
] | None:
    profiles = pr_safe_daily_authority_containment_target_profiles(changed_paths)
    if target_id is None:
        return profiles[0] if profiles else None
    return next((profile for profile in profiles if profile[0] == target_id), None)


def daily_runtime_integration_regressions_identity_contract(
    target_id: str,
) -> tuple[
    dict[str, str] | None,
    dict[str, str] | None,
    dict[str, str],
    dict[str, str],
] | None:
    if target_id == PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_ID:
        return (
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_BASE_RAW_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_RAW_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_MODE_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_OBJECT_TYPE_BY_PATH,
        )
    if target_id == PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_ID:
        return (
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_BASE_RAW_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_RAW_SHA256_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_MODE_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_OBJECT_TYPE_BY_PATH,
        )
    if target_id == PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_ID:
        return (
            None,
            None,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_MODE_BY_PATH,
            PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_OBJECT_TYPE_BY_PATH,
        )
    return None


def is_preauthorized_daily_authority_containment_target(
    base_ref: str,
    changed_paths: set[str],
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> bool:
    profiles = pr_safe_daily_authority_containment_target_profiles(changed_paths)
    if not profiles:
        return False
    if not re.fullmatch(r"[0-9a-f]{40}", str(base_ref)):
        return False

    root = Path(repository_root).resolve()
    if not _pr_safe_repo_ref_is_ancestor(root, base_ref, head_ref):
        return False
    for profile in profiles:
        (
            _target_id,
            base_content_ref_sha,
            _helper_path,
            _test_path,
            base_sha256_by_path,
            target_sha256_by_path,
            target_paths,
        ) = profile
        if set(base_sha256_by_path) != target_paths:
            continue
        if not _pr_safe_repo_ref_is_ancestor(root, base_content_ref_sha, base_ref):
            continue
        exact_profile = True
        for path in sorted(target_paths):
            base_blob = _pr_safe_repo_blob(root, base_ref, path)
            target_blob = _pr_safe_repo_blob(root, head_ref, path)
            expected_base_sha = base_sha256_by_path[path]
            expected_target_sha = target_sha256_by_path[path]
            if expected_base_sha is None:
                if (
                    base_blob is not None
                    or _pr_safe_repo_blob_mode(root, base_ref, path) is not None
                ):
                    exact_profile = False
                    break
            elif (
                base_blob is None
                or canonical_blob_sha256(base_blob) != expected_base_sha
                or _pr_safe_repo_blob_mode(root, base_ref, path) != "100644"
            ):
                exact_profile = False
                break
            if (
                target_blob is None
                or canonical_blob_sha256(target_blob) != expected_target_sha
                or _pr_safe_repo_blob_mode(root, head_ref, path) != "100644"
            ):
                exact_profile = False
                break
        identity_contract = daily_runtime_integration_regressions_identity_contract(
            _target_id
        )
        if exact_profile and identity_contract is not None:
            base_raw_hashes, target_raw_hashes, modes, object_types = identity_contract
            if set(modes) != target_paths:
                exact_profile = False
            elif set(object_types) != target_paths:
                exact_profile = False
            elif any(
                modes[path] != "100644" or object_types[path] != "blob"
                for path in target_paths
            ):
                exact_profile = False
            elif base_raw_hashes is not None and (
                set(base_raw_hashes) != target_paths
                or set(target_raw_hashes or {}) != target_paths
                or any(
                    hashlib.sha256(
                        _pr_safe_repo_blob(root, base_ref, path) or b""
                    ).hexdigest()
                    != base_raw_hashes[path]
                    or hashlib.sha256(
                        _pr_safe_repo_blob(root, head_ref, path) or b""
                    ).hexdigest()
                    != (target_raw_hashes or {})[path]
                    for path in target_paths
                )
            ):
                exact_profile = False
            elif not _pr_safe_repo_exact_modified_paths(
                root,
                base_ref,
                head_ref,
                target_paths,
            ):
                exact_profile = False
        if exact_profile:
            return True
    return False


def validate_daily_runtime_integration_regressions_audit_metadata(
    target_id: str | None,
    *,
    repository: str,
    base_repository: str,
    head_repository: str,
    run_attempt: str,
    pull_request_number: str,
) -> list[str]:
    if target_id not in {
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_ID,
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_ID,
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_ID,
    }:
        return []
    errors: list[str] = []
    expected_repository = PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_REPOSITORY
    if repository != expected_repository:
        errors.append("daily runtime integration target repository mismatch")
    if base_repository != expected_repository:
        errors.append("daily runtime integration target base repository mismatch")
    if head_repository != expected_repository:
        errors.append("daily runtime integration target head repository mismatch")
    if run_attempt != str(
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_RUN_ATTEMPT
    ):
        errors.append("daily runtime integration target run_attempt mismatch")
    if pull_request_number != str(
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PULL_REQUEST_NUMBER
    ):
        errors.append("daily runtime integration target pull request mismatch")
    return errors


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
    immutable_changes = sorted(changed_paths & PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS)
    if immutable_changes:
        errors.append(
            "PR may not modify the base-owned PR-safe trust root: "
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
        errors.append("preauthorized PR-safe helper/test blobs must all exist")
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
            "PR-safe helper migration must change exactly the preauthorized paths: "
            + "; or ".join(
                ", ".join(sorted(paths))
                for paths in (
                    PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
                    PR_SAFE_AUTHORIZED_STAGE1_PATHS,
                    PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
                )
            )
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
        if row.get("migration_id", "").strip()
        == migration_id
    ]
    if len(matching) != 1:
        errors.append(
            "base authorization ledger must contain exactly one matching PR-safe migration"
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
        errors.append("PR-safe migration authorization status is not preauthorized")
    if not authorization.get("approval_reference", "").strip():
        errors.append("PR-safe migration authorization lacks approval_reference")
    if observed_paths != authorized_paths:
        errors.append("PR-safe migration authorization changed_paths mismatch")
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
            errors.append("PR-safe migration was already consumed by the base helper")
        if marker not in current_helper:
            errors.append("PR-safe migration id is absent from the current helper")
    elif migration_id == PR_SAFE_SNAPSHOT_MIGRATION_ID:
        snapshot_expected = {
            "base_helper_sha256": PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256,
            "current_helper_sha256": PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256,
            "current_test_sha256": PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256,
        }
        for field, expected_sha in snapshot_expected.items():
            if expected[field] != expected_sha:
                errors.append(f"snapshot preauthorization pinned {field} mismatch")
        if base_test is None:
            errors.append("snapshot preauthorization base test blob must exist")
        elif canonical_blob_sha256(base_test) != PR_SAFE_SNAPSHOT_BASE_TEST_SHA256:
            errors.append("snapshot preauthorization pinned base_test_sha256 mismatch")
    elif migration_id in {
        PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID,
        PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID,
        PR_SAFE_REVENUE_PROMOTION_PREPARATION_V2_TARGET_ID,
        PR_SAFE_REVENUE_PROMOTION_PREPARATION_TARGET_ID,
    }:
        target_profile = pr_safe_revenue_forward_holdout_target_profile(
            authorized_paths,
            target_id=migration_id,
        )
        if target_profile is None:
            errors.append("revenue forward-holdout target profile is missing")
            return errors
        _, _, target_helper, target_test, base_hashes, target_hashes, _ = target_profile
        target_expected = {
            "base_helper_sha256": base_hashes[target_helper],
            "current_helper_sha256": target_hashes[target_helper],
            "current_test_sha256": target_hashes[target_test],
        }
        for field, expected_sha in target_expected.items():
            if expected[field] != expected_sha:
                errors.append(f"revenue forward-holdout target pinned {field} mismatch")
    elif migration_id in {
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V3_TARGET_ID,
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_V2_TARGET_ID,
        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_TARGET_ID,
        PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID,
        PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID,
        PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V2_TARGET_ID,
        PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V3_TARGET_ID,
        PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_V4_TARGET_ID,
    }:
        target_profile = pr_safe_daily_authority_containment_target_profile(
            authorized_paths,
            target_id=migration_id,
        )
        if target_profile is None:
            errors.append("daily authority containment target profile is missing")
            return errors
        _, _, target_helper, target_test, base_hashes, target_hashes, _ = target_profile
        target_expected = {
            "base_helper_sha256": base_hashes[target_helper],
            "current_helper_sha256": target_hashes[target_helper],
            "current_test_sha256": target_hashes[target_test],
        }
        for field, expected_sha in target_expected.items():
            if expected[field] != expected_sha:
                errors.append(f"daily runtime target pinned {field} mismatch")
    else:
        errors.append(f"unsupported PR-safe migration id: {migration_id}")
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


def parse_git_name_status_z(payload: bytes) -> tuple[set[str], list[str]]:
    fields = payload.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    paths: set[str] = set()
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
            else:
                paths.add(path)
        index += path_count
    return paths, errors


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


def validate_pr_safe_regular_blob_modes(
    base_sha: str,
    head_sha: str,
) -> list[str]:
    errors: list[str] = []
    protected_paths = (
        PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS | PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS
    )
    for ref_label, ref in (("base", base_sha), ("head", head_sha)):
        for path in sorted(protected_paths):
            try:
                entry = git_tree_entry_at_ref(ref, path)
            except RuntimeError as exc:
                errors.append(str(exc))
                continue
            if entry is None:
                errors.append(
                    f"PR-safe protected path is missing from {ref_label}: {path}"
                )
                continue
            mode, object_type, _object_id, observed_path = entry
            if (
                observed_path != path
                or object_type != "blob"
                or mode not in PR_SAFE_REGULAR_BLOB_MODES
            ):
                errors.append(
                    "PR-safe protected path must remain a regular blob: "
                    f"ref={ref_label} path={path} mode={mode} type={object_type} "
                    f"observed_path={observed_path}"
                )
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


def validate_pr_safe_control_plane_migration(
    base_sha: str,
    head_sha: str,
    *,
    repository: str = "",
    base_repository: str = "",
    head_repository: str = "",
    run_attempt: str = "",
    pull_request_number: str = "",
) -> list[str]:
    errors: list[str] = []
    is_replay_target = False
    is_local_replay_target = False
    is_revenue_forward_holdout_target = False
    revenue_forward_holdout_target_profile = None
    is_daily_authority_containment_target = False
    daily_authority_containment_target_profile = None
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base_sha):
        return [f"invalid base SHA: {base_sha!r}"]
    if not re.fullmatch(r"[0-9a-fA-F]{40}", head_sha):
        return [f"invalid head SHA: {head_sha!r}"]
    try:
        checkout_sha = git_output_bytes("rev-parse", "HEAD").decode().strip()
        if checkout_sha.lower() != base_sha.lower():
            errors.append(
                "base-owned guard checkout does not match pull request base SHA: "
                f"checkout={checkout_sha} base={base_sha}"
            )
        diff_payload = git_output_bytes(
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            "--find-copies",
            "--diff-filter=ACDMRT",
            f"{base_sha}...{head_sha}",
            "--",
        )
        changed_paths, diff_errors = parse_git_name_status_z(diff_payload)
        errors.extend(diff_errors)
        is_replay_target = (
            changed_paths == PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
        )
        is_local_replay_target = (
            changed_paths == PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
        )
        is_revenue_forward_holdout_target = bool(
            pr_safe_revenue_forward_holdout_target_profiles(changed_paths)
        )
        revenue_forward_holdout_target_profile = (
            preauthorized_revenue_forward_holdout_target_profile(
                base_sha,
                changed_paths,
                repository_root=ROOT,
                head_ref=head_sha,
            )
        )
        contract = pr_safe_migration_contract_for_paths(
            changed_paths,
            target_id=(
                revenue_forward_holdout_target_profile[0]
                if revenue_forward_holdout_target_profile is not None
                else None
            ),
        )
        daily_authority_containment_target_profile = (
            pr_safe_daily_authority_containment_target_profile(changed_paths)
        )
        is_daily_authority_containment_target = (
            daily_authority_containment_target_profile is not None
        )
        if (
            contract is None
            and not is_replay_target
            and not is_local_replay_target
            and not is_revenue_forward_holdout_target
        ):
            errors.append(
                "PR-safe audit requires exactly the preauthorized changed paths: "
                + "; or ".join(
                    ", ".join(sorted(paths))
                    for paths in (
                        PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS,
                        PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS,
                        PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS,
                        PR_SAFE_REVENUE_PROMOTION_PREPARATION_PATHS,
                        PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS,
                        PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
                        PR_SAFE_AUTHORIZED_STAGE1_PATHS,
                        PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
                        PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS,
                        PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS,
                        PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_PATHS,
                    )
                )
            )
            contract = (
                PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID,
                PR_SAFE_ADVANCED_HELPER,
                PR_SAFE_ADVANCED_TEST,
                PR_SAFE_AUTHORIZED_STAGE1_PATHS,
            )
        authorization_payload = git_blob_at_ref(base_sha, PR_SAFE_AUTHORIZATION_PATH)
        lifecycle_authorization_payload = git_blob_at_ref(
            base_sha,
            PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
        )
    except (OSError, RuntimeError) as exc:
        return [*errors, f"cannot load base-owned PR-safe evidence: {exc}"]

    errors.extend(
        validate_daily_runtime_integration_regressions_audit_metadata(
            (
                daily_authority_containment_target_profile[0]
                if daily_authority_containment_target_profile is not None
                else None
            ),
            repository=repository,
            base_repository=base_repository,
            head_repository=head_repository,
            run_attempt=run_attempt,
            pull_request_number=pull_request_number,
        )
    )

    errors.extend(validate_pr_safe_regular_blob_modes(base_sha, head_sha))
    errors.extend(
        validate_pr_safe_exact_migration_blob_modes(changed_paths, base_sha, head_sha)
    )
    if authorization_payload is None:
        errors.append("base-owned PR-safe authorization ledger is missing")
        authorization_payload = b""
    elif is_replay_target or is_local_replay_target:
        _rows, authorization_errors = parse_pr_safe_authorizations(
            authorization_payload
        )
        errors.extend(authorization_errors)
    if lifecycle_authorization_payload is None:
        errors.append("base-owned lifecycle authorization ledger is missing")
    else:
        _rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_authorization_payload
        )
        errors.extend(lifecycle_errors)

    if is_replay_target or is_local_replay_target:
        strict_surfaces = (
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
            if is_local_replay_target
            else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES
        )
        if not is_preauthorized_daily_full_checkpoint_replay_migration(
            base_sha,
            changed_paths,
            strict_surfaces,
            repository_root=ROOT,
            head_ref=head_sha,
        ):
            errors.append(
                "base-owned audit rejected the exact validation replay target"
            )
    elif contract is not None:
        errors.extend(
            validate_pr_safe_control_plane_delta(
                changed_paths,
                base_helper=git_blob_at_ref(base_sha, contract[1]),
                base_test=git_blob_at_ref(base_sha, contract[2]),
                current_helper=git_blob_at_ref(head_sha, contract[1]),
                current_test=git_blob_at_ref(head_sha, contract[2]),
                authorization_payload=authorization_payload,
                changed_workflow_blobs={
                    path: git_blob_at_ref(head_sha, path)
                    for path in changed_paths
                    if path.startswith(".github/workflows/")
                    and Path(path).suffix in {".yml", ".yaml"}
                },
                target_id=(
                    revenue_forward_holdout_target_profile[0]
                    if revenue_forward_holdout_target_profile is not None
                    else None
                ),
            )
        )
    if (
        is_revenue_forward_holdout_target
        and revenue_forward_holdout_target_profile is None
    ):
        errors.append(
            "base-owned audit rejected the exact revenue forward-holdout target"
        )
    if contract is not None and not (is_replay_target or is_local_replay_target):
        if (
            is_daily_authority_containment_target
            and not is_preauthorized_daily_authority_containment_target(
                base_sha,
                changed_paths,
                repository_root=ROOT,
                head_ref=head_sha,
            )
        ):
            errors.append(
                "base-owned audit rejected the exact daily authority containment target"
            )
        if contract[0] == PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID:
            errors.extend(
                validate_pr_safe_advanced_lifecycle_inventory_delta(
                    git_blob_at_ref(
                        base_sha,
                        PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY,
                    ),
                    git_blob_at_ref(
                        head_sha,
                        PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY,
                    ),
                )
            )
        elif contract[0] == PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID:
            errors.extend(
                validate_pr_safe_input_bound_lifecycle_inventory_delta(
                    git_blob_at_ref(
                        base_sha,
                        PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY,
                    ),
                    git_blob_at_ref(
                        head_sha,
                        PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY,
                    ),
                )
            )
    return errors


def _positive_integer(value: str, label: str, errors: list[str]) -> int | None:
    if not re.fullmatch(r"[1-9][0-9]*", value):
        errors.append(f"audit metadata {label} must be a positive integer")
        return None
    return int(value)


def _pr_safe_blob_evidence(ref: str, path: str) -> dict[str, str | None]:
    entry = git_tree_entry_at_ref(ref, path)
    payload = git_blob_at_ref(ref, path)
    if entry is None or payload is None:
        return {
            "path": path,
            "mode": None,
            "object_type": None,
            "object_id": None,
            "raw_sha256": None,
            "canonical_sha256": None,
        }
    mode, object_type, object_id, observed_path = entry
    return {
        "path": observed_path,
        "mode": mode,
        "object_type": object_type,
        "object_id": object_id,
        "raw_sha256": hashlib.sha256(payload).hexdigest(),
        "canonical_sha256": canonical_blob_sha256(payload),
    }


def build_pr_safe_audit_manifest(
    *,
    base_sha: str,
    head_sha: str,
    validation_errors: list[str],
    repository: str,
    workflow_ref: str,
    workflow_sha: str,
    run_id: str,
    run_attempt: str,
    event_name: str,
    event_action: str,
    base_ref: str,
    base_repository: str,
    head_repository: str,
    pull_request_number: str,
) -> dict[str, object]:
    errors = list(validation_errors)
    if repository != PR_SAFE_REPOSITORY:
        errors.append(
            f"audit metadata repository mismatch: {repository!r}"
        )
    if event_name != "pull_request_target":
        errors.append(
            f"audit metadata event_name must be pull_request_target: {event_name!r}"
        )
    if event_action not in PR_SAFE_ALLOWED_EVENT_ACTIONS:
        errors.append(f"audit metadata event_action is not allowed: {event_action!r}")
    if base_ref != "main":
        errors.append(f"audit metadata base_ref must be main: {base_ref!r}")
    if base_repository != PR_SAFE_REPOSITORY:
        errors.append(
            f"audit metadata base_repository mismatch: {base_repository!r}"
        )
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", head_repository):
        errors.append(
            f"audit metadata head_repository is malformed: {head_repository!r}"
        )
    if workflow_ref != PR_SAFE_EXPECTED_WORKFLOW_REF:
        errors.append(
            "audit metadata workflow_ref must identify the exact main workflow ref"
        )
    if workflow_sha.lower() != base_sha.lower():
        errors.append(
            "audit metadata workflow_sha must equal the pull request base SHA"
        )
    parsed_run_id = _positive_integer(run_id, "run_id", errors)
    parsed_run_attempt = _positive_integer(run_attempt, "run_attempt", errors)
    if parsed_run_attempt is not None and parsed_run_attempt != 1:
        errors.append("audit metadata run_attempt must be 1; reruns are not eligible")
    parsed_pr_number = _positive_integer(
        pull_request_number,
        "pull_request_number",
        errors,
    )

    changed_paths: set[str] = set()
    is_replay_target = False
    is_local_replay_target = False
    is_revenue_forward_holdout_target = False
    revenue_forward_holdout_target_profile = None
    is_daily_authority_containment_target = False
    daily_authority_containment_target_profile = None
    migration_contract: tuple[str, str, str, frozenset[str]] | None = None
    try:
        diff_payload = git_output_bytes(
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            "--find-copies",
            "--diff-filter=ACDMRT",
            f"{base_sha}...{head_sha}",
            "--",
        )
        changed_paths, diff_errors = parse_git_name_status_z(diff_payload)
        errors.extend(diff_errors)
        is_replay_target = (
            changed_paths == PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
        )
        is_local_replay_target = (
            changed_paths == PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
        )
        is_revenue_forward_holdout_target = bool(
            pr_safe_revenue_forward_holdout_target_profiles(changed_paths)
        )
        revenue_forward_holdout_target_profile = (
            preauthorized_revenue_forward_holdout_target_profile(
                base_sha,
                changed_paths,
                repository_root=ROOT,
                head_ref=head_sha,
            )
        )
        migration_contract = pr_safe_migration_contract_for_paths(
            changed_paths,
            target_id=(
                revenue_forward_holdout_target_profile[0]
                if revenue_forward_holdout_target_profile is not None
                else None
            ),
        )
        daily_authority_containment_target_profile = (
            pr_safe_daily_authority_containment_target_profile(changed_paths)
        )
        is_daily_authority_containment_target = (
            daily_authority_containment_target_profile is not None
        )
        errors.extend(
            validate_daily_runtime_integration_regressions_audit_metadata(
                (
                    daily_authority_containment_target_profile[0]
                    if daily_authority_containment_target_profile is not None
                    else None
                ),
                repository=repository,
                base_repository=base_repository,
                head_repository=head_repository,
                run_attempt=run_attempt,
                pull_request_number=pull_request_number,
            )
        )
        if (
            migration_contract is None
            and not is_replay_target
            and not is_local_replay_target
            and not is_revenue_forward_holdout_target
        ):
            errors.append(
                "audit manifest changed paths do not match the exact preauthorization"
            )
        checkout_sha = git_output_bytes("rev-parse", "HEAD").decode().strip()
    except (OSError, RuntimeError, UnicodeError) as exc:
        errors.append(f"cannot collect audit Git evidence: {exc}")
        checkout_sha = ""

    authorization_payload = git_blob_at_ref(base_sha, PR_SAFE_AUTHORIZATION_PATH)
    lifecycle_payload = git_blob_at_ref(
        base_sha,
        PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
    )
    authorization_rows: list[dict[str, str]] = []
    lifecycle_rows: list[dict[str, str]] = []
    if authorization_payload is not None:
        authorization_rows, authorization_errors = parse_pr_safe_authorizations(
            authorization_payload
        )
        errors.extend(authorization_errors)
    if lifecycle_payload is not None:
        lifecycle_rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_payload
        )
        errors.extend(lifecycle_errors)

    replay_target_verified = False
    if is_replay_target or is_local_replay_target:
        strict_surfaces = (
            PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
            if is_local_replay_target
            else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES
        )
        replay_target_verified = (
            is_preauthorized_daily_full_checkpoint_replay_migration(
                base_sha,
                changed_paths,
                strict_surfaces,
                repository_root=ROOT,
                head_ref=head_sha,
            )
        )
        if not replay_target_verified:
            errors.append(
                "audit manifest validation replay target failed exact base-owned preauthorization"
            )

    revenue_forward_holdout_target_verified = False
    if is_revenue_forward_holdout_target:
        revenue_forward_holdout_target_verified = (
            revenue_forward_holdout_target_profile is not None
        )
        if not revenue_forward_holdout_target_verified:
            errors.append(
                "audit manifest revenue forward-holdout target failed exact base-owned preauthorization"
            )

    daily_authority_containment_target_verified = False
    if is_daily_authority_containment_target:
        daily_authority_containment_target_verified = (
            is_preauthorized_daily_authority_containment_target(
                base_sha,
                changed_paths,
                repository_root=ROOT,
                head_ref=head_sha,
            )
        )
        if not daily_authority_containment_target_verified:
            errors.append(
                "audit manifest daily authority containment target failed exact base-owned preauthorization"
            )
    daily_runtime_identity_contract = (
        daily_runtime_integration_regressions_identity_contract(
            daily_authority_containment_target_profile[0]
        )
        if daily_authority_containment_target_profile is not None
        else None
    )

    migration_id = (
        migration_contract[0]
        if migration_contract is not None
        else PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID
        if is_local_replay_target
        else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_ID
        if is_replay_target
        else ""
    )
    matching_authorizations = [
        row
        for row in authorization_rows
        if row.get("migration_id", "").strip()
        == migration_id
    ]
    migration = matching_authorizations[0] if len(matching_authorizations) == 1 else {}
    authorized_paths = (
        PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
        if is_local_replay_target
        else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
        if is_replay_target
        else migration_contract[3]
        if migration_contract is not None
        else frozenset()
    )
    protected_blobs = {
        path: {
            "base": _pr_safe_blob_evidence(base_sha, path),
            "head": _pr_safe_blob_evidence(head_sha, path),
        }
        for path in sorted(
            PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS
            | PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS
            | authorized_paths
        )
    }
    unique_errors = list(dict.fromkeys(errors))
    return {
        "schema_version": PR_SAFE_AUDIT_MANIFEST_SCHEMA_VERSION,
        "audit_mode": PR_SAFE_AUDIT_MODE,
        "trust_identity_claimed": False,
        "required_context_used": False,
        "workflow_path": PR_SAFE_BASE_GUARD_WORKFLOW,
        "repository": repository,
        "workflow_ref": workflow_ref,
        "workflow_sha": workflow_sha.lower(),
        "event_name": event_name,
        "event_action": event_action,
        "base_ref": base_ref,
        "base_repository": base_repository,
        "head_repository": head_repository,
        "run_id": parsed_run_id,
        "run_attempt": parsed_run_attempt,
        "pull_request_number": parsed_pr_number,
        "base_sha": base_sha.lower(),
        "head_sha": head_sha.lower(),
        "checkout_sha": checkout_sha.lower(),
        "changed_paths": sorted(changed_paths),
        "changed_path_allowlist": sorted(authorized_paths),
        "changed_paths_match_allowlist": changed_paths == authorized_paths,
        "manual_gate_eligible": not unique_errors
        and changed_paths == authorized_paths,
        "preauthorization": {
            "path": PR_SAFE_AUTHORIZATION_PATH,
            "canonical_sha256": (
                canonical_blob_sha256(authorization_payload)
                if authorization_payload is not None
                else None
            ),
            "migration": migration,
        },
        "exact_research_target_preauthorization": {
            "target_id": (
                revenue_forward_holdout_target_profile[0]
                if revenue_forward_holdout_target_profile is not None
                else None
            ),
            "base_content_ref_sha": (
                revenue_forward_holdout_target_profile[1]
                if revenue_forward_holdout_target_profile is not None
                else None
            ),
            "base_sha256_by_path": (
                revenue_forward_holdout_target_profile[4]
                if revenue_forward_holdout_target_profile is not None
                else {}
            ),
            "target_sha256_by_path": (
                revenue_forward_holdout_target_profile[5]
                if revenue_forward_holdout_target_profile is not None
                else {}
            ),
            "verified": revenue_forward_holdout_target_verified,
        },
        "daily_authority_containment_target_preauthorization": {
            "target_id": (
                daily_authority_containment_target_profile[0]
                if daily_authority_containment_target_profile is not None
                else None
            ),
            "base_content_ref_sha": (
                daily_authority_containment_target_profile[1]
                if daily_authority_containment_target_profile is not None
                else None
            ),
            "base_sha256_by_path": (
                daily_authority_containment_target_profile[4]
                if daily_authority_containment_target_profile is not None
                else {}
            ),
            "target_sha256_by_path": (
                daily_authority_containment_target_profile[5]
                if daily_authority_containment_target_profile is not None
                else {}
            ),
            "base_raw_sha256_by_path": (
                daily_runtime_identity_contract[0]
                if daily_runtime_identity_contract is not None
                else {}
            ),
            "target_raw_sha256_by_path": (
                daily_runtime_identity_contract[1]
                if daily_runtime_identity_contract is not None
                else {}
            ),
            "mode_by_path": (
                daily_runtime_identity_contract[2]
                if daily_runtime_identity_contract is not None
                else {}
            ),
            "object_type_by_path": (
                daily_runtime_identity_contract[3]
                if daily_runtime_identity_contract is not None
                else {}
            ),
            "verified": daily_authority_containment_target_verified,
        },
        "replay_target_preauthorization": {
            "target_id": (
                PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID
                if is_local_replay_target
                else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_ID
                if is_replay_target
                else None
            ),
            "strict_surfaces": (
                sorted(PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES)
                if is_local_replay_target
                else sorted(PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES)
                if is_replay_target
                else []
            ),
            "base_sha256_by_path": (
                PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH
                if is_local_replay_target
                else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH
                if is_replay_target
                else {}
            ),
            "target_sha256_by_path": (
                PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_SHA256_BY_PATH
                if is_local_replay_target
                else PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH
                if is_replay_target
                else {}
            ),
            "verified": replay_target_verified,
        },
        "lifecycle_preauthorization": {
            "path": PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
            "canonical_sha256": (
                canonical_blob_sha256(lifecycle_payload)
                if lifecycle_payload is not None
                else None
            ),
            "migrations": lifecycle_rows,
        },
        "protected_blobs": protected_blobs,
        "validation": {
            "passed": not unique_errors,
            "errors": unique_errors,
        },
    }


def write_pr_safe_audit_manifest(
    manifest: dict[str, object],
    destination: Path,
) -> str:
    payload = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()


def validate_pr_safe_base_guard_repository_invariants(
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    try:
        authorization_payload = (ROOT / PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    except OSError as exc:
        errors.append(f"cannot read PR-safe authorization ledger: {exc}")
    else:
        authorization_rows, authorization_errors = parse_pr_safe_authorizations(
            authorization_payload
        )
        errors.extend(authorization_errors)
        errors.extend(validate_pr_safe_authorization_history(authorization_rows))

    try:
        lifecycle_payload = (ROOT / PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH).read_bytes()
    except OSError as exc:
        errors.append(f"cannot read lifecycle authorization ledger: {exc}")
    else:
        _rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_payload
        )
        errors.extend(lifecycle_errors)

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
        "--validate-pr-safe-control-plane-migration",
        action="store_true",
    )
    parser.add_argument("--base-sha", default="")
    parser.add_argument("--head-sha", default="")
    parser.add_argument("--audit-manifest", default="")
    parser.add_argument("--repository", default="")
    parser.add_argument("--workflow-ref", default="")
    parser.add_argument("--workflow-sha", default="")
    parser.add_argument("--run-id", default="")
    parser.add_argument("--run-attempt", default="")
    parser.add_argument("--event-name", default="")
    parser.add_argument("--event-action", default="")
    parser.add_argument("--base-ref", default="")
    parser.add_argument("--base-repository", default="")
    parser.add_argument("--head-repository", default="")
    parser.add_argument("--pull-request-number", default="")
    args = parser.parse_args(argv or [])
    if args.validate_pr_safe_control_plane_migration:
        errors = validate_pr_safe_control_plane_migration(
            args.base_sha.strip(),
            args.head_sha.strip(),
            repository=args.repository.strip(),
            base_repository=args.base_repository.strip(),
            head_repository=args.head_repository.strip(),
            run_attempt=args.run_attempt.strip(),
            pull_request_number=args.pull_request_number.strip(),
        )
        if args.audit_manifest:
            manifest = build_pr_safe_audit_manifest(
                base_sha=args.base_sha.strip(),
                head_sha=args.head_sha.strip(),
                validation_errors=errors,
                repository=args.repository.strip(),
                workflow_ref=args.workflow_ref.strip(),
                workflow_sha=args.workflow_sha.strip(),
                run_id=args.run_id.strip(),
                run_attempt=args.run_attempt.strip(),
                event_name=args.event_name.strip(),
                event_action=args.event_action.strip(),
                base_ref=args.base_ref.strip(),
                base_repository=args.base_repository.strip(),
                head_repository=args.head_repository.strip(),
                pull_request_number=args.pull_request_number.strip(),
            )
            errors = list(manifest["validation"]["errors"])
            manifest_path = Path(args.audit_manifest).resolve()
            manifest_sha256 = write_pr_safe_audit_manifest(manifest, manifest_path)
            print(f"audit_manifest={manifest_path}")
            print(f"audit_manifest_sha256={manifest_sha256}")
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("base-owned PR-safe control-plane audit validation passed")
        print(f"audit_mode={PR_SAFE_AUDIT_MODE}")
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
