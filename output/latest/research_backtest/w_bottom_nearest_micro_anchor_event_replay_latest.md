# W-Bottom Nearest Micro Anchor Event Replay

- generated_at: `2026-06-25 14:30:19 Asia/Taipei`
- model_id: `w_bottom_right_side`
- confirmation_model_id: `neckline_volume_breakout_confirmation`
- overlay_model_id: `tdcc_weekly_ranking_formula`
- research_id: `w_bottom_nearest_micro_anchor_event_replay`
- source_research_id: `w_bottom_left_anchor_rule_replay`
- tested_left_anchor_rule_id: `nearest_micro_pressure_45d_min15_before_left_low`
- scope: research/backtest only; `approved_for_daily=False` and `not_production_ready_research_only`.
- production impact: `none`; this does not modify daily model conditions, scoring, ranking, PDF consumers, or production baselines.

## Event Set Summary

| event_set_id | sample_size | unique_stocks | breakout_signal_count | mature_sample_size | win_rate_pct | avg_a_return_pct | delta_sample_size_vs_baseline | delta_win_rate_pct_vs_baseline | delta_avg_a_return_pct_vs_baseline | sample_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_current_detector | 470 | 289 | 56 | 52 | 30.7692 | 0.1621 |  |  |  | medium_mature_sample_size;research_only |
| variant_nearest_micro_45d_event_replay | 372 | 246 | 55 | 51 | 33.3333 | 0.6943 | -98 | 2.5641 | 0.5322 | medium_mature_sample_size;research_only |

## Candidate Set Comparison

| comparison_status | sample_size | unique_stocks | sample_warning |
| --- | --- | --- | --- |
| all_union | 588 | 328 | low_mature_sample_size;research_only |
| common | 254 | 179 | low_mature_sample_size;research_only |
| variant_only | 118 | 98 | low_mature_sample_size;research_only |
| baseline_only | 216 | 156 | low_mature_sample_size;research_only |

## Variant-Only Sample

| stock_id | stock_name | signal_date | variant_left_peak_date | variant_left_low_date | variant_neckline_date | variant_right_low_date | variant_breakout_date | variant_a_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8374 | 羅昇 | 20260105 | 20251106 | 20251119 | 20251205 | 20251218 |  |  |
| 3041 | 揚智 | 20260107 | 20251106 | 20251121 | 20251210 | 20260102 | 20260123 | -14.4246 |
| 4919 | 新唐 | 20260107 | 20251028 | 20251119 | 20251210 | 20251230 | 20260119 | -0.6711 |
| 4952 | 凌通 | 20260107 | 20251103 | 20251121 | 20251215 | 20251226 |  |  |
| 2382 | 廣達 | 20260108 | 20251030 | 20251119 | 20251209 | 20251230 |  |  |
| 2436 | 偉詮電 | 20260108 | 20251028 | 20251119 | 20251201 | 20251205 |  |  |
| 2520 | 冠德 | 20260108 | 20250924 | 20251105 | 20251224 | 20260105 |  |  |
| 2363 | 矽統 | 20260109 | 20251106 | 20251121 | 20251208 | 20260105 | 20260121 | -13.9966 |
| 3312 | 弘憶股 | 20260112 | 20250923 | 20251107 | 20251113 | 20251202 |  |  |
| 1616 | 億泰 | 20260113 | 20251113 | 20251211 | 20251229 | 20260108 | 20260120 | -5.0987 |
| 2017 | 官田鋼 | 20260113 | 20250925 | 20251105 | 20251113 | 20260106 |  |  |
| 6550 | 北極星藥業-KY | 20260113 | 20251104 | 20251121 | 20251127 | 20251209 |  |  |
| 1589 | 永冠-KY | 20260114 | 20251031 | 20251121 | 20251215 | 20260106 | 20260119 | -0.8152 |
| 2351 | 順德 | 20260114 | 20251112 | 20251218 | 20251229 | 20260109 | 20260120 | 3.5294 |
| 6285 | 啟碁 | 20260114 | 20251105 | 20251119 | 20251203 | 20251231 | 20260120 | 46.2687 |
| 6592 | 和潤企業 | 20260114 | 20250930 | 20251105 | 20251124 | 20260105 |  |  |
| 1316 | 上曜 | 20260115 | 20251031 | 20251121 | 20251219 | 20260109 |  |  |
| 2482 | 連宇 | 20260115 | 20251030 | 20251121 | 20251216 | 20260105 |  |  |
| 2923 | 鼎固-KY | 20260115 | 20250922 | 20251105 | 20251212 | 20260109 |  |  |
| 4440 | 宜新實業 | 20260116 | 20251029 | 20251119 | 20251219 | 20260109 |  |  |
| 8101 | 華冠 | 20260119 | 20251113 | 20251126 | 20251202 | 20260113 |  |  |
| 2438 | 翔耀 | 20260120 | 20251204 | 20260102 | 20260109 | 20260115 |  |  |
| 3338 | 泰碩 | 20260120 | 20251104 | 20251121 | 20251201 | 20260113 |  |  |
| 5471 | 松翰 | 20260120 | 20251021 | 20251121 | 20251204 | 20260106 |  |  |
| 1515 | 力山 | 20260121 | 20250911 | 20251105 | 20251210 | 20260113 |  |  |
| 1310 | 台苯 | 20260122 | 20250821 | 20251003 | 20251202 | 20251226 | 20260303 | 6.5421 |
| 4737 | 華廣 | 20260123 | 20251117 | 20251215 | 20251230 | 20260108 |  |  |
| 6695 | 芯鼎 | 20260123 | 20251107 | 20251119 | 20251223 | 20260113 |  |  |
| 1447 | 力鵬 | 20260126 | 20250821 | 20251105 | 20251204 | 20260121 | 20260127 | -2.0313 |
| 4746 | 台耀 | 20260127 | 20251126 | 20260106 | 20260116 | 20260122 |  |  |

## Interpretation Guardrails

- This is a candidate event replay, not a production model promotion.
- The production-like 180-trading-day history gate remains active; manual positive examples are not force-added.
- Only the left anchor selector changes from the current detector to nearest micro pressure high in the 45-trading-day window.
- A better-looking anchor is insufficient for promotion unless it improves stable event outcomes across broader samples.
