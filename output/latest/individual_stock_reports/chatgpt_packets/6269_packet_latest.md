# INDIVIDUAL STOCK CHATGPT PACKET - 6269 台郡

## Metadata
- generated_at: 2026-06-21 22:24:10 Asia/Taipei
- stock_id: 6269
- stock_name: 台郡
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6269_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6269_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6269_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6269_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6269_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6269_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6269_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6269.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6269.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6269.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6269.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6269_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6269_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6269_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: high_level_distribution_risk
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- date: 20260618
- open: 80
- high: 81.8
- low: 77
- close: 79.6
- volume: 18354410
- ma5: 75.74
- ema23_primary: 69.46
- distance_to_ema23_pct: 14.6
- ma20: 69.28
- ma60: 64.69
- ma120: 61.75
- return_5d: 20.97
- return_20d: 35.6
- volume_ratio: 1.6
- distance_to_ma20_pct_auxiliary: 14.9
- distance_to_high_60_pct: -2.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,58.8,62.9,58.8,62.4,4292319,60.94,2.4,61.94,61.23,1.04
20260525,63.2,66.4,63.1,64.7,4827940,61.25,5.63,61.87,61.21,1.15
20260526,64.9,64.9,63.1,64.2,3010657,61.5,4.39,61.8,61.19,0.72
20260527,64.3,65,62.2,62.8,3455027,61.61,1.94,61.72,61.16,0.82
20260528,63,64,60.5,60.8,3752094,61.54,-1.2,61.58,61.13,0.88
20260529,62.3,63,61.7,62.9,2807130,61.65,2.02,61.43,61.16,0.66
20260601,69.1,69.1,69.1,69.1,3699567,62.27,10.96,61.49,61.38,0.91
20260602,76,76,70.5,74.9,42564190,63.33,18.28,61.81,61.67,7.08
20260603,75.2,80,72.2,77.5,24865302,64.51,20.14,62.28,61.97,3.56
20260604,76.4,76.8,71.4,71.5,13826623,65.09,9.85,62.53,62.23,1.85
20260605,70.4,70.7,66.9,68.1,8750621,65.34,4.22,62.78,62.46,1.14
20260608,61.3,65.2,61.3,64.5,9343237,65.27,-1.18,63.1,62.64,1.22
20260609,64.9,70.3,63.1,69.4,8655752,65.61,5.77,63.7,62.89,1.1
20260610,67.4,74.5,67.4,68.3,11947552,65.84,3.74,64.31,63.11,1.45
20260611,69,70.5,64.9,65.8,7467368,65.83,-0.05,64.65,63.28,0.89
20260612,68,72.3,67.7,72.3,8194271,66.37,8.93,65.42,63.54,0.95
20260615,71.5,75.7,71.1,73.6,14693655,66.98,9.89,66.3,63.81,1.6
20260616,74.2,79.5,72.4,73.3,12846757,67.5,8.59,67.14,64.08,1.32
20260617,72.5,80.6,72.3,79.9,21371868,68.54,16.58,68.23,64.41,2.01
20260618,80,81.8,77,79.6,18354410,69.46,14.6,69.28,64.69,1.6
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 37.4
- over_600_ratio: 34.5
- over_800_ratio: 31.77
- over_1000_ratio: 30.13
- over_400_change_1w: 4.08
- over_800_change_1w: 3.72
- over_1000_change_1w: 3.42
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,35.38,,30.14,,29.32,,0,False,False
20260508,35.05,-0.33,30.19,0.05,29.08,-0.24,1,False,True
20260515,32.57,-2.48,27.23,-2.96,26.68,-2.4,0,False,False
20260522,32.22,-0.35,26.92,-0.31,25.82,-0.86,1,False,False
20260529,32.85,0.63,28.23,1.31,27.11,1.29,2,True,True
20260605,33.97,1.12,28.27,0.04,27.18,0.07,3,True,True
20260612,33.32,-0.65,28.05,-0.22,26.71,-0.47,0,False,False
20260618,37.4,4.08,31.77,3.72,30.13,3.42,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6269 | 台郡 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | stale_signal | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6269 | 台郡 | 2 | 2 | 3 | 8 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 6269 | 台郡 | 40 | 0 | 13349930.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
