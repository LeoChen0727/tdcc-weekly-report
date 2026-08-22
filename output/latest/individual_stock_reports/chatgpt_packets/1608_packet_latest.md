# INDIVIDUAL STOCK CHATGPT PACKET - 1608 華榮

## Metadata
- generated_at: 2026-08-22 22:26:34 Asia/Taipei
- stock_id: 1608
- stock_name: 華榮
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1608_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1608_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1608_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1608_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1608_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1608_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1608_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1608.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1608.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1608.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1608.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1608_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1608_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1608_latest.md?ref=main

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
- open: 35.8
- high: 36.05
- low: 35.55
- close: 35.85
- volume: 2057475
- ma5: 35.69
- ema23_primary: 34.43
- distance_to_ema23_pct: 4.11
- ma20: 33.61
- ma60: 33.85
- ma120: 33.46
- return_5d: -3.11
- return_20d: 19.5
- volume_ratio: 0.32
- distance_to_ma20_pct_auxiliary: 6.66
- distance_to_high_60_pct: -9.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,30.3,30.3,28.95,29.5,1914939,32.45,-9.1,32.78,33.62,0.69
20260728,29,29.25,28.3,28.3,2275192,32.11,-11.86,32.55,33.55,0.81
20260729,28.55,28.6,26.85,27.55,3353291,31.73,-13.17,32.24,33.45,1.17
20260730,27.5,27.75,26.7,26.95,1443282,31.33,-13.98,31.91,33.34,0.51
20260731,28.2,29.5,28.2,29.35,2752611,31.16,-5.82,31.68,33.28,0.96
20260803,29.2,31.4,29.1,31.15,3557170,31.16,-0.04,31.5,33.23,1.25
20260804,34.25,34.25,34.25,34.25,5652537,31.42,9,31.44,33.23,2.06
20260805,33.95,35.5,33.25,33.4,22414576,31.59,5.74,31.39,33.22,6.1
20260806,34.5,35.4,34,34.4,9789218,31.82,8.11,31.41,33.23,2.41
20260807,34.5,35.8,34.5,34.95,8807920,32.08,8.94,31.45,33.25,1.99
20260810,35,36.15,34.7,35.75,9423837,32.39,10.38,31.56,33.3,1.97
20260811,35.95,37,35.8,36.45,8146839,32.73,11.38,31.75,33.38,1.63
20260812,36.3,39.2,36.3,37.95,19567525,33.16,14.44,31.97,33.48,3.33
20260813,37.95,37.95,36.6,36.8,10071318,33.46,9.97,32.15,33.57,1.6
20260814,36.8,37.35,36.6,37,4753650,33.76,9.6,32.38,33.66,0.75
20260817,36.95,37,36.05,36.35,4006303,33.97,6.99,32.63,33.72,0.63
20260818,36.35,36.45,35.25,35.45,3197293,34.1,3.97,32.81,33.76,0.5
20260819,34.95,35.55,34.5,35.3,2810934,34.2,3.22,33.05,33.78,0.44
20260820,35.7,35.9,35.35,35.5,1778592,34.31,3.48,33.32,33.81,0.28
20260821,35.8,36.05,35.55,35.85,2057475,34.43,4.11,33.61,33.85,0.32
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 65.37
- over_600_ratio: 64.14
- over_800_ratio: 63.36
- over_1000_ratio: 62.12
- over_400_change_1w: -0.19
- over_800_change_1w: -0.1
- over_1000_change_1w: -0.35
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,66.36,1.84,63.81,1.49,62.71,2.34,5,True,True
20260612,64.61,-1.75,61.84,-1.97,60.59,-2.12,0,False,False
20260618,64.78,0.17,62.58,0.74,61.02,0.43,1,True,True
20260626,64.47,-0.31,61.94,-0.64,60.67,-0.35,0,False,False
20260703,64.1,-0.37,62.06,0.12,60.95,0.28,1,False,True
20260709,64.28,0.18,61.84,-0.22,60.43,-0.52,2,False,False
20260717,63.87,-0.41,61.71,-0.13,60.58,0.15,3,False,True
20260724,63.33,-0.54,61.47,-0.24,60.37,-0.21,0,False,False
20260731,63.3,-0.03,61.05,-0.42,60.23,-0.14,0,False,False
20260807,63.55,0.25,61.57,0.52,60.6,0.37,1,True,True
20260814,65.56,2.01,63.46,1.89,62.47,1.87,2,True,True
20260821,65.37,-0.19,63.36,-0.1,62.12,-0.35,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1608 | 華榮 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.股東會決議日:115/06/17 2.許可從事競業行為之董事姓名及職稱:  董事/第一伸銅科技股份有限公司代表人:王宏仁 3.許可從事競業行為之項目:經營其他與本公司營業範圍相同之公司及擔任  董事或經理人之行為。 4.許可從事競業行為之期間:擔任本公司董事期間。 5.決議情形（請依公司法第209條說明表決結果）:  本議案經已發行股份總數二分之一以上股東出席，出席股東表決權三分之  二以上同意照案通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用。 7.所擔任該大陸地區事業之公司名稱及職務:不適用。 8.所擔任該大陸地區事業地址:不適用。 9.所擔任該大陸地區事業營業項目:不適用。 10.對本公司財務業務之影響程度:無。 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用。 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 1608 | 華榮 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.股東會決議日:115/06/17 2.許可從事競業行為之董事姓名及職稱:  董事/第一伸銅科技股份有限公司代表人:王宏仁 3.許可從事競業行為之項目:經營其他與本公司營業範圍相同之公司及擔任  董事或經理人之行為。 4.許可從事競業行為之期間:擔任本公司董事期間。 5.決議情形（請依公司法第209條說明表決結果）:  本議案經已發行股份總數二分之一以上股東出席，出席股東表決權三分之  二以上同意照案通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用。 7.所擔任該大陸地區事業之公司名稱及職務:不適用。 8.所擔任該大陸地區事業地址:不適用。 9.所擔任該大陸地區事業營業項目:不適用。 10.對本公司財務業務之影響程度:無。 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用。 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1608 | 華榮 | 4 | 2 | 4 | 4 | 6 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1608 | 華榮 | 12 | 0 | 99250.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
