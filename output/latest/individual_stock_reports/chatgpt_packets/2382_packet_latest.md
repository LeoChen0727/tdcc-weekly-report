# INDIVIDUAL STOCK CHATGPT PACKET - 2382 廣達

## Metadata
- generated_at: 2026-07-08 22:26:42 Asia/Taipei
- stock_id: 2382
- stock_name: 廣達
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 300
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2382_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2382_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2382_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2382_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2382_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2382_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2382_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2382.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2382.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2382.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2382.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2382_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2382_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2382_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260708
- open: 376
- high: 380.5
- low: 367
- close: 377
- volume: 15636669
- ma5: 374.8
- ema23_primary: 368.5
- distance_to_ema23_pct: 2.31
- ma20: 371.95
- ma60: 346.82
- ma120: 316.62
- return_5d: 1.34
- return_20d: 0.53
- volume_ratio: 0.78
- distance_to_ma20_pct_auxiliary: 1.36
- distance_to_high_60_pct: -13.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,370,380.5,363.5,380.5,46184781,353.06,7.77,342.68,321.64,0.78
20260611,373.5,385,359,370,48409395,354.47,4.38,344.45,322.99,0.8
20260612,378,384,372,372,24305308,355.93,4.51,347.75,324.38,0.42
20260615,381.5,386.5,368,370,22408965,357.1,3.61,351.25,325.66,0.39
20260616,371.5,372.5,362,362.5,20112630,357.55,1.38,354.88,326.93,0.35
20260617,361,374,358,374,21858689,358.92,4.2,359.07,328.43,0.39
20260618,374.5,379.5,372.5,376,22566584,360.35,4.34,362.48,330.03,0.41
20260622,378.5,385,376.5,380,20023542,361.99,4.98,365.68,331.68,0.37
20260623,381,381,368,372.5,16362886,362.86,2.66,368.48,333.13,0.31
20260624,367,372,364.5,372,11120601,363.62,2.3,371.25,334.55,0.22
20260625,375,375,365,366.5,13596942,363.86,0.72,373.98,335.84,0.27
20260626,362,372,357,362,20757530,363.71,-0.47,376.65,337.19,0.43
20260629,368,372,363,367,11562314,363.98,0.83,378.05,338.67,0.26
20260630,371,371.5,365.5,368,10784000,364.32,1.01,377.82,339.96,0.26
20260701,373.5,376.5,368.5,372,13594000,364.96,1.93,376.4,341.42,0.39
20260702,366,372,365.5,369,8737000,365.29,1.01,374,342.75,0.3
20260703,369,378,368.5,377,13135151,366.27,2.93,372.65,343.91,0.5
20260706,381.5,393,378,378,23761000,367.25,2.93,372.02,344.99,0.98
20260707,374.5,380,372.5,373,15592266,367.73,1.43,371.85,345.85,0.72
20260708,376,380.5,367,377,15636669,368.5,2.31,371.95,346.82,0.78
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 85.44
- over_600_ratio: 84
- over_800_ratio: 82.8
- over_1000_ratio: 81.48
- over_400_change_1w: 0.11
- over_800_change_1w: 0.24
- over_1000_change_1w: 0.21
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.93,,83.29,,81.96,,0,False,False
20260508,86.08,0.15,83.52,0.23,82.11,0.15,1,True,True
20260515,86.17,0.09,83.49,-0.03,82.02,-0.09,2,False,False
20260522,85.21,-0.96,82.63,-0.86,81.18,-0.84,0,False,False
20260529,84.84,-0.37,82.16,-0.47,80.72,-0.46,0,False,False
20260605,85.79,0.95,83.03,0.87,81.77,1.05,1,True,True
20260612,85.52,-0.27,82.76,-0.27,81.44,-0.33,0,False,False
20260618,85.38,-0.14,82.72,-0.04,81.4,-0.04,0,False,False
20260626,85.33,-0.05,82.56,-0.16,81.27,-0.13,0,False,False
20260703,85.44,0.11,82.8,0.24,81.48,0.21,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 2382 | 廣達 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期: 115/07/02 2.除權、息類別（請填入「除權」、「除息」或「除權息」）: 除息 3.普通股發放股利種類及金額:  (1) 普通股-現金股利：每股配發現金股利15.6元；金額 60,256,987,940元  (2) 普通股-股票股利：0 4.除權（息）交易日:115/07/16 5.最後過戶日: 115/07/17 6.停止過戶起始日期: 115/07/18 7.停止過戶截止日期: 115/07/22 8.除權（息）基準日: 115/07/22 9.債券最後申請轉換日期: 不適用 10.債券停止轉換起始日期: 不適用 11.債券停止轉換截止日期: 不適用 12.普通股現金股利發放日期: 115/08/28 13.其他應敘明事項:  依115年02月26日董事會決議，現金股利配發基準日、停止過戶日、發放日  及本公司海外第四次無擔保轉換公司債停止轉換期間、調整現金股利配息率等  相關事宜，授權董事長全權處理之；calendar event: ex_dividend on 20260716; status=confirmed; proximity=within_14d |
| 20260708 | 2382 | 廣達 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期: 115/07/02 2.除權、息類別（請填入「除權」、「除息」或「除權息」）: 除息 3.普通股發放股利種類及金額:  (1) 普通股-現金股利：每股配發現金股利15.6元；金額 60,256,987,940元  (2) 普通股-股票股利：0 4.除權（息）交易日:115/07/16 5.最後過戶日: 115/07/17 6.停止過戶起始日期: 115/07/18 7.停止過戶截止日期: 115/07/22 8.除權（息）基準日: 115/07/22 9.債券最後申請轉換日期: 不適用 10.債券停止轉換起始日期: 不適用 11.債券停止轉換截止日期: 不適用 12.普通股現金股利發放日期: 115/08/28 13.其他應敘明事項:  依115年02月26日董事會決議，現金股利配發基準日、停止過戶日、發放日  及本公司海外第四次無擔保轉換公司債停止轉換期間、調整現金股利配息率等  相關事宜，授權董事長全權處理之；calendar event: ex_dividend on 20260716; status=confirmed; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260708 | 2382 | 廣達 | revenue_breakout_low_response | 營收爆發低反應股 | 19.0 | 4.0 | A_優先追蹤 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期: 115/07/02 2.除權、息類別（請填入「除權」、「除息」或「除權息」）: 除息 3.普通股發放股利種類及金額:  (1) 普通股-現金股利：每股配發現金股利15.6元；金額 60,256,987,940元  (2) 普通股-股票股利：0 4.除權（息）交易日:115/07/16 5.最後過戶日: 115/07/17 6.停止過戶起始日期: 115/07/18 7.停止過戶截止日期: 115/07/22 8.除權（息）基準日: 115/07/22 9.債券最後申請轉換日期: 不適用 10.債券停止轉換起始日期: 不適用 11.債券停止轉換截止日期: 不適用 12.普通股現金股利發放日期: 115/08/28 13.其他應敘明事項:  依115年02月26日董事會決議，現金股利配發基準日、停止過戶日、發放日  及本公司海外第四次無擔保轉換公司債停止轉換期間、調整現金股利配息率等  相關事宜，授權董事長全權處理之；calendar event: ex_dividend on 20260716; status=confirmed; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 2382 | 廣達 | 18 | 12 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
