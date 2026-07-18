from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_volume_breakout_watch import (  # noqa: E402
    FORBIDDEN_WATCH_MIRROR_COLUMNS,
    VOLUME_BREAKOUT_RULE_VERSION,
    WATCH_COLUMNS,
    _process_latest_path,
    _process_price_history_path,
    add_price_metrics,
    canonical_text_sha256,
    classify_watch,
    detect_volume_breakout,
    ensure_watch_schema,
    event_log_has_formal_bottom_history,
    filter_latest_to_effective_signal_date,
)
from build_volume_attack_theme_layer import (  # noqa: E402
    enrich_stocks,
    sha256_file as theme_canonical_text_sha256,
)
from validate_volume_attack_theme_layer import (  # noqa: E402
    sha256_file as theme_validator_canonical_text_sha256,
)
from validate_volume_breakout_watch import (  # noqa: E402
    advisory_as_of_matches_signal_date,
    advisory_source_lineage_errors,
    canonical_text_sha256 as validator_canonical_text_sha256,
    forbidden_watch_columns,
)


class VolumeBreakoutWatchTest(unittest.TestCase):
    @staticmethod
    def _theme_enrichment_inputs() -> tuple[pd.DataFrame, ...]:
        watch = pd.DataFrame(
            [
                {
                    "signal_date": "20260718",
                    "stock_id": "6505",
                    "stock_name": "台塑化",
                    "volume_breakout_type": "bottom_volume_attack",
                    "selection_status": "selected",
                    "volume_breakout_priority": "A_bottom_volume_attack",
                    "advisory_volume_breakout_score": "71",
                    "advisory_volume_breakout_rank": "1",
                    "advisory_score_as_of": "20260718",
                    "advisory_score_source_artifact": "data/stock_price_history/6505.csv",
                    "advisory_score_source_sha256": "a" * 64,
                    "future_unregistered_context": "must_not_leak",
                }
            ]
        )
        empty = pd.DataFrame()
        candidates = pd.DataFrame(
            [
                {
                    "stock_id": "6505",
                    "signal_date": "20260718",
                    "warrant_flow_signal": "call_strong_inflow",
                    "score": "999",
                    "rank": "1",
                    "warrant_flow_score": "999",
                }
            ]
        )
        official = pd.DataFrame(
            [
                {
                    "stock_id": "6505",
                    "date": "20260718",
                    "warrant_flow_signal": "call_strong_inflow",
                }
            ]
        )
        return watch, empty, empty, candidates, empty, official

    def test_theme_layer_uses_allowlisted_canonical_candidate_warrant(self) -> None:
        out = enrich_stocks(
            *self._theme_enrichment_inputs(),
            warrant_as_of="20260718",
            candidate_source_sha256="c" * 64,
            official_warrant_source_sha256="f" * 64,
        )

        self.assertEqual(out.iloc[0]["warrant_flow_signal"], "call_strong_inflow")
        self.assertEqual(out.iloc[0]["volume_breakout_score"], "71")
        self.assertEqual(out.iloc[0]["volume_breakout_rank"], "1")
        self.assertEqual(out.iloc[0]["volume_watch_as_of"], "20260718")
        self.assertNotIn("advisory_volume_breakout_score", out.columns)
        self.assertNotIn("advisory_volume_breakout_rank", out.columns)
        self.assertNotIn("future_unregistered_context", out.columns)
        self.assertNotIn("score", out.columns)
        self.assertNotIn("rank", out.columns)
        self.assertNotIn("warrant_flow_score", out.columns)
        self.assertEqual(
            out.iloc[0]["advisory_score_source_artifact"],
            "data/stock_price_history/6505.csv",
        )
        self.assertEqual(out.iloc[0]["advisory_score_source_sha256"], "a" * 64)
        self.assertEqual(out.iloc[0]["has_bullish_warrant_signal"], "True")
        self.assertEqual(out.iloc[0]["warrant_flow_as_of"], "20260718")
        self.assertEqual(
            out.iloc[0]["warrant_flow_source_artifact"],
            "output/latest/all_candidates_latest.csv",
        )
        self.assertEqual(out.iloc[0]["warrant_flow_source_sha256"], "c" * 64)
        self.assertEqual(
            out.iloc[0]["warrant_flow_official_source_artifact"],
            "output/latest/warrant_flow_latest.csv",
        )
        self.assertEqual(out.iloc[0]["warrant_flow_official_source_sha256"], "f" * 64)

    def test_theme_layer_fails_when_official_warrant_row_lacks_candidate_projection(self) -> None:
        watch, theme, two_line, _candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )

        with self.assertRaisesRegex(RuntimeError, "no canonical all_candidates row"):
            enrich_stocks(
                watch,
                theme,
                two_line,
                pd.DataFrame(),
                taxonomy,
                official,
            )

    def test_theme_layer_fails_on_candidate_official_warrant_mismatch(self) -> None:
        watch, theme, two_line, candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        candidates.loc[0, "warrant_flow_signal"] = "no_signal"

        with self.assertRaisesRegex(RuntimeError, "canonical warrant projection mismatch"):
            enrich_stocks(watch, theme, two_line, candidates, taxonomy, official)

    def test_theme_layer_allows_duplicate_candidate_themes_when_warrant_matches(self) -> None:
        watch, theme, two_line, candidates, _taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        candidates["theme_group"] = "candidate_theme_a"
        second = candidates.iloc[0].copy()
        second["theme_group"] = "candidate_theme_b"
        candidates = pd.concat([candidates, second.to_frame().T], ignore_index=True)
        taxonomy = pd.DataFrame(
            [{"stock_id": "6505", "theme_group": "taxonomy_theme"}]
        )

        out = enrich_stocks(
            watch,
            theme,
            two_line,
            candidates,
            taxonomy,
            official,
            candidate_source_sha256="c" * 64,
            official_warrant_source_sha256="f" * 64,
        )

        self.assertEqual(out.iloc[0]["warrant_flow_signal"], "call_strong_inflow")
        self.assertEqual(out.iloc[0]["theme_name"], "taxonomy_theme")

    def test_theme_layer_fails_on_duplicate_candidate_warrant_conflict(self) -> None:
        watch, theme, two_line, candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        candidates["theme_group"] = "candidate_theme_a"
        second = candidates.iloc[0].copy()
        second["theme_group"] = "candidate_theme_b"
        second["warrant_flow_signal"] = "no_signal"
        candidates = pd.concat([candidates, second.to_frame().T], ignore_index=True)

        with self.assertRaisesRegex(
            RuntimeError,
            "conflicting_fields=warrant_flow_signal",
        ):
            enrich_stocks(
                watch,
                theme,
                two_line,
                candidates,
                taxonomy,
                official,
            )

    def test_theme_layer_fails_when_positive_candidate_lacks_official_row(self) -> None:
        watch, theme, two_line, candidates, taxonomy, _official = (
            self._theme_enrichment_inputs()
        )

        with self.assertRaisesRegex(
            RuntimeError,
            "positive all_candidates warrant projection lacks official canonical row",
        ):
            enrich_stocks(
                watch,
                theme,
                two_line,
                candidates,
                taxonomy,
                pd.DataFrame(columns=["date", "stock_id", "warrant_flow_signal"]),
                warrant_as_of="20260718",
                candidate_source_sha256="c" * 64,
                official_warrant_source_sha256="f" * 64,
            )

    def test_theme_layer_fails_on_watch_advisory_as_of_mismatch(self) -> None:
        watch, theme, two_line, candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        watch.loc[0, "advisory_score_as_of"] = "20260717"

        with self.assertRaisesRegex(RuntimeError, "advisory_score_as_of mismatch"):
            enrich_stocks(
                watch,
                theme,
                two_line,
                candidates,
                taxonomy,
                official,
            )

    def test_theme_layer_rejects_legacy_watch_score_rank_fields(self) -> None:
        watch, theme, two_line, candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        watch["volume_breakout_score"] = "99"

        with self.assertRaisesRegex(RuntimeError, "forbidden legacy score/rank"):
            enrich_stocks(
                watch,
                theme,
                two_line,
                candidates,
                taxonomy,
                official,
            )

    def test_theme_layer_rejects_unregistered_watch_warrant_field(self) -> None:
        watch, theme, two_line, candidates, taxonomy, official = (
            self._theme_enrichment_inputs()
        )
        watch["warrant_flow_signal"] = "watch_poison"

        with self.assertRaisesRegex(RuntimeError, "unregistered sensitive fields"):
            enrich_stocks(
                watch,
                theme,
                two_line,
                candidates,
                taxonomy,
                official,
            )

    def test_empty_watch_schema_keeps_required_columns(self) -> None:
        out = ensure_watch_schema(pd.DataFrame())

        self.assertEqual(out.columns.tolist(), WATCH_COLUMNS)
        self.assertTrue(out.empty)
        self.assertFalse(any(column.startswith("warrant_") for column in WATCH_COLUMNS))
        self.assertNotIn("call_warrant_count", WATCH_COLUMNS)
        self.assertNotIn("put_warrant_count", WATCH_COLUMNS)
        self.assertNotIn("score", WATCH_COLUMNS)
        self.assertNotIn("rank", WATCH_COLUMNS)
        self.assertIn("advisory_volume_breakout_score", WATCH_COLUMNS)
        self.assertIn("advisory_volume_breakout_rank", WATCH_COLUMNS)
        self.assertIn("advisory_score_as_of", WATCH_COLUMNS)
        self.assertIn("advisory_score_source_artifact", WATCH_COLUMNS)
        self.assertIn("advisory_score_source_sha256", WATCH_COLUMNS)
        self.assertNotIn("volume_breakout_score", WATCH_COLUMNS)
        self.assertNotIn("volume_breakout_rank", WATCH_COLUMNS)
        self.assertEqual(
            FORBIDDEN_WATCH_MIRROR_COLUMNS,
            frozenset(
                {
                    "call_warrant_count",
                    "put_warrant_count",
                    "score",
                    "rank",
                    "volume_breakout_score",
                    "volume_breakout_rank",
                }
            ),
        )

    def test_partial_watch_schema_adds_missing_columns_and_preserves_extra(self) -> None:
        out = ensure_watch_schema(
            pd.DataFrame(
                [
                    {
                        "signal_date": "20260718",
                        "stock_id": "2317",
                        "custom_note": "keep",
                        "advisory_volume_breakout_score": "72",
                        "advisory_volume_breakout_rank": "3",
                        "warrant_flow_signal": "watch_poison",
                        "call_warrant_count": "2",
                        "score": "99",
                        "rank": "1",
                        "volume_breakout_score": "98",
                        "volume_breakout_rank": "2",
                    }
                ]
            )
        )

        self.assertEqual(out.iloc[0]["stock_id"], "2317")
        self.assertEqual(out.iloc[0]["custom_note"], "keep")
        self.assertEqual(out.iloc[0]["advisory_volume_breakout_score"], "72")
        self.assertEqual(out.iloc[0]["advisory_volume_breakout_rank"], "3")
        self.assertEqual(out.iloc[0]["advisory_score_as_of"], "20260718")
        self.assertFalse(
            {
                "warrant_flow_signal",
                "call_warrant_count",
                "score",
                "rank",
                "volume_breakout_score",
                "volume_breakout_rank",
            }
            .intersection(out.columns)
        )
        for col in WATCH_COLUMNS:
            self.assertIn(col, out.columns)

    def test_classify_watch_assigns_advisory_rank_and_as_of(self) -> None:
        source = pd.DataFrame(
            [
                {
                    "signal_date": "20260718",
                    "stock_id": "1111",
                    "advisory_volume_breakout_score": "50",
                    "volume_ratio": "2.0",
                },
                {
                    "signal_date": "20260718",
                    "stock_id": "2222",
                    "advisory_volume_breakout_score": "70",
                    "volume_ratio": "2.0",
                },
            ]
        )

        out = classify_watch(source)

        self.assertEqual(out["stock_id"].tolist(), ["2222", "1111"])
        self.assertEqual(out["advisory_volume_breakout_rank"].tolist(), [1, 2])
        self.assertEqual(out["advisory_score_as_of"].tolist(), ["20260718", "20260718"])
        self.assertNotIn("volume_breakout_score", out.columns)
        self.assertNotIn("volume_breakout_rank", out.columns)

    def test_advisory_rank_is_stable_when_equal_rows_are_reversed(self) -> None:
        rows = [
            {
                "signal_date": "20260718",
                "stock_id": "2222",
                "advisory_volume_breakout_score": "70",
                "volume_ratio": "2.0",
            },
            {
                "signal_date": "20260718",
                "stock_id": "1111",
                "advisory_volume_breakout_score": "70",
                "volume_ratio": "2.0",
            },
        ]

        forward = classify_watch(pd.DataFrame(rows))
        reversed_input = classify_watch(pd.DataFrame(list(reversed(rows))))

        self.assertEqual(forward["stock_id"].tolist(), ["1111", "2222"])
        self.assertEqual(
            forward[["stock_id", "advisory_volume_breakout_rank"]].to_dict("records"),
            reversed_input[["stock_id", "advisory_volume_breakout_rank"]].to_dict(
                "records"
            ),
        )

    def test_validator_forbids_warrant_score_and_rank_mirrors(self) -> None:
        self.assertEqual(
            forbidden_watch_columns(
                [
                    "stock_id",
                    "volume_breakout_score",
                    "volume_breakout_rank",
                    "warrant_flow_signal",
                    "call_warrant_count",
                    "score",
                    "rank",
                    "advisory_volume_breakout_score",
                    "advisory_volume_breakout_rank",
                ]
            ),
            [
                "call_warrant_count",
                "rank",
                "score",
                "volume_breakout_rank",
                "volume_breakout_score",
                "warrant_flow_signal",
            ],
        )

    def test_advisory_score_as_of_must_equal_signal_date(self) -> None:
        valid = pd.DataFrame(
            [{"signal_date": "20260718", "advisory_score_as_of": "20260718"}]
        )
        stale = valid.copy()
        stale.loc[0, "advisory_score_as_of"] = "20260717"
        blank = valid.copy()
        blank.loc[0, "advisory_score_as_of"] = ""

        self.assertTrue(advisory_as_of_matches_signal_date(valid))
        self.assertFalse(advisory_as_of_matches_signal_date(stale))
        self.assertFalse(advisory_as_of_matches_signal_date(blank))

    def test_advisory_score_source_lineage_is_hash_pinned(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "data/stock_price_history/6505.csv"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text("date,stock_id,close\n20260718,6505,42\n", encoding="utf-8")
            source_sha = canonical_text_sha256(source)
            watch = pd.DataFrame(
                [
                    {
                        "stock_id": "6505",
                        "advisory_score_source_artifact": (
                            "data/stock_price_history/6505.csv"
                        ),
                        "advisory_score_source_sha256": source_sha,
                    }
                ]
            )

            self.assertEqual(advisory_source_lineage_errors(watch, root), [])
            watch.loc[0, "advisory_score_source_sha256"] = "0" * 64
            self.assertTrue(advisory_source_lineage_errors(watch, root))

    def test_canonical_text_sha_is_equal_for_lf_and_crlf(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            lf_path = Path(temp_dir) / "lf.csv"
            crlf_path = Path(temp_dir) / "crlf.csv"
            lf_path.write_bytes(b"date,stock_id\n20260718,6505\n")
            crlf_path.write_bytes(b"date,stock_id\r\n20260718,6505\r\n")

            expected = canonical_text_sha256(lf_path)

            self.assertEqual(expected, canonical_text_sha256(crlf_path))
            self.assertEqual(expected, validator_canonical_text_sha256(lf_path))
            self.assertEqual(expected, validator_canonical_text_sha256(crlf_path))
            self.assertEqual(expected, theme_canonical_text_sha256(lf_path))
            self.assertEqual(expected, theme_canonical_text_sha256(crlf_path))
            self.assertEqual(expected, theme_validator_canonical_text_sha256(lf_path))
            self.assertEqual(expected, theme_validator_canonical_text_sha256(crlf_path))

    def test_full_and_fast_watch_paths_have_identical_advisory_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            dates = pd.date_range("2026-04-01", periods=81, freq="D").strftime(
                "%Y%m%d"
            )
            rows = [
                {
                    "date": date,
                    "stock_id": "6505",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 98.0,
                    "high": 100.0,
                    "low": 95.0,
                    "close": 98.0,
                    "volume": 2_000_000,
                }
                for date in dates
            ]
            rows[-1].update(
                {
                    "open": 100.0,
                    "high": 104.0,
                    "low": 99.0,
                    "close": 103.0,
                    "volume": 5_000_000,
                }
            )
            pd.DataFrame(rows).to_csv(source, index=False)

            full_rows, _events = _process_price_history_path(source, dates[-1])
            fast_rows = _process_latest_path(source, dates[-1])

        self.assertEqual(len(full_rows), 1)
        self.assertEqual(len(fast_rows), 1)
        for field in (
            "signal_date",
            "stock_id",
            "advisory_volume_breakout_score",
            "advisory_score_source_artifact",
            "advisory_score_source_sha256",
        ):
            self.assertEqual(full_rows[0][field], fast_rows[0][field], field)

    def test_filter_does_not_fall_back_to_stale_signal_before_report_date(self) -> None:
        latest = pd.DataFrame(
            [
                {"signal_date": "20260529", "stock_id": "2317"},
                {"signal_date": "20260528", "stock_id": "2330"},
            ]
        )

        out, effective_date = filter_latest_to_effective_signal_date(latest, "20260530")

        self.assertEqual(effective_date, "20260530")
        self.assertTrue(out.empty)

    def test_filter_uses_exact_main_date_when_available(self) -> None:
        latest = pd.DataFrame(
            [
                {"signal_date": "20260529", "stock_id": "2317"},
                {"signal_date": "20260530", "stock_id": "2330"},
            ]
        )

        out, effective_date = filter_latest_to_effective_signal_date(latest, "20260530")

        self.assertEqual(effective_date, "20260530")
        self.assertEqual(out["stock_id"].tolist(), ["2330"])

    def test_old_broad_event_log_forces_formal_bottom_rebuild(self) -> None:
        old_events = pd.DataFrame(
            [
                {"volume_breakout_type": "loose_platform_volume_watch"},
                {"volume_breakout_type": "strict_60d_volume_breakout"},
            ]
        )
        formal_events = pd.DataFrame(
            [
                {
                    "volume_breakout_type": "bottom_volume_attack",
                    "volume_breakout_rule_version": VOLUME_BREAKOUT_RULE_VERSION,
                },
            ]
        )
        stale_formal_events = pd.DataFrame(
            [
                {"volume_breakout_type": "bottom_volume_attack"},
            ]
        )

        self.assertFalse(event_log_has_formal_bottom_history(old_events))
        self.assertFalse(event_log_has_formal_bottom_history(stale_formal_events))
        self.assertTrue(event_log_has_formal_bottom_history(formal_events))

    def test_locked_limit_up_low_volume_ratio_is_bottom_volume_attack(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202605{idx + 1:02d}",
                    "stock_id": "4916",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 72.0,
                    "high": 74.4,
                    "low": 70.0,
                    "close": 74.4,
                    "volume": 7_300_000,
                }
            )
        rows.append(
            {
                "date": "20260526",
                "stock_id": "4916",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 81.8,
                "high": 81.8,
                "low": 81.8,
                "close": 81.8,
                "volume": 3_578_609,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))
        signal = detect_volume_breakout(df.iloc[-1])

        self.assertIsNotNone(signal)
        assert signal is not None
        self.assertEqual(signal.event_type, "bottom_volume_attack")
        self.assertIn("locked_limit_up_breakout", signal.notes)
        self.assertIn("locked_limit_no_volume_gate", signal.notes)
        self.assertLess(float(df.iloc[-1]["volume_ratio"]), 2.0)

    def test_locked_limit_up_does_not_require_average_volume_gate(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202606{idx + 1:02d}",
                    "stock_id": "4916",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 72.0,
                    "high": 74.4,
                    "low": 70.0,
                    "close": 74.4,
                    "volume": 10,
                }
            )
        rows.append(
            {
                "date": "20260626",
                "stock_id": "4916",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 81.8,
                "high": 81.8,
                "low": 81.8,
                "close": 81.8,
                "volume": 10,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))
        signal = detect_volume_breakout(df.iloc[-1])

        self.assertIsNotNone(signal)
        assert signal is not None
        self.assertEqual(signal.event_type, "bottom_volume_attack")
        self.assertIn("locked_limit_up_breakout", signal.notes)
        self.assertIn("locked_limit_no_volume_gate", signal.notes)
        self.assertNotIn("volume_ma20_lots_ge_1000", signal.notes)

    def test_non_locked_low_volume_ratio_breakout_still_fails(self) -> None:
        rows: list[dict[str, object]] = []
        for idx in range(25):
            rows.append(
                {
                    "date": f"202604{idx + 1:02d}",
                    "stock_id": "1234",
                    "stock_name": "TEST",
                    "market": "TWSE",
                    "open": 98.0,
                    "high": 100.0,
                    "low": 95.0,
                    "close": 98.0,
                    "volume": 2_000_000,
                }
            )
        rows.append(
            {
                "date": "20260501",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "open": 101.0,
                "high": 110.0,
                "low": 99.0,
                "close": 110.0,
                "volume": 3_000_000,
            }
        )
        df = add_price_metrics(pd.DataFrame(rows))

        self.assertIsNone(detect_volume_breakout(df.iloc[-1]))


if __name__ == "__main__":
    unittest.main()
