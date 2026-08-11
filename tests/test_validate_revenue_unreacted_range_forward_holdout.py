from __future__ import annotations

import ast
from copy import deepcopy
from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TESTS = ROOT / "tests"
for path in (SCRIPTS, TESTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import validate_revenue_unreacted_range_forward_holdout as validator  # noqa: E402
from revenue_unreacted_range_forward_holdout import (  # noqa: E402
    PR462_PROJECTED_EPISODE_ROW_COUNT,
    PR462_PROJECTED_EPISODE_SEMANTIC_SHA256,
    PRIMARY_VARIANT_ID,
    build_forward_holdout,
    write_forward_holdout,
)
from test_revenue_unreacted_range_forward_holdout import (  # noqa: E402
    GENERATED_AT,
    _price_frame,
    _source_manifest,
    _source_row,
    holdout_inputs,
)


def _valid_bundle():
    source, daily, source_manifest = holdout_inputs()
    manifest, detail, summary, comparison, anomaly = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    return {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
        "source": source,
        "daily": daily,
        "source_manifest": source_manifest,
    }


def _errors(bundle: dict[str, object]) -> list[str]:
    return validator.validate_frames(
        bundle["manifest"],
        bundle["detail"],
        bundle["summary"],
        bundle["comparison"],
        bundle["anomaly"],
        source_detail=bundle["source"],
        daily_by_stock=bundle["daily"],
        source_manifest=bundle["source_manifest"],
        history_frames=bundle.get("history"),
    )


def _assert_error(errors: list[str], *needles: str) -> None:
    joined = "\n".join(errors).lower()
    assert errors, "validator unexpectedly accepted a corrupted holdout"
    assert any(needle.lower() in joined for needle in needles), joined


def test_validator_is_independent_and_accepts_exact_replay() -> None:
    validator_path = Path(validator.__file__).resolve()
    tree = ast.parse(validator_path.read_text(encoding="utf-8-sig"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module)
    assert "revenue_unreacted_range_forward_holdout" not in imported
    assert _errors(_valid_bundle()) == []


def test_validator_recomputes_capture_envelope_and_checks_all_five_surfaces() -> None:
    bundle = _valid_bundle()
    for surface in ("manifest", "detail", "summary", "comparison", "anomaly"):
        corrupted = _valid_bundle()
        frame = corrupted[surface].copy()
        if frame.empty:
            continue
        frame.at[frame.index[0], "capture_id"] = "f" * 64
        corrupted[surface] = frame
        _assert_error(_errors(corrupted), "capture-envelope", "capture_id")

    bundle = _valid_bundle()
    daily = {stock_id: frame.copy() for stock_id, frame in bundle["daily"].items()}
    last = daily["1111"].index[-1]
    daily["1111"].at[last, "analysis_close"] += 0.001
    daily["1111"].at[last, "close"] += 0.001
    bundle["daily"] = daily
    _assert_error(_errors(bundle), "capture-envelope", "price", "lineage")

    bundle = _valid_bundle()
    manifest = bundle["manifest"].copy()
    manifest.at[0, "artifact_row_key"] = "not-manifest"
    bundle["manifest"] = manifest
    _assert_error(_errors(bundle), "artifact_row_key", "manifest")


def test_validator_requires_exact_pr462_projection_pin() -> None:
    exact = _valid_bundle()["source_manifest"].iloc[0]
    assert int(exact["projected_episode_row_count"]) == PR462_PROJECTED_EPISODE_ROW_COUNT
    assert (
        exact["projected_episode_semantic_sha256"]
        == PR462_PROJECTED_EPISODE_SEMANTIC_SHA256
    )
    for column, value in (
        ("projected_episode_row_count", PR462_PROJECTED_EPISODE_ROW_COUNT - 1),
        ("projected_episode_semantic_sha256", "0" * 64),
    ):
        bundle = _valid_bundle()
        manifest = bundle["source_manifest"].copy()
        manifest.at[0, column] = value
        bundle["source_manifest"] = manifest
        _assert_error(_errors(bundle), "pr462", "projected episode")


def test_validator_rejects_detail_lineage_and_business_row_key_forgery() -> None:
    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    detail.at[0, "training_source_projection_semantic_sha256"] = "f" * 64
    mapping = detail.iloc[0].drop(labels=["event_row_canonical_sha256"]).to_dict()
    detail.at[0, "event_row_canonical_sha256"] = validator._mapping_sha(mapping)
    bundle["detail"] = detail
    _assert_error(
        _errors(bundle),
        "detail capture-envelope lineage drift",
        "training_source_projection_semantic_sha256",
    )

    bundle = _valid_bundle()
    summary = bundle["summary"].copy()
    extra = summary.iloc[[0]].copy()
    extra["artifact_row_key"] = "extra-unique-row-key"
    bundle["summary"] = pd.concat([summary, extra], ignore_index=True)
    _assert_error(_errors(bundle), "summary row multiplicity drift")

    bundle = _valid_bundle()
    anomaly = bundle["anomaly"].copy()
    anomaly.at[0, "artifact_row_key"] = "wrong-but-unique-row-key"
    bundle["anomaly"] = anomaly
    _assert_error(_errors(bundle), "anomaly artifact/business key drift")


def test_validator_reads_five_histories_and_accepts_current_capture_parity(
    tmp_path: Path,
) -> None:
    bundle = _valid_bundle()
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    paths = write_forward_holdout(
        *(bundle[name] for name in names),
        output_root=tmp_path,
    )
    bundle["history"] = {
        name: pd.read_csv(
            paths[f"{name}_history"],
            dtype={"stock_id": str, "capture_id": str, "artifact_row_key": str},
            keep_default_na=False,
            low_memory=False,
        )
        for name in names
    }
    assert _errors(bundle) == []
    assert {
        name for name in validator.DEFAULT_PATHS if name.endswith("_history")
    } == {f"{name}_history" for name in names}
    assert all(
        "output/history/research" in validator.DEFAULT_PATHS[f"{name}_history"].as_posix()
        for name in names
    )


def test_validator_rejects_history_schema_duplicate_presence_and_semantic_drift() -> None:
    names = ("manifest", "detail", "summary", "comparison", "anomaly")

    bundle = _valid_bundle()
    bundle["history"] = {name: bundle[name].copy() for name in names}
    duplicate = bundle["history"]["summary"].iloc[[0]].copy()
    bundle["history"]["summary"] = pd.concat(
        [bundle["history"]["summary"], duplicate], ignore_index=True
    )
    _assert_error(_errors(bundle), "duplicate capture/artifact row keys")

    bundle = _valid_bundle()
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history"]["summary"] = bundle["history"]["summary"].iloc[1:].copy()
    _assert_error(_errors(bundle), "current-capture row presence drift")

    bundle = _valid_bundle()
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history"]["summary"].at[0, "event_count"] = 999
    _assert_error(_errors(bundle), "current-capture semantic parity drift")

    bundle = _valid_bundle()
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history"]["comparison"] = bundle["history"]["comparison"].drop(
        columns=["comparison_conclusion"]
    )
    _assert_error(_errors(bundle), "history schema drift")


def test_validator_rejects_bridge_signal_leaking_into_primary_holdout() -> None:
    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    leaked = detail.iloc[[0]].copy()
    leaked["artifact_row_key"] = leaked["artifact_row_key"].astype(str) + "|bridge"
    leaked["event_key"] = leaked["event_key"].astype(str) + "|bridge"
    leaked["trigger_date"] = "20260803"
    detail = pd.concat([detail, leaked], ignore_index=True)
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "bridge", "holdout start")


def test_validator_rejects_future_source_row_and_asof_leakage() -> None:
    bundle = _valid_bundle()
    source = bundle["source"].copy()
    daily = bundle["daily"]
    stock_id = str(source.at[0, "stock_id"])
    price = daily[stock_id]
    future_date = "20260805"
    future_index = int(price.index[price["date"].astype(str).eq(future_date)][0])
    separator = "|"
    source.at[0, "qualifying_update_count"] = 2
    source.at[0, "qualifying_revenue_periods"] += separator + "202607"
    source.at[0, "qualifying_source_dates"] += separator + future_date
    source.at[0, "qualifying_cross_market_resolution_ids"] += separator + "none"
    source.at[0, "qualifying_source_row_canonical_sha256s"] += separator + "7" * 64
    source.at[0, "qualifying_canonical_source_table_dates"] += separator + future_date
    source.at[0, "qualifying_trade_dates"] += separator + future_date
    source.at[0, "qualifying_sequence_indices"] += separator + str(future_index)
    source.at[0, "qualifying_source_revenue_anomaly_candidate_flags"] += (
        separator + "False"
    )
    source.at[0, "latest_qualifying_revenue_period"] = "202607"
    source.at[0, "latest_qualifying_source_date"] = future_date
    source.at[0, "latest_qualifying_cross_market_resolution_id"] = "none"
    source.at[0, "latest_qualifying_source_row_canonical_sha256"] = "7" * 64
    source.at[0, "latest_qualifying_canonical_source_table_date"] = future_date
    source.at[0, "latest_qualifying_trade_date"] = future_date
    source.at[0, "latest_qualifying_sequence_index"] = future_index
    bundle["source"] = source
    _assert_error(_errors(bundle), "future", "point-in-time", "cutoff", "as-of")

    for column in (
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_canonical_source_table_date",
    ):
        bundle = _valid_bundle()
        detail = bundle["detail"].copy()
        target = detail.index[
            detail["variant_id"].eq(PRIMARY_VARIANT_ID)
            & detail["stock_id"].astype(str).eq("1111")
        ][0]
        detail.at[target, column] = "20260805"
        bundle["detail"] = detail
        _assert_error(_errors(bundle), "future", "point-in-time", "as-of", column)

    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    target = detail.index[detail["stock_id"].astype(str).eq("1111")][0]
    detail.at[target, "source_asof_sequence_index"] = int(
        detail.at[target, "trigger_index"]
    ) + 1
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "future", "sequence", "point-in-time")


def test_validator_recomputes_anomaly_flag_from_asof_row_not_future_episode() -> None:
    source_date = "20260617"
    future_date = "20260805"
    source_row = _source_row(
        stock_id="7777",
        position="mid",
        anomaly_candidate=False,
        source_date=source_date,
    )
    price = _price_frame(
        trigger_dates=("20260804",),
        position="mid",
        source_date=source_date,
    )
    future_index = int(price.index[price["date"].astype(str).eq(future_date)][0])
    source_row.update(
        {
            "latest_qualifying_revenue_period": "202607",
            "latest_qualifying_source_date": future_date,
            "latest_qualifying_source_row_canonical_sha256": "7" * 64,
            "latest_qualifying_canonical_source_table_date": future_date,
            "latest_qualifying_trade_date": future_date,
            "latest_qualifying_sequence_index": future_index,
            "qualifying_update_count": 2,
            "qualifying_revenue_periods": "202605|202607",
            "qualifying_source_dates": f"{source_date}|{future_date}",
            "qualifying_cross_market_resolution_ids": "none|none",
            "qualifying_source_row_canonical_sha256s": f"{'4' * 64}|{'7' * 64}",
            "qualifying_canonical_source_table_dates": f"{source_date}|{future_date}",
            "qualifying_trade_dates": f"{source_date}|{future_date}",
            "qualifying_sequence_indices": (
                f"{source_row['episode_start_sequence_index']}|{future_index}"
            ),
            "qualifying_source_revenue_anomaly_candidate_flags": "False|True",
            "qualifying_source_revenue_anomaly_candidate_flag": True,
        }
    )
    source = pd.DataFrame([source_row])
    source_manifest = _source_manifest()
    manifest, detail, summary, comparison, anomaly = build_forward_holdout(
        source,
        {"7777": price},
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    bundle = {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
        "source": source,
        "daily": {"7777": price},
        "source_manifest": source_manifest,
    }
    assert str(detail.iloc[0]["source_anomaly_candidate_flag"]).lower() == "false"
    assert _errors(bundle) == []

    corrupted = detail.copy()
    corrupted.at[0, "source_anomaly_candidate_flag"] = True
    bundle["detail"] = corrupted
    _assert_error(_errors(bundle), "anomaly", "source_anomaly_candidate_flag")


def test_validator_rejects_d2_entry_or_d30_offset_drift() -> None:
    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    target = detail.index[detail["stock_id"].astype(str).eq("1111")][0]
    detail.at[target, "entry_date"] = detail.at[target, "confirmation_date"]
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "d+2", "entry", "confirmation")

    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    target = detail.index[detail["stock_id"].astype(str).eq("1111")][0]
    detail.at[target, "holding_session_index_offset"] = 30
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "d+30", "offset", "29", "holding")


def test_validator_rejects_right_censored_return_in_mature_metrics() -> None:
    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    target = detail.index[detail["stock_id"].astype(str).eq("3333")][0]
    detail.at[target, "realized_return_pct"] = 99.0
    detail.at[target, "return_outcome"] = "win"
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "right-censored", "right_censored", "mature")

    bundle = _valid_bundle()
    summary = bundle["summary"].copy()
    target = summary.index[summary["variant_id"].eq(PRIMARY_VARIANT_ID)][0]
    summary.at[target, "mature_count"] = int(summary.at[target, "mature_count"]) + 1
    bundle["summary"] = summary
    _assert_error(_errors(bundle), "mature", "right-censored", "summary")


def test_validator_rejects_same_stock_overlap_and_false_rearm() -> None:
    source = pd.DataFrame(
        [_source_row(stock_id="5555", position="mid", source_date="20260713")]
    )
    daily = {
        "5555": _price_frame(
            trigger_dates=("20260804", "20260820", "20260918"),
            position="mid",
            return_pct=8.0,
            end_date="20261130",
            source_date="20260713",
        )
    }
    source_manifest = _source_manifest(1)
    manifest, detail, summary, comparison, anomaly = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert len(detail) == 2
    corrupted = detail.copy()
    corrupted.at[1, "entry_date"] = corrupted.at[0, "exit_date"]
    corrupted.at[1, "entry_index"] = corrupted.at[0, "exit_index"]
    bundle = {
        "manifest": manifest,
        "detail": corrupted,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
        "source": source,
        "daily": daily,
        "source_manifest": source_manifest,
    }
    _assert_error(_errors(bundle), "overlap", "rearm", "prior exit")


def test_validator_rejects_challenger_parity_or_union_count_drift() -> None:
    bundle = _valid_bundle()
    comparison = bundle["comparison"].copy()
    union = comparison.index[
        comparison["variant_id"].eq("source_low_or_mid_falling_union")
    ][0]
    comparison.at[union, "event_count"] = int(comparison.at[union, "event_count"]) + 1
    bundle["comparison"] = comparison
    _assert_error(_errors(bundle), "union", "challenger", "comparison", "parity")


def test_validator_rejects_anomaly_exclusion_from_primary_metrics() -> None:
    bundle = _valid_bundle()
    detail = bundle["detail"].copy()
    target = detail.index[
        detail["stock_id"].astype(str).eq("1111")
        & detail["variant_id"].eq(PRIMARY_VARIANT_ID)
    ][0]
    assert bool(detail.at[target, "anomaly_candidate_flag"])
    detail.at[target, "primary_metric_included"] = False
    bundle["detail"] = detail
    _assert_error(_errors(bundle), "anomaly", "primary", "retain")

    bundle = _valid_bundle()
    anomaly = bundle["anomaly"].copy()
    target = anomaly.index[
        anomaly["variant_id"].eq(PRIMARY_VARIANT_ID)
        & anomaly["analysis_basis"].eq("primary_candidate_retaining")
    ][0]
    anomaly.at[target, "excluded_anomaly_candidate_count"] = 1
    bundle["anomaly"] = anomaly
    _assert_error(_errors(bundle), "anomaly", "primary", "retain")


def test_validator_rejects_anchor_rule_or_source_cutoff_drift() -> None:
    bundle = _valid_bundle()
    manifest = bundle["manifest"].copy()
    manifest.at[0, "preregistration_merge_commit"] = "0" * 40
    bundle["manifest"] = manifest
    _assert_error(_errors(bundle), "preregistration", "anchor", "commit")

    bundle = _valid_bundle()
    manifest = bundle["manifest"].copy()
    manifest.at[0, "rule_canonical_sha256"] = "f" * 64
    bundle["manifest"] = manifest
    _assert_error(_errors(bundle), "rule", "canonical", "drift")

    bundle = _valid_bundle()
    source_manifest = bundle["source_manifest"].copy()
    source_manifest.at[0, "cutoff_date"] = "20260714"
    bundle["source_manifest"] = source_manifest
    _assert_error(_errors(bundle), "cutoff", "20260713", "training")


def test_validator_rejects_formal_ranking_or_pdf_consumer_leakage() -> None:
    for frame_name, column in (
        ("manifest", "formal_model_use_allowed"),
        ("detail", "presentation_allowed"),
        ("summary", "approved_for_daily"),
        ("comparison", "promotion_evidence_allowed"),
        ("anomaly", "production_change"),
        ("manifest", "ranking_consumption_allowed"),
        ("manifest", "pdf_consumption_allowed"),
    ):
        bundle = _valid_bundle()
        frame = deepcopy(bundle[frame_name])
        frame.at[frame.index[0], column] = True
        bundle[frame_name] = frame
        _assert_error(
            _errors(bundle),
            column,
            "formal",
            "consumer",
            "research-only",
        )


def test_validator_accepts_accumulating_holdout_with_no_mature_rows() -> None:
    source = pd.DataFrame([_source_row(stock_id="6666", position="mid")])
    daily = {
        "6666": _price_frame(
            trigger_dates=("20260806",),
            position="mid",
            end_date="20260828",
        )
    }
    source_manifest = _source_manifest(1)
    manifest, detail, summary, comparison, anomaly = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    assert manifest.iloc[0]["holdout_status"] == "holdout_accumulating"
    assert (summary["mature_count"].astype(int) == 0).all()
    bundle = {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
        "source": source,
        "daily": daily,
        "source_manifest": source_manifest,
    }
    assert _errors(bundle) == []
