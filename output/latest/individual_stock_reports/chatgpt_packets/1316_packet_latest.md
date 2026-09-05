# INDIVIDUAL STOCK CHATGPT PACKET - 1316 上曜

## Metadata
- generated_at: 2026-09-05 22:15:25 Asia/Taipei
- stock_id: 1316
- stock_name: 上曜
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 347
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1316_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1316_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1316_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1316_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1316.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1316.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1316.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1316.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1316_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1316_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1316_latest.md?ref=main

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
- date: 20260904
- open: 10.8
- high: 10.8
- low: 10.55
- close: 10.6
- volume: 2288111
- ma5: 10.81
- ema23_primary: 10.74
- distance_to_ema23_pct: -1.29
- ma20: 10.75
- ma60: 10.49
- ma120: 10.96
- return_5d: -4.93
- return_20d: 5.47
- volume_ratio: 0.5
- distance_to_ma20_pct_auxiliary: -1.37
- distance_to_high_60_pct: -15.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,10.05,10.1,9.97,10.05,1019099,10.14,-0.86,10.1,10.39,0.68
20260811,10.05,10.15,9.99,10.05,1666702,10.13,-0.79,10.09,10.38,1.14
20260812,10.1,10.3,10.1,10.25,1886399,10.14,1.08,10.08,10.37,1.27
20260813,10.25,10.25,10,10,1683345,10.13,-1.27,10.06,10.36,1.12
20260814,10.05,10.1,9.98,10,1865881,10.12,-1.16,10.06,10.35,1.29
20260817,10.2,10.8,10.2,10.8,6532040,10.17,6.15,10.09,10.35,3.87
20260818,10.6,10.65,10.35,10.45,2191846,10.2,2.48,10.1,10.35,1.26
20260819,10.3,10.6,10.25,10.6,1386924,10.23,3.61,10.11,10.36,0.79
20260820,10.65,10.9,10.5,10.65,3262176,10.27,3.74,10.13,10.37,1.75
20260821,10.75,11.35,10.75,11.2,10948958,10.34,8.28,10.18,10.38,4.59
20260824,11.55,11.95,11.2,11.3,10301476,10.42,8.41,10.24,10.4,3.59
20260825,11.1,11.2,10.8,11.05,4379692,10.48,5.48,10.29,10.42,1.49
20260826,11.2,11.8,11.15,11.6,7382497,10.57,9.75,10.39,10.44,2.38
20260827,11.75,12.5,11.5,11.75,15123908,10.67,10.14,10.5,10.46,3.97
20260828,11.85,11.95,11.05,11.15,9614361,10.71,4.13,10.56,10.47,2.28
20260831,10.95,11.05,10.75,10.95,2944664,10.73,2.07,10.6,10.48,0.68
20260901,10.95,11.1,10.85,10.95,3030294,10.75,1.89,10.65,10.48,0.69
20260902,10.85,11,10.75,10.8,1481541,10.75,0.46,10.69,10.49,0.34
20260903,10.9,11.05,10.7,10.75,1882638,10.75,-0.01,10.72,10.49,0.42
20260904,10.8,10.8,10.55,10.6,2288111,10.74,-1.29,10.75,10.49,0.5
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 41.88
- over_600_ratio: 37.57
- over_800_ratio: 33.63
- over_1000_ratio: 32.61
- over_400_change_1w: -0.83
- over_800_change_1w: -1.29
- over_1000_change_1w: -0.6
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,38.46,-0.06,30.59,0.21,28.5,-0.03,1,False,True
20260626,38.69,0.23,30.45,-0.14,28.36,-0.14,2,False,False
20260703,39.01,0.32,30.7,0.25,28.12,-0.24,3,False,True
20260709,38.94,-0.07,30.73,0.03,28.12,0,4,False,True
20260717,42.89,3.95,35.12,4.39,32.68,4.56,5,True,True
20260724,43.08,0.19,34.97,-0.15,32.76,0.08,6,False,True
20260731,42.76,-0.32,34.92,-0.05,32.76,0,7,False,False
20260807,43.1,0.34,34.91,-0.01,32.96,0.2,8,False,True
20260814,42.94,-0.16,35.19,0.28,33.23,0.27,9,False,True
20260821,42.79,-0.15,35.12,-0.07,33.17,-0.06,0,False,False
20260828,42.71,-0.08,34.92,-0.2,33.21,0.04,1,False,True
20260904,41.88,-0.83,33.63,-1.29,32.61,-0.6,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 1316 | 上曜 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  承認114年度虧損撥補案。                  經票決結果:贊成205,280,383權，反對1,458,697權                  廢票0權，贊成占表決總權數95.30%，本案照                  原議案通過。 3.重要決議事項二、章程修訂:                  修訂本公司章程案。                  經票決結果:贊成206,124,489權，反對680,662權                  廢票0權，贊成占表決總權數95.70%，本案照                  原議案通過。 4.重要決議事項三、營業報告書及財務報表:                  承認114年度營業報告書及財務報表案。                  經票決結果:贊成206,092,573權，反對655,634權，                  廢票0權，贊成占表決總權數95.68%，本案照                  原議案通過。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:                   (1) 本公司114年度營業狀況報告。                   (2) 審計委員會查核本公司114年度決算表冊報告書。                   (3) 募集與發行可轉換公司債有關事項報告。                   (4) 114年私募普通股案執行情形。                   (5) 擬辦理私募普通股案。                       經票決結果:贊成204,537,662權，反對2,257,514權                       廢票0權，贊成占表決總權數94.96%，本案照                       原議案通過。 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 1316 | 上曜 | revenue_pullback | 營收成長股價回檔 | 84.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  承認114年度虧損撥補案。                  經票決結果:贊成205,280,383權，反對1,458,697權                  廢票0權，贊成占表決總權數95.30%，本案照                  原議案通過。 3.重要決議事項二、章程修訂:                  修訂本公司章程案。                  經票決結果:贊成206,124,489權，反對680,662權                  廢票0權，贊成占表決總權數95.70%，本案照                  原議案通過。 4.重要決議事項三、營業報告書及財務報表:                  承認114年度營業報告書及財務報表案。                  經票決結果:贊成206,092,573權，反對655,634權，                  廢票0權，贊成占表決總權數95.68%，本案照                  原議案通過。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:                   (1) 本公司114年度營業狀況報告。                   (2) 審計委員會查核本公司114年度決算表冊報告書。                   (3) 募集與發行可轉換公司債有關事項報告。                   (4) 114年私募普通股案執行情形。                   (5) 擬辦理私募普通股案。                       經票決結果:贊成204,537,662權，反對2,257,514權                       廢票0權，贊成占表決總權數94.96%，本案照                       原議案通過。 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260904 | 1316 | 上曜 | revenue_breakout_low_response | 營收爆發低反應股 | 16 | 29 | B_可觀察 |  |  |  | stale_signal | 1.股東常會日期:115/06/24 2.重要決議事項一、盈餘分配或盈虧撥補:                  承認114年度虧損撥補案。                  經票決結果:贊成205,280,383權，反對1,458,697權                  廢票0權，贊成占表決總權數95.30%，本案照                  原議案通過。 3.重要決議事項二、章程修訂:                  修訂本公司章程案。                  經票決結果:贊成206,124,489權，反對680,662權                  廢票0權，贊成占表決總權數95.70%，本案照                  原議案通過。 4.重要決議事項三、營業報告書及財務報表:                  承認114年度營業報告書及財務報表案。                  經票決結果:贊成206,092,573權，反對655,634權，                  廢票0權，贊成占表決總權數95.68%，本案照                  原議案通過。 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:                   (1) 本公司114年度營業狀況報告。                   (2) 審計委員會查核本公司114年度決算表冊報告書。                   (3) 募集與發行可轉換公司債有關事項報告。                   (4) 114年私募普通股案執行情形。                   (5) 擬辦理私募普通股案。                       經票決結果:贊成204,537,662權，反對2,257,514權                       廢票0權，贊成占表決總權數94.96%，本案照                       原議案通過。 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 1316 | 上曜 | 15 | 6 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
