from __future__ import annotations

import hashlib
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

import revenue_unreacted_range_forward_holdout as v1  # noqa: E402
import revenue_unreacted_range_forward_holdout_v2 as v2  # noqa: E402
import validate_revenue_unreacted_range_forward_holdout_v2 as v2_validator  # noqa: E402
from test_revenue_unreacted_range_forward_holdout import (  # noqa: E402
    _price_frame,
    _source_manifest,
    _source_row,
)


GENERATED_AT = "2026-08-28 12:00:00 Asia/Taipei"


def _v2_manifest() -> pd.DataFrame:
    manifest = _source_manifest()
    manifest.loc[0, "artifact_version"] = v2.SOURCE_PROJECTION_ARTIFACT_VERSION
    manifest.loc[0, "projection_version"] = v2.SOURCE_PROJECTION_ARTIFACT_VERSION
    manifest.loc[0, "projected_episode_row_count"] = v2.PROJECTED_EPISODE_ROW_COUNT
    manifest.loc[0, "projected_episode_semantic_sha256"] = (
        v2.PROJECTED_EPISODE_SEMANTIC_SHA256
    )
    manifest.loc[0, "candidate_status"] = "generated_pending_supersede_approval"
    return manifest


def _pre_start_inputs() -> tuple[pd.DataFrame, dict[str, pd.DataFrame], pd.DataFrame]:
    source = pd.DataFrame([_source_row(stock_id="1111", position="mid")])
    daily = {
        "1111": _price_frame(
            trigger_dates=(),
            position="mid",
            end_date="20260828",
        )
    }
    return source, daily, _v2_manifest()


def _bind_fixture_manifest(monkeypatch: pytest.MonkeyPatch, manifest: pd.DataFrame) -> None:
    canonical_sha = v1._canonical_frame_sha256(manifest)
    monkeypatch.setattr(v2, "SELECTED_V2_MANIFEST_CANONICAL_SHA256", canonical_sha)
    monkeypatch.setattr(
        v2_validator,
        "SELECTED_V2_MANIFEST_CANONICAL_SHA256",
        canonical_sha,
    )


def test_pre_start_capture_is_empty_research_only_and_independently_validated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)

    v1_defaults = (
        v1.ARTIFACT_ID,
        v1.ARTIFACT_VERSION,
        v1.HOLDOUT_START_DATE,
        v1.DATA_CONTRACT_SHA256,
        v1.ALLOW_PRE_START_EMPTY_CAPTURE,
    )
    frames = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )
    manifest, detail, summary, comparison, anomaly = frames

    assert detail.empty
    assert manifest.iloc[0]["artifact_id"] == v2.ARTIFACT_ID
    assert manifest.iloc[0]["artifact_version"] == v2.ARTIFACT_VERSION
    assert manifest.iloc[0]["holdout_start_date"] == "20260831"
    assert manifest.iloc[0]["observed_through_date"] == "20260828"
    assert manifest.iloc[0]["holdout_status"] == "preregistered_waiting_for_start"
    assert set(summary["holdout_status"]) == {"preregistered_waiting_for_start"}
    assert set(comparison["comparison_conclusion"]) == {
        "no_promotion_conclusion_preregistered_waiting_for_start"
    }
    assert set(anomaly["research_only"].astype(str).str.lower()) == {"true"}
    for frame in frames:
        for column in v1.FALSE_FLAG_COLUMNS:
            assert set(frame[column].astype(str).str.lower()) <= {"false"}

    errors = v2_validator.validate_frames(
        *frames,
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=source_manifest,
    )
    assert errors == []
    assert (
        v1.ARTIFACT_ID,
        v1.ARTIFACT_VERSION,
        v1.HOLDOUT_START_DATE,
        v1.DATA_CONTRACT_SHA256,
        v1.ALLOW_PRE_START_EMPTY_CAPTURE,
    ) == v1_defaults


def test_v2_writer_uses_separate_exact17_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    frames = v2.build_forward_holdout(
        source,
        daily,
        source_manifest=source_manifest,
        generated_at=GENERATED_AT,
    )

    paths = v2.write_forward_holdout(
        *frames,
        replay_source_detail=source,
        output_root=tmp_path,
    )

    assert len(paths) == 17
    assert {path.relative_to(tmp_path).as_posix() for path in paths.values()} == set(
        v2.FORWARD_HOLDOUT_V2_ALLOWED_ARTIFACT_PATHS
    )
    assert all("forward_holdout_v2" in path.name for path in paths.values())
    assert not list(tmp_path.rglob("revenue_unreacted_range_forward_holdout_manifest*"))


def test_selected_v2_manifest_binding_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source, daily, source_manifest = _pre_start_inputs()
    _bind_fixture_manifest(monkeypatch, source_manifest)
    source_manifest.loc[0, "projected_episode_semantic_sha256"] = "0" * 64

    with pytest.raises(RuntimeError, match="selected manifest drift"):
        v2.build_forward_holdout(
            source,
            daily,
            source_manifest=source_manifest,
            generated_at=GENERATED_AT,
        )


def test_v1_exact17_metadata_reproduces_authorized_bundle_digest() -> None:
    lines = [
        f"{path}|{size}|{digest}\n"
        for path, (size, digest) in sorted(v2.V1_EXACT17_PATH_EVIDENCE.items())
    ]
    assert len(lines) == 17
    assert hashlib.sha256("".join(lines).encode("utf-8")).hexdigest() == (
        v2.V1_EXACT17_BUNDLE_SHA256
    )


def test_v1_exact17_freeze_reports_the_drifting_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    relative = "output/latest/research_backtest/frozen.csv"
    payload = b"frozen\n"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    bundle = hashlib.sha256(
        f"{relative}|{len(payload)}|{digest}\n".encode("utf-8")
    ).hexdigest()
    monkeypatch.setattr(v2, "V1_EXACT17_PATH_EVIDENCE", {relative: (len(payload), digest)})
    monkeypatch.setattr(v2, "V1_EXACT17_BUNDLE_SHA256", bundle)
    assert v2.validate_v1_exact17_freeze(root=tmp_path) == bundle

    path.write_bytes(b"drift\n")
    with pytest.raises(RuntimeError, match="frozen.csv"):
        v2.validate_v1_exact17_freeze(root=tmp_path)


def test_v1_exact17_freeze_uses_git_blob_identity_for_clean_crlf_checkout(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Forward Holdout Test"],
        cwd=repo,
        check=True,
    )
    (repo / ".gitattributes").write_text("*.csv text eol=crlf\n", encoding="utf-8")
    relative = "output/latest/research_backtest/frozen.csv"
    path = repo / relative
    path.parent.mkdir(parents=True)
    path.write_bytes(b"header\nvalue\n")
    subprocess.run(
        ["git", "add", ".gitattributes", relative],
        cwd=repo,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "freeze fixture"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    path.unlink()
    subprocess.run(["git", "checkout", "--", relative], cwd=repo, check=True)

    blob = subprocess.run(
        ["git", "cat-file", "blob", f"HEAD:{relative}"],
        cwd=repo,
        check=True,
        capture_output=True,
    ).stdout
    assert b"\r\n" in path.read_bytes()
    assert b"\r\n" not in blob
    digest = hashlib.sha256(blob).hexdigest()
    bundle = hashlib.sha256(
        f"{relative}|{len(blob)}|{digest}\n".encode("utf-8")
    ).hexdigest()
    monkeypatch.setattr(v2, "V1_EXACT17_PATH_EVIDENCE", {relative: (len(blob), digest)})
    monkeypatch.setattr(v2, "V1_EXACT17_BUNDLE_SHA256", bundle)

    assert v2.validate_v1_exact17_freeze(root=repo) == bundle
    path.write_text("header\nchanged\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="working-tree drift"):
        v2.validate_v1_exact17_freeze(root=repo)
