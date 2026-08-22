from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
import re
import statistics
import subprocess
from collections import defaultdict
from pathlib import Path, PurePosixPath, PureWindowsPath


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DECISION = ROOT / "config/revenue_unreacted_range_promotion_preparation_registry.csv"
DEFAULT_ANOMALIES = ROOT / "config/revenue_unreacted_range_anomaly_disposition_registry.csv"
DEFAULT_SUMMARY = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
)
DEFAULT_DETAIL = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv"
)
CANONICAL_PROJECTION_MANIFEST = ROOT / (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
V2_PROJECTION_VERSION = "source_snapshot_projection_v2_20260822"
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
DECISION_COLUMNS = tuple(EXPECTED_DECISION)

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
            "monthly_revenue_history_blob_sha256",
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


def _trusted_v1_source_blob(path: Path) -> bytes:
    contract = TRUSTED_V1_SOURCE_ARTIFACTS.get(Path(path))
    if contract is None:
        raise RuntimeError(f"unapproved trusted v1 promotion source path: {path}")
    if not re.fullmatch(r"[0-9a-f]{40}", TRUSTED_V1_SOURCE_REVISION):
        raise RuntimeError("trusted v1 promotion source revision is not a full SHA")
    commit = _git("rev-parse", "--verify", f"{TRUSTED_V1_SOURCE_REVISION}^{{commit}}")
    if commit.returncode != 0 or commit.stdout.decode("ascii", errors="replace").strip() != TRUSTED_V1_SOURCE_REVISION:
        raise RuntimeError("trusted v1 promotion source revision is unavailable")
    ancestor = _git("merge-base", "--is-ancestor", TRUSTED_V1_SOURCE_REVISION, "HEAD")
    if ancestor.returncode != 0:
        raise RuntimeError("trusted v1 promotion source revision is not an ancestor of HEAD")
    repo_path = str(contract["path"])
    tree = _git("ls-tree", TRUSTED_V1_SOURCE_REVISION, "--", repo_path)
    fields = tree.stdout.decode("utf-8", errors="replace").strip().split(None, 3)
    if (
        tree.returncode != 0
        or len(fields) != 4
        or fields[0] != "100644"
        or fields[1] != "blob"
        or fields[2] != contract["blob"]
        or fields[3] != repo_path
    ):
        raise RuntimeError(f"trusted v1 promotion source tree identity mismatch: {repo_path}")
    blob = _git("cat-file", "blob", str(contract["blob"]))
    if blob.returncode != 0:
        raise RuntimeError(f"trusted v1 promotion source blob is unreadable: {repo_path}")
    if len(blob.stdout) != contract["bytes"]:
        raise RuntimeError(f"trusted v1 promotion source byte count mismatch: {repo_path}")
    if hashlib.sha256(blob.stdout).hexdigest() != contract["sha256"]:
        raise RuntimeError(f"trusted v1 promotion source SHA-256 mismatch: {repo_path}")
    return blob.stdout


def _canonical_projection_version() -> str:
    columns, rows, errors = _read_csv(CANONICAL_PROJECTION_MANIFEST)
    if errors or len(rows) != 1 or "projection_version" not in columns:
        return ""
    return rows[0].get("projection_version", "").strip()


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


def validate_decision(path: Path) -> tuple[dict[str, str] | None, list[str]]:
    columns, rows, errors = _read_csv(path)
    if columns and tuple(columns) != DECISION_COLUMNS:
        errors.append("promotion preparation registry columns must match the exact contract")
    if len(rows) != 1:
        errors.append(f"promotion preparation registry must contain exactly one row; actual={len(rows)}")
        return None, errors
    row = rows[0]
    for column, expected in EXPECTED_DECISION.items():
        if row.get(column, "") != expected:
            errors.append(
                f"promotion preparation {column} mismatch: expected={expected!r}; actual={row.get(column, '')!r}"
            )
    formula_sha256 = hashlib.sha256(
        row.get("rule_formula_canonical", "").encode("utf-8")
    ).hexdigest()
    if formula_sha256 != row.get("rule_formula_sha256", ""):
        errors.append(
            "promotion preparation rule_formula_sha256 does not bind the canonical formula"
        )
    return row, errors


def validate_anomalies(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    columns, rows, errors = _read_csv(path)
    if columns and tuple(columns) != ANOMALY_COLUMNS:
        errors.append("anomaly disposition registry columns must match the exact contract")
    keys = [row.get("operation_key", "") for row in rows]
    if len(keys) != len(set(keys)):
        errors.append("anomaly disposition registry has duplicate operation_key rows")
    actual = {row.get("operation_key", ""): row for row in rows}
    if set(actual) != set(EXPECTED_ANOMALIES):
        errors.append(
            "anomaly disposition registry must contain the exact frozen 8 operation keys; "
            f"missing={sorted(set(EXPECTED_ANOMALIES) - set(actual))}; "
            f"extra={sorted(set(actual) - set(EXPECTED_ANOMALIES))}"
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
    for key, expected_values in EXPECTED_ANOMALIES.items():
        row = actual.get(key)
        if row is None:
            continue
        if row.get("model_id") != "revenue_unreacted_range":
            errors.append(f"{key}: model_id must be revenue_unreacted_range")
        for column, expected in zip(identity_columns, expected_values, strict=True):
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
    if len(rows) != 8:
        errors.append(f"anomaly disposition registry must contain exactly 8 rows; actual={len(rows)}")
    return actual, errors


def _summary_matches(row: dict[str, str]) -> bool:
    selection = {
        key: SUMMARY_EXPECTED[key]
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
) -> tuple[dict[str, str] | None, list[str]]:
    _columns, rows, errors = _read_csv(path, payload=payload, label=label)
    selected = [row for row in rows if _summary_matches(row)]
    if len(selected) != 1:
        errors.append(f"source summary must contain exactly one frozen selected slice; actual={len(selected)}")
        return None, errors
    row = selected[0]
    for column, expected in SUMMARY_EXPECTED.items():
        if row.get(column, "") != expected:
            errors.append(
                f"source summary {column} mismatch: expected={expected!r}; actual={row.get(column, '')!r}"
            )
    return row, errors


def _detail_matches(row: dict[str, str]) -> bool:
    return (
        row.get("source_variant_id") == EXPECTED_DECISION["source_variant_id"]
        and row.get("lifecycle_policy_id") == EXPECTED_DECISION["lifecycle_policy_id"]
        and row.get("confirmation_variant_id") == EXPECTED_DECISION["confirmation_variant_id"]
        and row.get("holding_days") == "30"
        and row.get("stop_policy_id") == EXPECTED_DECISION["stop_policy_id"]
        and _is_true(row.get("mid_falling_member", ""))
        and _is_true(row.get("primary_included", ""))
    )


def validate_detail(
    path: Path,
    anomaly_rows: dict[str, dict[str, str]],
    *,
    payload: bytes | None = None,
    label: str | None = None,
) -> tuple[list[dict[str, str]], list[str]]:
    _columns, rows, errors = _read_csv(path, payload=payload, label=label)
    selected = [row for row in rows if _detail_matches(row)]
    if len(selected) != 52:
        errors.append(f"source detail frozen selected slice must contain 52 rows; actual={len(selected)}")
        return selected, errors

    expected_constants = {
        "model_id": "revenue_unreacted_range",
        "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
        "artifact_version": "low_mid_falling_candidate_v1_20260720",
        "candidate_detail_row_set_sha256": EXPECTED_DECISION["candidate_detail_row_set_sha256"],
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
        expected_text = EXPECTED_DECISION[column]
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


def validate(
    *,
    decision_path: Path = DEFAULT_DECISION,
    anomaly_path: Path = DEFAULT_ANOMALIES,
    summary_path: Path = DEFAULT_SUMMARY,
    detail_path: Path = DEFAULT_DETAIL,
    require_source_artifacts: bool = False,
) -> list[str]:
    errors: list[str] = []
    _decision, decision_errors = validate_decision(decision_path)
    anomaly_rows, anomaly_errors = validate_anomalies(anomaly_path)
    errors.extend(decision_errors)
    errors.extend(anomaly_errors)

    trusted_summary: bytes | None = None
    trusted_detail: bytes | None = None
    use_trusted_v1_sources = (
        Path(summary_path).resolve() == DEFAULT_SUMMARY.resolve()
        and Path(detail_path).resolve() == DEFAULT_DETAIL.resolve()
        and _canonical_projection_version() == V2_PROJECTION_VERSION
    )
    if use_trusted_v1_sources:
        try:
            trusted_summary = _trusted_v1_source_blob(DEFAULT_SUMMARY)
            trusted_detail = _trusted_v1_source_blob(DEFAULT_DETAIL)
        except RuntimeError as exc:
            errors.append(str(exc))
    if use_trusted_v1_sources:
        summary_exists = trusted_summary is not None
        detail_exists = trusted_detail is not None
    else:
        summary_exists = summary_path.is_file()
        detail_exists = detail_path.is_file()
    if require_source_artifacts or summary_exists or detail_exists:
        if not summary_exists or not detail_exists:
            errors.append(
                "source artifacts must be supplied as a complete summary/detail pair when validation is enabled"
            )
        else:
            source_label = (
                f"trusted Git {TRUSTED_V1_SOURCE_REVISION}"
                if use_trusted_v1_sources
                else None
            )
            _summary, summary_errors = validate_summary(
                summary_path,
                payload=trusted_summary,
                label=(f"{source_label}:{TRUSTED_V1_SOURCE_ARTIFACTS[DEFAULT_SUMMARY]['path']}" if source_label else None),
            )
            _detail, detail_errors = validate_detail(
                detail_path,
                anomaly_rows,
                payload=trusted_detail,
                label=(f"{source_label}:{TRUSTED_V1_SOURCE_ARTIFACTS[DEFAULT_DETAIL]['path']}" if source_label else None),
            )
            errors.extend(summary_errors)
            errors.extend(detail_errors)
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently validate the frozen revenue promotion-preparation decision."
    )
    parser.add_argument("--decision", type=Path, default=DEFAULT_DECISION)
    parser.add_argument("--anomaly-registry", type=Path, default=DEFAULT_ANOMALIES)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--detail", type=Path, default=DEFAULT_DETAIL)
    parser.add_argument(
        "--require-source-artifacts",
        action="store_true",
        help="Fail unless both source summary and detail artifacts exist.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(
        decision_path=args.decision,
        anomaly_path=args.anomaly_registry,
        summary_path=args.summary,
        detail_path=args.detail,
        require_source_artifacts=args.require_source_artifacts,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if (
        args.summary.resolve() == DEFAULT_SUMMARY.resolve()
        and args.detail.resolve() == DEFAULT_DETAIL.resolve()
        and _canonical_projection_version() == V2_PROJECTION_VERSION
    ):
        source_state = f"historical v1 source artifacts validated from trusted Git {TRUSTED_V1_SOURCE_REVISION}"
    else:
        source_state = "source artifacts validated" if args.summary.is_file() else "source artifacts absent; registry-only validation"
    print(
        "PASS: revenue_unreacted_range promotion preparation independently validated; "
        f"{source_state}; formal flags remain false; anomaly worklist=8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
