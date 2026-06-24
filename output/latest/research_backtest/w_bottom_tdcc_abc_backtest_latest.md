# W-Bottom TDCC A/B/C Backtest

- generated_at: `2026-06-24 21:57:31 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- overlay_model_id: `tdcc_weekly_ranking_formula`
- research_id: `w_bottom_tdcc_abc_backtest`
- advisory_status: `warning_research_variant_only`
- scope: research only; all rows keep `approved_for_daily=False`.
- note: this uses a research-only W-bottom symmetric-time parameter set while the production PR is still unmerged.

## Event Counts

- raw_event_rows: `5128`
- dedup_event_rows: `940`

## Primary Rows

| abc_stage | tdcc_filter_id | sample_size | mature_sample_size | win_rate | avg_return | median_return | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_w_neckline_breakout_next_open | all_any_rank_age0 | 56 | 52 | 30.77 | 0.1621 | -1.7857 | medium |
| B_tdcc_filter_next_open | all_any_rank_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_any_rank_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_top10_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top10_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top20_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top20_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top50_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_top50_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_any_rank_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_any_rank_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_top10_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top10_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top20_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top20_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top50_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_top50_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| C_tdcc_filter_post_confirmation_next_open | all_any_rank_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_any_rank_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top10_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top10_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top20_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top20_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top50_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top50_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_any_rank_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_any_rank_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top10_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top10_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top20_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top20_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top50_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top50_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |

## Largest Mature Samples

| abc_stage | tdcc_filter_id | sample_size | mature_sample_size | win_rate | avg_return | median_return | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_w_neckline_breakout_next_open | all_any_rank_age0 | 56 | 52 | 30.77 | 0.1621 | -1.7857 | medium |
| B_tdcc_filter_next_open | all_any_rank_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_any_rank_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_top50_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | all_top50_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_any_rank_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_any_rank_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_top50_age14 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| B_tdcc_filter_next_open | weekly_increase_top50_age7 | 2 | 2 | 100.0 | 32.8436 | 32.8436 | low |
| C_tdcc_filter_post_confirmation_next_open | all_any_rank_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_any_rank_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top50_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top50_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_any_rank_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_any_rank_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top50_age14 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top50_age7 | 2 | 2 | 100.0 | 19.9435 | 19.9435 | low |
| B_tdcc_filter_next_open | all_top10_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top10_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top20_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | all_top20_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top10_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top10_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top20_age14 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| B_tdcc_filter_next_open | weekly_increase_top20_age7 | 1 | 1 | 100.0 | 11.3744 | 11.3744 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top10_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top10_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top20_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | all_top20_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top10_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top10_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top20_age14 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |
| C_tdcc_filter_post_confirmation_next_open | weekly_increase_top20_age7 | 1 | 1 | 100.0 | 13.0488 | 13.0488 | low |

## Interpretation Guardrails

- `A_w_neckline_breakout_next_open`: W-bottom symmetric neckline volume breakout, enter next open.
- `B_tdcc_filter_next_open`: A plus an as-of TDCC filter, enter next open after W neckline breakout.
- `C_tdcc_filter_post_confirmation_next_open`: B plus a volume-breakout-style post confirmation trigger.
- TDCC filters use as-of matching only; future TDCC rows are not allowed.
- Low sample rows are directional research evidence only and must not be promoted directly into production.
