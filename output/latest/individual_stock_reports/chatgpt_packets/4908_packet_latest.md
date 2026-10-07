# INDIVIDUAL STOCK CHATGPT PACKET - 4908 前鼎

## Metadata
- generated_at: 2026-10-07 22:18:31 Asia/Taipei
- stock_id: 4908
- stock_name: 前鼎
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 266
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4908_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4908_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4908_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4908_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4908_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4908_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4908_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4908.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4908.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4908.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4908.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4908_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4908_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4908_latest.md?ref=main

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
- date: 20261002
- open: 210
- high: 224.5
- low: 210
- close: 224.5
- volume: 2693000
- ma5: 210.3
- ema23_primary: 213.39
- distance_to_ema23_pct: 5.21
- ma20: 224.78
- ma60: 179.79
- ma120: 194.72
- return_5d: 6.9
- return_20d: 2.98
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: -0.12
- distance_to_high_60_pct: -15.28

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,220,229.5,200.5,204.5,2615000,177.47,15.23,171.7,168.64,0.62
20260904,214,224.5,199,224.5,1723000,181.39,23.77,175.75,169.05,0.41
20260907,230.5,231.5,220.5,223,1347000,184.86,20.63,179.15,169.56,0.33
20260908,224,235.5,221,227.5,1855000,188.41,20.75,182.97,170.03,0.44
20260909,238.5,243,229.5,242,2885000,192.88,25.47,186.95,170.8,0.69
20260910,239,265,238,249,14247000,197.55,26.04,191.4,171.65,3.02
20260911,242.5,253,235,237.5,6619000,200.88,18.23,195.53,172.39,1.32
20260914,227.5,235,220,225.5,4042000,202.93,11.12,198.62,172.62,0.79
20260915,223,245,218,224,7655000,204.69,9.43,202.32,173,1.41
20260916,226,243,223.5,240.5,10761000,207.67,15.81,206.72,173.48,1.81
20260917,245,262,232.5,238,10187000,210.2,13.23,210.93,174.07,1.59
20260918,240,248.5,232.5,243.5,7631000,212.98,14.33,215.45,174.87,1.13
20260921,241.5,245,231.5,232,4282000,214.56,8.13,219.68,175.65,0.62
20260922,233.5,234,222.5,222.5,3017000,215.22,3.38,222.7,176.31,0.43
20260923,222.5,225,207.5,210,3835000,214.79,-2.23,224.3,176.66,0.58
20260924,209,213,205,210,2573000,214.39,-2.05,225.03,177.28,0.41
20260929,208.5,212,205,205.5,1222000,213.65,-3.81,225.8,177.82,0.21
20260930,210.5,212,205.5,207,1262000,213.09,-2.86,225.7,178.26,0.24
20261001,208,209,204,204.5,1068000,212.38,-3.71,224.45,178.75,0.2
20261002,210,224.5,210,224.5,2693000,213.39,5.21,224.78,179.79,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 53.1
- over_600_ratio: 51.16
- over_800_ratio: 49.28
- over_1000_ratio: 42.42
- over_400_change_1w: 0.51
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.14
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,54.1,1.32,49,0,44.3,0,1,False,False
20260724,54.06,-0.04,49,0,44.3,0,0,False,False
20260731,54.74,0.68,50.06,1.06,44.3,0,1,False,True
20260807,54.2,-0.54,49.47,-0.59,43.71,-0.59,2,False,False
20260814,52.88,-1.32,48.85,-0.62,40.95,-2.76,0,False,False
20260821,53.13,0.25,47.81,-1.04,40.95,0,1,False,False
20260828,53.05,-0.08,49.13,1.32,42.29,1.34,2,False,True
20260904,55.94,2.89,49.39,0.26,43.59,1.3,3,True,True
20260911,57.77,1.83,51.17,1.78,44.16,0.57,4,True,True
20260918,56.2,-1.57,50.04,-1.13,44.24,0.08,5,False,True
20260924,52.59,-3.61,49.24,-0.8,42.28,-1.96,0,False,False
20261002,53.1,0.51,49.28,0.04,42.42,0.14,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 4908 | 前鼎 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/09/22 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告。 3.財務業務資訊: (1)單月(註1)            115年08月         114年08月        與去年同期增減% ---------------------------------------------------------------------------- 營業收入(百萬元)          97                 75                29% 稅前淨利(百萬元)          24                 19                26% 本期淨利(百萬元)          19                 15                27% 稅後每股盈餘(元)        0.24               0.19                26%  (2)單季(註2)            115年第2季        114年第2季       與去年同期增減% ---------------------------------------------------------------------------- 營業收入(百萬元)         255                206                24% 稅前淨利(百萬元)          65                 13               400% 本期淨利(百萬元)          52                 11               373% 稅後每股盈餘(元)        0.67               0.14               379%  (3)最近四季累計(註3)  114年第3季至115年第2季 ------------------------------------------- 營業收入(百萬元)         917 稅前淨利(百萬元)         230 本期淨利(百萬元)         196 稅後每股盈餘(元)        2.52  (4)公司每股面額：10元  4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: 註1:以上115年08月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之合併數 ，未經會計師查核(閱)，僅供投資人參考。 註2:最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公司 採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註3:最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計師 查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 4908 | 前鼎 | 7 | 1 | 5 | 7 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
