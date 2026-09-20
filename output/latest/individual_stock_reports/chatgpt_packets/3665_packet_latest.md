# INDIVIDUAL STOCK CHATGPT PACKET - 3665 貿聯-KY

## Metadata
- generated_at: 2026-09-20 22:16:59 Asia/Taipei
- stock_id: 3665
- stock_name: 貿聯-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 357
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260918
- open: 2060
- high: 2210
- low: 2045
- close: 2210
- volume: 6471964
- ma5: 2030
- ema23_primary: 2068.08
- distance_to_ema23_pct: 6.86
- ma20: 2064
- ma60: 2069.92
- ma120: 2178
- return_5d: 17.87
- return_20d: -2.86
- volume_ratio: 2.07
- distance_to_ma20_pct_auxiliary: 7.07
- distance_to_high_60_pct: -13.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
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
20260907,2175,2185,2060,2070,2560427,2149.09,-3.68,2163.75,2085.5,0.86
20260908,2070,2070,1930,1935,3246234,2131.25,-9.21,2150.5,2079.25,1.09
20260909,1935,2015,1890,1975,2477275,2118.23,-6.76,2141.5,2074.42,0.84
20260910,1960,1975,1925,1930,930001,2102.54,-8.21,2127.75,2071.25,0.33
20260911,1880,1890,1850,1875,1944589,2083.58,-10.01,2111.5,2067.67,0.68
20260914,1825,2000,1810,1955,2220323,2072.86,-5.69,2102.5,2065.25,0.77
20260915,1940,2020,1925,1980,2594783,2065.13,-4.12,2089.5,2065.08,0.91
20260916,1980,2030,1935,1995,2539303,2059.28,-3.12,2079.25,2065,0.88
20260917,2035,2085,1985,2010,3284559,2055.17,-2.2,2067.25,2065.08,1.1
20260918,2060,2210,2045,2210,6471964,2068.08,6.86,2064,2069.92,2.07
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 61.77
- over_600_ratio: 56.34
- over_800_ratio: 49.27
- over_1000_ratio: 44.37
- over_400_change_1w: 0.37
- over_800_change_1w: -0.91
- over_1000_change_1w: 0.51
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
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
20260911,61.4,-0.22,50.18,0.49,43.86,-0.9,1,False,True
20260918,61.77,0.37,49.27,-0.91,44.37,0.51,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3665 | 貿聯-KY | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 3665 | 貿聯-KY | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3665 | 貿聯-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  | call_put_bullish | stale_signal | 1.事實發生日:115/08/21 2.發生緣由:本公司偵測到部份資訊系統遭受網路安全事件。 3.處理過程: 本公司於偵測到異常後，已立即啟動資安應變機制與隔離受影響之資訊系統措施 ，進行全面清查與復原作業，並同步委請外部資安專家協助復原與調查。 4.預計可能損失或影響:經初步評估對公司整體營運及財務無重大影響。 5.可能獲得保險理賠之金額:評估中。 6.改善情形及未來因應措施: 本公司將持續提升網路與資訊基礎架構之資安防護姿態（security posture） ，以確保資料安全與營運韌性。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3665 | 貿聯-KY | 4 | 4 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3665 | 貿聯-KY | 304 | 9 | 64382380.0 | 188960.0 | 340.72 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
