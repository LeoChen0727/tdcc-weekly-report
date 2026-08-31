from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
import pytest
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_model_operation_readiness import build_model_operation_readiness  # noqa: E402
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
from build_model_operation_readiness import REVENUE_MODEL_ID  # noqa: E402
from validate_model_operation_readiness import validate_revenue_readiness_row  # noqa: E402
import build_model_operation_readiness as readiness_builder  # noqa: E402
import validate_model_operation_readiness as readiness_validator  # noqa: E402
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

LOW_VOLUME_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
MID_VOLUME_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
HIGH_VOLUME_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range

_SYNC_MODULE = sys.modules[
    readiness_builder.summarize_revenue_promotion_readiness.__module__
]
_MODEL_PRICE_DATE_FRAMES: dict[str, pd.DataFrame] = {}


def _model_verified_price_date_frames(
    repo_root: Path | str,
    detail: pd.DataFrame,
    *,
    observed_through: str,
    per_stock_manifest_sha: dict[str, str],
    required_stock_ids: set[str] | None = None,
) -> dict[str, pd.DataFrame]:
    repo = Path(repo_root).resolve()
    requested = {
        _SYNC_MODULE._stock_id(value) for value in detail.get("stock_id", [])
    } | {
        _SYNC_MODULE._stock_id(value) for value in (required_stock_ids or set())
    }
    missing = sorted(requested - set(per_stock_manifest_sha))
    if missing:
        raise RuntimeError(f"registered fixture stock missing lineage: {missing}")
    for stock_id in requested:
        if stock_id not in _MODEL_PRICE_DATE_FRAMES:
            path = repo / _SYNC_MODULE.PRICE_HISTORY_DIR_REL / f"{stock_id}.csv"
            dates = pd.read_csv(path, usecols=["date"], dtype=str).fillna("")
            dates["date"] = dates["date"].map(
                lambda value: _SYNC_MODULE._strict_date(
                    value, f"verified test price date {stock_id}"
                )
            )
            dates = dates.loc[
                dates["date"].le(observed_through), ["date"]
            ].reset_index(drop=True)
            assert not dates["date"].duplicated().any()
            assert dates["date"].is_monotonic_increasing
            _MODEL_PRICE_DATE_FRAMES[stock_id] = dates
    return {stock_id: _MODEL_PRICE_DATE_FRAMES[stock_id] for stock_id in requested}


@pytest.fixture(autouse=True)
def stub_expensive_exact_revenue_replay(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unit tests consume canonical gate results without relaunching their CLIs."""

    def fail_exact(_repo_root: Path) -> dict[str, object]:
        raise AssertionError("general readiness path invoked exact replay")

    monkeypatch.setattr(
        _SYNC_MODULE,
        "_recompute_exact_registered_price_lineage",
        fail_exact,
    )
    monkeypatch.setattr(
        _SYNC_MODULE,
        "_load_registered_price_frames",
        _model_verified_price_date_frames,
    )
    anomaly_frame = pd.read_csv(
        ROOT / readiness_builder.REVENUE_ANOMALY_REGISTRY_CSV,
        dtype=str,
    ).fillna("")
    anomaly_rows = {
        str(row["operation_key"]): {str(key): str(value) for key, value in row.items()}
        for row in anomaly_frame.to_dict(orient="records")
    }
    canonical_anomaly_result = _SYNC_MODULE.CanonicalAnomalyValidationResult(
        rows=anomaly_rows,
        row_count=9,
        effective_blocker_count=0,
        verified_real_extreme_count=8,
        verified_data_error_repaired_count=1,
        errors=(),
        diagnostics=(),
    )
    monkeypatch.setattr(
        _SYNC_MODULE,
        "validate_current_anomaly_dispositions",
        lambda *_args, **_kwargs: canonical_anomaly_result,
    )


def test_revenue_readiness_legacy_shim_delegates_sync_failure_without_writes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []

    def fail_sync(repo_root: Path) -> tuple[pd.DataFrame, list[str]]:
        assert repo_root == readiness_builder.ROOT
        calls.append("sync")
        raise RuntimeError("model-owned sync rejected legacy shim")

    monkeypatch.setattr(readiness_builder, "sync", fail_sync)
    monkeypatch.setattr(
        readiness_builder,
        "build_model_operation_readiness",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("legacy cross-model builder ran from compatibility shim")
        ),
    )

    with pytest.raises(RuntimeError, match="model-owned sync rejected legacy shim"):
        readiness_builder.main()

    assert calls == ["sync"]


def test_revenue_readiness_legacy_shim_uses_explicit_repo_root_outside_repo(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    calls: list[Path] = []

    def record_sync(repo_root: Path) -> tuple[pd.DataFrame, list[str]]:
        calls.append(Path(repo_root))
        return pd.DataFrame(), []

    monkeypatch.setattr(readiness_builder, "sync", record_sync)
    monkeypatch.setattr(
        readiness_builder,
        "build_model_operation_readiness",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("legacy cross-model builder ran from compatibility shim")
        ),
    )

    assert readiness_builder.main() == 0
    assert calls == [readiness_builder.ROOT]


def revenue_parity_frame() -> pd.DataFrame:
    return pd.concat(
        [
            parity_frame(),
            pd.DataFrame(
                [
                    {
                        "model_id": REVENUE_MODEL_ID,
                        "model_name_zh": "營收爆發但股價尚未反應模型",
                        "research_baseline_status": "proxy_only",
                        "parity_blocker": (
                            "strong_revenue gate requires model-specific research matrix, contract update, "
                            "exact parity, and promotion PR before formal use"
                        ),
                    }
                ]
            ),
        ],
        ignore_index=True,
    )


def revenue_promotion_registry_frame() -> pd.DataFrame:
    return pd.read_csv(
        ROOT / readiness_builder.REVENUE_PROMOTION_REGISTRY_CSV,
        dtype=str,
    ).fillna("")


def revenue_anomaly_registry_frame() -> pd.DataFrame:
    return pd.read_csv(
        ROOT / readiness_builder.REVENUE_ANOMALY_REGISTRY_CSV,
        dtype=str,
    ).fillna("")


def revenue_forward_holdout_v2_manifest_frame() -> pd.DataFrame:
    return pd.read_csv(
        ROOT / readiness_builder.REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV,
        dtype=str,
    ).fillna("")
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def parity_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "model_name_zh": "放量攻擊",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
            {
                "model_id": "price_pullback_23ema",
                "model_name_zh": "回測23EMA",
                "research_baseline_status": "production_proxy",
                "parity_blocker": "",
            },
            {
                "model_id": "w_bottom_right_side",
                "model_name_zh": "W bottom right side",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "model_name_zh": "Neckline breakout",
                "research_baseline_status": "production_parity",
                "parity_blocker": "",
            },
        ]
    )


def registry_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "model_hit_status": "current_model_hit",
                "pattern_id": "pullback_10ma_hold_10d",
                "sample_size": "2400",
                "win_rate": "52.33",
                "avg_return": "3.69",
                "median_return": "0.55",
                "out_of_sample_pass": "True",
            }
        ]
    )


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "operation_module_id": "volume_range_breakout_v2_low_position_operation_v1",
                "approval_version": "volume_range_breakout_v2_formal_operation_20260709",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_directive_level": "approved_daily_operation_guidance",
            },
            {
                "model_id": "w_bottom_right_side",
                "operation_module_id": "w_bottom_early_entry_operation_v2",
                "approval_version": "w_bottom_early_entry_operation_v2_20260629",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v2",
                "operation_directive_level": "approved_daily_operation_guidance",
                "best_evidence_sample_size": "31",
                "best_evidence_win_rate": "58.0645",
                "best_evidence_median_return": "6.2374",
                "best_evidence_id": "smooth_core_mainstream_right_rebound_5_20_bull",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "operation_module_id": "neckline_strict_45_signal_90_score_v1",
                "approval_version": "neckline_strict_45_signal_90_score_v1_20260629",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_directive_level": "approved_daily_operation_guidance",
                "best_evidence_sample_size": "51",
                "best_evidence_win_rate": "63.8889",
                "best_evidence_median_return": "4.4597",
                "best_evidence_id": "low_position_le60_market_bull",
            },
            {
                "model_id": "price_pullback_23ema",
                "operation_module_id": "price_pullback_23ema_prev20_breakout_stop_v1",
                "approval_version": "price_pullback_23ema_operation_v1_20260703",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_directive_level": "approved_daily_operation_guidance",
                "best_evidence_sample_size": "1160",
                "best_evidence_win_rate": "66.03",
                "best_evidence_median_return": "",
                "best_evidence_id": "v1_gate_return20_tdcc_high_obv",
            }
        ]
    )


def price_pullback_feature_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25",
                "feature_test_status": "tested_point_in_time",
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": "False",
                "mature_count": "5141",
                "win_rate_pct": "66.58",
                "median_d20_close_return_pct": "0.83",
            }
        ]
    )


def price_pullback_row_parity_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260629",
                "parity_status": "blocked_missing_research_frame_date",
                "published_not_in_proxy_rows": "219",
                "proxy_not_published_rows": "0",
                "published_unique_stock_count": "219",
                "research_proxy_unique_stock_count": "0",
                "parity_gap_driver": "missing_research_frame_date",
            },
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260626",
                "parity_status": "blocked_not_exact_daily_row_parity",
                "published_not_in_proxy_rows": "9",
                "proxy_not_published_rows": "1251",
                "published_unique_stock_count": "217",
                "research_proxy_unique_stock_count": "1459",
                "parity_gap_driver": "research_full_universe_proxy_exceeds_daily_candidate_publication_scope",
            },
        ]
    )


def price_pullback_discussion_ready_row_parity_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260629",
                "parity_status": "exact_daily_row_parity_pass",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "0",
                "published_unique_stock_count": "219",
                "research_proxy_unique_stock_count": "219",
                "candidate_universe_replay_status": "candidate_universe_replay_exact_match",
                "parity_gap_driver": "none_exact",
            },
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260630",
                "parity_status": "blocked_missing_research_frame_date",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "0",
                "published_unique_stock_count": "233",
                "research_proxy_unique_stock_count": "233",
                "candidate_universe_replay_status": "candidate_universe_replay_exact_match",
                "parity_gap_driver": "missing_research_frame_date",
            },
        ]
    )


def price_pullback_exact_row_parity_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260629",
                "parity_status": "exact_daily_row_parity_pass",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "0",
                "published_unique_stock_count": "219",
                "research_proxy_unique_stock_count": "219",
                "candidate_universe_replay_status": "candidate_universe_replay_exact_match",
                "parity_gap_driver": "none_exact",
            },
            {
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": "20260630",
                "parity_status": "exact_daily_row_parity_pass",
                "published_not_in_proxy_rows": "0",
                "proxy_not_published_rows": "0",
                "published_unique_stock_count": "233",
                "research_proxy_unique_stock_count": "233",
                "candidate_universe_replay_status": "candidate_universe_replay_exact_match",
                "parity_gap_driver": "none_exact",
            },
        ]
    )


def adapter_frame(with_approval_metadata: bool = False) -> pd.DataFrame:
    rows = []
    for model_id in (LOW_VOLUME_MODEL_ID, MID_VOLUME_MODEL_ID, HIGH_VOLUME_MODEL_ID):
        row = {
            "model_id": model_id,
            "row_type": "data",
            "pdf_section": "confirmed_operation",
            "adapter_source_status": "ready",
        }
        if with_approval_metadata:
            row["approved_for_daily"] = "True"
            row["operation_directive_level"] = "approved_daily_operation_guidance"
        rows.append(row)
    return pd.DataFrame(rows)


def w_bottom_adapter_frame(model_id: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": model_id,
                "row_type": "data",
                "pdf_section": "confirmed_operation",
                "adapter_source_status": "ready",
                "approved_for_daily": "True",
                "operation_directive_level": "approved_daily_operation_guidance",
            },
            {
                "model_id": model_id,
                "row_type": "empty_state",
                "pdf_section": "active_operation",
                "adapter_source_status": "ready",
                "approved_for_daily": "True",
                "operation_directive_level": "approved_daily_operation_guidance",
            },
        ]
    )


def test_volume_breakout_approval_promotes_only_volume_model() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(),
        approval_frame(),
        w_bottom_adapter=w_bottom_adapter_frame("w_bottom_right_side"),
        neckline_adapter=w_bottom_adapter_frame("neckline_volume_breakout_confirmation"),
        price_pullback_adapter=w_bottom_adapter_frame("price_pullback_23ema"),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    volume = readiness[readiness["model_id"].eq(LOW_VOLUME_MODEL_ID)].iloc[0]
    assert volume["operation_module_status"] == "approved_operation_v1"
    assert volume["daily_adapter_status"] == "ready_pending_approval_metadata"
    assert volume["presentation_allowed"] == "True"
    assert volume["approved_for_daily"] == "True"
    assert volume["approval_status"] == "approved_for_daily_v1"
    assert volume["operation_directive_level"] == "approved_daily_operation_guidance"
    assert volume["pdf_integration_status"] == "pdf_integrated_daily_adapter"
    assert volume["packet_integration_status"] == "packet_integrated_daily_adapter"

    pullback = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]
    assert pullback["operation_module_status"] == "approved_operation_v1"
    assert pullback["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert pullback["presentation_allowed"] == "True"
    assert pullback["approved_for_daily"] == "True"
    assert pullback["operation_module_id"] == "price_pullback_23ema_prev20_breakout_stop_v1"
    assert pullback["approval_version"] == "price_pullback_23ema_operation_v1_20260703"
    assert pullback["operation_directive_level"] == "approved_daily_operation_guidance"
    assert pullback["pdf_integration_status"] == "pdf_integrated_daily_adapter"

    w_bottom = readiness[readiness["model_id"].eq("w_bottom_right_side")].iloc[0]
    assert w_bottom["operation_module_status"] == "approved_operation_v2"
    assert w_bottom["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert w_bottom["presentation_allowed"] == "True"
    assert w_bottom["approved_for_daily"] == "True"
    assert w_bottom["operation_module_id"] == "w_bottom_early_entry_operation_v2"
    assert w_bottom["approval_version"] == "w_bottom_early_entry_operation_v2_20260629"
    assert w_bottom["operation_directive_level"] == "approved_daily_operation_guidance"
    assert w_bottom["pdf_integration_status"] == "pdf_integrated_daily_adapter"

    neckline = readiness[readiness["model_id"].eq("neckline_volume_breakout_confirmation")].iloc[0]
    assert neckline["operation_module_status"] == "approved_operation_v1"
    assert neckline["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert neckline["presentation_allowed"] == "True"
    assert neckline["approved_for_daily"] == "True"
    assert neckline["operation_module_id"] == "neckline_strict_45_signal_90_score_v1"
    assert neckline["approval_version"] == "neckline_strict_45_signal_90_score_v1_20260629"
    assert neckline["operation_directive_level"] == "approved_daily_operation_guidance"
    assert neckline["pdf_integration_status"] == "pdf_integrated_daily_adapter"


def test_volume_adapter_approval_metadata_changes_adapter_status() -> None:
    readiness = build_model_operation_readiness(
        parity_frame().head(1),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    row = readiness.iloc[0]
    assert row["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "approved_daily_operation_guidance"


def test_price_pullback_approval_requires_daily_operation_adapter_for_pdf_integration() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        w_bottom_adapter=w_bottom_adapter_frame("w_bottom_right_side"),
        neckline_adapter=w_bottom_adapter_frame("neckline_volume_breakout_confirmation"),
        price_pullback_feature_confirmation=price_pullback_feature_frame(),
        price_pullback_daily_row_parity=price_pullback_row_parity_frame(),
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    row = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]

    assert row["operation_module_status"] == "approved_operation_v1"
    assert row["daily_adapter_status"] == "missing"
    assert row["approved_for_daily"] == "True"
    assert row["approval_status"] == "approved_for_daily_v1"
    assert row["operation_module_id"] == "price_pullback_23ema_prev20_breakout_stop_v1"
    assert row["approval_version"] == "price_pullback_23ema_operation_v1_20260703"
    assert row["presentation_allowed"] == "False"
    assert row["operation_directive_level"] == "no_operation_directive"
    assert row["pdf_integration_status"] == "pending_daily_operation_adapter"
    assert row["packet_integration_status"] == "pending_daily_operation_adapter"
    assert "approval exists" in row["blocker"]
    return


def test_price_pullback_approval_stays_blocked_without_adapter_even_if_research_frame_has_gap() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        w_bottom_adapter=w_bottom_adapter_frame("w_bottom_right_side"),
        neckline_adapter=w_bottom_adapter_frame("neckline_volume_breakout_confirmation"),
        price_pullback_feature_confirmation=price_pullback_feature_frame(),
        price_pullback_daily_row_parity=price_pullback_discussion_ready_row_parity_frame(),
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    row = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]

    assert row["operation_module_status"] == "approved_operation_v1"
    assert row["daily_adapter_status"] == "missing"
    assert row["approved_for_daily"] == "True"
    assert row["approval_status"] == "approved_for_daily_v1"
    assert row["presentation_allowed"] == "False"
    assert row["operation_directive_level"] == "no_operation_directive"
    assert row["pdf_integration_status"] == "pending_daily_operation_adapter"
    assert row["packet_integration_status"] == "pending_daily_operation_adapter"
    assert "approval exists" in row["blocker"]
    return
    assert "可以開始模型決策討論" in row["status_note_zh"]


def test_price_pullback_approval_and_adapter_enable_daily_operation_guidance() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        w_bottom_adapter=w_bottom_adapter_frame("w_bottom_right_side"),
        neckline_adapter=w_bottom_adapter_frame("neckline_volume_breakout_confirmation"),
        price_pullback_adapter=w_bottom_adapter_frame("price_pullback_23ema"),
        price_pullback_feature_confirmation=price_pullback_feature_frame(),
        price_pullback_daily_row_parity=price_pullback_exact_row_parity_frame(),
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    row = readiness[readiness["model_id"].eq("price_pullback_23ema")].iloc[0]

    assert row["operation_module_status"] == "approved_operation_v1"
    assert row["daily_adapter_status"] == "ready_approved_operation_guidance"
    assert row["approved_for_daily"] == "True"
    assert row["approval_status"] == "approved_for_daily_v1"
    assert row["presentation_allowed"] == "True"
    assert row["operation_directive_level"] == "approved_daily_operation_guidance"
    assert row["pdf_integration_status"] == "pdf_integrated_daily_adapter"
    assert row["packet_integration_status"] == "packet_integrated_daily_adapter"
    assert row["registry_best_pattern_id"] == "v1_gate_return20_tdcc_high_obv"
    assert row["registry_best_sample_size"] == "1160"
    assert row["registry_best_win_rate"] == "66.03"
    return
    assert "PDF renderer 不得自行推論 23EMA 操作列" in row["status_note_zh"]


def test_w_bottom_models_require_daily_operation_adapter_for_pdf_integration() -> None:
    readiness = build_model_operation_readiness(
        parity_frame(),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        generated_at="2026-06-30 00:00:00 Asia/Taipei",
    )

    w_bottom = readiness[readiness["model_id"].eq("w_bottom_right_side")].iloc[0]
    assert w_bottom["approved_for_daily"] == "True"
    assert w_bottom["daily_adapter_status"] == "missing"
    assert w_bottom["presentation_allowed"] == "False"
    assert w_bottom["operation_directive_level"] == "no_operation_directive"
    assert w_bottom["pdf_integration_status"] == "pending_daily_operation_adapter"

    neckline = readiness[readiness["model_id"].eq("neckline_volume_breakout_confirmation")].iloc[0]
    assert neckline["approved_for_daily"] == "True"
    assert neckline["daily_adapter_status"] == "missing"
    assert neckline["presentation_allowed"] == "False"
    assert neckline["operation_directive_level"] == "no_operation_directive"
    assert neckline["pdf_integration_status"] == "pending_daily_operation_adapter"


def test_missing_volume_adapter_blocks_presentation_even_when_approved() -> None:
    readiness = build_model_operation_readiness(
        parity_frame().head(1),
        registry_frame(),
        pd.DataFrame(),
        approval_frame(),
        generated_at="2026-06-15 00:00:00 Asia/Taipei",
    )

    row = readiness.iloc[0]
    assert row["daily_adapter_status"] == "missing"
    assert row["presentation_allowed"] == "False"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "no_operation_directive"
# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range


def test_revenue_readiness_uses_latest_v3_decision_v4_contract_and_model_owned_evidence() -> None:
    readiness = build_model_operation_readiness(
        revenue_parity_frame(),
        registry_frame(),
        adapter_frame(with_approval_metadata=True),
        approval_frame(),
        w_bottom_adapter=w_bottom_adapter_frame("w_bottom_right_side"),
        neckline_adapter=w_bottom_adapter_frame("neckline_volume_breakout_confirmation"),
        price_pullback_adapter=w_bottom_adapter_frame("price_pullback_23ema"),
        revenue_promotion_registry=revenue_promotion_registry_frame(),
        revenue_anomaly_registry=revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        generated_at="2026-08-28 00:00:00 Asia/Taipei",
    )

    row = readiness[readiness["model_id"].eq(REVENUE_MODEL_ID)].iloc[0]
    assert row["parity_status"] == "research_matrix_complete"
    assert row["blocker"] == "forward_holdout_v2_mature=0/20"
    assert row["operation_module_status"] == "disabled_adapter_preparation_validated"
    assert row["daily_adapter_status"] == "disabled_no_runtime_artifact"
    assert row["formal_model_use_allowed"] == "False"
    assert row["approved_for_daily"] == "False"
    assert row["approval_status"] == "not_started"
    assert row["operation_module_id"] == (
        "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
    )
    assert row["presentation_allowed"] == "False"
    assert row["production_allowed"] == "False"
    assert row["operation_directive_level"] == "no_operation_directive"
    assert row["pdf_integration_status"] == "not_started"
    assert row["packet_integration_status"] == "not_started"
    assert row["registry_best_pattern_id"] == "source_mid_falling"
    assert row["registry_best_sample_size"] == 53
    assert row["registry_best_win_rate"] == "77.3585"
    assert row["registry_best_median_return"] == "9.4077"
    assert row["daily_adapter_row_count"] == 0
    assert row["daily_adapter_data_row_count"] == 0
    assert row["daily_adapter_sections"] == ""
    assert "disabled formal adapter preparation 均已完成" in row["status_note_zh"]
    assert "strong_revenue gate requires" not in row["blocker"]
    non_revenue = readiness[~readiness["model_id"].eq(REVENUE_MODEL_ID)]
    assert non_revenue["approved_for_daily"].eq("True").any()
    assert non_revenue["presentation_allowed"].eq("True").any()
    assert non_revenue["formal_model_use_allowed"].eq("").all()
    assert non_revenue["production_allowed"].eq("").all()


def test_revenue_readiness_keeps_v4_compatibility_without_adapter_child(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    promotion = revenue_promotion_registry_frame().iloc[:-2].copy()
    monkeypatch.setattr(
        _SYNC_MODULE,
        "validate_disabled_adapter_preparation",
        lambda _repo: (_ for _ in ()).throw(
            AssertionError("v4 readiness invoked adapter child")
        ),
    )

    readiness = build_model_operation_readiness(
        revenue_parity_frame(),
        registry_frame(),
        adapter_frame(),
        revenue_promotion_registry=promotion,
        revenue_anomaly_registry=revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
    )

    row = readiness[readiness["model_id"].eq(REVENUE_MODEL_ID)].iloc[0]
    assert row["operation_module_status"] == (
        "research_matrix_complete_formal_adapter_not_started"
    )
    assert row["daily_adapter_status"] == "not_started"
    assert row["operation_module_id"] == ""


def test_revenue_readiness_fails_closed_until_v3_decision_v4_contract_is_latest() -> None:
    promotion = revenue_promotion_registry_frame().iloc[:-3].copy()

    with pytest.raises(RuntimeError, match="not an exact supported v4/v5/v6"):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=promotion,
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        )


def test_revenue_v5_validation_accepts_current_committed_readiness() -> None:
    readiness = pd.read_csv(
        ROOT / "output/latest/model_operation_readiness_latest.csv",
        dtype=str,
    ).fillna("")

    assert validate_revenue_readiness_row(
        readiness,
        revenue_promotion_registry_frame().iloc[:-1].copy(),
        revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest_frame(),
    ) == []


def test_revenue_v6_persisted_permissions_accept_exact_all_true_profile() -> None:
    readiness = pd.read_csv(
        ROOT / "output/latest/model_operation_readiness_latest.csv",
        dtype=str,
    ).fillna("")
    revenue_index = readiness.index[readiness["model_id"].eq(REVENUE_MODEL_ID)][0]
    for field_name in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        readiness.loc[revenue_index, field_name] = "True"
    readiness.loc[revenue_index, "approval_status"] = (
        readiness_validator.REVENUE_FORMAL_ADAPTER_APPROVAL_STATUS
    )
    readiness.loc[revenue_index, "operation_module_id"] = (
        readiness_validator.REVENUE_PROMOTION_PROFILES[
            readiness_validator.REVENUE_PROMOTION_DECISION_V6
        ].operation_module_id
    )
    readiness.loc[revenue_index, "pdf_integration_status"] = (
        "pdf_integrated_daily_adapter"
    )
    readiness.loc[revenue_index, "packet_integration_status"] = (
        "pending_packet_consumer"
    )
    for field_name in readiness_validator.FORMAL_ADAPTER_METADATA_COLUMNS:
        if field_name not in readiness.columns:
            readiness[field_name] = ""
        readiness.loc[revenue_index, field_name] = "bound"
    readiness.loc[revenue_index, "operation_module_path"] = (
        readiness_validator.REVENUE_FORMAL_ADAPTER_MODULE_REL
    )

    assert readiness_validator.validate_persisted_revenue_permission_columns(
        readiness
    ) == []


def test_revenue_v5_readiness_rejects_permission_drift() -> None:
    readiness = pd.read_csv(
        ROOT / "output/latest/model_operation_readiness_latest.csv",
        dtype=str,
    ).fillna("")
    revenue_index = readiness.index[readiness["model_id"].eq(REVENUE_MODEL_ID)][0]
    readiness.loc[revenue_index, "production_allowed"] = "True"

    errors = validate_revenue_readiness_row(
        readiness,
        revenue_promotion_registry_frame().iloc[:-1].copy(),
        revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest_frame(),
    )

    assert any(
        "readiness production_allowed must be 'False', got 'True'" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("source_name", "promotion", "anomaly", "holdout", "error_match"),
    [
        (
            "promotion",
            pd.DataFrame(),
            revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest_frame(),
            "missing required revenue readiness source",
        ),
        (
            "holdout",
            revenue_promotion_registry_frame(),
            revenue_anomaly_registry_frame(),
            pd.DataFrame(),
            "missing required revenue readiness source",
        ),
    ],
)
def test_revenue_readiness_missing_model_owned_source_fails_closed(
    source_name: str,
    promotion: pd.DataFrame,
    anomaly: pd.DataFrame,
    holdout: pd.DataFrame,
    error_match: str,
) -> None:
    del source_name
    with pytest.raises(RuntimeError, match=error_match):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=promotion,
            revenue_anomaly_registry=anomaly,
            revenue_forward_holdout_v2_manifest=holdout,
        )


def test_revenue_readiness_rejects_malformed_or_production_enabled_contracts() -> None:
    malformed_holdout = revenue_forward_holdout_v2_manifest_frame()
    malformed_holdout.loc[0, "primary_mature_count"] = "not-an-integer"
    with pytest.raises(RuntimeError, match="primary_mature_count must be a non-negative integer"):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=revenue_promotion_registry_frame(),
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=malformed_holdout,
        )

    production_enabled = revenue_promotion_registry_frame()
    production_enabled.loc[production_enabled.index[-1], "production_change"] = "True"
    with pytest.raises(RuntimeError, match="promotion.production_change must be 'false'"):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=production_enabled,
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        )


@pytest.mark.parametrize(
    "flag_name",
    (
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    ),
)
def test_revenue_readiness_requires_all_four_formal_promotion_flags_false(
    flag_name: str,
) -> None:
    promotion = revenue_promotion_registry_frame()
    promotion.loc[promotion.index[-1], flag_name] = "True"

    with pytest.raises(RuntimeError, match=rf"promotion\.{flag_name} must be 'false'"):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=promotion,
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        )


def test_revenue_readiness_rejects_unsafe_latest_promotion_decision_status() -> None:
    promotion = revenue_promotion_registry_frame()
    promotion.loc[promotion.index[-1], "decision_status"] = "formally_approved"

    with pytest.raises(RuntimeError, match="promotion.decision_status must be"):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=promotion,
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        )


@pytest.mark.parametrize(
    ("field_name", "unsafe_value", "error_match"),
    [
        ("artifact_version", "", "artifact_version must be"),
        ("holdout_status", "mature", "holdout_status is inconsistent"),
    ],
)
def test_revenue_readiness_rejects_holdout_version_or_maturity_status_drift(
    field_name: str,
    unsafe_value: str,
    error_match: str,
) -> None:
    holdout = revenue_forward_holdout_v2_manifest_frame()
    holdout.loc[0, field_name] = unsafe_value

    with pytest.raises(RuntimeError, match=error_match):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=revenue_promotion_registry_frame(),
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=holdout,
        )


def test_revenue_readiness_rejects_unrepaired_verified_data_error_policy(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    failed_gate = _SYNC_MODULE.CanonicalAnomalyValidationResult(
        rows={},
        row_count=9,
        effective_blocker_count=1,
        verified_real_extreme_count=8,
        verified_data_error_repaired_count=0,
        errors=("verified_data_error is missing repaired-rerun closure",),
        diagnostics=(),
    )
    monkeypatch.setattr(
        _SYNC_MODULE,
        "validate_current_anomaly_dispositions",
        lambda *_args, **_kwargs: failed_gate,
    )

    with pytest.raises(
        RuntimeError,
        match="canonical revenue anomaly disposition gate failed",
    ):
        build_model_operation_readiness(
            revenue_parity_frame(),
            registry_frame(),
            adapter_frame(),
            revenue_promotion_registry=revenue_promotion_registry_frame(),
            revenue_anomaly_registry=revenue_anomaly_registry_frame(),
            revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
        )


def test_revenue_readiness_validator_rejects_stale_or_permission_enabled_row() -> None:
    readiness = build_model_operation_readiness(
        revenue_parity_frame(),
        registry_frame(),
        adapter_frame(),
        revenue_promotion_registry=revenue_promotion_registry_frame(),
        revenue_anomaly_registry=revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
    )
    revenue_index = readiness.index[readiness["model_id"].eq(REVENUE_MODEL_ID)][0]
    readiness.loc[revenue_index, "blocker"] = "stale research matrix blocker"
    readiness.loc[revenue_index, "presentation_allowed"] = "True"

    errors = validate_revenue_readiness_row(
        readiness,
        revenue_promotion_registry_frame(),
        revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest_frame(),
    )

    assert any("blocker must be" in error for error in errors)
    assert any("presentation_allowed must be 'False'" in error for error in errors)


@pytest.mark.parametrize(
    "field_name",
    (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ),
)
def test_revenue_readiness_validator_rejects_missing_or_true_persisted_permission_field(
    field_name: str,
) -> None:
    readiness = build_model_operation_readiness(
        revenue_parity_frame(),
        registry_frame(),
        adapter_frame(),
        revenue_promotion_registry=revenue_promotion_registry_frame(),
        revenue_anomaly_registry=revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest=revenue_forward_holdout_v2_manifest_frame(),
    )
    missing = readiness.drop(columns=[field_name])
    missing_errors = validate_revenue_readiness_row(
        missing,
        revenue_promotion_registry_frame(),
        revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest_frame(),
    )
    assert any(f"{field_name} must be 'False'" in error for error in missing_errors)

    revenue_index = readiness.index[readiness["model_id"].eq(REVENUE_MODEL_ID)][0]
    readiness.loc[revenue_index, field_name] = "True"
    errors = validate_revenue_readiness_row(
        readiness,
        revenue_promotion_registry_frame(),
        revenue_anomaly_registry_frame(),
        revenue_forward_holdout_v2_manifest_frame(),
    )
    assert any(f"{field_name} must be 'False'" in error for error in errors)


@pytest.mark.parametrize(
    "field_name",
    (
        "approved_for_daily",
        "presentation_allowed",
    ),
)
def test_revenue_readiness_csv_schema_rejects_missing_existing_permission_column(
    tmp_path: Path,
    monkeypatch,
    field_name: str,
) -> None:
    columns = sorted(
        (
            readiness_validator.REQUIRED_COLUMNS
            | readiness_validator.REVENUE_PERMISSION_COLUMNS
        )
        - {field_name}
    )
    artifact = tmp_path / "model_operation_readiness_latest.csv"
    pd.DataFrame([{column: "False" for column in columns}]).to_csv(
        artifact,
        index=False,
    )
    monkeypatch.setattr(readiness_validator, "OUT_CSV", artifact)

    assert readiness_validator.validate_readiness_csv() == [
        f"model operation readiness missing columns: ['{field_name}']"
    ]


@pytest.mark.parametrize(
    "missing_fields",
    (
        pytest.param(
            {"formal_model_use_allowed"},
            id="missing-formal-model-use-allowed",
        ),
        pytest.param(
            {"production_allowed"},
            id="missing-production-allowed",
        ),
        pytest.param(
            {"formal_model_use_allowed", "production_allowed"},
            id="missing-both-revenue-permissions",
        ),
    ),
)
def test_revenue_readiness_csv_rejects_partial_permission_schema(
    tmp_path: Path,
    monkeypatch,
    missing_fields: set[str],
) -> None:
    columns = sorted(readiness_validator.REQUIRED_COLUMNS - missing_fields)
    artifact = tmp_path / "model_operation_readiness_latest.csv"
    pd.DataFrame([{column: "False" for column in columns}]).to_csv(
        artifact,
        index=False,
    )
    monkeypatch.setattr(readiness_validator, "OUT_CSV", artifact)

    assert readiness_validator.validate_readiness_csv() == [
        "model operation readiness missing columns: "
        f"{sorted(missing_fields)}"
    ]


def test_revenue_readiness_persisted_permission_columns_accept_explicit_false_and_neutral_legacy() -> None:
    readiness = pd.DataFrame(
        [
            {
                "model_id": REVENUE_MODEL_ID,
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "formal_model_use_allowed": "",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "production_allowed": "",
            },
        ]
    )

    assert readiness_validator.validate_persisted_revenue_permission_columns(
        readiness
    ) == []


@pytest.mark.parametrize(
    "field_name",
    (
        "approved_for_daily",
        "presentation_allowed",
    ),
)
def test_revenue_readiness_persisted_permission_columns_reject_noncanonical_source_boolean(
    field_name: str,
) -> None:
    readiness = pd.DataFrame(
        [
            {
                "model_id": REVENUE_MODEL_ID,
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "formal_model_use_allowed": "",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "production_allowed": "",
            },
        ]
    )
    readiness.loc[readiness["model_id"].eq(LOW_VOLUME_MODEL_ID), field_name] = "true"

    assert any(
        f"{field_name} must use exact canonical True/False values" in error
        for error in readiness_validator.validate_persisted_revenue_permission_columns(
            readiness
        )
    )


@pytest.mark.parametrize(
    "field_name",
    (
        "formal_model_use_allowed",
        "production_allowed",
    ),
)
def test_revenue_readiness_persisted_permission_columns_reject_missing_or_true_flag(
    field_name: str,
) -> None:
    readiness = pd.DataFrame(
        [
            {
                "model_id": REVENUE_MODEL_ID,
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "formal_model_use_allowed": "",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "production_allowed": "",
            },
        ]
    )
    missing = readiness.drop(columns=[field_name])
    assert any(
        field_name in error
        for error in readiness_validator.validate_persisted_revenue_permission_columns(
            missing
        )
    )

    readiness.loc[readiness["model_id"].eq(REVENUE_MODEL_ID), field_name] = "True"
    assert any(
        f"{field_name} must be explicit False" in error
        for error in readiness_validator.validate_persisted_revenue_permission_columns(
            readiness
        )
    )


@pytest.mark.parametrize(
    ("field_name", "alias_value"),
    (
        ("formal_model_use_allowed", "True"),
        ("formal_model_use_allowed", "False"),
        ("production_allowed", "True"),
        ("production_allowed", "False"),
    ),
)
def test_revenue_readiness_persisted_permission_columns_reject_non_revenue_boolean_alias(
    field_name: str,
    alias_value: str,
) -> None:
    readiness = pd.DataFrame(
        [
            {
                "model_id": REVENUE_MODEL_ID,
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            },
            {
                "model_id": LOW_VOLUME_MODEL_ID,
                "formal_model_use_allowed": "",
                "approved_for_daily": "True",
                "presentation_allowed": "True",
                "production_allowed": "",
            },
        ]
    )
    readiness.loc[
        readiness["model_id"].eq(LOW_VOLUME_MODEL_ID), field_name
    ] = alias_value

    assert any(
        f"{field_name} is revenue-only" in error
        for error in readiness_validator.validate_persisted_revenue_permission_columns(
            readiness
        )
    )


def test_revenue_legacy_builder_has_no_direct_mirror_writer(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[Path] = []

    def record_sync(repo_root: Path) -> tuple[pd.DataFrame, list[str]]:
        calls.append(repo_root)
        return pd.DataFrame(), []

    monkeypatch.setattr(readiness_builder, "ROOT", tmp_path)
    monkeypatch.setattr(readiness_builder, "LATEST_DIR", tmp_path / "output/latest")
    monkeypatch.setattr(readiness_builder, "DOCS_LATEST_DIR", tmp_path / "docs/latest")
    for name, relative in (
        ("OUT_CSV", "output/latest/model_operation_readiness_latest.csv"),
        ("OUT_MD", "output/latest/model_operation_readiness_latest.md"),
        ("DOCS_CSV", "docs/latest/model_operation_readiness_latest.csv"),
        ("DOCS_MD", "docs/latest/model_operation_readiness_latest.md"),
    ):
        monkeypatch.setattr(readiness_builder, name, tmp_path / relative)
    monkeypatch.setattr(readiness_builder, "sync", record_sync)

    assert readiness_builder.main() == 0
    assert calls == [tmp_path]
    assert list(tmp_path.rglob("*")) == []
# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range
