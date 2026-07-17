# INDIVIDUAL STOCK CHATGPT PACKET - 3003 健和興

## Metadata
- generated_at: 2026-07-17 22:26:42 Asia/Taipei
- stock_id: 3003
- stock_name: 健和興
- packet_status: standard_180d_window_packet
- latest_price_date: 20260716
- price_rows: 305
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3003_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3003_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3003_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3003_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3003_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3003_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3003_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3003.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3003.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3003.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3003.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3003_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3003_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3003_latest.md?ref=main

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
- date: 20260716
- open: 63.9
- high: 67.8
- low: 63.5
- close: 66
- volume: 1487336
- ma5: 64.26
- ema23_primary: 65.06
- distance_to_ema23_pct: 1.44
- ma20: 66.37
- ma60: 61.87
- ma120: 55.87
- return_5d: -0.9
- return_20d: -2.08
- volume_ratio: 1.07
- distance_to_ma20_pct_auxiliary: -0.56
- distance_to_high_60_pct: -7.43

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260617,67.4,67.8,66.4,67,3580906,62.66,6.93,63.2,57.09,1.79
20260618,67.4,71.3,67.2,69.9,4157767,63.26,10.49,63.66,57.44,1.93
20260622,70.3,70.3,67.6,68.5,2419321,63.7,7.54,63.99,57.74,1.1
20260623,69,69.3,67.4,68.5,1593596,64.1,6.87,64.37,58.04,0.73
20260624,67.7,70.4,67.4,70.2,2109435,64.61,8.66,64.75,58.36,0.95
20260625,71.1,71.1,68,68.6,1499314,64.94,5.64,65.03,58.67,0.71
20260626,68.1,68.2,65.7,65.7,1558944,65,1.07,65.2,58.94,0.75
20260629,66.3,67.6,64.8,65.6,904723,65.05,0.84,65.35,59.23,0.44
20260630,66.2,66.5,65.4,66.4,587059,65.17,1.89,65.56,59.5,0.29
20260701,67.2,67.4,65.8,65.9,592964,65.23,1.03,65.77,59.78,0.29
20260702,65.4,66.2,65.3,65.5,607977,65.25,0.38,65.92,60.05,0.3
20260703,64.7,65.4,63.7,65.3,768220,65.25,0.07,66.06,60.31,0.38
20260706,65.7,67.3,65.7,66.3,656619,65.34,1.47,66.22,60.57,0.33
20260707,67.3,69,66.1,66.1,1415179,65.4,1.06,66.48,60.84,0.71
20260708,67.1,67.4,65.1,66.6,921935,65.5,1.67,66.6,61.06,0.47
20260709,67.2,67.2,65.9,66.1,512440,65.55,0.83,66.7,61.25,0.28
20260713,67.2,67.2,63.4,64.1,937847,65.43,-2.04,66.56,61.43,0.53
20260714,63,64.2,60.3,62,1108741,65.15,-4.83,66.46,61.55,0.67
20260715,62.4,63.1,61.5,63.1,504853,64.98,-2.89,66.44,61.69,0.32
20260716,63.9,67.8,63.5,66,1487336,65.06,1.44,66.37,61.87,1.07
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 57.79
- over_600_ratio: 55.53
- over_800_ratio: 51.87
- over_1000_ratio: 51.34
- over_400_change_1w: 0.04
- over_800_change_1w: -0.34
- over_1000_change_1w: 0.19
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.01,,51.64,,50.57,,0,False,False
20260508,57.48,0.47,51.68,0.04,50.6,0.03,1,True,True
20260515,57.46,-0.02,51.87,0.19,50.73,0.13,2,False,True
20260522,57.65,0.19,51.91,0.04,50.85,0.12,3,True,True
20260529,57,-0.65,52.07,0.16,50.94,0.09,4,False,True
20260605,57.21,0.21,52.08,0.01,50.91,-0.03,5,False,True
20260612,57.18,-0.03,51.81,-0.27,50.76,-0.15,6,False,False
20260618,57.58,0.4,51.41,-0.4,50.88,0.12,7,False,True
20260626,57.75,0.17,52.21,0.8,51.15,0.27,8,True,True
20260703,57.79,0.04,51.87,-0.34,51.34,0.19,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260716 | 3003 | 健和興 | pattern | 型態觀察 | 54.0 |  |  | pullback_right_side |  | call_inflow | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/07/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額: (1)現金股利新台幣155,654,890元整。 4.除權（息）交易日:115/08/06 5.最後過戶日:115/08/07 6.停止過戶起始日期:115/08/08 7.停止過戶截止日期:115/08/12 8.除權（息）基準日:115/08/12 9.債券最後申請轉換日期:無。 10.債券停止轉換起始日期:無。 11.債券停止轉換截止日期:無。 12.普通股現金股利發放日期:115/08/26 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:無。 15.外幣現金股利發放對象:無。 16.外幣現金股利匯率決定方式:無。 17.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |
| 20260716 | 3003 | 健和興 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/07/16 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額: (1)現金股利新台幣155,654,890元整。 4.除權（息）交易日:115/08/06 5.最後過戶日:115/08/07 6.停止過戶起始日期:115/08/08 7.停止過戶截止日期:115/08/12 8.除權（息）基準日:115/08/12 9.債券最後申請轉換日期:無。 10.債券停止轉換起始日期:無。 11.債券停止轉換截止日期:無。 12.普通股現金股利發放日期:115/08/26 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:無。 15.外幣現金股利發放對象:無。 16.外幣現金股利匯率決定方式:無。 17.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260716 | 3003 | 健和興 | 1 | 1 | 2 | 3 | 10 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 10 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260716 | 3003 | 健和興 | 5 | 0 | 1318990.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
