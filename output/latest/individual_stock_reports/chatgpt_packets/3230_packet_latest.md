# INDIVIDUAL STOCK CHATGPT PACKET - 3230 錦明

## Metadata
- generated_at: 2026-08-21 22:27:17 Asia/Taipei
- stock_id: 3230
- stock_name: 錦明
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3230_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3230_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3230_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3230_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3230.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3230.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3230.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3230.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3230_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3230_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3230_latest.md?ref=main

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
- open: 41.65
- high: 45.35
- low: 41.3
- close: 43.25
- volume: 1415000
- ma5: 42.48
- ema23_primary: 41.79
- distance_to_ema23_pct: 3.48
- ma20: 40.34
- ma60: 39.73
- ma120: 38.81
- return_5d: -2.7
- return_20d: 7.59
- volume_ratio: 1.5
- distance_to_ma20_pct_auxiliary: 7.21
- distance_to_high_60_pct: -24.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,39.15,40,38.45,39.7,961000,44.04,-9.85,47.99,37.41,0.45
20260728,39,39.6,37.55,37.55,985000,43.5,-13.67,47.68,37.44,0.49
20260729,37,39.95,35,35.95,1545000,42.87,-16.14,47.16,37.43,1.01
20260730,35.4,36.4,34.5,34.5,591000,42.17,-18.19,46.5,37.41,0.4
20260731,36.85,37,35.2,36.3,705000,41.68,-12.91,45.74,37.43,0.51
20260803,35.45,39.8,35.45,39.25,632000,41.48,-5.37,45.12,37.52,0.49
20260804,39.5,40.95,39.15,40.2,906000,41.37,-2.83,44.58,37.62,0.71
20260805,40.95,42.05,40.95,41,886000,41.34,-0.82,44.1,37.76,0.7
20260806,41,41.75,39.6,41.35,746000,41.34,0.02,43.57,37.9,0.59
20260807,41,41.3,40.1,40.25,510000,41.25,-2.42,42.97,38.03,0.4
20260810,40.25,41.5,40.25,40.8,501000,41.21,-1,42.24,38.19,0.41
20260811,40.8,42.4,40,41.75,638000,41.26,1.19,41.64,38.38,0.53
20260812,42.05,42.6,40.95,40.95,650000,41.23,-0.68,40.99,38.52,0.54
20260813,40.95,42.2,40.45,40.45,605000,41.17,-1.74,40.48,38.64,0.5
20260814,40.5,44.45,40,44.45,1589000,41.44,7.26,40.44,38.84,1.29
20260817,47,47.25,42.5,44,2810000,41.65,5.63,40.48,39.04,2.09
20260818,44,45,42.1,42.5,1062000,41.72,1.86,40.25,39.21,0.87
20260819,42.55,43.8,41.1,41.1,559000,41.67,-1.37,40.17,39.35,0.55
20260820,41.45,43.7,41.45,41.55,559000,41.66,-0.27,40.19,39.52,0.59
20260821,41.65,45.35,41.3,43.25,1415000,41.79,3.48,40.34,39.73,1.5
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 52.6
- over_600_ratio: 51.66
- over_800_ratio: 49.38
- over_1000_ratio: 45.24
- over_400_change_1w: -0.35
- over_800_change_1w: 1.03
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,57.01,-0.17,53.67,-0.57,51.62,-0.57,0,False,False
20260605,57.01,0,53.36,-0.31,51.3,-0.32,1,False,False
20260612,56.91,-0.1,53.36,0,51.3,0,0,False,False
20260618,56.64,-0.27,53.13,-0.23,51.08,-0.22,0,False,False
20260626,53.04,-3.6,50.22,-2.91,48.19,-2.89,0,False,False
20260703,53.96,0.92,48.83,-1.39,46.8,-1.39,1,False,False
20260709,53.77,-0.19,48.42,-0.41,45.31,-1.49,0,False,False
20260717,54.21,0.44,48.47,0.05,45.3,-0.01,1,False,True
20260724,52.41,-1.8,48.49,0.02,45.28,-0.02,2,False,True
20260731,53.02,0.61,48.42,-0.07,45.28,0,3,False,False
20260807,52.95,-0.07,48.35,-0.07,45.24,-0.04,0,False,False
20260814,52.6,-0.35,49.38,1.03,45.24,0,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3230 | 錦明 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | stale_signal | 1.事實發生日:115/07/01 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                       最近一月單月     去年同月      與去年同期增減%                         (115/05)       (114/05) --------------------------------------------------------------------- 營業收入(百萬元)             36            33             9.09% 稅前淨利(百萬元)            (12)          (23)           47.83% 歸屬母公司業主淨利(百萬元)  (12)          (20)           40.00% 每股盈餘(元)              (0.15)        (0.23)           34.78% (2)單季                      最近一季單季       去年同期     與去年同期增減%                       (115第1季)       (114第1季) ----------------------------------------------------------------------- 營業收入(百萬元)            101           118           (14.41%) 稅前淨利(百萬元)            (39)          (13)         (200.00%) 歸屬母公司業主淨利(百萬元)  (38)          (13)         (192.31%) 每股盈餘(元)              (0.45)        (0.15)         (200.00%) (3)最近四季累計                                  (114年第2季至115年第1季) ---------------------------------------------------------- 營業收入(百萬元)                          386 稅前淨利(百萬元)                         (164) 歸屬母公司業主淨利(百萬元)               (162) 每股盈餘(元)                            (1.90) (4)公司每股面額:10元。 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）: (1)115/06/26 公告本公司115年股東常會重要決議事項 (2)115/06/26 公告本公司115年股東常會全面改選董事(含獨立董事) 暨董事變動達三分之一 (3)115/06/26 公告本公司董事會選任董事長與副董事長 (4)115/06/26 公告本公司第3屆審計委員會委員 (5)115/06/26 公告本公司法人董事指派代表人 (6)115/06/26 公告本公司115年股東常會同意解除新任董事競業禁止之限制 (7)115/06/26 公告本公司董事會決議通過委任第6屆薪酬委員會委員 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計 準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字， 且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經 會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3230 | 錦明 | 1 | 1 | 1 | 1 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
