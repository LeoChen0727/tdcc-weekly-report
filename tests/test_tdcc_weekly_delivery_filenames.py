from pathlib import Path

import pandas as pd
import pytest

from scripts import build_tdcc_weekly_candidate_reports as builder
from scripts import validate_tdcc_weekly_candidate_reports as validator


MODEL_CROSS_WEEKLY_SECTION = "model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10"
MODEL_CROSS_CONSECUTIVE_SECTION = "model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10"


def _tdcc_manifest() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "section_order": 1,
                "section_id": "weekly_increase",
                "section_title_zh": "Weekly increase",
                "table_contract": "tdcc_ranking",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 2,
                "section_id": "consecutive_accumulation",
                "section_title_zh": "Consecutive accumulation",
                "table_contract": "tdcc_ranking",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 3,
                "section_id": MODEL_CROSS_WEEKLY_SECTION,
                "section_title_zh": "Weekly increase x model",
                "table_contract": "model_cross",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
            {
                "section_order": 4,
                "section_id": MODEL_CROSS_CONSECUTIVE_SECTION,
                "section_title_zh": "Consecutive accumulation x model",
                "table_contract": "model_cross",
                "include_in_highlight": True,
                "highlight_limit": 10,
                "include_in_full": True,
                "full_limit": 50,
                "required": True,
                "enabled": True,
                "notes_zh": "",
            },
        ],
        columns=builder.SECTION_MANIFEST_COLUMNS,
    )


def _tdcc_report(section_ids: list[str], report_kind: str = "highlight") -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    stock_by_section = {
        "weekly_increase": "1001",
        "consecutive_accumulation": "1002",
        MODEL_CROSS_WEEKLY_SECTION: "1003",
        MODEL_CROSS_CONSECUTIVE_SECTION: "1004",
    }
    for index, section_id in enumerate(section_ids, start=1):
        row = {column: "" for column in builder.REPORT_COLUMNS}
        row.update(
            {
                "report_kind": report_kind,
                "section_id": section_id,
                "section_name_zh": section_id,
                "section_rank": "1",
                "tdcc_list_type": section_id,
                "signal_date": "20260626",
                "stock_id": stock_by_section[section_id],
                "stock_name": f"Stock {index}",
                "tdcc_score": "10",
                "tdcc_effective_increase_count": "1",
                "tdcc_high_pair_effective_streak_weeks": "2",
            }
        )
        if section_id.startswith("model_cross_"):
            row["model_id"] = "tdcc_short_term_continuation_d5_d10"
        row.update(builder.report_facts(pd.Series(row)))
        rows.append(row)
    return builder.ensure_columns(pd.DataFrame(rows), builder.REPORT_COLUMNS)


def test_tdcc_weekly_delivery_pdf_paths_use_report_ready_signal_date() -> None:
    paths = builder.delivery_pdf_paths("20260612")

    assert paths["highlight"] == Path(
        "output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_20260612.pdf"
    )
    assert paths["full"] == Path(
        "output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_20260612.pdf"
    )
    assert validator.delivery_pdf_path("highlight", "20260612") == paths["highlight"]
    assert validator.delivery_pdf_path("full", "20260612") == paths["full"]


def test_tdcc_weekly_delivery_pdf_paths_reject_non_signal_date() -> None:
    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        builder.delivery_pdf_path("highlight", "2026-06-12")

    with pytest.raises(RuntimeError, match="YYYYMMDD"):
        validator.delivery_pdf_path("full", "")


def test_tdcc_weekly_model_cross_empty_sections_do_not_fail_builder_validation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manifest = _tdcc_manifest()
    highlight = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    full = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "full")
    # This unit test covers section rules; PDF content has its own contract tests.
    for attribute in ("HIGHLIGHT_PDF", "FULL_PDF"):
        path = tmp_path / f"{attribute}.pdf"
        path.write_bytes(b"%PDF-1.4\n" + b" " * 10000)
        monkeypatch.setattr(builder, attribute, path)

    builder.validate_outputs(highlight, full, manifest)


def test_tdcc_weekly_builder_rejects_report_ready_dataset_id_mismatch() -> None:
    manifest = _tdcc_manifest()
    highlight = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    full = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "full")
    highlight["source_tdcc_dataset_id"] = "tdcc-20260626-wrong"
    full["source_tdcc_dataset_id"] = "tdcc-20260626-wrong"

    with pytest.raises(RuntimeError, match="source_tdcc_dataset_id mismatch"):
        builder.validate_outputs(
            highlight,
            full,
            manifest,
            expected_dataset_id="tdcc-20260626-expected",
        )


def test_tdcc_weekly_model_cross_ranks_by_model_score_before_tdcc_rank() -> None:
    weekly = builder.ensure_columns(
        pd.DataFrame(
            [
                {"stock_id": "1001", "rank": 1, "tdcc_weekly_increase_score": 90},
                {"stock_id": "1002", "rank": 2, "tdcc_weekly_increase_score": 80},
                {"stock_id": "1003", "rank": 3, "tdcc_weekly_increase_score": 70},
            ]
        ),
        builder.BASE_COLUMNS,
    )
    consecutive = builder.ensure_columns(pd.DataFrame(), builder.BASE_COLUMNS)
    daily_models = pd.DataFrame(
        [
            {
                "stock_id": "1001",
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_name_zh": "TDCC short-term continuation",
                "display_rank": 10,
                "model_score": 60,
                "source_hit_labels_zh": "",
                "risk_tags_zh": "",
                "next_confirmation_zh": "",
                "recommended_usage_zh": "",
                "source_category_zh": "Short-term model",
            },
            {
                "stock_id": "1002",
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_name_zh": "TDCC short-term continuation",
                "display_rank": 20,
                "model_score": 100,
                "source_hit_labels_zh": "",
                "risk_tags_zh": "",
                "next_confirmation_zh": "",
                "recommended_usage_zh": "",
                "source_category_zh": "Short-term model",
            },
            {
                "stock_id": "1003",
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_name_zh": "TDCC short-term continuation",
                "display_rank": 30,
                "model_score": 80,
                "source_hit_labels_zh": "",
                "risk_tags_zh": "",
                "next_confirmation_zh": "",
                "recommended_usage_zh": "",
                "source_category_zh": "Short-term model",
            },
        ]
    )

    cross = builder.build_model_cross(weekly, consecutive, daily_models)
    weekly_cross = cross[cross["tdcc_list_type"] == "weekly_increase"].sort_values("tdcc_model_rank_in_list")

    assert weekly_cross["stock_id"].tolist() == ["1002", "1003", "1001"]
    assert weekly_cross["model_score"].astype(float).tolist() == [100.0, 80.0, 60.0]
    assert weekly_cross["tdcc_rank"].astype(int).tolist() == [2, 3, 1]


def test_tdcc_weekly_core_required_sections_still_fail_when_empty() -> None:
    manifest = _tdcc_manifest()
    highlight = _tdcc_report(["consecutive_accumulation"], "highlight")
    full = _tdcc_report(["consecutive_accumulation"], "full")

    with pytest.raises(RuntimeError, match="weekly_increase"):
        builder.validate_outputs(highlight, full, manifest)


def test_tdcc_weekly_markdown_lists_empty_model_cross_sections(tmp_path: Path) -> None:
    manifest = _tdcc_manifest()
    report = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    path = tmp_path / "tdcc_weekly.md"

    builder.write_report_md(report, path, "TDCC weekly", manifest, "highlight", "20260626")

    text = path.read_text(encoding="utf-8")
    assert "## Consecutive accumulation x model" in text
    assert "本週無符合此模型交集條件" in text


def test_tdcc_weekly_validator_lists_empty_model_cross_sections_as_zero_count_warning() -> None:
    manifest = _tdcc_manifest()
    report = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    weekly_source = report[report["section_id"].eq("weekly_increase")].copy()
    consecutive_source = report[report["section_id"].eq("consecutive_accumulation")].copy()
    errors: list[str] = []
    warnings: list[str] = []

    validator.validate_report(
        report,
        "highlight report-ready CSV",
        "highlight",
        "20260626",
        weekly_source,
        consecutive_source,
        manifest,
        errors,
        warnings,
    )

    assert errors == []
    assert any(MODEL_CROSS_CONSECUTIVE_SECTION in warning for warning in warnings)
    section_counts = validator.report_section_counts(report, manifest, "highlight")
    assert section_counts[MODEL_CROSS_WEEKLY_SECTION] == 0
    assert section_counts[MODEL_CROSS_CONSECUTIVE_SECTION] == 0


def test_tdcc_weekly_validator_rejects_model_cross_not_sorted_by_model_score() -> None:
    manifest = _tdcc_manifest()
    base = _tdcc_report(["weekly_increase", "consecutive_accumulation"], "highlight")
    model_rows = []
    for section_rank, stock_id, tdcc_rank, model_rank, model_score in [
        ("1", "1003", "1", "10", "60"),
        ("2", "1004", "2", "20", "100"),
    ]:
        row = {column: "" for column in builder.REPORT_COLUMNS}
        row.update(
            {
                "report_kind": "highlight",
                "section_id": MODEL_CROSS_WEEKLY_SECTION,
                "section_name_zh": "Weekly increase x model",
                "section_rank": section_rank,
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": tdcc_rank,
                "signal_date": "20260626",
                "stock_id": stock_id,
                "stock_name": f"Stock {stock_id}",
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_rank": model_rank,
                "tdcc_model_rank_in_list": section_rank,
                "model_score": model_score,
            }
        )
        model_rows.append(row)
    report = builder.ensure_columns(pd.concat([base, pd.DataFrame(model_rows)], ignore_index=True), builder.REPORT_COLUMNS)
    weekly_source = pd.DataFrame([{"stock_id": "1001"}])
    consecutive_source = pd.DataFrame([{"stock_id": "1002"}])
    errors: list[str] = []
    warnings: list[str] = []

    validator.validate_report(
        report,
        "highlight report-ready CSV",
        "highlight",
        "20260626",
        weekly_source,
        consecutive_source,
        manifest,
        errors,
        warnings,
    )

    assert any("not sorted by model_score desc" in error for error in errors)


def test_tdcc_weekly_validator_warns_invalid_single_holder_spike_without_failing_report() -> None:
    report = builder.ensure_columns(
        pd.DataFrame(
            [
                {
                    "stock_id": "2380",
                    "tdcc_1w_change_400": "54.95",
                    "tdcc_1w_change_600": "59.51",
                    "tdcc_1w_change_800": "61.04",
                    "tdcc_1w_change_1000": "62.59",
                }
            ]
        ),
        builder.REPORT_COLUMNS,
    )
    holder_ratio = pd.DataFrame(
        [
            {
                "code": "2380",
                "over_400_pct": "100.0",
                "over_600_pct": "100.0",
                "over_800_pct": "100.0",
                "over_1000_pct": "100.0",
            }
        ]
    )
    warnings: list[str] = []

    validator.validate_no_invalid_single_holder_spikes(
        report,
        holder_ratio,
        "highlight report-ready CSV",
        warnings,
    )

    assert warnings
    assert "2380" in warnings[0]


def test_tdcc_weekly_builder_quarantines_invalid_holder_distribution_codes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    invalid_path = tmp_path / "tdcc_invalid_holder_distribution_latest.csv"
    invalid_path.write_text(
        "\n".join(
            [
                "date,code,name,invalid_reason,active_level,active_holders,active_ratio_pct,total_holders,total_ratio_pct",
                "20260626,2380,虹光,single_holder_or_placeholder_distribution,15,1,100.0,1,100.0",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(builder, "INVALID_HOLDER_DISTRIBUTION_CSV", invalid_path)
    latest = pd.DataFrame(
        [
            {"signal_date": "20260626", "stock_id": "2380", "stock_name": "虹光"},
            {"signal_date": "20260626", "stock_id": "3374", "stock_name": "精材"},
        ]
    )

    filtered = builder.filter_invalid_holder_distributions(latest, "20260626")

    assert filtered["stock_id"].tolist() == ["3374"]


def _fuqiao_factual_ranking() -> pd.DataFrame:
    row = {
        "rank": 1,
        "signal_date": "20260904",
        "stock_id": "1815",
        "stock_name": "富喬",
        "tdcc_weekly_increase_score": 84.71,
        "tdcc_consecutive_accumulation_score": 94.71,
        "tdcc_1w_change_400": 6.10,
        "tdcc_1w_change_600": 6.23,
        "tdcc_1w_change_800": 6.21,
        "tdcc_1w_change_1000": 6.88,
        "tdcc_effective_increase_count": 4,
        "tdcc_high_pair_effective_streak_weeks": 3,
        "tdcc_consecutive_up_weeks": 5,
        "tdcc_price_phase": "tdcc_leading_price",
        "tdcc_phase_group_zh": "TDCC 領先股價 / 潛伏吸籌",
        "risk_bucket": "strong_but_pre_move",
        "risk_bucket_zh": "籌碼強但尚未發動",
        "price_context_date": "20260904",
        "price_context_source": "data/stock_price_history/1815.csv",
        "price_start_date_5d": "20260828",
        "price_start_date_10d": "20260821",
        "price_start_date_20d": "20260807",
        "report_price_return_5d": -5.577689,
        "report_price_return_10d": 5.803571,
        "report_price_return_20d": 37.951106,
        "report_distance_ma20_pct": 9.7476,
    }
    row.update(builder.report_facts(pd.Series(row)))
    return builder.ensure_columns(pd.DataFrame([row]), builder.BASE_COLUMNS)


def _fuqiao_factual_report() -> tuple[pd.DataFrame, pd.DataFrame]:
    ranking = _fuqiao_factual_ranking()
    daily_models = pd.DataFrame([{
        "stock_id": "1815",
        "model_id": "tdcc_short_term_continuation_d5_d10",
        "model_name_zh": "TDCC短線延續模型 D+5/D+10",
        "display_rank": 8,
        "model_score": 82.0,
        "why_selected_human_zh": "潛伏吸籌，尚未發動，預期上漲",
        "next_confirmation_zh": "突破即可買進",
        "recommended_usage_zh": "研究勝率99%，立即買進",
        "source_hit_labels_zh": "",
        "risk_tags_zh": "",
        "source_category_zh": "短線專項",
    }])
    cross = builder.build_model_cross(ranking, ranking, daily_models)
    sections = builder.build_report_source_sections(ranking, ranking, cross)
    report = builder.build_report_ready(sections, _tdcc_manifest(), "highlight")
    return ranking, report


def test_tdcc_weekly_fuqiao_reports_actual_windows_without_pre_move_claims() -> None:
    ranking, report = _fuqiao_factual_report()
    assert len(report) == 4
    assert report["stock_id"].tolist() == ["1815"] * 4
    for _, row in report.iterrows():
        assert row["report_price_return_5d"] == pytest.approx(-5.577689)
        assert row["report_price_return_20d"] == pytest.approx(37.951106)
        assert row["tdcc_1w_change_1000"] == pytest.approx(6.88)
        assert row["tdcc_high_pair_effective_streak_weeks"] == 3
        assert "-5.58%" in row["price_facts_zh"]
        assert "+5.80%" in row["price_facts_zh"]
        assert "+37.95%" in row["price_facts_zh"]
        assert "+9.75%" in row["price_facts_zh"]
        assert "+6.88" in row["tdcc_facts_zh"]
        assert row["historical_evidence_status"] == validator.HISTORICAL_EVIDENCE_STATUS
        assert row["historical_evidence_zh"] == validator.HISTORICAL_EVIDENCE_TEXT
    errors: list[str] = []
    validator.validate_report_facts(report, "fuqiao", ranking, ranking, errors)
    assert errors == []


def test_tdcc_weekly_display_does_not_import_phase_or_unapproved_model_prose() -> None:
    _, report = _fuqiao_factual_report()
    legacy_columns = {"tdcc_phase_group_zh", "risk_bucket", "risk_bucket_zh", "why_selected_zh", "next_confirmation_zh", "operation_note_zh"}
    for columns in [builder.PDF_RANKING_COLUMNS, builder.PDF_MODEL_CROSS_COLUMNS]:
        assert not legacy_columns.intersection(columns)
        text = builder.pdf_display_table(report, columns).to_string(index=False)
        for unsupported in ["潛伏吸籌", "尚未發動", "预期", "預期上漲", "立即買進", "研究勝率99%"]:
            assert unsupported not in text
        assert validator.HISTORICAL_EVIDENCE_TEXT in text


@pytest.mark.parametrize(
    ("column", "value", "expected_error"),
    [
        ("report_price_return_20d", 0.0, "factual value differs"),
        ("tdcc_1w_change_1000", "", "factual value differs"),
        ("price_context_date", "20260907", "no later than signal_date"),
        ("price_start_date_5d", "20260904", "must precede"),
        ("price_context_source", "output/latest/research_backtest/metrics.csv", "canonical stock price history"),
        ("historical_evidence_status", "approved", "not approved"),
        ("historical_evidence_zh", "研究平均報酬+20%", "unavailable approved matching metrics"),
        ("price_facts_zh", "潛伏吸籌，尚未發動", "unsupported interpretation"),
        ("price_facts_zh", "有望上漲25%", "must contain only"),
    ],
)
def test_tdcc_weekly_factual_validator_rejects_drift_or_unapproved_claims(column, value, expected_error) -> None:
    ranking, report = _fuqiao_factual_report()
    report[column] = report[column].astype(object)
    report.loc[report.index[0], column] = value
    errors: list[str] = []
    validator.validate_report_facts(report, "injected", ranking, ranking, errors)
    assert any(expected_error in error for error in errors)


def test_tdcc_weekly_missing_price_is_disclosed_and_not_converted_to_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(builder, "cached_price_history", lambda stock_id: pd.DataFrame())
    before = _fuqiao_factual_ranking().drop(columns=validator.REPORT_PRICE_COLUMNS)
    enriched = builder.add_report_price_context(before)
    row = enriched.iloc[0]
    for column in validator.PRICE_RETURN_COLUMNS + ["report_distance_ma20_pct"]:
        assert validator.safe_str(row.get(column)) == ""
    facts = builder.report_facts(row)
    assert "0.00%" not in facts["price_facts_zh"]
    assert facts["price_facts_zh"]
    report = builder.build_report_source_sections(enriched, enriched, pd.DataFrame())
    errors: list[str] = []
    validator.validate_report_facts(report, "missing price", enriched, enriched, errors)
    assert errors == []
    report.loc[report.index[0], "report_price_return_5d"] = 0.0
    errors = []
    validator.validate_report_facts(report, "fabricated zero", enriched, enriched, errors)
    assert any("factual value differs" in error for error in errors)


def test_tdcc_weekly_price_context_excludes_future_and_preserves_ranking(monkeypatch: pytest.MonkeyPatch) -> None:
    dates = pd.bdate_range("20260807", "20260904").strftime("%Y%m%d").tolist()
    closes = [100.0] * len(dates)
    closes[0], closes[10], closes[15], closes[20] = 85.9, 112.0, 125.5, 118.5
    price = pd.DataFrame({"date": dates + ["20260907"], "close": closes + [999.0], "ma20": [107.975] * len(dates) + [999.0]})
    monkeypatch.setattr(builder, "cached_price_history", lambda stock_id: price)
    before = _fuqiao_factual_ranking()
    protected = ["stock_id", "rank", "tdcc_weekly_increase_score", "tdcc_consecutive_accumulation_score", "tdcc_price_phase"]
    enriched = builder.add_report_price_context(before)
    pd.testing.assert_frame_equal(enriched[protected], before[protected])
    row = enriched.iloc[0]
    assert row["price_context_date"] == "20260904"
    assert row["price_start_date_5d"] == "20260828"
    assert row["price_start_date_10d"] == "20260821"
    assert row["price_start_date_20d"] == "20260807"
    assert row["report_price_return_5d"] == pytest.approx((118.5 / 125.5 - 1) * 100, abs=0.000001)
    assert row["report_price_return_10d"] == pytest.approx((118.5 / 112.0 - 1) * 100, abs=0.000001)
    assert row["report_price_return_20d"] == pytest.approx((118.5 / 85.9 - 1) * 100, abs=0.000001)


def test_tdcc_weekly_invalid_last_price_does_not_reuse_an_older_close(monkeypatch: pytest.MonkeyPatch) -> None:
    price = pd.DataFrame([
        {"date": "20260903", "close": 120.0, "ma20": 107.0},
        {"date": "20260904", "close": float("nan"), "ma20": 107.975},
        {"date": "20260907", "close": 130.0, "ma20": 110.0},
    ])
    monkeypatch.setattr(builder, "cached_price_history", lambda stock_id: price)
    enriched = builder.add_report_price_context(_fuqiao_factual_ranking())
    row = enriched.iloc[0]
    assert all(validator.safe_str(row.get(column)) == "" for column in validator.REPORT_PRICE_COLUMNS)
    assert "截至缺資料" in builder.report_facts(row)["price_facts_zh"]


def test_tdcc_weekly_artifact_validator_rejects_legacy_claims_split_across_pdf_lines() -> None:
    manifest = _tdcc_manifest()
    text = "TDCC data date: 20260904\n" + "\n".join(manifest["section_title_zh"])
    errors: list[str] = []
    validator.validate_artifact(text, "PDF", "highlight", "20260904", manifest, errors)
    assert errors == []
    validator.validate_artifact(text + "\n潛伏\n吸籌／尚未\n發動", "PDF", "highlight", "20260904", manifest, errors)
    assert any("unsupported market interpretations" in error for error in errors)


def test_tdcc_weekly_blank_price_date_does_not_extend_the_available_window(monkeypatch: pytest.MonkeyPatch) -> None:
    price = pd.DataFrame({
        "date": ["", "20260831", "20260901", "20260902", "20260903", "20260904"],
        "close": [1.0, 100.0, 101.0, 102.0, 103.0, 104.0],
        "ma20": [100.0] * 6,
    })
    monkeypatch.setattr(builder, "cached_price_history", lambda stock_id: price)
    row = builder.add_report_price_context(_fuqiao_factual_ranking()).iloc[0]
    assert row["price_context_date"] == "20260904"
    assert validator.safe_str(row["price_start_date_5d"]) == ""
    assert validator.safe_str(row["report_price_return_5d"]) == ""
