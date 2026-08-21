# INDIVIDUAL STOCK CHATGPT PACKET - 2465 麗臺

## Metadata
- generated_at: 2026-08-21 22:27:01 Asia/Taipei
- stock_id: 2465
- stock_name: 麗臺
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2465_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2465_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2465_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2465_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2465_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2465_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2465_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2465.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2465.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2465.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2465.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2465_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2465_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2465_latest.md?ref=main

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
- date: 20260821
- open: 86.6
- high: 89.3
- low: 85
- close: 85.9
- volume: 3498808
- ma5: 86.92
- ema23_primary: 85.58
- distance_to_ema23_pct: 0.37
- ma20: 84.43
- ma60: 81.12
- ma120: 73.6
- return_5d: -10.43
- return_20d: 6.71
- volume_ratio: 0.9
- distance_to_ma20_pct_auxiliary: 1.74
- distance_to_high_60_pct: -19.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,80.5,80.5,77.2,79,844435,79.36,-0.46,78.28,80.42,0.4
20260728,76.9,77,74.3,74.6,884545,78.96,-5.53,78.48,80.43,0.42
20260729,75,76,69,72.6,1648382,78.43,-7.44,78.56,80.29,0.76
20260730,71.5,73,67.4,67.6,1208160,77.53,-12.81,78.36,79.92,0.55
20260731,72.5,74.3,72.3,73.4,783087,77.19,-4.91,78.5,79.73,0.35
20260803,72.7,78,72.4,75.5,684932,77.05,-2.01,78.61,79.55,0.31
20260804,75.3,78.4,75.2,78,711541,77.13,1.13,78.73,79.5,0.32
20260805,80.1,85.8,79.6,85.8,3001815,77.85,10.21,79.32,79.49,1.28
20260806,86.3,89.4,83.2,85.5,3916388,78.49,8.94,79.53,79.49,1.63
20260807,85.5,87.2,83.6,85.1,1499084,79.04,7.67,79.31,79.52,0.71
20260810,90,93.6,87.7,93.6,7060430,80.25,16.63,79.69,79.7,3.6
20260811,94.6,95.8,86.8,86.9,5914780,80.81,7.54,79.79,79.86,2.88
20260812,87.5,95.5,87.2,95.5,8870219,82.03,16.42,80.4,80.19,3.72
20260813,99.1,105,95.7,105,12841286,83.94,25.08,81.61,80.68,4.33
20260814,106,106.5,95.8,95.9,8885098,84.94,12.9,82.58,81.02,2.68
20260817,95.9,96.5,87,90.6,5379521,85.41,6.07,83.39,81.14,1.53
20260818,90.6,91.6,85.5,86.2,3913211,85.48,0.85,83.83,81.15,1.06
20260819,85,90.5,84.4,85.9,3986951,85.51,0.45,84,81.14,1.06
20260820,86.5,88.6,84.5,86,2625968,85.55,0.52,84.16,81.12,0.7
20260821,86.6,89.3,85,85.9,3498808,85.58,0.37,84.43,81.12,0.9
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 45.43
- over_600_ratio: 40.74
- over_800_ratio: 36.86
- over_1000_ratio: 35.85
- over_400_change_1w: 6.03
- over_800_change_1w: 6.41
- over_1000_change_1w: 6.27
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,38.48,2.23,32.11,1.51,31.15,1.5,2,True,True
20260605,36.47,-2.01,31.72,-0.39,30.8,-0.35,0,False,False
20260612,35.96,-0.51,31.62,-0.1,29.58,-1.22,0,False,False
20260618,36.28,0.32,31.67,0.05,30.72,1.14,1,False,True
20260626,35.51,-0.77,29.58,-2.09,29.58,-1.14,0,False,False
20260703,35.67,0.16,29.58,0,29.58,0,1,False,False
20260709,36.46,0.79,30.71,1.13,30.71,1.13,2,True,True
20260717,36.66,0.2,30.6,-0.11,29.58,-1.13,3,False,False
20260724,37.34,0.68,30.58,-0.02,29.58,0,4,False,False
20260731,36.35,-0.99,29.58,-1,29.58,0,0,False,False
20260807,39.4,3.05,30.45,0.87,29.58,0,1,False,True
20260814,45.43,6.03,36.86,6.41,35.85,6.27,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2465 | 麗臺 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | repeated_but_no_breakout | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):4,074,873 5.1月1日累計至本期止營業毛利(毛損) (仟元):474,947 6.1月1日累計至本期止營業利益(損失) (仟元):265,271 7.1月1日累計至本期止稅前淨利(淨損) (仟元):305,368 8.1月1日累計至本期止本期淨利(淨損) (仟元):261,923 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):261,923 10.1月1日累計至本期止基本每股盈餘(損失) (元):2.79 11.期末總資產(仟元):2,375,431 12.期末總負債(仟元):1,012,098 13.期末歸屬於母公司業主之權益(仟元):1,363,333 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2465 | 麗臺 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):4,074,873 5.1月1日累計至本期止營業毛利(毛損) (仟元):474,947 6.1月1日累計至本期止營業利益(損失) (仟元):265,271 7.1月1日累計至本期止稅前淨利(淨損) (仟元):305,368 8.1月1日累計至本期止本期淨利(淨損) (仟元):261,923 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):261,923 10.1月1日累計至本期止基本每股盈餘(損失) (元):2.79 11.期末總資產(仟元):2,375,431 12.期末總負債(仟元):1,012,098 13.期末歸屬於母公司業主之權益(仟元):1,363,333 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 2465 | 麗臺 | revenue_breakout_low_response | 營收爆發低反應股 | 23 | 4 | A_優先追蹤 |  |  |  | repeated_but_no_breakout | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):4,074,873 5.1月1日累計至本期止營業毛利(毛損) (仟元):474,947 6.1月1日累計至本期止營業利益(損失) (仟元):265,271 7.1月1日累計至本期止稅前淨利(淨損) (仟元):305,368 8.1月1日累計至本期止本期淨利(淨損) (仟元):261,923 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):261,923 10.1月1日累計至本期止基本每股盈餘(損失) (元):2.79 11.期末總資產(仟元):2,375,431 12.期末總負債(仟元):1,012,098 13.期末歸屬於母公司業主之權益(仟元):1,363,333 14.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2465 | 麗臺 | 11 | 3 | 5 | 10 | 13 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 13 次，但尚未有效突破，需等待攻擊確認。 |

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
