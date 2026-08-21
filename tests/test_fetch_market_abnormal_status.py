from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo

import pandas as pd
import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_weekly_surge_multifactor_candidates as surge_multifactor
import build_weekly_surge_strict_parameter_candidates as surge_strict
from scripts import fetch_market_abnormal_status as market_abnormal


TARGET_DATE = "20260821"
FIXED_NOW = datetime(2026, 8, 21, 13, 45, 12, tzinfo=ZoneInfo("Asia/Taipei"))


class FakeResponse:
    def __init__(
        self,
        payload: bytes,
        *,
        status_code: int = 200,
        content_type: str = "application/json; charset=utf-8",
        retry_after: str | None = None,
    ) -> None:
        self.content = payload
        self.status_code = status_code
        self.headers = {"Content-Type": content_type}
        if retry_after is not None:
            self.headers["Retry-After"] = retry_after

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"status={self.status_code}")


def valid_source_rows() -> dict[str, list[dict[str, str]]]:
    return {
        "twse_disposition": [
            {
                "Date": "1150821",
                "Code": "2330",
                "Name": "台積電",
                "NumberOfAnnouncement": "1",
                "ReasonsOfDisposition": "測試處置",
                "DispositionPeriod": "115/08/21~115/08/31",
                "DispositionMeasures": "第一次處置",
                "Detail": "測試處置詳情",
            }
        ],
        "twse_attention": [
            {
                "Date": "1150821",
                "Code": "2317",
                "Name": "鴻海",
                "NumberOfAnnouncement": "1",
                "TradingInfoForAttention": "測試注意",
            }
        ],
        "twse_attention_note": [
            {
                "Code": "2454",
                "Name": "聯發科",
                "RecentlyMetAttentionSecuritiesCriteria": "115年8月20日至115年8月21日連續二次",
            }
        ],
        "tpex_disposition": [
            {
                "Date": "1150821",
                "SecuritiesCompanyCode": "5483",
                "CompanyName": "中美晶",
                "DispositionPeriod": "1150821~1150831",
                "DispositionReasons": "測試處置",
                "DisposalCondition": "每五分鐘撮合",
            }
        ],
        "tpex_attention": [
            {
                "Date": "1150821",
                "SecuritiesCompanyCode": "6488",
                "CompanyName": "環球晶",
                "TradingInformation": "測試注意",
            }
        ],
        "tpex_attention_note": [
            {
                "Date": "20260821",
                "SecuritiesCompanyCode": "8299",
                "CompanyName": "群聯",
                "AccumulationSituation": "連續二次",
            }
        ],
        "tpex_trading_mode": [
            {
                "Date": "1150821",
                "SecuritiesCompanyCode": "4747",
                "CompanyName": "強生",
                "AlteredTrading": "Ｙ",
                "PeriodicTrading": "",
                "ManagedStock": "",
                "MatchingFrequency": "",
                "SuspensionOfTrading": "Ｙ",
            }
        ],
    }


def source_payloads(
    rows: dict[str, list[dict[str, str]]] | None = None,
) -> dict[str, bytes]:
    rows = rows or valid_source_rows()
    return {
        name: json.dumps(value, ensure_ascii=False).encode("utf-8")
        for name, value in rows.items()
    }


def install_live_http(
    monkeypatch: pytest.MonkeyPatch,
    payloads: dict[str, bytes],
    *,
    override_name: str | None = None,
    override_events: list[FakeResponse | Exception] | None = None,
) -> list[str]:
    url_to_name = {url: name for name, url in market_abnormal.SOURCE_URLS.items()}
    calls: list[str] = []
    event_index = 0

    def fake_get(url: str, timeout: int) -> FakeResponse:
        nonlocal event_index
        assert timeout == 30
        name = url_to_name[url]
        calls.append(name)
        if name == override_name and override_events:
            event = override_events[min(event_index, len(override_events) - 1)]
            event_index += 1
            if isinstance(event, Exception):
                raise event
            return event
        return FakeResponse(payloads[name])

    monkeypatch.setattr(market_abnormal.requests, "get", fake_get)
    return calls


def configure_current_day(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(market_abnormal, "now_taipei", lambda: FIXED_NOW)
    monkeypatch.setattr(market_abnormal.time, "sleep", lambda _seconds: None)


def assert_no_latest_or_history(tmp_path: Path) -> None:
    for relative in (
        "output/latest/market_abnormal_status_latest.csv",
        "output/latest/market_abnormal_status_latest.md",
        "docs/latest/market_abnormal_status_latest.csv",
        "docs/latest/market_abnormal_status_latest.md",
        "output/history/market_abnormal_status/market_abnormal_status_history.csv",
    ):
        assert not (tmp_path / relative).exists()


def test_live_current_fetch_publishes_complete_bundle_and_target_lineage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    calls = install_live_http(monkeypatch, source_payloads())

    result = market_abnormal.run(TARGET_DATE)

    assert calls == list(market_abnormal.SOURCE_URLS)
    assert result["access_mode"] == "live_current_endpoints"
    manifest_path = tmp_path / result["manifest_path"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["target_date"] == TARGET_DATE
    assert manifest["fetch_date"] == TARGET_DATE
    assert manifest["fetched_at"] == "2026-08-21 13:45:12 Asia/Taipei"
    assert set(manifest["sources"]) == set(market_abnormal.SOURCE_URLS)
    assert not list(manifest_path.parent.parent.glob(f".{TARGET_DATE}-*"))
    for name, entry in manifest["sources"].items():
        raw_path = tmp_path / entry["path"]
        assert raw_path.is_file()
        assert hashlib.sha256(raw_path.read_bytes()).hexdigest() == entry["raw_sha256"]
        assert entry["row_count"] == 1
        assert set(market_abnormal.SOURCE_REQUIRED_COLUMNS[name]).issubset(
            entry["columns"]
        )

    latest = pd.read_csv(
        tmp_path / market_abnormal.OUT_CSV, dtype=str, keep_default_na=False
    )
    history = pd.read_csv(
        tmp_path / market_abnormal.HISTORY_CSV, dtype=str, keep_default_na=False
    )
    assert set(latest["target_date"]) == {TARGET_DATE}
    assert set(latest["fetch_date"]) == {TARGET_DATE}
    assert set(latest["fetched_at"]) == {"2026-08-21 13:45:12 Asia/Taipei"}
    assert latest["announcement_date"].le(TARGET_DATE).all()
    assert history.duplicated(["target_date", "stock_id"]).sum() == 0
    assert (tmp_path / market_abnormal.OUT_CSV).read_bytes() == (
        tmp_path / market_abnormal.DOCS_CSV
    ).read_bytes()


def test_twse_legal_empty_sentinel_preserves_schema_without_false_failure() -> None:
    sentinel = pd.DataFrame(
        [
            {
                "Date": "",
                "Code": "",
                "Name": "",
                "NumberOfAnnouncement": "0",
                "TradingInfoForAttention": "",
            }
        ]
    )

    market_abnormal.validate_source_frame(
        "twse_attention", sentinel, target_date=TARGET_DATE
    )


def test_legal_noncandidate_codes_are_validated_but_never_truncated_into_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    rows = valid_source_rows()
    rows["twse_disposition"].append(
        {
            "Date": "1150817",
            "Code": "911608",
            "Name": "越南控-DR",
            "NumberOfAnnouncement": "1",
            "ReasonsOfDisposition": "測試合法TDR",
            "DispositionPeriod": "115/08/17~115/08/31",
            "DispositionMeasures": "第一次處置",
            "Detail": "測試合法六碼證券代碼",
        }
    )
    rows["twse_disposition"].append(
        {
            "Date": "1150819",
            "Code": "72381U",
            "Name": "測試權證",
            "NumberOfAnnouncement": "1",
            "ReasonsOfDisposition": "測試合法權證代碼",
            "DispositionPeriod": "115/08/19~115/08/31",
            "DispositionMeasures": "第一次處置",
            "Detail": "測試Git歷史實證英數代碼",
        }
    )
    rows["twse_disposition"].append(
        {
            "Date": "1150818",
            "Code": "00632R",
            "Name": "元大台灣50反1",
            "NumberOfAnnouncement": "1",
            "ReasonsOfDisposition": "測試合法ETF代碼",
            "DispositionPeriod": "115/08/18~115/08/31",
            "DispositionMeasures": "第一次處置",
            "Detail": "測試合法英數證券代碼",
        }
    )
    install_live_http(monkeypatch, source_payloads(rows))

    market_abnormal.run(TARGET_DATE)

    latest = pd.read_csv(
        tmp_path / market_abnormal.OUT_CSV, dtype=str, keep_default_na=False
    )
    assert "9116" not in set(latest["stock_id"])
    assert "911608" not in set(latest["stock_id"])
    assert "0063" not in set(latest["stock_id"])
    assert "00632R" not in set(latest["stock_id"])
    assert "7238" not in set(latest["stock_id"])
    assert "72381U" not in set(latest["stock_id"])
    raw = json.loads(
        (
            tmp_path
            / market_abnormal.source_path_for(TARGET_DATE, "twse_disposition")
        ).read_text(encoding="utf-8")
    )
    assert any(row["Code"] == "911608" for row in raw)
    assert any(row["Code"] == "00632R" for row in raw)
    assert any(row["Code"] == "72381U" for row in raw)


def test_exact_target_bundle_replay_never_calls_live_and_deduplicates_history(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    install_live_http(monkeypatch, source_payloads())
    market_abnormal.run(TARGET_DATE)

    monkeypatch.setattr(
        market_abnormal.requests,
        "get",
        lambda *_args, **_kwargs: pytest.fail("replay must not call live endpoints"),
    )
    result = market_abnormal.run(TARGET_DATE)

    assert result["access_mode"] == "exact_target_bundle_replay"
    history = pd.read_csv(
        tmp_path / market_abnormal.HISTORY_CSV, dtype=str, keep_default_na=False
    )
    assert history.duplicated(["target_date", "stock_id"]).sum() == 0
    assert len(history) == result["latest_rows"]


@pytest.mark.parametrize(
    "failure_mode",
    [
        "timeout",
        "http",
        "content_type",
        "json",
        "empty",
        "schema",
        "punctuation_code",
        "letters_only_code",
        "overlong_code",
    ],
)
def test_live_source_failure_never_publishes_partial_bundle_or_outputs(
    failure_mode: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    rows = valid_source_rows()
    payloads = source_payloads(rows)
    failing_name = "tpex_disposition"
    if failure_mode == "timeout":
        events: list[FakeResponse | Exception] = [
            requests.Timeout("injected timeout")
        ]
    elif failure_mode == "http":
        response = FakeResponse(payloads[failing_name], status_code=503)
    elif failure_mode == "content_type":
        response = FakeResponse(payloads[failing_name], content_type="text/html")
    elif failure_mode == "json":
        response = FakeResponse(b"{not-json")
    elif failure_mode == "empty":
        response = FakeResponse(b"[]")
    elif failure_mode == "schema":
        rows[failing_name][0].pop("Date")
        response = FakeResponse(source_payloads(rows)[failing_name])
    else:
        invalid_codes = {
            "punctuation_code": "BAD-CODE!",
            "letters_only_code": "ABCD",
            "overlong_code": "1234567",
        }
        rows[failing_name][0]["SecuritiesCompanyCode"] = invalid_codes[failure_mode]
        response = FakeResponse(source_payloads(rows)[failing_name])
    if failure_mode != "timeout":
        events = [response]
    calls = install_live_http(
        monkeypatch,
        payloads,
        override_name=failing_name,
        override_events=events,
    )

    with pytest.raises(RuntimeError, match="bounded retries"):
        market_abnormal.run(TARGET_DATE)

    assert calls.count(failing_name) == market_abnormal.FETCH_ATTEMPTS
    assert not (tmp_path / market_abnormal.manifest_path_for(TARGET_DATE)).exists()
    assert_no_latest_or_history(tmp_path)


def test_transient_transport_and_content_failures_fresh_fetch_until_valid(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    payloads = source_payloads()
    source_name = "twse_disposition"
    sleeps: list[float] = []
    monkeypatch.setattr(market_abnormal.time, "sleep", sleeps.append)
    calls = install_live_http(
        monkeypatch,
        payloads,
        override_name=source_name,
        override_events=[
            FakeResponse(payloads[source_name], status_code=429, retry_after="7"),
            FakeResponse(b"{not-json"),
            FakeResponse(payloads[source_name]),
        ],
    )

    result = market_abnormal.run(TARGET_DATE)

    assert result["access_mode"] == "live_current_endpoints"
    assert calls.count(source_name) == 3
    assert sleeps == [7.0, 0.5]
    assert (tmp_path / market_abnormal.manifest_path_for(TARGET_DATE)).is_file()


@pytest.mark.parametrize("failure_mode", ["future", "unverifiable"])
def test_target_sensitive_row_date_failure_is_fail_closed(
    failure_mode: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    rows = valid_source_rows()
    if failure_mode == "future":
        rows["tpex_attention"][0]["Date"] = "1150822"
    else:
        rows["twse_attention_note"][0][
            "RecentlyMetAttentionSecuritiesCriteria"
        ] = "無可驗日期"
    install_live_http(monkeypatch, source_payloads(rows))

    with pytest.raises(RuntimeError, match="target-sensitive row"):
        market_abnormal.run(TARGET_DATE)

    assert not (tmp_path / market_abnormal.manifest_path_for(TARGET_DATE)).exists()
    assert_no_latest_or_history(tmp_path)


def test_historical_target_without_bundle_publishes_truthful_unavailable_snapshot(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    historical_target = "20260820"
    stale_latest = tmp_path / market_abnormal.OUT_CSV
    stale_latest.parent.mkdir(parents=True)
    stale_latest.write_text(
        "stock_id,market_abnormal_status\n2330,normal\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        market_abnormal.requests,
        "get",
        lambda *_args, **_kwargs: pytest.fail("historical target must not call live"),
    )

    result = market_abnormal.run(historical_target)
    replay = market_abnormal.run(historical_target)

    assert result["access_mode"] == "historical_unavailable"
    assert replay["manifest_sha256"] == result["manifest_sha256"]
    manifest = json.loads(
        (tmp_path / market_abnormal.manifest_path_for(historical_target)).read_text(
            encoding="utf-8"
        )
    )
    assert manifest == {
        "collection_mode": "historical_unavailable",
        "fetch_date": TARGET_DATE,
        "fetched_at": "2026-08-21 13:45:12 Asia/Taipei",
        "reason": market_abnormal.HISTORICAL_UNAVAILABLE_REASON,
        "schema_version": market_abnormal.BUNDLE_SCHEMA_VERSION,
        "source_count": 0,
        "sources": {},
        "target_date": historical_target,
    }
    latest = pd.read_csv(
        tmp_path / market_abnormal.OUT_CSV, dtype=str, keep_default_na=False
    )
    history = pd.read_csv(
        tmp_path / market_abnormal.HISTORY_CSV, dtype=str, keep_default_na=False
    )
    assert list(latest.columns) == market_abnormal.LATEST_COLUMNS
    assert latest.empty
    assert history.empty
    markdown = (tmp_path / market_abnormal.OUT_MD).read_text(encoding="utf-8")
    assert "historical_unavailable" in markdown
    assert "no stock may be inferred normal" in markdown
    assert (tmp_path / market_abnormal.OUT_CSV).read_bytes() == (
        tmp_path / market_abnormal.DOCS_CSV
    ).read_bytes()

    candidates = pd.DataFrame({"stock_id": ["2330"]})
    monkeypatch.setattr(
        surge_multifactor,
        "MARKET_ABNORMAL_STATUS_CSV",
        tmp_path / market_abnormal.OUT_CSV,
    )
    monkeypatch.setattr(
        surge_strict,
        "MARKET_ABNORMAL_STATUS_CSV",
        tmp_path / market_abnormal.OUT_CSV,
    )
    for consumer in (surge_multifactor, surge_strict):
        attached = consumer.attach_market_abnormal_status(candidates)
        assert attached["market_abnormal_status"].tolist() == ["not_checked"]
        assert attached["market_abnormal_risk_level"].tolist() == [
            "history_not_backfilled"
        ]


def test_current_target_incomplete_bundle_directory_fails_without_live_refetch(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    incomplete_bundle = (
        tmp_path / market_abnormal.manifest_path_for(TARGET_DATE).parent / "sources"
    )
    incomplete_bundle.mkdir(parents=True)
    monkeypatch.setattr(
        market_abnormal.requests,
        "get",
        lambda *_args, **_kwargs: pytest.fail("incomplete bundle must not refetch"),
    )

    with pytest.raises(FileNotFoundError, match="manifest is missing"):
        market_abnormal.run(TARGET_DATE)

    assert_no_latest_or_history(tmp_path)


@pytest.mark.parametrize("tamper", ["missing_source", "raw_hash", "columns", "row_count"])
def test_replay_rejects_incomplete_or_tampered_bundle_before_output_write(
    tamper: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    install_live_http(monkeypatch, source_payloads())
    market_abnormal.materialize_sources(TARGET_DATE)
    manifest_path = tmp_path / market_abnormal.manifest_path_for(TARGET_DATE)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_name = "twse_attention"
    raw_path = tmp_path / manifest["sources"][source_name]["path"]
    if tamper == "missing_source":
        raw_path.unlink()
    elif tamper == "raw_hash":
        raw_path.write_bytes(raw_path.read_bytes() + b" ")
    elif tamper == "columns":
        manifest["sources"][source_name]["columns"] = ["wrong"]
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    else:
        manifest["sources"][source_name]["row_count"] = 999
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    monkeypatch.setattr(
        market_abnormal.requests,
        "get",
        lambda *_args, **_kwargs: pytest.fail("existing bundle must not refetch"),
    )

    with pytest.raises((FileNotFoundError, ValueError)):
        market_abnormal.run(TARGET_DATE)

    assert_no_latest_or_history(tmp_path)


def test_atomic_bundle_rename_failure_removes_staging_and_writes_no_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    install_live_http(monkeypatch, source_payloads())
    monkeypatch.setattr(
        market_abnormal.os,
        "rename",
        lambda *_args: (_ for _ in ()).throw(OSError("injected rename failure")),
    )

    with pytest.raises(OSError, match="injected rename failure"):
        market_abnormal.run(TARGET_DATE)

    assert not (tmp_path / market_abnormal.manifest_path_for(TARGET_DATE)).exists()
    bundle_root = tmp_path / market_abnormal.BUNDLE_ROOT
    assert not list(bundle_root.glob(f".{TARGET_DATE}-*"))
    assert_no_latest_or_history(tmp_path)


def test_each_output_replace_is_atomic_for_an_existing_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "latest.csv"
    target.write_bytes(b"old\n")
    monkeypatch.setattr(
        market_abnormal.os,
        "replace",
        lambda *_args: (_ for _ in ()).throw(OSError("injected replace failure")),
    )

    with pytest.raises(OSError, match="injected replace failure"):
        market_abnormal.atomic_write_bytes(target, b"new\n")

    assert target.read_bytes() == b"old\n"
    assert not list(tmp_path.glob(".latest.csv.*"))


def test_output_group_is_not_claimed_as_transactional_on_mid_write_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    install_live_http(monkeypatch, source_payloads())
    original_write = market_abnormal.atomic_write_bytes

    def fail_at_history(path: Path, payload: bytes) -> None:
        if path == market_abnormal.HISTORY_CSV:
            raise OSError("injected history write failure")
        original_write(path, payload)

    monkeypatch.setattr(market_abnormal, "atomic_write_bytes", fail_at_history)

    with pytest.raises(OSError, match="injected history write failure"):
        market_abnormal.run(TARGET_DATE)

    assert (tmp_path / market_abnormal.OUT_CSV).is_file()
    assert (tmp_path / market_abnormal.DOCS_CSV).is_file()
    assert not (tmp_path / market_abnormal.HISTORY_CSV).exists()
    assert not (tmp_path / market_abnormal.OUT_MD).exists()
    assert not (tmp_path / market_abnormal.DOCS_MD).exists()


def test_legacy_history_target_date_is_not_guessed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    configure_current_day(tmp_path, monkeypatch)
    history_path = tmp_path / market_abnormal.HISTORY_CSV
    history_path.parent.mkdir(parents=True)
    legacy_row = {column: "" for column in market_abnormal.LEGACY_LATEST_COLUMNS}
    legacy_row.update(
        {
            "fetch_date": "20260613",
            "fetched_at": "2026-06-13 19:37:21 Asia/Taipei",
            "stock_id": "2330",
            "data_quality_status": "ok",
        }
    )
    pd.DataFrame([legacy_row]).to_csv(history_path, index=False, encoding="utf-8-sig")
    install_live_http(monkeypatch, source_payloads())

    market_abnormal.run(TARGET_DATE)

    history = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    legacy = history.loc[history["fetch_date"].eq("20260613")]
    assert legacy["target_date"].tolist() == [""]
    assert history.loc[history["target_date"].eq(TARGET_DATE)].duplicated(
        ["target_date", "stock_id"]
    ).sum() == 0


def test_cli_requires_explicit_target_date() -> None:
    with pytest.raises(SystemExit):
        market_abnormal.main([])


def test_bundle_git_attribute_preserves_literal_raw_bytes_with_autocrlf(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    def git(*args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", *args], cwd=repo, check=True, capture_output=True
        )

    git("init", "-q")
    git("config", "user.email", "market-abnormal-test@example.invalid")
    git("config", "user.name", "Market Abnormal Test")
    git("config", "core.autocrlf", "true")

    attributes_path = repo / ".gitattributes"
    attributes_path.write_bytes((ROOT / ".gitattributes").read_bytes())
    bundle_path_text = (
        "data/market_abnormal_status/bundles/20260821/"
        "sources/twse_attention.json"
    )
    bundle_path = repo / bundle_path_text
    bundle_path.parent.mkdir(parents=True)
    raw_payload = b'[\n  {"Code":"2330","Name":"TSMC"}\n]\n'
    raw_sha256 = hashlib.sha256(raw_payload).hexdigest()
    bundle_path.write_bytes(raw_payload)

    git("add", "--", ".gitattributes", bundle_path_text)
    git("commit", "-qm", "fixture with literal bundle bytes")
    attribute = git("check-attr", "text", "--", bundle_path_text)
    assert attribute.stdout.decode().strip() == f"{bundle_path_text}: text: unset"
    assert git("show", f"HEAD:{bundle_path_text}").stdout == raw_payload

    bundle_path.unlink()
    git("checkout", "--", bundle_path_text)
    checked_out = bundle_path.read_bytes()
    assert checked_out == raw_payload
    assert hashlib.sha256(checked_out).hexdigest() == raw_sha256

    attribute_rule = "data/market_abnormal_status/bundles/** -text"
    without_rule = "\n".join(
        line
        for line in attributes_path.read_text(encoding="utf-8").splitlines()
        if line != attribute_rule
    )
    attributes_path.write_text(without_rule + "\n", encoding="utf-8", newline="\n")
    git("add", "--", ".gitattributes")
    git("commit", "-qm", "remove literal bundle byte protection")
    missing_attribute = git("check-attr", "text", "--", bundle_path_text)
    assert missing_attribute.stdout.decode().strip() == (
        f"{bundle_path_text}: text: unspecified"
    )

    bundle_path.unlink()
    git("checkout", "--", bundle_path_text)
    mutated_checkout = bundle_path.read_bytes()
    assert mutated_checkout == raw_payload.replace(b"\n", b"\r\n")
    assert hashlib.sha256(mutated_checkout).hexdigest() != raw_sha256
