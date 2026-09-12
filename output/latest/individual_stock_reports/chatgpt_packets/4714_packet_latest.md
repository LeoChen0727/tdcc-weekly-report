# INDIVIDUAL STOCK CHATGPT PACKET - 4714 永捷

## Metadata
- generated_at: 2026-09-12 15:43:45 Asia/Taipei
- stock_id: 4714
- stock_name: 永捷
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4714_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4714_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4714_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4714_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4714_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4714_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4714_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4714.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4714.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4714.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4714.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4714_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4714_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4714_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 11
- high: 11.75
- low: 10.85
- close: 11.7
- volume: 3108000
- ma5: 11.05
- ema23_primary: 10.94
- distance_to_ema23_pct: 6.92
- ma20: 10.91
- ma60: 11.17
- ma120: 12.71
- return_5d: 9.86
- return_20d: 11.96
- volume_ratio: 2.22
- distance_to_ma20_pct_auxiliary: 7.22
- distance_to_high_60_pct: -12.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,10.5,10.85,10.5,10.65,655000,10.76,-1,10.49,12.01,0.87
20260818,10.7,10.7,10.5,10.5,547000,10.74,-2.2,10.47,11.96,0.75
20260819,10.5,10.5,10.35,10.45,443000,10.71,-2.45,10.44,11.91,0.62
20260820,10.5,10.65,10.45,10.55,426000,10.7,-1.39,10.42,11.85,0.6
20260821,10.55,10.8,10.5,10.75,827000,10.7,0.44,10.42,11.8,1.17
20260824,10.9,11.1,10.75,10.75,824000,10.71,0.4,10.42,11.75,1.15
20260825,10.75,10.75,10.6,10.65,280000,10.7,-0.49,10.44,11.71,0.41
20260826,10.8,11.7,10.75,11.35,2386000,10.76,5.52,10.51,11.67,3.35
20260827,11.05,12.4,11,11.8,6602000,10.84,8.82,10.6,11.64,6.65
20260828,11.8,11.95,11.2,11.4,3531000,10.89,4.69,10.67,11.6,3.17
20260831,11.25,11.45,11,11.15,1360000,10.91,2.19,10.72,11.55,1.19
20260901,11.1,11.15,10.9,10.9,1062000,10.91,-0.1,10.75,11.5,0.91
20260902,10.9,10.95,10.85,10.85,272000,10.91,-0.51,10.77,11.46,0.24
20260903,10.9,11,10.6,10.6,514000,10.88,-2.57,10.77,11.41,0.45
20260904,10.75,10.75,10.5,10.65,457000,10.86,-1.94,10.79,11.37,0.4
20260907,10.7,10.7,10.55,10.55,252000,10.83,-2.63,10.79,11.32,0.22
20260908,10.65,10.95,10.6,10.8,649000,10.83,-0.3,10.8,11.27,0.57
20260909,10.9,11.35,10.7,11.2,1660000,10.86,3.11,10.83,11.24,1.39
20260910,11.4,11.6,10.95,11,2151000,10.87,1.16,10.85,11.2,1.7
20260911,11,11.75,10.85,11.7,3108000,10.94,6.92,10.91,11.17,2.22
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 29.36
- over_600_ratio: 26.62
- over_800_ratio: 24.45
- over_1000_ratio: 22.9
- over_400_change_1w: 0.3
- over_800_change_1w: 0.12
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,21.14,-1.91,15.96,-0.67,15.96,0.39,1,False,True
20260703,21.81,0.67,15.96,0,15.96,0,2,False,False
20260709,21.21,-0.6,15.78,-0.18,15.78,-0.18,0,False,False
20260717,29.02,7.81,23.54,7.76,21.98,6.2,1,True,True
20260724,28.75,-0.27,24.37,0.83,22.02,0.04,2,False,True
20260731,28.74,-0.01,23.4,-0.97,21.88,-0.14,3,False,False
20260807,29.09,0.35,23.9,0.5,22.38,0.5,4,True,True
20260814,29.14,0.05,24,0.1,22.48,0.1,5,False,True
20260821,29.32,0.18,23.64,-0.36,21.7,-0.78,6,False,False
20260828,29.21,-0.11,24.27,0.63,22.31,0.61,7,False,True
20260904,29.06,-0.15,24.33,0.06,22.79,0.48,8,False,True
20260911,29.36,0.3,24.45,0.12,22.9,0.11,9,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 4714 | 永捷 | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/08/28 1.召開法人說明會之日期：115/08/28 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：Webex視訊會議 4.法人說明會擇要訊息：本公司受邀凱基證券舉辦之線上法人說明會 5.其他應敘明事項：完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 4714 | 永捷 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/08/28 1.召開法人說明會之日期：115/08/28 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：Webex視訊會議 4.法人說明會擇要訊息：本公司受邀凱基證券舉辦之線上法人說明會 5.其他應敘明事項：完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 4714 | 永捷 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/08/28 1.召開法人說明會之日期：115/08/28 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：Webex視訊會議 4.法人說明會擇要訊息：本公司受邀凱基證券舉辦之線上法人說明會 5.其他應敘明事項：完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 4714 | 永捷 | 1 | 1 | 1 | 2 | 5 | repeated_but_no_breakout | 近 10 日上榜 2 次、近 20 日上榜 5 次，但尚未有效突破，需等待攻擊確認。 |

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
