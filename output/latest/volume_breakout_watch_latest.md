# Bottom Volume Attack Watch

- generated_at: `2026-06-11 18:23:00 Asia/Taipei`
- main_price_date: `20260605`
- total_watch_rows: `21`
- priority_distribution: `{'A_bottom_volume_attack': 16, 'B_bottom_volume_attack_with_risk': 5}`
- type_distribution: `{'bottom_volume_attack': 21}`
- scope_distribution: `{'bottom_volume_attack': 21}`
- selection_status_distribution: `{'selected': 21}`

## Interpretation

- Official model type is `bottom_volume_attack` only.
- Hard gates: close >= prior 20 trading day high excluding signal day * 1.02, volume_ratio >= 2.0, 20D average volume >= 1000 lots, and bullish candle.
- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.
- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.
- Entry basis for research/reporting is next trading day open after the signal date.
- This list is a model-selected universe and backtest layer. It is not standalone buy advice.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3015 | 全漢 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 10.74 | 37.251 | 35.8974 | 31.013500665525772 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 1708 | 東鹼 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 7.1749 | 28.534 | 31.9892 | 22.291407222914074 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 6890 | 來億-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 7.0143 | 44.7761 | 57.4675 | 38.25541619156214 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 2461 | 光群雷 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | B_confirm_needed | strong_accumulation | first_seen | 6.2628 | 20.0 | 18.1818 | 17.878192534381142 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 1810 | 和成 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 5.2884 | 15.8974 | 22.1622 | 17.356873945216144 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 3018 | 隆銘綠能 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.2539 | 24.7346 | 15.7635 | 19.30750875767884 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 7 | 4190 | 佐登-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.6749 | 11.6803 | 10.7724 | 10.390925663358331 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 8 | 6916 | 華凌 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 4.1348 | 13.9276 | 8.7766 | 12.734288864388077 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 9 | 3226 | 龍鋒 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.1002 | 8.8664 | 18.1486 | 14.481293520594818 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 10 | 2903 | 遠百 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.6847 | 7.7982 | 6.0948 | 5.76057605760576 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 11 | 1904 | 正隆 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | mild_accumulation | continued_overheated | 4.3601 | 15.2632 | 25.5014 | 13.633415488390188 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 12 | 3406 | 玉晶光 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | continued_many_days | 2.4884 | 13.1012 | 34.7826 | 18.054353470659514 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 13 | 2883 | 凱基金 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 3.2164 | 22.6667 | 20.524 | 22.42182302062541 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 14 | 1809 | 中釉 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 2.3783 | 36.8542 | 65.5556 | 34.620814275227296 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 15 | 8070 | 長華* | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_challenge | C_watch_only | strong_accumulation | continued_overheated | 2.456 | 19.4286 | 30.083 | 26.40491910689986 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 16 | 2493 | 揚博 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | neckline_challenge | B_confirm_needed | mild_accumulation | continued_many_days | 3.5965 | 11.25 | 35.3612 | 22.399862472064626 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 17 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 8.6996 | 18.4825 | 27.9412 | 21.314741035856557 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 18 | 2855 | 統一證 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 3.1384 | 24.4211 | 47.75 | 32.8911124852437 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 19 | 3376 | 新日興 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | B_confirm_needed | distribution_warning | continued_many_days | 2.3305 | 17.037 | 17.037 | 13.07251908396947 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 20 | 2501 | 國建 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | neckline_breakout | C_watch_only | distribution_warning | stale_signal | 2.1563 | 6.4018 | 4.7826 | 7.481324562381553 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 21 | 2442 | 新美齊 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | platform_breakout | C_watch_only | distribution_warning | stale_signal | 2.1852 | 6.7024 | 6.7024 | 6.6023838221507924 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

