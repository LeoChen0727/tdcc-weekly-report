from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from scripts import daily_source_recovery_bundle as bundle
from scripts import repair_recent_daily_price_gaps as recent


DATE = "20260811"
BASE_SHA_PLACEHOLDER = "0" * 40
TEST_RELEASE_ID = "src-test1"
CONFIRM_RELEASE_ID = "src-conf1"


def _git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def _price_payload(date_text: str = DATE) -> bytes:
    lines = ["date,stock_id,stock_name,market,open,high,low,close,volume,trading_value,source"]
    for index in range(1000):
        lines.append(
            f"{date_text},{1000 + index},Stock {index},TWSE,10,11,9,10.5,1000,10500,TWSE_TEST_SOURCE"
        )
    return ("\n".join(lines) + "\n").encode()


def _market(date_text: str = DATE) -> dict[str, object]:
    return {
        "assessment_date": date_text,
        "market_status": "open_confirmed",
        "phase": "confirm",
        "market_session_date": date_text,
        "expected_main_price_date": date_text,
        "should_run_daily_pipeline": True,
        "reason_code": "twse_tpex_target_date_confirmed",
        "generated_at": "2026-08-11T20:00:00+08:00",
    }


def _repo(tmp_path: Path) -> tuple[Path, str]:
    root = tmp_path / "repo"
    root.mkdir(parents=True)
    subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
    payload = _price_payload()
    for relative in bundle.required_source_paths(DATE):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload if "daily_price" in relative else b"date,reason\n")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "base"], cwd=root, check=True, capture_output=True)
    return root, _git(root, "rev-parse", "HEAD")


def _build_and_commit(root: Path, base_sha: str) -> tuple[dict[str, object], str]:
    result = bundle.build_bundle(
        root,
        trading_date=DATE,
        release_id=TEST_RELEASE_ID,
        source_base_sha=base_sha,
        run_id="123",
        run_attempt=1,
        market_session=_market(),
    )
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "bundle"], cwd=root, check=True, capture_output=True)
    return result, _git(root, "rev-parse", "HEAD")


def _commit_authority_surfaces(root: Path) -> str:
    (root / "output/latest/market_session_status_latest.json").write_bytes(
        bundle.json_bytes(_market())
    )
    (root / "output/latest/data_freshness_latest.csv").write_text(
        "market_session_status,market_session_date,expected_main_price_date,main_price_date,"
        "report_ready,warrant_ready,daily_pdf_ready\n"
        f"open_confirmed,{DATE},{DATE},{DATE},True,True,True\n",
        encoding="utf-8",
    )
    (root / "output/latest/data_freshness_latest.md").write_text(
        "# Daily authority test release\n",
        encoding="utf-8",
    )
    (root / "output/latest/daily_authority_release_latest.json").write_bytes(
        bundle.json_bytes({"release_id": "test-authority-release"})
    )
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        ["git", "commit", "-m", "authority release"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    return _git(root, "rev-parse", "HEAD")


def test_recent_repair_includes_current_trading_day_and_handles_weekend() -> None:
    target, dates = recent.expected_recent_trading_dates(DATE, 7, set())
    assert target == DATE
    assert DATE in dates

    weekend_target, weekend_dates = recent.expected_recent_trading_dates("20260809", 7, set())
    assert weekend_target == "20260807"
    assert "20260809" not in weekend_dates


def test_bundle_build_git_verify_and_materialize_exact_sources(tmp_path: Path) -> None:
    root, base_sha = _repo(tmp_path)
    official_latest = root / "output/latest/official_daily_price_latest.csv"
    official_latest.write_bytes(b"stale mutable latest\n")
    result, commit_sha = _build_and_commit(root, base_sha)
    canonical = root / f"data/daily_price/daily_price_{DATE}.csv"
    expected = canonical.read_bytes()
    canonical.write_text("wrong current data\n", encoding="utf-8")

    manifest = bundle.verify_bundle_from_git(
        root,
        source_commit_sha=commit_sha,
        manifest_path=result["manifest_path"],
        manifest_sha256=result["manifest_sha256"],
        source_bundle_sha=result["manifest"]["source_bundle_sha"],
        trading_date=DATE,
        materialize=True,
        state_output=root / "state-copy.json",
    )

    assert canonical.read_bytes() == expected
    assert official_latest.read_bytes() == expected
    assert json.loads(
        (root / "output/latest/market_session_status_latest.json").read_text(encoding="utf-8")
    )["market_status"] == "open_confirmed"
    assert manifest["trading_date"] == DATE
    assert json.loads((root / "state-copy.json").read_text())["phase"] == "bundle_ready"


def test_bundle_market_confirmation_reads_date_locked_official_projection(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, base_sha = _repo(tmp_path)
    official_latest = root / "output/latest/official_daily_price_latest.csv"
    official_latest.write_bytes(b"stale mutable latest\n")

    def fake_refresh(observed_root: Path, *, phase: str, write_files: bool) -> dict[str, object]:
        assert observed_root == root
        assert phase == "confirm"
        assert write_files is False
        assert official_latest.read_bytes() == _price_payload()
        return _market()

    monkeypatch.setattr(bundle.market_session_calendar, "refresh_market_session_status", fake_refresh)
    result = bundle.build_bundle(
        root,
        trading_date=DATE,
        release_id=CONFIRM_RELEASE_ID,
        source_base_sha=base_sha,
        run_id="124",
        run_attempt=1,
    )

    assert result["manifest"]["market_session"]["payload"]["phase"] == "confirm"
    assert official_latest.read_bytes() == _price_payload()


@pytest.mark.parametrize("failure", ["missing", "wrong_date", "row_drift"])
def test_bundle_build_rejects_missing_or_non_authoritative_price_sources(
    tmp_path: Path, failure: str
) -> None:
    root, base_sha = _repo(tmp_path)
    target = root / f"data/daily_price/daily_price_{DATE}.csv"
    if failure == "missing":
        target.unlink()
    elif failure == "wrong_date":
        target.write_bytes(_price_payload("20260810"))
    else:
        target.write_bytes(target.read_bytes() + b"20260811,9999,Drift,TWSE,1,1,1,1,1,1,TWSE_TEST_SOURCE\n")

    with pytest.raises(bundle.DailySourceRecoveryError):
        bundle.build_bundle(
            root,
            trading_date=DATE,
            release_id=TEST_RELEASE_ID,
            source_base_sha=base_sha,
            run_id="123",
            run_attempt=1,
            market_session=_market(),
        )


def test_bundle_build_failure_rolls_back_without_partial_final_root(tmp_path: Path) -> None:
    root, base_sha = _repo(tmp_path)
    final_root = root / bundle.bundle_root_path(DATE, TEST_RELEASE_ID)
    official_latest = root / "output/latest/official_daily_price_latest.csv"
    previous_official = b"previous official latest\n"
    official_latest.write_bytes(previous_official)

    with pytest.raises(bundle.DailySourceRecoveryError, match="injected"):
        bundle.build_bundle(
            root,
            trading_date=DATE,
            release_id=TEST_RELEASE_ID,
            source_base_sha=base_sha,
            run_id="123",
            run_attempt=1,
            market_session=_market(),
            fail_after_official_publish=True,
        )

    assert not final_root.exists()
    assert official_latest.read_bytes() == previous_official
    assert not list(final_root.parent.glob(".prepare-*"))


def test_git_verifier_rejects_manifest_hash_content_path_date_and_mode_drift(tmp_path: Path) -> None:
    root, base_sha = _repo(tmp_path)
    result, commit_sha = _build_and_commit(root, base_sha)
    common = {
        "root": root,
        "source_commit_sha": commit_sha,
        "manifest_path": result["manifest_path"],
        "manifest_sha256": result["manifest_sha256"],
        "source_bundle_sha": result["manifest"]["source_bundle_sha"],
        "trading_date": DATE,
    }
    for override in (
        {"manifest_sha256": "f" * 64},
        {"source_bundle_sha": "e" * 64},
        {"manifest_path": "../manifest.json"},
        {"trading_date": "20260810"},
        {"source_commit_sha": BASE_SHA_PLACEHOLDER},
    ):
        with pytest.raises(bundle.DailySourceRecoveryError):
            bundle.verify_bundle_from_git(**(common | override))


def test_git_verifier_rejects_payload_mode_and_state_drift(tmp_path: Path) -> None:
    payload_root, payload_base = _repo(tmp_path / "payload")
    payload_result, payload_commit = _build_and_commit(payload_root, payload_base)
    payload_path = payload_root / payload_result["manifest"]["files"][0]["bundle_path"]
    payload_path.write_bytes(payload_path.read_bytes() + b"drift\n")
    subprocess.run(["git", "add", payload_path.as_posix()], cwd=payload_root, check=True)
    subprocess.run(["git", "commit", "-m", "payload drift"], cwd=payload_root, check=True, capture_output=True)
    with pytest.raises(bundle.DailySourceRecoveryError, match="payload identity"):
        bundle.verify_bundle_from_git(
            payload_root,
            source_commit_sha=_git(payload_root, "rev-parse", "HEAD"),
            manifest_path=payload_result["manifest_path"],
            manifest_sha256=payload_result["manifest_sha256"],
            source_bundle_sha=payload_result["manifest"]["source_bundle_sha"],
            trading_date=DATE,
        )

    mode_root, mode_base = _repo(tmp_path / "mode")
    mode_result, _ = _build_and_commit(mode_root, mode_base)
    mode_path = mode_result["manifest"]["files"][0]["bundle_path"]
    subprocess.run(["git", "update-index", "--chmod=+x", mode_path], cwd=mode_root, check=True)
    subprocess.run(["git", "commit", "-m", "mode drift"], cwd=mode_root, check=True, capture_output=True)
    with pytest.raises(bundle.DailySourceRecoveryError, match="unexpected Git mode"):
        bundle.verify_bundle_from_git(
            mode_root,
            source_commit_sha=_git(mode_root, "rev-parse", "HEAD"),
            manifest_path=mode_result["manifest_path"],
            manifest_sha256=mode_result["manifest_sha256"],
            source_bundle_sha=mode_result["manifest"]["source_bundle_sha"],
            trading_date=DATE,
        )

    state_root, state_base = _repo(tmp_path / "state")
    state_result, _ = _build_and_commit(state_root, state_base)
    state_path = state_root / bundle.bundle_root_path(
        DATE, state_result["manifest"]["release_id"]
    ) / "state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["phase"] = "failed"
    state["error"] = "forged"
    state_path.write_bytes(bundle.json_bytes(state))
    subprocess.run(["git", "add", state_path.as_posix()], cwd=state_root, check=True)
    subprocess.run(["git", "commit", "-m", "state drift"], cwd=state_root, check=True, capture_output=True)
    with pytest.raises(bundle.DailySourceRecoveryError, match="state identity"):
        bundle.verify_bundle_from_git(
            state_root,
            source_commit_sha=_git(state_root, "rev-parse", "HEAD"),
            manifest_path=state_result["manifest_path"],
            manifest_sha256=state_result["manifest_sha256"],
            source_bundle_sha=state_result["manifest"]["source_bundle_sha"],
            trading_date=DATE,
        )


def test_git_verifier_rejects_source_commit_outside_current_head_ancestry(
    tmp_path: Path,
) -> None:
    root, base_sha = _repo(tmp_path)
    result, source_commit = _build_and_commit(root, base_sha)
    subprocess.run(["git", "checkout", "--detach", base_sha], cwd=root, check=True, capture_output=True)
    (root / "unrelated.txt").write_text("diverged\n", encoding="utf-8")
    subprocess.run(["git", "add", "unrelated.txt"], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "diverged head"], cwd=root, check=True, capture_output=True)

    with pytest.raises(bundle.DailySourceRecoveryError, match="not an ancestor"):
        bundle.verify_bundle_from_git(
            root,
            source_commit_sha=source_commit,
            manifest_path=result["manifest_path"],
            manifest_sha256=result["manifest_sha256"],
            source_bundle_sha=result["manifest"]["source_bundle_sha"],
            trading_date=DATE,
        )


def test_state_machine_failure_injection_chain_is_monotonic_and_exact() -> None:
    state = bundle.new_state(
        trading_date=DATE,
        release_id=TEST_RELEASE_ID,
        source_bundle_sha="a" * 64,
        source_base_sha="b" * 40,
        run_id="123",
        run_attempt=1,
        phase="source_absent",
    )
    state = bundle.transition_state(state, "repairing")
    state = bundle.transition_state(state, "bundle_ready")
    state = bundle.transition_state(state, "bundle_committed", source_bundle_commit_sha="c" * 40)
    state = bundle.transition_state(
        state,
        "resume_dispatched",
        resume_workflow_path=bundle.WORKFLOW_PATH,
        resume_baseline_run_id="100",
        resume_dispatch_started_at="2026-08-11T20:30:00Z",
        resume_expected_head_sha="d" * 40,
        resume_expected_display_title="Daily Full Pipeline | recovery=test-token",
        resume_reservation_path=f"output/history/daily_source_recovery_reservations/{DATE}.json",
        resume_reservation_sha256="e" * 64,
    )
    state = bundle.transition_state(
        state,
        "resume_running",
        resume_workflow_run_id="101",
        resume_workflow_run_attempt="1",
        resume_workflow_run_url="https://github.com/example/repo/actions/runs/101",
    )
    state = bundle.transition_state(state, "resume_succeeded", resume_conclusion="success")
    state = bundle.transition_state(state, "confirm_source_gate")
    assert state["phase"] == "confirm_source_gate"

    with pytest.raises(bundle.DailySourceRecoveryError, match="forbidden"):
        bundle.transition_state(state, "repairing")


def test_completed_authority_skips_resume_with_exact_release_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, base_sha = _repo(tmp_path)
    authority_release_sha = _commit_authority_surfaces(root)
    bundle_result, head_sha = _build_and_commit(root, authority_release_sha)
    market_path = root / "output/latest/market_session_status_latest.json"
    freshness_path = root / "output/latest/data_freshness_latest.csv"
    release_id = "daily-authority-20260811-existing"
    monkeypatch.setattr(
        bundle.daily_authority_release,
        "validate_authority_release",
        lambda observed_root: {
            "release_id": release_id,
            "generation_id": release_id,
            "base_commit_sha": base_sha,
        },
    )

    bundle_identity = {
        "source_commit_sha": head_sha,
        "manifest_path": bundle_result["manifest_path"],
        "manifest_sha256": bundle_result["manifest_sha256"],
        "source_bundle_sha": bundle_result["manifest"]["source_bundle_sha"],
    }
    identity = bundle.existing_authority_completion(root, DATE, **bundle_identity)

    assert identity == {
        "release_id": release_id,
        "generation_id": release_id,
        "commit_sha": authority_release_sha,
    }
    state = bundle.new_state(
        trading_date=DATE,
        release_id=TEST_RELEASE_ID,
        source_bundle_sha="a" * 64,
        source_base_sha=head_sha,
        run_id="123",
        run_attempt=1,
        phase="bundle_committed",
    )
    state = bundle.transition_state(
        state,
        "resume_not_required",
        existing_authority_release_id=identity["release_id"],
        existing_authority_generation_id=identity["generation_id"],
        existing_authority_commit_sha=identity["commit_sha"],
    )
    assert bundle.transition_state(state, "confirm_source_gate")["phase"] == "confirm_source_gate"

    freshness_path.write_text(
        freshness_path.read_text(encoding="utf-8").replace(",True,True,True", ",False,False,False"),
        encoding="utf-8",
    )
    assert bundle.existing_authority_completion(root, DATE, **bundle_identity) is None

    freshness_path.write_text(
        "market_session_status,market_session_date,expected_main_price_date,main_price_date,"
        "report_ready,warrant_ready,daily_pdf_ready\n"
        f"open_confirmed,{DATE},{DATE},{DATE},True,True,True\n",
        encoding="utf-8",
    )
    canonical_path = root / bundle_result["manifest"]["files"][0]["path"]
    canonical_path.write_bytes(canonical_path.read_bytes() + b"drift\n")
    assert bundle.existing_authority_completion(root, DATE, **bundle_identity) is None


@pytest.mark.parametrize("revision_kind", ["price", "calendar"])
def test_completed_authority_rejects_same_day_source_revision(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, revision_kind: str
) -> None:
    root, authority_base_sha = _repo(tmp_path)
    _commit_authority_surfaces(root)
    if revision_kind == "price":
        revised_price = _price_payload().replace(b"TWSE_TEST_SOURCE", b"TWSE_TEST_SOURCE_REV2")
        for relative in bundle.required_source_paths(DATE):
            if "daily_price" in relative:
                (root / relative).write_bytes(revised_price)
    else:
        (root / "data/market_calendar/exceptional_non_trading_days.csv").write_bytes(
            b"date,reason\n20260811,test revision\n"
        )
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        ["git", "commit", "-m", "source revision"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    revision_sha = _git(root, "rev-parse", "HEAD")
    bundle_result, source_commit_sha = _build_and_commit(root, revision_sha)
    (root / "output/latest/market_session_status_latest.json").write_bytes(
        bundle.json_bytes(_market())
    )
    (root / "output/latest/data_freshness_latest.csv").write_text(
        "market_session_status,market_session_date,expected_main_price_date,main_price_date,"
        "report_ready,warrant_ready,daily_pdf_ready\n"
        f"open_confirmed,{DATE},{DATE},{DATE},True,True,True\n",
        encoding="utf-8",
    )
    release_id = "daily-authority-20260811-stale-source"
    monkeypatch.setattr(
        bundle.daily_authority_release,
        "validate_authority_release",
        lambda observed_root: {
            "release_id": release_id,
            "generation_id": release_id,
            "base_commit_sha": authority_base_sha,
        },
    )

    assert bundle.existing_authority_completion(
        root,
        DATE,
        source_commit_sha=source_commit_sha,
        manifest_path=bundle_result["manifest_path"],
        manifest_sha256=bundle_result["manifest_sha256"],
        source_bundle_sha=bundle_result["manifest"]["source_bundle_sha"],
    ) is None


def test_materialization_rejects_stale_market_state_and_rolls_back_partial_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, base_sha = _repo(tmp_path)
    result, source_commit = _build_and_commit(root, base_sha)
    common = {
        "root": root,
        "source_commit_sha": source_commit,
        "manifest_path": result["manifest_path"],
        "manifest_sha256": result["manifest_sha256"],
        "source_bundle_sha": result["manifest"]["source_bundle_sha"],
        "trading_date": DATE,
        "materialize": True,
    }
    market_path = root / "output/latest/market_session_status_latest.json"
    newer_market = _market() | {
        "assessment_date": "20260812",
        "market_session_date": "20260812",
        "expected_main_price_date": "20260812",
        "generated_at": "2026-08-12T20:00:00+08:00",
    }
    market_path.write_bytes(bundle.json_bytes(newer_market))
    with pytest.raises(bundle.DailySourceRecoveryError, match="not monotonic"):
        bundle.verify_bundle_from_git(**common)
    assert market_path.read_bytes() == bundle.json_bytes(newer_market)

    market_path.write_bytes(bundle.json_bytes(_market()))
    targets = [root / entry["path"] for entry in result["manifest"]["files"]]
    for index, target in enumerate(targets):
        target.write_bytes(f"before-{index}\n".encode("ascii"))
    before = {target: target.read_bytes() for target in [*targets, market_path]}
    original_write = bundle._write_atomic
    calls = 0

    def fail_second_write(path: Path, payload: bytes) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected materialization write failure")
        original_write(path, payload)

    monkeypatch.setattr(bundle, "_write_atomic", fail_second_write)
    with pytest.raises(OSError, match="injected materialization"):
        bundle.verify_bundle_from_git(**common)
    assert {target: target.read_bytes() for target in before} == before


def test_uncertain_dispatch_cannot_be_retried_or_rebound() -> None:
    state = bundle.new_state(
        trading_date=DATE,
        release_id=TEST_RELEASE_ID,
        source_bundle_sha="a" * 64,
        source_base_sha="b" * 40,
        run_id="123",
        run_attempt=1,
        phase="bundle_committed",
    )
    failed = bundle.transition_state(state, "failed", error="dispatch correlation uncertain")
    with pytest.raises(bundle.DailySourceRecoveryError, match="forbidden"):
        bundle.transition_state(failed, "resume_dispatched")


def test_run_correlation_requires_unique_title_head_attempt_baseline_and_window() -> None:
    expected = {
        "databaseId": 201,
        "attempt": 1,
        "createdAt": "2026-08-11T12:30:05Z",
        "event": "workflow_dispatch",
        "workflowName": "Daily Full Pipeline",
        "headSha": "d" * 40,
        "displayTitle": "Daily Full Pipeline | recovery=test-token",
        "url": "https://github.com/example/repo/actions/runs/201",
    }
    noise = [
        expected | {"databaseId": 199},
        expected | {"databaseId": 202, "attempt": 2},
        expected | {"databaseId": 203, "headSha": "e" * 40},
        expected | {"databaseId": 204, "displayTitle": "Daily Full Pipeline | recovery=other"},
        expected | {"databaseId": 205, "createdAt": "2026-08-11T13:00:00Z"},
    ]
    observed = bundle.select_correlated_run(
        [*noise, expected],
        baseline_run_id=200,
        dispatch_started_at="2026-08-11T12:30:00Z",
        expected_head_sha="d" * 40,
        expected_display_title="Daily Full Pipeline | recovery=test-token",
    )
    assert observed == expected

    with pytest.raises(bundle.DailySourceRecoveryError, match="multiple"):
        bundle.select_correlated_run(
            [expected, expected | {"databaseId": 206}],
            baseline_run_id=200,
            dispatch_started_at="2026-08-11T12:30:00Z",
            expected_head_sha="d" * 40,
            expected_display_title="Daily Full Pipeline | recovery=test-token",
        )

    stable_title = f"Daily Full Pipeline | recovery=daily-source-{DATE}"
    bundle.reject_existing_recovery_run([], expected_display_title=stable_title)
    with pytest.raises(bundle.DailySourceRecoveryError, match="already exists"):
        bundle.reject_existing_recovery_run(
            [expected | {"displayTitle": stable_title}],
            expected_display_title=stable_title,
        )


def test_dispatch_reservation_is_date_scoped_immutable_and_bundle_bound(tmp_path: Path) -> None:
    root, base_sha = _repo(tmp_path)
    result, source_commit = _build_and_commit(root, base_sha)
    expected_title = f"Daily Full Pipeline | recovery=daily-source-{DATE}"
    reserved = bundle.create_dispatch_reservation(
        root,
        trading_date=DATE,
        source_commit_sha=source_commit,
        manifest_path=result["manifest_path"],
        manifest_sha256=result["manifest_sha256"],
        source_bundle_sha=result["manifest"]["source_bundle_sha"],
        baseline_run_id=200,
        dispatch_started_at="2026-08-11T12:30:00Z",
        expected_display_title=expected_title,
    )
    reservation_path = root / reserved["path"]
    assert reserved["path"] == f"output/history/daily_source_recovery_reservations/{DATE}.json"
    assert bundle.sha256_bytes(reservation_path.read_bytes()) == reserved["sha256"]
    assert reserved["payload"]["source_bundle_sha"] == result["manifest"]["source_bundle_sha"]

    with pytest.raises(bundle.DailySourceRecoveryError, match="already exists"):
        bundle.create_dispatch_reservation(
            root,
            trading_date=DATE,
            source_commit_sha=source_commit,
            manifest_path=result["manifest_path"],
            manifest_sha256=result["manifest_sha256"],
            source_bundle_sha=result["manifest"]["source_bundle_sha"],
            baseline_run_id=200,
            dispatch_started_at="2026-08-11T12:30:00Z",
            expected_display_title=expected_title,
        )

    subprocess.run(["git", "add", reserved["path"]], cwd=root, check=True)
    subprocess.run(
        ["git", "commit", "-m", "reserve recovery"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    reservation_head = _git(root, "rev-parse", "HEAD")
    verified = bundle.verify_dispatch_reservation(
        root,
        trading_date=DATE,
        reservation_path=reserved["path"],
        reservation_sha256=reserved["sha256"],
        expected_head_sha=reservation_head,
        source_commit_sha=source_commit,
        manifest_path=result["manifest_path"],
        manifest_sha256=result["manifest_sha256"],
        source_bundle_sha=result["manifest"]["source_bundle_sha"],
        correlation_id=f"daily-source-{DATE}",
    )
    assert verified == reserved["payload"]
    with pytest.raises(bundle.DailySourceRecoveryError, match="SHA-256 mismatch"):
        bundle.verify_dispatch_reservation(
            root,
            trading_date=DATE,
            reservation_path=reserved["path"],
            reservation_sha256="f" * 64,
            expected_head_sha=reservation_head,
            source_commit_sha=source_commit,
            manifest_path=result["manifest_path"],
            manifest_sha256=result["manifest_sha256"],
            source_bundle_sha=result["manifest"]["source_bundle_sha"],
            correlation_id=f"daily-source-{DATE}",
        )

    with pytest.raises(bundle.DailySourceRecoveryError, match="title mismatch"):
        bundle.create_dispatch_reservation(
            root,
            trading_date=DATE,
            source_commit_sha=source_commit,
            manifest_path=result["manifest_path"],
            manifest_sha256=result["manifest_sha256"],
            source_bundle_sha=result["manifest"]["source_bundle_sha"],
            baseline_run_id=200,
            dispatch_started_at="2026-08-11T12:30:00Z",
            expected_display_title="Daily Full Pipeline | recovery=other-date",
        )
