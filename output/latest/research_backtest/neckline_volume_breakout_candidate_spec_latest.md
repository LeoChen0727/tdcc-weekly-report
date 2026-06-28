# Neckline Volume Breakout Candidate Spec

- generated_at: `2026-06-29 07:00:38 Asia/Taipei`
- model_id: `neckline_volume_breakout_confirmation`
- source_model_id: `w_bottom_right_side`
- neckline_pattern_subtype: `w_bottom`
- source_research_id: `w_bottom_nearest_micro_anchor_event_replay`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- production impact: `none`; this spec does not update production model conditions, scoring, ranking, PDF logic, or baseline.

## Boundary

This candidate spec covers only the W-bottom subtype of `neckline_volume_breakout_confirmation`.
It does not define generic previous-high breakouts, descending-resistance breakouts, inverse head-and-shoulders, or triple-bottom logic.

## Tradability Warning

A-entry means buying next open after the breakout date. If a segment requires a later post-confirmation trigger, A-entry metrics use future information and are not tradable as breakout-day evidence.
C-entry means waiting for that later confirmation and then buying next open, so C-entry is the tradable interpretation for post-confirmation segments.

## Current Conclusion

The current replay does not yet support promotion to production. The all-breakout A-entry sample is tradable but weak, and the post-confirmation filter improves only the non-tradable A-entry view while the tradable C-entry view does not improve enough.
This version also tests breakout-day tradable filters such as signal candle quality, non-bearish pre-breakout context, market regime, and low-position context. These filters are still advisory unless a separate promotion PR approves a specific rule.
Best breakout-day tradable filter in this run is `w_bottom_breakout_signal_quality_pre60_non_bearish_lowpos70_sym1p5` with A-entry win rate `40.4255%`, average return `0.0174%`, and median return `-4.1353%`.
This is not strong enough for approved operation evidence because the win rate stays near 40% and the median return is not positive.

## Buy / Sell / Evaluation

- A-entry: buy next open after the neckline volume breakout date.
- C-entry: buy next open after selected post-confirmation date.
- Exit: stop if signal-day low is broken; otherwise sell at the 10th trading-day close.
- Win rate here means positive close/stop exit return over evaluated rows. It is not the early-entry +10%/+5% rule.
- Tradable breakout-day filters use only price/market data available on or before the breakout signal day.

## Metrics

| segment_id | status | sample | A evaluated | A win rate | A avg return | C evaluated | C win rate | C avg return | warning |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| w_bottom_breakout_all_sym1p5 | tradable_breakout_baseline_research_only | 209 | 204 | 38.7255 | 1.6363 | 146 | 38.3562 | 1.3633 |  |
| w_bottom_breakout_post_confirmation_sym1p5 | future_filter_leakage_for_a_entry_c_entry_not_improved | 150 | 147 | 51.7007 | 3.0946 | 146 | 38.3562 | 1.3633 | A-entry metrics for this segment are not tradable as a breakout-day rule if the segment requires a later post-confirmation trigger. Use C-entry metrics for the tradable post-confirmation entry. |
| w_bottom_breakout_second_arc_ge_1p5_sym1p5 | comparison_only_research_only | 87 | 85 | 31.7647 | 0.1443 | 56 | 32.1429 | 0.1154 |  |
| w_bottom_breakout_second_arc_ge_1p5_post_confirmation_sym1p5 | future_filter_leakage_for_a_entry_c_entry_not_improved | 57 | 56 | 46.4286 | 2.0482 | 56 | 32.1429 | 0.1154 | A-entry metrics for this segment are not tradable as a breakout-day rule if the segment requires a later post-confirmation trigger. Use C-entry metrics for the tradable post-confirmation entry. |
| w_bottom_breakout_tdcc_any_age7_sym1p5 | small_sample_comparison_only | 3 | 3 | 33.3333 | 15.8250 | 1 | 100.0000 | 26.8382 |  |
| w_bottom_breakout_second_arc_ge_1p5_tdcc_any_age7_sym1p5 | small_sample_comparison_only | 2 | 2 | 50.0000 | 25.4470 | 1 | 100.0000 | 26.8382 |  |
| w_bottom_breakout_signal_quality_sym1p5 | tradable_breakout_day_filter_research_only | 142 | 137 | 40.1460 | 1.2944 | 104 | 36.5385 | 0.2877 |  |
| w_bottom_breakout_pre60_non_bearish_sym1p5 | tradable_breakout_day_filter_research_only | 159 | 154 | 38.3117 | 1.6120 | 110 | 35.4545 | 0.8914 |  |
| w_bottom_breakout_market_bull_sym1p5 | tradable_breakout_day_filter_research_only | 155 | 150 | 38.0000 | 1.6442 | 108 | 38.8889 | 1.3200 |  |
| w_bottom_breakout_signal_quality_pre60_non_bearish_sym1p5 | tradable_breakout_day_filter_research_only | 130 | 125 | 40.0000 | 1.1342 | 96 | 34.3750 | 0.0689 |  |
| w_bottom_breakout_signal_quality_pre60_non_bearish_lowpos70_sym1p5 | tradable_breakout_day_filter_research_only | 49 | 47 | 40.4255 | 0.0174 | 39 | 30.7692 | -1.1305 |  |

## Next Review

Next work should move away from simple breakout-day filters and test alternative operation definitions: retest-hold-then-attack entry, close-based +10% / +5% neutral outcome, and better pre-breakout context classifiers. It should not promote this research variant into production baseline without a separate model-change PR.
