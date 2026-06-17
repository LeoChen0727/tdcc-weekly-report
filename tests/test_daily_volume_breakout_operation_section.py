from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402
import build_volume_breakout_confirmed_operation_backtest as operation_backtest  # noqa: E402
import generate_chatgpt_side_daily_reports as pdf_generator  # noqa: E402
import validate_chatgpt_side_volume_operation_pdf_integration as pdf_integration_validator  # noqa: E402


def approval_stub() -> dict[str, str]:
    return {
        "approval_source": "approved_operation_patterns_latest.csv",
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": "volume_breakout_confirmed_operation_v1",
        "approval_version": "volume_breakout_operation_v1_20260615",
        "operation_directive_level": "approved_daily_operation_guidance",
        "row_action_status": "",
        "buy_rank_eligible": "False",
        "buy_filter_id": "positive_evidence_oos_rank_v1",
        "approval_note_zh": "approved for test",
    }


def volume_signal(stock_id: str = "1234", signal_date: str = "20260616", rank: str = "1") -> dict[str, str]:
    return {
        "model_id": "volume_range_breakout",
        "signal_date": signal_date,
        "stock_id": stock_id,
        "stock_name": "測試股",
        "display_rank": rank,
        "model_score": "70",
        "same_model_repeat_status_zh": "新進榜",
        "next_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
        "risk_tags_zh": "依模型風險欄位管理",
    }


def formal_summary(
    trigger_id: str = "next_day_continuation_confirmed",
    tdcc_list_type: str = "no_tdcc",
    rank_bucket: str = "all",
    confluence_scope: str = "operation_trigger",
    confluence_id: str = "all_confirmed_volume_breakout",
    sample_size: str = "30",
    win_rate: str = "60",
    avg_return: str = "3.5",
    median_return: str = "2.5",
    score: str = "18",
    oos: str = "True",
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "tdcc_list_type": tdcc_list_type,
                "rank_bucket": rank_bucket,
                "trigger_id": trigger_id,
                "confluence_scope": confluence_scope,
                "confluence_id": confluence_id,
                "sample_size": sample_size,
                "win_rate": win_rate,
                "avg_return": avg_return,
                "median_return": median_return,
                "ranking_research_score": score,
                "out_of_sample_pass": oos,
                "confidence_status": "中",
            }
        ]
    )


def patch_lifecycle_sources(monkeypatch, tmp_path: Path, stock_id: str, price_rows: list[dict[str, str]]) -> Path:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    price_dir = tmp_path / "data" / "stock_price_history"
    snapshot_dir.mkdir(parents=True)
    price_dir.mkdir(parents=True)
    pd.DataFrame(price_rows).to_csv(price_dir / f"{stock_id}.csv", index=False)
    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "STOCK_PRICE_HISTORY_DIR", price_dir)
    return snapshot_dir


def build_rows_for_test(signals: pd.DataFrame, report_date: str, summary: pd.DataFrame) -> pd.DataFrame:
    rows, _audit = builder.build_lifecycle_rows(
        signals,
        report_date,
        int(signals["stock_id"].nunique()) if not signals.empty else 0,
        approval_stub(),
        "2026-06-17 12:00:00 Asia/Taipei",
        summary,
    )
    return pd.DataFrame(rows, columns=builder.OUTPUT_COLUMNS)


def backtest_lifecycle_state(stock_id: str, signal_date: str, report_date: str) -> str:
    price = builder.load_price_history(stock_id)
    signal_positions = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    report_positions = price.index[price["date"].astype(str).eq(report_date)].tolist()
    assert signal_positions
    assert report_positions
    lifecycle = operation_backtest.lifecycle_state_for_signal(
        price,
        int(signal_positions[-1]),
        int(report_positions[-1]),
    )
    return str(lifecycle["operation_lifecycle_state"])


def test_lifecycle_keeps_unconfirmed_signal_pending(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert pending["stock_id"].tolist() == ["1234", "1234"]
    assert set(pending["pending_age_zh"]) == {"D+1 待確認"}
    assert set(pending["row_action_status"]) == {"pending_confirmation"}
    assert set(pending["buy_rank_eligible"]) == {"False"}
    assert pending["selected_trigger_id"].eq("").all()
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "pending_confirmation"


def test_lifecycle_confirms_signal_on_report_date(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.3", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["selected_trigger_id"]) == {"next_day_continuation_confirmed"}
    assert set(confirmed["confirmation_date"]) == {"20260617"}
    assert pending.empty
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "confirmed_operation"


def test_lifecycle_moves_prior_confirmed_signal_to_active(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.2", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.2", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert active["stock_id"].tolist() == ["1234", "1234"]
    assert confirmed.empty
    assert set(active["row_action_status"]) == {"active_operation"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["selected_trigger_id"]) == {"next_day_continuation_confirmed"}
    assert set(active["confirmation_date"]) == {"20260616"}
    assert backtest_lifecycle_state("1234", "20260615", "20260617") == "active_operation"


def test_lifecycle_expired_signal_matches_backtest_terminal_state(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "9.5", "high": "9.8", "low": "8.8", "close": "9.2", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "expired"


def test_lifecycle_does_not_promote_confirmed_signal_without_positive_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.3", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    weak_summary = formal_summary()
    weak_summary["median_return"] = "-1"
    out = build_rows_for_test(pd.DataFrame(), "20260617", weak_summary)

    assert out.empty


def test_lifecycle_does_not_apply_tdcc_top10_evidence_to_no_tdcc_stock(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.3", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    tdcc_top10_only = formal_summary(
        tdcc_list_type="weekly_increase",
        rank_bucket="top_10",
        sample_size="10",
        win_rate="70",
        avg_return="22.68",
        median_return="21.09",
        score="32.78",
        oos="True",
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", tdcc_top10_only)

    assert out.empty


def test_lifecycle_uses_exact_no_tdcc_row_level_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.3", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )
    summary = pd.concat(
        [
            formal_summary(
                tdcc_list_type="weekly_increase",
                rank_bucket="top_10",
                sample_size="10",
                win_rate="70",
                avg_return="22.68",
                median_return="21.09",
                score="32.78",
                oos="True",
            ),
            formal_summary(
                tdcc_list_type="no_tdcc",
                rank_bucket="all",
                sample_size="22",
                win_rate="55",
                avg_return="4.2",
                median_return="1.8",
                score="9.5",
                oos="True",
            ),
        ],
        ignore_index=True,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", summary)

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["sample_size"]) == {"22"}
    assert set(confirmed["win_rate_zh"]) == {"55.00%"}
    assert set(confirmed["median_return_zh"]) == {"1.80%"}
    assert set(confirmed["evidence_tdcc_list_type"]) == {"no_tdcc"}
    assert set(confirmed["evidence_rank_bucket"]) == {"all"}


def test_daily_signal_context_uses_report_date_as_authority() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": "volume_range_breakout", "signal_date": "20260612", "stock_id": "1111"},
            {"model_id": "volume_range_breakout", "signal_date": "20260615", "stock_id": "2222"},
            {"model_id": "volume_range_breakout", "signal_date": "20260615", "stock_id": "3333"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 2


def test_daily_signal_context_does_not_promote_stale_model_signal_date() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": "volume_range_breakout", "signal_date": "20260612", "stock_id": "1111"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 0


def test_pdf_volume_operation_uses_taxonomy_for_report_line_fallback() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1438",
                "stock_display": "1438 三地開發",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )
    inputs = {
        "stock_theme_taxonomy": pd.DataFrame(
            [
                {
                    "stock_id": "1438",
                    "stock_name": "三地開發",
                    "industry": "建材營造",
                    "report_line_memberships": "non_mainstream",
                    "mainstream_report_eligible": "False",
                    "non_mainstream_report_eligible": "True",
                }
            ]
        )
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "non_mainstream")

    assert "1438" not in set(mainstream["stock_id"].astype(str))
    assert "1438" in set(non_mainstream["stock_id"].astype(str))
    assert mainstream[mainstream["row_type"].eq("empty_state")]["stock_display"].tolist() == ["目前無資料"]


def test_pdf_volume_operation_does_not_guess_missing_taxonomy() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "9999",
                "stock_display": "9999 未分類",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            }
        ]
    )

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "non_mainstream")

    assert mainstream.empty
    assert non_mainstream.empty


def test_pdf_volume_operation_ignores_non_string_membership_values() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "6209",
                "stock_display": "6209 今國光",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "2",
                "stock_id": "6668",
                "stock_display": "6668 中揚光",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
        ]
    )
    inputs = {
        "stock_theme_taxonomy": pd.DataFrame(
            [
                {
                    "stock_id": "6209",
                    "report_line_memberships": float("nan"),
                    "taxonomy_report_line_memberships": 3.14,
                },
                {
                    "stock_id": "6668",
                    "report_line_memberships": "mainstream|non_mainstream",
                    "taxonomy_report_line_memberships": float("nan"),
                },
            ]
        )
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "non_mainstream")

    assert set(mainstream["stock_id"].astype(str)) == {"6668"}
    assert set(non_mainstream["stock_id"].astype(str)) == {"6668"}


def test_daily_pipeline_runs_volume_breakout_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/build_daily_volume_breakout_operation_section.py" in workflow
    assert "python scripts/validate_daily_volume_breakout_operation_section.py" in workflow


def test_daily_pdf_generator_does_not_read_research_operation_artifacts_directly() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    if not generator.exists():
        return
    source = generator.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "render_volume_range_breakout_operation_section" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source


def test_daily_pdf_generator_omits_obsolete_volume_breakout_explanatory_text() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    source = generator.read_text(encoding="utf-8", errors="replace")

    for token in [
        "放量攻擊模型操作參考",
        "以下僅呈現 daily adapter 已核准欄位",
        "PDF 不重新計算進場",
        "待確認列只作觀察",
    ]:
        assert token not in source
    assert source.count("if desc and model_id != VOLUME_BREAKOUT_MODEL_ID") == 2

    forbidden_text = "".join(pdf_integration_validator.FORBIDDEN_VOLUME_EXPLANATORY_TEXT)
    for token in [
        "不含今日的前20日最高價",
        "一般放量突破需收盤價",
        "鎖量漲停突破不要求量比",
        "放量攻擊模型操作參考",
        "PDF不重新計算進場",
    ]:
        assert token in forbidden_text


def test_pdf_chart_renderer_prefers_local_source_worktree_price_window(monkeypatch, tmp_path) -> None:
    calls: list[str] = []

    def fake_read_csv(path, **kwargs):
        calls.append(str(path))
        if str(path).startswith("https://"):
            raise AssertionError("raw GitHub price URL should not be used when local source data exists")
        return pd.DataFrame(
            [
                {"date": "2026-06-15", "open": "10", "high": "11", "low": "9", "close": "10.5", "volume": "1000"},
                {"date": "2026-06-16", "open": "10.5", "high": "12", "low": "10", "close": "11.5", "volume": "2000"},
                {"date": "2026-06-17", "open": "11.5", "high": "13", "low": "11", "close": "12.5", "volume": "3000"},
            ]
        )

    monkeypatch.setattr(pdf_generator, "read_csv", fake_read_csv)
    monkeypatch.setattr(pdf_generator, "LATEST", tmp_path / "output" / "latest")
    monkeypatch.setattr(pdf_generator, "CHARTS", tmp_path / "charts")
    monkeypatch.setitem(
        pdf_generator.REMOTE_README,
        "individual_stock_price_raw_url_template",
        "https://example.invalid/{stock_id}_price_window_180_latest.csv",
    )
    pdf_generator.CHARTS.mkdir(parents=True, exist_ok=True)

    chart = pdf_generator.plot_stock_chart("2330", "台積電", pd.Series(dtype=object))

    assert chart is not None
    assert chart.exists()
    assert calls == [
        str(tmp_path / "output" / "latest" / "individual_stock_price_windows" / "2330_price_window_180_latest.csv")
    ]


def test_daily_packet_builder_uses_daily_adapter_not_research_operation_artifacts() -> None:
    packet_builder = ROOT / "build_chatgpt_daily_report_packet.py"
    source = packet_builder.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "build_volume_operation_packet_lines" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "historical_pattern_operation_registry_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source


def operation_rows_for_limit_test(
    pdf_section: str,
    count: int,
    pdf_view: str = "highlight",
    stock_start: int = 5000,
) -> pd.DataFrame:
    rows = []
    for index in range(count):
        rows.append(
            {
                "model_id": "volume_range_breakout",
                "pdf_view": pdf_view,
                "pdf_section": pdf_section,
                "row_type": "data",
                "display_order": str(index + 1),
                "stock_id": str(stock_start + index),
                "stock_display": f"{stock_start + index} Test",
                "row_action_status": (
                    "confirmed_buy_candidate"
                    if pdf_section == "confirmed_operation"
                    else "pending_confirmation"
                    if pdf_section == "pending_confirmation"
                    else "active_operation"
                ),
                "buy_rank_eligible": "True" if pdf_section == "confirmed_operation" else "False",
            }
        )
    return pd.DataFrame(rows)


def test_pdf_operation_highlight_limits_are_section_specific() -> None:
    confirmed = operation_rows_for_limit_test("confirmed_operation", 12)
    pending = operation_rows_for_limit_test("pending_confirmation", 8)
    active = operation_rows_for_limit_test("active_operation", 7)

    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(confirmed, "highlight", "confirmed_operation")) == 10
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(pending, "highlight", "pending_confirmation")) == 5
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(active, "highlight", "active_operation")) == 5

    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(confirmed, "full", "confirmed_operation")) == 12
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(pending, "full", "pending_confirmation")) == 8
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(active, "full", "active_operation")) == 7


def test_pdf_operation_highlight_limits_apply_after_report_line_filter() -> None:
    rows = operation_rows_for_limit_test("pending_confirmation", 8)
    taxonomy = []
    for index, stock_id in enumerate(rows["stock_id"].astype(str).tolist()):
        taxonomy.append(
            {
                "stock_id": stock_id,
                "report_line_memberships": "mainstream" if index < 6 else "non_mainstream",
                "mainstream_report_eligible": "True" if index < 6 else "False",
                "non_mainstream_report_eligible": "False" if index < 6 else "True",
            }
        )
    inputs = {
        "volume_operation": rows,
        "stock_theme_taxonomy": pd.DataFrame(taxonomy),
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(
        pdf_generator.volume_operation_frame(inputs, "highlight", "pending_confirmation"),
        inputs,
        "mainstream",
    )
    mainstream = pdf_generator.limit_volume_operation_rows_for_pdf_view(
        mainstream,
        "highlight",
        "pending_confirmation",
    )
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(
        pdf_generator.volume_operation_frame(inputs, "highlight", "pending_confirmation"),
        inputs,
        "non_mainstream",
    )
    non_mainstream = pdf_generator.limit_volume_operation_rows_for_pdf_view(
        non_mainstream,
        "highlight",
        "pending_confirmation",
    )

    assert len(mainstream) == 5
    assert len(non_mainstream) == 2


def test_pdf_operation_renderer_uses_row_level_buy_eligibility(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1111",
                "stock_display": "1111 測試A",
                "trigger_zh": "隔日續強確認",
                "entry_basis_zh": "確認後下一交易日開盤",
                "entry_price_status_zh": "進場價待下一交易日開盤",
                "stop_basis_zh": "跌破 6/11 最低價 10.00",
                "exit_rule_zh": "第 10 個交易日收盤出場",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "avg_return_zh": "+21.67%",
                "median_return_zh": "+21.09%",
                "confidence_zh": "低",
                "operation_status_zh": "已確認",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "2222",
                "stock_display": "2222 測試B",
                "pending_age_zh": "D+1，剩 9 個交易日",
                "pending_group_zh": "D+0-D+1 等隔日續強",
                "pending_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
                "entry_basis_zh": "尚未確認，不列進場價",
                "stop_basis_zh": "跌破 6/11 最低價 20.00",
                "operation_status_zh": "待確認",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "operation_asof_date": "20260612",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "operation_status_zh": "操作中",
                "adapter_note_zh": "目前無操作中追蹤列。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        "highlight",
    )

    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    for token in [
        "放量攻擊模型操作參考",
        "以下僅呈現 daily adapter 已核准欄位",
        "PDF 不重新計算進場",
        "待確認列只作觀察",
    ]:
        assert token not in story_text

    assert len(captured_tables) == 3
    confirmed, pending, active = captured_tables
    assert confirmed[0] == [
        "排名",
        "股票",
        "確認方式",
        "買入方式",
        "進場價狀態",
        "停損價",
        "出場規則",
        "樣本數",
        "勝率",
        "平均報酬",
        "中位數報酬",
        "信心",
    ]
    assert confirmed[1][1] == "1111 測試A"
    assert "2222 測試B" not in " ".join(str(cell) for row in confirmed for cell in row)
    assert pending[0] == ["股票", "等待天數", "等待分組", "待確認條件", "進場價狀態", "停損基準", "狀態"]
    assert pending[1][0] == "2222 測試B"
    assert pending[1][4] == "尚未確認，不列進場價"
    assert active[0] == ["狀態", "股票 / 說明", "備註"]
    assert active[1][0] == "操作中"

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "buy_rank_eligible" not in visible
    assert "row_action_status" not in visible
    assert "confirmed_buy_candidate" not in visible


def test_pdf_operation_renderer_collapses_empty_state_rows(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "adapter_note_zh": "已確認操作：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "adapter_note_zh": "待確認：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "adapter_note_zh": "操作中：來源日期不符，今日不顯示舊操作列；不重新計算操作規則。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(story, {"volume_operation": rows}, "highlight")

    assert captured_tables == []
    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    assert "今日沒有可顯示的放量攻擊操作列。" in story_text
