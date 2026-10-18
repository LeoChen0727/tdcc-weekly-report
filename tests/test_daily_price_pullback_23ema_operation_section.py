from __future__ import annotations

from pathlib import Path
import hashlib
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_price_pullback_23ema_operation_section as builder  # noqa: E402
import validate_daily_operation_adapter_protected_fields as protected_fields  # noqa: E402
import validate_daily_price_pullback_23ema_operation_section as validator  # noqa: E402


@pytest.fixture(autouse=True)
def isolated_confirmation_history(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(builder, "ROOT", tmp_path)
    monkeypatch.setattr(builder, "MODEL_SNAPSHOT_DIR", tmp_path / "output/history/daily_model_snapshots")


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": builder.MODEL_ID,
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_module_id": builder.OPERATION_MODULE_ID,
                "approval_version": builder.APPROVAL_VERSION,
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": builder.BUY_FILTER_ID,
                "approval_note_zh": "approved",
            }
        ]
    )


def signal_row(signal_date: str = "20260703") -> dict[str, str]:
    return {
        "model_id": builder.MODEL_ID,
        "model_name_zh": builder.MODEL_NAME_ZH,
        "signal_date": signal_date,
        "stock_id": "1234",
        "stock_name": "TestCo",
        "report_bucket": "mainstream",
        "report_line": "mainstream",
        "report_line_memberships": "mainstream",
        "price_pullback_operation_quality": "technical_strength",
        "price_pullback_reason_tags": "base_v1|technical_strength_rsi60_macd_positive",
        "price_pullback_risk_tags": "",
        "model_score": "70",
        "model_rank": "3",
        "display_rank": "4",
        "model_rank_overall": "5",
    }


def save_original_confirmation(signal_date: str = "20260703", **changes: str) -> dict[str, str]:
    source = signal_row(signal_date)
    source.update(changes)
    rows = builder.confirmed_rows(pd.Series(source), approval_frame().iloc[0].to_dict(), signal_date, 1, "original_generation")
    payload = pd.DataFrame(rows).to_csv(index=False, lineterminator="\n").encode("utf-8")
    sha = hashlib.sha256(payload).hexdigest()
    relative = Path("output/history/daily_model_snapshots") / f"daily_price_pullback_23ema_operation_section_{signal_date}_r1_{sha[:12]}.csv"
    path = builder.ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    entry = {
        "snapshot_report_date": signal_date, "artifact_id": "price_pullback_23ema_operation_section",
        "snapshot_path": relative.as_posix(), "snapshot_sha256": sha,
        "snapshot_revision": "r1", "supersedes_snapshot_sha256": "", "revision_reason": "original_confirmed_rows",
    }
    pd.DataFrame([entry]).to_csv(builder.MODEL_SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv", index=False)
    return entry


def active_price() -> pd.DataFrame:
    return pd.DataFrame([
        {"date": date, "open": opening, "high": high, "low": 9.7, "close": close}
        for date, opening, high, close in [
            ("20260701", 10.0, 12.0, 10.0), ("20260702", 10.0, 11.8, 10.1),
            ("20260703", 10.0, 10.5, 10.0), ("20260706", 10.1, 10.6, 10.2),
            ("20260707", 10.2, 10.7, 10.3), ("20260708", 10.3, 10.8, 10.4),
        ]
    ])


def test_current_price_pullback_signal_becomes_confirmed_operation_rows(monkeypatch) -> None:
    section, audit = builder.build_section(
        pd.DataFrame([signal_row("20260703")]),
        approval_frame(),
        "20260703",
        "2026-07-03 18:00:00 Asia/Taipei",
    )

    confirmed = section[
        section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")
    ]
    assert set(confirmed["pdf_view"]) == {"highlight", "full"}
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["operation_quality"]) == {"technical_strength"}
    assert set(confirmed["row_metric_status"]) == {"ready"}
    assert set(confirmed["row_metric_scope"]) == {"exact_combo"}
    assert set(confirmed["row_metric_win_rate_zh"]) == {builder.TECHNICAL_WIN_RATE}
    assert set(confirmed["row_metric_avg_return_zh"]) == {builder.TECHNICAL_AVG_RETURN}
    assert set(confirmed["entry_rule_id"]) == {builder.ENTRY_RULE_ID}
    assert set(confirmed["entry_basis_zh"]) == {builder.ENTRY_BASIS_ZH}
    assert set(confirmed["exit_rule_id"]) == {builder.EXIT_RULE_ID}
    assert set(confirmed["exit_rule_zh"]) == {builder.EXIT_RULE_ZH}
    assert set(confirmed["stop_basis_zh"]) == {builder.STOP_BASIS_ZH}
    assert "隔日開盤買入" in builder.ENTRY_BASIS_ZH
    assert "隔日開盤賣出" in builder.EXIT_RULE_ZH
    assert "較低者的4%" in builder.STOP_BASIS_ZH
    assert "下一個交易日" not in (
        builder.ENTRY_BASIS_ZH + builder.EXIT_RULE_ZH + builder.STOP_BASIS_ZH
    )
    assert "active_operation" in set(section["pdf_section"])
    assert not audit.empty


def test_prior_buy_ranked_confirmed_snapshot_becomes_active_tracking_row(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260701", "open": 10.0, "high": 12.0, "low": 9.8, "close": 10.0},
            {"date": "20260702", "open": 10.0, "high": 11.8, "low": 9.7, "close": 10.1},
            {"date": "20260703", "open": 10.0, "high": 10.5, "low": 9.9, "close": 10.0},
            {"date": "20260706", "open": 10.1, "high": 10.6, "low": 9.9, "close": 10.2},
            {"date": "20260707", "open": 10.2, "high": 10.7, "low": 10.0, "close": 10.3},
            {"date": "20260708", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.4},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    entry = save_original_confirmation()

    section, audit = builder.build_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        "20260708",
        "2026-07-08 18:00:00 Asia/Taipei",
    )

    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert set(active["pdf_view"]) == {"highlight", "full"}
    assert set(active["row_action_status"]) == {"active_operation"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["entry_date"]) == {"20260706"}
    assert set(active["model_rank"]) == {"3"}
    assert set(active["display_rank"]) == {"4"}
    assert set(active["model_rank_overall"]) == {"5"}
    assert set(active["confirmation_source_sha256"]) == {entry["snapshot_sha256"]}
    assert set(active["confirmation_snapshot_revision"]) == {"r1"}
    assert "active_operation" in set(audit["audit_status"])


def test_price_pullback_supported_states_pass_protected_contract(monkeypatch) -> None:
    confirmed_section, _ = builder.build_section(
        pd.DataFrame([signal_row("20260703")]),
        approval_frame(),
        "20260703",
        "2026-07-03 18:00:00 Asia/Taipei",
    )

    price = pd.DataFrame(
        [
            {"date": "20260701", "open": 10.0, "high": 12.0, "low": 9.8, "close": 10.0},
            {"date": "20260702", "open": 10.0, "high": 11.8, "low": 9.7, "close": 10.1},
            {"date": "20260703", "open": 10.0, "high": 10.5, "low": 9.9, "close": 10.0},
            {"date": "20260706", "open": 10.1, "high": 10.6, "low": 9.9, "close": 10.2},
            {"date": "20260707", "open": 10.2, "high": 10.7, "low": 10.0, "close": 10.3},
            {"date": "20260708", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.4},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    save_original_confirmation()
    active_section, _ = builder.build_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        "20260708",
        "2026-07-08 18:00:00 Asia/Taipei",
    )

    combined = pd.concat([confirmed_section, active_section], ignore_index=True)
    assert protected_fields.validate_adapter_frame(
        combined,
        builder.MODEL_ID,
        required_states={"confirmed", "active", "empty"},
    ) == []
    assert validator.validate_section(confirmed_section) == []
    assert validator.validate_section(active_section) == []


def test_raw_old_signal_alone_never_creates_active_without_original_confirmation(monkeypatch) -> None:
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: pytest.fail("raw old signal must not enter lifecycle"))
    section, audit = builder.build_section(pd.DataFrame([signal_row()]), approval_frame(), "20260708", "fixture")
    assert section[section["row_type"].eq("data")].empty
    assert "blocked_missing_original_confirmation" in set(audit["audit_status"])
    assert "missing_confirmation_manifest" in set(audit["reason"])


@pytest.mark.parametrize("field", ["model_rank", "display_rank", "model_rank_overall"])
def test_current_missing_rank_is_not_replaced_with_display_order(field) -> None:
    signal = signal_row()
    signal[field] = ""
    signal["display_order"] = "1"
    with pytest.raises(RuntimeError, match="missing original model/display rank"):
        builder.build_section(pd.DataFrame([signal]), approval_frame(), "20260703", "fixture")


def test_original_rank_and_content_stay_frozen_when_current_signal_changes(monkeypatch) -> None:
    save_original_confirmation()
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: active_price())
    current = signal_row("20260708")
    current.update(model_rank="1", display_rank="1", model_rank_overall="1", model_score="99", price_pullback_operation_quality="base")
    section, audit = builder.build_section(pd.DataFrame([current]), approval_frame(), "20260708", "fixture")
    data = section[section["row_type"].eq("data")]
    assert set(data["pdf_section"]) == {"active_operation"}
    assert set(data["model_rank"]) == {"3"}
    assert set(data["display_rank"]) == {"4"}
    assert set(data["model_score"]) == {"70"}
    assert set(data["operation_quality"]) == {"technical_strength"}
    assert "suppressed_existing_active_position" in set(audit["audit_status"])


def test_different_report_line_is_not_suppressed_by_existing_active(monkeypatch) -> None:
    save_original_confirmation()
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: active_price())
    current = signal_row("20260708")
    current.update(report_bucket="non_mainstream", report_line="non_mainstream")
    section, _ = builder.build_section(pd.DataFrame([current]), approval_frame(), "20260708", "fixture")
    data = section[section["row_type"].eq("data")]
    assert set(data[data["pdf_section"].eq("active_operation")]["report_line"]) == {"mainstream"}
    assert set(data[data["pdf_section"].eq("confirmed_operation")]["report_line"]) == {"non_mainstream"}


def test_new_confirmation_allowed_after_prior_position_exits(monkeypatch) -> None:
    save_original_confirmation()
    price = active_price()
    price.loc[price["date"].eq("20260707"), "close"] = 12.5
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    section, audit = builder.build_section(pd.DataFrame([signal_row("20260708")]), approval_frame(), "20260708", "fixture")
    data = section[section["row_type"].eq("data")]
    assert set(data["pdf_section"]) == {"confirmed_operation"}
    assert "exited" in set(audit["operation_lifecycle_state"])


def test_active_rows_reject_unranked_source_before_price_replay(monkeypatch) -> None:
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: pytest.fail("unranked rows must not replay lifecycle"))
    raw = signal_row()
    raw.update(pdf_section="confirmed_unranked_operation", buy_rank_eligible="False")
    rows, audit = builder.active_rows(pd.Series(raw), {}, "20260708", 0, "fixture")
    assert rows == []
    assert audit["reason"] == "original_buy_ranked_confirmation_required"


def test_protected_fields_are_written_once_by_adapter_constructors() -> None:
    assert protected_fields._validate_producer_ast(ROOT / "scripts/build_daily_price_pullback_23ema_operation_section.py") == []


def test_daily_full_pipeline_runs_price_pullback_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    assert "python scripts/build_daily_price_pullback_23ema_operation_section.py" in workflow
    assert "python scripts/validate_daily_price_pullback_23ema_operation_section.py" in workflow
    for name in [
        "daily_price_pullback_23ema_operation_section_latest.csv",
        "daily_price_pullback_23ema_operation_section_latest.md",
        "daily_price_pullback_23ema_operation_evidence_audit_latest.csv",
        "daily_price_pullback_23ema_operation_evidence_audit_latest.md",
    ]:
        assert f"cp output/latest/{name} docs/latest/{name}" in workflow
    assert "git add docs/latest/daily_price_pullback_23ema_operation_*_latest.*" in workflow
