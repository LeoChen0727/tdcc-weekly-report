# volume_range_breakout_v2_candidate_bucket_contract

This is a research-only contract for the next `volume_range_breakout` v2 discussion.
It does not modify `config/stock_model_contract_registry.csv`, daily ranking, PDF
operation rows, or any production buy gate.

## Baseline Scope

- Parent production model under review: `volume_range_breakout`.
- Source artifact: `output/latest/research_backtest/volume_range_breakout_v2_position_shape_matrix_detail_latest.csv`.
- Baseline operation research scope: `d15_close_only_next_day_continuation_ma20_ema23_stop`.
- Confirmation rule: `next_day_continuation_confirmed_close_only`.
- Entry rule: `confirmation_next_open`.
- Stop/exit policy: MA20/EMA23 close-confirmed stop for 4 days, otherwise fixed D+15 close exit.
- Sample count is reported as context only. Small sample count is not a disqualifier by itself.

## Candidate Models

The artifact fixes two research-only candidate model buckets:

1. `volume_range_breakout_v2_low_position_volume_attack` / `低位放量攻擊`
   - `position_bucket_120d == low_pos_le40`.
   - Includes `consolidation`, `non_consolidation`, and `wide_range`.
   - This intentionally broadens the user-facing meaning from `低位盤整` to `低位放量攻擊`, because the current data shows low-position non-consolidation can also perform well.

2. `volume_range_breakout_v2_mid_position_momentum_attack` / `中位動能放量攻擊`
   - `position_bucket_120d == mid_pos_40_75`.
   - Includes only `non_consolidation` and `wide_range`.
   - Excludes `mid_pos_40_75 + consolidation`, because the current D+15 baseline does not support treating that bucket as the same momentum model.

These two candidate model event sets must be non-overlapping. The validator fails if the same `source_event_key` appears in both models.

## High-Position Audit Buckets

High-position buckets are not promoted into the two candidate models in this artifact.
They remain explicit audit/rescue subjects:

- `high_pos_gt75_non_consolidation`
- `high_pos_gt75_wide_range`

The stratification table may show conditions that improve those high-position buckets,
but those rows are only `stratification_only_not_candidate_or_confirmation_gate`.
They cannot become a hidden daily buy gate without a separate model decision.

## Stratification Tests

The artifact tests these feature layers as research-only stratification:

- `tdcc_weekly_increase_top20`
- `tdcc_any_top20`
- `tech_ma60_gt_ma120`
- `tech_ret20_0_to_25`
- `tech_dist_ema23_0_to_15`
- `volume_ratio_2_to_6`
- `not_limit_up_like`
- `breakout_over_prev60_2_to_10`

These are not production gates. If one is later promoted, it must become either an
explicit model condition or an explicit score/risk tag, never a hidden approval layer.

## Output Artifacts

- `output/latest/research_backtest/volume_range_breakout_v2_candidate_bucket_contract_latest.csv`
- `output/latest/research_backtest/volume_range_breakout_v2_candidate_bucket_contract_detail_latest.csv`
- `output/latest/research_backtest/volume_range_breakout_v2_candidate_bucket_contract_stratification_latest.csv`
- `output/latest/research_backtest/volume_range_breakout_v2_candidate_bucket_contract_latest.md`
- `output/history/research/volume_range_breakout_v2_candidate_bucket_contract.csv`
- `output/history/research/volume_range_breakout_v2_candidate_bucket_contract_detail.csv`
- `output/history/research/volume_range_breakout_v2_candidate_bucket_contract_stratification.csv`

## Guardrails

Builder: `scripts/build_volume_range_breakout_v2_candidate_bucket_contract.py`.

`scripts/validate_volume_range_breakout_v2_candidate_bucket_contract.py` enforces:

- All rows remain `warning_research_variant_only`.
- `approved_for_daily` remains false.
- `production_readiness` remains `not_production_ready_research_only`.
- Candidate model detail rows are non-overlapping.
- The two candidate model event sets match the explicit 120-day position/shape rules.
- High-position buckets are present only as audit/rescue stratification subjects.
- Stratification conditions remain non-gating.
- `meets_win_return_metric` depends only on win rate >= 60%, positive average return, and positive median return.
