# INDIVIDUAL STOCK CHATGPT PACKET - 7780 大研生醫*

## Metadata
- generated_at: 2026-06-12 22:24:37 Asia/Taipei
- stock_id: 7780
- stock_name: 大研生醫*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260612
- price_rows: 168
- latest_tdcc_date: 20260605
- tdcc_rows: 6
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/7780_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/7780_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7780_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7780_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7780_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7780_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/7780_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/7780_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7780_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7780_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/7780_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/7780_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7780.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7780.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7780.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7780.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7780_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7780_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7780_latest.md?ref=main

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
- action_rating_display_zh: 減碼
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 型態觀察 已出現風險管理訊號，操作評級為「減碼」。
- entry_strategy_zh: 目前風險升高，以降低部位為主，不建議新買。
- position_sizing_zh: 降低部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 歷史不足、TDCC 轉弱警訊、量價失敗
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 已出現風險管理訊號，操作評級為「減碼」。 進場策略：目前風險升高，以降低部位為主，不建議新買。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足、TDCC 轉弱警訊、量價失敗

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: reduce
- action_rating_label_zh: 減碼
- confidence_level: low
- thesis_state: failed_breakout
- entry_style: no_entry_now
- position_sizing: reduce_position

### management_plan
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- near_23ema_or_support
- revenue_not_deteriorating
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
- insufficient_tdcc_history
- tdcc_distribution_warning
- volume_price_failure

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260612
- open: 18.45
- high: 18.95
- low: 18.35
- close: 18.8
- volume: 3035293
- ma5: 18.14
- ema23_primary: 18.32
- distance_to_ema23_pct: 2.64
- ma20: 18.07
- ma60: 19.12
- ma120: 58.42
- return_5d: 7.12
- return_20d: 4.16
- volume_ratio: 1.47
- distance_to_ma20_pct_auxiliary: 4.07
- distance_to_high_60_pct: -19.66

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260513,18.05,18.45,17.9,18.35,2140073,19.47,-5.76,19.14,20.85,0.89
20260514,18.35,18.4,18,18,1716426,19.35,-6.98,19,20.71,0.72
20260515,18,18,17.8,17.9,2042104,19.23,-6.91,18.86,20.55,0.85
20260518,18.1,18.3,17.8,18.25,1994139,19.15,-4.69,18.76,20.41,0.85
20260519,18.25,18.55,18.15,18.45,1821683,19.09,-3.35,18.68,20.28,0.83
20260520,18.5,18.6,18.3,18.5,1227672,19.04,-2.84,18.61,20.18,0.58
20260521,18.5,18.65,18.4,18.5,1053097,19,-2.61,18.54,20.09,0.51
20260522,18.5,18.55,18.1,18.5,1959926,18.95,-2.4,18.5,19.99,0.99
20260525,18.5,18.55,18.05,18.15,2684953,18.89,-3.9,18.46,19.87,1.37
20260526,18.05,18.05,17.7,17.9,2760349,18.8,-4.81,18.42,19.75,1.39
20260527,17.9,18.05,17.65,17.75,1859753,18.72,-5.17,18.37,19.64,0.94
20260528,17.75,17.75,17.5,17.6,2705503,18.62,-5.5,18.32,19.53,1.32
20260529,17.6,17.65,17.45,17.6,1948799,18.54,-5.06,18.27,19.45,0.94
20260601,17.65,17.9,17.55,17.6,1891580,18.46,-4.66,18.23,19.38,0.9
20260602,17.6,17.7,17.5,17.55,1866974,18.38,-4.54,18.16,19.31,0.89
20260603,17.5,17.9,17.5,17.8,2465125,18.34,-2.92,18.12,19.23,1.16
20260604,17.6,17.7,17.5,17.55,1866974,18.27,-3.94,18.06,19.19,0.89
20260605,18.05,18.5,18,18.15,2507007,18.26,-0.6,18.03,19.16,1.19
20260611,18.55,18.55,18.05,18.4,1684297,18.27,0.7,18.03,19.13,0.81
20260612,18.45,18.95,18.35,18.8,3035293,18.32,2.64,18.07,19.12,1.47
```

## Latest TDCC Snapshot
- as_of_date: 20260605
- over_400_ratio: 75.38
- over_600_ratio: 74.31
- over_800_ratio: 74.15
- over_1000_ratio: 73.57
- over_400_change_1w: 0.07
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,75.19,,73.93,,73.04,,0,False,False
20260508,75.17,-0.02,73.73,-0.2,73.04,0,1,False,False
20260515,74.84,-0.33,73.6,-0.13,73.02,-0.02,0,False,False
20260522,75.12,0.28,74,0.4,73.42,0.4,1,True,True
20260529,75.31,0.19,74.15,0.15,73.57,0.15,2,True,True
20260605,75.38,0.07,74.15,0,73.57,0,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260612 | 7780 | 大研生醫* | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | stale_signal | calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_14d |
| 20260612 | 7780 | 大研生醫* | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  | no_signal | stale_signal | calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_14d |
| 20260612 | 7780 | 大研生醫* | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | no_signal | stale_signal | calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260612 | 7780 | 大研生醫* | 4 | 4 | 4 | 9 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260612 | 7780 | 大研生醫* | 6 | 0 | 18630.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
