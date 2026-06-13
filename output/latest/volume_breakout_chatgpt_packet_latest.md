# VOLUME ATTACK CHATGPT PACKET

## Metadata
- generated_at: `2026-06-13 15:18:23 Asia/Taipei`
- main_price_date: `20260612`
- watch_rows: `6`
- bottom_volume_attack_count: `6`
- selected_rows: `6`
- rows_with_risk_tags: `5`
- watch_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.csv
- watch_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_watch_latest.md
- backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.csv
- backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/volume_breakout_backtest_latest.md

## Model Definition

- Model display name: 放量攻擊模型.
- Hard gates: close >= prior 20 trading day high excluding signal day * 1.02; volume_ratio >= 2.0; 20D average volume >= 1000 lots; bullish candle.
- The model intentionally does not require a 60D high breakout or moving-average reclaim.
- The model emits selected rows only. Risk flags and score components are ranking/operation context, not a separate watch/risk status.
- Same-day fake breakout is not confirmed on the signal date. Do not label a selected row as failed breakout until later price action confirms failure.
- Research entry basis is signal date next trading day open.

## Top Volume Attack

| volume_breakout_rank | stock_id | stock_name | volume_breakout_type | volume_watch_scope | volume_breakout_priority | selection_status | category | pattern_stage | decision_priority | tdcc_status | repeat_appear_label | volume_ratio | return_5d | return_20d | risk_flags | next_volume_breakout_confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1714 | 和桐 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | platform_breakout | C_watch_only | mild_accumulation | continued_overheated | 6.358 | 52.0 | 48.2927 | continued_overheated/long_upper_shadow_quality_penalty | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 2 | 8105 | 凌巨 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | C_watch_only | strong_accumulation | continued_overheated | 2.1366 | 5.8962 | 52.2034 | continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 3 | 1307 | 三芳 | bottom_volume_attack | bottom_volume_attack | A_bottom_volume_attack | selected | true_breakout | breakout_confirmed | A_priority_watch | mild_accumulation | first_seen | 2.4243 | 10.8597 | 13.7771 |  | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 4 | 2243 | 宏旭-KY | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 2.3306 | 32.8571 | 67.5676 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 5 | 2483 | 百容 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | continued_overheated | 2.1612 | 49.4118 | 54.878 | tdcc_distribution_warning/continued_overheated | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |
| 6 | 6153 | 嘉聯益 | bottom_volume_attack | bottom_volume_attack | B_bottom_volume_attack_with_risk | selected | true_breakout | breakout_confirmed | C_watch_only | distribution_warning | first_seen | 4.0304 | 17.1053 | 20.5962 | tdcc_distribution_warning | 以訊號日隔天開盤為進場假設；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則降低部位或退出。 |

## Backtest Summary

_No rows._

## Rules

- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.
- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.
- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.
- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.
- If the stock falls back below the prior-20D-high breakout threshold after entry, later reports may tag failure or reduce risk.

