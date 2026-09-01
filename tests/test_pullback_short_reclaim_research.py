from __future__ import annotations

import ast
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import build_pullback_short_reclaim_research as producer  # noqa: E402
import validate_pullback_short_reclaim_research as validator  # noqa: E402


REPORT_DATE = "20260803"


def _signal_row(
    stock_id: str,
    *,
    report_line: str = "mainstream",
    model_id: str = producer.MODEL_ID,
    score: str = "60",
) -> dict[str, str]:
    return {
        "signal_date": REPORT_DATE,
        "source_row_index": stock_id,
        "stock_id": stock_id,
        "stock_name": f"Stock {stock_id}",
        "model_id": model_id,
        "model_name_zh": "回檔後短線轉強模型",
        "main_condition_met": "True",
        "entry_basis": "signal_date_next_open",
        "model_score": score,
        "score_components": "base=50",
        "risk_penalty_tags": "",
        "next_confirmation": "close_confirmed",
        "model_main_conditions": "published_exact_signal",
        "model_add_score_items": "",
        "model_forbidden_veto": "",
        "model_operation_guidance": "research_only",
        "selection_semantics": "published_signal_truth",
        "model_rank": "1",
        "report_line": report_line,
        "report_bucket": report_line,
    }


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def _snapshot_path(
    snapshot_dir: Path,
    rows: list[dict[str, str]],
    revision: str,
) -> tuple[Path, str]:
    staging = snapshot_dir / f"staging_{revision}.csv"
    _write_csv(staging, rows)
    sha = producer.canonical_file_sha256(staging)
    path = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{REPORT_DATE}_{revision}_{sha[:12]}.csv"
    )
    staging.rename(path)
    return path, sha


def _manifest_row(
    path: Path,
    sha: str,
    revision: str,
    *,
    supersedes: str = "",
    reason: str = "fixture",
) -> dict[str, str]:
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    return {
        "snapshot_report_date": REPORT_DATE,
        "snapshot_revision": revision,
        "supersedes_snapshot_sha256": supersedes,
        "revision_reason": reason,
        "generated_at": "2026-08-03 18:00:00 Asia/Taipei",
        "pipeline_commit_sha": "a" * 40,
        "main_price_date": REPORT_DATE,
        "report_ready": "True",
        "artifact_id": producer.ARTIFACT_ID,
        "source_path": "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "snapshot_path": path.resolve().as_posix(),
        "source_sha256": sha,
        "snapshot_sha256": sha,
        "row_count": str(len(frame)),
        "column_count": str(len(frame.columns)),
        "purpose": "as_published_daily_model_snapshot",
    }


def _write_price(
    price_dir: Path,
    stock_id: str,
    closes: list[float],
    *,
    entry_open: float = 100.0,
) -> None:
    dates = pd.bdate_range("2026-08-03", periods=len(closes) + 1)
    rows: list[dict[str, object]] = [
        {
            "date": dates[0].strftime("%Y%m%d"),
            "stock_id": stock_id,
            "open": entry_open,
            "close": entry_open,
        }
    ]
    for position, close in enumerate(closes, start=1):
        rows.append(
            {
                "date": dates[position].strftime("%Y%m%d"),
                "stock_id": stock_id,
                "open": entry_open if position == 1 else closes[position - 2],
                "close": close,
            }
        )
    _write_csv(price_dir / f"{stock_id}.csv", rows)


def _fixture(
    tmp_path: Path,
    *,
    target_rows: list[dict[str, str]] | None = None,
    include_r1: bool = True,
    price_rows: dict[str, list[float]] | None = None,
) -> tuple[Path, Path, Path]:
    snapshot_dir = tmp_path / "output/history/daily_model_snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    latest_rows = target_rows or [
        _signal_row("1111", report_line="mainstream"),
        _signal_row("1111", report_line="non_mainstream"),
        _signal_row("2222"),
        _signal_row("3333", model_id="another_model"),
    ]
    manifest_rows: list[dict[str, str]] = []
    supersedes = ""
    if include_r1:
        r1_path, r1_sha = _snapshot_path(
            snapshot_dir,
            [_signal_row("9999")],
            "r1",
        )
        manifest_rows.append(_manifest_row(r1_path, r1_sha, "r1", reason="initial"))
        supersedes = r1_sha
        revision = "r2"
    else:
        revision = "r1"
    latest_path, latest_sha = _snapshot_path(snapshot_dir, latest_rows, revision)
    manifest_rows.append(
        _manifest_row(
            latest_path,
            latest_sha,
            revision,
            supersedes=supersedes,
            reason="corrected_latest" if include_r1 else "initial",
        )
    )
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    _write_csv(manifest_path, manifest_rows)
    price_dir = tmp_path / "data/stock_price_history"
    for stock_id, closes in (
        price_rows
        or {
            "1111": [100, 101, 102, 103, 110, 105, 104, 103, 102, 100]
            + [99] * 9
            + [80],
            "2222": [100, 120, 140, 160, 200] + [200] * 15,
        }
    ).items():
        _write_price(price_dir, stock_id, closes)
    return snapshot_dir, manifest_path, price_dir


def _build(
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
) -> producer.ReplayBundle:
    return producer.build_replay(
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
        generated_at="2026-09-01 12:00:00 Asia/Taipei",
    )


def test_latest_revision_exact_signal_replay_and_identity_dedup(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    assert set(bundle.events["snapshot_revision"]) == {"r2"}
    assert set(bundle.events["stock_id"]) == {"1111", "2222"}
    assert len(bundle.events) == 3
    duplicate = bundle.events[bundle.events["stock_id"].eq("1111")]
    assert len(duplicate) == 2
    assert duplicate["primary_metric_included"].tolist() == ["True", "False"]
    assert duplicate["source_row_sha256"].nunique() == 2
    canonical = duplicate[duplicate["primary_metric_included"].eq("True")].iloc[0]
    assert canonical["entry_date"] == "20260804"
    assert float(canonical["entry_open_price"]) == 100.0
    assert float(canonical["d5_return_pct"]) == 10.0
    assert canonical["d5_outcome"] == "win"
    assert float(canonical["d10_return_pct"]) == 0.0
    assert canonical["d10_outcome"] == "neutral"
    assert float(canonical["d20_return_pct"]) == -20.0
    assert canonical["d20_outcome"] == "failure"
    d5 = bundle.summary[bundle.summary["horizon"].eq("D+5")].iloc[0]
    assert int(d5["published_source_row_count"]) == 3
    assert int(d5["unique_signal_event_count"]) == 2
    assert int(d5["duplicate_presentation_row_count"]) == 1
    assert int(d5["mature_count"]) == 2
    assert set(bundle.summary["formal_use_allowed"]) == {"False"}
    assert set(bundle.summary["operation_contract_status"]) == {"decision_required"}
    assert validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    ) == []


def test_anomaly_candidate_is_unresolved_and_retained_in_primary_metrics(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    anomaly = bundle.anomalies[
        bundle.anomalies["stock_id"].eq("2222")
        & bundle.anomalies["horizon"].eq("D+5")
    ].iloc[0]
    assert float(anomaly["realized_return_pct"]) == 100.0
    assert anomaly["statistical_trigger_status"] == "anomaly_candidate"
    assert anomaly["final_disposition"] == "unresolved_anomaly_candidate"
    assert anomaly["retained_in_primary_metrics"] == "True"
    d5 = bundle.summary[bundle.summary["horizon"].eq("D+5")].iloc[0]
    assert int(d5["mature_count"]) == 2
    assert int(d5["unresolved_anomaly_candidate_count"]) == 1
    assert int(d5["excluded_anomaly_candidate_count"]) == 0
    assert float(d5["average_return_pct"]) == 55.0
    assert int(d5["sensitivity_sample_count"]) == 1
    assert int(d5["sensitivity_excluded_anomaly_candidate_count"]) == 1
    assert float(d5["sensitivity_average_return_pct"]) == 10.0
    assert d5["sensitivity_is_corrected_primary"] == "False"
    assert d5["price_source_formal_lineage_status"] == (
        "mutable_current_files_unpinned_block_formal_use"
    )


def test_maturity_is_explicit_for_partial_and_missing_price_history(
    tmp_path: Path,
) -> None:
    rows = [_signal_row("1111"), _signal_row("4444")]
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=rows,
        include_r1=False,
        price_rows={"1111": [101, 102, 103, 104, 105, 106, 107]},
    )

    bundle = _build(snapshot_dir, manifest_path, price_dir)

    partial = bundle.events[bundle.events["stock_id"].eq("1111")].iloc[0]
    missing = bundle.events[bundle.events["stock_id"].eq("4444")].iloc[0]
    assert partial["d5_maturity_status"] == "mature"
    assert partial["d10_maturity_status"] == "not_mature"
    assert partial["d20_maturity_status"] == "not_mature"
    assert missing["d5_maturity_status"] == "missing_price_history"
    assert missing["price_source_sha256"] == ""
    assert int(bundle.summary.loc[bundle.summary["horizon"].eq("D+5"), "mature_count"].iloc[0]) == 1
    assert int(bundle.summary.loc[bundle.summary["horizon"].eq("D+10"), "mature_count"].iloc[0]) == 0
    assert int(
        bundle.summary.loc[
            bundle.summary["horizon"].eq("D+5"), "right_censored_count"
        ].iloc[0]
    ) == 1
    assert int(
        bundle.summary.loc[
            bundle.summary["horizon"].eq("D+10"), "right_censored_count"
        ].iloc[0]
    ) == 2


def test_snapshot_row_count_mismatch_fails_closed(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[manifest.index[-1], "row_count"] = "999"
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")

    with pytest.raises(RuntimeError, match="row/column count mismatch"):
        _build(snapshot_dir, manifest_path, price_dir)


def test_duplicate_report_rows_with_semantic_drift_fail_closed(tmp_path: Path) -> None:
    rows = [
        _signal_row("1111", report_line="mainstream", score="60"),
        _signal_row("1111", report_line="non_mainstream", score="61"),
    ]
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=rows,
        include_r1=False,
        price_rows={"1111": [100] * 20},
    )

    with pytest.raises(RuntimeError, match="disagree on signal semantics"):
        _build(snapshot_dir, manifest_path, price_dir)


def test_independent_validator_detects_return_formal_and_summary_tampering(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    events = bundle.events.astype(object).copy()
    summary = bundle.summary.astype(object).copy()
    events.loc[events.index[0], "d5_return_pct"] = "999"
    events.loc[events.index[0], "formal_use_allowed"] = "True"
    summary.loc[summary["horizon"].eq("D+5"), "mature_count"] = "999"

    errors = validator.validate_replay_bundle(
        events,
        summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )

    assert any("formal_use_allowed" in error for error in errors)
    assert any("d5_return_pct mismatch" in error for error in errors)
    assert any("mature_count mismatch" in error for error in errors)


def test_independent_validator_detects_removed_or_promoted_anomaly(tmp_path: Path) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    anomalies = bundle.anomalies.copy()
    anomalies.loc[anomalies.index[0], "final_disposition"] = "verified_real_extreme"

    errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )

    assert any("final_disposition mismatch" in error for error in errors)

    removed_errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies.iloc[0:0].copy(),
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("does not exactly match numerical trigger candidates" in error for error in removed_errors)


def test_validator_rejects_revision_source_row_and_price_lineage_tampering(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)

    wrong_revision = bundle.events.astype(object).copy()
    wrong_revision.loc[wrong_revision.index[0], "snapshot_revision"] = "r1"
    revision_errors = validator.validate_replay_bundle(
        wrong_revision,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("latest-revision pullback source rows" in error for error in revision_errors)

    wrong_hashes = bundle.events.astype(object).copy()
    wrong_hashes.loc[wrong_hashes.index[0], "source_row_sha256"] = "0" * 64
    wrong_hashes.loc[wrong_hashes.index[1], "price_source_sha256"] = "1" * 64
    hash_errors = validator.validate_replay_bundle(
        wrong_hashes,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("source_row_sha256 mismatch" in error for error in hash_errors)
    assert any("price_source_sha256 mismatch" in error for error in hash_errors)

    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest.loc[manifest["snapshot_revision"].eq("r2"), "supersedes_snapshot_sha256"] = (
        "f" * 64
    )
    manifest.to_csv(manifest_path, index=False, encoding="utf-8", lineterminator="\n")
    chain_errors = validator.validate_replay_bundle(
        bundle.events,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("supersedes_snapshot_sha256" in error for error in chain_errors)


def test_validator_recomputes_anomaly_trigger_and_rejects_gate_promotion(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(tmp_path)
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    anomaly_event_index = bundle.events.index[
        bundle.events["stock_id"].eq("2222")
        & bundle.events["primary_metric_included"].eq("True")
    ][0]
    cleared = bundle.events.astype(object).copy()
    cleared.loc[anomaly_event_index, "d5_anomaly_candidate"] = "False"
    cleared.loc[anomaly_event_index, "statistical_trigger_status"] = "not_triggered"
    cleared.loc[anomaly_event_index, "anomaly_candidate_horizons"] = ""
    cleared.loc[anomaly_event_index, "anomaly_disposition"] = "not_applicable"
    trigger_errors = validator.validate_replay_bundle(
        cleared,
        bundle.summary,
        bundle.anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("d5_anomaly_candidate mismatch" in error for error in trigger_errors)

    events = bundle.events.astype(object).copy()
    summary = bundle.summary.astype(object).copy()
    anomalies = bundle.anomalies.astype(object).copy()
    events.loc[events.index[0], "formal_use_allowed"] = "True"
    events.loc[events.index[0], "trade_eligible"] = "True"
    events.loc[events.index[0], "promotion_evidence_allowed"] = "True"
    events.loc[events.index[0], "operation_contract_status"] = "approved"
    summary.loc[summary.index[0], "promotion_evidence_allowed"] = "True"
    summary.loc[summary.index[0], "sensitivity_is_corrected_primary"] = "True"
    anomalies.loc[anomalies.index[0], "promotion_evidence_allowed"] = "True"
    gate_errors = validator.validate_replay_bundle(
        events,
        summary,
        anomalies,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    )
    assert any("formal_use_allowed" in error for error in gate_errors)
    assert any("trade_eligible" in error for error in gate_errors)
    assert any("promotion_evidence_allowed" in error for error in gate_errors)
    assert any("operation_contract_status" in error for error in gate_errors)
    assert any("corrected primary" in error for error in gate_errors)


def test_empty_anomaly_artifact_keeps_schema_and_validates_from_files(
    tmp_path: Path,
) -> None:
    snapshot_dir, manifest_path, price_dir = _fixture(
        tmp_path,
        target_rows=[_signal_row("1111")],
        include_r1=False,
        price_rows={"1111": [101] * 20},
    )
    bundle = _build(snapshot_dir, manifest_path, price_dir)
    output_dir = tmp_path / "research"
    events_path, summary_path, anomalies_path = producer.write_replay(bundle, output_dir)

    assert bundle.anomalies.empty
    assert set(validator.ANOMALY_REQUIRED_COLUMNS).issubset(bundle.anomalies.columns)
    assert validator.validate_files(
        events_path=events_path,
        summary_path=summary_path,
        anomalies_path=anomalies_path,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
    ) == []


def test_validator_imports_are_limited_to_stdlib_pandas_and_low_level_utils() -> None:
    source_path = SCRIPTS / "validate_pullback_short_reclaim_research.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    imported_modules: set[str] = set()
    project_imports: list[ast.ImportFrom] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)
            if node.module.split(".", 1)[0] not in sys.stdlib_module_names and (
                node.module.split(".", 1)[0] != "pandas"
            ):
                project_imports.append(node)

    allowed_roots = set(sys.stdlib_module_names) | {"pandas"}
    unexpected = {
        module
        for module in imported_modules
        if module.split(".", 1)[0] not in allowed_roots
        and not module.endswith("_utils")
    }
    assert unexpected == set()
    assert len(project_imports) == 2
    assert all(
        node.module is not None
        and "." not in node.module
        and node.module.endswith("_utils")
        and all(
            alias.name.startswith(("normalize_", "safe_", "select_", "snapshot_"))
            for alias in node.names
        )
        for node in project_imports
    )


def test_cli_write_is_wrapped_by_model_owned_artifact_guard() -> None:
    source_path = SCRIPTS / "build_pullback_short_reclaim_research.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    main = next(
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "main"
    )
    guards = [
        node
        for node in ast.walk(main)
        if isinstance(node, ast.With)
        and any(
            isinstance(item.context_expr, ast.Call)
            and isinstance(item.context_expr.func, ast.Name)
            and item.context_expr.func.id == "model_owned_artifact_guard"
            for item in node.items
        )
    ]

    assert len(guards) == 1
    preflight_statement = next(
        node
        for node in main.body
        if isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Name)
        and node.value.func.id == "_preflight_model_owned_outputs"
    )
    guard_statement = next(node for node in main.body if node is guards[0])
    assert main.body.index(preflight_statement) < main.body.index(guard_statement)


def test_cli_without_registered_ownership_leaves_no_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry_path = tmp_path / "config/model_research_artifact_ownership.csv"
    _write_csv(
        registry_path,
        [
            {
                "owner_model_id": "unrelated_model",
                "producer": "unrelated_producer",
                "artifact_glob": "output/latest/research_backtest/unrelated_*",
                "artifact_class": "model_research_output",
                "change_policy": "model_owned_write",
                "formal_evidence_status": "research_only",
            }
        ],
    )
    monkeypatch.setattr(producer, "ROOT", tmp_path)
    output_dir = tmp_path / "output/latest/research_backtest"

    with pytest.raises(RuntimeError, match="unregistered artifact change"):
        producer.main([])

    assert not output_dir.exists()
    assert all(
        not path.exists() for path in producer._replay_output_paths(output_dir)
    )
