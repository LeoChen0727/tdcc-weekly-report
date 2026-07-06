from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402
import build_volume_breakout_confirmed_operation_backtest as operation_backtest  # noqa: E402
import generate_chatgpt_side_daily_reports as pdf_generator  # noqa: E402
import validate_chatgpt_side_volume_operation_pdf_integration as pdf_integration_validator  # noqa: E402
import validate_daily_volume_breakout_operation_section as section_validator  # noqa: E402


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
    trigger_id: str = "next_day_break_signal_high_confirmed",
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
    signal_log = tmp_path / "output" / "history" / "daily_candidate_models" / "daily_candidate_model_signal_log.csv"
    price_dir = tmp_path / "data" / "stock_price_history"
    snapshot_dir.mkdir(parents=True)
    signal_log.parent.mkdir(parents=True)
    price_dir.mkdir(parents=True)
    pd.DataFrame(columns=["signal_date", "model_id", "stock_id", "stock_name"]).to_csv(signal_log, index=False)
    pd.DataFrame(price_rows).to_csv(price_dir / f"{stock_id}.csv", index=False)
    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "MODEL_SIGNAL_LOG_CSV", signal_log)
    monkeypatch.setattr(builder, "STOCK_PRICE_HISTORY_DIR", price_dir)
    return snapshot_dir


def build_rows_for_test(signals: pd.DataFrame, report_date: str, summary: pd.DataFrame) -> pd.DataFrame:
    rows, _audit = build_rows_and_audit_for_test(signals, report_date, summary)
    return rows


def build_rows_and_audit_for_test(
    signals: pd.DataFrame,
    report_date: str,
    summary: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, audit = builder.build_lifecycle_rows(
        signals,
        report_date,
        int(signals["stock_id"].nunique()) if not signals.empty else 0,
        approval_stub(),
        "2026-06-17 12:00:00 Asia/Taipei",
        summary,
    )
    return (
        pd.DataFrame(rows, columns=builder.OUTPUT_COLUMNS),
        pd.DataFrame(audit, columns=builder.EVIDENCE_AUDIT_COLUMNS),
    )


def output_row(**updates: str) -> dict[str, str]:
    row = {col: "" for col in builder.OUTPUT_COLUMNS}
    row.update(
        {
            "model_id": "volume_range_breakout",
            "pdf_view": "highlight",
            "pdf_section": "confirmed_operation",
            "row_type": "empty_state",
            "operation_asof_date": "20260615",
            "operation_source_date_status": "ready",
            "display_order": "0",
            "operation_status": "confirmed_operation",
            "row_action_status": "empty_state",
            "buy_rank_eligible": "False",
            "generated_at": "2026-06-16 08:00:00 Asia/Taipei",
        }
    )
    row.update(updates)
    return row


def audit_row(**updates: str) -> dict[str, str]:
    row = {col: "" for col in builder.EVIDENCE_AUDIT_COLUMNS}
    row.update(
        {
            "model_id": "volume_range_breakout",
            "operation_asof_date": "20260615",
            "stock_id": "1234",
            "signal_date": "20260615",
            "operation_lifecycle_state": "confirmed_operation",
            "audit_status": "candidate_evaluated",
            "included_in_daily_adapter": "False",
            "generated_at": "2026-06-16 08:00:00 Asia/Taipei",
        }
    )
    row.update(updates)
    return row


def test_build_reuses_existing_published_operation_snapshot(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    latest_dir.mkdir(parents=True)
    snapshot_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "main_price_date": "20260615",
                "report_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(latest_dir / "data_freshness_latest.csv", index=False)
    pd.DataFrame([volume_signal("9999", "20260615")]).to_csv(
        latest_dir / "daily_candidate_model_signals_for_report_latest.csv",
        index=False,
    )
    pd.DataFrame([{"model_id": "volume_range_breakout", **approval_stub()}]).to_csv(
        latest_dir / "approved_operation_patterns_latest.csv",
        index=False,
    )
    formal_summary().to_csv(latest_dir / "approved_formal_summary.csv", index=False)
    pd.DataFrame([output_row(stock_id="", stock_display="目前無資料")]).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_section_20260615.csv",
        index=False,
    )
    pd.DataFrame([audit_row()]).to_csv(
        snapshot_dir / "daily_volume_breakout_operation_evidence_audit_20260615.csv",
        index=False,
    )

    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", snapshot_dir)
    monkeypatch.setattr(builder, "DAILY_SIGNALS_CSV", latest_dir / "daily_candidate_model_signals_for_report_latest.csv")
    monkeypatch.setattr(builder, "APPROVAL_CSV", latest_dir / "approved_operation_patterns_latest.csv")
    monkeypatch.setattr(builder, "FORMAL_SUMMARY_CSV", latest_dir / "approved_formal_summary.csv")
    monkeypatch.setattr(builder, "DATA_FRESHNESS_CSV", latest_dir / "data_freshness_latest.csv")
    monkeypatch.delenv(builder.ALLOW_SNAPSHOT_REWRITE_ENV, raising=False)

    section, audit = builder.build()

    assert section["stock_id"].tolist() == [""]
    assert section["row_type"].tolist() == ["empty_state"]
    assert audit["stock_id"].tolist() == ["1234"]


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
    assert pending["stock_id"].tolist() == ["1234"]
    assert pending["pdf_view"].tolist() == ["full"]
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
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
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
    assert set(confirmed["selected_trigger_id"]) == {"next_day_break_signal_high_confirmed"}
    assert set(confirmed["confirmation_date"]) == {"20260617"}
    assert pending.empty
    assert backtest_lifecycle_state("1234", "20260616", "20260617") == "confirmed_operation"


def test_lifecycle_reads_published_signal_log_when_snapshot_is_missing(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    assert not (snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv").exists()
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        builder.MODEL_SIGNAL_LOG_CSV,
        index=False,
    )

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["stock_id"].tolist() == ["1234", "1234"]
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}


def test_lifecycle_does_not_read_selected_volume_history_as_adapter_source(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    assert not (snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv").exists()
    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty


def test_lifecycle_moves_prior_confirmed_signal_to_active(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
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
    assert set(active["selected_trigger_id"]) == {"next_day_break_signal_high_confirmed"}
    assert set(active["confirmation_date"]) == {"20260616"}
    assert backtest_lifecycle_state("1234", "20260615", "20260617") == "active_operation"


def test_active_operation_wins_over_new_confirmed_signal_for_same_stock(monkeypatch, tmp_path) -> None:
    patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "13", "low": "11.6", "close": "12.8", "volume": "1300"},
        ],
    )
    pd.DataFrame(
        [
            volume_signal("1234", "20260615", "1"),
            volume_signal("1234", "20260616", "2"),
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert active["stock_id"].tolist() == ["1234", "1234"]
    assert confirmed.empty
    assert set(active["signal_date"]) == {"20260615"}
    assert set(active["confirmation_date"]) == {"20260616"}
    assert set(active["operation_status"]) == {"active_operation"}
    assert set(active["row_action_status"]) == {"active_operation"}
    included = audit[audit["included_in_daily_adapter"].eq("True")]
    assert included[["stock_id", "signal_date"]].drop_duplicates().to_dict("records") == [
        {"stock_id": "1234", "signal_date": "20260615"}
    ]
    suppressed = audit[
        audit["audit_status"].eq("positive_row_evidence")
        & audit["stock_id"].eq("1234")
        & audit["signal_date"].eq("20260616")
    ]
    assert not suppressed.empty
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}


def test_active_operation_audits_new_pending_same_stock_suppression(monkeypatch, tmp_path) -> None:
    patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.5", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
            {"date": "20260617", "open": "11.7", "high": "12.5", "low": "11.6", "close": "12", "volume": "1100"},
        ],
    )
    pd.DataFrame(
        [
            volume_signal("1234", "20260615", "1"),
            volume_signal("1234", "20260617", "2"),
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    active = out[out["pdf_section"].eq("active_operation") & out["row_type"].eq("data")]
    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert set(active["signal_date"]) == {"20260615"}
    assert pending.empty
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed[["stock_id", "signal_date", "operation_lifecycle_state"]].to_dict("records") == [
        {
            "stock_id": "1234",
            "signal_date": "20260617",
            "operation_lifecycle_state": "pending_confirmation",
        }
    ]
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}
    assert set(suppressed["reason"]) == {"same_stock_lifecycle_suppressed_by_active_operation"}
    section_validator.validate_lifecycle_suppression_audit(audit)


def test_lifecycle_collapses_duplicate_signal_sources_without_last_row_overwrite(monkeypatch, tmp_path) -> None:
    patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame(
        [
            {**volume_signal("1234", "20260616"), "report_bucket": "mainstream", "model_rank": "1", "display_rank": ""},
            {**volume_signal("1234", "20260616"), "report_bucket": "non_mainstream", "model_rank": "99", "display_rank": ""},
        ]
    ).to_csv(builder.MODEL_SIGNAL_LOG_CSV, index=False)

    out = build_rows_for_test(pd.DataFrame(), "20260617", formal_summary())

    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert pending["stock_id"].tolist() == ["1234"]
    assert set(pending["display_order"]) == {"1"}
    assert set(pending["signal_date"]) == {"20260616"}


def test_lifecycle_audits_missing_report_date_price_gap(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260615", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260616", "open": "10.2", "high": "10.7", "low": "10.4", "close": "10.5", "volume": "900"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260615")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        index=False,
    )

    out, audit = build_rows_and_audit_for_test(pd.DataFrame(), "20260617", formal_summary())

    assert out.empty
    assert audit["audit_status"].tolist() == ["source_gap"]
    assert audit["operation_lifecycle_state"].tolist() == ["source_gap"]
    assert audit["included_in_daily_adapter"].tolist() == ["False"]
    assert audit["reason"].tolist() == ["operation_asof_date_missing_in_stock_price_history"]
    section_validator.validate_source_gap_audit(audit)


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
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
        ],
    )
    pd.DataFrame([volume_signal("1234", "20260616")]).to_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        index=False,
    )

    weak_summary = formal_summary()
    weak_summary["median_return"] = "-1"
    out = build_rows_for_test(pd.DataFrame(), "20260617", weak_summary)

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    unranked = out[out["pdf_section"].eq("confirmed_unranked_operation") & out["row_type"].eq("data")]
    assert confirmed.empty
    assert unranked["stock_id"].tolist() == ["1234"]
    assert unranked["pdf_view"].tolist() == ["full"]
    assert set(unranked["row_action_status"]) == {"confirmed_not_buy_ranked"}
    assert set(unranked["buy_rank_eligible"]) == {"False"}
    assert set(unranked["entry_price"]) == {""}
    assert set(unranked["stop_loss_price"]) == {""}
    assert set(unranked["evidence_match_status"]) == {"row_level_evidence_not_buy_ranked"}


def test_lifecycle_does_not_apply_tdcc_top10_evidence_to_no_tdcc_stock(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
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

    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    unranked = out[out["pdf_section"].eq("confirmed_unranked_operation") & out["row_type"].eq("data")]
    assert confirmed.empty
    assert unranked["stock_id"].tolist() == ["1234"]
    assert unranked["pdf_view"].tolist() == ["full"]
    assert set(unranked["row_action_status"]) == {"confirmed_not_buy_ranked"}
    assert set(unranked["buy_rank_eligible"]) == {"False"}
    assert set(unranked["evidence_match_status"]) == {"no_matching_row_level_evidence"}


def test_lifecycle_uses_exact_no_tdcc_row_level_evidence(monkeypatch, tmp_path) -> None:
    snapshot_dir = patch_lifecycle_sources(
        monkeypatch,
        tmp_path,
        "1234",
        [
            {"date": "20260616", "open": "10", "high": "11", "low": "9", "close": "10", "volume": "1000"},
            {"date": "20260617", "open": "10.6", "high": "12", "low": "10.9", "close": "11.5", "volume": "1200"},
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


def test_volume_operation_validator_rejects_unsynced_model_signal_log(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    history_dir = tmp_path / "output" / "history" / "daily_candidate_models"
    latest_dir.mkdir(parents=True)
    history_dir.mkdir(parents=True)

    freshness = latest_dir / "data_freshness_latest.csv"
    latest_signals = latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    signal_log = history_dir / "daily_candidate_model_signal_log.csv"

    pd.DataFrame(
        [
            {
                "main_price_date": "20260618",
                "report_ready": "True",
                "warrant_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(freshness, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": "volume_range_breakout",
            }
        ]
    ).to_csv(latest_signals, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "3002",
                "model_id": "volume_range_breakout",
            }
        ]
    ).to_csv(signal_log, index=False)

    monkeypatch.setattr(section_validator, "DATA_FRESHNESS_CSV", freshness)
    monkeypatch.setattr(section_validator, "DAILY_SIGNALS_CSV", latest_signals)
    monkeypatch.setattr(section_validator, "MODEL_SIGNAL_LOG_CSV", signal_log)

    section = pd.DataFrame([{"daily_signal_date": "20260618"}])
    with pytest.raises(SystemExit):
        section_validator.validate_latest_signal_log_sync(section)


def test_volume_operation_validator_allows_lineage_only_signal_log_rows(monkeypatch, tmp_path) -> None:
    latest_dir = tmp_path / "output" / "latest"
    history_dir = tmp_path / "output" / "history" / "daily_candidate_models"
    latest_dir.mkdir(parents=True)
    history_dir.mkdir(parents=True)

    freshness = latest_dir / "data_freshness_latest.csv"
    latest_signals = latest_dir / "daily_candidate_model_signals_for_report_latest.csv"
    signal_log = history_dir / "daily_candidate_model_signal_log.csv"

    pd.DataFrame(
        [
            {
                "main_price_date": "20260618",
                "report_ready": "True",
                "warrant_ready": "True",
                "daily_pdf_ready": "True",
            }
        ]
    ).to_csv(freshness, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": "volume_range_breakout",
            }
        ]
    ).to_csv(latest_signals, index=False)
    pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "report_bucket": "mainstream",
                "stock_id": "2061",
                "model_id": "volume_range_breakout",
            },
            {
                "signal_date": "20260618",
                "report_bucket": "",
                "stock_id": "5211",
                "model_id": "volume_range_breakout",
            },
        ]
    ).to_csv(signal_log, index=False)

    monkeypatch.setattr(section_validator, "DATA_FRESHNESS_CSV", freshness)
    monkeypatch.setattr(section_validator, "DAILY_SIGNALS_CSV", latest_signals)
    monkeypatch.setattr(section_validator, "MODEL_SIGNAL_LOG_CSV", signal_log)

    section = pd.DataFrame(
        [
            {
                "daily_signal_date": "20260618",
                "row_type": "data",
                "stock_id": "2061",
                "daily_volume_model_signal_count": "1",
            }
        ]
    )
    section_validator.validate_latest_signal_log_sync(section)


def test_volume_operation_builder_rejects_latest_signal_date_mismatch() -> None:
    signals = pd.DataFrame(
        [
            {
                "signal_date": "20260618",
                "stock_id": "2061",
                "model_id": "volume_range_breakout",
            }
        ]
    )

    with pytest.raises(RuntimeError, match="main_price_date=20260617"):
        builder.require_latest_signals_match_report_date(signals, "20260617")


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
    assert 'DAILY_HIGHLIGHT_DESCRIPTION_POLICY = "program_side_non_volume"' in source
    assert "should_render_highlight_model_description(model_id)" in source

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
        str(
            tmp_path
            / "output"
            / "latest"
            / "individual_stock_reports"
            / "price_windows"
            / "2330_price_window_180_latest.csv"
        )
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
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(pending, "highlight", "pending_confirmation")) == 8
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(active, "highlight", "active_operation")) == 5

    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(confirmed, "full", "confirmed_operation")) == 12
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(pending, "full", "pending_confirmation")) == 8
    assert len(pdf_generator.limit_volume_operation_rows_for_pdf_view(active, "full", "active_operation")) == 7


def test_pdf_operation_highlight_limits_apply_after_report_line_filter() -> None:
    rows = operation_rows_for_limit_test("active_operation", 8)
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
        pdf_generator.volume_operation_frame(inputs, "highlight", "active_operation"),
        inputs,
        "mainstream",
    )
    mainstream = pdf_generator.limit_volume_operation_rows_for_pdf_view(
        mainstream,
        "highlight",
        "active_operation",
    )
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(
        pdf_generator.volume_operation_frame(inputs, "highlight", "active_operation"),
        inputs,
        "non_mainstream",
    )
    non_mainstream = pdf_generator.limit_volume_operation_rows_for_pdf_view(
        non_mainstream,
        "highlight",
        "active_operation",
    )

    assert len(mainstream) == 5
    assert len(non_mainstream) == 2


def test_pdf_operation_renderer_uses_row_level_buy_eligibility(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
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
                "trigger_zh": "舊確認方式不可出現",
                "entry_basis_zh": "舊買入方式不可出現",
                "entry_price_status_zh": "舊進場價狀態不可出現",
                "stop_basis_zh": "舊停損基準不可出現",
                "exit_rule_zh": "舊出場規則不可出現",
                "selected_trigger_id": "next_day_break_signal_high_confirmed",
                "selected_confirmation_date": "20260612",
                "confirmation_date": "20260612",
                "entry_rule_id": "confirmation_next_open",
                "entry_price_basis": "next_open_after_confirmation",
                "entry_date": "",
                "entry_price": "",
                "stop_loss_rule_id": "signal_low_stop",
                "stop_loss_price": "10.00",
                "stop_loss_label_zh": "6/11最低點",
                "exit_rule_id": "signal_low_stop_or_fixed_10d_close",
                "planned_holding_days": "10",
                "operation_age_days": "1",
                "operation_score": "12.3",
                "tdcc_score": "1.0",
                "pattern_score": "2.0",
                "risk_penalty": "0",
                "final_rank_score": "88.8",
                "rank_reason_zh": "正式分數理由",
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
                "entry_basis_zh": "舊待確認進場欄位不可出現",
                "entry_price_status_zh": "舊待確認進場狀態不可出現",
                "stop_basis_zh": "舊待確認停損欄位不可出現",
                "operation_score": "4.0",
                "final_rank_score": "77.6",
                "rank_reason_zh": "待確認分數理由",
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

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "放量攻擊模型 - 本日可買 / 已確認買入候選"
    assert confirmed[1] == [
        "排名",
        "股票",
        "確認方式",
        "確認日",
        "買入方式",
        "停損基準",
        "出場規則",
        "操作 / 最終分數",
        "樣本數",
        "勝率",
        "中位數報酬",
        "排名原因",
    ]
    assert confirmed[2][1] == "1111 測試A"
    assert confirmed[2][2] == "隔日突破訊號高點"
    assert confirmed[2][3] == "2026/6/12"
    assert confirmed[2][4] == "確認後下一交易日開盤，尚未產生"
    assert confirmed[2][5] == "6/11最低點 10.00"
    assert confirmed[2][6] == "跌破停損基準，否則最多第 10 個交易日收盤"
    assert confirmed[2][7] == "操作 12.30 / 最終 88.80"
    assert confirmed[2][11] == "正式分數理由"
    assert "2222 測試B" not in " ".join(str(cell) for row in confirmed for cell in row)
    assert active[0][0] == "放量攻擊模型 - 操作中"
    assert active[1] == ["股票", "確認方式", "進場日 / 價", "停損基準", "持有天數", "出場規則", "操作 / 最終分數", "備註"]
    assert active[2][7] == "目前無操作中追蹤列"

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "2222 測試B" not in visible
    assert "待確認分數理由" not in visible
    assert "buy_rank_eligible" not in visible
    assert "row_action_status" not in visible
    assert "confirmed_buy_candidate" not in visible
    assert "舊確認方式不可出現" not in visible
    assert "舊買入方式不可出現" not in visible
    assert "舊進場價狀態不可出現" not in visible
    assert "舊停損基準不可出現" not in visible
    assert "舊出場規則不可出現" not in visible


def test_pdf_operation_renderer_full_shows_confirmed_unranked(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_unranked_operation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "3333",
                "stock_display": "3333 測試C",
                "selected_trigger_id": "next_day_break_signal_high_confirmed",
                "selected_confirmation_date": "20260612",
                "confirmation_date": "20260612",
                "rank_reason_zh": "已確認但證據未過門檻",
                "sample_size": "2098",
                "win_rate_zh": "38.13%",
                "median_return_zh": "-3.28%",
                "evidence_match_status": "row_level_evidence_not_buy_ranked",
                "row_action_status": "confirmed_not_buy_ranked",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "pending_confirmation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        "full",
    )

    assert len(captured_tables) == 4
    _, unranked, _, _ = captured_tables
    assert unranked[0][0] == "放量攻擊模型 - 已確認但未通過買入排名門檻"
    assert unranked[1] == ["股票", "確認方式", "確認日", "未列排名原因", "樣本數", "勝率", "中位數報酬", "證據狀態"]
    assert unranked[2][0] == "3333 測試C"
    assert unranked[2][3] == "已確認但證據未過門檻"
    assert unranked[2][7] == "歷史證據未過門檻"
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "confirmed_not_buy_ranked" not in visible
    assert "row_level_evidence_not_buy_ranked" not in visible


def test_pdf_operation_renderer_keeps_highlight_empty_tables(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
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

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "放量攻擊模型 - 本日可買 / 已確認買入候選"
    assert confirmed[1][:2] == ["排名", "股票"]
    assert confirmed[2][11] == "本日無股票推薦"
    assert active[0][0] == "放量攻擊模型 - 操作中"
    assert active[1][:2] == ["股票", "確認方式"]
    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    assert "本日可買 / 已確認買入候選" in story_text
    assert "操作中" in story_text
    assert "待確認" not in story_text
    assert "今日沒有可顯示的放量攻擊操作列。" not in story_text
def w_bottom_readiness(model_id: str, status: str = "pdf_integrated_daily_adapter") -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": model_id,
                "pdf_integration_status": status,
                "daily_adapter_sections": "confirmed_operation,active_operation",
            }
        ]
    )


def w_bottom_operation_row(
    model_id: str,
    pdf_section: str,
    row_type: str = "data",
    stock_id: str = "1111",
    stock_display: str = "1111 WBuy",
    report_line: str = "mainstream",
    row_action_status: str = "confirmed_buy_candidate",
    buy_rank_eligible: str = "True",
) -> dict[str, str]:
    return {
        "model_id": model_id,
        "model_name_zh": model_id,
        "pdf_view": "highlight",
        "pdf_section": pdf_section,
        "pdf_section_zh": pdf_section,
        "row_type": row_type,
        "operation_asof_date": "20260630",
        "operation_source_date_status": "current_report_date",
        "report_line": report_line,
        "report_line_memberships": "mainstream|non_mainstream" if report_line == "both" else report_line,
        "display_order": "1",
        "stock_id": stock_id,
        "stock_name": stock_display,
        "stock_display": stock_display,
        "operation_status": pdf_section,
        "operation_status_zh": pdf_section,
        "quality_status_zh": "adapter evidence",
        "row_action_status": row_action_status,
        "buy_rank_eligible": buy_rank_eligible,
        "signal_date": "20260630",
        "entry_rule_id": "test_entry_rule",
        "entry_basis_zh": "adapter entry basis",
        "entry_date": "20260701" if row_type == "data" else "",
        "entry_price": "10.5" if row_type == "data" else "",
        "stop_loss_rule_id": "test_stop_rule",
        "stop_loss_price": "9.8",
        "stop_loss_label_zh": "adapter stop",
        "exit_rule_id": "test_exit_rule",
        "exit_rule_zh": "adapter exit",
        "planned_holding_days": "20",
        "operation_age_days": "2",
        "sample_size": "31",
        "win_rate_zh": "58.06%",
        "median_return_zh": "6.24%",
        "pdf_note_zh": "model-owned adapter row",
        "adapter_note_zh": "PDF must not infer lifecycle",
    }


def price_pullback_operation_row(
    pdf_section: str,
    row_type: str = "data",
    stock_id: str = "3333",
    stock_display: str = "3333 PricePullback",
    operation_quality: str = "technical_strength",
    report_line: str = "mainstream",
    row_action_status: str = "confirmed_buy_candidate",
    buy_rank_eligible: str = "True",
) -> dict[str, str]:
    return {
        "model_id": pdf_generator.PRICE_PULLBACK_MODEL_ID,
        "model_name_zh": "23EMA回檔模型",
        "pdf_view": "highlight",
        "pdf_section": pdf_section,
        "pdf_section_zh": pdf_section,
        "row_type": row_type,
        "operation_asof_date": "20260703",
        "operation_source_date_status": "current_report_date",
        "report_line": report_line,
        "report_line_memberships": "mainstream|non_mainstream" if report_line == "both" else report_line,
        "display_order": "1",
        "stock_id": stock_id,
        "stock_name": stock_display,
        "stock_display": stock_display,
        "operation_status": pdf_section,
        "operation_status_zh": pdf_section,
        "operation_quality": operation_quality,
        "operation_quality_zh": "技術強勢" if operation_quality == "technical_strength" else "基礎",
        "row_action_status": row_action_status,
        "buy_rank_eligible": buy_rank_eligible,
        "signal_date": "20260703",
        "entry_rule_id": "signal_date_next_open",
        "entry_basis_zh": "本表股票為23EMA回檔模型通過候選，隔日開盤買入。",
        "stop_loss_rule_id": "sustained_close_below_lower_ma20_ema23_4pct_4d",
        "stop_basis_zh": "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。",
        "exit_rule_id": "close_prev20_high_break_next_open",
        "exit_rule_zh": "收盤突破訊號日前20日高點後，隔日開盤賣出。",
        "planned_holding_days": "20",
        "operation_age_days": "2" if row_type == "data" else "",
        "sample_size": "1160",
        "win_rate_zh": "66.03%",
        "neutral_rate_zh": "5.60%",
        "failure_rate_zh": "28.36%",
        "avg_return_zh": "+2.90%",
        "technical_package_win_rate_zh": "75.54%",
        "technical_package_neutral_rate_zh": "3.52%",
        "technical_package_failure_rate_zh": "20.95%",
        "technical_package_avg_return_zh": "+2.96%",
        "rank_reason_zh": "技術強勢；20日漲幅0~25%、TDCC高門檻增加、OBV站上MA20",
        "risk_tags_zh": "",
    }


def test_price_pullback_pdf_renderer_uses_model_owned_adapter_rows(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    operation_rows = pd.DataFrame(
        [
            price_pullback_operation_row("confirmed_operation"),
            price_pullback_operation_row(
                "active_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
        ]
    )
    candidate_signals = pd.DataFrame(
        [
            {
                "model_id": pdf_generator.PRICE_PULLBACK_MODEL_ID,
                "stock_id": "9999",
                "stock_name": "CandidateLeak",
                "report_line": "mainstream",
                "same_model_repeat_status_zh": "新上榜",
            }
        ]
    )

    story: list = []
    rendered = pdf_generator.render_model_operation_section_if_applicable(
        story,
        {
            "model_readiness": w_bottom_readiness(pdf_generator.PRICE_PULLBACK_MODEL_ID),
            pdf_generator.PRICE_PULLBACK_OPERATION_INPUT_KEY: operation_rows,
            "model_signals": candidate_signals,
        },
        pdf_generator.PRICE_PULLBACK_MODEL_ID,
        "highlight",
        "mainstream",
    )

    assert rendered is True
    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "23EMA回檔模型 - 本日可買 / 已確認買入候選"
    assert confirmed[1] == ["股票", "操作品質", "訊號日", "買入", "賣出", "停損", "勝/和/敗/報酬", "理由 / 風險"]
    assert "排名" not in confirmed[1]
    assert confirmed[2][0] == "3333 PricePullback"
    assert confirmed[2][1] == "技術強勢"
    assert "隔日開盤買入" in confirmed[2][3]
    assert "隔日開盤賣出" in confirmed[2][4]
    assert "下一個交易日" not in confirmed[2][3]
    assert "下一個交易日" not in confirmed[2][4]
    assert "66.03%" in confirmed[2][6]
    assert "75.54%" in confirmed[2][6]
    assert active[0][0] == "23EMA回檔模型 - 操作中"
    assert active[2][6] == pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "9999" not in visible
    assert "CandidateLeak" not in visible


def test_w_bottom_pdf_renderer_uses_model_owned_adapter_rows(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    operation_rows = pd.DataFrame(
        [
            w_bottom_operation_row(model_id, "confirmed_operation", stock_id="1111", stock_display="1111 WBuy"),
            w_bottom_operation_row(
                model_id,
                "active_operation",
                stock_id="2222",
                stock_display="2222 WActive",
                row_action_status="active_tracking",
                buy_rank_eligible="False",
            ),
        ]
    )
    candidate_signals = pd.DataFrame(
        [
            {
                "model_id": model_id,
                "stock_id": "9999",
                "stock_name": "CandidateLeak",
                "report_line": "mainstream",
                "same_model_repeat_status_zh": "新上榜",
            }
        ]
    )

    story: list = []
    pdf_generator.render_w_bottom_operation_section(
        story,
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": operation_rows,
            "model_signals": candidate_signals,
        },
        model_id,
        "highlight",
        "mainstream",
    )

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "W底右側模型 - 本日可買 / 已確認買入候選"
    assert confirmed[2][1] == "1111 WBuy"
    assert active[0][0] == "W底右側模型 - 操作中"
    assert active[2][0] == "2222 WActive"
    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "9999" not in visible
    assert "CandidateLeak" not in visible
    story_text = "\n".join(
        flowable.getPlainText()
        for flowable in story
        if hasattr(flowable, "getPlainText")
    )
    assert pdf_generator.OPERATION_CONFIRMED_BUY_TABLE_TITLE in story_text
    assert pdf_generator.OPERATION_ACTIVE_TABLE_TITLE in story_text
    assert "新上榜" not in story_text
    assert "重複上榜" not in story_text


def test_w_bottom_pdf_renderer_sanitizes_pending_entry_price_text(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    confirmed = w_bottom_operation_row(model_id, "confirmed_operation")
    confirmed.update(
        {
            "entry_basis_zh": "",
            "entry_rule_id": "",
            "entry_price_status_zh": "下一個交易日開盤價待確認",
            "entry_date": "",
            "entry_price": "",
        }
    )
    active_empty = w_bottom_operation_row(
        model_id,
        "active_operation",
        row_type="empty_state",
        stock_id="",
        stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
        report_line="both",
        row_action_status="empty_state",
        buy_rank_eligible="False",
    )

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_right_side_operation": pd.DataFrame([confirmed, active_empty]),
        },
        model_id,
        "highlight",
        "mainstream",
    )

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "待確認" not in visible
    assert "確認價未定" in visible


def test_w_bottom_pdf_renderer_fails_closed_without_integrated_readiness() -> None:
    model_id = pdf_generator.W_BOTTOM_RIGHT_SIDE_MODEL_ID
    operation_rows = pd.DataFrame([w_bottom_operation_row(model_id, "confirmed_operation")])

    with pytest.raises(RuntimeError, match="pdf_integrated_daily_adapter"):
        pdf_generator.render_w_bottom_operation_section(
            [],
            {
                "model_readiness": w_bottom_readiness(model_id, status="pending_pdf_renderer"),
                "w_bottom_right_side_operation": operation_rows,
            },
            model_id,
            "highlight",
            "mainstream",
        )


def test_w_bottom_pdf_renderer_keeps_model_owned_empty_state_inside_tables(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None, **_kwargs):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    model_id = pdf_generator.W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID
    operation_rows = pd.DataFrame(
        [
            w_bottom_operation_row(
                model_id,
                "confirmed_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.MODEL_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
            w_bottom_operation_row(
                model_id,
                "active_operation",
                row_type="empty_state",
                stock_id="",
                stock_display=pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT,
                report_line="both",
                row_action_status="empty_state",
                buy_rank_eligible="False",
            ),
        ]
    )

    pdf_generator.render_w_bottom_operation_section(
        [],
        {
            "model_readiness": w_bottom_readiness(model_id),
            "w_bottom_neckline_operation": operation_rows,
        },
        model_id,
        "highlight",
        "mainstream",
    )

    assert len(captured_tables) == 2
    confirmed, active = captured_tables
    assert confirmed[0][0] == "W底頸線帶量突破確認模型 - 本日可買 / 已確認買入候選"
    assert confirmed[2][-1] == pdf_generator.MODEL_EMPTY_STATE_TEXT
    assert active[0][0] == "W底頸線帶量突破確認模型 - 操作中"
    assert active[2][-1] == pdf_generator.OPERATION_ACTIVE_EMPTY_STATE_TEXT
