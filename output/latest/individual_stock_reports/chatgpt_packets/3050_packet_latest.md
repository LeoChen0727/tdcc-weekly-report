# INDIVIDUAL STOCK CHATGPT PACKET - 3050 鈺德

## Metadata
- generated_at: 2026-06-21 22:23:16 Asia/Taipei
- stock_id: 3050
- stock_name: 鈺德
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 30
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3050_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3050_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3050_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3050_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3050_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3050_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3050_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3050.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3050.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3050.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3050.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3050_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3050_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3050_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260618
- open: 13
- high: 13.05
- low: 12.85
- close: 13
- volume: 987996
- ma5: 13
- ema23_primary: 12.86
- distance_to_ema23_pct: 1.12
- ma20: 12.91
- ma60: 12.83
- ma120: 13.22
- return_5d: 2.36
- return_20d: 7
- volume_ratio: 0.65
- distance_to_ma20_pct_auxiliary: 0.66
- distance_to_high_60_pct: -10.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,12.25,12.5,12.15,12.5,762105,12.35,1.19,12.21,12.92,1.19
20260525,12.6,12.85,12.3,12.75,1575940,12.39,2.94,12.23,12.91,2.3
20260526,12.8,12.95,12.15,12.35,1363058,12.38,-0.26,12.23,12.89,1.95
20260527,12.4,12.65,12.05,12.4,1299753,12.38,0.13,12.23,12.86,1.75
20260528,12.45,12.85,12.3,12.45,1204887,12.39,0.49,12.24,12.85,1.55
20260529,12.6,12.6,12.35,12.55,898638,12.4,1.18,12.26,12.83,1.12
20260601,12.5,12.8,12.4,12.75,1087585,12.43,2.56,12.28,12.83,1.3
20260602,12.75,13.25,12.55,13.2,1407409,12.5,5.63,12.32,12.84,1.6
20260603,13.45,14.5,13.1,14.1,7133127,12.63,11.64,12.42,12.85,5.94
20260604,13.9,14.15,13.6,13.6,2495214,12.71,7,12.48,12.87,1.95
20260605,13.6,13.9,13,13.45,1557607,12.77,5.31,12.54,12.88,1.18
20260608,12.25,12.8,12.25,12.8,920706,12.77,0.2,12.56,12.88,0.68
20260609,12.8,13,12.65,12.85,743335,12.78,0.54,12.58,12.88,0.56
20260610,12.8,13.15,12.65,12.85,1134542,12.79,0.5,12.62,12.88,0.84
20260611,12.7,12.9,12.4,12.7,1010206,12.78,-0.62,12.64,12.88,0.75
20260612,12.8,13.05,12.8,12.95,957018,12.79,1.22,12.7,12.88,0.7
20260615,13.1,13.4,13.1,13.3,1323953,12.84,3.62,12.77,12.88,0.94
20260616,13.35,13.35,12.8,12.8,1113221,12.83,-0.26,12.81,12.87,0.77
20260617,12.7,13.1,12.65,12.95,1576105,12.84,0.84,12.87,12.84,1.05
20260618,13,13.05,12.85,13,987996,12.86,1.12,12.91,12.83,0.65
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 53.22
- over_600_ratio: 49.4
- over_800_ratio: 47.21
- over_1000_ratio: 45
- over_400_change_1w: 0.41
- over_800_change_1w: -0.35
- over_1000_change_1w: -0.27
- tdcc_consecutive_up_weeks: 17
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260402,51.66,0.83,45.3,0.18,43.57,0.17,6,True,True
20260410,51.78,0.12,45.31,0.01,43.58,0.01,7,True,True
20260417,52.13,0.35,44.79,-0.52,43.59,0.01,8,False,True
20260424,51.34,-0.79,45.8,1.01,43.38,-0.21,9,False,True
20260430,51.3,-0.04,46.3,0.5,43.34,-0.04,10,False,True
20260508,51.33,0.03,45.82,-0.48,44.04,0.7,11,False,True
20260515,51.65,0.32,45.95,0.13,44.2,0.16,12,True,True
20260522,51.98,0.33,45.99,0.04,44.24,0.04,13,True,True
20260529,52.46,0.48,46.58,0.59,44.3,0.06,14,True,True
20260605,53.06,0.6,47.26,0.68,45.01,0.71,15,True,True
20260612,52.81,-0.25,47.56,0.3,45.27,0.26,16,False,True
20260618,53.22,0.41,47.21,-0.35,45,-0.27,17,False,False
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
