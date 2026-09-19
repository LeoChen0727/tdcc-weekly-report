# INDIVIDUAL STOCK CHATGPT PACKET - 8028 昇陽半導體

## Metadata
- generated_at: 2026-09-19 15:54:56 Asia/Taipei
- stock_id: 8028
- stock_name: 昇陽半導體
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8028_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8028_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8028_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8028_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8028_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8028_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8028_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8028.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8028.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8028.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8028.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8028_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8028_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8028_latest.md?ref=main

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
- open: 250
- high: 258
- low: 242.5
- close: 257
- volume: 11292233
- ma5: 236.4
- ema23_primary: 243.75
- distance_to_ema23_pct: 5.44
- ma20: 240.22
- ma60: 270.62
- ma120: 265.62
- return_5d: 13.97
- return_20d: 5.98
- volume_ratio: 3.24
- distance_to_ma20_pct_auxiliary: 6.98
- distance_to_high_60_pct: -29.4

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,242.5,249.5,242.5,242.5,1249637,264.86,-8.44,257.82,296.06,0.45
20260825,240,243,231,242,1801046,262.96,-7.97,255.93,294.64,0.66
20260826,241.5,246.5,240.5,246.5,1327218,261.59,-5.77,255.65,292.81,0.49
20260827,249.5,251.5,244,248.5,1894678,260.5,-4.61,256.7,291.37,0.7
20260828,251.5,255.5,249,249,2310457,259.54,-4.06,256.9,289.77,0.84
20260831,246.5,246.5,237,241,3870838,257.99,-6.59,255.93,288.11,1.35
20260901,242.5,256,242.5,255,3511893,257.74,-1.06,255.28,286.73,1.17
20260902,250,253,245,245.5,2559823,256.72,-4.37,253.45,285.76,0.84
20260903,248,249,236.5,236.5,1932954,255.04,-7.27,251.55,284.55,0.68
20260904,242,244,234.5,239,1322617,253.7,-5.8,250.8,283.28,0.5
20260907,243,256,241,249.5,5872402,253.35,-1.52,250.07,282.38,2.13
20260908,249,249,235.5,236.5,5180911,251.95,-6.13,248.85,281.07,1.8
20260909,237.5,240.5,235,236,1546612,250.62,-5.83,247.4,279.69,0.55
20260910,235.5,235.5,228,229.5,2746280,248.86,-7.78,245.5,278.28,0.98
20260911,223,226.5,221.5,225.5,2654941,246.91,-8.67,243.62,276.85,1.01
20260914,220,224.5,216.5,221.5,2320122,244.79,-9.52,241.45,275.35,0.89
20260915,221,231.5,220,226.5,3338771,243.27,-6.89,240.35,273.75,1.31
20260916,228,236.5,227,233,3815963,242.41,-3.88,239.65,272.47,1.46
20260917,237.5,249.5,235.5,244,9261432,242.55,0.6,239.5,271.38,3.1
20260918,250,258,242.5,257,11292233,243.75,5.44,240.22,270.62,3.24
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 47.96
- over_600_ratio: 43.48
- over_800_ratio: 38.8
- over_1000_ratio: 36.8
- over_400_change_1w: 0.21
- over_800_change_1w: 0.42
- over_1000_change_1w: 0.95
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,51.66,1.34,40.27,-0.32,37.4,0.34,1,False,True
20260709,51.65,-0.01,39.5,-0.77,38.5,1.1,2,False,True
20260717,55.83,4.18,45.44,5.94,42.89,4.39,3,True,True
20260724,53.04,-2.79,43.04,-2.4,39.55,-3.34,0,False,False
20260731,52.32,-0.72,42.6,-0.44,41.6,2.05,1,False,True
20260807,51.26,-1.06,42.2,-0.4,39.78,-1.82,0,False,False
20260814,51.61,0.35,41.89,-0.31,39.35,-0.43,1,False,False
20260821,50.9,-0.71,41.15,-0.74,39.18,-0.17,0,False,False
20260828,49.64,-1.26,40.57,-0.58,39.1,-0.08,0,False,False
20260904,48.63,-1.01,39.72,-0.85,38.2,-0.9,0,False,False
20260911,47.75,-0.88,38.38,-1.34,35.85,-2.35,0,False,False
20260918,47.96,0.21,38.8,0.42,36.8,0.95,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 8028 | 昇陽半導體 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_put_bullish | continued_2_3d | 1.原預定買回股份總金額上限(元):3,483,787,097 2.原預定買回之期間:115/08/13~115/10/12 3.原預定買回之數量(股):300,000 4.原預定買回區間價格(元):210.00~430.00 5.本次實際買回期間:115/08/14~115/08/24 6.本次已買回股份數量(股):300,000 7.本次已買回股份總金額(元):77,256,299 8.本次平均每股買回價格(元):257.52 9.累積已持有自己公司股份數量(股):1,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):0.56 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 8028 | 昇陽半導體 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_put_bullish | continued_2_3d | 1.原預定買回股份總金額上限(元):3,483,787,097 2.原預定買回之期間:115/08/13~115/10/12 3.原預定買回之數量(股):300,000 4.原預定買回區間價格(元):210.00~430.00 5.本次實際買回期間:115/08/14~115/08/24 6.本次已買回股份數量(股):300,000 7.本次已買回股份總金額(元):77,256,299 8.本次平均每股買回價格(元):257.52 9.累積已持有自己公司股份數量(股):1,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):0.56 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 8028 | 昇陽半導體 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_put_bullish | continued_2_3d | 1.原預定買回股份總金額上限(元):3,483,787,097 2.原預定買回之期間:115/08/13~115/10/12 3.原預定買回之數量(股):300,000 4.原預定買回區間價格(元):210.00~430.00 5.本次實際買回期間:115/08/14~115/08/24 6.本次已買回股份數量(股):300,000 7.本次已買回股份總金額(元):77,256,299 8.本次平均每股買回價格(元):257.52 9.累積已持有自己公司股份數量(股):1,000,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):0.56 11.本次未執行完畢之原因:  12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 8028 | 昇陽半導體 | 2 | 2 | 2 | 2 | 2 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 8028 | 昇陽半導體 | 123 | 5 | 19011920.0 | 76940.0 | 247.1 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
