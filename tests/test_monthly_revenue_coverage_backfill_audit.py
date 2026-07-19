from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_monthly_revenue_coverage_backfill_audit as coverage_builder  # noqa: E402
from build_monthly_revenue_coverage_backfill_audit import (  # noqa: E402
    AUDIT_ID,
    REQUIRED_MIN_HISTORY_MONTHS,
    build_detail,
    build_summary,
    summarize_history_scope,
    summarize_signal_scope,
)
from daily_snapshot_revision_utils import snapshot_file_sha256  # noqa: E402
from validate_monthly_revenue_coverage_backfill_audit import validate_detail, validate_summary  # noqa: E402
from backfill_monthly_revenue_history_from_mops_html import period_add_months  # noqa: E402


def history_row(stock_id: str = "2330", source_table_date: str = "20260617", revenue_period: str = "202605") -> dict[str, str]:
    return {
        "stock_id": stock_id,
        "stock_name": "TSMC",
        "revenue_period": revenue_period,
        "source_table_date": source_table_date,
        "revenue_numerical_anomaly_flag": "False",
    }


def signal_row(signal_date: str, model_id: str = "price_pullback_23ema", stock_id: str = "2330") -> dict[str, str]:
    return {
        "signal_date": signal_date,
        "model_id": model_id,
        "stock_id": stock_id,
        "stock_name": "TSMC",
    }


def test_coverage_audit_uses_source_table_date_asof_boundary() -> None:
    history = pd.DataFrame([history_row()])
    signals = pd.DataFrame(
        [
            signal_row("20260616"),
            signal_row("20260617"),
            signal_row("20260618", stock_id="9999"),
        ]
    )

    detail = build_detail(signals, history, "fixture_signals.csv")

    assert list(detail["coverage_status"]) == [
        "missing_asof_revenue_on_or_before_signal_date",
        "ready_asof_history_row",
        "missing_stock_in_monthly_revenue_history",
    ]
    assert detail.iloc[0]["research_join_allowed"] == "False"
    assert detail.iloc[1]["matched_revenue_period"] == "202605"
    assert detail.iloc[1]["research_join_allowed"] == "True"
    assert detail.iloc[1]["formal_model_revenue_gate_ready"] == "False"


def test_coverage_audit_marks_target_models_backfill_required_when_history_is_short() -> None:
    history = pd.DataFrame([history_row()])
    signals = pd.DataFrame(
        [
            signal_row("20260618", model_id="price_pullback_23ema"),
            signal_row("20260618", model_id="revenue_unreacted_range"),
        ]
    )
    detail = build_detail(signals, history, "fixture_signals.csv")
    summary = build_summary(history, detail, "fixture_signals.csv")

    targets = summary[summary["scope"].isin(["model:price_pullback_23ema", "model:revenue_unreacted_range"])]

    assert set(targets["formal_model_revenue_gate_ready"]) == {"False"}
    assert set(targets["backfill_required"]) == {"True"}
    assert all("history_period_count_lt_24" in reason for reason in targets["blocker_reason"])
    assert validate_summary(summary.astype(str)) == []
    assert validate_detail(detail.astype(str), summary.astype(str)) == []


def test_canonical_history_scope_checks_month_depth_not_signal_coverage() -> None:
    history = pd.DataFrame(
        [
            history_row(
                revenue_period=period_add_months("202401", offset),
                source_table_date=period_add_months("202401", offset + 1) + "17",
            )
            for offset in range(REQUIRED_MIN_HISTORY_MONTHS)
        ]
    )

    summary_row = summarize_history_scope(history)

    assert summary_row["formal_model_revenue_gate_ready"] == "True"
    assert summary_row["backfill_required"] == "False"
    assert summary_row["blocker_reason"] == "signal_scope_not_evaluated_in_history_row"


def test_validator_rejects_ready_scope_with_insufficient_months() -> None:
    history = pd.DataFrame([history_row()])
    detail = build_detail(pd.DataFrame([signal_row("20260618")]), history, "fixture_signals.csv")
    summary = pd.DataFrame(
        [
            summarize_signal_scope("daily_model_signal_log_all_models", detail, history, "fixture_signals.csv")
        ]
    )
    summary.loc[0, "formal_model_revenue_gate_ready"] = "True"
    summary.loc[0, "backfill_required"] = "False"

    errors = validate_summary(summary.astype(str))

    assert any("insufficient history months" in error for error in errors)
    assert summary.loc[0, "audit_id"] == AUDIT_ID


def test_signal_fallback_selects_same_day_manifest_max_revision(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(coverage_builder, "SIGNAL_LOG_CSV", tmp_path / "missing.csv")
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    r1 = snapshot_dir / "daily_candidate_model_signals_for_report_20260717.csv"
    pd.DataFrame([signal_row("20260717", stock_id="1111")]).to_csv(
        r1, index=False
    )
    r1_sha = snapshot_file_sha256(r1)
    staging = snapshot_dir / "signals-r2-staging.csv"
    pd.DataFrame([signal_row("20260717", stock_id="2222")]).to_csv(
        staging, index=False
    )
    r2_sha = snapshot_file_sha256(staging)
    r2 = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_20260717_r2_{r2_sha[:12]}.csv"
    )
    staging.rename(r2)
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": r1.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": r1_sha,
            },
            {
                "snapshot_report_date": "20260717",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": r1_sha,
                "revision_reason": "same_day_correction",
                "artifact_id": "model_signals_for_report",
                "snapshot_path": r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": r2_sha,
            },
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )

    signals, source = coverage_builder.load_signal_rows(
        snapshot_dir=snapshot_dir,
        repository_root=tmp_path,
    )

    assert signals["stock_id"].tolist() == ["2222"]
    assert signals["source_snapshot_file"].tolist() == [r2.as_posix()]
    assert source.endswith("daily_published_model_snapshot_manifest.csv")
