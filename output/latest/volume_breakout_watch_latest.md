# Volume Attack Watch

- generated_at: `2026-06-26 19:44:52 Asia/Taipei`
- main_price_date: `20260626`
- total_watch_rows: `12`
- priority_distribution: `{'A_bottom_volume_attack': 12}`
- type_distribution: `{'bottom_volume_attack': 12}`
- scope_distribution: `{'bottom_volume_attack': 12}`
- selection_status_distribution: `{'selected': 12}`

## Interpretation

- Official model type is `bottom_volume_attack` only.
- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.
- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.
- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.
- Research observation basis is next trading day open after the signal date.
- This list is a model-selected universe and backtest layer. It is not standalone buy advice.

## Top Watch List

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | repeat_appear_label | volume_ratio | return_5d | return_20d | distance_to_ma20_pct | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 6226 | 光鼎 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 10.5856 | 47.1774 | 36.194 | 37.554173732805715 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 2 | 5230 | 雷笛克光學 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | first_seen | 7.1019 | 12.4122 | 45.4545 | 26.682501979414084 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 3 | 4707 | 磐亞 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 6.9988 | 21.9027 | 83.6667 | 34.45583211322598 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 4 | 5348 | 正能量智能 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 13.4147 | 11.1111 | 4.5198 | 15.643069229567107 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 5 | 1435 | 中福 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 5.966 | 76.2646 | 23.7705 | 46.530810286268796 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 6 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | continued_overheated | 2.9698 | 54.5076 | 119.2913 | 60.47248631518294 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 7 | 3230 | 錦明 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | range_rebound | neckline_breakout | continued_overheated | 4.1386 | 35.5442 | 30.8703 | 28.41375976798519 | continued_overheated | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 8 | 1718 | 中纖 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | first_seen | 4.4441 | 13.8917 | 76.7036 | 23.38165320349672 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 9 | 5211 | 蒙恬 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 3.8028 | 10.7895 | 18.5915 | 10.35386631716908 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 10 | 6259 | 百徽 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected |  |  |  | 0.6415 | 28.681 | 55.0832 | 38.07290380975892 |  | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 11 | 1515 | 力山 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | continued_overheated | 3.7475 | 18.677 | 38.9522 | 24.477094174063872 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |
| 12 | 6672 | 騰輝電子-KY | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | first_seen | 2.7281 | 28.9183 | 38.0615 | 26.39324748403853 | long_upper_shadow_quality_penalty | 以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。 |

