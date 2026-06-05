from __future__ import annotations

import shutil
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    load_market_index_history,
    main_price_date_from_freshness,
    market_row_on_or_before,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
)


MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
FUTURES_OPTIONS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
PACKET_MD = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"
DOCS_PACKET_MD = DOCS_LATEST_DIR / PACKET_MD.name


def _latest_row_at_or_before(df: pd.DataFrame, date: str) -> pd.Series:
    if df.empty or "date" not in df.columns:
        return pd.Series(dtype=object)
    work = df.copy()
    work["date"] = work["date"].map(normalize_date)
    work = work[work["date"].le(date)].sort_values("date")
    if work.empty:
        return pd.Series(dtype=object)
    return work.iloc[-1]


def _fmt(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if pd.isna(num):
        text = safe_str(value)
        return text if text else "-"
    if abs(float(num)) >= 1000:
        return f"{float(num):,.0f}"
    return f"{float(num):.{digits}f}".rstrip("0").rstrip(".")


def _fmt_pct(value: Any) -> str:
    text = _fmt(value)
    return "-" if text == "-" else f"{text}%"


def _bool_text(value: Any) -> str:
    text = safe_str(value).lower()
    if text in {"true", "1", "yes", "y"}:
        return "True"
    if text in {"false", "0", "no", "n"}:
        return "False"
    return safe_str(value) or "-"


def _index_row(index_history: pd.DataFrame, index_code: str, main_date: str) -> pd.Series:
    row = market_row_on_or_before(index_history, index_code, main_date)
    return row if row is not None else pd.Series(dtype=object)


def _date_note(name: str, source_date: str, main_date: str) -> str:
    if not source_date:
        return f"- {name}: missing"
    if source_date == main_date:
        return f"- {name}: {source_date}"
    return f"- {name}: {source_date} (latest available at or before main_price_date={main_date})"


def build() -> str:
    main_date = normalize_date(main_price_date_from_freshness())
    if not main_date:
        raise RuntimeError("Cannot build market timing packet: main_price_date is missing.")

    market_regime = read_csv(MARKET_REGIME_CSV, dtype=str)
    futures = read_csv(FUTURES_OPTIONS_CSV, dtype=str)
    index_history = load_market_index_history(update_if_missing=True)

    regime_row = _latest_row_at_or_before(market_regime, main_date)
    futures_row = _latest_row_at_or_before(futures, main_date)
    twse = _index_row(index_history, "TWSE", main_date)
    tpex = _index_row(index_history, "TPEX", main_date)

    regime_date = normalize_date(regime_row.get("date", "")) if not regime_row.empty else ""
    futures_date = normalize_date(futures_row.get("date", "")) if not futures_row.empty else ""
    twse_date = normalize_date(twse.get("date", "")) if not twse.empty else ""
    tpex_date = normalize_date(tpex.get("date", "")) if not tpex.empty else ""

    status_parts: list[str] = []
    for label, source_date in [
        ("market_regime", regime_date),
        ("futures_options", futures_date),
        ("TWSE", twse_date),
        ("TPEx", tpex_date),
    ]:
        if source_date and source_date != main_date:
            status_parts.append(f"{label}_date={source_date}")
        if not source_date:
            status_parts.append(f"{label}_missing")
    packet_status = "ready" if not status_parts else "partial_market_context"

    lines = [
        "# MARKET TIMING CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- main_price_date: {main_date}",
        f"- packet_source: daily_market_regime_dashboard",
        f"- packet_status: {packet_status}",
        f"- packet_status_note: {'; '.join(status_parts) if status_parts else 'all source rows aligned with main_price_date'}",
        "- tuning_status: not_ready",
        "",
        "## Source Dates",
        _date_note("market_regime_latest.csv", regime_date, main_date),
        _date_note("futures_options_indicators_latest.csv", futures_date, main_date),
        _date_note("TWSE market index", twse_date, main_date),
        _date_note("TPEx market index", tpex_date, main_date),
        "",
        "## Current Market Technical State",
        "| index_id | trade_date | close | ret_5d | ret_20d | above_ma20 | above_ma60 | market_regime | risk_level |",
        "| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- |",
        (
            f"| TWSE | {twse_date or '-'} | {_fmt(twse.get('close', regime_row.get('twse_close', '')))} "
            f"| {_fmt_pct(twse.get('return_5d', regime_row.get('twse_return_5d', '')))} "
            f"| {_fmt_pct(twse.get('return_20d', regime_row.get('twse_return_20d', '')))} "
            f"| {_bool_text(twse.get('above_ma20', regime_row.get('twse_above_ma20', '')))} "
            f"| {_bool_text(twse.get('above_ma60', regime_row.get('twse_above_ma60', '')))} "
            f"| {safe_str(regime_row.get('market_regime', '')) or '-'} "
            f"| {safe_str(regime_row.get('risk_level', '')) or '-'} |"
        ),
        (
            f"| TPEx | {tpex_date or '-'} | {_fmt(tpex.get('close', regime_row.get('tpex_close', '')))} "
            f"| {_fmt_pct(tpex.get('return_5d', regime_row.get('tpex_return_5d', '')))} "
            f"| {_fmt_pct(tpex.get('return_20d', regime_row.get('tpex_return_20d', '')))} "
            f"| {_bool_text(tpex.get('above_ma20', regime_row.get('tpex_above_ma20', '')))} "
            f"| {_bool_text(tpex.get('above_ma60', regime_row.get('tpex_above_ma60', '')))} "
            f"| {safe_str(regime_row.get('market_regime', '')) or '-'} "
            f"| {safe_str(regime_row.get('risk_level', '')) or '-'} |"
        ),
        "",
        "## Futures Options Context",
        "| item | value | note |",
        "| --- | ---: | --- |",
        f"| foreign_tx_futures_net_oi | {_fmt(futures_row.get('foreign_tx_futures_net_oi', ''))} | TX futures direction anchor |",
        f"| foreign_futures_net_oi | {_fmt(futures_row.get('foreign_futures_net_oi', ''))} | broad futures exposure only, not TX direction |",
        f"| put_call_oi_ratio_pct | {_fmt_pct(futures_row.get('put_call_oi_ratio_pct', ''))} | hedging background only |",
        f"| taiwan_vix | {_fmt(futures_row.get('taiwan_vix', ''))} | volatility / hedging context only |",
        f"| retail_mtx_net_oi_proxy | {_fmt(futures_row.get('retail_mtx_net_oi_proxy', ''))} | contrarian sentiment proxy only |",
        f"| retail_mtx_proxy_method | {safe_str(futures_row.get('retail_mtx_proxy_method', '')) or '-'} | source method |",
        "",
        "## Usage Boundary",
        "- This packet is daily market context only; it is not a stock recommendation list.",
        "- VIX, Put/Call, retail MTX, and foreign futures fields must be cross-checked with TWSE / TPEx position and market_regime.",
        "- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.",
        "- Research/backtest scripts must not overwrite this daily packet in the daily pipeline.",
        "",
    ]

    PACKET_MD.parent.mkdir(parents=True, exist_ok=True)
    PACKET_MD.write_text("\n".join(lines), encoding="utf-8")
    DOCS_PACKET_MD.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PACKET_MD, DOCS_PACKET_MD)
    print(f"Saved: {PACKET_MD}")
    print(f"Saved: {DOCS_PACKET_MD}")
    return main_date


def main() -> None:
    build()


if __name__ == "__main__":
    main()
