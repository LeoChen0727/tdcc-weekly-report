# INDIVIDUAL STOCK CHATGPT PACKET - 3652 精聯

## Metadata
- generated_at: 2026-06-21 22:23:33 Asia/Taipei
- stock_id: 3652
- stock_name: 精聯
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
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_initial
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
- model_recommended
- decision_score_high
- price_structure_not_broken
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
- open: 38.25
- high: 40.95
- low: 38.1
- close: 40.2
- volume: 2847772
- ma5: 37.22
- ema23_primary: 34.22
- distance_to_ema23_pct: 17.48
- ma20: 34.48
- ma60: 30.69
- ma120: 29.47
- return_5d: 24.27
- return_20d: 32.89
- volume_ratio: 5.1
- distance_to_ma20_pct_auxiliary: 16.6
- distance_to_high_60_pct: -1.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,30,31.8,30,31.35,155752,29.79,5.23,30.37,28.41,0.65
20260525,31.7,32.7,31.7,31.95,299361,29.97,6.6,30.5,28.47,1.19
20260526,34.45,34.45,32.5,32.8,444509,30.21,8.58,30.52,28.54,1.92
20260527,33.15,33.65,32.55,32.8,393246,30.42,7.81,30.57,28.62,2.28
20260528,33.65,35.4,33.65,33.95,947658,30.72,10.52,30.66,28.71,4.65
20260529,34.8,36.85,34.5,35.1,600426,31.08,12.92,30.89,28.84,2.73
20260601,35.4,36.45,34.8,36.4,460504,31.53,15.46,31.2,28.99,1.96
20260602,36.5,36.5,34.9,35.5,317778,31.86,11.44,31.46,29.14,1.29
20260603,35.8,36.1,34.9,34.95,326837,32.11,8.83,31.72,29.27,1.28
20260604,34.95,34.95,34.25,34.35,228886,32.3,6.34,31.94,29.41,0.87
20260605,34.4,34.4,33.4,33.95,225734,32.44,4.66,32.16,29.53,0.85
20260608,30.65,32.3,30.65,31.85,288454,32.39,-1.67,32.21,29.6,1.09
20260609,32.5,33.7,32.3,33.5,202553,32.48,3.13,32.35,29.7,0.75
20260610,33.05,34.1,32.5,32.65,188369,32.5,0.47,32.48,29.79,0.68
20260611,32.7,32.8,31.5,32.35,148710,32.48,-0.41,32.59,29.88,0.53
20260612,32.95,35.55,32.95,35.55,493181,32.74,8.58,32.88,30.01,1.64
20260615,36,36.65,35.25,36.2,968350,33.03,9.6,33.21,30.14,2.81
20260616,36.25,38.5,36.25,36.9,776663,33.35,10.64,33.58,30.3,2.03
20260617,37.9,39.75,37,37.25,844769,33.68,10.61,33.98,30.47,2
20260618,38.25,40.95,38.1,40.2,2847772,34.22,17.48,34.48,30.69,5.1
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 71.57
- over_600_ratio: 69.81
- over_800_ratio: 68.91
- over_1000_ratio: 67.58
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
20260430,71.57,,68.91,,67.58,,0,False,False
20260508,71.57,0,68.91,0,67.58,0,0,False,False
20260515,71.57,0,68.91,0,67.58,0,0,False,False
20260522,71.57,0,68.91,0,67.58,0,0,False,False
20260529,71.58,0.01,68.92,0.01,67.59,0.01,1,True,True
20260605,71.58,0,68.92,0,67.59,0,0,False,False
20260612,71.57,-0.01,68.91,-0.01,67.58,-0.01,0,False,False
20260618,71.57,0,68.91,0,67.58,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3652 | 精聯 | true_breakout | 嚴格突破 | 92.0 |  |  | platform_breakout |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3652 | 精聯 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
