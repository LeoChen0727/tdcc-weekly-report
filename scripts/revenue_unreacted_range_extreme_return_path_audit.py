from __future__ import annotations

import hashlib
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_extreme_return_path_audit"
ARTIFACT_VERSION = "extreme_return_path_raw_price_v1_20260712"
EXTREME_ABS_RETURN_PCT = 80.0
MARKET_LIMIT_AUDIT_THRESHOLD_PCT = 11.0

LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
RAW_PRICE_DIR = ROOT / "data/daily_price"
COMPANY_CALENDAR = ROOT / "data/company_calendar/company_event_calendar.csv"

CORPORATE_ACTION_EVENT_TYPES = {
    "capital_reduction",
    "ex_dividend",
    "ex_right",
    "reverse_split",
    "stock_split",
    "suspension",
    "resumption",
}

COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "episode_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "entry_open",
    "exit_date",
    "exit_close",
    "realized_return_pct",
    "extreme_threshold_abs_pct",
    "price_path_trading_rows",
    "raw_source_rows_expected",
    "raw_source_rows_matched",
    "entry_open_raw_match",
    "exit_close_raw_match",
    "all_ohlc_raw_match",
    "missing_raw_dates",
    "path_start_previous_close",
    "max_abs_daily_price_move_pct",
    "market_limit_violation_count",
    "limit_up_like_day_count",
    "limit_down_like_day_count",
    "corporate_action_event_count_in_window",
    "corporate_action_event_types_in_window",
    "company_calendar_coverage_status",
    "raw_price_source_sha256",
    "price_path_classification",
    "impossible_return_flag",
    "decision_basis_handling",
    "sensitivity_basis_handling",
    "production_change",
    "promotion_readiness",
]


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _raw_price_row(stock_id: str, date: str) -> tuple[pd.Series | None, Path]:
    path = RAW_PRICE_DIR / f"{date}.csv"
    if not path.is_file():
        return None, path
    raw = pd.read_csv(path, dtype={"ticker": str, "stock_id": str}, low_memory=False)
    id_column = "stock_id" if "stock_id" in raw.columns else "ticker" if "ticker" in raw.columns else ""
    if not id_column:
        raise RuntimeError(f"raw daily price file lacks stock_id/ticker: {path}")
    rows = raw[raw[id_column].astype(str).str.zfill(4).eq(stock_id)]
    if len(rows) != 1:
        return None, path
    return rows.iloc[0], path


def _calendar_events(stock_id: str, entry_date: str, exit_date: str) -> tuple[int, str]:
    if not COMPANY_CALENDAR.is_file():
        return 0, ""
    calendar = pd.read_csv(COMPANY_CALENDAR, dtype={"stock_id": str}, low_memory=False)
    dates = calendar["event_date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
    event_types = calendar["event_type"].astype(str).str.strip()
    mask = (
        calendar["stock_id"].astype(str).str.zfill(4).eq(stock_id)
        & dates.between(entry_date, exit_date)
        & event_types.isin(CORPORATE_ACTION_EVENT_TYPES)
    )
    matched = sorted(set(event_types[mask]))
    return int(mask.sum()), ";".join(matched)


def _target_episodes(detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "episode_key",
        "stock_id",
        "signal_date",
        "confirmation_date",
        "entry_date",
        "entry_price",
        "exit_date",
        "exit_price",
        "realized_return_pct",
        "decision_basis",
        "sensitivity_basis",
        "feature_time_basis",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise RuntimeError(f"extreme return source detail missing columns: {missing}")
    realized = pd.to_numeric(detail["realized_return_pct"], errors="coerce")
    mask = (
        _boolish(detail["decision_basis"])
        & ~_boolish(detail["sensitivity_basis"])
        & detail["feature_time_basis"].astype(str).eq("signal_date_close")
        & realized.abs().ge(EXTREME_ABS_RETURN_PCT)
    )
    return detail.loc[mask].drop_duplicates("episode_key").sort_values(
        ["realized_return_pct", "stock_id"], ascending=[False, True]
    )


def build_extreme_return_path_audit(detail: pd.DataFrame) -> pd.DataFrame:
    generated_at = _now_text()
    rows: list[dict[str, object]] = []
    for episode in _target_episodes(detail).itertuples(index=False):
        stock_id = str(episode.stock_id).zfill(4)
        entry_date = str(episode.entry_date)
        exit_date = str(episode.exit_date)
        history_path = PRICE_HISTORY_DIR / f"{stock_id}.csv"
        if not history_path.is_file():
            raise RuntimeError(f"missing stock price history for extreme audit: {history_path}")
        history = pd.read_csv(history_path, dtype={"stock_id": str, "date": str}, low_memory=False)
        history["date"] = history["date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        history = history.sort_values("date").reset_index(drop=True)
        path_rows = history[history["date"].between(entry_date, exit_date)].copy()
        if path_rows.empty:
            raise RuntimeError(f"empty price path for extreme audit: {episode.episode_key}")
        entry_positions = history.index[history["date"].eq(entry_date)].tolist()
        if len(entry_positions) != 1:
            raise RuntimeError(f"entry date is not unique in price history: {episode.episode_key}")
        entry_position = entry_positions[0]
        prior_close = (
            float(pd.to_numeric(history.loc[entry_position - 1, "close"], errors="coerce"))
            if entry_position > 0
            else float("nan")
        )

        raw_match_count = 0
        all_ohlc_match = True
        missing_raw_dates: list[str] = []
        raw_hashes: list[str] = []
        entry_open_raw_match = False
        exit_close_raw_match = False
        for path_row in path_rows.itertuples(index=False):
            date = str(path_row.date)
            raw_row, raw_path = _raw_price_row(stock_id, date)
            if raw_row is None:
                missing_raw_dates.append(date)
                all_ohlc_match = False
                continue
            raw_hashes.append(f"{date}:{_sha256(raw_path)}")
            comparisons = []
            for history_column, raw_column in (("open", "open"), ("high", "high"), ("low", "low"), ("close", "close")):
                left = float(pd.to_numeric(getattr(path_row, history_column), errors="coerce"))
                right = float(pd.to_numeric(raw_row[raw_column], errors="coerce"))
                comparisons.append(abs(left - right) <= 1e-8)
            row_match = all(comparisons)
            raw_match_count += int(row_match)
            all_ohlc_match = all_ohlc_match and row_match
            if date == entry_date:
                entry_open_raw_match = (
                    abs(float(path_row.open) - float(episode.entry_price)) <= 1e-8 and comparisons[0]
                )
            if date == exit_date:
                exit_close_raw_match = (
                    abs(float(path_row.close) - float(episode.exit_price)) <= 1e-8 and comparisons[3]
                )

        previous_close = path_rows["close"].shift(1)
        previous_close.iloc[0] = prior_close
        move_columns = []
        for price_column in ("open", "high", "low", "close"):
            price = pd.to_numeric(path_rows[price_column], errors="coerce")
            move_columns.append((price / previous_close - 1.0) * 100.0)
        moves = pd.concat(move_columns, axis=1)
        max_move_by_day = moves.abs().max(axis=1)
        close_moves = moves.iloc[:, 3]
        violation_count = int(max_move_by_day.gt(MARKET_LIMIT_AUDIT_THRESHOLD_PCT).sum())
        calendar_event_count, calendar_event_types = _calendar_events(stock_id, entry_date, exit_date)
        impossible = bool(
            missing_raw_dates
            or not all_ohlc_match
            or not entry_open_raw_match
            or not exit_close_raw_match
            or violation_count > 0
        )
        raw_source_sha = hashlib.sha256("\n".join(raw_hashes).encode("utf-8")).hexdigest()
        stock_names = path_rows["stock_name"].dropna().astype(str)
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "episode_key": str(episode.episode_key),
                "stock_id": stock_id,
                "stock_name": stock_names.iloc[-1] if not stock_names.empty else "",
                "signal_date": str(episode.signal_date),
                "confirmation_date": str(episode.confirmation_date),
                "entry_date": entry_date,
                "entry_open": round(float(episode.entry_price), 4),
                "exit_date": exit_date,
                "exit_close": round(float(episode.exit_price), 4),
                "realized_return_pct": round(float(episode.realized_return_pct), 4),
                "extreme_threshold_abs_pct": EXTREME_ABS_RETURN_PCT,
                "price_path_trading_rows": int(len(path_rows)),
                "raw_source_rows_expected": int(len(path_rows)),
                "raw_source_rows_matched": raw_match_count,
                "entry_open_raw_match": entry_open_raw_match,
                "exit_close_raw_match": exit_close_raw_match,
                "all_ohlc_raw_match": all_ohlc_match,
                "missing_raw_dates": ";".join(missing_raw_dates),
                "path_start_previous_close": round(prior_close, 4),
                "max_abs_daily_price_move_pct": round(float(max_move_by_day.max()), 4),
                "market_limit_violation_count": violation_count,
                "limit_up_like_day_count": int(close_moves.ge(9.0).sum()),
                "limit_down_like_day_count": int(close_moves.le(-9.0).sum()),
                "corporate_action_event_count_in_window": calendar_event_count,
                "corporate_action_event_types_in_window": calendar_event_types,
                "company_calendar_coverage_status": "current_snapshot_not_full_historical_corporate_action_pit_layer",
                "raw_price_source_sha256": raw_source_sha,
                "price_path_classification": (
                    "requires_data_quality_exception_review"
                    if impossible
                    else "plausible_extreme_continuous_gain"
                ),
                "impossible_return_flag": impossible,
                "decision_basis_handling": (
                    "exclude_until_resolved" if impossible else "retain_as_observed_trade"
                ),
                "sensitivity_basis_handling": "exclude_abs_ge80_to_show_tail_dependence",
                "production_change": False,
                "promotion_readiness": "research_only_anomaly_evidence_not_promotion",
            }
        )
    return pd.DataFrame(rows, columns=COLUMNS)


def _markdown(audit: pd.DataFrame) -> str:
    display = audit[
        [
            "stock_id",
            "stock_name",
            "entry_date",
            "entry_open",
            "exit_date",
            "exit_close",
            "realized_return_pct",
            "price_path_trading_rows",
            "max_abs_daily_price_move_pct",
            "limit_up_like_day_count",
            "market_limit_violation_count",
            "price_path_classification",
        ]
    ]
    lines = [
        "# 營收低反應模型極端報酬價格路徑稽核",
        "",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- extreme threshold: `abs(realized_return_pct) >= {EXTREME_ABS_RETURN_PCT:.0f}%`",
        "- operation basis: 確認後下一交易日開盤進場，確認日後第 20 個交易日收盤出場。",
        "- raw verification: 每個持有交易日的 OHLC 均逐列對照 `data/daily_price/YYYYMMDD.csv`。",
        "- interpretation: `plausible_extreme_continuous_gain` 表示價格路徑可實現且 raw 資料一致，不表示適合直接用於 promotion。",
        "- calendar limitation: 現有 company calendar 不是完整歷史公司行動 PIT 層，因此公司行動欄只作輔助揭露。",
        "- decision: 可實現極端值保留於主樣本，同時另列排除 `abs >= 80%` 的敏感度結果。",
        "- financial statement scope: EPS、毛利率、營益率、營業利益、業外與淨利均未納入。",
        "",
        display.to_markdown(index=False),
        "",
    ]
    return "\n".join(lines)


def write_extreme_return_path_audit(audit: pd.DataFrame) -> None:
    for path in (LATEST_CSV, HISTORY_CSV, DOCS_CSV):
        path.parent.mkdir(parents=True, exist_ok=True)
        audit.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(audit)
    for path in (LATEST_MD, DOCS_MD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8", newline="\n")
