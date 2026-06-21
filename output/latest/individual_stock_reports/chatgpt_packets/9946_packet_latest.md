# INDIVIDUAL STOCK CHATGPT PACKET - 9946 三發地產

## Metadata
- generated_at: 2026-06-21 22:24:54 Asia/Taipei
- stock_id: 9946
- stock_name: 三發地產
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/9946_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/9946_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9946_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9946_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9946_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9946_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9946_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9946.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9946.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9946.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9946.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9946_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9946_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9946_latest.md?ref=main

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
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
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
- no_major_tdcc_warning
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 20.7
- high: 21.85
- low: 20.4
- close: 20.6
- volume: 3024717
- ma5: 19.66
- ema23_primary: 17.89
- distance_to_ema23_pct: 15.16
- ma20: 17.52
- ma60: 17.04
- ma120: 17.45
- return_5d: 15.73
- return_20d: 22.62
- volume_ratio: 2.26
- distance_to_ma20_pct_auxiliary: 17.6
- distance_to_high_60_pct: -5.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,16.8,16.85,16.7,16.8,485554,16.62,1.05,16.35,17.02,0.81
20260525,16.8,16.9,16.4,16.4,718925,16.61,-1.24,16.36,17.01,1.16
20260526,16.4,16.45,16.2,16.35,307518,16.58,-1.42,16.37,17.01,0.51
20260527,16.35,16.35,16.1,16.2,500512,16.55,-2.13,16.38,17,0.82
20260528,16.2,16.45,16.15,16.35,313533,16.54,-1.12,16.39,16.99,0.51
20260529,16.3,16.45,16.25,16.45,303429,16.53,-0.48,16.42,16.99,0.5
20260601,16.45,16.55,16.2,16.55,555667,16.53,0.12,16.47,16.99,0.91
20260602,16.55,16.55,16.35,16.55,326585,16.53,0.11,16.51,16.98,0.54
20260603,16.55,16.9,16.45,16.9,584000,16.56,2.04,16.57,16.97,0.95
20260604,16.9,17.05,16.85,16.95,790328,16.59,2.14,16.63,16.98,1.26
20260605,17.1,17.25,16.95,17.15,1646474,16.64,3.06,16.68,16.98,2.4
20260608,16.8,16.95,16.4,16.85,1092324,16.66,1.15,16.69,16.96,1.54
20260609,16.85,17.1,16.75,16.95,846673,16.68,1.6,16.7,16.95,1.18
20260610,16.75,17.85,16.75,17.8,2743093,16.78,6.1,16.76,16.95,3.53
20260611,18.1,18.1,17.5,17.8,1485233,16.86,5.57,16.8,16.93,1.89
20260612,17.95,18.35,17.8,17.95,1602968,16.95,5.89,16.86,16.93,1.95
20260615,18.15,19.35,17.85,19.3,2936230,17.15,12.55,16.98,16.95,3.19
20260616,20.1,21,19.5,19.95,4544523,17.38,14.78,17.14,16.98,4.03
20260617,19.8,20.55,19.6,20.5,1978222,17.64,16.21,17.33,17.01,1.64
20260618,20.7,21.85,20.4,20.6,3024717,17.89,15.16,17.52,17.04,2.26
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 81.22
- over_600_ratio: 79.35
- over_800_ratio: 78.72
- over_1000_ratio: 77.32
- over_400_change_1w: 0.12
- over_800_change_1w: 0.6
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260402,81.12,0.08,77.84,0.29,76.69,0,7,False,True
20260410,81.15,0.03,77.83,-0.01,76.69,0,8,False,False
20260417,81.01,-0.14,77.83,0,76.69,0,0,False,False
20260424,81.08,0.07,77.56,-0.27,76.69,0,1,False,False
20260430,81.09,0.01,77.82,0.26,76.69,0,2,False,True
20260508,81.23,0.14,77.83,0.01,76.69,0,3,False,True
20260515,81.03,-0.2,77.95,0.12,76.82,0.13,4,False,True
20260522,81.12,0.09,78.11,0.16,76.98,0.16,5,False,True
20260529,81.19,0.07,78.2,0.09,77.07,0.09,6,True,True
20260605,81.06,-0.13,78.27,0.07,77.14,0.07,7,False,True
20260612,81.1,0.04,78.12,-0.15,77.25,0.11,8,False,True
20260618,81.22,0.12,78.72,0.6,77.32,0.07,9,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 9946 | 三發地產 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 9946 | 三發地產 | 7 | 2 | 5 | 7 | 7 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

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
