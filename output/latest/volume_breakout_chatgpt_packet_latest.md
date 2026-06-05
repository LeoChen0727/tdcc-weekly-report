# BOTTOM VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-06-06 02:41:08 Asia/Taipei`
- main_price_date: `20260605`
- watch_rows: `21`
- bottom_volume_attack_count: `21`
- selected_rows: `21`
- rows_with_risk_tags: `15`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Model Definition

- Model display name: 底部放量攻擊模型.
- Hard gates: close >= prior 20 trading day high excluding signal day * 1.02; volume_ratio >= 2.0; 20D average volume >= 1000 lots; bullish candle.
- The model intentionally does not require a 60D high breakout or moving-average reclaim.
- The model emits selected rows only. Risk flags and score components are ranking/operation context, not a separate watch/risk status.
- Same-day fake breakout is not confirmed on the signal date. Do not label a selected row as failed breakout until later price action confirms failure.
- Research entry basis is signal date next trading day open.

## Top Bottom Volume Attack

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3015 | 全漢 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 10.74 | 37.251 | 35.8974 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 1708 | 東鹼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 7.1749 | 28.534 | 31.9892 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 6890 | 來億-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 7.0143 | 44.7761 | 57.4675 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 2461 | 光群雷 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | B_confirm_needed | strong_accumulation | first_seen | 6.2628 | 20.0 | 18.1818 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 1810 | 和成 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 5.2884 | 15.8974 | 22.1622 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 3018 | 隆銘綠能 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.2539 | 24.7346 | 15.7635 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 7 | 4190 | 佐登-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.6749 | 11.6803 | 10.7724 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 8 | 6916 | 華凌 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.1348 | 13.9276 | 8.7766 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 9 | 3226 | 龍鋒 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.1002 | 8.8664 | 18.1486 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 10 | 2903 | 遠百 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.6847 | 7.7982 | 6.0948 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 11 | 1904 | 正隆 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 4.3601 | 15.2632 | 25.5014 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 12 | 3406 | 玉晶光 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | continued_many_days | 2.4884 | 13.1012 | 34.7826 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 13 | 2883 | 凱基金 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 3.2164 | 22.6667 | 20.524 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 14 | 1809 | 中釉 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 2.3783 | 36.8542 | 65.5556 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 15 | 8070 | 長華* | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 2.456 | 19.4286 | 30.083 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 16 | 2493 | 揚博 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | neckline_challenge | B_confirm_needed | mild_accumulation | continued_many_days | 3.5965 | 11.25 | 35.3612 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 17 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 8.6996 | 18.4825 | 27.9412 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 18 | 2855 | 統一證 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 3.1384 | 24.4211 | 47.75 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 19 | 3376 | 新日興 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | B_confirm_needed | distribution_warning | continued_many_days | 2.3305 | 17.037 | 17.037 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 20 | 2501 | 國建 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | neckline_breakout | C_watch_only | distribution_warning | stale_signal | 2.1563 | 6.4018 | 4.7826 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 21 | 2442 | 新美齊 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | platform_breakout | C_watch_only | distribution_warning | stale_signal | 2.1852 | 6.7024 | 6.7024 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

## Backtest Summary

_No rows._

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.
- If the stock falls back below the prior-20D-high breakout threshold after entry, later reports may tag failure or reduce risk.

