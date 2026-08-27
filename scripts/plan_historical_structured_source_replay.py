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
    *,
    high_water: str,
) -> tuple[str, str]:
    d0_labels = [
        "market_index.TWSE",
        "market_index.TPEX",
        "market_index_ohlc.TWSE",
        "market_index_ohlc.TPEX",
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

    warrant_labels = ["warrant_daily", "warrant_flow"]
    warrant_dates = {tail_dates.get(label, "") for label in warrant_labels}
    allowed_warrant_dates = {base_date} if base_date else set()
    if base_date and base_date == high_water:
        allowed_warrant_dates.add(replay.previous_trading_date(base_date))
    if len(warrant_dates) != 1 or not warrant_dates.issubset(
        allowed_warrant_dates
    ):
        details = ", ".join(
            f"{label}={tail_dates.get(label)}" for label in warrant_labels
        )
        errors.append(
            "warrant source tails must be one common D0, or D-1 only for the "
            "current no-replay state: "
            f"{details} allowed={sorted(allowed_warrant_dates)}"
        )

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
    required_base, taifex_dated_tail_date = _source_contract_base(
        tail_dates,
        high_water=high_water,
    )
    warrant_tail_date = tail_dates["warrant_daily"]
    if required_base > high_water:
        raise RuntimeError(
            "historical replay planner structured base is later than price/history high-water: "
            f"required_base_date={required_base} "
            f"price_history_high_water_date={high_water}"
        )

    if required_base == high_water:
        reason = (
            "structured_sources_already_at_price_history_high_water"
            if (
                taifex_dated_tail_date == high_water
                and warrant_tail_date == high_water
            )
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


def require_pk_unique(
    evidence: dict[str, Any],
    *,
    source_id: str,
    target_date: str,
) -> dict[str, Any]:
    if evidence.get("pk_unique") is not True or any(
        component.get("pk_unique") is not True
        for component in evidence.get("components", [])
    ):
        raise RuntimeError(
            "historical structured-source PK conflict: "
            f"source={source_id} target_date={target_date} reason=duplicate_pk"
        )
    return evidence


def validate_recent_structured_source_coverage(
    end_date: str,
    *,
    count: int,
    allow_historical_structured_absence: bool = False,
) -> None:
    target_dates = recent_trading_dates_ending_at(end_date, count=count)
    for target_date in target_dates:
        require_pk_unique(
            replay.build_source_output_evidence("market_index", target_date),
            source_id="market_index",
            target_date=target_date,
        )
    validate_warrant_structured_source_coverage(
        end_date,
        count=count,
        allow_historical_absence=allow_historical_structured_absence,
    )
    validate_taifex_structured_source_coverage(
        end_date,
        count=count,
        allow_historical_absence=allow_historical_structured_absence,
    )


def validate_warrant_structured_source_coverage(
    end_date: str,
    *,
    count: int,
    allow_historical_absence: bool = False,
) -> dict[str, dict[str, Any]]:
    evidence: dict[str, dict[str, Any]] = {}
    for target_date in recent_trading_dates_ending_at(end_date, count=count):
        daily_path = Path(
            f"output/history/warrant_daily/warrant_daily_{target_date}.csv"
        )
        flow_path = Path(
            f"output/history/warrant_flow/warrant_flow_{target_date}.csv"
        )
        daily_exists = daily_path.exists()
        flow_exists = flow_path.exists()
        if target_date == end_date or not allow_historical_absence:
            output_evidence = require_pk_unique(
                replay.build_source_output_evidence(
                    "official_warrant_daily",
                    target_date,
                ),
                source_id="official_warrant_daily",
                target_date=target_date,
            )
            evidence[target_date] = {
                "historical_absence_status": "not_applicable",
                "output_evidence": output_evidence,
            }
            continue
        if daily_exists != flow_exists:
            raise RuntimeError(
                "historical warrant paired artifact mismatch: "
                f"target_date={target_date} reason=warrant_pair_lineage_mismatch "
                f"warrant_daily_exists={daily_exists} warrant_flow_exists={flow_exists}"
            )
        if not daily_exists:
            evidence[target_date] = {
                "historical_absence_status": "paired_artifacts_absent_non_blocking",
                "warrant_daily_path": daily_path.as_posix(),
                "warrant_daily_exists": False,
                "warrant_flow_path": flow_path.as_posix(),
                "warrant_flow_exists": False,
            }
            continue
        output_evidence = require_pk_unique(
            replay.build_source_output_evidence(
                "official_warrant_daily",
                target_date,
            ),
            source_id="official_warrant_daily",
            target_date=target_date,
        )
        evidence[target_date] = {
            "historical_absence_status": "not_applicable",
            "output_evidence": output_evidence,
        }
    return evidence


def validate_taifex_structured_source_coverage(
    end_date: str,
    *,
    count: int,
    allow_historical_absence: bool = False,
) -> None:
    vix_path, vix_pk_columns = replay.TAIFEX_HISTORY_SPECS[TAIFEX_VIX_SOURCE_ID]
    for target_date in recent_trading_dates_ending_at(end_date, count=count):
        if target_date == end_date or not allow_historical_absence:
            require_pk_unique(
                replay.build_source_output_evidence(
                    "taifex_futures_options_vix",
                    target_date,
                ),
                source_id="taifex_futures_options_vix",
                target_date=target_date,
            )
            continue
        require_pk_unique(
            replay.canonical_target_slice(
                vix_path,
                target_date,
                pk_columns=vix_pk_columns,
            ),
            source_id=TAIFEX_VIX_SOURCE_ID,
            target_date=target_date,
        )
        replay.validate_taifex_raw_history_parity(
            target_date,
            allow_historical_unilateral_gaps=True,
        )


def validate_operational_structured_source_coverage(
    high_water: str,
    *,
    taifex_dated_tail_date: str,
    warrant_tail_date: str,
    count: int,
    allow_historical_structured_absence: bool = False,
) -> None:
    vix_path, vix_pk_columns = replay.TAIFEX_HISTORY_SPECS[TAIFEX_VIX_SOURCE_ID]
    for target_date in recent_trading_dates_ending_at(high_water, count=count):
        require_pk_unique(
            replay.build_source_output_evidence("market_index", target_date),
            source_id="market_index",
            target_date=target_date,
        )
        require_pk_unique(
            replay.canonical_target_slice(
                vix_path,
                target_date,
                pk_columns=vix_pk_columns,
            ),
            source_id=TAIFEX_VIX_SOURCE_ID,
            target_date=target_date,
        )
    validate_warrant_structured_source_coverage(
        warrant_tail_date,
        count=count,
        allow_historical_absence=allow_historical_structured_absence,
    )
    validate_taifex_structured_source_coverage(
        taifex_dated_tail_date,
        count=count,
        allow_historical_absence=allow_historical_structured_absence,
    )


def build_plan(*, max_replay_dates: int) -> dict[str, Any]:
    matrix = replay.source_tail_matrix()
    plan = plan_from_tail_matrix(matrix, max_replay_dates=max_replay_dates)
    warrant_tail_date = _required_date(matrix.get("warrant_daily"), "warrant_daily")
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
                warrant_tail_date=warrant_tail_date,
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
        if (
            plan["taifex_dated_tail_date"] == required_base
            and warrant_tail_date == required_base
        ):
            validate_recent_structured_source_coverage(
                required_base,
                count=max_replay_dates,
                allow_historical_structured_absence=True,
            )
        else:
            validate_operational_structured_source_coverage(
                required_base,
                taifex_dated_tail_date=plan["taifex_dated_tail_date"],
                warrant_tail_date=warrant_tail_date,
                count=max_replay_dates,
                allow_historical_structured_absence=True,
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
