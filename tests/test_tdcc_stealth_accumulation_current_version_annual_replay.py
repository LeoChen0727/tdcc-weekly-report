"""一年 current-version 回放的聚焦回歸；合成輸入不構成 PIT／promotion 證據。"""

from __future__ import annotations

import csv
import gzip
import io
import json
import sys
from decimal import Decimal, localcontext
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_tdcc_stealth_accumulation_current_version_annual_replay as producer  # noqa: E402


TDCC_LEVELS = (
    "400,001-600,000", "600,001-800,000", "800,001-1,000,000",
    "more than 1,000,001",
)
WARMUP_FIELDS = ["日 期", "成交張數", "成交仟元", "開盤", "最高", "最低", "收盤"]
FALSE_CONTRACT_FLAGS = (
    "formal_use", "promotion_evidence_allowed", "input_availability_proven",
    "full_period_pit_complete", "calendar_complete_coverage_verified",
    "corporate_action_complete_coverage_verified", "ordinary_stock_universe_certified",
    "private_raw_publication_allowed",
)


def contract() -> dict:
    return json.loads((ROOT / producer.CONTRACT_FILE).read_text(encoding="utf-8-sig"))


def csv_payload(rows: list[dict], fields: list[str] | None = None) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields or list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


class FakeGitSource:
    """只有明列 blob 的記憶體 reader；不下載、不 materialize 真實資料。"""

    def __init__(self, blobs: dict[tuple[str, str], bytes]):
        self.blobs = blobs
        self.calls: list[tuple[str, str]] = []
        self.sources: dict = {}

    def tree(self, ref):
        return {path: producer.sha(value) for (version, path), value in self.blobs.items() if version == ref}

    def blob(self, ref, path):
        self.calls.append((ref, path))
        value = self.blobs[(ref, path)]
        self.sources[(ref, path)] = dict(ref=ref, path=path, bytes=len(value), sha256=producer.sha(value))
        return value


def quote(date="20250801", **updates):
    row = dict(stock_id="2330", stock_name="合成測試", market="TPEX", date=date,
               source="MAIN_CANONICAL", open="10", high="12", low="9", close="11",
               volume="1234000", trading_value="100000")
    row.update(updates)
    return row


def price_source(rows: list[dict], *, extras: dict | None = None):
    ref = contract()["price_source_ref"]
    blobs = {(ref, "data/daily_price/" + row["date"].replace("-", "") + ".csv"): csv_payload([row]) for row in rows}
    blobs.update(extras or {})
    return FakeGitSource(blobs)


def warmup_input(*, date="114/08/01", volume="1,234", close="11", **changes):
    table = dict(fields=WARMUP_FIELDS, data=[[date, volume, "100", "10", "12", "9", close]])
    payload = json.dumps(dict(tables=[table]), ensure_ascii=False).encode("utf-8")
    item = dict(kind="price_warmup", path="synthetic/warmup.json", stock_id="2330",
                sha256=producer.sha(payload))
    item.update(changes)
    return item, payload


def price_subcontract(items):
    # 技術 reader 的輸入 fixture，絕不傳給正式 validate_contract 冒充固定契約。
    return dict(price_source_ref=contract()["price_source_ref"], history_start="20250401",
                as_of="20260909", requested_signal_start="20250910", external_files=items)


def tdcc_input(*, ratios=("1.2", "2.3", "3.4", "4.5"), omit=None, extra=True):
    rows = [dict(日期="2025-09-05", 股票代碼="2330", 持股分級=level, 比例=value)
            for level, value in zip(TDCC_LEVELS, ratios) if level != omit]
    if extra:
        rows.extend([dict(日期="2025-09-05", 股票代碼="2330", 持股分級="adjustment", 比例="888"),
                     dict(日期="2025-09-05", 股票代碼="2330", 持股分級="total", 比例="100")])
    payload = csv_payload(rows)
    item = dict(kind="tdcc", path="synthetic/one-week.csv", date="20250905", rows=len(rows),
                sha256=producer.sha(payload))
    technical = dict(external_files=[item], expected_tdcc_weeks=1, expected_tdcc_rows=len(rows))
    return technical, {item["path"]: payload}


@pytest.fixture(scope="module")
def frozen_selector():
    # 只讀固定 Git objects 中的 allowlisted 函式；不 import 任何 independent validator。
    return producer.load_selector(producer.GitSource(ROOT), contract())


def selector_row(**changes):
    row = dict(tdcc_price_phase="", tdcc_status="", tdcc_accumulation_signal="mild_accumulation",
               volume_confirmed_breakout=False, volume_ratio="1.2", return_5d="3", return_20d="7",
               open="99", high="101", low="98", close="100", high_20="110", low_20="90",
               volume_ma20_lots="1000", previous_20d_high_ex_today="110",
               previous_close="99", daily_return_calc="1")
    row.update(changes)
    return row


def test_registered_contract_has_exact_55_tdcc_and_65_external_inputs():
    current = contract()
    producer.validate_contract(current)
    files = current["external_files"]
    tdcc = [item for item in files if item["kind"] == "tdcc"]
    assert len(files) == len({item["path"] for item in files}) == 65
    assert len(tdcc) == len({item["date"] for item in tdcc}) == 55
    assert current["expected_tdcc_weeks"] == 55
    assert current["expected_tdcc_rows"] == sum(item["rows"] for item in tdcc) == 3667325
    assert max(item["date"] for item in tdcc) == "20260904"
    assert all(len(item["sha256"]) == 64 for item in files)
    assert all(current[key] is False for key in FALSE_CONTRACT_FLAGS)
    assert current["price_source_ref"] == current["outcome_ref"]
    assert {producer.PREFIX + suffix for suffix in current["artifact_kinds"]} == producer.GENERATED


@pytest.mark.parametrize("change", ["path", "sha256", "remove_week", "extra_week", "date", "rows"])
def test_fixed_external_allowlist_cannot_be_changed(change):
    current = contract()
    item = next(item for item in current["external_files"] if item["kind"] == "tdcc")
    if change == "remove_week":
        current["external_files"].remove(item)
    elif change == "extra_week":
        current["external_files"].append(dict(item, path="unapproved.csv", date="20260911"))
    elif change == "rows":
        item["rows"] += 1
    else:
        item[change] = {"path": "unapproved.csv", "sha256": "0" * 64, "date": "20260911"}[change]
    with pytest.raises((ValueError, RuntimeError)):
        producer.validate_contract(current)


@pytest.mark.parametrize("field", FALSE_CONTRACT_FLAGS)
def test_pit_and_formal_flags_cannot_be_enabled(field, tmp_path):
    current = contract()
    current[field] = True
    with pytest.raises((ValueError, RuntimeError)):
        producer.build(tmp_path, current, tmp_path)


@pytest.mark.parametrize("field", ["selector_ref", "classifier_ref", "operation_ref", "outcome_ref", "price_source_ref"])
def test_pinned_source_ref_change_is_rejected(field):
    current = contract()
    current[field] = "0" * 40
    with pytest.raises((ValueError, RuntimeError)):
        producer.validate_contract(current)


def test_external_reader_reads_only_named_path_and_exact_hash(tmp_path):
    named = tmp_path / "named.csv"
    named.write_bytes(b"synthetic,only\n1,2\n")
    (tmp_path / "unlisted.csv").write_bytes(b"never consumed")
    technical = {"external_files": [dict(path=named.name, sha256=producer.sha(named.read_bytes()))]}
    assert producer.external_inputs(tmp_path, technical) == {named.name: named.read_bytes()}
    named.write_bytes(b"modified\n")
    with pytest.raises(ValueError, match="hash mismatch"):
        producer.external_inputs(tmp_path, technical)


def test_external_reader_does_not_substitute_same_bytes_at_another_path(tmp_path):
    payload = b"synthetic\n"
    (tmp_path / "wrong.csv").write_bytes(payload)
    with pytest.raises(ValueError, match="Missing/linked"):
        producer.external_inputs(tmp_path, {"external_files": [dict(path="required.csv", sha256=producer.sha(payload))]})


def test_tdcc_four_bins_exclude_adjustment_and_total():
    technical, payloads = tdcc_input()
    row = producer.load_tdcc(technical, payloads)["20250905"]["2330"]
    assert row["p400"] == pytest.approx(11.4)
    assert row["p1000"] == pytest.approx(4.5)


def test_equal_tdcc_decimal_aggregates_never_create_phantom_accumulation(frozen_selector):
    """只重分配400四bin，不可把二進位加法誤差變成 mild 或 up weeks。"""
    _, classify = frozen_selector
    dates = ("20250815", "20250822", "20250829", "20250905")
    distributions = (("0.15", "0.15", "0", "0"), ("0.1", "0.2", "0", "0")) * 2
    items, payloads = [], {}
    for date, distribution in zip(dates, distributions):
        rows = [dict(日期=date, 股票代碼="2330", 持股分級=level, 比例=ratio)
                for level, ratio in zip(TDCC_LEVELS, distribution)]
        payload = csv_payload(rows)
        item = dict(kind="tdcc", path=f"synthetic/equal-aggregate-{date}.csv", date=date,
                    rows=4, sha256=producer.sha(payload))
        items.append(item)
        payloads[item["path"]] = payload
    technical = dict(external_files=items, expected_tdcc_weeks=4, expected_tdcc_rows=16)
    # 重現舊失敗，證明此fixture實際跨過 frozen classifier 的正值邊界。
    old_float_sums = [sum(float(value) for value in distribution) for distribution in distributions]
    assert old_float_sums == [0.3, 0.30000000000000004, 0.3, 0.30000000000000004]
    old_delta = old_float_sums[-1] - old_float_sums[0]
    old_up = sum(after > before for before, after in zip(old_float_sums, old_float_sums[1:]))
    assert old_delta > 0 and old_up == 2
    assert classify(4, old_delta, 0, old_up, 0)[0] == "mild_accumulation"
    with localcontext() as context:
        context.prec = 6
        weeks = producer.load_tdcc(technical, payloads)
    p400 = [weeks[date]["2330"]["p400"] for date in dates]
    p1000 = [weeks[date]["2330"]["p1000"] for date in dates]
    assert p400 == [0.3] * 4
    assert p1000 == [0.0] * 4
    delta400 = p400[-1] - p400[0]
    up400 = sum(after > before for before, after in zip(p400, p400[1:]))
    delta1000 = p1000[-1] - p1000[0]
    up1000 = sum(after > before for before, after in zip(p1000, p1000[1:]))
    assert (delta400, delta1000, up400, up1000) == (0, 0, 0, 0)
    assert classify(4, delta400, delta1000, up400, up1000)[0] == "neutral"


@pytest.mark.parametrize("omit", TDCC_LEVELS)
def test_missing_tdcc_bin_stays_none_not_zero(omit):
    technical, payloads = tdcc_input(omit=omit)
    row = producer.load_tdcc(technical, payloads)["20250905"]["2330"]
    assert row["p400"] is None
    if omit == TDCC_LEVELS[-1]:
        assert row["p1000"] is None


@pytest.mark.parametrize("invalid", ["", "--", "NaN", "inf"])
def test_invalid_tdcc_ratio_is_not_zero_filled(invalid):
    technical, payloads = tdcc_input(ratios=(invalid, "2", "3", "4"))
    row = producer.load_tdcc(technical, payloads)["20250905"]["2330"]
    assert row["p400"] is None
    assert row["p1000"] == 4


@pytest.mark.parametrize("defect", ["duplicate_bin", "wrong_date", "row_count", "week_count"])
def test_tdcc_shape_and_effective_date_fail_closed(defect):
    technical, payloads = tdcc_input()
    item = technical["external_files"][0]
    rows = producer.records(payloads[item["path"]])
    if defect == "duplicate_bin":
        rows.append(dict(rows[0]))
        item["rows"] += 1
        technical["expected_tdcc_rows"] += 1
    elif defect == "wrong_date":
        rows[0]["日期"] = "2025-09-12"
    elif defect == "row_count":
        item["rows"] += 1
    else:
        technical["expected_tdcc_weeks"] = 2
    payloads[item["path"]] = csv_payload(rows)
    with pytest.raises(ValueError):
        producer.load_tdcc(technical, payloads)


def synthetic_build(tmp_path, monkeypatch, frozen_selector, *, defect="complete", extra_price_dates=(), closed_dates=()):
    """完整固定 contract 不變；只注入明示的合成已解析輸入，結果留在記憶體。"""
    current = contract()
    ref = current["price_source_ref"]
    start = current["requested_signal_start"]
    dates = [date for date, weekday in producer.date_range("20250801", start) if weekday < 5][-21:]
    dates.extend(extra_price_dates)
    source = price_source([quote(date, open="99", high="110", low="90", close="100", volume="1200000") for date in dates])
    price_rows = {date: producer.daily(source, ref, date)[0] for date in dates}
    metadata = {date: producer.daily(source, ref, date)[1] for date in dates}
    for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
        source.blobs[(ref, path)] = b"date\n"
    source.blobs[(current["operation_ref"], "scripts/build_tdcc_stealth_accumulation_operation_replay.py")] = b"# synthetic source receipt only\n"
    source.blobs[(current["operation_ref"], "docs/specs/tdcc_stealth_accumulation_operation_replay_v3.md")] = b"synthetic source receipt only\n"
    source.blobs[(ref, "scripts/build_stock_price_history.py")] = b"# synthetic source receipt only\n"
    retained = current["anomaly_retention_reference"]
    source.blobs[(retained["ref"], retained["path"])] = json.dumps({retained["field"]: []}).encode()
    tdcc_items = sorted((item for item in current["external_files"] if item["kind"] == "tdcc" and item["date"] <= start), key=lambda item: item["date"])[-4:]
    assert len(tdcc_items) == 4
    weeks = {item["date"]: {"2330": dict(date=item["date"], row_date_valid=True,
             p400=10 + index, p1000=5 + index / 10, path=item["path"])} for index, item in enumerate(tdcc_items)}
    if defect == "missing_week":
        weeks[tdcc_items[0]["date"]] = {}
    elif defect == "missing_bin":
        weeks[tdcc_items[0]["date"]]["2330"]["p400"] = None
    payloads = {item["path"]: b"date,scheduled_closed\n" for item in current["external_files"]}
    if closed_dates:
        for item in current["external_files"]:
            if item["kind"] == "calendar":
                payloads[item["path"]] = csv_payload([
                    dict(date=date, scheduled_closed="True") for date in closed_dates
                ])
    monkeypatch.setattr(producer, "GitSource", lambda _: source)
    monkeypatch.setattr(producer, "load_selector", lambda *_: frozen_selector)
    monkeypatch.setattr(producer, "external_inputs", lambda *_: payloads)
    monkeypatch.setattr(producer, "load_tdcc", lambda *_: weeks)
    monkeypatch.setattr(producer, "read_current_prices", lambda *_: (price_rows, metadata, dict(warmup_nonquote_rows=0, supplemental_price_rows=0)))
    return producer.build(tmp_path, current, tmp_path)


@pytest.mark.parametrize("defect", ["missing_week", "missing_bin", "complete"])
def test_four_week_feature_gate_never_zero_fills_missing_coverage(defect, tmp_path, monkeypatch, frozen_selector):
    artifacts = synthetic_build(tmp_path, monkeypatch, frozen_selector, defect=defect)
    assert set(artifacts) == producer.GENERATED
    manifest = json.loads(artifacts[producer.NAMES["source_manifest"]])
    assert manifest["full_period_pit_complete"] is False
    assert manifest["formal_use"] is False
    assert manifest["promotion_evidence_allowed"] is False
    features = producer.records(gzip.decompress(artifacts[producer.NAMES["features"]]))
    assert len(features) == 1
    row = features[0]
    assert row["history_observations"] == "21"
    assert row["input_availability_proven"] == row["formal_use"] == row["promotion_evidence_allowed"] == "False"
    if defect == "complete":
        assert row["feature_supported"] == row["selected"] == "True"
        assert float(row["tdcc_400_change_sum"]) == pytest.approx(3)
        assert float(row["tdcc_1000_change_sum"]) == pytest.approx(0.3)
        assert row["tdcc_400_up_weeks"] == row["tdcc_1000_up_weeks"] == "3"
    else:
        assert row["feature_supported"] == row["selected"] == "False"
        assert "tdcc_four_batch_coverage_missing" in row["unsupported_reasons"]
        assert row["tdcc_400_change_sum"] == row["tdcc_1000_change_sum"] == ""
        assert row["tdcc_accumulation_signal"] == ""


def test_closed_date_disclosure_is_signal_prefix_and_only_actual_price_copies(tmp_path, monkeypatch, frozen_selector):
    """合成 closure 僅供欄位時序回歸，不宣稱是真實交易所休市事件。"""
    artifacts = synthetic_build(
        tmp_path, monkeypatch, frozen_selector,
        extra_price_dates=("20250911", "20250912"),
        closed_dates=("20250812", "20250911"),
    )
    features = {row["signal_date"]: row for row in producer.records(
        gzip.decompress(artifacts[producer.NAMES["features"]])
    )}
    coverage = {row["signal_date"]: row for row in producer.records(artifacts[producer.NAMES["coverage"]])}
    assert set(features) == {"20250910", "20250912"}
    for rows in (features, coverage):
        assert rows["20250910"]["historical_closed_date_files_excluded"] == ""
        assert rows["20250912"]["historical_closed_date_files_excluded"] == "20250911"
        assert "20250911" not in rows
    for row in features.values():
        assert row["feature_supported"] == row["selected"] == "True"
        assert row["history_observations"] == "21"
        assert "20250911" not in row["observed_history_dates"].split(";")
        assert "20250812" not in row["historical_closed_date_files_excluded"].split(";")
    manifest = json.loads(artifacts[producer.NAMES["source_manifest"]])
    assert manifest["evidence"]["calendar_closures"] == ["20250812", "20250911"]


def test_current_prices_use_canonical_day_and_same_pinned_ref_not_alias_cache():
    ref = contract()["price_source_ref"]
    canonical = quote("20250909")
    extras = {
        (ref, "data/daily_price/2025-09-09.csv"): csv_payload([quote("20250909", close="999")]),
        (ref, "data/stock_price_history/2330.csv"): b"old cached values must never be read",
        ("0" * 40, "data/daily_price/20250909.csv"): csv_payload([quote("20250909", close="777")]),
    }
    source = price_source([canonical], extras=extras)
    prices, metadata, supplemental = producer.read_current_prices(source, price_subcontract([]), {})
    assert prices["20250909"]["2330"]["close"] == 11
    assert source.calls == [(ref, "data/daily_price/20250909.csv")]
    assert prices["20250909"]["2330"]["source_ref"] == ref
    assert metadata["20250909"]["path"] == "data/daily_price/20250909.csv"
    assert supplemental["supplemental_price_rows"] == 0


def test_daily_alias_alone_is_not_a_canonical_day():
    ref = contract()["price_source_ref"]
    source = FakeGitSource({(ref, "data/daily_price/2025-09-09.csv"): csv_payload([quote("20250909")])})
    rows, meta = producer.daily(source, ref, "20250909")
    assert rows == {} and meta["missing"] is True and source.calls == []


def test_daily_code_universe_retains_possible_tdr_and_marks_bad_date():
    ref = contract()["price_source_ref"]
    rows = [quote("20250909", stock_id=sid) for sid in ("2330", "9103", "0050", "12345")]
    rows.append(quote("20250908", stock_id="5678"))
    source = FakeGitSource({(ref, "data/daily_price/20250909.csv"): csv_payload(rows)})
    actual, meta = producer.daily(source, ref, "20250909")
    assert set(actual) == {"2330", "9103", "5678"}
    assert actual["5678"]["date_mismatch"] is True
    assert not producer.valid_price(actual["5678"])
    assert meta["excluded_code_rows"] == 2


def test_warmup_lots_are_multiplied_by_1000_shares():
    item, payload = warmup_input()
    prices, _, counts = producer.read_current_prices(FakeGitSource({}), price_subcontract([item]), {item["path"]: payload})
    assert prices["20250801"]["2330"]["volume"] == 1234000
    assert prices["20250801"]["2330"]["source"] == "TPEx_OFFICIAL_MONTHLY_CURRENT_VERSION"
    assert counts == dict(warmup_nonquote_rows=0, supplemental_price_rows=1)


def test_warmup_missing_volume_is_none_not_zero():
    item, payload = warmup_input(volume="--")
    prices, _, _ = producer.read_current_prices(FakeGitSource({}), price_subcontract([item]), {item["path"]: payload})
    assert prices["20250801"]["2330"]["volume"] is None


def test_warmup_nonquote_ohlc_is_not_added_as_zero():
    item, payload = warmup_input(close="--")
    prices, _, counts = producer.read_current_prices(FakeGitSource({}), price_subcontract([item]), {item["path"]: payload})
    assert prices == {}
    assert counts == dict(warmup_nonquote_rows=1, supplemental_price_rows=0)


@pytest.mark.parametrize("date", ["114/09/10", "114/09/11"])
def test_warmup_cannot_supply_signal_start_or_later(date):
    item, payload = warmup_input(date=date)
    with pytest.raises(ValueError, match="Warmup cannot supply"):
        producer.read_current_prices(FakeGitSource({}), price_subcontract([item]), {item["path"]: payload})


def test_equal_valid_main_row_keeps_original_main_lineage():
    item, payload = warmup_input()
    prices, _, counts = producer.read_current_prices(price_source([quote()]), price_subcontract([item]), {item["path"]: payload})
    assert prices["20250801"]["2330"]["source"] == "MAIN_CANONICAL"
    assert prices["20250801"]["2330"]["source_path"] == "data/daily_price/20250801.csv"
    assert counts["supplemental_price_rows"] == 0


@pytest.mark.parametrize("change", [dict(close="10.5"), dict(volume="999")])
def test_warmup_cannot_overwrite_conflicting_valid_main_row(change):
    item, payload = warmup_input(**change)
    with pytest.raises(ValueError, match="valid-row conflict"):
        producer.read_current_prices(price_source([quote()]), price_subcontract([item]), {item["path"]: payload})


def test_warmup_can_replace_invalid_main_ohlc_row():
    item, payload = warmup_input()
    prices, _, counts = producer.read_current_prices(price_source([quote(close="--")]), price_subcontract([item]), {item["path"]: payload})
    assert prices["20250801"]["2330"]["close"] == 11
    assert prices["20250801"]["2330"]["source_path"] == "external:" + item["path"]
    assert counts["supplemental_price_rows"] == 1


@pytest.mark.parametrize("existing", [True, False])
def test_recovery_is_only_for_an_absent_exact_main_day(existing):
    row = quote("20250915")
    row["volume_shares"] = row.pop("volume")
    payload = csv_payload([row])
    item = dict(kind="price_recovery", path="synthetic/recovery.csv", date="20250915", rows=1, sha256=producer.sha(payload))
    technical = dict(price_subcontract([item]), as_of="20250915")
    source = price_source([quote("20250915", close="--")]) if existing else FakeGitSource({})
    if existing:
        with pytest.raises(ValueError, match="absent exact main day"):
            producer.read_current_prices(source, technical, {item["path"]: payload})
    else:
        prices, _, _ = producer.read_current_prices(source, technical, {item["path"]: payload})
        assert prices["20250915"]["2330"]["source"] == "OFFICIAL_RECOVERED_CURRENT_VERSION"


@pytest.mark.parametrize("s400,s1000,u400,u1000,expected", [
    (0.36, 0.4, 2, 2, "strong_accumulation"),
    (0.01, -1, 1, 0, "mild_accumulation"),
    (-1, 0.01, 0, 1, "mild_accumulation"),
    (0.36, 0.4, 1, 2, "mild_accumulation"),
    (0.36, 0.4, 2, 1, "mild_accumulation"),
    (0, 0, 0, 0, "neutral"),
])
def test_frozen_classifier_strong_requires_both_positive_and_two_up(frozen_selector, s400, s1000, u400, u1000, expected):
    _, classify = frozen_selector
    assert classify(4, s400, s1000, u400, u1000)[0] == expected


@pytest.mark.parametrize("enum,selected", [("mild_accumulation", True), ("strong_accumulation", True),
                                         ("neutral", False), ("distribution_warning", False),
                                         ("unrecognized", False), ("", False)])
def test_frozen_v2_enum_fallback_is_fail_closed(frozen_selector, enum, selected):
    evaluate, _ = frozen_selector
    actual = evaluate(selector_row(tdcc_accumulation_signal=enum))
    assert actual["selector_selected"] is selected
    if selected:
        assert actual["tdcc_positive_resolution"] == "recognized_enum_positive_fallback"


@pytest.mark.parametrize("phase", ["price_leading_tdcc", "overheated_after_tdcc"])
def test_frozen_forbidden_phase_cannot_be_overridden_by_positive_enum(frozen_selector, phase):
    evaluate, _ = frozen_selector
    assert evaluate(selector_row(tdcc_price_phase=phase))["selector_selected"] is False


@pytest.mark.parametrize("close,selected", [("81", True), ("80.9999", False),
                                          ("121", True), ("121.0001", False)])
def test_frozen_range_bounds_are_inclusive(frozen_selector, close, selected):
    evaluate, _ = frozen_selector
    assert evaluate(selector_row(close=close))["selector_selected"] is selected


@pytest.mark.parametrize("field,before,boundary", [("volume_ratio", "2.4999", "2.5"),
                                                ("return_5d", "7.9999", "8"),
                                                ("return_20d", "19.9999", "20")])
def test_frozen_selector_numeric_boundaries(frozen_selector, field, before, boundary):
    evaluate, _ = frozen_selector
    assert evaluate(selector_row(**{field: before}))["selector_selected"] is True
    assert evaluate(selector_row(**{field: boundary}))["selector_selected"] is False


def test_frozen_attack_exclusion_keeps_2pct_volume_and_lot_boundaries(frozen_selector):
    evaluate, _ = frozen_selector
    row = selector_row(open="100", high="103", low="99", close="102", volume_ratio="2",
                       previous_20d_high_ex_today="100", volume_ma20_lots="1000")
    actual = evaluate(row)
    assert actual["attack_already_started"] is True
    assert actual["selector_selected"] is False
    for update in (dict(close="101.9999"), dict(volume_ratio="1.9999"), dict(volume_ma20_lots="999.9999")):
        actual = evaluate(dict(row, **update))
        assert actual["attack_already_started"] is False
        assert actual["selector_selected"] is True


def test_frozen_locked_limit_attack_does_not_require_volume(frozen_selector):
    evaluate, _ = frozen_selector
    row = selector_row(open="109", high="109", low="109", close="109", previous_close="100",
                       daily_return_calc="9", previous_20d_high_ex_today="100", volume_ratio="0.1")
    assert evaluate(row)["attack_already_started"] is True


@pytest.mark.parametrize("slippage", [0, 10, 20])
def test_costs_use_exact_1000_shares_both_fees_and_sell_tax(slippage):
    actual = producer.cost_cashflows("100", "110", slippage)
    with localcontext() as context:
        context.prec = 50
        slip = Decimal(slippage) / 10000
        buy = Decimal(100000) * (1 + slip)
        sell = Decimal(110000) * (1 - slip)
        buy_fee = buy * Decimal("0.001425")
        sell_fee = sell * Decimal("0.001425")
        tax = sell * Decimal("0.003")
        assert Decimal(actual["entry_notional"]) == buy
        assert Decimal(actual["exit_notional"]) == sell
        assert Decimal(actual["buy_fee"]) == buy_fee
        assert Decimal(actual["sell_fee"]) == sell_fee
        assert Decimal(actual["sell_tax"]) == tax
        assert Decimal(actual["net_pnl"]) == sell - sell_fee - tax - buy - buy_fee
        assert Decimal(actual["net_return_pct"]) == (sell - sell_fee - tax - buy - buy_fee) / (buy + buy_fee) * 100
    assert actual["shares"] == "1000"


def test_low_notional_minimum_fees_and_caller_decimal_precision():
    expected = producer.cost_cashflows("1.23456789", "1.34567891", 10)
    with localcontext() as context:
        context.prec = 6
        actual = producer.cost_cashflows("1.23456789", "1.34567891", 10)
    assert actual == expected
    assert Decimal(actual["buy_fee"]) == Decimal(actual["sell_fee"]) == 20
    assert Decimal(actual["sell_tax"]) == Decimal("4.03299969327")


@pytest.mark.parametrize("entry,exit,slippage", [(0, 100, 0), (-1, 100, 0), (100, "NaN", 0),
                                               (100, "Infinity", 0), (100, 110, 5)])
def test_costs_reject_invalid_prices_or_new_slippage_scenarios(entry, exit, slippage):
    with pytest.raises(ValueError):
        producer.cost_cashflows(entry, exit, slippage)


def test_writer_emits_only_exact_nine_model_owned_filenames(tmp_path, monkeypatch):
    # 同一 pytest tmp_path 的 Windows 長路徑表示，不改 TEMP/TMP 或另選目錄。
    if sys.platform == "win32":
        tmp_path = Path("\\\\?\\" + str(tmp_path))
    monkeypatch.setattr(producer, "SEALED_ROOT", tmp_path / "synthetic-sealed-evidence")
    output = tmp_path / producer.DIRECTORY
    artifacts = {name: b"synthetic-only\n" for name in producer.GENERATED}
    producer.write_outputs(tmp_path, output, artifacts)
    assert {path.name for path in output.iterdir()} == producer.GENERATED
    assert len(list(output.iterdir())) == 9
    assert all(path.read_bytes() == artifacts[path.name] for path in output.iterdir())


@pytest.mark.parametrize("defect", ["missing", "extra", "escape", "nonbytes", "wrong_directory"])
def test_writer_rejects_nonexact_allowlists_before_writing(tmp_path, defect, monkeypatch):
    monkeypatch.setattr(producer, "SEALED_ROOT", tmp_path / "synthetic-sealed-evidence")
    output = tmp_path / producer.DIRECTORY
    artifacts = {name: b"synthetic-only\n" for name in producer.GENERATED}
    if defect == "missing":
        artifacts.pop(next(iter(artifacts)))
    elif defect == "extra":
        artifacts["other_model.csv"] = b"bad"
    elif defect == "escape":
        artifacts["../escape.csv"] = artifacts.pop(next(iter(artifacts)))
    elif defect == "nonbytes":
        artifacts[next(iter(artifacts))] = "not-bytes"
    else:
        output = tmp_path / "wrong-family"
    with pytest.raises(ValueError):
        producer.write_outputs(tmp_path, output, artifacts)
    assert not output.exists()


def test_writer_never_targets_sealed_evidence(tmp_path, monkeypatch):
    monkeypatch.setattr(producer, "SEALED_ROOT", tmp_path)
    with pytest.raises(ValueError, match="Sealed"):
        producer.write_outputs(tmp_path, tmp_path / producer.DIRECTORY,
                               {name: b"synthetic-only\n" for name in producer.GENERATED})
    assert not (tmp_path / producer.DIRECTORY).exists()
