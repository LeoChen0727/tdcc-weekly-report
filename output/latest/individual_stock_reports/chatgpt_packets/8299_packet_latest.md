# INDIVIDUAL STOCK CHATGPT PACKET - 8299 群聯

## Metadata
- generated_at: 2026-09-26 22:17:53 Asia/Taipei
- stock_id: 8299
- stock_name: 群聯
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: True
- sell_strategy_summary_exists: True
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8299_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8299_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8299_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8299_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8299.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8299.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8299.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8299.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8299_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8299_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8299_latest.md?ref=main

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
- date: 20260924
- open: 2195
- high: 2195
- low: 2095
- close: 2125
- volume: 3897000
- ma5: 2163
- ema23_primary: 2075.17
- distance_to_ema23_pct: 2.4
- ma20: 2073.25
- ma60: 2017.42
- ma120: 2126.46
- return_5d: 7.87
- return_20d: -1.39
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: 2.5
- distance_to_high_60_pct: -12.19

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,2170,2195,2115,2150,2786000,2050.06,4.88,2047,2114.67,0.56
20260831,2130,2185,2110,2165,16851000,2059.64,5.12,2067.25,2107.75,3.05
20260901,2185,2185,2080,2125,3863000,2065.08,2.9,2082.5,2102.33,0.7
20260902,2100,2115,2060,2065,2900000,2065.08,-0,2093.5,2099.25,0.53
20260903,2085,2120,1990,2000,3126000,2059.65,-2.9,2092.25,2093.25,0.58
20260904,2025,2050,1970,2015,2747000,2055.93,-1.99,2092,2090.92,0.53
20260907,2075,2115,2065,2095,2545000,2059.19,1.74,2094.75,2089.17,0.5
20260908,2115,2160,2080,2085,2551000,2061.34,1.15,2094.5,2085.42,0.5
20260909,2100,2125,2070,2085,1866000,2063.31,1.05,2088.25,2081.5,0.38
20260910,2100,2120,2065,2065,2295000,2063.45,0.07,2077.5,2076.33,0.49
20260911,2000,2000,1920,1990,4480000,2057.33,-3.27,2073,2070.67,1.09
20260914,1920,1960,1910,1935,2062000,2047.14,-5.48,2065.5,2060.75,0.52
20260915,1935,1960,1900,1920,2009000,2036.54,-5.72,2061.5,2049.75,0.52
20260916,1930,1985,1910,1985,2818000,2032.25,-2.32,2062.5,2042.33,0.74
20260917,2000,2040,1950,1970,2601000,2027.06,-2.81,2061.25,2033.5,0.69
20260918,2030,2140,2010,2140,6143000,2036.47,5.08,2064.5,2027.92,1.58
20260921,2145,2190,2115,2150,4229000,2045.93,5.09,2065.25,2025.25,1.11
20260922,2195,2240,2165,2185,4869000,2057.52,6.2,2070.25,2022.67,1.26
20260923,2280,2350,2200,2215,7052000,2070.64,6.97,2074.75,2019.83,1.73
20260924,2195,2195,2095,2125,3897000,2075.17,2.4,2073.25,2017.42,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 39.55
- over_600_ratio: 36.11
- over_800_ratio: 33.19
- over_1000_ratio: 29.18
- over_400_change_1w: 1.47
- over_800_change_1w: 1.98
- over_1000_change_1w: 1.75
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,45.05,-0.48,35.99,-1.93,33.98,-0.68,0,False,False
20260717,44.14,-0.91,36.55,0.56,34.96,0.98,1,False,True
20260724,43.59,-0.55,36.89,0.34,33.16,-1.8,2,False,True
20260731,42.31,-1.28,35.63,-1.26,33.18,0.02,3,False,True
20260807,43.36,1.05,35.8,0.17,34.62,1.44,4,True,True
20260814,43.38,0.02,36.77,0.97,34.76,0.14,5,True,True
20260821,41.53,-1.85,35.67,-1.1,32.44,-2.32,0,False,False
20260828,42.41,0.88,36.35,0.68,34.36,1.92,1,True,True
20260904,39.21,-3.2,30.55,-5.8,27.3,-7.06,0,False,False
20260911,39.31,0.1,31.24,0.69,27.89,0.59,1,True,True
20260918,38.08,-1.23,31.21,-0.03,27.43,-0.46,0,False,False
20260924,39.55,1.47,33.19,1.98,29.18,1.75,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 8299 | 群聯 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/09/15 1.召開法人說明會之日期：115/09/15 2.召開法人說明會之時間：13 時 30 分 3.召開法人說明會之地點：UBS證券安排之實體會議 4.法人說明會擇要訊息：本公司受邀參加UBS證券舉辦之投資論壇，說明營運績效等。 5.其他應敘明事項：會議細節請洽UBS證券 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 8299 | 群聯 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/09/15 1.召開法人說明會之日期：115/09/15 2.召開法人說明會之時間：13 時 30 分 3.召開法人說明會之地點：UBS證券安排之實體會議 4.法人說明會擇要訊息：本公司受邀參加UBS證券舉辦之投資論壇，說明營運績效等。 5.其他應敘明事項：會議細節請洽UBS證券 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 8299 | 群聯 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 21 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/09/15 1.召開法人說明會之日期：115/09/15 2.召開法人說明會之時間：13 時 30 分 3.召開法人說明會之地點：UBS證券安排之實體會議 4.法人說明會擇要訊息：本公司受邀參加UBS證券舉辦之投資論壇，說明營運績效等。 5.其他應敘明事項：會議細節請洽UBS證券 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 8299 | 群聯 | 27 | 27 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
