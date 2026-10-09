"""Independently verify the frozen pullback known-share-unit supplement."""
from __future__ import annotations

import argparse
import base64
import csv
from datetime import datetime
from decimal import Decimal
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
import statistics
import subprocess
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "pullback_short_reclaim"
OWNER_ID = "pullback_short_reclaim_share_unit_reconciliation"
VERSION = "pullback_short_reclaim_share_unit_reconciliation_v1"
CONFIG_REL = "config/pullback_short_reclaim_share_unit_reconciliation_v1.json"
SOURCE_COMMIT = "50baf29c849e5ca54a54e0f59800cef3fbe410c0"
PRICE_COMMIT = "12b817cbac0e198ac614a542e5cbf057959ed4a5"
SOURCE_ARTIFACTS = {
    "events": {"path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_events_latest.csv", "raw_sha256": "f134c54fd2c854fe9397de525857ab58c5ca42867479f58acb5323e97838ed5b"},
    "summary": {"path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_summary_latest.csv", "raw_sha256": "d408734460e4760a024e165fd523cef6f770ef6ad9b56e5f43aa4db0cf82c742"},
    "anomalies": {"path": "output/latest/research_backtest/pullback_short_reclaim_published_signal_replay_anomaly_candidates_latest.csv", "raw_sha256": "7fd2e3e0ad6a00526f612a1df58de265834bf7c317fa2ba10af28f7a8c71a199"},
    "snapshot": {"path": "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_20260713.csv", "raw_sha256": "bdc85cb76e4215785b3c7a72b7934b8655d5b824f1a8f2654f488891e851d564"},
}
PRICE_SOURCE = {"commit": PRICE_COMMIT, "path": "data/stock_price_history/5904.csv", "raw_sha256": "0a2318bd5fc59c4f7fccebe36f54af1b9706977b022a42bc89a7856e67129b7f"}
OFFICIAL_URL = "https://www.tpex.org.tw/storage/eb_data/11507/11500046541.html"
RECEIPT_SHA256 = "5a8f94d8d4707589b59920e3791bf303eab4a966f0bc47ae3f04a503097338ee"
ACTION_FACTS = {"stock_id": "5904", "effective_date": "20260810", "share_factor": 10, "suspension_start": "20260730", "suspension_end": "20260807", "official_url": OFFICIAL_URL, "receipt_sha256": RECEIPT_SHA256}
CONFIG_LIMITATIONS = {
    "scope": "single_known_share_unit_price_supplement_not_corrected_primary",
    "first_publication_pit_verified": False, "full_corporate_action_coverage": False,
    "cash_flow_status": "not_modelled_not_total_return", "formal_model_use_allowed": False,
    "promotion_allowed": False, "old_research_preserved": True,
    "anomaly_disposition": "unresolved_anomaly_candidate",
    "horizon_basis": "original_available_stock_price_row_count_not_market_calendar",
    "user_authorization_ref": "user_requested_remaining_model_repairs_20261009",
}
PREFIX = "output/research/pullback_short_reclaim/" + VERSION + "_"
OUTPUTS = {"detail": PREFIX + "detail.csv", "summary": PREFIX + "summary.csv", "manifest": PREFIX + "manifest.json"}
HORIZONS = (5, 10, 20)
RESULT_STATUS = "partial_known_share_unit_price_proxy_not_corrected_primary"
DETAIL_COLUMNS = tuple(name for h in HORIZONS for name in (f"d{h}_share_factor", f"d{h}_share_unit_return_pct")) + (
    "share_unit_reconciliation_version", "unit_adjustment_status", "cash_flow_status",
    "share_unit_result_status", "first_publication_pit_proven", "total_return_complete",
    "numerical_disposition_changed", "known_share_action_evidence_url",
)
SUMMARY_COLUMNS = tuple("partial_known_share_unit_" + key for key in (
    "mature_count", "affected_count", "win_count", "neutral_count", "failure_count",
    "win_rate_pct", "average_return_pct", "median_return_pct", "result_status",
)) + ("cash_flow_status", "first_publication_pit_proven", "total_return_complete", "numerical_disposition_changed")
LIMITATIONS = {
    "formal_use_allowed": False, "trade_eligible": False, "promotion_evidence_allowed": False,
    "first_publication_pit_proven": False, "total_return_complete": False,
    "numerical_disposition_changed": False, "cash_flow_status": "not_modelled_not_total_return",
    "result_status": RESULT_STATUS, "holding_basis": "original_individual_price_row_count_unchanged",
    "other_corporate_action_coverage": "not_verified",
}
TARGET_EVENT_ID = "df9a30670ce02e662c16ea4cb0d08465f838b65b2f053f794cebe59c581045b5"
TARGET_ROWS = {
    "entry": ("20260714", "open", "665", "17a4e5ce9fc48cb79371bf09581a2f29323a0e4196b5b0529135714f3144c49c"),
    "d5": ("20260720", "close", "611", "6e3b52a84a2795a37a5f156a5b814287cec5aa173c1ff0c5b49b6cea427eb24f"),
    "d10": ("20260727", "close", "668", "1a83c8d47bf5f16f5fcaed062748ebff08b7d1c81fc1ca1edeb3b64757c8c44d"),
    "d20": ("20260819", "close", "78", "1e14aafa1aacf7b70e96f4a4d6602b6e571a0f397283847a863c4b7fb7f884f9"),
}


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _csv(raw: bytes) -> pd.DataFrame:
    header = next(csv.reader(io.StringIO(raw.decode("utf-8-sig"))))
    if len(header) != len(set(header)):
        raise ValueError("duplicate CSV columns")
    return pd.read_csv(io.BytesIO(raw), dtype=str, keep_default_na=False)


def _git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "--no-replace-objects", "-C", str(root), *args], check=True,
                          capture_output=True, timeout=60).stdout


def _read_blob(root: Path, commit: str, path: str, digest: str) -> bytes:
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("source commit is not immutable")
    if _git(root, "rev-parse", "--verify", commit + "^{commit}").decode().strip() != commit:
        raise ValueError("source commit mismatch")
    entries = [entry for entry in _git(root, "ls-tree", "-z", commit, "--", path).split(b"\0") if entry]
    if len(entries) != 1:
        raise ValueError("frozen source missing: " + path)
    metadata, actual_path = entries[0].split(b"\t", 1)
    mode, kind, oid = metadata.decode("ascii").split()
    if mode != "100644" or kind != "blob" or actual_path.decode("utf-8") != path:
        raise ValueError("frozen source is not the exact regular blob")
    raw = _git(root, "cat-file", "blob", oid)
    if _sha(raw) != digest:
        raise ValueError("frozen source raw SHA mismatch: " + path)
    return raw


def load_sources(root: Path) -> dict[str, bytes]:
    sources = {key: _read_blob(root, SOURCE_COMMIT, spec["path"], spec["raw_sha256"])
               for key, spec in SOURCE_ARTIFACTS.items()}
    sources["price"] = _read_blob(root, PRICE_COMMIT, PRICE_SOURCE["path"], PRICE_SOURCE["raw_sha256"])
    return sources


class _NoticeText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"style", "script"}:
            self.hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"style", "script"}:
            self.hidden -= 1

    def handle_data(self, text: str) -> None:
        if not self.hidden:
            self.parts.append(text)


def verify_config(config: dict[str, Any]) -> None:
    expected = {"artifact_version": VERSION, "model_id": MODEL_ID, "source_commit": SOURCE_COMMIT,
                "source_artifacts": SOURCE_ARTIFACTS, "price_source": PRICE_SOURCE,
                "limitations": CONFIG_LIMITATIONS}
    if set(config) != {*expected, "action"} or any(_canonical(config.get(k)) != _canonical(v) for k, v in expected.items()):
        raise ValueError("frozen config identity/source/boundary mismatch")
    action = config["action"]
    if set(action) != {*ACTION_FACTS, "receipt_body_base64", "retrieved_at"} or any(_canonical(action.get(k)) != _canonical(v) for k, v in ACTION_FACTS.items()):
        raise ValueError("official action hard anchor mismatch")
    raw = base64.b64decode(action["receipt_body_base64"], validate=True)
    if _sha(raw) != RECEIPT_SHA256:
        raise ValueError("official receipt immutable SHA mismatch")
    retrieved = datetime.fromisoformat(action["retrieved_at"])
    if retrieved.tzinfo is None or retrieved.strftime("%Y%m%d") < "20260714":
        raise ValueError("official receipt retrieval timestamp invalid")
    parser = _NoticeText()
    parser.feed(raw.decode("utf-8"))
    text = re.sub(r"\s+", "", "".join(parser.parts))
    for token in ("115年7月14日", "證櫃監字第11500046541號", "寶雅國際股份有限公司",
                  "5904", "股票面額由每股10元變更為每股1元", "每1股換發新股票10股",
                  "暫停股票櫃檯買賣日期：115年7月30日至115年8月7日",
                  "公司新股票開始櫃檯買賣日期：115年8月10日"):
        if token not in text:
            raise ValueError("official receipt fact missing: " + token)


def _row_hash(row: dict[str, str]) -> str:
    return _sha(_canonical({key: value.strip() for key, value in row.items()}))


def verify_frozen_lineage(frames: dict[str, pd.DataFrame]) -> None:
    old = frames["events"]
    canonical = old[old.primary_metric_included.eq("True")]
    if len(old) != 3020 or len(canonical) != 2992 or canonical.signal_event_id.nunique() != 2992:
        raise ValueError("frozen population is not 3020 rows/2992 canonical events")
    target = old[old.signal_event_id.eq(TARGET_EVENT_ID)]
    if len(target) != 1 or set(old[old.stock_id.eq("5904")].signal_event_id) != {TARGET_EVENT_ID}:
        raise ValueError("5904 target event identity mismatch")
    event = target.iloc[0]
    snapshot = frames["snapshot"]
    if len(snapshot) != 434 or len(snapshot.columns) != 125 or len(snapshot[snapshot.model_id.eq(MODEL_ID)]) != 102:
        raise ValueError("target published snapshot shape mismatch")
    published = snapshot.iloc[344].to_dict()  # CSV physical row 346, after one header.
    if (published["stock_id"] != "5904" or published["signal_date"] != "20260713"
            or published["model_id"] != MODEL_ID or _row_hash(published) != event.source_row_sha256
            or event.source_row_sha256 != "07aa86fd2592ae80a7525dfb92881ff8db94cba50f09ff13308b740c9a215515"):
        raise ValueError("target published source row identity/hash mismatch")
    prices = frames["price"]
    if prices.date.duplicated().any() or prices.date.between("20260730", "20260807").any():
        raise ValueError("price identity or official suspension continuity mismatch")
    future = prices[prices.date.gt("20260713")].sort_values("date").reset_index(drop=True)
    if "20260810" not in set(future.date) or event.price_source_sha256 != PRICE_SOURCE["raw_sha256"]:
        raise ValueError("resumption date/original price source mismatch")
    for label, (date, column, value, row_sha) in TARGET_ROWS.items():
        horizon_index = 0 if label == "entry" else int(label[1:]) - 1
        price = future.iloc[horizon_index].to_dict()
        price_field = "entry_open_price" if label == "entry" else label + "_exit_close_price"
        date_field = "entry_date" if label == "entry" else label + "_exit_date"
        hash_field = "entry_price_row_sha256" if label == "entry" else label + "_exit_price_row_sha256"
        if (price["date"] != date or Decimal(price[column]) != Decimal(value)
                or _row_hash(price) != row_sha or event[hash_field] != row_sha
                or event[date_field] != date or Decimal(event[price_field]) != Decimal(value)):
            raise ValueError("original individual-stock-row price/date/hash mismatch: " + label)
    anomalies = frames["anomalies"]
    if (len(anomalies) != 1 or anomalies.iloc[0].signal_event_id != TARGET_EVENT_ID
            or anomalies.iloc[0].final_disposition != "unresolved_anomaly_candidate"
            or anomalies.iloc[0].retained_in_primary_metrics != "True"):
        raise ValueError("frozen unresolved anomaly population changed")


def _number(value: str) -> Decimal:
    result = Decimal(value)
    if not result.is_finite():
        raise ValueError("non-finite price/return")
    return result


def _assert_number(actual: str, expected: Decimal, field: str) -> None:
    if abs(_number(actual) - expected) > Decimal("0.00000051"):
        raise ValueError("independent numerical mismatch: " + field)


def verify_detail(frozen: pd.DataFrame, actual: pd.DataFrame) -> None:
    if list(actual.columns) != [*frozen.columns, *DETAIL_COLUMNS] or len(actual) != len(frozen):
        raise ValueError("detail schema/row count mismatch")
    if not actual.loc[:, frozen.columns].equals(frozen):
        raise ValueError("frozen detail cells/order changed")
    crossings = {h: 0 for h in HORIZONS}
    for old, row in zip(frozen.to_dict("records"), actual.to_dict("records")):
        adjusted = False
        for h in HORIZONS:
            prefix = f"d{h}"
            crosses = (old["stock_id"] == "5904" and old[prefix + "_maturity_status"] == "mature"
                       and old["entry_date"] < "20260810" <= old[prefix + "_exit_date"])
            if row[prefix + "_share_factor"] != ("10" if crosses else "1"):
                raise ValueError("share factor/date boundary mismatch: " + prefix)
            if crosses:
                entry, exit_price = _number(old["entry_open_price"]), _number(old[prefix + "_exit_close_price"])
                if entry <= 0 or exit_price <= 0:
                    raise ValueError("non-positive target price")
                _assert_number(row[prefix + "_share_unit_return_pct"], (exit_price * 10 / entry - 1) * 100, prefix)
                crossings[h] += 1
                adjusted = True
            elif row[prefix + "_share_unit_return_pct"] != old[prefix + "_return_pct"]:
                raise ValueError("unaffected/immature outcome changed: " + prefix)
        expected = {
            "share_unit_reconciliation_version": VERSION,
            "unit_adjustment_status": "known_split_applied_partial_coverage" if adjusted else "no_known_split_applied_coverage_not_verified",
            "cash_flow_status": "not_modelled_not_total_return", "share_unit_result_status": RESULT_STATUS,
            "first_publication_pit_proven": "False", "total_return_complete": "False", "numerical_disposition_changed": "False",
            "known_share_action_evidence_url": OFFICIAL_URL if adjusted else "",
        }
        if any(row[k] != v for k, v in expected.items()):
            raise ValueError("detail interpretation/boundary mismatch")
    if crossings != {5: 0, 10: 0, 20: 1}:
        raise ValueError("unexpected affected horizon population")


def verify_summary(frozen: pd.DataFrame, actual: pd.DataFrame, detail: pd.DataFrame) -> None:
    if list(actual.columns) != [*frozen.columns, *SUMMARY_COLUMNS] or len(actual) != 3:
        raise ValueError("summary schema/row count mismatch")
    if not actual.loc[:, frozen.columns].equals(frozen):
        raise ValueError("frozen summary cells/order changed")
    for row in actual.to_dict("records"):
        prefix = "d" + row["horizon"].split("+")[1]
        selected = detail[detail.primary_metric_included.eq("True") & detail[prefix + "_maturity_status"].eq("mature")]
        values = [_number(value) for value in selected[prefix + "_share_unit_return_pct"]]
        n = len(values)
        counts = {"mature_count": n, "affected_count": sum(selected[prefix + "_share_factor"].eq("10")),
                  "win_count": sum(x > 0 for x in values), "neutral_count": sum(x == 0 for x in values), "failure_count": sum(x < 0 for x in values)}
        for field, number in counts.items():
            if row["partial_known_share_unit_" + field] != str(number):
                raise ValueError("supplement summary population/count mismatch: " + field)
        numbers = {"win_rate_pct": Decimal(counts["win_count"]) * 100 / n,
                   "average_return_pct": sum(values) / n, "median_return_pct": statistics.median(values)}
        for field, value in numbers.items():
            _assert_number(row["partial_known_share_unit_" + field], value, field)
        text = {"partial_known_share_unit_result_status": RESULT_STATUS, "cash_flow_status": "not_modelled_not_total_return",
                "first_publication_pit_proven": "False", "total_return_complete": "False", "numerical_disposition_changed": "False"}
        if any(row[k] != v for k, v in text.items()):
            raise ValueError("supplement summary unsupported formal/total-return claim")


def validate_bundle(root: Path, detail: pd.DataFrame, summary: pd.DataFrame, manifest: dict[str, Any],
                    *, config: dict[str, Any] | None = None, sources: dict[str, bytes] | None = None) -> dict[str, Any]:
    config = config if config is not None else json.loads((root / CONFIG_REL).read_text(encoding="utf-8-sig"))
    verify_config(config)
    sources = sources if sources is not None else load_sources(root)
    expected_hashes = {**{k: v["raw_sha256"] for k, v in SOURCE_ARTIFACTS.items()}, "price": PRICE_SOURCE["raw_sha256"]}
    if {k: _sha(v) for k, v in sources.items()} != expected_hashes:
        raise ValueError("immutable input raw SHA mismatch")
    frames = {key: _csv(raw) for key, raw in sources.items()}
    verify_frozen_lineage(frames)
    verify_detail(frames["events"], detail)
    verify_summary(frames["summary"], summary, detail)
    expected = {
        "artifact_version": VERSION, "model_id": MODEL_ID, "owner_id": OWNER_ID,
        "source_commit": SOURCE_COMMIT, "source_artifacts": SOURCE_ARTIFACTS,
        "price_source": PRICE_SOURCE, "action": config["action"], "config_canonical_sha256": _sha(_canonical(config)),
        "source_row_count": 3020, "unique_signal_event_count": 2992, "source_anomaly_count": 1,
        "old_columns_and_row_order_unchanged": True, "original_primary_metrics_and_unresolved_dispositions_retained": True,
        "output_sha256": {OUTPUTS["detail"]: _sha(detail.to_csv(index=False, lineterminator="\n").encode("utf-8")),
                          OUTPUTS["summary"]: _sha(summary.to_csv(index=False, lineterminator="\n").encode("utf-8"))},
        **LIMITATIONS,
    }
    if _canonical(manifest) != _canonical(expected):
        raise ValueError("manifest identity/source/output SHA/boundary mismatch")
    return {"source_rows": 3020, "unique_signal_events": 2992, "known_action_affected_rows": 1,
            "unresolved_anomalies_retained": 1, "formal_use_allowed": False, "total_return_complete": False}


def validate(root: Path = ROOT) -> dict[str, Any]:
    raw = {key: (root / path).read_bytes() for key, path in OUTPUTS.items()}
    manifest = json.loads(raw["manifest"])
    if raw["manifest"] != _canonical(manifest) + b"\n":
        raise ValueError("manifest physical serialization is not canonical")
    if manifest.get("output_sha256") != {OUTPUTS[k]: _sha(raw[k]) for k in ("detail", "summary")}:
        raise ValueError("physical output byte SHA mismatch")
    return validate_bundle(root, _csv(raw["detail"]), _csv(raw["summary"]), manifest)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    print(json.dumps(validate(args.repo_root), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
