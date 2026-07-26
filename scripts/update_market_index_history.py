from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    MARKET_INDEX_OHLC_PATH,
    MARKET_INDEX_PATH,
    market_index_source_provenance,
    normalize_date,
    now_text,
    reset_market_index_source_provenance,
    update_market_index_history,
)


STATUS_JSON = Path("output/latest/market_index_source_status_latest.json")
STATUS_MD = Path("output/latest/market_index_source_status_latest.md")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-date", default="")
    parser.add_argument("--target-index-code", action="append", choices=["TWSE", "TPEX"])
    parser.add_argument("--months", type=int, default=18)
    return parser.parse_args()


def parse_target_date(value: str) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if len(text) != 8 or not text.isdigit():
        raise RuntimeError("--target-date must be calendar-valid YYYYMMDD")
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError("--target-date must be calendar-valid YYYYMMDD") from exc
    return text


def dataset_state(path: Path, target_date: str) -> dict[str, object]:
    if not path.exists():
        return {"tail_by_index": {}, "future_rows": 0, "future_rows_sha256": ""}
    frame = pd.read_csv(path, dtype=str).fillna("")
    if frame.empty or "date" not in frame.columns or "index_code" not in frame.columns:
        return {"tail_by_index": {}, "future_rows": 0, "future_rows_sha256": ""}
    frame["date"] = frame["date"].map(normalize_date)
    tails = {
        code: str(part["date"].max())
        for code, part in frame[frame["date"] != ""].groupby("index_code")
    }
    future = frame[frame["date"] > target_date].sort_values(["index_code", "date"])
    future_bytes = future.to_csv(index=False, lineterminator="\n").encode("utf-8")
    return {
        "tail_by_index": tails,
        "future_rows": len(future),
        "future_rows_sha256": hashlib.sha256(future_bytes).hexdigest(),
    }


def write_status(
    target_date: str,
    df,
    before_state: dict[str, dict[str, object]],
    requested_codes: set[str],
) -> None:
    observed = {}
    for code in sorted(requested_codes):
        part = df[
            df["index_code"].astype(str).eq(code)
            & df["date"].map(normalize_date).eq(target_date)
        ]
        observed[code] = target_date if len(part) == 1 else ""
    if target_date and observed != {code: target_date for code in sorted(requested_codes)}:
        raise RuntimeError(f"market-index status cannot prove exact target rows: {observed}")
    context_max = dict(df.attrs.get("target_calculation_context_max_date_by_index", {}))
    future_rows_used = bool(
        target_date
        and (
            set(context_max) != requested_codes
            or any(str(value) > target_date for value in context_max.values())
        )
    )
    if target_date and context_max != {code: target_date for code in sorted(requested_codes)}:
        raise RuntimeError(
            "market-index runtime context cannot prove target-safe calculation: "
            f"{context_max}"
        )
    after_state = {
        MARKET_INDEX_PATH.as_posix(): dataset_state(MARKET_INDEX_PATH, target_date),
        MARKET_INDEX_OHLC_PATH.as_posix(): dataset_state(MARKET_INDEX_OHLC_PATH, target_date),
    }
    if target_date:
        for path_text, before in before_state.items():
            after = after_state[path_text]
            if before.get("future_rows_sha256") != after.get("future_rows_sha256"):
                raise RuntimeError(f"market-index target replay changed preserved future rows: {path_text}")
    payload = {
        "generated_at": now_text(),
        "mode": "reconstructed_source_tail_gap" if target_date else "latest_refresh",
        "requested_date": target_date,
        "observed_dates": observed,
        "requested_index_codes": sorted(requested_codes),
        "publication_status": "reconstructed_not_as_published" if target_date else "as_published",
        "as_published": False if target_date else True,
        "fallback_used": False,
        "future_rows_used": future_rows_used,
        "calculation_context_max_date_by_index": context_max,
        "before_state": before_state,
        "after_state": after_state,
        "future_rows_preserved": True if target_date else "not_applicable",
        "turnover_contract": {
            "TWSE": "official_historical_month_endpoint",
            "TPEX": "unavailable_from_official_historical_index_month_endpoint",
        },
        "sources": market_index_source_provenance(),
        "outputs": {
            MARKET_INDEX_PATH.as_posix(): file_sha256(MARKET_INDEX_PATH),
            MARKET_INDEX_OHLC_PATH.as_posix(): file_sha256(MARKET_INDEX_OHLC_PATH),
        },
    }
    STATUS_JSON.parent.mkdir(parents=True, exist_ok=True)
    STATUS_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    STATUS_MD.write_text(
        "\n".join(
            [
                "# Market Index Source Status",
                "",
                f"- generated_at: `{payload['generated_at']}`",
                f"- mode: `{payload['mode']}`",
                f"- requested_date: `{target_date}`",
                f"- observed_dates: `{json.dumps(observed, ensure_ascii=False, sort_keys=True)}`",
                f"- source_response_count: `{len(payload['sources'])}`",
                "- fallback_used: `False`",
                "- future_rows_used: `False`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    target_date = parse_target_date(args.target_date)
    requested_codes = set(args.target_index_code or ["TWSE", "TPEX"])
    before_state = {
        MARKET_INDEX_PATH.as_posix(): dataset_state(MARKET_INDEX_PATH, target_date),
        MARKET_INDEX_OHLC_PATH.as_posix(): dataset_state(MARKET_INDEX_OHLC_PATH, target_date),
    }
    reset_market_index_source_provenance()
    df = update_market_index_history(
        months=args.months,
        target_date=target_date,
        target_index_codes=requested_codes,
    )
    write_status(target_date, df, before_state, requested_codes)
    print(f"Saved market index history rows={len(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
