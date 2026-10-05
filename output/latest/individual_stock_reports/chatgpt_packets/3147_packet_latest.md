# INDIVIDUAL STOCK CHATGPT PACKET - 3147 大綜

## Metadata
- generated_at: 2026-10-04 22:17:04 Asia/Taipei
- stock_id: 3147
- stock_name: 大綜
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3147_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3147_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3147_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3147_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3147_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3147_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3147_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3147.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3147.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3147.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3147.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3147_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3147_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3147_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20261002
- open: 266
- high: 273
- low: 255
- close: 264.5
- volume: 2133000
- ma5: 252.3
- ema23_primary: 237.32
- distance_to_ema23_pct: 11.45
- ma20: 233.8
- ma60: 229.13
- ma120: 226.58
- return_5d: 12.79
- return_20d: 19.95
- volume_ratio: 2.98
- distance_to_ma20_pct_auxiliary: 13.13
- distance_to_high_60_pct: -3.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,221,223,215,215,339000,223.89,-3.97,222.88,249.36,0.69
20260904,216,224,216,223.5,359000,223.86,-0.16,222.9,247.75,0.87
20260907,226,226.5,218.5,221.5,359000,223.66,-0.97,222.38,246.14,0.95
20260908,222,222.5,218,218,152000,223.19,-2.33,221.97,244.14,0.42
20260909,222.5,227.5,221,226.5,366000,223.47,1.36,221.82,242.4,1.04
20260910,226.5,231,223.5,223.5,382000,223.47,0.01,221.3,240.29,1.1
20260911,220.5,226.5,219.5,221,349000,223.26,-1.01,220.75,238.47,1.05
20260914,223.5,232.5,222,226,1190000,223.49,1.12,220.53,236.79,3.16
20260915,229,233.5,225,227,746000,223.78,1.44,220.62,235.24,1.9
20260916,228,239.5,228,233,964000,224.55,3.76,221.2,233.69,2.27
20260917,234,240,230,232.5,632000,225.22,3.23,221.62,231.9,1.48
20260918,234.5,244,234,242.5,956000,226.66,6.99,222.9,230.19,2.11
20260921,240.5,244.5,236.5,238,608000,227.6,4.57,223.97,228.98,1.29
20260922,238,239,231.5,232,585000,227.97,1.77,224.75,228.19,1.2
20260923,232.5,236,231.5,234.5,236000,228.51,2.62,225.4,227.9,0.49
20260924,235,249.5,234,243,1233000,229.72,5.78,226.7,227.89,2.34
20260929,240,244.5,237,243,561000,230.83,5.27,227.9,227.96,1.04
20260930,245.5,250,243.5,243.5,524000,231.88,5.01,229.18,228.08,0.95
20261001,242,267.5,240,267.5,1630000,234.85,13.9,231.6,228.47,2.63
20261002,266,273,255,264.5,2133000,237.32,11.45,233.8,229.13,2.98
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 54.64
- over_600_ratio: 51.17
- over_800_ratio: 49.67
- over_1000_ratio: 47.6
- over_400_change_1w: -0.15
- over_800_change_1w: -0.02
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,57.09,0.09,52.06,0,49.95,0,2,False,False
20260724,57.47,0.38,52.15,0.09,50.04,0.09,3,True,True
20260731,55.74,-1.73,52.09,-0.06,50.01,-0.03,0,False,False
20260807,56.15,0.41,52.5,0.41,50.42,0.41,1,True,True
20260814,55.78,-0.37,52.13,-0.37,50.18,-0.24,0,False,False
20260821,55.89,0.11,52.24,0.11,50.36,0.18,1,True,True
20260828,55.45,-0.44,51.8,-0.44,49.95,-0.41,0,False,False
20260904,55.21,-0.24,49.79,-2.01,47.6,-2.35,0,False,False
20260911,56.22,1.01,49.95,0.16,49.95,2.35,1,True,True
20260918,55.04,-1.18,49.82,-0.13,47.6,-2.35,0,False,False
20260924,54.79,-0.25,49.69,-0.13,47.6,0,0,False,False
20261002,54.64,-0.15,49.67,-0.02,47.6,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3147 | 大綜 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.事實發生日:115/07/03 2.發生緣由:依證券櫃檯買賣中心通知處理辦理公告。 3.財務業務資訊: (1)單月                      最近一月單月       去年同月       與去年同期增減%                        (115/05)         (114/05) ----------------------------------------------------------------------- 營業收入(百萬元)        3,023.39          331.35           812.45% 稅前淨利(百萬元)          198.46           -9.99       (去年同期為虧損) 本期淨利(百萬元)          158.73           -9.99       (去年同期為虧損) 每股盈餘(元)                3.63           -0.23       (去年同期為虧損) ======================================================================== (2)單季                      最近一季單季       去年同期       與去年同期增減%                        (115第1季)       (114第1季) ----------------------------------------------------------------------- 營業收入(百萬元)        2,986.52         3,148.37           -5.14% 稅前淨利(百萬元)          202.62           174.39           16.19% 本期淨利(百萬元)          159.83           138.00           15.82% 每股盈餘(元)                3.66             3.16           15.82% ======================================================================= (3)最近四季累計                           114年第2季至115年第1季 ----------------------------------------------------------------------- 營業收入(百萬元)                  8,009.21 稅前淨利(百萬元)                    504.70 本期淨利(百萬元)                    390.26 每股盈餘(元)                          8.93 ======================================================================= (4)公司每股面額：10元。 (5)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製    之合併數，未經會計師查核(閱)，僅供投資人參考。 (6)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係    本公司採IFRS下編製之合併數，業經會計師查核(閱)，謹供投資人參考。 (7)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經    會計師查核(閱)，謹供投資人參考。 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3147 | 大綜 | 2 | 2 | 3 | 3 | 3 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
