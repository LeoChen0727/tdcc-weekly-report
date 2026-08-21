# INDIVIDUAL STOCK CHATGPT PACKET - 2476 鉅祥

## Metadata
- generated_at: 2026-08-21 22:27:01 Asia/Taipei
- stock_id: 2476
- stock_name: 鉅祥
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
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
- date: 20260821
- open: 119
- high: 120.5
- low: 114.5
- close: 116.5
- volume: 1915312
- ma5: 118.8
- ema23_primary: 120.77
- distance_to_ema23_pct: -3.53
- ma20: 119.28
- ma60: 122.84
- ma120: 112.16
- return_5d: -2.92
- return_20d: -2.1
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: -2.33
- distance_to_high_60_pct: -16.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,118.5,120,115.5,118.5,1531494,123.45,-4.01,125.88,122.58,0.43
20260728,113,114.5,110.5,111,2296392,122.42,-9.33,125.1,122.47,0.65
20260729,111.5,112.5,100.5,106,3979833,121.05,-12.43,123.9,122.34,1.13
20260730,105,109,102.5,105.5,1760534,119.75,-11.9,122.75,122.17,0.52
20260731,115,115,109,113.5,1687661,119.23,-4.81,121.72,122.16,0.53
20260803,112.5,120.5,111.5,119,1740390,119.21,-0.18,121.03,122.23,0.58
20260804,118,121.5,118,119,1109853,119.19,-0.16,120.17,122.35,0.39
20260805,122,127,122,124.5,2041019,119.64,4.07,119.85,122.43,0.77
20260806,124,128,120.5,127.5,1879952,120.29,5.99,119.62,122.58,0.79
20260807,125.5,128,124,125.5,1042657,120.73,3.95,119.45,122.7,0.45
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
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 67.55
- over_600_ratio: 64.92
- over_800_ratio: 62.19
- over_1000_ratio: 61.02
- over_400_change_1w: -0.46
- over_800_change_1w: -0.12
- over_1000_change_1w: 0.74
- tdcc_consecutive_up_weeks: 13
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,63.26,0.87,56.99,1.42,56.17,1.82,2,True,True
20260605,62.91,-0.35,57.94,0.95,55.16,-1.01,3,False,True
20260612,63.65,0.74,57.95,0.01,56.73,1.57,4,True,True
20260618,64.42,0.77,57.87,-0.08,56.67,-0.06,5,False,False
20260626,65.76,1.34,59.46,1.59,57.81,1.14,6,True,True
20260703,66.2,0.44,60.2,0.74,57.75,-0.06,7,False,True
20260709,66.28,0.08,59.76,-0.44,58.13,0.38,8,False,True
20260717,67.21,0.93,60.83,1.07,58.81,0.68,9,True,True
20260724,67.02,-0.19,61.12,0.29,59.53,0.72,10,False,True
20260731,67.32,0.3,61.11,-0.01,59.91,0.38,11,False,True
20260807,68.01,0.69,62.31,1.2,60.28,0.37,12,False,True
20260814,67.55,-0.46,62.19,-0.12,61.02,0.74,13,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2476 | 鉅祥 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名: 馬淑琴小姐 廖雅苓小姐 陳宏毅先生 劉思敏小姐 6.新任者簡歷: 馬淑琴小姐  佳霖會計師事務所會計師 廖雅苓小姐  美商應用材料股份有限公司供應商品管經理 陳宏毅先生  財政部國有財產局科長 劉思敏小姐  信昌機械廠股份有限公司桃園分公司財務處副理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:  新任 8.異動原因:配合本公司115年6月12日股東會董事全面改選，  第5屆薪資報酬委員會委員任期屆滿，故重新委任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/08/04~115/06/08 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 2476 | 鉅祥 | revenue_breakout_low_response | 營收爆發低反應股 | 17 | 23 | A_優先追蹤 |  |  | no_signal | repeated_but_no_breakout | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:不適用 4.舊任者簡歷:不適用 5.新任者姓名: 馬淑琴小姐 廖雅苓小姐 陳宏毅先生 劉思敏小姐 6.新任者簡歷: 馬淑琴小姐  佳霖會計師事務所會計師 廖雅苓小姐  美商應用材料股份有限公司供應商品管經理 陳宏毅先生  財政部國有財產局科長 劉思敏小姐  信昌機械廠股份有限公司桃園分公司財務處副理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）:  新任 8.異動原因:配合本公司115年6月12日股東會董事全面改選，  第5屆薪資報酬委員會委員任期屆滿，故重新委任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/08/04~115/06/08 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2476 | 鉅祥 | 34 | 6 | 5 | 10 | 20 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 20 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2476 | 鉅祥 | 66 | 0 | 4132310.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
