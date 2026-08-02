# INDIVIDUAL STOCK CHATGPT PACKET - 3652 精聯

## Metadata
- generated_at: 2026-08-02 22:27:24 Asia/Taipei
- stock_id: 3652
- stock_name: 精聯
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3652_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3652_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3652_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3652_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3652_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3652_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3652_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3652.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3652.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3652.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3652.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3652_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3652_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3652_latest.md?ref=main

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
- model_category_display_zh: 單一個股分析
- score_interpretation_zh: 目前缺少完整分數資料，需以價格、TDCC 與風險條件輔助判斷。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 單一個股分析 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260730
- open: 28.35
- high: 29.5
- low: 28.2
- close: 28.4
- volume: 231248
- ma5: 30.04
- ema23_primary: 32.44
- distance_to_ema23_pct: -12.45
- ma20: 32.55
- ma60: 33.64
- ma120: 30.85
- return_5d: -18.27
- return_20d: -23.14
- volume_ratio: 0.39
- distance_to_ma20_pct_auxiliary: -12.76
- distance_to_high_60_pct: -34.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,36.3,37.9,36.25,37.9,235971,36.95,2.56,37.06,32.61,0.23
20260703,37.5,38.5,37.35,38.5,135343,37.08,3.83,37.27,32.8,0.13
20260706,38.2,38.7,37.2,37.3,176238,37.1,0.54,37.44,32.97,0.17
20260707,37.1,37.1,35,35.1,348219,36.93,-4.96,37.6,33.1,0.34
20260708,35.2,35.2,33.6,34.6,282617,36.74,-5.82,37.66,33.22,0.27
20260709,34.65,34.65,33.8,33.9,201515,36.5,-7.13,37.72,33.32,0.19
20260713,33.85,33.85,32.4,32.4,220037,36.16,-10.4,37.72,33.4,0.21
20260714,32.4,32.4,30.8,32.05,220057,35.82,-10.52,37.55,33.47,0.21
20260715,31.65,31.65,30.75,31.25,117487,35.44,-11.82,37.3,33.52,0.12
20260716,31.4,31.85,30.75,30.8,348344,35.05,-12.13,36.99,33.57,0.36
20260717,30.05,30.05,28.8,29,260971,34.55,-16.05,36.58,33.59,0.28
20260720,28.95,31.9,28.9,31,1598418,34.25,-9.49,36.12,33.62,1.84
20260721,31.05,31.8,29.6,30.7,973308,33.95,-9.59,35.52,33.65,1.26
20260722,30.65,33.5,30.5,31.6,2896155,33.76,-6.39,35.06,33.68,4.52
20260723,34.75,34.75,34.75,34.75,446298,33.84,2.69,34.76,33.72,0.69
20260724,37.15,37.15,32.3,32.35,2220160,33.72,-4.05,34.32,33.73,3.11
20260727,32.35,32.35,31.1,31.4,231698,33.52,-6.34,33.91,33.72,0.36
20260728,30.85,31,29.25,29.25,460668,33.17,-11.81,33.45,33.7,0.73
20260729,29.9,29.9,27.8,28.8,309806,32.8,-12.21,32.98,33.67,0.5
20260730,28.35,29.5,28.2,28.4,231248,32.44,-12.45,32.55,33.64,0.39
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 72.16
- over_600_ratio: 69.72
- over_800_ratio: 67.82
- over_1000_ratio: 67.82
- over_400_change_1w: 0.11
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,71.57,0,68.91,0,67.58,0,0,False,False
20260522,71.57,0,68.91,0,67.58,0,0,False,False
20260529,71.58,0.01,68.92,0.01,67.59,0.01,1,True,True
20260605,71.58,0,68.92,0,67.59,0,0,False,False
20260612,71.57,-0.01,68.91,-0.01,67.58,-0.01,0,False,False
20260618,71.57,0,68.91,0,67.58,0,0,False,False
20260626,72.53,0.96,68.91,0,67.58,0,1,False,False
20260703,71.57,-0.96,68.91,0,67.58,0,0,False,False
20260709,71.57,0,68.91,0,67.58,0,0,False,False
20260717,71.57,0,68.91,0,67.58,0,0,False,False
20260724,72.05,0.48,67.71,-1.2,67.71,0.13,1,False,True
20260731,72.16,0.11,67.82,0.11,67.82,0.11,2,True,True
```

## Candidate Context
| status |
| --- |
| no rows |

## Repeat Appearance Context
| status |
| --- |
| no rows |

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
