from __future__ import annotations

import hashlib
import json
import subprocess

import pytest

from scripts import validate_recent_daily_price_repair_staged_paths as validator


def _json_bytes(payload: dict[str, object]) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _bundle_fixture(
    *,
    include_tpex: bool = True,
    market_bundle_path_override: str = "",
    source_base_sha: str = "",
) -> dict[str, object]:
    target_date = "20260811"
    release_id = "daily-source-20260811-run-1"
    source_base_sha = source_base_sha or "a" * 40
    bundle_root = f"output/history/daily_source_bundles/{target_date}/{release_id}"
    price_rows = [f"{target_date},2330,TWSE"]
    if include_tpex:
        price_rows.append(f"{target_date},6488,TPEx")
    price = ("date,stock_id,market\n" + "\n".join(price_rows) + "\n").encode()
    markdown = b"# official price fetch\n"
    fetch = _json_bytes(
        {
            "target_date": target_date,
            "saved_price_date": target_date,
            "is_target_date": True,
            "full_market_ok": True,
            "twse_rows": 1,
            "tpex_rows": 1,
            "total_rows": 2,
            "wrong_date_rows": 0,
            "latest_price_bytes": len(price),
            "latest_price_sha256": hashlib.sha256(price).hexdigest(),
            "fetch_markdown_bytes": len(markdown),
            "fetch_markdown_sha256": hashlib.sha256(markdown).hexdigest(),
        }
    )
    source_payloads = {
        f"data/daily_price/{target_date}.csv": price,
        f"data/daily_price/daily_price_{target_date}.csv": price,
        "output/latest/official_daily_price_latest.csv": price,
        "output/latest/official_price_fetch_latest.json": fetch,
        "output/latest/official_price_fetch_latest.md": markdown,
        "data/market_calendar/exceptional_non_trading_days.csv": b"date,reason\n",
    }
    index_payloads = dict(source_payloads)
    files: list[dict[str, object]] = []
    entries: list[tuple[str, tuple[str, ...]]] = []
    for index, (path, payload) in enumerate(source_payloads.items(), start=1):
        bundle_path = f"{bundle_root}/files/{index:02d}-{path.rsplit('/', 1)[-1]}"
        index_payloads[bundle_path] = payload
        entries.append(("A", (bundle_path,)))
        files.append(
            {
                "path": path,
                "bundle_path": bundle_path,
                "mode": "100644",
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    entries.extend(("M", (path,)) for path in sorted(validator.OFFICIAL_TRIPLET))
    market_status = {
        "market_status": "open_confirmed",
        "phase": "confirm",
        "market_session_date": target_date,
        "expected_main_price_date": target_date,
    }
    market_payload = _json_bytes(market_status)
    market_path = f"{bundle_root}/market_session_status.json"
    index_payloads[market_path] = market_payload
    entries.append(("A", (market_path,)))
    confirmation = {
        "path": f"data/daily_price/daily_price_{target_date}.csv",
        "price_bytes": len(price),
        "price_sha256": hashlib.sha256(price).hexdigest(),
        "fetch_status_path": "output/latest/official_price_fetch_latest.json",
        "fetch_status_bytes": len(fetch),
        "fetch_status_sha256": hashlib.sha256(fetch).hexdigest(),
        "fetch_markdown_path": "output/latest/official_price_fetch_latest.md",
        "fetch_markdown_bytes": len(markdown),
        "fetch_markdown_sha256": hashlib.sha256(markdown).hexdigest(),
        "twse_rows": 1,
        "tpex_rows": 1,
        "total_rows": 2,
        "wrong_date_rows": 0,
    }
    identity: dict[str, object] = {
        "schema_version": validator.BUNDLE_SCHEMA,
        "trading_date": target_date,
        "release_id": release_id,
        "source_base_sha": source_base_sha,
        "source_workflow_run_id": "1",
        "source_workflow_run_attempt": 1,
        "source_identities": ["test"],
        "files": files,
        "official_price_confirmation": confirmation,
        "market_session": {
            "bundle_path": market_bundle_path_override or market_path,
            "mode": "100644",
            "bytes": len(market_payload),
            "sha256": hashlib.sha256(market_payload).hexdigest(),
            "payload": market_status,
        },
    }
    source_bundle_sha = hashlib.sha256(_json_bytes(identity)).hexdigest()
    manifest = dict(identity)
    manifest["source_bundle_sha"] = source_bundle_sha
    manifest_payload = _json_bytes(manifest)
    manifest_path = f"{bundle_root}/manifest.json"
    index_payloads[manifest_path] = manifest_payload
    entries.append(("A", (manifest_path,)))
    state_path = f"{bundle_root}/state.json"
    index_payloads[state_path] = _json_bytes(
        {
            "schema_version": validator.STATE_SCHEMA,
            "phase": "bundle_ready",
            "trading_date": target_date,
            "release_id": release_id,
            "source_bundle_sha": source_bundle_sha,
            "source_base_sha": source_base_sha,
        }
    )
    entries.append(("A", (state_path,)))
    return {
        "target_date": target_date,
        "source_base_sha": source_base_sha,
        "manifest_path": manifest_path,
        "manifest_sha256": hashlib.sha256(manifest_payload).hexdigest(),
        "source_bundle_sha": source_bundle_sha,
        "entries": entries,
        "payloads": index_payloads,
        "modes": {path: "100644" for path in index_payloads},
    }


def _validate_fixture(fixture: dict[str, object]) -> list[str]:
    payloads = fixture["payloads"]
    modes = fixture["modes"]
    assert isinstance(payloads, dict)
    assert isinstance(modes, dict)
    return validator.validate_bundle_identity(
        fixture["entries"],
        target_date=str(fixture["target_date"]),
        source_base_sha=str(fixture["source_base_sha"]),
        observed_head_sha=str(fixture["source_base_sha"]),
        manifest_path=str(fixture["manifest_path"]),
        manifest_sha256=str(fixture["manifest_sha256"]),
        source_bundle_sha=str(fixture["source_bundle_sha"]),
        read_index_bytes=lambda path: payloads[path],
        read_index_mode=lambda path: modes[path],
    )


def test_exact_staged_bundle_identity_passes() -> None:
    assert _validate_fixture(_bundle_fixture()) == []


def test_staged_bundle_recomputes_full_market_rows_from_index_csv() -> None:
    errors = _validate_fixture(_bundle_fixture(include_tpex=False))
    assert any("full-market" in error for error in errors)
    assert any("row count mismatch" in error for error in errors)


def test_staged_bundle_rejects_manifest_market_object_path_drift() -> None:
    errors = _validate_fixture(
        _bundle_fixture(
            market_bundle_path_override="output/latest/market_session_status_latest.json"
        )
    )
    assert any("market payload mismatch" in error for error in errors)


@pytest.mark.parametrize(
    "mutation",
    ["bundle_bytes", "mode", "base_sha"],
)
def test_staged_bundle_identity_drift_fails_closed(mutation: str) -> None:
    fixture = _bundle_fixture()
    if mutation == "bundle_bytes":
        manifest = json.loads(
            fixture["payloads"][fixture["manifest_path"]].decode("utf-8")
        )
        fixture["payloads"][manifest["files"][0]["bundle_path"]] += b"tamper"
    elif mutation == "mode":
        fixture["modes"][fixture["manifest_path"]] = "120000"
    else:
        fixture["source_base_sha"] = "b" * 40
    assert _validate_fixture(fixture)


def test_git_index_allows_unchanged_price_member_with_stale_status_repair(
    tmp_path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(
        ["git", "init", "-q", "--initial-branch=main"], cwd=repo, check=True
    )
    subprocess.run(
        ["git", "config", "user.email", "repair@example.invalid"],
        cwd=repo,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Repair Test"], cwd=repo, check=True
    )
    initial_fixture = _bundle_fixture()
    payloads = initial_fixture["payloads"]
    assert isinstance(payloads, dict)
    baseline_paths = [
        path
        for path in payloads
        if not path.startswith("output/history/daily_source_bundles/")
    ]
    for relative in baseline_paths:
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if relative == "output/latest/official_price_fetch_latest.json":
            path.write_bytes(b'{"saved_price_date":"20260810"}\n')
        elif relative == "output/latest/official_price_fetch_latest.md":
            path.write_bytes(b"# stale status\n")
        else:
            path.write_bytes(payloads[relative])
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "baseline"], cwd=repo, check=True)
    source_base_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repo, text=True
    ).strip()
    fixture = _bundle_fixture(source_base_sha=source_base_sha)
    payloads = fixture["payloads"]
    manifest_path = fixture["manifest_path"]

    for relative, payload in payloads.items():
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    changed = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only"], cwd=repo, text=True
    ).splitlines()
    assert "output/latest/official_daily_price_latest.csv" not in changed
    assert "output/latest/official_price_fetch_latest.json" in changed
    assert "output/latest/official_price_fetch_latest.md" in changed

    monkeypatch.setattr(validator, "ROOT", repo)
    errors = validator.validate_bundle_identity(
        validator.staged_entries(),
        target_date=str(fixture["target_date"]),
        source_base_sha=str(fixture["source_base_sha"]),
        observed_head_sha=validator.repository_head_sha(),
        manifest_path=str(manifest_path),
        manifest_sha256=str(fixture["manifest_sha256"]),
        source_bundle_sha=str(fixture["source_bundle_sha"]),
        read_index_bytes=validator.read_staged_bytes,
        read_index_mode=validator.read_staged_mode,
    )
    assert errors == []


def test_date_scoped_source_bundle_paths_are_exactly_allowed() -> None:
    prefix = "output/history/daily_source_bundles/20260811/daily-source-20260811-run-1/"
    entries = [
        ("A", (prefix + "manifest.json",)),
        ("A", (prefix + "state.json",)),
        ("A", (prefix + "market_session_status.json",)),
        ("A", (prefix + "files/01-20260811.csv",)),
        ("A", (prefix + "files/02-daily_price_20260811.csv",)),
        ("A", (prefix + "files/03-official_daily_price_latest.csv",)),
        ("A", (prefix + "files/04-official_price_fetch_latest.json",)),
        ("A", (prefix + "files/05-official_price_fetch_latest.md",)),
        ("A", (prefix + "files/06-exceptional_non_trading_days.csv",)),
        ("M", ("output/latest/official_daily_price_latest.csv",)),
        ("M", ("output/latest/official_price_fetch_latest.json",)),
        ("M", ("output/latest/official_price_fetch_latest.md",)),
    ]
    assert validator.validate_entries(entries) == []


def test_source_bundle_path_escape_and_extra_payload_are_rejected() -> None:
    prefix = "output/history/daily_source_bundles/20260811/daily-source-20260811-run-1/"
    errors = validator.validate_entries(
        [
            ("A", (prefix + "files/05-extra.csv",)),
            ("A", (prefix + "../escaped.json",)),
        ]
    )
    assert len(errors) == 2


def test_exact_data_only_repair_paths_are_allowed() -> None:
    entries = [
        ("A", ("data/daily_price/daily_price_20260730.csv",)),
        ("A", ("data/daily_price/20260730.csv",)),
        ("M", ("data/stock_price_history/2330.csv",)),
        ("M", ("data/market_calendar/exceptional_non_trading_days.csv",)),
        ("M", ("output/latest/recent_daily_price_gap_repair_latest.json",)),
        ("M", ("output/latest/official_daily_price_latest.csv",)),
        ("M", ("output/latest/official_price_fetch_latest.json",)),
        ("M", ("output/latest/official_price_fetch_latest.md",)),
        ("M", ("output/latest/repair_daily_" + "price_range_latest.csv",)),
        ("M", ("output/latest/stock_price_history_manifest.md",)),
        ("M", ("docs/latest/stock_price_history_manifest.json",)),
    ]

    assert validator.validate_entries(entries) == []


def test_model_pdf_and_unexpected_paths_are_rejected() -> None:
    entries = [
        ("M", ("output/latest/all_candidates_latest.csv",)),
        ("A", ("output/latest/daily_market_summary_latest.pdf",)),
        ("M", ("scripts/repair_recent_daily_" + "price_gaps.py",)),
    ]

    errors = validator.validate_entries(entries)

    assert len(errors) == 3
    assert all("not allowed" in error for error in errors)


def test_deletion_rename_copy_and_empty_index_are_rejected() -> None:
    assert validator.validate_entries([]) == [
        "recent daily-price repair has no staged paths to validate"
    ]
    for entry in (
        ("D", ("data/daily_price/20260730.csv",)),
        ("R", ("data/daily_price/20260730.csv", "data/daily_price/20260731.csv")),
        ("C", ("data/stock_price_history/2330.csv", "data/stock_price_history/2331.csv")),
    ):
        errors = validator.validate_entries([entry])
        assert len(errors) == 1
        assert "must be add/modify only" in errors[0]
