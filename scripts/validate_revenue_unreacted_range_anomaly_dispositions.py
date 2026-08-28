from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
EVIDENCE_SCHEMA_VERSION = "revenue_unreacted_range_anomaly_evidence_v1"
REGISTRY_VERSION = "anomaly_disposition_v3_20260829"
LEGACY_V2_REGISTRY_CANONICAL_SHA256 = (
    "626c580b53868bb6dee2474c2640647fe89d411fb929975afb5aafb22d4c75c3"
)
REGISTRY_PATH = Path(
    "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv"
)
LEGACY_V2_REGISTRY_PATH = Path(
    "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
)
MIGRATION_PATH = Path(
    "config/revenue_unreacted_range_anomaly_disposition_migrations.csv"
)
REPAIR_CLOSURE_PATH = Path(
    "config/revenue_unreacted_range_anomaly_repair_closure_registry.csv"
)
MONTHLY_REVENUE_PATH = Path(
    "data/monthly_revenue_history/monthly_revenue_history.csv"
)
EVIDENCE_ROOT = PurePosixPath("docs/evidence/revenue_unreacted_range")
OFFICIAL_EVENT_HISTORY_BASE_URLS = frozenset(
    {
        "https://www.twse.com.tw/rwd/zh/exRight/TWT49U",
        "https://www.twse.com.tw/rwd/zh/reducation/TWTAUU",
        "https://www.twse.com.tw/rwd/zh/change/TWTB8U",
        "https://www.twse.com.tw/rwd/zh/afterTrading/TWTAWU",
    }
)
INDEPENDENT_CORROBORATION_HOSTS = frozenset(
    {
        "5850web.moneydj.com",
        "www.moneydj.com",
        "tw.stock.yahoo.com",
        "www.wantgoo.com",
        "goodinfo.tw",
    }
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
EVIDENCE_REFERENCE_RE = re.compile(
    r"^evidence_id=(?P<evidence_id>[a-z0-9][a-z0-9_.-]*);"
    r"path=(?P<path>[^;\r\n]+);"
    r"canonical_sha256=(?P<canonical_sha256>[0-9a-f]{64})$"
)
CANONICAL_JSON_VERSION = "canonical_json_v1"
CANONICAL_CSV_VERSION = "canonical_csv_semantic_v1"
RULE_FORMULA_SHA256 = (
    "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
)
REPAIR_ID = (
    "revenue_unreacted_range_6177_trigger_asof_anomaly_attribution_"
    "repair_v1_20260829"
)
REPAIR_OPERATION_KEY = (
    "rearm_after_realized_exit_next_trade_day|"
    "delayed_next_close_continuation_bonus|6177|"
    "absolute_or_two_month_yoy_ge15|6177|20250517|1|20251204|20251208"
)
PRIMARY_METRIC_SIGNATURE = (
    "operation_count=53;unique_stock_count=48;unique_episode_count=48;"
    "win_count=41;neutral_count=0;failure_count=12;win_rate_pct=77.3585;"
    "avg_return_pct=14.895;median_return_pct=9.4077"
)
SENSITIVITY_METRIC_SIGNATURE = (
    "operation_count=45;win_count=35;failure_count=10;win_rate_pct=77.7778;"
    "avg_return_pct=14.1697;median_return_pct=9.3306"
)

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
ROOT_CHECK_EVIDENCE_KEYS = {
    "identity_non_overlap_status": "identity_non_overlap",
    "formal_operation_replay_status": "formal_operation_replay",
    "pit_calendar_continuity_status": "pit_calendar_continuity",
    "raw_source_lineage_status": "raw_source_lineage",
    "units_formula_adjustment_status": "units_formula_adjustment",
    "authoritative_event_history_status": "authoritative_event_history",
    "independent_source_corroboration_status": "independent_source_corroboration",
    "reproducible_evidence_reference_status": "reproducible_evidence_reference",
}
REGISTRY_COLUMNS = (
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
    "repair_satisfaction_status",
    "effective_anomaly_gate_status",
    "evidence_reference",
    "approved_reason_reference",
    "reviewed_at",
)
MIGRATION_COLUMNS = (
    "migration_id",
    "migration_date",
    "model_id",
    "from_registry_version",
    "to_registry_version",
    "from_registry_path",
    "to_registry_path",
    "from_registry_canonical_sha256",
    "to_registry_canonical_sha256",
    "operation_key_count",
    "verified_real_extreme_count",
    "verified_data_error_count",
    "verified_non_comparable_count",
    "unresolved_count",
    "evidence_count",
    "repair_closure_id",
    "authorization_reference",
    "append_only",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_change",
)
REPAIR_CLOSURE_COLUMNS = (
    "repair_id",
    "repair_date",
    "model_id",
    "operation_key",
    "root_cause",
    "source_owner_lane",
    "from_candidate_artifact_version",
    "to_source_first_artifact_version",
    "to_rearmed_artifact_version",
    "to_operation_lag_artifact_version",
    "to_position_shape_artifact_version",
    "to_candidate_artifact_version",
    "before_baseline_commit",
    "before_candidate_summary_path",
    "before_candidate_summary_canonical_sha256",
    "before_candidate_detail_path",
    "before_candidate_detail_canonical_sha256",
    "candidate_summary_path",
    "candidate_summary_canonical_sha256",
    "candidate_detail_path",
    "candidate_detail_canonical_sha256",
    "before_candidate_detail_row_sha256",
    "after_candidate_detail_row_sha256",
    "operation_business_field_change_count",
    "primary_metric_rerun_completed",
    "selected_operation_business_row_set_sha256_before",
    "selected_operation_business_row_set_sha256_after",
    "primary_metrics_semantic_sha256_before",
    "primary_metrics_semantic_sha256_after",
    "anomaly_attribution_row_set_sha256_before",
    "anomaly_attribution_row_set_sha256_after",
    "trigger_asof_event_periods",
    "trigger_asof_available_dates",
    "trigger_asof_canonical_row_sha256s",
    "trigger_asof_raw_file_sha256s_diagnostic",
    "excluded_future_event_periods",
    "excluded_future_available_dates",
    "excluded_future_canonical_row_sha256s",
    "excluded_future_raw_file_sha256s_diagnostic",
    "selected_operation_count",
    "selected_operation_key_set_sha256",
    "selected_candidate_row_set_sha256",
    "current_anomaly_operation_key_set_sha256",
    "primary_metric_signature",
    "sensitivity_metric_signature",
    "rule_formula_sha256",
    "operation_identity_preserved",
    "primary_metrics_preserved",
    "repair_status",
    "authorization_reference",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_change",
)
REGISTRY_PROVENANCE_COLUMNS = frozenset({"anomaly_source_raw_file_sha256s"})
ARTIFACT_PROVENANCE_COLUMNS = frozenset(
    {"generated_at", "monthly_revenue_history_blob_sha256"}
)
V2_CANDIDATE_SUMMARY_PATH = Path(
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
)
V2_CANDIDATE_DETAIL_PATH = Path(
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv"
)
V3_CANDIDATE_SUMMARY_PATH = Path(
    "output/history/research/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_v3_20260829.csv"
)
V3_CANDIDATE_DETAIL_PATH = Path(
    "output/history/research/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_v3_20260829.csv"
)
V3_CANDIDATE_SUMMARY_SEMANTIC_SHA256 = (
    "b43bf4b560e0753402c99582f2a8077aff7bdcb47ec634c93da68c8d06c15cae"
)
V3_CANDIDATE_DETAIL_SEMANTIC_SHA256 = (
    "c9855fdee65ca95c60b870201754b9b16c8d5f3396339acc0512e7a731383b65"
)
V3_CANDIDATE_SUMMARY_ROW_COUNT = 24
V3_CANDIDATE_DETAIL_ROW_COUNT = 308
V2_CANDIDATE_BASELINE_COMMIT = (
    "c8c8b046db3e23f7da9baf1b04508f433f13bc21"
)
V2_CANDIDATE_ARTIFACT_VERSION = "low_mid_falling_candidate_v2_20260822"
SELECTED_FILTER = {
    "lifecycle_policy_id": "rearm_after_realized_exit_next_trade_day",
    "confirmation_variant_id": "delayed_next_close_continuation_bonus",
    "holding_days": "30",
    "stop_policy_id": "none_no_stop_reference",
}
SELECTED_BUSINESS_COLUMNS = (
    "operation_key",
    "stock_id",
    "episode_key",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "realized_return_pct",
    "return_outcome",
    "source_anchor_date",
    "source_position_120d_pct",
    "source_shape_return20_pct",
    "source_shape_range23_pct",
    "source_shape_ema23_slope5_pct",
    "source_position_bucket",
    "source_shape_bucket",
    "mid_falling_member",
)
PRIMARY_METRIC_COLUMNS = (
    "operation_count", "unique_stock_count", "unique_episode_count",
    "win_count", "neutral_count", "failure_count", "win_rate_pct",
    "neutral_rate_pct", "failure_rate_pct", "avg_return_pct",
    "median_return_pct", "p10_return_pct", "p90_return_pct",
    "min_return_pct", "max_return_pct", "return_ge20_count",
    "return_ge20_rate_pct", "return_le_minus20_count",
    "return_le_minus20_rate_pct",
)
ANOMALY_ATTRIBUTION_COLUMNS = (
    "operation_key", "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "operation_return_review_candidate_flag",
    "combined_exclusion_candidate_flag", "primary_included",
    "sensitivity_included",
)
V3_CANDIDATE_ROW_PROVENANCE_COLUMNS = frozenset(
    {"generated_at", "monthly_revenue_history_blob_sha256"}
)
V3_CANDIDATE_POST_HASH_COLUMNS = frozenset(
    {
        "candidate_detail_row_sha256",
        "detail_artifact_canonical_sha256",
        "source_first_canonical_row_set_sha256",
        "rearmed_operation_canonical_row_set_sha256",
        "price_history_canonical_set_sha256",
        "candidate_detail_row_set_sha256",
    }
)


@dataclass(frozen=True)
class ExpectedCase:
    stock_id: str
    stock_name: str
    trigger_date: str
    confirmation_date: str
    entry_date: str
    exit_date: str
    trigger_close: str
    confirmation_close: str
    entry_open: str
    exit_close: str
    realized_return_pct: str
    candidate_v2_row_sha256: str
    candidate_v3_row_sha256: str
    evidence_id: str
    evidence_path: str
    disposition: str
    candidate_kind: str
    anomaly_attribution_mode: str
    anomaly_source_event_periods: tuple[str, ...]
    anomaly_source_source_dates: tuple[str, ...]
    anomaly_source_available_dates: tuple[str, ...]
    anomaly_source_canonical_row_sha256s: tuple[str, ...]
    anomaly_attribution_note: str
    evidence_monthly_events: tuple[tuple[str, str, str, str, bool], ...]
    reviewed_at: str
    evidence_canonical_sha256: str


def _case(
    operation_key: str,
    *,
    stock_id: str,
    stock_name: str,
    dates: Sequence[str],
    prices: Sequence[str],
    realized_return_pct: str,
    candidate_v2_row_sha256: str,
    candidate_v3_row_sha256: str,
    candidate_kind: str,
    anomaly_attribution_mode: str,
    anomaly_source_event_periods: Sequence[str],
    anomaly_source_source_dates: Sequence[str],
    anomaly_source_available_dates: Sequence[str],
    anomaly_source_canonical_row_sha256s: Sequence[str],
    anomaly_attribution_note: str,
    evidence_monthly_events: Sequence[tuple[str, str, str, str, bool]],
    reviewed_at: str,
    evidence_canonical_sha256: str,
    disposition: str = "verified_real_extreme",
) -> tuple[str, ExpectedCase]:
    entry_date = dates[2]
    evidence_id = f"revenue_unreacted_range_anomaly_{stock_id}_{entry_date}_v1"
    return operation_key, ExpectedCase(
        stock_id=stock_id,
        stock_name=stock_name,
        trigger_date=dates[0],
        confirmation_date=dates[1],
        entry_date=entry_date,
        exit_date=dates[3],
        trigger_close=prices[0],
        confirmation_close=prices[1],
        entry_open=prices[2],
        exit_close=prices[3],
        realized_return_pct=realized_return_pct,
        candidate_v2_row_sha256=candidate_v2_row_sha256,
        candidate_v3_row_sha256=candidate_v3_row_sha256,
        evidence_id=evidence_id,
        evidence_path=(
            f"docs/evidence/revenue_unreacted_range/{evidence_id}.json"
        ),
        disposition=disposition,
        candidate_kind=candidate_kind,
        anomaly_attribution_mode=anomaly_attribution_mode,
        anomaly_source_event_periods=tuple(anomaly_source_event_periods),
        anomaly_source_source_dates=tuple(anomaly_source_source_dates),
        anomaly_source_available_dates=tuple(anomaly_source_available_dates),
        anomaly_source_canonical_row_sha256s=tuple(
            anomaly_source_canonical_row_sha256s
        ),
        anomaly_attribution_note=anomaly_attribution_note,
        evidence_monthly_events=tuple(evidence_monthly_events),
        reviewed_at=reviewed_at,
        evidence_canonical_sha256=evidence_canonical_sha256,
    )


EXPECTED_CASES = dict(
    [
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2408|absolute_or_two_month_yoy_ge15|2408|20260417|2|20260427|20260429",
            stock_id="2408", stock_name="南亞科",
            dates=("20260427", "20260428", "20260429", "20260610"),
            prices=("226.5", "237.5", "236.0", "333.0"),
            realized_return_pct="41.1017",
            candidate_v2_row_sha256="8642cd7286a0eee22ba76d69e6ab826c9ec22c3e83a3ed63fef27753e81f0168",
            candidate_v3_row_sha256="21301aeb57c77c93c156d2a1bdeafa7c150a8969e518f43a392703adc4f6d67d",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202603",),
            anomaly_source_source_dates=("20260417",),
            anomaly_source_available_dates=("20260417",),
            anomaly_source_canonical_row_sha256s=(
                "aeec5b0f201473cc8c1760527f46596a0af3c756a2d3396679eb7f72246ee356",
            ),
            anomaly_attribution_note=(
                "exact anomalous qualifying monthly-revenue event known by trigger"
            ),
            evidence_monthly_events=((
                "202603", "20260417", "20260417",
                "aeec5b0f201473cc8c1760527f46596a0af3c756a2d3396679eb7f72246ee356",
                True,
            ),),
            reviewed_at="2026-08-29T05:15:00+08:00",
            evidence_canonical_sha256="5d373a53f05cc3a379867fc79195253709a949c9a820c980e255fd431a4975ad",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2451|absolute_or_two_month_yoy_ge15|2451|20250517|1|20260313|20260317",
            stock_id="2451", stock_name="創見",
            dates=("20260313", "20260316", "20260317", "20260429"),
            prices=("236.0", "259.5", "264.0", "268.0"),
            realized_return_pct="1.5152",
            candidate_v2_row_sha256="e5eed6f2f6d39d9da369041116395383580ef98274e7490bcaadc6a23a22d20e",
            candidate_v3_row_sha256="f291c44cc871a882bcdc8218ec5a4bddee9a3e0f7638373b7f322baa9da5fe63",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202601",),
            anomaly_source_source_dates=("20260217",),
            anomaly_source_available_dates=("20260223",),
            anomaly_source_canonical_row_sha256s=(
                "535dfa06caf2e73a1afba4cbaae0e731bdecf5a1377de6d0f619535ccd533fc1",
            ),
            anomaly_attribution_note=(
                "exact anomalous qualifying monthly-revenue event known by trigger"
            ),
            evidence_monthly_events=((
                "202601", "20260217", "20260223",
                "535dfa06caf2e73a1afba4cbaae0e731bdecf5a1377de6d0f619535ccd533fc1",
                True,
            ),),
            reviewed_at="2026-08-29T05:20:00+08:00",
            evidence_canonical_sha256="0d274ce56a68d9bea62209273a927ed3c98fb2a325e478bd27d511bb3e9fc76c",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2478|absolute_or_two_month_yoy_ge15|2478|20260217|2|20260416|20260420",
            stock_id="2478", stock_name="大毅",
            dates=("20260416", "20260417", "20260420", "20260601"),
            prices=("74.2", "77.2", "78.9", "144.0"),
            realized_return_pct="82.5095",
            candidate_v2_row_sha256="facf4234439f7b5627a00b3bfa82c2976559357c218b0a341ca0a5a0e2d53a9b",
            candidate_v3_row_sha256="a912c8f349268cf956c476d232f5fb5d8dc160a4747b2c3450989651cf6726e2",
            candidate_kind="operation_return_review_candidate",
            anomaly_attribution_mode="operation_return_review_not_source_attributed",
            anomaly_source_event_periods=(),
            anomaly_source_source_dates=(),
            anomaly_source_available_dates=(),
            anomaly_source_canonical_row_sha256s=(),
            anomaly_attribution_note=(
                "operation-return magnitude review is not a monthly-revenue source "
                "anomaly attribution"
            ),
            evidence_monthly_events=(),
            reviewed_at="2026-08-29T05:22:00+08:00",
            evidence_canonical_sha256="ff5cac95a0f7fd619f35c5f20493ce1c434d5e3524a390e878fdd2e32d06de59",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2527|absolute_or_two_month_yoy_ge15|2527|20260517|1|20260526|20260528",
            stock_id="2527", stock_name="宏璟",
            dates=("20260526", "20260527", "20260528", "20260709"),
            prices=("35.15", "36.25", "36.3", "42.6"),
            realized_return_pct="17.3554",
            candidate_v2_row_sha256="34d2b8aa9258ae1a686feaa937ada66e56c238c7dd5994299b4a3c74ee5d8c6a",
            candidate_v3_row_sha256="37a9860d661afe44b5c3e096d01ed6983a5c7370f823b7f10d2361718e8eb924",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202604",),
            anomaly_source_source_dates=("20260517",),
            anomaly_source_available_dates=("20260518",),
            anomaly_source_canonical_row_sha256s=(
                "047b94ab8b2e136f27ad1ac45f8259b25f852cfbc64b2f6f80eb02eae2926abc",
            ),
            anomaly_attribution_note=(
                "exact anomalous qualifying monthly-revenue event known by trigger"
            ),
            evidence_monthly_events=((
                "202604", "20260517", "20260518",
                "047b94ab8b2e136f27ad1ac45f8259b25f852cfbc64b2f6f80eb02eae2926abc",
                True,
            ),),
            reviewed_at="2026-08-29T05:24:00+08:00",
            evidence_canonical_sha256="882bd68a119918f0dffa86144c53727ba8ddf8d82d5e619adacf058a1da61910",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20251128|20251202",
            stock_id="3535", stock_name="晶彩科",
            dates=("20251128", "20251201", "20251202", "20260114"),
            prices=("83.3", "91.6", "91.3", "88.9"),
            realized_return_pct="-2.6287",
            candidate_v2_row_sha256="f7ed7ce96221e2754d299f73ee1025763d7d8b858b19232c18a4e3b21032c5c2",
            candidate_v3_row_sha256="c94ce0382b68452d01ce6e78535ab065b082b5597d72408533e6c152d282564b",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202509", "202510"),
            anomaly_source_source_dates=("20251017", "20251117"),
            anomaly_source_available_dates=("20251017", "20251117"),
            anomaly_source_canonical_row_sha256s=(
                "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203",
                "cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40",
            ),
            anomaly_attribution_note=(
                "two exact anomalous qualifying events known by trigger in the "
                "shared episode"
            ),
            evidence_monthly_events=(
                ("202509", "20251017", "20251017", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203", True),
                ("202510", "20251117", "20251117", "cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", True),
            ),
            reviewed_at="2026-08-29T05:26:00+08:00",
            evidence_canonical_sha256="4e9c88f59972cb9a33e3cdde7803ae832efa2969854385de250021084e07b3bb",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20260119|20260121",
            stock_id="3535", stock_name="晶彩科",
            dates=("20260119", "20260120", "20260121", "20260313"),
            prices=("106.5", "115.5", "113.0", "126.0"),
            realized_return_pct="11.5044",
            candidate_v2_row_sha256="e4b00d986b4af400e6cc05ce38687964f7de9944914d77eb31fc0a9755a64596",
            candidate_v3_row_sha256="b2333cd6eaefc2c3ad015592c92dd6967acdfc321ecbf0c1698c9393d63ebec7",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202509", "202510"),
            anomaly_source_source_dates=("20251017", "20251117"),
            anomaly_source_available_dates=("20251017", "20251117"),
            anomaly_source_canonical_row_sha256s=(
                "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203",
                "cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40",
            ),
            anomaly_attribution_note=(
                "two exact anomalous qualifying events known by trigger in the "
                "shared episode"
            ),
            evidence_monthly_events=(
                ("202509", "20251017", "20251017", "6d3a88558f79830a784f840551769cc8933e119ab8f3cbc8bf845fda0732d203", True),
                ("202510", "20251117", "20251117", "cbbc556f48ffed56bf54c0868d64eef15c9669a287670f9f782b2ca2bfffbc40", True),
            ),
            reviewed_at="2026-08-29T05:27:00+08:00",
            evidence_canonical_sha256="285c60545a3e00ec57beb0aa370adad624ad40843d52e78979d1fea7c06c4554",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|4142|absolute_or_two_month_yoy_ge15|4142|20250617|1|20260109|20260113",
            stock_id="4142", stock_name="國光生",
            dates=("20260109", "20260112", "20260113", "20260305"),
            prices=("19.95", "20.45", "20.45", "17.8"),
            realized_return_pct="-12.9584",
            candidate_v2_row_sha256="2f36fb8d8e6bd05b879a164e5748d318088ebc6936d1d97dc9a9cd728c0bc35b",
            candidate_v3_row_sha256="7547ba8e255b548e942d4bff0aa29ca282b2ba88b83c54f9bbf1a2b20b8987d3",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202511",),
            anomaly_source_source_dates=("20251217",),
            anomaly_source_available_dates=("20251217",),
            anomaly_source_canonical_row_sha256s=(
                "6200122b66aa1cfc523f215276d07af291f0aac27cab819e3964d3038473f45a",
            ),
            anomaly_attribution_note=(
                "exact anomalous qualifying monthly-revenue event known by trigger"
            ),
            evidence_monthly_events=((
                "202511", "20251217", "20251217",
                "6200122b66aa1cfc523f215276d07af291f0aac27cab819e3964d3038473f45a",
                True,
            ),),
            reviewed_at="2026-08-29T05:29:00+08:00",
            evidence_canonical_sha256="ad6df4a233114cc5ea7da97db13d9af232e148fd65e089200fcb3eec3e96f334",
        ),
        _case(
            "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|5484|absolute_or_two_month_yoy_ge15|5484|20251017|1|20260515|20260519",
            stock_id="5484", stock_name="慧友",
            dates=("20260515", "20260518", "20260519", "20260630"),
            prices=("40.6", "41.4", "40.3", "45.7"),
            realized_return_pct="13.3995",
            candidate_v2_row_sha256="5f3ca72b872eeb3f02e078e9544b456751e6dc2c4fc7942a7a023c961a6ce514",
            candidate_v3_row_sha256="654a0d4af4a87a6d170c1f49effd2a76ac81889847158dab2240c5a90b88e3f4",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode="exact_anomaly_causing_qualifying_source_events",
            anomaly_source_event_periods=("202512",),
            anomaly_source_source_dates=("20260117",),
            anomaly_source_available_dates=("20260119",),
            anomaly_source_canonical_row_sha256s=(
                "e91f324a5d4c664bf1ca2e329f094212294de006eec1b3395cec5b7b4ff8324c",
            ),
            anomaly_attribution_note=(
                "exact anomalous qualifying event not the latest 202603 source "
                "available by trigger"
            ),
            evidence_monthly_events=((
                "202512", "20260117", "20260119",
                "e91f324a5d4c664bf1ca2e329f094212294de006eec1b3395cec5b7b4ff8324c",
                True,
            ),),
            reviewed_at="2026-08-29T05:31:00+08:00",
            evidence_canonical_sha256="d7498b09ef8c540041d2ccc7c68d711f9d54e5fb16b0d5057a8adddb0dc362a5",
        ),
        _case(
            REPAIR_OPERATION_KEY,
            stock_id="6177", stock_name="達麗",
            dates=("20251204", "20251205", "20251208", "20260120"),
            prices=("48.25", "48.30", "48.35", "50.90"),
            realized_return_pct="5.274",
            candidate_v2_row_sha256="e3ff0aa0f2af328e8e959321235acc79af9efdf0a7df508db4d55bac57b88e23",
            candidate_v3_row_sha256="2af20806fe14f601812f6183fda2421deff0e5c649ab1e76c719430d40825ea4",
            candidate_kind="source_anomaly_candidate",
            anomaly_attribution_mode=(
                "trigger_asof_repaired_no_anomalous_qualifying_source_event"
            ),
            anomaly_source_event_periods=("202504", "202509"),
            anomaly_source_source_dates=("20250517", "20251017"),
            anomaly_source_available_dates=("20250519", "20251017"),
            anomaly_source_canonical_row_sha256s=(
                "1cb88da0fb389f1e4775c6ae2c05d1c4813d7c584e9e2fc0ba7183d4bf7e1e71",
                "d8d8792b836c414d9356e174e055619cc9eedf4627a8f52235bb4994cf2f495b",
            ),
            anomaly_attribution_note=(
                "trigger-as-of qualifying events 202504 and 202509 were "
                "non-anomalous; post-trigger 202512 event available 20260119 is "
                "excluded from attribution"
            ),
            evidence_monthly_events=(
                ("202504", "20250517", "20250519", "1cb88da0fb389f1e4775c6ae2c05d1c4813d7c584e9e2fc0ba7183d4bf7e1e71", False),
                ("202509", "20251017", "20251017", "d8d8792b836c414d9356e174e055619cc9eedf4627a8f52235bb4994cf2f495b", False),
                ("202512", "20260117", "20260119", "d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1", True),
            ),
            reviewed_at="2026-08-29T05:32:00+08:00",
            evidence_canonical_sha256="c4da5ecf9d6864ea8af798d138537dcc3f8ff97c7e1bdac2de7b402a572bb471",
            disposition="verified_data_error",
        ),
    ]
)

SOURCE_IDENTITY_COLUMNS = (
    "market", "source_market_name", "source_table_date", "source_kind",
    "source_url", "source_file",
)
BUSINESS_PAYLOAD_COLUMNS = (
    "stock_id", "stock_name", "industry", "revenue_period", "revenue_period_roc",
    "monthly_revenue", "previous_month_revenue", "last_year_month_revenue",
    "month_over_month_pct", "latest_revenue_yoy_pct", "cumulative_revenue",
    "last_year_cumulative_revenue", "cumulative_revenue_yoy_pct", "note",
    "revenue_positive_flag", "revenue_strong_flag",
    "revenue_numerical_anomaly_flag", "revenue_numerical_anomaly_reason",
    "point_in_time_status", "research_join_allowed",
    "allowed_for_formal_historical_model_use", "formal_use_blocker", "coverage_note",
)
RAW_ROW_CANONICAL_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
RAW_ROW_NUMERIC_COLUMNS = frozenset(
    {
        "monthly_revenue", "previous_month_revenue", "last_year_month_revenue",
        "month_over_month_pct", "latest_revenue_yoy_pct", "cumulative_revenue",
        "last_year_cumulative_revenue", "cumulative_revenue_yoy_pct",
    }
)
RAW_ROW_BOOLEAN_COLUMNS = frozenset(
    {
        "revenue_positive_flag", "revenue_strong_flag",
        "revenue_numerical_anomaly_flag", "research_join_allowed",
        "allowed_for_formal_historical_model_use",
    }
)
PRICE_ROW_CANONICAL_COLUMNS = (
    "date",
    "stock_id",
    "stock_name",
    "market",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "trading_value",
)
PRICE_ROW_NUMERIC_COLUMNS = frozenset(
    {"open", "high", "low", "close", "volume", "trading_value"}
)
REPAIR_CLOSURE_PROVENANCE_COLUMNS = frozenset(
    {
        "trigger_asof_raw_file_sha256s_diagnostic",
        "excluded_future_raw_file_sha256s_diagnostic",
    }
)


@dataclass
class ValidationResult:
    rows: dict[str, dict[str, str]]
    effective_blockers: list[str]
    current_anomaly_keys: list[str]
    errors: list[str]
    diagnostics: list[str]


def _canonical_json_sha256(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _is_transport_provenance_name(name: object) -> bool:
    normalized = str(name).strip().lower()
    return (
        normalized == "generated_at"
        or normalized.startswith("raw_")
        or "blob_sha256" in normalized
        or "byte_sha256" in normalized
        or "bytes_sha256" in normalized
        or "crlf" in normalized
        or "line_ending" in normalized
    )


def _without_transport_provenance(value: object) -> object:
    if isinstance(value, Mapping):
        return {
            str(key): _without_transport_provenance(item)
            for key, item in value.items()
            if not _is_transport_provenance_name(key)
            or str(key) == "raw_source_lineage"
        }
    if isinstance(value, list):
        return [_without_transport_provenance(item) for item in value]
    return value


def evidence_canonical_sha256(document: Mapping[str, Any]) -> str:
    return _canonical_json_sha256(
        {
            "schema_version": document.get("schema_version"),
            "evidence_id": document.get("evidence_id"),
            "semantic_payload": _without_transport_provenance(
                document.get("semantic_payload")
            ),
        }
    )


def _read_csv_bytes(
    data: bytes,
    *,
    source_name: str,
) -> tuple[list[str], list[dict[str, str]]]:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{source_name}: invalid UTF-8 CSV: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text))
    columns = list(reader.fieldnames or [])
    if not columns:
        raise ValueError(f"{source_name}: missing CSV header")
    if len(columns) != len(set(columns)) or any(not column for column in columns):
        raise ValueError(f"{source_name}: invalid CSV header")
    rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError(f"{source_name}: row wider than CSV header")
    return columns, rows


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    return _read_csv_bytes(path.read_bytes(), source_name=str(path))


def _read_git_blob(
    repo_root: Path,
    *,
    commit_sha: str,
    logical_path: Path,
) -> bytes:
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise ValueError("immutable baseline commit must be a full SHA-1")
    resolved = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(repo_root),
            "rev-parse",
            "--verify",
            f"{commit_sha}^{{commit}}",
        ],
        check=False,
        capture_output=True,
    )
    if resolved.returncode or resolved.stdout.decode("ascii", errors="replace").strip() != commit_sha:
        raise ValueError(
            f"immutable v2 baseline is not the exact commit {commit_sha}"
        )
    ancestor = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(repo_root),
            "merge-base",
            "--is-ancestor",
            commit_sha,
            "HEAD",
        ],
        check=False,
        capture_output=True,
    )
    if ancestor.returncode:
        raise ValueError(
            f"immutable v2 baseline commit is not an ancestor of HEAD: {commit_sha}"
        )
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(repo_root),
            "cat-file",
            "blob",
            f"{commit_sha}:{logical_path.as_posix()}",
        ],
        check=False,
        capture_output=True,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(
            "immutable v2 baseline Git blob unavailable: "
            f"{commit_sha}:{logical_path.as_posix()}: {detail}"
        )
    return result.stdout


def _read_git_csv(
    repo_root: Path,
    *,
    commit_sha: str,
    logical_path: Path,
) -> tuple[list[str], list[dict[str, str]]]:
    data = _read_git_blob(
        repo_root,
        commit_sha=commit_sha,
        logical_path=logical_path,
    )
    return _read_csv_bytes(
        data,
        source_name=f"{commit_sha}:{logical_path.as_posix()}",
    )


def csv_semantic_sha256(
    path: Path,
    *,
    excluded_columns: frozenset[str] = frozenset(),
) -> str:
    return csv_bytes_semantic_sha256(
        path.read_bytes(),
        excluded_columns=excluded_columns,
        source_name=str(path),
    )


def csv_bytes_semantic_sha256(
    data: bytes,
    *,
    excluded_columns: frozenset[str] = frozenset(),
    source_name: str = "<bytes>",
) -> str:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{source_name}: invalid UTF-8 CSV: {exc}") from exc
    reader = csv.DictReader(io.StringIO(text))
    columns = list(reader.fieldnames or [])
    if not columns or len(columns) != len(set(columns)) or any(
        not column for column in columns
    ):
        raise ValueError(f"{source_name}: invalid CSV header")
    rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError(f"{source_name}: row wider than CSV header")
    semantic_columns = [column for column in columns if column not in excluded_columns]
    return _canonical_json_sha256(
        [
            CANONICAL_CSV_VERSION,
            semantic_columns,
            [
                [
                    _canonical_generic_value(row.get(column, ""))
                    for column in semantic_columns
                ]
                for row in rows
            ],
        ]
    )


def artifact_semantic_sha256(path: Path) -> str:
    return artifact_bytes_semantic_sha256(
        path.read_bytes(),
        source_name=str(path),
    )


def artifact_bytes_semantic_sha256(data: bytes, *, source_name: str) -> str:
    columns, rows = _read_csv_bytes(data, source_name=source_name)
    semantic_columns = [
        column
        for column in columns
        if column not in ARTIFACT_PROVENANCE_COLUMNS
        and not _is_transport_provenance_name(column)
    ]
    return _records_semantic_sha256(rows, semantic_columns, row_set=False)


def legacy_artifact_bytes_semantic_sha256(data: bytes, *, source_name: str) -> str:
    columns, _rows = _read_csv_bytes(data, source_name=source_name)
    excluded = frozenset(
        column
        for column in columns
        if column in ARTIFACT_PROVENANCE_COLUMNS
        or _is_transport_provenance_name(column)
    )
    return csv_bytes_semantic_sha256(
        data,
        excluded_columns=excluded,
        source_name=source_name,
    )


def _records_semantic_sha256(
    rows: Sequence[Mapping[str, str]],
    columns: Sequence[str],
    *,
    row_set: bool,
) -> str:
    records = [
        json.dumps(
            {column: str(row.get(column, "")) for column in columns},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        for row in rows
    ]
    if row_set:
        records.sort()
    return hashlib.sha256(("\n".join(records) + "\n").encode("utf-8")).hexdigest()


def _selected_business_rows(rows: Sequence[Mapping[str, str]]) -> list[dict[str, str]]:
    selected = []
    for row in rows:
        if row.get("model_id", "") != MODEL_ID:
            continue
        if row.get("source_variant_id", "") != "absolute_or_two_month_yoy_ge15":
            continue
        if any(row.get(column, "") != expected for column, expected in SELECTED_FILTER.items()):
            continue
        if not _is_true(row.get("mid_falling_member", "")):
            continue
        selected.append(dict(row))
    return sorted(selected, key=lambda row: row.get("operation_key", ""))


def _selected_primary_summary(rows: Sequence[Mapping[str, str]]) -> list[dict[str, str]]:
    return [
        dict(row)
        for row in rows
        if row.get("analysis_basis") == "primary_candidate_retaining"
        and row.get("candidate_variant_id") == "source_mid_falling"
        and all(
            row.get(column, "") == expected
            for column, expected in SELECTED_FILTER.items()
        )
    ]


def _decimal_text(value: object) -> str:
    text = str(value).strip()
    try:
        number = Decimal(text)
    except InvalidOperation as exc:
        raise ValueError(f"invalid decimal {text!r}") from exc
    if not number.is_finite():
        raise ValueError(f"non-finite decimal {text!r}")
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _canonical_generic_value(value: object) -> str:
    text = "" if value is None else str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    if re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        text,
    ):
        unsigned = text.lstrip("+-")
        integer_part = re.split(r"[eE]", unsigned, maxsplit=1)[0].split(
            ".", maxsplit=1
        )[0]
        if not (len(integer_part) > 1 and integer_part.startswith("0")):
            return _decimal_text(text)
    return text


def candidate_detail_row_semantic_sha256(row: Mapping[str, str]) -> str:
    payload = [
        [column, _canonical_generic_value(value)]
        for column, value in sorted(row.items())
        if column not in V3_CANDIDATE_ROW_PROVENANCE_COLUMNS
        and not _is_transport_provenance_name(column)
        and column not in V3_CANDIDATE_POST_HASH_COLUMNS
    ]
    return _canonical_json_sha256(payload)


def _canonical_monthly_value(column: str, value: object) -> str:
    text = "" if value is None else str(value).strip()
    if column == "stock_id":
        return text.split(".", maxsplit=1)[0].zfill(4)
    if column == "revenue_period":
        return re.sub(r"\D", "", text).zfill(6)
    if column == "source_table_date":
        return re.sub(r"\D", "", text).zfill(8)
    if column == "market":
        return text.lower()
    if column == "source_market_name":
        return text.upper()
    if column in RAW_ROW_NUMERIC_COLUMNS:
        return _decimal_text(text) if text else ""
    if column in RAW_ROW_BOOLEAN_COLUMNS:
        lowered = text.lower()
        if lowered not in {"true", "false"}:
            raise ValueError(f"invalid canonical boolean {column}={text!r}")
        return lowered
    return text


def monthly_revenue_row_canonical_sha256(row: Mapping[str, str]) -> str:
    missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(row))
    if missing:
        raise ValueError(f"monthly revenue row missing columns: {missing}")
    values = [
        _canonical_monthly_value(column, row.get(column, ""))
        for column in RAW_ROW_CANONICAL_COLUMNS
    ]
    return _canonical_json_sha256(
        [CANONICAL_JSON_VERSION, list(RAW_ROW_CANONICAL_COLUMNS), values]
    )


def price_history_row_canonical_sha256(row: Mapping[str, str]) -> str:
    missing = sorted(set(PRICE_ROW_CANONICAL_COLUMNS) - set(row))
    if missing:
        raise ValueError(f"price-history row missing columns: {missing}")
    values: list[str] = []
    for column in PRICE_ROW_CANONICAL_COLUMNS:
        text = str(row.get(column, "")).strip()
        if column == "date":
            value = re.sub(r"\D", "", text).zfill(8)
        elif column == "stock_id":
            value = text.split(".", maxsplit=1)[0].zfill(4)
        elif column == "market":
            value = text.lower()
        elif column in PRICE_ROW_NUMERIC_COLUMNS:
            value = _decimal_text(text) if text else ""
        else:
            value = text
        values.append(value)
    return _canonical_json_sha256(
        [CANONICAL_JSON_VERSION, list(PRICE_ROW_CANONICAL_COLUMNS), values]
    )


def _is_true(value: object) -> bool:
    return str(value).strip().lower() == "true"


def _safe_repo_path(repo_root: Path, logical_path: str) -> Path:
    posix = PurePosixPath(logical_path)
    if posix.is_absolute() or ".." in posix.parts or "\\" in logical_path:
        raise ValueError(f"unsafe repository path: {logical_path!r}")
    return repo_root.joinpath(*posix.parts)


def _validate_price_replay(
    repo_root: Path,
    case: ExpectedCase,
    replay: Mapping[str, Any],
) -> list[str]:
    errors: list[str] = []
    path = repo_root / "data/stock_price_history" / f"{case.stock_id}.csv"
    try:
        _columns, rows = _read_csv(path)
    except (OSError, ValueError) as exc:
        return [f"{case.stock_id}: price history unavailable: {exc}"]
    by_date = {row.get("date", ""): row for row in rows}
    if len(by_date) != len(rows):
        errors.append(f"{case.stock_id}: price history contains duplicate dates")
    checks = (
        (case.trigger_date, "close", case.trigger_close, "trigger_close"),
        (case.confirmation_date, "close", case.confirmation_close, "confirmation_close"),
        (case.entry_date, "open", case.entry_open, "entry_open"),
        (case.exit_date, "close", case.exit_close, "exit_close"),
    )
    evidence_row_hashes = replay.get("price_row_canonical_sha256s")
    if not isinstance(evidence_row_hashes, dict):
        errors.append(f"{case.stock_id}: canonical price-row SHA evidence missing")
        evidence_row_hashes = {}
    for date, column, expected, evidence_field in checks:
        row = by_date.get(date)
        if row is None:
            errors.append(f"{case.stock_id}: missing registered price date {date}")
            continue
        try:
            observed = _decimal_text(row.get(column, ""))
            evidence_value = _decimal_text(replay.get(evidence_field, ""))
        except ValueError as exc:
            errors.append(f"{case.stock_id}: {exc}")
            continue
        if observed != _decimal_text(expected) or evidence_value != _decimal_text(expected):
            errors.append(
                f"{case.stock_id}: {evidence_field} mismatch; "
                f"expected={expected}; registered={observed}; evidence={evidence_value}"
            )
        try:
            observed_row_sha = price_history_row_canonical_sha256(row)
        except ValueError as exc:
            errors.append(f"{case.stock_id}: {exc}")
        else:
            evidence_row_sha = evidence_row_hashes.get(evidence_field, "")
            if not SHA256_RE.fullmatch(str(evidence_row_sha)):
                errors.append(
                    f"{case.stock_id}: {evidence_field} canonical price-row SHA malformed"
                )
            elif observed_row_sha != evidence_row_sha:
                errors.append(
                    f"{case.stock_id}: {evidence_field} canonical price-row SHA drifted"
                )
    ordered_dates = [row.get("date", "") for row in rows]
    try:
        trigger_index = ordered_dates.index(case.trigger_date)
        confirmation_index = ordered_dates.index(case.confirmation_date)
        entry_index = ordered_dates.index(case.entry_date)
        exit_index = ordered_dates.index(case.exit_date)
        if confirmation_index != trigger_index + 1 or entry_index != trigger_index + 2:
            errors.append(f"{case.stock_id}: D+1/D+2 session offsets drifted")
        if exit_index != entry_index + 29:
            errors.append(f"{case.stock_id}: D+30 close offset 29 drifted")
    except ValueError:
        pass
    try:
        calculated = (
            (Decimal(case.exit_close) - Decimal(case.entry_open))
            / Decimal(case.entry_open)
            * Decimal("100")
        )
        observed_return = Decimal(str(replay.get("realized_return_pct", "")))
        registered_return = Decimal(case.realized_return_pct)
        if abs(calculated - observed_return) > Decimal("0.00005"):
            errors.append(f"{case.stock_id}: evidence return formula does not replay")
        if abs(observed_return - registered_return) > Decimal("0.00005"):
            errors.append(f"{case.stock_id}: evidence return differs from registered return")
    except (InvalidOperation, ZeroDivisionError):
        errors.append(f"{case.stock_id}: malformed operation replay decimal")
    if replay.get("formula") != "(exit_close-entry_open)/entry_open*100":
        errors.append(f"{case.stock_id}: operation return formula identity drifted")
    query_months = list(
        dict.fromkeys(
            (
                case.trigger_date[:6],
                case.confirmation_date[:6],
                case.entry_date[:6],
                case.exit_date[:6],
            )
        )
    )
    expected_queries = [
        "https://www.twse.com.tw/exchangeReport/STOCK_DAY?"
        f"response=json&date={month}01&stockNo={case.stock_id}"
        for month in query_months
    ]
    if replay.get("official_price_queries") != expected_queries:
        errors.append(f"{case.stock_id}: official TWSE price query identity drifted")
    return errors


def _validate_monthly_lineage(
    repo_root: Path,
    case: ExpectedCase,
    lineage: Mapping[str, Any],
    diagnostics: list[str],
) -> list[str]:
    errors: list[str] = []
    events = lineage.get("monthly_revenue_events")
    if not isinstance(events, list):
        return [f"{case.stock_id}: monthly_revenue_events must be a list"]
    observed_event_identity: list[tuple[str, str, str, str, bool]] = []
    for event in events:
        if not isinstance(event, dict):
            errors.append(f"{case.stock_id}: monthly revenue event is not an object")
            continue
        if not isinstance(event.get("source_anomaly_candidate"), bool):
            errors.append(
                f"{case.stock_id}/{event.get('period', '')}: "
                "source_anomaly_candidate must be an explicit boolean"
            )
            continue
        observed_event_identity.append(
            (
                str(event.get("period", "")),
                str(event.get("source_table_date", "")),
                str(event.get("available_date", "")),
                str(event.get("canonical_row_sha256", "")),
                bool(event["source_anomaly_candidate"]),
            )
        )
    if tuple(observed_event_identity) != case.evidence_monthly_events:
        errors.append(
            f"{case.stock_id}: evidence monthly-revenue event identity drifted"
        )
    try:
        _columns, rows = _read_csv(repo_root / MONTHLY_REVENUE_PATH)
    except (OSError, ValueError) as exc:
        return [f"{case.stock_id}: monthly revenue history unavailable: {exc}"]
    try:
        _price_columns, price_rows = _read_csv(
            repo_root / "data/stock_price_history" / f"{case.stock_id}.csv"
        )
    except (OSError, ValueError) as exc:
        return [f"{case.stock_id}: price calendar unavailable for PIT replay: {exc}"]
    price_dates = sorted(row.get("date", "") for row in price_rows)
    by_key: dict[tuple[str, str], list[dict[str, str]]] = {}
    for source_row in rows:
        key = (
            source_row.get("stock_id", "").zfill(4),
            source_row.get("revenue_period", ""),
        )
        by_key.setdefault(key, []).append(source_row)
    for event in events:
        if not isinstance(event, dict):
            continue
        period = str(event.get("period", ""))
        matched_rows = by_key.get((case.stock_id, period), [])
        if not matched_rows:
            errors.append(f"{case.stock_id}: missing monthly revenue period {period}")
            continue
        if len(matched_rows) != 1:
            errors.append(
                f"{case.stock_id}/{period}: expected exactly one canonical monthly-revenue row; "
                f"actual={len(matched_rows)}"
            )
            continue
        row = matched_rows[0]
        source_table_date = str(event.get("source_table_date", ""))
        available_date = str(event.get("available_date", ""))
        if row.get("source_table_date", "") != source_table_date:
            errors.append(f"{case.stock_id}/{period}: source table date drifted")
        expected_available_date = next(
            (date for date in price_dates if date >= source_table_date),
            "",
        )
        if available_date != expected_available_date:
            errors.append(
                f"{case.stock_id}/{period}: trade-aligned available date drifted"
            )
        try:
            observed_sha = monthly_revenue_row_canonical_sha256(row)
        except ValueError as exc:
            errors.append(f"{case.stock_id}/{period}: {exc}")
            continue
        expected_sha = str(event.get("canonical_row_sha256", ""))
        if observed_sha != expected_sha:
            errors.append(
                f"{case.stock_id}/{period}: canonical monthly-revenue row SHA drifted"
            )
        if isinstance(event.get("source_anomaly_candidate"), bool):
            observed_flag = _is_true(row.get("revenue_numerical_anomaly_flag", ""))
            if observed_flag is not bool(event["source_anomaly_candidate"]):
                errors.append(f"{case.stock_id}/{period}: anomaly flag drifted")
        source_url = str(event.get("source_url", ""))
        if not source_url.startswith("https://mopsov.twse.com.tw/nas/t21/"):
            errors.append(f"{case.stock_id}/{period}: official MOPS source URL missing")
        elif source_url != row.get("source_url", ""):
            errors.append(f"{case.stock_id}/{period}: official MOPS source URL drifted")
        raw_hash = str(event.get("raw_file_sha256_diagnostic", ""))
        source_file = row.get("source_file", "")
        if raw_hash and source_file:
            try:
                observed_raw = hashlib.sha256(
                    _safe_repo_path(repo_root, source_file).read_bytes()
                ).hexdigest()
                if observed_raw != raw_hash:
                    diagnostics.append(
                        f"{case.stock_id}/{period}: raw source SHA differs; "
                        "canonical semantic row remains the hard gate"
                    )
            except OSError as exc:
                diagnostics.append(
                    f"{case.stock_id}/{period}: raw source diagnostic unavailable: {exc}"
                )
    return errors


def _validate_independent_corroboration(
    repo_root: Path,
    case: ExpectedCase,
    corroboration: Mapping[str, Any],
) -> list[str]:
    errors: list[str] = []
    if corroboration.get("independent_underlying_measurement") is not False:
        errors.append(
            f"{case.stock_id}: corroboration must not claim an independent "
            "underlying measurement"
        )
    if corroboration.get("classification") != (
        "independent_public_provider_corroboration"
    ):
        errors.append(f"{case.stock_id}: independent corroboration classification drifted")
    if not str(corroboration.get("finding", "")).strip():
        errors.append(f"{case.stock_id}: independent corroboration finding missing")
    sources = corroboration.get("sources")
    if not isinstance(sources, list) or not sources or any(
        not isinstance(source, str) or not source.startswith("https://")
        for source in sources
    ):
        errors.append(f"{case.stock_id}: independent corroboration URLs missing")
        sources = []
    else:
        invalid_hosts = sorted(
            {
                urlsplit(source).hostname or ""
                for source in sources
                if (urlsplit(source).hostname or "")
                not in INDEPENDENT_CORROBORATION_HOSTS
            }
        )
        if invalid_hosts:
            errors.append(
                f"{case.stock_id}: unapproved corroboration hosts {invalid_hosts}"
            )
    facts = corroboration.get("observed_facts")
    if not isinstance(facts, list) or not facts:
        return [*errors, f"{case.stock_id}: independent corroboration facts missing"]
    try:
        _monthly_columns, monthly_rows = _read_csv(repo_root / MONTHLY_REVENUE_PATH)
        _price_columns, price_rows = _read_csv(
            repo_root / "data/stock_price_history" / f"{case.stock_id}.csv"
        )
    except (OSError, ValueError) as exc:
        return [*errors, f"{case.stock_id}: corroboration replay source unavailable: {exc}"]
    monthly_by_period: dict[str, list[dict[str, str]]] = {}
    for row in monthly_rows:
        if row.get("stock_id", "").zfill(4) == case.stock_id:
            monthly_by_period.setdefault(row.get("revenue_period", ""), []).append(row)
    price_by_date = {row.get("date", ""): row for row in price_rows}
    if len(price_by_date) != len(price_rows):
        errors.append(f"{case.stock_id}: price history contains duplicate dates")
    seen_fact_keys: set[tuple[str, str]] = set()
    for index, fact in enumerate(facts):
        label = f"{case.stock_id}: corroboration fact[{index}]"
        if not isinstance(fact, dict):
            errors.append(f"{label} must be an object")
            continue
        if fact.get("stock_id") != case.stock_id:
            errors.append(f"{label} stock_id mismatch")
        source_url = fact.get("source_url")
        if source_url not in sources:
            errors.append(f"{label} source_url is not registered in sources")
        elif (urlsplit(str(source_url)).hostname or "") not in (
            INDEPENDENT_CORROBORATION_HOSTS
        ):
            errors.append(f"{label} source_url host is not independent allowlisted")
        fact_kind = fact.get("fact_kind")
        if fact_kind == "public_provider_monthly_revenue_report":
            period = str(fact.get("revenue_period", ""))
            fact_key = (str(fact_kind), period)
            matched = monthly_by_period.get(period, [])
            if len(matched) != 1:
                errors.append(
                    f"{label} must bind exactly one canonical monthly-revenue row"
                )
                continue
            row = matched[0]
            comparisons = {
                "provider_reported_monthly_revenue_thousand_twd": row.get(
                    "monthly_revenue", ""
                ),
                "canonical_monthly_revenue_thousand_twd": row.get(
                    "monthly_revenue", ""
                ),
                "canonical_yoy_pct": row.get("latest_revenue_yoy_pct", ""),
            }
            for field, expected in comparisons.items():
                try:
                    observed = _decimal_text(fact.get(field, ""))
                    canonical = _decimal_text(expected)
                except ValueError as exc:
                    errors.append(f"{label} {field}: {exc}")
                    continue
                if observed != canonical:
                    errors.append(f"{label} {field} does not match canonical row")
            try:
                provider_yoy = Decimal(
                    _decimal_text(fact.get("provider_reported_yoy_pct", ""))
                )
                canonical_yoy = Decimal(
                    _decimal_text(row.get("latest_revenue_yoy_pct", ""))
                )
            except (InvalidOperation, ValueError) as exc:
                errors.append(f"{label} malformed provider YoY: {exc}")
                continue
            delta = abs(provider_yoy - canonical_yoy)
            expected_result = (
                "monthly_revenue_and_yoy_exact"
                if delta == 0
                else "monthly_revenue_exact_yoy_display_rounding_only"
            )
            if delta > Decimal("0.011"):
                errors.append(f"{label} provider YoY differs beyond display rounding")
            if fact.get("comparison_result") != expected_result:
                errors.append(f"{label} comparison_result mismatch")
        elif fact_kind == "public_provider_daily_price_report":
            date = str(fact.get("date", ""))
            fact_key = (str(fact_kind), date)
            row = price_by_date.get(date)
            if row is None:
                errors.append(f"{label} registered price row is missing")
                continue
            for price_field in ("open", "high", "low", "close"):
                evidence_field = f"provider_reported_{price_field}"
                try:
                    observed = _decimal_text(fact.get(evidence_field, ""))
                    registered = _decimal_text(row.get(price_field, ""))
                except ValueError as exc:
                    errors.append(f"{label} {evidence_field}: {exc}")
                    continue
                if observed != registered:
                    errors.append(
                        f"{label} {evidence_field} does not match registered row"
                    )
            if fact.get("comparison_result") != "exact_match_registered_price_row":
                errors.append(f"{label} comparison_result mismatch")
        else:
            errors.append(f"{label} unsupported fact_kind {fact_kind!r}")
            continue
        if fact_key in seen_fact_keys:
            errors.append(f"{label} duplicates a corroboration fact identity")
        seen_fact_keys.add(fact_key)
    expected_fact_count = 2 if case.stock_id == "2478" else 1
    if len(facts) != expected_fact_count:
        errors.append(
            f"{case.stock_id}: corroboration fact count mismatch; "
            f"expected={expected_fact_count}; actual={len(facts)}"
        )
    return errors


def _validate_evidence(
    repo_root: Path,
    row: Mapping[str, str],
    case: ExpectedCase,
    diagnostics: list[str],
) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    match = EVIDENCE_REFERENCE_RE.fullmatch(row.get("evidence_reference", ""))
    if match is None:
        return None, [f"{case.stock_id}: malformed canonical evidence reference"]
    if match.group("evidence_id") != case.evidence_id:
        errors.append(f"{case.stock_id}: evidence_id mismatch")
    if match.group("path") != case.evidence_path:
        errors.append(f"{case.stock_id}: evidence path mismatch")
    try:
        path = _safe_repo_path(repo_root, match.group("path"))
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        return None, [*errors, f"{case.stock_id}: evidence cannot be read: {exc}"]
    if not isinstance(document, dict):
        return None, [*errors, f"{case.stock_id}: evidence root must be an object"]
    if document.get("schema_version") != EVIDENCE_SCHEMA_VERSION:
        errors.append(f"{case.stock_id}: evidence schema version mismatch")
    if document.get("evidence_id") != case.evidence_id:
        errors.append(f"{case.stock_id}: document evidence_id mismatch")
    observed_evidence_sha = evidence_canonical_sha256(document)
    if observed_evidence_sha != match.group("canonical_sha256"):
        errors.append(f"{case.stock_id}: evidence canonical semantic SHA mismatch")
    if not SHA256_RE.fullmatch(case.evidence_canonical_sha256):
        errors.append(f"{case.stock_id}: immutable expected evidence SHA is malformed")
    elif observed_evidence_sha != case.evidence_canonical_sha256:
        errors.append(f"{case.stock_id}: evidence differs from immutable expected semantics")
    payload = document.get("semantic_payload")
    if not isinstance(payload, dict):
        return document, [*errors, f"{case.stock_id}: semantic_payload missing"]
    if payload.get("model_id") != MODEL_ID or payload.get("operation_key") != row.get(
        "operation_key"
    ):
        errors.append(f"{case.stock_id}: evidence model/operation identity mismatch")
    identity = payload.get("identity")
    if not isinstance(identity, dict):
        errors.append(f"{case.stock_id}: evidence identity missing")
        identity = {}
    expected_identity = {
        "stock_id": case.stock_id,
        "stock_name": case.stock_name,
        "trigger_date": case.trigger_date,
        "confirmation_date": case.confirmation_date,
        "entry_date": case.entry_date,
        "exit_date": case.exit_date,
        "candidate_v2_row_sha256": case.candidate_v2_row_sha256,
        "candidate_v3_row_sha256": case.candidate_v3_row_sha256,
    }
    for field, expected in expected_identity.items():
        if identity.get(field) != expected:
            errors.append(f"{case.stock_id}: evidence identity.{field} mismatch")
    attribution = payload.get("attribution")
    expected_attribution = {
        "candidate_kind": case.candidate_kind,
        "anomaly_attribution_mode": case.anomaly_attribution_mode,
        "source_event_periods": list(case.anomaly_source_event_periods),
        "source_table_dates": list(case.anomaly_source_source_dates),
        "source_available_dates": list(case.anomaly_source_available_dates),
        "source_canonical_row_sha256s": list(
            case.anomaly_source_canonical_row_sha256s
        ),
        "anomaly_attribution_note": case.anomaly_attribution_note,
    }
    if attribution != expected_attribution:
        errors.append(f"{case.stock_id}: evidence attribution identity mismatch")
    root_checks = payload.get("root_checks")
    if not isinstance(root_checks, dict):
        return document, [*errors, f"{case.stock_id}: root_checks missing"]
    for registry_column, evidence_key in ROOT_CHECK_EVIDENCE_KEYS.items():
        check = root_checks.get(evidence_key)
        if row.get(registry_column) != "pass":
            errors.append(f"{case.stock_id}: registry {registry_column} must be pass")
        if not isinstance(check, dict) or check.get("status") != "pass":
            errors.append(f"{case.stock_id}: evidence {evidence_key} must pass")
    identity_check = root_checks.get("identity_non_overlap")
    if not isinstance(identity_check, dict) or not str(
        identity_check.get("finding", "")
    ).strip():
        errors.append(f"{case.stock_id}: identity/non-overlap finding missing")
    replay = root_checks.get("formal_operation_replay")
    if isinstance(replay, dict):
        errors.extend(_validate_price_replay(repo_root, case, replay))
    lineage = root_checks.get("raw_source_lineage")
    if isinstance(lineage, dict):
        errors.extend(_validate_monthly_lineage(repo_root, case, lineage, diagnostics))
        if lineage.get("price_history_path") != (
            f"data/stock_price_history/{case.stock_id}.csv"
        ):
            errors.append(f"{case.stock_id}: registered price-history path drifted")
    pit_check = root_checks.get("pit_calendar_continuity")
    if not isinstance(pit_check, dict) or not str(pit_check.get("finding", "")).strip():
        errors.append(f"{case.stock_id}: PIT/calendar finding missing")
    units = root_checks.get("units_formula_adjustment")
    if not isinstance(units, dict):
        errors.append(f"{case.stock_id}: unit/formula evidence missing")
    else:
        if units.get("price_unit") != "TWD_per_share":
            errors.append(f"{case.stock_id}: price unit mismatch")
        if units.get("revenue_unit") != "thousand_TWD":
            errors.append(f"{case.stock_id}: revenue unit mismatch")
        if not str(units.get("operation_basis", "")).strip():
            errors.append(f"{case.stock_id}: operation-basis evidence missing")
        exact_operation_basis = {
            "entry_price_basis": "next_trading_day_open_after_close_confirmation",
            "exit_price_basis": "fixed_d30_close_offset29",
            "intraday_operation_basis_used": False,
        }
        for field, expected in exact_operation_basis.items():
            if units.get(field) != expected:
                errors.append(f"{case.stock_id}: structured operation basis mismatch: {field}")
    corroboration = root_checks.get("independent_source_corroboration")
    if isinstance(corroboration, dict):
        errors.extend(
            _validate_independent_corroboration(repo_root, case, corroboration)
        )
    event_history = root_checks.get("authoritative_event_history")
    if isinstance(event_history, dict):
        expected_params = {
            "stockNo": case.stock_id,
            "startDate": case.trigger_date,
            "endDate": case.exit_date,
        }
        if event_history.get("request_params") != expected_params:
            errors.append(f"{case.stock_id}: official event-history request params drifted")
        if event_history.get("query_window") != (
            f"{case.trigger_date}..{case.exit_date}"
        ):
            errors.append(f"{case.stock_id}: official event-history query window drifted")
        official_sources = event_history.get("official_sources")
        if not isinstance(official_sources, list) or not official_sources:
            errors.append(f"{case.stock_id}: official event-history sources missing")
        elif not OFFICIAL_EVENT_HISTORY_BASE_URLS.issubset(set(official_sources)):
            errors.append(f"{case.stock_id}: official TWSE event-history surfaces missing")
        if not str(event_history.get("finding", "")).strip():
            errors.append(f"{case.stock_id}: authoritative event-history finding missing")
    reproducible = root_checks.get("reproducible_evidence_reference")
    if not isinstance(reproducible, dict) or not str(
        reproducible.get("replay_basis", "")
    ).strip():
        errors.append(f"{case.stock_id}: reproducible replay basis missing")
    disposition = payload.get("disposition")
    if not isinstance(disposition, dict):
        errors.append(f"{case.stock_id}: evidence disposition missing")
    else:
        for field in ("final_disposition", "primary_handling", "promotion_gate_status"):
            if disposition.get(field) != row.get(field):
                errors.append(f"{case.stock_id}: evidence disposition.{field} mismatch")
        for field in (
            "repair_satisfaction_status",
            "effective_anomaly_gate_status",
        ):
            if disposition.get(field) != row.get(field):
                errors.append(f"{case.stock_id}: evidence disposition.{field} mismatch")
    provenance = document.get("provenance")
    if not isinstance(provenance, dict) or provenance.get(
        "raw_byte_identity_policy"
    ) != "diagnostic_only_not_promotion_gate":
        errors.append(f"{case.stock_id}: raw-byte provenance policy is not diagnostic-only")
    if not isinstance(provenance, dict) or provenance.get("retrieved_at") != case.reviewed_at:
        errors.append(f"{case.stock_id}: evidence reviewed timestamp mismatch")
    return document, errors


def _selected_rows(detail_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return _selected_business_rows(detail_rows)


def _key_set_sha256(keys: Sequence[str]) -> str:
    return _canonical_json_sha256(sorted(keys))


def _candidate_row_set_sha256(rows: Sequence[Mapping[str, str]]) -> str:
    return _canonical_json_sha256(
        sorted(
            [
                {
                    "operation_key": row.get("operation_key", ""),
                    "candidate_detail_row_sha256": row.get(
                        "candidate_detail_row_sha256", ""
                    ),
                }
                for row in rows
            ],
            key=lambda item: item["operation_key"],
        )
    )


def _metric_signature(rows: Sequence[Mapping[str, str]]) -> str:
    returns = [Decimal(row.get("realized_return_pct", "")) for row in rows]
    wins = sum(value > 0 for value in returns)
    neutral = sum(value == 0 for value in returns)
    failures = sum(value < 0 for value in returns)
    ordered = sorted(returns)
    median = ordered[len(ordered) // 2]
    average = sum(returns) / Decimal(len(returns))
    win_rate = Decimal(wins) / Decimal(len(returns)) * Decimal("100")
    stocks = {row.get("stock_id", "") for row in rows}
    episodes = {row.get("episode_key", "") for row in rows}
    return (
        f"operation_count={len(rows)};unique_stock_count={len(stocks)};"
        f"unique_episode_count={len(episodes)};win_count={wins};neutral_count={neutral};"
        f"failure_count={failures};win_rate_pct={win_rate.quantize(Decimal('0.0001'))};"
        f"avg_return_pct={average.quantize(Decimal('0.0001')).normalize()};"
        f"median_return_pct={median.normalize()}"
    )


def _sensitivity_metric_signature(rows: Sequence[Mapping[str, str]]) -> str:
    included = [row for row in rows if _is_true(row.get("sensitivity_included", ""))]
    returns = [Decimal(row.get("realized_return_pct", "")) for row in included]
    wins = sum(value > 0 for value in returns)
    failures = sum(value < 0 for value in returns)
    ordered = sorted(returns)
    median = ordered[len(ordered) // 2]
    average = sum(returns) / Decimal(len(returns))
    win_rate = Decimal(wins) / Decimal(len(returns)) * Decimal("100")
    return (
        f"operation_count={len(included)};win_count={wins};failure_count={failures};"
        f"win_rate_pct={win_rate.quantize(Decimal('0.0001'))};"
        f"avg_return_pct={average.quantize(Decimal('0.0001')).normalize()};"
        f"median_return_pct={median.normalize()}"
    )


def _validate_repair_closure(
    repo_root: Path,
    registry_rows: Mapping[str, Mapping[str, str]],
    diagnostics: list[str],
) -> tuple[bool, list[str]]:
    errors: list[str] = []
    path = repo_root / REPAIR_CLOSURE_PATH
    try:
        columns, rows = _read_csv(path)
    except (OSError, ValueError) as exc:
        return False, [f"repair closure registry unavailable: {exc}"]
    if tuple(columns) != REPAIR_CLOSURE_COLUMNS:
        errors.append("repair closure registry columns must match the exact contract")
    if len(rows) != 1:
        return False, [*errors, f"repair closure registry must contain exact one row; actual={len(rows)}"]
    row = rows[0]
    exact = {
        "repair_id": REPAIR_ID,
        "repair_date": "2026-08-29",
        "model_id": MODEL_ID,
        "operation_key": REPAIR_OPERATION_KEY,
        "root_cause": "derived_attribution_future_leakage_episode_any_flag_applied_before_source_available_date",
        "source_owner_lane": "research_backtest",
        "from_candidate_artifact_version": "low_mid_falling_candidate_v2_20260822",
        "to_source_first_artifact_version": "source_first_condition_v3_20260720",
        "to_rearmed_artifact_version": "rearmed_operation_grid_v3_20260829",
        "to_operation_lag_artifact_version": "operation_lag_bucket_v3_20260829",
        "to_position_shape_artifact_version": "position_shape_transition_matrix_v3_20260829",
        "to_candidate_artifact_version": "low_mid_falling_candidate_v3_20260829",
        "before_baseline_commit": V2_CANDIDATE_BASELINE_COMMIT,
        "before_candidate_summary_path": V2_CANDIDATE_SUMMARY_PATH.as_posix(),
        "before_candidate_detail_path": V2_CANDIDATE_DETAIL_PATH.as_posix(),
        "candidate_summary_path": V3_CANDIDATE_SUMMARY_PATH.as_posix(),
        "candidate_detail_path": V3_CANDIDATE_DETAIL_PATH.as_posix(),
        "before_candidate_detail_row_sha256": EXPECTED_CASES[
            REPAIR_OPERATION_KEY
        ].candidate_v2_row_sha256,
        "operation_business_field_change_count": "0",
        "primary_metric_rerun_completed": "True",
        "trigger_asof_event_periods": "202504|202509",
        "trigger_asof_available_dates": "20250519|20251017",
        "trigger_asof_canonical_row_sha256s": (
            "1cb88da0fb389f1e4775c6ae2c05d1c4813d7c584e9e2fc0ba7183d4bf7e1e71|"
            "d8d8792b836c414d9356e174e055619cc9eedf4627a8f52235bb4994cf2f495b"
        ),
        "excluded_future_event_periods": "202512",
        "excluded_future_available_dates": "20260119",
        "excluded_future_canonical_row_sha256s": (
            "d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1"
        ),
        "selected_operation_count": "53",
        "primary_metric_signature": PRIMARY_METRIC_SIGNATURE,
        "sensitivity_metric_signature": SENSITIVITY_METRIC_SIGNATURE,
        "rule_formula_sha256": RULE_FORMULA_SHA256,
        "operation_identity_preserved": "True",
        "primary_metrics_preserved": "True",
        "repair_status": "verified_repaired_rerun_complete",
        "authorization_reference": "user_authorized_3A_3C_20260829",
        "research_only": "True",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "production_change": "False",
    }
    for field, expected in exact.items():
        if row.get(field, "") != expected:
            errors.append(
                f"repair closure {field} mismatch: expected={expected!r}; actual={row.get(field, '')!r}"
            )
    raw_diagnostics = {
        "trigger_asof_raw_file_sha256s_diagnostic": (
            "4eba010d3afeb2b50f3b6e88a60fb699bfad9d34b1e991c0cc8b898775b1231f|"
            "6bb7ac7c837884520e1aae63cd2d12ba2f2da7a88117d9308e39fab94842426e"
        ),
        "excluded_future_raw_file_sha256s_diagnostic": (
            "d30e0dab4891bc9fc8d8416b911a0b04d2e9d167a8411dc0794de6f6a414eabc"
        ),
    }
    for field, expected in raw_diagnostics.items():
        if row.get(field, "") != expected:
            diagnostics.append(
                f"repair closure {field} differs; canonical revenue rows remain the hard gate"
            )
    repair_row = registry_rows.get(REPAIR_OPERATION_KEY, {})
    if row.get("after_candidate_detail_row_sha256") != repair_row.get(
        "candidate_detail_row_sha256"
    ):
        errors.append("repair closure after candidate row SHA does not bind v3 registry")
    for field in (
        "selected_operation_business_row_set_sha256_before",
        "selected_operation_business_row_set_sha256_after",
        "primary_metrics_semantic_sha256_before",
        "primary_metrics_semantic_sha256_after",
        "anomaly_attribution_row_set_sha256_before",
        "anomaly_attribution_row_set_sha256_after",
    ):
        if not SHA256_RE.fullmatch(row.get(field, "")):
            errors.append(f"repair closure {field} must be an exact SHA-256")
    if row.get("selected_operation_business_row_set_sha256_before") != row.get(
        "selected_operation_business_row_set_sha256_after"
    ):
        errors.append("repair closure operation business row-set changed")
    if row.get("primary_metrics_semantic_sha256_before") != row.get(
        "primary_metrics_semantic_sha256_after"
    ):
        errors.append("repair closure primary metric semantics changed")
    if row.get("anomaly_attribution_row_set_sha256_before") == row.get(
        "anomaly_attribution_row_set_sha256_after"
    ):
        errors.append("repair closure anomaly attribution row-set did not change")
    try:
        summary_path = _safe_repo_path(repo_root, row.get("candidate_summary_path", ""))
        detail_path = _safe_repo_path(repo_root, row.get("candidate_detail_path", ""))
        summary_sha = artifact_semantic_sha256(summary_path)
        detail_sha = artifact_semantic_sha256(detail_path)
        _summary_columns, summary_rows = _read_csv(summary_path)
        _detail_columns, detail_rows = _read_csv(detail_path)
        before_summary_bytes = _read_git_blob(
            repo_root,
            commit_sha=V2_CANDIDATE_BASELINE_COMMIT,
            logical_path=V2_CANDIDATE_SUMMARY_PATH,
        )
        before_detail_bytes = _read_git_blob(
            repo_root,
            commit_sha=V2_CANDIDATE_BASELINE_COMMIT,
            logical_path=V2_CANDIDATE_DETAIL_PATH,
        )
        _before_summary_columns, before_summary_rows = _read_csv_bytes(
            before_summary_bytes,
            source_name=(
                f"{V2_CANDIDATE_BASELINE_COMMIT}:"
                f"{V2_CANDIDATE_SUMMARY_PATH.as_posix()}"
            ),
        )
        _before_detail_columns, before_detail_rows = _read_csv_bytes(
            before_detail_bytes,
            source_name=(
                f"{V2_CANDIDATE_BASELINE_COMMIT}:"
                f"{V2_CANDIDATE_DETAIL_PATH.as_posix()}"
            ),
        )
    except (OSError, ValueError) as exc:
        return False, [*errors, f"repair closure artifact unavailable: {exc}"]
    if summary_sha != row.get("candidate_summary_canonical_sha256"):
        errors.append("repair closure candidate summary canonical semantic SHA mismatch")
    if detail_sha != row.get("candidate_detail_canonical_sha256"):
        errors.append("repair closure candidate detail canonical semantic SHA mismatch")
    if summary_sha != V3_CANDIDATE_SUMMARY_SEMANTIC_SHA256:
        errors.append("repaired v3 candidate summary drifted from the exact semantic pin")
    if detail_sha != V3_CANDIDATE_DETAIL_SEMANTIC_SHA256:
        errors.append("repaired v3 candidate detail drifted from the exact semantic pin")
    if len(summary_rows) != V3_CANDIDATE_SUMMARY_ROW_COUNT:
        errors.append("repaired v3 candidate summary row count drifted")
    if len(detail_rows) != V3_CANDIDATE_DETAIL_ROW_COUNT:
        errors.append("repaired v3 candidate detail row count drifted")
    if any(
        item.get("artifact_version") != "low_mid_falling_candidate_v3_20260829"
        for item in [*summary_rows, *detail_rows]
    ):
        errors.append("repaired v3 candidate artifact version drifted")
    before_summary_sha = legacy_artifact_bytes_semantic_sha256(
        before_summary_bytes,
        source_name=(
            f"{V2_CANDIDATE_BASELINE_COMMIT}:"
            f"{V2_CANDIDATE_SUMMARY_PATH.as_posix()}"
        ),
    )
    before_detail_sha = legacy_artifact_bytes_semantic_sha256(
        before_detail_bytes,
        source_name=(
            f"{V2_CANDIDATE_BASELINE_COMMIT}:"
            f"{V2_CANDIDATE_DETAIL_PATH.as_posix()}"
        ),
    )
    if row.get("before_candidate_summary_canonical_sha256") != before_summary_sha:
        errors.append("repair closure immutable v2 summary semantic SHA mismatch")
    if row.get("before_candidate_detail_canonical_sha256") != before_detail_sha:
        errors.append("repair closure immutable v2 detail semantic SHA mismatch")
    if not before_summary_rows or not before_detail_rows:
        errors.append("immutable v2 baseline artifacts must be non-empty")
    if any(
        item.get("artifact_version") != V2_CANDIDATE_ARTIFACT_VERSION
        for item in [*before_summary_rows, *before_detail_rows]
    ):
        errors.append("immutable v2 baseline artifact version drifted")
    before_business_rows = _selected_business_rows(before_detail_rows)
    after_business_rows = _selected_business_rows(detail_rows)
    before_primary_rows = _selected_primary_summary(before_summary_rows)
    after_primary_rows = _selected_primary_summary(summary_rows)
    if len(before_business_rows) != 53 or len(after_business_rows) != 53:
        errors.append("repair closure business projections must contain exact 53 rows")
    if len(before_primary_rows) != 1 or len(after_primary_rows) != 1:
        errors.append("repair closure primary summaries must contain exact one row")
    before_by_key = {
        item.get("operation_key", ""): item for item in before_business_rows
    }
    after_by_key = {
        item.get("operation_key", ""): item for item in after_business_rows
    }
    if set(before_by_key) != set(after_by_key):
        errors.append("repair closure operation-key set changed across repair")
    business_field_change_count = sum(
        _canonical_generic_value(before_by_key[operation_key].get(field, ""))
        != _canonical_generic_value(after_by_key[operation_key].get(field, ""))
        for operation_key in set(before_by_key) & set(after_by_key)
        for field in SELECTED_BUSINESS_COLUMNS
    )
    if str(business_field_change_count) != row.get(
        "operation_business_field_change_count"
    ):
        errors.append(
            "repair closure operation business field change count does not replay"
        )
    changed_attribution_keys = {
        operation_key
        for operation_key in set(before_by_key) & set(after_by_key)
        if any(
            before_by_key[operation_key].get(field, "")
            != after_by_key[operation_key].get(field, "")
            for field in ANOMALY_ATTRIBUTION_COLUMNS
        )
    }
    if changed_attribution_keys != {REPAIR_OPERATION_KEY}:
        errors.append(
            "repair closure attribution diff must change only the exact 6177 "
            f"operation; actual={sorted(changed_attribution_keys)}"
        )
    recomputed_repair_bindings = {
        "selected_operation_business_row_set_sha256_before": (
            _records_semantic_sha256(
                before_business_rows, SELECTED_BUSINESS_COLUMNS, row_set=True
            )
        ),
        "selected_operation_business_row_set_sha256_after": (
            _records_semantic_sha256(
                after_business_rows, SELECTED_BUSINESS_COLUMNS, row_set=True
            )
        ),
        "primary_metrics_semantic_sha256_before": _records_semantic_sha256(
            before_primary_rows, PRIMARY_METRIC_COLUMNS, row_set=False
        ),
        "primary_metrics_semantic_sha256_after": _records_semantic_sha256(
            after_primary_rows, PRIMARY_METRIC_COLUMNS, row_set=False
        ),
        "anomaly_attribution_row_set_sha256_before": _records_semantic_sha256(
            before_business_rows, ANOMALY_ATTRIBUTION_COLUMNS, row_set=True
        ),
        "anomaly_attribution_row_set_sha256_after": _records_semantic_sha256(
            after_business_rows, ANOMALY_ATTRIBUTION_COLUMNS, row_set=True
        ),
    }
    for field, observed in recomputed_repair_bindings.items():
        if row.get(field) != observed:
            errors.append(f"repair closure independently recomputed {field} mismatch")
    selected = _selected_rows(detail_rows)
    keys = [item.get("operation_key", "") for item in selected]
    if len(selected) != 53 or len(keys) != len(set(keys)):
        errors.append("repaired selected candidate set must contain 53 unique operations")
    if any(not _is_true(item.get("primary_included", "")) for item in selected):
        errors.append("repaired selected candidate set must retain every row in Primary")
    key_sha = _key_set_sha256(keys)
    row_set_sha = _candidate_row_set_sha256(selected)
    current_anomaly_keys = sorted(
        item.get("operation_key", "")
        for item in selected
        if _is_true(item.get("combined_exclusion_candidate_flag", ""))
    )
    current_anomaly_sha = _key_set_sha256(current_anomaly_keys)
    bindings = {
        "selected_operation_key_set_sha256": key_sha,
        "selected_candidate_row_set_sha256": row_set_sha,
        "current_anomaly_operation_key_set_sha256": current_anomaly_sha,
    }
    for field, observed in bindings.items():
        if row.get(field) != observed:
            errors.append(f"repair closure {field} mismatch")
    try:
        if _metric_signature(selected) != PRIMARY_METRIC_SIGNATURE:
            errors.append("repaired primary metric signature drifted")
        if _sensitivity_metric_signature(selected) != SENSITIVITY_METRIC_SIGNATURE:
            errors.append("repaired sensitivity metric signature drifted")
    except (InvalidOperation, ZeroDivisionError):
        errors.append("repaired candidate metrics contain malformed returns")
    if len(current_anomaly_keys) != 8 or set(current_anomaly_keys) != (
        set(EXPECTED_CASES) - {REPAIR_OPERATION_KEY}
    ):
        errors.append("repaired current anomaly set must be the exact eight verified real extremes")
    selected_by_key = {item.get("operation_key", ""): item for item in selected}
    for operation_key, registry_row in registry_rows.items():
        selected_row = selected_by_key.get(operation_key)
        if selected_row is None:
            errors.append(f"repair closure missing selected operation {operation_key}")
            continue
        if selected_row.get("candidate_detail_row_sha256") != registry_row.get(
            "candidate_detail_row_sha256"
        ):
            errors.append(f"repair closure candidate row SHA mismatch: {operation_key}")
        if selected_row.get("artifact_version") != "low_mid_falling_candidate_v3_20260829":
            errors.append(f"repair closure candidate row version mismatch: {operation_key}")
        if candidate_detail_row_semantic_sha256(selected_row) != selected_row.get(
            "candidate_detail_row_sha256"
        ):
            errors.append(
                f"repair closure candidate canonical semantic row SHA mismatch: {operation_key}"
            )
    repaired = selected_by_key.get(REPAIR_OPERATION_KEY, {})
    if _is_true(repaired.get("source_anomaly_candidate_flag", "")) or _is_true(
        repaired.get("combined_exclusion_candidate_flag", "")
    ):
        errors.append("6177 repaired row still carries the future-contaminated anomaly flag")
    expected_after_flags = {
        operation_key: {
            "source_anomaly_candidate_flag": operation_key
            not in {REPAIR_OPERATION_KEY}
            and case.candidate_kind == "source_anomaly_candidate",
            "unresolved_price_path_candidate_flag": False,
            "operation_return_review_candidate_flag": (
                case.candidate_kind == "operation_return_review_candidate"
            ),
            "combined_exclusion_candidate_flag": operation_key
            != REPAIR_OPERATION_KEY,
            "primary_included": True,
            "sensitivity_included": operation_key == REPAIR_OPERATION_KEY,
        }
        for operation_key, case in EXPECTED_CASES.items()
    }
    for operation_key, expected_flags in expected_after_flags.items():
        candidate = selected_by_key.get(operation_key, {})
        for field, expected in expected_flags.items():
            if candidate.get(field, "") != str(expected):
                errors.append(
                    f"repair closure exact attribution flag mismatch: "
                    f"{operation_key}/{field}"
                )
    before_repaired = before_by_key.get(REPAIR_OPERATION_KEY, {})
    expected_before_repaired_flags = {
        "source_anomaly_candidate_flag": "True",
        "unresolved_price_path_candidate_flag": "False",
        "operation_return_review_candidate_flag": "False",
        "combined_exclusion_candidate_flag": "True",
        "primary_included": "True",
        "sensitivity_included": "False",
    }
    for field, expected in expected_before_repaired_flags.items():
        if before_repaired.get(field, "") != expected:
            errors.append(f"immutable v2 6177 attribution flag mismatch: {field}")
    exact_repaired_pit = {
        "asof_latest_qualifying_revenue_period": "202509",
        "asof_latest_qualifying_source_date": "20251017",
        "asof_latest_qualifying_source_row_canonical_sha256": (
            "d8d8792b836c414d9356e174e055619cc9eedf4627a8f52235bb4994cf2f495b"
        ),
        "asof_latest_qualifying_canonical_source_table_date": "20251017",
        "asof_latest_qualifying_trade_date": "20251017",
        "asof_latest_qualifying_sequence_index": "133",
        "latest_source_to_trigger_trading_days": "33",
        "future_qualifying_update_ignored_count": "6",
    }
    for field, expected in exact_repaired_pit.items():
        if repaired.get(field, "") != expected:
            errors.append(f"6177 repaired trigger-as-of PIT identity mismatch: {field}")
    if (
        repaired.get("asof_latest_qualifying_revenue_period") == "202512"
        or repaired.get("asof_latest_qualifying_source_row_canonical_sha256")
        == "d26bc6a94cf5869836e96f77b7af128b007b3159ae7680eb4e14030c7d19aae1"
    ):
        errors.append("6177 repaired row still uses the excluded future 202512 source")
    return not errors, errors


def _validate_migration(
    repo_root: Path,
    registry_rows: Mapping[str, Mapping[str, str]],
) -> list[str]:
    errors: list[str] = []
    try:
        columns, rows = _read_csv(repo_root / MIGRATION_PATH)
    except (OSError, ValueError) as exc:
        return [f"anomaly disposition migration unavailable: {exc}"]
    if tuple(columns) != MIGRATION_COLUMNS:
        errors.append("anomaly disposition migration columns must match the exact contract")
    if len(rows) != 1:
        return [*errors, f"anomaly disposition migration must contain exact one row; actual={len(rows)}"]
    row = rows[0]
    from_path = repo_root / LEGACY_V2_REGISTRY_PATH
    to_path = repo_root / REGISTRY_PATH
    try:
        from_sha = csv_semantic_sha256(
            from_path, excluded_columns=REGISTRY_PROVENANCE_COLUMNS
        )
        to_sha = csv_semantic_sha256(
            to_path, excluded_columns=REGISTRY_PROVENANCE_COLUMNS
        )
    except (OSError, ValueError) as exc:
        return [*errors, f"anomaly registry semantic SHA unavailable: {exc}"]
    if from_sha != LEGACY_V2_REGISTRY_CANONICAL_SHA256:
        errors.append(
            "legacy v2 anomaly registry semantic drifted from the immutable approved baseline"
        )
    exact = {
        "migration_id": "revenue_unreacted_range_anomaly_disposition_v2_to_v3_20260829",
        "migration_date": "2026-08-29",
        "model_id": MODEL_ID,
        "from_registry_version": "anomaly_disposition_v2_20260828",
        "to_registry_version": REGISTRY_VERSION,
        "from_registry_path": LEGACY_V2_REGISTRY_PATH.as_posix(),
        "to_registry_path": REGISTRY_PATH.as_posix(),
        "from_registry_canonical_sha256": LEGACY_V2_REGISTRY_CANONICAL_SHA256,
        "to_registry_canonical_sha256": to_sha,
        "operation_key_count": "9",
        "verified_real_extreme_count": "8",
        "verified_data_error_count": "1",
        "verified_non_comparable_count": "0",
        "unresolved_count": "0",
        "evidence_count": "9",
        "repair_closure_id": REPAIR_ID,
        "authorization_reference": "user_authorized_3A_3C_20260829",
        "append_only": "True",
        "research_only": "True",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "production_change": "False",
    }
    for field, expected in exact.items():
        if row.get(field, "") != expected:
            errors.append(
                f"anomaly disposition migration {field} mismatch: "
                f"expected={expected!r}; actual={row.get(field, '')!r}"
            )
    if len(registry_rows) != 9:
        errors.append("anomaly disposition migration target row count drifted")
    return errors


def validate_bundle(
    repo_root: Path | str = ROOT,
    *,
    require_effective_nonblocking: bool = False,
) -> ValidationResult:
    repo = Path(repo_root).resolve()
    errors: list[str] = []
    diagnostics: list[str] = []
    path = repo / REGISTRY_PATH
    try:
        columns, rows = _read_csv(path)
    except (OSError, ValueError) as exc:
        return ValidationResult(
            {}, [], [], [f"v3 anomaly registry unavailable: {exc}"], []
        )
    if tuple(columns) != REGISTRY_COLUMNS:
        errors.append("v3 anomaly registry columns must match the exact contract")
    actual = {row.get("operation_key", ""): row for row in rows}
    if len(actual) != len(rows):
        errors.append("v3 anomaly registry contains duplicate operation_key rows")
    if set(actual) != set(EXPECTED_CASES):
        errors.append(
            "v3 anomaly registry operation-key set drifted; "
            f"missing={sorted(set(EXPECTED_CASES) - set(actual))}; "
            f"extra={sorted(set(actual) - set(EXPECTED_CASES))}"
        )
    disposition_counts: dict[str, int] = {}
    for operation_key, case in EXPECTED_CASES.items():
        row = actual.get(operation_key)
        if row is None:
            continue
        if row.get("model_id") != MODEL_ID:
            errors.append(f"{case.stock_id}: model_id mismatch")
        exact_identity = {
            "stock_id": case.stock_id,
            "trigger_date": case.trigger_date,
            "confirmation_date": case.confirmation_date,
            "entry_date": case.entry_date,
            "exit_date": case.exit_date,
            "realized_return_pct": case.realized_return_pct,
            "candidate_detail_row_sha256": case.candidate_v3_row_sha256,
            "candidate_kind": case.candidate_kind,
            "anomaly_attribution_mode": case.anomaly_attribution_mode,
            "anomaly_source_event_periods": (
                "|".join(case.anomaly_source_event_periods)
                if case.anomaly_source_event_periods
                else "not_applicable"
            ),
            "anomaly_source_available_dates": (
                "|".join(case.anomaly_source_available_dates)
                if case.anomaly_source_available_dates
                else "not_applicable"
            ),
            "anomaly_source_canonical_row_sha256s": (
                "|".join(case.anomaly_source_canonical_row_sha256s)
                if case.anomaly_source_canonical_row_sha256s
                else "not_applicable"
            ),
            "anomaly_attribution_note": case.anomaly_attribution_note,
            "final_disposition": case.disposition,
            "approved_reason_reference": "",
            "reviewed_at": case.reviewed_at,
        }
        for field, expected in exact_identity.items():
            if row.get(field, "") != expected:
                errors.append(f"{case.stock_id}: registry {field} mismatch")
        if not (
            len(case.anomaly_source_event_periods)
            == len(case.anomaly_source_source_dates)
            == len(case.anomaly_source_available_dates)
            == len(case.anomaly_source_canonical_row_sha256s)
        ):
            errors.append(f"{case.stock_id}: expected attribution tuple width drifted")
        for available_date in case.anomaly_source_available_dates:
            if not re.fullmatch(r"\d{8}", available_date):
                errors.append(f"{case.stock_id}: malformed attribution available date")
            elif available_date > case.trigger_date:
                errors.append(
                    f"{case.stock_id}: post-trigger event used as anomaly attribution"
                )
        candidate_sha = row.get("candidate_detail_row_sha256", "")
        if not SHA256_RE.fullmatch(candidate_sha):
            errors.append(f"{case.stock_id}: invalid repaired candidate row SHA")
        if any(row.get(column) != "pass" for column in ROOT_CHECK_COLUMNS):
            errors.append(f"{case.stock_id}: all eight root checks must pass")
        if case.disposition == "verified_real_extreme":
            expected_policy = (
                "retain_in_primary_metrics",
                "eligible_only_after_all_other_model_gates",
                "not_applicable_no_repair",
            )
        else:
            expected_policy = (
                "repair_completed_primary_metrics_preserved",
                "eligible_only_after_all_other_model_gates",
                "verified_repaired_rerun",
            )
        if (
            row.get("primary_handling"),
            row.get("promotion_gate_status"),
            row.get("repair_satisfaction_status"),
        ) != expected_policy:
            errors.append(f"{case.stock_id}: disposition policy mismatch")
        if row.get("effective_anomaly_gate_status") != "satisfied":
            errors.append(f"{case.stock_id}: effective anomaly gate must be satisfied")
        document, evidence_errors = _validate_evidence(repo, row, case, diagnostics)
        errors.extend(evidence_errors)
        if document is not None and case.disposition == "verified_data_error":
            root_cause = document.get("semantic_payload", {}).get("root_cause", {})
            if not isinstance(root_cause, dict) or root_cause.get("repair_id") != REPAIR_ID:
                errors.append("6177 evidence does not bind the exact repair identity")
        disposition_counts[case.disposition] = disposition_counts.get(case.disposition, 0) + 1
    expected_counts = {"verified_real_extreme": 8, "verified_data_error": 1}
    if disposition_counts != expected_counts:
        errors.append(
            f"v3 anomaly dispositions must be exact {expected_counts}; actual={disposition_counts}"
        )
    closure_ok, closure_errors = _validate_repair_closure(repo, actual, diagnostics)
    errors.extend(closure_errors)
    errors.extend(_validate_migration(repo, actual))
    effective_blockers: list[str] = []
    for operation_key, row in actual.items():
        if row.get("final_disposition") == "verified_real_extreme":
            continue
        if (
            operation_key == REPAIR_OPERATION_KEY
            and row.get("final_disposition") == "verified_data_error"
            and closure_ok
        ):
            continue
        effective_blockers.append(operation_key)
    if require_effective_nonblocking and effective_blockers:
        errors.append(
            "promotion-candidate anomaly gate remains blocked: "
            f"operation_keys={effective_blockers}"
        )
    current_anomaly_keys = sorted(
        operation_key
        for operation_key, row in actual.items()
        if row.get("final_disposition") == "verified_real_extreme"
    )
    return ValidationResult(
        actual,
        effective_blockers,
        current_anomaly_keys,
        errors,
        diagnostics,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the sole canonical revenue_unreacted_range v3 anomaly "
            "disposition, evidence, and repaired-rerun closure gate."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--require-effective-nonblocking", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = validate_bundle(
        args.repo_root,
        require_effective_nonblocking=args.require_effective_nonblocking,
    )
    for diagnostic in result.diagnostics:
        print(f"DIAGNOSTIC: {diagnostic}")
    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "PASS: revenue_unreacted_range anomaly dispositions validated; "
        f"rows={len(result.rows)}; effective_blockers={len(result.effective_blockers)}; "
        "verified_real_extreme=8; verified_data_error_repaired=1; "
        "raw-byte and line-ending identities=diagnostic-only"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
