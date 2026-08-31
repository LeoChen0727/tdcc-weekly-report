from __future__ import annotations

import importlib.metadata
import inspect
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_revenue_unreacted_range_operation_readiness as syncer  # noqa: E402


_REAL_LOAD_REGISTERED_PRICE_FRAMES = syncer._load_registered_price_frames
_REAL_VALIDATE_FORMAL_ADAPTER_RUNTIME = syncer.validate_formal_adapter_runtime
_CURRENT_REGISTERED_PRICE_FRAMES: dict[str, pd.DataFrame] | None = None
_BASELINE_MANIFEST = pd.read_csv(
    ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
).fillna("")
_BASELINE_MANIFEST_ROW = _BASELINE_MANIFEST.iloc[0]
_BASELINE_OBSERVED = _BASELINE_MANIFEST_ROW["observed_through_date"]
_BASELINE_REPLAY = pd.read_csv(
    ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
).fillna("")
_BASELINE_SOURCE = syncer._normalize_replay_source(_BASELINE_REPLAY)
_BASELINE_STOCK_IDS = {
    syncer._stock_id(value) for value in _BASELINE_SOURCE["stock_id"]
}
_BASELINE_PRICE_SHA = syncer._parse_price_semantic_projection_stock_sha_set(
    _BASELINE_MANIFEST_ROW
)


def test_canonical_anomaly_gate_requires_isolated_exact_pass_protocol(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    observed: dict[str, object] = {}

    def completed(command: list[str], **kwargs: object) -> SimpleNamespace:
        observed["command"] = command
        observed["kwargs"] = kwargs
        return SimpleNamespace(
            returncode=0,
            stdout=(
                "PASS: revenue_unreacted_range anomaly dispositions validated; "
                "rows=9; effective_blockers=0; verified_real_extreme=8; "
                "verified_data_error_repaired=1; "
                "raw-byte and line-ending identities=diagnostic-only\n"
            ),
            stderr="",
        )

    monkeypatch.setattr(syncer.subprocess, "run", completed)
    result = syncer.validate_current_anomaly_dispositions(
        ROOT,
        require_effective_nonblocking=True,
    )

    assert result.errors == ()
    assert observed["command"][:3] == [sys.executable, "-I", "-B"]
    assert observed["command"][-1] == "--require-effective-nonblocking"
    assert observed["kwargs"]["timeout"] == 300


@pytest.mark.parametrize(
    ("stdout", "stderr", "expected"),
    [
        ("unexpected success\n", "", "unknown output"),
        ("", "unexpected stderr", "emitted stderr"),
    ],
)
def test_canonical_anomaly_gate_rejects_nonprotocol_success(
    monkeypatch: pytest.MonkeyPatch,
    stdout: str,
    stderr: str,
    expected: str,
) -> None:
    monkeypatch.setattr(
        syncer.subprocess,
        "run",
        lambda *_args, **_kwargs: SimpleNamespace(
            returncode=0,
            stdout=stdout,
            stderr=stderr,
        ),
    )
    result = syncer.validate_current_anomaly_dispositions(
        ROOT,
        require_effective_nonblocking=True,
    )

    assert any(expected in error for error in result.errors)


def test_disabled_adapter_gate_uses_exact_isolated_command_and_protocol(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    observed: dict[str, object] = {}

    def committed_source(
        repo: Path,
        logical_path: str,
    ) -> syncer.AttestedAdapterSource:
        assert repo == ROOT
        return syncer.AttestedAdapterSource(
            logical_path=logical_path,
            committed_object_id="a" * 40,
            blob=(ROOT / logical_path).read_bytes(),
        )

    def completed(command: list[str], **kwargs: object) -> SimpleNamespace:
        observed["command"] = command
        observed["kwargs"] = kwargs
        return SimpleNamespace(
            returncode=0,
            stdout=syncer.REVENUE_ADAPTER_VALIDATION_PASS + "\n",
            stderr="",
        )

    monkeypatch.setattr(syncer, "_committed_adapter_source", committed_source)
    monkeypatch.setattr(syncer.subprocess, "run", completed)

    result = syncer.validate_disabled_adapter_preparation(ROOT)

    assert result == syncer.DisabledAdapterPreparationValidationResult(
        validator_rel=syncer.REVENUE_ADAPTER_VALIDATOR_REL,
        module_rel=syncer.REVENUE_ADAPTER_MODULE_REL,
        protocol_line=syncer.REVENUE_ADAPTER_VALIDATION_PASS,
    )
    assert observed["command"] == [
        sys.executable,
        "-I",
        "-B",
        observed["command"][3],
        "--phase",
        "disabled-preparation",
        "--module",
        observed["command"][7],
    ]
    command = observed["command"]
    kwargs = observed["kwargs"]
    isolated_root = Path(kwargs["cwd"])
    assert isolated_root != ROOT
    assert Path(command[3]).parent == isolated_root / "scripts"
    assert Path(command[7]).parent == isolated_root / "scripts"
    assert Path(command[3]).name == Path(syncer.REVENUE_ADAPTER_VALIDATOR_REL).name
    assert Path(command[7]).name == Path(syncer.REVENUE_ADAPTER_MODULE_REL).name
    assert kwargs["timeout"] == 300
    assert kwargs["check"] is False
    assert kwargs["env"]["PYTHONNOUSERSITE"] == "1"
    assert "adapter_result" not in inspect.signature(
        syncer.summarize_revenue_promotion_readiness
    ).parameters


@pytest.mark.parametrize(
    ("returncode", "stdout", "stderr", "message"),
    [
        (0, "unexpected success\n", "", "protocol missing"),
        (
            0,
            (
                syncer.REVENUE_ADAPTER_VALIDATION_PASS
                + "\n"
                + syncer.REVENUE_ADAPTER_VALIDATION_PASS
                + "\n"
            ),
            "",
            "protocol missing",
        ),
        (0, syncer.REVENUE_ADAPTER_VALIDATION_PASS + "\n", "warning\n", "stderr"),
        (1, "ERROR: rejected\n", "", "failed with exit 1"),
    ],
)
def test_disabled_adapter_gate_rejects_nonexact_protocol(
    monkeypatch: pytest.MonkeyPatch,
    returncode: int,
    stdout: str,
    stderr: str,
    message: str,
) -> None:
    monkeypatch.setattr(
        syncer,
        "_committed_adapter_source",
        lambda _repo, logical_path: syncer.AttestedAdapterSource(
            logical_path=logical_path,
            committed_object_id="a" * 40,
            blob=(ROOT / logical_path).read_bytes(),
        ),
    )
    monkeypatch.setattr(
        syncer.subprocess,
        "run",
        lambda *_args, **_kwargs: SimpleNamespace(
            returncode=returncode,
            stdout=stdout,
            stderr=stderr,
        ),
    )

    with pytest.raises(RuntimeError, match=message):
        syncer.validate_disabled_adapter_preparation(ROOT)


def test_disabled_adapter_gate_fails_closed_on_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        syncer,
        "_committed_adapter_source",
        lambda _repo, logical_path: syncer.AttestedAdapterSource(
            logical_path=logical_path,
            committed_object_id="a" * 40,
            blob=(ROOT / logical_path).read_bytes(),
        ),
    )
    monkeypatch.setattr(
        syncer.subprocess,
        "run",
        lambda command, **_kwargs: (_ for _ in ()).throw(
            subprocess.TimeoutExpired(command, timeout=300)
        ),
    )

    with pytest.raises(RuntimeError, match="timed out"):
        syncer.validate_disabled_adapter_preparation(ROOT)


def test_disabled_adapter_source_requires_exact_committed_git_blob_identity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(command: list[str], **_kwargs: object) -> SimpleNamespace:
        calls.append(command)
        object_id = "a" * 40 if "rev-parse" in command else "b" * 40
        return SimpleNamespace(returncode=0, stdout=object_id + "\n", stderr="")

    monkeypatch.setattr(syncer.subprocess, "run", fake_run)

    with pytest.raises(RuntimeError, match="differs from committed HEAD blob"):
        syncer._committed_adapter_source(
            ROOT,
            syncer.REVENUE_ADAPTER_VALIDATOR_REL,
        )

    assert len(calls) == 2
    assert "rev-parse" in calls[0]
    assert "hash-object" in calls[1]


def test_disabled_adapter_executes_materialized_head_blobs_after_worktree_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    scripts = repo / "scripts"
    scripts.mkdir(parents=True)
    worktree_validator = scripts / Path(syncer.REVENUE_ADAPTER_VALIDATOR_REL).name
    worktree_module = scripts / Path(syncer.REVENUE_ADAPTER_MODULE_REL).name
    worktree_validator.write_bytes(b"mutable validator")
    worktree_module.write_bytes(b"mutable module")
    head_blobs = {
        syncer.REVENUE_ADAPTER_VALIDATOR_REL: b"exact HEAD validator",
        syncer.REVENUE_ADAPTER_MODULE_REL: b"exact HEAD module",
    }

    monkeypatch.setattr(
        syncer,
        "_committed_adapter_source",
        lambda _repo, logical_path: syncer.AttestedAdapterSource(
            logical_path=logical_path,
            committed_object_id="a" * 40,
            blob=head_blobs[logical_path],
        ),
    )

    def completed(command: list[str], **_kwargs: object) -> SimpleNamespace:
        worktree_validator.write_bytes(b"mutated after attest")
        worktree_module.write_bytes(b"mutated after attest")
        assert Path(command[3]) != worktree_validator
        assert Path(command[7]) != worktree_module
        assert Path(command[3]).read_bytes() == head_blobs[
            syncer.REVENUE_ADAPTER_VALIDATOR_REL
        ]
        assert Path(command[7]).read_bytes() == head_blobs[
            syncer.REVENUE_ADAPTER_MODULE_REL
        ]
        return SimpleNamespace(
            returncode=0,
            stdout=syncer.REVENUE_ADAPTER_VALIDATION_PASS + "\n",
            stderr="",
        )

    monkeypatch.setattr(syncer.subprocess, "run", completed)

    syncer.validate_disabled_adapter_preparation(repo)


@pytest.fixture(autouse=True)
def cache_verified_current_cheap_inputs(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unit cases reuse one verified current cheap input load per pytest process."""

    def cached_registered_prices(
        repo_root: Path | str,
        detail: pd.DataFrame,
        *,
        observed_through: str,
        per_stock_manifest_sha: dict[str, str],
        required_stock_ids: set[str] | None = None,
    ) -> dict[str, pd.DataFrame]:
        global _CURRENT_REGISTERED_PRICE_FRAMES
        repo = Path(repo_root).resolve()
        requested = {
            syncer._stock_id(value) for value in detail.get("stock_id", [])
        } | {
            syncer._stock_id(value) for value in (required_stock_ids or set())
        }
        if (
            repo != ROOT
            or observed_through != _BASELINE_OBSERVED
            or not requested.issubset(_BASELINE_STOCK_IDS)
        ):
            return _REAL_LOAD_REGISTERED_PRICE_FRAMES(
                repo,
                detail,
                observed_through=observed_through,
                per_stock_manifest_sha=per_stock_manifest_sha,
                required_stock_ids=required_stock_ids,
            )
        if _CURRENT_REGISTERED_PRICE_FRAMES is None:
            _CURRENT_REGISTERED_PRICE_FRAMES = {}
        for stock_id in requested:
            if stock_id in _CURRENT_REGISTERED_PRICE_FRAMES:
                continue
            path = ROOT / syncer.PRICE_HISTORY_DIR_REL / f"{stock_id}.csv"
            dates = pd.read_csv(path, usecols=["date"], dtype=str).fillna("")
            dates["date"] = dates["date"].map(
                lambda value: syncer._strict_date(
                    value, f"verified test price date {stock_id}"
                )
            )
            dates = dates.loc[
                dates["date"].le(_BASELINE_OBSERVED), ["date"]
            ].reset_index(drop=True)
            assert not dates["date"].duplicated().any()
            assert dates["date"].is_monotonic_increasing
            _CURRENT_REGISTERED_PRICE_FRAMES[stock_id] = dates
        return {
            stock_id: _CURRENT_REGISTERED_PRICE_FRAMES[stock_id]
            for stock_id in requested
        }

    monkeypatch.setattr(
        syncer,
        "_load_registered_price_frames",
        cached_registered_prices,
    )
    monkeypatch.setattr(
        syncer,
        "validate_formal_adapter_runtime",
        lambda _repo: syncer.FormalAdapterRuntimeValidationResult(
            operation_module_path=syncer.REVENUE_FORMAL_ADAPTER_MODULE_REL,
            operation_module_canonical_sha256="1" * 64,
            adapter_artifact_id=syncer.REVENUE_FORMAL_ADAPTER_ARTIFACT_ID,
            adapter_artifact_version=syncer.REVENUE_FORMAL_ADAPTER_APPROVAL_VERSION,
            adapter_artifact_path=syncer.REVENUE_FORMAL_ADAPTER_ARTIFACT_REL,
            adapter_artifact_canonical_sha256="2" * 64,
            adapter_schema_version=syncer.REVENUE_FORMAL_ADAPTER_SCHEMA_VERSION,
            lifecycle_contract_version=syncer.REVENUE_FORMAL_ADAPTER_LIFECYCLE_VERSION,
            row_count=12,
            data_row_count=0,
            sections=syncer.REVENUE_FORMAL_ADAPTER_SECTIONS,
        ),
    )


def readiness_row(model_id: str) -> dict[str, str]:
    row = {field_name: "" for field_name in syncer.LEGACY_COLUMNS}
    row.update(
        {
            "generated_at": "committed-time",
            "model_id": model_id,
            "model_name_zh": "營收模型" if model_id == syncer.MODEL_ID else "其他模型",
            "parity_status": "stale" if model_id == syncer.MODEL_ID else "production_parity",
            "blocker": "stale blocker" if model_id == syncer.MODEL_ID else "unchanged blocker",
            "operation_module_status": "baseline_only_no_validated_operation_module",
            "daily_adapter_status": "not_started",
            "approved_for_daily": "False" if model_id == syncer.MODEL_ID else "True",
            "approval_status": "not_started",
            "presentation_allowed": "False" if model_id == syncer.MODEL_ID else "True",
            "operation_directive_level": "no_operation_directive",
            "pdf_integration_status": "not_started",
            "packet_integration_status": "not_started",
            "registry_pattern_count": "0",
            "registry_current_model_pattern_count": "0",
            "registry_best_sample_size": "0",
            "daily_adapter_row_count": "0",
            "daily_adapter_data_row_count": "0",
            "status_note_zh": "保留原值",
        }
    )
    return row


def revenue_summary() -> dict[str, str | int]:
    return {
        "parity_status": "research_matrix_complete",
        "blocker": "forward_holdout_v2_mature=0/20",
        "operation_module_status": "disabled_adapter_preparation_validated",
        "daily_adapter_status": "disabled_no_runtime_artifact",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "operation_module_id": (
            "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
        ),
        "operation_module_path": "",
        "operation_module_canonical_sha256": "",
        "adapter_artifact_id": "",
        "adapter_artifact_version": "",
        "adapter_artifact_path": "",
        "adapter_artifact_canonical_sha256": "",
        "adapter_schema_version": "",
        "lifecycle_contract_version": "",
        "approval_version": "",
        "presentation_allowed": "False",
        "production_allowed": "False",
        "operation_directive_level": "no_operation_directive",
        "pdf_integration_status": "not_started",
        "packet_integration_status": "not_started",
        "registry_pattern_count": 1,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": "source_mid_falling",
        "registry_best_sample_size": 53,
        "registry_best_win_rate": "77.3585",
        "registry_best_median_return": "9.4077",
        "daily_adapter_row_count": 0,
        "daily_adapter_data_row_count": 0,
        "daily_adapter_sections": "",
        "status_note_zh": "僅月營收；正式權限維持關閉。",
    }


def test_v6_summary_enables_formal_adapter_and_keeps_holdout_as_monitoring(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        syncer,
        "validate_formal_adapter_runtime",
        lambda _repo: syncer.FormalAdapterRuntimeValidationResult(
            operation_module_path=syncer.REVENUE_FORMAL_ADAPTER_MODULE_REL,
            operation_module_canonical_sha256="1" * 64,
            adapter_artifact_id=syncer.REVENUE_FORMAL_ADAPTER_ARTIFACT_ID,
            adapter_artifact_version=(
                "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
            ),
            adapter_artifact_path=syncer.REVENUE_FORMAL_ADAPTER_ARTIFACT_REL,
            adapter_artifact_canonical_sha256="2" * 64,
            adapter_schema_version=syncer.REVENUE_FORMAL_ADAPTER_SCHEMA_VERSION,
            lifecycle_contract_version=(
                syncer.REVENUE_FORMAL_ADAPTER_LIFECYCLE_VERSION
            ),
            row_count=12,
            data_row_count=0,
            sections=syncer.REVENUE_FORMAL_ADAPTER_SECTIONS,
        ),
    )
    promotion = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL,
        dtype=str,
    ).fillna("")

    summary = syncer.summarize_revenue_promotion_readiness(
        promotion,
        pd.DataFrame(),
        holdout,
        holdout_detail=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
        ).fillna(""),
        holdout_summary=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
        ).fillna(""),
        replay_source=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
        ).fillna(""),
        source_projection_manifest=pd.read_csv(
            ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
        ).fillna(""),
        repo_root=ROOT,
    )

    assert summary["blocker"] == "none"
    assert summary["parity_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    assert summary["operation_module_status"] == (
        "approved_operation_v2_provisional_backtest_supported_oos_unconfirmed"
    )
    assert summary["daily_adapter_status"] == "ready_empty_no_operation_rows"
    assert summary["formal_model_use_allowed"] == "True"
    assert summary["approved_for_daily"] == "True"
    assert summary["presentation_allowed"] == "True"
    assert summary["production_allowed"] == "True"
    assert summary["approval_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    assert summary["pdf_integration_status"] == "pdf_integrated_daily_adapter"
    assert summary["packet_integration_status"] == "pending_packet_consumer"
    assert summary["daily_adapter_row_count"] == 12
    assert summary["daily_adapter_data_row_count"] == 0
    assert summary["daily_adapter_sections"] == ",".join(
        syncer.REVENUE_FORMAL_ADAPTER_SECTIONS
    )


def legacy_readiness() -> pd.DataFrame:
    return pd.DataFrame(
        [
            readiness_row("other_model"),
            readiness_row(syncer.MODEL_ID),
            readiness_row("second_other_model"),
        ],
        columns=syncer.LEGACY_COLUMNS,
    )


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def formal_adapter_runtime_repo(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    committed_history_semantic_drift: bool = False,
) -> tuple[Path, Path, Path, bytes]:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "config", "core.autocrlf", "false")

    monkeypatch.setattr(syncer, "REVENUE_FORMAL_ADAPTER_MODULE_REL", "module.py")
    monkeypatch.setattr(syncer, "REVENUE_FORMAL_ADAPTER_VALIDATOR_REL", "validator.py")
    monkeypatch.setattr(syncer, "REVENUE_FORMAL_ADAPTER_ARTIFACT_REL", "runtime.csv")
    monkeypatch.setattr(syncer, "REVENUE_FORMAL_ADAPTER_HISTORY_DIRECTORY_REL", "history")

    (repo / "module.py").write_text("ADAPTER_VERSION = 'test'\n", encoding="utf-8")
    (repo / "validator.py").write_text(
        "import csv\n"
        "import sys\n"
        "from pathlib import Path\n"
        "artifact = Path(sys.argv[sys.argv.index('--artifact') + 1])\n"
        "with artifact.open(encoding='utf-8-sig', newline='') as handle:\n"
        "    rows = list(csv.DictReader(handle))\n"
        "data_rows = sum(row['row_type'] == 'data' for row in rows)\n"
        "print('PASS: formal revenue operation adapter is independently valid '"
        "f'asof=20260828 rows={len(rows)} data_rows={data_rows} '"
        "f'empty_rows={len(rows) - data_rows}')\n",
        encoding="utf-8",
    )

    runtime_semantic = syncer._formal_adapter_semantic_payload(
        (ROOT / "output/latest/daily_revenue_unreacted_range_operation_section_latest.csv").read_bytes(),
        "runtime fixture",
    )
    runtime_path = repo / "runtime.csv"
    runtime_path.write_bytes(runtime_semantic)
    runtime_sha = syncer.hashlib.sha256(runtime_semantic).hexdigest()
    history_path = (
        repo
        / "history"
        / (
            "daily_revenue_unreacted_range_operation_section_"
            f"{syncer.REVENUE_FORMAL_ADAPTER_REPORT_DATE}_{runtime_sha}.csv"
        )
    )
    history_path.parent.mkdir(parents=True)
    history_semantic = runtime_semantic
    if committed_history_semantic_drift:
        history_semantic = runtime_semantic.replace(
            b"post_launch_monitoring_non_hard_no_tuning",
            b"post_launch_monitoring_semantic_drift",
            1,
        )
        assert history_semantic != runtime_semantic
    history_path.write_bytes(history_semantic)
    git(repo, "add", ".")
    git(repo, "commit", "-m", "formal adapter fixture")
    return repo, runtime_path, history_path, runtime_semantic


def exact_attestation(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    replay_source: pd.DataFrame,
) -> dict[str, object]:
    row = manifest.iloc[0]
    return {
        "data_contract_version": row["data_contract_version"],
        "data_contract_sha256": row["data_contract_sha256"],
        "source_detail_promotion_semantic_sha256": (
            syncer._promotion_semantic_source_sha256(replay_source)
        ),
        "price_semantic_projection_version": row[
            "price_semantic_projection_version"
        ],
        "price_semantic_projection_schema_sha256": row[
            "price_semantic_projection_schema_sha256"
        ],
        "price_semantic_projection_columns": row[
            "price_semantic_projection_columns"
        ],
        "price_semantic_projection_decimal_scale": int(
            row["price_semantic_projection_decimal_scale"]
        ),
        "price_semantic_projection_canonical_sha256": row[
            "price_semantic_projection_canonical_sha256"
        ],
        "price_semantic_projection_stock_canonical_sha256s": (
            syncer._parse_price_semantic_projection_stock_sha_set(row)
        ),
        "price_semantic_projection_stock_count": row[
            "price_semantic_projection_stock_count"
        ],
        "price_semantic_projection_row_count": row[
            "price_semantic_projection_row_count"
        ],
        "price_semantic_projection_role": row[
            "price_semantic_projection_role"
        ],
        "price_semantic_projection_migration_id": row[
            "price_semantic_projection_migration_id"
        ],
        "price_semantic_projection_authorization_reference": row[
            "price_semantic_projection_authorization_reference"
        ],
        "observed_through_date": row["observed_through_date"],
        "expected_manifest_canonical_sha256": (
            syncer._promotion_semantic_frame_sha256(
                manifest,
                frame_name="manifest",
            )
        ),
        "expected_detail_canonical_sha256": (
            syncer._promotion_semantic_frame_sha256(
                detail,
                frame_name="detail",
            )
        ),
        "expected_summary_canonical_sha256": (
            syncer._promotion_semantic_frame_sha256(
                summary,
                frame_name="summary",
            )
        ),
        "replay_child_mode": syncer.EXACT_REPLAY_CHILD_MODE,
        "replay_child_modules": list(syncer.EXACT_REPLAY_CHILD_MODULES),
    }


def exact_replay_protocol_payload(
    head_sha: str,
    tree_sha: str,
    runtime_fingerprint: dict[str, str],
) -> dict[str, object]:
    frame_attestations = {
        frame_name: {
            "canonical_sha256": digest_token * 64,
            "row_count": 1,
            "column_count": 1,
        }
        for frame_name, digest_token in zip(
            ("manifest", "detail", "summary", "comparison", "anomaly"),
            ("a", "b", "c", "d", "e"),
        )
    }
    return {
        "protocol_version": syncer.EXACT_REPLAY_PROTOCOL_VERSION,
        "commit_sha": head_sha,
        "tree_sha": tree_sha,
        "runtime_fingerprint": runtime_fingerprint,
        "capture_id": "f" * 64,
        "data_contract_version": syncer.DATA_CONTRACT_VERSION,
        "data_contract_sha256": syncer.DATA_CONTRACT_SHA256,
        "source_detail_promotion_semantic_sha256": "6" * 64,
        "price_semantic_projection_version": (
            syncer.PRICE_SEMANTIC_PROJECTION_VERSION
        ),
        "price_semantic_projection_schema_sha256": (
            syncer.PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_columns": "|".join(
            syncer.PRICE_SEMANTIC_PROJECTION_COLUMNS
        ),
        "price_semantic_projection_decimal_scale": (
            syncer.PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE
        ),
        "price_semantic_projection_stock_canonical_sha256s": {
            "2330": "8" * 64
        },
        "price_semantic_projection_canonical_sha256": "9" * 64,
        "price_semantic_projection_stock_count": 1,
        "price_semantic_projection_row_count": 10,
        "price_semantic_projection_role": syncer.PRICE_SEMANTIC_PROJECTION_ROLE,
        "price_semantic_projection_migration_id": (
            syncer.PRICE_SEMANTIC_PROJECTION_MIGRATION_ID
        ),
        "price_semantic_projection_authorization_reference": (
            syncer.PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE
        ),
        "observed_through_date": "20260828",
        "expected_manifest_canonical_sha256": "a" * 64,
        "expected_detail_canonical_sha256": "b" * 64,
        "expected_summary_canonical_sha256": "c" * 64,
        "frame_attestations": frame_attestations,
        "replay_child_mode": syncer.EXACT_REPLAY_CHILD_MODE,
        "replay_child_modules": list(syncer.EXACT_REPLAY_CHILD_MODULES),
    }


def completed_process(
    *,
    returncode: int = 0,
    stdout: str = "",
    stderr: str = "",
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(
        args=["test"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


def test_build_replaces_only_revenue_and_keeps_non_revenue_fields_exact() -> None:
    base = legacy_readiness()
    expected_non_revenue = base[
        ~base["model_id"].eq(syncer.MODEL_ID)
    ].reset_index(drop=True)

    actual = syncer.build_revenue_only_readiness(
        base,
        revenue_summary(),
        generated_at="new-revenue-time",
    )

    assert tuple(actual.columns) == syncer.TARGET_COLUMNS
    assert actual["model_id"].tolist() == base["model_id"].tolist()
    actual_non_revenue = actual[
        ~actual["model_id"].eq(syncer.MODEL_ID)
    ].reset_index(drop=True)
    pd.testing.assert_frame_equal(
        actual_non_revenue[list(syncer.LEGACY_COLUMNS)],
        expected_non_revenue,
    )
    assert actual_non_revenue["generated_at"].eq("committed-time").all()
    for field_name in syncer.REVENUE_PERMISSION_COLUMNS:
        assert actual_non_revenue[field_name].eq("").all()

    revenue = actual[actual["model_id"].eq(syncer.MODEL_ID)].iloc[0]
    assert revenue["generated_at"] == "new-revenue-time"
    assert revenue["model_name_zh"] == "營收模型"
    for field_name, expected in revenue_summary().items():
        assert revenue[field_name] == str(expected)


def test_build_accepts_only_canonical_extended_disabled_source() -> None:
    base = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="first-time",
    )
    rebuilt = syncer.build_revenue_only_readiness(
        base,
        revenue_summary(),
        generated_at="second-time",
    )
    non_revenue = rebuilt[~rebuilt["model_id"].eq(syncer.MODEL_ID)]
    assert non_revenue["generated_at"].eq("committed-time").all()
    assert rebuilt.loc[
        rebuilt["model_id"].eq(syncer.MODEL_ID), "generated_at"
    ].item() == "second-time"

    unsafe = base.copy()
    unsafe.loc[unsafe["model_id"].eq(syncer.MODEL_ID), "production_allowed"] = "True"
    with pytest.raises(
        RuntimeError,
        match="permission quartet disagrees at production_allowed",
    ):
        syncer.build_revenue_only_readiness(
            unsafe,
            revenue_summary(),
            generated_at="unsafe",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("duplicate", "duplicate model_id"),
        ("blank", "blank model_id"),
        ("schema", "schema drift"),
        ("noncanonical_bool", "non-canonical values"),
    ),
)
def test_build_fails_closed_on_identity_or_schema_drift(
    mutation: str,
    message: str,
) -> None:
    base = legacy_readiness()
    if mutation == "duplicate":
        base.loc[2, "model_id"] = "other_model"
    elif mutation == "blank":
        base.loc[2, "model_id"] = ""
    elif mutation == "schema":
        base["unexpected"] = ""
    elif mutation == "noncanonical_bool":
        base.loc[0, "approved_for_daily"] = "true"

    with pytest.raises(RuntimeError, match=message):
        syncer.build_revenue_only_readiness(
            base,
            revenue_summary(),
            generated_at="new-time",
        )


def test_build_fails_closed_on_same_model_summary_schema_drift() -> None:
    incomplete = revenue_summary()
    incomplete.pop("blocker")
    with pytest.raises(RuntimeError, match="summary schema drift"):
        syncer.build_revenue_only_readiness(
            legacy_readiness(),
            incomplete,
            generated_at="new-time",
        )


def test_formal_adapter_runtime_tolerates_bom_and_crlf_transport_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, runtime_path, history_path, runtime_semantic = formal_adapter_runtime_repo(
        tmp_path,
        monkeypatch,
    )
    transport_variant = b"\xef\xbb\xbf" + runtime_semantic.replace(b"\n", b"\r\n")
    runtime_path.write_bytes(transport_variant)
    history_path.write_bytes(transport_variant)

    result = _REAL_VALIDATE_FORMAL_ADAPTER_RUNTIME(repo)

    assert result.adapter_artifact_canonical_sha256 == syncer.hashlib.sha256(
        runtime_semantic
    ).hexdigest()
    assert result.row_count > 0
    assert result.data_row_count == 0


@pytest.mark.parametrize("drift_location", ("worktree_history", "committed_history"))
def test_formal_adapter_runtime_rejects_history_semantic_drift(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    drift_location: str,
) -> None:
    repo, _runtime_path, history_path, runtime_semantic = formal_adapter_runtime_repo(
        tmp_path,
        monkeypatch,
        committed_history_semantic_drift=drift_location == "committed_history",
    )
    if drift_location == "worktree_history":
        drifted = runtime_semantic.replace(
            b"post_launch_monitoring_non_hard_no_tuning",
            b"post_launch_monitoring_semantic_drift",
            1,
        )
        assert drifted != runtime_semantic
        history_path.write_bytes(drifted)

    with pytest.raises(RuntimeError, match="does not semantically bind"):
        _REAL_VALIDATE_FORMAL_ADAPTER_RUNTIME(repo)


def test_committed_source_treats_crlf_as_diagnostic_and_semantic_drift_as_error(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    source = repo / "source.csv"
    source.write_bytes(b"key,value\nrow,one\n")
    git(repo, "add", "source.csv")
    git(repo, "commit", "-m", "source")

    source.write_bytes(b"key,value\r\nrow,one\r\n")
    committed, diagnostic = syncer._committed_semantic_source(
        repo,
        "source.csv",
        csv_source=True,
    )
    assert committed == b"key,value\nrow,one\n"
    assert diagnostic is not None
    assert "diagnostic only" in diagnostic

    source.write_bytes(b"key,value\nrow,two\n")
    with pytest.raises(RuntimeError, match="semantic drift from HEAD"):
        syncer._committed_semantic_source(
            repo,
            "source.csv",
            csv_source=True,
        )


def test_committed_anomaly_source_treats_raw_file_sha_as_diagnostic_only(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    source = repo / syncer.ANOMALY_REGISTRY_REL
    source.parent.mkdir(parents=True)
    source.write_text(
        "operation_key,final_disposition,anomaly_source_raw_file_sha256s\n"
        "key-1,verified_real_extreme,raw-a\n",
        encoding="utf-8",
        newline="\n",
    )
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "canonical anomaly source")

    source.write_text(
        "operation_key,final_disposition,anomaly_source_raw_file_sha256s\r\n"
        "key-1,verified_real_extreme,raw-b\r\n",
        encoding="utf-8",
        newline="",
    )
    _committed, diagnostic = syncer._committed_semantic_source(
        repo,
        syncer.ANOMALY_REGISTRY_REL,
        csv_source=True,
    )
    assert diagnostic is not None
    assert "raw-file-SHA diagnostic only" in diagnostic

    source.write_text(
        "operation_key,final_disposition,anomaly_source_raw_file_sha256s\n"
        "key-1,verified_data_error,raw-b\n",
        encoding="utf-8",
        newline="\n",
    )
    with pytest.raises(RuntimeError, match="semantic drift from HEAD"):
        syncer._committed_semantic_source(
            repo,
            syncer.ANOMALY_REGISTRY_REL,
            csv_source=True,
        )


def test_committed_anomaly_source_keeps_raw_source_lineage_as_semantic_gate(
    tmp_path: Path,
) -> None:
    assert not syncer._is_transport_provenance_column("raw_source_lineage_status")
    assert 'startswith("raw_")' not in Path(syncer.__file__).read_text(encoding="utf-8")
    repo = tmp_path / "repo"
    source = repo / syncer.ANOMALY_REGISTRY_REL
    source.parent.mkdir(parents=True)
    source.write_text(
        "operation_key,final_disposition,raw_source_lineage_status\n"
        "key-1,verified_real_extreme,pass\n",
        encoding="utf-8",
        newline="\n",
    )
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "canonical anomaly source")

    source.write_text(
        "operation_key,final_disposition,raw_source_lineage_status\n"
        "key-1,verified_real_extreme,missing\n",
        encoding="utf-8",
        newline="\n",
    )
    with pytest.raises(RuntimeError, match="semantic drift from HEAD"):
        syncer._committed_semantic_source(
            repo,
            syncer.ANOMALY_REGISTRY_REL,
            csv_source=True,
        )


def test_bulk_registered_price_read_is_single_call_crlf_safe_and_semantic_strict(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    price_path = repo / syncer.PRICE_HISTORY_DIR_REL / "2330.csv"
    resolution_path = repo / syncer.PRICE_RESOLUTION_REL
    price_path.parent.mkdir(parents=True)
    resolution_path.parent.mkdir(parents=True, exist_ok=True)
    price_lf = b"date,open,close\n20260102,100,101\n"
    resolution_lf = (
        b"resolution_id,stock_id,resume_date,exchange_ratio\n"
    )
    price_path.write_bytes(price_lf)
    resolution_path.write_bytes(resolution_lf)
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "registered price inputs")
    logical_paths = [
        syncer.PRICE_RESOLUTION_REL,
        f"{syncer.PRICE_HISTORY_DIR_REL}/2330.csv",
    ]

    calls: list[tuple[list[str], dict[str, object]]] = []

    def counted_popen(
        argv: list[str], **kwargs: object
    ) -> subprocess.Popen[bytes]:
        calls.append((list(argv), dict(kwargs)))
        return subprocess.Popen(argv, **kwargs)

    price_path.write_bytes(price_lf.replace(b"\n", b"\r\n"))
    committed = syncer._bulk_committed_registered_price_sources(
        repo,
        logical_paths,
        popen_factory=counted_popen,
    )
    assert syncer._canonical_csv(
        committed[logical_paths[1]], logical_paths[1]
    ) == syncer._canonical_csv(price_lf, "expected-price")
    assert len(calls) == 1
    argv, kwargs = calls[0]
    assert argv == [
        "git",
        "--no-replace-objects",
        "cat-file",
        "--batch",
    ]
    assert "shell" not in kwargs
    assert kwargs["env"]["GIT_NO_REPLACE_OBJECTS"] == "1"

    for semantic_mutation in (
        b"date,open,close\n20260103,100,101\n",
        b"date,open,close\n20260102,100,999\n",
    ):
        calls.clear()
        price_path.write_bytes(semantic_mutation)
        with pytest.raises(RuntimeError, match="semantic drift from HEAD"):
            syncer._bulk_committed_registered_price_sources(
                repo,
                logical_paths,
                popen_factory=counted_popen,
            )
        assert len(calls) == 1


@pytest.mark.parametrize(
    ("payload", "message"),
    (
        (b"HEAD:config/source.csv missing\n", "source is missing"),
        (b"a" * 40 + b" tree 0\n\n", "not an exact blob"),
        (b"a" * 40 + b" blob 0\n\nextra", "unexpected extra output"),
    ),
)
def test_bulk_registered_price_batch_protocol_fails_closed(
    tmp_path: Path,
    payload: bytes,
    message: str,
) -> None:
    repo = tmp_path / "repo"
    source = repo / syncer.PRICE_RESOLUTION_REL
    source.parent.mkdir(parents=True)
    source.write_text("key,value\n", encoding="utf-8", newline="\n")
    seen_input: list[bytes] = []

    class FakeProcess:
        returncode = 0

        def communicate(self, *, input: bytes) -> tuple[bytes, bytes]:
            seen_input.append(input)
            return payload, b""

    def fake_popen(
        argv: list[str], **kwargs: object
    ) -> FakeProcess:
        assert argv == ["git", "--no-replace-objects", "cat-file", "--batch"]
        assert "shell" not in kwargs
        return FakeProcess()

    with pytest.raises(RuntimeError, match=message):
        syncer._bulk_committed_registered_price_sources(
            repo,
            [syncer.PRICE_RESOLUTION_REL],
            popen_factory=fake_popen,
        )
    assert seen_input == [f"HEAD:{syncer.PRICE_RESOLUTION_REL}\n".encode()]


def test_load_committed_inputs_rejects_committed_output_docs_mirror_drift(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    csv_data = legacy_readiness().to_csv(index=False, lineterminator="\n").encode()
    drifted_csv = csv_data.replace(b"unchanged blocker", b"drifted blocker", 1)
    for logical_path in syncer.READINESS_MIRROR_RELS:
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if logical_path == syncer.DOCS_CSV_REL:
            path.write_bytes(drifted_csv)
        elif logical_path.endswith(".csv"):
            path.write_bytes(csv_data)
        else:
            path.write_text("# committed readiness\n", encoding="utf-8")
    for logical_path in syncer.CANONICAL_SOURCE_RELS:
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("model_id\nrevenue_unreacted_range\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "drifted mirrors")

    with pytest.raises(RuntimeError, match="output/docs readiness CSV mirrors differ"):
        syncer.load_committed_inputs(repo)


def test_write_scope_is_exact_four_byte_paired_mirrors(tmp_path: Path) -> None:
    readiness = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="new-time",
    )
    syncer.write_readiness_mirrors(
        tmp_path,
        readiness,
        generated_at="new-time",
    )

    written = {
        path.relative_to(tmp_path).as_posix()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    assert written == set(syncer.READINESS_MIRROR_RELS)
    assert (
        tmp_path / syncer.OUT_CSV_REL
    ).read_bytes() == (tmp_path / syncer.DOCS_CSV_REL).read_bytes()
    markdown = (tmp_path / syncer.OUT_MD_REL).read_bytes()
    assert markdown == (tmp_path / syncer.DOCS_MD_REL).read_bytes()
    text = markdown.decode("utf-8")
    assert "| formal_model_use_allowed |" in text
    assert "| production_allowed |" in text
    status_row = next(
        line for line in text.splitlines() if f"| {syncer.MODEL_ID} |" in line
    )
    assert status_row.count("False") >= 4


def test_current_canonical_sources_build_exact_v6_provisional_revenue_row() -> None:
    base = pd.read_csv(ROOT / syncer.OUT_CSV_REL, dtype=str).fillna("")
    promotion = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    anomalies = pd.read_csv(
        ROOT / syncer.ANOMALY_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL,
        dtype=str,
    ).fillna("")
    detail = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL,
        dtype=str,
    ).fillna("")
    holdout_summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL,
        dtype=str,
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL,
        dtype=str,
    ).fillna("")
    source_projection_manifest = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL,
        dtype=str,
    ).fillna("")
    syncer.validate_revenue_readiness_exact_replay(
        holdout,
        holdout_detail=detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        repo_root=ROOT,
    )
    summary = syncer.summarize_revenue_promotion_readiness(
        promotion,
        anomalies,
        holdout,
        holdout_detail=detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        source_projection_manifest=source_projection_manifest,
        repo_root=ROOT,
    )

    readiness = syncer.build_revenue_only_readiness(
        base,
        summary,
        generated_at="deterministic-test-time",
    )
    revenue = readiness[readiness["model_id"].eq(syncer.MODEL_ID)].iloc[0]
    assert revenue["blocker"] == "none"
    assert revenue["parity_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    assert revenue["operation_module_status"] == (
        "approved_operation_v2_provisional_backtest_supported_oos_unconfirmed"
    )
    assert revenue["daily_adapter_status"] == "ready_empty_no_operation_rows"
    assert revenue["operation_module_id"] == (
        "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
    )
    assert revenue["daily_adapter_row_count"] == "12"
    assert revenue["daily_adapter_data_row_count"] == "0"
    assert revenue["daily_adapter_sections"] == ",".join(
        syncer.REVENUE_FORMAL_ADAPTER_SECTIONS
    )
    assert revenue["formal_model_use_allowed"] == "True"
    assert revenue["approved_for_daily"] == "True"
    assert revenue["presentation_allowed"] == "True"
    assert revenue["production_allowed"] == "True"
    assert revenue["pdf_integration_status"] == "pdf_integrated_daily_adapter"
    assert revenue["packet_integration_status"] == "pending_packet_consumer"


def test_v4_profile_remains_compatible_without_consuming_adapter_gate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    promotion = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("").iloc[:-2]
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL,
        dtype=str,
    ).fillna("")
    monkeypatch.setattr(
        syncer,
        "validate_disabled_adapter_preparation",
        lambda _repo: (_ for _ in ()).throw(
            AssertionError("v4 profile invoked the v5 adapter gate")
        ),
    )

    summary = syncer.summarize_revenue_promotion_readiness(
        promotion,
        anomalies,
        holdout,
        holdout_detail=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
        ).fillna(""),
        holdout_summary=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
        ).fillna(""),
        replay_source=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
        ).fillna(""),
        source_projection_manifest=pd.read_csv(
            ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
        ).fillna(""),
        repo_root=ROOT,
    )

    assert summary["blocker"].endswith("formal_adapter=not_started")
    assert summary["operation_module_status"] == (
        "research_matrix_complete_formal_adapter_not_started"
    )
    assert summary["daily_adapter_status"] == "not_started"
    assert summary["operation_module_id"] == ""


@pytest.mark.parametrize(
    ("field_name", "value", "message"),
    [
        ("decision_id", "unknown_future_decision", "not an exact supported v4/v5/v6"),
        (
            "contract_version",
            "revenue_unreacted_range_promotion_preparation_contract_v5_20260829",
            "mixed with decision profile",
        ),
        (
            "formal_adapter_gate",
            "disabled_adapter_preparation_non_hard_production_approval_hard_gate",
            "promotion.formal_adapter_gate",
        ),
    ],
)
def test_latest_promotion_profile_rejects_unknown_or_mixed_version(
    field_name: str,
    value: str,
    message: str,
) -> None:
    promotion = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("")
    promotion.loc[promotion.index[-1], field_name] = value

    with pytest.raises(RuntimeError, match=message):
        syncer._validated_revenue_promotion_row(promotion)


def test_import_does_not_load_legacy_cross_model_builder() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            "-c",
            (
                "import sys; sys.path.insert(0, 'scripts'); "
                "import sync_revenue_unreacted_range_operation_readiness; "
                "assert 'build_model_operation_readiness' not in sys.modules"
            ),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0, result.stderr


def test_adapter_validation_does_not_import_adapter_or_validator_into_parent() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-I",
            "-B",
            "-c",
            (
                "import pathlib,sys; root=pathlib.Path(sys.argv[1]); "
                "sys.path.insert(0,str(root/'scripts')); "
                "import sync_revenue_unreacted_range_operation_readiness as s; "
                "s.validate_disabled_adapter_preparation(root); "
                "assert 'revenue_unreacted_range_operation_adapter' not in sys.modules; "
                "assert 'validate_revenue_unreacted_range_operation_adapter' not in sys.modules"
            ),
            str(ROOT),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0, result.stderr


def test_exact_replay_child_dependencies_and_execution_boundary_are_explicit() -> None:
    assert syncer.EXACT_REPLAY_CHILD_MODULES == (
        "revenue_unreacted_range_forward_holdout_v2",
        "validate_revenue_unreacted_range_forward_holdout_v2",
    )
    assert syncer.EXACT_REPLAY_CHILD_MODE == (
        "trusted_same_model_in_memory_canonical_replay"
    )
    source = Path(syncer.__file__).read_text(encoding="utf-8")
    assert '[sys.executable, "-I", "-B", "-c", child_source]' in source
    assert source.count('"--no-replace-objects"') >= 5
    assert '"--porcelain=v1"' in source
    assert '"worktree"' in source
    assert '"--detach"' in source
    child_env = syncer._exact_replay_child_env()
    assert child_env["GIT_NO_REPLACE_OBJECTS"] == "1"
    assert child_env["NoDefaultCurrentDirectoryInExePath"] == "1"
    assert "validate_v1_exact17_freeze" in source
    assert "producer_v2.engine.build_forward_holdout" in source
    assert "promotion semantic frame drift" in source
    assert '"from exact build: " + name' in source
    assert "promotion_semantic_source_sha256" in source
    assert "source_detail_promotion_semantic_sha256" in source
    assert syncer.EXACT_REPLAY_PROTOCOL_VERSION.endswith("v3_20260829")
    assert source.count("validate_v1_exact17_freeze") >= 2
    assert "build_model_operation_readiness" not in source
    assert set(syncer.READINESS_MIRROR_RELS) == {
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/model_operation_readiness_latest.md",
        "docs/latest/model_operation_readiness_latest.csv",
        "docs/latest/model_operation_readiness_latest.md",
    }


def test_exact_replay_child_promotion_projection_matches_parent() -> None:
    source = Path(syncer.__file__).read_text(encoding="utf-8")
    child_start = source.index(
        "child_source = _exact_replay_child_bootstrap_source"
    )
    helper_start = source.index('RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN = "', child_start)
    helper_end = source.index("\n\ncommit_sha = EXPECTED_COMMIT_SHA", helper_start)
    child_namespace: dict[str, object] = {
        "validator_v2": importlib.import_module(
            "validate_revenue_unreacted_range_forward_holdout_v2"
        ),
    }
    # Execute only the bounded repository-owned helper embedded in the child.
    exec(source[helper_start:helper_end], child_namespace)
    child_hash = child_namespace["promotion_semantic_frame_sha256"]
    assert callable(child_hash)

    base = pd.DataFrame(
        [
            {
                syncer.RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN: "1" * 64,
                syncer.SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN: "2" * 64,
                syncer.CAPTURE_LEGACY_ENVELOPE_COLUMN: "3" * 64,
                syncer.EVENT_LEGACY_ENVELOPE_COLUMN: "4" * 64,
                "monthly_revenue_canonical_table_sha256": "5" * 64,
                "source_asof_row_canonical_sha256": "6" * 64,
            }
        ]
    )
    parent_base = syncer._promotion_semantic_frame_sha256(
        base,
        frame_name="detail",
    )
    assert child_hash(base, "detail") == parent_base
    cases = (
        (
            {
                syncer.RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN: "a" * 64,
                syncer.SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN: "b" * 64,
                syncer.CAPTURE_LEGACY_ENVELOPE_COLUMN: "c" * 64,
                syncer.EVENT_LEGACY_ENVELOPE_COLUMN: "d" * 64,
            },
            False,
        ),
        (
            {
                "price_input_canonical_sha256": "a" * 64,
                "price_input_stock_canonical_sha256s": "2330:" + "b" * 64,
            },
            False,
        ),
        ({"price_semantic_projection_canonical_sha256": "e" * 64}, True),
        ({"monthly_revenue_canonical_table_sha256": "e" * 64}, True),
        ({"unregistered_semantic_column": "unexpected"}, True),
    )
    for mutation, must_reject in cases:
        candidate = base.assign(**mutation)
        parent_hash = syncer._promotion_semantic_frame_sha256(
            candidate,
            frame_name="detail",
        )
        assert child_hash(candidate, "detail") == parent_hash
        assert (parent_hash != parent_base) is must_reject


def test_exact_replay_launcher_ignores_pythonpath_sitecustomize(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    (repo / "tracked.txt").write_text("tracked\n", encoding="utf-8")
    git(repo, "add", "tracked.txt")
    git(repo, "commit", "-m", "tracked")
    head_sha = git(repo, "rev-parse", "HEAD")

    malicious = tmp_path / "malicious"
    malicious.mkdir()
    sentinel = tmp_path / "sitecustomize-wrote.txt"
    (malicious / "sitecustomize.py").write_text(
        "from pathlib import Path\n"
        f"Path({str(sentinel)!r}).write_text('unsafe', encoding='utf-8')\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("PYTHONPATH", str(malicious))

    result = syncer._run_exact_replay_child(
        repo,
        head_sha,
        "print('isolated-child')",
        timeout_seconds=30,
    )
    assert result.stdout.strip() == "isolated-child"
    assert not sentinel.exists()


def test_exact_replay_worktree_materializes_git_blob_bytes(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "config", "core.autocrlf", "true")
    (repo / "tracked.txt").write_text("first\nsecond\n", encoding="utf-8")
    git(repo, "add", "tracked.txt")
    git(repo, "commit", "-m", "tracked")
    head_sha = git(repo, "rev-parse", "HEAD")

    child_source = r'''
import subprocess
from pathlib import Path

blob = subprocess.run(
    ["git", "--no-replace-objects", "cat-file", "blob", "HEAD:tracked.txt"],
    check=True,
    stdout=subprocess.PIPE,
).stdout
assert Path("tracked.txt").read_bytes() == blob
print("blob-bytes-ok")
'''
    result = syncer._run_exact_replay_child(
        repo,
        head_sha,
        child_source,
        timeout_seconds=30,
    )
    assert result.stdout.strip() == "blob-bytes-ok"


def test_exact_replay_child_repository_write_fails_post_status(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    (repo / "tracked.txt").write_text("tracked\n", encoding="utf-8")
    git(repo, "add", "tracked.txt")
    git(repo, "commit", "-m", "tracked")
    head_sha = git(repo, "rev-parse", "HEAD")

    with pytest.raises(RuntimeError, match="mutated its clean worktree"):
        syncer._run_exact_replay_child(
            repo,
            head_sha,
            (
                "from pathlib import Path; "
                "Path('escaped.txt').write_text('unsafe', encoding='utf-8')"
            ),
            timeout_seconds=30,
        )


def test_exact_replay_worktree_ignores_local_replace_ref(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    tracked = repo / "tracked.txt"
    tracked.write_text("original\n", encoding="utf-8")
    git(repo, "add", "tracked.txt")
    git(repo, "commit", "-m", "original")
    original_sha = git(repo, "rev-parse", "HEAD")

    tracked.write_text("replacement\n", encoding="utf-8")
    git(repo, "commit", "-am", "replacement")
    replacement_sha = git(repo, "rev-parse", "HEAD")
    git(repo, "replace", original_sha, replacement_sha)

    result = syncer._run_exact_replay_child(
        repo,
        original_sha,
        "from pathlib import Path; print(Path('tracked.txt').read_text().strip())",
        timeout_seconds=30,
    )
    assert result.stdout.strip() == "original"




def test_exact_replay_child_dirty_worktree_fails_closed(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    temp_parent = tmp_path / "exact-temp"
    temp_parent.mkdir()

    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
        rendered = [str(value) for value in command]
        clean_repo = temp_parent / "repo"
        if rendered[1:7] == [
            "-c",
            "core.autocrlf=false",
            "--no-replace-objects",
            "worktree",
            "add",
            "--detach",
        ]:
            clean_repo.mkdir()
            return completed_process()
        if rendered[0] == sys.executable:
            return completed_process(stdout="child-output\n")
        if rendered[:5] == [
            "git",
            "--no-replace-objects",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        ]:
            return completed_process(stdout="?? escaped.txt\n")
        if rendered[1:4] == ["--no-replace-objects", "worktree", "remove"]:
            clean_repo.rmdir()
            return completed_process()
        raise AssertionError(rendered)

    with pytest.raises(RuntimeError, match="mutated its clean worktree"):
        syncer._run_exact_replay_child(
            repo,
            "a" * 40,
            "print('child')",
            run_command=fake_run,
            make_temp_dir=lambda **_kwargs: str(temp_parent),
        )


def test_exact_replay_primary_child_error_survives_cleanup_error(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    temp_parent = tmp_path / "exact-temp"
    temp_parent.mkdir()

    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
        rendered = [str(value) for value in command]
        clean_repo = temp_parent / "repo"
        if rendered[1:7] == [
            "-c",
            "core.autocrlf=false",
            "--no-replace-objects",
            "worktree",
            "add",
            "--detach",
        ]:
            clean_repo.mkdir()
            return completed_process()
        if rendered[0] == sys.executable:
            return completed_process(returncode=7, stderr="child-boom")
        if rendered[:5] == [
            "git",
            "--no-replace-objects",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        ]:
            return completed_process()
        if rendered[1:4] == ["--no-replace-objects", "worktree", "remove"]:
            return completed_process(returncode=1, stderr="remove-boom")
        raise AssertionError(rendered)

    with pytest.raises(RuntimeError) as caught:
        syncer._run_exact_replay_child(
            repo,
            "a" * 40,
            "print('child')",
            run_command=fake_run,
            make_temp_dir=lambda **_kwargs: str(temp_parent),
        )
    message = str(caught.value)
    assert "child-boom" in message
    assert "cleanup failures" in message
    assert "remove-boom" in message


def test_exact_replay_timeout_still_checks_and_cleans_worktree(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    temp_parent = tmp_path / "exact-temp"
    temp_parent.mkdir()
    calls: list[str] = []

    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
        rendered = [str(value) for value in command]
        clean_repo = temp_parent / "repo"
        if rendered[1:7] == [
            "-c",
            "core.autocrlf=false",
            "--no-replace-objects",
            "worktree",
            "add",
            "--detach",
        ]:
            clean_repo.mkdir()
            calls.append("add")
            return completed_process()
        if rendered[0] == sys.executable:
            calls.append("child")
            raise subprocess.TimeoutExpired(rendered, timeout=1)
        if rendered[:5] == [
            "git",
            "--no-replace-objects",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
        ]:
            calls.append("status")
            return completed_process()
        if rendered[1:4] == ["--no-replace-objects", "worktree", "remove"]:
            calls.append("remove")
            clean_repo.rmdir()
            return completed_process()
        raise AssertionError(rendered)

    with pytest.raises(RuntimeError, match="timed out after 1 seconds"):
        syncer._run_exact_replay_child(
            repo,
            "a" * 40,
            "print('child')",
            timeout_seconds=1,
            run_command=fake_run,
            make_temp_dir=lambda **_kwargs: str(temp_parent),
        )
    assert calls == ["add", "child", "status", "remove"]
    assert not temp_parent.exists()


def test_exact_replay_add_failure_preserves_primary_and_partial_cleanup(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    temp_parent = tmp_path / "exact-temp"
    temp_parent.mkdir()

    def fake_run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
        rendered = [str(value) for value in command]
        clean_repo = temp_parent / "repo"
        if rendered[1:7] == [
            "-c",
            "core.autocrlf=false",
            "--no-replace-objects",
            "worktree",
            "add",
            "--detach",
        ]:
            clean_repo.mkdir()
            return completed_process(returncode=1, stderr="partial-add-boom")
        if rendered[1:4] == ["--no-replace-objects", "worktree", "remove"]:
            return completed_process(returncode=1, stderr="partial-remove-boom")
        raise AssertionError(rendered)

    with pytest.raises(RuntimeError) as caught:
        syncer._run_exact_replay_child(
            repo,
            "a" * 40,
            "print('child')",
            run_command=fake_run,
            make_temp_dir=lambda **_kwargs: str(temp_parent),
        )
    message = str(caught.value)
    assert "partial-add-boom" in message
    assert "cleanup failures" in message
    assert "partial-remove-boom" in message


def test_exact_replay_payload_rejects_identity_and_five_frame_schema() -> None:
    head_sha = "1" * 40
    tree_sha = "2" * 40
    runtime = {"python": "3.13.0", "pandas": "2.2.0", "numpy": "2.1.0"}
    payload = exact_replay_protocol_payload(head_sha, tree_sha, runtime)

    wrong_identity = dict(payload)
    wrong_identity["tree_sha"] = "3" * 40
    result = completed_process(
        stdout=syncer.EXACT_REPLAY_SENTINEL + json.dumps(wrong_identity)
    )
    with pytest.raises(RuntimeError, match="committed identity drift"):
        syncer._parse_exact_replay_payload(
            result,
            head_sha=head_sha,
            tree_sha=tree_sha,
            runtime_fingerprint=runtime,
        )

    missing_frame = dict(payload)
    missing_frame["frame_attestations"] = dict(payload["frame_attestations"])
    missing_frame["frame_attestations"].pop("anomaly")
    result = completed_process(
        stdout=syncer.EXACT_REPLAY_SENTINEL + json.dumps(missing_frame)
    )
    with pytest.raises(RuntimeError, match="five-frame attestation drift"):
        syncer._parse_exact_replay_payload(
            result,
            head_sha=head_sha,
            tree_sha=tree_sha,
            runtime_fingerprint=runtime,
        )


def test_exact_replay_cache_binds_commit_tree_runtime_and_runs_child_once(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    (repo / "tracked.txt").write_text("tracked\n", encoding="utf-8")
    git(repo, "add", "tracked.txt")
    git(repo, "commit", "-m", "tracked")
    head_sha = git(repo, "rev-parse", "HEAD")
    tree_sha = git(repo, "rev-parse", "HEAD^{tree}")
    runtime = {
        "python": sys.version.split()[0],
        "pandas": pd.__version__,
        "numpy": importlib.metadata.version("numpy"),
    }
    payload = exact_replay_protocol_payload(head_sha, tree_sha, runtime)
    child_calls: list[str] = []

    def fake_child(
        _repo: Path,
        observed_head: str,
        _source: str,
    ) -> subprocess.CompletedProcess[str]:
        child_calls.append(observed_head)
        return completed_process(
            stdout=syncer.EXACT_REPLAY_SENTINEL + json.dumps(payload)
        )

    monkeypatch.setattr(syncer, "_run_exact_replay_child", fake_child)
    syncer._EXACT_PRICE_LINEAGE_CACHE.clear()
    try:
        first = syncer._recompute_exact_registered_price_lineage(repo)
        second = syncer._recompute_exact_registered_price_lineage(repo)
    finally:
        syncer._EXACT_PRICE_LINEAGE_CACHE.clear()
    assert first == second == payload
    assert child_calls == [head_sha]


@pytest.mark.parametrize(
    ("field_name", "forged_value", "expected_error"),
    (
        ("rule_canonical_sha256", "0" * 64, "rule_canonical_sha256 drift"),
        ("data_contract_version", "legacy-v2", "data_contract_version drift"),
        ("data_contract_sha256", "0" * 64, "data_contract_sha256 drift"),
        (
            "price_semantic_projection_version",
            "legacy-prepared-frame",
            "price_semantic_projection_version drift",
        ),
        (
            "price_semantic_projection_schema_sha256",
            "0" * 64,
            "price_semantic_projection_schema_sha256 drift",
        ),
        (
            "price_semantic_projection_canonical_sha256",
            "0" * 64,
            "placeholder SHA-256",
        ),
        (
            "price_semantic_projection_columns",
            "date|close",
            "price_semantic_projection_columns drift",
        ),
        (
            "price_semantic_projection_decimal_scale",
            "7",
            "price_semantic_projection_decimal_scale drift",
        ),
        (
            "price_semantic_projection_role",
            "diagnostic_only",
            "price_semantic_projection_role drift",
        ),
        (
            "price_semantic_projection_migration_id",
            "unregistered",
            "price_semantic_projection_migration_id drift",
        ),
        (
            "price_semantic_projection_authorization_reference",
            "missing",
            "price_semantic_projection_authorization_reference drift",
        ),
    ),
)
def test_full_v2_gate_rejects_bad_rule_canonical_sha(
    field_name: str,
    forged_value: str,
    expected_error: str,
) -> None:
    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    holdout.loc[0, field_name] = forged_value
    with pytest.raises(RuntimeError, match=expected_error):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            holdout,
            holdout_detail=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
            ).fillna(""),
            holdout_summary=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
            ).fillna(""),
            replay_source=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
            ).fillna(""),
            source_projection_manifest=pd.read_csv(
                ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
            ).fillna(""),
        )


def test_full_v2_gate_rejects_placeholder_per_stock_price_digest() -> None:
    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    holdout = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    tokens = holdout.loc[
        0, "price_semantic_projection_stock_canonical_sha256s"
    ].split("|")
    first_stock = tokens[0].split(":", 1)[0]
    tokens[0] = f"{first_stock}:{'0' * 64}"
    holdout.loc[
        0, "price_semantic_projection_stock_canonical_sha256s"
    ] = "|".join(tokens)
    with pytest.raises(RuntimeError, match="placeholder SHA-256"):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            holdout,
            holdout_detail=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
            ).fillna(""),
            holdout_summary=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
            ).fillna(""),
            replay_source=pd.read_csv(
                ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
            ).fillna(""),
            source_projection_manifest=pd.read_csv(
                ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
            ).fillna(""),
        )

    legacy_diagnostic_only = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    legacy_diagnostic_only.loc[0, "price_input_canonical_sha256"] = "malformed"
    legacy_diagnostic_only.loc[
        0, "price_input_stock_canonical_sha256s"
    ] = "malformed"
    legacy_diagnostic_only.loc[0, "price_input_stock_count"] = "malformed"
    legacy_diagnostic_only.loc[0, "price_input_row_count"] = "malformed"
    summary = syncer.summarize_revenue_promotion_readiness(
        promotion,
        anomalies,
        legacy_diagnostic_only,
        holdout_detail=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
        ).fillna(""),
        holdout_summary=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
        ).fillna(""),
        replay_source=pd.read_csv(
            ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
        ).fillna(""),
        source_projection_manifest=pd.read_csv(
            ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
        ).fillna(""),
    )
    assert summary["formal_model_use_allowed"] == "False"
    assert summary["production_allowed"] == "False"


def test_full_v2_gate_rejects_self_consistent_forged_mature_row_before_d30(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    price_path = repo / syncer.PRICE_HISTORY_DIR_REL / "2330.csv"
    price_path.parent.mkdir(parents=True)
    price_path.write_text(
        "date,open,close\n"
        "20260831,100,100\n"
        "20260901,110,110\n",
        encoding="utf-8",
        newline="\n",
    )
    resolution_path = repo / syncer.PRICE_RESOLUTION_REL
    resolution_path.parent.mkdir(parents=True, exist_ok=True)
    resolution_path.write_bytes((ROOT / syncer.PRICE_RESOLUTION_REL).read_bytes())
    git(repo, "init")
    git(repo, "config", "user.name", "test")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "registered price evidence")

    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    manifest = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
    ).fillna("")
    source_projection_manifest = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
    ).fillna("")

    manifest.loc[0, "observed_through_date"] = "20260901"
    manifest.loc[0, "holdout_status"] = "holdout_accumulating"
    manifest.loc[0, "holdout_event_count"] = "1"
    manifest.loc[0, "mature_event_count"] = "1"
    manifest.loc[0, "right_censored_event_count"] = "0"
    manifest.loc[0, "primary_mature_count"] = "1"
    manifest.loc[0, "primary_right_censored_count"] = "0"
    manifest_row = manifest.iloc[0]
    capture_envelope = {
        "artifact_version": syncer.REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "rule_canonical_sha256": syncer.RULE_CANONICAL_SHA256,
        "data_contract_sha256": syncer.DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": syncer.PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": "20260901",
        "source_detail_canonical_sha256": manifest_row[
            "source_detail_canonical_sha256"
        ],
        "price_semantic_projection_version": (
            syncer.PRICE_SEMANTIC_PROJECTION_VERSION
        ),
        "price_semantic_projection_schema_sha256": (
            syncer.PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_canonical_sha256": manifest_row[
            "price_semantic_projection_canonical_sha256"
        ],
        **{
            field_name: manifest_row[field_name]
            for field_name in syncer.MONTHLY_LINEAGE_COLUMNS
        },
        "training_source_projection_semantic_sha256": (
            syncer.PROJECTED_EPISODE_SEMANTIC_SHA256
        ),
        "training_source_projected_episode_row_count": (
            syncer.PROJECTED_EPISODE_ROW_COUNT
        ),
        "training_source_manifest_canonical_sha256": (
            syncer.SELECTED_V2_MANIFEST_CANONICAL_SHA256
        ),
    }
    capture_id = syncer._canonical_json_sha256(capture_envelope)
    manifest.loc[0, "capture_id"] = capture_id

    detail_columns = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, nrows=0
    ).columns
    event = {column: "" for column in detail_columns}
    for column in detail_columns:
        if column in manifest.columns:
            event[column] = str(manifest.loc[0, column])
    event.update(
        {
            "capture_id": capture_id,
            "artifact_row_key": "forged|2330|20260831",
            "event_key": "forged|2330|20260831",
            "variant_id": syncer.PRIMARY_VARIANT_ID,
            "candidate_variant_id": syncer.PRIMARY_VARIANT_ID,
            "primary_variant_member": "True",
            "low_falling_member": "False",
            "low_or_mid_falling_union_member": "True",
            "lifecycle_policy_id": "rearm_after_realized_exit_next_trade_day",
            "confirmation_variant_id": "delayed_next_close_continuation_bonus",
            "holding_days": "30",
            "holding_session_index_offset": "29",
            "stop_policy_id": "none_no_stop_reference",
            "stock_id": "2330",
            "stock_name": "台積電",
            "episode_key": "forged-episode",
            "source_asof_date": "20260828",
            "source_asof_trade_date": "20260828",
            "source_asof_canonical_source_table_date": "20260828",
            "trigger_index": "0",
            "trigger_date": "20260831",
            "trigger_close": "100",
            "confirmation_index": "1",
            "confirmation_date": "20260901",
            "confirmation_close": "110",
            "entry_index": "2",
            "entry_price_basis": "analysis_open",
            "entry_date": "20260902",
            "entry_price": "110",
            "planned_exit_index": "31",
            "planned_exit_date": "20261013",
            "exit_index": "31",
            "exit_date": "20261013",
            "exit_price": "121",
            "exit_price_basis": "analysis_close",
            "exit_reason": "fixed_d30_close",
            "return_valid": "True",
            "right_censored": "False",
            "realized_return_pct": "10",
            "return_outcome": "win",
            "realized_return_ge20": "False",
            "operation_return_review_candidate_flag": "False",
            "operation_status": "mature_operation",
            "anomaly_candidate_flag": "False",
            "source_anomaly_candidate_flag": "False",
            "unresolved_price_path_candidate_flag": "False",
            "primary_metric_included": "True",
            "sensitivity_metric_included": "True",
            "same_stock_non_overlap_applied": "True",
            "financial_statement_scope": (
                syncer.REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE
            ),
            "research_only": "True",
            "formal_model_use_allowed": "False",
            "approved_for_daily": "False",
            "presentation_allowed": "False",
            "promotion_evidence_allowed": "False",
            "production_change": "False",
        }
    )
    event["event_row_canonical_sha256"] = syncer._canonical_mapping_sha256(
        {
            key: value
            for key, value in event.items()
            if key != "event_row_canonical_sha256"
        }
    )
    detail = pd.DataFrame([event], columns=detail_columns)
    assert detail.loc[0, "event_row_canonical_sha256"] == (
        syncer._canonical_mapping_sha256(
            detail.drop(columns=["event_row_canonical_sha256"]).iloc[0].to_dict()
        )
    )

    summary["holdout_status"] = "holdout_accumulating"
    for column in ("event_count", "mature_count", "right_censored_count"):
        summary[column] = "0"
    primary = summary["variant_id"].eq(syncer.PRIMARY_VARIANT_ID)
    summary.loc[primary, "event_count"] = "1"
    summary.loc[primary, "mature_count"] = "1"
    union = summary["variant_id"].eq("source_low_or_mid_falling_union")
    summary.loc[union, "event_count"] = "1"
    summary.loc[union, "mature_count"] = "1"

    attestation = exact_attestation(manifest, detail, summary, replay_source)
    monkeypatch.setattr(
        syncer,
        "_recompute_exact_registered_price_lineage",
        lambda _repo_root: attestation,
    )
    maturity_only_prices = pd.DataFrame(
        {
            "date": ["20260831", "20260901"],
            "analysis_open": [100.0, 110.0],
            "analysis_close": [100.0, 110.0],
        }
    )
    monkeypatch.setattr(
        syncer,
        "_load_registered_price_frames",
        lambda *_args, **_kwargs: {"2330": maturity_only_prices},
    )
    monkeypatch.setattr(
        syncer,
        "_validate_replay_source_pit_lineage",
        lambda *_args, **_kwargs: None,
    )
    monkeypatch.setattr(
        syncer,
        "_validate_detail_source_asof_against_replay",
        lambda *_args, **_kwargs: None,
    )
    monkeypatch.setattr(
        syncer,
        "validate_disabled_adapter_preparation",
        lambda _repo: syncer.DisabledAdapterPreparationValidationResult(
            validator_rel=syncer.REVENUE_ADAPTER_VALIDATOR_REL,
            module_rel=syncer.REVENUE_ADAPTER_MODULE_REL,
            protocol_line=syncer.REVENUE_ADAPTER_VALIDATION_PASS,
        ),
    )

    with pytest.raises(
        RuntimeError,
        match=r"independently replayed D\+2 entry and D\+30",
    ):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            manifest,
            holdout_detail=detail,
            holdout_summary=summary,
            replay_source=replay_source,
            source_projection_manifest=source_projection_manifest,
            repo_root=repo,
        )


def test_registered_price_gate_recomputes_mature_exit_and_realized_return() -> None:
    dates = pd.bdate_range("2026-08-31", periods=32).strftime("%Y%m%d").tolist()
    price = pd.DataFrame(
        {
            "date": dates,
            "analysis_open": [100.0] * 32,
            "analysis_close": [100.0, 101.0, *([100.0] * 28), 110.0, 120.0],
        }
    )
    event = {
        "price_input_canonical_sha256": "a" * 64,
        "price_semantic_projection_version": (
            syncer.PRICE_SEMANTIC_PROJECTION_VERSION
        ),
        "price_semantic_projection_schema_sha256": (
            syncer.PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_canonical_sha256": "b" * 64,
        "holding_days": "30",
        "holding_session_index_offset": "29",
        "stock_id": "2330",
        "trigger_index": "0",
        "trigger_date": dates[0],
        "trigger_close": "100",
        "confirmation_index": "1",
        "confirmation_date": dates[1],
        "confirmation_close": "101",
        "entry_index": "2",
        "entry_price_basis": "analysis_open",
        "entry_date": dates[2],
        "entry_price": "100",
        "planned_exit_index": "31",
        "planned_exit_date": dates[31],
        "exit_index": "31",
        "exit_date": dates[31],
        "exit_price": "120",
        "exit_price_basis": "analysis_close",
        "exit_reason": "fixed_d30_close",
        "return_valid": "True",
        "right_censored": "False",
        "realized_return_pct": "20",
        "return_outcome": "win",
        "realized_return_ge20": "False",
        "operation_return_review_candidate_flag": "False",
        "operation_status": "mature_operation",
    }
    detail = pd.DataFrame([event])
    syncer._validate_detail_maturity_against_registered_prices(
        detail,
        observed_through=dates[-1],
        registered_prices={"2330": price},
        manifest_price_projection_sha="b" * 64,
    )

    forged_return = detail.copy()
    forged_return.loc[0, "realized_return_pct"] = "19"
    with pytest.raises(RuntimeError, match=r"realized_return_pct.*disagrees"):
        syncer._validate_detail_maturity_against_registered_prices(
            forged_return,
            observed_through=dates[-1],
            registered_prices={"2330": price},
            manifest_price_projection_sha="b" * 64,
        )

    invalid_confirmation_price = price.copy()
    invalid_confirmation_price.loc[1, "analysis_close"] = 99.0
    invalid_confirmation_detail = detail.copy()
    invalid_confirmation_detail.loc[0, "confirmation_close"] = "99"
    with pytest.raises(RuntimeError, match=r"frozen D\+1 confirmation rule"):
        syncer._validate_detail_maturity_against_registered_prices(
            invalid_confirmation_detail,
            observed_through=dates[-1],
            registered_prices={"2330": invalid_confirmation_price},
            manifest_price_projection_sha="b" * 64,
        )


def test_mid_event_membership_counts_in_primary_and_union_summaries() -> None:
    detail = pd.DataFrame(
        [
            {
                "primary_variant_member": "True",
                "low_falling_member": "False",
                "low_or_mid_falling_union_member": "True",
                "return_valid": "True",
                "right_censored": "False",
            }
        ]
    )
    counts = {
        variant_id: int(syncer._variant_membership(detail, variant_id).sum())
        for variant_id in syncer.ALL_VARIANT_IDS
    }
    assert counts == {
        syncer.PRIMARY_VARIANT_ID: 1,
        "source_low_falling": 0,
        "source_low_or_mid_falling_union": 1,
    }


@pytest.mark.parametrize("mutation", ("duplicate", "unlinked_episode", "deleted"))
def test_exact_replay_attestation_rejects_event_set_mutations(
    mutation: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    manifest = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
    ).fillna("")
    expected_detail = pd.DataFrame(
        [
            {
                "event_key": "expected-event",
                "episode_key": "expected-episode",
                "monthly_revenue_history_blob_sha256": manifest.loc[
                    0, "monthly_revenue_history_blob_sha256"
                ],
                "source_detail_canonical_sha256": manifest.loc[
                    0, "source_detail_canonical_sha256"
                ],
                "capture_id": manifest.loc[0, "capture_id"],
                "source_asof_row_canonical_sha256": "2" * 64,
                "event_row_canonical_sha256": "3" * 64,
            }
        ]
    )
    replay_source = pd.DataFrame(
        [
            {
                "monthly_revenue_history_blob_sha256": manifest.loc[
                    0, "monthly_revenue_history_blob_sha256"
                ],
                "source_row_canonical_sha256": "1" * 64,
            }
        ]
    )
    attestation = exact_attestation(
        manifest,
        expected_detail,
        summary,
        replay_source,
    )
    monkeypatch.setattr(
        syncer,
        "_recompute_exact_registered_price_lineage",
        lambda _repo_root: attestation,
    )

    provenance_manifest = manifest.copy()
    provenance_detail = expected_detail.copy()
    provenance_summary = summary.copy()
    provenance_replay_source = replay_source.copy()
    provenance_manifest.loc[0, "monthly_revenue_history_blob_sha256"] = "4" * 64
    provenance_manifest.loc[0, "source_detail_canonical_sha256"] = "5" * 64
    provenance_manifest.loc[0, "capture_id"] = "6" * 64
    provenance_manifest.loc[0, "price_input_canonical_sha256"] = "diagnostic-only"
    provenance_manifest.loc[0, "price_input_stock_canonical_sha256s"] = (
        "malformed-diagnostic-only"
    )
    provenance_manifest.loc[0, "price_input_stock_count"] = "diagnostic-only"
    provenance_manifest.loc[0, "price_input_row_count"] = "diagnostic-only"
    provenance_detail.loc[0, "monthly_revenue_history_blob_sha256"] = "4" * 64
    provenance_detail.loc[0, "source_detail_canonical_sha256"] = "5" * 64
    provenance_detail.loc[0, "capture_id"] = "6" * 64
    provenance_detail.loc[0, "event_row_canonical_sha256"] = "7" * 64
    if "capture_id" in provenance_summary.columns:
        provenance_summary["capture_id"] = "6" * 64
    provenance_replay_source["monthly_revenue_history_blob_sha256"] = "4" * 64
    syncer._validate_exact_registered_price_lineage(
        ROOT,
        provenance_manifest.iloc[0],
        manifest=provenance_manifest,
        detail=provenance_detail,
        summary=provenance_summary,
        replay_source=provenance_replay_source,
        observed_through=provenance_manifest.loc[0, "observed_through_date"],
        per_stock_manifest_sha=syncer._parse_price_semantic_projection_stock_sha_set(
            provenance_manifest.iloc[0]
        ),
    )

    hard_semantic_manifest = manifest.copy()
    hard_semantic_manifest.loc[0, "monthly_revenue_canonical_table_sha256"] = (
        "8" * 64
    )
    with pytest.raises(RuntimeError, match="manifest promotion semantic drift"):
        syncer._validate_exact_registered_price_lineage(
            ROOT,
            hard_semantic_manifest.iloc[0],
            manifest=hard_semantic_manifest,
            detail=expected_detail,
            summary=summary,
            replay_source=replay_source,
            observed_through=hard_semantic_manifest.loc[
                0, "observed_through_date"
            ],
            per_stock_manifest_sha=syncer._parse_price_semantic_projection_stock_sha_set(
                hard_semantic_manifest.iloc[0]
            ),
        )
    if mutation == "duplicate":
        candidate_detail = pd.concat(
            [expected_detail, expected_detail], ignore_index=True
        )
    elif mutation == "unlinked_episode":
        candidate_detail = expected_detail.copy()
        candidate_detail.loc[0, "episode_key"] = "forged-unlinked-episode"
    else:
        candidate_detail = expected_detail.iloc[0:0].copy()

    with pytest.raises(
        RuntimeError,
        match="candidate detail promotion semantic drift",
    ):
        syncer._validate_exact_registered_price_lineage(
            ROOT,
            manifest.iloc[0],
            manifest=manifest,
            detail=candidate_detail,
            summary=summary,
            replay_source=replay_source,
            observed_through=manifest.loc[0, "observed_through_date"],
            per_stock_manifest_sha=syncer._parse_price_semantic_projection_stock_sha_set(
                manifest.iloc[0]
            ),
        )


@pytest.mark.parametrize("mutation", ("future_date", "placeholder_hash"))
def test_cheap_replay_source_rejects_invalid_pit_or_row_hash_format(
    mutation: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    manifest = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    detail = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
    ).fillna("")
    summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
    ).fillna("")
    projection = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
    ).fillna("")
    def fail_exact(_repo_root: Path) -> dict[str, object]:
        raise AssertionError("cheap replay-source validation invoked exact replay")

    monkeypatch.setattr(syncer, "_recompute_exact_registered_price_lineage", fail_exact)
    monkeypatch.setattr(
        syncer,
        "_load_registered_price_frames",
        lambda *_args, **_kwargs: {},
    )

    selected_index = replay_source.index[
        replay_source["condition_variant_id"].eq(syncer.SOURCE_VARIANT_ID)
    ][0]
    if mutation == "future_date":
        source_dates = replay_source.loc[
            selected_index, "qualifying_source_dates"
        ].split("|")
        canonical_dates = replay_source.loc[
            selected_index, "qualifying_canonical_source_table_dates"
        ].split("|")
        source_dates[-1] = "20991231"
        canonical_dates[-1] = "20991231"
        replay_source.loc[selected_index, "qualifying_source_dates"] = "|".join(
            source_dates
        )
        replay_source.loc[
            selected_index, "qualifying_canonical_source_table_dates"
        ] = "|".join(canonical_dates)
        replay_source.loc[selected_index, "latest_qualifying_source_date"] = (
            "20991231"
        )
        replay_source.loc[
            selected_index, "latest_qualifying_canonical_source_table_date"
        ] = "20991231"
        if len(source_dates) == 1:
            replay_source.loc[selected_index, "episode_start_source_date"] = (
                "20991231"
            )
            replay_source.loc[
                selected_index, "episode_start_canonical_source_table_date"
            ] = "20991231"
    else:
        forged_hash = "0" * 64
        source_hashes = replay_source.loc[
            selected_index, "qualifying_source_row_canonical_sha256s"
        ].split("|")
        source_hashes[-1] = forged_hash
        replay_source.loc[
            selected_index, "qualifying_source_row_canonical_sha256s"
        ] = "|".join(source_hashes)
        replay_source.loc[
            selected_index, "latest_qualifying_source_row_canonical_sha256"
        ] = forged_hash
        if len(source_hashes) == 1:
            replay_source.loc[
                selected_index, "episode_start_source_row_canonical_sha256"
            ] = forged_hash
    normalized_source = syncer._normalize_replay_source(replay_source).reset_index(
        drop=True
    )
    manifest.loc[0, "source_detail_canonical_sha256"] = (
        syncer._canonical_frame_sha256(normalized_source)
    )
    row = manifest.iloc[0]
    capture_envelope = {
        "artifact_version": syncer.REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "rule_canonical_sha256": syncer.RULE_CANONICAL_SHA256,
        "data_contract_sha256": syncer.DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": syncer.PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": row["observed_through_date"],
        "source_detail_canonical_sha256": row["source_detail_canonical_sha256"],
        "price_semantic_projection_version": (
            syncer.PRICE_SEMANTIC_PROJECTION_VERSION
        ),
        "price_semantic_projection_schema_sha256": (
            syncer.PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_canonical_sha256": row[
            "price_semantic_projection_canonical_sha256"
        ],
        **{field_name: row[field_name] for field_name in syncer.MONTHLY_LINEAGE_COLUMNS},
        "training_source_projection_semantic_sha256": (
            syncer.PROJECTED_EPISODE_SEMANTIC_SHA256
        ),
        "training_source_projected_episode_row_count": (
            syncer.PROJECTED_EPISODE_ROW_COUNT
        ),
        "training_source_manifest_canonical_sha256": (
            syncer.SELECTED_V2_MANIFEST_CANONICAL_SHA256
        ),
    }
    manifest.loc[0, "capture_id"] = syncer._canonical_json_sha256(
        capture_envelope
    )

    expected_error = (
        "source date exceeds trade date|future PIT lineage"
        if mutation == "future_date"
        else "placeholder SHA-256"
    )
    with pytest.raises(RuntimeError, match=expected_error):
        syncer.summarize_revenue_promotion_readiness(
            promotion,
            anomalies,
            manifest,
            holdout_detail=detail,
            holdout_summary=summary,
            replay_source=replay_source,
            source_projection_manifest=projection,
            repo_root=ROOT,
        )


def test_cheap_replay_lineage_does_not_claim_independent_raw_monthly_truth() -> None:
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
    ).fillna("")
    selected_index = replay_source.index[
        replay_source["condition_variant_id"].eq(syncer.SOURCE_VARIANT_ID)
    ][0]
    forged_hash = "c" * 64
    source_hashes = replay_source.loc[
        selected_index, "qualifying_source_row_canonical_sha256s"
    ].split("|")
    source_hashes[-1] = forged_hash
    replay_source.loc[
        selected_index, "qualifying_source_row_canonical_sha256s"
    ] = "|".join(source_hashes)
    replay_source.loc[
        selected_index, "latest_qualifying_source_row_canonical_sha256"
    ] = forged_hash
    if len(source_hashes) == 1:
        replay_source.loc[
            selected_index, "episode_start_source_row_canonical_sha256"
        ] = forged_hash

    normalized = syncer._normalize_replay_source(replay_source)
    episode_key = replay_source.loc[selected_index, "episode_key"]
    lineage = syncer._replay_lineage_values(normalized.loc[episode_key])

    assert lineage["source_hashes"][-1] == forged_hash
    assert not hasattr(syncer, "_canonical_monthly_revenue_fact_map")


def test_replay_source_trade_date_must_be_first_registered_session_on_or_after_source() -> None:
    source_hash = "a" * 64
    episode_key = "episode-first-session"
    normalized_source = pd.DataFrame(
        [
            {
                "episode_key": episode_key,
                "stock_id": "2330",
                "qualifying_update_count": "1",
                "qualifying_revenue_periods": "202601",
                "qualifying_source_dates": "20260217",
                "qualifying_cross_market_resolution_ids": "none",
                "qualifying_source_row_canonical_sha256s": source_hash,
                "qualifying_canonical_source_table_dates": "20260217",
                "qualifying_trade_dates": "20260218",
                "qualifying_sequence_indices": "1",
                "episode_start_revenue_period": "202601",
                "episode_start_source_date": "20260217",
                "episode_start_cross_market_resolution_id": "none",
                "episode_start_source_row_canonical_sha256": source_hash,
                "episode_start_canonical_source_table_date": "20260217",
                "episode_start_trade_date": "20260218",
                "episode_start_sequence_index": "1",
                "latest_qualifying_revenue_period": "202601",
                "latest_qualifying_source_date": "20260217",
                "latest_qualifying_cross_market_resolution_id": "none",
                "latest_qualifying_source_row_canonical_sha256": source_hash,
                "latest_qualifying_canonical_source_table_date": "20260217",
                "latest_qualifying_trade_date": "20260218",
                "latest_qualifying_sequence_index": "1",
            }
        ]
    ).set_index("episode_key", drop=False)
    registered_prices = {
        "2330": pd.DataFrame({"date": ["20260217", "20260218"]})
    }

    with pytest.raises(RuntimeError, match="not the first normalized registered session"):
        syncer._validate_replay_source_pit_lineage(
            normalized_source,
            observed_through="20260218",
            registered_prices=registered_prices,
        )


def test_detail_source_asof_is_bound_to_replay_lineage() -> None:
    source_hash = "a" * 64
    episode_key = "episode-1"
    normalized_source = pd.DataFrame(
        [
            {
                "episode_key": episode_key,
                "stock_id": "2330",
                "qualifying_update_count": "2",
                "qualifying_revenue_periods": "202601|202602",
                "qualifying_source_dates": "20260217|20260317",
                "qualifying_cross_market_resolution_ids": "none|none",
                "qualifying_source_row_canonical_sha256s": (
                    f"{source_hash}|{'b' * 64}"
                ),
                "qualifying_canonical_source_table_dates": "20260217|20260317",
                "qualifying_trade_dates": "20260217|20260317",
                "qualifying_sequence_indices": "0|2",
                "episode_start_revenue_period": "202601",
                "episode_start_source_date": "20260217",
                "episode_start_cross_market_resolution_id": "none",
                "episode_start_source_row_canonical_sha256": source_hash,
                "episode_start_canonical_source_table_date": "20260217",
                "episode_start_trade_date": "20260217",
                "episode_start_sequence_index": "0",
                "latest_qualifying_revenue_period": "202602",
                "latest_qualifying_source_date": "20260317",
                "latest_qualifying_cross_market_resolution_id": "none",
                "latest_qualifying_source_row_canonical_sha256": "b" * 64,
                "latest_qualifying_canonical_source_table_date": "20260317",
                "latest_qualifying_trade_date": "20260317",
                "latest_qualifying_sequence_index": "2",
            }
        ]
    ).set_index("episode_key", drop=False)
    prices = pd.DataFrame(
        {"date": ["20260217", "20260218", "20260317", "20260318"]}
    )
    detail = pd.DataFrame(
        [
            {
                "episode_key": episode_key,
                "stock_id": "2330",
                "trigger_index": "3",
                "source_asof_date": "20260317",
                "source_asof_trade_date": "20260317",
                "source_asof_revenue_period": "202602",
                "source_asof_row_canonical_sha256": "b" * 64,
                "source_asof_canonical_source_table_date": "20260317",
                "source_asof_sequence_index": "2",
                "source_to_trigger_trading_days": "1",
                "future_qualifying_update_ignored_count": "0",
            }
        ]
    )
    syncer._validate_detail_source_asof_against_replay(
        detail,
        normalized_source=normalized_source,
        registered_prices={"2330": prices},
    )

    forged = detail.copy()
    forged.loc[0, "source_asof_row_canonical_sha256"] = "c" * 64
    with pytest.raises(RuntimeError, match="source-asof drift"):
        syncer._validate_detail_source_asof_against_replay(
            forged,
            normalized_source=normalized_source,
            registered_prices={"2330": prices},
        )


def test_summary_and_source_validator_do_not_run_exact_replay(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_exact(_repo_root: Path) -> dict[str, object]:
        raise AssertionError("cheap readiness validation invoked exact replay")

    monkeypatch.setattr(
        syncer,
        "_recompute_exact_registered_price_lineage",
        fail_exact,
    )
    promotion = pd.read_csv(ROOT / syncer.PROMOTION_REGISTRY_REL, dtype=str).fillna("")
    anomalies = pd.read_csv(ROOT / syncer.ANOMALY_REGISTRY_REL, dtype=str).fillna("")
    manifest = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_MANIFEST_REL, dtype=str
    ).fillna("")
    detail = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_DETAIL_REL, dtype=str
    ).fillna("")
    summary = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_SUMMARY_REL, dtype=str
    ).fillna("")
    replay_source = pd.read_csv(
        ROOT / syncer.FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL, dtype=str
    ).fillna("")
    projection = pd.read_csv(
        ROOT / syncer.SOURCE_PROJECTION_MANIFEST_REL, dtype=str
    ).fillna("")

    result = syncer.summarize_revenue_promotion_readiness(
        promotion,
        anomalies,
        manifest,
        holdout_detail=detail,
        holdout_summary=summary,
        replay_source=replay_source,
        source_projection_manifest=projection,
        repo_root=ROOT,
    )

    assert result["formal_model_use_allowed"] == "True"
    assert syncer.validate_revenue_readiness_source_files(ROOT) == []


def test_revenue_readiness_sync_writer_runs_exact_gate_before_any_mirror_write(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base = legacy_readiness()
    placeholder = pd.DataFrame()
    monkeypatch.setattr(
        syncer,
        "load_committed_inputs",
        lambda _repo: (
            base,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            [],
        ),
    )
    monkeypatch.setattr(
        syncer,
        "validate_revenue_promotion_registry",
        lambda _path: (
            pd.read_csv(
                ROOT / syncer.PROMOTION_REGISTRY_REL,
                dtype=str,
            ).fillna("").iloc[-2].to_dict(),
            [],
        ),
    )
    monkeypatch.setattr(
        syncer,
        "validate_current_anomaly_dispositions",
        lambda _repo, **_kwargs: SimpleNamespace(errors=[]),
    )
    monkeypatch.setattr(
        syncer,
        "summarize_revenue_promotion_readiness",
        lambda *_args, **_kwargs: revenue_summary(),
    )
    calls: list[str] = []

    def fail_exact(*_args: object, **_kwargs: object) -> None:
        calls.append("exact")
        raise RuntimeError("exact replay rejected writer")

    monkeypatch.setattr(syncer, "validate_revenue_readiness_exact_replay", fail_exact)
    monkeypatch.setattr(
        syncer,
        "write_readiness_mirrors",
        lambda *_args, **_kwargs: calls.append("write"),
    )

    with pytest.raises(RuntimeError, match="exact replay rejected writer"):
        syncer.sync(tmp_path, generated_at="deterministic-test-time")

    assert calls == ["exact"]


def test_v5_adapter_gate_fails_before_exact_replay_and_any_mirror_write(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    placeholder = pd.DataFrame()
    promotion_frame = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("").iloc[:-1]
    monkeypatch.setattr(
        syncer,
        "load_committed_inputs",
        lambda _repo: (
            legacy_readiness(),
            promotion_frame,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            placeholder,
            [],
        ),
    )
    latest = pd.read_csv(
        ROOT / syncer.PROMOTION_REGISTRY_REL,
        dtype=str,
    ).fillna("").iloc[-2].to_dict()
    monkeypatch.setattr(
        syncer,
        "validate_revenue_promotion_registry",
        lambda _path: (latest, []),
    )
    monkeypatch.setattr(
        syncer,
        "validate_current_anomaly_dispositions",
        lambda _repo, **_kwargs: SimpleNamespace(errors=[]),
    )
    calls: list[str] = []

    def fail_adapter(_repo: Path) -> None:
        calls.append("adapter")
        raise RuntimeError("adapter gate rejected readiness")

    monkeypatch.setattr(syncer, "validate_disabled_adapter_preparation", fail_adapter)
    monkeypatch.setattr(
        syncer,
        "validate_revenue_readiness_exact_replay",
        lambda *_args, **_kwargs: calls.append("exact"),
    )
    monkeypatch.setattr(
        syncer,
        "write_readiness_mirrors",
        lambda *_args, **_kwargs: calls.append("write"),
    )

    with pytest.raises(RuntimeError, match="adapter gate rejected readiness"):
        syncer.sync(tmp_path, generated_at="deterministic-test-time")

    assert calls == ["adapter"]


def test_markdown_status_table_must_match_canonical_csv_non_revenue_cells() -> None:
    readiness = syncer.build_revenue_only_readiness(
        legacy_readiness(),
        revenue_summary(),
        generated_at="new-time",
    )
    markdown = syncer.render_markdown(readiness, generated_at="new-time")
    syncer.validate_markdown_status_table_matches_csv(
        markdown,
        readiness,
        source_name="memory.md",
    )
    drifted = readiness.copy()
    drifted.loc[drifted["model_id"].eq("other_model"), "blocker"] = "drifted"
    with pytest.raises(RuntimeError, match="disagrees with canonical CSV"):
        syncer.validate_markdown_status_table_matches_csv(
            markdown,
            drifted,
            source_name="memory.md",
        )
