# INDIVIDUAL STOCK CHATGPT PACKET - 3360 尚立

## Metadata
- generated_at: 2026-07-19 22:27:13 Asia/Taipei
- stock_id: 3360
- stock_name: 尚立
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3360_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3360_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3360_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3360_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3360_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3360_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3360_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3360.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3360.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3360.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3360.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3360_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3360_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3360_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260717
- open: 20.35
- high: 21
- low: 19.15
- close: 19.55
- volume: 4692000
- ma5: 20.95
- ema23_primary: 19.43
- distance_to_ema23_pct: 0.63
- ma20: 20.09
- ma60: 16.34
- ma120: 15.72
- return_5d: -2.74
- return_20d: 17.77
- volume_ratio: 0.68
- distance_to_ma20_pct_auxiliary: -2.7
- distance_to_high_60_pct: -18.03

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,16.4,16.85,16,16.25,2522000,14.93,8.81,14.78,14.47,3.12
20260622,16.35,17.55,15.8,17.25,3356000,15.13,14.04,14.89,14.51,3.44
20260623,16.95,18.35,16.7,17.95,6700000,15.36,16.85,15.06,14.55,5.12
20260624,18.85,19.7,18.8,19.7,5402000,15.72,25.29,15.32,14.62,3.42
20260625,21.65,21.65,19.3,20.9,19335000,16.16,29.37,15.66,14.72,7.6
20260626,20,20.2,19.1,19.1,5924000,16.4,16.46,15.91,14.8,2.09
20260629,19.2,21,19.2,20.65,9414000,16.75,23.25,16.23,14.91,2.84
20260630,21,22.7,20.7,22.7,14577000,17.25,31.59,16.66,15.05,3.61
20260701,23.05,23.85,21,21.25,11151000,17.58,20.85,17,15.17,2.43
20260702,20.9,22.4,20.9,21.85,4492000,17.94,21.8,17.35,15.3,0.93
20260703,21.6,21.9,20.3,20.4,3676000,18.14,12.43,17.63,15.39,0.73
20260706,20.65,21.2,20.35,20.6,2420000,18.35,12.27,17.93,15.5,0.47
20260707,20.65,20.8,19,19.15,3069000,18.42,3.99,18.18,15.59,0.58
20260708,19.2,19.5,18.45,19.25,1748000,18.48,4.14,18.43,15.67,0.33
20260709,19.25,20.8,18.8,20.1,2674000,18.62,7.95,18.7,15.77,0.49
20260713,20.8,22.1,19.7,20.15,10779000,18.75,7.48,18.97,15.87,1.83
20260714,20.3,21.85,19.8,21.45,5404000,18.97,13.06,19.29,15.99,0.88
20260715,20.95,23.45,20.7,22.85,9874000,19.3,18.42,19.67,16.14,1.5
20260716,23.05,23.5,20.6,20.75,11570000,19.42,6.87,19.95,16.25,1.63
20260717,20.35,21,19.15,19.55,4692000,19.43,0.63,20.09,16.34,0.68
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 23.95
- over_600_ratio: 20.69
- over_800_ratio: 18.06
- over_1000_ratio: 16.99
- over_400_change_1w: -1.94
- over_800_change_1w: -0.83
- over_1000_change_1w: -0.77
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.97,,21.23,,17.76,,0,False,False
20260508,27.81,-0.16,21.23,0,17.76,0,0,False,False
20260515,26.95,-0.86,21.14,-0.09,17.76,0,0,False,False
20260522,26.99,0.04,21.15,0.01,17.76,0,1,False,True
20260529,27.04,0.05,20.09,-1.06,17.76,0,2,False,False
20260605,26.8,-0.24,21.14,1.05,17.76,0,3,False,True
20260612,26.19,-0.61,20.09,-1.05,17.76,0,0,False,False
20260618,29.43,3.24,20.09,0,17.76,0,1,False,False
20260626,25.96,-3.47,17.76,-2.33,17.76,0,0,False,False
20260703,27.07,1.11,20.24,2.48,19.13,1.37,1,True,True
20260709,25.89,-1.18,18.89,-1.35,17.76,-1.37,0,False,False
20260717,23.95,-1.94,18.06,-0.83,16.99,-0.77,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3360 | 尚立 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 3360 | 尚立 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  |  | stale_signal | calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3360 | 尚立 | 8 | 2 | 5 | 8 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
