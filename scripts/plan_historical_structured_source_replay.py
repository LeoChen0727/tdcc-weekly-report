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


TAIFEX_DATED_SOURCE_IDS = tuple(replay.TAIFEX_DATED_RAW_SOURCE_IDS)
TAIFEX_VIX_SOURCE_ID = "taiwan_vix"


def _required_date(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise RuntimeError(f"historical replay planner tail is empty: {label}")
    return replay.parse_date(text, label)


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RuntimeError(f"historical replay planner tail group is invalid: {label}")
    return value


def _structured_tail_dates(matrix: dict[str, Any]) -> dict[str, str]:
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

    return dict(dated_tails)


def _source_contract_base(
    tail_dates: dict[str, str],
) -> tuple[str, str]:
    d0_labels = [
        "market_index.TWSE",
        "market_index.TPEX",
        "market_index_ohlc.TWSE",
        "market_index_ohlc.TPEX",
        "warrant_daily",
        "warrant_flow",
        f"taifex.{TAIFEX_VIX_SOURCE_ID}",
    ]
    exact_dates = {tail_dates.get(label, "") for label in d0_labels}
    errors: list[str] = []
    if len(exact_dates) != 1:
        details = ", ".join(
            f"{label}={tail_dates.get(label)}" for label in d0_labels
        )
        errors.append("D0 structured source tails must share one date: " + details)
        base_date = ""
    else:
        base_date = next(iter(exact_dates))

    delayed_labels = [f"taifex.{source_id}" for source_id in TAIFEX_DATED_SOURCE_IDS]
    delayed_dates = {tail_dates.get(label, "") for label in delayed_labels}
    allowed_delayed_dates = (
        {base_date, replay.previous_trading_date(base_date)} if base_date else set()
    )
    if len(delayed_dates) != 1 or not delayed_dates.issubset(allowed_delayed_dates):
        details = ", ".join(
            f"{label}={tail_dates.get(label)}" for label in delayed_labels
        )
        errors.append(
            "TAIFEX dated source tails must be one common D0 or D-1 trading date: "
            f"{details} allowed={sorted(allowed_delayed_dates)}"
        )
    if errors:
        raise RuntimeError(
            "historical replay planner source-specific operational tail mismatch: "
            + "; ".join(errors)
        )
    return base_date, next(iter(delayed_dates))


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

    tail_dates = _structured_tail_dates(matrix)
    required_base, taifex_dated_tail_date = _source_contract_base(tail_dates)
    if required_base > high_water:
        raise RuntimeError(
            "historical replay planner structured base is later than price/history high-water: "
            f"required_base_date={required_base} "
            f"price_history_high_water_date={high_water}"
        )

    if required_base == high_water:
        reason = (
            "structured_sources_already_at_price_history_high_water"
            if taifex_dated_tail_date == high_water
            else "structured_sources_satisfy_source_specific_operational_tails"
        )
        return {
            "should_replay": False,
            "start_date": "",
            "end_date": "",
            "price_history_high_water_date": high_water,
            "required_base_date": high_water,
            "taifex_dated_tail_date": taifex_dated_tail_date,
            "repair_taifex_base_date": "",
            "trading_dates": [],
            "reason": reason,
        }

    calendar_start = (
        datetime.strptime(required_base, "%Y%m%d") + timedelta(days=1)
    ).strftime("%Y%m%d")
    advance_dates = replay.expected_trading_dates(calendar_start, high_water)
    if not advance_dates:
        raise RuntimeError("historical replay planner window has no trading dates")
    first_date = advance_dates[0]
    observed_previous = replay.previous_trading_date(first_date)
    if observed_previous != required_base:
        raise RuntimeError(
            "historical replay planner structured base is not immediately before the "
            "first replay trading date: "
            f"first_date={first_date} previous_trading_date={observed_previous} "
            f"required_base_date={required_base}"
        )

    if len(advance_dates) == 1:
        return {
            "should_replay": False,
            "start_date": "",
            "end_date": "",
            "price_history_high_water_date": high_water,
            "required_base_date": required_base,
            "taifex_dated_tail_date": taifex_dated_tail_date,
            "repair_taifex_base_date": "",
            "trading_dates": [],
            "reason": "structured_sources_ready_for_single_daily_full_advance",
        }

    trading_dates = advance_dates[:-1]
    if not trading_dates or trading_dates[-1] != replay.previous_trading_date(high_water):
        raise RuntimeError(
            "historical replay planner pre-resume window does not end immediately before "
            f"price/history high-water: trading_dates={trading_dates} high_water={high_water}"
        )
    repair_taifex_base_date = (
        required_base if taifex_dated_tail_date != required_base else ""
    )
    replay_action_count = len(trading_dates) + bool(repair_taifex_base_date)
    if replay_action_count > max_replay_dates:
        raise RuntimeError(
            "historical replay planner window exceeds --max-replay-dates: "
            f"replay_action_count={replay_action_count} "
            f"trading_date_count={len(trading_dates)} "
            f"taifex_base_repair_count={int(bool(repair_taifex_base_date))} "
            f"max_replay_dates={max_replay_dates}"
        )

    return {
        "should_replay": True,
        "start_date": first_date,
        "end_date": trading_dates[-1],
        "price_history_high_water_date": high_water,
        "required_base_date": required_base,
        "taifex_dated_tail_date": taifex_dated_tail_date,
        "repair_taifex_base_date": repair_taifex_base_date,
        "trading_dates": trading_dates,
        "reason": "structured_sources_require_pre_resume_catch_up",
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


def validate_operational_structured_source_coverage(
    high_water: str,
    *,
    taifex_dated_tail_date: str,
    count: int,
) -> None:
    vix_path, vix_pk_columns = replay.TAIFEX_HISTORY_SPECS[TAIFEX_VIX_SOURCE_ID]
    for target_date in recent_trading_dates_ending_at(high_water, count=count):
        replay.build_source_output_evidence("market_index", target_date)
        replay.build_source_output_evidence("official_warrant_daily", target_date)
        replay.canonical_target_slice(
            vix_path,
            target_date,
            pk_columns=vix_pk_columns,
        )
    for target_date in recent_trading_dates_ending_at(
        taifex_dated_tail_date,
        count=count,
    ):
        replay.build_source_output_evidence("taifex_futures_options_vix", target_date)


def build_plan(*, max_replay_dates: int) -> dict[str, Any]:
    matrix = replay.source_tail_matrix()
    plan = plan_from_tail_matrix(matrix, max_replay_dates=max_replay_dates)
    if plan["should_replay"]:
        replay.validate_exact_baseline(
            matrix,
            plan["required_base_date"],
            plan["price_history_high_water_date"],
            repair_taifex_base_date=plan["repair_taifex_base_date"],
        )
        if plan["repair_taifex_base_date"]:
            validate_operational_structured_source_coverage(
                plan["required_base_date"],
                taifex_dated_tail_date=plan["taifex_dated_tail_date"],
                count=max_replay_dates,
            )
        else:
            validate_recent_structured_source_coverage(
                plan["required_base_date"],
                count=max_replay_dates,
            )
    else:
        high_water = plan["price_history_high_water_date"]
        replay.validate_daily_price_canonical_legacy_pair(high_water)
        replay.validate_stock_history_date_coverage(
            high_water,
            manifest_end_date=high_water,
        )
        required_base = plan["required_base_date"]
        if plan["taifex_dated_tail_date"] == required_base:
            validate_recent_structured_source_coverage(
                required_base,
                count=max_replay_dates,
            )
        else:
            validate_operational_structured_source_coverage(
                required_base,
                taifex_dated_tail_date=plan["taifex_dated_tail_date"],
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
