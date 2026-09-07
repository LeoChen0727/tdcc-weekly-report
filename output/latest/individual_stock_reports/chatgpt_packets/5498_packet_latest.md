# INDIVIDUAL STOCK CHATGPT PACKET - 5498 凱崴

## Metadata
- generated_at: 2026-09-06 22:17:45 Asia/Taipei
- stock_id: 5498
- stock_name: 凱崴
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5498_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5498.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5498.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5498_latest.md?ref=main

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
- date: 20260904
- open: 54
- high: 54.7
- low: 52.5
- close: 53.4
- volume: 1189000
- ma5: 54.94
- ema23_primary: 52.83
- distance_to_ema23_pct: 1.07
- ma20: 52.86
- ma60: 54.71
- ma120: 60.27
- return_5d: -8.09
- return_20d: 10.1
- volume_ratio: 0.42
- distance_to_ma20_pct_auxiliary: 1.02
- distance_to_high_60_pct: -26.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,49.5,51.2,48.65,50.6,1667000,49.72,1.77,47.64,58.44,0.83
20260811,50.6,53.2,50.5,51.1,2773000,49.83,2.54,47.46,58.12,1.39
20260812,50.9,56,50.9,55.2,4016000,50.28,9.78,47.4,57.89,1.89
20260813,55.9,56.2,53,53.3,3942000,50.53,5.47,47.37,57.69,1.75
20260814,53.7,53.7,51.8,51.8,1590000,50.64,2.29,47.51,57.53,0.74
20260817,51.9,52.4,50.6,51.2,1122000,50.69,1.01,47.71,57.34,0.54
20260818,51.5,52.2,49.8,49.8,1290000,50.61,-1.6,47.83,57.06,0.62
20260819,48.4,50.3,48.2,49.2,1174000,50.49,-2.56,47.8,56.74,0.58
20260820,49.85,52.2,49.05,50.7,1617000,50.51,0.37,47.9,56.41,0.8
20260821,53,54.8,50.3,50.4,4222000,50.5,-0.2,48.13,56.1,1.95
20260824,50.5,52.5,50.1,51.1,1880000,50.55,1.08,48.33,55.86,0.87
20260825,50.5,52.2,48.9,52.1,1357000,50.68,2.8,48.76,55.63,0.64
20260826,52.5,55.4,52.2,54.6,4485000,51.01,7.04,49.44,55.44,2.04
20260827,54.6,54.6,53,53.3,2227000,51.2,4.1,50.2,55.27,1.02
20260828,54.4,58.5,53.6,58.1,6537000,51.77,12.22,51.01,55.2,2.66
20260831,56.4,61.3,55.5,56.2,7707000,52.14,7.78,51.59,55.12,2.83
20260901,56.1,59.2,55.8,56.4,3837000,52.5,7.43,52.07,55.03,1.36
20260902,56.4,56.9,55.6,55.8,1948000,52.77,5.74,52.48,55,0.68
20260903,55.9,56.9,52.9,52.9,2471000,52.78,0.22,52.62,54.83,0.86
20260904,54,54.7,52.5,53.4,1189000,52.83,1.07,52.86,54.71,0.42
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 34.83
- over_600_ratio: 33.21
- over_800_ratio: 31.83
- over_1000_ratio: 30.04
- over_400_change_1w: -0.14
- over_800_change_1w: -0.35
- over_1000_change_1w: 0.09
- tdcc_consecutive_up_weeks: 8
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,33.47,-1.88,31.13,-1.87,30.25,-1.87,0,False,False
20260626,33.75,0.28,31.13,0,30.25,0,1,False,False
20260703,33.47,-0.28,30.55,-0.58,29.67,-0.58,0,False,False
20260709,33.2,-0.27,30.55,0,29.67,0,0,False,False
20260717,33.19,-0.01,30.97,0.42,29.67,0,1,False,True
20260724,34.19,1,31.18,0.21,29.39,-0.28,2,False,True
20260731,35.06,0.87,31.18,0,29.39,0,3,False,False
20260807,34.57,-0.49,31.71,0.53,29.92,0.53,4,False,True
20260814,34.62,0.05,32.06,0.35,29.39,-0.53,5,False,True
20260821,35.6,0.98,32.1,0.04,29.39,0,6,False,True
20260828,34.97,-0.63,32.18,0.08,29.95,0.56,7,False,True
20260904,34.83,-0.14,31.83,-0.35,30.04,0.09,8,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 5498 | 凱崴 | pattern | 型態觀察 | 48.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/01 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利總額48,387,137元(每股0.25元) 4.除權（息）交易日:115/09/17 5.最後過戶日:115/09/18 6.停止過戶起始日期:115/09/19 7.停止過戶截止日期:115/09/23 8.除權（息）基準日:115/09/23 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.現金股利發放日期:115/10/15 13.其他應敘明事項: 以上相關事宜，如經主管機關核示修正，或因應客觀環境之營運需要而須 變更或新訂時，授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 5498 | 凱崴 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/01 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利總額48,387,137元(每股0.25元) 4.除權（息）交易日:115/09/17 5.最後過戶日:115/09/18 6.停止過戶起始日期:115/09/19 7.停止過戶截止日期:115/09/23 8.除權（息）基準日:115/09/23 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.現金股利發放日期:115/10/15 13.其他應敘明事項: 以上相關事宜，如經主管機關核示修正，或因應客觀環境之營運需要而須 變更或新訂時，授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 5498 | 凱崴 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 5 | A_優先追蹤 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/09/01 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:現金股利總額48,387,137元(每股0.25元) 4.除權（息）交易日:115/09/17 5.最後過戶日:115/09/18 6.停止過戶起始日期:115/09/19 7.停止過戶截止日期:115/09/23 8.除權（息）基準日:115/09/23 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.現金股利發放日期:115/10/15 13.其他應敘明事項: 以上相關事宜，如經主管機關核示修正，或因應客觀環境之營運需要而須 變更或新訂時，授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 5498 | 凱崴 | 15 | 10 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
