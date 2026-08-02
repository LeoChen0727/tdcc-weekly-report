# INDIVIDUAL STOCK CHATGPT PACKET - 1402 遠東新

## Metadata
- generated_at: 2026-08-01 22:26:24 Asia/Taipei
- stock_id: 1402
- stock_name: 遠東新
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
- tdcc_rows: 36
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1402_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1402_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1402_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1402_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1402_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1402_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1402_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1402.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1402.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1402.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1402.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1402_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1402_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1402_latest.md?ref=main

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
- near_23ema_or_support
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
- date: 20260730
- open: 27.4
- high: 27.4
- low: 26.8
- close: 27.15
- volume: 13948622
- ma5: 27.32
- ema23_primary: 27.52
- distance_to_ema23_pct: -1.35
- ma20: 27.61
- ma60: 27.27
- ma120: 27.23
- return_5d: -0.18
- return_20d: -4.06
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: -1.66
- distance_to_high_60_pct: -9.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,28.2,28.65,28.2,28.4,11108929,27.94,1.63,28.13,26.84,0.31
20260703,28.25,29.9,28.25,29.1,25497121,28.04,3.78,28.21,26.88,0.75
20260706,29.3,29.8,29.05,29.1,12555083,28.13,3.45,28.29,26.92,0.41
20260707,29.05,29.1,28.2,28.35,21682221,28.15,0.72,28.36,26.95,0.76
20260708,28.45,28.75,27.7,27.85,27962921,28.12,-0.97,28.37,26.97,1.03
20260709,27.75,27.95,27.2,27.45,27617109,28.07,-2.2,28.36,26.99,1.06
20260713,27.45,27.7,26.8,26.85,44969324,27.97,-3.99,28.34,26.99,1.71
20260714,25.75,26.7,25.75,26.35,42826352,27.83,-5.32,28.3,26.99,1.59
20260715,26.5,27.75,26.25,27.55,35978832,27.81,-0.93,28.3,27.01,1.29
20260716,27.35,27.9,27.3,27.8,21827775,27.81,-0.02,28.27,27.04,0.81
20260717,27.6,28.2,27.6,27.7,23024082,27.8,-0.35,28.21,27.07,0.87
20260720,27.9,28.15,27.25,27.3,18759029,27.76,-1.64,28.13,27.09,0.73
20260721,27.55,27.85,27.35,27.35,18716985,27.72,-1.34,28.06,27.11,0.75
20260722,27.35,27.85,27.2,27.2,15942868,27.68,-1.73,27.99,27.13,0.65
20260723,27.45,27.5,26.9,27.2,18684169,27.64,-1.59,27.93,27.15,0.77
20260724,27,27.65,27,27.35,26234889,27.61,-0.96,27.86,27.17,1.09
20260727,27.45,27.7,27.4,27.45,16657114,27.6,-0.55,27.81,27.19,0.7
20260728,27.5,27.7,27.2,27.4,11021149,27.58,-0.67,27.73,27.22,0.48
20260729,27.65,27.75,26.7,27.25,16977601,27.56,-1.11,27.66,27.25,0.75
20260730,27.4,27.4,26.8,27.15,13948622,27.52,-1.35,27.61,27.27,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 88.76
- over_600_ratio: 87.93
- over_800_ratio: 87.4
- over_1000_ratio: 86.78
- over_400_change_1w: 0.17
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,88.06,0.28,86.3,0.29,85.55,0.25,3,True,True
20260522,88.24,0.18,86.4,0.1,85.68,0.13,4,True,True
20260529,86.68,-1.56,84.73,-1.67,83.98,-1.7,0,False,False
20260605,87,0.32,85.32,0.59,84.66,0.68,1,True,True
20260612,87.56,0.56,86.02,0.7,85.4,0.74,2,True,True
20260618,88.08,0.52,86.59,0.57,85.92,0.52,3,True,True
20260626,88.46,0.38,87.06,0.47,86.39,0.47,4,True,True
20260703,88.61,0.15,87.18,0.12,86.53,0.14,5,True,True
20260709,88.7,0.09,87.27,0.09,86.67,0.14,6,True,True
20260717,88.46,-0.24,87.06,-0.21,86.49,-0.18,0,False,False
20260724,88.59,0.13,87.2,0.14,86.63,0.14,1,True,True
20260731,88.76,0.17,87.4,0.2,86.78,0.15,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1402 | 遠東新 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.證券名稱: 亞洲水泥股份有限公司 普通股股票 2.交易日期:115/6/17~115/6/29 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年06月29日 5.交易數量、每單位價格及交易總金額: 交易數量：8,362,000股 每單位價格：新台幣35.98元整 交易總金額：新台幣300,900,058元整 6.處分利益（或損失）（取得有價證券者不適用）: 不適用 7.與交易標的公司之關係: 企業採權益法評價之被投資公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 持有股數：23,147,674股 持有金額：新台幣882,861,598元整 持股比例：0.65% 權利受限情形：無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 佔總資產比例：0.90% 佔股東權益比例：1.42% 營運資金：新台幣-2,597,834仟元整 資金來源：營業收入 10.取得或處分之具體目的: 增加投資 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1402 | 遠東新 | 2 | 2 | 2 | 5 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1402 | 遠東新 | 11 | 0 | 994020.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
