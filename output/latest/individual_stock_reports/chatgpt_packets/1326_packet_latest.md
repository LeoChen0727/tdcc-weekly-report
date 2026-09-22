# INDIVIDUAL STOCK CHATGPT PACKET - 1326 台化

## Metadata
- generated_at: 2026-09-20 22:15:41 Asia/Taipei
- stock_id: 1326
- stock_name: 台化
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1326_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1326_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1326_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1326_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1326.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1326.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1326.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1326.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1326_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1326_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1326_latest.md?ref=main

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
- date: 20260918
- open: 69.1
- high: 69.2
- low: 67.1
- close: 68.1
- volume: 24373131
- ma5: 67.18
- ema23_primary: 66.71
- distance_to_ema23_pct: 2.09
- ma20: 67.36
- ma60: 63.53
- ma120: 56.48
- return_5d: -2.99
- return_20d: 13.31
- volume_ratio: 0.62
- distance_to_ma20_pct_auxiliary: 1.09
- distance_to_high_60_pct: -12.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,59.9,60.5,56.3,57.1,33373804,59.53,-4.08,58.55,58.68,1.19
20260825,56.5,58.3,56.1,58,10506144,59.4,-2.36,58.4,58.81,0.4
20260826,57.9,60.9,57.7,60.3,28273104,59.48,1.39,58.49,58.92,1.12
20260827,61,64.2,60.1,63.2,38108484,59.79,5.71,58.83,59.07,1.52
20260828,63.5,64.2,62,62.1,23816854,59.98,3.54,59.06,59.16,1
20260831,62,68.3,61.9,68.3,71396602,60.67,12.57,59.66,59.38,2.75
20260901,69.3,74.9,67.3,74.3,119283939,61.81,20.21,60.47,59.74,3.91
20260902,74.5,74.7,70.5,72.8,62533246,62.72,16.06,61.18,60.14,1.93
20260903,72.1,78.2,69.3,69.7,82419512,63.3,10.1,61.76,60.5,2.3
20260904,70,70.8,67.4,69.8,41291535,63.85,9.33,62.3,60.89,1.13
20260907,70.2,75.1,69.9,71.9,57918008,64.52,11.44,62.96,61.32,1.5
20260908,72.6,72.6,70.1,70.6,24157597,65.02,8.57,63.58,61.68,0.62
20260909,70.9,73.5,70.2,71.8,37249918,65.59,9.47,64.19,62.02,0.94
20260910,72,72.7,70.3,71.3,22295065,66.06,7.92,64.78,62.34,0.56
20260911,70.4,71.8,69.8,70.2,18556570,66.41,5.71,65.27,62.61,0.47
20260914,70.5,70.5,66.2,67.6,27922318,66.51,1.64,65.68,62.84,0.7
20260915,66.6,66.8,64.9,65.8,23789944,66.45,-0.98,66,63,0.6
20260916,66.1,67.7,65.4,65.8,15902772,66.4,-0.9,66.45,63.21,0.41
20260917,66.3,68.7,66.1,68.6,24043657,66.58,3.04,66.97,63.39,0.61
20260918,69.1,69.2,67.1,68.1,24373131,66.71,2.09,67.36,63.53,0.62
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 83.04
- over_600_ratio: 82.06
- over_800_ratio: 81.23
- over_1000_ratio: 80.42
- over_400_change_1w: -0.14
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,82.95,-0.02,81.12,-0.01,80.46,0.02,3,False,True
20260709,82.54,-0.41,80.82,-0.3,80.1,-0.36,0,False,False
20260717,82.32,-0.22,80.59,-0.23,79.89,-0.21,0,False,False
20260724,82.79,0.47,80.99,0.4,80.26,0.37,1,True,True
20260731,82.15,-0.64,80.37,-0.62,79.68,-0.58,0,False,False
20260807,81.83,-0.32,80.07,-0.3,79.39,-0.29,0,False,False
20260814,81.84,0.01,80.05,-0.02,79.35,-0.04,1,False,False
20260821,81.68,-0.16,79.84,-0.21,79.05,-0.3,0,False,False
20260828,81.92,0.24,79.97,0.13,79.22,0.17,1,True,True
20260904,83.08,1.16,81.22,1.25,80.52,1.3,2,True,True
20260911,83.18,0.1,81.31,0.09,80.62,0.1,3,True,True
20260918,83.04,-0.14,81.23,-0.08,80.42,-0.2,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1326 | 台化 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/08/27 1.召開法人說明會之日期：115/08/27 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：華南永昌綜合證券(台北市民生東路四段54號4樓) 4.法人說明會擇要訊息：本公司受邀參加華南永昌證券舉辦之法人說明會，說明本公司115年上半年之營運概況及產業展望 5.其他應敘明事項：如遇颱風影響，依臺北市政府公告停止上班訊息，本次說明會將擇期舉辦。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 1326 | 台化 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/08/27 1.召開法人說明會之日期：115/08/27 2.召開法人說明會之時間：14 時 00 分 3.召開法人說明會之地點：華南永昌綜合證券(台北市民生東路四段54號4樓) 4.法人說明會擇要訊息：本公司受邀參加華南永昌證券舉辦之法人說明會，說明本公司115年上半年之營運概況及產業展望 5.其他應敘明事項：如遇颱風影響，依臺北市政府公告停止上班訊息，本次說明會將擇期舉辦。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1326 | 台化 | 3 | 3 | 3 | 5 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1326 | 台化 | 138 | 5 | 14358110.0 | 84830.0 | 169.26 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
