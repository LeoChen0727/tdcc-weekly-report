# INDIVIDUAL STOCK CHATGPT PACKET - 5880 合庫金

## Metadata
- generated_at: 2026-09-20 22:17:36 Asia/Taipei
- stock_id: 5880
- stock_name: 合庫金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5880_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5880_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5880_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5880_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5880.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5880.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5880.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5880.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5880_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5880_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5880_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260918
- open: 27.5
- high: 27.5
- low: 27.05
- close: 27.3
- volume: 30844955
- ma5: 27.33
- ema23_primary: 26.48
- distance_to_ema23_pct: 3.1
- ma20: 26.35
- ma60: 25.7
- ma120: 24.57
- return_5d: 0.37
- return_20d: 8.98
- volume_ratio: 1.51
- distance_to_ma20_pct_auxiliary: 3.6
- distance_to_high_60_pct: -1.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,25.1,25.2,24.85,25,7888175,25.21,-0.82,25.56,24.91,0.28
20260825,25,25.25,24.95,25.05,12487194,25.19,-0.57,25.51,24.95,0.44
20260826,25,25.1,24.85,25,8363717,25.18,-0.7,25.46,24.99,0.32
20260827,25,25.3,24.95,25.05,10831100,25.17,-0.46,25.36,25.02,0.46
20260828,25.1,25.3,25.05,25.25,9386451,25.17,0.3,25.24,25.05,0.44
20260831,25.25,25.65,25.05,25.55,45412466,25.2,1.37,25.18,25.08,2.04
20260901,25.35,25.7,25.3,25.6,15139049,25.24,1.44,25.13,25.12,0.71
20260902,25.6,26.3,25.5,26.3,36416956,25.33,3.85,25.11,25.17,1.63
20260903,26.3,26.85,26.25,26.7,32491451,25.44,4.95,25.14,25.22,1.44
20260904,26.7,26.7,26.3,26.65,21410399,25.54,4.34,25.16,25.27,0.94
20260907,26.75,26.75,26.3,26.5,15517404,25.62,3.43,25.18,25.31,0.7
20260908,26.45,26.85,26.2,26.85,20999269,25.72,4.38,25.33,25.36,1.02
20260909,26.7,26.85,26.45,26.85,15145888,25.82,4,25.46,25.4,0.74
20260910,26.6,26.85,26.55,26.85,12158726,25.9,3.65,25.6,25.44,0.61
20260911,26.55,27.2,26.55,27.2,28731550,26.01,4.57,25.75,25.48,1.38
20260914,26.95,27.45,26.85,27.45,22723824,26.13,5.05,25.88,25.53,1.13
20260915,27.55,27.55,26.8,27,23217099,26.2,3.04,25.98,25.57,1.16
20260916,27.1,27.35,26.75,27.35,19851298,26.3,3.99,26.1,25.61,1.03
20260917,27.25,27.6,27.1,27.55,20508852,26.4,4.34,26.24,25.67,1.05
20260918,27.5,27.5,27.05,27.3,30844955,26.48,3.1,26.35,25.7,1.51
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 75.36
- over_600_ratio: 73.35
- over_800_ratio: 72.17
- over_1000_ratio: 71.46
- over_400_change_1w: 0.19
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.22
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,73.6,0.03,70.4,0.01,69.58,0.01,5,True,True
20260709,73.75,0.15,70.55,0.15,69.74,0.16,6,True,True
20260717,73.91,0.16,70.7,0.15,69.91,0.17,7,True,True
20260724,74.12,0.21,70.96,0.26,70.15,0.24,8,True,True
20260731,74.62,0.5,71.51,0.55,70.7,0.55,9,True,True
20260807,74.7,0.08,71.62,0.11,70.8,0.1,10,True,True
20260814,74.48,-0.22,71.36,-0.26,70.57,-0.23,0,False,False
20260821,74.59,0.11,71.47,0.11,70.69,0.12,1,True,True
20260828,74.65,0.06,71.53,0.06,70.76,0.07,2,True,True
20260904,74.91,0.26,71.82,0.29,71.06,0.3,3,True,True
20260911,75.17,0.26,71.97,0.15,71.24,0.18,4,True,True
20260918,75.36,0.19,72.17,0.2,71.46,0.22,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5880 | 合庫金 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管(如:執行長、營運長、 行銷長及策略長等)、財務主管、會計主管、公司治理主管、資訊安全長、研發主管、 內部稽核主管或訴訟及非訟代理人）:法遵主管 2.發生變動日期:115/09/17 3.舊任者姓名、級職及簡歷:無 4.新任者姓名、級職及簡歷:朱清松/稽核部總稽核 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、「退休」、「死亡」、「新 任」或「解任」）:新任 6.異動原因:新任 7.生效日期:115/09/18 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 5880 | 合庫金 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管(如:執行長、營運長、 行銷長及策略長等)、財務主管、會計主管、公司治理主管、資訊安全長、研發主管、 內部稽核主管或訴訟及非訟代理人）:法遵主管 2.發生變動日期:115/09/17 3.舊任者姓名、級職及簡歷:無 4.新任者姓名、級職及簡歷:朱清松/稽核部總稽核 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、「退休」、「死亡」、「新 任」或「解任」）:新任 6.異動原因:新任 7.生效日期:115/09/18 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5880 | 合庫金 | 19 | 3 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
