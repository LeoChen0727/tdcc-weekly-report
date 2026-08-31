from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
import statistics
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Mapping, Sequence

from validate_revenue_unreacted_range_anomaly_dispositions import (
    validate_bundle as validate_current_anomaly_dispositions,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DECISION = ROOT / "config/revenue_unreacted_range_promotion_preparation_registry.csv"
DEFAULT_ANOMALIES = ROOT / "config/revenue_unreacted_range_anomaly_disposition_registry.csv"
DEFAULT_ANOMALIES_V2 = ROOT / (
    "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
)
DEFAULT_MIGRATIONS = ROOT / (
    "config/revenue_unreacted_range_promotion_preparation_migrations.csv"
)
DEFAULT_FORWARD_HOLDOUT_V2_MANIFEST = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv"
)
DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS = {
    "manifest": DEFAULT_FORWARD_HOLDOUT_V2_MANIFEST,
    "detail": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_event_detail_latest.csv",
    "summary": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_maturity_status_latest.csv",
    "comparison": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_comparison_latest.csv",
    "anomaly": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_anomaly_sensitivity_latest.csv",
    "manifest_history": ROOT
    / "output/history/research/revenue_unreacted_range_forward_holdout_v2_manifest.csv",
    "detail_history": ROOT
    / "output/history/research/revenue_unreacted_range_forward_holdout_v2_event_detail.csv",
    "summary_history": ROOT
    / "output/history/research/"
    "revenue_unreacted_range_forward_holdout_v2_maturity_status.csv",
    "comparison_history": ROOT
    / "output/history/research/revenue_unreacted_range_forward_holdout_v2_comparison.csv",
    "anomaly_history": ROOT
    / "output/history/research/"
    "revenue_unreacted_range_forward_holdout_v2_anomaly_sensitivity.csv",
    "source_manifest": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
    "source_detail": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_replay_source_detail_latest.csv",
}
FORWARD_HOLDOUT_V2_VALIDATOR = (
    ROOT / "scripts/validate_revenue_unreacted_range_forward_holdout_v2.py"
)
DEFAULT_OPERATION_READINESS = ROOT / "output/latest/model_operation_readiness_latest.csv"
MODEL_OPERATION_READINESS_VALIDATOR = ROOT / "scripts/validate_model_operation_readiness.py"
DAILY_PDF_CONSUMER_VALIDATOR = ROOT / "scripts/validate_daily_pdf_contract_consumers.py"
FORMAL_ADAPTER_PDF_CONSUMER_VALIDATOR = (
    ROOT / "scripts/validate_revenue_unreacted_range_pdf_consumer_contract.py"
)
FORMAL_ADAPTER_MODULE = (
    ROOT / "scripts/build_daily_revenue_unreacted_range_operation_section.py"
)
FORMAL_ADAPTER_VALIDATOR = (
    ROOT / "scripts/validate_daily_revenue_unreacted_range_operation_section.py"
)
FORMAL_ADAPTER_ARTIFACT = (
    ROOT / "output/latest/daily_revenue_unreacted_range_operation_section_latest.csv"
)
FORMAL_ADAPTER_HISTORY_DIRECTORY = ROOT / "output/history/daily_model_snapshots"
FORMAL_ADAPTER_MODULE_ID = "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
FORMAL_ADAPTER_ARTIFACT_ID = "daily_revenue_unreacted_range_operation_section"
FORMAL_ADAPTER_SCHEMA_VERSION = "revenue_unreacted_range_operation_section_schema_v2"
FORMAL_ADAPTER_LIFECYCLE_VERSION = "revenue_unreacted_range_lifecycle_v2"
FORMAL_ADAPTER_APPROVAL_VERSION = (
    "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
)
FORMAL_ADAPTER_APPROVAL_STATUS = "provisional_backtest_supported_oos_unconfirmed"
FORMAL_ADAPTER_OPERATION_MODULE_STATUS = (
    "approved_operation_v2_provisional_backtest_supported_oos_unconfirmed"
)
FORMAL_ADAPTER_REQUIRED_SECTIONS = {
    "active_operation",
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
}
FORMAL_ADAPTER_READINESS_COLUMNS = {
    "model_id",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
    "approval_status",
    "approval_version",
    "operation_module_status",
    "operation_module_id",
    "operation_module_path",
    "operation_module_canonical_sha256",
    "daily_adapter_status",
    "adapter_artifact_id",
    "adapter_artifact_version",
    "adapter_artifact_path",
    "adapter_artifact_canonical_sha256",
    "adapter_schema_version",
    "lifecycle_contract_version",
    "daily_adapter_sections",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
}
VALIDATION_PHASES = ("research-only", "promotion-candidate", "production-pdf")
DEFAULT_SUMMARY = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
)
DEFAULT_DETAIL = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv"
)
TRUSTED_V1_SOURCE_REVISION = "b7ab7b6122b422e941efa3a3a1a915fbfcb59f4d"
TRUSTED_V1_SOURCE_ARTIFACTS = {
    DEFAULT_SUMMARY: {
        "path": "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
        "blob": "39acbd8261038ce76a71a51e13864046d5334f00",
        "bytes": 54481,
        "sha256": "f4cc336bb3aaf5997913544472c9bbac9e591af72a4957f63ba884e26f384ad8",
    },
    DEFAULT_DETAIL: {
        "path": "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
        "blob": "b7f5f313fb98d5b34ff2714c2f5ccb99e97326c7",
        "bytes": 1005708,
        "sha256": "dee8e7e43d13786657ac0b8997fde606df36cf591463e325de36dada5373757c",
    },
}
TRUSTED_V2_SOURCE_REVISION = "8b72df7090536a49258b7d27192585c3f4b4f75d"
TRUSTED_V2_SOURCE_ARTIFACTS = {
    DEFAULT_SUMMARY: {
        "path": "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
        "blob": "a3343c5fcf163eda469ee2423d32e6372da14b91",
        "bytes": 54494,
        "sha256": "1268f4bfe825a30ea876cc9eac20800d21802d1fbd212b91ab4829f70752e281",
    },
    DEFAULT_DETAIL: {
        "path": "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
        "blob": "656ad7ac399bb93090bb478733c9c0baa1ed6f64",
        "bytes": 1012187,
        "sha256": "0d272c9263b60816cace92f8ed790a1b376cad7952c7ad13a689961cd45920ad",
    },
}

ROOT_CHECK_COLUMNS = (
    "identity_non_overlap_status",
    "formal_operation_replay_status",
    "pit_calendar_continuity_status",
    "raw_source_lineage_status",
    "units_formula_adjustment_status",
    "authoritative_event_history_status",
    "independent_source_corroboration_status",
    "reproducible_evidence_reference_status",
)

EXPECTED_DECISION = {
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_20260812",
    "decision_date": "2026-08-12",
    "model_id": "revenue_unreacted_range",
    "source_artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
    "source_artifact_version": "low_mid_falling_candidate_v1_20260720",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v2_20260812",
    "rule_spec_id": "revenue_unreacted_range_source_mid_falling_d30_v1",
    "rule_formula_canonical": "anchor=revenue_available;revenue_rule=(latest_revenue_yoy_pct>=30 OR cumulative_revenue_yoy_pct>=20) OR ((period_ordinal(revenue_period)-period_ordinal(previous_revenue_period))=1 AND latest_revenue_yoy_pct>=15 AND previous_latest_revenue_yoy_pct>=15);position_window=exactly_120_prior_adjusted_sessions_excluding_anchor;position_rule=40<position_120d_pct<=75;shape_rule=shape_return20_pct<-5_and_shape_ema23_slope5_pct<0;source_to_trigger_trading_days=0..60;trigger_rule=analysis_close_crosses_above_prior20_analysis_close_high_and_ma60>ma120;confirmation_rule=D+1_analysis_close>trigger_analysis_close;entry_rule=D+2_analysis_open;exit_rule=D+30_analysis_close_offset29;stop_rule=none_no_stop_reference",
    "rule_formula_sha256": "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633",
    "data_contract_sha256": "4aff77863a07ba5fe7c574731ea84ac778b85daffbbfe7123d38cccd4cc61432",
    "producer_semantic_sha256": "0ed8a7240a9abe10e89b70e462390c5c3a7245ee013e37e88d1323374d072000",
    "source_first_producer_semantic_sha256": "2ffc0a9206a1088621561183b748804b490658b46f4a21b7fffe58ef7e88be39",
    "rearmed_producer_semantic_sha256": "1613efe9a464e70f4dc5db3ba7d9ec251d4d73dccbf020ecf7b73b562e77f9af",
    "position_shape_producer_semantic_sha256": "b164724d153fe0f132372f533765b83ac1e72955052a17fa8d408f1657ca1f00",
    "monthly_revenue_history_blob_sha256": "84424e2ce456a0334268b54851d8a395f0cf3826fa755d0e589b2a797005d84e",
    "monthly_revenue_canonical_table_sha256": "89df0f3a5d19facb9169970450108b0bb32d0b41548d1a834fa4055bbe323e21",
    "cross_market_resolution_registry_canonical_sha256": "a109e7e2f041f7fa116a5d123dfc4b4bd24f508ece7b2e9721e44c293a608fdb",
    "source_first_selected_slice_canonical_sha256": "8a2e7185ba96eea9391070769aa5d1e25f540a79563779cc2812214b0000570e",
    "rearmed_d30_no_stop_slice_canonical_sha256": "c652900f843fe16a53ba1f0fec28a5905eebd30b77686943ff368ded2d37ea04",
    "price_history_manifest_canonical_sha256": "eae2b08620c2af42adc3147f820859d69c35fd1f7e5af8ece7df9707f6b624f7",
    "detail_artifact_canonical_sha256": "e5e0148f7ea8bb60c146b26d83d756464f555766ce87de0151c41ca8d988557b",
    "source_first_canonical_row_set_sha256": "1bb445ae703310c5b016ff88ce5b74e425cd3e7163a5d978080c820afbf222b5",
    "rearmed_operation_canonical_row_set_sha256": "9cd604699e3a5c7f32076f1199e1ff42071f5892ea0ddb341b49e048a97b146d",
    "price_history_canonical_set_sha256": "8ddf1fe9ec0d34bc908f95b3c78cae4d2b94024abc9f2ac9c4664e1c93bd6f9e",
    "candidate_detail_row_set_sha256": "fd5be1bf8c44d3c0144d044c5485558faf09fef2ae6ec3e2d755bef29227c987",
    "source_variant_id": "absolute_or_two_month_yoy_ge15",
    "revenue_rule": "(latest_revenue_yoy_pct>=30 OR cumulative_revenue_yoy_pct>=20) OR ((period_ordinal(revenue_period)-period_ordinal(previous_revenue_period))=1 AND latest_revenue_yoy_pct>=15 AND previous_latest_revenue_yoy_pct>=15)",
    "analysis_basis": "primary_candidate_retaining",
    "lifecycle_policy_id": "rearm_after_realized_exit_next_trade_day",
    "confirmation_variant_id": "delayed_next_close_continuation_bonus",
    "candidate_variant_id": "source_mid_falling",
    "candidate_member_column": "mid_falling_member",
    "source_anchor_id": "revenue_available",
    "position_window_policy": "exactly_120_prior_adjusted_sessions_excluding_anchor",
    "position_rule": "40<position_120d_pct<=75",
    "source_position_bucket": "mid_pos_40_75",
    "shape_rule": "shape_return20_pct<-5_and_shape_ema23_slope5_pct<0",
    "source_shape_bucket": "falling",
    "source_to_trigger_trading_day_min": "0",
    "source_to_trigger_trading_day_max": "60",
    "trigger_rule": "analysis_close_crosses_above_prior20_analysis_close_high_and_ma60>ma120",
    "confirmation_rule": "D+1_analysis_close>trigger_analysis_close",
    "entry_rule": "D+2_analysis_open",
    "exit_rule": "D+30_analysis_close_offset29",
    "holding_days": "30",
    "holding_session_index_offset": "29",
    "holding_session_contract": "inclusive_entry_session_count_30_exit_offset_29",
    "confirmation_offset_trading_days": "1",
    "entry_offset_trading_days": "2",
    "entry_price_basis": "analysis_open",
    "exit_price_basis": "fixed_future_close",
    "stop_policy_id": "none_no_stop_reference",
    "same_stock_non_overlap_policy": "same_stock_entry_after_prior_realized_exit",
    "anomaly_policy": "primary_retains_all_anomaly_candidates_candidate_exclusion_is_sensitivity_only",
    "financial_statement_scope": "monthly_revenue_only_EPS_gross_margin_operating_margin_operating_income_non_operating_income_net_income_excluded",
    "operation_count": "52", "unique_stock_count": "47", "unique_episode_count": "47",
    "win_count": "41", "neutral_count": "0", "failure_count": "11",
    "win_rate_pct": "78.8462", "neutral_rate_pct": "0.0", "failure_rate_pct": "21.1538",
    "avg_return_pct": "15.8235", "median_return_pct": "10.9837",
    "p10_return_pct": "-10.8794", "p90_return_pct": "42.41",
    "min_return_pct": "-19.6694", "max_return_pct": "82.5095",
    "return_ge20_count": "19", "return_ge20_rate_pct": "36.5385",
    "return_le_minus20_count": "0", "return_le_minus20_rate_pct": "0.0",
    "source_anomaly_candidate_count": "7", "unresolved_price_path_candidate_count": "0",
    "operation_return_review_candidate_count": "1", "combined_exclusion_candidate_count": "8",
    "same_stock_overlap_pair_count": "0", "forward_holdout_gate_policy": "monitoring_non_hard_gate",
    "forward_holdout_first_interpretation_min_mature": "20",
    "user_decision_reference": "user_decision_20260812",
    "same_model_variant_policy": "source_low_falling_and_low_mid_union_are_challenger_variants_not_distinct_models",
    "decision_status": "selected_pending_anomaly_resolution_and_formal_adapter",
    "anomaly_disposition_gate": "blocked_pending_8_root_cause_dispositions",
    "formal_adapter_gate": "not_started_hard_gate",
    "approved_for_daily": "False", "presentation_allowed": "False",
    "formal_model_use_allowed": "False", "production_change": "False",
    "promotion_scope": "promotion_preparation_only_no_production_pdf_or_apps_script",
}
EXPECTED_DECISION_V1 = EXPECTED_DECISION
EXPECTED_DECISION_V2 = {
    **EXPECTED_DECISION_V1,
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_v2_20260828",
    "decision_date": "2026-08-28",
    "source_artifact_version": "low_mid_falling_candidate_v2_20260822",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v3_20260828",
    "producer_semantic_sha256": "98c661dbb761aad0f36feb88c3da395abe2908f922b95536a546d336c877f7e1",
    "rearmed_producer_semantic_sha256": "d13176cc5309875db771d8840aeedc0c2e7b8f69ef6ebf53772b87ed7931e70b",
    "position_shape_producer_semantic_sha256": "0cfea3d0f02371e727b2903a1cb5dccb19750d0073daaaea72e4f0a4f7635952",
    "monthly_revenue_history_blob_sha256": "f5b94f1aba6554746bb8065d3c9e571df6934aabc80ecfff4ec7193bcb7ec36a",
    "source_first_selected_slice_canonical_sha256": "b590a10b791e7f239b189beba7b8c61f7294b3ce0ba9bd404d49b45844d760f3",
    "rearmed_d30_no_stop_slice_canonical_sha256": "490b8567e54de61e66c92eafb1df8dbc6865de51785cbb6335b94239f1c473a5",
    "price_history_manifest_canonical_sha256": "3ca2bc672afd57171db031505ad088f4813f92eb76c94bb62cee515f41d70463",
    "detail_artifact_canonical_sha256": "5e446585d3f409c7e1a80df6162663c132a081f5d0bb9e923cee5dd4413327ab",
    "source_first_canonical_row_set_sha256": "6ab55882856b3d835e14892bb02b2b32ba30e9027ec2337482cdb6a24ac9b9c3",
    "rearmed_operation_canonical_row_set_sha256": "27e82f73b0536f1314265d8f74fb78266d86775e5d4584d76ddaa5d4a0190fcc",
    "price_history_canonical_set_sha256": "68b63607532f97ba52c6480e63ff5941082372ce367720bcdf785d862a8b0717",
    "candidate_detail_row_set_sha256": "d597ced885cd997c1a6942336150013aaa01ae918dcddf3b968c0ec2b9c12fcb",
    "operation_count": "53",
    "unique_stock_count": "48",
    "unique_episode_count": "48",
    "win_count": "41",
    "neutral_count": "0",
    "failure_count": "12",
    "win_rate_pct": "77.3585",
    "neutral_rate_pct": "0.0",
    "failure_rate_pct": "22.6415",
    "avg_return_pct": "14.895",
    "median_return_pct": "9.4077",
    "p10_return_pct": "-11.04",
    "p90_return_pct": "42.2669",
    "min_return_pct": "-19.6694",
    "max_return_pct": "82.5095",
    "return_ge20_count": "19",
    "return_ge20_rate_pct": "35.8491",
    "return_le_minus20_count": "0",
    "return_le_minus20_rate_pct": "0.0",
    "source_anomaly_candidate_count": "8",
    "unresolved_price_path_candidate_count": "0",
    "operation_return_review_candidate_count": "1",
    "combined_exclusion_candidate_count": "9",
    "user_decision_reference": "user_authorized_2A_20260828",
    "decision_status": "selected_pending_anomaly_resolution_forward_holdout_v2_maturity_and_formal_adapter",
    "anomaly_disposition_gate": "blocked_pending_9_root_cause_dispositions_and_1_trigger_asof_attribution_reconciliation",
    "promotion_scope": "promotion_preparation_v2_migration_only_no_production_pdf_or_apps_script",
}
EXPECTED_DECISION_V3 = {
    **EXPECTED_DECISION_V2,
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_v3_20260828",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v4_20260828",
    "forward_holdout_gate_policy": "research_and_disabled_adapter_preparation_non_hard_promotion_candidate_and_production_approval_hard_gate",
    "user_decision_reference": "user_authorized_3A_3C_20260828",
    "decision_status": "research_complete_promotion_blocked_waiting_anomaly_forward_holdout_and_formal_adapter",
    "anomaly_disposition_gate": "research_non_hard_promotion_candidate_hard_pending_9_root_cause_dispositions",
    "formal_adapter_gate": "disabled_adapter_preparation_non_hard_production_approval_hard_gate",
    "promotion_scope": "staged_contract_research_only_and_disabled_adapter_preparation_no_production_daily_full_pdf_or_apps_script",
}
EXPECTED_DECISION_V4 = {
    **EXPECTED_DECISION_V3,
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_v4_20260829",
    "decision_date": "2026-08-29",
    "source_artifact_version": "low_mid_falling_candidate_v3_20260829",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v5_20260829",
    "producer_semantic_sha256": "6939dc6d88cf0248a5bffad9cc98a96b3165f76165e60b8f0558a59e16690d39",
    "source_first_producer_semantic_sha256": "032df33eeffdd8a2414c318d4ab523be63a2f0863ce0a5f0e725ef94def6d108",
    "rearmed_producer_semantic_sha256": "a00cc4b4437a8929782a4e82bbbdaf3bb20e43404a9afa4cda8184a8e80e044e",
    "position_shape_producer_semantic_sha256": "4ff586a9a67d3f3322a0e87b182feb800aa0cbf4aca0c56a1b84e34a212b44ab",
    "monthly_revenue_history_blob_sha256": "f5b94f1aba6554746bb8065d3c9e571df6934aabc80ecfff4ec7193bcb7ec36a",
    "source_first_selected_slice_canonical_sha256": "defeb9490c7b119d47b42481ba1b85f879e257c4db10d749989ba734afa0ff11",
    "rearmed_d30_no_stop_slice_canonical_sha256": "1029abdfd0bfe4c24d6ada1de1d10c824d7e3ade1bb06ed25939bd59fe4cdba5",
    "price_history_manifest_canonical_sha256": "3ca2bc672afd57171db031505ad088f4813f92eb76c94bb62cee515f41d70463",
    "detail_artifact_canonical_sha256": "24d9900c956273ba72c5f9f2d3e2b77be3bea201c4f2996b9e4ea782d67e2b3a",
    "source_first_canonical_row_set_sha256": "5d4ca1a2ca35cf714e40cda1af0d7298800d41b08e27489a2a413b52467ce716",
    "rearmed_operation_canonical_row_set_sha256": "7cbc5d31f7f25fbef289c789d40cb4918822f70cb0f8f61d6f8897cb900a0c46",
    "price_history_canonical_set_sha256": "68b63607532f97ba52c6480e63ff5941082372ce367720bcdf785d862a8b0717",
    "candidate_detail_row_set_sha256": "f91dd55cab602224011fc68b65dcb4e7dfb59b7720fb1cce0941941234c78c93",
    "source_anomaly_candidate_count": "7",
    "operation_return_review_candidate_count": "1",
    "combined_exclusion_candidate_count": "8",
    "user_decision_reference": "user_authorized_3A_3C_20260829",
    "decision_status": "anomaly_disposition_complete_promotion_blocked_waiting_forward_holdout_and_formal_adapter",
    "anomaly_disposition_gate": "verified_8_real_extreme_1_data_error_repaired_effective_blockers_0",
    "formal_adapter_gate": "disabled_adapter_preparation_non_hard_production_approval_hard_gate",
    "promotion_scope": "research_only_anomaly_disposition_closed_waiting_forward_holdout_and_disabled_adapter_no_production_daily_full_pdf_or_apps_script",
}
EXPECTED_DECISION_V5 = {
    **EXPECTED_DECISION_V4,
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_v5_20260829",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v6_20260829",
    "decision_status": "promotion_blocked_waiting_forward_holdout_v2_maturity",
    "anomaly_disposition_gate": "verified_8_real_extreme_1_data_error_repaired_effective_blockers_0",
    "formal_adapter_gate": "disabled_adapter_preparation_validated_non_hard_production_approval_hard_gate",
    "approved_for_daily": "False",
    "presentation_allowed": "False",
    "formal_model_use_allowed": "False",
    "production_change": "False",
    "promotion_scope": "research_only_anomaly_closed_disabled_adapter_preparation_validated_waiting_forward_holdout_v2_maturity_no_production_daily_full_pdf_packet_runtime_artifact_or_apps_script",
}
EXPECTED_DECISION_V6 = {
    **EXPECTED_DECISION_V5,
    "decision_id": "revenue_unreacted_range_source_mid_falling_promotion_preparation_v6_20260830",
    "decision_date": "2026-08-30",
    "contract_version": "revenue_unreacted_range_promotion_preparation_contract_v7_20260830",
    "forward_holdout_gate_policy": "post_launch_monitoring_non_hard_no_tuning",
    "user_decision_reference": "user_authorized_4A_4C_20260830",
    "decision_status": "provisional_backtest_supported_oos_unconfirmed",
    "formal_adapter_gate": "formal_adapter_v2_approved_production_hard_gate_satisfied",
    "approved_for_daily": "True",
    "presentation_allowed": "True",
    "formal_model_use_allowed": "True",
    "production_change": "True",
    "promotion_scope": "provisional_production_daily_full_pdf_enabled_forward_holdout_post_launch_monitoring_no_tuning_apps_script_forbidden_legacy_selector_retired_code_retained_pending_dependency_audit",
}
EXPECTED_DECISIONS = (
    EXPECTED_DECISION_V1,
    EXPECTED_DECISION_V2,
    EXPECTED_DECISION_V3,
    EXPECTED_DECISION_V4,
    EXPECTED_DECISION_V5,
    EXPECTED_DECISION_V6,
)
DECISION_COLUMNS = tuple(EXPECTED_DECISION)
V4_TO_V5_ALLOWED_CHANGED_DECISION_FIELDS = frozenset(
    {
        "decision_id",
        "contract_version",
        "decision_status",
        "formal_adapter_gate",
        "promotion_scope",
    }
)
V4_TO_V5_COMMON_DECISION_FIELDS = tuple(
    column
    for column in DECISION_COLUMNS
    if column not in V4_TO_V5_ALLOWED_CHANGED_DECISION_FIELDS
)
V5_TO_V6_ALLOWED_CHANGED_DECISION_FIELDS = frozenset(
    {
        "decision_id",
        "decision_date",
        "contract_version",
        "forward_holdout_gate_policy",
        "user_decision_reference",
        "decision_status",
        "formal_adapter_gate",
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
        "promotion_scope",
    }
)
V5_TO_V6_FROZEN_BUSINESS_FIELDS = tuple(
    column
    for column in DECISION_COLUMNS
    if column not in V5_TO_V6_ALLOWED_CHANGED_DECISION_FIELDS
)

ANOMALY_COLUMNS = (
    "model_id",
    "operation_key",
    "candidate_detail_row_sha256",
    "candidate_kind",
    "anomaly_attribution_mode",
    "anomaly_source_event_periods",
    "anomaly_source_available_dates",
    "anomaly_source_canonical_row_sha256s",
    "anomaly_source_raw_file_sha256s",
    "anomaly_attribution_note",
    "stock_id",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "realized_return_pct",
    *ROOT_CHECK_COLUMNS,
    "final_disposition",
    "primary_handling",
    "promotion_gate_status",
    "evidence_reference",
    "approved_reason_reference",
    "reviewed_at",
)

EXPECTED_ANOMALIES = {
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2408|absolute_or_two_month_yoy_ge15|2408|20260417|2|20260427|20260429": ("dd3f9e0e3a98f1d19d7bafa2f6a26107401ad50194410f6043f7d33bb745932e", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202603", "20260417", "aeec5b0f201473cc8c1760527f46596a0af3c756a2d3396679eb7f72246ee356", "bd571ae41f02b7214bdf33f0ec0046dbd882cf04637d20c623cbed5fb8986be4", "exact anomalous qualifying monthly-revenue event known by trigger", "2408", "20260427", "20260428", "20260429", "20260610", "41.1017"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2451|absolute_or_two_month_yoy_ge15|2451|20251217|2|20260313|20260317": ("339e08fab18293b366138668a8e5598f919c915a93d0dd99a39d2092d135cfba", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202601", "20260217", "535dfa06caf2e73a1afba4cbaae0e731bdecf5a1377de6d0f619535ccd533fc1", "7b31102b97d450fa4de777477198f8655447cf3037993e8fc50f6fc40de30a50", "exact anomalous qualifying monthly-revenue event known by trigger", "2451", "20260313", "20260316", "20260317", "20260429", "1.5152"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2478|absolute_or_two_month_yoy_ge15|2478|20260217|2|20260416|20260420": ("301defe6487ff208f73e169fb65b280940682a1194ef5c36da1b5759bf0fc84c", "operation_return_review_candidate", "operation_return_review_not_source_attributed", "not_applicable", "not_applicable", "not_applicable", "not_applicable", "operation-return magnitude review is not a monthly-revenue source anomaly attribution", "2478", "20260416", "20260417", "20260420", "20260601", "82.5095"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2527|absolute_or_two_month_yoy_ge15|2527|20260517|1|20260526|20260528": ("4dedbef9a790f22aedb1de28329158f3f248ab00ee303e78492a30081b5fcf85", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202604", "20260517", "047b94ab8b2e136f27ad1ac45f8259b25f852cfbc64b2f6f80eb02eae2926abc", "07c771646a550e5831176efac2067f2ea9436c8cb1700dbe5900b8d86e7d0769", "exact anomalous qualifying monthly-revenue event known by trigger", "2527", "20260526", "20260527", "20260528", "20260709", "17.3554"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20251128|20251202": ("6823ad385a0246f94e1ad7dd74d43769147b5d0b81ea047cb1c4488504f728ca", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202509|202510", "20251017|20251117", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203|cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", "6bb7ac7c837884520e1aae63cd2d12ba2f2da7a88117d9308e39fab94842426e|8f8dc5a3c5ec13150f027cb47b6c80f5661e649f16d0632aeedfdd588f8cb817", "two exact anomalous qualifying events known by trigger in the shared episode", "3535", "20251128", "20251201", "20251202", "20260114", "-2.6287"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20260119|20260121": ("0d422492d733ad369e247e222299e39c6e34b068ee3cc80ef29559c2d8188d1b", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202509|202510", "20251017|20251117", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203|cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", "6bb7ac7c837884520e1aae63cd2d12ba2f2da7a88117d9308e39fab94842426e|8f8dc5a3c5ec13150f027cb47b6c80f5661e649f16d0632aeedfdd588f8cb817", "two exact anomalous qualifying events known by trigger in the shared episode", "3535", "20260119", "20260120", "20260121", "20260313", "11.5044"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|4142|absolute_or_two_month_yoy_ge15|4142|20250617|1|20260109|20260113": ("9636feedf298a97e39226731f29160d9d5db9f2fc3dab9d3e01839482d4125c1", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202511", "20251217", "6200122b66aa1cfc523f215276d07af291f0aac27cab819e3964d3038473f45a", "d5470ceb0bc50ca464c5bc06d03bd5e0bdc02d4112bb3cc813f9e9517e466925", "exact anomalous qualifying monthly-revenue event known by trigger", "4142", "20260109", "20260112", "20260113", "20260305", "-12.9584"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|5484|absolute_or_two_month_yoy_ge15|5484|20251017|1|20260515|20260519": ("1bfa169064788747a18ac6a8a0297cbc46b43dac9fa33a6fc0774760f4cf1bd6", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202512", "20260117", "e91f324a5d4c664bf1ca2e329f094212294de006eec1b3395cec5b7b4ff8324c", "d30e0dab4891bc9fc8d8416b911a0b04d2e9d167a8411dc0794de6f6a414eabc", "exact anomalous qualifying event not the latest 202603 source available by trigger", "5484", "20260515", "20260518", "20260519", "20260630", "13.3995"),
}
EXPECTED_ANOMALIES_V1 = EXPECTED_ANOMALIES
EXPECTED_ANOMALIES_V2 = {
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2408|absolute_or_two_month_yoy_ge15|2408|20260417|2|20260427|20260429": ("8642cd7286a0eee22ba76d69e6ab826c9ec22c3e83a3ed63fef27753e81f0168", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202603", "20260417", "aeec5b0f201473cc8c1760527f46596a0af3c756a2d3396679eb7f72246ee356", "bd571ae41f02b7214bdf33f0ec0046dbd882cf04637d20c623cbed5fb8986be4", "exact anomalous qualifying monthly-revenue event known by trigger", "2408", "20260427", "20260428", "20260429", "20260610", "41.1017"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2451|absolute_or_two_month_yoy_ge15|2451|20250517|1|20260313|20260317": ("e5eed6f2f6d39d9da369041116395383580ef98274e7490bcaadc6a23a22d20e", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202601", "20260217", "535dfa06caf2e73a1afba4cbaae0e731bdecf5a1377de6d0f619535ccd533fc1", "7b31102b97d450fa4de777477198f8655447cf3037993e8fc50f6fc40de30a50", "exact anomalous qualifying monthly-revenue event known by trigger", "2451", "20260313", "20260316", "20260317", "20260429", "1.5152"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2478|absolute_or_two_month_yoy_ge15|2478|20260217|2|20260416|20260420": ("facf4234439f7b5627a00b3bfa82c2976559357c218b0a341ca0a5a0e2d53a9b", "operation_return_review_candidate", "operation_return_review_not_source_attributed", "not_applicable", "not_applicable", "not_applicable", "not_applicable", "operation-return magnitude review is not a monthly-revenue source anomaly attribution", "2478", "20260416", "20260417", "20260420", "20260601", "82.5095"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2527|absolute_or_two_month_yoy_ge15|2527|20260517|1|20260526|20260528": ("34d2b8aa9258ae1a686feaa937ada66e56c238c7dd5994299b4a3c74ee5d8c6a", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202604", "20260517", "047b94ab8b2e136f27ad1ac45f8259b25f852cfbc64b2f6f80eb02eae2926abc", "07c771646a550e5831176efac2067f2ea9436c8cb1700dbe5900b8d86e7d0769", "exact anomalous qualifying monthly-revenue event known by trigger", "2527", "20260526", "20260527", "20260528", "20260709", "17.3554"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20251128|20251202": ("f7ed7ce96221e2754d299f73ee1025763d7d8b858b19232c18a4e3b21032c5c2", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202509|202510", "20251017|20251117", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203|cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", "6bb7ac7c837884520e1aae63cd2d12ba2f2da7a88117d9308e39fab94842426e|8f8dc5a3c5ec13150f027cb47b6c80f5661e649f16d0632aeedfdd588f8cb817", "two exact anomalous qualifying events known by trigger in the shared episode", "3535", "20251128", "20251201", "20251202", "20260114", "-2.6287"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20260119|20260121": ("e4b00d986b4af400e6cc05ce38687964f7de9944914d77eb31fc0a9755a64596", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202509|202510", "20251017|20251117", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203|cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", "6bb7ac7c837884520e1aae63cd2d12ba2f2da7a88117d9308e39fab94842426e|8f8dc5a3c5ec13150f027cb47b6c80f5661e649f16d0632aeedfdd588f8cb817", "two exact anomalous qualifying events known by trigger in the shared episode", "3535", "20260119", "20260120", "20260121", "20260313", "11.5044"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|4142|absolute_or_two_month_yoy_ge15|4142|20250617|1|20260109|20260113": ("2f36fb8d8e6bd05b879a164e5748d318088ebc6936d1d97dc9a9cd728c0bc35b", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202511", "20251217", "6200122b66aa1cfc523f215276d07af291f0aac27cab819e3964d3038473f45a", "d5470ceb0bc50ca464c5bc06d03bd5e0bdc02d4112bb3cc813f9e9517e466925", "exact anomalous qualifying monthly-revenue event known by trigger", "4142", "20260109", "20260112", "20260113", "20260305", "-12.9584"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|5484|absolute_or_two_month_yoy_ge15|5484|20251017|1|20260515|20260519": ("5f3ca72b872eeb3f02e078e9544b456751e6dc2c4fc7942a7a023c961a6ce514", "source_anomaly_candidate", "exact_anomaly_causing_qualifying_source_events", "202512", "20260117", "e91f324a5d4c664bf1ca2e329f094212294de006eec1b3395cec5b7b4ff8324c", "d30e0dab4891bc9fc8d8416b911a0b04d2e9d167a8411dc0794de6f6a414eabc", "exact anomalous qualifying event not the latest 202603 source available by trigger", "5484", "20260515", "20260518", "20260519", "20260630", "13.3995"),
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|6177|absolute_or_two_month_yoy_ge15|6177|20250517|1|20251204|20251208": ("e3ff0aa0f2af328e8e959321235acc79af9efdf0a7df508db4d55bac57b88e23", "source_anomaly_candidate", "published_episode_level_source_flag_no_trigger_asof_event_requires_reconciliation", "not_applicable_pending_trigger_asof_reconciliation", "not_applicable_pending_trigger_asof_reconciliation", "not_applicable_pending_trigger_asof_reconciliation", "not_applicable_pending_trigger_asof_reconciliation", "published episode-level flag is future-contaminated: no anomalous qualifying source event was known by trigger; first such event period 202512 available 20260117 canonical d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1 is post-trigger and not attribution evidence", "6177", "20251204", "20251205", "20251208", "20260120", "5.274"),
}

DISPOSITION_POLICIES = {
    "unresolved_anomaly_candidate": (
        "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only",
        "blocked_pending_root_cause",
    ),
    "verified_real_extreme": (
        "retain_in_primary_metrics",
        "eligible_only_after_all_other_model_gates",
    ),
    "verified_data_error": (
        "repair_source_and_rerun_old_metrics_forbidden",
        "blocked_until_repaired_rerun",
    ),
    "verified_non_comparable": (
        "exclude_only_with_approved_reason_and_rerun",
        "requires_model_governance_review",
    ),
}
IMMUTABLE_EVIDENCE_RE = re.compile(
    r"^evidence_id=(?P<evidence_id>[a-z0-9][a-z0-9_.-]*);"
    r"path=(?P<path>[^;\r\n]+);"
    r"sha256=(?P<sha256>[0-9a-f]{64})$"
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_IMMUTABLE_EVIDENCE_ROOTS = (
    PurePosixPath("docs/evidence/revenue_unreacted_range"),
    PurePosixPath("data/revenue_unreacted_range/evidence"),
)

SUMMARY_EXPECTED = {
    "model_id": "revenue_unreacted_range",
    "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
    "artifact_version": "low_mid_falling_candidate_v1_20260720",
    **{
        column: EXPECTED_DECISION[column]
        for column in (
            "data_contract_sha256",
            "producer_semantic_sha256",
            "source_first_producer_semantic_sha256",
            "rearmed_producer_semantic_sha256",
            "position_shape_producer_semantic_sha256",
            "monthly_revenue_canonical_table_sha256",
            "cross_market_resolution_registry_canonical_sha256",
            "source_first_selected_slice_canonical_sha256",
            "rearmed_d30_no_stop_slice_canonical_sha256",
            "price_history_manifest_canonical_sha256",
            "detail_artifact_canonical_sha256",
            "source_first_canonical_row_set_sha256",
            "rearmed_operation_canonical_row_set_sha256",
            "price_history_canonical_set_sha256",
            "candidate_detail_row_set_sha256",
        )
    },
    "source_variant_id": EXPECTED_DECISION["source_variant_id"],
    "analysis_basis": EXPECTED_DECISION["analysis_basis"],
    "lifecycle_policy_id": EXPECTED_DECISION["lifecycle_policy_id"],
    "confirmation_variant_id": EXPECTED_DECISION["confirmation_variant_id"],
    "candidate_variant_id": EXPECTED_DECISION["candidate_variant_id"],
    "candidate_member_column": EXPECTED_DECISION["candidate_member_column"],
    "holding_days": "30",
    "stop_policy_id": EXPECTED_DECISION["stop_policy_id"],
    "operation_count": "52",
    "unique_stock_count": "47",
    "unique_episode_count": "47",
    "win_count": "41",
    "neutral_count": "0",
    "failure_count": "11",
    "win_rate_pct": "78.8462",
    "neutral_rate_pct": "0.0",
    "failure_rate_pct": "21.1538",
    "avg_return_pct": "15.8235",
    "median_return_pct": "10.9837",
    "p10_return_pct": "-10.8794",
    "p90_return_pct": "42.41",
    "min_return_pct": "-19.6694",
    "max_return_pct": "82.5095",
    "return_ge20_count": "19",
    "return_ge20_rate_pct": "36.5385",
    "return_le_minus20_count": "0",
    "return_le_minus20_rate_pct": "0.0",
    "source_anomaly_candidate_count": "7",
    "unresolved_price_path_candidate_count": "0",
    "operation_return_review_candidate_count": "1",
    "combined_exclusion_candidate_count": "8",
    "same_stock_overlap_pair_count": "0",
    "approved_for_daily": "False",
    "presentation_allowed": "False",
    "formal_model_use_allowed": "False",
    "production_change": "False",
}
SUMMARY_EXPECTED_V1 = SUMMARY_EXPECTED
SUMMARY_EXPECTED_V2 = {
    **SUMMARY_EXPECTED_V1,
    "artifact_version": "low_mid_falling_candidate_v2_20260822",
    **{
        column: EXPECTED_DECISION_V2[column]
        for column in (
            "data_contract_sha256",
            "producer_semantic_sha256",
            "source_first_producer_semantic_sha256",
            "rearmed_producer_semantic_sha256",
            "position_shape_producer_semantic_sha256",
            "monthly_revenue_canonical_table_sha256",
            "cross_market_resolution_registry_canonical_sha256",
            "source_first_selected_slice_canonical_sha256",
            "rearmed_d30_no_stop_slice_canonical_sha256",
            "price_history_manifest_canonical_sha256",
            "detail_artifact_canonical_sha256",
            "source_first_canonical_row_set_sha256",
            "rearmed_operation_canonical_row_set_sha256",
            "price_history_canonical_set_sha256",
            "candidate_detail_row_set_sha256",
            "operation_count",
            "unique_stock_count",
            "unique_episode_count",
            "win_count",
            "neutral_count",
            "failure_count",
            "win_rate_pct",
            "neutral_rate_pct",
            "failure_rate_pct",
            "avg_return_pct",
            "median_return_pct",
            "p10_return_pct",
            "p90_return_pct",
            "min_return_pct",
            "max_return_pct",
            "return_ge20_count",
            "return_ge20_rate_pct",
            "return_le_minus20_count",
            "return_le_minus20_rate_pct",
            "source_anomaly_candidate_count",
            "unresolved_price_path_candidate_count",
            "operation_return_review_candidate_count",
            "combined_exclusion_candidate_count",
        )
    },
}
EXPECTED_MONTHLY_REVENUE_BLOB_PROVENANCE = {
    SUMMARY_EXPECTED_V1["artifact_version"]: EXPECTED_DECISION_V1[
        "monthly_revenue_history_blob_sha256"
    ],
    SUMMARY_EXPECTED_V2["artifact_version"]: EXPECTED_DECISION_V2[
        "monthly_revenue_history_blob_sha256"
    ],
}

EXPECTED_MIGRATION = {
    "migration_id": "revenue_unreacted_range_promotion_preparation_v1_to_v2_20260828",
    "migration_date": "2026-08-28",
    "model_id": "revenue_unreacted_range",
    "from_decision_id": EXPECTED_DECISION_V1["decision_id"],
    "to_decision_id": EXPECTED_DECISION_V2["decision_id"],
    "from_source_artifact_version": EXPECTED_DECISION_V1["source_artifact_version"],
    "to_source_artifact_version": EXPECTED_DECISION_V2["source_artifact_version"],
    "from_source_revision": TRUSTED_V1_SOURCE_REVISION,
    "to_source_revision": TRUSTED_V2_SOURCE_REVISION,
    "from_summary_blob_sha1": "39acbd8261038ce76a71a51e13864046d5334f00",
    "from_summary_bytes": "54481",
    "from_summary_sha256": "f4cc336bb3aaf5997913544472c9bbac9e591af72a4957f63ba884e26f384ad8",
    "from_detail_blob_sha1": "b7f5f313fb98d5b34ff2714c2f5ccb99e97326c7",
    "from_detail_bytes": "1005708",
    "from_detail_sha256": "dee8e7e43d13786657ac0b8997fde606df36cf591463e325de36dada5373757c",
    "to_summary_blob_sha1": "a3343c5fcf163eda469ee2423d32e6372da14b91",
    "to_summary_bytes": "54494",
    "to_summary_sha256": "1268f4bfe825a30ea876cc9eac20800d21802d1fbd212b91ab4829f70752e281",
    "to_detail_blob_sha1": "656ad7ac399bb93090bb478733c9c0baa1ed6f64",
    "to_detail_bytes": "1012187",
    "to_detail_sha256": "0d272c9263b60816cace92f8ed790a1b376cad7952c7ad13a689961cd45920ad",
    "source_projection_diff_summary_path": "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_summary.csv",
    "source_projection_diff_summary_sha256": "e2124dc58b95ff1e11a7add5bf671ca142b5cc1cc6b538ce57090735d56beeed",
    "source_projection_diff_detail_path": "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_detail.csv",
    "source_projection_diff_detail_sha256": "68c9cfb143a663bd86f62a356d5dd09cd38edd7e16f2cb726d1a3f4aa62ef4d6",
    "source_projection_supersede_evidence_path": "output/history/research/revenue_unreacted_range_source_snapshot_projection_supersede_evidence_v2_20260822.csv",
    "source_projection_supersede_evidence_sha256": "33a7ac67a98c0e6fd3836e8bedd250940ccadd567e71c50bb94e9cbda70ef79b",
    "v1_operation_count": "52",
    "v2_operation_count": "53",
    "exact_common_operation_key_count": "46",
    "raw_added_operation_key_count": "7",
    "raw_removed_operation_key_count": "6",
    "episode_identity_rekey_count": "2",
    "semantic_persistent_trajectory_count": "48",
    "true_added_operation_count": "5",
    "true_removed_operation_count": "4",
    "common_business_field_change_count": "0",
    "v1_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry.csv",
    "v1_anomaly_registry_sha256": "8d13efcce3feecf23231b53ec3e880cf82f72bfd4efcb9aaccc99eab18905ecc",
    "v1_anomaly_count": "8",
    "v2_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
    "v2_anomaly_registry_sha256": "172687dc6cd63ef1c65c4b4a15229e30c411647a8d81b0c483d96684d1348491",
    "v2_anomaly_count": "9",
    "authorization_reference": "user_authorized_2A_20260828",
    "migration_scope": "promotion_preparation_and_research_only_forward_holdout_v2_migration_no_production_daily_full_pdf_or_apps_script",
    "research_only": "True",
    "formal_model_use_allowed": "False",
    "approved_for_daily": "False",
    "presentation_allowed": "False",
    "production_change": "False",
}
EXPECTED_MIGRATION_V1_TO_V2 = EXPECTED_MIGRATION
EXPECTED_MIGRATION_V2_TO_V3 = {
    **EXPECTED_MIGRATION_V1_TO_V2,
    "migration_id": "revenue_unreacted_range_promotion_preparation_v2_to_v3_contract_stage_gate_20260828",
    "from_decision_id": EXPECTED_DECISION_V2["decision_id"],
    "to_decision_id": EXPECTED_DECISION_V3["decision_id"],
    "from_source_artifact_version": EXPECTED_DECISION_V2["source_artifact_version"],
    "to_source_artifact_version": EXPECTED_DECISION_V3["source_artifact_version"],
    "from_source_revision": TRUSTED_V2_SOURCE_REVISION,
    "to_source_revision": TRUSTED_V2_SOURCE_REVISION,
    "from_summary_blob_sha1": "a3343c5fcf163eda469ee2423d32e6372da14b91",
    "from_summary_bytes": "54494",
    "from_summary_sha256": "1268f4bfe825a30ea876cc9eac20800d21802d1fbd212b91ab4829f70752e281",
    "from_detail_blob_sha1": "656ad7ac399bb93090bb478733c9c0baa1ed6f64",
    "from_detail_bytes": "1012187",
    "from_detail_sha256": "0d272c9263b60816cace92f8ed790a1b376cad7952c7ad13a689961cd45920ad",
    "source_projection_diff_summary_path": "",
    "source_projection_diff_summary_sha256": "",
    "source_projection_diff_detail_path": "",
    "source_projection_diff_detail_sha256": "",
    "source_projection_supersede_evidence_path": "",
    "source_projection_supersede_evidence_sha256": "",
    "v1_operation_count": "53",
    "v2_operation_count": "53",
    "exact_common_operation_key_count": "53",
    "raw_added_operation_key_count": "0",
    "raw_removed_operation_key_count": "0",
    "episode_identity_rekey_count": "0",
    "semantic_persistent_trajectory_count": "53",
    "true_added_operation_count": "0",
    "true_removed_operation_count": "0",
    "common_business_field_change_count": "0",
    "v1_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
    "v1_anomaly_registry_sha256": "172687dc6cd63ef1c65c4b4a15229e30c411647a8d81b0c483d96684d1348491",
    "v1_anomaly_count": "9",
    "v2_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
    "v2_anomaly_registry_sha256": "172687dc6cd63ef1c65c4b4a15229e30c411647a8d81b0c483d96684d1348491",
    "v2_anomaly_count": "9",
    "authorization_reference": "user_authorized_3A_3C_20260828",
    "migration_scope": "contract_stage_gate_only_no_source_or_business_semantic_change_no_production_daily_full_pdf_or_apps_script",
}
EXPECTED_MIGRATION_V3_TO_V4 = {
    **EXPECTED_MIGRATION_V2_TO_V3,
    "migration_id": "revenue_unreacted_range_promotion_preparation_v3_to_v4_anomaly_closure_20260829",
    "migration_date": "2026-08-29",
    "from_decision_id": EXPECTED_DECISION_V3["decision_id"],
    "to_decision_id": EXPECTED_DECISION_V4["decision_id"],
    "from_source_artifact_version": EXPECTED_DECISION_V3["source_artifact_version"],
    "to_source_artifact_version": EXPECTED_DECISION_V4["source_artifact_version"],
    "from_source_revision": TRUSTED_V2_SOURCE_REVISION,
    "to_source_revision": "f9d76fe1ace0d61c303b73c42981482daeef7938",
    "from_summary_blob_sha1": "a3343c5fcf163eda469ee2423d32e6372da14b91",
    "from_summary_bytes": "54494",
    "from_summary_sha256": "1268f4bfe825a30ea876cc9eac20800d21802d1fbd212b91ab4829f70752e281",
    "from_detail_blob_sha1": "656ad7ac399bb93090bb478733c9c0baa1ed6f64",
    "from_detail_bytes": "1012187",
    "from_detail_sha256": "0d272c9263b60816cace92f8ed790a1b376cad7952c7ad13a689961cd45920ad",
    "to_summary_blob_sha1": "21d2497566e2d37eae40893282f5c2112a23ca94",
    "to_summary_bytes": "54511",
    "to_summary_sha256": "7830186063badbcafa6d80bf44f546dcf03d7ad5ee0068f352554e28f2608b64",
    "to_detail_blob_sha1": "2c742c9a6e4cd980b1aca812e386499a228ef9a5",
    "to_detail_bytes": "1012196",
    "to_detail_sha256": "7dc4f1f89a16dd77d39af175de1dfd3340059a863a670c77e0276d8ec91582d7",
    "source_projection_diff_summary_path": "output/history/research/revenue_unreacted_range_trigger_asof_anomaly_migration_validation_summary_v1_20260829.csv",
    "source_projection_diff_summary_sha256": "25c9b1a26436109c0c6611533bae0047eb11a48554fdb179880e3e3843eb93ef",
    "source_projection_diff_detail_path": "output/history/research/revenue_unreacted_range_trigger_asof_anomaly_migration_diff_detail_v1_20260829.csv",
    "source_projection_diff_detail_sha256": "34f7b14deb2e39c60d1c012e9342ac7e7f1b1315942b467737f9a2bedaab0db0",
    "source_projection_supersede_evidence_path": "output/history/research/revenue_unreacted_range_trigger_asof_anomaly_migration_manifest_v1_20260829.csv",
    "source_projection_supersede_evidence_sha256": "db2a08ba4acb4aadefe64ef95f78603d3fc3d1b1b6724daac83c45944c89ee06",
    "v1_operation_count": "53",
    "v2_operation_count": "53",
    "exact_common_operation_key_count": "53",
    "raw_added_operation_key_count": "0",
    "raw_removed_operation_key_count": "0",
    "episode_identity_rekey_count": "0",
    "semantic_persistent_trajectory_count": "53",
    "true_added_operation_count": "0",
    "true_removed_operation_count": "0",
    "common_business_field_change_count": "0",
    "v1_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv",
    "v1_anomaly_registry_sha256": "172687dc6cd63ef1c65c4b4a15229e30c411647a8d81b0c483d96684d1348491",
    "v1_anomaly_count": "9",
    "v2_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv",
    "v2_anomaly_registry_sha256": "d56fb059cb008b504cb6f64464277e5252566059512ba723668e3cd5f824d489",
    "v2_anomaly_count": "8",
    "authorization_reference": "user_authorized_3A_3C_20260829",
    "migration_scope": "anomaly_disposition_closure_and_repaired_v3_binding_no_production_daily_full_pdf_or_apps_script",
}
EXPECTED_MIGRATION_V4_TO_V5 = {
    **EXPECTED_MIGRATION_V3_TO_V4,
    "migration_id": "revenue_unreacted_range_promotion_preparation_v4_to_v5_disabled_adapter_preparation_20260829",
    "from_decision_id": EXPECTED_DECISION_V4["decision_id"],
    "to_decision_id": EXPECTED_DECISION_V5["decision_id"],
    "from_source_artifact_version": EXPECTED_DECISION_V4["source_artifact_version"],
    "to_source_artifact_version": EXPECTED_DECISION_V5["source_artifact_version"],
    "from_source_revision": "f9d76fe1ace0d61c303b73c42981482daeef7938",
    "to_source_revision": "f9d76fe1ace0d61c303b73c42981482daeef7938",
    "from_summary_blob_sha1": "21d2497566e2d37eae40893282f5c2112a23ca94",
    "from_summary_bytes": "54511",
    "from_summary_sha256": "7830186063badbcafa6d80bf44f546dcf03d7ad5ee0068f352554e28f2608b64",
    "from_detail_blob_sha1": "2c742c9a6e4cd980b1aca812e386499a228ef9a5",
    "from_detail_bytes": "1012196",
    "from_detail_sha256": "7dc4f1f89a16dd77d39af175de1dfd3340059a863a670c77e0276d8ec91582d7",
    "to_summary_blob_sha1": "21d2497566e2d37eae40893282f5c2112a23ca94",
    "to_summary_bytes": "54511",
    "to_summary_sha256": "7830186063badbcafa6d80bf44f546dcf03d7ad5ee0068f352554e28f2608b64",
    "to_detail_blob_sha1": "2c742c9a6e4cd980b1aca812e386499a228ef9a5",
    "to_detail_bytes": "1012196",
    "to_detail_sha256": "7dc4f1f89a16dd77d39af175de1dfd3340059a863a670c77e0276d8ec91582d7",
    "source_projection_diff_summary_path": "",
    "source_projection_diff_summary_sha256": "",
    "source_projection_diff_detail_path": "",
    "source_projection_diff_detail_sha256": "",
    "source_projection_supersede_evidence_path": "",
    "source_projection_supersede_evidence_sha256": "",
    "common_business_field_change_count": "0",
    "v1_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv",
    "v1_anomaly_registry_sha256": "d56fb059cb008b504cb6f64464277e5252566059512ba723668e3cd5f824d489",
    "v1_anomaly_count": "8",
    "v2_anomaly_registry_path": "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv",
    "v2_anomaly_registry_sha256": "d56fb059cb008b504cb6f64464277e5252566059512ba723668e3cd5f824d489",
    "v2_anomaly_count": "8",
    "authorization_reference": "user_authorized_3A_3C_20260829",
    "migration_scope": "disabled_adapter_preparation_validation_only_no_source_or_business_semantic_change_no_production_daily_full_pdf_packet_runtime_artifact_or_apps_script",
    "research_only": "True",
    "formal_model_use_allowed": "False",
    "approved_for_daily": "False",
    "presentation_allowed": "False",
    "production_change": "False",
}
EXPECTED_MIGRATION_V5_TO_V6 = {
    **EXPECTED_MIGRATION_V4_TO_V5,
    "migration_id": "revenue_unreacted_range_promotion_preparation_v5_to_v6_provisional_activation_20260830",
    "migration_date": "2026-08-30",
    "from_decision_id": EXPECTED_DECISION_V5["decision_id"],
    "to_decision_id": EXPECTED_DECISION_V6["decision_id"],
    "authorization_reference": "user_authorized_4A_4C_20260830",
    "migration_scope": "provisional_production_activation_formal_adapter_v2_daily_full_pdf_forward_holdout_post_launch_monitoring_no_tuning_apps_script_forbidden_no_source_or_frozen_business_semantic_change",
    "research_only": "False",
    "formal_model_use_allowed": "True",
    "approved_for_daily": "True",
    "presentation_allowed": "True",
    "production_change": "True",
}
EXPECTED_MIGRATIONS = (
    EXPECTED_MIGRATION_V1_TO_V2,
    EXPECTED_MIGRATION_V2_TO_V3,
    EXPECTED_MIGRATION_V3_TO_V4,
    EXPECTED_MIGRATION_V4_TO_V5,
    EXPECTED_MIGRATION_V5_TO_V6,
)
MIGRATION_COLUMNS = tuple(EXPECTED_MIGRATION)
MIGRATION_PROVENANCE_COLUMNS = frozenset(
    {
        "from_summary_blob_sha1",
        "from_summary_bytes",
        "from_summary_sha256",
        "from_detail_blob_sha1",
        "from_detail_bytes",
        "from_detail_sha256",
        "to_summary_blob_sha1",
        "to_summary_bytes",
        "to_summary_sha256",
        "to_detail_blob_sha1",
        "to_detail_bytes",
        "to_detail_sha256",
        "source_projection_diff_summary_sha256",
        "source_projection_diff_detail_sha256",
        "source_projection_supersede_evidence_sha256",
        "v1_anomaly_registry_sha256",
        "v2_anomaly_registry_sha256",
    }
)


def _read_csv_payload(
    payload: bytes,
    *,
    label: str,
) -> tuple[list[str], list[dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        with io.StringIO(payload.decode("utf-8-sig"), newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            columns = list(reader.fieldnames or [])
    except (UnicodeError, csv.Error) as exc:
        return [], [], [f"cannot read CSV {label}: {exc}"]
    if not rows:
        errors.append(f"CSV is empty: {label}")
    return columns, rows, errors


def _read_csv(
    path: Path,
    *,
    payload: bytes | None = None,
    label: str | None = None,
) -> tuple[list[str], list[dict[str, str]], list[str]]:
    if payload is None:
        if not path.is_file():
            return [], [], [f"missing CSV: {path}"]
        try:
            payload = path.read_bytes()
        except OSError as exc:
            return [], [], [f"cannot read CSV {path}: {exc}"]
    return _read_csv_payload(payload, label=label or str(path))


def _git(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )


def _trusted_source_blob(version: str, path: Path) -> bytes:
    if version == "v1":
        revision = TRUSTED_V1_SOURCE_REVISION
        contracts = TRUSTED_V1_SOURCE_ARTIFACTS
    elif version == "v2":
        revision = TRUSTED_V2_SOURCE_REVISION
        contracts = TRUSTED_V2_SOURCE_ARTIFACTS
    else:
        raise RuntimeError(f"unapproved trusted promotion source version: {version}")
    contract = contracts.get(Path(path))
    if contract is None:
        raise RuntimeError(f"unapproved trusted {version} promotion source path: {path}")
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise RuntimeError(f"trusted {version} promotion source revision is not a full SHA")
    commit = _git("rev-parse", "--verify", f"{revision}^{{commit}}")
    if commit.returncode != 0 or commit.stdout.decode("ascii", errors="replace").strip() != revision:
        raise RuntimeError(f"trusted {version} promotion source revision is unavailable")
    ancestor = _git("merge-base", "--is-ancestor", revision, "HEAD")
    if ancestor.returncode != 0:
        raise RuntimeError(f"trusted {version} promotion source revision is not an ancestor of HEAD")
    repo_path = str(contract["path"])
    tree = _git("ls-tree", revision, "--", repo_path)
    fields = tree.stdout.decode("utf-8", errors="replace").strip().split(None, 3)
    if (
        tree.returncode != 0
        or len(fields) != 4
        or fields[0] != "100644"
        or fields[1] != "blob"
        or fields[3] != repo_path
    ):
        raise RuntimeError(f"trusted {version} promotion source tree path mismatch: {repo_path}")
    blob = _git("cat-file", "blob", fields[2])
    if blob.returncode != 0:
        raise RuntimeError(f"trusted {version} promotion source blob is unreadable: {repo_path}")
    return blob.stdout


def _trusted_v1_source_blob(path: Path) -> bytes:
    return _trusted_source_blob("v1", path)


def _trusted_v2_source_blob(path: Path) -> bytes:
    return _trusted_source_blob("v2", path)


def _is_true(value: str) -> bool:
    return value.strip().lower() == "true"


def _is_false(value: str) -> bool:
    return value.strip().lower() == "false"


def _round4(value: float) -> float:
    return round(value + 0.0, 4)


def _linear_quantile(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _validate_immutable_evidence_reference(
    value: str,
    *,
    operation_key: str,
    field_name: str,
) -> list[str]:
    errors: list[str] = []
    match = IMMUTABLE_EVIDENCE_RE.fullmatch(value)
    if match is None:
        return [
            f"{operation_key}: {field_name} must use the structured immutable evidence reference format"
        ]

    raw_path = match.group("path")
    posix_path = PurePosixPath(raw_path)
    windows_path = PureWindowsPath(raw_path)
    if (
        posix_path.is_absolute()
        or windows_path.is_absolute()
        or "\\" in raw_path
    ):
        return [f"{operation_key}: {field_name} path must be repo-relative"]
    if any(part in {"", ".", ".."} for part in posix_path.parts):
        return [f"{operation_key}: {field_name} path must not contain dot segments"]

    root = ROOT.resolve()
    evidence_path = (root / Path(*posix_path.parts)).resolve()
    try:
        evidence_path.relative_to(root)
    except ValueError:
        return [f"{operation_key}: {field_name} path escapes the repository root"]

    allowed = False
    for allowed_relative in ALLOWED_IMMUTABLE_EVIDENCE_ROOTS:
        allowed_root = (root / Path(*allowed_relative.parts)).resolve()
        try:
            evidence_path.relative_to(allowed_root)
        except ValueError:
            continue
        allowed = evidence_path != allowed_root
        if allowed:
            break
    if not allowed:
        allowed_text = ", ".join(str(path) for path in ALLOWED_IMMUTABLE_EVIDENCE_ROOTS)
        return [
            f"{operation_key}: {field_name} path is outside the allowed model-owned evidence roots: "
            f"{allowed_text}"
        ]

    if not evidence_path.is_file():
        return [
            f"{operation_key}: {field_name} path does not resolve to an existing file: {raw_path}"
        ]
    try:
        actual_sha256 = hashlib.sha256(evidence_path.read_bytes()).hexdigest()
    except OSError as exc:
        return [f"{operation_key}: cannot read {field_name} path {raw_path}: {exc}"]
    if actual_sha256 != match.group("sha256"):
        errors.append(
            f"{operation_key}: {field_name} sha256 mismatch: "
            f"expected={match.group('sha256')}; actual={actual_sha256}"
        )
    return errors


def validate_decision(
    path: Path,
    *,
    diagnostics: list[str] | None = None,
) -> tuple[dict[str, str] | None, list[str]]:
    columns, rows, errors = _read_csv(path)
    if columns and tuple(columns) != DECISION_COLUMNS:
        errors.append("promotion preparation registry columns must match the exact contract")
    if len(rows) != len(EXPECTED_DECISIONS):
        errors.append(
            "promotion preparation registry must preserve the exact v1/v2 prefix and the "
            f"append-only v3 through v6 decision chain; actual={len(rows)}"
        )
        return None, errors
    for version, (row, expected_row) in enumerate(
        zip(rows, EXPECTED_DECISIONS, strict=True), start=1
    ):
        for column, expected in expected_row.items():
            if column == "monthly_revenue_history_blob_sha256":
                if row.get(column, "") != expected and diagnostics is not None:
                    diagnostics.append(
                        f"promotion preparation v{version} raw monthly-revenue "
                        "blob SHA differs (diagnostic only)"
                    )
                continue
            if row.get(column, "") != expected:
                errors.append(
                    f"promotion preparation {column} mismatch in v{version}: "
                    f"expected={expected!r}; actual={row.get(column, '')!r}"
                )
        formula_sha256 = hashlib.sha256(
            row.get("rule_formula_canonical", "").encode("utf-8")
        ).hexdigest()
        if formula_sha256 != row.get("rule_formula_sha256", ""):
            errors.append(
                "promotion preparation rule_formula_sha256 does not bind the canonical formula "
                f"in v{version}"
            )
    if len(rows) == len(EXPECTED_DECISIONS):
        changed_v4_v5_fields = [
            column
            for column in V4_TO_V5_COMMON_DECISION_FIELDS
            if rows[-3].get(column, "") != rows[-2].get(column, "")
        ]
        if changed_v4_v5_fields:
            errors.append(
                "promotion preparation v4-to-v5 changed frozen common decision fields: "
                f"{changed_v4_v5_fields}"
            )
        changed_v5_v6_fields = [
            column
            for column in V5_TO_V6_FROZEN_BUSINESS_FIELDS
            if rows[-2].get(column, "") != rows[-1].get(column, "")
        ]
        if changed_v5_v6_fields:
            errors.append(
                "promotion preparation v5-to-v6 changed frozen business fields: "
                f"{changed_v5_v6_fields}"
            )
    return rows[-1], errors


def validate_anomalies(
    path: Path,
    *,
    expected_anomalies: dict[str, tuple[str, ...]] = EXPECTED_ANOMALIES_V1,
    version_label: str = "v1",
    diagnostics: list[str] | None = None,
) -> tuple[dict[str, dict[str, str]], list[str]]:
    columns, rows, errors = _read_csv(path)
    if columns and tuple(columns) != ANOMALY_COLUMNS:
        errors.append("anomaly disposition registry columns must match the exact contract")
    keys = [row.get("operation_key", "") for row in rows]
    if len(keys) != len(set(keys)):
        errors.append("anomaly disposition registry has duplicate operation_key rows")
    actual = {row.get("operation_key", ""): row for row in rows}
    if set(actual) != set(expected_anomalies):
        errors.append(
            f"anomaly disposition registry {version_label} must contain the exact frozen "
            f"{len(expected_anomalies)} operation keys; "
            f"missing={sorted(set(expected_anomalies) - set(actual))}; "
            f"extra={sorted(set(actual) - set(expected_anomalies))}"
        )
    identity_columns = (
        "candidate_detail_row_sha256",
        "candidate_kind",
        "anomaly_attribution_mode",
        "anomaly_source_event_periods",
        "anomaly_source_available_dates",
        "anomaly_source_canonical_row_sha256s",
        "anomaly_source_raw_file_sha256s",
        "anomaly_attribution_note",
        "stock_id",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "realized_return_pct",
    )
    for key, expected_values in expected_anomalies.items():
        row = actual.get(key)
        if row is None:
            continue
        if row.get("model_id") != "revenue_unreacted_range":
            errors.append(f"{key}: model_id must be revenue_unreacted_range")
        for column, expected in zip(identity_columns, expected_values, strict=True):
            if column == "anomaly_source_raw_file_sha256s":
                if row.get(column, "") != expected and diagnostics is not None:
                    diagnostics.append(
                        f"{key}: {column} differs (diagnostic only); canonical "
                        "monthly-revenue row hashes remain the hard gate"
                    )
                continue
            if row.get(column, "") != expected:
                errors.append(
                    f"{key}: {column} mismatch: expected={expected!r}; actual={row.get(column, '')!r}"
                )
        disposition = row.get("final_disposition", "")
        if disposition not in DISPOSITION_POLICIES:
            errors.append(f"{key}: invalid final_disposition={disposition!r}")
        check_values = [row.get(column, "") for column in ROOT_CHECK_COLUMNS]
        if any(value not in {"pending", "pass", "fail"} for value in check_values):
            errors.append(f"{key}: every root-check status must be pending, pass, or fail")
        expected_policy = DISPOSITION_POLICIES.get(disposition)
        if expected_policy and (
            row.get("primary_handling"), row.get("promotion_gate_status")
        ) != expected_policy:
            errors.append(
                f"{key}: disposition policy mismatch for {disposition}: "
                f"expected={expected_policy}; actual="
                f"{(row.get('primary_handling'), row.get('promotion_gate_status'))}"
            )
        if disposition == "unresolved_anomaly_candidate":
            if row.get("evidence_reference", "").strip():
                errors.append(f"{key}: unresolved candidate cannot claim final evidence")
            if row.get("approved_reason_reference", "").strip():
                errors.append(f"{key}: unresolved candidate cannot claim an approved reason")
        elif disposition.startswith("verified_"):
            if set(check_values) != {"pass"}:
                errors.append(f"{key}: verified disposition requires all eight root checks to pass")
            errors.extend(
                _validate_immutable_evidence_reference(
                    row.get("evidence_reference", ""),
                    operation_key=key,
                    field_name="evidence_reference",
                )
            )
            if not row.get("reviewed_at", "").strip():
                errors.append(f"{key}: verified disposition requires reviewed_at")
            approved_reason = row.get("approved_reason_reference", "")
            if disposition == "verified_non_comparable":
                errors.extend(
                    _validate_immutable_evidence_reference(
                        approved_reason,
                        operation_key=key,
                        field_name="approved_reason_reference",
                    )
                )
            elif approved_reason.strip():
                errors.append(
                    f"{key}: approved_reason_reference is allowed only for verified_non_comparable"
                )
        attribution_mode = row.get("anomaly_attribution_mode", "")
        if attribution_mode == "exact_anomaly_causing_qualifying_source_events":
            for available_date in row.get("anomaly_source_available_dates", "").split("|"):
                if available_date and available_date > row.get("trigger_date", ""):
                    errors.append(
                        f"{key}: anomaly source available date is after trigger and cannot be attributed"
                    )
        if row.get("stock_id") == "6177" and version_label == "v2":
            placeholder = "not_applicable_pending_trigger_asof_reconciliation"
            for column in (
                "anomaly_source_event_periods",
                "anomaly_source_available_dates",
                "anomaly_source_canonical_row_sha256s",
            ):
                if row.get(column) != placeholder:
                    errors.append(
                        f"{key}: 6177 future-contaminated attribution must remain fail-closed in {column}"
                    )
            if row.get("pit_calendar_continuity_status") != "fail":
                errors.append(f"{key}: 6177 pit_calendar_continuity_status must remain fail")
            if row.get("raw_source_lineage_status") != "fail":
                errors.append(f"{key}: 6177 raw_source_lineage_status must remain fail")
    if len(rows) != len(expected_anomalies):
        errors.append(
            f"anomaly disposition registry {version_label} must contain exactly "
            f"{len(expected_anomalies)} rows; actual={len(rows)}"
        )
    return actual, errors


def validate_migration(path: Path) -> tuple[dict[str, str] | None, list[str]]:
    columns, rows, errors = _read_csv(path)
    if columns and tuple(columns) != MIGRATION_COLUMNS:
        errors.append("promotion preparation migration ledger columns must match the exact contract")
    if len(rows) != len(EXPECTED_MIGRATIONS):
        errors.append(
            "promotion preparation migration ledger must preserve the exact append-only "
            "v1-to-v2 through v5-to-v6 chain; "
            f"actual={len(rows)}"
        )
        return None, errors
    for version, (row, expected_row) in enumerate(
        zip(rows, EXPECTED_MIGRATIONS, strict=True), start=1
    ):
        for column, expected in expected_row.items():
            if column in MIGRATION_PROVENANCE_COLUMNS:
                continue
            if row.get(column, "") != expected:
                errors.append(
                    f"promotion preparation migration {column} mismatch in row {version}: "
                    f"expected={expected!r}; actual={row.get(column, '')!r}"
                )
    return rows[0], errors


def _migration_git_blob(treeish: str, repo_path: str) -> tuple[bytes | None, str | None]:
    posix_path = PurePosixPath(repo_path)
    windows_path = PureWindowsPath(repo_path)
    if (
        not repo_path
        or posix_path.is_absolute()
        or windows_path.is_absolute()
        or "\\" in repo_path
        or any(part in {"", ".", ".."} for part in posix_path.parts)
    ):
        return None, f"migration artifact path is not a safe repo-relative path: {repo_path!r}"
    spec = f":{repo_path}" if treeish == ":" else f"{treeish}:{repo_path}"
    result = _git("show", spec)
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        return None, (
            f"migration artifact Git blob is unavailable: {spec}"
            + (f"; {detail}" if detail else "")
        )
    return result.stdout, None


def validate_migration_artifact_bindings(
    row: dict[str, str],
    *,
    diagnostics: list[str] | None = None,
) -> list[str]:
    """Audit raw ledger identities while semantic validators remain hard gates.

    This is intentionally part of the explicit trusted ``--source-audit all``
    path.  Governance-only validation remains cheap and does not reach into Git,
    Raw blob SHA, byte count, and line-ending differences are diagnostics only;
    the selected rows, canonical source rows, cutoffs, and business projections
    are independently replayed below.
    """

    errors: list[str] = []
    for version, prefix, revision, contracts in (
        ("v1", "from", TRUSTED_V1_SOURCE_REVISION, TRUSTED_V1_SOURCE_ARTIFACTS),
        ("v2", "to", TRUSTED_V2_SOURCE_REVISION, TRUSTED_V2_SOURCE_ARTIFACTS),
    ):
        for artifact_name, artifact_path in (
            ("summary", DEFAULT_SUMMARY),
            ("detail", DEFAULT_DETAIL),
        ):
            contract = contracts[artifact_path]
            repo_path = str(contract["path"])
            payload, error = _migration_git_blob(revision, repo_path)
            if error is not None:
                errors.append(error)
                continue
            assert payload is not None
            observed = {
                "blob_sha1": hashlib.sha1(
                    f"blob {len(payload)}\0".encode("ascii") + payload
                ).hexdigest(),
                "bytes": str(len(payload)),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
            for suffix, actual in observed.items():
                column = f"{prefix}_{artifact_name}_{suffix}"
                if row.get(column, "") != actual:
                    if diagnostics is not None:
                        diagnostics.append(
                            f"migration {version} {artifact_name} {suffix} raw identity "
                            "differs (diagnostic only) "
                            f"to {revision}:{repo_path}; expected={actual}; "
                            f"actual={row.get(column, '')}"
                        )

    for path_column, sha_column in (
        ("source_projection_diff_summary_path", "source_projection_diff_summary_sha256"),
        ("source_projection_diff_detail_path", "source_projection_diff_detail_sha256"),
        (
            "source_projection_supersede_evidence_path",
            "source_projection_supersede_evidence_sha256",
        ),
    ):
        repo_path = row.get(path_column, "")
        revision = row.get("to_source_revision", "")
        payload, error = _migration_git_blob(revision, repo_path)
        if error is not None:
            errors.append(error)
            continue
        assert payload is not None
        actual = hashlib.sha256(payload).hexdigest()
        if row.get(sha_column, "") != actual:
            if diagnostics is not None:
                diagnostics.append(
                    f"migration {sha_column} raw identity differs (diagnostic only) "
                    f"from {revision}:{repo_path}; expected={actual}; "
                    f"actual={row.get(sha_column, '')}"
                )

    for version in ("v1", "v2"):
        path_column = f"{version}_anomaly_registry_path"
        sha_column = f"{version}_anomaly_registry_sha256"
        repo_path = row.get(path_column, "")
        payload, error = _migration_git_blob(":", repo_path)
        if error is not None:
            errors.append(error)
            continue
        assert payload is not None
        actual = hashlib.sha256(payload).hexdigest()
        if row.get(sha_column, "") != actual:
            if diagnostics is not None:
                diagnostics.append(
                    f"migration {sha_column} raw identity differs (diagnostic only) "
                    f"from current index:{repo_path}; expected={actual}; "
                    f"actual={row.get(sha_column, '')}"
                )
    return errors


def _summary_matches(
    row: dict[str, str],
    expected_summary: dict[str, str] = SUMMARY_EXPECTED_V1,
) -> bool:
    selection = {
        key: expected_summary[key]
        for key in (
            "source_variant_id",
            "analysis_basis",
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "candidate_variant_id",
            "holding_days",
            "stop_policy_id",
        )
    }
    return all(row.get(key, "") == value for key, value in selection.items())


def validate_summary(
    path: Path,
    *,
    payload: bytes | None = None,
    label: str | None = None,
    expected_summary: dict[str, str] = SUMMARY_EXPECTED_V1,
    diagnostics: list[str] | None = None,
) -> tuple[dict[str, str] | None, list[str]]:
    _columns, rows, errors = _read_csv(path, payload=payload, label=label)
    selected = [row for row in rows if _summary_matches(row, expected_summary)]
    if len(selected) != 1:
        errors.append(f"source summary must contain exactly one frozen selected slice; actual={len(selected)}")
        return None, errors
    row = selected[0]
    for column, expected in expected_summary.items():
        if row.get(column, "") != expected:
            errors.append(
                f"source summary {column} mismatch: expected={expected!r}; actual={row.get(column, '')!r}"
            )
    raw_blob_sha = row.get("monthly_revenue_history_blob_sha256", "").strip().lower()
    expected_raw_blob_sha = EXPECTED_MONTHLY_REVENUE_BLOB_PROVENANCE.get(
        expected_summary["artifact_version"], ""
    )
    if not SHA256_RE.fullmatch(raw_blob_sha):
        if diagnostics is not None:
            diagnostics.append(
                "source summary monthly_revenue_history_blob_sha256 is missing or invalid; "
                "raw mutable blob identity is provenance-only"
            )
    elif raw_blob_sha != expected_raw_blob_sha and diagnostics is not None:
        diagnostics.append(
            "source summary monthly_revenue_history_blob_sha256 differs from the captured "
            "provenance value; canonical semantic hashes and row identities remain the "
            "promotion-blocking lineage"
        )
    return row, errors


def _detail_matches(
    row: dict[str, str],
    expected_decision: dict[str, str] = EXPECTED_DECISION_V1,
) -> bool:
    return (
        row.get("source_variant_id") == expected_decision["source_variant_id"]
        and row.get("lifecycle_policy_id") == expected_decision["lifecycle_policy_id"]
        and row.get("confirmation_variant_id") == expected_decision["confirmation_variant_id"]
        and row.get("holding_days") == "30"
        and row.get("stop_policy_id") == expected_decision["stop_policy_id"]
        and _is_true(row.get("mid_falling_member", ""))
        and _is_true(row.get("primary_included", ""))
    )


def validate_detail(
    path: Path,
    anomaly_rows: dict[str, dict[str, str]],
    *,
    payload: bytes | None = None,
    label: str | None = None,
    expected_decision: dict[str, str] = EXPECTED_DECISION_V1,
    expected_summary: dict[str, str] = SUMMARY_EXPECTED_V1,
) -> tuple[list[dict[str, str]], list[str]]:
    _columns, rows, errors = _read_csv(path, payload=payload, label=label)
    selected = [row for row in rows if _detail_matches(row, expected_decision)]
    expected_count = int(expected_decision["operation_count"])
    if len(selected) != expected_count:
        errors.append(
            "source detail frozen selected slice must contain "
            f"{expected_count} rows; actual={len(selected)}"
        )
        return selected, errors

    expected_constants = {
        "model_id": "revenue_unreacted_range",
        "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
        "artifact_version": expected_summary["artifact_version"],
        "candidate_detail_row_set_sha256": expected_decision["candidate_detail_row_set_sha256"],
        "holding_session_index_offset": "29",
        "holding_session_contract": "inclusive_entry_session_count_30_exit_offset_29",
        "entry_price_basis": "analysis_open",
        "fixed_exit_price_basis": "analysis_close",
        "exit_price_basis": "fixed_future_close",
        "source_position_bucket": "mid_pos_40_75",
        "source_shape_bucket": "falling",
        "position_policy": "anchor adjusted close positioned within the adjusted analysis-high/analysis-low range of exactly 120 prior trading sessions, excluding the anchor",
        "shape_policy": "revenue-model-owned descriptive shape: adjusted close return from t-20 to anchor; adjusted-close range across the 23 sessions ending at anchor; EMA23 through anchor with five-session slope",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "formal_model_use_allowed": "False",
        "production_change": "False",
    }
    for index, row in enumerate(selected, start=1):
        for column, expected in expected_constants.items():
            if row.get(column, "") != expected:
                errors.append(
                    f"source detail row {index} {column} mismatch: expected={expected!r}; actual={row.get(column, '')!r}"
                )
        if not _is_false(row.get("intraday_operation_basis_used", "")):
            errors.append(f"source detail row {index} uses an intraday operation basis")
        if not _is_true(row.get("same_stock_non_overlap_applied", "")):
            errors.append(f"source detail row {index} lacks same-stock non-overlap enforcement")
        if row.get("source_anchor_date", "") != row.get(
            "asof_latest_qualifying_trade_date", ""
        ):
            errors.append(f"source detail row {index} is not anchored at revenue_available")
        try:
            position = float(row["source_position_120d_pct"])
            shape_return20 = float(row["source_shape_return20_pct"])
            shape_ema23_slope5 = float(row["source_shape_ema23_slope5_pct"])
            source_lag = int(row["latest_source_to_trigger_trading_days"])
            trigger_index = int(row["trigger_index"])
            confirmation_index = int(row["confirmation_index"])
            entry_index = int(row["entry_index"])
            exit_index = int(row["exit_index"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"source detail row {index} has invalid frozen rule fields")
        else:
            if not 40.0 < position <= 75.0:
                errors.append(f"source detail row {index} violates 40<position_120d_pct<=75")
            if not shape_return20 < -5.0 or not shape_ema23_slope5 < 0.0:
                errors.append(f"source detail row {index} violates the falling shape rule")
            if not 0 <= source_lag <= 60:
                errors.append(f"source detail row {index} violates the 0..60 source lag rule")
            if confirmation_index != trigger_index + 1:
                errors.append(f"source detail row {index} violates D+1 confirmation timing")
            if entry_index != trigger_index + 2:
                errors.append(f"source detail row {index} violates D+2 entry timing")
            if exit_index != entry_index + 29:
                errors.append(f"source detail row {index} violates D+30 offset29 exit timing")

    operation_keys = [row.get("operation_key", "") for row in selected]
    if len(operation_keys) != len(set(operation_keys)):
        errors.append("source detail selected slice has duplicate operation_key rows")

    by_stock: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in selected:
        by_stock[row.get("stock_id", "")].append(row)
    overlap_pairs = 0
    for stock_id, stock_rows in by_stock.items():
        ordered = sorted(stock_rows, key=lambda item: item.get("entry_date", ""))
        for previous, current in zip(ordered, ordered[1:]):
            if current.get("entry_date", "") <= previous.get("exit_date", ""):
                overlap_pairs += 1
                errors.append(
                    f"same-stock overlap: stock_id={stock_id}; prior_exit={previous.get('exit_date')}; "
                    f"next_entry={current.get('entry_date')}"
                )
    if overlap_pairs != 0:
        errors.append(f"source detail same-stock overlap pair count must be zero; actual={overlap_pairs}")

    returns = [float(row["realized_return_pct"]) for row in selected]
    outcomes = [row.get("return_outcome", "") for row in selected]
    computed = {
        "operation_count": len(selected),
        "unique_stock_count": len({row.get("stock_id", "") for row in selected}),
        "unique_episode_count": len({row.get("episode_key", "") for row in selected}),
        "win_count": outcomes.count("win"),
        "neutral_count": outcomes.count("neutral"),
        "failure_count": outcomes.count("failure"),
        "win_rate_pct": _round4(outcomes.count("win") / len(selected) * 100.0),
        "neutral_rate_pct": _round4(outcomes.count("neutral") / len(selected) * 100.0),
        "failure_rate_pct": _round4(outcomes.count("failure") / len(selected) * 100.0),
        "avg_return_pct": _round4(statistics.fmean(returns)),
        "median_return_pct": _round4(statistics.median(returns)),
        "p10_return_pct": _round4(_linear_quantile(returns, 0.10)),
        "p90_return_pct": _round4(_linear_quantile(returns, 0.90)),
        "min_return_pct": _round4(min(returns)),
        "max_return_pct": _round4(max(returns)),
        "return_ge20_count": sum(value >= 20.0 for value in returns),
        "return_ge20_rate_pct": _round4(
            sum(value >= 20.0 for value in returns) / len(selected) * 100.0
        ),
        "return_le_minus20_count": sum(value <= -20.0 for value in returns),
        "return_le_minus20_rate_pct": _round4(
            sum(value <= -20.0 for value in returns) / len(selected) * 100.0
        ),
        "source_anomaly_candidate_count": sum(
            _is_true(row.get("source_anomaly_candidate_flag", "")) for row in selected
        ),
        "unresolved_price_path_candidate_count": sum(
            _is_true(row.get("unresolved_price_path_candidate_flag", "")) for row in selected
        ),
        "operation_return_review_candidate_count": sum(
            _is_true(row.get("operation_return_review_candidate_flag", "")) for row in selected
        ),
        "combined_exclusion_candidate_count": sum(
            _is_true(row.get("combined_exclusion_candidate_flag", "")) for row in selected
        ),
    }
    for column, actual in computed.items():
        expected_text = expected_decision[column]
        if isinstance(actual, float):
            if not math.isclose(actual, float(expected_text), rel_tol=0.0, abs_tol=0.00005):
                errors.append(
                    f"source detail recomputed {column} mismatch: expected={expected_text}; actual={actual}"
                )
        elif actual != int(expected_text):
            errors.append(
                f"source detail recomputed {column} mismatch: expected={expected_text}; actual={actual}"
            )

    artifact_candidates = {
        row.get("operation_key", ""): row
        for row in selected
        if _is_true(row.get("combined_exclusion_candidate_flag", ""))
    }
    if set(artifact_candidates) != set(anomaly_rows):
        errors.append(
            "source detail anomaly candidate set does not match disposition registry; "
            f"missing={sorted(set(anomaly_rows) - set(artifact_candidates))}; "
            f"extra={sorted(set(artifact_candidates) - set(anomaly_rows))}"
        )
    for key, disposition_row in anomaly_rows.items():
        detail_row = artifact_candidates.get(key)
        if detail_row is None:
            continue
        if detail_row.get("candidate_detail_row_sha256") != disposition_row.get(
            "candidate_detail_row_sha256"
        ):
            errors.append(f"{key}: candidate_detail_row_sha256 is not bound to source detail")
        expected_kind = (
            "operation_return_review_candidate"
            if _is_true(detail_row.get("operation_return_review_candidate_flag", ""))
            else "source_anomaly_candidate"
        )
        if disposition_row.get("candidate_kind") != expected_kind:
            errors.append(f"{key}: candidate_kind is not bound to source detail flags")
    return selected, errors


TRAJECTORY_FIELDS = (
    "stock_id",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "realized_return_pct",
    "return_outcome",
)
COMMON_BUSINESS_FIELDS = (
    *TRAJECTORY_FIELDS,
    "entry_price",
    "exit_price",
    "entry_price_basis",
    "exit_price_basis",
)


def _trajectory_key(row: dict[str, str]) -> tuple[str, ...]:
    return tuple(row.get(column, "") for column in TRAJECTORY_FIELDS)


def validate_v1_v2_reconciliation(
    v1_rows: list[dict[str, str]],
    v2_rows: list[dict[str, str]],
    migration_row: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    v1_by_key = {row.get("operation_key", ""): row for row in v1_rows}
    v2_by_key = {row.get("operation_key", ""): row for row in v2_rows}
    common_keys = set(v1_by_key) & set(v2_by_key)
    raw_added = set(v2_by_key) - set(v1_by_key)
    raw_removed = set(v1_by_key) - set(v2_by_key)
    common_business_changes = sum(
        any(v1_by_key[key].get(field, "") != v2_by_key[key].get(field, "") for field in COMMON_BUSINESS_FIELDS)
        for key in common_keys
    )

    v1_by_trajectory = {_trajectory_key(row): row for row in v1_rows}
    v2_by_trajectory = {_trajectory_key(row): row for row in v2_rows}
    common_trajectories = set(v1_by_trajectory) & set(v2_by_trajectory)
    rekeyed_trajectories = {
        trajectory
        for trajectory in common_trajectories
        if v1_by_trajectory[trajectory].get("operation_key")
        != v2_by_trajectory[trajectory].get("operation_key")
    }
    rekeyed_stocks = {trajectory[0] for trajectory in rekeyed_trajectories}
    computed = {
        "v1_operation_count": len(v1_rows),
        "v2_operation_count": len(v2_rows),
        "exact_common_operation_key_count": len(common_keys),
        "raw_added_operation_key_count": len(raw_added),
        "raw_removed_operation_key_count": len(raw_removed),
        "episode_identity_rekey_count": len(rekeyed_trajectories),
        "semantic_persistent_trajectory_count": len(common_trajectories),
        "true_added_operation_count": len(set(v2_by_trajectory) - set(v1_by_trajectory)),
        "true_removed_operation_count": len(set(v1_by_trajectory) - set(v2_by_trajectory)),
        "common_business_field_change_count": common_business_changes,
    }
    for column, actual in computed.items():
        expected = int(migration_row.get(column, "-1"))
        if actual != expected:
            errors.append(
                f"v1 to v2 selected-operation reconciliation {column} mismatch: "
                f"expected={expected}; actual={actual}"
            )
    if rekeyed_stocks != {"2451", "3665"}:
        errors.append(
            "v1 to v2 episode identity rekeys must be exactly stocks 2451 and 3665; "
            f"actual={sorted(rekeyed_stocks)}"
        )
    return errors


def _nonnegative_int(
    row: dict[str, str],
    column: str,
    *,
    label: str,
    errors: list[str],
) -> int | None:
    try:
        value = int(row.get(column, ""))
    except (TypeError, ValueError):
        errors.append(f"{label} {column} must be an integer")
        return None
    if value < 0:
        errors.append(f"{label} {column} must be non-negative")
        return None
    return value


def _run_canonical_validator(
    label: str,
    command: Sequence[str],
) -> list[str]:
    """Run one repository-owned validator without a shell or fallback path."""

    try:
        result = subprocess.run(
            list(command),
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return [f"{label} could not start: {exc}"]
    if result.returncode == 0:
        return []
    output = "\n".join(
        part.strip() for part in (result.stdout, result.stderr) if part.strip()
    )
    if len(output) > 4000:
        output = output[-4000:]
    return [
        f"{label} failed with exit code {result.returncode}"
        + (f": {output}" if output else "")
    ]


def _validate_forward_holdout_v2_evidence(
    *,
    evidence_paths: Mapping[str, Path] | None,
    price_input_directory: Path | None,
    history_base_ref: str | None,
) -> list[str]:
    """Delegate the promotion evidence decision to the independent v2 replay validator."""

    paths = dict(DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS)
    if evidence_paths is not None:
        unknown = sorted(set(evidence_paths) - set(paths))
        if unknown:
            return [f"forward holdout v2 evidence contains unsupported paths: {unknown}"]
        paths.update({name: Path(path) for name, path in evidence_paths.items()})
    errors: list[str] = []
    if not FORWARD_HOLDOUT_V2_VALIDATOR.is_file():
        errors.append(
            "promotion-candidate canonical forward holdout v2 validator is missing: "
            f"{FORWARD_HOLDOUT_V2_VALIDATOR}"
        )
    for name, path in paths.items():
        if not path.is_file():
            errors.append(
                "promotion-candidate forward holdout v2 evidence is missing: "
                f"{name}={path}"
            )
    if price_input_directory is None:
        errors.append(
            "promotion-candidate forward holdout v2 requires an explicit "
            "price_input_directory for independent replay"
        )
    elif not Path(price_input_directory).is_dir():
        errors.append(
            "promotion-candidate forward holdout v2 price_input_directory is missing: "
            f"{price_input_directory}"
        )
    normalized_base_ref = (history_base_ref or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", normalized_base_ref):
        errors.append(
            "promotion-candidate forward holdout v2 history_base_ref must be an "
            "immutable 40-character Git commit"
        )
    if errors:
        return errors

    command = [
        sys.executable,
        str(FORWARD_HOLDOUT_V2_VALIDATOR),
        "--manifest",
        str(paths["manifest"]),
        "--detail",
        str(paths["detail"]),
        "--summary",
        str(paths["summary"]),
        "--comparison",
        str(paths["comparison"]),
        "--anomaly",
        str(paths["anomaly"]),
        "--manifest-history",
        str(paths["manifest_history"]),
        "--detail-history",
        str(paths["detail_history"]),
        "--summary-history",
        str(paths["summary_history"]),
        "--comparison-history",
        str(paths["comparison_history"]),
        "--anomaly-history",
        str(paths["anomaly_history"]),
        "--source-manifest",
        str(paths["source_manifest"]),
        "--source-detail",
        str(paths["source_detail"]),
        "--price-input-directory",
        str(price_input_directory),
        "--history-base-ref",
        normalized_base_ref,
    ]
    return _run_canonical_validator(
        "promotion-candidate canonical forward holdout v2 validation",
        command,
    )


def _validate_formal_readiness_row(
    operation_readiness_path: Path,
) -> tuple[dict[str, str] | None, list[str]]:
    errors: list[str] = []
    if Path(operation_readiness_path).resolve() != DEFAULT_OPERATION_READINESS.resolve():
        errors.append(
            "production-pdf readiness must use the canonical model_operation_readiness_latest.csv"
        )
        return None, errors
    columns, readiness_rows, read_errors = _read_csv(Path(operation_readiness_path))
    errors.extend(
        f"production-pdf formal readiness hard gate: {error}" for error in read_errors
    )
    missing_columns = sorted(FORMAL_ADAPTER_READINESS_COLUMNS - set(columns))
    if columns and missing_columns:
        errors.append(
            "production-pdf readiness schema is incomplete; missing="
            f"{missing_columns}"
        )
    matching = [
        row for row in readiness_rows if row.get("model_id") == "revenue_unreacted_range"
    ]
    if len(matching) != 1:
        if readiness_rows or not read_errors:
            errors.append(
                "production-pdf formal readiness hard gate requires exactly one "
                f"revenue_unreacted_range row; actual={len(matching)}"
            )
        return None, errors
    readiness = matching[0]
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        if not _is_true(readiness.get(column, "")):
            errors.append(f"production-pdf readiness requires {column}=True")
    exact_values = {
        "approval_status": FORMAL_ADAPTER_APPROVAL_STATUS,
        "approval_version": FORMAL_ADAPTER_APPROVAL_VERSION,
        "operation_module_status": FORMAL_ADAPTER_OPERATION_MODULE_STATUS,
        "operation_module_id": FORMAL_ADAPTER_MODULE_ID,
        "operation_module_path": FORMAL_ADAPTER_MODULE.relative_to(ROOT).as_posix(),
        "adapter_artifact_id": FORMAL_ADAPTER_ARTIFACT_ID,
        "adapter_artifact_version": FORMAL_ADAPTER_APPROVAL_VERSION,
        "adapter_artifact_path": FORMAL_ADAPTER_ARTIFACT.relative_to(ROOT).as_posix(),
        "adapter_schema_version": FORMAL_ADAPTER_SCHEMA_VERSION,
        "lifecycle_contract_version": FORMAL_ADAPTER_LIFECYCLE_VERSION,
        "operation_directive_level": "approved_daily_operation_guidance",
        "pdf_integration_status": "pdf_integrated_daily_adapter",
        "packet_integration_status": "pending_packet_consumer",
    }
    for column, expected in exact_values.items():
        if readiness.get(column, "") != expected:
            errors.append(
                f"production-pdf readiness {column} mismatch: "
                f"expected={expected!r}; actual={readiness.get(column, '')!r}"
            )
    if readiness.get("daily_adapter_status", "") not in {
        "ready_approved_operation_guidance",
        "ready_empty_no_operation_rows",
    }:
        errors.append(
            "production-pdf readiness daily_adapter_status must be an exact ready state"
        )
    for column in (
        "operation_module_canonical_sha256",
        "adapter_artifact_canonical_sha256",
    ):
        if not SHA256_RE.fullmatch(readiness.get(column, "").strip().lower()):
            errors.append(f"production-pdf readiness {column} must be canonical SHA-256")
    section_tokens = [
        token.strip()
        for token in readiness.get("daily_adapter_sections", "").split(",")
        if token.strip()
    ]
    if len(section_tokens) != len(set(section_tokens)) or set(section_tokens) != (
        FORMAL_ADAPTER_REQUIRED_SECTIONS
    ):
        errors.append(
            "production-pdf readiness daily_adapter_sections must contain exactly "
            f"{sorted(FORMAL_ADAPTER_REQUIRED_SECTIONS)}"
        )
    return readiness, errors


def _validate_formal_adapter_and_consumers(
    readiness: Mapping[str, str],
    *,
    history_base_ref: str | None,
) -> list[str]:
    errors: list[str] = []
    normalized_base_ref = (history_base_ref or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", normalized_base_ref):
        errors.append(
            "production-pdf formal adapter history_base_ref must be an immutable "
            "40-character Git commit"
        )
    for label, path, kind in (
        ("formal operation module", FORMAL_ADAPTER_MODULE, "file"),
        ("formal adapter validator", FORMAL_ADAPTER_VALIDATOR, "file"),
        ("formal adapter artifact", FORMAL_ADAPTER_ARTIFACT, "file"),
        ("formal adapter history", FORMAL_ADAPTER_HISTORY_DIRECTORY, "directory"),
        ("model readiness validator", MODEL_OPERATION_READINESS_VALIDATOR, "file"),
        (
            "revenue PDF consumer validator",
            FORMAL_ADAPTER_PDF_CONSUMER_VALIDATOR,
            "file",
        ),
        ("PDF consumer validator", DAILY_PDF_CONSUMER_VALIDATOR, "file"),
    ):
        exists = path.is_dir() if kind == "directory" else path.is_file()
        if not exists:
            errors.append(f"production-pdf canonical {label} is missing: {path}")
    if errors:
        return errors
    try:
        module_text = FORMAL_ADAPTER_MODULE.read_bytes().decode("utf-8-sig")
        normalized_module = module_text.replace("\r\n", "\n").replace("\r", "\n")
        module_sha = hashlib.sha256(normalized_module.encode("utf-8")).hexdigest()
        artifact_columns, artifact_rows, artifact_read_errors = _read_csv(
            FORMAL_ADAPTER_ARTIFACT
        )
        errors.extend(
            f"production-pdf formal adapter canonical artifact: {error}"
            for error in artifact_read_errors
        )
        if "generated_at" not in artifact_columns:
            errors.append(
                "production-pdf formal adapter artifact is missing generated_at"
            )
            artifact_semantic = b""
        else:
            output = io.StringIO(newline="")
            writer = csv.DictWriter(
                output,
                fieldnames=artifact_columns,
                lineterminator="\n",
                extrasaction="raise",
            )
            writer.writeheader()
            for artifact_row in artifact_rows:
                normalized_row = dict(artifact_row)
                normalized_row["generated_at"] = ""
                writer.writerow(normalized_row)
            artifact_semantic = output.getvalue().encode("utf-8")
        artifact_sha = hashlib.sha256(artifact_semantic).hexdigest()
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        return [f"production-pdf formal adapter canonical binding failed: {exc}"]
    if module_sha != readiness.get("operation_module_canonical_sha256", ""):
        errors.append(
            "production-pdf formal adapter module canonical SHA-256 mismatch"
        )
    if artifact_sha != readiness.get("adapter_artifact_canonical_sha256", ""):
        errors.append(
            "production-pdf formal adapter artifact canonical SHA-256 mismatch"
        )
    history_snapshot = (
        FORMAL_ADAPTER_HISTORY_DIRECTORY
        / (
            "daily_revenue_unreacted_range_operation_section_20260828_"
            f"{artifact_sha}.csv"
        )
    )
    history_fs_path = (
        Path("\\\\?\\" + str(history_snapshot.resolve()))
        if sys.platform == "win32"
        else history_snapshot
    )
    if not history_fs_path.is_file():
        errors.append(
            "production-pdf canonical formal adapter history snapshot is missing: "
            f"{history_snapshot}"
        )
    else:
        try:
            history_bytes = history_fs_path.read_bytes()
        except OSError as exc:
            errors.append(
                f"production-pdf formal adapter history snapshot is unreadable: {exc}"
            )
        else:
            if history_bytes != artifact_semantic:
                errors.append(
                    "production-pdf formal adapter history snapshot does not exactly "
                    "bind the canonical runtime artifact"
                )
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", normalized_base_ref, "HEAD"],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if ancestor.returncode != 0:
        errors.append(
            "production-pdf formal adapter history_base_ref is not an ancestor of HEAD"
        )
    history_diff = subprocess.run(
        [
            "git",
            "diff",
            "--name-status",
            f"{normalized_base_ref}..HEAD",
            "--",
            FORMAL_ADAPTER_HISTORY_DIRECTORY.relative_to(ROOT).as_posix(),
        ],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if history_diff.returncode != 0:
        errors.append("production-pdf formal adapter history diff could not be verified")
    else:
        non_append = [
            line for line in history_diff.stdout.splitlines() if not line.startswith("A\t")
        ]
        if non_append:
            errors.append(
                "production-pdf formal adapter history is not append-only: "
                f"{non_append}"
            )
    if errors:
        return errors
    commands = (
        (
            "production-pdf canonical revenue formal adapter validation",
            [
                sys.executable,
                str(FORMAL_ADAPTER_VALIDATOR),
                "--artifact",
                str(FORMAL_ADAPTER_ARTIFACT),
                "--source-module",
                str(FORMAL_ADAPTER_MODULE),
                "--history-snapshot",
                str(history_fs_path),
            ],
        ),
        (
            "production-pdf canonical model operation readiness validation",
            [sys.executable, str(MODEL_OPERATION_READINESS_VALIDATOR)],
        ),
        (
            "production-pdf model-owned revenue PDF consumer contract validation",
            [
                sys.executable,
                str(FORMAL_ADAPTER_PDF_CONSUMER_VALIDATOR),
                "--phase",
                "production-approval",
                "--adapter-artifact",
                str(FORMAL_ADAPTER_ARTIFACT),
                "--operation-readiness",
                str(DEFAULT_OPERATION_READINESS),
            ],
        ),
        (
            "production-pdf canonical PDF consumer contract validation",
            [sys.executable, str(DAILY_PDF_CONSUMER_VALIDATOR), "--phase", "full"],
        ),
    )
    for label, command in commands:
        errors.extend(_run_canonical_validator(label, command))
    return errors


def validate_phase_gates(
    phase: str,
    decision_row: dict[str, str] | None,
    _legacy_anomaly_rows: dict[str, dict[str, str]],
    *,
    source_contract_verified: bool = False,
    forward_holdout_manifest_path: Path = DEFAULT_FORWARD_HOLDOUT_V2_MANIFEST,
    forward_holdout_evidence_paths: Mapping[str, Path] | None = None,
    forward_holdout_price_input_directory: Path | None = None,
    forward_holdout_history_base_ref: str | None = None,
    operation_readiness_path: Path = DEFAULT_OPERATION_READINESS,
    formal_adapter_history_base_ref: str | None = None,
) -> list[str]:
    """Apply only the gates belonging to the requested promotion phase.

    This validator is read-only.  Selecting ``production-pdf`` verifies static
    approval/readiness contracts; it does not run production, Daily Full, a PDF
    renderer, or Apps Script.
    """

    if phase not in VALIDATION_PHASES:
        return [f"unsupported promotion validation phase: {phase}"]
    if decision_row is None:
        return [f"{phase} phase cannot run without a valid latest decision row"]
    errors: list[str] = []
    if not source_contract_verified:
        errors.append(
            f"{phase} phase requires the trusted v2 PIT/lineage source contract; "
            "run with --source-audit v2 or --source-audit all"
        )
        return errors
    anomaly_result = validate_current_anomaly_dispositions(
        ROOT,
        require_effective_nonblocking=phase != "research-only",
    )
    errors.extend(
        f"canonical anomaly disposition gate: {error}"
        for error in anomaly_result.errors
    )
    if phase == "research-only":
        return errors

    effective_evidence_paths = dict(forward_holdout_evidence_paths or {})
    effective_evidence_paths["manifest"] = Path(forward_holdout_manifest_path)
    errors.extend(
        _validate_forward_holdout_v2_evidence(
            evidence_paths=effective_evidence_paths,
            price_input_directory=forward_holdout_price_input_directory,
            history_base_ref=forward_holdout_history_base_ref,
        )
    )
    _columns, holdout_rows, holdout_errors = _read_csv(
        Path(forward_holdout_manifest_path)
    )
    errors.extend(
        f"promotion-candidate forward holdout hard gate: {error}"
        for error in holdout_errors
    )
    if len(holdout_rows) != 1:
        if not holdout_errors:
            errors.append(
                "promotion-candidate forward holdout hard gate requires exactly one "
                f"manifest row; actual={len(holdout_rows)}"
            )
    else:
        row = holdout_rows[0]
        expected = {
            "model_id": "revenue_unreacted_range",
            "artifact_id": "revenue_unreacted_range_forward_holdout_v2",
            "artifact_version": "forward_holdout_v2_20260828",
            "artifact_row_key": "manifest",
            "holdout_start_date": "20260831",
            "append_only_history": "True",
            "research_only": "True",
            "formal_model_use_allowed": "False",
            "approved_for_daily": "False",
            "presentation_allowed": "False",
            "production_change": "False",
        }
        for column, expected_value in expected.items():
            if row.get(column, "") != expected_value:
                errors.append(
                    "promotion-candidate forward holdout hard gate contract drift: "
                    f"{column}; expected={expected_value!r}; actual={row.get(column, '')!r}"
                )
        mature = _nonnegative_int(
            row,
            "primary_mature_count",
            label="forward holdout manifest",
            errors=errors,
        )
        _nonnegative_int(
            row,
            "primary_right_censored_count",
            label="forward holdout manifest",
            errors=errors,
        )
        _nonnegative_int(
            row,
            "holdout_event_count",
            label="forward holdout manifest",
            errors=errors,
        )
        _nonnegative_int(
            row,
            "mature_event_count",
            label="forward holdout manifest",
            errors=errors,
        )
        _nonnegative_int(
            row,
            "bridge_excluded_signal_count",
            label="forward holdout manifest",
            errors=errors,
        )
        minimum = int(decision_row["forward_holdout_first_interpretation_min_mature"])
        maturity_is_hard_gate = not (
            decision_row.get("decision_id") == EXPECTED_DECISION_V6["decision_id"]
            and decision_row.get("forward_holdout_gate_policy")
            == "post_launch_monitoring_non_hard_no_tuning"
        )
        if maturity_is_hard_gate and mature is not None and mature < minimum:
            errors.append(
                "promotion-candidate forward holdout maturity hard gate is not met: "
                f"primary_mature_count={mature}; required={minimum}"
            )

    if phase == "production-pdf":
        for column in (
            "formal_model_use_allowed",
            "approved_for_daily",
            "presentation_allowed",
            "production_change",
        ):
            if not _is_true(decision_row.get(column, "")):
                errors.append(
                    f"production-pdf phase requires latest decision {column}=True"
                )
        if "disabled_adapter_preparation" in decision_row.get("formal_adapter_gate", ""):
            errors.append(
                "production-pdf phase requires a later append-only formal adapter approval; "
                "disabled adapter preparation is non-hard only before production approval"
            )
        if errors:
            return errors
        readiness, readiness_errors = _validate_formal_readiness_row(
            Path(operation_readiness_path)
        )
        errors.extend(readiness_errors)
        if readiness is None or errors:
            return errors
        errors.extend(
            _validate_formal_adapter_and_consumers(
                readiness,
                history_base_ref=formal_adapter_history_base_ref,
            )
        )
    return errors


def validate(
    *,
    decision_path: Path = DEFAULT_DECISION,
    anomaly_path: Path = DEFAULT_ANOMALIES,
    anomaly_v2_path: Path = DEFAULT_ANOMALIES_V2,
    migration_path: Path = DEFAULT_MIGRATIONS,
    summary_path: Path | None = None,
    detail_path: Path | None = None,
    require_source_artifacts: bool = False,
    source_audit: str | None = None,
    historical_v1_source_audit: bool = False,
    historical_v2_source_audit: bool = False,
    phase: str | None = None,
    forward_holdout_manifest_path: Path = DEFAULT_FORWARD_HOLDOUT_V2_MANIFEST,
    forward_holdout_evidence_paths: Mapping[str, Path] | None = None,
    forward_holdout_price_input_directory: Path | None = None,
    forward_holdout_history_base_ref: str | None = None,
    operation_readiness_path: Path = DEFAULT_OPERATION_READINESS,
    formal_adapter_history_base_ref: str | None = None,
    diagnostics: list[str] | None = None,
) -> list[str]:
    errors: list[str] = []
    decision_row, decision_errors = validate_decision(
        decision_path,
        diagnostics=diagnostics,
    )
    anomaly_rows, anomaly_errors = validate_anomalies(
        anomaly_path,
        expected_anomalies=EXPECTED_ANOMALIES_V1,
        version_label="v1",
        diagnostics=diagnostics,
    )
    anomaly_v2_rows, anomaly_v2_errors = validate_anomalies(
        anomaly_v2_path,
        expected_anomalies=EXPECTED_ANOMALIES_V2,
        version_label="v2",
        diagnostics=diagnostics,
    )
    migration_row, migration_errors = validate_migration(migration_path)
    errors.extend(decision_errors)
    errors.extend(anomaly_errors)
    errors.extend(anomaly_v2_errors)
    errors.extend(migration_errors)
    if phase is None and all(
        Path(actual).resolve() == Path(expected).resolve()
        for actual, expected in (
            (decision_path, DEFAULT_DECISION),
            (anomaly_path, DEFAULT_ANOMALIES),
            (anomaly_v2_path, DEFAULT_ANOMALIES_V2),
            (migration_path, DEFAULT_MIGRATIONS),
        )
    ):
        anomaly_result = validate_current_anomaly_dispositions(ROOT)
        errors.extend(
            f"canonical anomaly disposition gate: {error}"
            for error in anomaly_result.errors
        )
        if diagnostics is not None:
            diagnostics.extend(anomaly_result.diagnostics)
    explicit_summary = Path(summary_path) if summary_path is not None else None
    explicit_detail = Path(detail_path) if detail_path is not None else None
    explicit_source_requested = (
        explicit_summary is not None or explicit_detail is not None
    )
    requested_audits = [
        value
        for value in (
            source_audit,
            "v1" if historical_v1_source_audit else None,
            "v2" if historical_v2_source_audit else None,
        )
        if value is not None
    ]
    if len(requested_audits) > 1:
        errors.append("source audit selectors are mutually exclusive")
        return errors
    normalized_audit = requested_audits[0] if requested_audits else None
    if normalized_audit not in {None, "v1", "v2", "all"}:
        errors.append(f"unsupported source audit version: {normalized_audit}")
        return errors
    if normalized_audit and explicit_source_requested:
        if normalized_audit == "v1" and historical_v1_source_audit:
            errors.append(
                "historical v1 source audit cannot be combined with explicit summary/detail paths"
            )
        else:
            errors.append("trusted source audit cannot be combined with explicit summary/detail paths")
        return errors
    if historical_v1_source_audit and explicit_source_requested:
        errors.append(
            "historical v1 source audit cannot be combined with explicit summary/detail paths"
        )
        return errors

    if normalized_audit:
        versions = ("v1", "v2") if normalized_audit == "all" else (normalized_audit,)
        if normalized_audit == "all" and migration_row is not None:
            errors.extend(
                validate_migration_artifact_bindings(
                    migration_row,
                    diagnostics=diagnostics,
                )
            )
        selected_by_version: dict[str, list[dict[str, str]]] = {}
        for version in versions:
            revision = (
                TRUSTED_V1_SOURCE_REVISION if version == "v1" else TRUSTED_V2_SOURCE_REVISION
            )
            contracts = (
                TRUSTED_V1_SOURCE_ARTIFACTS
                if version == "v1"
                else TRUSTED_V2_SOURCE_ARTIFACTS
            )
            try:
                if version == "v1":
                    trusted_summary = _trusted_v1_source_blob(DEFAULT_SUMMARY)
                    trusted_detail = _trusted_v1_source_blob(DEFAULT_DETAIL)
                else:
                    trusted_summary = _trusted_v2_source_blob(DEFAULT_SUMMARY)
                    trusted_detail = _trusted_v2_source_blob(DEFAULT_DETAIL)
            except RuntimeError as exc:
                errors.append(str(exc))
                return errors
            source_label = f"trusted Git {revision}"
            if version == "v1":
                _summary, summary_errors = validate_summary(
                    DEFAULT_SUMMARY,
                    payload=trusted_summary,
                    label=f"{source_label}:{contracts[DEFAULT_SUMMARY]['path']}",
                    diagnostics=diagnostics,
                )
                selected, detail_errors = validate_detail(
                    DEFAULT_DETAIL,
                    anomaly_rows,
                    payload=trusted_detail,
                    label=f"{source_label}:{contracts[DEFAULT_DETAIL]['path']}",
                )
            else:
                _summary, summary_errors = validate_summary(
                    DEFAULT_SUMMARY,
                    payload=trusted_summary,
                    label=f"{source_label}:{contracts[DEFAULT_SUMMARY]['path']}",
                    expected_summary=SUMMARY_EXPECTED_V2,
                    diagnostics=diagnostics,
                )
                selected, detail_errors = validate_detail(
                    DEFAULT_DETAIL,
                    anomaly_v2_rows,
                    payload=trusted_detail,
                    label=f"{source_label}:{contracts[DEFAULT_DETAIL]['path']}",
                    expected_decision=EXPECTED_DECISION_V2,
                    expected_summary=SUMMARY_EXPECTED_V2,
                )
            errors.extend(summary_errors)
            errors.extend(detail_errors)
            selected_by_version[version] = selected
        if normalized_audit == "all" and migration_row is not None:
            errors.extend(
                validate_v1_v2_reconciliation(
                    selected_by_version["v1"],
                    selected_by_version["v2"],
                    migration_row,
                )
            )
    elif explicit_source_requested or require_source_artifacts:
        source_summary_path = explicit_summary
        source_detail_path = explicit_detail
        if (
            source_summary_path is None
            or source_detail_path is None
            or not source_summary_path.is_file()
            or not source_detail_path.is_file()
        ):
            errors.append(
                "source artifacts must be supplied as a complete summary/detail "
                "pair using explicit --summary and --detail paths when validation "
                "is enabled"
            )
        else:
            _summary, summary_errors = validate_summary(
                source_summary_path,
                diagnostics=diagnostics,
            )
            _detail, detail_errors = validate_detail(
                source_detail_path,
                anomaly_rows,
            )
            errors.extend(summary_errors)
            errors.extend(detail_errors)
    if phase is not None:
        errors.extend(
            validate_phase_gates(
                phase,
                decision_row,
                anomaly_v2_rows,
                source_contract_verified=normalized_audit in {"v2", "all"},
                forward_holdout_manifest_path=forward_holdout_manifest_path,
                forward_holdout_evidence_paths=forward_holdout_evidence_paths,
                forward_holdout_price_input_directory=(
                    forward_holdout_price_input_directory
                ),
                forward_holdout_history_base_ref=forward_holdout_history_base_ref,
                operation_readiness_path=operation_readiness_path,
                formal_adapter_history_base_ref=formal_adapter_history_base_ref,
            )
        )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently validate the frozen revenue promotion-preparation decision."
    )
    parser.add_argument("--decision", type=Path, default=DEFAULT_DECISION)
    parser.add_argument("--anomaly-registry", type=Path, default=DEFAULT_ANOMALIES)
    parser.add_argument("--anomaly-registry-v2", type=Path, default=DEFAULT_ANOMALIES_V2)
    parser.add_argument("--migration-ledger", type=Path, default=DEFAULT_MIGRATIONS)
    parser.add_argument(
        "--phase",
        choices=VALIDATION_PHASES,
        default="research-only",
        help=(
            "Validate only the requested staged gate. production-pdf is static/read-only "
            "and never invokes production, Daily Full, PDF rendering, or Apps Script."
        ),
    )
    parser.add_argument(
        "--forward-holdout-manifest",
        type=Path,
        default=DEFAULT_FORWARD_HOLDOUT_V2_MANIFEST,
    )
    for evidence_name, default_path in DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS.items():
        if evidence_name == "manifest":
            continue
        parser.add_argument(
            f"--forward-holdout-{evidence_name.replace('_', '-')}",
            dest=f"forward_holdout_{evidence_name}",
            type=Path,
            default=default_path,
        )
    parser.add_argument(
        "--forward-holdout-price-input-directory",
        type=Path,
        help="Explicit normalized price bundle used by the independent v2 replay validator.",
    )
    parser.add_argument(
        "--forward-holdout-history-base-ref",
        help="Immutable 40-character Git commit for append-only forward-holdout history.",
    )
    parser.add_argument(
        "--operation-readiness",
        type=Path,
        default=DEFAULT_OPERATION_READINESS,
    )
    parser.add_argument(
        "--formal-adapter-history-base-ref",
        help="Immutable 40-character Git commit for formal adapter lifecycle history.",
    )
    parser.add_argument("--summary", type=Path)
    parser.add_argument("--detail", type=Path)
    parser.add_argument(
        "--require-source-artifacts",
        action="store_true",
        help="Require an explicit --summary/--detail source-artifact pair.",
    )
    parser.add_argument(
        "--historical-v1-source-audit",
        action="store_true",
        help=(
            "Explicitly replay the frozen v1 source artifacts from their trusted "
            "Git revision. A staged research/promotion gate still requires v2 or all."
        ),
    )
    parser.add_argument(
        "--historical-v2-source-audit",
        action="store_true",
        help="Explicitly replay the frozen v2 source artifacts from trusted Git.",
    )
    parser.add_argument(
        "--source-audit",
        choices=("v1", "v2", "all"),
        help="Replay one or both immutable source versions; all also validates v1-to-v2 reconciliation.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    diagnostics: list[str] = []
    forward_holdout_evidence_paths = {
        evidence_name: getattr(args, f"forward_holdout_{evidence_name}")
        for evidence_name in DEFAULT_FORWARD_HOLDOUT_V2_EVIDENCE_PATHS
        if evidence_name != "manifest"
    }
    errors = validate(
        decision_path=args.decision,
        anomaly_path=args.anomaly_registry,
        anomaly_v2_path=args.anomaly_registry_v2,
        migration_path=args.migration_ledger,
        summary_path=args.summary,
        detail_path=args.detail,
        require_source_artifacts=args.require_source_artifacts,
        source_audit=args.source_audit,
        historical_v1_source_audit=args.historical_v1_source_audit,
        historical_v2_source_audit=args.historical_v2_source_audit,
        phase=args.phase,
        forward_holdout_manifest_path=args.forward_holdout_manifest,
        forward_holdout_evidence_paths=forward_holdout_evidence_paths,
        forward_holdout_price_input_directory=(
            args.forward_holdout_price_input_directory
        ),
        forward_holdout_history_base_ref=args.forward_holdout_history_base_ref,
        operation_readiness_path=args.operation_readiness,
        formal_adapter_history_base_ref=args.formal_adapter_history_base_ref,
        diagnostics=diagnostics,
    )
    for diagnostic in diagnostics:
        print(f"DIAGNOSTIC: {diagnostic}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if args.source_audit:
        source_state = f"trusted source audit={args.source_audit}"
    elif args.historical_v1_source_audit:
        source_state = f"historical v1 source artifacts validated from trusted Git {TRUSTED_V1_SOURCE_REVISION}"
    elif args.historical_v2_source_audit:
        source_state = f"historical v2 source artifacts validated from trusted Git {TRUSTED_V2_SOURCE_REVISION}"
    elif args.summary is not None and args.detail is not None:
        source_state = "explicit source artifacts validated"
    else:
        source_state = "registry/anomaly governance-only validation"
    print(
        "PASS: revenue_unreacted_range promotion preparation independently validated; "
        f"phase={args.phase}; {source_state}; staged formal-state contract matched; "
        "anomaly worklists=v1:8,v2:9"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
