# INDIVIDUAL STOCK CHATGPT PACKET - 6127 九豪

## Metadata
- generated_at: 2026-09-06 22:17:52 Asia/Taipei
- stock_id: 6127
- stock_name: 九豪
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
- date: 20260904
- open: 47.6
- high: 49.7
- low: 47.6
- close: 49.05
- volume: 3088000
- ma5: 48.66
- ema23_primary: 50.61
- distance_to_ema23_pct: -3.09
- ma20: 49.73
- ma60: 62.71
- ma120: 56.76
- return_5d: -3.44
- return_20d: 1.98
- volume_ratio: 0.99
- distance_to_ma20_pct_auxiliary: -1.38
- distance_to_high_60_pct: -51.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,50.5,52.2,50.1,50.3,2624000,56.07,-10.3,53.56,67.19,0.64
20260811,50.2,54.3,50,51.6,6448000,55.7,-7.36,52.79,67.28,1.58
20260812,51.8,53.3,50.9,51.8,3570000,55.38,-6.46,51.94,67.32,0.91
20260813,52.6,55.9,52.5,52.8,6064000,55.16,-4.28,51.25,67.41,1.53
20260814,53.2,53.2,51.1,51.7,3600000,54.87,-5.78,50.83,67.4,0.91
20260817,51.5,51.5,49.95,50.4,1827000,54.5,-7.52,50.59,67.36,0.48
20260818,50.4,51.4,48.15,48.35,2025000,53.99,-10.44,50.2,67.29,0.54
20260819,46.9,51.5,46.7,49.7,4124000,53.63,-7.33,49.76,67.25,1.11
20260820,50.1,50.5,48.3,48.95,2100000,53.24,-8.06,49.39,67.11,0.58
20260821,49,49.5,48.5,48.7,1132000,52.86,-7.87,49.22,66.98,0.32
20260824,48.4,49.8,48.2,48.2,1101000,52.47,-8.14,48.96,66.76,0.32
20260825,48,48,46.15,47.75,1459000,52.08,-8.31,48.92,66.43,0.44
20260826,48.5,50.8,47.75,49.45,1852000,51.86,-4.65,49.12,66.02,0.58
20260827,49.65,51.2,49.35,50.9,2292000,51.78,-1.7,49.56,65.52,0.73
20260828,52.2,54.3,50.3,50.8,8176000,51.7,-1.74,49.8,65.12,2.39
20260831,50.9,52,47.85,48.4,2977000,51.42,-5.88,49.81,64.67,0.93
20260901,48.7,51.5,48.7,50.4,3928000,51.34,-1.83,49.88,64.25,1.23
20260902,49.45,50.2,48.55,48.6,2198000,51.11,-4.91,49.84,63.79,0.7
20260903,48.9,49.1,46.8,46.85,1821000,50.76,-7.69,49.69,63.18,0.59
20260904,47.6,49.7,47.6,49.05,3088000,50.61,-3.09,49.73,62.71,0.99
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 21.44
- over_600_ratio: 19.79
- over_800_ratio: 19.21
- over_1000_ratio: 16.83
- over_400_change_1w: -1.93
- over_800_change_1w: -2.53
- over_1000_change_1w: -2.45
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,25.34,2.76,21.17,4.67,20.34,4.67,1,True,True
20260626,30.12,4.78,24.03,2.86,23.13,2.79,2,True,True
20260703,25.6,-4.52,23.59,-0.44,22.7,-0.43,0,False,False
20260709,22.17,-3.43,17.72,-5.87,16.85,-5.85,0,False,False
20260717,21.92,-0.25,18.49,0.77,16.96,0.11,1,False,True
20260724,22.3,0.38,19.7,1.21,18.96,2,2,True,True
20260731,23.54,1.24,18.6,-1.1,17.69,-1.27,3,False,False
20260807,23.17,-0.37,20.11,1.51,16.64,-1.05,4,False,True
20260814,22.11,-1.06,18.92,-1.19,15.67,-0.97,0,False,False
20260821,22.46,0.35,19.33,0.41,17.67,2,1,True,True
20260828,23.37,0.91,21.74,2.41,19.28,1.61,2,True,True
20260904,21.44,-1.93,19.21,-2.53,16.83,-2.45,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6127 | 九豪 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/07/02 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊:   (1)單月                             最近一月單月     去年同月       與去年同期                               (115/5)         (114/5)           增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)               88              83             6.0%    稅前淨利(百萬元)              -17             -30            43.3%    本期淨利(百萬元)              -17             -30            43.3%    每股盈餘(元)                -0.16           -0.28            42.9%   =======================  ==============  ==============  ==============    (2)單季                            最近一季單季     去年同期       與去年同期                             (115第1季)      (114第1季)        增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)              243            252             -3.6%    稅前淨利(損)(百萬元)          -62             90           -168.9%    本期淨利(損)(百萬元)          -55             46           -219.6%    每股盈餘(元)                -0.51           0.42           -221.4%   =======================  ==============  ==============  ==============    (3)最近四季累計                               114年第2季至115年第1季   -----------------------  -----------------------------    營業收入(百萬元)                    984    稅前淨利(百萬元)                    (65)    本期淨利(百萬元)                    (50)    每股盈餘(元)                      (0.46)    每股面額：10元  4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項:   (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之      合併數，未經會計師查核(閱)，僅供投資人參考。   (2)最近一季115年第1季係指單季數字，業經會計師查核(閱)，僅供投資人參考。   (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經      會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6127 | 九豪 | 1 | 1 | 2 | 4 | 4 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
