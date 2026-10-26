from __future__ import annotations

import csv
import io
from pathlib import Path
import shutil
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_neckline_operation_metadata import (  # noqa: E402
    CSV_CONSUMERS,
    DETAIL_PATH,
    MARKDOWN_PATHS,
    MODEL_ID,
    validate_metadata,
)


@pytest.fixture
def evidence_root(tmp_path: Path) -> Path:
    paths = [DETAIL_PATH, Path("scripts/build_approved_operation_patterns.py"), *MARKDOWN_PATHS]
    for output, mirror, *_ in CSV_CONSUMERS:
        paths.extend((output, mirror))
    for relative in paths:
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    return tmp_path


def mutate_csv(path: Path, selector: dict[str, str], field: str | None, value: str = "") -> None:
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
    fields = list(rows[0])
    selected = [row for row in rows if all(row.get(key) == expected for key, expected in selector.items())]
    assert len(selected) == 1
    if field is None:
        rows.remove(selected[0])
    else:
        selected[0][field] = value
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(stream.getvalue(), encoding="utf-8-sig", newline="")


def test_frozen_metadata_preserves_51_trades_and_50_stocks(evidence_root: Path) -> None:
    assert validate_metadata(evidence_root) == []
    rows = list(csv.DictReader(io.StringIO((evidence_root / DETAIL_PATH).read_text(encoding="utf-8-sig"))))
    assert len(rows) == 51
    assert len({row["stock_id"] for row in rows}) == 50
    assert sum(row["stock_id"] == "2368" for row in rows) == 2


@pytest.mark.parametrize("consumer", CSV_CONSUMERS)
def test_wrong_distinct_count_fails_even_when_mirrors_agree(evidence_root: Path, consumer: tuple) -> None:
    output, mirror, selector, _, stock_field = consumer
    for relative in (output, mirror):
        mutate_csv(evidence_root / relative, selector, stock_field, "51")
    errors = validate_metadata(evidence_root)
    assert any(stock_field in error and "50" in error for error in errors)


@pytest.mark.parametrize("consumer", CSV_CONSUMERS)
def test_missing_neckline_row_fails(evidence_root: Path, consumer: tuple) -> None:
    output, mirror, selector, *_ = consumer
    for relative in (output, mirror):
        mutate_csv(evidence_root / relative, selector, None)
    assert any("指定頸線中繼資料" in error for error in validate_metadata(evidence_root))


@pytest.mark.parametrize("consumer", CSV_CONSUMERS)
def test_csv_mirror_drift_fails(evidence_root: Path, consumer: tuple) -> None:
    _, mirror, selector, _, stock_field = consumer
    mutate_csv(evidence_root / mirror, selector, stock_field, "51")
    assert any("mirror" in error for error in validate_metadata(evidence_root))


def test_changed_trade_population_fails_frozen_sha(evidence_root: Path) -> None:
    path = evidence_root / DETAIL_PATH
    content = path.read_bytes()
    assert b"272.0000" in content
    path.write_bytes(content.replace(b"272.0000", b"273.0000", 1))
    assert any("SHA-256" in error for error in validate_metadata(evidence_root))


def test_windows_line_endings_keep_canonical_frozen_sha(evidence_root: Path) -> None:
    path = evidence_root / DETAIL_PATH
    path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
    assert validate_metadata(evidence_root) == []


def test_trade_count_must_not_be_changed_to_distinct_count(evidence_root: Path) -> None:
    output, mirror, selector, trade_fields, _ = CSV_CONSUMERS[0]
    for relative in (output, mirror):
        mutate_csv(evidence_root / relative, selector, trade_fields[0], "50")
    assert any(trade_fields[0] in error for error in validate_metadata(evidence_root))


def test_duplicate_approved_row_fails(evidence_root: Path) -> None:
    output, _, selector, *_ = CSV_CONSUMERS[1]
    path = evidence_root / output
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
    selected = next(row for row in rows if all(row.get(key) == expected for key, expected in selector.items()))
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writerow(selected)
    with path.open("a", encoding="utf-8", newline="") as handle:
        handle.write(stream.getvalue())
    assert any("實際 2" in error for error in validate_metadata(evidence_root))


def test_incorrect_producer_constant_fails_without_importing_producer(evidence_root: Path) -> None:
    path = evidence_root / "scripts/build_approved_operation_patterns.py"
    content = path.read_text(encoding="utf-8")
    start = content.index("NECKLINE_APPROVAL_METRICS = {")
    end = content.index("\n}", start)
    block = content[start:end]
    assert '"unique_stock_count": "50"' in block
    path.write_text(content[:start] + block.replace('"unique_stock_count": "50"', '"unique_stock_count": "51"') + content[end:], encoding="utf-8")
    assert any("NECKLINE_APPROVAL_METRICS[unique_stock_count]" in error for error in validate_metadata(evidence_root))


def test_markdown_count_and_mirror_drift_fail(evidence_root: Path) -> None:
    path = evidence_root / MARKDOWN_PATHS[1]
    content = path.read_text(encoding="utf-8")
    line = next(line for line in content.splitlines() if line.startswith(f"| {MODEL_ID} |"))
    assert " | 51 | 50 | " in line
    path.write_text(content.replace(line, line.replace(" | 51 | 50 | ", " | 51 | 51 | ")), encoding="utf-8")
    errors = validate_metadata(evidence_root)
    assert any("Markdown" in error for error in errors)
    assert any("mirror" in error for error in errors)


def test_unrelated_first_pass_population_is_not_reinterpreted(evidence_root: Path) -> None:
    output, _, *_ = CSV_CONSUMERS[1]
    rows = list(csv.DictReader(io.StringIO((evidence_root / output).read_text(encoding="utf-8-sig"))))
    row = next(row for row in rows if row["model_id"] == MODEL_ID and row["sample_status"] == "ok_first_pass")
    assert (row["selected_stock_days"], row["selected_unique_stocks"]) == ("8590", "1722")
    assert validate_metadata(evidence_root) == []
