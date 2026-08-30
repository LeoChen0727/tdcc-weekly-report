from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_approved_operation_patterns import build_approval  # noqa: E402
from formal_model_evidence import evidence_pin_for_model  # noqa: E402
from validate_formal_model_evidence_pins import (  # noqa: E402
    LEGACY_REVENUE_CONDITION,
    LEGACY_REVENUE_CONTRACT,
    LEGACY_REVENUE_SURFACE,
    PREPARED_REVENUE_CONDITION,
    PREPARED_REVENUE_CONTRACT,
    PREPARED_REVENUE_PIN,
    PREPARED_REVENUE_SURFACE,
    validate,
)


REVENUE_MODEL_ID = "revenue_unreacted_range"

PREPARED_PIN_ROW = {"model_id": REVENUE_MODEL_ID, **PREPARED_REVENUE_PIN}

PREPARED_B9_ROW_SHA256 = {
    "contract": "63f54faa20ad2e098ce1d2165a84a0aee4c5a347d29fd1ee49079573d625cb39",
    "condition": "02b3a2d6297aff69b1abecc5b71e6423e26b55fcb7780c9c2bad8f42f4a1c958",
    "surface": "3ea0cc29ff7672f0de4f62c89e10d5b97f326eff83e7ca55c7d654f505963858",
    "pin": "19466dc47a3215f7e2fcd48dd5041598cc00c6c93203e850789dec6bb3b24567",
}

LEGACY_BA78_ROW_SHA256 = {
    "contract": "5b5c65891d2e6310893992087d29731767f56ec4ff1cdc5110e4adb29fa0dfdd",
    "condition": "ae1630eb53e15b98a88a05aa551029698720d2bf58e127c598c209a363e5b8ae",
    "surface": "52a67dfc2618be74fe023e3f1e5411189bfdc50268a86c937214f826de727b6b",
}

REGISTRY_SPECS = {
    "contract": (ROOT / "config/stock_model_contract_registry.csv", "model_id"),
    "condition": (ROOT / "config/daily_model_condition_spec.csv", "model_id"),
    "surface": (ROOT / "config/model_surface_registry.csv", "surface_id"),
    "pins": (ROOT / "config/formal_model_evidence_pins.csv", "model_id"),
}


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _replace_revenue_row(
    path: Path,
    id_column: str,
    expected: dict[str, str],
) -> None:
    fields, rows = _read_csv(path)
    expected_fields = {id_column, *expected}
    assert set(fields) == expected_fields
    indexes = [index for index, row in enumerate(rows) if row.get(id_column) == REVENUE_MODEL_ID]
    insert_at = indexes[0] if indexes else len(rows)
    rows = [row for row in rows if row.get(id_column) != REVENUE_MODEL_ID]
    exact_row = {
        field: REVENUE_MODEL_ID if field == id_column else expected[field]
        for field in fields
    }
    rows.insert(min(insert_at, len(rows)), exact_row)
    _write_csv(path, fields, rows)


def _set_pin_phase(path: Path, *, prepared: bool) -> None:
    fields, rows = _read_csv(path)
    rows = [row for row in rows if row.get("model_id") != REVENUE_MODEL_ID]
    if prepared:
        rows.append({field: PREPARED_PIN_ROW.get(field, "") for field in fields})
    _write_csv(path, fields, rows)


def _copy_registries(tmp_path: Path, *, prepared: bool = False) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for name, (source, _) in REGISTRY_SPECS.items():
        fields, rows = _read_csv(source)
        destination = tmp_path / source.name
        _write_csv(destination, fields, rows)
        paths[name] = destination
    _replace_revenue_row(
        paths["contract"],
        "model_id",
        PREPARED_REVENUE_CONTRACT if prepared else LEGACY_REVENUE_CONTRACT,
    )
    _replace_revenue_row(
        paths["condition"],
        "model_id",
        PREPARED_REVENUE_CONDITION if prepared else LEGACY_REVENUE_CONDITION,
    )
    _replace_revenue_row(
        paths["surface"],
        "surface_id",
        PREPARED_REVENUE_SURFACE if prepared else LEGACY_REVENUE_SURFACE,
    )
    _set_pin_phase(paths["pins"], prepared=prepared)
    return paths


def _mutate_revenue_row(
    path: Path,
    id_column: str,
    *,
    updates: dict[str, str] | None = None,
    remove: bool = False,
    duplicate: bool = False,
) -> None:
    fields, rows = _read_csv(path)
    indexes = [index for index, row in enumerate(rows) if row.get(id_column) == REVENUE_MODEL_ID]
    assert len(indexes) == 1
    index = indexes[0]
    if remove:
        rows.pop(index)
    else:
        rows[index].update(updates or {})
        if duplicate:
            rows.append(dict(rows[index]))
    _write_csv(path, fields, rows)


def _set_prepared_phase(paths: dict[str, Path]) -> None:
    _replace_revenue_row(paths["contract"], "model_id", PREPARED_REVENUE_CONTRACT)
    _replace_revenue_row(paths["condition"], "model_id", PREPARED_REVENUE_CONDITION)
    _replace_revenue_row(paths["surface"], "surface_id", PREPARED_REVENUE_SURFACE)


def _add_prepared_pin(paths: dict[str, Path]) -> None:
    _set_pin_phase(paths["pins"], prepared=True)


def _validate_paths(paths: dict[str, Path]) -> list[str]:
    return validate(
        pin_registry=paths["pins"],
        contract_registry=paths["contract"],
        condition_spec_registry=paths["condition"],
        surface_registry=paths["surface"],
        evidence_root=ROOT,
    )


def _canonical_row_sha256(row: dict[str, str]) -> str:
    payload = json.dumps(
        row,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def test_formal_model_evidence_pins_validate() -> None:
    assert validate() == []


def test_prepared_fixture_matches_reviewed_b9_rows() -> None:
    fixtures = {
        "contract": PREPARED_REVENUE_CONTRACT,
        "condition": PREPARED_REVENUE_CONDITION,
        "surface": PREPARED_REVENUE_SURFACE,
        "pin": {
            field: value
            for field, value in PREPARED_PIN_ROW.items()
            if field != "model_id"
        },
    }
    assert {
        name: _canonical_row_sha256(row)
        for name, row in fixtures.items()
    } == PREPARED_B9_ROW_SHA256


def test_legacy_fixture_matches_reviewed_ba78_rows() -> None:
    fixtures = {
        "contract": LEGACY_REVENUE_CONTRACT,
        "condition": LEGACY_REVENUE_CONDITION,
        "surface": LEGACY_REVENUE_SURFACE,
    }
    assert {
        name: _canonical_row_sha256(row)
        for name, row in fixtures.items()
    } == LEGACY_BA78_ROW_SHA256


def test_legacy_v2_exact_state_requires_no_revenue_pin(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    assert _validate_paths(paths) == []

    _add_prepared_pin(paths)
    errors = _validate_paths(paths)
    assert any("unexpected formal model evidence pins" in error for error in errors)


def test_prepared_v3_exact_state_requires_exact_revenue_pin(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path, prepared=True)
    assert _validate_paths(paths) == []


def test_prepared_v3_without_revenue_pin_fails_closed(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    _set_prepared_phase(paths)
    errors = _validate_paths(paths)
    assert any("requires exactly one revenue_unreacted_range evidence pin" in error for error in errors)
    assert any("missing formal model evidence pins" in error for error in errors)


def test_prepared_v3_duplicate_revenue_pin_fails_closed(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    _set_prepared_phase(paths)
    _add_prepared_pin(paths)
    fields, rows = _read_csv(paths["pins"])
    revenue_row = next(row for row in rows if row.get("model_id") == REVENUE_MODEL_ID)
    rows.append(dict(revenue_row))
    _write_csv(paths["pins"], fields, rows)

    errors = _validate_paths(paths)
    assert any("requires exactly one revenue_unreacted_range evidence pin" in error for error in errors)
    assert any("duplicate formal model evidence pins" in error for error in errors)


@pytest.mark.parametrize(
    "prepared_registries",
    [
        {"contract"},
        {"condition"},
        {"surface"},
        {"contract", "condition"},
        {"contract", "surface"},
        {"condition", "surface"},
    ],
)
def test_partial_prepared_registry_transition_is_rejected(
    tmp_path: Path,
    prepared_registries: set[str],
) -> None:
    paths = _copy_registries(tmp_path)
    if "contract" in prepared_registries:
        _replace_revenue_row(paths["contract"], "model_id", PREPARED_REVENUE_CONTRACT)
    if "condition" in prepared_registries:
        _replace_revenue_row(paths["condition"], "model_id", PREPARED_REVENUE_CONDITION)
    if "surface" in prepared_registries:
        _replace_revenue_row(paths["surface"], "surface_id", PREPARED_REVENUE_SURFACE)
    errors = _validate_paths(paths)
    assert any("unsupported or mixed revenue formal evidence phase" in error for error in errors)


@pytest.mark.parametrize(
    "permission",
    [
        "approved_for_daily_pdf",
        "approved_for_tdcc_weekly_pdf",
        "approved_for_individual_pdf",
    ],
)
@pytest.mark.parametrize(
    ("registry_name", "id_column"),
    [("contract", "model_id"), ("surface", "surface_id")],
)
def test_prepared_v3_requires_all_pdf_permissions_false(
    tmp_path: Path,
    registry_name: str,
    id_column: str,
    permission: str,
) -> None:
    paths = _copy_registries(tmp_path)
    _set_prepared_phase(paths)
    _add_prepared_pin(paths)
    _mutate_revenue_row(paths[registry_name], id_column, updates={permission: "true"})
    errors = _validate_paths(paths)
    assert any("unsupported or mixed revenue formal evidence phase" in error for error in errors)


def test_unknown_revenue_contract_version_is_rejected(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    _mutate_revenue_row(paths["contract"], "model_id", updates={"contract_version": "v4"})
    errors = _validate_paths(paths)
    assert any("unsupported or mixed revenue formal evidence phase" in error for error in errors)


def test_registry_values_without_headers_fail_closed(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    text = paths["surface"].read_text(encoding="utf-8")
    lines = text.splitlines()
    revenue_index = next(
        index for index, line in enumerate(lines) if line.startswith(f"{REVENUE_MODEL_ID},")
    )
    lines[revenue_index] += ",unexpected"
    paths["surface"].write_text("\n".join(lines) + "\n", encoding="utf-8")
    errors = _validate_paths(paths)
    assert any("values without headers" in error for error in errors)


@pytest.mark.parametrize(
    ("registry_name", "id_column", "field"),
    [
        ("contract", "model_id", "input_columns"),
        ("contract", "model_id", "output_columns"),
        ("contract", "model_id", "production_source_file"),
        ("condition", "model_id", "operation_contract"),
        ("surface", "surface_id", "implementation_sources"),
        ("surface", "surface_id", "notes"),
    ],
)
def test_prepared_v3_rejects_legacy_business_semantic_fields(
    tmp_path: Path,
    registry_name: str,
    id_column: str,
    field: str,
) -> None:
    paths = _copy_registries(tmp_path)
    _, legacy_rows = _read_csv(paths[registry_name])
    legacy_row = next(row for row in legacy_rows if row.get(id_column) == REVENUE_MODEL_ID)
    legacy_value = legacy_row[field]
    _set_prepared_phase(paths)
    _add_prepared_pin(paths)
    _mutate_revenue_row(
        paths[registry_name],
        id_column,
        updates={field: legacy_value},
    )
    errors = _validate_paths(paths)
    assert any("unsupported or mixed revenue formal evidence phase" in error for error in errors)


@pytest.mark.parametrize(
    ("field", "invalid_value"),
    [
        ("approval_version", "wrong_approval"),
        ("evidence_path", "config/approved_operation_evidence/wrong.csv"),
        ("evidence_format", "text"),
        ("evidence_version", "wrong_version"),
        ("evidence_version_column", "wrong_column"),
        ("canonical_sha256", "0" * 64),
        ("owner_lane", "research_backtest"),
        ("pin_status", "advisory"),
        ("notes", "mutable note"),
    ],
)
def test_prepared_v3_revenue_pin_fields_are_exact(
    tmp_path: Path,
    field: str,
    invalid_value: str,
) -> None:
    paths = _copy_registries(tmp_path)
    _set_prepared_phase(paths)
    _add_prepared_pin(paths)
    _mutate_revenue_row(paths["pins"], "model_id", updates={field: invalid_value})
    errors = _validate_paths(paths)
    assert any(f"prepared evidence pin {field} mismatch" in error for error in errors)


@pytest.mark.parametrize(
    ("registry_name", "id_column"),
    [
        ("contract", "model_id"),
        ("condition", "model_id"),
        ("surface", "surface_id"),
    ],
)
@pytest.mark.parametrize("mutation", ["missing", "duplicate"])
def test_revenue_phase_registry_requires_exactly_one_row(
    tmp_path: Path,
    registry_name: str,
    id_column: str,
    mutation: str,
) -> None:
    paths = _copy_registries(tmp_path)
    _mutate_revenue_row(
        paths[registry_name],
        id_column,
        remove=mutation == "missing",
        duplicate=mutation == "duplicate",
    )
    errors = _validate_paths(paths)
    assert any("must contain exactly one revenue_unreacted_range row" in error for error in errors)


def test_existing_required_pin_remains_required_in_legacy_and_prepared_phases(
    tmp_path: Path,
) -> None:
    for prepared in (False, True):
        phase_path = tmp_path / ("prepared" if prepared else "legacy")
        phase_path.mkdir()
        paths = _copy_registries(phase_path)
        if prepared:
            _set_prepared_phase(paths)
            _add_prepared_pin(paths)
        fields, rows = _read_csv(paths["pins"])
        removed_model = "price_pullback_23ema"
        rows = [row for row in rows if row.get("model_id") != removed_model]
        _write_csv(paths["pins"], fields, rows)
        errors = _validate_paths(paths)
        assert any(
            "missing formal model evidence pins" in error and removed_model in error
            for error in errors
        )


def test_unexpected_non_revenue_pin_remains_rejected(tmp_path: Path) -> None:
    paths = _copy_registries(tmp_path)
    fields, rows = _read_csv(paths["pins"])
    unexpected = dict(rows[0])
    unexpected["model_id"] = "unexpected_model"
    rows.append(unexpected)
    _write_csv(paths["pins"], fields, rows)
    errors = _validate_paths(paths)
    assert any(
        "unexpected formal model evidence pins" in error and "unexpected_model" in error
        for error in errors
    )


def test_approved_operation_rows_carry_exact_evidence_pins() -> None:
    approval = build_approval("2026-07-12 00:00:00 Asia/Taipei")
    assert len(approval) == 6
    for _, row in approval.iterrows():
        pin = evidence_pin_for_model(str(row["model_id"]), str(row["approval_version"]))
        assert row["evidence_artifact_version"] == pin.evidence_version
        assert row["evidence_canonical_sha256"] == pin.canonical_sha256
        assert row["evidence_pin_source"] == pin.evidence_path


def test_price_pullback_pin_uses_promoted_spec_not_mutable_latest() -> None:
    pin = evidence_pin_for_model(
        "price_pullback_23ema",
        "price_pullback_23ema_operation_v1_20260703",
    )
    assert pin.evidence_path == "docs/specs/price_pullback_23ema_operation_candidate_spec.md"
    assert "latest" not in pin.evidence_path
