# TDCC Signal Tracking

This document describes the TDCC signal tracking layer used by the weekly TDCC report, ABM pre-move accumulation model, and TDCC effectiveness report.

## Raw Signal vs Normalized Signal

`output/history/tdcc_signals/tdcc_signal_log.csv`

- Keeps threshold-level raw signals.
- A stock can appear more than once when it triggers multiple thresholds such as over 400, 600, 800, or 1000 lots.
- This file is kept for compatibility and raw audit trails.

`output/history/tdcc_signals/tdcc_normalized_signal_log.csv`

- Keeps one normalized signal per stock per signal date.
- Key: `signal_id = {signal_date}_{code}_normalized`.
- This is the preferred table for ranking, weekly summaries, ABM scoring, and monthly effectiveness statistics.
- Multiple threshold triggers for the same stock on the same signal date must not be double counted.

## TDCC Snapshot

`output/history/tdcc_signals/tdcc_signal_snapshot.csv` freezes the state available at signal time.

Important groups of fields:

- Threshold flags: `has_400`, `has_600`, `has_800`, `has_1000`.
- TDCC streaks: `tdcc_400_streak_weeks`, `tdcc_600_streak_weeks`, `tdcc_800_streak_weeks`, `tdcc_1000_streak_weeks`, `all_threshold_streak_weeks`.
- TDCC changes before signal: `tdcc_1w_change_*`, `tdcc_2w_change_*`, `tdcc_3w_change_*`.
- Price reaction before signal: `price_ret_1w`, `price_ret_2w`, `price_ret_3w`, `price_ret_4w`.
- Relative reaction before signal: `relative_ret_1w`, `relative_ret_2w`, `relative_ret_3w`, `relative_ret_4w`.
- Volume reaction: `volume_ratio_1w`, `volume_ratio_2w`.
- Position context: `distance_from_20d_high`, `distance_from_60d_high`, `distance_from_ma20`, `distance_from_ma60`.
- Market context: `benchmark_index`, `market_regime`.
- Phase label: `tdcc_price_phase`.

The snapshot must use only data available on or before `signal_date`. Future prices are used only by the performance table, never to rewrite the original phase.

## Per-stock TDCC History

`data/tdcc_stock_history/{stock_id}.csv` stores weekly TDCC history for one stock.

The weekly TDCC workflow rebuilds these files from `output/history/tdcc/tdcc_holder_ratio_*.csv` and the latest TDCC holder ratio file. Each file is deduped by `as_of_date + stock_id`, sorted by date, and keeps history instead of only the latest row.

Historical backfill is handled by `scripts/backfill_tdcc_history.py`. TDCC OpenData currently exposes the latest all-market file only, so historical backfill uses the official TDCC query page by weekly date and stock id. The script intentionally defaults to a bounded universe such as `chatgpt-top` to avoid tens of thousands of requests. It writes:

- `output/history/tdcc/tdcc_holder_ratio_{date}.csv`
- `data/tdcc_stock_history_raw/{stock_id}.csv`
- `output/latest/tdcc_history_backfill_manifest_latest.csv`
- `output/latest/tdcc_history_backfill_manifest_latest.md`

After a backfill, run `python scripts/build_tdcc_stock_history.py` and then rebuild the TDCC signal structures, ABM, normalized performance, effectiveness report, and ChatGPT tracking packet.

Important fields:

- `over_400_ratio`, `over_600_ratio`, `over_800_ratio`, `over_1000_ratio`.
- `over_400_change_1w`, `over_800_change_1w`, `over_1000_change_1w`.
- `over_400_change_2w`, `over_800_change_2w`, `over_1000_change_2w`.
- `over_400_change_3w`, `over_800_change_3w`, `over_1000_change_3w`.
- `tdcc_consecutive_up_weeks`.
- `all_thresholds_up`, `high_thresholds_up`, `four_thresholds_sync_up`.
- `theme_breadth_level`.

If the raw TDCC source does not provide retail ratio or total shareholder count, those columns stay blank instead of failing the workflow.

The individual stock report first reads `data/tdcc_stock_history/{stock_id}.csv`. If it is missing, it falls back to normalized TDCC signal tables, marks the history source, and continues the stock report with `insufficient_tdcc_history` when needed.

## TDCC-price Phase

`tdcc_price_phase` describes the relationship between TDCC accumulation and price reaction at the signal date.

- `tdcc_leading_price`: TDCC has improved for at least two weeks, but price and relative return have not reacted much.
- `tdcc_price_confirmed`: TDCC has improved and price/volume already confirmed.
- `price_leading_tdcc`: price has already moved strongly before TDCC confirmation.
- `tdcc_price_divergence`: TDCC improved but price and relative return are still weak.
- `overheated_after_tdcc`: price is already stretched after TDCC strength.
- `failed_after_tdcc`: TDCC improved but price later broke down in the available context.
- `insufficient_price_context`: price, volume, or benchmark history is not enough for a reliable phase.

This field is designed to answer the core question: did TDCC lead price, confirm price, or arrive after price had already reacted?

## Theme Breadth

`output/history/tdcc_signals/theme_breadth_history.csv` stores one row per `signal_date + primary_theme`.

It estimates whether TDCC strength is broad across a theme or concentrated in only one or two names.

Key fields:

- `total_signal_count`
- `increase_400_count`, `increase_600_count`, `increase_800_count`, `increase_1000_count`
- `all_threshold_count`
- `consecutive_2w_count`
- `consecutive_3w_count`
- `breadth_score`
- `sync_status`
- `theme_priority`
- `theme_breadth_level`

## Performance Maturity

`output/history/tdcc_signals/tdcc_signal_performance.csv` tracks D+1, D+2, D+5, D+10, and D+20 results.

Rules:

- D+N fields are filled only when enough future trading days exist.
- `mature_dN=True` means that horizon is ready for statistics.
- Pending rows are not positive or negative.
- Performance includes both absolute return and relative return versus TWSE or TPEx benchmark where available.

## Effectiveness Report

`output/latest/tdcc_signal_effectiveness_latest.md` and `output/latest/tdcc_signal_effectiveness_latest.csv` summarize factor effectiveness.

The report includes:

- TDCC threshold factor groups.
- ABM factor groups.
- TDCC-price phase factor groups.
- TDCC consecutive weeks x phase distribution.
- Phase D+5, D+10, and D+20 performance when mature data exists.
- Setup type x phase.
- Theme breadth x phase.
- Market regime x phase.

`sample_size` is the number of signals in a group. `mature_sample_dN` is the number of rows actually used for D+N performance statistics.
