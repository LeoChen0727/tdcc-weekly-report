# INDIVIDUAL STOCK CHATGPT PACKET - 3432 台端

## Metadata
- generated_at: 2026-06-21 22:23:26 Asia/Taipei
- stock_id: 3432
- stock_name: 台端
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 283
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3432_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3432_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3432_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3432_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3432_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3432_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3432_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3432.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3432.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3432.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3432.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3432_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3432_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3432_latest.md?ref=main

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
- open: 18.5
- high: 19.35
- low: 18.5
- close: 18.7
- volume: 55501
- ma5: 18.46
- ema23_primary: 18.71
- distance_to_ema23_pct: -0.06
- ma20: 18.72
- ma60: 18.44
- ma120: 17.41
- return_5d: -3.86
- return_20d: -1.58
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: -0.09
- distance_to_high_60_pct: -19.91

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,19,19.15,18.6,19.15,73895,19.21,-0.34,20.09,17.83,0.2
20260525,18.65,20.15,18.6,19.9,283394,19.27,3.26,20.14,17.87,0.78
20260526,20.5,20.5,19,19.35,92913,19.28,0.37,20.09,17.9,0.28
20260527,19.35,19.35,18.75,18.85,71965,19.24,-2.04,19.9,17.93,0.28
20260528,19.1,19.3,18.6,18.75,91616,19.2,-2.35,19.77,17.95,0.4
20260529,18.65,19.65,18.5,18.8,106033,19.17,-1.92,19.75,17.99,0.5
20260601,18.8,19.2,18.7,18.8,59773,19.14,-1.76,19.62,18.03,0.3
20260602,19.15,19.15,18.65,18.8,89296,19.11,-1.62,19.43,18.07,0.55
20260603,18.6,18.9,18.5,18.8,81458,19.08,-1.49,19.32,18.1,0.59
20260604,18.8,18.8,18.45,18.5,48846,19.04,-2.81,19.2,18.13,0.38
20260605,18.5,18.8,18.25,18.45,69735,18.99,-2.82,19.11,18.15,0.6
20260608,16.75,17.95,16.75,17.95,21283,18.9,-5.03,19.02,18.17,0.21
20260609,17.7,18.6,17.7,18.6,34658,18.87,-1.46,18.98,18.2,0.38
20260610,17.35,18.2,17.35,17.9,52753,18.79,-4.75,18.89,18.23,0.6
20260611,19.6,19.6,18,19.45,89680,18.85,3.19,18.9,18.27,1.05
20260612,19.4,19.4,18,18.7,77230,18.84,-0.72,18.88,18.31,0.93
20260615,18.75,18.95,18.35,18.5,53872,18.81,-1.64,18.82,18.34,0.68
20260616,18.45,18.8,18,18,69284,18.74,-3.95,18.75,18.37,0.87
20260617,18.35,18.6,18.3,18.4,22217,18.71,-1.67,18.73,18.41,0.29
20260618,18.5,19.35,18.5,18.7,55501,18.71,-0.06,18.72,18.44,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 66.5
- over_600_ratio: 64.06
- over_800_ratio: 62.56
- over_1000_ratio: 58.48
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,66.5,,62.56,,58.48,,0,False,False
20260508,66.5,0,62.56,0,58.48,0,0,False,False
20260515,66.5,0,62.56,0,58.48,0,0,False,False
20260522,66.5,0,62.56,0,58.48,0,0,False,False
20260529,66.5,0,62.56,0,58.48,0,0,False,False
20260605,66.5,0,62.56,0,58.48,0,0,False,False
20260612,66.5,0,62.56,0,58.48,0,0,False,False
20260618,66.5,0,62.56,0,58.48,0,0,False,False
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
