from __future__ import annotations

import copy
import csv
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_EVEN
import hashlib
import io
import json
from pathlib import Path
import subprocess

import pytest

from scripts import build_stock_price_history as history
from scripts import repair_daily_price_range as daily
from scripts import validate_tpex_nine_row_history_repair as validator


MANIFEST_PATH = Path(__file__).resolve().parents[1] / "config/tpex_official_field_repair_2026_nine_rows.json"
BASE_COLUMNS = ["date", "stock_id", "stock_name", "market", "open", "high", "low", "close", "volume", "trading_value", "source"]
HISTORY_COLUMNS = BASE_COLUMNS + ["source_file", "volume_ma20", "volume_ratio", "ma20"]


def _sha(payload):
    return hashlib.sha256(payload).hexdigest()


def _csv_bytes(header, rows, ending):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=header, lineterminator=ending)
    writer.writeheader()
    writer.writerows(rows)
    return b"\xef\xbb\xbf" + stream.getvalue().encode("utf-8")


def _records(payload):
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))


def _patch(payload, key, updates):
    lines = payload.splitlines(keepends=True)
    rows = _records(payload)
    header = list(rows[0])
    for index, row in enumerate(rows, start=1):
        if (row["stock_id"], row["date"]) != key:
            continue
        row.update(updates)
        line = lines[index]
        ending = "\r\n" if line.endswith(b"\r\n") else "\n" if line.endswith(b"\n") else ""
        stream = io.StringIO(newline="")
        csv.writer(stream, lineterminator=ending).writerow([row[column] for column in header])
        lines[index] = stream.getvalue().encode("utf-8")
        return b"".join(lines)
    raise AssertionError(f"missing synthetic identity: {key}")


def _bind(manifest, before, after):
    for item in manifest["files"]:
        item["before_sha256"] = _sha(before[item["path"]])
        item["after_sha256"] = _sha(after[item["path"]])


def _fixed_four(value):
    return str(value.quantize(Decimal("0.0001"), rounding=ROUND_HALF_EVEN))


@pytest.fixture
def repair_fixture():
    """Portable bytes; no F: receipts, local Git objects, or protected data."""
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    facts = {(row["stock_id"], row["date"]): row for row in manifest["rows"]}
    windows = {(row["stock_id"], row["date"]) for row in manifest["history_windows"]}
    before = {}
    for date in manifest["dates"]:
        rows = [{
            "date": date, "stock_id": "2330", "stock_name": "台積電",
            "market": "TWSE", "open": "10", "high": "12", "low": "9", "close": "11",
            "volume": "98765", "trading_value": "1086415", "source": "TWSE_JSON",
        }]
        for stock in manifest["stock_ids"]:
            fact = facts[(stock, date)]
            named = dict(zip(fact["official_fields"], fact["official_row"]))
            rows.append({
                "date": date, "stock_id": stock, "stock_name": "合成樣本",
                "market": "TPEx", "open": str(named["開盤"]), "high": str(named["最高"]),
                "low": str(named["最低"]), "close": str(named["收盤"]),
                "volume": "10000", "trading_value": "110000", "source": fact["source_before"],
            })
        payload = _csv_bytes(BASE_COLUMNS, rows, "\r\n")
        for prefix in ("", "daily_price_"):
            before[f"data/daily_price/{prefix}{date}.csv"] = payload
    preceding = []
    day = datetime.strptime("20260527", "%Y%m%d") - timedelta(days=1)
    while len(preceding) < 20:
        if day.weekday() < 5:
            preceding.append(day.strftime("%Y%m%d"))
        day -= timedelta(days=1)
    preceding.reverse()
    for stock in manifest["stock_ids"]:
        dates = preceding + sorted(date for candidate, date in windows if candidate == stock) + ["20260706"]
        rows = []
        volumes = [Decimal(10000 + index * 37) for index in range(len(dates))]
        for index, date in enumerate(dates):
            sample = volumes[max(0, index - 19):index + 1]
            mean = sum(sample) / len(sample) if len(sample) >= 5 else None
            fact = facts.get((stock, date))
            row = {
                "date": date, "stock_id": stock, "stock_name": "合成樣本", "market": "TPEx",
                "open": "10", "high": "12", "low": "9", "close": "11",
                "volume": str(volumes[index]), "trading_value": "110000",
                "source": fact["source_before"] if fact else "TPEX_NEW_JSON",
                "source_file": f"data/daily_price/daily_price_{date}.csv",
                "volume_ma20": _fixed_four(mean) if mean is not None else "",
                "volume_ratio": _fixed_four(volumes[index] / mean) if mean is not None else "",
                "ma20": "10.1250",
            }
            if fact:
                named = dict(zip(fact["official_fields"], fact["official_row"]))
                row.update({column: str(named[label]) for column, label in
                            (("open", "開盤"), ("high", "最高"), ("low", "最低"), ("close", "收盤"))})
            rows.append(row)
        before[f"data/stock_price_history/{stock}.csv"] = _csv_bytes(HISTORY_COLUMNS, rows, "\n")
    # Expected bytes are projected independently of both production writers.
    after = dict(before)
    for path, payload in before.items():
        for key, fact in facts.items():
            if key in {(row["stock_id"], row["date"]) for row in _records(payload)}:
                after[path] = _patch(after[path], key, {
                    "volume": fact["volume_shares"], "trading_value": fact["trading_value_ntd"],
                    "source": fact["source_after"],
                })
        if path.startswith("data/stock_price_history/"):
            rows = _records(after[path])
            for index, row in enumerate(rows):
                key = row["stock_id"], row["date"]
                if key in windows:
                    sample = [Decimal(candidate["volume"]) for candidate in rows[max(0, index - 19):index + 1]]
                    mean = sum(sample) / len(sample)
                    after[path] = _patch(after[path], key, {
                        "volume_ma20": _fixed_four(mean),
                        "volume_ratio": _fixed_four(Decimal(row["volume"]) / mean),
                    })
    _bind(manifest, before, after)
    return manifest, before, after


def _produced(before, manifest):
    return {**daily.build_tpex_nine_row_daily_postimages(before, manifest),
            **history.build_tpex_nine_row_history_postimages(before, manifest)}


def test_nine_keys_and_99_physical_rows_match_independent_bytes(repair_fixture):
    manifest, before, expected = repair_fixture
    original = copy.deepcopy(before)
    produced = _produced(before, manifest)
    assert produced == expected
    assert before == original
    result = validator.validate_repair_postimages(before, produced, manifest)
    assert result["result"] == "PASS"
    assert result["logical_stock_date_keys"] == 9
    assert result["changed_physical_rows"] == 99
    assert result["raw_daily_copy_rows"] == 18
    assert result["history_primary_rows"] == 9
    assert result["history_derived_rows"] == 81
    assert result["original_publication_version_verified"] is False


def test_prices_other_indicators_and_unselected_bytes_stay_unchanged(repair_fixture):
    manifest, before, _ = repair_fixture
    after = _produced(before, manifest)
    primary = {(row["stock_id"], row["date"]) for row in manifest["rows"]}
    windows = {(row["stock_id"], row["date"]) for row in manifest["history_windows"]}
    for path in before:
        old_lines = before[path].splitlines(keepends=True)
        new_lines = after[path].splitlines(keepends=True)
        assert old_lines[0] == new_lines[0]
        for index, (old, new) in enumerate(zip(_records(before[path]), _records(after[path])), start=1):
            key = old["stock_id"], old["date"]
            allowed = {"volume", "trading_value", "source"} if key in primary else set()
            if path.startswith("data/stock_price_history/") and key in windows:
                allowed |= {"volume_ma20", "volume_ratio"}
            assert all(old[column] == new[column] for column in old if column not in allowed)
            if not allowed:
                assert old_lines[index] == new_lines[index]
            assert old_lines[index].endswith(b"\r\n") == new_lines[index].endswith(b"\r\n")


def test_rolling20_includes_current_volume_and_divides_before_rounding(repair_fixture):
    manifest, before, _ = repair_fixture
    after = _produced(before, manifest)
    rows = _records(after["data/stock_price_history/5498.csv"])
    index = next(i for i, row in enumerate(rows) if row["date"] == "20260527")
    sample = [Decimal(row["volume"]) for row in rows[index - 19:index + 1]]
    mean = sum(sample) / 20
    assert Decimal(rows[index]["volume_ma20"]) == mean.quantize(Decimal("0.0001"))
    assert Decimal(rows[index]["volume_ratio"]) == (Decimal(rows[index]["volume"]) / mean).quantize(Decimal("0.0001"))
    excluding_current = sum(Decimal(row["volume"]) for row in rows[index - 20:index]) / 20
    assert Decimal(rows[index]["volume_ma20"]) != excluding_current


@pytest.mark.parametrize("writer,path", [
    (daily.build_tpex_nine_row_daily_postimages, "data/daily_price/20260527.csv"),
    (history.build_tpex_nine_row_history_postimages, "data/stock_price_history/5498.csv"),
])
@pytest.mark.parametrize("sha_field,match", [("before_sha256", "before SHA"), ("after_sha256", "postimage SHA")])
def test_writer_rejects_wrong_sha(repair_fixture, writer, path, sha_field, match):
    manifest, before, _ = repair_fixture
    next(item for item in manifest["files"] if item["path"] == path)[sha_field] = "0" * 64
    with pytest.raises(ValueError, match=match):
        writer(before, manifest)


@pytest.mark.parametrize("writer", [daily.build_tpex_nine_row_daily_postimages, history.build_tpex_nine_row_history_postimages])
def test_writer_rejects_unknown_share_unit_version(repair_fixture, writer):
    manifest, before, _ = repair_fixture
    manifest["rows"][0]["source_after"] = manifest["rows"][0]["source_before"] + "_LOTS_V1"
    with pytest.raises(ValueError, match="unknown source units"):
        writer(before, manifest)


def test_validator_rejects_pit_claim_and_unknown_units(repair_fixture):
    manifest, before, after = repair_fixture
    manifest["original_publication_version_verified"] = True
    with pytest.raises(ValueError, match="original publication/PIT"):
        validator.validate_repair_postimages(before, after, manifest)
    manifest["original_publication_version_verified"] = False
    manifest["rows"][0]["source_after"] = manifest["rows"][0]["source_before"] + "_SHARES_V2"
    with pytest.raises(ValueError, match="share-unit version"):
        validator.validate_repair_postimages(before, after, manifest)


@pytest.mark.parametrize("column,value,date,match", [
    ("close", "999999", "20260527", "unapproved column/price"),
    ("volume_ma20", "1", "20260527", "independent volume_ma20"),
    ("volume", "1", "20260706", "unselected CSV row"),
])
def test_independent_validator_catches_semantic_mutation_after_sha_rebinding(repair_fixture, column, value, date, match):
    manifest, before, after = repair_fixture
    path = "data/stock_price_history/5498.csv"
    after[path] = _patch(after[path], ("5498", date), {column: value})
    _bind(manifest, before, after)
    with pytest.raises(ValueError, match=match):
        validator.validate_repair_postimages(before, after, manifest)


def test_daily_alias_mismatch_is_rejected_after_sha_rebinding(repair_fixture):
    manifest, before, after = repair_fixture
    path = "data/daily_price/20260527.csv"
    for payloads in (before, after):
        payloads[path] = _patch(payloads[path], ("2330", "20260527"), {"stock_name": "台積電別名"})
    _bind(manifest, before, after)
    with pytest.raises(ValueError, match="daily aliases disagree"):
        daily.build_tpex_nine_row_daily_postimages(before, manifest)
    with pytest.raises(ValueError, match="daily aliases differ"):
        validator.validate_repair_postimages(before, after, manifest)


def test_history_window_boundary_is_rejected(repair_fixture):
    manifest, before, after = repair_fixture
    manifest["history_windows"][0]["date"] = "20260706"
    with pytest.raises(ValueError, match="history window mismatch"):
        history.build_tpex_nine_row_history_postimages(before, manifest)
    with pytest.raises(ValueError, match="history window boundary mismatch"):
        validator.validate_repair_postimages(before, after, manifest)


@pytest.mark.parametrize("writer,path", [
    (daily.build_tpex_nine_row_daily_postimages, "data/daily_price/20260527.csv"),
    (history.build_tpex_nine_row_history_postimages, "data/stock_price_history/5498.csv"),
])
def test_missing_primary_identity_is_rejected(repair_fixture, writer, path):
    manifest, before, after = repair_fixture
    lines = before[path].splitlines(keepends=True)
    index = next(i for i, row in enumerate(_records(before[path]), start=1)
                 if (row["stock_id"], row["date"]) == ("5498", "20260527"))
    before[path] = b"".join(lines[:index] + lines[index + 1:])
    _bind(manifest, before, after)
    with pytest.raises(ValueError, match="missing .* identity"):
        writer(before, manifest)


@pytest.mark.parametrize("writer,path", [
    (daily.build_tpex_nine_row_daily_postimages, "data/daily_price/20260527.csv"),
    (history.build_tpex_nine_row_history_postimages, "data/stock_price_history/5498.csv"),
])
def test_duplicate_primary_identity_is_rejected(repair_fixture, writer, path):
    manifest, before, after = repair_fixture
    lines = before[path].splitlines(keepends=True)
    index = next(i for i, row in enumerate(_records(before[path]), start=1)
                 if (row["stock_id"], row["date"]) == ("5498", "20260527"))
    before[path] += lines[index]
    _bind(manifest, before, after)
    with pytest.raises(ValueError, match="duplicate identity|malformed history identities/order"):
        writer(before, manifest)


def _indexed_fixture(tmp_path, before):
    repo = tmp_path / "repo"
    repo.mkdir()

    def git(*args, payload=None):
        return subprocess.run(["git", *args], cwd=repo, input=payload, capture_output=True, check=True).stdout

    git("init", "-q")
    entries = []
    for path, payload in {**before, "keep.txt": b"unrelated staged entry\n"}.items():
        blob = git("hash-object", "-w", "--stdin", payload=payload).decode().strip()
        entries.append(f"100644 {blob}\t{path}\n")
    git("update-index", "--index-info", payload="".join(entries).encode())
    git("update-index", "--skip-worktree", "--stdin", payload=("\n".join(before) + "\n").encode())
    return repo, git


def test_staging_publishes_all_nine_without_data_checkout_and_preserves_next_lock(repair_fixture, tmp_path, monkeypatch):
    manifest, before, after = repair_fixture
    repo, git = _indexed_fixture(tmp_path, before)
    index = repo / ".git/index"
    real_replace = daily.os.replace

    def replace_then_next_git_lock(source, target):
        real_replace(source, target)
        Path(source).write_bytes(b"subsequent Git lock")

    monkeypatch.setattr(daily.os, "replace", replace_then_next_git_lock)
    result = daily.stage_tpex_nine_row_repair(repo, manifest, tmp_path / "index-temp")
    assert result["changed_physical_rows"] == 99
    assert {path: git("show", f":{path}") for path in before} == after
    assert git("show", ":keep.txt") == b"unrelated staged entry\n"
    assert not (repo / "data").exists()
    assert all(line.startswith(b"S ") for line in git("ls-files", "-v", "data").splitlines())
    assert index.with_name("index.lock").read_bytes() == b"subsequent Git lock"


def test_staging_publish_failure_leaves_original_index_byte_identical(repair_fixture, tmp_path, monkeypatch):
    manifest, before, _ = repair_fixture
    repo, git = _indexed_fixture(tmp_path, before)
    index = repo / ".git/index"
    original_index = index.read_bytes()

    def fail_publish(source, target):
        raise OSError("simulated index publication failure")

    monkeypatch.setattr(daily.os, "replace", fail_publish)
    with pytest.raises(OSError, match="publication failure"):
        daily.stage_tpex_nine_row_repair(repo, manifest, tmp_path / "index-temp")
    assert index.read_bytes() == original_index
    assert {path: git("show", f":{path}") for path in before} == before
    assert not index.with_name("index.lock").exists()
    assert not (repo / "data").exists()
    assert list((tmp_path / "index-temp").iterdir()) == []
