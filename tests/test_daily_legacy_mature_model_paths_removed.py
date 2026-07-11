from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_daily_legacy_mature_model_paths_removed as validator


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def test_legacy_mature_model_path_validator_passes_current_repo() -> None:
    assert validator.main() == 0


def test_formal_csv_rejects_deprecated_or_alias_model_ids(monkeypatch, tmp_path: Path) -> None:
    path = tmp_path / "formal.csv"
    write_csv(path, [{"model_id": "w_bottom", "row_type": "data"}])
    monkeypatch.setattr(validator, "FORMAL_MODEL_ID_CSVS", (path,))

    errors = validator.validate_formal_csvs()

    assert errors
    assert "legacy or alias model_id=w_bottom" in errors[0]


def test_source_snippets_reject_executable_deprecated_functions(monkeypatch, tmp_path: Path) -> None:
    path = tmp_path / "model_layer.py"
    path.write_text("def cond_platform_strength(row):\n    return True\n", encoding="utf-8")
    monkeypatch.setattr(validator, "FORBIDDEN_SOURCE_SNIPPETS", {path: ("def cond_platform_strength(",)})

    errors = validator.validate_source_snippets()

    assert errors
    assert "def cond_platform_strength(" in errors[0]


def test_operation_adapter_rejects_unexpected_model_id(monkeypatch, tmp_path: Path) -> None:
    path = tmp_path / "adapter.csv"
    write_csv(
        path,
        [
            {
                "model_id": "price_pullback_23ema_research",
                "row_type": "data",
                "approved_for_daily": "True",
                "operation_module_approved_for_daily": "True",
            }
        ],
    )
    monkeypatch.setattr(validator, "EXPECTED_ADAPTER_MODELS", {path: {"price_pullback_23ema"}})

    errors = validator.validate_adapter_model_sets()

    assert errors
    assert "unexpected model_ids" in errors[0]
