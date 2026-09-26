# INDIVIDUAL STOCK CHATGPT PACKET - 4991 環宇-KY

## Metadata
- generated_at: 2026-09-26 15:52:30 Asia/Taipei
- stock_id: 4991
- stock_name: 環宇-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4991_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4991_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4991_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4991_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4991_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4991_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4991_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4991.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4991.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4991.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4991.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4991_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4991_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4991_latest.md?ref=main

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
- open: 447.5
- high: 464
- low: 436
- close: 463.5
- volume: 3067000
- ma5: 471.2
- ema23_primary: 470.11
- distance_to_ema23_pct: -1.41
- ma20: 480.75
- ma60: 459.05
- ma120: 549.29
- return_5d: 7.54
- return_20d: -13.85
- volume_ratio: 0.66
- distance_to_ma20_pct_auxiliary: -3.59
- distance_to_high_60_pct: -20.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,538,540,511,520,9170000,474.21,9.66,474.65,486.02,2.22
20260831,515,543,505,539,5904000,479.61,12.38,482.2,483.64,1.34
20260901,530,554,511,544,8989000,484.97,12.17,488.07,481.81,1.86
20260902,524,545,524,530,5659000,488.72,8.45,491.12,480.44,1.13
20260903,536,560,480.5,484.5,12932000,488.37,-0.79,493.25,478.55,2.32
20260904,499,505,470,497,1118000,489.09,1.62,494.85,477.85,0.2
20260907,520,520,489,494,543000,489.5,0.92,494,477.25,0.1
20260908,500,501,467,493,635000,489.79,0.66,494.6,476.23,0.13
20260909,511,520,495,499,710000,490.56,1.72,495.32,475.48,0.16
20260910,499.5,511,487,488,784000,490.35,-0.48,495.82,473.83,0.19
20260911,455,478,448.5,448.5,4002000,486.86,-7.88,495.25,471.98,0.95
20260914,430,451.5,422,445,3429000,483.37,-7.94,493.1,469.96,0.79
20260915,445.5,448,418,418,2828000,477.92,-12.54,489.75,467.52,0.64
20260916,424,438.5,417,428,4127000,473.76,-9.66,486.82,465.73,0.9
20260917,445,458,428.5,431,3647000,470.2,-8.34,482.38,463.52,0.77
20260918,450.5,474,450.5,474,7333000,470.52,0.74,482.02,462.06,1.58
20260921,480,508,478,498,8007000,472.81,5.33,485.18,461.91,1.66
20260922,499,504,470,473,5427000,472.82,0.04,486.57,461.75,1.11
20260923,476.5,477.5,439.5,447.5,5308000,470.71,-4.93,484.48,460.38,1.08
20260924,447.5,464,436,463.5,3067000,470.11,-1.41,480.75,459.05,0.66
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 47.02
- over_600_ratio: 42.12
- over_800_ratio: 39.29
- over_1000_ratio: 35.73
- over_400_change_1w: -0.09
- over_800_change_1w: -0.51
- over_1000_change_1w: -1.91
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,53.58,-4.2,43.53,-1.85,41.31,-4.07,0,False,False
20260717,54.92,1.34,45.1,1.57,43.62,2.31,1,True,True
20260724,54.42,-0.5,42.54,-2.56,42.54,-1.08,0,False,False
20260731,52.94,-1.48,44.27,1.73,42.85,0.31,1,False,True
20260807,52.62,-0.32,43.61,-0.66,42.91,0.06,2,False,True
20260814,52.28,-0.34,43.94,0.33,40.32,-2.59,3,False,True
20260821,50.88,-1.4,44.14,0.2,40.38,0.06,4,False,True
20260828,51.84,0.96,45.23,1.09,43.01,2.63,5,True,True
20260904,48.44,-3.4,42.03,-3.2,41.33,-1.68,0,False,False
20260911,47.56,-0.88,42.22,0.19,39.45,-1.88,1,False,True
20260918,47.11,-0.45,39.8,-2.42,37.64,-1.81,0,False,False
20260924,47.02,-0.09,39.29,-0.51,35.73,-1.91,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4991 | 環宇-KY | pattern | 型態觀察 | 45.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/08/31 2.發生緣由:依櫃買中心通知辦理 3.財務業務資訊: (一)單月                   115年07月        114年07月       與去年同期增減% 營業收入(百萬元)             145               156                -7.05% 稅前淨利(百萬元)             -34                10              -440.00% 歸屬母公司業主淨利(百萬元)   -21                10              -310.00% 每股盈餘(元)                -0.18             0.09              -300.00% (二)單季                  115年第2季      114年第2季      與去年同期增減% 營業收入(百萬元)             770              490               57.14% 稅前淨利(百萬元)             134                6             2133.33% 歸屬母公司業主淨利(百萬元)   110               14              685.71% 每股盈餘(元)                0.92             0.13              607.69% (三)最近四季累計                    114年第3季至115年第2季 營業收入(百萬元)                            2,717 稅前淨利(百萬元)                              467 歸屬母公司業主淨利(百萬元)                    388 每股盈餘(元)                                 3.32 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註1：115年07月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註3：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 4991 | 環宇-KY | revenue_pullback | 營收成長股價回檔 | 76.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/31 2.發生緣由:依櫃買中心通知辦理 3.財務業務資訊: (一)單月                   115年07月        114年07月       與去年同期增減% 營業收入(百萬元)             145               156                -7.05% 稅前淨利(百萬元)             -34                10              -440.00% 歸屬母公司業主淨利(百萬元)   -21                10              -310.00% 每股盈餘(元)                -0.18             0.09              -300.00% (二)單季                  115年第2季      114年第2季      與去年同期增減% 營業收入(百萬元)             770              490               57.14% 稅前淨利(百萬元)             134                6             2133.33% 歸屬母公司業主淨利(百萬元)   110               14              685.71% 每股盈餘(元)                0.92             0.13              607.69% (三)最近四季累計                    114年第3季至115年第2季 營業收入(百萬元)                            2,717 稅前淨利(百萬元)                              467 歸屬母公司業主淨利(百萬元)                    388 每股盈餘(元)                                 3.32 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註1：115年07月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公 司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註3：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計 師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4991 | 環宇-KY | 8 | 8 | 5 | 8 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
