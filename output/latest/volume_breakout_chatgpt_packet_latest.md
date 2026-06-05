# BOTTOM VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-06-05 14:48:49 Asia/Taipei`
- main_price_date: `20260603`
- watch_rows: `56`
- bottom_volume_attack_count: `56`
- selected_rows: `56`
- rows_with_risk_tags: `31`
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
| 1 | 1714 | 和桐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 6.5187 | 17.0213 | 19.8257 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 2323 | 中環 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 5.4541 | 23.7864 | 20.283 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 1710 | 東聯 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | repeated_but_no_breakout | 4.7868 | 23.5521 | 29.5547 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 1608 | 華榮 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 5.3553 | 17.0877 | 19.2133 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 8454 | 富邦媒 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 3.5699 | 52.8796 | 61.7729 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 3049 | 精金 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 4.8879 | 29.5082 | 22.9572 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 7 | 2009 | 第一銅 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 4.6628 | 13.8539 | 17.7083 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 8 | 1314 | 中石化 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 5.9679 | 17.1014 | 11.7566 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 9 | 2405 | 輔信 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 5.0716 | 32.3171 | 42.7632 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 10 | 3050 | 鈺德 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | pattern | platform_right_side | B_confirm_needed | strong_accumulation | continued_2_3d | 5.9386 | 13.7097 | 16.0494 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 11 | 8101 | 華冠 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.8227 | 18.9781 | 30.4 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 12 | 1708 | 東鹼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | neckline_breakout | C_watch_only | mild_accumulation | continued_overheated | 4.9856 | 12.7438 | 10.5867 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 13 | 1612 | 宏泰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | strong_accumulation | continued_many_days | 4.4403 | 7.0461 | 7.483 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 14 | 1618 | 合機 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | B_confirm_needed | neutral | repeated_but_no_breakout | 4.2669 | 8.134 | 17.4026 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 15 | 1447 | 力鵬 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | pattern | platform_right_side | C_watch_only | mild_accumulation | continued_overheated | 2.7586 | 26.7273 | 40.5242 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 16 | 2031 | 新光鋼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | continued_many_days | 3.7526 | 8.3655 | 6.8528 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 17 | 6005 | 群益證 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | pattern | platform_right_side | C_watch_only | mild_accumulation | continued_overheated | 2.5878 | 27.7143 | 49.0 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 18 | 2457 | 飛宏 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 2.2755 | 15.6746 | 16.3673 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 19 | 3021 | 鴻名 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.1196 | 60.3206 | 143.1611 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 20 | 3311 | 閎暉 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | repeated_but_no_breakout | 5.1734 | 12.3209 | 28.3142 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 21 | 1529 | 樂事綠能 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.641 | 9.7996 | 10.0446 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 22 | 1304 | 台聚 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.646 | 20.1681 | 8.3333 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 23 | 1313 | 聯成 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | pattern | early_entry_watch | B_confirm_needed | strong_accumulation | repeated_but_no_breakout | 4.2837 | 15.534 | 10.1852 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 24 | 8077 | 洛碁 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.6309 | 15.4545 | 16.916 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 25 | 1718 | 中纖 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 2.2681 | 39.4612 | 37.0717 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 26 | 2017 | 官田鋼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | continued_2_3d | 2.6729 | 8.642 | 11.2644 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 27 | 1434 | 福懋 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.9226 | 11.0 | 3.4161 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 28 | 4976 | 佳凌 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.6388 | 12.1359 | 20.7317 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 29 | 1312 | 國喬 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.0063 | 45.7916 | 24.8927 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 30 | 2324 | 仁寶 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.5131 | 40.8683 | 61.1301 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 31 | 4306 | 炎洲 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.687 | 8.3333 | 14.1221 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 32 | 2474 | 可成 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 3.5216 | 23.2614 | 22.673 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 33 | 1307 | 三芳 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | B_confirm_needed | mild_accumulation | continued_2_3d | 2.562 | 11.1111 | 8.8 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 34 | 1605 | 華新 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.1607 | 13.8667 | 30.9816 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 35 | 6120 | 達運 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.1948 | 15.8273 | 23.3716 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 36 | 2201 | 裕隆 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | B_confirm_needed | mild_accumulation | repeated_but_no_breakout | 2.2939 | 10.2079 | 7.3665 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 37 | 2104 | 國際中橡 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.083 | 14.0974 | 9.7561 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 38 | 1440 | 南紡 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | platform_right_side | C_watch_only | distribution_warning | continued_overheated | 4.6347 | 29.4606 | 24.3028 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 39 | 2390 | 云辰 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 4.5223 | 20.0935 | 35.1209 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 40 | 1444 | 力麗 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | neckline_challenge | C_watch_only | distribution_warning | stale_signal | 5.0401 | 29.1883 | 24.4592 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

## Backtest Summary

_No rows._

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.
- If the stock falls back below the prior-20D-high breakout threshold after entry, later reports may tag failure or reduce risk.

