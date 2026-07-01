# INDIVIDUAL STOCK CHATGPT PACKET - 2882 國泰金

## Metadata
- generated_at: 2026-07-01 22:27:25 Asia/Taipei
- stock_id: 2882
- stock_name: 國泰金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 295
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2882_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2882_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2882_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2882_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2882_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2882_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2882_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2882.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2882.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2882.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2882.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2882_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2882_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2882_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260701
- open: 100
- high: 101
- low: 94.3
- close: 95
- volume: 78426000
- ma5: 102.46
- ema23_primary: 100.49
- distance_to_ema23_pct: -5.47
- ma20: 103.87
- ma60: 86.39
- ma120: 80.58
- return_5d: -13.64
- return_20d: 6.5
- volume_ratio: 1.54
- distance_to_ma20_pct_auxiliary: -8.54
- distance_to_high_60_pct: -19.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,89.9,92.5,89.2,91.8,57367426,81.95,12.02,81.31,75.96,1.27
20260604,96.3,96.3,91.8,94.4,54014109,82.99,13.75,82.08,76.36,1.15
20260605,94.4,100,93.7,100,69269147,84.41,18.47,83.08,76.85,1.43
20260608,97.8,97.8,94,95,57020304,85.29,11.39,83.92,77.23,1.14
20260609,95.3,104,95.3,104,55872704,86.85,19.75,85.3,77.76,1.1
20260610,102,102.5,99.4,99.9,42154420,87.94,13.61,86.42,78.23,0.82
20260611,101,101.5,97.7,100.5,36086504,88.98,12.94,87.61,78.7,0.7
20260612,102,105.5,99.7,100.5,32131390,89.94,11.74,88.75,79.15,0.64
20260615,105,105.5,103,104,25382726,91.11,14.14,90.11,79.66,0.5
20260616,104.5,109.5,104,109.5,54388852,92.65,18.19,91.69,80.29,1.07
20260617,110,117,108,113.5,49607947,94.38,20.25,93.47,80.98,0.96
20260618,115,117.5,114,115.5,48383199,96.14,20.13,95.31,81.72,0.93
20260622,117,117.5,112,113,34442840,97.55,15.84,96.97,82.42,0.66
20260623,113,116.5,113,113.5,29407198,98.88,14.79,98.58,83.12,0.58
20260624,110.5,114,110,110,34364951,99.8,10.22,99.92,83.77,0.69
20260625,110,113,109,111.5,29350842,100.78,10.64,101.22,84.45,0.61
20260626,110.5,111.5,105,106,57625079,101.21,4.73,102.28,85.05,1.21
20260629,105,105.5,100.5,101.5,68446464,101.24,0.26,103.08,85.57,1.44
20260630,96.8,99,94.4,98.3,102686000,100.99,-2.67,103.58,86.01,2.06
20260701,100,101,94.3,95,78426000,100.49,-5.47,103.87,86.39,1.54
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 85.87
- over_600_ratio: 84.85
- over_800_ratio: 84.17
- over_1000_ratio: 83.55
- over_400_change_1w: 0.01
- over_800_change_1w: 0.02
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,85.28,,83.42,,82.78,,0,False,False
20260508,85.29,0.01,83.42,0,82.8,0.02,1,False,True
20260515,85.26,-0.03,83.41,-0.01,82.8,0,0,False,False
20260522,85.32,0.06,83.52,0.11,82.91,0.11,1,True,True
20260529,85.47,0.15,83.67,0.15,83.04,0.13,2,True,True
20260605,85.58,0.11,83.84,0.17,83.22,0.18,3,True,True
20260612,85.77,0.19,84.06,0.22,83.43,0.21,4,True,True
20260618,85.86,0.09,84.15,0.09,83.55,0.12,5,True,True
20260626,85.87,0.01,84.17,0.02,83.55,0,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2882 | 國泰金 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.董事會、股東會決議或公司決定日期:115/06/30 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放股利種類及金額:本公司114年度盈餘分派案，業經115年6月29日董事會 （代行股東會）通過，分配現金股利新台幣5,000,000,000元。 4.除權（息）交易日:115/07/07 5.最後過戶日:115/07/08 6.停止過戶起始日期:115/07/09 7.停止過戶截止日期:115/07/13 8.除權（息）基準日:115/07/13 9.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2882 | 國泰金 | 6 | 5 | 5 | 8 | 14 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 2882 | 國泰金 | 41 | 2 | 5986850.0 | 743820.0 | 8.05 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
