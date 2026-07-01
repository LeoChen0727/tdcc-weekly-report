# INDIVIDUAL STOCK CHATGPT PACKET - 6684 安格

## Metadata
- generated_at: 2026-07-01 22:28:34 Asia/Taipei
- stock_id: 6684
- stock_name: 安格
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 160
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6684_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6684_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6684_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6684_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6684_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6684_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6684_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6684.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6684.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6684.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6684.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6684_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6684_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6684_latest.md?ref=main

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
- date: 20260701
- open: 59.6
- high: 64.5
- low: 58.5
- close: 64.5
- volume: 2629000
- ma5: 61.68
- ema23_primary: 54.61
- distance_to_ema23_pct: 18.1
- ma20: 53.57
- ma60: 48.76
- ma120: 48.05
- return_5d: 0.78
- return_20d: 43.65
- volume_ratio: 1.75
- distance_to_ma20_pct_auxiliary: 20.4
- distance_to_high_60_pct: -3.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,45.2,45.7,44.85,45.2,45000,45.95,-1.64,46.23,45.7,0.29
20260604,45.05,45.1,44.35,44.5,45000,45.83,-2.91,45.9,45.73,0.35
20260605,44.5,48.95,44.5,48.95,48000,46.09,6.2,45.92,45.82,0.44
20260608,45.15,48.15,44.35,47.3,881000,46.19,2.4,45.87,45.85,6.11
20260609,48,49.5,47.7,48.8,689000,46.41,5.15,45.96,45.91,4.3
20260610,48.5,52.3,48.5,49.4,960000,46.66,5.88,46.13,45.97,4.82
20260611,49.4,51.3,47.5,49.4,497000,46.89,5.36,46.3,46.04,2.27
20260612,49.9,51.3,49.7,49.7,287000,47.12,5.47,46.53,46.1,1.3
20260615,50.8,51,49.8,50.6,290000,47.41,6.73,46.84,46.16,1.26
20260616,50.8,50.8,48.5,48.55,203000,47.51,2.2,47.05,46.21,0.9
20260617,48.5,50.2,47.65,50.1,256000,47.72,4.98,47.28,46.28,1.11
20260618,51,52,50.2,50.5,363000,47.95,5.31,47.49,46.38,1.49
20260622,51.3,55.5,51.3,55.5,1335000,48.58,14.24,47.88,46.57,4.32
20260623,61,61,59,60.5,5332000,49.58,22.04,48.49,46.84,9.31
20260624,60.4,66.5,57.8,64,4817000,50.78,26.04,49.33,47.17,5.94
20260625,63.7,64.5,60.2,63.9,2993000,51.87,23.19,50.23,47.5,3.12
20260626,64.4,66.5,62,62.5,5702000,52.76,18.47,51.15,47.83,4.59
20260629,62.8,63.6,58.3,58.8,1834000,53.26,10.4,51.87,48.13,1.38
20260630,59,61.6,58,58.7,839000,53.71,9.28,52.59,48.39,0.61
20260701,59.6,64.5,58.5,64.5,2629000,54.61,18.1,53.57,48.76,1.75
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 34.15
- over_600_ratio: 33.09
- over_800_ratio: 31.51
- over_1000_ratio: 31.51
- over_400_change_1w: -0.34
- over_800_change_1w: -1.92
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.64,,33.58,,31.51,,0,False,False
20260508,34.67,0.03,33.61,0.03,31.51,0,1,False,True
20260515,34.51,-0.16,33.45,-0.16,31.51,0,0,False,False
20260522,34.52,0.01,33.46,0.01,31.51,0,1,False,True
20260529,34.47,-0.05,33.41,-0.05,31.51,0,0,False,False
20260605,34.24,-0.23,31.51,-1.9,31.51,0,0,False,False
20260612,34.37,0.13,33.31,1.8,31.51,0,1,False,True
20260618,34.49,0.12,33.43,0.12,31.51,0,2,False,True
20260626,34.15,-0.34,31.51,-1.92,31.51,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6684 | 安格 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6684 | 安格 | 1 | 1 | 3 | 5 | 5 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
