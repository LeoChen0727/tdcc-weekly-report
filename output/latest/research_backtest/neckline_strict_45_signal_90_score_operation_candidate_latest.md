# Neckline Strict 45 Signal 90 Score Operation Candidate

- generated_at: `2026-06-29 07:20:26 Asia/Taipei`
- model_id: `neckline_volume_breakout_confirmation`
- operation_candidate_id: `neckline_strict_45_signal_90_score_v1`
- research_id: `neckline_strict_45_signal_90_score_operation_candidate`
- source_research_id: `structured_neckline_dual_window_risk_penalty_audit`
- source_risk_rule_id: `broad_45_non_bearish_with_90_warning`
- segment_id: `low_position_le60_market_bull`
- entry_rule_id: `close_ge_1pct_within_3_sessions_next_open`
- exit_rule_id: `tp10_close_win_5pct_pullback_neutral_else_20d_close_loss`
- outcome_definition_version: `tp10_close_win_5pct_pullback_neutral_else_20d_loss_v1`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `false`
- production impact: `none`; this candidate does not update production model conditions, scoring, ranking, PDF logic, daily_full_pipeline, or production baseline.

## Candidate Semantics

- 45-day context is the entry-signal gate: `filter_45` must be `auto_non_bearish`.
- 90-day context is score adjustment only, not an entry exclusion; `filter_90=auto_bearish` rows remain eligible with penalty labels.
- Entry uses the next open after the confirmation close, so it is tradable and does not use same-day close as a buy price.
- This is research-only evidence. Promotion requires a separate daily_model_maintenance PR before removing or replacing production models.

## Summary

| source_candidate_count | confirmation_candidate_count | tradable_entry_count | win_count | neutral_count | loss_count | pure_win_rate_pct | neutral_inclusive_success_rate_pct | avg_return_pct | median_return_pct | filter90_auto_bearish_confirmed_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 87 | 51 | 51 | 23 | 15 | 13 | 63.8889 | 74.5098 | 4.3784 | 4.4597 | 19 |

## Selected Rule

- entry_rule: `After a 45-day non-bearish neckline candidate, wait until close return from the original retest entry is at least +1% within 3 sessions, then buy next open.`
- exit_rule: `Win when close return reaches +10%; neutral when close return first reaches +5% then closes back at or below +5% before +10%; otherwise sell at the 20th close.`
- signal_window_role: `45d_auto_non_bearish_required_entry_signal`
- score_window_role: `90d_context_score_adjustment_only_not_entry_exclusion`

## Outcome And PDF Metric Definitions

- pdf_metric_label: `operation-rule win rate and neutral-inclusive success rate`
- win_definition: `close return reaches +10% before the 20-session limit`
- neutral_definition: `close return reaches +5% first, then closes back at or below +5% before +10%`
- loss_definition: `no +10% close win and no neutral trigger before the 20th close, even if the final return is positive`
- pdf_subtitle_note: `PDF subtitle must label this as operation-rule evidence: win=+10% close hit; neutral=+5% close reached then pulled back to +5%; loss=otherwise 20th close.`

## Detail Preview

| outcome_result | stock_id | stock_name | signal_date | confirmation_signal_date | confirmation_entry_date | return_pct | context_45 | context_90 | filter_90 | score_adjustment_points | score_adjustment_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| loss | 2368 | 金像電 | 20250522 | 20250603 | 20250604 | 8.2721 | volatile_mixed | bearish | auto_bearish | 5 | heavy_90d_risk_penalty |
| loss | 6451 | 訊芯-KY | 20250807 | 20250812 | 20250813 | -8.6207 | slow_uptrend | bearish | auto_bearish | 1 | moderate_90d_risk_penalty |
| loss | 2324 | 仁寶 | 20250917 | 20250925 | 20250926 | -8.1944 | sideways_or_consolidation | sideways_or_consolidation | auto_non_bearish | 0 | clean_or_repair_credit |
| loss | 2327 | 國巨* | 20260113 | 20260122 | 20260123 | -7.1192 | sideways_or_consolidation | bearish | auto_bearish | 5 | heavy_90d_risk_penalty |
| loss | 6197 | 佳必琪 | 20260311 | 20260317 | 20260318 | -6.7358 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| loss | 8289 | 泰藝 | 20260224 | 20260302 | 20260303 | -6.1743 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| loss | 6706 | 惠特 | 20250918 | 20250930 | 20251001 | -25.0567 | volatile_mixed | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| loss | 4973 | 廣穎電通 | 20260312 | 20260318 | 20260319 | -20.0824 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| loss | 3051 | 力特 | 20260116 | 20260121 | 20260122 | -19.4056 | slow_uptrend | bearish | auto_bearish | 3 | moderate_90d_risk_penalty |
| loss | 4534 | 慶騰 | 20260123 | 20260225 | 20260226 | -17.5896 | slow_uptrend | bearish | auto_bearish | 4 | heavy_90d_risk_penalty |
| loss | 4526 | 東台 | 20260116 | 20260123 | 20260126 | -16.4420 | sideways_or_consolidation | bearish | auto_bearish | 5 | heavy_90d_risk_penalty |
| loss | 4533 | 協易機 | 20260121 | 20260127 | 20260128 | -15.1220 | slow_uptrend | bearish | auto_bearish | 5 | heavy_90d_risk_penalty |
| loss | 3714 | 富采 | 20251231 | 20260107 | 20260108 | -1.8717 | sideways_or_consolidation | bearish | auto_bearish | 4 | heavy_90d_risk_penalty |
| neutral | 3661 | 世芯-KY | 20250627 | 20250702 | 20250703 | 4.7328 | slow_uptrend | bearish | auto_bearish | 3 | moderate_90d_risk_penalty |
| neutral | 1326 | 台化 | 20250723 | 20250730 | 20250731 | 4.4597 | sideways_or_consolidation | bearish | auto_bearish | 4 | heavy_90d_risk_penalty |
| neutral | 3596 | 智易 | 20260226 | 20260306 | 20260309 | 4.4041 | sideways_or_consolidation | bearish | auto_bearish | 4 | heavy_90d_risk_penalty |
| neutral | 4904 | 遠傳 | 20250930 | 20251007 | 20251008 | 4.2129 | sideways_or_consolidation | sideways_or_consolidation | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 6234 | 高僑 | 20260414 | 20260422 | 20260423 | 3.9239 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 3017 | 奇鋐 | 20250604 | 20250611 | 20250612 | 3.7344 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 2368 | 金像電 | 20250630 | 20250708 | 20250709 | 3.6508 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 4707 | 磐亞 | 20260410 | 20260417 | 20260420 | 3.6424 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 4540 | 全球傳動 | 20260115 | 20260120 | 20260121 | 3.6325 | sideways_or_consolidation | bearish | auto_bearish | 6 | heavy_90d_risk_penalty |
| neutral | 2455 | 全新 | 20250611 | 20250625 | 20250626 | 3.4615 | volatile_mixed | bearish | auto_bearish | 7 | heavy_90d_risk_penalty |
| neutral | 1313 | 聯成 | 20250716 | 20250728 | 20250729 | 2.9268 | sideways_or_consolidation | volatile_mixed | auto_non_bearish | 2 | non_bearish_with_risk_tags |
| neutral | 3037 | 欣興 | 20250703 | 20250710 | 20250711 | 1.5810 | slow_uptrend | bearish | auto_bearish | 2 | moderate_90d_risk_penalty |
| neutral | 2301 | 光寶科 | 20250703 | 20250710 | 20250711 | 1.2766 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| neutral | 6147 | 頎邦 | 20260312 | 20260318 | 20260319 | -3.0683 | sideways_or_consolidation | bearish | auto_bearish | 6 | heavy_90d_risk_penalty |
| neutral | 3645 | 達邁 | 20260115 | 20260120 | 20260121 | -0.5961 | sideways_or_consolidation | bearish | auto_bearish | 8 | heavy_90d_risk_penalty |
| win | 8383 | 千附 | 20260413 | 20260416 | 20260417 | 20.1401 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 8046 | 南電 | 20250703 | 20250711 | 20250714 | 19.7232 | slow_uptrend | bearish | auto_bearish | 4 | heavy_90d_risk_penalty |
| win | 1727 | 中華化 | 20250723 | 20250728 | 20250729 | 19.4611 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 1802 | 台玻 | 20250715 | 20250724 | 20250725 | 16.8704 | slow_uptrend | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 1447 | 力鵬 | 20260518 | 20260522 | 20260525 | 16.5552 | sideways_or_consolidation | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 3704 | 合勤控 | 20250826 | 20250829 | 20250901 | 15.5882 | sideways_or_consolidation | sideways_or_consolidation | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 3163 | 波若威 | 20260128 | 20260209 | 20260210 | 15.5357 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 6016 | 康和證 | 20260424 | 20260506 | 20260507 | 15.0718 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 8163 | 達方 | 20260508 | 20260515 | 20260518 | 14.9123 | sideways_or_consolidation | sideways_or_consolidation | auto_non_bearish | 1 | clean_or_repair_credit |
| win | 2316 | 楠梓電 | 20250723 | 20250731 | 20250801 | 14.9045 | slow_uptrend | slow_uptrend | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 8033 | 雷虎 | 20250723 | 20250728 | 20250729 | 13.9952 | sideways_or_consolidation | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
| win | 6209 | 今國光 | 20250805 | 20250811 | 20250812 | 13.7705 | volatile_mixed | volatile_mixed | auto_non_bearish | 0 | clean_or_repair_credit |
