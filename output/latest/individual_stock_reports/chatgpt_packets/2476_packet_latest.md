# INDIVIDUAL STOCK CHATGPT PACKET - 2476 鉅祥

## Metadata
- generated_at: 2026-09-06 22:16:27 Asia/Taipei
- stock_id: 2476
- stock_name: 鉅祥
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2476_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2476_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2476.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2476.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2476.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2476.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2476_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2476_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2476_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- confidence_level: medium
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
- date: 20260904
- open: 124.5
- high: 124.5
- low: 119.5
- close: 121
- volume: 1628089
- ma5: 124.4
- ema23_primary: 122.5
- distance_to_ema23_pct: -1.23
- ma20: 122.55
- ma60: 123.25
- ma120: 115.93
- return_5d: -3.59
- return_20d: -3.59
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: -1.26
- distance_to_high_60_pct: -13.57

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,128.5,128.5,124.5,126,1948850,121.17,3.99,119.42,122.82,0.86
20260811,127,127,122,124.5,1580685,121.44,2.52,119.55,122.97,0.75
20260812,124.5,128,123,128,2235083,121.99,4.93,119.47,123.13,1.07
20260813,126,126.5,121.5,123,2043314,122.07,0.76,119.05,123.27,0.98
20260814,123,123,118.5,120,2064328,121.9,-1.56,119.12,123.37,1.03
20260817,118.5,120,117,119.5,949009,121.7,-1.81,119.42,123.36,0.54
20260818,118.5,123,117,119.5,2115786,121.52,-1.66,119.55,123.33,1.19
20260819,117.5,121,117,119,2081413,121.31,-1.9,119.45,123.24,1.14
20260820,118.5,121,118,119.5,1377367,121.16,-1.37,119.4,123.05,0.75
20260821,119,120.5,114.5,116.5,1915312,120.77,-3.53,119.28,122.84,1.02
20260824,116,118,114,115.5,858844,120.33,-4.01,119.12,122.73,0.47
20260825,115,120.5,112.5,120.5,2196705,120.34,0.13,119.6,122.71,1.2
20260826,120,127,119.5,125.5,3530774,120.77,3.91,120.58,122.77,1.95
20260827,125.5,128,124,126.5,2486571,121.25,4.33,121.62,122.89,1.35
20260828,126.5,127.5,123.5,125.5,2057693,121.61,3.2,122.22,122.93,1.1
20260831,124.5,126,122.5,125.5,1342005,121.93,2.93,122.55,123.01,0.73
20260901,126,130,125.5,127.5,2318908,122.39,4.17,122.97,123.13,1.22
20260902,127,127.5,125,125.5,989187,122.65,2.32,123.03,123.26,0.53
20260903,126.5,126.5,121.5,122.5,1245283,122.64,-0.11,122.78,123.21,0.68
20260904,124.5,124.5,119.5,121,1628089,122.5,-1.23,122.55,123.25,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 67.87
- over_600_ratio: 65.45
- over_800_ratio: 61.64
- over_1000_ratio: 59.23
- over_400_change_1w: -0.01
- over_800_change_1w: -0.62
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 16
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,64.42,0.77,57.87,-0.08,56.67,-0.06,5,False,False
20260626,65.76,1.34,59.46,1.59,57.81,1.14,6,True,True
20260703,66.2,0.44,60.2,0.74,57.75,-0.06,7,False,True
20260709,66.28,0.08,59.76,-0.44,58.13,0.38,8,False,True
20260717,67.21,0.93,60.83,1.07,58.81,0.68,9,True,True
20260724,67.02,-0.19,61.12,0.29,59.53,0.72,10,False,True
20260731,67.32,0.3,61.11,-0.01,59.91,0.38,11,False,True
20260807,68.01,0.69,62.31,1.2,60.28,0.37,12,False,True
20260814,67.55,-0.46,62.19,-0.12,61.02,0.74,13,False,True
20260821,67.31,-0.24,62.19,0,60.58,-0.44,14,False,False
20260828,67.88,0.57,62.26,0.07,59.43,-1.15,15,False,True
20260904,67.87,-0.01,61.64,-0.62,59.23,-0.2,16,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2476 | 鉅祥 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名: 馬淑琴小姐 廖雅苓小姐 陳宏毅先生 劉思敏小姐 6.新任者簡歷: 馬淑琴小姐  佳霖會計師事務所會計師 廖雅苓小姐  美商應用材料股份有限公司供應商品管經理 陳宏毅先生  財政部國有財產局科長 劉思敏小姐  信昌機械廠股份有限公司桃園分公司財務處副理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:  新任 8.異動原因:配合本公司115年6月12日股東會董事全面改選，  第5屆薪資報酬委員會委員任期屆滿，故重新委任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/08/04~115/06/08 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2476 | 鉅祥 | revenue_breakout_low_response | 營收爆發低反應股 | 11 | 63 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名: 馬淑琴小姐 廖雅苓小姐 陳宏毅先生 劉思敏小姐 6.新任者簡歷: 馬淑琴小姐  佳霖會計師事務所會計師 廖雅苓小姐  美商應用材料股份有限公司供應商品管經理 陳宏毅先生  財政部國有財產局科長 劉思敏小姐  信昌機械廠股份有限公司桃園分公司財務處副理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:  新任 8.異動原因:配合本公司115年6月12日股東會董事全面改選，  第5屆薪資報酬委員會委員任期屆滿，故重新委任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/08/04~115/06/08 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2476 | 鉅祥 | 2 | 2 | 4 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2476 | 鉅祥 | 78 | 0 | 4193640.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
