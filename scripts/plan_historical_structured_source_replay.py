from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import replay_historical_structured_sources as replay  # noqa: E402


def _required_date(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise RuntimeError(f"historical replay planner tail is empty: {label}")
    return replay.parse_date(text, label)


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RuntimeError(f"historical replay planner tail group is invalid: {label}")
    return value


def _aligned_structured_base(matrix: dict[str, Any]) -> str:
    dated_tails: list[tuple[str, str]] = []
    for family in ("market_index", "market_index_ohlc"):
        values = _require_mapping(matrix.get(family), family)
        for index_code in ("TWSE", "TPEX"):
            dated_tails.append(
                (
                    f"{family}.{index_code}",
                    _required_date(values.get(index_code), f"{family}.{index_code}"),
                )
            )

    taifex = _require_mapping(matrix.get("taifex"), "taifex")
    expected_taifex = set(replay.TAIFEX_HISTORY_SPECS)
    observed_taifex = set(taifex)
    if observed_taifex != expected_taifex:
        raise RuntimeError(
            "historical replay planner TAIFEX tail set mismatch: "
            f"observed={sorted(observed_taifex)} expected={sorted(expected_taifex)}"
        )
    for source_id in replay.TAIFEX_HISTORY_SPECS:
        dated_tails.append(
            (
                f"taifex.{source_id}",
                _required_date(taifex.get(source_id), f"taifex.{source_id}"),
            )
        )

    for family in ("warrant_daily", "warrant_flow"):
        dated_tails.append((family, _required_date(matrix.get(family), family)))

    distinct_dates = {date for _, date in dated_tails}
    if len(distinct_dates) != 1:
        details = ", ".join(f"{label}={date}" for label, date in dated_tails)
        raise RuntimeError(
            "historical replay planner structured tails are not aligned: " + details
        )
    return next(iter(distinct_dates))


def plan_from_tail_matrix(
    matrix: dict[str, Any],
    *,
    max_replay_dates: int,
) -> dict[str, Any]:
    if max_replay_dates < 1:
        raise RuntimeError("--max-replay-dates must be a positive integer")
    if not isinstance(matrix, dict):
        raise RuntimeError("historical replay planner source tail matrix is invalid")

    daily_price = _required_date(matrix.get("daily_price"), "daily_price")
    stock_history = _require_mapping(
        matrix.get("stock_price_history"), "stock_price_history"
    )
    stock_history_max = _required_date(
        stock_history.get("max_date"), "stock_price_history.max_date"
    )
    if daily_price != stock_history_max:
        raise RuntimeError(
            "historical replay planner price/history tails are not aligned: "
            f"daily_price={daily_price} stock_price_history.max_date={stock_history_max}"
        )
    high_water = daily_price
    required_base = _aligned_structured_base(matrix)

    try:
        high_water_trading_dates = replay.expected_trading_dates(high_water, high_water)
    except RuntimeError as exc:
        if str(exc) != "historical source replay window has no trading dates":
            raise
        high_water_trading_dates = []
    if high_water_trading_dates != [high_water]:
        raise RuntimeError(
            "historical replay planner price/history high-water is not a trading date: "
            f"{high_water}"
        )

    if required_base > high_water:
        raise RuntimeError(
            "historical replay planner structured base is later than price/history high-water: "
            f"required_base_date={required_base} "
            f"price_history_high_water_date={high_water}"
        )
    if required_base == high_water:
        return {
            "should_replay": False,
            "start_date": "",
            "end_date": "",
            "price_history_high_water_date": high_water,
            "required_base_date": required_base,
            "trading_dates": [],
            "reason": "structured_sources_already_at_price_history_high_water",
        }

    calendar_start = (
        datetime.strptime(required_base, "%Y%m%d") + timedelta(days=1)
    ).strftime("%Y%m%d")
    trading_dates = replay.expected_trading_dates(calendar_start, high_water)
    if not trading_dates:
        raise RuntimeError("historical replay planner window has no trading dates")
    first_date = trading_dates[0]
    observed_previous = replay.previous_trading_date(first_date)
    if observed_previous != required_base:
        raise RuntimeError(
            "historical replay planner structured base is not immediately before the "
            "first replay trading date: "
            f"first_date={first_date} previous_trading_date={observed_previous} "
            f"required_base_date={required_base}"
        )
    if len(trading_dates) > max_replay_dates:
        raise RuntimeError(
            "historical replay planner window exceeds --max-replay-dates: "
            f"trading_date_count={len(trading_dates)} max_replay_dates={max_replay_dates}"
        )

    return {
        "should_replay": True,
        "start_date": first_date,
        "end_date": high_water,
        "price_history_high_water_date": high_water,
        "required_base_date": required_base,
        "trading_dates": trading_dates,
        "reason": "structured_sources_behind_price_history_high_water",
    }


def recent_trading_dates_ending_at(end_date: str, *, count: int) -> list[str]:
    if count < 1:
        raise RuntimeError("recent structured-source integrity count must be positive")
    dates = [end_date]
    while len(dates) < count:
        dates.append(replay.previous_trading_date(dates[-1]))
    return list(reversed(dates))


def validate_recent_structured_source_coverage(
    end_date: str,
    *,
    count: int,
) -> None:
    for target_date in recent_trading_dates_ending_at(end_date, count=count):
        replay.build_source_output_evidence("market_index", target_date)
        replay.build_source_output_evidence("taifex_futures_options_vix", target_date)
        replay.build_source_output_evidence("official_warrant_daily", target_date)


def build_plan(*, max_replay_dates: int) -> dict[str, Any]:
    matrix = replay.source_tail_matrix()
    plan = plan_from_tail_matrix(matrix, max_replay_dates=max_replay_dates)
    replay.validate_exact_baseline(
        matrix,
        plan["required_base_date"],
        plan["price_history_high_water_date"],
    )
    validate_recent_structured_source_coverage(
        plan["required_base_date"],
        count=max_replay_dates,
    )
    return plan


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-replay-dates", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    payload = build_plan(max_replay_dates=args.max_replay_dates)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
