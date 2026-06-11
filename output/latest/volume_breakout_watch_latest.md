# Bottom Volume Attack Watch

- generated_at: `2026-06-11 16:11:21 Asia/Taipei`
- main_price_date: `20260611`
- total_watch_rows: `13`
- priority_distribution: `{'A_bottom_volume_attack': 7, 'B_bottom_volume_attack_with_risk': 6}`
- type_distribution: `{'bottom_volume_attack': 13}`
- scope_distribution: `{'bottom_volume_attack': 13}`
- selection_status_distribution: `{'selected': 13}`

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
| 1 | 1438 | 三地開發 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 6.3279 | 20.25 | 10.8295 | 16.917841516772004 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 1714 | 和桐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 6.4424 | 46.789 | 46.789 | 42.20115538438749 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 2537 | 聯上發 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | strong_accumulation | continued_overheated | 7.1809 | 12.4378 | 10.2439 | 14.604462474645041 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 8021 | 尖點 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | B_confirm_needed | mild_accumulation | first_seen | 3.5006 | 22.8448 | 32.8671 | 28.18350480688143 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 5345 | 馥鴻 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  |  |  | 2.0603 | 43.4077 | 62.5287 | 60.29928579526134 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 2597 | 潤弘 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | mild_accumulation | continued_overheated | 2.5679 | 22.5225 | 27.5 | 22.430607651912982 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 7 | 4306 | 炎洲 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | A_priority_watch | mild_accumulation | continued_2_3d | 2.9076 | 11.2281 | 18.7266 | 13.234506161814608 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 8 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 3.9146 | 35.8824 | 46.2025 | 35.100887026025916 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 9 | 2243 | 宏旭-KY | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | first_seen | 2.9276 | 13.0217 | 56.351 | 37.36430962767579 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 10 | 9910 | 豐泰 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.0611 | 34.9096 | 30.3763 | 32.81303484630658 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 11 | 7788 | 松川精密 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.7142 | 43.0079 | 48.4932 | 36.74782389302385 | tdcc_distribution_warning/continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 12 | 2547 | 日勝生 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | range_rebound | platform_breakout | C_watch_only | distribution_warning | stale_signal | 2.8575 | 10.8871 | 7.3171 | 8.970231314081921 | tdcc_distribution_warning/stale_signal | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 13 | 2484 | 希華 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | platform_breakout | C_watch_only | distribution_warning | continued_overheated | 3.2054 | 14.0977 | 53.2828 | 25.225643406055 | tdcc_distribution_warning/continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

