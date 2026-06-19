# INDIVIDUAL STOCK CHATGPT PACKET - 1319 東陽

## Metadata
- generated_at: 2026-06-19 22:22:53 Asia/Taipei
- stock_id: 1319
- stock_name: 東陽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260612
- tdcc_rows: 29
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: 

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/1319_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/1319_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1319_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1319_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1319_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1319_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/1319_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/1319_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1319_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1319_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/1319_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/1319_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1319.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1319.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1319.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1319.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1319_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1319_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1319_latest.md?ref=main

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
- date: 20260618
- open: 102.5
- high: 104
- low: 98.9
- close: 99.2
- volume: 10059795
- ma5: 101.24
- ema23_primary: 94.54
- distance_to_ema23_pct: 4.93
- ma20: 94.45
- ma60: 84.24
- ma120: 91.25
- return_5d: -2.75
- return_20d: 23.85
- volume_ratio: 1.25
- distance_to_ma20_pct_auxiliary: 5.02
- distance_to_high_60_pct: -8.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,80.9,82.4,80.1,81.6,3108916,79.45,2.71,78.1,82.64,1.01
20260525,82.6,82.7,80.7,80.8,2980663,79.56,1.56,78.38,82.29,0.95
20260526,81.1,81.7,80,80.1,2164140,79.61,0.62,78.7,81.96,0.7
20260527,80.6,80.6,78.6,78.7,2749301,79.53,-1.04,78.86,81.61,0.88
20260528,86.5,86.5,86.5,86.5,4171274,80.11,7.97,79.44,81.42,1.32
20260529,95.1,95.1,91.8,95.1,11135579,81.36,16.89,80.45,81.42,3.14
20260601,91.1,92.6,86.9,87.5,18936391,81.87,6.87,81.08,81.35,4.34
20260602,87.8,93.9,87.8,92.1,14762947,82.72,11.33,81.86,81.32,3.02
20260603,93.4,96.5,91.6,94.3,14980041,83.69,12.68,82.81,81.34,2.77
20260604,94,97,92.6,96.5,8512601,84.76,13.86,83.64,81.49,1.54
20260605,96.8,98,94.3,97.9,8960487,85.85,14.03,84.52,81.67,1.57
20260608,93,97.8,93,97.8,8704441,86.85,12.61,85.37,81.81,1.45
20260609,98.3,105,97.2,105,10912887,88.36,18.83,86.62,82.1,1.71
20260610,103,108,102,107,10501382,89.91,19,87.97,82.45,1.54
20260611,107,108,99.9,102,9837282,90.92,12.19,89.11,82.74,1.37
20260612,101.5,103,99.5,99.5,4951777,91.64,8.58,90.16,82.98,0.68
20260615,101.5,105,100,105,5380191,92.75,13.21,91.41,83.33,0.72
20260616,105,105,99.6,100,4029888,93.35,7.12,92.41,83.63,0.53
20260617,101,103,99.7,102.5,3853522,94.12,8.91,93.5,83.95,0.5
20260618,102.5,104,98.9,99.2,10059795,94.54,4.93,94.45,84.24,1.25
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 85.63
- over_600_ratio: 83.66
- over_800_ratio: 82.74
- over_1000_ratio: 82.31
- over_400_change_1w: 1.63
- over_800_change_1w: 2.1
- over_1000_change_1w: 1.97
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260327,84.41,0.17,81.23,0.37,80.3,0.36,1,True,True
20260402,84.5,0.09,81.15,-0.08,80.22,-0.08,2,False,False
20260410,84.27,-0.23,80.97,-0.18,79.73,-0.49,0,False,False
20260417,83.76,-0.51,80.31,-0.66,79.53,-0.2,0,False,False
20260424,83.02,-0.74,79.91,-0.4,78.85,-0.68,0,False,False
20260430,82.91,-0.11,79.93,0.02,79.16,0.31,1,False,True
20260508,82.66,-0.25,79.31,-0.62,79.01,-0.15,0,False,False
20260515,82.67,0.01,79.73,0.42,79.43,0.42,1,True,True
20260522,82.84,0.17,80.01,0.28,79.71,0.28,2,True,True
20260529,82.82,-0.02,79.62,-0.39,79.17,-0.54,0,False,False
20260605,84,1.18,80.64,1.02,80.34,1.17,1,True,True
20260612,85.63,1.63,82.74,2.1,82.31,1.97,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1319 | 東陽 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | continued_2_3d | 1.發生變動日期:115/06/17 2.功能性委員會名稱:薪資報酬委員會 3.舊任者姓名:林幹雄、蔡明田、鄭雁玲 4.舊任者簡歷:林幹雄/開銘實業股份有限公司總經理、 蔡明田/成功大學工程管理學院工程管理碩士專班兼任教授、 鄭雁玲/就業情報資訊(股)公司職涯顧問 5.新任者姓名:尚未委任 6.新任者簡歷:尚未委任 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:薪資報酬委員會委員任期與董事會董事任期相同，配合董事會董事 任期屆滿解任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/29~115/06/18 10.新任生效日期:尚未委任 11.其他應敘明事項:新任委員待召開董事會重新委任後,另行公告；calendar event: ex_dividend on 20260622; status=confirmed; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1319 | 東陽 | 2 | 2 | 3 | 6 | 9 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1319 | 東陽 | 20 | 0 | 1092080.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
