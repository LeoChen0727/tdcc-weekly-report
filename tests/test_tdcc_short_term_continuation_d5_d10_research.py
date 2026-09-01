from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_tdcc_short_term_continuation_d5_d10_research as producer  # noqa: E402
import validate_tdcc_short_term_continuation_d5_d10_research as validator  # noqa: E402


def canonical_json_sha256(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def normalized_text_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def manifest_identity_payload(manifest: dict[str, object]) -> dict[str, object]:
    snapshots = [
        {
            "date": str(item["date"]),
            "row_count": int(item["row_count"]),
            "stock_count": int(item["stock_count"]),
            "sha256": str(item["sha256"]),
        }
        for item in manifest["history_snapshots"]  # type: ignore[index]
    ]
    return {
        "schema_version": str(manifest["schema_version"]),
        "signal_date": str(manifest["signal_date"]),
        "official_date_source": str(manifest["official_date_source"]),
        "required_dates": list(manifest["required_dates"]),  # type: ignore[arg-type]
        "history_dates": list(manifest["history_dates"]),  # type: ignore[arg-type]
        "current_stock_count": int(manifest["current_stock_count"]),
        "history_snapshots": snapshots,
        "accepted_history_exceptions": list(
            manifest["accepted_history_exceptions"]  # type: ignore[arg-type]
        ),
    }


def write_manifest(path: Path, manifest: dict[str, object]) -> None:
    dataset_hash = canonical_json_sha256(manifest_identity_payload(manifest))
    manifest["dataset_hash"] = dataset_hash
    manifest["dataset_id"] = f"tdcc-{manifest['signal_date']}-{dataset_hash[:16]}"
    path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")


def refresh_manifest_from_history(paths: dict[str, Path]) -> dict[str, object]:
    manifest = json.loads(paths["tdcc_manifest"].read_text(encoding="utf-8"))
    for item in manifest["history_snapshots"]:
        source_path = paths["repo_root"] / item["path"]
        frame = pd.read_csv(source_path, dtype=str, keep_default_na=False)
        item["row_count"] = len(frame)
        item["stock_count"] = (
            frame["code"].astype(str).str.strip().str.replace(r"\.0$", "", regex=True).nunique()
            if "code" in frame
            else 0
        )
        item["sha256"] = normalized_text_sha256(source_path)
    write_manifest(paths["tdcc_manifest"], manifest)
    return manifest


def write_fixture(tmp_path: Path) -> dict[str, Path]:
    repo_root = tmp_path
    price_dir = repo_root / "data/stock_price_history"
    price_dir.mkdir(parents=True)
    dates = pd.bdate_range("2025-01-02", periods=180)
    index = np.arange(len(dates), dtype=float)
    base_close = 50 + 0.12 * index + 2 * np.sin(index / 5)
    close = base_close.copy()
    close[140] = base_close[140] * 1.5
    open_price = base_close * (1 + 0.001 * np.cos(index / 4))
    high = np.maximum(base_close + 1, close + 0.5)
    low = np.minimum(base_close - 1, open_price - 0.5)
    price = pd.DataFrame(
        {
            "date": dates.strftime("%Y%m%d"),
            "stock_id": "1234",
            "open": open_price,
            "high": high,
            "low": low,
            "close": close,
        }
    )
    price_path = price_dir / "1234.csv"
    price.to_csv(price_path, index=False)

    enriched = producer.load_price_frame(price_path, "1234")
    for signal_index in (125, 130):
        row = enriched.iloc[signal_index]
        assert 0 <= row["bb_width_percentile_120d"] <= 80
        assert row["k_value"] > row["d_value"]
        assert row["k_value"] < 90
        assert row["macd_hist"] > 0

    signal_dates = [str(price.iloc[index_value]["date"]) for index_value in (125, 130)]
    history_dir = repo_root / "output/history/tdcc"
    history_dir.mkdir(parents=True)
    history_snapshots: list[dict[str, object]] = []
    for signal_date in signal_dates:
        source_path = history_dir / f"tdcc_holder_ratio_{signal_date}.csv"
        pd.DataFrame(
            [
                {
                    "date": signal_date,
                    "code": "1234",
                    "name": "測試股",
                    "over_400_pct": "10",
                    "over_600_pct": "8",
                    "over_800_pct": "6",
                    "over_1000_pct": "4",
                }
            ]
        ).to_csv(source_path, index=False, lineterminator="\n")
        history_snapshots.append(
            {
                "date": signal_date,
                "path": source_path.relative_to(repo_root).as_posix(),
                "row_count": 1,
                "stock_count": 1,
                "sha256": normalized_text_sha256(source_path),
            }
        )
    manifest: dict[str, object] = {
        "status": "pass",
        "schema_version": "tdcc_dataset_manifest_v1",
        "hash_mode": "utf8_text_lf_normalized_sha256",
        "signal_date": signal_dates[-1],
        "official_date_source": "fixture://tdcc",
        "canonical_source_root": "output/history/tdcc",
        "required_dates": signal_dates,
        "history_dates": signal_dates,
        "current_stock_count": 1,
        "history_snapshot_count": 2,
        "history_snapshots": history_snapshots,
        "accepted_history_exceptions": [],
    }
    tdcc_manifest_path = repo_root / "output/latest/tdcc_dataset_manifest_latest.json"
    tdcc_manifest_path.parent.mkdir(parents=True)
    write_manifest(tdcc_manifest_path, manifest)
    dataset_id = str(manifest["dataset_id"])

    snapshot = pd.DataFrame(
        [
            {
                "signal_id": f"{date}_1234_normalized",
                "signal_date": date,
                "code": "1234",
                "name": "測試股",
                "tdcc_price_phase": "overheated_after_tdcc",
                "overheat_bucket": "overheated",
                "is_all_thresholds": "True",
                "tdcc_consecutive_up_weeks": "1",
                "price_ret_1w": "15",
                "price_ret_2w": "25",
                "market_regime": "mild_bull",
                "benchmark_index": "TWSE",
                "source_tdcc_dataset_id": dataset_id,
            }
            for date in signal_dates
        ]
    )
    snapshot_path = repo_root / "output/history/tdcc_signals/tdcc_signal_snapshot.csv"
    snapshot_path.parent.mkdir(parents=True)
    snapshot.to_csv(snapshot_path, index=False)

    published = pd.DataFrame(
        [
            {
                "snapshot_report_date": signal_dates[0],
                "stock_id": "5678",
                "model_id": producer.MODEL_ID,
                "trade_eligible": "False",
                "forward_window_status": "ready",
                "return_d5_close_pct": "25",
                "return_d10_close_pct": "-5",
            },
            {
                "snapshot_report_date": signal_dates[0],
                "stock_id": "9999",
                "model_id": "unrelated_model",
                "trade_eligible": "True",
                "forward_window_status": "ready",
                "return_d5_close_pct": "99",
                "return_d10_close_pct": "99",
            },
        ]
    )
    published_path = repo_root / "output/history/research/daily_published_snapshot_ranking_events.csv"
    published_path.parent.mkdir(parents=True)
    published.to_csv(published_path, index=False)
    return {
        "repo_root": repo_root,
        "price_dir": price_dir,
        "snapshot": snapshot_path,
        "tdcc_manifest": tdcc_manifest_path,
        "published": published_path,
        "history_dir": history_dir,
        "output_dir": repo_root / "artifacts",
    }


def produce_fixture(tmp_path: Path) -> tuple[dict[str, Path], producer.OutputPaths]:
    paths = write_fixture(tmp_path)
    outputs = producer.produce_artifacts(
        snapshot_path=paths["snapshot"],
        tdcc_manifest_path=paths["tdcc_manifest"],
        price_dir=paths["price_dir"],
        published_path=paths["published"],
        output_dir=paths["output_dir"],
        repo_root=paths["repo_root"],
    )
    return paths, outputs


def validate_fixture(paths: dict[str, Path], outputs: producer.OutputPaths) -> list[str]:
    return validator.validate_artifacts(
        events_path=outputs.events,
        summary_path=outputs.summary,
        manifest_path=outputs.manifest,
        anomaly_path=outputs.anomaly,
        snapshot_path=paths["snapshot"],
        tdcc_manifest_path=paths["tdcc_manifest"],
        price_dir=paths["price_dir"],
        published_path=paths["published"],
        repo_root=paths["repo_root"],
    )


def assert_manifest_loaders_reject(
    paths: dict[str, Path],
    expected_error: str,
) -> None:
    loaders = (producer.load_tdcc_manifest, validator.load_source_manifest)
    for loader in loaders:
        with pytest.raises(RuntimeError, match=expected_error):
            loader(paths["tdcc_manifest"], repo_root=paths["repo_root"])


@pytest.mark.parametrize(
    "invalid_token",
    ["yes", "1", "true", "FALSE", "unknown", "", " True ", "\tFalse\n"],
)
def test_canonical_source_rule_c_boolean_tokens_fail_closed(
    tmp_path: Path,
    invalid_token: str,
) -> None:
    paths = write_fixture(tmp_path)
    snapshot = pd.read_csv(paths["snapshot"], dtype=str, keep_default_na=False)
    snapshot.loc[0, "is_all_thresholds"] = invalid_token
    snapshot.to_csv(paths["snapshot"], index=False)

    producer_manifest = producer.load_tdcc_manifest(
        paths["tdcc_manifest"], repo_root=paths["repo_root"]
    )
    with pytest.raises(RuntimeError, match="expected exact True or False"):
        producer.load_signal_snapshot(paths["snapshot"], producer_manifest)

    validator_manifest = validator.load_source_manifest(
        paths["tdcc_manifest"], repo_root=paths["repo_root"]
    )
    with pytest.raises(RuntimeError, match="expected exact True or False"):
        validator.load_source_snapshot(paths["snapshot"], validator_manifest)


@pytest.mark.parametrize("module", [producer, validator])
@pytest.mark.parametrize(
    "invalid_date",
    [
        "20261340",
        "20260230",
        "20260001",
        "2026011",
        "20260101.0",
        "x20260101",
        " 20260101 ",
        "\t20260228\n",
    ],
)
def test_yyyymmdd_identity_requires_real_exact_round_trip(
    module: object,
    invalid_date: str,
) -> None:
    assert module.normalize_date(invalid_date) == ""
    assert module.normalize_date("20260228") == "20260228"


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    [
        ("path", "approved root"),
        ("hash", "hash mismatch"),
        ("row_count", "row_count mismatch"),
        (
            "current_stock_count",
            "current_stock_count does not match final history snapshot",
        ),
        (
            "accepted_exception",
            "accepted history exceptions do not match verified required snapshots",
        ),
        ("dataset_hash", "dataset_hash does not match verified history"),
        ("dataset_id", "dataset_id does not bind verified history"),
    ],
)
def test_manifest_history_lineage_and_dataset_binding_fail_closed(
    tmp_path: Path,
    mutation: str,
    expected_error: str,
) -> None:
    paths = write_fixture(tmp_path)
    manifest = json.loads(paths["tdcc_manifest"].read_text(encoding="utf-8"))
    first = manifest["history_snapshots"][0]
    if mutation == "path":
        first["path"] = (
            "output/history/not_tdcc/"
            f"tdcc_holder_ratio_{first['date']}.csv"
        )
    elif mutation == "hash":
        first["sha256"] = "0" * 64
    elif mutation == "row_count":
        first["row_count"] = 99
    elif mutation == "current_stock_count":
        manifest["current_stock_count"] = 2
    elif mutation == "accepted_exception":
        manifest["accepted_history_exceptions"] = [
            {"date": first["date"], "stock_id": "9999"}
        ]
    elif mutation == "dataset_hash":
        manifest["dataset_hash"] = "0" * 64
    elif mutation == "dataset_id":
        manifest["dataset_id"] = f"tdcc-{manifest['signal_date']}-deadbeefdeadbeef"
    else:  # pragma: no cover - parametrization is exhaustive
        raise AssertionError(mutation)
    if mutation in {"current_stock_count", "accepted_exception"}:
        write_manifest(paths["tdcc_manifest"], manifest)
    else:
        paths["tdcc_manifest"].write_text(
            json.dumps(manifest, ensure_ascii=False),
            encoding="utf-8",
        )
    assert_manifest_loaders_reject(paths, expected_error)


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    [
        ("schema", "missing required columns"),
        ("date_identity", "date identity mismatch"),
        ("duplicate_stock", "stock identity is empty or duplicated"),
    ],
)
def test_manifest_history_file_schema_and_identity_fail_closed(
    tmp_path: Path,
    mutation: str,
    expected_error: str,
) -> None:
    paths = write_fixture(tmp_path)
    manifest = json.loads(paths["tdcc_manifest"].read_text(encoding="utf-8"))
    first = manifest["history_snapshots"][0]
    source_path = paths["repo_root"] / first["path"]
    frame = pd.read_csv(source_path, dtype=str, keep_default_na=False)
    if mutation == "schema":
        frame = frame.drop(columns=["over_1000_pct"])
    elif mutation == "date_identity":
        frame.loc[0, "date"] = "20240101"
    elif mutation == "duplicate_stock":
        frame = pd.concat([frame, frame.iloc[[0]]], ignore_index=True)
    else:  # pragma: no cover - parametrization is exhaustive
        raise AssertionError(mutation)
    frame.to_csv(source_path, index=False, lineterminator="\n")
    refresh_manifest_from_history(paths)
    assert_manifest_loaders_reject(paths, expected_error)


def test_exact_union_replay_is_close_confirmed_and_fail_closed(tmp_path: Path) -> None:
    paths, outputs = produce_fixture(tmp_path)
    events = pd.read_csv(outputs.events, dtype=str, keep_default_na=False)
    summary = pd.read_csv(outputs.summary, dtype=str, keep_default_na=False)
    manifest = pd.read_csv(outputs.manifest, dtype=str, keep_default_na=False).iloc[0]
    anomaly = pd.read_csv(outputs.anomaly, dtype=str, keep_default_na=False)

    assert events["signal_event_key"].nunique() == 2
    assert len(events) == 4
    assert set(events["scenario_id"]) == {"fixed_d5_close", "fixed_d10_close"}
    assert set(events["matched_rule_count"]) == {"3"}
    assert events["rule_membership_overlap"].eq("True").all()
    assert events.groupby("signal_event_key")["scenario_id"].nunique().eq(2).all()
    assert events["entry_rule_id"].eq(producer.ENTRY_RULE_ID).all()
    assert set(events["exit_rule_id"]) == {"signal_dplus_5_close", "signal_dplus_10_close"}
    assert events["stop_rule_id"].eq(producer.STOP_RULE_ID).all()
    assert events["intraday_metrics_formal_use"].eq("False").all()
    assert events["formal_use"].eq("False").all()
    assert events["promotion_blocked"].eq("True").all()

    source_price = pd.read_csv(paths["price_dir"] / "1234.csv", dtype={"date": str})
    first_signal = source_price.index[source_price["date"].eq(events.iloc[0]["signal_date"])][0]
    first_d5 = events[
        events["signal_date"].eq(events.iloc[0]["signal_date"])
        & events["scenario_id"].eq("fixed_d5_close")
    ].iloc[0]
    assert first_d5["entry_date"] == source_price.iloc[first_signal + 1]["date"]
    assert first_d5["exit_date"] == source_price.iloc[first_signal + 5]["date"]
    expected_return = (
        source_price.iloc[first_signal + 5]["close"]
        / source_price.iloc[first_signal + 1]["open"]
        - 1
    ) * 100
    assert float(first_d5["realized_return_pct"]) == pytest.approx(expected_return)

    assert events.loc[
        events["scenario_id"].eq("fixed_d10_close"), "same_stock_overlap_candidate"
    ].eq("True").all()
    assert events.loc[
        events["scenario_id"].eq("fixed_d5_close"), "same_stock_overlap_candidate"
    ].eq("False").all()
    primary_anomaly = anomaly[anomaly["evidence_role"].eq("primary_exact_union_replay")]
    assert not primary_anomaly.empty
    assert primary_anomaly["final_disposition"].eq("unresolved_anomaly_candidate").all()
    assert primary_anomaly["retained_in_primary_metrics"].eq("True").all()
    assert primary_anomaly["excluded_from_primary_metrics"].eq("False").all()
    supplementary = summary[summary["group_kind"].eq("published_snapshot_supplementary")]
    assert set(supplementary["evidence_role"]) == {"supplementary_published_snapshot"}
    overall = summary[summary["group_kind"].eq("overall_union")]
    assert overall["right_censored_count"].eq("0").all()
    assert overall["sensitivity_is_corrected_primary"].eq("False").all()
    d10_overall = overall[overall["scenario_id"].eq("fixed_d10_close")].iloc[0]
    assert int(d10_overall["candidate_exclusion_sensitivity_valid_return_count"]) < int(
        d10_overall["valid_return_count"]
    )
    assert int(d10_overall["candidate_exclusion_sensitivity_excluded_candidate_count"]) == int(
        d10_overall["anomaly_candidate_count"]
    )
    assert manifest["published_snapshot_role"] == producer.PUBLISHED_ROLE
    assert manifest["pit_replay_status"] == producer.PIT_STATUS
    assert manifest["formal_operation_contract_defined"] == "False"
    assert manifest["formal_use"] == "False"
    assert manifest["promotion_blocked"] == "True"
    assert validate_fixture(paths, outputs) == []


def test_independent_validator_rejects_tampered_realized_return(tmp_path: Path) -> None:
    paths, outputs = produce_fixture(tmp_path)
    events = pd.read_csv(outputs.events, dtype=str, keep_default_na=False)
    events.loc[0, "realized_return_pct"] = "999"
    events.to_csv(outputs.events, index=False)
    errors = validate_fixture(paths, outputs)
    assert errors
    assert "realized_return_pct mismatch" in errors[0]


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    [
        ("anomaly_flag", "anomaly_candidate mismatch"),
        ("formal_flag", "formal_use must remain false"),
        ("promotion_flag", "promotion_blocked must be true"),
        ("blank_false_token", "formal_use must remain false"),
        ("numeric_true_token", "promotion_blocked must be true"),
        ("pit_status", "PIT blocker status mismatch"),
        ("promotion_reason", "promotion_block_reason mismatch"),
        ("source_lineage", "source_price_sha256 mismatch"),
        ("membership", "matched_rule_ids mismatch"),
    ],
)
def test_independent_validator_rejects_adversarial_contract_tampering(
    tmp_path: Path,
    mutation: str,
    expected_error: str,
) -> None:
    paths, outputs = produce_fixture(tmp_path)
    events = pd.read_csv(outputs.events, dtype=str, keep_default_na=False)
    if mutation == "anomaly_flag":
        index = events.index[events["anomaly_candidate"].eq("True")][0]
        events.loc[index, "anomaly_candidate"] = "False"
    elif mutation == "formal_flag":
        events.loc[0, "formal_use"] = "True"
    elif mutation == "promotion_flag":
        events.loc[0, "promotion_blocked"] = "False"
    elif mutation == "blank_false_token":
        events.loc[0, "formal_use"] = ""
    elif mutation == "numeric_true_token":
        events.loc[0, "promotion_blocked"] = "1"
    elif mutation == "pit_status":
        events.loc[0, "pit_replay_status"] = "resolved"
    elif mutation == "promotion_reason":
        events.loc[0, "promotion_block_reason"] = "resolved"
    elif mutation == "source_lineage":
        events.loc[0, "source_price_sha256"] = "0" * 64
    elif mutation == "membership":
        events.loc[0, "matched_rule_ids"] = producer.RULE_A
    else:  # pragma: no cover - parametrization is exhaustive
        raise AssertionError(mutation)
    events.to_csv(outputs.events, index=False)
    errors = validate_fixture(paths, outputs)
    assert errors
    assert expected_error in errors[0]


@pytest.mark.parametrize(
    ("artifact", "field", "value", "expected_error"),
    [
        ("summary", "pit_replay_status", "resolved", "summary PIT status mismatch"),
        (
            "summary",
            "promotion_block_reason",
            "resolved",
            "summary promotion_block_reason mismatch",
        ),
        (
            "manifest",
            "pit_replay_blocker",
            "resolved",
            "research manifest pit_replay_blocker mismatch",
        ),
        (
            "manifest",
            "promotion_block_reason",
            "resolved",
            "research manifest promotion_block_reason mismatch",
        ),
        (
            "manifest",
            "formal_use",
            "True",
            "research manifest formal_use must remain false",
        ),
        (
            "manifest",
            "formal_use",
            "",
            "research manifest formal_use must remain false",
        ),
        (
            "manifest",
            "promotion_blocked",
            "False",
            "research manifest promotion_blocked must remain true",
        ),
        (
            "manifest",
            "promotion_blocked",
            "1",
            "research manifest promotion_blocked must remain true",
        ),
    ],
)
def test_summary_and_manifest_exact_blockers_fail_closed(
    tmp_path: Path,
    artifact: str,
    field: str,
    value: str,
    expected_error: str,
) -> None:
    paths, outputs = produce_fixture(tmp_path)
    artifact_path = outputs.summary if artifact == "summary" else outputs.manifest
    frame = pd.read_csv(artifact_path, dtype=str, keep_default_na=False)
    frame.loc[0, field] = value
    frame.to_csv(artifact_path, index=False)
    errors = validate_fixture(paths, outputs)
    assert errors
    assert expected_error in errors[0]


def test_validator_is_independent_and_cli_is_guarded() -> None:
    validator_path = Path(validator.__file__)
    validator_source = validator_path.read_text(encoding="utf-8")
    tree = ast.parse(validator_source)
    imported_modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)
    allowed_imports = {
        "__future__",
        "argparse",
        "hashlib",
        "json",
        "math",
        "datetime",
        "pathlib",
        "typing",
        "numpy",
        "pandas",
    }
    assert imported_modules <= allowed_imports
    producer_source = Path(producer.__file__).read_text(encoding="utf-8")
    assert "with model_owned_artifact_guard(MODEL_ID, PRODUCER):" in producer_source


def test_output_ownership_preflight_rejects_unregistered_paths_without_writes(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "ownership.csv"
    pd.DataFrame(
        [
            {
                "owner_model_id": "unrelated_model",
                "producer": "scripts/unrelated.py",
                "artifact_glob": "output/latest/research_backtest/unrelated_*",
                "artifact_class": "research",
                "change_policy": "model_owned_write",
                "formal_evidence_status": "research_only",
            }
        ]
    ).to_csv(registry_path, index=False)
    output_dir = tmp_path / "output/latest/research_backtest"
    with pytest.raises(RuntimeError, match="unregistered artifact change"):
        producer.preflight_output_ownership(
            output_dir,
            repo_root=tmp_path,
            registry_path=registry_path,
        )
    expected = producer.output_paths(output_dir)
    assert not output_dir.exists()
    assert not any(
        path.exists()
        for path in (expected.events, expected.summary, expected.manifest, expected.anomaly)
    )


def test_cli_stops_at_ownership_preflight_before_producer(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    called = False

    def blocked_preflight(*args: object, **kwargs: object) -> producer.OutputPaths:
        raise RuntimeError("ownership preflight blocked")

    def forbidden_producer(*args: object, **kwargs: object) -> producer.OutputPaths:
        nonlocal called
        called = True
        raise AssertionError("producer must not run before ownership preflight")

    monkeypatch.setattr(
        producer,
        "parse_args",
        lambda: SimpleNamespace(
            signal_snapshot=tmp_path / "snapshot.csv",
            tdcc_manifest=tmp_path / "manifest.json",
            price_dir=tmp_path / "prices",
            published_snapshot=tmp_path / "published.csv",
            no_published_supplement=True,
            output_dir=tmp_path / "output",
        ),
    )
    monkeypatch.setattr(producer, "preflight_output_ownership", blocked_preflight)
    monkeypatch.setattr(producer, "produce_artifacts", forbidden_producer)
    with pytest.raises(RuntimeError, match="ownership preflight blocked"):
        producer.main()
    assert called is False
    assert not (tmp_path / "output").exists()


def test_missing_required_price_column_fails_closed(tmp_path: Path) -> None:
    paths = write_fixture(tmp_path)
    price_path = paths["price_dir"] / "1234.csv"
    price = pd.read_csv(price_path)
    price = price.drop(columns=["open"])
    price.to_csv(price_path, index=False)
    with pytest.raises(RuntimeError, match="missing required columns"):
        producer.produce_artifacts(
            snapshot_path=paths["snapshot"],
            tdcc_manifest_path=paths["tdcc_manifest"],
            price_dir=paths["price_dir"],
            published_path=paths["published"],
            output_dir=paths["output_dir"],
            repo_root=paths["repo_root"],
        )
