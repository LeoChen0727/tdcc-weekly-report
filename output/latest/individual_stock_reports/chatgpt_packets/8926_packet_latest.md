# INDIVIDUAL STOCK CHATGPT PACKET - 8926 台汽電

## Metadata
- generated_at: 2026-07-10 22:28:42 Asia/Taipei
- stock_id: 8926
- stock_name: 台汽電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8926_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8926_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8926_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8926_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8926_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8926_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8926_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8926.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8926.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8926.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8926.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8926_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8926_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8926_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure
- acceptable_risk_reward

### post_entry_watch_items
- next_monthly_revenue
- next_tdcc_update
- 23ema_hold_or_reclaim
- volume_price_confirmation
- prior_high_breakout_quality
- sector_benchmark_strength
- event_follow_through
- warrant_overheat_check

### downgrade_reason
- none

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260709
- open: 79.8
- high: 79.9
- low: 75.3
- close: 76
- volume: 11979255
- ma5: 77.64
- ema23_primary: 74.93
- distance_to_ema23_pct: 1.42
- ma20: 77.17
- ma60: 63.3
- ma120: 53.85
- return_5d: 4.11
- return_20d: 1.33
- volume_ratio: 1.15
- distance_to_ma20_pct_auxiliary: -1.52
- distance_to_high_60_pct: -9.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,77,77.3,73.6,75.5,15998730,65.36,15.52,66.64,53.04,1.09
20260612,76.8,78.3,74,74.2,12637681,66.09,12.26,67.29,53.5,0.88
20260615,74.7,75,72.2,72.4,11202241,66.62,8.68,68.03,53.93,0.79
20260616,72.5,78.6,72.5,76.8,14340085,67.47,13.83,69.03,54.42,0.99
20260617,76.9,79.8,75.6,79.4,12526055,68.46,15.98,70,54.98,0.86
20260618,79.7,82,78.4,79,12774581,69.34,13.93,70.9,55.53,0.87
20260622,80,80.7,79,79,7788449,70.15,12.62,71.81,56.09,0.53
20260623,80.3,84.3,80,82.2,13250509,71.15,15.53,72.79,56.69,0.91
20260624,82.2,83.8,80.8,81.9,8481706,72.05,13.68,73.45,57.28,0.6
20260625,82.2,82.2,77.9,78.1,12777391,72.55,7.65,73.74,57.81,0.95
20260626,78.1,78.2,75.5,76.2,10265393,72.85,4.59,74.19,58.35,0.8
20260629,77.5,78.8,75.7,76.9,6460899,73.19,5.07,74.7,58.91,0.51
20260630,77.2,77.7,76.1,76.3,7513000,73.45,3.88,75.16,59.46,0.61
20260701,76.6,76.6,73.7,74.3,9540000,73.52,1.06,75.5,59.97,0.76
20260702,73,74.3,72.3,73,5788000,73.48,-0.65,75.63,60.47,0.48
20260703,72.9,76,72.7,75,5555355,73.61,1.9,75.76,60.99,0.48
20260706,76.7,81.5,75.4,81,12725000,74.22,9.13,76.33,61.62,1.1
20260707,80,82.4,77.7,78.5,10746676,74.58,5.26,76.91,62.2,0.92
20260708,79,79.1,76.2,77.7,6556322,74.84,3.82,77.12,62.76,0.59
20260709,79.8,79.9,75.3,76,11979255,74.93,1.42,77.17,63.3,1.15
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 59.99
- over_600_ratio: 57.31
- over_800_ratio: 55.71
- over_1000_ratio: 54.56
- over_400_change_1w: -1.23
- over_800_change_1w: -1.16
- over_1000_change_1w: -1.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.56,,56.21,,54.7,,0,False,False
20260508,61.03,0.47,56.89,0.68,55.01,0.31,1,True,True
20260515,61.28,0.25,57.09,0.2,55.46,0.45,2,True,True
20260522,65.53,4.25,62.18,5.09,60.95,5.49,3,True,True
20260529,60.62,-4.91,57.13,-5.05,55.31,-5.64,0,False,False
20260605,60.77,0.15,57.25,0.12,55.66,0.35,1,True,True
20260612,61.14,0.37,57.11,-0.14,55.43,-0.23,2,False,False
20260618,61.47,0.33,57.34,0.23,55.86,0.43,3,True,True
20260626,61.22,-0.25,56.87,-0.47,55.62,-0.24,0,False,False
20260703,59.99,-1.23,55.71,-1.16,54.56,-1.06,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 8926 | 台汽電 | pattern | 型態觀察 | 54.0 |  |  | pullback_right_side |  | call_inflow | repeated_but_no_breakout | 1.發生變動日期:115/07/01 2.法人名稱:大亞電線電纜股份有限公司 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名:李文彬 6.新任者簡歷:大亞電線電纜股份有限公司銅材暨台北管理處執行顧問 7.異動原因:法人董事指派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）:115/06/30~118/06/29 9.新任生效日期:115/07/01 10.其他應敘明事項:無 |
| 20260709 | 8926 | 台汽電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.發生變動日期:115/07/01 2.法人名稱:大亞電線電纜股份有限公司 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名:李文彬 6.新任者簡歷:大亞電線電纜股份有限公司銅材暨台北管理處執行顧問 7.異動原因:法人董事指派代表人 8.原任期（例xx/xx/xx至xx/xx/xx）:115/06/30~118/06/29 9.新任生效日期:115/07/01 10.其他應敘明事項:無；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 8926 | 台汽電 | 13 | 6 | 5 | 10 | 18 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 18 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 8926 | 台汽電 | 4 | 0 | 1489140.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
