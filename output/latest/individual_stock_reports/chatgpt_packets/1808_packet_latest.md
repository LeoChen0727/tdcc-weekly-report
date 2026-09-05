# INDIVIDUAL STOCK CHATGPT PACKET - 1808 潤隆

## Metadata
- generated_at: 2026-09-05 22:15:41 Asia/Taipei
- stock_id: 1808
- stock_name: 潤隆
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 341
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 41
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1808_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1808_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1808_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1808_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1808.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1808.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1808.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1808.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1808_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1808_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1808_latest.md?ref=main

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
- date: 20260904
- open: 35.5
- high: 35.5
- low: 34.55
- close: 34.7
- volume: 1770833
- ma5: 34.98
- ema23_primary: 34.3
- distance_to_ema23_pct: 1.16
- ma20: 34.41
- ma60: 32.44
- ma120: 31.18
- return_5d: -0.29
- return_20d: 4.99
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: 0.84
- distance_to_high_60_pct: -8.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,32.95,33.5,32.5,33.35,1795207,32.04,4.07,32.16,30.93,1.2
20260811,33,33,32.05,32.45,2163855,32.08,1.16,32.24,30.98,1.39
20260812,32.45,32.9,32.25,32.75,856372,32.13,1.92,32.32,31.04,0.56
20260813,32.75,33.3,32.6,33.1,992260,32.21,2.75,32.37,31.11,0.67
20260814,33.05,33.1,32.65,32.65,702605,32.25,1.24,32.4,31.17,0.5
20260817,32.6,33.1,32.35,33,803021,32.31,2.12,32.45,31.23,0.58
20260818,32.75,33.2,32.6,32.85,516786,32.36,1.52,32.49,31.3,0.38
20260819,32.6,33.55,32.6,33.3,2331317,32.44,2.66,32.56,31.37,1.61
20260820,33.6,34.5,33.4,34.5,2685441,32.61,5.8,32.68,31.46,1.73
20260821,34.65,37.8,34.3,37,7419835,32.97,12.21,32.92,31.61,3.97
20260824,37.05,37.35,35.4,35.7,3635477,33.2,7.52,33.1,31.73,1.8
20260825,35.6,36.55,35,36.35,2131106,33.46,8.62,33.34,31.84,1.02
20260826,36.15,36.35,34.65,35.6,2830968,33.64,5.82,33.55,31.95,1.31
20260827,35.25,36.25,35.05,35.95,1644881,33.83,6.25,33.72,32.06,0.77
20260828,35.9,35.95,34.65,34.8,2527720,33.91,2.61,33.81,32.13,1.21
20260831,34.65,35,33.95,34.1,2545863,33.93,0.5,33.86,32.17,1.21
20260901,34,34.9,34,34.85,3335679,34.01,2.48,33.98,32.23,1.57
20260902,34.75,35.45,34.75,35.45,2109015,34.13,3.88,34.13,32.31,0.96
20260903,35.45,36.1,34.8,35.8,2500291,34.27,4.48,34.33,32.39,1.11
20260904,35.5,35.5,34.55,34.7,1770833,34.3,1.16,34.41,32.44,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 80.82
- over_600_ratio: 79.64
- over_800_ratio: 79.2
- over_1000_ratio: 78.8
- over_400_change_1w: -0.03
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,79.55,0.07,78.01,-0.11,77.7,-0.02,6,False,False
20260626,79.65,0.1,78.1,0.09,77.6,-0.1,7,False,True
20260703,79.51,-0.14,78.1,0,77.6,0,8,False,False
20260709,79.66,0.15,78.2,0.1,77.59,-0.01,9,False,True
20260717,79.95,0.29,78.29,0.09,77.77,0.18,10,True,True
20260724,80.18,0.23,78.49,0.2,78.08,0.31,11,True,True
20260731,80.4,0.22,78.7,0.21,78.19,0.11,12,True,True
20260807,80.22,-0.18,78.57,-0.13,78.16,-0.03,0,False,False
20260814,80.47,0.25,78.82,0.25,78.31,0.15,1,True,True
20260821,80.63,0.16,79.04,0.22,78.54,0.23,2,True,True
20260828,80.85,0.22,79.35,0.31,78.86,0.32,3,True,True
20260904,80.82,-0.03,79.2,-0.15,78.8,-0.06,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 1808 | 潤隆 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/08/10 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:  現金股利：新台幣1,339,547,615元（每股配發1.5元） 4.除權（息）交易日:115/09/23 5.最後過戶日:115/09/27 6.停止過戶起始日期:115/09/28 7.停止過戶截止日期:115/10/02 8.除權（息）基準日:115/10/02 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/10/30 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:   凡於除息基準日股東名冊記載之股東，可依其持股比例，享有配發現金股利之權利，   俟後如因法令變更或主管機關調整或本公司因買回、註銷、公司債股份轉換、發行新   股或其他影響股份變動原因，致影響流通在外股份數量，股東配息比率因而發生變動   時，董事長依流通在外普通股股數計算調整配息比率。；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d |
| 20260904 | 1808 | 潤隆 | revenue_pullback | 營收成長股價回檔 | 84.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/08/10 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:  現金股利：新台幣1,339,547,615元（每股配發1.5元） 4.除權（息）交易日:115/09/23 5.最後過戶日:115/09/27 6.停止過戶起始日期:115/09/28 7.停止過戶截止日期:115/10/02 8.除權（息）基準日:115/10/02 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/10/30 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:   凡於除息基準日股東名冊記載之股東，可依其持股比例，享有配發現金股利之權利，   俟後如因法令變更或主管機關調整或本公司因買回、註銷、公司債股份轉換、發行新   股或其他影響股份變動原因，致影響流通在外股份數量，股東配息比率因而發生變動   時，董事長依流通在外普通股股數計算調整配息比率。；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260904 | 1808 | 潤隆 | revenue_breakout_low_response | 營收爆發低反應股 | 20 | 26 | B_可觀察 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/08/10 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:  現金股利：新台幣1,339,547,615元（每股配發1.5元） 4.除權（息）交易日:115/09/23 5.最後過戶日:115/09/27 6.停止過戶起始日期:115/09/28 7.停止過戶截止日期:115/10/02 8.除權（息）基準日:115/10/02 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/10/30 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:   凡於除息基準日股東名冊記載之股東，可依其持股比例，享有配發現金股利之權利，   俟後如因法令變更或主管機關調整或本公司因買回、註銷、公司債股份轉換、發行新   股或其他影響股份變動原因，致影響流通在外股份數量，股東配息比率因而發生變動   時，董事長依流通在外普通股股數計算調整配息比率。；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 1808 | 潤隆 | 17 | 8 | 5 | 10 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
