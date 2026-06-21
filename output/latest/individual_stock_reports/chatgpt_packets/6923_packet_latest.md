# INDIVIDUAL STOCK CHATGPT PACKET - 6923 中台

## Metadata
- generated_at: 2026-06-21 22:24:29 Asia/Taipei
- stock_id: 6923
- stock_name: 中台
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6923_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6923_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6923_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6923_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6923_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6923_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6923_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6923.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6923.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6923.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6923.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6923_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6923_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6923_latest.md?ref=main

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
- open: 77.5
- high: 77.8
- low: 76.7
- close: 77.7
- volume: 166103
- ma5: 78.78
- ema23_primary: 78.84
- distance_to_ema23_pct: -1.45
- ma20: 78.38
- ma60: 79.56
- ma120: 87.32
- return_5d: -1.02
- return_20d: -1.15
- volume_ratio: 1.06
- distance_to_ma20_pct_auxiliary: -0.87
- distance_to_high_60_pct: -12.99

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,78,79.2,77,79.2,173893,80.68,-1.83,81.83,82.38,0.78
20260525,78.6,80.4,78.4,78.7,167419,80.51,-2.25,81.58,82.11,0.76
20260526,78.6,79.3,78.1,78.8,203268,80.37,-1.95,81.31,81.88,0.92
20260527,79.9,79.9,78.4,78.5,228200,80.21,-2.14,80.98,81.65,1.02
20260528,79.2,79.2,77.2,77.8,123239,80.01,-2.76,80.56,81.43,0.56
20260529,78,78.2,77.1,77.6,161492,79.81,-2.77,80.17,81.23,0.75
20260601,77.6,77.7,76.6,77.3,165407,79.6,-2.89,79.81,81.09,0.79
20260602,77.4,77.5,76.7,77.2,98082,79.4,-2.77,79.39,80.91,0.5
20260603,77.5,78.8,77.4,78.3,154497,79.31,-1.27,79.17,80.7,0.83
20260604,78.6,79.8,78.5,79.3,277879,79.31,-0.01,78.97,80.59,1.45
20260605,79.8,79.8,78.2,78.7,99293,79.26,-0.7,78.75,80.45,0.53
20260608,76.1,77.8,76.1,77.2,156299,79.09,-2.39,78.57,80.27,0.84
20260609,77.1,79.8,77,78.1,103404,79,-1.14,78.38,80.14,0.6
20260610,76.7,79.5,76.7,78.5,145101,78.96,-0.59,78.22,80.02,0.86
20260611,78.5,78.9,77.6,78.5,83079,78.92,-0.54,78.16,79.88,0.52
20260612,78.5,79,78,78.4,50251,78.88,-0.61,78.12,79.76,0.33
20260615,79.6,82.2,79.3,80.8,196853,79.04,2.23,78.32,79.68,1.28
20260616,81.6,82.2,78,80,219281,79.12,1.11,78.45,79.65,1.39
20260617,77.3,78.6,76.2,77,165402,78.94,-2.46,78.42,79.57,1.04
20260618,77.5,77.8,76.7,77.7,166103,78.84,-1.45,78.38,79.56,1.06
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 69.46
- over_600_ratio: 64.9
- over_800_ratio: 58.67
- over_1000_ratio: 53.6
- over_400_change_1w: -0.28
- over_800_change_1w: -0.21
- over_1000_change_1w: -0.24
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,68.01,,57.62,,52.58,,0,False,False
20260508,69.02,1.01,57.62,0,52.58,0,1,False,False
20260515,69.27,0.25,58.44,0.82,52.5,-0.08,2,False,True
20260522,69.5,0.23,58.65,0.21,53.61,1.11,3,True,True
20260529,69.58,0.08,58.76,0.11,53.72,0.11,4,True,True
20260605,69.65,0.07,58.76,0,53.72,0,5,False,False
20260612,69.74,0.09,58.88,0.12,53.84,0.12,6,True,True
20260618,69.46,-0.28,58.67,-0.21,53.6,-0.24,0,False,False
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
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6923 | 中台 | 5 | 0 | 0.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
