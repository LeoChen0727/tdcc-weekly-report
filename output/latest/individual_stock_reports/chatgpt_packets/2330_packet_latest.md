# INDIVIDUAL STOCK CHATGPT PACKET - 2330 台積電

## Metadata
- generated_at: 2026-07-14 22:26:31 Asia/Taipei
- stock_id: 2330
- stock_name: 台積電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260713
- price_rows: 302
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: True
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2330_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2330_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2330.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2330.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2330.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2330.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2330_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2330_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2330_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260713
- open: 2460
- high: 2480
- low: 2440
- close: 2440
- volume: 35310380
- ma5: 2444
- ema23_primary: 2404.5
- distance_to_ema23_pct: 1.48
- ma20: 2420.75
- ma60: 2299.92
- ma120: 2070.54
- return_5d: -0.2
- return_20d: 8.44
- volume_ratio: 0.96
- distance_to_ma20_pct_auxiliary: 0.8
- distance_to_high_60_pct: -3.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260612,2325,2325,2290,2310,26306885,2284.01,1.14,2298.5,2128.42,0.62
20260615,2360,2375,2345,2375,30228535,2291.59,3.64,2305.25,2136.25,0.72
20260616,2375,2400,2350,2400,37145708,2300.63,4.32,2315,2145.42,0.89
20260617,2355,2385,2350,2385,30059393,2307.66,3.35,2325,2154.5,0.73
20260618,2395,2415,2385,2410,49982610,2316.19,4.05,2334,2164.5,1.18
20260622,2455,2510,2455,2510,45207883,2332.34,7.62,2346.75,2176.17,1.04
20260623,2510,2535,2490,2490,39537895,2345.47,6.16,2355.75,2186.92,0.9
20260624,2435,2445,2390,2390,67304477,2349.19,1.74,2361.75,2196.08,1.48
20260625,2410,2420,2390,2390,41099957,2352.59,1.59,2366.25,2205.58,0.9
20260626,2360,2370,2325,2340,53800344,2351.54,-0.49,2368.5,2214.92,1.16
20260629,2330,2395,2330,2370,38133782,2353.08,0.72,2369.25,2225.08,0.89
20260630,2440,2475,2410,2410,42817000,2357.82,2.21,2372,2234.33,1.02
20260701,2495,2505,2475,2505,30361000,2370.08,5.69,2378.25,2245.92,0.73
20260702,2450,2480,2445,2465,27140000,2377.99,3.66,2380.25,2256,0.66
20260703,2415,2465,2415,2445,32905868,2383.58,2.58,2383.25,2264.25,0.8
20260706,2465,2500,2455,2460,19209000,2389.95,2.93,2388,2272.67,0.48
20260707,2480,2500,2440,2440,30367854,2394.12,1.92,2395.25,2280,0.78
20260708,2445,2465,2420,2465,25519599,2400.02,2.71,2403.25,2287.92,0.66
20260709,2450,2460,2415,2415,34681018,2401.27,0.57,2411.25,2293.92,0.93
20260713,2460,2480,2440,2440,35310380,2404.5,1.48,2420.75,2299.92,0.96
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 87.81
- over_600_ratio: 86.76
- over_800_ratio: 85.82
- over_1000_ratio: 85.09
- over_400_change_1w: -0.02
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.32,,86.35,,85.58,,0,False,False
20260508,88.28,-0.04,86.32,-0.03,85.58,0,0,False,False
20260515,88.18,-0.1,86.21,-0.11,85.47,-0.11,0,False,False
20260522,88.1,-0.08,86.11,-0.1,85.39,-0.08,0,False,False
20260529,88.12,0.02,86.14,0.03,85.41,0.02,1,True,True
20260605,88.12,0,86.14,0,85.42,0.01,2,False,True
20260612,87.89,-0.23,85.94,-0.2,85.18,-0.24,0,False,False
20260618,87.92,0.03,85.98,0.04,85.22,0.04,1,True,True
20260626,87.83,-0.09,85.84,-0.14,85.11,-0.11,0,False,False
20260703,87.81,-0.02,85.82,-0.02,85.09,-0.02,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 2330 | 台積電 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | mixed_flow | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/07/16 1.召開法人說明會之日期：115/07/16 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：台北文華東方酒店B2 文華廳（台北市松山區敦化北路158號） 4.法人說明會擇要訊息：(1)公布本公司2026年第2季財務報告及2026年第3季業績展望。(2)參加方式：請參見https://investor.tsmc.com/chinese/quarterly-results/2026/q2 5.其他應敘明事項：無。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |
| 20260713 | 2330 | 台積電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | mixed_flow | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/07/16 1.召開法人說明會之日期：115/07/16 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：台北文華東方酒店B2 文華廳（台北市松山區敦化北路158號） 4.法人說明會擇要訊息：(1)公布本公司2026年第2季財務報告及2026年第3季業績展望。(2)參加方式：請參見https://investor.tsmc.com/chinese/quarterly-results/2026/q2 5.其他應敘明事項：無。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260713 | 2330 | 台積電 | revenue_breakout_low_response | 營收爆發低反應股 | 17.0 | 23.0 | D_降級_TDCC轉弱 |  |  | mixed_flow | stale_signal | 符合條款第四條第XX款：12 事實發生日：115/07/16 1.召開法人說明會之日期：115/07/16 2.召開法人說明會之時間：14 時 00 分  3.召開法人說明會之地點：台北文華東方酒店B2 文華廳（台北市松山區敦化北路158號） 4.法人說明會擇要訊息：(1)公布本公司2026年第2季財務報告及2026年第3季業績展望。(2)參加方式：請參見https://investor.tsmc.com/chinese/quarterly-results/2026/q2 5.其他應敘明事項：無。 完整財務業務資訊請至公開資訊觀測站之法人說明會一覽表或法說會項目下查閱。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 2330 | 台積電 | 25 | 8 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 2330 | 台積電 | 928 | 189 | 163263700.0 | 1832770.0 | 89.08 | mixed_flow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
