# INDIVIDUAL STOCK CHATGPT PACKET - 3041 揚智

## Metadata
- generated_at: 2026-07-12 22:26:57 Asia/Taipei
- stock_id: 3041
- stock_name: 揚智
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3041_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3041_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3041_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3041_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3041_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3041_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3041_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3041.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3041.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3041.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3041.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3041_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3041_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3041_latest.md?ref=main

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
- date: 20260709
- open: 26.75
- high: 27.3
- low: 26.25
- close: 26.45
- volume: 1101412
- ma5: 27.41
- ema23_primary: 27.3
- distance_to_ema23_pct: -3.12
- ma20: 27.88
- ma60: 25.54
- ma120: 25
- return_5d: -6.54
- return_20d: 11.37
- volume_ratio: 0.27
- distance_to_ma20_pct_auxiliary: -5.14
- distance_to_high_60_pct: -18.62

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,24.5,24.9,23.2,24.25,1859312,24.65,-1.62,24.91,23.82,0.93
20260612,24.75,25.55,24.5,24.55,1831003,24.64,-0.37,24.98,23.83,0.91
20260615,24.95,27,24.95,27,5633383,24.84,8.71,25.15,23.89,2.51
20260616,28,28.3,26.4,26.4,5542209,24.97,5.74,25.33,23.93,2.24
20260617,26.4,29,26,29,5313504,25.3,14.61,25.6,24.02,1.99
20260618,29,29.8,28,28.15,13516089,25.54,10.22,25.77,24.09,4.2
20260622,29,30.95,29,30.95,7407056,25.99,19.08,25.95,24.22,2.23
20260623,32,32.5,30.55,31.2,11710657,26.43,18.07,26.16,24.35,3.16
20260624,30.5,32,29.8,30.85,5043562,26.79,15.14,26.39,24.48,1.31
20260625,31,31.15,29.25,29.25,3772109,27,8.34,26.55,24.59,0.96
20260626,28.7,28.9,27.15,27.3,2851145,27.02,1.02,26.65,24.67,0.72
20260629,27.4,27.75,26.7,26.8,1985892,27.01,-0.76,26.71,24.76,0.5
20260630,27.25,29.4,27.1,28.6,2667000,27.14,5.39,26.86,24.87,0.65
20260701,29.05,29.5,27.65,28,1970000,27.21,2.9,26.97,24.97,0.48
20260702,27.9,28.7,27.5,28.3,1249000,27.3,3.66,27.06,25.08,0.31
20260703,28.35,29.8,28.1,28.8,2314651,27.43,5.01,27.24,25.19,0.57
20260706,28.85,29.85,28.05,28.4,1614000,27.51,3.25,27.43,25.3,0.4
20260707,28.4,28.55,26.3,26.75,2075861,27.44,-2.53,27.6,25.39,0.51
20260708,26.75,27,26.05,26.65,1187961,27.38,-2.66,27.75,25.47,0.29
20260709,26.75,27.3,26.25,26.45,1101412,27.3,-3.12,27.88,25.54,0.27
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 27.5
- over_600_ratio: 25.84
- over_800_ratio: 23.81
- over_1000_ratio: 21.73
- over_400_change_1w: 0.12
- over_800_change_1w: -0.78
- over_1000_change_1w: -1.44
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,22.11,,20.51,,19.84,,0,False,False
20260508,22.87,0.76,20.64,0.13,20.64,0.8,1,True,True
20260515,22.95,0.08,20.52,-0.12,20.52,-0.12,2,False,False
20260522,24.6,1.65,21.62,1.1,20.92,0.4,3,True,True
20260529,25.64,1.04,23.05,1.43,22.34,1.42,4,True,True
20260605,25.25,-0.39,23.7,0.65,21.74,-0.6,5,False,True
20260612,23.65,-1.6,22.03,-1.67,21.32,-0.42,0,False,False
20260618,28.47,4.82,25.46,3.43,24.75,3.43,1,True,True
20260626,27.38,-1.09,24.59,-0.87,23.17,-1.58,0,False,False
20260703,27.5,0.12,23.81,-0.78,21.73,-1.44,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3041 | 揚智 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會決議日期或發生變動日期:115/07/08 2.人員別（請輸入董事長或總經理）:總經理 3.舊任者姓名:連建欽 4.舊任者簡歷:本公司總經理 5.新任者姓名:洪元忠 6.新任者簡歷:本公司業務副總經理 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「職務調整」、「資遣」、 「退休」、「逝世」或「新任」）:職務調整 8.異動原因:職務調整 9.新任生效日期:115/07/08 10.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3041 | 揚智 | 10 | 3 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
