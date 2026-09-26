# INDIVIDUAL STOCK CHATGPT PACKET - 4979 華星光

## Metadata
- generated_at: 2026-09-26 22:17:04 Asia/Taipei
- stock_id: 4979
- stock_name: 華星光
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
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4979_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4979_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4979_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4979_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4979_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4979_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4979_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4979.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4979.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4979.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4979.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4979_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4979_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4979_latest.md?ref=main

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
- date: 20260924
- open: 581
- high: 590
- low: 559
- close: 563
- volume: 8532000
- ma5: 597.4
- ema23_primary: 571.69
- distance_to_ema23_pct: -1.52
- ma20: 584.85
- ma60: 505.94
- ma120: 538.05
- return_5d: 1.26
- return_20d: -8.75
- volume_ratio: 1.22
- distance_to_ma20_pct_auxiliary: -3.74
- distance_to_high_60_pct: -14.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,603,621,596,610,2414000,534.25,14.18,536.88,485.9,0.23
20260831,606,613,589,609,2001000,540.48,12.68,546.98,486.22,0.2
20260901,609,613,595,600,2039000,545.44,10,554.6,486.28,0.2
20260902,600,624,600,624,2615000,551.99,13.05,561.2,487.73,0.26
20260903,633,635,572,572,2518000,553.66,3.31,565.4,487.93,0.25
20260904,615,629,590,629,18513000,559.94,12.33,572.45,490.02,1.72
20260907,630,635,590,590,15293000,562.44,4.9,575.15,491.97,1.38
20260908,598,630,590,605,12521000,565.99,6.89,579.9,493.7,1.17
20260909,631,658,602,610,15851000,569.66,7.08,582.35,494.7,1.49
20260910,601,602,571,571,8587000,569.77,0.22,582.7,494.75,0.88
20260911,545,558,525,531,1772000,566.54,-6.27,583.15,494.5,0.18
20260914,510,547,508,547,966000,564.91,-3.17,583.25,494.17,0.1
20260915,542,542,501,509,1726000,560.25,-9.15,582.3,493.45,0.18
20260916,516,547,510,547,1024000,559.15,-2.17,583.2,493.82,0.11
20260917,556,561,532,556,917000,558.88,-0.52,582.5,494.75,0.1
20260918,578,611,571,611,9561000,563.23,8.48,584.2,497.01,1.05
20260921,616,650,609,618,14408000,567.79,8.84,587.75,499.66,1.57
20260922,630,637,605,605,11366000,570.89,5.97,587.95,502.13,1.27
20260923,612,613,583,590,7144000,572.48,3.06,587.55,504.07,0.89
20260924,581,590,559,563,8532000,571.69,-1.52,584.85,505.94,1.22
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 45.73
- over_600_ratio: 37.76
- over_800_ratio: 33.02
- over_1000_ratio: 27.93
- over_400_change_1w: 1.86
- over_800_change_1w: 1.23
- over_1000_change_1w: 1.16
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,38.01,-0.67,31.68,-0.17,27.81,-0.25,2,False,False
20260717,37.81,-0.2,30.74,-0.94,26.24,-1.57,0,False,False
20260724,39.79,1.98,30.38,-0.36,25.98,-0.26,1,False,False
20260731,38.74,-1.05,28.07,-2.31,24.42,-1.56,0,False,False
20260807,41,2.26,29.8,1.73,26.17,1.75,1,True,True
20260814,43.37,2.37,31.99,2.19,26.24,0.07,2,True,True
20260821,41.89,-1.48,31.56,-0.43,25.41,-0.83,0,False,False
20260828,45.58,3.69,35.76,4.2,28.8,3.39,1,True,True
20260904,43.94,-1.64,31.6,-4.16,25.96,-2.84,0,False,False
20260911,44.68,0.74,30.93,-0.67,25.91,-0.05,1,False,False
20260918,43.87,-0.81,31.79,0.86,26.77,0.86,2,False,True
20260924,45.73,1.86,33.02,1.23,27.93,1.16,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4979 | 華星光 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/09/23 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                最近一月單月      去年同月       與去年同期增減%                    (115/08)      (114/08) ----------------------------------------------------------------- 營業收入(百萬元)     546            398              37.19% 稅前淨利(百萬元)     113             90              25.56% 歸屬母公司業主淨利    92             90               2.22% (百萬元) 每股盈餘(元)        0.64           0.64                  - ================================================================= (2)單季                最近一季單季       去年同期     與去年同期增減%                (115年第2季)     (114年第2季) ----------------------------------------------------------------- 營業收入(百萬元)  1,289           1,087             18.58% 稅前淨利(百萬元)    248              95            161.05% 歸屬母公司業主淨利  184              95             93.68% (百萬元) 每股盈餘(元)       1.29            0.67             92.54% ================================================================= (3)最近四季累計                      114年第3季至115年第2季 ---------------------------------------------------------------- 營業收入(百萬元)              4,713 稅前淨利(百萬元)              1,004 歸屬母公司業主淨利              870 (百萬元) 每股盈餘(元)                   6.15 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)115年8月和去年同期比較數之財務資料係本公司採IFRS會計  　準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第2季係指單季數字，係經會計師查核(閱)。 (3)最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合    併數，業經會計師查核(閱)。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 4979 | 華星光 | revenue_pullback | 營收成長股價回檔 | 67.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/23 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                最近一月單月      去年同月       與去年同期增減%                    (115/08)      (114/08) ----------------------------------------------------------------- 營業收入(百萬元)     546            398              37.19% 稅前淨利(百萬元)     113             90              25.56% 歸屬母公司業主淨利    92             90               2.22% (百萬元) 每股盈餘(元)        0.64           0.64                  - ================================================================= (2)單季                最近一季單季       去年同期     與去年同期增減%                (115年第2季)     (114年第2季) ----------------------------------------------------------------- 營業收入(百萬元)  1,289           1,087             18.58% 稅前淨利(百萬元)    248              95            161.05% 歸屬母公司業主淨利  184              95             93.68% (百萬元) 每股盈餘(元)       1.29            0.67             92.54% ================================================================= (3)最近四季累計                      114年第3季至115年第2季 ---------------------------------------------------------------- 營業收入(百萬元)              4,713 稅前淨利(百萬元)              1,004 歸屬母公司業主淨利              870 (百萬元) 每股盈餘(元)                   6.15 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)115年8月和去年同期比較數之財務資料係本公司採IFRS會計  　準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第2季係指單季數字，係經會計師查核(閱)。 (3)最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合    併數，業經會計師查核(閱)。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4979 | 華星光 | 5 | 3 | 5 | 9 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
