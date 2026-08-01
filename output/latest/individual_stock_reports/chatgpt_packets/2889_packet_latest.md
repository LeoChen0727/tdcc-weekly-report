# INDIVIDUAL STOCK CHATGPT PACKET - 2889 國票金

## Metadata
- generated_at: 2026-08-01 22:27:09 Asia/Taipei
- stock_id: 2889
- stock_name: 國票金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2889_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2889_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2889_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2889_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2889.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2889.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2889.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2889.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2889_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2889_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2889_latest.md?ref=main

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
- date: 20260730
- open: 15.45
- high: 15.7
- low: 15.3
- close: 15.65
- volume: 8908918
- ma5: 15.62
- ema23_primary: 15.51
- distance_to_ema23_pct: 0.94
- ma20: 15.58
- ma60: 15.07
- ma120: 15.49
- return_5d: 0
- return_20d: 5.39
- volume_ratio: 1.07
- distance_to_ma20_pct_auxiliary: 0.43
- distance_to_high_60_pct: -2.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,14.85,14.9,14.75,14.8,2748291,14.91,-0.76,14.98,14.87,0.39
20260703,14.75,15,14.75,15,5493281,14.92,0.54,14.97,14.87,0.77
20260706,15,15.25,15,15.2,8356861,14.94,1.72,14.98,14.86,1.16
20260707,15.1,15.3,15.1,15.3,8919366,14.97,2.18,15.01,14.86,1.23
20260708,15.5,15.95,15.5,15.7,24296189,15.03,4.43,15.04,14.87,3
20260709,15.7,15.95,15.65,15.8,24647542,15.1,4.65,15.08,14.88,2.78
20260713,15.9,16.1,15.7,15.85,11883776,15.16,4.55,15.13,14.89,1.29
20260714,15.95,15.95,15.5,15.7,10264268,15.21,3.25,15.16,14.89,1.11
20260715,15.8,15.9,15.7,15.8,3988521,15.25,3.57,15.2,14.9,0.44
20260716,15.8,15.85,15.75,15.85,2917915,15.3,3.57,15.24,14.91,0.33
20260717,15.8,15.85,15.6,15.7,7668636,15.34,2.36,15.26,14.92,0.9
20260720,15.75,15.8,15.55,15.7,5457749,15.37,2.16,15.29,14.94,0.65
20260721,15.7,15.9,15.65,15.8,6260496,15.4,2.57,15.32,14.95,0.75
20260722,15.75,15.85,15.65,15.7,6958678,15.43,1.76,15.36,14.97,0.84
20260723,15.75,15.8,15.55,15.65,3908623,15.45,1.32,15.39,14.99,0.48
20260724,15.6,15.75,15.5,15.75,6052478,15.47,1.8,15.43,15.01,0.73
20260727,15.75,15.75,15.55,15.7,3998181,15.49,1.35,15.47,15.02,0.51
20260728,15.6,15.6,15.5,15.6,5477802,15.5,0.64,15.52,15.04,0.69
20260729,15.6,15.6,15.15,15.4,8337721,15.49,-0.59,15.54,15.06,1.03
20260730,15.45,15.7,15.3,15.65,8908918,15.51,0.94,15.58,15.07,1.07
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 73.79
- over_600_ratio: 72.75
- over_800_ratio: 71.79
- over_1000_ratio: 71.22
- over_400_change_1w: 0.15
- over_800_change_1w: 0.17
- over_1000_change_1w: 0.22
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,74.36,-0.09,72.51,-0.08,71.87,-0.11,0,False,False
20260522,74.4,0.04,72.58,0.07,71.94,0.07,1,True,True
20260529,74.39,-0.01,72.52,-0.06,71.9,-0.04,0,False,False
20260605,74.39,0,72.51,-0.01,71.87,-0.03,0,False,False
20260612,74.28,-0.11,72.43,-0.08,71.79,-0.08,0,False,False
20260618,74.13,-0.15,72.26,-0.17,71.62,-0.17,0,False,False
20260626,73.93,-0.2,72.02,-0.24,71.37,-0.25,0,False,False
20260703,73.77,-0.16,71.85,-0.17,71.18,-0.19,0,False,False
20260709,73.84,0.07,71.89,0.04,71.2,0.02,1,True,True
20260717,73.83,-0.01,71.82,-0.07,71.15,-0.05,0,False,False
20260724,73.64,-0.19,71.62,-0.2,71,-0.15,0,False,False
20260731,73.79,0.15,71.79,0.17,71.22,0.22,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2889 | 國票金 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/14 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除權 3.發放股利種類及金額: 股票股利每股配發新台幣0.135281元(金額:250,000,000元) 4.除權（息）交易日:NA 5.最後過戶日:NA 6.停止過戶起始日期:115/07/17 7.停止過戶截止日期:115/07/21 8.除權（息）基準日:115/07/21 9.其他應敘明事項: (1).本次發行新股業經金融監督管理委員會民國115年7月8日申報生效在案。 (2).股票股利於經濟部核准變更登記後30日內交付股東。 (3).發放對象為本公司之唯一法人股東國票金融控股股份有限公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2889 | 國票金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/14 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除權 3.發放股利種類及金額: 股票股利每股配發新台幣0.135281元(金額:250,000,000元) 4.除權（息）交易日:NA 5.最後過戶日:NA 6.停止過戶起始日期:115/07/17 7.停止過戶截止日期:115/07/21 8.除權（息）基準日:115/07/21 9.其他應敘明事項: (1).本次發行新股業經金融監督管理委員會民國115年7月8日申報生效在案。 (2).股票股利於經濟部核准變更登記後30日內交付股東。 (3).發放對象為本公司之唯一法人股東國票金融控股股份有限公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2889 | 國票金 | 11 | 3 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
