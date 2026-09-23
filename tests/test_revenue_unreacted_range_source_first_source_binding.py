from __future__ import annotations

import ast
import csv
import io
from pathlib import Path
import stat
import subprocess
import sys
from types import SimpleNamespace

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_revenue_unreacted_range_source_first_source_binding as binding  # noqa: E402
import validate_revenue_unreacted_range_source_snapshot_projection as lineage  # noqa: E402


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8-sig")


def _raw_row(stock: str, period: str, market: str, date: str) -> dict[str, str]:
    row = {column: "" for column in lineage.RAW_ROW_CANONICAL_COLUMNS}
    row.update(
        stock_id=stock,
        stock_name=f"Stock {stock}",
        industry="synthetic",
        revenue_period=period,
        revenue_period_roc="11506",
        market=market,
        source_market_name="TPEX" if market == "otc" else "TWSE",
        source_table_date=date,
        source_kind="official_mops_current_monthly_revenue_openapi",
        source_url=f"https://example.test/{market}.csv",
        source_file=f"data/monthly_revenue_history/raw/{market}_{date}.csv",
        monthly_revenue="1000",
        previous_month_revenue="900",
        last_year_month_revenue="800",
        month_over_month_pct="11.1111",
        latest_revenue_yoy_pct="25",
        cumulative_revenue="6000",
        last_year_cumulative_revenue="5000",
        cumulative_revenue_yoy_pct="20",
        revenue_positive_flag="True",
        revenue_strong_flag="True",
        revenue_numerical_anomaly_flag="False",
        point_in_time_status="ready_official_source_table_date",
        research_join_allowed="True",
        allowed_for_formal_historical_model_use="False",
        formal_use_blocker="research_only",
        coverage_note="synthetic",
    )
    return row


def _registry_row(earlier: dict[str, str], later: dict[str, str]) -> dict[str, str]:
    row = {column: "" for column in lineage.MONTHLY_RESOLUTION_COLUMNS}
    row.update(
        resolution_id="synthetic_equal_payload_mirror",
        model_id=binding.MODEL_ID,
        stock_id=earlier["stock_id"],
        revenue_period=earlier["revenue_period"],
        official_market_transition_date="20260716",
        canonical_source_table_date=earlier["source_table_date"],
        canonical_row_canonical_sha256=lineage._raw_row_sha256(pd.Series(earlier)),
        resolution_status="registered_equal_payload_cross_market_mirror",
        canonicalization_policy="earliest_official_source_table_date",
        evidence_url="https://example.test/transition",
        formal_model_use_allowed="False",
        notes="synthetic",
    )
    for prefix, source in (("earlier", earlier), ("later", later)):
        row.update({f"{prefix}_{column}": source[column] for column in lineage.SOURCE_IDENTITY_COLUMNS})
        row[f"{prefix}_raw_row_canonical_sha256"] = lineage._raw_row_sha256(pd.Series(source))
    return row


def _write_binding(path: Path, rows: list[dict[str, str]]) -> None:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=binding.BINDING_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(buffer.getvalue().encode("utf-8"))


@pytest.fixture()
def frozen_bundle(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> SimpleNamespace:
    early = _raw_row("1101", "202605", "listed", "20260610")
    mirror_early = _raw_row("5236", "202606", "otc", "20260715")
    mirror_late = _raw_row("5236", "202606", "listed", "20260717")
    raw = pd.DataFrame([early, mirror_early, mirror_late])
    registry = pd.DataFrame([_registry_row(mirror_early, mirror_late)], columns=lineage.MONTHLY_RESOLUTION_COLUMNS)
    canonical = lineage._resolve_monthly(raw, registry, None)
    payloads = {
        binding.REVENUE_REL: _csv_bytes(raw),
        binding.RESOLUTION_REL: _csv_bytes(registry),
    }
    full_lineage = {
        "monthly_revenue_history_blob_sha256": binding._sha256(payloads[binding.REVENUE_REL]),
        "monthly_revenue_canonical_table_sha256": lineage._canonical_monthly_table_sha256(canonical),
        "cross_market_resolution_registry_canonical_sha256": lineage._monthly_registry_sha256(registry),
    }
    artifact_frame = pd.DataFrame(
        [{
            "generated_at": "2026-09-12 22:02:24 Asia/Taipei",
            "model_id": binding.MODEL_ID,
            "artifact_id": binding.ARTIFACT_ID,
            "artifact_version": binding.ARTIFACT_VERSION,
            **full_lineage,
            "approved_for_daily": "False",
            "production_change": "False",
            "sample_count": "12",
        }]
    )
    for path in binding.ARTIFACT_PATHS:
        payloads[path] = (
            _csv_bytes(artifact_frame)
            if path.endswith(".csv")
            else "# 營收來源優先研究\n研究日期：2026-09-12\n".encode("utf-8")
        )
    source_canonical = {
        binding.REVENUE_REL: full_lineage["monthly_revenue_canonical_table_sha256"],
        binding.RESOLUTION_REL: full_lineage["cross_market_resolution_registry_canonical_sha256"],
    }
    rows = []
    for path, role in binding.EXPECTED_ROLES.items():
        payload = payloads[path]
        rows.append({
            "binding_version": binding.BINDING_VERSION,
            "model_id": binding.MODEL_ID,
            "artifact_version": binding.ARTIFACT_VERSION,
            "approval_ref": binding.APPROVAL_REF,
            "source_commit": binding.SOURCE_COMMIT,
            "role": role,
            "path": path,
            "git_blob_oid": binding._git_blob_oid(payload),
            "git_bytes_sha256": binding._sha256(payload),
            "canonical_sha256": source_canonical.get(path, binding._sha256(binding.canonical_transport_bytes(payload))),
            "research_only": "true",
            "formal_model_use_allowed": "false",
            "promotion_evidence_allowed": "false",
            "pdf_consumption_allowed": "false",
        })
    binding_path = tmp_path / binding.BINDING_REL
    _write_binding(binding_path, rows)
    for path in binding.ARTIFACT_PATHS:
        destination = tmp_path / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payloads[path])
    git_calls: list[tuple[str, ...]] = []

    def fake_git(repository_root: Path, *args: str) -> bytes:
        assert repository_root == tmp_path
        git_calls.append(args)
        if args == ("rev-parse", "--verify", f"{binding.SOURCE_COMMIT}^{{commit}}"):
            return (binding.SOURCE_COMMIT + "\n").encode("ascii")
        if args[:3] == ("ls-tree", "-z", binding.SOURCE_COMMIT):
            assert args[3] == "--"
            path = args[4]
            return f"100644 blob {binding._git_blob_oid(payloads[path])}\t{path}\0".encode("utf-8")
        if args[0] == "show":
            commit, path = args[1].split(":", 1)
            assert commit == binding.SOURCE_COMMIT
            return payloads[path]
        raise AssertionError(f"unexpected Git request: {args}")

    monkeypatch.setattr(binding, "_git", fake_git)
    return SimpleNamespace(
        root=tmp_path,
        binding_path=binding_path,
        rows=rows,
        payloads=payloads,
        full_lineage=full_lineage,
        git_calls=git_calls,
        fake_git=fake_git,
    )


def test_frozen_sources_are_reconstructed_independently(frozen_bundle: SimpleNamespace) -> None:
    context = binding.load_bound_source_context(frozen_bundle.root)
    assert context.source_commit == binding.SOURCE_COMMIT
    assert context.full_lineage == frozen_bundle.full_lineage
    assert context.cutoff_count == 1
    assert set(context.source_lineage) == {("1101", "202605"), ("5236", "202606")}
    assert context.source_lineage[("1101", "202605")]["cross_market_resolution_id"] == "none"
    assert context.source_lineage[("5236", "202606")]["source_date"] == "20260715"
    assert context.source_lineage[("5236", "202606")]["cross_market_resolution_id"] == "synthetic_equal_payload_mirror"
    assert context.artifacts == {path: frozen_bundle.payloads[path] for path in binding.ARTIFACT_PATHS}
    assert not (frozen_bundle.root / binding.REVENUE_REL).exists()


def test_mutable_current_source_does_not_replace_the_pinned_source(frozen_bundle: SimpleNamespace) -> None:
    current_path = frozen_bundle.root / binding.REVENUE_REL
    current_path.parent.mkdir(parents=True, exist_ok=True)
    current_path.write_bytes(b"new current snapshot is deliberately not the frozen input\n")
    assert binding.load_bound_source_context(frozen_bundle.root).full_lineage == frozen_bundle.full_lineage


@pytest.mark.parametrize("path", binding.ARTIFACT_PATHS)
def test_every_physical_artifact_is_mandatory_without_git_fallback(frozen_bundle: SimpleNamespace, path: str) -> None:
    (frozen_bundle.root / path).unlink()
    errors = binding.validate(frozen_bundle.root)
    assert errors and "missing source binding file" in errors[0]
    assert frozen_bundle.git_calls == []


def test_explicit_all_six_payloads_are_supported_without_materialization(frozen_bundle: SimpleNamespace) -> None:
    artifacts = {path: frozen_bundle.payloads[path] for path in binding.ARTIFACT_PATHS}
    for path in binding.ARTIFACT_PATHS:
        (frozen_bundle.root / path).unlink()
    assert binding.validate(frozen_bundle.root, artifacts=artifacts) == []


@pytest.mark.parametrize("mutation", ["missing", "foreign", "path_alias", "not_bytes"])
def test_explicit_artifacts_fail_closed(frozen_bundle: SimpleNamespace, mutation: str) -> None:
    artifacts = {path: frozen_bundle.payloads[path] for path in binding.ARTIFACT_PATHS}
    first = binding.ARTIFACT_PATHS[0]
    if mutation == "missing":
        del artifacts[first]
    elif mutation == "foreign":
        artifacts["../other_model.csv"] = b"foreign"
    elif mutation == "path_alias":
        artifacts["./" + first] = artifacts.pop(first)
    else:
        artifacts[first] = "not bytes"
    assert binding.validate(frozen_bundle.root, artifacts=artifacts)


@pytest.mark.parametrize("path", binding.ARTIFACT_PATHS)
def test_bom_and_crlf_transport_only_is_allowed(frozen_bundle: SimpleNamespace, path: str) -> None:
    original = frozen_bundle.payloads[path]
    transported = b"\xef\xbb\xbf" + binding.canonical_transport_bytes(original).replace(b"\n", b"\r\n")
    (frozen_bundle.root / path).write_bytes(transported)
    context = binding.load_bound_source_context(frozen_bundle.root)
    assert context.artifacts[path] == original
    assert (frozen_bundle.root / path).read_bytes() == transported


@pytest.mark.parametrize("path", binding.ARTIFACT_PATHS)
def test_any_artifact_content_change_is_blocking(frozen_bundle: SimpleNamespace, path: str) -> None:
    (frozen_bundle.root / path).write_bytes(frozen_bundle.payloads[path] + b"modified\n")
    assert "frozen artifact content drift" in binding.validate(frozen_bundle.root)[0]


@pytest.mark.parametrize("old,new", [(b"2026-09-12", b"2026-09-13"), (b",12\n", b",13\n")])
def test_generated_at_and_numeric_changes_are_not_transport(frozen_bundle: SimpleNamespace, old: bytes, new: bytes) -> None:
    path = binding.ARTIFACT_PATHS[0]
    payload = frozen_bundle.payloads[path]
    assert old in payload
    (frozen_bundle.root / path).write_bytes(payload.replace(old, new))
    assert "frozen artifact content drift" in binding.validate(frozen_bundle.root)[0]


@pytest.mark.parametrize("column,value", [
    ("model_id", "other_model"),
    ("binding_version", "latest"),
    ("artifact_version", "new_version"),
    ("approval_ref", "unapproved"),
    ("source_commit", "main"),
    ("source_commit", "a" * 40),
    ("role", "formal_adapter"),
    ("research_only", "false"),
    ("formal_model_use_allowed", "true"),
    ("promotion_evidence_allowed", "true"),
    ("pdf_consumption_allowed", "true"),
    ("promotion_evidence_allowed", "False"),
    ("git_blob_oid", "not-a-git-oid"),
    ("git_bytes_sha256", "F" * 64),
    ("canonical_sha256", ""),
])
def test_binding_contract_and_flags_are_exact(frozen_bundle: SimpleNamespace, column: str, value: str) -> None:
    frozen_bundle.rows[0][column] = value
    _write_binding(frozen_bundle.binding_path, frozen_bundle.rows)
    assert binding.validate(frozen_bundle.root)
    assert frozen_bundle.git_calls == []


@pytest.mark.parametrize("path", ["../outside.csv", "/absolute.csv", "C:/outside.csv", "data/../file.csv", "./data/file.csv"])
def test_binding_paths_cannot_escape_the_exact_allowlist(frozen_bundle: SimpleNamespace, path: str) -> None:
    frozen_bundle.rows[0]["path"] = path
    _write_binding(frozen_bundle.binding_path, frozen_bundle.rows)
    assert "exact path set drift" in binding.validate(frozen_bundle.root)[0]


@pytest.mark.parametrize("mutation", ["duplicate", "missing", "extra", "schema"])
def test_binding_cardinality_and_schema_are_closed(frozen_bundle: SimpleNamespace, mutation: str) -> None:
    rows = frozen_bundle.rows
    if mutation == "duplicate":
        rows[0] = rows[1].copy()
    elif mutation == "missing":
        rows.pop()
    elif mutation == "extra":
        rows.append(rows[0].copy())
    _write_binding(frozen_bundle.binding_path, rows)
    if mutation == "schema":
        payload = frozen_bundle.binding_path.read_bytes().replace(b"binding_version,", b"wrong_column,", 1)
        frozen_bundle.binding_path.write_bytes(payload)
    assert binding.validate(frozen_bundle.root)


@pytest.mark.parametrize("path", [binding.REVENUE_REL, binding.RESOLUTION_REL, binding.ARTIFACT_PATHS[0]])
def test_git_source_or_artifact_blob_tampering_is_blocking(frozen_bundle: SimpleNamespace, path: str) -> None:
    frozen_bundle.payloads[path] += b"unexpected edit\n"
    assert "Git blob identity/type drift" in binding.validate(frozen_bundle.root)[0]


@pytest.mark.parametrize("column", ["git_bytes_sha256", "canonical_sha256"])
@pytest.mark.parametrize("index", [0, 1, 2])
def test_well_formed_but_incorrect_hashes_fail(frozen_bundle: SimpleNamespace, column: str, index: int) -> None:
    frozen_bundle.rows[index][column] = "0" * 64
    _write_binding(frozen_bundle.binding_path, frozen_bundle.rows)
    assert binding.validate(frozen_bundle.root)


@pytest.mark.parametrize("case", ["wrong_commit", "missing_git", "symlink_blob", "wrong_bytes"])
def test_immutable_git_identity_is_required(frozen_bundle: SimpleNamespace, monkeypatch: pytest.MonkeyPatch, case: str) -> None:
    original = frozen_bundle.fake_git

    def changed_git(root: Path, *args: str) -> bytes:
        if case == "missing_git":
            raise RuntimeError("missing bound Git object")
        payload = original(root, *args)
        if case == "wrong_commit" and args[0] == "rev-parse":
            return b"b" * 40 + b"\n"
        if case == "symlink_blob" and args[0] == "ls-tree":
            return payload.replace(b"100644", b"120000", 1)
        if case == "wrong_bytes" and args[0] == "show":
            return payload + b"modified"
        return payload

    monkeypatch.setattr(binding, "_git", changed_git)
    assert binding.validate(frozen_bundle.root)


def test_git_subprocess_disables_replace_objects(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    calls = []

    def fake_run(command: list[str], **kwargs: object) -> SimpleNamespace:
        calls.append((command, kwargs))
        return SimpleNamespace(stdout=b"result")

    monkeypatch.setattr(subprocess, "run", fake_run)
    assert binding._git(tmp_path, "show", binding.SOURCE_COMMIT) == b"result"
    assert calls[0][0] == ["git", "--no-replace-objects", "-C", str(tmp_path), "show", binding.SOURCE_COMMIT]
    assert calls[0][1]["check"] is True


@pytest.mark.parametrize("case", ["symlink_file", "symlink_parent", "reparse_parent", "directory_file"])
def test_unsafe_physical_paths_fail_without_reading_through_them(frozen_bundle: SimpleNamespace, monkeypatch: pytest.MonkeyPatch, case: str) -> None:
    target = frozen_bundle.root / binding.ARTIFACT_PATHS[0]
    if case in {"symlink_parent", "reparse_parent"}:
        target = target.parent
    original_lstat = Path.lstat

    def unsafe_lstat(path: Path) -> object:
        if path == target:
            return SimpleNamespace(
                st_mode=stat.S_IFLNK if case.startswith("symlink") else stat.S_IFDIR,
                st_file_attributes=0x400 if case == "reparse_parent" else 0,
            )
        return original_lstat(path)

    monkeypatch.setattr(Path, "lstat", unsafe_lstat)
    assert binding.validate(frozen_bundle.root)


def test_binding_file_cannot_be_outside_repository(frozen_bundle: SimpleNamespace) -> None:
    outside = frozen_bundle.root.parent / "outside.csv"
    assert "outside repository" in binding.validate(frozen_bundle.root, binding_path=outside)[0]


def test_cli_discloses_retained_research_only_not_recomputed(frozen_bundle: SimpleNamespace, capsys: pytest.CaptureFixture[str]) -> None:
    assert binding.main(["--repo-root", str(frozen_bundle.root)]) == 0
    output = capsys.readouterr().out
    assert f"source_commit={binding.SOURCE_COMMIT}" in output
    assert "retained_frozen_source_evidence" in output
    assert "research_only=true" in output
    assert "promotion_evidence_allowed=false" in output
    assert "no_recompute" in output


def test_checked_in_binding_is_exact_and_research_only() -> None:
    rows = binding._binding_rows((ROOT / binding.BINDING_REL).read_bytes())
    assert set(rows) == set(binding.EXPECTED_ROLES)
    assert all(row["source_commit"] == binding.SOURCE_COMMIT for row in rows.values())


def test_validator_does_not_import_model_business_implementation() -> None:
    tree = ast.parse((SCRIPTS / "validate_revenue_unreacted_range_source_first_source_binding.py").read_text(encoding="utf-8"))
    local_imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module and "revenue_unreacted_range" in node.module]
    assert local_imports == ["validate_revenue_unreacted_range_source_snapshot_projection"]
