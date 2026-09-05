# INDIVIDUAL STOCK CHATGPT PACKET - 3221 台嘉碩

## Metadata
- generated_at: 2026-09-05 22:16:27 Asia/Taipei
- stock_id: 3221
- stock_name: 台嘉碩
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3221_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3221_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3221_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3221_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3221_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3221_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3221_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3221.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3221.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3221.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3221.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3221_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3221_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3221_latest.md?ref=main

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
- open: 49.15
- high: 50.4
- low: 48.6
- close: 49.4
- volume: 1658000
- ma5: 49.52
- ema23_primary: 48.97
- distance_to_ema23_pct: 0.87
- ma20: 48.75
- ma60: 52.04
- ma120: 48.41
- return_5d: 1.23
- return_20d: 7.04
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 1.33
- distance_to_high_60_pct: -28.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,48.5,49.6,47.45,48.2,2153000,48.82,-1.26,47.38,54.06,0.57
20260811,48.5,50.2,48,48.25,2502000,48.77,-1.06,47.17,54.19,0.67
20260812,48.1,49.6,47.95,49,2131000,48.79,0.43,46.98,54.26,0.57
20260813,49.3,52,49.3,49.35,4624000,48.84,1.05,46.73,54.33,1.31
20260814,50,50.1,47.2,47.45,2137000,48.72,-2.61,46.66,54.32,0.61
20260817,48.4,49.5,47.45,48.85,1962000,48.73,0.24,46.8,54.28,0.57
20260818,48.6,48.85,46.25,46.5,1550000,48.54,-4.21,46.8,54.12,0.45
20260819,45,48.5,45,47.85,1892000,48.49,-1.31,46.84,53.91,0.56
20260820,49.1,49.8,47,48.15,2018000,48.46,-0.64,46.99,53.73,0.59
20260821,47.9,51.3,47.9,48.85,7204000,48.49,0.74,46.97,53.6,2.03
20260824,48.6,49,47.6,47.6,1434000,48.42,-1.69,46.83,53.39,0.46
20260825,47.1,49.45,46.05,49.3,1974000,48.49,1.67,46.99,53.21,0.65
20260826,50.1,50.9,49.5,50,3199000,48.62,2.85,47.37,53.09,1.06
20260827,50.4,50.9,49.2,49.25,2010000,48.67,1.19,47.82,52.95,0.69
20260828,49.6,50.8,48.8,48.8,1550000,48.68,0.25,48.05,52.79,0.54
20260831,48,49.1,47.25,47.85,905000,48.61,-1.57,48.17,52.67,0.33
20260901,48.05,52,48.05,51.3,4083000,48.84,5.05,48.38,52.57,1.58
20260902,50.3,52.1,50,51,4214000,49.02,4.05,48.55,52.45,1.6
20260903,51,51.3,48,48.05,2423000,48.94,-1.81,48.59,52.19,0.91
20260904,49.15,50.4,48.6,49.4,1658000,48.97,0.87,48.75,52.04,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 24.87
- over_600_ratio: 19.8
- over_800_ratio: 13.24
- over_1000_ratio: 9.11
- over_400_change_1w: -1.23
- over_800_change_1w: -0.86
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,26.2,-1.6,14.14,0.22,10.86,1.13,1,False,True
20260626,25.43,-0.77,13.81,-0.33,9.61,-1.25,0,False,False
20260703,30.76,5.33,15.12,1.31,11.06,1.45,1,True,True
20260709,26.48,-4.28,13.86,-1.26,10.58,-0.48,0,False,False
20260717,24.89,-1.59,12.82,-1.04,9.54,-1.04,0,False,False
20260724,23.93,-0.96,12.77,-0.05,9.49,-0.05,0,False,False
20260731,23.65,-0.28,12.77,0,9.49,0,0,False,False
20260807,24.13,0.48,12.77,0,9.49,0,1,False,False
20260814,24.28,0.15,12.8,0.03,9.52,0.03,2,True,True
20260821,24.9,0.62,13.33,0.53,9.12,-0.4,3,False,True
20260828,26.1,1.2,14.1,0.77,9.1,-0.02,4,False,True
20260904,24.87,-1.23,13.24,-0.86,9.11,0.01,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3221 | 台嘉碩 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 盈餘分配之現金股利NT$8,308,969元(每股配發新台幣0.08元) 資本公積發放之現金NT$20,772,422元(每股配發新台幣0.2元) 3.變更後發放股利種類及金額: 盈餘分配之現金股利NT$8,308,969元(每股配發新台幣0.07914117 元) 資本公積發放之現金NT$20,772,422元(每股配發新台幣0.19785292元) 4.變更原因: 本公司因限制員工權利新股收回註銷股份致流通在外之股數變動為104,989,210股， 經115年05月26日董事會決議授權董事長依相關法令辦理調整配息率。 5.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 3221 | 台嘉碩 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: 盈餘分配之現金股利NT$8,308,969元(每股配發新台幣0.08元) 資本公積發放之現金NT$20,772,422元(每股配發新台幣0.2元) 3.變更後發放股利種類及金額: 盈餘分配之現金股利NT$8,308,969元(每股配發新台幣0.07914117 元) 資本公積發放之現金NT$20,772,422元(每股配發新台幣0.19785292元) 4.變更原因: 本公司因限制員工權利新股收回註銷股份致流通在外之股數變動為104,989,210股， 經115年05月26日董事會決議授權董事長依相關法令辦理調整配息率。 5.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3221 | 台嘉碩 | 4 | 4 | 4 | 9 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
