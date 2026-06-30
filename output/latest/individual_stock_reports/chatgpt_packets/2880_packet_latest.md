# INDIVIDUAL STOCK CHATGPT PACKET - 2880 華南金

## Metadata
- generated_at: 2026-06-30 22:26:53 Asia/Taipei
- stock_id: 2880
- stock_name: 華南金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2880_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2880_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2880.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2880.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2880.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2880.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2880_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2880_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2880_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260630
- open: 37.35
- high: 38.15
- low: 37.2
- close: 38
- volume: 16627000
- ma5: 37.44
- ema23_primary: 36.14
- distance_to_ema23_pct: 5.15
- ma20: 36.59
- ma60: 34.34
- ma120: 33.96
- return_5d: 1.2
- return_20d: 15.68
- volume_ratio: 0.36
- distance_to_ma20_pct_auxiliary: 3.85
- distance_to_high_60_pct: -3.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,32.5,34.4,32.4,34.05,115623011,32.18,5.8,32.03,33.39,2.46
20260603,34.15,36.5,33.7,36.4,83036548,32.53,11.88,32.22,33.41,1.65
20260604,36,38.6,35.5,37.7,92745091,32.96,14.37,32.44,33.46,1.73
20260605,37.15,37.25,34.5,34.8,40543106,33.12,5.08,32.51,33.47,0.74
20260608,34.1,34.45,33,33.5,38433694,33.15,1.06,32.52,33.46,0.69
20260609,33.35,35.6,33.35,35.45,40383122,33.34,6.33,32.67,33.48,0.71
20260610,34.8,35.9,34.55,35.35,28108247,33.51,5.5,32.8,33.51,0.49
20260611,35.25,36.3,34.7,35.65,28478851,33.69,5.83,32.95,33.54,0.49
20260612,35.9,37,35.75,36,38300652,33.88,6.26,33.13,33.59,0.64
20260615,37.5,37.5,36.1,36.7,18966806,34.11,7.58,33.37,33.64,0.32
20260616,36.7,37.6,36.55,37.45,27840857,34.39,8.89,33.63,33.71,0.47
20260617,36.95,38.6,36.95,38.1,32919856,34.7,9.79,33.94,33.79,0.55
20260618,38.15,39.2,38,38.35,67936605,35.01,9.55,34.25,33.88,1.11
20260622,38.45,38.5,37.05,37.6,43716046,35.22,6.75,34.53,33.95,0.71
20260623,37.2,38,36.95,37.55,48365107,35.42,6.03,34.88,34.01,0.79
20260624,37.2,37.35,36.25,37,55048004,35.55,4.08,35.23,34.07,0.92
20260625,36.55,38,36.5,38,52957611,35.75,6.29,35.63,34.14,0.9
20260626,36.9,37.75,36.9,36.9,28094453,35.85,2.94,35.99,34.2,0.51
20260629,37.55,37.8,37,37.3,24107283,35.97,3.7,36.34,34.27,0.48
20260630,37.35,38.15,37.2,38,16627000,36.14,5.15,36.59,34.34,0.36
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 81.26
- over_600_ratio: 80.11
- over_800_ratio: 79.46
- over_1000_ratio: 78.8
- over_400_change_1w: 0.06
- over_800_change_1w: 0.06
- over_1000_change_1w: 0.06
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.95,,79.12,,78.44,,0,False,False
20260508,80.86,-0.09,79.03,-0.09,78.36,-0.08,0,False,False
20260515,80.84,-0.02,79.02,-0.01,78.36,0,0,False,False
20260522,80.81,-0.03,79.03,0.01,78.37,0.01,1,False,True
20260529,80.46,-0.35,78.68,-0.35,78.02,-0.35,0,False,False
20260605,81.06,0.6,79.28,0.6,78.59,0.57,1,True,True
20260612,81.07,0.01,79.26,-0.02,78.57,-0.02,2,False,False
20260618,81.2,0.13,79.4,0.14,78.74,0.17,3,True,True
20260626,81.26,0.06,79.46,0.06,78.8,0.06,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2880 | 華南金 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管(如:執行長、營運長、 行銷長及策略長等)、財務主管、會計主管、公司治理主管、資訊安全長、研發主管、 內部稽核主管或訴訟及非訟代理人）:總機構法令遵循主管 2.發生變動日期:115/06/29 3.舊任者姓名、級職及簡歷:許素蓉，華南金控副總經理(總機構法令遵循主管) 4.新任者姓名、級職及簡歷:魯瑞鋒，華南銀行債權管理部經理 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、「退休」、「死亡」、「新 任」或「解任」）:退休 6.異動原因:退休 7.生效日期:115/07/16 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |
| 20260630 | 2880 | 華南金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管(如:執行長、營運長、 行銷長及策略長等)、財務主管、會計主管、公司治理主管、資訊安全長、研發主管、 內部稽核主管或訴訟及非訟代理人）:總機構法令遵循主管 2.發生變動日期:115/06/29 3.舊任者姓名、級職及簡歷:許素蓉，華南金控副總經理(總機構法令遵循主管) 4.新任者姓名、級職及簡歷:魯瑞鋒，華南銀行債權管理部經理 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、「退休」、「死亡」、「新 任」或「解任」）:退休 6.異動原因:退休 7.生效日期:115/07/16 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2880 | 華南金 | 23 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2880 | 華南金 | 2 | 0 | 18100.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
