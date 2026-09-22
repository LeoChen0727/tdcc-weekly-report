# INDIVIDUAL STOCK CHATGPT PACKET - 1455 集盛

## Metadata
- generated_at: 2026-09-20 22:15:44 Asia/Taipei
- stock_id: 1455
- stock_name: 集盛
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
- tdcc_rows: 43
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1455_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1455_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1455_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1455_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1455_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1455_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1455_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1455.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1455.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1455.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1455.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1455_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1455_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1455_latest.md?ref=main

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
- date: 20260918
- open: 9.92
- high: 9.95
- low: 9.74
- close: 9.95
- volume: 1004247
- ma5: 9.73
- ema23_primary: 9.82
- distance_to_ema23_pct: 1.33
- ma20: 9.92
- ma60: 9.63
- ma120: 9.22
- return_5d: 1.12
- return_20d: -1.49
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: 0.31
- distance_to_high_60_pct: -17.77

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,10.2,10.25,9.95,10,1502316,9.6,4.11,9.4,9.53,1.12
20260825,10,10.05,9.85,9.94,854286,9.63,3.19,9.45,9.55,0.63
20260826,9.99,10,9.87,9.99,637918,9.66,3.39,9.51,9.57,0.49
20260827,9.98,10.05,9.92,9.98,726285,9.69,3,9.58,9.58,0.56
20260828,10,10.05,9.97,9.97,901205,9.71,2.65,9.65,9.59,0.69
20260831,10,10.1,9.95,10,845296,9.74,2.71,9.72,9.6,0.63
20260901,10,10.6,10,10.25,3348017,9.78,4.81,9.8,9.62,2.27
20260902,10.3,10.3,10,10.15,1291807,9.81,3.46,9.87,9.63,0.85
20260903,10.2,10.4,9.97,9.97,1902317,9.82,1.49,9.92,9.63,1.21
20260904,10.1,10.1,9.93,9.96,891137,9.83,1.27,9.97,9.63,0.56
20260907,10.05,10.05,9.71,9.8,1674869,9.83,-0.32,9.96,9.63,1.18
20260908,9.8,9.9,9.73,9.9,933596,9.84,0.63,9.98,9.63,0.69
20260909,9.9,10.1,9.8,10,1128381,9.85,1.51,9.98,9.63,0.86
20260910,10,10,9.93,9.97,478826,9.86,1.1,9.98,9.63,0.38
20260911,9.93,9.96,9.76,9.84,1005983,9.86,-0.2,9.99,9.63,0.79
20260914,9.81,9.82,9.7,9.7,449168,9.85,-1.48,9.98,9.62,0.36
20260915,9.7,9.72,9.59,9.6,470308,9.83,-2.3,9.96,9.62,0.4
20260916,9.62,9.65,9.52,9.52,476524,9.8,-2.86,9.93,9.62,0.42
20260917,9.51,9.95,9.51,9.89,963403,9.81,0.84,9.93,9.62,0.85
20260918,9.92,9.95,9.74,9.95,1004247,9.82,1.33,9.92,9.63,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 67.22
- over_600_ratio: 65.25
- over_800_ratio: 64.49
- over_1000_ratio: 63.09
- over_400_change_1w: 0.14
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.4
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,67.26,0.09,64.99,0.2,63.8,0.22,2,False,True
20260709,66.45,-0.81,63.74,-1.25,62.89,-0.91,0,False,False
20260717,66.69,0.24,63.96,0.22,62.62,-0.27,1,False,True
20260724,66.8,0.11,64.03,0.07,62.7,0.08,2,False,True
20260731,66.99,0.19,64.24,0.21,62.7,0,3,False,True
20260807,66.91,-0.08,63.93,-0.31,62.91,0.21,4,False,True
20260814,66.93,0.02,64.15,0.22,62.97,0.06,5,False,True
20260821,67.1,0.17,64.45,0.3,63.11,0.14,6,True,True
20260828,67.02,-0.08,64.28,-0.17,63.25,0.14,7,False,True
20260904,67.04,0.02,64.19,-0.09,62.98,-0.27,8,False,False
20260911,67.08,0.04,64.52,0.33,63.49,0.51,9,True,True
20260918,67.22,0.14,64.49,-0.03,63.09,-0.4,10,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1455 | 集盛 | pattern | 型態觀察 | 46.0 |  |  | base_building |  |  | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/06/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:  ..........資本公積發放現金，新台幣85,070,140元 (每股配發0.16元) 4.除權（息）交易日:115/07/03 5.最後過戶日:115/07/06 6.停止過戶起始日期:115/07/07 7.停止過戶截止日期:115/07/11 8.除權（息）基準日:115/07/11 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/05 13.其他應敘明事項:   (1) 本次資本公積發放現金基準日前，如因法令變更、主管機關要求或流通在外       股份數量異動，致使股東配發現金比率發生變動而需修正時，本公司董事會       授權董事長全權處理之。   (2) 每位股東發放計算至元為止，元以下無條件捨去，並將捨去金額計入本公司       之其他收入，匯費或掛號費（支票寄發）由股東負擔，自發放金額中扣除，       若配發金額不足匯費或郵資時，將以平信郵寄支票方式發放。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1455 | 集盛 | 1 | 1 | 1 | 4 | 7 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

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
