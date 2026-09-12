# INDIVIDUAL STOCK CHATGPT PACKET - 2883 凱基金

## Metadata
- generated_at: 2026-09-12 22:16:19 Asia/Taipei
- stock_id: 2883
- stock_name: 凱基金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2883.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2883.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2883.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2883.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2883_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2883_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2883_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 36.95
- high: 37.85
- low: 36.75
- close: 37.85
- volume: 44415166
- ma5: 37.21
- ema23_primary: 34.29
- distance_to_ema23_pct: 10.39
- ma20: 33.88
- ma60: 31.38
- ma120: 26.93
- return_5d: 3.13
- return_20d: 19.59
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: 11.73
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,31.5,31.65,30.9,31.4,52124434,30.57,2.71,30.64,28.72,1.14
20260818,31.1,31.35,30.85,30.95,50381336,30.6,1.14,30.7,28.87,1.09
20260819,30.7,30.85,30.3,30.4,41106180,30.59,-0.61,30.7,29.02,0.91
20260820,30.7,30.7,30.05,30.4,26497717,30.57,-0.56,30.68,29.16,0.6
20260821,30.4,31.55,30.3,31.55,49167372,30.65,2.93,30.72,29.32,1.09
20260824,31.75,31.95,30.7,31,36847710,30.68,1.04,30.73,29.47,0.81
20260825,31,31.7,30.9,31.7,37151287,30.77,3.04,30.84,29.62,0.83
20260826,31.65,33.1,31.6,32.25,65204736,30.89,4.41,31,29.78,1.45
20260827,32.75,33,32.15,32.15,35842285,30.99,3.73,31.16,29.93,0.8
20260828,32.5,32.8,32.15,32.75,20878621,31.14,5.17,31.25,30.04,0.51
20260831,32.7,33.85,32.55,33.85,104070641,31.37,7.92,31.42,30.15,2.4
20260901,33.9,35.1,33.9,34.95,63652325,31.67,10.37,31.64,30.27,1.42
20260902,34.85,35.6,34.6,35.5,47214212,31.98,10.99,31.84,30.42,1.08
20260903,35.65,36.75,35.6,35.9,60617343,32.31,11.11,32.1,30.53,1.36
20260904,36.4,36.7,35.95,36.7,42802542,32.68,12.31,32.4,30.68,0.94
20260907,37.1,37.45,36.3,36.95,51314316,33.03,11.86,32.69,30.83,1.11
20260908,36.9,37.6,36.75,37.3,34505752,33.39,11.72,33,30.99,0.73
20260909,37.05,37.25,36,36.75,52826646,33.67,9.15,33.28,31.12,1.09
20260910,36.45,37.4,36.45,37.2,41645435,33.96,9.53,33.56,31.25,0.86
20260911,36.95,37.85,36.75,37.85,44415166,34.29,10.39,33.88,31.38,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 69.14
- over_600_ratio: 67.44
- over_800_ratio: 66.34
- over_1000_ratio: 65.36
- over_400_change_1w: 0.1
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,67.59,-0.1,64.72,-0.14,63.78,-0.15,0,False,False
20260703,67.26,-0.33,64.28,-0.44,63.32,-0.46,0,False,False
20260709,67.7,0.44,64.75,0.47,63.82,0.5,1,True,True
20260717,67.79,0.09,64.81,0.06,63.84,0.02,2,True,True
20260724,68.07,0.28,65.15,0.34,64.18,0.34,3,True,True
20260731,68.08,0.01,65.17,0.02,64.22,0.04,4,True,True
20260807,68.41,0.33,65.51,0.34,64.57,0.35,5,True,True
20260814,68.55,0.14,65.64,0.13,64.68,0.11,6,True,True
20260821,68.55,0,65.64,0,64.66,-0.02,0,False,False
20260828,68.83,0.28,65.99,0.35,65.01,0.35,1,True,True
20260904,69.04,0.21,66.23,0.24,65.27,0.26,2,True,True
20260911,69.14,0.1,66.34,0.11,65.36,0.09,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2883 | 凱基金 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  | call_strong_inflow | continued_2_3d | 1.主管機關核准減資日期:115/09/07 2.辦理資本變更登記完成日期:115/09/07 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）:   (1)收回已發行限制員工權利新股註銷減資前：本公司實收資本額為新臺幣        185,569,894,140元，發行股數為18,556,989,414股。   (2)收回已發行限制員工權利新股註銷減資後：本公司實收資本額為新臺幣        185,567,548,490元，發行股數為18,556,754,849股（減資普通股234,565股）。   (3)收回已發行限制員工權利新股註銷對本公司每股淨值無影響。 4.預計換股作業計畫:不適用。 5.預計減資新股上市後之上市普通股股數:不適用。 6.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:不適用。 7.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，請說明股權流通性偏低   之因應措施:不適用。 8.其他應敘明事項:本公司於115年9月9日收到經濟部變更登記核准函，特此公告。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2883 | 凱基金 | 2 | 2 | 3 | 7 | 16 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2883 | 凱基金 | 31 | 0 | 7774890.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
