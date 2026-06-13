# Volume Attack Watch

- generated_at: `2026-06-14 00:21:54 Asia/Taipei`
- main_price_date: `20260612`
- total_watch_rows: `6`
- priority_distribution: `{'A_bottom_volume_attack': 3, 'B_bottom_volume_attack_with_risk': 3}`
- type_distribution: `{'bottom_volume_attack': 6}`
- scope_distribution: `{'bottom_volume_attack': 6}`
- selection_status_distribution: `{'selected': 6}`

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
| 1 | 1714 | 和桐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 6.358 | 52.0 | 48.2927 | 46.52014652014651 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 8105 | 凌巨 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | strong_accumulation | continued_overheated | 2.1366 | 5.8962 | 52.2034 | 25.01740219963804 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 1307 | 三芳 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 2.4243 | 10.8597 | 13.7771 | 13.61001623000233 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 2243 | 宏旭-KY | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 2.3306 | 32.8571 | 67.5676 | 46.499950772866015 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 2.1612 | 49.4118 | 54.878 | 44.74309051191945 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 6153 | 嘉聯益 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | first_seen | 4.0304 | 17.1053 | 20.5962 | 19.913769873349494 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

