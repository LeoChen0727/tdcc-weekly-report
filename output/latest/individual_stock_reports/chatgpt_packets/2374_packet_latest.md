# INDIVIDUAL STOCK CHATGPT PACKET - 2374 佳能

## Metadata
- generated_at: 2026-08-22 15:59:45 Asia/Taipei
- stock_id: 2374
- stock_name: 佳能
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2374_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2374_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2374_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2374_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2374_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2374_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2374_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2374.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2374.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2374.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2374.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2374_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2374_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2374_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
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
- open: 68.2
- high: 69.1
- low: 67.8
- close: 68.5
- volume: 4136830
- ma5: 68.54
- ema23_primary: 69.26
- distance_to_ema23_pct: -1.1
- ma20: 68.04
- ma60: 72.51
- ma120: 73.43
- return_5d: -2.84
- return_20d: 1.48
- volume_ratio: 1.38
- distance_to_ma20_pct_auxiliary: 0.68
- distance_to_high_60_pct: -20.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,68.5,69.5,67.5,68.1,3852334,71.62,-4.91,72.09,76.57,0.98
20260728,65.3,66.1,63.8,63.9,3670244,70.98,-9.97,71.64,76.33,0.95
20260729,64.5,65.3,59.6,62.6,5034138,70.28,-10.92,71.02,76,1.27
20260730,62,62.8,59,59.6,3098746,69.39,-14.11,70.33,75.64,0.79
20260731,63.5,65.3,62.8,63.9,2998247,68.93,-7.3,69.67,75.39,0.84
20260803,64.1,67.5,64.1,67.3,3563169,68.79,-2.17,69.18,75.18,1
20260804,66.5,67.8,66.3,67.4,2336799,68.68,-1.86,68.68,75,0.68
20260805,68.6,69.7,68.1,69.3,3202837,68.73,0.83,68.41,74.81,0.95
20260806,69.5,70,68.6,69.6,2143220,68.8,1.16,68.14,74.6,0.63
20260807,71.1,71.5,69.4,70,3509122,68.9,1.59,67.89,74.43,1.02
20260810,70.6,72.8,69.7,72.4,4334880,69.19,4.63,67.73,74.3,1.3
20260811,72.6,73,71.1,71.1,3589722,69.35,2.52,67.67,74.12,1.11
20260812,71.3,72.1,71.2,71.5,2217576,69.53,2.83,67.61,73.94,0.68
20260813,72,72.5,70.9,70.9,2078358,69.65,1.8,67.55,73.78,0.65
20260814,71.2,71.4,70.4,70.5,2006128,69.72,1.12,67.69,73.65,0.67
20260817,70.5,72.2,70.5,70.9,2376701,69.82,1.55,67.97,73.49,0.82
20260818,71.1,71.2,69.3,69.3,2515816,69.77,-0.68,68.08,73.25,0.86
20260819,66.3,68.4,66.3,66.9,1850802,69.53,-3.79,68.04,72.97,0.63
20260820,67.3,68.1,66.6,67.1,1295775,69.33,-3.22,67.99,72.72,0.45
20260821,68.2,69.1,67.8,68.5,4136830,69.26,-1.1,68.04,72.51,1.38
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 27.03
- over_600_ratio: 25.39
- over_800_ratio: 23.91
- over_1000_ratio: 22.61
- over_400_change_1w: -0.64
- over_800_change_1w: -0.73
- over_1000_change_1w: -0.73
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,30.51,0,26.61,-0.27,25.01,-0.51,0,False,False
20260612,28.02,-2.49,25.06,-1.55,23.73,-1.28,0,False,False
20260618,28.44,0.42,25.06,0,23.49,-0.24,1,False,False
20260626,28.18,-0.26,25.22,0.16,23.09,-0.4,2,False,True
20260703,28.05,-0.13,24.17,-1.05,22.26,-0.83,0,False,False
20260709,27.74,-0.31,24.11,-0.06,23.02,0.76,1,False,True
20260717,27.52,-0.22,24.18,0.07,23.1,0.08,2,False,True
20260724,27.78,0.26,24.66,0.48,23.37,0.27,3,False,True
20260731,27.34,-0.44,24.3,-0.36,22.45,-0.92,0,False,False
20260807,27.56,0.22,24.81,0.51,23.22,0.77,1,True,True
20260814,27.67,0.11,24.64,-0.17,23.34,0.12,2,False,True
20260821,27.03,-0.64,23.91,-0.73,22.61,-0.73,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2374 | 佳能 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.股東會決議日:115/06/25 2.許可從事競業行為之董事姓名及職稱: 董事：董俊仁(佳美投資股份有限公司代表人) 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司。 4.許可從事競業行為之期間:任職本公司董事之職務期間。 5.決議情形（請依公司法第209條說明表決結果）: 表決時出席股東表決權數183,090,559權，贊成權數180,560,083權，占總權數98.61%； 本案依票決方式表決通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用。 7.所擔任該大陸地區事業之公司名稱及職務:不適用。 8.所擔任該大陸地區事業地址:不適用。 9.所擔任該大陸地區事業營業項目:不適用。 10.對本公司財務業務之影響程度:無。 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用。 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2374 | 佳能 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.股東會決議日:115/06/25 2.許可從事競業行為之董事姓名及職稱: 董事：董俊仁(佳美投資股份有限公司代表人) 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司。 4.許可從事競業行為之期間:任職本公司董事之職務期間。 5.決議情形（請依公司法第209條說明表決結果）: 表決時出席股東表決權數183,090,559權，贊成權數180,560,083權，占總權數98.61%； 本案依票決方式表決通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用。 7.所擔任該大陸地區事業之公司名稱及職務:不適用。 8.所擔任該大陸地區事業地址:不適用。 9.所擔任該大陸地區事業營業項目:不適用。 10.對本公司財務業務之影響程度:無。 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用。 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 2374 | 佳能 | revenue_breakout_low_response | 營收爆發低反應股 | 13 | 43 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.股東會決議日:115/06/25 2.許可從事競業行為之董事姓名及職稱: 董事：董俊仁(佳美投資股份有限公司代表人) 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司。 4.許可從事競業行為之期間:任職本公司董事之職務期間。 5.決議情形（請依公司法第209條說明表決結果）: 表決時出席股東表決權數183,090,559權，贊成權數180,560,083權，占總權數98.61%； 本案依票決方式表決通過。 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用。 7.所擔任該大陸地區事業之公司名稱及職務:不適用。 8.所擔任該大陸地區事業地址:不適用。 9.所擔任該大陸地區事業營業項目:不適用。 10.對本公司財務業務之影響程度:無。 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用。 12.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2374 | 佳能 | 4 | 4 | 4 | 4 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2374 | 佳能 | 60 | 0 | 744820.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
