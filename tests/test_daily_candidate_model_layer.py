from __future__ import annotations

import ast
import hashlib
import inspect
import json
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_all_candidates_latest as all_candidates_builder  # noqa: E402
import build_daily_candidate_model_layer as model_layer  # noqa: E402
from build_volume_breakout_watch import canonical_csv_slice_sha256  # noqa: E402
from build_daily_candidate_model_layer import (  # noqa: E402
    MODEL_SCORE_PROFILES,
    annotate_frontpage_uniqueness,
    attach_model_recommendations,
    attach_same_model_repeat,
    build_parameter_table,
    build_frontpage_unique,
    build_report_ready_model_signals,
    build_signals,
    build_specs,
    cond_neckline_volume_breakout_confirmation,
    cond_pullback,
    cond_revenue_unreacted,
    cond_tdcc_stealth,
    cond_w_bottom_right,
    report_bucket,
    score_pullback,
    update_model_signal_log,
)
from audit_daily_candidate_model_selection_correctness import (  # noqa: E402
    model_stock_key_set,
    selected_price_pullback_23ema_condition,
)
from validate_volume_breakout_watch import (  # noqa: E402
    advisory_source_lineage_errors,
    canonical_csv_slice_sha256 as validator_canonical_csv_slice_sha256,
)
from validate_daily_candidate_model_layer import (  # noqa: E402
    dedicated_operation_only_derived_artifact_errors,
    dedicated_operation_only_signal_errors,
)

LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
MID_VOLUME_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
HIGH_VOLUME_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"


def make_row(**overrides: object) -> pd.Series:
    base: dict[str, object] = {
        "stock_id": "9999",
        "stock_name": "TEST",
        "volume_ratio": "2.0",
        "volume_breakout_type": "bottom_volume_attack",
        "selection_status": "selected",
        "volume_breakout_priority": "A_bottom_volume_attack",
        "close": "103",
        "open": "100",
        "high": "104",
        "low": "95",
        "previous_close": "99",
        "previous_20d_high": "100",
        "volume_ma20": "2000",
        "close_above_range_high": "False",
        "distance_23ema_pct": "1.5",
        "ema23_slope_pct": "0.5",
        "return_20d": "5",
        "return_20d_pct": "5",
        "price_pullback_tdcc_history_available": "True",
        "price_pullback_high_thresholds_up": "True",
        "price_pullback_all_thresholds_up": "False",
        "price_pullback_obv_above_ma20": "True",
        "price_pullback_rsi14": "62",
        "price_pullback_macd_hist": "0.5",
        "tdcc_judgement": "mild_accumulation",
        "warrant_flow_signal": "no_signal",
        "structural_theme_bucket": "",
        "theme_structural_status": "",
    }
    base.update(overrides)
    return pd.Series(base)


def candidate_rows_with_lineage(rows: list[dict[str, object]]) -> pd.DataFrame:
    payload: list[dict[str, object]] = []
    for index, source in enumerate(rows, start=2):
        row = dict(source)
        row.setdefault("signal_date", "20260530")
        raw_stock_id = str(
            row.get("candidate_source_raw_stock_id", row.get("stock_id", ""))
        )
        normalized_stock_id = str(
            row.get(
                "candidate_source_normalized_stock_id",
                row.get("stock_id", ""),
            )
        )
        artifact = str(
            row.get(
                "candidate_source_artifact",
                f"output/latest/test_source_{index}.csv",
            )
        )
        record_number = str(row.get("candidate_source_record_number", index))
        artifact_sha256 = str(
            row.get(
                "candidate_source_artifact_sha256",
                hashlib.sha256(artifact.encode("utf-8")).hexdigest(),
            )
        )
        row_sha256 = str(
            row.get(
                "candidate_source_row_sha256",
                hashlib.sha256(
                    f"{artifact}|{record_number}|{normalized_stock_id}".encode("utf-8")
                ).hexdigest(),
            )
        )
        row.update(
            {
                "candidate_source_raw_stock_id": raw_stock_id,
                "candidate_source_normalized_stock_id": normalized_stock_id,
                "candidate_source_identity_columns": row.get(
                    "candidate_source_identity_columns", "stock_id"
                ),
                "candidate_source_artifact": artifact,
                "candidate_source_producer": row.get(
                    "candidate_source_producer", "tests/fixture.py"
                ),
                "candidate_source_artifact_sha256": artifact_sha256,
                "candidate_source_record_number": record_number,
                "candidate_source_row_sha256": row_sha256,
                "candidate_source_row_id": row.get(
                    "candidate_source_row_id",
                    f"{artifact}@{artifact_sha256}#{record_number}:"
                    f"{normalized_stock_id}:{row_sha256}",
                ),
            }
        )
        payload.append(row)
    return pd.DataFrame(payload)


def volume_v2_price_history(signal_date: str = "20260530") -> pd.DataFrame:
    dates = pd.date_range(end=pd.to_datetime(signal_date), periods=120, freq="D").strftime("%Y%m%d")
    rows = [
        {
            "date": date,
            "open": "100",
            "high": "200",
            "low": "80",
            "close": "100",
            "volume": "1000",
        }
        for date in dates
    ]
    rows[-1].update({"open": "100", "high": "104", "low": "95", "close": "103", "volume": "3000"})
    return pd.DataFrame(rows)


def mid_position_volume_v2_price_history(signal_date: str = "20260530") -> pd.DataFrame:
    dates = pd.date_range(end=pd.to_datetime(signal_date), periods=120, freq="D").strftime("%Y%m%d")
    rows = [
        {
            "date": date,
            "open": "100",
            "high": "120",
            "low": "80",
            "close": "100",
            "volume": "1000",
        }
        for date in dates
    ]
    rows[-1].update({"open": "98", "high": "105", "low": "95", "close": "101", "volume": "3000"})
    return pd.DataFrame(rows)


def high_position_volume_v2_price_history(signal_date: str = "20260530") -> pd.DataFrame:
    dates = pd.date_range(end=pd.to_datetime(signal_date), periods=120, freq="D").strftime("%Y%m%d")
    rows: list[dict[str, str]] = []
    for index, date in enumerate(dates):
        close = 90 if index < 60 else 100
        rows.append(
            {
                "date": date,
                "open": str(close),
                "high": "110",
                "low": "80",
                "close": str(close),
                "volume": "1000",
            }
        )
    rows[-1].update({"open": "104", "high": "110", "low": "100", "close": "108", "volume": "3000"})
    return pd.DataFrame(rows)


def write_volume_v2_watch_fixture(
    source: pd.DataFrame,
    watch_path: Path,
    price_path: Path,
    price_history: pd.DataFrame,
) -> None:
    price_history.to_csv(price_path, index=False)
    payload = source.copy()
    payload["advisory_score_as_of"] = payload["signal_date"]
    payload["advisory_score_source_artifact"] = price_path.as_posix()
    signal_dates = sorted(set(payload["signal_date"].astype(str)))
    if len(signal_dates) != 1:
        raise AssertionError(f"watch fixture requires one signal date: {signal_dates}")
    payload["advisory_score_source_sha256"] = (
        model_layer.volume_v2_canonical_text_sha256(price_path, signal_dates[0])
    )
    payload.to_csv(watch_path, index=False, encoding="utf-8-sig")


def warrant_formal_sync_fixture() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw_rows = [
        {
            "signal_date": "20260717",
            "report_line": "mainstream",
            "report_bucket": "mainstream",
            "source_row_index": "candidate:0",
            "stock_id": "2330",
            "model_id": "hot_theme_pullback",
            "base_model_score": "80",
            "final_rank_score": "80",
            "model_score": "80",
            "model_rank": "2",
            "score_components": "base=50 | hot theme +30",
            "warrant_flow_signal": "no_signal",
        },
        {
            "signal_date": "20260717",
            "report_line": "mainstream",
            "report_bucket": "mainstream",
            "source_row_index": "candidate:1",
            "stock_id": "2317",
            "model_id": "hot_theme_pullback",
            "base_model_score": "81",
            "final_rank_score": "81",
            "model_score": "81",
            "model_rank": "1",
            "score_components": "base=50 | hot theme +26 | warrant bullish +5",
            "warrant_flow_signal": "call_inflow",
        },
        {
            "signal_date": "20260717",
            "report_line": "mainstream",
            "report_bucket": "mainstream",
            "source_row_index": "candidate:2",
            "stock_id": "2454",
            "model_id": "price_pullback_23ema",
            "base_model_score": "70",
            "final_rank_score": "70",
            "model_score": "70",
            "model_rank": "1",
            "score_components": "base=70 | price_pullback_v1_required_gate",
            "warrant_flow_signal": "no_signal",
        },
        {
            "signal_date": "20260717",
            "report_line": "non_mainstream",
            "report_bucket": "non_mainstream",
            "source_row_index": "tdcc_edge:0",
            "stock_id": "1301",
            "model_id": "tdcc_short_term_continuation_d5_d10",
            "base_model_score": "60",
            "final_rank_score": "60",
            "model_score": "60",
            "model_rank": "1",
            "score_components": "base=50 | D+10 win 70.0% +5.0",
            "warrant_flow_signal": "",
        },
    ]
    raw = pd.DataFrame(raw_rows)
    report = raw.copy()
    report["merged_score_components"] = report["score_components"].str.replace(
        " | ",
        " / ",
        regex=False,
    )
    current_history = [
        {
            column: row[column]
            for column in (
                "signal_date",
                "report_bucket",
                "stock_id",
                "model_id",
                "base_model_score",
                "final_rank_score",
                "model_score",
                "model_rank",
            )
        }
        for row in raw_rows
    ]
    prior = dict(current_history[0])
    prior.update(
        {
            "signal_date": "20260715",
            "base_model_score": "75",
            "final_rank_score": "75",
            "model_score": "75",
            "model_rank": "1",
        }
    )
    history = pd.DataFrame([prior, *current_history])
    history["immutable_prior_cell"] = ""
    history.loc[0, "immutable_prior_cell"] = "  preserve prior spacing exactly  "
    candidates = pd.DataFrame(
        [
            {
                "signal_date": "20260717",
                "stock_id": "2330",
                "warrant_flow_signal": "call_inflow",
            },
            {
                "signal_date": "20260717",
                "stock_id": "2317",
                "warrant_flow_signal": "no_signal",
            },
            {
                "signal_date": "20260717",
                "stock_id": "2454",
                "warrant_flow_signal": "call_inflow",
            },
        ]
    )
    return candidates, raw, report, history


class DailyCandidateModelLayerTest(unittest.TestCase):
    def _dispatch_mid_volume_fixture(
        self,
        *,
        watch_updates: dict[str, str] | None = None,
        candidates: pd.DataFrame | None = None,
        stock_id: str = "1618",
        duplicate_selected_watch: bool = False,
    ) -> pd.DataFrame:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": stock_id,
                    "stock_name": "TEST",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "advisory_volume_breakout_score": "70",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_taxonomy_path = model_layer.VOLUME_BREAKOUT_TAXONOMY
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            taxonomy_path = temp_dir / "stock_theme_taxonomy_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / f"{stock_id}.csv",
                mid_position_volume_v2_price_history(),
            )
            pd.DataFrame(
                [
                    {
                        "stock_id": stock_id,
                        "stock_name": "TEST",
                        "industry": "test_industry",
                        "primary_theme": "test_theme",
                        "structural_theme_bucket": "test_theme",
                        "effective_mainstream_label": "core_mainstream",
                        "report_line_memberships": "mainstream",
                        "mainstream_report_eligible": "True",
                        "non_mainstream_report_eligible": "False",
                        "dual_report_membership_flag": "False",
                    }
                ]
            ).to_csv(taxonomy_path, index=False, encoding="utf-8-sig")
            if watch_updates:
                payload = pd.read_csv(temp_path, dtype=str, keep_default_na=False)
                for field, value in watch_updates.items():
                    payload[field] = value
                payload.to_csv(temp_path, index=False, encoding="utf-8-sig")
            if duplicate_selected_watch:
                payload = pd.read_csv(
                    temp_path, dtype=str, keep_default_na=False
                )
                pd.concat([payload, payload], ignore_index=True).to_csv(
                    temp_path, index=False, encoding="utf-8-sig"
                )
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.VOLUME_BREAKOUT_TAXONOMY = taxonomy_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                return model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidates
                    if candidates is not None
                    else candidate_rows_with_lineage(
                        [{"stock_id": stock_id, "warrant_flow_signal": "call_inflow"}]
                    ),
                    "20260530",
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.VOLUME_BREAKOUT_TAXONOMY = original_taxonomy_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir

    def test_required_models_are_parameterized(self) -> None:
        model_ids = set(build_parameter_table(build_specs())["model_id"])
        self.assertTrue(
            {
                LOW_VOLUME_MODEL_ID,
                MID_VOLUME_MODEL_ID,
                HIGH_VOLUME_MODEL_ID,
                "price_pullback_23ema",
                "revenue_unreacted_range",
                "w_bottom_right_side",
                "neckline_volume_breakout_confirmation",
                "pullback_short_reclaim",
                "tdcc_stealth_accumulation",
                "tdcc_short_term_continuation_d5_d10",
                "short_term_surge_d5_d10",
                "group_fund_rotation",
                "explosive_volume_red_candle",
                "five_day_20pct_precursor",
                "disposition_attention_event_tag",
                "msci_event_tag",
            }.issubset(model_ids)
        )

    def test_revenue_v2_metadata_remains_visible_without_legacy_scoring(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        revenue = params.loc["revenue_unreacted_range"]

        self.assertEqual(revenue["pdf_visibility"], "pdf_core_model")
        self.assertEqual(revenue["entry_basis"], "confirmation_d2_open")
        self.assertEqual(
            revenue["score_profile_id"],
            "revenue_unreacted_range_source_mid_falling_v2_frozen_no_score",
        )
        self.assertEqual(
            revenue["score_profile_scope"],
            "not_applicable_dedicated_operation_adapter",
        )
        self.assertEqual(
            revenue["parameter_status"],
            "contract_prepared_permissions_false",
        )
        self.assertEqual(revenue["base_score"], "")
        self.assertIn("凍結 source_mid_falling v2", revenue["main_conditions"])
        self.assertIn("D+2 開盤", revenue["operation_guidance"])

    def test_parameter_table_keeps_pdf_research_and_event_layers_separate(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        self.assertNotIn("volume_range_breakout", params.index)
        self.assertEqual(params.loc[LOW_VOLUME_MODEL_ID, "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc[MID_VOLUME_MODEL_ID, "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc[HIGH_VOLUME_MODEL_ID, "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc["tdcc_short_term_continuation_d5_d10", "pdf_visibility"], "pdf_core_model")
        self.assertEqual(params.loc["short_term_surge_d5_d10", "pdf_visibility"], "research_only_not_pdf_core")
        self.assertEqual(params.loc["explosive_volume_red_candle", "pdf_visibility"], "research_only_not_pdf_core")
        self.assertEqual(params.loc["disposition_attention_event_tag", "pdf_visibility"], "pdf_risk_tag_only")
        self.assertNotIn("near_high_neckline_challenge", params.index)
        self.assertNotIn("platform_strengthening", params.index)

    def test_formal_pdf_models_do_not_keep_legacy_common_scoring(self) -> None:
        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        source = source_path.read_text(encoding="utf-8")

        self.assertNotIn("def model_score_common(", source)
        self.assertNotIn('"legacy_common"', source)

    def test_deprecated_neckline_and_platform_models_have_no_executable_source(self) -> None:
        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        source = source_path.read_text(encoding="utf-8")

        forbidden_snippets = {
            "def cond_neckline_challenge(",
            "def cond_platform_strength(",
            "def score_neckline_challenge(",
            "def score_platform_strength(",
            '"near_high_neckline_challenge": ScoreProfile',
            '"platform_strengthening": ScoreProfile',
            'ModelSpec(\n            "near_high_neckline_challenge"',
            'ModelSpec(\n            "platform_strengthening"',
        }
        for snippet in forbidden_snippets:
            self.assertNotIn(snippet, source)

    def test_pdf_core_models_have_independent_condition_and_score_functions(self) -> None:
        specs = [spec for spec in build_specs() if spec.pdf_visibility == "pdf_core_model"]
        condition_names = [spec.condition_func.__name__ for spec in specs]
        score_names = [spec.score_func.__name__ for spec in specs]
        self.assertEqual(len(condition_names), len(set(condition_names)))
        self.assertEqual(len(score_names), len(set(score_names)))
        self.assertNotIn("model_score_common", score_names)
        self.assertEqual(
            {spec.model_id for spec in specs},
            {
                LOW_VOLUME_MODEL_ID,
                MID_VOLUME_MODEL_ID,
                HIGH_VOLUME_MODEL_ID,
                "price_pullback_23ema",
                "hot_theme_pullback",
                "revenue_unreacted_range",
                "w_bottom_right_side",
                "neckline_volume_breakout_confirmation",
                "pullback_short_reclaim",
                "tdcc_stealth_accumulation",
            },
        )

    def test_pdf_core_models_do_not_call_each_other_conditions_or_scores(self) -> None:
        specs = [spec for spec in build_specs() if spec.pdf_visibility == "pdf_core_model"]
        condition_by_func = {spec.condition_func.__name__: spec.model_id for spec in specs}
        score_by_func = {spec.score_func.__name__: spec.model_id for spec in specs}
        all_condition_funcs = set(condition_by_func)
        all_score_funcs = set(score_by_func)

        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        funcs = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}

        cross_condition_calls: list[str] = []
        for func_name, model_id in condition_by_func.items():
            for node in ast.walk(funcs[func_name]):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    callee = node.func.id
                    if callee in condition_by_func and callee != func_name:
                        cross_condition_calls.append(f"{model_id}:{func_name}->{callee}")
                    if callee in all_score_funcs:
                        cross_condition_calls.append(f"{model_id}:{func_name}->{callee}")

        cross_score_calls: list[str] = []
        for func_name, model_id in score_by_func.items():
            for node in ast.walk(funcs[func_name]):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    callee = node.func.id
                    if callee in all_score_funcs and callee != func_name:
                        cross_score_calls.append(f"{model_id}:{func_name}->{callee}")
                    if callee in all_condition_funcs:
                        cross_score_calls.append(f"{model_id}:{func_name}->{callee}")

        self.assertEqual(cross_condition_calls, [])
        self.assertEqual(cross_score_calls, [])

    def test_pdf_facing_helpers_are_not_duplicated(self) -> None:
        source_path = ROOT / "scripts" / "build_daily_candidate_model_layer.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        names = [
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name
            in {
                "same_model_repeat_status_zh",
                "same_model_repeat_note_zh",
                "apply_display_columns",
                "attach_report_contract_columns",
            }
        ]
        for name in set(names):
            self.assertEqual(names.count(name), 1, name)

    def test_model_score_profiles_are_independent_and_visible(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        self.assertEqual(params.loc[LOW_VOLUME_MODEL_ID, "score_profile_id"], LOW_VOLUME_MODEL_ID)
        self.assertEqual(params.loc[MID_VOLUME_MODEL_ID, "score_profile_id"], MID_VOLUME_MODEL_ID)
        self.assertEqual(params.loc[HIGH_VOLUME_MODEL_ID, "score_profile_id"], HIGH_VOLUME_MODEL_ID)
        self.assertEqual(params.loc["price_pullback_23ema", "score_profile_id"], "price_pullback_23ema")
        self.assertEqual(
            params.loc["neckline_volume_breakout_confirmation", "score_profile_id"],
            "neckline_volume_breakout_confirmation",
        )
        self.assertEqual(params.loc["tdcc_stealth_accumulation", "score_profile_id"], "tdcc_stealth_accumulation")
        self.assertNotEqual(
            params.loc[LOW_VOLUME_MODEL_ID, "volume_ratio_bonus_per_1x"],
            params.loc["price_pullback_23ema", "volume_ratio_bonus_per_1x"],
        )
        self.assertNotEqual(
            params.loc["tdcc_stealth_accumulation", "tdcc_positive_bonus"],
            params.loc[LOW_VOLUME_MODEL_ID, "tdcc_positive_bonus"],
        )
        self.assertNotIn("legacy_common", MODEL_SCORE_PROFILES)

    def test_volume_v2_score_components_zh_hides_raw_contract_slugs(self) -> None:
        raw = (
            "type=bottom_volume_attack | volume_ratio=4.4664 | base=60 | "
            "profile=volume_range_breakout_v2_low_position_volume_attack | "
            "position_bucket_120d=low_pos_le40 | shape_bucket=non_consolidation"
        )

        zh = model_layer.score_components_zh(raw)

        for token in [
            "base=",
            "profile=",
            "volume_range_breakout_v2",
            "position_bucket_120d",
            "low_pos_le40",
            "shape_bucket",
            "non_consolidation",
        ]:
            self.assertNotIn(token, zh)
        self.assertIn("基礎分60", zh)
        self.assertIn("120日位階=低位", zh)
        self.assertIn("型態=非盤整", zh)

    def test_pdf_models_use_next_open_entry_basis(self) -> None:
        params = build_parameter_table(build_specs())
        pdf_rows = params[params["pdf_visibility"].isin(["pdf_core_model", "pdf_specialty_section"])]
        expected = {
            LOW_VOLUME_MODEL_ID: "confirmation_next_open",
            MID_VOLUME_MODEL_ID: "confirmation_next_open",
            HIGH_VOLUME_MODEL_ID: "confirmation_next_open",
            "revenue_unreacted_range": "confirmation_d2_open",
        }
        for _, row in pdf_rows.iterrows():
            self.assertEqual(
                row["entry_basis"],
                expected.get(row["model_id"], "signal_date_next_open"),
                row["model_id"],
            )

    def test_volume_breakout_v2_condition_text_replaces_legacy_v1_text(self) -> None:
        params = build_parameter_table(build_specs()).set_index("model_id")
        self.assertNotIn("volume_range_breakout", params.index)
        low_condition_text = params.loc[LOW_VOLUME_MODEL_ID, "main_conditions"]
        mid_condition_text = params.loc[MID_VOLUME_MODEL_ID, "main_conditions"]
        high_condition_text = params.loc[HIGH_VOLUME_MODEL_ID, "main_conditions"]

        self.assertIn("60", low_condition_text)
        self.assertIn("120", low_condition_text)
        self.assertIn("120", mid_condition_text)
        self.assertIn("MA60", high_condition_text)
        self.assertIn("MA120", high_condition_text)
        condition_spec = pd.read_csv(ROOT / "config" / "daily_model_condition_spec.csv")
        self.assertNotIn("volume_range_breakout", set(condition_spec["model_id"].astype(str)))
        self.assertNotIn("cond_volume_breakout", set(condition_spec["condition_function"].astype(str)))
        self.assertNotIn("score_volume_breakout", set(condition_spec["score_function"].astype(str)))
        self.assertIn(
            "cond_volume_breakout_v2_low_position_watch_only",
            set(condition_spec["condition_function"].astype(str)),
        )
        self.assertIn(
            "cond_volume_breakout_v2_mid_position_watch_only",
            set(condition_spec["condition_function"].astype(str)),
        )
        self.assertIn(
            "cond_volume_breakout_v2_high_position_watch_only",
            set(condition_spec["condition_function"].astype(str)),
        )


    def test_locked_limit_up_low_volume_ratio_is_volume_breakout(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="81.8",
            open="81.8",
            high="81.8",
            low="81.8",
            previous_close="74.4",
            previous_20d_high="74.4",
            volume_ratio="0.504",
            volume_ma20="7099858.7",
        )

        score, components, _risks = model_layer.score_volume_breakout_v2_low_position(row)

        self.assertGreater(score, 0)
        self.assertTrue(any("locked_limit_up_breakout" in item for item in components))


    def test_locked_limit_up_signal_row_does_not_emit_legacy_v1_model(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            close="81.8",
            open="81.8",
            high="81.8",
            low="81.8",
            previous_close="74.4",
            previous_20d_high="74.4",
            volume_ratio="0.504",
            volume_ma20="7099858.7",
        )

        out = build_signals(pd.DataFrame([row]), build_specs(), "20260612")

        self.assertNotIn("volume_range_breakout", set(out["model_id"].astype(str)))



    def test_dedicated_volume_breakout_table_is_independent_from_candidate_model(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1617",
                    "stock_name": "榮星",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_score": "88",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct|volume_ratio_ge_2|volume_ma20_lots_ge_1000|bullish_candle",
                    "volume_ratio": "3.17",
                    "warrant_flow_signal": "no_signal",
                    "tdcc_status": "distribution_warning",
                    "theme_group": "watch_poison_theme",
                    "return_5d": "7.0",
                    "return_20d": "6.3",
                    "next_volume_breakout_confirmation": "confirm close above MA20/EMA23",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "1617.csv",
                volume_v2_price_history(),
            )
            source_bytes_before = temp_path.read_bytes()
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidate_rows_with_lineage(
                        [
                            {
                                "stock_id": "1617",
                                "warrant_flow_signal": "call_inflow",
                                "tdcc_status": "strong_accumulation",
                                "theme_group": "canonical_theme",
                                "score": "1",
                                "rank": "1",
                                "category": "range_rebound",
                            },
                            {
                                "stock_id": "1617",
                                "warrant_flow_signal": "call_inflow",
                                "tdcc_status": "strong_accumulation",
                                "score": "99",
                                "rank": "9",
                                "category": "pattern",
                            },
                        ]
                    ),
                    "20260530",
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir
            source_bytes_after = temp_path.read_bytes()

        self.assertEqual(source_bytes_before, source_bytes_after)
        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["stock_id"], "1617")
        self.assertEqual(row["model_id"], LOW_VOLUME_MODEL_ID)
        self.assertIn("operation_score", row.index)
        self.assertIn("tdcc_score", row.index)
        self.assertIn("pattern_score", row.index)
        self.assertIn("risk_penalty", row.index)
        self.assertIn("final_rank_score", row.index)
        self.assertEqual(float(row["model_score"]), float(row["final_rank_score"]))
        self.assertEqual(row["volume_position_bucket_120d"], "low_pos_le40")
        self.assertEqual(row["warrant_flow_signal"], "call_inflow")
        self.assertEqual(row["tdcc_status"], "strong_accumulation")
        self.assertIn("warrant bullish +2", row["score_components"])
        self.assertIn("TDCC positive +4", row["score_components"])
        self.assertEqual(len(row["candidate_source_row_ids"].split("|")), 2)
        self.assertNotIn("watch_poison_theme", row.astype(str).tolist())
        self.assertNotIn("volume_range_breakout", set(out["model_id"].astype(str)))

    def test_mid_position_volume_breakout_uses_canonical_candidate_warrant(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1618",
                    "stock_name": "MID",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct|volume_ratio_ge_2",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                    "warrant_flow_signal": "no_signal",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "1618.csv",
                mid_position_volume_v2_price_history(),
            )
            source_bytes_before = temp_path.read_bytes()
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidate_rows_with_lineage(
                        [{"stock_id": "1618", "warrant_flow_signal": "call_inflow"}]
                    ),
                    "20260530",
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir
            source_bytes_after = temp_path.read_bytes()

        self.assertEqual(source_bytes_before, source_bytes_after)
        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["model_id"], MID_VOLUME_MODEL_ID)
        self.assertEqual(row["warrant_flow_signal"], "call_inflow")
        self.assertIn("warrant bullish +2", row["score_components"])

    def test_volume_v2_dispatcher_fails_on_unregistered_same_name_collision(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1618",
                    "stock_name": "MID",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct|volume_ratio_ge_2",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                    "future_shared_semantic": "watch_value",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "1618.csv",
                mid_position_volume_v2_price_history(),
            )
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                with self.assertRaisesRegex(
                    RuntimeError,
                    "unregistered same-name field collision.*future_shared_semantic",
                ):
                    model_layer.append_volume_breakout_signals(
                        pd.DataFrame(),
                        candidate_rows_with_lineage(
                            [
                                {
                                    "stock_id": "1618",
                                    "warrant_flow_signal": "call_inflow",
                                    "future_shared_semantic": "canonical_value",
                                }
                            ]
                        ),
                        "20260530",
                    )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir

    def test_volume_v2_dispatcher_ignores_unregistered_candidate_only_field(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1618",
                    "stock_name": "MID",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        original_score_profile = model_layer.score_volume_breakout_profile
        candidate_field_seen: list[bool] = []

        def score_probe(row: pd.Series, profile_id: str):
            candidate_field_seen.append("future_candidate_only_semantic" in row.index)
            return original_score_profile(row, profile_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "1618.csv",
                mid_position_volume_v2_price_history(),
            )
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            model_layer.score_volume_breakout_profile = score_probe
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidate_rows_with_lineage(
                        [
                            {
                                "stock_id": "1618",
                                "warrant_flow_signal": "call_inflow",
                                "future_candidate_only_semantic": "injected",
                            }
                        ]
                    ),
                    "20260530",
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir
                model_layer.score_volume_breakout_profile = original_score_profile

        self.assertEqual(len(out), 1)
        self.assertEqual(candidate_field_seen, [False])

    def test_volume_v2_dispatcher_rejects_stale_advisory_day(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "advisory lineage date mismatch"):
            self._dispatch_mid_volume_fixture(
                watch_updates={
                    "signal_date": "20260529",
                    "advisory_score_as_of": "20260529",
                }
            )

    def test_volume_v2_dispatcher_rejects_tampered_advisory_source_sha(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "source SHA-256 mismatch"):
            self._dispatch_mid_volume_fixture(
                watch_updates={"advisory_score_source_sha256": "0" * 64}
            )

    def test_volume_v2_watch_advisory_lineage_resolves_repo_relative_source(self) -> None:
        original_file = model_layer.__file__
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source_path = root / "data" / "stock_price_history" / "1618.csv"
            source_path.parent.mkdir(parents=True)
            source_path.write_text(
                "date,stock_id,close\n20260530,1618,42\n",
                encoding="utf-8",
            )
            row = pd.Series(
                {
                    "stock_id": "1618",
                    "signal_date": "20260530",
                    "advisory_score_as_of": "20260530",
                    "advisory_score_source_artifact": (
                        "data/stock_price_history/1618.csv"
                    ),
                    "advisory_score_source_sha256": (
                        model_layer.volume_v2_canonical_text_sha256(
                            source_path, "20260530"
                        )
                    ),
                }
            )
            model_layer.__file__ = str(root / "scripts" / "build_daily_candidate_model_layer.py")
            try:
                model_layer.validate_volume_v2_watch_advisory_lineage(
                    row, "20260530"
                )
            finally:
                model_layer.__file__ = original_file

    def test_volume_v2_lineage_producer_validator_consumer_parity(self) -> None:
        original_file = model_layer.__file__
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source_path = root / "data" / "stock_price_history" / "1618.csv"
            source_path.parent.mkdir(parents=True)
            as_of_text = (
                "date,stock_id,close\n"
                "20260529,1618,41\n"
                "20260530,1618,42\n"
            )
            source_path.write_text(
                as_of_text + "20260601,1618,43\n",
                encoding="utf-8",
            )
            expected = canonical_csv_slice_sha256(source_path, "20260530")
            self.assertEqual(
                validator_canonical_csv_slice_sha256(source_path, "20260530"),
                expected,
            )
            self.assertEqual(
                model_layer.volume_v2_canonical_text_sha256(
                    source_path, "20260530"
                ),
                expected,
            )
            watch = pd.DataFrame(
                [
                    {
                        "stock_id": "1618",
                        "signal_date": "20260530",
                        "advisory_score_as_of": "20260530",
                        "advisory_score_source_artifact": (
                            "data/stock_price_history/1618.csv"
                        ),
                        "advisory_score_source_sha256": expected,
                    }
                ]
            )
            self.assertEqual(advisory_source_lineage_errors(watch, root), [])

            model_layer.__file__ = str(root / "scripts" / "build_daily_candidate_model_layer.py")
            try:
                model_layer.validate_volume_v2_watch_advisory_lineage(
                    watch.iloc[0], "20260530"
                )
                source_path.write_text(
                    as_of_text
                    + "20260603,1618,45\n"
                    + "20260601,1618,43\n"
                    + "20260603,1618,999\n",
                    encoding="utf-8",
                )
                model_layer.validate_volume_v2_watch_advisory_lineage(
                    watch.iloc[0], "20260530"
                )
                self.assertEqual(advisory_source_lineage_errors(watch, root), [])
                source_path.write_text(
                    as_of_text
                    + "20260603,1618,998\n"
                    + "20260601,1618,999\n"
                    + "20260603,1618,997\n",
                    encoding="utf-8",
                )
                model_layer.validate_volume_v2_watch_advisory_lineage(
                    watch.iloc[0], "20260530"
                )
                self.assertEqual(advisory_source_lineage_errors(watch, root), [])

                source_path.write_text(
                    "date,stock_id,close\n"
                    "20260529,1618,40\n"
                    "20260530,1618,42\n"
                    "20260601,1618,43\n",
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(RuntimeError, "source SHA-256 mismatch"):
                    model_layer.validate_volume_v2_watch_advisory_lineage(
                        watch.iloc[0], "20260530"
                    )
                self.assertTrue(advisory_source_lineage_errors(watch, root))
            finally:
                model_layer.__file__ = original_file

    def test_volume_v2_watch_advisory_lineage_rejects_missing_relative_source(self) -> None:
        row = pd.Series(
            {
                "stock_id": "1618",
                "signal_date": "20260530",
                "advisory_score_as_of": "20260530",
                "advisory_score_source_artifact": "data/stock_price_history/missing.csv",
                "advisory_score_source_sha256": "0" * 64,
            }
        )

        with self.assertRaisesRegex(RuntimeError, "source artifact is missing"):
            model_layer.validate_volume_v2_watch_advisory_lineage(row, "20260530")

    def test_volume_v2_watch_advisory_lineage_rejects_tampered_relative_sha(self) -> None:
        original_file = model_layer.__file__
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source_path = root / "data" / "stock_price_history" / "1618.csv"
            source_path.parent.mkdir(parents=True)
            source_path.write_text(
                "date,stock_id,close\n20260530,1618,42\n",
                encoding="utf-8",
            )
            row = pd.Series(
                {
                    "stock_id": "1618",
                    "signal_date": "20260530",
                    "advisory_score_as_of": "20260530",
                    "advisory_score_source_artifact": (
                        "data/stock_price_history/1618.csv"
                    ),
                    "advisory_score_source_sha256": "0" * 64,
                }
            )
            model_layer.__file__ = str(root / "scripts" / "build_daily_candidate_model_layer.py")
            try:
                with self.assertRaisesRegex(RuntimeError, "source SHA-256 mismatch"):
                    model_layer.validate_volume_v2_watch_advisory_lineage(
                        row, "20260530"
                    )
            finally:
                model_layer.__file__ = original_file

    def test_volume_v2_dispatcher_sha_is_lf_crlf_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            lf_path = Path(tmpdir) / "lf.csv"
            crlf_path = Path(tmpdir) / "crlf.csv"
            lf_path.write_bytes(b"date,stock_id\n20260530,1618\n")
            crlf_path.write_bytes(b"date,stock_id\r\n20260530,1618\r\n")

            self.assertEqual(
                model_layer.volume_v2_canonical_text_sha256(lf_path),
                model_layer.volume_v2_canonical_text_sha256(crlf_path),
            )

    def test_volume_v2_dispatcher_rejects_ambiguous_candidate_duplicates(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "call_inflow",
                    "score": "70",
                    "rank": "1",
                },
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "put_inflow",
                    "score": "70",
                    "rank": "1",
                },
            ]
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "conflicting canonical warrant signals",
        ):
            self._dispatch_mid_volume_fixture(candidates=candidates)

    def test_volume_v2_dispatcher_ignores_non_relevant_ambiguous_duplicates(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {"stock_id": "1618", "warrant_flow_signal": "call_inflow"},
                {
                    "stock_id": "1808",
                    "warrant_flow_signal": "call_inflow",
                    "tdcc_status": "accumulation",
                },
                {
                    "stock_id": "1808",
                    "warrant_flow_signal": "put_inflow",
                    "tdcc_status": "distribution",
                },
            ]
        )

        out = self._dispatch_mid_volume_fixture(candidates=candidates)

        self.assertEqual(len(out), 1)
        self.assertEqual(out.iloc[0]["stock_id"], "1618")

    def test_volume_v2_dispatcher_rejects_relevant_consumed_field_conflict(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "call_inflow",
                    "tdcc_status": "accumulation",
                },
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "call_inflow",
                    "tdcc_status": "distribution",
                },
            ]
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "change formal model outcome.*conflicting_fields=.*tdcc_status",
        ):
            self._dispatch_mid_volume_fixture(candidates=candidates)

    def test_volume_v2_dispatcher_resolves_equal_rows_and_preserves_lineage(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "call_inflow",
                    "score": "70",
                    "rank": "1",
                    "theme_group": "theme_a",
                    "category": "range_rebound",
                },
                {
                    "stock_id": "1618",
                    "warrant_flow_signal": "call_inflow",
                    "score": "99",
                    "rank": "9",
                    "theme_group": "theme_b",
                    "category": "pattern",
                },
            ]
        )

        out = self._dispatch_mid_volume_fixture(candidates=candidates)

        self.assertEqual(len(out), 1)
        self.assertEqual(out.iloc[0]["warrant_flow_signal"], "call_inflow")
        self.assertEqual(
            len(out.iloc[0]["candidate_source_row_ids"].split("|")), 2
        )
        self.assertEqual(
            set(out.iloc[0]["candidate_source_categories"].split("|")),
            {"range_rebound", "pattern"},
        )

    def test_exact_2451_raw_sources_reach_lookup_with_distinct_lineage(self) -> None:
        columns = [
            "date",
            "stock_id",
            "ticker",
            "category",
            "platform_high",
            "short_platform_high",
            "platform_width_pct",
            "short_platform_width_pct",
            "false_breakout_risk",
            "revenue_yoy_pct",
            "cumulative_yoy_pct",
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            range_path = temp_dir / "range_rebound_watch_latest.csv"
            revenue_path = temp_dir / "revenue_pullback_latest.csv"
            pd.DataFrame(
                [
                    {
                        "date": "20260731",
                        "stock_id": "2451",
                        "ticker": "2451",
                        "category": "range_rebound",
                        "platform_high": "280",
                        "short_platform_high": "280",
                        "platform_width_pct": "29.63",
                        "short_platform_width_pct": "29.63",
                        "false_breakout_risk": "False",
                        "revenue_yoy_pct": "381.5468504599",
                        "cumulative_yoy_pct": "422.1697253819",
                    }
                ],
                columns=columns,
            ).to_csv(range_path, index=False, encoding="utf-8-sig")
            pd.DataFrame(
                [
                    {
                        "date": "20260731",
                        "stock_id": "2451",
                        "ticker": "2451",
                        "category": "revenue_pullback",
                        "platform_high": "",
                        "short_platform_high": "",
                        "platform_width_pct": "",
                        "short_platform_width_pct": "",
                        "false_breakout_risk": "",
                        "revenue_yoy_pct": "381.55",
                        "cumulative_yoy_pct": "422.17",
                    }
                ],
                columns=columns,
            ).to_csv(revenue_path, index=False, encoding="utf-8-sig")
            loaded = pd.concat(
                [
                    all_candidates_builder.load_source_file(
                        {
                            "path": range_path,
                            "producer": "stock_daily_monitor.py",
                            "default_category": "range_rebound",
                            "default_category_cn": "range rebound",
                        }
                    ),
                    all_candidates_builder.load_source_file(
                        {
                            "path": revenue_path,
                            "producer": "stock_daily_monitor.py",
                            "default_category": "revenue_pullback",
                            "default_category_cn": "revenue pullback",
                        }
                    ),
                ],
                ignore_index=True,
                sort=False,
            )

        sourced_rows = model_layer.volume_v2_candidate_lookup(
            loaded, {"2451"}
        )["2451"]
        self.assertEqual(len(sourced_rows), 2)
        self.assertEqual(
            {row["candidate_source_identity_columns"] for row in sourced_rows},
            {"stock_id;ticker"},
        )
        self.assertEqual(
            {row["candidate_source_producer"] for row in sourced_rows},
            {"stock_daily_monitor.py"},
        )
        self.assertEqual(
            {row["category"] for row in sourced_rows},
            {"range_rebound", "revenue_pullback"},
        )
        self.assertEqual(
            len({row["candidate_source_row_id"] for row in sourced_rows}), 2
        )

    def test_all_candidates_same_grain_duplicate_fails_before_silent_choice(self) -> None:
        rows = pd.DataFrame(
            [
                {
                    "date": "20260731",
                    "category": "range_rebound",
                    "stock_id": "2451",
                    "score": "80",
                    "rank": "1",
                    "candidate_source_artifact": "source.csv",
                    "candidate_source_record_number": "2",
                    "candidate_source_row_id": "source-row-a",
                },
                {
                    "date": "20260731",
                    "category": "range_rebound",
                    "stock_id": "2451",
                    "score": "79",
                    "rank": "2",
                    "candidate_source_artifact": "source.csv",
                    "candidate_source_record_number": "3",
                    "candidate_source_row_id": "source-row-b",
                },
            ]
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "duplicate source rows at the canonical date/category/stock_id grain",
        ):
            all_candidates_builder.deduplicate_candidates(rows)

    def test_volume_v2_dispatcher_rejects_duplicate_selected_watch_rows(self) -> None:
        with self.assertRaisesRegex(
            RuntimeError,
            "duplicate selected normalized stock rows",
        ):
            self._dispatch_mid_volume_fixture(duplicate_selected_watch=True)

    def test_volume_v2_dispatcher_identical_duplicates_are_deterministic(self) -> None:
        row = {
            "stock_id": "1618",
            "signal_date": "20260530",
            "warrant_flow_signal": "call_inflow",
            "tdcc_status": "accumulation",
        }
        candidates = candidate_rows_with_lineage([row, dict(row)])

        first = self._dispatch_mid_volume_fixture(candidates=candidates)
        second = self._dispatch_mid_volume_fixture(
            candidates=candidates.iloc[::-1].reset_index(drop=True)
        )

        source_specific_fields = {
            "candidate_presentation_source_artifact",
            "candidate_presentation_source_artifact_sha256",
        }
        pd.testing.assert_frame_equal(
            first.drop(columns=source_specific_fields),
            second.drop(columns=source_specific_fields),
        )
        first_descriptor = json.loads(
            first.iloc[0]["candidate_presentation_source_artifact"]
        )
        second_descriptor = json.loads(
            second.iloc[0]["candidate_presentation_source_artifact"]
        )
        for descriptor in (first_descriptor, second_descriptor):
            self.assertEqual(
                descriptor["candidate_source_row_ids"],
                sorted(descriptor["candidate_source_row_ids"]),
            )
            self.assertEqual(
                descriptor["presentation_row_sha256"],
                first.iloc[0]["candidate_presentation_source_row_sha256"],
            )

    def test_volume_v2_dispatcher_preserves_2451_complementary_source_rows(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {
                    "stock_id": "2451",
                    "category": "range_rebound",
                    "candidate_source_artifact": "output/latest/range_rebound_watch_latest.csv",
                    "platform_high": "280",
                    "short_platform_high": "280",
                    "platform_width_pct": "29.63",
                    "short_platform_width_pct": "29.63",
                    "false_breakout_risk": "False",
                    "revenue_yoy_pct": "381.5468504599",
                    "cumulative_yoy_pct": "422.1697253819",
                    "signal_date": "20260731",
                    "warrant_flow_signal": "call_inflow",
                },
                {
                    "stock_id": "2451",
                    "category": "revenue_pullback",
                    "candidate_source_artifact": "output/latest/revenue_pullback_latest.csv",
                    "platform_high": "",
                    "short_platform_high": "",
                    "platform_width_pct": "",
                    "short_platform_width_pct": "",
                    "false_breakout_risk": "",
                    "revenue_yoy_pct": "381.55",
                    "cumulative_yoy_pct": "422.17",
                    "signal_date": "20260731",
                    "warrant_flow_signal": "call_inflow",
                },
            ]
        )

        sourced_rows = model_layer.volume_v2_candidate_lookup(candidates, {"2451"})["2451"]
        reversed_sourced_rows = model_layer.volume_v2_candidate_lookup(
            candidates.iloc[::-1].reset_index(drop=True), {"2451"}
        )["2451"]

        self.assertEqual(len(sourced_rows), 2)
        self.assertEqual(
            [row["candidate_source_row_id"] for row in sourced_rows],
            [row["candidate_source_row_id"] for row in reversed_sourced_rows],
        )
        self.assertEqual(
            {row["category"] for row in sourced_rows},
            {"range_rebound", "revenue_pullback"},
        )

    def test_volume_v2_dispatcher_2451_projection_keeps_score_parity(self) -> None:
        stock_id = "2451"
        canonical = candidate_rows_with_lineage(
            [
                {
                    "stock_id": stock_id,
                    "platform_high": "280",
                    "short_platform_high": "280",
                    "platform_width_pct": "29.63",
                    "short_platform_width_pct": "29.63",
                    "false_breakout_risk": "False",
                    "revenue_yoy_pct": "381.5468504599",
                    "cumulative_yoy_pct": "422.1697253819",
                    "signal_date": "20260530",
                    "warrant_flow_signal": "call_inflow",
                }
            ]
        )
        complementary = candidate_rows_with_lineage(
            [
                dict(canonical.iloc[0], category="range_rebound"),
                {
                    "stock_id": stock_id,
                    "category": "revenue_pullback",
                    "platform_high": "",
                    "short_platform_high": "",
                    "platform_width_pct": "",
                    "short_platform_width_pct": "",
                    "false_breakout_risk": "",
                    "revenue_yoy_pct": "381.55",
                    "cumulative_yoy_pct": "422.17",
                    "signal_date": "20260530",
                    "warrant_flow_signal": "call_inflow",
                },
            ]
        )

        baseline = self._dispatch_mid_volume_fixture(
            candidates=canonical,
            stock_id=stock_id,
        )
        projected = self._dispatch_mid_volume_fixture(
            candidates=complementary,
            stock_id=stock_id,
        )

        parity_columns = [
            "model_id",
            "stock_id",
            "model_score",
            "final_rank_score",
            "model_rank",
            "score_components",
            "risk_penalty_tags",
            "warrant_flow_signal",
        ]
        pd.testing.assert_frame_equal(
            baseline[parity_columns].reset_index(drop=True),
            projected[parity_columns].reset_index(drop=True),
        )
        presentation_columns = [
            "stock_name",
            "industry",
            "primary_theme",
            "effective_primary_theme",
            "secondary_themes",
            "effective_structural_theme_bucket",
            "effective_mainstream_label",
            "report_line_memberships",
            "mainstream_report_eligible",
            "non_mainstream_report_eligible",
            "dual_report_membership_flag",
            "report_bucket",
        ]
        pd.testing.assert_frame_equal(
            baseline[presentation_columns].reset_index(drop=True),
            projected[presentation_columns].reset_index(drop=True),
        )
        self.assertEqual(projected.iloc[0]["original_category"], "volume_breakout")
        sourced_rows = model_layer.volume_v2_candidate_lookup(
            complementary, {stock_id}
        )[stock_id]
        self.assertEqual(
            projected.iloc[0]["candidate_source_row_ids"].split("|"),
            [row["candidate_source_row_id"] for row in sourced_rows],
        )
        self.assertEqual(
            projected.iloc[0]["candidate_source_row_sha256s"].split("|"),
            [row["candidate_source_row_sha256"] for row in sourced_rows],
        )
        self.assertEqual(
            projected.iloc[0]["candidate_source_categories"].split("|"),
            [row.get("category", "") or "<blank>" for row in sourced_rows],
        )
        self.assertRegex(
            projected.iloc[0]["candidate_formal_outcome_sha256"],
            r"^[0-9a-f]{64}$",
        )
        self.assertEqual(
            projected.iloc[0]["candidate_formal_outcome_sha256"],
            model_layer._volume_v2_formal_outcome_sha256(projected.iloc[0]),
        )
        presentation = {
            "stock_name": projected.iloc[0]["stock_name"],
            "industry": projected.iloc[0]["industry"],
            "primary_theme": projected.iloc[0]["primary_theme"],
            "secondary_themes": projected.iloc[0]["secondary_themes"],
            "effective_structural_theme_bucket": projected.iloc[0][
                "effective_structural_theme_bucket"
            ],
            "effective_mainstream_label": projected.iloc[0][
                "effective_mainstream_label"
            ],
            "report_line_memberships": projected.iloc[0][
                "report_line_memberships"
            ],
            "mainstream_report_eligible": projected.iloc[0][
                "mainstream_report_eligible"
            ],
            "non_mainstream_report_eligible": projected.iloc[0][
                "non_mainstream_report_eligible"
            ],
            "dual_report_membership_flag": projected.iloc[0][
                "dual_report_membership_flag"
            ],
            "report_bucket": projected.iloc[0]["report_bucket"],
        }
        expected_presentation_sha = hashlib.sha256(
            json.dumps(
                presentation,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(
            projected.iloc[0]["candidate_presentation_source_row_sha256"],
            expected_presentation_sha,
        )
        descriptor_text = projected.iloc[0][
            "candidate_presentation_source_artifact"
        ]
        descriptor = json.loads(descriptor_text)
        self.assertEqual(
            descriptor["contract"], "volume_v2_formal_presentation_v1"
        )
        self.assertEqual(descriptor["mode"], "all_candidates")
        self.assertEqual(
            descriptor["candidate_source_row_ids"],
            projected.iloc[0]["candidate_source_row_ids"].split("|"),
        )
        self.assertEqual(
            descriptor["candidate_source_row_sha256s"],
            projected.iloc[0]["candidate_source_row_sha256s"].split("|"),
        )
        self.assertEqual(
            descriptor["candidate_source_categories"],
            projected.iloc[0]["candidate_source_categories"].split("|"),
        )
        self.assertEqual(
            descriptor["presentation_row_sha256"],
            expected_presentation_sha,
        )
        self.assertEqual(
            projected.iloc[0][
                "candidate_presentation_source_artifact_sha256"
            ],
            hashlib.sha256(descriptor_text.encode("utf-8")).hexdigest(),
        )
        report = model_layer.build_report_ready_model_signals(projected)
        for field in [
            "candidate_source_row_ids",
            "candidate_source_row_sha256s",
            "candidate_source_categories",
            "candidate_formal_outcome_sha256",
            "candidate_presentation_source_artifact",
            "candidate_presentation_source_artifact_sha256",
            "candidate_presentation_source_row_sha256",
        ]:
            self.assertEqual(report.iloc[0][field], projected.iloc[0][field])

    def test_volume_v2_dispatcher_rejects_conflict_that_changes_formal_outcome(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {"stock_id": "1618", "revenue_yoy_pct": "29.99"},
                {"stock_id": "1618", "revenue_yoy_pct": "30.00"},
            ]
        )

        with self.assertRaisesRegex(RuntimeError, "change formal model outcome"):
            self._dispatch_mid_volume_fixture(candidates=candidates)

    def test_volume_v2_dispatcher_rejects_conflicting_presentation(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {"stock_id": "1618", "industry": "industry_a"},
                {"stock_id": "1618", "industry": "industry_b"},
            ]
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "change formal presentation.*conflicting_fields=industry",
        ):
            self._dispatch_mid_volume_fixture(candidates=candidates)

    def test_volume_v2_dispatcher_rejects_non_equity_identity_collapse(self) -> None:
        candidates = candidate_rows_with_lineage(
            [
                {
                    "stock_id": "2451",
                    "candidate_source_raw_stock_id": "2451A",
                    "candidate_source_normalized_stock_id": "2451",
                }
            ]
        )

        with self.assertRaisesRegex(RuntimeError, "would collapse a non-equity identifier"):
            model_layer.volume_v2_candidate_lookup(candidates, {"2451"})

    def test_volume_v2_dispatcher_rejects_duplicate_rows_without_source_lineage(self) -> None:
        candidates = pd.DataFrame(
            [
                {"stock_id": "2451", "platform_high": "280"},
                {"stock_id": "2451", "platform_high": ""},
            ]
        )

        with self.assertRaisesRegex(RuntimeError, "missing source identity lineage"):
            model_layer.volume_v2_candidate_lookup(candidates, {"2451"})

    def test_volume_v2_dispatcher_rejects_duplicate_source_row_id(self) -> None:
        candidate = candidate_rows_with_lineage([{"stock_id": "2451"}])
        candidates = pd.concat([candidate, candidate.copy()], ignore_index=True)

        with self.assertRaisesRegex(RuntimeError, "reuse candidate_source_row_id"):
            model_layer.volume_v2_candidate_lookup(candidates, {"2451"})

    def test_volume_v2_dispatcher_fails_on_stale_watch_score_rank_collision(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "1618",
                    "stock_name": "MID",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior20_high_102pct|volume_ratio_ge_2",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                    "score": "999",
                    "rank": "999",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "1618.csv",
                mid_position_volume_v2_price_history(),
            )
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                with self.assertRaisesRegex(
                    RuntimeError,
                    "unregistered same-name field collision.*rank.*score",
                ):
                    model_layer.append_volume_breakout_signals(
                        pd.DataFrame(),
                        candidate_rows_with_lineage(
                            [
                                {
                                    "stock_id": "1618",
                                    "warrant_flow_signal": "call_inflow",
                                    "score": "1",
                                    "rank": "1",
                                }
                            ]
                        ),
                        "20260530",
                    )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir

    def test_high_position_volume_breakout_requires_ma60_above_ma120(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "2489",
                    "stock_name": "HIGH",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_score": "88",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "volume_breakout_notes": "close_ge_prior60_high_102pct|volume_ratio_ge_2",
                    "volume_ratio": "3.0",
                    "range_width_40_pct": "45",
                    "warrant_flow_signal": "no_signal",
                    "next_volume_breakout_confirmation": "next day continuation close-only",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "2489.csv",
                high_position_volume_v2_price_history(),
            )
            source_bytes_before = temp_path.read_bytes()
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidate_rows_with_lineage(
                        [
                            {
                                "stock_id": "2489",
                                "warrant_flow_signal": "call_inflow",
                                "category": "range_rebound",
                            },
                            {
                                "stock_id": "2489",
                                "warrant_flow_signal": "call_inflow",
                                "category": "pattern",
                            },
                        ]
                    ),
                    "20260530",
                )
                out_without_warrant = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(),
                    candidate_rows_with_lineage(
                        [
                            {
                                "stock_id": "2489",
                                "warrant_flow_signal": "no_signal",
                                "category": "range_rebound",
                            },
                            {
                                "stock_id": "2489",
                                "warrant_flow_signal": "no_signal",
                                "category": "pattern",
                            },
                        ]
                    ),
                    "20260530",
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir
            source_bytes_after = temp_path.read_bytes()

        self.assertEqual(source_bytes_before, source_bytes_after)
        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["model_id"], HIGH_VOLUME_MODEL_ID)
        self.assertEqual(row["volume_position_bucket_120d"], "high_pos_gt75")
        self.assertEqual(row["volume_shape_bucket"], "non_consolidation")
        self.assertEqual(row["volume_ma60_gt_ma120"], "True")
        self.assertEqual(row["warrant_flow_signal"], "call_inflow")
        self.assertEqual(len(row["candidate_source_row_ids"].split("|")), 2)
        self.assertEqual(row["model_score"], out_without_warrant.iloc[0]["model_score"])
        self.assertNotIn("warrant bullish", row["score_components"])
        self.assertIn("profile=volume_range_breakout_v2_high_position_volume_attack", row["score_components"])
        self.assertNotIn("一價鎖漲停放量突破", row["rank_reason_zh"])

    def test_volume_breakout_without_candidate_ignores_global_official_warrant_row(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "stock_id": "2059",
                    "stock_name": "CHUAN_HU",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "warrant_flow_signal": "call_inflow",
                    "volume_ratio": "3.17",
                }
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_warrant_path = model_layer.WARRANT_FLOW
        original_price_dir = model_layer.STOCK_PRICE_HISTORY_DIR
        original_taxonomy_path = model_layer.VOLUME_BREAKOUT_TAXONOMY
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_path = temp_dir / "volume_breakout_watch_latest.csv"
            warrant_path = temp_dir / "warrant_flow_latest.csv"
            taxonomy_path = temp_dir / "stock_theme_taxonomy_latest.csv"
            price_dir = temp_dir / "stock_price_history"
            price_dir.mkdir()
            write_volume_v2_watch_fixture(
                source,
                temp_path,
                price_dir / "2059.csv",
                volume_v2_price_history(),
            )
            pd.DataFrame(
                [
                    {
                        "date": "20260530",
                        "stock_id": "9999",
                        "warrant_flow_signal": "no_signal",
                    }
                ]
            ).to_csv(warrant_path, index=False, encoding="utf-8-sig")
            pd.DataFrame(
                [
                    {
                        "stock_id": "2059",
                        "industry": "electronic",
                        "effective_primary_theme": "electronic_component_general_theme",
                        "effective_mainstream_label": "core_mainstream",
                    }
                ]
            ).to_csv(taxonomy_path, index=False, encoding="utf-8-sig")
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.WARRANT_FLOW = warrant_path
            model_layer.STOCK_PRICE_HISTORY_DIR = price_dir
            model_layer.VOLUME_BREAKOUT_TAXONOMY = taxonomy_path
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(), pd.DataFrame(), "20260530"
                )
                pd.DataFrame(
                    [
                        {
                            "date": "20260530",
                            "stock_id": "2059",
                            "warrant_flow_signal": "call_inflow",
                        }
                    ]
                ).to_csv(warrant_path, index=False, encoding="utf-8-sig")
                out_with_global_warrant = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(), pd.DataFrame(), "20260530"
                )
                pd.DataFrame(
                    [
                        {
                            "date": "20260530",
                            "stock_id": "2059",
                            "warrant_flow_signal": "call_inflow",
                        },
                        {
                            "date": "20260530",
                            "stock_id": "2059",
                            "warrant_flow_signal": "no_signal",
                        },
                    ]
                ).to_csv(warrant_path, index=False, encoding="utf-8-sig")
                with self.assertRaisesRegex(
                    RuntimeError,
                    "duplicate normalized identities",
                ):
                    model_layer.append_volume_breakout_signals(
                        pd.DataFrame(), pd.DataFrame(), "20260530"
                    )
                pd.DataFrame(
                    [
                        {
                            "date": "20260530",
                            "stock_id": "9999",
                            "warrant_flow_signal": "no_signal",
                        }
                    ]
                ).to_csv(warrant_path, index=False, encoding="utf-8-sig")
                pd.DataFrame(
                    [{"stock_id": "9999", "industry": "other"}]
                ).to_csv(taxonomy_path, index=False, encoding="utf-8-sig")
                with self.assertRaisesRegex(
                    RuntimeError,
                    "no canonical taxonomy source row: stock_id=2059",
                ):
                    model_layer.append_volume_breakout_signals(
                        pd.DataFrame(), pd.DataFrame(), "20260530"
                    )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.WARRANT_FLOW = original_warrant_path
                model_layer.STOCK_PRICE_HISTORY_DIR = original_price_dir
                model_layer.VOLUME_BREAKOUT_TAXONOMY = original_taxonomy_path

        self.assertEqual(len(out), 1)
        self.assertEqual(out.iloc[0]["stock_id"], "2059")
        self.assertEqual(out.iloc[0]["warrant_flow_signal"], "")
        self.assertNotIn("warrant bullish", out.iloc[0]["score_components"])
        self.assertEqual(len(out_with_global_warrant), 1)
        self.assertEqual(out_with_global_warrant.iloc[0]["warrant_flow_signal"], "")
        self.assertEqual(
            out_with_global_warrant.iloc[0]["model_score"], out.iloc[0]["model_score"]
        )

    def test_nonmember_volume_watch_rows_skip_before_provenance_checks(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260716",
                    "stock_id": stock_id,
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                }
                for stock_id in ("4139", "1439")
            ]
        )
        original_path = model_layer.VOLUME_BREAKOUT_WATCH
        original_memberships = model_layer.volume_v2_model_memberships
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = Path(tmpdir) / "volume_breakout_watch_latest.csv"
            source.to_csv(temp_path, index=False, encoding="utf-8-sig")
            model_layer.VOLUME_BREAKOUT_WATCH = temp_path
            model_layer.volume_v2_model_memberships = lambda *_args, **_kwargs: ([], {})
            try:
                out = model_layer.append_volume_breakout_signals(
                    pd.DataFrame(), pd.DataFrame(), "20260716"
                )
            finally:
                model_layer.VOLUME_BREAKOUT_WATCH = original_path
                model_layer.volume_v2_model_memberships = original_memberships

        self.assertTrue(out.empty)

    def test_pullback_model_does_not_require_breakout(self) -> None:
        row = make_row(
            volume_breakout_type="",
            close_above_range_high="False",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.3",
        )
        self.assertTrue(cond_pullback(row))

    def test_pullback_v1_requires_tdcc_obv_and_uses_quality_tags_without_score_ranking(self) -> None:
        positive = make_row(
            return_20d="12",
            return_20d_pct="12",
        )
        missing_tdcc = make_row(
            price_pullback_tdcc_history_available="False",
            price_pullback_high_thresholds_up="False",
        )
        overextended = make_row(
            return_20d="38",
            return_20d_pct="38",
        )

        self.assertTrue(cond_pullback(positive))
        self.assertFalse(cond_pullback(missing_tdcc))
        self.assertFalse(cond_pullback(overextended))

        positive_score, positive_components, positive_risks = score_pullback(positive)

        self.assertEqual(positive_score, 70.0)
        self.assertIn("price_pullback_v1_required_gate", positive_components)
        self.assertIn("price_pullback_return20_0_25_required", positive_components)
        self.assertIn("price_pullback_tdcc_high_thresholds_up_required", positive_components)
        self.assertIn("price_pullback_obv_above_ma20_required", positive_components)
        self.assertIn("price_pullback_technical_strength_package", positive_components)
        self.assertNotIn("price_pullback_return20_over_25_no_bonus", positive_risks)

    def test_selection_audit_validates_price_pullback_enriched_signal_context(self) -> None:
        source = make_row(
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.3",
            return_20d="12",
            return_20d_pct="12",
            price_pullback_tdcc_history_available="",
            price_pullback_high_thresholds_up="",
            price_pullback_obv_above_ma20="",
        )
        selected = pd.Series(
            {
                "stock_id": "9999",
                "model_id": "price_pullback_23ema",
                "main_condition_met": "True",
                "price_pullback_tdcc_history_available": "True",
                "price_pullback_high_thresholds_up": "True",
                "price_pullback_obv_above_ma20": "True",
            }
        )

        self.assertTrue(selected_price_pullback_23ema_condition(selected, source))

        missing_obv = selected.copy()
        missing_obv["price_pullback_obv_above_ma20"] = "False"
        self.assertFalse(selected_price_pullback_23ema_condition(missing_obv, source))

    def test_pre_breakout_models_exclude_confirmed_breakouts(self) -> None:
        breakout = make_row(
            category="true_breakout",
            volume_breakout_type="bottom_volume_attack",
            platform_breakout_flag="True",
            neckline_breakout_flag="True",
            volume_confirmed_breakout="True",
            close_above_range_high="True",
            distance_to_previous_high_pct="1.0",
            platform_base_flag="True",
            platform_width_pct="10",
            volume_ratio="3.5",
            previous_20d_high="100",
            volume_ma20="2000",
            ema23_slope_pct="0.5",
            close="105",
            open="100",
        )
        signals = build_signals(pd.DataFrame([breakout]), build_specs(), "20260709")
        selected_models = set(signals.get("model_id", pd.Series(dtype=str)).astype(str))
        self.assertNotIn("near_high_neckline_challenge", selected_models)
        self.assertNotIn("platform_strengthening", selected_models)

    def test_w_bottom_requires_double_bottom_geometry_not_generic_pattern_flag(self) -> None:
        broad_flag = make_row(
            category="range_rebound",
            w_bottom_flag="True",
            w_bottom_right_side_flag="True",
            pattern_stage="neckline_challenge",
            second_low_gap_pct="",
            distance_to_neckline_pct="",
        )
        self.assertFalse(cond_w_bottom_right(broad_flag))

        generic_platform = make_row(
            category="pattern",
            w_bottom_flag="True",
            w_bottom_right_side_flag="True",
            pattern_stage="platform_right_side",
            second_low_gap_pct="",
            distance_to_neckline_pct="",
        )
        self.assertFalse(cond_w_bottom_right(generic_platform))

        clean_w = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            w_bottom_flag="",
            w_bottom_right_side_flag="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
            red_body_ratio_2_vs_1="1.2",
        )
        self.assertTrue(cond_w_bottom_right(clean_w))

        higher_position_clean_w = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="58",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
            red_body_ratio_2_vs_1="1.2",
        )
        self.assertTrue(cond_w_bottom_right(higher_position_clean_w))

        slight_undercut = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="-0.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertTrue(cond_w_bottom_right(slight_undercut))

        deep_undercut = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="-4.0",
            distance_to_neckline_pct="-12.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(deep_undercut))

        right_low_too_high = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="12.0",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(right_low_too_high))

        far_from_neckline_but_turning_up = make_row(
            category="pattern",
            pattern_stage="right_side_rebound",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-12.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="5.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertTrue(cond_w_bottom_right(far_from_neckline_but_turning_up))

        right_side_too_early = make_row(
            category="pattern",
            pattern_stage="right_side_rebound",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-12.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="2.5",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(right_side_too_early))

        right_side_too_extended = make_row(
            category="pattern",
            pattern_stage="right_side_rebound",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="18.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(right_side_too_extended))

        weak_second_attack = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.8",
            red_body_ratio_2_vs_1="2.0",
        )
        self.assertTrue(cond_w_bottom_right(weak_second_attack))

        high_level_pullback = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="62",
            w_bottom_base_width_pct="18",
            return_20d_pct="42",
            distance_to_previous_60d_high_pct="-0.5",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(high_level_pullback))

        no_base_context = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="",
            w_bottom_base_width_pct="",
            platform_width_pct="",
            short_platform_width_pct="",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(no_base_context))

        already_broken = make_row(
            category="pattern",
            pattern_stage="breakout_confirmed",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="1.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="5.0",
            attack2_gain_pct="9.0",
            volume_ratio_2_vs_1="1.6",
        )
        self.assertFalse(cond_w_bottom_right(already_broken))

        range_rebound_with_detected_w = make_row(
            stock_id="1618",
            category="range_rebound",
            pattern_stage="neckline_challenge",
            signal_date="20260529",
            volume_breakout_type="",
            close_above_range_high="",
        )
        self.assertFalse(cond_w_bottom_right(range_rebound_with_detected_w))

    def test_w_bottom_requires_second_arc_volume_not_red_body_only(self) -> None:
        red_body_only = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            volume_breakout_type="",
            close_above_range_high="",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="9.0",
            second_arc_volume_ratio="0.9",
            red_body_ratio_2_vs_1="3.0",
        )

        self.assertFalse(cond_w_bottom_right(red_body_only))

    def test_detected_w_bottom_context_exposes_arc_volume_fields(self) -> None:
        context = model_layer.detected_w_bottom_context(
            make_row(stock_id="1618", signal_date="20260529", volume_breakout_type="")
        )

        self.assertTrue(context["available"])
        self.assertEqual(context["first_arc_start_date"], context["left_peak_date"])
        self.assertEqual(context["first_arc_end_date"], context["neckline_date"])
        self.assertEqual(context["second_arc_start_date"], context["neckline_date"])
        self.assertEqual(context["second_arc_end_date"], "20260529")
        self.assertTrue(context["w_shape_quality_passed"])
        self.assertEqual(context["w_shape_quality_failures"], "")
        self.assertTrue(context["w_bottom_long_position_ok"])
        self.assertLessEqual(float(context["w_bottom_current_vs_long_median_pct"]), 0.0)
        self.assertGreaterEqual(int(context["w_bottom_long_position_days"]), 180)
        self.assertGreaterEqual(int(context["left_descent_days"]), 5)
        self.assertGreaterEqual(int(context["first_rebound_days"]), 5)
        self.assertGreaterEqual(int(context["second_decline_days"]), 3)
        self.assertGreaterEqual(int(context["right_rebound_days"]), 4)
        self.assertGreater(float(context["first_arc_month_avg_volume"]), 0)
        self.assertGreater(float(context["second_arc_avg_daily_volume"]), 0)
        self.assertGreater(float(context["second_arc_volume_ratio"]), 0)
        self.assertGreaterEqual(float(context["first_arc_red_candle_ratio"]), 0.0)
        self.assertLessEqual(float(context["first_arc_red_candle_ratio"]), 1.0)
        self.assertGreaterEqual(float(context["second_arc_red_candle_ratio"]), 0.0)
        self.assertLessEqual(float(context["second_arc_red_candle_ratio"]), 1.0)

    def test_detected_w_bottom_rejects_disconnected_shape(self) -> None:
        row = make_row(
            stock_id="6462",
            signal_date="20260623",
            volume_breakout_type="",
            close_above_range_high="",
        )

        context = model_layer.detected_w_bottom_context(row)

        self.assertTrue(context["available"])
        self.assertFalse(context["context_ok"])
        self.assertFalse(context["w_shape_quality_passed"])
        self.assertIn("left_descent_too_short", context["w_shape_quality_failures"])
        self.assertIn("right_rebound_faded", context["w_shape_quality_failures"])
        self.assertFalse(cond_w_bottom_right(row))

    def test_w_bottom_segment_quality_rejects_faded_right_side(self) -> None:
        df = pd.DataFrame(
            {
                "high": [15, 14, 13, 12, 11, 10, 11, 12, 13, 14, 15, 14, 13, 12, 10, 14, 13, 12],
                "low": [14, 13, 12, 11, 10, 9.5, 10, 11, 12, 13, 14, 13, 12, 11, 9.6, 10, 9.8, 9.7],
                "close": [14.5, 13.5, 12.5, 11.5, 10.5, 9.8, 10.5, 11.5, 12.5, 13.5, 14.5, 13.5, 12.5, 11.5, 9.8, 13.5, 12.5, 10.0],
            }
        )

        quality = model_layer.w_bottom_segment_quality(
            df,
            left_peak_idx=0,
            left_low_idx=5,
            neckline_idx=10,
            right_low_idx=14,
            current_close=10.0,
        )

        self.assertFalse(quality["w_shape_quality_passed"])
        self.assertIn("right_rebound_faded", quality["w_shape_quality_failures"])

    def test_w_bottom_long_price_position_requires_below_year_median(self) -> None:
        history = pd.DataFrame({"close": list(range(1, 253))})

        low_metrics = model_layer.w_bottom_long_price_position_metrics(history, current_close=100.0)
        high_metrics = model_layer.w_bottom_long_price_position_metrics(history, current_close=200.0)

        self.assertTrue(low_metrics["w_bottom_long_position_ok"])
        self.assertFalse(high_metrics["w_bottom_long_position_ok"])
        self.assertEqual(high_metrics["w_bottom_long_position_fail_reason"], "current_close_above_long_median")

    def test_w_bottom_red_candle_bonus_uses_ratio_not_count(self) -> None:
        high_ratio = make_row(
            first_arc_red_candle_ratio="0.40",
            second_arc_red_candle_ratio="0.58",
        )
        mild_ratio = make_row(
            first_arc_red_candle_ratio="0.40",
            second_arc_red_candle_ratio="0.49",
        )
        count_only = make_row(
            red_body_ratio_2_vs_1="3.0",
        )

        high_bonus, high_components = model_layer.w_bottom_red_candle_ratio_bonus(high_ratio)
        mild_bonus, mild_components = model_layer.w_bottom_red_candle_ratio_bonus(mild_ratio)
        count_bonus, count_components = model_layer.w_bottom_red_candle_ratio_bonus(count_only)

        self.assertEqual(high_bonus, 4.0)
        self.assertTrue(any("second arc red candle ratio improved" in item for item in high_components))
        self.assertEqual(mild_bonus, 2.0)
        self.assertTrue(any("second arc red candle ratio mildly improved" in item for item in mild_components))
        self.assertEqual(count_bonus, 0.0)
        self.assertEqual(count_components, [])

    def test_w_bottom_score_adds_red_candle_ratio_bonus(self) -> None:
        row = make_row(
            category="pattern",
            pattern_stage="near_neckline",
            second_low_gap_pct="1.5",
            distance_to_neckline_pct="-2.0",
            w_bottom_low_position_pct="22",
            w_bottom_base_width_pct="18",
            attack1_gain_pct="8.0",
            attack2_gain_pct="9.0",
            second_arc_volume_ratio="1.35",
            first_arc_red_candle_ratio="0.40",
            second_arc_red_candle_ratio="0.58",
        )

        _score, components, _risks = model_layer.score_w_bottom(row)

        self.assertTrue(any("second arc red candle ratio improved +4" in item for item in components))

    def test_w_bottom_low_position_is_score_not_gate(self) -> None:
        low_position = make_row(w_bottom_low_position_pct="8")
        high_position = make_row(w_bottom_low_position_pct="48")

        low_score, low_components, low_risks = model_layer.w_bottom_low_position_score(low_position)
        high_score, high_components, high_risks = model_layer.w_bottom_low_position_score(high_position)

        self.assertEqual(low_score, 8.0)
        self.assertTrue(any("W low position very low +8" in item for item in low_components))
        self.assertEqual(low_risks, [])
        self.assertEqual(high_score, -5.0)
        self.assertEqual(high_components, [])
        self.assertTrue(any("W_low_position_too_high_penalty" in item for item in high_risks))

    def test_neckline_volume_breakout_confirmation_requires_arc_volume_quality(self) -> None:
        row = make_row(
            category="pattern",
            pattern_stage="neckline_breakout",
            close="105",
            open="101",
            high="106",
            low="100",
            previous_close="100",
            neckline_price="100",
            distance_to_neckline_pct="5.0",
            second_low_gap_pct="1.5",
            w_bottom_base_width_pct="18",
            second_arc_volume_ratio="1.35",
            first_arc_red_candle_ratio="0.40",
            second_arc_red_candle_ratio="0.58",
            neckline_context_filter_45="auto_non_bearish",
            neckline_context_filter_90="auto_non_bearish",
            volume_ratio="2.5",
            volume_ma20="2000",
        )
        weak_arc = row.copy()
        weak_arc["second_arc_volume_ratio"] = "1.0"

        self.assertTrue(cond_neckline_volume_breakout_confirmation(row))
        self.assertFalse(cond_neckline_volume_breakout_confirmation(weak_arc))
        _score, components, _risks = model_layer.score_neckline_volume_breakout_confirmation(row)
        self.assertTrue(any("second arc red candle ratio improved +4" in item for item in components))

    def test_neckline_locked_limit_up_bypasses_signal_volume_not_arc_volume(self) -> None:
        row = make_row(
            category="pattern",
            pattern_stage="neckline_breakout",
            close="110",
            open="110",
            high="110",
            low="110",
            previous_close="100",
            neckline_price="105",
            distance_to_neckline_pct="4.8",
            second_low_gap_pct="1.5",
            w_bottom_base_width_pct="18",
            second_arc_volume_ratio="1.35",
            neckline_context_filter_45="auto_non_bearish",
            neckline_context_filter_90="auto_non_bearish",
            volume_ratio="",
            volume_ma20="",
        )
        weak_arc = row.copy()
        weak_arc["second_arc_volume_ratio"] = "1.0"

        self.assertTrue(cond_neckline_volume_breakout_confirmation(row))
        self.assertFalse(cond_neckline_volume_breakout_confirmation(weak_arc))

    def test_neckline_breakout_score_keeps_candle_quality_penalty(self) -> None:
        row = make_row(
            close="105",
            open="104",
            high="112",
            low="100",
            previous_close="100",
            neckline_price="100",
            distance_to_neckline_pct="5.0",
            second_low_gap_pct="1.5",
            w_bottom_base_width_pct="18",
            second_arc_volume_ratio="1.35",
            neckline_context_filter_45="auto_non_bearish",
            neckline_context_filter_90="auto_non_bearish",
            volume_ratio="2.5",
            volume_ma20="2000",
        )

        _score, _components, risks = model_layer.score_neckline_volume_breakout_confirmation(row)

        self.assertTrue(any(str(risk).startswith("long_upper_shadow_quality_penalty") for risk in risks))

    def test_neckline_breakout_requires_45d_non_bearish_context(self) -> None:
        row = make_row(
            category="pattern",
            pattern_stage="neckline_breakout",
            close="105",
            open="101",
            high="106",
            low="100",
            previous_close="100",
            neckline_price="100",
            distance_to_neckline_pct="5.0",
            second_low_gap_pct="1.5",
            w_bottom_base_width_pct="18",
            second_arc_volume_ratio="1.35",
            neckline_context_filter_45="auto_bearish",
            neckline_context_filter_90="auto_non_bearish",
            volume_ratio="2.5",
            volume_ma20="2000",
        )

        self.assertFalse(cond_neckline_volume_breakout_confirmation(row))

    def test_neckline_90d_bearish_context_is_score_penalty_not_entry_gate(self) -> None:
        row = make_row(
            category="pattern",
            pattern_stage="neckline_breakout",
            close="105",
            open="101",
            high="106",
            low="100",
            previous_close="100",
            neckline_price="100",
            distance_to_neckline_pct="5.0",
            second_low_gap_pct="1.5",
            w_bottom_base_width_pct="18",
            second_arc_volume_ratio="1.35",
            neckline_context_filter_45="auto_non_bearish",
            neckline_context_filter_90="auto_bearish",
            neckline_context_return_90="-15",
            neckline_context_slope20_90="-3",
            neckline_context_drawdown_90="-26",
            volume_ratio="2.5",
            volume_ma20="2000",
        )

        self.assertTrue(cond_neckline_volume_breakout_confirmation(row))
        _score, _components, risks = model_layer.score_neckline_volume_breakout_confirmation(row)
        self.assertTrue(any(str(risk).startswith("neckline_90d_context_penalty") for risk in risks))

    def test_risk_penalty_does_not_cancel_model_entry(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            volume_ratio="2.2",
            tdcc_judgement="distribution_warning",
            return_20d="85",
        )
        score, _components, risks = model_layer.score_volume_breakout_v2_low_position(row)
        self.assertGreater(score, 0)
        self.assertTrue(any(str(risk).startswith("tdcc_distribution_penalty") for risk in risks))
        self.assertFalse(any(str(risk).startswith("false_breakout_risk_penalty") for risk in risks))

    def test_same_stock_can_enter_multiple_models(self) -> None:
        row = make_row(
            volume_breakout_type="bottom_volume_attack",
            volume_ratio="2.0",
            distance_23ema_pct="1.0",
            ema23_slope_pct="0.8",
        )
        self.assertTrue(model_layer.active_price_attack_for_early_models(row))
        self.assertTrue(cond_pullback(row))

    def test_tdcc_stealth_excludes_late_and_overheated_phases(self) -> None:
        base = make_row(
            volume_ratio="1.0",
            volume_breakout_type="",
            tdcc_price_phase="tdcc_leading_price",
            return_20d="5",
            close="100",
            high_20="105",
            low_20="95",
        )
        self.assertTrue(cond_tdcc_stealth(base))
        late = base.copy()
        late["tdcc_price_phase"] = "price_leading_tdcc"
        overheated = base.copy()
        overheated["tdcc_price_phase"] = "overheated_after_tdcc"
        self.assertFalse(cond_tdcc_stealth(late))
        self.assertFalse(cond_tdcc_stealth(overheated))

    def test_active_volume_attack_is_not_stealth_or_unreacted_story(self) -> None:
        row = make_row(
            volume_ratio="3.98",
            volume_breakout_type="",
            volume_confirmed_breakout="True",
            latest_revenue_yoy="93",
            cumulative_yoy_pct="16",
            return_5d="8.18",
            return_20d="17.22",
            close="58.2",
            open="55.4",
            previous_close="53",
            previous_20d_high="55",
            volume_ma20="2000",
            high_20="59.8",
            low_20="49",
            tdcc_price_phase="tdcc_leading_price",
        )
        self.assertTrue(model_layer.active_price_attack_for_early_models(row))
        self.assertFalse(cond_revenue_unreacted(row))
        self.assertFalse(cond_tdcc_stealth(row))

    def test_legacy_revenue_selector_is_immutable_but_unreachable_from_daily_signals(self) -> None:
        row = make_row(
            volume_ratio="1.0",
            volume_breakout_type="",
            volume_confirmed_breakout="False",
            latest_revenue_yoy="35",
            cumulative_yoy_pct="25",
            return_5d="0",
            return_20d="0",
            close="100",
            high_20="105",
            low_20="95",
        )
        self.assertTrue(cond_revenue_unreacted(row))

        revenue_spec = next(
            spec
            for spec in build_specs()
            if spec.model_id == "revenue_unreacted_range"
        )
        self.assertEqual(
            revenue_spec.condition_func.__name__,
            "cond_revenue_unreacted",
        )
        self.assertTrue(revenue_spec.condition_func(row))

        signals = build_signals(
            pd.DataFrame([row]),
            build_specs(),
            "20260831",
        )
        self.assertFalse(
            signals.get("model_id", pd.Series(dtype=str))
            .astype(str)
            .eq("revenue_unreacted_range")
            .any()
        )

    def test_generic_signal_validator_rejects_dedicated_revenue_rows(self) -> None:
        generic = pd.DataFrame(
            [
                {"model_id": "revenue_unreacted_range"},
                {"model_id": "price_pullback_23ema"},
            ]
        )
        errors = dedicated_operation_only_signal_errors(
            generic,
            artifact_name="raw.csv",
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("artifact=raw.csv", errors[0])
        self.assertIn("model_id=revenue_unreacted_range", errors[0])
        self.assertEqual(
            dedicated_operation_only_signal_errors(
                generic[
                    generic["model_id"].ne("revenue_unreacted_range")
                ],
                artifact_name="report.csv",
            ),
            [],
        )

    def test_derived_artifact_validator_rejects_legacy_revenue_rosters(self) -> None:
        frontpage = pd.DataFrame(
            [
                {
                    "primary_model_id": "revenue_unreacted_range",
                    "model_hit_ids": "price_pullback_23ema|revenue_unreacted_range",
                }
            ]
        )
        repeat = pd.DataFrame([{"model_id": "revenue_unreacted_range"}])
        summary = pd.DataFrame(
            [
                {
                    "model_id": "revenue_unreacted_range",
                    "new_stock_id": "6177",
                    "new_stock_name": "達麗",
                    "repeated_stock_id": "",
                    "repeated_stock_name": "",
                    "new_signal_stock_display": "6177 達麗",
                    "new_stock_display": "6177 達麗",
                    "repeated_signal_stock_display": "今日無候選",
                    "repeated_stock_display": "今日無候選",
                }
            ]
        )

        errors = dedicated_operation_only_derived_artifact_errors(
            frontpage,
            repeat,
            summary,
        )

        self.assertEqual(len(errors), 3)
        self.assertTrue(
            any("forbidden_in_frontpage_artifact" in error for error in errors)
        )
        self.assertTrue(
            any("forbidden_in_repeat_artifact" in error for error in errors)
        )
        self.assertTrue(
            any("summary_must_be_empty_roster_row" in error for error in errors)
        )

    def test_derived_artifact_validator_allows_empty_revenue_summary_row(self) -> None:
        frontpage = pd.DataFrame(
            [
                {
                    "primary_model_id": "price_pullback_23ema",
                    "model_hit_ids": "price_pullback_23ema",
                }
            ]
        )
        repeat = pd.DataFrame([{"model_id": "price_pullback_23ema"}])
        summary = pd.DataFrame(
            [
                {
                    "model_id": "revenue_unreacted_range",
                    "new_stock_id": "",
                    "new_stock_name": "",
                    "repeated_stock_id": "",
                    "repeated_stock_name": "",
                    "new_signal_stock_display": "今日無候選",
                    "new_stock_display": "今日無候選",
                    "repeated_signal_stock_display": "今日無候選",
                    "repeated_stock_display": "今日無候選",
                }
            ]
        )

        self.assertEqual(
            dedicated_operation_only_derived_artifact_errors(
                frontpage,
                repeat,
                summary,
            ),
            [],
        )

    def test_model_signal_log_replaces_current_date_snapshot(self) -> None:
        current = pd.DataFrame(
            [
                {
                    "signal_date": "20260531",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "放量攻擊模型",
                    "model_group": "pdf_core_model",
                    "model_score": "75.9",
                    "model_rank": "1",
                }
            ]
        )
        old_history = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": "price_pullback_23ema",
                },
                {
                    "signal_date": "20260531",
                    "report_bucket": "mainstream",
                    "stock_id": "3046",
                    "stock_name": "建碁",
                    "model_id": "tdcc_stealth_accumulation",
                },
            ]
        )
        original_dir = model_layer.MODEL_HISTORY_DIR
        original_csv = model_layer.MODEL_SIGNAL_LOG_CSV
        original_theme_history = model_layer.DAILY_THEME_STATUS_HISTORY_CSVS
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_csv = temp_dir / "daily_candidate_model_signal_log.csv"
            temp_theme_history = temp_dir / "daily_theme_status_history.csv"
            old_history.to_csv(temp_csv, index=False, encoding="utf-8-sig")
            pd.DataFrame(columns=["signal_date", "stock_id", "volume_breakout_type", "selection_status"]).to_csv(
                temp_theme_history,
                index=False,
            )
            model_layer.MODEL_HISTORY_DIR = temp_dir
            model_layer.MODEL_SIGNAL_LOG_CSV = temp_csv
            model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = [temp_theme_history]
            try:
                out = update_model_signal_log(current)
            finally:
                model_layer.MODEL_HISTORY_DIR = original_dir
                model_layer.MODEL_SIGNAL_LOG_CSV = original_csv
                model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = original_theme_history

        current_day = out[out["signal_date"].astype(str).eq("20260531")]
        self.assertEqual(set(current_day["model_id"]), {LOW_VOLUME_MODEL_ID})
        self.assertIn("price_pullback_23ema", set(out["model_id"]))

    def test_model_signal_log_preserves_effective_volume_v2_resolution_lineage(self) -> None:
        lineage = {
            "candidate_source_row_ids": "source-a:"
            + "a" * 64
            + "|source-b:"
            + "b" * 64,
            "candidate_source_row_sha256s": "a" * 64 + "|" + "b" * 64,
            "candidate_source_categories": "range_rebound|revenue_pullback",
            "candidate_formal_outcome_sha256": "c" * 64,
            "candidate_presentation_source_artifact": '{"contract":"volume_v2_formal_presentation_v1"}',
            "candidate_presentation_source_artifact_sha256": "d" * 64,
            "candidate_presentation_source_row_sha256": "e" * 64,
        }
        current = pd.DataFrame(
            [
                {
                    "signal_date": "20260731",
                    "report_bucket": "mainstream",
                    "stock_id": "2451",
                    "stock_name": "創見",
                    "model_id": MID_VOLUME_MODEL_ID,
                    "model_name_zh": "中位動能放量攻擊",
                    "model_group": "pdf_core_model",
                    "model_score": "76.4",
                    "model_rank": "1",
                    **lineage,
                }
            ]
        )
        original_dir = model_layer.MODEL_HISTORY_DIR
        original_csv = model_layer.MODEL_SIGNAL_LOG_CSV
        original_theme_history = model_layer.DAILY_THEME_STATUS_HISTORY_CSVS
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_csv = temp_dir / "daily_candidate_model_signal_log.csv"
            pd.DataFrame(
                columns=["signal_date", "report_bucket", "stock_id", "model_id"]
            ).to_csv(temp_csv, index=False)
            model_layer.MODEL_HISTORY_DIR = temp_dir
            model_layer.MODEL_SIGNAL_LOG_CSV = temp_csv
            model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = []
            try:
                out = update_model_signal_log(current)
            finally:
                model_layer.MODEL_HISTORY_DIR = original_dir
                model_layer.MODEL_SIGNAL_LOG_CSV = original_csv
                model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = original_theme_history

        row = out.iloc[0]
        for field, value in lineage.items():
            self.assertEqual(row[field], value)

    def test_model_signal_log_rejects_duplicate_effective_volume_v2_identity(self) -> None:
        duplicate = {
            "signal_date": "20260731",
            "report_bucket": "mainstream",
            "stock_id": "2451",
            "model_id": MID_VOLUME_MODEL_ID,
        }
        with self.assertRaisesRegex(
            RuntimeError, "duplicate formal identities"
        ):
            model_layer.snapshot_model_signals(
                pd.DataFrame([duplicate, dict(duplicate)])
            )

    def test_model_signal_log_backfills_selected_bottom_volume_attack_lineage(self) -> None:
        current = pd.DataFrame(
            [
                {
                    "signal_date": "20260618",
                    "report_bucket": "mainstream",
                    "stock_id": "1905",
                    "stock_name": "Test",
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "放量攻擊模型",
                    "model_group": "pdf_core_model",
                    "model_score": "70",
                    "model_rank": "1",
                }
            ]
        )
        original_dir = model_layer.MODEL_HISTORY_DIR
        original_csv = model_layer.MODEL_SIGNAL_LOG_CSV
        original_theme_history = model_layer.DAILY_THEME_STATUS_HISTORY_CSVS
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_dir = Path(tmpdir)
            temp_csv = temp_dir / "daily_candidate_model_signal_log.csv"
            temp_theme_history = temp_dir / "daily_theme_status_history.csv"
            pd.DataFrame(columns=["signal_date", "report_bucket", "stock_id", "model_id"]).to_csv(
                temp_csv,
                index=False,
            )
            pd.DataFrame(
                [
                    {
                        "signal_date": "20260611",
                        "stock_id": "2243",
                        "stock_name": "Test2243",
                        "theme_name": "Auto",
                        "volume_breakout_type": "bottom_volume_attack",
                        "volume_breakout_priority": "B_bottom_volume_attack_with_risk",
                        "selection_status": "selected",
                    }
                ]
            ).to_csv(temp_theme_history, index=False)
            model_layer.MODEL_HISTORY_DIR = temp_dir
            model_layer.MODEL_SIGNAL_LOG_CSV = temp_csv
            model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = [temp_theme_history]
            try:
                out = update_model_signal_log(current)
            finally:
                model_layer.MODEL_HISTORY_DIR = original_dir
                model_layer.MODEL_SIGNAL_LOG_CSV = original_csv
                model_layer.DAILY_THEME_STATUS_HISTORY_CSVS = original_theme_history

        backfilled = out[
            out["signal_date"].astype(str).eq("20260611")
            & out["stock_id"].astype(str).eq("2243")
            & out["model_id"].astype(str).eq("volume_range_breakout")
        ]
        self.assertEqual(len(backfilled), 0)
        self.assertNotIn("volume_range_breakout", set(out["model_id"].astype(str)))
        self.assertNotIn("true_breakout", set(out["model_id"].astype(str)))

    def test_mainstream_bucket_does_not_change_score(self) -> None:
        mainstream = make_row(
            structural_theme_bucket="ai_server_ipc_theme",
            theme_structural_status="core_mainstream_theme",
        )
        non_mainstream = make_row(
            structural_theme_bucket="traditional_textile_theme",
            theme_structural_status="non_mainstream_theme",
        )
        self.assertEqual(score_pullback(mainstream)[0], score_pullback(non_mainstream)[0])
        self.assertEqual(report_bucket(mainstream), "mainstream")
        self.assertEqual(report_bucket(non_mainstream), "non_mainstream")

    def test_model_recommendations_are_attached_to_signals(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "stock_id": "9999",
                    "model_score": 80,
                }
            ]
        )
        recs = pd.DataFrame(
            [
                {
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "recommended_usage": "promote_to_pdf_core",
                    "recommended_close_exit_horizon": "D+10",
                    "best_close_win_rate_pct": "76.71",
                    "best_avg_close_return_pct": "15.56",
                    "recommended_high_exit_horizon": "D+10",
                    "best_avg_high_return_pct": "21.3",
                    "best_high_5pct_hit_rate_pct": "70.0",
                    "recommended_sample_size": "161",
                    "recommended_unique_stocks": "107",
                    "recommended_sample_status": "ok_first_pass",
                    "model_revision_note": "Promote to specialty table.",
                }
            ]
        )
        out = attach_model_recommendations(signals, recs)
        self.assertEqual(out.loc[0, "recommended_usage"], "promote_to_pdf_core")
        self.assertEqual(out.loc[0, "recommended_close_exit_horizon"], "D+10")
        self.assertEqual(out.loc[0, "best_close_win_rate_pct"], "76.71")

    def test_model_signals_dedupe_same_stock_same_model_bucket(self) -> None:
        rows = [
            make_row(
                source_row_index="a",
                stock_id="9999",
                category="range_rebound",
                score="10",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
            make_row(
                source_row_index="b",
                stock_id="9999",
                category="pattern",
                score="99",
                report_line_memberships="mainstream",
                mainstream_report_eligible="True",
            ),
        ]
        out = build_signals(pd.DataFrame(rows), build_specs(), "20260530")
        dup_count = out.duplicated(["model_id", "report_bucket", "stock_id"]).sum()
        self.assertEqual(dup_count, 0)

    def test_audit_core_completeness_ignores_presentation_bucket(self) -> None:
        expected = pd.DataFrame(
            [{"report_bucket": "non_mainstream", "model_id": "price_pullback_23ema", "stock_id": "1503"}]
        )
        actual = pd.DataFrame(
            [{"report_bucket": "mainstream", "model_id": "price_pullback_23ema", "stock_id": "1503"}]
        )
        self.assertEqual(model_stock_key_set(expected), model_stock_key_set(actual))

    def test_report_ready_signals_merge_same_display_model_same_stock(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "CANON",
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "放量攻擊模型",
                    "model_score": "80",
                    "model_rank": "2",
                    "original_category": "range_rebound",
                    "source_row_index": "46",
                    "next_confirmation": "A",
                    "score_components": "volume",
                    "risk_penalty_tags": "",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "CANON",
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "放量攻擊模型",
                    "model_score": "90",
                    "model_rank": "1",
                    "original_category": "revenue_pullback",
                    "source_row_index": "175",
                    "next_confirmation": "B",
                    "score_components": "range",
                    "risk_penalty_tags": "risk_a",
                },
            ]
        )
        out = build_report_ready_model_signals(signals)
        self.assertEqual(len(out), 1)
        row = out.iloc[0]
        self.assertEqual(row["model_id"], LOW_VOLUME_MODEL_ID)
        self.assertEqual(row["model_rank"], 1)
        self.assertEqual(row["merged_same_model_source_count"], 2)
        self.assertIn(LOW_VOLUME_MODEL_ID, row["merged_model_ids"])
        self.assertIn("range_rebound", row["merged_source_categories"])
        self.assertIn("revenue_pullback", row["merged_source_categories"])

    def test_frontpage_unique_keeps_one_row_per_stock_but_preserves_model_hits(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": "range_rebound",
                    "model_name_zh": "區間內轉強",
                    "model_group": "pdf_core_model",
                    "model_score": "82",
                    "model_rank": "1",
                    "effective_primary_theme": "機器人",
                    "risk_penalty_tags": "repeated_but_no_breakout",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": "revenue_unreacted_range",
                    "model_name_zh": "營收爆發尚未反應",
                    "model_group": "pdf_core_model",
                    "model_score": "70",
                    "model_rank": "3",
                    "effective_primary_theme": "機器人",
                    "risk_penalty_tags": "needs_eps_confirmation",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "9999",
                    "stock_name": "測試股",
                    "model_id": "range_rebound",
                    "model_name_zh": "區間內轉強",
                    "model_group": "pdf_core_model",
                    "model_score": "75",
                    "model_rank": "2",
                    "effective_primary_theme": "測試族群",
                    "risk_penalty_tags": "",
                },
            ]
        )
        annotated = annotate_frontpage_uniqueness(signals)
        canons = annotated[annotated["stock_id"] == "2374"]
        self.assertEqual((canons["frontpage_display_allowed"] == "True").sum(), 1)
        self.assertEqual((canons["frontpage_duplicate_reason"] == "duplicate_stock_already_shown_on_frontpage").sum(), 1)

        frontpage = build_frontpage_unique(annotated)
        self.assertEqual((frontpage["stock_id"] == "2374").sum(), 1)
        row = frontpage[frontpage["stock_id"] == "2374"].iloc[0]
        self.assertEqual(row["model_hit_count"], 2)
        self.assertIn("區間內轉強", row["model_hits"])
        self.assertIn("營收爆發尚未反應", row["model_hits"])

    def test_same_model_repeat_is_separate_and_frontpage_prefers_new_signals(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2347",
                    "stock_name": "OLD",
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔",
                    "model_group": "pdf_core_model",
                    "model_score": "99",
                    "model_rank": "1",
                    "effective_primary_theme": "AI",
                    "risk_penalty_tags": "",
                },
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "9999",
                    "stock_name": "NEW",
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔",
                    "model_group": "pdf_core_model",
                    "model_score": "70",
                    "model_rank": "2",
                    "effective_primary_theme": "AI",
                    "risk_penalty_tags": "",
                },
            ]
        )
        model_log = pd.DataFrame(
            [
                {"signal_date": "20260529", "report_bucket": "mainstream", "stock_id": "2347", "model_id": "price_pullback_23ema"},
                {"signal_date": "20260530", "report_bucket": "mainstream", "stock_id": "2347", "model_id": "price_pullback_23ema"},
                {"signal_date": "20260530", "report_bucket": "mainstream", "stock_id": "9999", "model_id": "price_pullback_23ema"},
            ]
        )

        annotated, repeat = attach_same_model_repeat(signals, model_log)
        old = annotated[annotated["stock_id"] == "2347"].iloc[0]
        new = annotated[annotated["stock_id"] == "9999"].iloc[0]
        self.assertEqual(old["same_model_consecutive_days"], 2)
        self.assertEqual(old["same_model_repeat_status"], "repeated_same_model_signal")
        self.assertEqual(new["same_model_repeat_status"], "new_model_signal")
        self.assertEqual(len(repeat), 1)
        self.assertEqual(repeat.iloc[0]["stock_id"], "2347")

        annotated = annotate_frontpage_uniqueness(annotated)
        frontpage = build_frontpage_unique(annotated)
        self.assertEqual(frontpage.iloc[0]["stock_id"], "9999")
        self.assertNotIn("2347", set(frontpage["stock_id"].astype(str)))
        repeat_reason = annotated.loc[annotated["stock_id"].eq("2347"), "frontpage_duplicate_reason"].iloc[0]
        self.assertEqual(repeat_reason, "same_model_repeat_moved_to_persistence_table")

    def test_dual_report_membership_expands_without_score_change(self) -> None:
        row = make_row(
            stock_id="1303",
            report_line_memberships="mainstream,non_mainstream",
            mainstream_report_eligible="True",
            non_mainstream_report_eligible="True",
            dual_report_membership_flag="True",
        )
        out = build_signals(pd.DataFrame([row]), build_specs(), "20260530")
        model_rows = out[out["model_id"] == "price_pullback_23ema"]
        self.assertEqual(set(model_rows["report_bucket"]), {"mainstream", "non_mainstream"})
        self.assertEqual(model_rows["model_score"].nunique(), 1)

    def test_output_has_effective_theme_fields_and_clean_guidance(self) -> None:
        row = make_row(
            stock_id="9998",
            next_confirmation="依D+5/D+10統計與短線支撐管理",
            effective_primary_theme="機器人自動化",
            structural_theme_bucket="robotics_automation_theme",
            mainstream_report_eligible="True",
        )
        out = build_signals(pd.DataFrame([row]), build_specs(), "20260530")
        self.assertIn("effective_primary_theme", out.columns)
        self.assertIn("effective_structural_theme_bucket", out.columns)
        self.assertIn("model_operation_guidance", out.columns)
        self.assertFalse(out["next_confirmation"].astype(str).str.contains(r"\?\?\?", regex=True).any())

    def test_report_ready_pdf_facing_columns_are_human_readable(self) -> None:
        signals = pd.DataFrame(
            [
                {
                    "signal_date": "20260530",
                    "report_bucket": "mainstream",
                    "stock_id": "2374",
                    "stock_name": "佳能",
                    "model_id": LOW_VOLUME_MODEL_ID,
                    "model_name_zh": "低位放量攻擊模型",
                    "model_score": "80",
                    "model_rank": "2",
                    "original_category": "range_rebound",
                    "source_row_index": "46",
                    "next_confirmation": "call_strong_inflow / neckline",
                    "score_components": "volume_ratio=2.0|tdcc_status=strong_accumulation",
                    "risk_penalty_tags": "false_breakout_risk",
                    "tdcc_status": "strong_accumulation",
                    "warrant_flow_signal": "call_strong_inflow",
                }
            ]
        )
        report_ready = model_layer.attach_report_contract_columns(
            model_layer.build_report_ready_model_signals(signals)
        )
        self.assertEqual(model_layer.RISK_TAG_ZH["false_breakout_risk"], "漲幅過低")
        self.assertEqual(model_layer.RISK_TAG_ZH["false_breakout_risk_penalty"], "漲幅過低扣分")
        self.assertIn("漲幅過低", report_ready["risk_tags_zh"].iloc[0])
        self.assertNotIn("假突破風險", report_ready["risk_tags_zh"].iloc[0])
        for col in [
            "model_name_zh",
            "source_hit_labels_zh",
            "why_selected_zh",
            "why_selected_human_zh",
            "risk_tags_zh",
            "next_confirmation_zh",
            "recommended_usage_zh",
            "warrant_flow_signal_zh",
        ]:
            self.assertIn(col, report_ready.columns)
            text = " ".join(report_ready[col].astype(str))
            self.assertNotRegex(text, r"\?\?\?|[a-z]+(?:_[a-z0-9]+){1,}")
        self.assertIn("放量攻擊", report_ready["model_name_zh"].iloc[0])

    def test_warrant_formal_sync_preserves_membership_and_protected_models(self) -> None:
        candidates, raw, report, history = warrant_formal_sync_fixture()
        raw_identity = raw[
            list(model_layer.WARRANT_FORMAL_SYNC_IDENTITY_COLUMNS)
        ].copy()
        report_identity = report[
            list(model_layer.WARRANT_FORMAL_SYNC_IDENTITY_COLUMNS)
        ].copy()
        prior_history = history[history["signal_date"].eq("20260715")].copy()
        protected_before = raw[
            raw["model_id"].isin(model_layer.WARRANT_FORMAL_SYNC_PROTECTED_MODEL_IDS)
        ][["model_id", "stock_id", "model_score", "model_rank"]].copy()

        synced_raw, synced_report, synced_history = (
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
            )
        )

        pd.testing.assert_frame_equal(
            raw_identity,
            synced_raw[list(model_layer.WARRANT_FORMAL_SYNC_IDENTITY_COLUMNS)],
        )
        pd.testing.assert_frame_equal(
            report_identity,
            synced_report[list(model_layer.WARRANT_FORMAL_SYNC_IDENTITY_COLUMNS)],
        )
        pd.testing.assert_frame_equal(
            prior_history.reset_index(drop=True),
            synced_history[synced_history["signal_date"].eq("20260715")].reset_index(
                drop=True
            ),
        )
        protected_after = synced_raw[
            synced_raw["model_id"].isin(model_layer.WARRANT_FORMAL_SYNC_PROTECTED_MODEL_IDS)
        ][["model_id", "stock_id", "model_score", "model_rank"]]
        pd.testing.assert_frame_equal(
            protected_before.reset_index(drop=True),
            protected_after.reset_index(drop=True),
        )

        mutable = synced_raw[
            synced_raw["model_id"].eq("hot_theme_pullback")
        ].set_index("stock_id")
        self.assertEqual(mutable.loc["2330", "model_score"], "85.0")
        self.assertEqual(mutable.loc["2330", "model_rank"], "1")
        self.assertIn("warrant bullish +5", mutable.loc["2330", "score_components"])
        self.assertEqual(mutable.loc["2317", "model_score"], "76.0")
        self.assertEqual(mutable.loc["2317", "model_rank"], "2")
        self.assertNotIn("warrant bullish", mutable.loc["2317", "score_components"])
        mutable_report = synced_report[
            synced_report["model_id"].eq("hot_theme_pullback")
        ].set_index("stock_id")
        self.assertEqual(
            mutable_report.loc["2330", "merged_score_components"],
            "base=50 / hot theme +30 / warrant bullish +5",
        )
        self.assertEqual(
            mutable_report.loc["2317", "merged_score_components"],
            "base=50 / hot theme +26",
        )
        protected = synced_raw.set_index("stock_id")
        self.assertEqual(protected.loc["2454", "warrant_flow_signal"], "call_inflow")
        self.assertEqual(protected.loc["2454", "model_score"], "70")
        self.assertEqual(protected.loc["1301", "warrant_flow_signal"], "")

    def test_volume_v2_formal_outcome_hash_uses_stable_one_decimal_numeric_contract(self) -> None:
        taxonomy_only = {
            "stock_id": "6152",
            "model_id": LOW_VOLUME_MODEL_ID,
            "signal_date": "20260810",
            "candidate_source_row_ids": "",
            "warrant_flow_signal": "",
            "base_model_score": 60.0,
            "operation_score": 20.0,
            "tdcc_score": 12.0,
            "pattern_score": 8.0,
            "risk_penalty": 0.0,
            "final_rank_score": 100,
            "rank_reason_zh": "cap reached",
            "model_score": 100,
            "score_components": "base=60 | operation=20 | tdcc=12 | pattern=8",
            "risk_penalty_tags": "",
            "tdcc_status": "strong_accumulation",
            "next_confirmation": "confirm next close",
        }
        persisted_taxonomy_only = {
            **taxonomy_only,
            "base_model_score": "60.0",
            "operation_score": "20.0",
            "tdcc_score": "12.0",
            "pattern_score": "8.0",
            "risk_penalty": "0.0",
            "final_rank_score": "100.0",
            "model_score": "100.0",
        }
        expected_taxonomy_envelope = {
            "model_id": LOW_VOLUME_MODEL_ID,
            "candidate_signal_date": "",
            "authoritative_warrant_signal": "",
            "base_model_score": "60.0",
            "operation_score": "20.0",
            "tdcc_score": "12.0",
            "pattern_score": "8.0",
            "risk_penalty": "0.0",
            "final_rank_score": "100.0",
            "rank_reason_zh": "cap reached",
            "model_score": "100.0",
            "score_components": "base=60 | operation=20 | tdcc=12 | pattern=8",
            "risk_penalty_tags": "",
            "tdcc_status": "strong_accumulation",
            "next_confirmation": "confirm next close",
        }

        self.assertEqual(
            model_layer._volume_v2_formal_outcome_envelope(taxonomy_only),
            expected_taxonomy_envelope,
        )
        self.assertEqual(
            model_layer._volume_v2_formal_outcome_sha256(taxonomy_only),
            model_layer._volume_v2_formal_outcome_sha256(persisted_taxonomy_only),
        )

        candidate_backed = {
            **taxonomy_only,
            "candidate_source_row_ids": "source-row:6152",
            "final_rank_score": "83.5",
            "model_score": 83.5,
        }
        candidate_backed_persisted = {
            **candidate_backed,
            "final_rank_score": 83.5,
            "model_score": "83.5",
        }
        self.assertEqual(
            model_layer._volume_v2_formal_outcome_envelope(candidate_backed)[
                "candidate_signal_date"
            ],
            "20260810",
        )
        self.assertEqual(
            model_layer._volume_v2_formal_outcome_sha256(candidate_backed),
            model_layer._volume_v2_formal_outcome_sha256(
                candidate_backed_persisted
            ),
        )
        real_score_drift = {**candidate_backed_persisted, "model_score": "83.4"}
        self.assertNotEqual(
            model_layer._volume_v2_formal_outcome_sha256(candidate_backed),
            model_layer._volume_v2_formal_outcome_sha256(real_score_drift),
        )

    def test_volume_v2_formal_outcome_numeric_contract_rejects_invalid_values(self) -> None:
        valid = {
            "model_id": LOW_VOLUME_MODEL_ID,
            "candidate_source_row_ids": "",
            "final_rank_score": "100.0",
            "model_score": "100.0",
        }
        for invalid in ("83.51", "NaN", "Infinity", "1e2", "not-a-score"):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(
                    RuntimeError,
                    "formal outcome numeric field is not canonicalizable",
                ):
                    model_layer._volume_v2_formal_outcome_sha256(
                        {**valid, "final_rank_score": invalid}
                    )

    def test_warrant_formal_sync_refreshes_effective_volume_v2_outcome_hash(self) -> None:
        immutable_lineage = {
            "candidate_source_row_ids": "source-a:" + "a" * 64,
            "candidate_source_row_sha256s": "a" * 64,
            "candidate_source_categories": "range_rebound",
            "candidate_presentation_source_artifact": (
                '{"contract":"volume_v2_formal_presentation_v1"}'
            ),
            "candidate_presentation_source_artifact_sha256": "b" * 64,
            "candidate_presentation_source_row_sha256": "c" * 64,
        }
        raw_row = {
            "signal_date": "20260801",
            "report_line": "mainstream",
            "report_bucket": "mainstream",
            "source_row_index": "candidate:0",
            "stock_id": "2451",
            "model_id": LOW_VOLUME_MODEL_ID,
            "model_name_zh": "低位放量攻擊",
            "model_group": "pdf_core_model",
            "base_model_score": "60.0",
            "operation_score": "60.0",
            "tdcc_score": "0.0",
            "pattern_score": "0.0",
            "risk_penalty": "0.0",
            "final_rank_score": "60.0",
            "rank_reason_zh": "",
            "model_score": "60.0",
            "model_rank": "1",
            "score_components": "base=60",
            "risk_penalty_tags": "",
            "tdcc_status": "",
            "next_confirmation": "confirm next close",
            "warrant_flow_signal": "no_signal",
            **immutable_lineage,
        }
        raw_row["candidate_formal_outcome_sha256"] = (
            model_layer._volume_v2_formal_outcome_sha256(raw_row)
        )
        old_outcome_sha256 = raw_row["candidate_formal_outcome_sha256"]
        raw = pd.DataFrame([raw_row])
        report = raw.copy()
        report["merged_score_components"] = "base=60"
        current_history = raw.drop(columns=["report_line", "source_row_index"]).copy()
        prior_history = current_history.copy()
        prior_history["signal_date"] = "20260731"
        prior_history["candidate_formal_outcome_sha256"] = prior_history.apply(
            model_layer._volume_v2_formal_outcome_sha256,
            axis=1,
        )
        history = pd.concat([prior_history, current_history], ignore_index=True)
        expected_prior_history = prior_history.reset_index(drop=True).copy()
        candidates = pd.DataFrame(
            [
                {
                    "signal_date": "20260801",
                    "stock_id": "2451",
                    "warrant_flow_signal": "call_inflow",
                }
            ]
        )

        synced_raw, synced_report, synced_history = (
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
            )
        )
        drifted_report_before_rebuild = synced_report.copy()
        drifted_report_before_rebuild.at[0, "tdcc_status"] = "forged_tdcc_status"
        with self.assertRaisesRegex(
            RuntimeError,
            "immutable outcome drift.*artifact=report.*field=tdcc_status",
        ):
            model_layer._warrant_sync_refresh_volume_v2_formal_resolution_lineage(
                synced_raw.copy(),
                drifted_report_before_rebuild,
                synced_history.copy(),
                {"20260801"},
            )

        drifted_history_before_rebuild = synced_history.copy()
        current_history_index = drifted_history_before_rebuild.index[
            drifted_history_before_rebuild["signal_date"].eq("20260801")
        ][0]
        drifted_history_before_rebuild.at[
            current_history_index, "next_confirmation"
        ] = "forged_next_confirmation"
        with self.assertRaisesRegex(
            RuntimeError,
            "immutable outcome drift.*artifact=history.*field=next_confirmation",
        ):
            model_layer._warrant_sync_refresh_volume_v2_formal_resolution_lineage(
                synced_raw.copy(),
                synced_report.copy(),
                drifted_history_before_rebuild,
                {"20260801"},
            )

        rebuilt_report, _, _ = model_layer.rebuild_warrant_formal_consumers(
            synced_report,
            synced_history,
        )
        final_raw, final_history = model_layer.finalize_warrant_formal_consumer_parity(
            synced_raw,
            rebuilt_report,
            synced_history,
        )
        model_layer._warrant_sync_validate_final_volume_v2_formal_resolution_lineage(
            final_raw,
            rebuilt_report,
            final_history,
        )

        outcome_hashes: set[str] = set()
        current_rows = (
            final_raw.iloc[0],
            rebuilt_report.iloc[0],
            final_history[final_history["signal_date"].eq("20260801")].iloc[0],
        )
        for row in current_rows:
            actual_sha256 = row["candidate_formal_outcome_sha256"]
            self.assertNotEqual(actual_sha256, old_outcome_sha256)
            self.assertEqual(
                actual_sha256,
                model_layer._volume_v2_formal_outcome_sha256(row),
            )
            outcome_hashes.add(actual_sha256)
            for field, expected in immutable_lineage.items():
                self.assertEqual(row[field], expected)
        self.assertEqual(len(outcome_hashes), 1)
        self.assertEqual(final_raw.iloc[0]["warrant_flow_signal"], "call_inflow")
        self.assertNotEqual(final_raw.iloc[0]["model_score"], "60.0")
        pd.testing.assert_frame_equal(
            final_history[final_history["signal_date"].eq("20260731")]
            .reset_index(drop=True),
            expected_prior_history,
        )

        drifted_report = rebuilt_report.copy()
        drifted_report.at[0, "score_components"] = "consumer rebuild drift"
        with self.assertRaisesRegex(
            RuntimeError,
            "final report outcome envelope/hash drift",
        ):
            model_layer._warrant_sync_validate_final_volume_v2_formal_resolution_lineage(
                final_raw,
                drifted_report,
                final_history,
            )

    def test_warrant_formal_sync_fails_closed_on_missing_or_conflicting_source(self) -> None:
        candidates, raw, report, history = warrant_formal_sync_fixture()
        missing = candidates[candidates["stock_id"].ne("2454")].copy()
        with self.assertRaisesRegex(RuntimeError, "no canonical all_candidates"):
            model_layer.synchronize_warrant_formal_frames(
                missing,
                raw,
                report,
                history,
            )

        conflicting = pd.concat(
            [
                candidates,
                pd.DataFrame(
                    [
                        {
                            "signal_date": "20260717",
                            "stock_id": "2330",
                            "warrant_flow_signal": "put_inflow",
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )
        with self.assertRaisesRegex(RuntimeError, "inconsistent duplicate warrant"):
            model_layer.synchronize_warrant_formal_frames(
                conflicting,
                raw,
                report,
                history,
            )

    def test_warrant_formal_sync_fails_closed_on_identity_or_model_drift(self) -> None:
        candidates, raw, report, history = warrant_formal_sync_fixture()
        duplicated = pd.concat([report, report.iloc[[0]]], ignore_index=True)
        with self.assertRaisesRegex(RuntimeError, "duplicate warrant formal-sync exact identity"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                duplicated,
                history,
            )

        unknown = raw.copy()
        unknown.loc[0, "model_id"] = "unregistered_model"
        unknown_report = report.copy()
        unknown_report.loc[0, "model_id"] = "unregistered_model"
        unknown_history = history.copy()
        unknown_history.loc[
            unknown_history["signal_date"].eq("20260717")
            & unknown_history["stock_id"].eq("2330"),
            "model_id",
        ] = "unregistered_model"
        with self.assertRaisesRegex(RuntimeError, "unregistered formal model ids"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                unknown,
                unknown_report,
                unknown_history,
            )

    def test_warrant_formal_sync_volume_row_uses_candidate_scoped_official_lineage(self) -> None:
        candidates, raw, report, history = warrant_formal_sync_fixture()
        price_mask = raw["model_id"].eq("price_pullback_23ema")
        raw.loc[price_mask, "model_id"] = HIGH_VOLUME_MODEL_ID
        raw.loc[price_mask, "source_row_index"] = "volume_breakout:0"
        report.loc[price_mask, "model_id"] = HIGH_VOLUME_MODEL_ID
        report.loc[price_mask, "source_row_index"] = "volume_breakout:0"
        history.loc[
            history["signal_date"].eq("20260717")
            & history["model_id"].eq("price_pullback_23ema"),
            "model_id",
        ] = HIGH_VOLUME_MODEL_ID
        candidates = candidates[candidates["stock_id"].ne("2454")].copy()
        taxonomy = pd.DataFrame([{"stock_id": "2454"}])
        lineage_temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(lineage_temp_dir.cleanup)
        lineage_source = Path(lineage_temp_dir.name) / "2454.csv"
        lineage_source.write_text(
            "date,stock_id,close\n20260717,2454,100\n",
            encoding="utf-8",
        )
        volume_watch = pd.DataFrame(
            [
                {
                    "stock_id": "2454",
                    "selection_status": "selected",
                    "volume_breakout_type": "bottom_volume_attack",
                    "signal_date": "20260717",
                    "advisory_score_as_of": "20260717",
                    "advisory_score_source_artifact": str(lineage_source),
                    "advisory_score_source_sha256": (
                        model_layer.volume_v2_canonical_text_sha256(
                            lineage_source, "20260717"
                        )
                    ),
                }
            ]
        )
        empty_official = pd.DataFrame(
            columns=["date", "stock_id", "warrant_flow_signal"]
        )
        negative_official = pd.DataFrame(
            [
                {
                    "date": "20260717",
                    "stock_id": "9999",
                    "warrant_flow_signal": "no_signal",
                }
            ]
        )

        with self.assertRaisesRegex(RuntimeError, "official warrant projection columns missing"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=pd.DataFrame(),
                volume_taxonomy=taxonomy,
                volume_watch=volume_watch,
            )

        with self.assertRaisesRegex(RuntimeError, "has no rows"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=empty_official,
                volume_taxonomy=taxonomy,
                volume_watch=volume_watch,
            )

        stale_official = negative_official.copy()
        stale_official.loc[0, "date"] = "20260716"
        with self.assertRaisesRegex(RuntimeError, "date mismatch"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=stale_official,
                volume_taxonomy=taxonomy,
                volume_watch=volume_watch,
            )

        duplicate_official = pd.concat(
            [negative_official, negative_official], ignore_index=True
        )
        with self.assertRaisesRegex(RuntimeError, "duplicate sources"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=duplicate_official,
                volume_taxonomy=taxonomy,
                volume_watch=volume_watch,
            )

        synced_raw, _, _ = model_layer.synchronize_warrant_formal_frames(
            candidates,
            raw,
            report,
            history,
            official_warrant=negative_official,
            volume_taxonomy=taxonomy,
            volume_watch=volume_watch,
        )
        volume = synced_raw[synced_raw["model_id"].eq(HIGH_VOLUME_MODEL_ID)].iloc[0]
        self.assertEqual(volume["warrant_flow_signal"], "")
        self.assertEqual(volume["model_score"], "70")

        global_only_official = pd.DataFrame(
            [
                {
                    "date": "20260717",
                    "stock_id": "2454",
                    "warrant_flow_signal": "call_inflow",
                }
            ]
        )
        global_synced_raw, _, _ = model_layer.synchronize_warrant_formal_frames(
            candidates,
            raw,
            report,
            history,
            official_warrant=global_only_official,
            volume_taxonomy=taxonomy,
            volume_watch=volume_watch,
        )
        global_volume = global_synced_raw[
            global_synced_raw["model_id"].eq(HIGH_VOLUME_MODEL_ID)
        ].iloc[0]
        self.assertEqual(global_volume["warrant_flow_signal"], "")
        self.assertEqual(global_volume["model_score"], "70")

        wrong_watch = volume_watch.copy()
        wrong_watch.loc[0, "selection_status"] = "watch_only"
        with self.assertRaisesRegex(RuntimeError, "no exact model-owned watch lineage"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=negative_official,
                volume_taxonomy=taxonomy,
                volume_watch=wrong_watch,
            )

        stale_watch = volume_watch.copy()
        stale_watch.loc[0, "advisory_score_as_of"] = "20260716"
        with self.assertRaisesRegex(RuntimeError, "advisory lineage date mismatch"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=negative_official,
                volume_taxonomy=taxonomy,
                volume_watch=stale_watch,
            )

        missing_source_watch = volume_watch.copy()
        missing_source_watch.loc[0, "advisory_score_source_artifact"] = ""
        with self.assertRaisesRegex(RuntimeError, "source artifact is blank"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=negative_official,
                volume_taxonomy=taxonomy,
                volume_watch=missing_source_watch,
            )

        wrong_sha_watch = volume_watch.copy()
        wrong_sha_watch.loc[0, "advisory_score_source_sha256"] = "0" * 64
        with self.assertRaisesRegex(RuntimeError, "SHA-256 mismatch"):
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
                official_warrant=negative_official,
                volume_taxonomy=taxonomy,
                volume_watch=wrong_sha_watch,
            )

    def test_warrant_formal_sync_rejects_mismatched_translated_bonus_marker(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "translated score marker"):
            model_layer._warrant_sync_update_score_components_zh(
                "基礎分60 | 權證偏多 +999",
                before_signal="no_signal",
                after_signal="call_inflow",
                bonus=Decimal("2"),
            )

        with self.assertRaisesRegex(RuntimeError, "translated score marker"):
            model_layer._warrant_sync_update_score_components_zh(
                "基礎分60 | 權證偏多 +2 | 權證偏多 +2",
                before_signal="call_inflow",
                after_signal="call_inflow",
                bonus=Decimal("2"),
            )

    def test_warrant_formal_sync_final_parity_is_allowlisted_and_current_only(self) -> None:
        candidates, raw, report, history = warrant_formal_sync_fixture()
        raw["score_components_zh"] = raw["score_components"].map(
            model_layer.score_components_zh
        )
        report["score_components_zh"] = raw["score_components_zh"]
        history["score_components_zh"] = "history"
        protected_original = raw.loc[
            raw["model_id"].eq("price_pullback_23ema"),
            "score_components_zh",
        ].iloc[0]
        synced_raw, synced_report, synced_history = (
            model_layer.synchronize_warrant_formal_frames(
                candidates,
                raw,
                report,
                history,
            )
        )
        synced_report.loc[
            synced_report["model_id"].eq("hot_theme_pullback"),
            "score_components_zh",
        ] = "fresh allowed display"
        synced_report.loc[
            synced_report["model_id"].eq("price_pullback_23ema"),
            "score_components_zh",
        ] = "must not enter protected score fields"

        final_raw, final_history = model_layer.finalize_warrant_formal_consumer_parity(
            synced_raw,
            synced_report,
            synced_history,
        )

        mutable_raw = final_raw[
            final_raw["model_id"].eq("hot_theme_pullback")
        ]
        self.assertEqual(set(mutable_raw["score_components_zh"]), {"fresh allowed display"})
        protected_raw = final_raw[
            final_raw["model_id"].eq("price_pullback_23ema")
        ].iloc[0]
        self.assertEqual(protected_raw["score_components_zh"], protected_original)
        prior = final_history[final_history["signal_date"].eq("20260715")].iloc[0]
        self.assertEqual(prior["score_components_zh"], "history")
        current_mutable = final_history[
            final_history["signal_date"].eq("20260717")
            & final_history["model_id"].eq("hot_theme_pullback")
        ]
        self.assertEqual(
            set(current_mutable["score_components_zh"]),
            {"fresh allowed display"},
        )

    def test_warrant_formal_sync_cli_never_dispatches_full_selection(self) -> None:
        original_sync = model_layer.run_warrant_formal_sync_only
        original_main = model_layer.main
        calls: list[str] = []
        try:
            model_layer.run_warrant_formal_sync_only = lambda: calls.append("warrant") or 0
            model_layer.main = lambda: calls.append("full") or 0
            self.assertEqual(
                model_layer.cli_main(["--warrant-formal-sync-only"]),
                0,
            )
        finally:
            model_layer.run_warrant_formal_sync_only = original_sync
            model_layer.main = original_main
        self.assertEqual(calls, ["warrant"])


    def test_rotation_theme_resolver_maps_known_raw_market_terms(self) -> None:
        for raw in ["ASIC", "DRAM IC", "DRAM/Flash", "MLCC", "MOSFET", "PCB", "optoelectronics"]:
            resolved = model_layer.resolve_rotation_theme(raw)
            self.assertEqual(resolved["theme_resolution_status"], "resolved")
            self.assertTrue(model_layer.has_cjk_text(resolved["theme_display_zh"]))

        unresolved = model_layer.resolve_rotation_theme("其他")
        self.assertEqual(unresolved["theme_resolution_status"], "unresolved")


    def test_group_rotation_outputs_pdf_safe_theme_display(self) -> None:
        taxonomy = pd.DataFrame(
            [
                {
                    "stock_id": "9103",
                    "stock_name": "美德醫療-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
                {
                    "stock_id": "9105",
                    "stock_name": "泰金寶-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
                {
                    "stock_id": "9136",
                    "stock_name": "巨騰-DR",
                    "industry": "91",
                    "basic_theme": "91",
                    "primary_theme": "DR_or_foreign_listing",
                    "secondary_themes": "",
                },
            ]
        )
        dates = pd.date_range("2026-04-01", periods=40, freq="B").strftime("%Y%m%d")
        history = pd.DataFrame(
            {
                "date": dates,
                "close": [100 + i for i in range(40)],
                "volume": [100] * 39 + [400],
                "volume_ma20": [100] * 40,
            }
        )

        original_path = model_layer.STOCK_THEME_TAXONOMY
        original_price_history = model_layer.price_history_for_stock
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_csv = Path(tmpdir) / "taxonomy.csv"
            taxonomy.to_csv(temp_csv, index=False, encoding="utf-8-sig")
            try:
                model_layer.STOCK_THEME_TAXONOMY = temp_csv
                model_layer.price_history_for_stock = lambda stock_id: history.copy()
                rotation = model_layer.build_rotation(pd.DataFrame(), dates[-1])
            finally:
                model_layer.STOCK_THEME_TAXONOMY = original_path
                model_layer.price_history_for_stock = original_price_history

        self.assertFalse(rotation.empty)
        self.assertIn("theme_display_zh", rotation.columns)
        self.assertIn("theme_resolution_status", rotation.columns)
        self.assertIn("theme_key", rotation.columns)
        self.assertEqual(set(rotation["theme"]), {"DR / 外國上市"})
        self.assertEqual(set(rotation["theme_display_zh"]), {"DR / 外國上市"})
        self.assertEqual(set(rotation["theme_resolution_status"]), {"resolved"})
        self.assertTrue(rotation["theme_key"].str.contains("DR_or_foreign_listing").any())
        self.assertFalse(rotation["theme"].str.contains(r"^\\d+$|DR_or_foreign_listing|其他", regex=True).any())


def test_report_signal_snapshot_score_schema_is_stable_without_volume_v2_rows() -> None:
    signals = pd.DataFrame(
        [
            {
                "signal_date": "20260805",
                "report_bucket": "mainstream",
                "model_id": "price_pullback_23ema",
                "model_name_zh": "23EMA回檔",
                "stock_id": "2330",
                "stock_name": "台積電",
                "model_score": "70",
                "model_rank": "1",
                "original_category": "pullback_rebound",
                "source_row_index": "0",
                "next_confirmation": "",
                "score_components": "",
                "risk_penalty_tags": "",
            }
        ]
    )

    raw, report = model_layer.finalize_daily_candidate_snapshot_schemas(
        signals,
        model_layer.build_report_ready_model_signals(signals),
    )
    assert set(model_layer.REPORT_SIGNAL_SNAPSHOT_SCORE_COLUMNS) <= set(raw.columns)
    assert set(model_layer.REPORT_SIGNAL_SNAPSHOT_SCORE_COLUMNS) <= set(report.columns)
    assert report.loc[0, list(model_layer.REPORT_SIGNAL_SNAPSHOT_SCORE_COLUMNS)].eq("").all()

    empty_raw, empty_report = model_layer.finalize_daily_candidate_snapshot_schemas(
        pd.DataFrame(),
        model_layer.build_report_ready_model_signals(pd.DataFrame()),
    )
    assert set(model_layer.REPORT_SIGNAL_SNAPSHOT_SCORE_COLUMNS) <= set(
        empty_raw.columns
    )
    assert set(model_layer.REPORT_SIGNAL_SNAPSHOT_SCORE_COLUMNS) <= set(
        empty_report.columns
    )

    main_source = inspect.getsource(model_layer.main)
    assert main_source.index("finalize_daily_candidate_snapshot_schemas") < (
        main_source.index("update_model_signal_log")
    )


if __name__ == "__main__":
    unittest.main()
