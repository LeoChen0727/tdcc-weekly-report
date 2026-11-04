# Volume Attack Watch

- generated_at: `2026-11-04 19:40:55 Asia/Taipei`
- main_price_date: `20261104`
- total_watch_rows: `4`
- priority_distribution: `{'A_bottom_volume_attack': 4}`
- type_distribution: `{'bottom_volume_attack': 4}`
- scope_distribution: `{'bottom_volume_attack': 4}`
- selection_status_distribution: `{'selected': 4}`

## Interpretation

- Official model type is `bottom_volume_attack` only.
- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.
- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.
- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.
- Research observation basis is next trading day open after the signal date.
- This list is a model-selected universe and backtest layer. It is not standalone buy advice.

## Top Watch List

| advisory_volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7819 | 精誠金融 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 8.1558 | 14.3077 | 10.2374 | 12.695282875777325 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 1410 | 南染 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 4.7115 | 10.0629 | 9.6033 | 10.213078618662763 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 2643 | 捷迅 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 11.4667 | 6.8471 | 8.2258 | 6.804615996816543 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 1416 | 廣豐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_2_3d | 2.3384 | 5.2045 | 19.4093 | 9.097918272937555 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

