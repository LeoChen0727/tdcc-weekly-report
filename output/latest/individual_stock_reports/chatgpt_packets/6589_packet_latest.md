# INDIVIDUAL STOCK CHATGPT PACKET - 6589 台康生技

## Metadata
- generated_at: 2026-09-20 22:18:01 Asia/Taipei
- stock_id: 6589
- stock_name: 台康生技
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 287
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6589_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6589_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6589_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6589_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6589_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6589_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6589_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6589.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6589.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6589.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6589.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6589_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6589_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6589_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260918
- open: 51.2
- high: 52.7
- low: 50.2
- close: 52.7
- volume: 1748855
- ma5: 49.91
- ema23_primary: 48.96
- distance_to_ema23_pct: 7.63
- ma20: 48.85
- ma60: 48.4
- ma120: 47.61
- return_5d: 16.34
- return_20d: 2.93
- volume_ratio: 2.82
- distance_to_ma20_pct_auxiliary: 7.88
- distance_to_high_60_pct: -1.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,51.2,52.5,50.1,50.3,514086,49.14,2.36,48.85,47.21,0.67
20260825,50.5,50.5,49.3,49.7,432331,49.19,1.05,49.04,47.34,0.57
20260826,49.8,50.7,49.8,50.5,450509,49.3,2.44,49.27,47.44,0.61
20260827,50.3,51.1,50,50.2,364960,49.37,1.68,49.53,47.55,0.5
20260828,50.2,50.6,49.8,49.85,414947,49.41,0.89,49.78,47.63,0.58
20260831,49.35,49.85,48,48.15,813553,49.31,-2.34,49.88,47.68,1.11
20260901,48,49,47.9,48,676497,49.2,-2.43,49.91,47.74,0.92
20260902,47.65,48.75,47.65,48.5,236897,49.14,-1.3,49.91,47.83,0.34
20260903,48.6,48.95,47.9,47.9,308436,49.04,-2.32,49.9,47.88,0.45
20260904,47.9,48.2,47.3,48.05,364628,48.95,-1.85,49.9,47.92,0.54
20260907,49.4,49.4,47.45,47.5,387555,48.83,-2.73,49.73,47.98,0.62
20260908,47.5,47.9,47.05,47.45,490988,48.72,-2.6,49.48,48.02,0.86
20260909,47.4,48.2,47.4,48.2,312942,48.67,-0.97,49.33,48.08,0.57
20260910,48.3,48.3,47.15,47.9,388240,48.61,-1.46,49.19,48.12,0.73
20260911,47.1,47.7,45,45.3,974907,48.33,-6.28,48.88,48.12,1.78
20260914,45.35,48.2,45.1,48.05,781892,48.31,-0.54,48.84,48.15,1.44
20260915,48,49.6,47.8,48.65,620762,48.34,0.64,48.84,48.19,1.12
20260916,49,50.2,48.85,48.95,628129,48.39,1.16,48.8,48.23,1.14
20260917,49,51.5,48.6,51.2,1508629,48.62,5.3,48.78,48.3,2.65
20260918,51.2,52.7,50.2,52.7,1748855,48.96,7.63,48.85,48.4,2.82
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 57.85
- over_600_ratio: 54.88
- over_800_ratio: 52.31
- over_1000_ratio: 50.25
- over_400_change_1w: -0.43
- over_800_change_1w: -0.68
- over_1000_change_1w: -0.39
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,57.26,-0.13,51.39,-0.4,49.69,-0.14,6,False,False
20260709,57.42,0.16,51.17,-0.22,49.18,-0.51,7,False,False
20260717,57.21,-0.21,51.58,0.41,49.84,0.66,8,False,True
20260724,57.33,0.12,51.58,0,49.83,-0.01,9,False,False
20260731,57.8,0.47,51.77,0.19,50.34,0.51,10,True,True
20260807,57.84,0.04,52.12,0.35,50.41,0.07,11,True,True
20260814,58.4,0.56,52.45,0.33,50.45,0.04,12,True,True
20260821,58.38,-0.02,52.22,-0.23,50.8,0.35,13,False,True
20260828,58.21,-0.17,52.98,0.76,50.72,-0.08,14,False,True
20260904,58.11,-0.1,52.99,0.01,50.66,-0.06,15,False,True
20260911,58.28,0.17,52.99,0,50.64,-0.02,16,False,False
20260918,57.85,-0.43,52.31,-0.68,50.25,-0.39,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6589 | 台康生技 | pullback_rebound | 回檔後短線轉強 | 63.0 |  |  |  |  |  | continued_2_3d | 1.原預定買回股份總金額上限(元):5,154,754,000 2.原預定買回之期間:115/05/15~115/07/13 3.原預定買回之數量(股):5,000,000 4.原預定買回區間價格(元):40.00~74.00 5.本次實際買回期間:115/05/18~115/07/13 6.本次已買回股份數量(股):5,000,000 7.本次已買回股份總金額(元):230,003,463 8.本次平均每股買回價格(元):46.00 9.累積已持有自己公司股份數量(股):9,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.93 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6589 | 台康生技 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | continued_2_3d | 1.原預定買回股份總金額上限(元):5,154,754,000 2.原預定買回之期間:115/05/15~115/07/13 3.原預定買回之數量(股):5,000,000 4.原預定買回區間價格(元):40.00~74.00 5.本次實際買回期間:115/05/18~115/07/13 6.本次已買回股份數量(股):5,000,000 7.本次已買回股份總金額(元):230,003,463 8.本次平均每股買回價格(元):46.00 9.累積已持有自己公司股份數量(股):9,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.93 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 6589 | 台康生技 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | continued_2_3d | 1.原預定買回股份總金額上限(元):5,154,754,000 2.原預定買回之期間:115/05/15~115/07/13 3.原預定買回之數量(股):5,000,000 4.原預定買回區間價格(元):40.00~74.00 5.本次實際買回期間:115/05/18~115/07/13 6.本次已買回股份數量(股):5,000,000 7.本次已買回股份總金額(元):230,003,463 8.本次平均每股買回價格(元):46.00 9.累積已持有自己公司股份數量(股):9,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.93 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6589 | 台康生技 | 2 | 2 | 2 | 2 | 4 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
