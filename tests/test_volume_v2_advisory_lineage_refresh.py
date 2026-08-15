from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_volume_v2_advisory_lineage_refresh as validator  # noqa: E402


STOCK_IDS = ("1111", "2222", *(str(stock_id) for stock_id in range(3001, 3012)))


def _git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args], stderr=subprocess.STDOUT, text=True
    ).strip()


def _write(repo: Path, relative_path: str, payload: str | bytes) -> None:
    path = repo / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, bytes):
        path.write_bytes(payload)
    else:
        path.write_text(payload, encoding="utf-8", newline="")


def _csv_bytes(columns: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames is not None
        return list(reader.fieldnames), list(reader)


def _write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.write_bytes(_csv_bytes(columns, rows))


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _fixture_slice_sha(path: Path, signal_date: str) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    header = rows[0]
    date_index = header.index("date")
    selected = [header]
    for row in rows[1:]:
        normalized_date = row[date_index].replace("-", "")
        if normalized_date <= signal_date:
            canonical_row = list(row)
            canonical_row[date_index] = normalized_date
            selected.append(canonical_row)
    stream = io.StringIO(newline="")
    csv.writer(stream, lineterminator="\n").writerows(selected)
    return _sha(stream.getvalue().encode("utf-8"))


def _theme_layer_md(watch_sha: str, generated_at: str) -> str:
    return (
        "# Volume Attack Theme Layer\n\n"
        f"- generated_at: `{generated_at}`\n"
        "- signal_date: `20260811`\n"
        f"- source_watch_sha256: `{watch_sha}`\n\n"
        "| theme_name | score |\n"
        "|:--|--:|\n"
        "| semiconductor | 100 |\n"
    )


def _theme_stocks_md(watch_sha: str, generated_at: str) -> str:
    return (
        "# Volume Attack Theme Stocks\n\n"
        f"- generated_at: `{generated_at}`\n"
        "- signal_date: `20260811`\n"
        f"- source_watch_sha256: `{watch_sha}`\n\n"
        "| stock_id | volume_breakout_score |\n"
        "|:--|--:|\n"
        "| 1111 | 63.56 |\n"
        "| 2222 | 58.61 |\n"
    )


@pytest.fixture
def refresh_repo(tmp_path: Path) -> tuple[Path, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init")
    _git(repo, "config", "user.name", "validator-test")
    _git(repo, "config", "user.email", "validator-test@example.com")
    _git(repo, "config", "core.autocrlf", "false")

    canonical_payloads = {
        stock_id: (
            "date,close\n"
            f"20260811,{position * 10}\n"
            f"20260812,{position * 10 + 1}\n"
        ).encode("utf-8")
        for position, stock_id in enumerate(STOCK_IDS, start=1)
    }
    for stock_id, payload in canonical_payloads.items():
        _write(repo, f"data/stock_price_history/{stock_id}.csv", payload)

    watch_columns = [
        "advisory_volume_breakout_rank",
        "signal_date",
        "advisory_score_as_of",
        "stock_id",
        "stock_name",
        "advisory_score_source_artifact",
        "advisory_score_source_sha256",
        "advisory_volume_breakout_score",
    ]
    watch_rows = [
        {
            "advisory_volume_breakout_rank": str(position),
            "signal_date": "20260811",
            "advisory_score_as_of": "2026-08-11",
            "stock_id": stock_id,
            "stock_name": f"Stock-{stock_id}",
            "advisory_score_source_artifact": f"data/stock_price_history/{stock_id}.csv",
            "advisory_score_source_sha256": f"{position:064x}",
            "advisory_volume_breakout_score": f"{64 - position / 2:.2f}",
        }
        for position, stock_id in enumerate(STOCK_IDS, start=1)
    ]
    watch_payload = _csv_bytes(watch_columns, watch_rows)
    _write(repo, validator.WATCH_CSV, watch_payload)
    old_watch_sha = _sha(watch_payload)

    stock_columns = [
        "stock_id",
        "stock_name",
        "advisory_score_source_sha256",
        "volume_breakout_score",
        "volume_breakout_rank",
        "volume_watch_source_artifact",
        "volume_watch_source_sha256",
        "theme_name",
    ]
    stock_rows = [
        {
            "stock_id": row["stock_id"],
            "stock_name": row["stock_name"],
            "advisory_score_source_sha256": row["advisory_score_source_sha256"],
            "volume_breakout_score": row["advisory_volume_breakout_score"],
            "volume_breakout_rank": row["advisory_volume_breakout_rank"],
            "volume_watch_source_artifact": validator.WATCH_CSV,
            "volume_watch_source_sha256": old_watch_sha,
            "theme_name": "semiconductor",
        }
        for row in watch_rows
    ]
    stock_payload = _csv_bytes(stock_columns, stock_rows)

    theme_payload = _csv_bytes(
        ["theme_name", "theme_strength_score", "interpretation"],
        [
            {
                "theme_name": "semiconductor",
                "theme_strength_score": "100",
                "interpretation": "unchanged business result",
            }
        ],
    )
    theme_md = _theme_layer_md(old_watch_sha, "2026-08-11 20:00:17 Asia/Taipei")
    stock_md = _theme_stocks_md(old_watch_sha, "2026-08-11 20:00:17 Asia/Taipei")

    _write(repo, validator.THEME_LAYER_CSV, theme_payload)
    _write(repo, validator.DOCS_THEME_LAYER_CSV, theme_payload)
    _write(repo, validator.THEME_LAYER_MD, theme_md)
    _write(repo, validator.DOCS_THEME_LAYER_MD, theme_md)
    _write(repo, validator.THEME_STOCKS_CSV, stock_payload)
    _write(repo, validator.DOCS_THEME_STOCKS_CSV, stock_payload)
    _write(repo, validator.THEME_STOCKS_MD, stock_md)
    _write(repo, validator.DOCS_THEME_STOCKS_MD, stock_md)

    _write(
        repo,
        validator.WATCH_MD,
        "# Watch\n\n- generated_at: `2026-08-11 20:00:17 Asia/Taipei`\n- rows: `13`\n",
    )
    _write(
        repo,
        validator.WATCH_PACKET_MD,
        "# Packet\n\n- generated_at: `2026-08-11 20:00:17 Asia/Taipei`\n- rows: `13`\n",
    )
    _write(
        repo,
        validator.VALIDATION_JSON,
        json.dumps(
            {
                "status": "pass",
                "validated_at": "2026-08-11T20:00:17+08:00",
                "rows": 13,
            },
            indent=2,
        )
        + "\n",
    )
    _write(
        repo,
        validator.VALIDATION_MD,
        "# Validation\n\n- validated_at: `2026-08-11 20:00:17 Asia/Taipei`\n- status: `pass`\n",
    )

    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "base artifacts")
    return repo, _git(repo, "rev-parse", "HEAD")


def _apply_refresh(repo: Path, *, metadata_changes: bool = False) -> None:
    watch_path = repo / validator.WATCH_CSV
    watch_columns, watch_rows = _read_csv(watch_path)
    for row in watch_rows:
        source = repo / row["advisory_score_source_artifact"]
        row["advisory_score_source_sha256"] = _fixture_slice_sha(
            source, row["advisory_score_as_of"].replace("-", "")
        )
    _write_csv(watch_path, watch_columns, watch_rows)
    watch_sha = _sha(watch_path.read_bytes())

    stock_path = repo / validator.THEME_STOCKS_CSV
    stock_columns, stock_rows = _read_csv(stock_path)
    watch_by_stock = {
        row["stock_id"]: row["advisory_score_source_sha256"] for row in watch_rows
    }
    for row in stock_rows:
        row["advisory_score_source_sha256"] = watch_by_stock[row["stock_id"]]
        row["volume_watch_source_sha256"] = watch_sha
    _write_csv(stock_path, stock_columns, stock_rows)
    _write(repo, validator.DOCS_THEME_STOCKS_CSV, stock_path.read_bytes())

    theme_md = _theme_layer_md(watch_sha, "2026-08-15 10:20:30 Asia/Taipei")
    stock_md = _theme_stocks_md(watch_sha, "2026-08-15 10:20:30 Asia/Taipei")
    _write(repo, validator.THEME_LAYER_MD, theme_md)
    _write(repo, validator.DOCS_THEME_LAYER_MD, theme_md)
    _write(repo, validator.THEME_STOCKS_MD, stock_md)
    _write(repo, validator.DOCS_THEME_STOCKS_MD, stock_md)

    if metadata_changes:
        _write(
            repo,
            validator.WATCH_MD,
            "# Watch\n\n- generated_at: `2026-08-15 10:20:30 Asia/Taipei`\n- rows: `13`\n",
        )
        _write(
            repo,
            validator.WATCH_PACKET_MD,
            "# Packet\n\n- generated_at: `2026-08-15 10:20:30 Asia/Taipei`\n- rows: `13`\n",
        )
        _write(
            repo,
            validator.VALIDATION_JSON,
            json.dumps(
                {
                    "status": "pass",
                    "validated_at": "2026-08-15T10:20:30+08:00",
                    "rows": 13,
                },
                indent=2,
            )
            + "\n",
        )
        _write(
            repo,
            validator.VALIDATION_MD,
            "# Validation\n\n- validated_at: `2026-08-15 10:20:30 Asia/Taipei`\n- status: `pass`\n",
        )


def _restore_metadata_paths(repo: Path, base_sha: str) -> None:
    for relative_path in validator.POST_BUILD_METADATA_ONLY:
        payload = subprocess.check_output(
            ["git", "-C", str(repo), "show", f"{base_sha}:{relative_path}"]
        )
        _write(repo, relative_path, payload)


def _commit_refresh(repo: Path, message: str = "refresh lineage") -> str:
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))
    _git(repo, "commit", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


def test_post_build_accepts_exact_refresh_and_four_metadata_only_changes(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo, metadata_changes=True)

    assert validator.validate_refresh(repo, base_sha, "post-build") == []


def test_final_accepts_exact_seven_paths_after_metadata_restore(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo, metadata_changes=True)
    _restore_metadata_paths(repo, base_sha)

    assert validator.validate_refresh(repo, base_sha, "final") == []
    assert set(_git(repo, "diff", "--name-only", base_sha).splitlines()) == set(
        validator.FINAL_EXPECTED_DIFF
    )


def test_staged_accepts_exact_seven_paths_and_no_residue(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))

    assert validator.validate_refresh(repo, base_sha, "staged") == []


def test_committed_accepts_one_clean_direct_child_with_exact_tree(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _commit_refresh(repo)

    assert validator.validate_refresh(repo, base_sha, "committed") == []


def test_committed_rejects_extra_commit_wrong_parent_and_revision_count(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _commit_refresh(repo)
    _git(repo, "commit", "--allow-empty", "-m", "unexpected extra commit")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("direct single parent=base" in error for error in errors)
    assert any("exactly one revision in base..HEAD" in error for error in errors)


def test_committed_rejects_staged_index_residue(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _commit_refresh(repo)
    path = repo / validator.THEME_STOCKS_MD
    path.write_text(path.read_text(encoding="utf-8") + "staged residue\n", encoding="utf-8")
    _git(repo, "add", validator.THEME_STOCKS_MD)

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("forbids index residue against HEAD" in error for error in errors)


def test_committed_rejects_unstaged_residue(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _commit_refresh(repo)
    path = repo / validator.THEME_STOCKS_MD
    path.write_text(path.read_text(encoding="utf-8") + "unstaged residue\n", encoding="utf-8")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("forbids unstaged residue" in error for error in errors)


def test_committed_rejects_untracked_residue(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _commit_refresh(repo)
    _write(repo, "untracked-residue.txt", "not allowed\n")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("forbids untracked residue" in error for error in errors)


def test_committed_rejects_non_100644_tree_mode(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))
    _git(repo, "update-index", "--chmod=+x", validator.WATCH_CSV)
    _git(repo, "commit", "-m", "refresh with wrong mode")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("must be mode 100644 blob" in error for error in errors)


def test_committed_rejects_non_blob_tree_type(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))
    _git(
        repo,
        "update-index",
        "--cacheinfo",
        "160000",
        base_sha,
        validator.WATCH_CSV,
    )
    _git(repo, "commit", "-m", "refresh with wrong object type")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("type=commit" in error for error in errors)
    assert any("must reference a blob object" in error for error in errors)


def test_committed_rejects_extra_committed_path(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _write(repo, "unexpected-committed-path.txt", "not allowed\n")
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF), "unexpected-committed-path.txt")
    _git(repo, "commit", "-m", "refresh with extra path")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("exact 7-path base..HEAD diff" in error for error in errors)


def test_committed_rejects_missing_committed_path(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    omitted = validator.DOCS_THEME_STOCKS_MD
    payload = subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{base_sha}:{omitted}"]
    )
    _write(repo, omitted, payload)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF - {omitted}))
    _git(repo, "commit", "-m", "refresh missing one path")

    errors = validator.validate_refresh(repo, base_sha, "committed")
    assert any("exact 7-path base..HEAD diff" in error for error in errors)


def test_canonical_slice_uses_as_of_and_ignores_future_rows(tmp_path: Path) -> None:
    source = tmp_path / "1111.csv"
    source.write_text(
        "date,close\n2026-08-10,9\n20260811,10\n20260812,11\n",
        encoding="utf-8",
    )
    expected = validator._canonical_csv_slice_sha256(source, "20260811")

    source.write_text(
        "date,close\n2026-08-10,9\n20260811,10\n20260812,999\n20260813,888\n",
        encoding="utf-8",
    )

    assert validator._canonical_csv_slice_sha256(source, "20260811") == expected


def test_canonical_slice_changes_when_through_as_of_value_changes(
    tmp_path: Path,
) -> None:
    source = tmp_path / "1111.csv"
    source.write_text(
        "date,close\n20260810,9\n20260811,10\n20260812,11\n",
        encoding="utf-8",
    )
    expected = validator._canonical_csv_slice_sha256(source, "20260811")
    source.write_text(
        "date,close\n20260810,9\n20260811,99\n20260812,11\n",
        encoding="utf-8",
    )

    assert validator._canonical_csv_slice_sha256(source, "20260811") != expected


def test_watch_missing_advisory_score_as_of_fails_closed(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    columns.remove("advisory_score_as_of")
    for row in rows:
        row.pop("advisory_score_as_of")
    _write_csv(path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("missing/invalid advisory_score_as_of" in error for error in errors)


def test_watch_invalid_advisory_score_as_of_fails_closed(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    rows[0]["advisory_score_as_of"] = "20260230"
    _write_csv(path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("missing/invalid advisory_score_as_of" in error for error in errors)


def test_watch_advisory_as_of_must_normalize_equal_to_signal_date(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    rows[0]["advisory_score_as_of"] = "2026-08-10"
    _write_csv(path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("must equal signal_date after normalization" in error for error in errors)


def test_watch_requires_exact_thirteen_rows(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    _write_csv(path, columns, rows[:-1])

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("requires exact 13 base/current rows" in error for error in errors)


def test_watch_requires_stale_to_new_lineage_on_all_thirteen_rows(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    base_payload = subprocess.check_output(
        ["git", "-C", str(repo), "show", f"{base_sha}:{validator.WATCH_CSV}"]
    )
    _base_columns, base_rows = validator._read_csv_bytes(base_payload, "base watch")
    rows[0][validator.WATCH_LINEAGE_COLUMN] = base_rows[0][validator.WATCH_LINEAGE_COLUMN]
    _write_csv(path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("stale lineage was not refreshed" in error for error in errors)
    assert any("changed=12 expected=13" in error for error in errors)


def test_watch_business_field_drift_fails_closed(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(path)
    rows[0]["advisory_volume_breakout_score"] = "99.99"
    _write_csv(path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("business/order drift" in error for error in errors)


def test_theme_stock_rank_drift_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.THEME_STOCKS_CSV
    columns, rows = _read_csv(path)
    rows[0]["volume_breakout_rank"] = "9"
    _write_csv(path, columns, rows)
    _write(repo, validator.DOCS_THEME_STOCKS_CSV, path.read_bytes())

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("business/order drift" in error for error in errors)


def test_watch_canonical_sha_mismatch_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    watch_path = repo / validator.WATCH_CSV
    columns, rows = _read_csv(watch_path)
    rows[0]["advisory_score_source_sha256"] = "f" * 64
    _write_csv(watch_path, columns, rows)

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("watch canonical SHA mismatch" in error for error in errors)


def test_watch_as_of_slice_rejects_through_date_source_mutation(
    refresh_repo: tuple[Path, str],
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    source = repo / "data/stock_price_history/1111.csv"
    source.write_text(
        source.read_text(encoding="utf-8").replace("20260811,10", "20260811,999"),
        encoding="utf-8",
    )

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("watch canonical SHA mismatch" in error for error in errors)


def test_theme_layer_csv_drift_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    for relative_path in validator.THEME_LAYER_CSV_PATHS:
        path = repo / relative_path
        _write(repo, relative_path, path.read_text(encoding="utf-8").replace("100", "99"))

    errors = validator.validate_refresh(repo, base_sha, "post-build")
    assert any("theme layer CSV must remain byte-identical" in error for error in errors)


def test_output_docs_mirror_mismatch_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.DOCS_THEME_STOCKS_MD
    path.write_text(path.read_text(encoding="utf-8") + "drift\n", encoding="utf-8")

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("output/docs mirror byte mismatch" in error for error in errors)


def test_metadata_business_change_fails_post_build(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo, metadata_changes=True)
    path = repo / validator.WATCH_PACKET_MD
    path.write_text(
        path.read_text(encoding="utf-8").replace("- rows: `13`", "- rows: `12`"),
        encoding="utf-8",
    )

    errors = validator.validate_refresh(repo, base_sha, "post-build")
    assert any("changed outside generated_at/validated_at" in error for error in errors)


def test_extra_path_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _write(repo, "output/latest/unapproved_refresh_artifact.csv", "x\n1\n")

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("outside temporary 13-path allowlist" in error for error in errors)


def test_invalid_or_non_exact_base_fails_closed(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)

    errors = validator.validate_refresh(repo, base_sha[:12], "final")
    assert errors == ["--base-sha must be an exact 40-hex commit SHA"]


def test_staged_phase_rejects_unstaged_residue(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))
    path = repo / validator.THEME_STOCKS_MD
    path.write_text(path.read_text(encoding="utf-8") + "unstaged\n", encoding="utf-8")

    errors = validator.validate_refresh(repo, base_sha, "staged")
    assert any("forbids unstaged residue" in error for error in errors)


def test_staged_phase_rejects_non_100644_mode(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    _git(repo, "add", *sorted(validator.FINAL_EXPECTED_DIFF))
    _git(repo, "update-index", "--chmod=+x", validator.WATCH_CSV)

    errors = validator.validate_refresh(repo, base_sha, "staged")
    assert any("mode 100644 regular file" in error for error in errors)


def test_final_phase_rejects_deleted_artifact(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    (repo / validator.THEME_STOCKS_MD).unlink()

    errors = validator.validate_refresh(repo, base_sha, "final")
    assert any("forbids delete/rename/add/type change" in error for error in errors)


def test_staged_phase_rejects_renamed_artifact(refresh_repo: tuple[Path, str]) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    renamed = "output/latest/renamed_volume_breakout_watch_latest.csv"
    _git(repo, "mv", validator.WATCH_CSV, renamed)
    _git(repo, "add", "--all")

    errors = validator.validate_refresh(repo, base_sha, "staged")
    assert any("forbids delete/rename/add/type change" in error for error in errors)


def test_cli_returns_nonzero_for_business_drift(
    refresh_repo: tuple[Path, str], capsys: pytest.CaptureFixture[str]
) -> None:
    repo, base_sha = refresh_repo
    _apply_refresh(repo)
    path = repo / validator.THEME_STOCKS_CSV
    columns, rows = _read_csv(path)
    rows.reverse()
    _write_csv(path, columns, rows)
    _write(repo, validator.DOCS_THEME_STOCKS_CSV, path.read_bytes())

    result = validator.main(
        ["--repo-root", str(repo), "--base-sha", base_sha, "--phase", "final"]
    )
    captured = capsys.readouterr()
    assert result == 1
    assert "ERROR:" in captured.out
    assert "business/order drift" in captured.out
