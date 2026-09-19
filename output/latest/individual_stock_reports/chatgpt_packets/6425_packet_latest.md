# INDIVIDUAL STOCK CHATGPT PACKET - 6425 易發

## Metadata
- generated_at: 2026-09-19 22:17:18 Asia/Taipei
- stock_id: 6425
- stock_name: 易發
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6425_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6425_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6425_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6425_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6425_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6425_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6425_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6425.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6425.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6425.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6425.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6425_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6425_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6425_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 63.7
- high: 68.5
- low: 63.7
- close: 68.2
- volume: 1711000
- ma5: 62.7
- ema23_primary: 62.46
- distance_to_ema23_pct: 9.18
- ma20: 63.06
- ma60: 61.91
- ma120: 71.99
- return_5d: 11.44
- return_20d: 18.4
- volume_ratio: 3
- distance_to_ma20_pct_auxiliary: 8.14
- distance_to_high_60_pct: -10.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,57.4,58.5,57.2,57.5,135000,58.77,-2.15,56.09,67.46,0.5
20260825,58.5,58.8,56.2,58.8,185000,58.77,0.05,56.33,66.87,0.7
20260826,58.8,64,58.8,62.9,875000,59.11,6.41,56.91,66.37,3.2
20260827,62.8,63.4,61.8,62.1,374000,59.36,4.61,57.56,65.94,1.35
20260828,62.9,66,61.2,65.2,393000,59.85,8.94,58.28,65.58,1.39
20260831,64.6,68,64.1,67.8,1189000,60.51,12.05,59.01,65.31,3.62
20260901,68.6,69.8,67.3,67.4,2299000,61.08,10.34,59.59,65.05,5.32
20260902,67.4,67.4,64.7,65,618000,61.41,5.84,60.06,64.84,1.37
20260903,65,65.2,61.2,61.5,441000,61.42,0.13,60.37,64.56,0.95
20260904,63.5,63.5,61.1,62.8,230000,61.53,2.06,60.74,64.33,0.49
20260907,62.9,63.5,62.5,62.9,182000,61.65,2.03,61.02,64.13,0.4
20260908,63.2,65.4,62.5,62.6,291000,61.73,1.41,61.26,63.92,0.66
20260909,62.7,66.1,62.4,65.8,1005000,62.07,6.02,61.65,63.7,2.09
20260910,65.8,65.8,63.6,64.3,334000,62.25,3.29,61.93,63.5,0.69
20260911,63,63,60.5,61.2,404000,62.16,-1.55,62.1,63.23,0.82
20260914,60.5,62.1,60,61.1,142000,62.08,-1.57,62.15,62.92,0.29
20260915,61.2,61.6,59.6,59.6,143000,61.87,-3.67,62.15,62.56,0.29
20260916,60.7,62.2,60.5,61.7,128000,61.86,-0.25,62.34,62.3,0.26
20260917,62,63.8,61.9,62.9,318000,61.94,1.55,62.53,62.04,0.65
20260918,63.7,68.5,63.7,68.2,1711000,62.46,9.18,63.06,61.91,3
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 43.29
- over_600_ratio: 37.42
- over_800_ratio: 35.92
- over_1000_ratio: 34.27
- over_400_change_1w: 0.72
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,42.73,-0.03,37.47,0.02,34.03,0,2,False,True
20260709,42.86,0.13,37.54,0.07,34.09,0.06,3,True,True
20260717,42.84,-0.02,37.53,-0.01,34.09,0,0,False,False
20260724,42.86,0.02,37.53,0,34.09,0,1,False,False
20260731,44.27,1.41,35.74,-1.79,34.09,0,2,False,False
20260807,42.58,-1.69,35.77,0.03,34.12,0.03,3,False,True
20260814,42.65,0.07,35.8,0.03,34.15,0.03,4,True,True
20260821,42.67,0.02,35.85,0.05,34.2,0.05,5,True,True
20260828,42.66,-0.01,35.89,0.04,34.24,0.04,6,False,True
20260904,42.7,0.04,35.92,0.03,34.27,0.03,7,True,True
20260911,42.57,-0.13,35.92,0,34.27,0,0,False,False
20260918,43.29,0.72,35.92,0,34.27,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6425 | 易發 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | first_seen | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管 (如:執行長、營運長、行銷長及策略長等)、財務主管、會計 主管、公司治理主管、資訊安全長、研發主管、內部稽核主管或訴訟及非 訟代理人）:財務主管、會計主管、公司治理主管、代理發言人 2.發生變動日期:115/06/17 3.舊任者姓名、級職及簡歷:邱耀進/管理部副總經理 4.新任者姓名、級職及簡歷:  (1)財務主管、公司治理主管：洪士傑/董事長室特助  (2)會計主管：蔡雅蜂/管理部經理  (3)代理發言人：張千駿/董事長室特助 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、 「退休」、「死亡」、「新任」或「解任」）:職務調整 6.異動原因:職務調整 7.生效日期:115/06/18 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6425 | 易發 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | first_seen | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管 (如:執行長、營運長、行銷長及策略長等)、財務主管、會計 主管、公司治理主管、資訊安全長、研發主管、內部稽核主管或訴訟及非 訟代理人）:財務主管、會計主管、公司治理主管、代理發言人 2.發生變動日期:115/06/17 3.舊任者姓名、級職及簡歷:邱耀進/管理部副總經理 4.新任者姓名、級職及簡歷:  (1)財務主管、公司治理主管：洪士傑/董事長室特助  (2)會計主管：蔡雅蜂/管理部經理  (3)代理發言人：張千駿/董事長室特助 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、 「退休」、「死亡」、「新任」或「解任」）:職務調整 6.異動原因:職務調整 7.生效日期:115/06/18 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 6425 | 易發 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | first_seen | 1.人員變動別（請輸入發言人、代理發言人、重要營運主管 (如:執行長、營運長、行銷長及策略長等)、財務主管、會計 主管、公司治理主管、資訊安全長、研發主管、內部稽核主管或訴訟及非 訟代理人）:財務主管、會計主管、公司治理主管、代理發言人 2.發生變動日期:115/06/17 3.舊任者姓名、級職及簡歷:邱耀進/管理部副總經理 4.新任者姓名、級職及簡歷:  (1)財務主管、公司治理主管：洪士傑/董事長室特助  (2)會計主管：蔡雅蜂/管理部經理  (3)代理發言人：張千駿/董事長室特助 5.異動情形（請輸入「辭職」、「職務調整」、「資遣」、 「退休」、「死亡」、「新任」或「解任」）:職務調整 6.異動原因:職務調整 7.生效日期:115/06/18 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6425 | 易發 | 1 | 1 | 1 | 2 | 4 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
