# INDIVIDUAL STOCK CHATGPT PACKET - 6617 共信-KY

## Metadata
- generated_at: 2026-09-05 15:54:19 Asia/Taipei
- stock_id: 6617
- stock_name: 共信-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6617_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6617_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6617_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6617_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6617_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6617_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6617_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6617.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6617.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6617.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6617.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6617_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6617_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6617_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 113
- high: 124
- low: 113
- close: 123
- volume: 1213000
- ma5: 119.9
- ema23_primary: 109.97
- distance_to_ema23_pct: 11.85
- ma20: 110.94
- ma60: 93.65
- ma120: 80.65
- return_5d: 0.41
- return_20d: 27.73
- volume_ratio: 1.07
- distance_to_ma20_pct_auxiliary: 10.87
- distance_to_high_60_pct: -5.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,99.4,105.5,91.9,105.5,1945000,88.46,19.27,91.78,79.81,3.61
20260811,105.5,116,102,102.5,2065000,89.63,14.36,91.65,80.48,3.33
20260812,102,104,98.9,102,737000,90.66,12.51,91.33,81.1,1.16
20260813,100.5,103.5,99.6,102,416000,91.6,11.35,90.65,81.72,0.67
20260814,100.5,104.5,99.2,101,579000,92.39,9.32,90.42,82.31,0.92
20260817,101.5,101.5,96.6,98.5,446000,92.9,6.03,90.35,82.86,0.69
20260818,98.5,99,94.8,96.1,476000,93.16,3.15,90,83.4,0.73
20260819,97,97,94.5,95.2,254000,93.33,2,89.83,83.9,0.39
20260820,104.5,104.5,104.5,104.5,292000,94.26,10.86,90.56,84.52,0.47
20260821,114.5,114.5,106.5,107.5,1617000,95.37,12.72,91.65,85.08,2.4
20260824,105.5,116,102.5,111,1358000,96.67,14.82,93,85.74,1.89
20260825,112,118,111,115.5,2252000,98.24,17.57,94.69,86.46,2.75
20260826,116,127,115.5,127,1653000,100.64,26.2,97.1,87.42,1.87
20260827,128,129.5,120,128.5,2101000,102.96,24.81,99.78,88.41,2.17
20260828,126,129.5,121,122.5,1315000,104.59,17.13,102.11,89.32,1.29
20260831,123,123,118.5,120.5,737000,105.91,13.77,104.14,90.2,0.71
20260901,121,124.5,119.5,122,970000,107.25,13.75,106.27,91.1,0.91
20260902,120,122,116.5,120.5,1202000,108.36,11.21,108.31,91.98,1.08
20260903,119.5,119.5,113.5,113.5,1087000,108.79,4.33,109.61,92.73,0.94
20260904,113,124,113,123,1213000,109.97,11.85,110.94,93.65,1.07
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 67.76
- over_600_ratio: 64.69
- over_800_ratio: 62.52
- over_1000_ratio: 59.79
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
20260618,67.6,0.18,62.43,0.18,59.63,0.18,1,True,True
20260626,67.6,0,62.43,0,59.63,0,0,False,False
20260703,67.96,0.36,62.42,-0.01,59.63,0,1,False,False
20260709,67.57,-0.39,62.55,0.13,59.79,0.16,2,False,True
20260717,67.57,0,62.55,0,59.79,0,0,False,False
20260724,67.6,0.03,62.56,0.01,59.79,0,1,False,True
20260731,67.6,0,62.56,0,59.79,0,0,False,False
20260807,67.58,-0.02,62.55,-0.01,59.79,0,0,False,False
20260814,67.76,0.18,62.54,-0.01,59.79,0,1,False,False
20260821,67.74,-0.02,62.52,-0.02,59.79,0,0,False,False
20260828,67.7,-0.04,62.52,0,59.79,0,0,False,False
20260904,67.76,0.06,62.52,0,59.79,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6617 | 共信-KY | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_2_3d | 1.事實發生日:115/07/08 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告 3.財務業務資訊: (1)單月(註1)                             最近一月單月   去年同月     與去年同期增減%                             (115年5月)   (114年5月) ------------------------------------------------------------------------ 營業收入（百萬元）           4.426         2.627         68.48% 稅前淨利（百萬元）           (9.751)       (6.287)       55.10%（持續虧損) 歸屬母公司業主淨利（百萬元） (6.557)       (3.590)       82.65%（持續虧損) 每股盈餘（元）               (0.08)        (0.05)        60.00%（持續虧損) =========================================================================  (2)單季(註2)                             最近一季單季   去年同期     與去年同期增減%                             (115年第1季)  (114年第1季) ------------------------------------------------------------------------ 營業收入（百萬元）           9.467         7.629         24.09% 稅前淨利（百萬元）          (41.472)       (13.207)      214.02%（持續虧損) 歸屬母公司業主淨利（百萬元）(39.621)       (11.728)      237.83%（持續虧損) 每股盈餘（元）              (0.32)         (0.09)        255.56%（持續虧損) ========================================================================  (3)最近四季累計(註3)                                 114年第1季至114年第4季 ------------------------------------------------------------ 營業收入（百萬元）                  36.446 稅前淨利（百萬元）                  (120.869) 歸屬母公司業主淨利（百萬元）        (114.126) 每股盈餘（元）                      (0.92) ============================================================ 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:有 115/06/30代子公司共信醫藥科技股份有限公司公告向歐洲專利 辦公室提出之專利申請案號：EP 21873130.5 已獲核准通知 115/07/01代子公司共信醫藥科技股份有限公司公告向美國專利 及商標局提出之專利申請案號：16/959,054 已獲核准通知 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製    之合併數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且    係本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第1季至114年第4季採IFRS編製之合併數，業    經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6617 | 共信-KY | 3 | 3 | 3 | 7 | 10 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
