# INDIVIDUAL STOCK CHATGPT PACKET - 1605 華新

## Metadata
- generated_at: 2026-06-30 22:26:23 Asia/Taipei
- stock_id: 1605
- stock_name: 華新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 294
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1605_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1605_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1605_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1605_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1605_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1605_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1605_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1605.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1605.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1605.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1605.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1605_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1605_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1605_latest.md?ref=main

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
- date: 20260630
- open: 35.95
- high: 37.85
- low: 35.95
- close: 37.2
- volume: 26577000
- ma5: 36.77
- ema23_primary: 37.33
- distance_to_ema23_pct: -0.36
- ma20: 38.13
- ma60: 35
- ma120: 35.37
- return_5d: -1.59
- return_20d: -6.3
- volume_ratio: 0.44
- distance_to_ma20_pct_auxiliary: -2.45
- distance_to_high_60_pct: -15.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,39.7,40.9,38.7,40.45,81787873,35.85,12.85,35.91,33.01,1.3
20260603,41.55,43.4,40.7,42.7,148415791,36.42,17.25,36.41,33.18,2.16
20260604,42.3,44,41.6,41.6,112532724,36.85,12.89,36.7,33.36,1.63
20260605,41.3,41.3,38.25,39.55,70754422,37.07,6.68,36.99,33.5,1.06
20260608,35.65,36.45,35.6,35.8,93563224,36.97,-3.16,37.03,33.53,1.38
20260609,36.35,36.7,35.5,36.5,45361586,36.93,-1.16,37.13,33.61,0.67
20260610,36.3,36.7,34.75,34.8,43859228,36.75,-5.31,37.11,33.66,0.65
20260611,34.3,34.6,33.2,34.3,31568318,36.55,-6.15,37.04,33.68,0.48
20260612,35.3,37.7,35.3,37.7,56774874,36.64,2.88,37.18,33.74,0.86
20260615,39.05,40.7,38.75,40,74844979,36.92,8.33,37.45,33.84,1.1
20260616,40.05,40.4,39,39.15,48695660,37.11,5.5,37.73,33.96,0.71
20260617,39.3,39.3,38.15,38.7,36776120,37.24,3.92,38.02,34.08,0.53
20260618,39.2,40.45,38.4,39,61750339,37.39,4.31,38.19,34.22,0.89
20260622,40.05,42.25,40.05,40.75,91792161,37.67,8.18,38.4,34.4,1.29
20260623,40.5,40.5,37.65,37.8,72133897,37.68,0.32,38.4,34.49,1.01
20260624,37.15,38.4,36.6,38.15,27657979,37.72,1.15,38.45,34.61,0.39
20260625,38.6,39.7,37.65,37.7,31695308,37.72,-0.04,38.45,34.73,0.45
20260626,37.6,37.6,35.35,35.4,43243213,37.52,-5.66,38.42,34.81,0.62
20260629,35.7,36.1,35.1,35.4,17681140,37.35,-5.21,38.26,34.9,0.27
20260630,35.95,37.85,35.95,37.2,26577000,37.33,-0.36,38.13,35,0.44
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 73.62
- over_600_ratio: 72.52
- over_800_ratio: 71.92
- over_1000_ratio: 71.22
- over_400_change_1w: -0.05
- over_800_change_1w: -0.23
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.77,,68.06,,67.43,,0,False,False
20260508,71.6,1.83,69.96,1.9,69.33,1.9,1,True,True
20260515,71.01,-0.59,69.27,-0.69,68.6,-0.73,0,False,False
20260522,71.44,0.43,69.8,0.53,68.96,0.36,1,True,True
20260529,71.94,0.5,70.29,0.49,69.55,0.59,2,True,True
20260605,73.86,1.92,72.26,1.97,71.62,2.07,3,True,True
20260612,72.92,-0.94,71.42,-0.84,70.69,-0.93,0,False,False
20260618,73.67,0.75,72.15,0.73,71.4,0.71,1,True,True
20260626,73.62,-0.05,71.92,-0.23,71.22,-0.18,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1605 | 華新 | pattern | 型態觀察 | 45.0 |  |  | pullback_entry_zone |  | call_inflow | stale_signal | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管(如:執行長、營運長、 行銷長及策略長等)、財務主管、會計主管、公司治理主管、資訊安全長、研發主管、 內部稽核主管或訴訟及非訟代理人）:重要營運主管 2.發生變動日期:115/06/29 3.舊任者姓名、級職及簡歷:  數位智能發展組織總經理:吳明機(職務調整)  歐洲區域執行長:不適用 4.新任者姓名、級職及簡歷:  數位智能發展組織總經理:不適用  歐洲區域執行長:Massimiliano Burelli / Cogne Acciai Speciali S.p.A.董事兼 執行長 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、「退休」、「死亡」、「新 任」或「解任」）:新任 6.異動原因:公司組織調整 7.生效日期:115/07/01 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1605 | 華新 | 2 | 2 | 3 | 8 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 1605 | 華新 | 147 | 0 | 9555010.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
