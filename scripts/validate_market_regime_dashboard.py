from __future__ import annotations

from pathlib import Path
import json
import sys

import pandas as pd


REQUIRED_FILES = [
    Path("data/market_index_history.csv"),
    Path("output/latest/market_benchmark_latest.csv"),
    Path("output/latest/futures_options_indicators_latest.csv"),
    Path("output/latest/futures_options_source_status_latest.json"),
    Path("output/latest/market_regime_latest.csv"),
    Path("output/latest/market_risk_dashboard_latest.md"),
    Path("output/latest/market_risk_dashboard_latest.pdf"),
    Path("docs/latest/market_risk_dashboard_latest.pdf"),
    Path("output/latest/charts/market_regime/market_index_technical_6m.png"),
    Path("output/latest/charts/market_regime/risk_indicators_6m.png"),
    Path("output/latest/charts/market_regime/foreign_futures_net_oi_6m.png"),
    Path("output/latest/charts/market_regime/retail_mtx_proxy_6m.png"),
]

REQUIRED_CHART_FILES = [
    Path("output/latest/charts/market_regime/market_index_technical_6m.png"),
    Path("output/latest/charts/market_regime/risk_indicators_6m.png"),
    Path("output/latest/charts/market_regime/foreign_futures_net_oi_6m.png"),
    Path("output/latest/charts/market_regime/retail_mtx_proxy_6m.png"),
]

REQUIRED_INDICATOR_COLUMNS = [
    "date",
    "foreign_tx_futures_net_oi",
    "retail_mtx_net_oi_proxy",
    "retail_mtx_proxy_method",
    "put_call_oi_ratio_pct",
    "taiwan_vix",
    "source_status",
]

REQUIRED_REGIME_COLUMNS = [
    "date",
    "market_regime",
    "risk_level",
    "risk_score",
    "twse_close",
    "tpex_close",
    "taiwan_vix",
    "put_call_oi_ratio_pct",
    "foreign_tx_futures_net_oi",
    "retail_mtx_net_oi_proxy",
    "retail_mtx_state",
]


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str)
    except Exception as exc:
        raise RuntimeError(f"failed to read {path}: {exc}") from exc


def main() -> int:
    for path in REQUIRED_FILES:
        if not path.exists():
            return fail(f"missing required file: {path}")
        if path.suffix.lower() == ".pdf" and path.stat().st_size < 20000:
            return fail(f"PDF too small: {path} size={path.stat().st_size}")
        if path in REQUIRED_CHART_FILES and path.stat().st_size < 5000:
            return fail(f"chart image too small or blank: {path} size={path.stat().st_size}")

    indicators = read_csv(Path("output/latest/futures_options_indicators_latest.csv"))
    regime = read_csv(Path("output/latest/market_regime_latest.csv"))
    for col in REQUIRED_INDICATOR_COLUMNS:
        if col not in indicators.columns:
            return fail(f"missing indicator column: {col}")
    for col in REQUIRED_REGIME_COLUMNS:
        if col not in regime.columns:
            return fail(f"missing regime column: {col}")
    if indicators.empty:
        return fail("futures/options indicator file is empty")
    if regime.empty:
        return fail("market regime file is empty")

    status = json.loads(Path("output/latest/futures_options_source_status_latest.json").read_text(encoding="utf-8"))
    if not status.get("sources"):
        return fail("source status has no source details")

    md = Path("output/latest/market_risk_dashboard_latest.md").read_text(encoding="utf-8")
    for marker in [
        "Market Risk Dashboard",
        "Market Index Regime",
        "Futures / Options Positioning",
        "Six-Month Technical Charts",
        "Technical / Pattern Notes",
        "Retail Mini-TAIEX Futures Proxy",
        "Usage Boundary",
    ]:
        if marker not in md:
            return fail(f"dashboard missing marker: {marker}")

    print("Market regime dashboard validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
