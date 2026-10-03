# INDIVIDUAL STOCK CHATGPT PACKET - 6127 九豪

## Metadata
- generated_at: 2026-10-03 22:17:54 Asia/Taipei
- stock_id: 6127
- stock_name: 九豪
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6127_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6127_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6127_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6127_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6127_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6127_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6127_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6127.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6127.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6127.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6127.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6127_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6127_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6127_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20261002
- open: 57
- high: 59.6
- low: 55.8
- close: 58.4
- volume: 29437000
- ma5: 53.14
- ema23_primary: 50.71
- distance_to_ema23_pct: 15.16
- ma20: 49.63
- ma60: 52.22
- ma120: 58.01
- return_5d: 21.79
- return_20d: 20.16
- volume_ratio: 6.26
- distance_to_ma20_pct_auxiliary: 17.68
- distance_to_high_60_pct: -25.7

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,48.9,49.1,46.8,46.85,1821000,50.76,-7.69,49.69,63.18,0.59
20260904,47.6,49.7,47.6,49.05,3088000,50.61,-3.09,49.73,62.71,0.99
20260907,50,50.9,49.45,49.65,2483000,50.53,-1.75,49.7,62.22,0.8
20260908,49.75,50,48.2,48.2,1832000,50.34,-4.25,49.53,61.76,0.64
20260909,48.5,51.9,48.1,51.8,3552000,50.46,2.66,49.53,61.31,1.23
20260910,49.95,50.3,48.35,49,6237000,50.34,-2.66,49.34,60.85,2.16
20260911,48.05,49.85,47.2,47.3,3997000,50.09,-5.56,49.12,60.29,1.37
20260914,46.95,47.95,45.4,47.45,2074000,49.87,-4.84,48.98,59.68,0.71
20260915,47.15,48.8,46.75,46.75,2057000,49.61,-5.76,48.9,59.03,0.7
20260916,47.2,48.95,46.9,48.55,1640000,49.52,-1.96,48.84,58.49,0.59
20260917,48.8,49.7,47.8,48.4,1615000,49.42,-2.07,48.81,57.88,0.58
20260918,49.1,49.65,48.3,48.85,1299000,49.38,-1.07,48.82,57.14,0.47
20260921,49.05,49.7,48.9,48.9,1670000,49.34,-0.89,48.85,56.43,0.59
20260922,49.8,50.2,48.05,48.15,1794000,49.24,-2.21,48.87,55.82,0.63
20260923,48.6,49.3,47.95,47.95,1215000,49.13,-2.4,48.8,55.07,0.43
20260924,47.55,48.9,47.4,47.8,1309000,49.02,-2.49,48.64,54.26,0.48
20260929,48.45,51.7,47.9,51,6392000,49.19,3.69,48.65,53.59,2.4
20260930,52,52.3,50,51.7,4064000,49.39,4.67,48.82,52.99,1.5
20261001,52.3,56.8,52.2,56.8,16443000,50.01,13.57,49.14,52.54,4.92
20261002,57,59.6,55.8,58.4,29437000,50.71,15.16,49.63,52.22,6.26
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 25.26
- over_600_ratio: 23.54
- over_800_ratio: 22.91
- over_1000_ratio: 19.74
- over_400_change_1w: 3.19
- over_800_change_1w: 4.37
- over_1000_change_1w: 1.98
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,21.92,-0.25,18.49,0.77,16.96,0.11,1,False,True
20260724,22.3,0.38,19.7,1.21,18.96,2,2,True,True
20260731,23.54,1.24,18.6,-1.1,17.69,-1.27,3,False,False
20260807,23.17,-0.37,20.11,1.51,16.64,-1.05,4,False,True
20260814,22.11,-1.06,18.92,-1.19,15.67,-0.97,0,False,False
20260821,22.46,0.35,19.33,0.41,17.67,2,1,True,True
20260828,23.37,0.91,21.74,2.41,19.28,1.61,2,True,True
20260904,21.44,-1.93,19.21,-2.53,16.83,-2.45,0,False,False
20260911,22.16,0.72,17.74,-1.47,17,0.17,1,False,True
20260918,21.12,-1.04,18.28,0.54,16.65,-0.35,2,False,True
20260924,22.07,0.95,18.54,0.26,17.76,1.11,3,True,True
20261002,25.26,3.19,22.91,4.37,19.74,1.98,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6127 | 九豪 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | continued_overheated | 1.事實發生日:115/07/02 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊:   (1)單月                             最近一月單月     去年同月       與去年同期                               (115/5)         (114/5)           增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)               88              83             6.0%    稅前淨利(百萬元)              -17             -30            43.3%    本期淨利(百萬元)              -17             -30            43.3%    每股盈餘(元)                -0.16           -0.28            42.9%   =======================  ==============  ==============  ==============    (2)單季                            最近一季單季     去年同期       與去年同期                             (115第1季)      (114第1季)        增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)              243            252             -3.6%    稅前淨利(損)(百萬元)          -62             90           -168.9%    本期淨利(損)(百萬元)          -55             46           -219.6%    每股盈餘(元)                -0.51           0.42           -221.4%   =======================  ==============  ==============  ==============    (3)最近四季累計                               114年第2季至115年第1季   -----------------------  -----------------------------    營業收入(百萬元)                    984    稅前淨利(百萬元)                    (65)    本期淨利(百萬元)                    (50)    每股盈餘(元)                      (0.46)    每股面額：10元  4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項:   (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之      合併數，未經會計師查核(閱)，僅供投資人參考。   (2)最近一季115年第1季係指單季數字，業經會計師查核(閱)，僅供投資人參考。   (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經      會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6127 | 九豪 | 2 | 2 | 3 | 5 | 9 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
