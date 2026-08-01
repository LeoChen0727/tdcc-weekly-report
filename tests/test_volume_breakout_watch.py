from __future__ import annotations

import os
import io
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
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
    canonical_csv_slice_sha256,
    canonical_text_sha256,
    classify_watch,
    detect_volume_breakout,
    ensure_watch_schema,
    event_log_has_formal_bottom_history,
    filter_latest_to_effective_signal_date,
)
from build_daily_candidate_model_layer import (  # noqa: E402
    volume_v2_canonical_text_sha256 as consumer_canonical_csv_slice_sha256,
)
from build_volume_attack_theme_layer import (  # noqa: E402
    apply_theme_status_to_stocks,
    build_theme_layer,
    enrich_stocks,
    read_csv_revision,
    sha256_file as theme_canonical_text_sha256,
    validate_official_warrant_source_revision,
)
import validate_volume_attack_theme_layer as theme_layer_validator  # noqa: E402
from validate_volume_attack_theme_layer import (  # noqa: E402
    canonical_text_sha256 as theme_validator_payload_sha256,
    resolve_pinned_canonical_source_revision,
    sha256_file as theme_validator_canonical_text_sha256,
)
from validate_volume_breakout_watch import (  # noqa: E402
    advisory_as_of_matches_signal_date,
    advisory_source_lineage_errors,
    canonical_csv_slice_sha256 as validator_canonical_csv_slice_sha256,
    canonical_text_sha256 as validator_canonical_text_sha256,
    forbidden_watch_columns,
)


class VolumeBreakoutWatchTest(unittest.TestCase):
    def setUp(self) -> None:
        self._theme_source_sha_patcher = patch(
            "build_volume_attack_theme_layer.sha256_file",
            return_value="e" * 64,
        )
        self._theme_source_sha_patcher.start()
        self.addCleanup(self._theme_source_sha_patcher.stop)

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

    def test_theme_official_source_revision_requires_one_matching_as_of(self) -> None:
        official = pd.DataFrame(
            [
                {
                    "date": "20260718",
                    "stock_id": "6505",
                    "warrant_flow_signal": "call_strong_inflow",
                }
            ]
        )

        self.assertEqual(
            validate_official_warrant_source_revision(
                official,
                expected_as_of="20260718",
                source_sha256="f" * 64,
            ),
            "20260718",
        )
        with self.assertRaisesRegex(RuntimeError, "source as-of mismatch"):
            validate_official_warrant_source_revision(
                official,
                expected_as_of="20260719",
                source_sha256="f" * 64,
            )

    def test_theme_official_source_revision_rejects_empty_or_undated_payload(
        self,
    ) -> None:
        with self.assertRaisesRegex(RuntimeError, "source is empty"):
            validate_official_warrant_source_revision(
                pd.DataFrame(columns=["date", "stock_id", "warrant_flow_signal"]),
                expected_as_of="20260718",
                source_sha256="f" * 64,
            )
        with self.assertRaisesRegex(RuntimeError, "row has no as-of"):
            validate_official_warrant_source_revision(
                pd.DataFrame(
                    [
                        {
                            "date": "",
                            "stock_id": "6505",
                            "warrant_flow_signal": "call_strong_inflow",
                        }
                    ]
                ),
                expected_as_of="20260718",
                source_sha256="f" * 64,
            )

    def test_theme_csv_revision_hashes_the_same_payload_it_parses(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "warrant.csv"
            captured_payload = (
                b"date,stock_id,warrant_flow_signal\n"
                b"20260718,6505,call_strong_inflow\n"
            )
            later_payload = (
                b"date,stock_id,warrant_flow_signal\n"
                b"20260718,6505,put_inflow\n"
            )
            source.write_bytes(later_payload)

            with patch.object(
                Path,
                "read_bytes",
                side_effect=[captured_payload, later_payload],
            ) as read_bytes:
                frame, payload_sha = read_csv_revision(source)

            self.assertEqual(read_bytes.call_count, 1)
            self.assertEqual(frame.iloc[0]["warrant_flow_signal"], "call_strong_inflow")
            self.assertEqual(
                payload_sha,
                theme_validator_payload_sha256(captured_payload),
            )

    def test_theme_validator_resolves_pinned_revision_after_latest_advances(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "output/latest/warrant_flow_latest.csv"
            source.parent.mkdir(parents=True)
            source.write_text(
                "date,stock_id,warrant_flow_signal\n"
                "20260717,6505,call_strong_inflow\n",
                encoding="utf-8",
            )
            old_sha = theme_validator_payload_sha256(source.read_bytes())
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "theme-test@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Theme Test"],
                cwd=root,
                check=True,
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "old warrant revision"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            source.write_text(
                "date,stock_id,warrant_flow_signal\n"
                "20260730,6505,call_strong_inflow\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "advance warrant latest"],
                cwd=root,
                check=True,
                capture_output=True,
            )

            payload, revision = resolve_pinned_canonical_source_revision(
                root,
                "output/latest/warrant_flow_latest.csv",
                old_sha,
            )

            self.assertEqual(theme_validator_payload_sha256(payload), old_sha)
            self.assertNotEqual(revision, "working_tree")

    def test_theme_validator_main_uses_pinned_revision_after_latest_advances(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            latest = root / "output/latest"
            latest.mkdir(parents=True)
            watch, theme_context, two_line, candidates, taxonomy, official = (
                self._theme_enrichment_inputs()
            )
            for frame in (watch, candidates, official):
                date_column = "signal_date" if "signal_date" in frame.columns else "date"
                frame[date_column] = "20260717"
            watch["advisory_score_as_of"] = "20260717"
            watch["volume_ratio"] = "2.0"

            watch_path = latest / "volume_breakout_watch_latest.csv"
            candidate_path = latest / "all_candidates_latest.csv"
            official_path = latest / "warrant_flow_latest.csv"
            watch.to_csv(watch_path, index=False, lineterminator="\n")
            candidates.to_csv(candidate_path, index=False, lineterminator="\n")
            official.to_csv(official_path, index=False, lineterminator="\n")
            watch_sha = theme_validator_payload_sha256(watch_path.read_bytes())
            candidate_sha = theme_validator_payload_sha256(candidate_path.read_bytes())
            official_sha = theme_validator_payload_sha256(official_path.read_bytes())

            stocks = enrich_stocks(
                watch,
                theme_context,
                two_line,
                candidates,
                taxonomy,
                official,
                warrant_as_of="20260717",
                volume_watch_source_sha256=watch_sha,
                candidate_source_sha256=candidate_sha,
                official_warrant_source_sha256=official_sha,
            )
            themes = build_theme_layer(stocks)
            stocks = apply_theme_status_to_stocks(stocks, themes)
            theme_path = latest / "volume_attack_theme_layer_latest.csv"
            stock_path = latest / "volume_attack_theme_stocks_latest.csv"
            themes.to_csv(theme_path, index=False, lineterminator="\n")
            stocks.to_csv(stock_path, index=False, lineterminator="\n")
            lineage_tokens = "\n".join(
                [
                    "source_watch: `output/latest/volume_breakout_watch_latest.csv`",
                    f"source_watch_sha256: `{watch_sha}`",
                    "warrant_projection_source: `output/latest/all_candidates_latest.csv`",
                    f"warrant_projection_source_sha256: `{candidate_sha}`",
                    "warrant_official_parity_source: `output/latest/warrant_flow_latest.csv`",
                    f"warrant_official_parity_source_sha256: `{official_sha}`",
                    "",
                ]
            )
            (latest / "volume_attack_theme_layer_latest.md").write_text(
                lineage_tokens,
                encoding="utf-8",
            )
            (latest / "volume_attack_theme_stocks_latest.md").write_text(
                lineage_tokens,
                encoding="utf-8",
            )

            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "theme-test@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Theme Test"],
                cwd=root,
                check=True,
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "pinned theme revision"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            base_sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            official.loc[0, "date"] = "20260730"
            official.loc[0, "warrant_flow_signal"] = "put_inflow"
            official.to_csv(official_path, index=False, lineterminator="\n")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "advance mutable warrant latest"],
                cwd=root,
                check=True,
                capture_output=True,
            )

            original_cwd = Path.cwd()
            try:
                os.chdir(root)
                with patch.object(theme_layer_validator, "ROOT", root), patch.dict(
                    os.environ,
                    {"BASE_SHA": base_sha},
                ):
                    self.assertEqual(theme_layer_validator.main(), 0)
            finally:
                os.chdir(original_cwd)
            result = pd.read_json(
                latest / "volume_attack_theme_layer_validation_latest.json",
                typ="series",
            )
            self.assertEqual(result["status"], "pass")

    def test_theme_validator_rejects_unreconstructable_pinned_revision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "output/latest/warrant_flow_latest.csv"
            source.parent.mkdir(parents=True)
            source.write_text(
                "date,stock_id,warrant_flow_signal\n"
                "20260730,6505,call_strong_inflow\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "theme-test@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Theme Test"],
                cwd=root,
                check=True,
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "only warrant revision"],
                cwd=root,
                check=True,
                capture_output=True,
            )

            with self.assertRaisesRegex(RuntimeError, "not reconstructable"):
                resolve_pinned_canonical_source_revision(
                    root,
                    "output/latest/warrant_flow_latest.csv",
                    "f" * 64,
                )

    def test_theme_validator_rejects_branch_only_revision_outside_trusted_ref(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "output/latest/warrant_flow_latest.csv"
            source.parent.mkdir(parents=True)
            source.write_text(
                "date,stock_id,warrant_flow_signal\n"
                "20260717,6505,call_strong_inflow\n",
                encoding="utf-8",
            )
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "theme-test@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Theme Test"],
                cwd=root,
                check=True,
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "trusted base"],
                cwd=root,
                check=True,
                capture_output=True,
            )
            base_sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            source.write_text(
                "date,stock_id,warrant_flow_signal\n"
                "20260718,6505,put_inflow\n",
                encoding="utf-8",
            )
            branch_only_sha = theme_validator_payload_sha256(source.read_bytes())
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(
                ["git", "commit", "-m", "branch only revision"],
                cwd=root,
                check=True,
                capture_output=True,
            )

            with self.assertRaisesRegex(RuntimeError, "not reconstructable"):
                resolve_pinned_canonical_source_revision(
                    root,
                    "output/latest/warrant_flow_latest.csv",
                    branch_only_sha,
                    trusted_ref=base_sha,
                    allow_live=True,
                )

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
        unrelated_official = pd.DataFrame(
            [
                {
                    "date": "20260718",
                    "stock_id": "9999",
                    "warrant_flow_signal": "no_signal",
                }
            ]
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
                unrelated_official,
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
        mixed = pd.DataFrame(
            [{"signal_date": "20260718", "advisory_score_as_of": "2026-07-18"}]
        )
        invalid_signal = valid.copy()
        invalid_signal.loc[0, "signal_date"] = "20260230"
        invalid_advisory = valid.copy()
        invalid_advisory.loc[0, "advisory_score_as_of"] = "2026-02-30"

        self.assertTrue(advisory_as_of_matches_signal_date(valid))
        self.assertTrue(advisory_as_of_matches_signal_date(mixed))
        self.assertFalse(advisory_as_of_matches_signal_date(stale))
        self.assertFalse(advisory_as_of_matches_signal_date(blank))
        self.assertFalse(advisory_as_of_matches_signal_date(invalid_signal))
        self.assertFalse(advisory_as_of_matches_signal_date(invalid_advisory))

    def test_mixed_date_formats_have_producer_validator_consumer_parity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            source.write_text(
                "date,stock_id,close\n"
                "2026-07-17,6505,41\n"
                "20260718,6505,42\n",
                encoding="utf-8",
            )
            hashers = (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            )
            expected = canonical_csv_slice_sha256(source, "20260718")
            for hasher in hashers:
                with self.subTest(hasher=hasher.__module__):
                    self.assertEqual(hasher(source, "2026-07-18"), expected)
            mixed_watch = pd.DataFrame(
                [{"signal_date": "2026-07-18", "advisory_score_as_of": "20260718"}]
            )
            self.assertTrue(advisory_as_of_matches_signal_date(mixed_watch))

    def test_advisory_score_source_lineage_is_hash_pinned(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "data/stock_price_history/6505.csv"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text("date,stock_id,close\n20260718,6505,42\n", encoding="utf-8")
            source_sha = canonical_csv_slice_sha256(source, "20260718")
            watch = pd.DataFrame(
                [
                    {
                        "stock_id": "6505",
                        "signal_date": "20260718",
                        "advisory_score_as_of": "20260718",
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

    def test_advisory_source_slice_is_stable_after_later_rows_append(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            as_of_text = (
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "20260718,6505,42\n"
            )
            source.write_text(as_of_text, encoding="utf-8")
            expected = canonical_text_sha256(source)

            source.write_text(
                as_of_text + "20260720,6505,43\n20260721,6505,44\n",
                encoding="utf-8",
            )

            self.assertEqual(
                canonical_csv_slice_sha256(source, "20260718"), expected
            )
            self.assertEqual(
                validator_canonical_csv_slice_sha256(source, "20260718"), expected
            )
            source.write_text(
                as_of_text + "20260720,6505,999\n20260721,6505,44\n",
                encoding="utf-8",
            )
            self.assertEqual(
                canonical_csv_slice_sha256(source, "20260718"), expected
            )
            self.assertEqual(
                validator_canonical_csv_slice_sha256(source, "20260718"), expected
            )

    def test_advisory_source_slice_rejects_prior_or_as_of_row_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            source.write_text(
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "20260718,6505,42\n"
                "20260720,6505,43\n",
                encoding="utf-8",
            )
            expected = canonical_csv_slice_sha256(source, "20260718")

            source.write_text(
                "date,stock_id,close\n"
                "20260717,6505,40\n"
                "20260718,6505,42\n"
                "20260720,6505,43\n",
                encoding="utf-8",
            )
            self.assertNotEqual(
                canonical_csv_slice_sha256(source, "20260718"), expected
            )

            source.write_text(
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "20260718,6505,99\n"
                "20260720,6505,43\n",
                encoding="utf-8",
            )
            self.assertNotEqual(
                validator_canonical_csv_slice_sha256(source, "20260718"), expected
            )

    def test_advisory_source_slice_fails_closed_on_invalid_date_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            source.write_text(
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "20260720,6505,43\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "exactly one as-of row"):
                canonical_csv_slice_sha256(source, "20260718")

            source.write_text(
                "date,stock_id,close\n"
                "20260718,6505,42\n"
                "20260717,6505,41\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "strictly increasing and unique"):
                validator_canonical_csv_slice_sha256(source, "20260718")

            source.write_text(
                "date,date,stock_id\n"
                "20260718,20260718,6505\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "exactly one date column"):
                canonical_csv_slice_sha256(source, "20260718")

    def test_advisory_source_slice_uses_strict_calendar_dates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            hashers = (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            )
            source.write_text(
                "date,stock_id,close\n20260230,6505,41\n",
                encoding="utf-8",
            )
            for hasher in hashers:
                with self.subTest(hasher=hasher.__module__):
                    with self.assertRaisesRegex(RuntimeError, "row date is invalid"):
                        hasher(source, "20260228")

            source.write_text(
                "date,stock_id,close\n20260228,6505,41\n",
                encoding="utf-8",
            )
            for invalid_as_of in ("20260230", "prefix20260228suffix", "2026-2-28"):
                for hasher in hashers:
                    with self.subTest(as_of=invalid_as_of, hasher=hasher.__module__):
                        with self.assertRaisesRegex(RuntimeError, "as-of date is invalid"):
                            hasher(source, invalid_as_of)

            source.write_text(
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "2026-07-17,6505,42\n"
                "20260718,6505,43\n",
                encoding="utf-8",
            )
            for hasher in hashers:
                with self.subTest(normalized_duplicate=hasher.__module__):
                    with self.assertRaisesRegex(RuntimeError, "strictly increasing and unique"):
                        hasher(source, "20260718")

    def test_advisory_source_slice_ignores_future_order_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "6505.csv"
            through_as_of = (
                "date,stock_id,close\n"
                "20260717,6505,41\n"
                "20260718,6505,42\n"
            )
            source.write_text(through_as_of, encoding="utf-8")
            expected = canonical_text_sha256(source)
            source.write_text(
                through_as_of
                + "20260721,6505,45\n"
                + "20260720,6505,44\n"
                + "20260721,6505,999\n",
                encoding="utf-8",
            )
            for hasher in (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            ):
                with self.subTest(hasher=hasher.__module__):
                    self.assertEqual(hasher(source, "20260718"), expected)

    def test_advisory_source_slice_canonicalizes_escaped_and_multiline_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            first = Path(temp_dir) / "first.csv"
            second = Path(temp_dir) / "second.csv"
            first.write_text(
                'date,stock_id,note\n'
                '2026-07-17,6505,"alpha, ""quoted"""\n'
                '20260718,6505,"line one\nline two"\n'
                '20260720,6505,future\n',
                encoding="utf-8",
            )
            second.write_bytes(
                b'\xef\xbb\xbfdate,stock_id,note\r\n'
                b'20260717,6505,"alpha, ""quoted"""\r\n'
                b'20260718,6505,"line one\r\nline two"\r\n'
                b'20260721,6505,ignored\r\n'
            )
            expected = canonical_csv_slice_sha256(first, "2026-07-18")
            for hasher in (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            ):
                with self.subTest(hasher=hasher.__module__):
                    self.assertEqual(hasher(first, "20260718"), expected)
                    self.assertEqual(hasher(second, "20260718"), expected)

            malformed = Path(temp_dir) / "malformed.csv"
            malformed.write_text(
                'date,stock_id,note\n20260718,6505,"unterminated\n',
                encoding="utf-8",
            )
            for hasher in (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            ):
                with self.subTest(malformed=hasher.__module__):
                    with self.assertRaisesRegex(RuntimeError, "CSV is invalid"):
                        hasher(malformed, "20260718")

    def test_materialized_20260717_artifact_hashes_are_slice_compatible(self) -> None:
        artifact_root = Path(os.environ.get("TDCC_VOLUME_LINEAGE_REPO_ROOT", ROOT))
        watch_path = artifact_root / "output/latest/volume_breakout_watch_latest.csv"
        if not watch_path.is_file():
            self.skipTest("current-main volume breakout artifacts are not materialized")
        expected = {
            "4139": "28cbde51ca0eb7a03631839d06c647647cf58cb8557964cd3632243458546e61",
            "6243": "418e3ed7d1dfa2e2f0d6cf8e02393204942b7e5bc97611e6458d1d0ef0716b8f",
            "3288": "2cdc283b3c40b503194efd275a761c4a740dd3458fc754864cc318fdde1f9929",
            "3024": "b60cdd6df569aa6640af0119ce693502f9e2a2a57430b56245230c950abff48b",
        }
        watch = pd.read_csv(watch_path, dtype=str, keep_default_na=False)
        current = watch[watch["signal_date"].astype(str) == "20260717"]
        self.assertEqual(len(current), len(expected))
        self.assertEqual(
            dict(zip(current["stock_id"], current["advisory_score_source_sha256"])),
            expected,
        )
        for row in current.to_dict("records"):
            source = artifact_root / row["advisory_score_source_artifact"]
            self.assertTrue(source.is_file(), source.as_posix())
            for hasher in (
                canonical_csv_slice_sha256,
                validator_canonical_csv_slice_sha256,
                consumer_canonical_csv_slice_sha256,
            ):
                with self.subTest(stock_id=row["stock_id"], hasher=hasher.__module__):
                    self.assertEqual(
                        hasher(source, row["advisory_score_as_of"]),
                        row["advisory_score_source_sha256"],
                    )

    def test_origin_main_20260717_artifact_hashes_survive_future_appends(self) -> None:
        repository = os.environ.get("TDCC_VOLUME_LINEAGE_GIT_REPO", "").strip()
        if not repository:
            self.skipTest("set TDCC_VOLUME_LINEAGE_GIT_REPO for origin/main integration")
        repo = Path(repository)

        def git_show(relative_path: str) -> str:
            return subprocess.check_output(
                [
                    "git",
                    "-c",
                    f"safe.directory={repo.resolve().as_posix()}",
                    "show",
                    f"origin/main:{relative_path}",
                ],
                cwd=repo,
            ).decode("utf-8-sig")

        expected = {
            "4139": "28cbde51ca0eb7a03631839d06c647647cf58cb8557964cd3632243458546e61",
            "6243": "418e3ed7d1dfa2e2f0d6cf8e02393204942b7e5bc97611e6458d1d0ef0716b8f",
            "3288": "2cdc283b3c40b503194efd275a761c4a740dd3458fc754864cc318fdde1f9929",
            "3024": "b60cdd6df569aa6640af0119ce693502f9e2a2a57430b56245230c950abff48b",
        }
        watch = pd.read_csv(
            io.StringIO(git_show("output/latest/volume_breakout_watch_latest.csv")),
            dtype=str,
            keep_default_na=False,
        )
        current = watch[watch["signal_date"].astype(str) == "20260717"]
        self.assertEqual(len(current), len(expected))
        self.assertEqual(
            dict(zip(current["stock_id"], current["advisory_score_source_sha256"])),
            expected,
        )
        for row in current.to_dict("records"):
            source_text = git_show(row["advisory_score_source_artifact"])
            with patch.object(Path, "read_text", return_value=source_text):
                for hasher in (
                    canonical_csv_slice_sha256,
                    validator_canonical_csv_slice_sha256,
                    consumer_canonical_csv_slice_sha256,
                ):
                    with self.subTest(
                        stock_id=row["stock_id"],
                        hasher=hasher.__module__,
                    ):
                        self.assertEqual(
                            hasher(
                                Path(row["advisory_score_source_artifact"]),
                                row["advisory_score_as_of"],
                            ),
                            row["advisory_score_source_sha256"],
                        )

    def test_canonical_text_sha_is_equal_for_lf_and_crlf(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            lf_path = Path(temp_dir) / "lf.csv"
            crlf_path = Path(temp_dir) / "crlf.csv"
            bom_path = Path(temp_dir) / "bom.csv"
            lf_path.write_bytes(b"date,stock_id\n20260718,6505\n")
            crlf_path.write_bytes(b"date,stock_id\r\n20260718,6505\r\n")
            bom_path.write_bytes(
                b"\xef\xbb\xbfdate,stock_id\r\n20260718,6505\r\n"
            )

            expected = canonical_text_sha256(lf_path)

            self.assertEqual(expected, canonical_text_sha256(crlf_path))
            self.assertEqual(expected, validator_canonical_text_sha256(lf_path))
            self.assertEqual(expected, validator_canonical_text_sha256(crlf_path))
            self.assertEqual(
                canonical_csv_slice_sha256(lf_path, "20260718"),
                canonical_csv_slice_sha256(crlf_path, "20260718"),
            )
            self.assertEqual(
                canonical_csv_slice_sha256(lf_path, "20260718"),
                canonical_csv_slice_sha256(bom_path, "20260718"),
            )
            self.assertEqual(
                validator_canonical_csv_slice_sha256(lf_path, "20260718"),
                validator_canonical_csv_slice_sha256(crlf_path, "20260718"),
            )
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
