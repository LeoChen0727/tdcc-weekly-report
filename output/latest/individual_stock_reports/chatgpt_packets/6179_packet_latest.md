# INDIVIDUAL STOCK CHATGPT PACKET - 6179 亞通

## Metadata
- generated_at: 2026-08-23 22:28:42 Asia/Taipei
- stock_id: 6179
- stock_name: 亞通
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6179_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6179_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6179_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6179_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6179.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6179.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6179.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6179.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6179_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6179_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6179_latest.md?ref=main

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
- open: 26.8
- high: 27.6
- low: 26.5
- close: 27.2
- volume: 1649000
- ma5: 27.11
- ema23_primary: 26.54
- distance_to_ema23_pct: 2.47
- ma20: 26.16
- ma60: 25.72
- ma120: 25.4
- return_5d: 0.55
- return_20d: 10.12
- volume_ratio: 1.06
- distance_to_ma20_pct_auxiliary: 3.97
- distance_to_high_60_pct: -7.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,24.7,25,24.15,24.35,484000,25.77,-5.51,26.23,25.12,0.27
20260728,23.9,24.15,23.5,24,922000,25.62,-6.34,26.14,25.12,0.52
20260729,24,24.2,22.4,23.1,1927000,25.41,-9.1,26.02,25.11,1.06
20260730,23.1,23.45,22.75,22.85,595000,25.2,-9.32,25.85,25.09,0.34
20260731,23.5,24.6,23.4,24.25,775000,25.12,-3.47,25.75,25.1,0.45
20260803,24.1,25.1,23.95,24.65,659000,25.08,-1.72,25.66,25.11,0.39
20260804,24.65,25.9,24.5,25.8,1221000,25.14,2.62,25.54,25.14,0.81
20260805,26.15,28.15,26.1,27.65,4146000,25.35,9.07,25.57,25.19,2.6
20260806,27.7,27.7,26,26.35,1740000,25.43,3.6,25.55,25.23,1.07
20260807,26.2,27.4,26.15,27.05,1179000,25.57,5.79,25.51,25.28,0.78
20260810,27.1,28.1,27.1,27.9,2417000,25.76,8.3,25.51,25.35,1.74
20260811,28,28,27.5,27.5,894000,25.91,6.15,25.5,25.4,0.67
20260812,27.6,27.85,27.3,27.35,929000,26.03,5.08,25.48,25.44,0.7
20260813,27.55,28.1,27.3,27.85,1753000,26.18,6.38,25.52,25.5,1.3
20260814,27.45,27.6,26.65,27.05,1450000,26.25,3.04,25.63,25.54,1.16
20260817,28,29.3,27.65,27.75,5003000,26.38,5.21,25.81,25.57,3.52
20260818,27.95,28.05,27.05,27.3,1613000,26.45,3.2,25.93,25.6,1.09
20260819,26.6,27.2,26.6,26.85,781000,26.49,1.37,26,25.63,0.53
20260820,27.15,27.45,26.4,26.45,850000,26.48,-0.13,26.04,25.67,0.57
20260821,26.8,27.6,26.5,27.2,1649000,26.54,2.47,26.16,25.72,1.06
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 40.99
- over_600_ratio: 37.04
- over_800_ratio: 33.91
- over_1000_ratio: 31.35
- over_400_change_1w: -0.94
- over_800_change_1w: -1.54
- over_1000_change_1w: -2.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,38.67,-0.61,31.63,-0.59,28.55,-0.99,0,False,False
20260612,38.24,-0.43,30.64,-0.99,28.54,-0.01,1,False,False
20260618,40.11,1.87,32.07,1.43,29.54,1,2,True,True
20260626,41.79,1.68,33.76,1.69,30.65,1.11,3,True,True
20260703,41.9,0.11,33.86,0.1,31.28,0.63,4,True,True
20260709,42.16,0.26,34.4,0.54,32.8,1.52,5,True,True
20260717,41.8,-0.36,33.6,-0.8,31.56,-1.24,0,False,False
20260724,41.2,-0.6,32.97,-0.63,30.91,-0.65,0,False,False
20260731,40.92,-0.28,33.9,0.93,30.26,-0.65,1,False,True
20260807,41.82,0.9,34.51,0.61,31.98,1.72,2,True,True
20260814,41.93,0.11,35.45,0.94,33.38,1.4,3,True,True
20260821,40.99,-0.94,33.91,-1.54,31.35,-2.03,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6179 | 亞通 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/06/26 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放股東現金每股0.5元(總額新台幣88,662,325元)；發放方式為   (1)資本公積發放現金新台幣88,662,325元 4.除權（息）交易日:115/08/14 5.最後過戶日:115/08/17 6.停止過戶起始日期:115/08/18 7.停止過戶截止日期:115/08/22 8.除權（息）基準日:115/08/22 9.債券最後申請轉換日期:115/07/24 10.債券停止轉換起始日期:115/07/28 11.債券停止轉換截止日期:115/08/22 12.普通股現金股利發放日期:115/09/10 13.其他應敘明事項:配合本公司第三次無擔保轉換公司債到期相關作業，   爰依董事會授權，調整除息基準日及相關作業時程，以維護投資人權益。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 6179 | 亞通 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/06/26 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放股東現金每股0.5元(總額新台幣88,662,325元)；發放方式為   (1)資本公積發放現金新台幣88,662,325元 4.除權（息）交易日:115/08/14 5.最後過戶日:115/08/17 6.停止過戶起始日期:115/08/18 7.停止過戶截止日期:115/08/22 8.除權（息）基準日:115/08/22 9.債券最後申請轉換日期:115/07/24 10.債券停止轉換起始日期:115/07/28 11.債券停止轉換截止日期:115/08/22 12.普通股現金股利發放日期:115/09/10 13.其他應敘明事項:配合本公司第三次無擔保轉換公司債到期相關作業，   爰依董事會授權，調整除息基準日及相關作業時程，以維護投資人權益。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 6179 | 亞通 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 27 | B_可觀察 |  |  |  | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/06/26 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:   發放股東現金每股0.5元(總額新台幣88,662,325元)；發放方式為   (1)資本公積發放現金新台幣88,662,325元 4.除權（息）交易日:115/08/14 5.最後過戶日:115/08/17 6.停止過戶起始日期:115/08/18 7.停止過戶截止日期:115/08/22 8.除權（息）基準日:115/08/22 9.債券最後申請轉換日期:115/07/24 10.債券停止轉換起始日期:115/07/28 11.債券停止轉換截止日期:115/08/22 12.普通股現金股利發放日期:115/09/10 13.其他應敘明事項:配合本公司第三次無擔保轉換公司債到期相關作業，   爰依董事會授權，調整除息基準日及相關作業時程，以維護投資人權益。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6179 | 亞通 | 1 | 1 | 3 | 7 | 15 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 15 次，但尚未有效突破，需等待攻擊確認。 |

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
