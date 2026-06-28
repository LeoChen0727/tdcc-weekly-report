# W-Bottom Nearest Micro Anchor Event Replay

- generated_at: `2026-06-26 23:02:54 Asia/Taipei`
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
| baseline_current_detector | 1929 | 994 | 205 | 202 | 29.2079 | 0.1508 |  |  |  | research_only |
| variant_nearest_micro_45d_event_replay | 1691 | 879 | 209 | 204 | 38.7255 | 1.6363 | -238 | 9.5176 | 1.4855 | research_only |

## Candidate Set Comparison

| comparison_status | sample_size | unique_stocks | sample_warning |
| --- | --- | --- | --- |
| all_union | 2537 | 1110 | low_mature_sample_size;research_only |
| common | 1083 | 663 | low_mature_sample_size;research_only |
| variant_only | 608 | 428 | low_mature_sample_size;research_only |
| baseline_only | 846 | 567 | low_mature_sample_size;research_only |

## Variant-Only Sample

| stock_id | stock_name | signal_date | variant_left_peak_date | variant_left_low_date | variant_neckline_date | variant_right_low_date | variant_breakout_date | variant_a_return_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1605 | 華新 | 20240930 | 20240718 | 20240806 | 20240902 | 20240910 |  |  |
| 1409 | 新纖 | 20241001 | 20240723 | 20240806 | 20240820 | 20240904 |  |  |
| 1903 | 士紙 | 20241001 | 20240723 | 20240806 | 20240903 | 20240920 |  |  |
| 2641 | 正德 | 20241004 | 20240723 | 20240806 | 20240826 | 20240909 |  |  |
| 5608 | 四維航 | 20241004 | 20240723 | 20240806 | 20240826 | 20240910 |  |  |
| 6799 | 來頡 | 20241004 | 20240716 | 20240806 | 20240830 | 20240919 |  |  |
| 2009 | 第一銅 | 20241008 | 20240723 | 20240806 | 20240820 | 20240904 |  |  |
| 2491 | 吉祥全 | 20241011 | 20240723 | 20240806 | 20240903 | 20240909 |  |  |
| 1904 | 正隆 | 20241015 | 20240719 | 20240911 | 20240930 | 20241009 |  |  |
| 3093 | 港建* | 20241016 | 20240717 | 20240806 | 20240902 | 20240911 |  |  |
| 3664 | 安瑞-KY | 20241017 | 20240719 | 20240806 | 20240812 | 20240816 |  |  |
| 4198 | 欣大健康 | 20241017 | 20240822 | 20240910 | 20240930 | 20241011 |  |  |
| 4736 | 泰博 | 20241017 | 20240619 | 20240806 | 20240902 | 20240919 |  |  |
| 3288 | 點晶 | 20241021 | 20240821 | 20240911 | 20240925 | 20241011 |  |  |
| 5211 | 蒙恬 | 20241021 | 20240723 | 20240806 | 20240826 | 20240912 |  |  |
| 6112 | 邁達特 | 20241023 | 20240801 | 20240909 | 20241007 | 20241016 |  |  |
| 3625 | 西勝 | 20241025 | 20240722 | 20240806 | 20240930 | 20241016 |  |  |
| 6164 | 華興 | 20241028 | 20240723 | 20240806 | 20240830 | 20240911 | 20241106 | 1.9108 |
| 6261 | 久元 | 20241028 | 20240717 | 20240806 | 20240819 | 20241014 |  |  |
| 2254 | 巨鎧精密-創 | 20241029 | 20240923 | 20241009 | 20241017 | 20241024 |  |  |
| 1538 | 正峰 | 20241030 | 20240814 | 20240910 | 20241007 | 20241024 |  |  |
| 6285 | 啟碁 | 20241030 | 20240828 | 20240909 | 20240925 | 20241014 |  |  |
| 4911 | 德英 | 20241105 | 20240723 | 20240806 | 20240814 | 20240925 |  |  |
| 4164 | 承業醫 | 20241107 | 20240722 | 20240806 | 20241016 | 20241101 |  |  |
| 6291 | 沛亨 | 20241107 | 20240718 | 20240806 | 20240902 | 20241101 |  |  |
| 6591 | 動力-KY | 20241107 | 20240827 | 20240909 | 20241028 | 20241104 |  |  |
| 6174 | 安碁 | 20241108 | 20240718 | 20240806 | 20240814 | 20240912 |  |  |
| 6785 | 昱展新藥 | 20241108 | 20240925 | 20241016 | 20241024 | 20241101 |  |  |
| 2395 | 研華 | 20241111 | 20240826 | 20240909 | 20240925 | 20241101 |  |  |
| 1308 | 亞聚 | 20241112 | 20240826 | 20240909 | 20240927 | 20241101 |  |  |

## Interpretation Guardrails

- This is a candidate event replay, not a production model promotion.
- The production-like 180-trading-day history gate remains active; manual positive examples are not force-added.
- Only the left anchor selector changes from the current detector to nearest micro pressure high in the 45-trading-day window.
- A better-looking anchor is insufficient for promotion unless it improves stable event outcomes across broader samples.
