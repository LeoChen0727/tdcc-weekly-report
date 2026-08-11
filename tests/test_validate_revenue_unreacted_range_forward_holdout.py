from __future__ import annotations

import ast
from copy import deepcopy
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest


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
        immutable_history_base_frames=bundle.get("history_base"),
    )


def _assert_error(errors: list[str], *needles: str) -> None:
    joined = "\n".join(errors).lower()
    assert errors, "validator unexpectedly accepted a corrupted holdout"
    assert any(needle.lower() in joined for needle in needles), joined


def test_bare_cli_fails_closed_without_explicit_inputs() -> None:
    with pytest.raises(SystemExit):
        validator.main([])


def _persist_standalone_cli_fixture(
    tmp_path: Path,
) -> tuple[list[str], Path]:
    bundle = _valid_bundle()
    replay_source = bundle["source"].copy().reset_index(drop=True)
    paths = write_forward_holdout(
        bundle["manifest"],
        bundle["detail"],
        bundle["summary"],
        bundle["comparison"],
        bundle["anomaly"],
        replay_source_detail=replay_source,
        output_root=tmp_path,
    )
    source_manifest_path = tmp_path / "source_projection_manifest.csv"
    bundle["source_manifest"].to_csv(source_manifest_path, index=False)
    price_directory = tmp_path / "price_inputs"
    price_directory.mkdir()
    for stock_id, frame in bundle["daily"].items():
        frame.to_csv(price_directory / f"{stock_id}.csv", index=False)

    args = [
        "--manifest",
        str(paths["manifest_latest"]),
        "--source-manifest",
        str(source_manifest_path),
        "--source-detail",
        str(paths["replay_source_latest"]),
        "--price-input-directory",
        str(price_directory),
        "--history-base-ref",
        "synthetic-immutable-base",
    ]
    for name in ("detail", "summary", "comparison", "anomaly"):
        args.extend((f"--{name.replace('_', '-')}", str(paths[f"{name}_latest"])))
    for name in ("manifest", "detail", "summary", "comparison", "anomaly"):
        args.extend(
            (
                f"--{name.replace('_', '-')}-history",
                str(paths[f"{name}_history"]),
            )
        )
    return args, paths["replay_source_latest"]


def _real_shape_round_trip_price_frame() -> pd.DataFrame:
    dates = pd.bdate_range("2026-06-01", periods=48)
    close = pd.Series(
        [100.00000000000001 + (index * 0.125) for index in range(len(dates))],
        dtype=float,
    )
    previous_high = close.shift(1).rolling(20, min_periods=20).max()
    breakout = close.gt(previous_high)
    sparse_ma120 = pd.Series(
        [float("nan")] * 7
        + [0.12345678901234566 + (index * 0.0001) for index in range(41)],
        dtype=float,
    )
    frame = pd.DataFrame(
        {
            "stock_id": ["0007"] * len(dates),
            "date": dates.strftime("%Y%m%d"),
            "open": close - 0.25,
            "high": close + 0.5,
            "low": close - 0.5,
            "close": close,
            "analysis_open": close - 0.25,
            "analysis_high": close + 0.5,
            "analysis_low": close - 0.5,
            "analysis_close": close,
            "ma60": pd.Series(
                [float("nan")] * 5
                + [1.2345678901234567 + (index * 0.001) for index in range(43)],
                dtype=float,
            ),
            "ma120": sparse_ma120,
            "analysis_ema23": close.ewm(span=23, adjust=False).mean(),
            "operation_ma20": close.rolling(20, min_periods=20).mean(),
            "operation_ema23": close.ewm(span=23, adjust=False).mean(),
            "analysis_price_adjustment_factor": [0.10000000000000002]
            * len(dates),
            "cross_breakout_prev20": (
                breakout & ~breakout.shift(1, fill_value=False).astype(bool)
            ),
            "verified_price_row": [index % 2 == 0 for index in range(len(dates))],
            "price_basis": ["pit_adjusted_close"] * len(dates),
            "optional_lineage_note": [
                ("", "authoritative", "NA", "N/A", "nan", "null")[index % 6]
                for index in range(len(dates))
            ],
        }
    )
    return frame


def _canonical_price_rows(frame: pd.DataFrame) -> list[list[str]]:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    return [
        [validator._canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]


def test_explicit_price_reader_round_trips_real_shape_sparse_and_boundary_floats(
    tmp_path: Path,
) -> None:
    frame = _real_shape_round_trip_price_frame()
    expected = validator._normalize_prices({"0007": frame})
    expected_lineage = validator._price_lineage(expected)
    price_directory = tmp_path / "price_inputs"
    price_directory.mkdir()
    price_path = price_directory / "0007.csv"

    # Exercise the exact default pandas serialization used by the workflow.
    frame.to_csv(price_path, index=False)
    loaded = validator._load_explicit_price_inputs(price_directory)
    observed = validator._normalize_prices(loaded)

    assert list(loaded) == ["0007"]
    assert loaded["0007"]["stock_id"].eq("0007").all()
    assert pd.isna(loaded["0007"].at[0, "ma120"])
    assert loaded["0007"].at[7, "ma120"] == frame.at[7, "ma120"]
    assert (
        loaded["0007"].at[0, "analysis_price_adjustment_factor"]
        == frame.at[0, "analysis_price_adjustment_factor"]
    )
    assert pd.isna(loaded["0007"].at[0, "optional_lineage_note"])
    assert loaded["0007"].loc[1:5, "optional_lineage_note"].tolist() == [
        "authoritative",
        "NA",
        "N/A",
        "nan",
        "null",
    ]
    assert _canonical_price_rows(observed["0007"]) == _canonical_price_rows(
        expected["0007"]
    )
    assert validator._frame_sha(observed["0007"]) == validator._frame_sha(
        expected["0007"]
    )
    assert validator._price_lineage(observed) == expected_lineage

    # The legacy reader leaves leading-blank numeric columns as object/string;
    # downstream normalization then preserves lexical decimals on operation MA
    # columns instead of the producer's float canonical form.  This proves the
    # fixture detects the original lineage defect rather than a no-op case.
    legacy = pd.read_csv(
        price_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    legacy_normalized = validator._normalize_prices({"0007": legacy})
    assert validator._price_lineage(legacy_normalized) != expected_lineage


def test_explicit_price_reader_rejects_missing_stock_identity(tmp_path: Path) -> None:
    frame = _real_shape_round_trip_price_frame()
    frame["stock_id"] = ""
    price_directory = tmp_path / "price_inputs"
    price_directory.mkdir()
    frame.to_csv(price_directory / "blank.csv", index=False)

    with pytest.raises(RuntimeError, match="stock identity is invalid"):
        validator._load_explicit_price_inputs(price_directory)


def test_explicit_price_reader_keeps_real_numeric_drift_fail_closed(
    tmp_path: Path,
) -> None:
    frame = _real_shape_round_trip_price_frame()
    expected = validator._normalize_prices({"0007": frame})
    expected_lineage = validator._price_lineage(expected)
    price_directory = tmp_path / "price_inputs"
    price_directory.mkdir()
    price_path = price_directory / "0007.csv"

    lineage_drift = frame.copy()
    lineage_drift.at[0, "analysis_price_adjustment_factor"] += 0.000001
    lineage_drift.to_csv(price_path, index=False)
    loaded_drift = validator._load_explicit_price_inputs(price_directory)
    normalized_drift = validator._normalize_prices(loaded_drift)
    assert validator._price_lineage(normalized_drift) != expected_lineage

    formula_drift = frame.copy()
    formula_drift.at[30, "analysis_close"] += 0.01
    formula_drift.to_csv(price_path, index=False)
    loaded_formula_drift = validator._load_explicit_price_inputs(price_directory)
    with pytest.raises(
        RuntimeError,
        match="derived price field differs from frozen analysis_close formula",
    ):
        validator._normalize_prices(loaded_formula_drift)


def test_standalone_cli_accepts_persisted_enriched_replay_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    args, replay_source_path = _persist_standalone_cli_fixture(tmp_path)
    monkeypatch.setattr(
        validator,
        "load_history_base_frames_from_git",
        lambda *_args, **_kwargs: {},
    )

    assert validator.main(args) == 0
    assert replay_source_path.is_file()
    assert "independently validated" in capsys.readouterr().out


def test_standalone_cli_rejects_replay_source_missing_anomaly_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    args, replay_source_path = _persist_standalone_cli_fixture(tmp_path)
    source = pd.read_csv(
        replay_source_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    ).drop(columns=["qualifying_source_revenue_anomaly_candidate_flags"])
    source.to_csv(replay_source_path, index=False)
    monkeypatch.setattr(
        validator,
        "load_history_base_frames_from_git",
        lambda *_args, **_kwargs: {},
    )

    assert validator.main(args) == 1
    output = capsys.readouterr().out
    assert "qualifying_source_revenue_anomaly_candidate_flags" in output


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
        ("projected_episode_row_count", PR462_PROJECTED_EPISODE_ROW_COUNT + 0.9),
        ("projected_episode_semantic_sha256", "0" * 64),
    ):
        bundle = _valid_bundle()
        manifest = bundle["source_manifest"].copy()
        manifest[column] = manifest[column].astype(object)
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
        replay_source_detail=bundle["source"],
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


def test_validator_rejects_clean_uncommitted_prior_capture_against_immutable_base() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )
    daily_second = {key: value.copy() for key, value in daily.items()}
    last = daily_second["1111"].index[-1]
    daily_second["1111"].at[last, "price_resolution_ids_on_date"] = "revision-1"
    second = build_forward_holdout(
        source,
        daily_second,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )
    daily_third = {key: value.copy() for key, value in daily_second.items()}
    daily_third["1111"].at[last, "price_resolution_ids_on_date"] = "revision-2"
    third = build_forward_holdout(
        source,
        daily_third,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:20:00 Asia/Taipei",
    )
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    history = {
        name: pd.concat([first_frame, second_frame, third_frame], ignore_index=True)
        for name, first_frame, second_frame, third_frame in zip(
            names, first, second, third, strict=True
        )
    }
    bundle = {
        **dict(zip(names, third, strict=True)),
        "source": source,
        "daily": daily_third,
        "source_manifest": source_manifest,
        "history": history,
        "history_base": dict(zip(names, first, strict=True)),
    }

    _assert_error(_errors(bundle), "uncommitted prior capture")


def test_validator_rejects_rewritten_uncommitted_current_capture() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )
    daily_second = {key: value.copy() for key, value in daily.items()}
    last = daily_second["1111"].index[-1]
    daily_second["1111"].at[last, "price_resolution_ids_on_date"] = "revision-1"
    second = build_forward_holdout(
        source,
        daily_second,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    history = {
        name: pd.concat([first_frame, second_frame], ignore_index=True)
        for name, first_frame, second_frame in zip(names, first, second, strict=True)
    }
    history["manifest"].at[len(first[0]), "rule_canonical_sha256"] = "f" * 64
    bundle = {
        **dict(zip(names, second, strict=True)),
        "source": source,
        "daily": daily_second,
        "source_manifest": source_manifest,
        "history": history,
        "history_base": dict(zip(names, first, strict=True)),
    }

    _assert_error(_errors(bundle), "current-capture semantic parity drift")


def test_validator_rejects_stale_existing_capture_as_current() -> None:
    source, daily, source_manifest = holdout_inputs()
    first = build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:00:00 Asia/Taipei",
    )
    daily_second = {key: value.copy() for key, value in daily.items()}
    last = daily_second["1111"].index[-1]
    daily_second["1111"].at[last, "price_resolution_ids_on_date"] = "revision-1"
    second = build_forward_holdout(
        source,
        daily_second,
        source_manifest=source_manifest,
        generated_at="2026-08-11 12:10:00 Asia/Taipei",
    )
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    history = {
        name: pd.concat([first_frame, second_frame], ignore_index=True)
        for name, first_frame, second_frame in zip(names, first, second, strict=True)
    }
    bundle = {
        **dict(zip(names, first, strict=True)),
        "source": source,
        "daily": daily,
        "source_manifest": source_manifest,
        "history": history,
        "history_base": {name: frame.copy() for name, frame in history.items()},
    }

    _assert_error(_errors(bundle), "not the contiguous terminal suffix")


def test_validator_rejects_current_capture_row_reordering() -> None:
    bundle = _valid_bundle()
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history_base"] = {name: bundle[name].copy() for name in names}
    bundle["detail"] = bundle["detail"].iloc[::-1].reset_index(drop=True)

    _assert_error(_errors(bundle), "current-capture row order drift")


def test_validator_immutable_base_prefix_includes_generated_at() -> None:
    bundle = _valid_bundle()
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history_base"] = {name: bundle[name].copy() for name in names}
    bundle["history_base"]["manifest"].at[0, "generated_at"] = (
        "2099-01-01 00:00:00 Asia/Taipei"
    )

    _assert_error(_errors(bundle), "immutable base prefix drift")


def test_validator_rejects_partial_immutable_base_surface_bundle() -> None:
    bundle = _valid_bundle()
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    bundle["history"] = {name: bundle[name].copy() for name in names}
    bundle["history_base"] = {
        name: bundle[name].copy() for name in names if name != "anomaly"
    }

    _assert_error(_errors(bundle), "immutable base surface set drift")


def test_git_history_loader_rejects_partial_five_surface_base(
    tmp_path: Path, monkeypatch
) -> None:
    bundle = _valid_bundle()
    names = ("manifest", "detail", "summary", "comparison", "anomaly")
    paths = {name: tmp_path / f"{name}.csv" for name in names}
    payloads = {
        path.relative_to(tmp_path).as_posix(): bundle[name].to_csv(index=False).encode()
        for name, path in paths.items()
    }
    missing = paths["anomaly"].relative_to(tmp_path).as_posix()

    def fake_run(command, **_kwargs):
        relative = str(command[2]).split(":", 1)[1]
        if relative == missing:
            return subprocess.CompletedProcess(
                command,
                128,
                stdout=b"",
                stderr=f"Path '{relative}' does not exist in 'base'".encode(),
            )
        return subprocess.CompletedProcess(
            command,
            0,
            stdout=payloads[relative],
            stderr=b"",
        )

    monkeypatch.setattr(validator.subprocess, "run", fake_run)
    with pytest.raises(RuntimeError, match="zero or all five surfaces"):
        validator.load_history_base_frames_from_git(
            "base",
            root=tmp_path,
            history_paths=paths,
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

    for column, invalid_value in (
        ("exit_price", "not-a-number"),
        ("realized_return_pct", float("inf")),
    ):
        bundle = _valid_bundle()
        detail = bundle["detail"].copy()
        target = detail.index[detail["stock_id"].astype(str).eq("3333")][0]
        detail[column] = detail[column].astype(object)
        detail.at[target, column] = invalid_value
        mapping = detail.loc[target].drop(
            labels=["event_row_canonical_sha256"]
        ).to_dict()
        detail.at[target, "event_row_canonical_sha256"] = validator._mapping_sha(
            mapping
        )
        bundle["detail"] = detail
        _assert_error(_errors(bundle), column, "numeric replay", "right-censored")


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


@pytest.mark.parametrize(
    "column",
    ("analysis_ema23", "cross_breakout_prev20"),
)
def test_validator_independently_rejects_precomputed_price_feature_drift(
    column: str,
) -> None:
    bundle = _valid_bundle()
    daily = {
        stock_id: frame.copy() for stock_id, frame in bundle["daily"].items()
    }
    target = daily["1111"]
    row = target.index[-1]
    if column == "cross_breakout_prev20":
        target.at[row, column] = not bool(target.at[row, column])
    else:
        target.at[row, column] = float(target.at[row, column]) + 0.5
    bundle["daily"] = daily

    _assert_error(_errors(bundle), "derived price field differs from frozen")


def test_validator_accepts_pr462_authoritative_prepared_ma_rounding() -> None:
    source, daily, source_manifest = holdout_inputs()
    rounded = {stock_id: frame.copy() for stock_id, frame in daily.items()}
    for frame in rounded.values():
        frame["ma60"] = pd.to_numeric(frame["ma60"], errors="coerce").round(4)
        frame["ma120"] = pd.to_numeric(frame["ma120"], errors="coerce").round(4)
    frames = build_forward_holdout(
        source,
        rounded,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )

    assert validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=rounded,
        source_manifest=source_manifest,
    ) == []


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

    for column in ("rule_contract_version", "data_contract_version"):
        bundle = _valid_bundle()
        manifest = bundle["manifest"].copy()
        manifest.at[0, column] = "drifted_contract_version"
        bundle["manifest"] = manifest
        _assert_error(_errors(bundle), "preregistration", "rule", "drift", column)

        bundle = _valid_bundle()
        detail = bundle["detail"].copy()
        detail.at[detail.index[0], column] = "drifted_contract_version"
        bundle["detail"] = detail
        _assert_error(_errors(bundle), "detail", "lineage", "drift", column)

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


def test_validator_rejects_malformed_governance_boolean_text() -> None:
    for frame_name, column in (
        ("manifest", "research_only"),
        ("summary", "formal_model_use_allowed"),
        ("comparison", "approved_for_daily"),
        ("anomaly", "promotion_evidence_allowed"),
        ("manifest", "pdf_consumption_allowed"),
    ):
        bundle = _valid_bundle()
        frame = bundle[frame_name].copy()
        frame[column] = frame[column].astype(object)
        frame.at[frame.index[0], column] = "not-a-boolean"
        bundle[frame_name] = frame
        _assert_error(_errors(bundle), column, "canonical boolean")

    for column in ("research_only", "ranking_consumption_allowed"):
        bundle = _valid_bundle()
        source_manifest = bundle["source_manifest"].copy()
        source_manifest[column] = source_manifest[column].astype(object)
        source_manifest.at[0, column] = "not-a-boolean"
        bundle["source_manifest"] = source_manifest
        _assert_error(_errors(bundle), column, "canonical boolean", "point-in-time")

    for value in (False, "not-a-boolean"):
        bundle = _valid_bundle()
        manifest = bundle["manifest"].copy()
        manifest["append_only_history"] = manifest["append_only_history"].astype(
            object
        )
        manifest.at[0, "append_only_history"] = value
        bundle["manifest"] = manifest
        _assert_error(_errors(bundle), "append_only_history")


def test_validator_rejects_malformed_detail_and_source_anomaly_booleans() -> None:
    for column in (
        "low_falling_member",
        "right_censored",
        "sensitivity_metric_included",
        "same_stock_non_overlap_applied",
    ):
        bundle = _valid_bundle()
        detail = bundle["detail"].copy()
        detail[column] = detail[column].astype(object)
        detail.at[detail.index[0], column] = "not-a-boolean"
        mapping = detail.iloc[0].drop(labels=["event_row_canonical_sha256"]).to_dict()
        detail.at[detail.index[0], "event_row_canonical_sha256"] = (
            validator._mapping_sha(mapping)
        )
        bundle["detail"] = detail
        _assert_error(_errors(bundle), "detail", column, "canonical boolean")

    for column in (
        "unresolved_price_path_candidate_flag",
        "qualifying_source_revenue_anomaly_candidate_flag",
        "qualifying_source_revenue_anomaly_candidate_flags",
    ):
        bundle = _valid_bundle()
        source = bundle["source"].copy()
        source[column] = source[column].astype(object)
        source.at[source.index[0], column] = "not-a-boolean"
        bundle["source"] = source
        _assert_error(_errors(bundle), "source anomaly", column, "canonical boolean")

    for column, value in (
        ("qualifying_update_count", 1.9),
        ("episode_start_sequence_index", 100.5),
        ("latest_qualifying_sequence_index", 100.5),
        ("qualifying_sequence_indices", "100.5"),
    ):
        bundle = _valid_bundle()
        source = bundle["source"].copy()
        source[column] = source[column].astype(object)
        source.at[source.index[0], column] = value
        bundle["source"] = source
        _assert_error(_errors(bundle), "source", "exact integer", "sequence")


def test_validator_rejects_closed_surface_metadata_and_count_drift() -> None:
    cases = (
        ("manifest", "preregistration_pr_number", "999", "preregistration"),
        ("manifest", "financial_statement_scope", "EPS_enabled", "financial"),
        ("manifest", "right_censored_event_count", 999, "right-censored"),
        ("manifest", "holdout_event_count", 0.9, "holdout event count"),
        ("manifest", "primary_mature_count", 999, "primary mature"),
        ("manifest", "primary_right_censored_count", 999, "primary right-censored"),
        ("detail", "candidate_variant_id", "wrong_variant", "candidate variant"),
        ("detail", "lifecycle_policy_id", "wrong_lifecycle", "lifecycle"),
        ("detail", "holding_days", 999, "holding days"),
        ("detail", "holding_days", 30.00005, "holding days"),
        (
            "detail",
            "holding_session_index_offset",
            29.00005,
            "holding offset",
        ),
        ("detail", "trigger_index", 196.00005, "exact-integer timing"),
        ("detail", "exit_reason", "wrong_exit", "exit reason"),
        ("detail", "financial_statement_scope", "EPS_enabled", "financial"),
        ("detail", "primary_metric_included", False, "primary metric"),
        ("detail", "same_stock_non_overlap_applied", False, "non-overlap"),
        ("summary", "variant_order", 99, "variant order"),
        ("summary", "variant_order", 1.00005, "variant order"),
        ("summary", "event_count", 1.9, "exact-integer metric"),
        ("summary", "variant_role", "wrong_role", "variant role"),
        ("summary", "bridge_excluded_signal_count", 999, "bridge exclusion"),
        ("summary", "anomaly_candidate_count", 999, "anomaly candidate count"),
        ("summary", "financial_statement_scope", "EPS_enabled", "financial"),
        ("comparison", "variant_order", 99, "variant order"),
        ("comparison", "variant_role", "wrong_role", "variant role"),
        ("comparison", "comparison_conclusion", "promotion_pass", "conclusion"),
        ("anomaly", "variant_order", 99, "variant order"),
        ("anomaly", "basis_order", 99, "basis order"),
        (
            "anomaly",
            "excluded_anomaly_candidate_count",
            0.9,
            "primary retention",
        ),
        ("anomaly", "anomaly_policy", "drop_candidates", "anomaly policy"),
    )
    for surface, column, value, needle in cases:
        bundle = _valid_bundle()
        frame = bundle[surface].copy()
        frame[column] = frame[column].astype(object)
        frame.at[frame.index[0], column] = value
        if surface == "detail":
            mapping = frame.iloc[0].drop(
                labels=["event_row_canonical_sha256"]
            ).to_dict()
            frame.at[frame.index[0], "event_row_canonical_sha256"] = (
                validator._mapping_sha(mapping)
            )
        bundle[surface] = frame
        _assert_error(_errors(bundle), needle, column)


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
