# INDIVIDUAL STOCK CHATGPT PACKET - 4147 中裕

## Metadata
- generated_at: 2026-08-22 22:27:46 Asia/Taipei
- stock_id: 4147
- stock_name: 中裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4147_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4147_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4147.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4147.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4147.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4147.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4147_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4147_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4147_latest.md?ref=main

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
- date: 20260821
- open: 63.7
- high: 64.7
- low: 63.1
- close: 63.1
- volume: 1213000
- ma5: 62.78
- ema23_primary: 61.73
- distance_to_ema23_pct: 2.22
- ma20: 60.49
- ma60: 60.42
- ma120: 55.91
- return_5d: -1.71
- return_20d: 7.68
- volume_ratio: 1.03
- distance_to_ma20_pct_auxiliary: 4.31
- distance_to_high_60_pct: -16.31

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,58.5,59.6,58.3,58.9,547000,61.54,-4.29,64.17,56.94,0.28
20260728,58.7,59.1,57.4,58,819000,61.25,-5.3,63.88,57.09,0.43
20260729,58.4,58.7,55,56.5,1309000,60.85,-7.15,63.46,57.22,0.71
20260730,56,58.6,55.7,56.2,1034000,60.46,-7.05,63.08,57.33,0.58
20260731,58,58.3,55,55,1010000,60.01,-8.35,62.64,57.42,0.57
20260803,55.1,57.8,54.6,56.9,607000,59.75,-4.77,61.98,57.55,0.39
20260804,56.9,57.8,56.5,57.6,439000,59.57,-3.31,61.26,57.68,0.32
20260805,57.8,59.3,57.8,59.1,573000,59.53,-0.72,60.58,57.85,0.45
20260806,59.5,59.5,57.8,58.5,323000,59.45,-1.59,59.97,57.99,0.27
20260807,57.8,58.5,56.4,56.8,720000,59.22,-4.09,59.33,58.12,0.65
20260810,58.3,62.1,58.2,61,1330000,59.37,2.74,59.16,58.24,1.28
20260811,60.2,64.5,60.2,63.5,1833000,59.72,6.34,59.13,58.45,1.71
20260812,63.5,69.8,63.4,68.5,5204000,60.45,13.32,59.29,58.76,4.04
20260813,66.5,67.8,64.9,65.2,1606000,60.84,7.16,59.25,59.02,1.24
20260814,65.2,65.2,63.3,64.2,917000,61.12,5.03,59.47,59.28,0.78
20260817,65.5,65.5,61.2,61.6,961000,61.16,0.71,59.6,59.49,0.84
20260818,62.6,64.6,60.9,63.1,1690000,61.33,2.89,59.83,59.7,1.43
20260819,62.9,63.3,62.2,62.4,441000,61.41,1.6,60.03,59.91,0.39
20260820,63.9,64.5,62.9,63.7,1016000,61.61,3.4,60.27,60.16,0.88
20260821,63.7,64.7,63.1,63.1,1213000,61.73,2.22,60.49,60.42,1.03
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 52.7
- over_600_ratio: 50.03
- over_800_ratio: 45.68
- over_1000_ratio: 44.72
- over_400_change_1w: -0.62
- over_800_change_1w: -0.11
- over_1000_change_1w: 0.23
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,52.76,0.83,45.9,0.53,43.63,0.21,2,True,True
20260612,52.69,-0.07,45.73,-0.17,43.2,-0.43,3,False,False
20260618,51.92,-0.77,45.68,-0.05,43.12,-0.08,0,False,False
20260626,52.11,0.19,45.8,0.12,43.9,0.78,1,False,True
20260703,52.41,0.3,45.98,0.18,43.75,-0.15,2,False,True
20260709,52.99,0.58,46.24,0.26,43.98,0.23,3,True,True
20260717,52.57,-0.42,45.76,-0.48,44.13,0.15,4,False,True
20260724,52.48,-0.09,45.35,-0.41,43.75,-0.38,0,False,False
20260731,52.7,0.22,45.48,0.13,43.55,-0.2,1,False,True
20260807,52.6,-0.1,45.56,0.08,43.65,0.1,2,False,True
20260814,53.32,0.72,45.79,0.23,44.49,0.84,3,True,True
20260821,52.7,-0.62,45.68,-0.11,44.72,0.23,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4147 | 中裕 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | repeated_but_no_breakout | 1.事實發生日:115/06/22 2.契約或承諾相對人:Samsung Biologics Co., Ltd. 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:115/06/22 5.主要內容（解除者不適用）:本公司與Samsung Biologics Co., Ltd.簽訂TMB-365 商業產品藥物原料之產品專屬協議（Product Specific Agreement–Commercial Product Drug Substance） 6.限制條款（解除者不適用）:無 7.承諾事項（解除者不適用）:無 8.其他重要約定事項（解除者不適用）:無 9.對公司財務、業務之影響:本公司與Samsung Biologics Co., Ltd.達成深度合作， 全面啟動 TMB-365 的技術移轉與規模化量產，以全力支持臨床試驗以及未來的 全球市場上市供應。 10.具體目的:本公司與Samsung Biologics Co., Ltd.達成深度合作，全面啟動 TMB-365 的技術移轉與規模化量產，以全力支持臨床試驗以及未來的全球市場 上市供應。 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4147 | 中裕 | 4 | 2 | 4 | 7 | 13 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 13 次，但尚未有效突破，需等待攻擊確認。 |

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
