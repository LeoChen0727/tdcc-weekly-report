# INDIVIDUAL STOCK CHATGPT PACKET - 6122 擎邦

## Metadata
- generated_at: 2026-08-02 22:28:02 Asia/Taipei
- stock_id: 6122
- stock_name: 擎邦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6122_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6122_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6122_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6122_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6122.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6122.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6122.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6122.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6122_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6122_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6122_latest.md?ref=main

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
- date: 20260730
- open: 48.7
- high: 49.45
- low: 48.6
- close: 48.8
- volume: 226000
- ma5: 49.43
- ema23_primary: 49.94
- distance_to_ema23_pct: -2.28
- ma20: 50.88
- ma60: 48.73
- ma120: 49.97
- return_5d: -3.75
- return_20d: -0.41
- volume_ratio: 0.38
- distance_to_ma20_pct_auxiliary: -4.09
- distance_to_high_60_pct: -8.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,49.65,52,49.2,52,2010000,47.99,8.35,47.7,48.47,6.76
20260703,52,52.5,50.9,51.5,944000,48.28,6.66,47.86,48.48,2.76
20260706,52,52.3,50.9,51.6,546000,48.56,6.26,48.01,48.49,1.49
20260707,51.6,51.7,49.95,50.4,454000,48.71,3.46,48.14,48.47,1.22
20260708,50.5,52,49.85,51.9,593000,48.98,5.96,48.35,48.5,1.5
20260709,51.9,52.5,50.7,51.8,648000,49.21,5.25,48.55,48.52,1.55
20260713,52.5,53,51.7,52,977000,49.45,5.16,48.84,48.55,2.2
20260714,52.6,53.2,51.2,51.2,862000,49.59,3.24,49.08,48.56,1.81
20260715,51.5,53.1,51.5,53.1,1048000,49.88,6.44,49.37,48.6,2.04
20260716,53,53,51.8,51.9,464000,50.05,3.69,49.62,48.63,0.87
20260717,51.6,52.7,50.2,50.6,745000,50.1,1,49.8,48.63,1.32
20260720,51,51.2,49.85,50.9,337000,50.17,1.46,50,48.64,0.59
20260721,51,51.3,50.5,50.6,404000,50.2,0.79,50.16,48.66,0.7
20260722,51.3,51.3,50.3,50.3,274000,50.21,0.18,50.34,48.68,0.47
20260723,50.5,51.2,50.3,50.7,278000,50.25,0.89,50.49,48.72,0.47
20260724,51,51,49.8,49.8,310000,50.21,-0.82,50.58,48.73,0.52
20260727,49.8,50.8,49.3,50.4,211000,50.23,0.34,50.74,48.75,0.35
20260728,50.4,50.4,48.8,49.15,295000,50.14,-1.97,50.83,48.75,0.49
20260729,49.25,49.7,48,49,408000,50.04,-2.09,50.89,48.75,0.66
20260730,48.7,49.45,48.6,48.8,226000,49.94,-2.28,50.88,48.73,0.38
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 30.99
- over_600_ratio: 29.73
- over_800_ratio: 24.28
- over_1000_ratio: 21.92
- over_400_change_1w: -0.56
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,30.09,-0.22,22.85,-0.01,20.49,-0.01,0,False,False
20260522,30.23,0.14,22.85,0,20.49,0,1,False,False
20260529,30.19,-0.04,22.84,-0.01,20.48,-0.01,0,False,False
20260605,30.11,-0.08,22.85,0.01,20.49,0.01,1,False,True
20260612,29.55,-0.56,22.84,-0.01,20.48,-0.01,0,False,False
20260618,29.55,0,22.84,0,20.48,0,0,False,False
20260626,29.55,0,22.84,0,20.48,0,0,False,False
20260703,29.57,0.02,22.86,0.02,20.5,0.02,1,True,True
20260709,30.79,1.22,22.88,0.02,20.52,0.02,2,True,True
20260717,31.65,0.86,24.24,1.36,21.88,1.36,3,True,True
20260724,31.55,-0.1,24.27,0.03,21.91,0.03,4,False,True
20260731,30.99,-0.56,24.28,0.01,21.92,0.01,5,False,True
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
