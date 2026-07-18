# Volume Attack Watch

- generated_at: `2026-07-18 17:44:49 Asia/Taipei`
- main_price_date: `20260717`
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
| 1 | 4139 | 馬光-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 9.2199 | 52.6104 | 56.701 | 44.43177499049791 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 6243 | 迅杰 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 6.2003 | 30.4678 | 62.5197 | 24.83367606144913 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 3288 | 點晶 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 4.2197 | 44.0541 | 22.2477 | 26.019624069038883 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 3024 | 憶聲 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | platform_breakout | repeated_but_no_breakout | 4.5208 | 14.5161 | 13.6 | 13.30540594454417 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

