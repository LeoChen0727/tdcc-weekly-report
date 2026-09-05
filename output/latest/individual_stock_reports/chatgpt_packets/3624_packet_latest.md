# INDIVIDUAL STOCK CHATGPT PACKET - 3624 光頡

## Metadata
- generated_at: 2026-09-05 22:16:42 Asia/Taipei
- stock_id: 3624
- stock_name: 光頡
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
- date: 20260904
- open: 87.6
- high: 93.2
- low: 87.6
- close: 93.2
- volume: 9062000
- ma5: 89.1
- ema23_primary: 88.79
- distance_to_ema23_pct: 4.97
- ma20: 88.38
- ma60: 106.25
- ma120: 87.16
- return_5d: 1.53
- return_20d: 24.6
- volume_ratio: 1.34
- distance_to_ma20_pct_auxiliary: 5.45
- distance_to_high_60_pct: -47.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,76,82.2,76,82.2,5119000,87.87,-6.45,82.88,109.92,1.65
20260811,82.2,89.4,80.3,85.2,12178000,87.65,-2.79,81.26,110.07,3.77
20260812,86.2,88.4,83.6,86.5,5990000,87.55,-1.2,79.89,110.11,1.85
20260813,88.5,95.1,88.5,95.1,7581000,88.18,7.85,79.22,110.18,2.27
20260814,96.2,99.4,86.6,89.5,11082000,88.29,1.37,78.81,110.17,3.05
20260817,87.9,89.9,85,87.5,3735000,88.23,-0.82,78.7,110.11,1.05
20260818,86.5,89.4,84.8,84.8,3335000,87.94,-3.57,78.4,109.99,1
20260819,82.5,93,82.5,89.7,10443000,88.09,1.83,78.19,109.92,2.77
20260820,90.4,92.4,85.4,86.3,6404000,87.94,-1.86,77.83,109.8,1.58
20260821,85.7,91.7,85.7,87.8,8009000,87.93,-0.14,78,109.7,1.81
20260824,86.9,89.1,86,86.1,3115000,87.77,-1.91,78.46,109.47,0.69
20260825,85.9,87.5,81.8,87.5,3088000,87.75,-0.29,79.38,109.09,0.67
20260826,87.5,95.8,86.3,91.2,6433000,88.04,3.59,80.82,108.73,1.31
20260827,91.4,94.3,88.6,90.9,7376000,88.28,2.97,82.52,108.21,1.44
20260828,93.9,98.9,90.5,91.8,14234000,88.57,3.65,83.98,107.82,2.49
20260831,90.7,94,87.3,88.3,5187000,88.55,-0.28,85.18,107.57,0.88
20260901,88.5,93.4,88.5,90.2,4833000,88.69,1.71,86.29,107.27,0.8
20260902,89.8,92.9,89,89,4938000,88.71,0.32,87,107.05,0.79
20260903,89.5,89.9,84.8,84.8,3522000,88.39,-4.06,87.46,106.59,0.55
20260904,87.6,93.2,87.6,93.2,9062000,88.79,4.97,88.38,106.25,1.34
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 53.37
- over_600_ratio: 50.56
- over_800_ratio: 48.39
- over_1000_ratio: 46.8
- over_400_change_1w: -1.96
- over_800_change_1w: -3.02
- over_1000_change_1w: -1.58
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,61.13,1.8,58.07,3.72,55.91,3,2,True,True
20260626,61.81,0.68,57.75,-0.32,56.21,0.3,3,False,True
20260703,63.14,1.33,58.95,1.2,57.37,1.16,4,True,True
20260709,61.35,-1.79,58.5,-0.45,56.97,-0.4,0,False,False
20260717,59.2,-2.15,54.71,-3.79,52.54,-4.43,0,False,False
20260724,59.26,0.06,55.49,0.78,54.75,2.21,1,True,True
20260731,57.41,-1.85,53.4,-2.09,51.88,-2.87,0,False,False
20260807,56.9,-0.51,52.49,-0.91,52.49,0.61,1,False,True
20260814,55.83,-1.07,52.22,-0.27,49.99,-2.5,0,False,False
20260821,54.51,-1.32,50.92,-1.3,47.87,-2.12,0,False,False
20260828,55.33,0.82,51.41,0.49,48.38,0.51,1,False,True
20260904,53.37,-1.96,48.39,-3.02,46.8,-1.58,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3624 | 光頡 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | repeated_but_no_breakout | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理公告。 3.財務業務資訊: (1)單月                             最近一月單月    去年同月      與去年同期增減% 期間                          (115/5)      (114/5) -------------------------------------------------------------------------- 營業收入(百萬元)                  290          222               30.63% 稅前淨利(百萬元)                   53          -11              581.82% 歸屬母公司業主淨利(百萬元)         37          -13              384.62% 每股盈餘(元)                     0.32        -0.11              390.91%  (2)單季                             最近一季單季     去年同期      與去年同期增減% 期間                          (115第1季)    (114第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                  728           619              17.61% 稅前淨利(百萬元)                  118            81              45.68% 歸屬母公司業主淨利(百萬元)         88            63              39.68% 每股盈餘(元)                     0.75          0.54              38.89%  (3)最近四季累計 期間                    (114年第2季至115年第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                2,784 稅前淨利(百萬元)                  317 歸屬母公司業主淨利(百萬元)        243 每股盈餘(元)                     2.07 -------------------------------------------------------------------------- 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司 依IFRS會計準則編製之合併自結數，未經會計師查核(核閱)， 僅供投資人參考。 (2)最近一季115年第1季及去年同期比較數係指單季數字， 係本公司依IFRS下編製之合併數，業係經會計師核閱，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季由本公司依IFRS編製之 合併數業經會計師查核(核閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3624 | 光頡 | 1 | 1 | 3 | 5 | 12 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 12 次，但尚未有效突破，需等待攻擊確認。 |

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
