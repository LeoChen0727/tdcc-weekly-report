# INDIVIDUAL STOCK CHATGPT PACKET - 6617 共信-KY

## Metadata
- generated_at: 2026-08-23 22:29:01 Asia/Taipei
- stock_id: 6617
- stock_name: 共信-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
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
- date: 20260821
- open: 114.5
- high: 114.5
- low: 106.5
- close: 107.5
- volume: 1617000
- ma5: 100.36
- ema23_primary: 95.37
- distance_to_ema23_pct: 12.72
- ma20: 91.65
- ma60: 85.08
- ma120: 77.17
- return_5d: 6.44
- return_20d: 25.29
- volume_ratio: 2.4
- distance_to_ma20_pct_auxiliary: 17.29
- distance_to_high_60_pct: -10.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,88.9,90.2,83.1,84.1,447000,92.03,-8.61,96.39,76.81,0.71
20260728,83.8,83.8,80.8,81.5,239000,91.15,-10.59,97.3,76.92,0.38
20260729,81,81,76.1,78.9,417000,90.13,-12.46,97.76,77.09,0.65
20260730,79.7,79.7,73.4,74.9,355000,88.86,-15.71,97.67,77.22,0.59
20260731,76.1,77.6,74.8,76,334000,87.79,-13.43,97.27,77.41,0.58
20260803,74.9,83.5,74.8,79.9,449000,87.13,-8.3,96.63,77.67,0.77
20260804,78.6,81.9,78.6,79.3,203000,86.48,-8.3,95.52,77.94,0.35
20260805,79.7,80.9,77.9,79.7,260000,85.91,-7.23,93.93,78.21,0.55
20260806,78.6,87.6,78.6,87.6,436000,86.05,1.8,92.44,78.64,1.04
20260807,88.6,96.3,86.1,96.3,1510000,86.91,10.81,91.75,79.12,3.26
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
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 67.74
- over_600_ratio: 64.7
- over_800_ratio: 62.52
- over_1000_ratio: 59.79
- over_400_change_1w: -0.02
- over_800_change_1w: -0.02
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,67.42,0.03,62.25,0.04,59.45,0.03,5,True,True
20260612,67.42,0,62.25,0,59.45,0,0,False,False
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
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6617 | 共信-KY | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/08 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告 3.財務業務資訊: (1)單月(註1)                             最近一月單月   去年同月     與去年同期增減%                             (115年5月)   (114年5月) ------------------------------------------------------------------------ 營業收入（百萬元）           4.426         2.627         68.48% 稅前淨利（百萬元）           (9.751)       (6.287)       55.10%（持續虧損) 歸屬母公司業主淨利（百萬元） (6.557)       (3.590)       82.65%（持續虧損) 每股盈餘（元）               (0.08)        (0.05)        60.00%（持續虧損) =========================================================================  (2)單季(註2)                             最近一季單季   去年同期     與去年同期增減%                             (115年第1季)  (114年第1季) ------------------------------------------------------------------------ 營業收入（百萬元）           9.467         7.629         24.09% 稅前淨利（百萬元）          (41.472)       (13.207)      214.02%（持續虧損) 歸屬母公司業主淨利（百萬元）(39.621)       (11.728)      237.83%（持續虧損) 每股盈餘（元）              (0.32)         (0.09)        255.56%（持續虧損) ========================================================================  (3)最近四季累計(註3)                                 114年第1季至114年第4季 ------------------------------------------------------------ 營業收入（百萬元）                  36.446 稅前淨利（百萬元）                  (120.869) 歸屬母公司業主淨利（百萬元）        (114.126) 每股盈餘（元）                      (0.92) ============================================================ 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:有 115/06/30代子公司共信醫藥科技股份有限公司公告向歐洲專利 辦公室提出之專利申請案號：EP 21873130.5 已獲核准通知 115/07/01代子公司共信醫藥科技股份有限公司公告向美國專利 及商標局提出之專利申請案號：16/959,054 已獲核准通知 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製    之合併數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且    係本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第1季至114年第4季採IFRS編製之合併數，業    經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6617 | 共信-KY | 1 | 1 | 3 | 3 | 6 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 6 次，但尚未有效突破，需等待攻擊確認。 |

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
