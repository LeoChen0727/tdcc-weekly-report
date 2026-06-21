# INDIVIDUAL STOCK CHATGPT PACKET - 1227 佳格

## Metadata
- generated_at: 2026-06-21 22:22:30 Asia/Taipei
- stock_id: 1227
- stock_name: 佳格
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1227_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1227_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1227_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1227_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1227_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1227_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1227_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1227.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1227.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1227.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1227.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1227_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1227_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1227_latest.md?ref=main

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
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 28.8
- high: 29.25
- low: 28.8
- close: 29.1
- volume: 2304172
- ma5: 28.97
- ema23_primary: 28.69
- distance_to_ema23_pct: 1.43
- ma20: 28.48
- ma60: 29.2
- ma120: 29.47
- return_5d: 0.87
- return_20d: 1.75
- volume_ratio: 0.91
- distance_to_ma20_pct_auxiliary: 2.19
- distance_to_high_60_pct: -6.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,28.5,28.55,28.35,28.45,634178,28.91,-1.6,28.79,29.63,0.69
20260525,28.4,28.4,28.05,28.1,1416096,28.85,-2.59,28.73,29.6,1.51
20260526,28.1,28.45,28.05,28.25,927467,28.8,-1.9,28.69,29.57,1
20260527,28.25,28.25,28,28.1,1730442,28.74,-2.22,28.63,29.53,1.74
20260528,28.1,28.1,27.9,27.9,1345180,28.67,-2.68,28.57,29.5,1.29
20260529,28,28.25,27.85,27.95,1491814,28.61,-2.3,28.52,29.47,1.42
20260601,27.95,28.3,27.85,28.2,2466740,28.57,-1.31,28.48,29.45,2.2
20260602,28.2,28.3,27.95,27.95,5123836,28.52,-2.01,28.44,29.43,3.85
20260603,28.35,28.5,28.1,28.4,5841275,28.51,-0.39,28.42,29.41,3.71
20260604,28.5,29,28.45,28.45,5792856,28.51,-0.2,28.4,29.39,3.19
20260605,28.7,28.9,28.55,28.85,2950700,28.54,1.1,28.39,29.38,1.52
20260608,28.4,28.6,28.1,28.3,3878594,28.52,-0.76,28.36,29.36,1.86
20260609,28.25,28.8,28.25,28.6,1376142,28.52,0.27,28.35,29.35,0.66
20260610,28.6,28.8,28.35,28.35,5228219,28.51,-0.56,28.33,29.33,2.28
20260611,28.5,29.1,28.45,28.85,2727374,28.54,1.1,28.34,29.3,1.15
20260612,29.2,29.45,29,29.1,1923673,28.58,1.81,28.38,29.28,0.8
20260615,29.3,29.3,28.8,28.95,1600710,28.61,1.17,28.41,29.26,0.65
20260616,28.95,28.95,28.7,28.85,925865,28.63,0.75,28.43,29.24,0.37
20260617,28.75,28.85,28.55,28.85,997128,28.65,0.69,28.45,29.21,0.4
20260618,28.8,29.25,28.8,29.1,2304172,28.69,1.43,28.48,29.2,0.91
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 66.86
- over_600_ratio: 65.46
- over_800_ratio: 64.72
- over_1000_ratio: 63.95
- over_400_change_1w: -0.05
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.22
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.6,,65.59,,64.9,,0,False,False
20260508,67.48,-0.12,65.49,-0.1,64.81,-0.09,0,False,False
20260515,67.5,0.02,65.45,-0.04,64.77,-0.04,1,False,False
20260522,67.45,-0.05,65.37,-0.08,64.59,-0.18,0,False,False
20260529,67.38,-0.07,65.22,-0.15,64.54,-0.05,0,False,False
20260605,67.04,-0.34,64.96,-0.26,64.28,-0.26,0,False,False
20260612,66.91,-0.13,64.76,-0.2,64.17,-0.11,0,False,False
20260618,66.86,-0.05,64.72,-0.04,63.95,-0.22,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1227 | 佳格 | pattern | 型態觀察 | 54.0 |  |  | base_building |  |  | stale_signal | 1.股東常會日期:115/06/17 2.重要決議事項一、盈餘分配或盈虧撥補: 通過承認114年度盈餘分派案 3.重要決議事項二、章程修訂: 通過修訂本公司章程案 4.重要決議事項三、營業報告書及財務報表: 通過承認114年度營業報告書及財務報表案 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:無 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1227 | 佳格 | 1 | 1 | 3 | 6 | 6 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
