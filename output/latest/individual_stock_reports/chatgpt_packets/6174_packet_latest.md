# INDIVIDUAL STOCK CHATGPT PACKET - 6174 安碁

## Metadata
- generated_at: 2026-08-21 22:27:53 Asia/Taipei
- stock_id: 6174
- stock_name: 安碁
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6174_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6174_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6174_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6174_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6174.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6174.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6174.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6174.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6174_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6174_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6174_latest.md?ref=main

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
- date: 20260821
- open: 44.5
- high: 47.3
- low: 44.4
- close: 45.15
- volume: 3514000
- ma5: 44.34
- ema23_primary: 44.77
- distance_to_ema23_pct: 0.84
- ma20: 42.47
- ma60: 48.49
- ma120: 38.97
- return_5d: 1.92
- return_20d: 3.79
- volume_ratio: 1.86
- distance_to_ma20_pct_auxiliary: 6.32
- distance_to_high_60_pct: -32.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,43.8,45.8,42.7,43.6,2421000,51.13,-14.72,53.69,48,0.65
20260728,41.8,42.85,40.6,41.1,1092000,50.29,-18.28,53.3,48.17,0.32
20260729,41,42.4,37,37.9,1473000,49.26,-23.06,52.71,48.23,0.44
20260730,37.9,41.65,37.5,38.45,2397000,48.36,-20.49,51.91,48.24,0.73
20260731,40.8,42.2,39.35,39.5,2912000,47.62,-17.05,51.08,48.22,1
20260803,38.9,41.95,38.85,40.3,2140000,47.01,-14.27,50,48.23,0.83
20260804,40.35,44.25,40.35,42.4,2953000,46.63,-9.06,48.97,48.25,1.39
20260805,43.05,43.85,41.8,42,2303000,46.24,-9.17,48.18,48.26,1.26
20260806,41.3,42.8,40.1,41.5,1139000,45.85,-9.48,47.19,48.3,0.78
20260807,41.5,42.6,40,40,1355000,45.36,-11.81,46.31,48.3,0.93
20260810,41.85,43.3,41.25,42.1,979000,45.09,-6.63,45.59,48.35,0.66
20260811,41.7,43.4,41.65,42.9,998000,44.9,-4.46,44.92,48.44,0.67
20260812,42.95,46.6,42.95,44.05,2164000,44.83,-1.75,44.2,48.49,1.38
20260813,44.5,48.45,44.15,47.5,4091000,45.06,5.42,43.59,48.62,2.39
20260814,47.6,47.6,44.05,44.3,2118000,44.99,-1.54,43.1,48.64,1.19
20260817,44.5,46.1,44.4,45.1,1076000,45,0.22,42.92,48.68,0.59
20260818,45.1,45.1,42.25,42.5,883000,44.79,-5.12,42.59,48.61,0.48
20260819,41.3,44.75,41.3,44.75,797000,44.79,-0.09,42.38,48.57,0.43
20260820,45.35,46.9,43.5,44.2,1044000,44.74,-1.21,42.38,48.52,0.56
20260821,44.5,47.3,44.4,45.15,3514000,44.77,0.84,42.47,48.49,1.86
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 63.23
- over_600_ratio: 59.35
- over_800_ratio: 56.73
- over_1000_ratio: 56.73
- over_400_change_1w: 0.06
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,61.2,-1.33,56.97,-0.04,56.97,-0.04,0,False,False
20260605,61.2,0,56.97,0,56.97,0,0,False,False
20260612,64.38,3.18,56.87,-0.1,56.87,-0.1,1,False,False
20260618,63.42,-0.96,56.81,-0.06,56.81,-0.06,0,False,False
20260626,61.81,-1.61,56.8,-0.01,56.8,-0.01,0,False,False
20260703,62.05,0.24,56.8,0,56.8,0,1,False,False
20260709,62.51,0.46,56.79,-0.01,56.79,-0.01,2,False,False
20260717,63.09,0.58,56.73,-0.06,56.73,-0.06,3,False,False
20260724,63.06,-0.03,56.73,0,56.73,0,0,False,False
20260731,64.28,1.22,56.73,0,56.73,0,1,False,False
20260807,63.17,-1.11,56.73,0,56.73,0,0,False,False
20260814,63.23,0.06,56.73,0,56.73,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6174 | 安碁 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 1.事實發生日:115/07/03 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: 基本資料： (一)最近一月單月             115年05月     114年05月     與去年同期增減(%) 營業收入(百萬元)                 64.19         51.42              24.83 稅前淨利(百萬元)                  6.76         -8.40             180.47 歸屬母公司業主淨利(百萬元)        5.72         -6.79             184.24 每股盈餘(元)                      0.11         -0.14             178.57 (二)最近一季單季            115年第1季    114年第1季     與去年同期增減(%) 營業收入(百萬元)                166.49        143.87              15.72 稅前淨利(百萬元)                 19.21         15.71              22.28 歸屬母公司業主淨利(百萬元)       16.48         13.55              21.62 每股盈餘(元)                      0.33          0.27              22.22 (三)最近四季累計            114年第2季至115年第1季 營業收入(百萬元)                633.63 稅前淨利(百萬元)                 42.42 歸屬母公司業主淨利(百萬元)       36.01 每股盈餘(元)                      0.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1) 以上115年5月、114年5月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併數，未經會計師查核(閱)，僅供投資人參考。 (2) 最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3) 最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 6174 | 安碁 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/03 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: 基本資料： (一)最近一月單月             115年05月     114年05月     與去年同期增減(%) 營業收入(百萬元)                 64.19         51.42              24.83 稅前淨利(百萬元)                  6.76         -8.40             180.47 歸屬母公司業主淨利(百萬元)        5.72         -6.79             184.24 每股盈餘(元)                      0.11         -0.14             178.57 (二)最近一季單季            115年第1季    114年第1季     與去年同期增減(%) 營業收入(百萬元)                166.49        143.87              15.72 稅前淨利(百萬元)                 19.21         15.71              22.28 歸屬母公司業主淨利(百萬元)       16.48         13.55              21.62 每股盈餘(元)                      0.33          0.27              22.22 (三)最近四季累計            114年第2季至115年第1季 營業收入(百萬元)                633.63 稅前淨利(百萬元)                 42.42 歸屬母公司業主淨利(百萬元)       36.01 每股盈餘(元)                      0.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1) 以上115年5月、114年5月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併數，未經會計師查核(閱)，僅供投資人參考。 (2) 最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3) 最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 6174 | 安碁 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/03 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: 基本資料： (一)最近一月單月             115年05月     114年05月     與去年同期增減(%) 營業收入(百萬元)                 64.19         51.42              24.83 稅前淨利(百萬元)                  6.76         -8.40             180.47 歸屬母公司業主淨利(百萬元)        5.72         -6.79             184.24 每股盈餘(元)                      0.11         -0.14             178.57 (二)最近一季單季            115年第1季    114年第1季     與去年同期增減(%) 營業收入(百萬元)                166.49        143.87              15.72 稅前淨利(百萬元)                 19.21         15.71              22.28 歸屬母公司業主淨利(百萬元)       16.48         13.55              21.62 每股盈餘(元)                      0.33          0.27              22.22 (三)最近四季累計            114年第2季至115年第1季 營業收入(百萬元)                633.63 稅前淨利(百萬元)                 42.42 歸屬母公司業主淨利(百萬元)       36.01 每股盈餘(元)                      0.72 (四)公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1) 以上115年5月、114年5月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併數，未經會計師查核(閱)，僅供投資人參考。 (2) 最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3) 最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6174 | 安碁 | 2 | 2 | 2 | 2 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
