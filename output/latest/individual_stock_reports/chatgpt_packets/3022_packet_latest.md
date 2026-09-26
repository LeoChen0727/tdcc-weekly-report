# INDIVIDUAL STOCK CHATGPT PACKET - 3022 威強電

## Metadata
- generated_at: 2026-09-26 22:16:34 Asia/Taipei
- stock_id: 3022
- stock_name: 威強電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3022_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3022_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3022_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3022_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3022_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3022_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3022_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3022.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3022.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3022.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3022.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3022_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3022_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3022_latest.md?ref=main

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
- date: 20260924
- open: 90.4
- high: 93.6
- low: 90.4
- close: 93.1
- volume: 1540683
- ma5: 91.82
- ema23_primary: 90.14
- distance_to_ema23_pct: 3.28
- ma20: 89.16
- ma60: 90.96
- ma120: 82.57
- return_5d: 4.72
- return_20d: 1.75
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: 4.42
- distance_to_high_60_pct: -20.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,91.8,92.3,90.1,90.3,1191175,93.3,-3.22,96.39,88.99,0.32
20260831,90.1,91.4,89.6,90.3,818397,93.05,-2.96,96.31,89.22,0.22
20260901,90.5,93.1,89.5,92.5,1667997,93,-0.54,96.39,89.48,0.46
20260902,91.6,92.3,90.4,90.4,854935,92.79,-2.57,96.03,89.67,0.26
20260903,90.6,90.9,87.1,87.2,1539796,92.32,-5.55,95.36,89.67,0.52
20260904,88,95.9,88,95.9,4749366,92.62,3.54,95,89.85,1.66
20260907,97,98.6,91.2,91.5,4751940,92.53,-1.11,93.93,89.94,1.78
20260908,89.4,89.4,85.5,86.4,3966075,92.02,-6.1,92.85,89.93,1.64
20260909,86.5,86.7,85.3,85.7,1501028,91.49,-6.33,91.86,89.94,0.65
20260910,85.6,85.6,84.1,84.4,1037667,90.9,-7.15,91.17,89.97,0.49
20260911,82.2,85,82.1,83.2,1163839,90.26,-7.82,90.62,89.96,0.59
20260914,82.7,87,82.7,86.2,1241326,89.92,-4.14,90.11,89.99,0.65
20260915,86.3,88.6,85.1,85.2,1114601,89.53,-4.83,89.73,90.02,0.6
20260916,85.3,86,84.8,86,564520,89.23,-3.62,89.44,90.09,0.31
20260917,86.1,90.5,86.1,88.9,2348054,89.2,-0.34,89.25,90.19,1.31
20260918,90.5,91.4,89.7,91,1158352,89.35,1.84,89.3,90.33,0.66
20260921,91.1,94.6,91,92.8,1972703,89.64,3.52,89.25,90.52,1.12
20260922,93.4,93.8,91.5,91.5,1048535,89.8,1.9,89.17,90.67,0.59
20260923,92.2,92.6,90.1,90.7,849829,89.87,0.92,89.08,90.79,0.49
20260924,90.4,93.6,90.4,93.1,1540683,90.14,3.28,89.16,90.96,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 65.74
- over_600_ratio: 63.41
- over_800_ratio: 62.26
- over_1000_ratio: 60.35
- over_400_change_1w: 0.25
- over_800_change_1w: 0.68
- over_1000_change_1w: 0.66
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,63.53,2.73,58.6,2.1,55.63,1.58,1,True,True
20260717,62.63,-0.9,58.07,-0.53,55.03,-0.6,0,False,False
20260724,64.16,1.53,59.7,1.63,56.62,1.59,1,True,True
20260731,64.99,0.83,60.36,0.66,57.95,1.33,2,True,True
20260807,66.52,1.53,61.39,1.03,57.52,-0.43,3,False,True
20260814,68.26,1.74,64.3,2.91,60.86,3.34,4,True,True
20260821,66.31,-1.95,60.28,-4.02,58.82,-2.04,0,False,False
20260828,66.1,-0.21,60.66,0.38,59.24,0.42,1,False,True
20260904,65.72,-0.38,60.8,0.14,59.37,0.13,2,False,True
20260911,64.62,-1.1,60.64,-0.16,58.74,-0.63,0,False,False
20260918,65.49,0.87,61.58,0.94,59.69,0.95,1,True,True
20260924,65.74,0.25,62.26,0.68,60.35,0.66,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3022 | 威強電 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/09/23 1.召開法人說明會之日期：115/09/23 2.召開法人說明會之時間：14 時 30 分 3.召開法人說明會之地點：元大金控大樓6樓(台北市敦化南路一段66號) 4.法人說明會擇要訊息：本公司受邀參加元大證券舉辦之法人說明會，會中將說明本公司115年第二季營運成果及未來展望。 5.其他應敘明事項：本次法人說明會參加人員以元大證券邀約對象為主。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3022 | 威強電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/09/23 1.召開法人說明會之日期：115/09/23 2.召開法人說明會之時間：14 時 30 分 3.召開法人說明會之地點：元大金控大樓6樓(台北市敦化南路一段66號) 4.法人說明會擇要訊息：本公司受邀參加元大證券舉辦之法人說明會，會中將說明本公司115年第二季營運成果及未來展望。 5.其他應敘明事項：本次法人說明會參加人員以元大證券邀約對象為主。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 3022 | 威強電 | revenue_breakout_low_response | 營收爆發低反應股 | 20 | 6 | A_優先追蹤 |  |  | call_inflow | repeated_but_no_breakout | 符合條款第四條第XX款：12 事實發生日：115/09/23 1.召開法人說明會之日期：115/09/23 2.召開法人說明會之時間：14 時 30 分 3.召開法人說明會之地點：元大金控大樓6樓(台北市敦化南路一段66號) 4.法人說明會擇要訊息：本公司受邀參加元大證券舉辦之法人說明會，會中將說明本公司115年第二季營運成果及未來展望。 5.其他應敘明事項：本次法人說明會參加人員以元大證券邀約對象為主。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3022 | 威強電 | 1 | 1 | 4 | 8 | 16 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 16 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3022 | 威強電 | 22 | 0 | 2935060.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
