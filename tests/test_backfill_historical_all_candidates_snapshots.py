from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import backfill_historical_all_candidates_snapshots_from_git_history as backfill  # noqa: E402
import update_daily_published_model_snapshots as publisher  # noqa: E402
from update_daily_published_model_snapshots import ARTIFACTS, MANIFEST_COLUMNS  # noqa: E402


REVISION_COLUMNS = {
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
}


def run_git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def init_repo(repo: Path) -> None:
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "test@example.com")
    run_git(repo, "config", "user.name", "Test User")
    run_git(repo, "config", "core.autocrlf", "false")


def csv_payload(rows: list[dict[str, str]], *, lineterminator: str = "\n") -> bytes:
    return pd.DataFrame(rows).to_csv(
        index=False,
        lineterminator=lineterminator,
    ).encode("utf-8")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(csv_payload(rows))


def canonical_sha(payload: bytes) -> str:
    canonical = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(canonical).hexdigest()


def artifact(artifact_id: str):
    return next(item for item in ARTIFACTS if item.artifact_id == artifact_id)


def all_candidates_required_row(report_date: str, stock_id: str) -> dict[str, str]:
    item = artifact("all_candidates_source_rows")
    row = {column: "1" for column in item.required_columns}
    row.update(
        {
            "date": report_date,
            "signal_date": report_date,
            "main_price_date": report_date,
            "stock_id": stock_id,
            "stock_name": f"stock {stock_id}",
            "category": "pattern",
            "candidate_source_type": "individual_quality_candidate",
            "candidate_line": "pattern_watch",
            "candidate_line_group": "individual_pattern_watch",
            "source_row_index": "0",
            "close": "101",
            "ema23": "100",
            "ma20": "100",
            "distance_to_ema23_pct": "1.0",
            "gap_ema23_pct": "1.0",
            "platform_low": "95",
            "short_platform_low": "96",
            "previous_20d_low": "94",
            "low_20": "94",
            "ma5_turning_up_flag": "False",
            "ma10_turning_up_flag": "False",
            "volume_ratio": "1.2",
            "return_20d": "5.0",
            "latest_revenue_yoy": "10.0",
            "cumulative_revenue_yoy": "8.0",
            "off_60d_low_pct": "12.0",
            "tdcc_judgement": "mild_accumulation",
            "tdcc_accumulation_signal": "True",
            "warrant_flow_signal": "neutral",
            "false_breakout_risk": "False",
        }
    )
    return row


def formal_signal_row(report_date: str, stock_id: str) -> dict[str, str]:
    item = artifact("model_signals_for_report")
    row = {column: "1" for column in item.required_columns}
    row.update(
        {
            "signal_date": report_date,
            "stock_id": stock_id,
            "model_id": "volume_range_breakout_v2_low_position_volume_attack",
            "model_name_zh": "低位放量攻擊",
            "model_score": "80",
            "base_model_score": "70",
            "operation_score": "75",
            "tdcc_score": "2",
            "pattern_score": "3",
            "risk_penalty": "0",
            "final_rank_score": "80",
            "rank_reason_zh": "test",
        }
    )
    return row


def snapshot_manifest_row(
    *,
    repo: Path,
    report_date: str,
    artifact_id: str,
    revision: str,
    snapshot_path: Path,
    supersedes_sha: str = "",
    snapshot_sha: str | None = None,
    generated_at: str = "2026-06-30 09:00:00 Asia/Taipei",
) -> dict[str, str]:
    frame = pd.read_csv(snapshot_path, dtype=str, keep_default_na=False)
    digest = snapshot_sha or canonical_sha(snapshot_path.read_bytes())
    item = artifact(artifact_id)
    row = {column: "" for column in MANIFEST_COLUMNS}
    row.update(
        {
            "snapshot_report_date": report_date,
            "snapshot_revision": revision,
            "supersedes_snapshot_sha256": supersedes_sha,
            "revision_reason": "initial_publish" if revision == "r1" else "formal_sync",
            "generated_at": generated_at,
            "pipeline_commit_sha": f"pipeline-{revision}",
            "main_price_date": report_date,
            "report_ready": "True",
            "warrant_ready": "True",
            "warrant_source_status": "ok",
            "warrant_daily_publish_allowed": "True",
            "warrant_pdf_visibility": "visible",
            "warrant_model_effect_allowed": "True",
            "warrant_pdf_effect_allowed": "True",
            "daily_pdf_ready": "True",
            "artifact_id": artifact_id,
            "source_path": f"output/latest/{item.source_name}",
            "snapshot_path": snapshot_path.relative_to(repo).as_posix(),
            "source_sha256": digest,
            "snapshot_sha256": digest,
            "row_count": str(len(frame)),
            "column_count": str(len(frame.columns)),
            "purpose": "as_published_daily_model_snapshot",
        }
    )
    return row


def publish_formal_revision(
    *,
    repo: Path,
    manifest_path: Path,
    existing_manifest_rows: list[dict[str, str]],
    report_date: str,
    revision: str,
    formal_stock_id: str,
    candidate_stock_id: str,
    supersedes_formal_sha: str = "",
) -> tuple[dict[str, str], str]:
    formal_payload = csv_payload([formal_signal_row(report_date, formal_stock_id)])
    formal_sha = canonical_sha(formal_payload)
    formal_path = (
        repo
        / "output"
        / "history"
        / "daily_model_snapshots"
        / f"daily_candidate_model_signals_for_report_{report_date}_{revision}_{formal_sha[:12]}.csv"
    )
    formal_path.parent.mkdir(parents=True, exist_ok=True)
    formal_path.write_bytes(formal_payload)
    formal_manifest_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="model_signals_for_report",
        revision=revision,
        snapshot_path=formal_path,
        supersedes_sha=supersedes_formal_sha,
    )

    source = repo / backfill.ALL_CANDIDATES_SOURCE
    write_csv(source, [all_candidates_required_row(report_date, candidate_stock_id)])
    write_csv(manifest_path, [*existing_manifest_rows, formal_manifest_row])
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", f"publish {report_date} {revision}")
    return formal_manifest_row, run_git(repo, "rev-parse", "HEAD")


@pytest.mark.parametrize(
    "legacy_columns",
    [publisher.LEGACY_MANIFEST_COLUMNS, publisher.PRE_WARRANT_LEGACY_MANIFEST_COLUMNS],
)
def test_normalized_manifest_accepts_only_registered_legacy_headers(
    legacy_columns: list[str],
) -> None:
    row = {column: "" for column in legacy_columns}
    row.update(
        {
            "snapshot_report_date": "20260615",
            "warrant_ready": "True",
            "artifact_id": "data_freshness",
        }
    )
    payload = pd.DataFrame([row], columns=legacy_columns).to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")

    normalized = backfill.normalized_manifest(payload)

    assert list(normalized.columns) == MANIFEST_COLUMNS
    assert normalized.iloc[0]["snapshot_revision"] == "r1"
    assert normalized.iloc[0]["revision_reason"] == publisher.LEGACY_REVISION_REASON
    assert normalized.iloc[0]["warrant_source_status"] == "ok"


@pytest.mark.parametrize("removed_column", ["row_count", "revision_reason"])
def test_normalized_manifest_rejects_unapproved_partial_schema(
    removed_column: str,
) -> None:
    row = {column: "" for column in MANIFEST_COLUMNS}
    frame = pd.DataFrame([row], columns=MANIFEST_COLUMNS).drop(
        columns=[removed_column]
    )

    with pytest.raises(RuntimeError, match="unapproved daily snapshot manifest schema"):
        backfill.normalized_manifest(
            frame.to_csv(index=False, lineterminator="\n").encode("utf-8")
        )


def test_uses_exact_formal_publication_not_later_same_date_blob_and_pairs_r2(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"

    formal_r1, publication_r1 = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date="20260615",
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )

    # A newer blob with the same date is not publication evidence for formal r1.
    write_csv(
        repo / backfill.ALL_CANDIDATES_SOURCE,
        [all_candidates_required_row("20260615", "9999")],
    )
    run_git(repo, "add", backfill.ALL_CANDIDATES_SOURCE)
    run_git(repo, "commit", "-m", "later same-date candidate blob")

    r1_rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=["20260615"],
        generated_at="2026-06-30 10:00:00 Asia/Taipei",
    )

    assert len(r1_rows) == 1
    assert r1_rows.iloc[0]["snapshot_revision"] == "r1"
    assert r1_rows.iloc[0]["pipeline_commit_sha"] == publication_r1
    assert not Path(r1_rows.iloc[0]["snapshot_path"]).is_absolute()
    assert "\\" not in r1_rows.iloc[0]["snapshot_path"]
    assert r1_rows.iloc[0]["snapshot_path"].startswith(
        "output/history/daily_model_snapshots/"
    )
    r1_path = next(snapshot_dir.glob("all_candidates_20260615_r1_*.csv"))
    assert pd.read_csv(r1_path, dtype=str).iloc[0]["stock_id"] == "1234"
    r1_bytes = r1_path.read_bytes()

    current_manifest = pd.read_csv(manifest_path, dtype=str).fillna("").to_dict("records")
    formal_r2, publication_r2 = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=current_manifest,
        report_date="20260615",
        revision="r2",
        formal_stock_id="2222",
        candidate_stock_id="5678",
        supersedes_formal_sha=formal_r1["snapshot_sha256"],
    )

    r2_rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=["20260615"],
        overwrite=True,
        generated_at="2026-06-30 11:00:00 Asia/Taipei",
    )

    assert len(r2_rows) == 1
    assert r2_rows.iloc[0]["snapshot_revision"] == "r2"
    assert r2_rows.iloc[0]["pipeline_commit_sha"] == publication_r2
    assert r2_rows.iloc[0]["revision_reason"] == "git_history_backfill_correction"
    assert r2_rows.iloc[0]["supersedes_snapshot_sha256"] == r1_rows.iloc[0][
        "snapshot_sha256"
    ]
    assert r1_path.read_bytes() == r1_bytes
    r2_path = next(snapshot_dir.glob("all_candidates_20260615_r2_*.csv"))
    assert pd.read_csv(r2_path, dtype=str).iloc[0]["stock_id"] == "5678"

    manifest = pd.read_csv(manifest_path, dtype=str).fillna("")
    candidate_rows = manifest[manifest["artifact_id"].eq("all_candidates_source_rows")]
    assert list(candidate_rows["snapshot_revision"]) == ["r1", "r2"]
    assert formal_r2["supersedes_snapshot_sha256"] == formal_r1["snapshot_sha256"]


def test_legacy_crlf_same_payload_is_noop_and_preserves_raw_r1_identity(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"

    formal_payload = csv_payload([formal_signal_row(report_date, "1111")])
    formal_sha = canonical_sha(formal_payload)
    formal_path = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    formal_path.parent.mkdir(parents=True, exist_ok=True)
    formal_path.write_bytes(formal_payload)
    formal_manifest_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="model_signals_for_report",
        revision="r1",
        snapshot_path=formal_path,
    )

    logical_candidate_rows = [all_candidates_required_row(report_date, "1234")]
    write_csv(repo / backfill.ALL_CANDIDATES_SOURCE, logical_candidate_rows)
    legacy_candidate_path = snapshot_dir / f"all_candidates_{report_date}.csv"
    legacy_candidate_path.write_bytes(
        csv_payload(logical_candidate_rows, lineterminator="\r\n")
    )
    raw_crlf_sha = hashlib.sha256(legacy_candidate_path.read_bytes()).hexdigest()
    candidate_manifest_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="all_candidates_source_rows",
        revision="r1",
        snapshot_path=legacy_candidate_path,
        snapshot_sha=raw_crlf_sha,
    )

    legacy_columns = [column for column in MANIFEST_COLUMNS if column not in REVISION_COLUMNS]
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([formal_manifest_row, candidate_manifest_row])[legacy_columns].to_csv(
        manifest_path,
        index=False,
        lineterminator="\n",
    )
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "legacy r1 publication")
    manifest_before = manifest_path.read_bytes()
    candidate_before = legacy_candidate_path.read_bytes()

    rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=[report_date],
        overwrite=True,
        generated_at="2026-06-30 10:00:00 Asia/Taipei",
    )

    assert rows.empty
    assert manifest_path.read_bytes() == manifest_before
    assert legacy_candidate_path.read_bytes() == candidate_before
    assert hashlib.sha256(candidate_before).hexdigest() == raw_crlf_sha
    assert not list(snapshot_dir.glob(f"all_candidates_{report_date}_r2_*.csv"))


def test_backfill_rejects_raw_crlf_hash_for_formal_r2(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"
    formal_r1, _ = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date=report_date,
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )

    crlf_payload = csv_payload(
        [formal_signal_row(report_date, "2222")],
        lineterminator="\r\n",
    )
    raw_crlf_sha = hashlib.sha256(crlf_payload).hexdigest()
    formal_r2_path = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{report_date}_r2_"
        f"{raw_crlf_sha[:12]}.csv"
    )
    formal_r2_path.write_bytes(crlf_payload)
    formal_r2 = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="model_signals_for_report",
        revision="r2",
        snapshot_path=formal_r2_path,
        supersedes_sha=formal_r1["snapshot_sha256"],
        snapshot_sha=raw_crlf_sha,
    )
    write_csv(
        repo / backfill.ALL_CANDIDATES_SOURCE,
        [all_candidates_required_row(report_date, "5678")],
    )
    write_csv(manifest_path, [formal_r1, formal_r2])
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "publish noncanonical formal r2")
    manifest_before = manifest_path.read_bytes()

    with pytest.raises(RuntimeError, match="paired formal snapshot SHA"):
        backfill.backfill_historical_all_candidates_snapshots(
            repo_root=repo,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=[report_date],
        )

    assert manifest_path.read_bytes() == manifest_before
    assert not list(snapshot_dir.glob(f"all_candidates_{report_date}_r1_*.csv"))
    assert not publisher.manifest_publication_lock_path(manifest_path).exists()


def test_backfill_rejects_raw_crlf_hash_for_existing_candidate_r2(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"
    formal_r1, _ = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date=report_date,
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )
    formal_r2, _ = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[formal_r1],
        report_date=report_date,
        revision="r2",
        formal_stock_id="2222",
        candidate_stock_id="5678",
        supersedes_formal_sha=formal_r1["snapshot_sha256"],
    )

    candidate_r1_payload = csv_payload(
        [all_candidates_required_row(report_date, "1234")]
    )
    candidate_r1_sha = canonical_sha(candidate_r1_payload)
    candidate_r1_path = snapshot_dir / (
        f"all_candidates_{report_date}_r1_{candidate_r1_sha[:12]}.csv"
    )
    candidate_r1_path.write_bytes(candidate_r1_payload)
    candidate_r1 = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="all_candidates_source_rows",
        revision="r1",
        snapshot_path=candidate_r1_path,
    )

    candidate_r2_payload = csv_payload(
        [all_candidates_required_row(report_date, "5678")],
        lineterminator="\r\n",
    )
    candidate_r2_raw_sha = hashlib.sha256(candidate_r2_payload).hexdigest()
    candidate_r2_path = snapshot_dir / (
        f"all_candidates_{report_date}_r2_{candidate_r2_raw_sha[:12]}.csv"
    )
    candidate_r2_path.write_bytes(candidate_r2_payload)
    candidate_r2 = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="all_candidates_source_rows",
        revision="r2",
        snapshot_path=candidate_r2_path,
        supersedes_sha=candidate_r1_sha,
        snapshot_sha=candidate_r2_raw_sha,
    )
    write_csv(
        manifest_path,
        [formal_r1, candidate_r1, formal_r2, candidate_r2],
    )
    manifest_before = manifest_path.read_bytes()

    with pytest.raises(
        RuntimeError,
        match="existing all_candidates revision snapshot SHA",
    ):
        backfill.backfill_historical_all_candidates_snapshots(
            repo_root=repo,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=[report_date],
            overwrite=True,
        )

    assert manifest_path.read_bytes() == manifest_before
    assert not publisher.manifest_publication_lock_path(manifest_path).exists()


def test_backfill_relocates_exact_legacy_absolute_formal_and_candidate_paths(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"

    formal_payload = csv_payload([formal_signal_row(report_date, "1111")])
    formal_sha = canonical_sha(formal_payload)
    formal_path = snapshot_dir / (
        f"daily_candidate_model_signals_for_report_{report_date}_r1_"
        f"{formal_sha[:12]}.csv"
    )
    formal_path.parent.mkdir(parents=True, exist_ok=True)
    formal_path.write_bytes(formal_payload)
    formal_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="model_signals_for_report",
        revision="r1",
        snapshot_path=formal_path,
    )

    candidate_payload = csv_payload(
        [all_candidates_required_row(report_date, "1234")]
    )
    candidate_sha = canonical_sha(candidate_payload)
    candidate_path = snapshot_dir / (
        f"all_candidates_{report_date}_r1_{candidate_sha[:12]}.csv"
    )
    candidate_path.write_bytes(candidate_payload)
    candidate_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="all_candidates_source_rows",
        revision="r1",
        snapshot_path=candidate_path,
    )
    for row in (formal_row, candidate_row):
        row["snapshot_path"] = (
            "C:/retired-worktree/repository/" + row["snapshot_path"]
        )
    write_csv(repo / backfill.ALL_CANDIDATES_SOURCE, [all_candidates_required_row(report_date, "1234")])
    write_csv(manifest_path, [formal_row, candidate_row])
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "legacy absolute publication")
    manifest_before = manifest_path.read_bytes()

    rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=[report_date],
        overwrite=True,
    )

    assert rows.empty
    assert manifest_path.read_bytes() == manifest_before
    assert not publisher.manifest_publication_lock_path(manifest_path).exists()


def test_backfill_first_parent_publication_uses_merge_not_unmerged_branch_commit(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    (repo / "README.md").write_text("base\n", encoding="utf-8")
    run_git(repo, "add", "README.md")
    run_git(repo, "commit", "-m", "base")
    main_branch = run_git(repo, "branch", "--show-current")
    run_git(repo, "checkout", "-b", "formal-publication")
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    _, branch_commit = publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date="20260615",
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )
    run_git(repo, "checkout", main_branch)
    run_git(repo, "merge", "--no-ff", "formal-publication", "-m", "merge formal publication")
    merge_commit = run_git(repo, "rev-parse", "HEAD")

    publication_commits = backfill.git_manifest_commits(repo, manifest_path)
    assert branch_commit not in publication_commits
    assert publication_commits == [merge_commit]
    changed_paths = backfill.git_changed_paths(repo, merge_commit)
    assert backfill.git_tree_path(manifest_path, repo) in changed_paths
    assert any(
        path.startswith(
            "output/history/daily_model_snapshots/"
            "daily_candidate_model_signals_for_report_20260615_r1_"
        )
        for path in changed_paths
    )

    rows = backfill.backfill_historical_all_candidates_snapshots(
        repo_root=repo,
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        dates=["20260615"],
    )
    assert len(rows) == 1
    assert rows.iloc[0]["pipeline_commit_sha"] == merge_commit
    assert rows.iloc[0]["pipeline_commit_sha"] != branch_commit


def test_backfill_lock_collision_keeps_unknown_lock_and_manifest(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date="20260615",
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )
    manifest_before = manifest_path.read_bytes()
    lock_path = publisher.manifest_publication_lock_path(manifest_path)
    unknown_lock = b"unknown backfill owner\n"
    lock_path.write_bytes(unknown_lock)

    with pytest.raises(RuntimeError, match="publication lock already exists"):
        backfill.backfill_historical_all_candidates_snapshots(
            repo_root=repo,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=["20260615"],
        )

    assert manifest_path.read_bytes() == manifest_before
    assert lock_path.read_bytes() == unknown_lock
    assert not list(snapshot_dir.glob("all_candidates_20260615_r1_*.csv"))


def test_missing_exact_formal_snapshot_evidence_fails_without_orphan(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    report_date = "20260615"

    formal_path = snapshot_dir / f"daily_candidate_model_signals_for_report_{report_date}.csv"
    write_csv(formal_path, [formal_signal_row(report_date, "1111")])
    bad_row = snapshot_manifest_row(
        repo=repo,
        report_date=report_date,
        artifact_id="model_signals_for_report",
        revision="r1",
        snapshot_path=formal_path,
        snapshot_sha="0" * 64,
    )
    bad_row["revision_reason"] = publisher.LEGACY_REVISION_REASON
    write_csv(repo / backfill.ALL_CANDIDATES_SOURCE, [all_candidates_required_row(report_date, "1234")])
    write_csv(manifest_path, [bad_row])
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "invalid formal publication evidence")
    manifest_before = manifest_path.read_bytes()

    with pytest.raises(RuntimeError, match="paired formal snapshot SHA"):
        backfill.backfill_historical_all_candidates_snapshots(
            repo_root=repo,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=[report_date],
            generated_at="2026-06-30 10:00:00 Asia/Taipei",
        )

    assert manifest_path.read_bytes() == manifest_before
    assert not list(snapshot_dir.glob(f"all_candidates_{report_date}_r1_*.csv"))
    assert not list(snapshot_dir.glob(".*.tmp"))
    assert not publisher.manifest_publication_lock_path(manifest_path).exists()


def test_atomic_failure_after_snapshot_promotion_leaves_no_orphan(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    init_repo(repo)
    snapshot_dir = repo / "output" / "history" / "daily_model_snapshots"
    manifest_path = snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    publish_formal_revision(
        repo=repo,
        manifest_path=manifest_path,
        existing_manifest_rows=[],
        report_date="20260615",
        revision="r1",
        formal_stock_id="1111",
        candidate_stock_id="1234",
    )
    manifest_before = manifest_path.read_bytes()
    real_replace = publisher.os.replace

    def fail_manifest_replace(source: Path | str, target: Path | str) -> None:
        if Path(target) == manifest_path:
            raise OSError("simulated manifest promotion failure")
        real_replace(source, target)

    monkeypatch.setattr(publisher.os, "replace", fail_manifest_replace)

    with pytest.raises(OSError, match="simulated manifest promotion failure"):
        backfill.backfill_historical_all_candidates_snapshots(
            repo_root=repo,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=["20260615"],
            generated_at="2026-06-30 10:00:00 Asia/Taipei",
        )

    assert manifest_path.read_bytes() == manifest_before
    assert not list(snapshot_dir.glob("all_candidates_20260615_r1_*.csv"))
    assert not list(snapshot_dir.glob(".*.tmp"))
    assert not publisher.manifest_publication_lock_path(manifest_path).exists()
