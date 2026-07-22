# INDIVIDUAL STOCK CHATGPT PACKET - 3624 光頡

## Metadata
- generated_at: 2026-07-22 22:27:58 Asia/Taipei
- stock_id: 3624
- stock_name: 光頡
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3624_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3624_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3624_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3624_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3624_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3624_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3624_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3624.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3624.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3624.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3624.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3624_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3624_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3624_latest.md?ref=main

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
- date: 20260717
- open: 101.5
- high: 105
- low: 97.7
- close: 97.7
- volume: 5211000
- ma5: 113.54
- ema23_primary: 128.47
- distance_to_ema23_pct: -23.95
- ma20: 141.21
- ma60: 104.79
- ma120: 79.96
- return_5d: -32.15
- return_20d: -33.08
- volume_ratio: 1.11
- distance_to_ma20_pct_auxiliary: -30.81
- distance_to_high_60_pct: -45.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,160.5,160.5,160.5,160.5,3604000,112.39,42.81,113.95,76.33,0.31
20260622,171.5,176.5,165.5,176.5,16410000,117.73,49.92,118.2,78.47,1.32
20260623,172,178,159,159,19730000,121.17,31.22,121.45,80.31,1.47
20260624,157.5,157.5,143.5,147.5,4084000,123.36,19.57,124.15,81.96,0.3
20260625,149.5,157,143.5,154,1942000,125.92,22.3,127.15,83.73,0.14
20260626,150,154,139,139,2020000,127.01,9.44,129.1,85.26,0.15
20260629,143,145,137.5,139,1304000,128.01,8.59,130.55,86.82,0.09
20260630,147,152.5,147,152.5,1137000,130.05,17.26,132.53,88.58,0.08
20260701,163,163,150,154.5,1480000,132.09,16.97,134.15,90.39,0.11
20260702,152,159,151.5,153.5,921000,133.87,14.66,136.07,92.19,0.07
20260703,153.5,158,147.5,155,744000,135.63,14.28,138.65,93.98,0.05
20260706,155,155,142,148,1895000,136.66,8.3,140.65,95.65,0.13
20260707,148,155,133.5,133.5,2025000,136.4,-2.12,142.2,97.05,0.15
20260708,136.5,140,125,140,1461000,136.7,2.42,143.57,98.51,0.12
20260709,144,147,143,144,1436000,137.31,4.87,145.1,100.03,0.13
20260713,142.5,146,130,130,7381000,136.7,-4.9,146.1,101.28,0.74
20260714,128.5,133,117,117.5,9710000,135.1,-13.03,146.07,102.31,1.03
20260715,120,120,111.5,114,5983000,133.34,-14.5,145.3,103.26,0.72
20260716,112,115,107.5,108.5,5441000,131.27,-17.35,143.62,104.11,0.86
20260717,101.5,105,97.7,97.7,5211000,128.47,-23.95,141.21,104.79,1.11
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 59.2
- over_600_ratio: 57.6
- over_800_ratio: 54.71
- over_1000_ratio: 52.54
- over_400_change_1w: -2.15
- over_800_change_1w: -3.79
- over_1000_change_1w: -4.43
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,48.62,,45.62,,43.34,,0,False,False
20260508,49.91,1.29,47.2,1.58,43.4,0.06,1,True,True
20260515,58.62,8.71,53.17,5.97,49.22,5.82,2,True,True
20260522,61.02,2.4,57.24,4.07,54.08,4.86,3,True,True
20260529,61.9,0.88,55.75,-1.49,53.49,-0.59,4,False,False
20260605,57.82,-4.08,51.3,-4.45,49.12,-4.37,0,False,False
20260612,59.33,1.51,54.35,3.05,52.91,3.79,1,True,True
20260618,61.13,1.8,58.07,3.72,55.91,3,2,True,True
20260626,61.81,0.68,57.75,-0.32,56.21,0.3,3,False,True
20260703,63.14,1.33,58.95,1.2,57.37,1.16,4,True,True
20260709,61.35,-1.79,58.5,-0.45,56.97,-0.4,0,False,False
20260717,59.2,-2.15,54.71,-3.79,52.54,-4.43,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3624 | 光頡 | revenue_pullback | 營收成長股價回檔 | 60.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理公告。 3.財務業務資訊: (1)單月                             最近一月單月    去年同月      與去年同期增減% 期間                          (115/5)      (114/5) -------------------------------------------------------------------------- 營業收入(百萬元)                  290          222               30.63% 稅前淨利(百萬元)                   53          -11              581.82% 歸屬母公司業主淨利(百萬元)         37          -13              384.62% 每股盈餘(元)                     0.32        -0.11              390.91%  (2)單季                             最近一季單季     去年同期      與去年同期增減% 期間                          (115第1季)    (114第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                  728           619              17.61% 稅前淨利(百萬元)                  118            81              45.68% 歸屬母公司業主淨利(百萬元)         88            63              39.68% 每股盈餘(元)                     0.75          0.54              38.89%  (3)最近四季累計 期間                    (114年第2季至115年第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                2,784 稅前淨利(百萬元)                  317 歸屬母公司業主淨利(百萬元)        243 每股盈餘(元)                     2.07 -------------------------------------------------------------------------- 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司 依IFRS會計準則編製之合併自結數，未經會計師查核(核閱)， 僅供投資人參考。 (2)最近一季115年第1季及去年同期比較數係指單季數字， 係本公司依IFRS下編製之合併數，業係經會計師核閱，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季由本公司依IFRS編製之 合併數業經會計師查核(核閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3624 | 光頡 | 2 | 2 | 4 | 8 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
