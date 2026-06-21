# INDIVIDUAL STOCK CHATGPT PACKET - 8121 越峰

## Metadata
- generated_at: 2026-06-21 22:24:44 Asia/Taipei
- stock_id: 8121
- stock_name: 越峰
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 152
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8121_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8121_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8121_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8121_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8121_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8121_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8121_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8121.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8121.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8121.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8121.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8121_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8121_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8121_latest.md?ref=main

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
- open: 51.9
- high: 54.6
- low: 48.7
- close: 53.4
- volume: 5924000
- ma5: 49.31
- ema23_primary: 42.43
- distance_to_ema23_pct: 25.85
- ma20: 42.95
- ma60: 33.24
- ma120: 30.58
- return_5d: 22.76
- return_20d: 42.97
- volume_ratio: 2.68
- distance_to_ma20_pct_auxiliary: 24.34
- distance_to_high_60_pct: -2.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,37.55,41,37.55,39.55,39000,32.35,22.27,32.2,27.71,0.02
20260525,40.3,43.5,37.6,43.5,41000,33.28,30.73,33.06,27.98,0.02
20260526,43.5,43.5,39.2,41.5,41000,33.96,22.2,33.78,28.21,0.02
20260527,40.8,43.2,40.2,41,41000,34.55,18.68,34.48,28.42,0.02
20260528,41.2,42.3,39.7,40,41000,35,14.28,35.11,28.63,0.02
20260529,41,41.6,40,40.45,41000,35.46,14.09,35.7,28.85,0.02
20260601,40.45,40.55,39.4,39.6,40000,35.8,10.61,36.12,29.1,0.02
20260602,40.2,40.2,37.5,38.75,38,36.05,7.5,36.41,29.32,0
20260603,38.9,40.3,38.55,39,39000,36.29,7.46,36.82,29.54,0.03
20260604,39,40.8,38.75,40.5,40000,36.64,10.52,37.2,29.81,0.03
20260605,40.7,41.8,38.4,40.75,40000,36.99,10.18,37.7,30.09,0.03
20260608,36.7,38,36.7,38,1980000,37.07,2.51,37.91,30.31,1.54
20260609,38,41.8,37.15,41.8,3586000,37.46,11.57,38.3,30.6,2.8
20260610,43.9,45.95,42.8,44.5,9095000,38.05,16.95,38.83,30.94,5.55
20260611,45.1,45.2,40.6,43.5,4939000,38.5,12.97,39.23,31.25,2.9
20260612,44.15,46.2,43.05,44.4,2895000,39,13.86,39.75,31.56,1.72
20260615,45.85,48.8,45.5,48.8,6864000,39.81,22.57,40.51,31.95,3.48
20260616,48.8,52,47.15,50.3,5939000,40.69,23.63,41.42,32.36,2.68
20260617,48.5,51,48.3,49.65,2539000,41.43,19.83,42.15,32.77,1.18
20260618,51.9,54.6,48.7,53.4,5924000,42.43,25.85,42.95,33.24,2.68
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 62.96
- over_600_ratio: 60
- over_800_ratio: 58.04
- over_1000_ratio: 55.97
- over_400_change_1w: 1.05
- over_800_change_1w: 0.14
- over_1000_change_1w: -0.34
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.37,,55.03,,53.05,,0,False,False
20260508,59.64,0.27,55.03,0,53.05,0,1,False,False
20260515,60.87,1.23,55.45,0.42,53.08,0.03,2,True,True
20260522,60.91,0.04,55.81,0.36,54.22,1.14,3,True,True
20260529,61.05,0.14,56.77,0.96,54.31,0.09,4,True,True
20260605,61.33,0.28,57.16,0.39,55.17,0.86,5,True,True
20260612,61.91,0.58,57.9,0.74,56.31,1.14,6,True,True
20260618,62.96,1.05,58.04,0.14,55.97,-0.34,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8121 | 越峰 | true_breakout | 嚴格突破 | 89.0 |  |  | platform_breakout |  |  | first_seen | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8121 | 越峰 | 1 | 1 | 1 | 1 | 2 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
