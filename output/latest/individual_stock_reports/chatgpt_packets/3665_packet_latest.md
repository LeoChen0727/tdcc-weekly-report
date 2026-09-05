# INDIVIDUAL STOCK CHATGPT PACKET - 3665 貿聯-KY

## Metadata
- generated_at: 2026-09-05 15:53:28 Asia/Taipei
- stock_id: 3665
- stock_name: 貿聯-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3665_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3665_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3665_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3665_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3665_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3665_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3665_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3665.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3665.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3665.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3665.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3665_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3665_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3665_latest.md?ref=main

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
- date: 20260904
- open: 2135
- high: 2175
- low: 2115
- close: 2145
- volume: 1458584
- ma5: 2180
- ema23_primary: 2156.28
- distance_to_ema23_pct: -0.52
- ma20: 2169.75
- ma60: 2087
- ma120: 2156.29
- return_5d: -5.09
- return_20d: -2.5
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: -1.14
- distance_to_high_60_pct: -16.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,2190,2300,2115,2190,4361567,2125.4,3.04,2090.25,2081.83,1.12
20260811,2145,2205,2070,2200,3555430,2131.61,3.21,2111.5,2081,0.91
20260812,2195,2195,2130,2155,2983890,2133.56,1,2123.75,2082,0.76
20260813,2180,2275,2165,2205,2695004,2139.52,3.06,2136.25,2085,0.69
20260814,2235,2245,2180,2200,1633275,2144.56,2.59,2158,2088.5,0.43
20260817,2185,2185,2095,2135,1878863,2143.76,-0.41,2173.75,2091.33,0.5
20260818,2130,2310,2125,2240,3107456,2151.78,4.1,2185.75,2092.75,0.83
20260819,2150,2210,2120,2200,2061571,2155.8,2.05,2190,2092.33,0.57
20260820,2225,2255,2180,2250,1488154,2163.65,3.99,2188.25,2090.08,0.44
20260821,2270,2360,2225,2275,3470516,2172.93,4.7,2191.75,2090.25,1.03
20260824,2275,2275,2050,2050,4781290,2162.68,-5.21,2186.75,2089.17,1.36
20260825,2035,2080,2010,2075,2634314,2155.38,-3.73,2179.75,2088.5,0.76
20260826,2035,2055,1930,2005,4874749,2142.85,-6.43,2175.5,2087.17,1.4
20260827,2040,2070,1980,2055,2917164,2135.52,-3.77,2182.75,2086.08,0.86
20260828,2075,2260,2070,2260,4068757,2145.9,5.32,2190.75,2087.17,1.17
20260831,2230,2240,2105,2170,3131169,2147.91,1.03,2194.5,2084.92,0.92
20260901,2190,2375,2165,2315,4568188,2161.83,7.09,2195.25,2087.58,1.33
20260902,2200,2235,2165,2170,3399837,2162.51,0.35,2186,2087.08,1
20260903,2170,2180,2100,2100,2445221,2157.3,-2.66,2172.5,2087.17,0.75
20260904,2135,2175,2115,2145,1458584,2156.28,-0.52,2169.75,2087,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 61.62
- over_600_ratio: 57.04
- over_800_ratio: 49.69
- over_1000_ratio: 44.76
- over_400_change_1w: -0.29
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,59.17,-0.43,49.23,1.18,44.71,0.75,2,False,True
20260626,58.59,-0.58,46.62,-2.61,41.54,-3.17,0,False,False
20260703,58.56,-0.03,46.99,0.37,41.89,0.35,1,False,True
20260709,58.76,0.2,47.65,0.66,42.61,0.72,2,True,True
20260717,60.91,2.15,47.63,-0.02,43.53,0.92,3,False,True
20260724,60.74,-0.17,47.95,0.32,43.84,0.31,4,False,True
20260731,61,0.26,49.54,1.59,43.63,-0.21,5,False,True
20260807,62.07,1.07,49.14,-0.4,45.07,1.44,6,False,True
20260814,62.24,0.17,50.41,1.27,44.48,-0.59,7,False,True
20260821,63.23,0.99,51.53,1.12,45.8,1.32,8,True,True
20260828,61.91,-1.32,49.73,-1.8,44.8,-1,0,False,False
20260904,61.62,-0.29,49.69,-0.04,44.76,-0.04,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3665 | 貿聯-KY | pattern | 型態觀察 | 45.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 3665 | 貿聯-KY | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 3665 | 貿聯-KY | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 56 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3665 | 貿聯-KY | 2 | 2 | 4 | 9 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3665 | 貿聯-KY | 312 | 10 | 20110850.0 | 293030.0 | 68.63 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
