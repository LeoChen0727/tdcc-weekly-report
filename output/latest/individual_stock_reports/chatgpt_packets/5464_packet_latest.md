# INDIVIDUAL STOCK CHATGPT PACKET - 5464 霖宏

## Metadata
- generated_at: 2026-09-19 15:53:57 Asia/Taipei
- stock_id: 5464
- stock_name: 霖宏
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5464_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5464.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5464.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5464_latest.md?ref=main

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
- action_summary_zh: 型態觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「高位整理」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: high_level_consolidation
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
- date: 20260918
- open: 91
- high: 95.9
- low: 90.1
- close: 92.7
- volume: 1024000
- ma5: 90.16
- ema23_primary: 80.59
- distance_to_ema23_pct: 15.03
- ma20: 78.38
- ma60: 79.14
- ma120: 66.68
- return_5d: 4.04
- return_20d: 34.93
- volume_ratio: 1.01
- distance_to_ma20_pct_auxiliary: 18.28
- distance_to_high_60_pct: -14.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,68,69.9,66.3,68.6,546000,71.48,-4.02,67.47,78.33,0.79
20260825,69.9,69.9,67,69.2,236000,71.29,-2.93,67.33,78.1,0.36
20260826,69.9,75.3,68.8,74,524000,71.51,3.48,67.79,78,0.79
20260827,69.7,72,68.3,71,1006000,71.47,-0.66,68.36,77.91,1.59
20260828,71.2,76,71.1,73.1,338000,71.61,2.09,68.75,77.96,0.55
20260831,72.9,72.9,70,70.8,237000,71.54,-1.03,69.08,78.04,0.4
20260901,74.3,74.3,69,69,319000,71.33,-3.26,69.34,78.07,0.54
20260902,68.8,70,68,69.3,169000,71.16,-2.61,69.67,78.16,0.29
20260903,69.7,71.9,68,69,375000,70.98,-2.79,69.75,78.14,0.7
20260904,69.3,70.2,68.3,69.5,211000,70.85,-1.91,70.09,78.17,0.44
20260907,74,76.4,74,76.4,756000,71.32,7.13,70.83,78.28,1.51
20260908,76.8,81.5,75.3,75.3,2246000,71.65,5.1,71.52,78.34,3.82
20260909,74.5,82.8,74.5,82.8,1659000,72.58,14.08,72.28,78.53,2.7
20260910,82.8,91,82.7,89.6,4380000,74,21.09,73.06,78.86,5.36
20260911,88,89.8,86.7,89.1,1127000,75.26,18.4,73.74,79.12,1.4
20260914,87.4,91.2,85.6,89.1,966000,76.41,16.61,74.42,79.37,1.17
20260915,89.4,89.4,85,85.2,724000,77.14,10.45,75.05,79.44,0.86
20260916,85.2,93.7,84.1,93.7,1171000,78.52,19.33,76.2,79.52,1.32
20260917,99,99.8,89.6,90.1,2268000,79.49,13.35,77.17,79.39,2.31
20260918,91,95.9,90.1,92.7,1024000,80.59,15.03,78.38,79.14,1.01
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 72.49
- over_600_ratio: 67.45
- over_800_ratio: 63.85
- over_1000_ratio: 58.83
- over_400_change_1w: -0.29
- over_800_change_1w: -0.38
- over_1000_change_1w: 0.72
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,72.97,0.52,65.89,-1.32,59.13,-2.67,9,False,False
20260709,72.46,-0.51,64.52,-1.37,59.18,0.05,10,False,True
20260717,72.49,0.03,64.56,0.04,60.42,1.24,11,False,True
20260724,72.61,0.12,65.28,0.72,61.14,0.72,12,True,True
20260731,73.56,0.95,65.71,0.43,61.57,0.43,13,True,True
20260807,73,-0.56,64.4,-1.31,58.85,-2.72,0,False,False
20260814,72.62,-0.38,64.58,0.18,59.03,0.18,1,False,True
20260821,72.1,-0.52,64.73,0.15,59.18,0.15,2,False,True
20260828,71.61,-0.49,62.84,-1.89,57.85,-1.33,0,False,False
20260904,72.21,0.6,66.14,3.3,58.52,0.67,1,True,True
20260911,72.78,0.57,64.23,-1.91,58.11,-0.41,2,False,False
20260918,72.49,-0.29,63.85,-0.38,58.83,0.72,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5464 | 霖宏 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | 1.發生變動日期:115/07/01 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名: 申元洪先生 林惠芬女士 林怡君女士 4.舊任者簡歷: 申元洪先生 世新大學專任助理教授 林惠芬女士 維揚聯合會計師事務所執業會計師 林怡君女士 立隆電子工業股份有限公司財務部經理 5.新任者姓名: 林惠芬女士 林怡君女士 陳麗玲女士 6.新任者簡歷: 林惠芬女士 維揚聯合會計師事務所執業會計師 林怡君女士 立隆電子工業股份有限公司財務部經理 陳麗玲女士 全達會計師事務所執業會計師 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:配合本公司115年股東常會董事改選而重新聘任 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/21~115/06/20 10.新任生效日期:115/06/25 11.其他應敘明事項:第六屆薪酬委員會委員任期自115/06/25起至本屆董事會任期 屆滿之日止。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 5464 | 霖宏 | 1 | 1 | 3 | 5 | 6 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 6 次，但尚未有效突破，需等待攻擊確認。 |

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
