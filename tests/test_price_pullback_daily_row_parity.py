from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_daily_model_parameter_research import build_price_pullback_daily_row_parity_audit  # noqa: E402
from validate_price_pullback_daily_row_parity import validate_row_parity_frame  # noqa: E402


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def research_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "date": "20260615",
                "stock_id": "1234",
                "distance_ema23_pct": 1.0,
                "platform_low": 0.0,
                "short_platform_low": 0.0,
                "previous_20d_low": 0.0,
                "low_20": 0.0,
                "range_low_20d_prev": 0.0,
                "close": 101.0,
                "ema23": 100.0,
                "ma20": 100.0,
                "ema23_slope_pct": 0.1,
                "ema23_slope_5d_pct": 0.1,
                "ma5_turning_up_flag": False,
                "ma10_turning_up_flag": False,
            },
            {
                "date": "20260615",
                "stock_id": "5678",
                "distance_ema23_pct": 2.0,
                "platform_low": 0.0,
                "short_platform_low": 0.0,
                "previous_20d_low": 0.0,
                "low_20": 0.0,
                "range_low_20d_prev": 0.0,
                "close": 102.0,
                "ema23": 100.0,
                "ma20": 100.0,
                "ema23_slope_pct": 0.1,
                "ema23_slope_5d_pct": 0.1,
                "ma5_turning_up_flag": False,
                "ma10_turning_up_flag": False,
            },
        ]
    )


def test_price_pullback_daily_row_parity_audit_reports_bidirectional_gaps(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260615.csv",
        [
            {"model_id": "price_pullback_23ema", "stock_id": "1234"},
            {"model_id": "price_pullback_23ema", "stock_id": "9999"},
            {"model_id": "volume_range_breakout", "stock_id": "5678"},
        ],
    )
    write_csv(
        snapshot_dir / "daily_candidate_model_signals_for_report_20260616.csv",
        [{"model_id": "price_pullback_23ema", "stock_id": "1234"}],
    )

    audit = build_price_pullback_daily_row_parity_audit(
        research_frame(),
        snapshot_dir=snapshot_dir,
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    first = audit[audit["snapshot_report_date"].eq("20260615")].iloc[0]
    assert first["published_unique_stock_count"] == 2
    assert first["research_proxy_unique_stock_count"] == 2
    assert first["overlap_stock_count"] == 1
    assert first["published_not_in_proxy_rows"] == 1
    assert first["proxy_not_published_rows"] == 1
    assert first["parity_status"] == "blocked_not_exact_daily_row_parity"
    assert first["published_not_in_proxy_sample"] == "9999"
    assert first["proxy_not_published_sample"] == "5678"

    second = audit[audit["snapshot_report_date"].eq("20260616")].iloc[0]
    assert second["research_frame_has_date"] == "False"
    assert second["parity_status"] == "blocked_missing_research_frame_date"

    assert validate_row_parity_frame(audit) == []


def test_price_pullback_daily_row_parity_validator_rejects_inconsistent_pass() -> None:
    frame = pd.DataFrame(
        [
            {
                "generated_at": "2026-06-30 00:00:00 Asia/Taipei",
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260615",
                "research_frame_has_date": "True",
                "published_row_count": "2",
                "published_unique_stock_count": "2",
                "published_duplicate_stock_count": "0",
                "research_proxy_unique_stock_count": "3",
                "overlap_stock_count": "2",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "1",
                "published_proxy_coverage_pct": "100",
                "proxy_publish_precision_pct": "66.67",
                "published_not_in_proxy_sample": "",
                "proxy_not_published_sample": "5678",
                "parity_scope": "signal_date_stock_id",
                "parity_status": "exact_daily_row_parity_pass",
                "parity_blocker": "",
            }
        ]
    )

    errors = validate_row_parity_frame(frame)

    assert any("exact parity pass is inconsistent" in error for error in errors)
