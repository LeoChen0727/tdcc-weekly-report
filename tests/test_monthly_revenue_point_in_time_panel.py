from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_monthly_revenue_point_in_time_panel import build_panel, parse_reported_release_date, parse_revenue_period  # noqa: E402
from daily_snapshot_revision_utils import snapshot_file_sha256  # noqa: E402
from validate_monthly_revenue_point_in_time_panel import validate_panel  # noqa: E402


def write_legacy_manifest(snapshot_dir: Path, path: Path, report_date: str) -> None:
    repository_root = snapshot_dir.parents[2]
    frame = pd.DataFrame(
        [
            {
                "snapshot_report_date": report_date,
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": path.relative_to(repository_root).as_posix(),
                "snapshot_sha256": snapshot_file_sha256(path),
            }
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )


def test_revenue_period_parser_treats_roc_year_month_as_period_not_release_date() -> None:
    assert parse_revenue_period("11505.0") == ("202605", "11505")
    assert parse_reported_release_date("11505.0") == ("", "not_actual_release_date_year_month")
    assert parse_reported_release_date("1150613") == ("20260613", "parsed_release_date")


def test_monthly_revenue_panel_builds_snapshot_observed_asof_rows(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    frame = pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505.0",
                "revenue_release_date": "11505.0",
                "revenue_yoy_pct": "39.6",
                "cumulative_yoy_pct": "42.1",
                "revenue_good_eps_unconfirmed_flag": "True",
            },
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505.0",
                "revenue_release_date": "11505.0",
                "revenue_yoy_pct": "39.6",
                "cumulative_yoy_pct": "42.1",
                "revenue_good_eps_unconfirmed_flag": "True",
            },
            {
                "stock_id": "9946",
                "stock_name": "三發地產",
                "revenue_period": "11505.0",
                "revenue_release_date": "1150613",
                "revenue_yoy_pct": "312.1",
                "cumulative_yoy_pct": "4373.5",
                "revenue_signal_type": "營建認列型 / 交屋認列型",
            },
        ]
    )
    snapshot_path = snapshot_dir / "all_candidates_20260615.csv"
    frame.to_csv(snapshot_path, index=False, encoding="utf-8-sig")
    write_legacy_manifest(snapshot_dir, snapshot_path, "20260615")

    panel = build_panel(snapshot_dir)

    assert validate_panel(panel.astype(str)) == []
    assert len(panel) == 2
    tsmc = panel[panel["stock_id"].eq("2330")].iloc[0]
    assert tsmc["observed_as_of_date"] == "20260615"
    assert tsmc["reported_release_date"] == ""
    assert tsmc["reported_release_date_status"] == "not_actual_release_date_year_month"
    assert tsmc["research_join_allowed"] == "True"
    assert tsmc["allowed_for_formal_historical_model_use"] == "False"
    assert tsmc["source_row_count"] == 2
    anomalous = panel[panel["stock_id"].eq("9946")].iloc[0]
    assert anomalous["revenue_numerical_anomaly_flag"] == "True"
    assert "cumulative_revenue_yoy_abs_ge_500pct" in anomalous["revenue_numerical_anomaly_reason"]


def test_monthly_revenue_validator_rejects_formal_use_claim(tmp_path: Path) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    frame = pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "台積電",
                "revenue_period": "11505",
                "revenue_yoy_pct": "39.6",
            }
        ]
    )
    snapshot_path = snapshot_dir / "all_candidates_20260615.csv"
    frame.to_csv(snapshot_path, index=False, encoding="utf-8-sig")
    write_legacy_manifest(snapshot_dir, snapshot_path, "20260615")
    panel = build_panel(snapshot_dir)
    panel.loc[0, "allowed_for_formal_historical_model_use"] = "True"

    errors = validate_panel(panel.astype(str))

    assert any("must not allow formal historical model use" in error for error in errors)


def test_monthly_revenue_panel_selects_same_day_manifest_max_revision(
    tmp_path: Path,
) -> None:
    snapshot_dir = tmp_path / "output" / "history" / "daily_model_snapshots"
    snapshot_dir.mkdir(parents=True)
    r1 = snapshot_dir / "all_candidates_20260615.csv"
    r2_staging = snapshot_dir / "all_candidates_r2_staging.csv"
    base = {
        "stock_id": "2330",
        "stock_name": "台積電",
        "revenue_period": "11505",
    }
    pd.DataFrame([{**base, "revenue_yoy_pct": "10"}]).to_csv(
        r1, index=False, encoding="utf-8-sig"
    )
    pd.DataFrame([{**base, "revenue_yoy_pct": "20"}]).to_csv(
        r2_staging, index=False, encoding="utf-8-sig"
    )
    r1_sha = snapshot_file_sha256(r1)
    r2_sha = snapshot_file_sha256(r2_staging)
    r2 = snapshot_dir / f"all_candidates_20260615_r2_{r2_sha[:12]}.csv"
    r2_staging.rename(r2)
    pd.DataFrame(
        [
            {
                "snapshot_report_date": "20260615",
                "snapshot_revision": "r1",
                "supersedes_snapshot_sha256": "",
                "revision_reason": "legacy_v1_manifest",
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": r1.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": r1_sha,
            },
            {
                "snapshot_report_date": "20260615",
                "snapshot_revision": "r2",
                "supersedes_snapshot_sha256": r1_sha,
                "revision_reason": "same_day_correction",
                "artifact_id": "all_candidates_source_rows",
                "snapshot_path": r2.relative_to(tmp_path).as_posix(),
                "snapshot_sha256": r2_sha,
            },
        ]
    ).to_csv(
        snapshot_dir / "daily_published_model_snapshot_manifest.csv", index=False
    )

    panel = build_panel(snapshot_dir)

    assert len(panel) == 1
    assert panel.iloc[0]["latest_revenue_yoy_pct"] == "20"
    assert panel.iloc[0]["source_snapshot_files"] == r2.as_posix()
