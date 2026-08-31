from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import archive_revenue_unreacted_range_legacy_runtime_evidence as producer  # noqa: E402
import validate_revenue_unreacted_range_legacy_runtime_evidence as validator  # noqa: E402


def _source_bytes(rows: list[dict[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=("signal_date", "stock_id", "model_id", "model_score"),
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return b"\xef\xbb\xbf" + output.getvalue().encode("utf-8")


def test_canonical_archive_preserves_only_legacy_rows_in_source_order() -> None:
    source = _source_bytes(
        [
            {
                "signal_date": "20260827",
                "stock_id": "1111",
                "model_id": producer.MODEL_ID,
                "model_score": "80",
            },
            {
                "signal_date": "20260828",
                "stock_id": "2222",
                "model_id": "price_pullback_23ema",
                "model_score": "70",
            },
            {
                "signal_date": "20260828",
                "stock_id": "3333",
                "model_id": producer.MODEL_ID,
                "model_score": "90",
            },
        ]
    )

    archive, source_count, archived_count, first_date, last_date = (
        producer.canonical_legacy_rows(source)
    )

    parsed = list(
        csv.DictReader(io.StringIO(archive.decode("utf-8-sig"), newline=""))
    )
    assert source_count == 3
    assert archived_count == 2
    assert [row["stock_id"] for row in parsed] == ["1111", "3333"]
    assert {row["model_id"] for row in parsed} == {producer.MODEL_ID}
    assert first_date == "20260827"
    assert last_date == "20260828"


def test_validator_replays_exact_committed_source_slice(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo = tmp_path / "repo"
    source_path = repo / producer.SOURCE_ARTIFACT
    source_path.parent.mkdir(parents=True)
    source = _source_bytes(
        [
            {
                "signal_date": "20260828",
                "stock_id": "6177",
                "model_id": producer.MODEL_ID,
                "model_score": "88",
            },
            {
                "signal_date": "20260828",
                "stock_id": "9999",
                "model_id": "price_pullback_23ema",
                "model_score": "70",
            },
        ]
    )
    source_path.write_bytes(source)
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "fixture"], cwd=repo, check=True)

    archive_path, manifest_row = producer.archive(repo, "HEAD")
    manifest = repo / producer.MANIFEST_PATH

    assert archive_path.exists()
    assert manifest_row["archived_row_count"] == "1"
    assert manifest_row["archive_artifact_sha256"] == hashlib.sha256(
        producer.canonical_csv_bytes(archive_path.read_bytes())
    ).hexdigest()
    assert validator.validate(repo, manifest) == []

    archive_text = archive_path.read_bytes().decode("utf-8-sig")
    archive_path.write_bytes(
        ("\ufeff" + archive_text.replace(",88\n", ",89\n")).encode("utf-8")
    )
    errors = validator.validate(repo, manifest)
    assert any("archive canonical semantic SHA-256 mismatch" in error for error in errors)


def test_archive_validator_ignores_raw_crlf_checkout_form(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    source_path = repo / producer.SOURCE_ARTIFACT
    source_path.parent.mkdir(parents=True)
    source_path.write_bytes(
        _source_bytes(
            [
                {
                    "signal_date": "20260828",
                    "stock_id": "6177",
                    "model_id": producer.MODEL_ID,
                    "model_score": "88",
                }
            ]
        )
    )
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "fixture"], cwd=repo, check=True)

    archive_path, manifest_row = producer.archive(repo, "HEAD")
    canonical = producer.canonical_csv_bytes(archive_path.read_bytes())
    crlf = canonical.decode("utf-8-sig").replace("\n", "\r\n")
    archive_path.write_bytes(("\ufeff" + crlf).encode("utf-8"))

    assert hashlib.sha256(producer.canonical_csv_bytes(archive_path.read_bytes())).hexdigest() == (
        manifest_row["archive_artifact_sha256"]
    )
    assert validator.validate(repo, repo / producer.MANIFEST_PATH) == []


def test_archive_is_idempotent_and_manifest_is_append_only(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    source_path = repo / producer.SOURCE_ARTIFACT
    source_path.parent.mkdir(parents=True)
    source_path.write_bytes(
        _source_bytes(
            [
                {
                    "signal_date": "20260828",
                    "stock_id": "6177",
                    "model_id": producer.MODEL_ID,
                    "model_score": "88",
                }
            ]
        )
    )
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "fixture"], cwd=repo, check=True)

    archive_path, _ = producer.archive(repo, "HEAD")
    first_archive = archive_path.read_bytes()
    first_manifest = (repo / producer.MANIFEST_PATH).read_bytes()
    producer.archive(repo, "HEAD")

    assert archive_path.read_bytes() == first_archive
    assert (repo / producer.MANIFEST_PATH).read_bytes() == first_manifest
