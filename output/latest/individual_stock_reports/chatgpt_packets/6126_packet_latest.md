# INDIVIDUAL STOCK CHATGPT PACKET - 6126 信音

## Metadata
- generated_at: 2026-07-08 22:27:55 Asia/Taipei
- stock_id: 6126
- stock_name: 信音
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 165
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6126_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6126_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6126_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6126_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6126.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6126.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6126.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6126.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6126_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6126_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6126_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
- decision_score_high
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
- date: 20260708
- open: 35.35
- high: 37.45
- low: 34.75
- close: 35.55
- volume: 3868000
- ma5: 35.67
- ema23_primary: 37.07
- distance_to_ema23_pct: -4.09
- ma20: 38.04
- ma60: 35.71
- ma120: 35.08
- return_5d: 0.99
- return_20d: -13.19
- volume_ratio: 1.16
- distance_to_ma20_pct_auxiliary: -6.55
- distance_to_high_60_pct: -20.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,39.95,41.8,38.55,38.6,4059000,37.2,3.76,36.96,33.59,2.83
20260611,39.6,42.45,39.1,41.55,11590000,37.56,10.61,37.41,33.74,5.94
20260612,42.05,42.95,40.1,40.25,10563000,37.79,6.52,37.78,33.88,4.49
20260615,40.9,43.3,40.1,41.65,6639000,38.11,9.29,38.17,34.01,2.55
20260616,41.95,42,39.4,39.4,3814000,38.22,3.1,38.46,34.1,1.4
20260617,39.5,40.7,38.9,40.4,2112000,38.4,5.21,38.78,34.23,0.79
20260618,40.6,41.25,40,40.3,1984000,38.56,4.52,39.01,34.38,0.77
20260622,40.9,40.9,39.7,40.15,2463000,38.69,3.77,39.22,34.53,0.91
20260623,40.7,40.75,39.25,39.4,2517000,38.75,1.68,39.38,34.66,0.89
20260624,39,39.8,38.55,39.8,1430000,38.84,2.48,39.55,34.81,0.5
20260625,40.05,41.1,39.5,39.6,2876000,38.9,1.8,39.77,34.96,0.95
20260626,39.6,39.6,35.65,35.75,4233000,38.64,-7.47,39.79,35.06,1.31
20260629,35.8,36.25,34.3,34.65,1869000,38.31,-9.54,39.75,35.16,0.56
20260630,35.7,35.9,35,35.8,994000,38.1,-6.03,39.67,35.26,0.29
20260701,36.1,36.8,35.2,35.2,1159000,37.86,-7.01,39.49,35.36,0.34
20260702,35.45,36.5,34.9,36,957000,37.7,-4.51,39.16,35.47,0.27
20260703,36,36.35,35.75,36.3,771000,37.58,-3.42,38.83,35.55,0.22
20260706,36.5,37.3,35.95,36.35,985000,37.48,-3.02,38.52,35.61,0.28
20260707,36.8,36.8,34.05,34.15,1619000,37.2,-8.21,38.31,35.65,0.48
20260708,35.35,37.45,34.75,35.55,3868000,37.07,-4.09,38.04,35.71,1.16
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 37.63
- over_600_ratio: 36.78
- over_800_ratio: 34.69
- over_1000_ratio: 32.74
- over_400_change_1w: -1.21
- over_800_change_1w: -0.04
- over_1000_change_1w: 0.04
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.86,,29.43,,28.17,,0,False,False
20260508,35.09,0.23,29.5,0.07,28.17,0,1,False,True
20260515,35.24,0.15,29.68,0.18,29.06,0.89,2,True,True
20260522,36.6,1.36,30.58,0.9,28.57,-0.49,3,False,True
20260529,37.63,1.03,32.34,1.76,30.3,1.73,4,True,True
20260605,39.56,1.93,35.35,3.01,34.73,4.43,5,True,True
20260612,39.78,0.22,35.42,0.07,32.66,-2.07,6,False,True
20260618,37.82,-1.96,33.09,-2.33,31.78,-0.88,0,False,False
20260626,38.84,1.02,34.73,1.64,32.7,0.92,1,True,True
20260703,37.63,-1.21,34.69,-0.04,32.74,0.04,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6126 | 信音 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/30 2.經理人或董事之名稱:楊政綱 總經理 3.所擔任該大陸地區事業之公司名稱及職務: 東莞市國聯電子有限公司 董事 4.所擔任該大陸地區事業地址: 廣東省東莞市塘廈鎮永太路3號15棟601室、701室 5.所擔任該大陸地區事業營業項目: 車用連接器、線束的生產、研發、銷售 6.對本公司財務業務之影響程度:子公司轉投資事業 7.經理人或董事如有對該大陸地區事業從事投資者，其投資金額及持股比例: 不適用 8.公司擬採行措施:將於最近一次董事會解除經理人競業禁止限制 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260708 | 6126 | 信音 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 11.0 | A_優先追蹤 |  |  |  | stale_signal | 1.事實發生日:115/06/30 2.經理人或董事之名稱:楊政綱 總經理 3.所擔任該大陸地區事業之公司名稱及職務: 東莞市國聯電子有限公司 董事 4.所擔任該大陸地區事業地址: 廣東省東莞市塘廈鎮永太路3號15棟601室、701室 5.所擔任該大陸地區事業營業項目: 車用連接器、線束的生產、研發、銷售 6.對本公司財務業務之影響程度:子公司轉投資事業 7.經理人或董事如有對該大陸地區事業從事投資者，其投資金額及持股比例: 不適用 8.公司擬採行措施:將於最近一次董事會解除經理人競業禁止限制 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6126 | 信音 | 2 | 2 | 2 | 6 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| status |
| --- |
| no rows |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
