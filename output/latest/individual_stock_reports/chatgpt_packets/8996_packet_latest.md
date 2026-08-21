# INDIVIDUAL STOCK CHATGPT PACKET - 8996 高力

## Metadata
- generated_at: 2026-08-21 22:28:29 Asia/Taipei
- stock_id: 8996
- stock_name: 高力
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8996_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8996_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8996.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8996.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8996.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8996.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8996_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8996_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8996_latest.md?ref=main

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
- date: 20260821
- open: 1105
- high: 1125
- low: 1085
- close: 1090
- volume: 1864549
- ma5: 1150
- ema23_primary: 1120.54
- distance_to_ema23_pct: -2.73
- ma20: 1060.15
- ma60: 1190.53
- ma120: 1098.31
- return_5d: -14.84
- return_20d: 8.46
- volume_ratio: 0.6
- distance_to_ma20_pct_auxiliary: 2.82
- distance_to_high_60_pct: -35.12

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,1055,1085,969,995,2480883,1171.73,-15.08,1226.7,1205.22,1.42
20260728,955,960,906,906,2221630,1149.59,-21.19,1198.25,1199.48,1.22
20260729,932,948,830,859,4770970,1125.37,-23.67,1163.7,1193.05,2.37
20260730,845,875,774,778,3831280,1096.42,-29.04,1124.85,1186.18,1.76
20260731,855,855,855,855,803625,1076.31,-20.56,1096.85,1181.02,0.37
20260803,889,940,888,940,1244282,1064.95,-11.73,1074.85,1178.77,0.58
20260804,1000,1030,990,1030,3449430,1062.04,-3.02,1055.1,1179.02,1.51
20260805,1050,1085,1030,1035,6155836,1059.78,-2.34,1040.1,1178.68,2.41
20260806,1055,1135,1040,1135,4365556,1066.05,6.47,1030.85,1180.02,1.64
20260807,1080,1135,1040,1045,4580949,1064.3,-1.81,1021.6,1180.35,1.64
20260810,1065,1110,1060,1075,2177049,1065.19,0.92,1013.35,1180.52,0.77
20260811,1060,1080,1045,1065,1153343,1065.17,-0.02,1007.85,1180.93,0.42
20260812,1070,1170,1065,1170,2782316,1073.91,8.95,1007.1,1183.02,0.98
20260813,1235,1285,1195,1285,3925113,1091.5,17.73,1015.1,1187.1,1.32
20260814,1325,1330,1245,1280,6188946,1107.21,15.61,1028.35,1191.87,1.93
20260817,1270,1290,1195,1215,2877863,1116.19,8.85,1040.55,1194.37,0.91
20260818,1265,1265,1165,1175,2317593,1121.09,4.81,1050.15,1194.45,0.73
20260819,1105,1155,1105,1135,2003400,1122.25,1.14,1052.9,1194.45,0.64
20260820,1180,1185,1090,1135,2441302,1123.31,1.04,1055.9,1192.62,0.79
20260821,1105,1125,1085,1090,1864549,1120.54,-2.73,1060.15,1190.53,0.6
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 51.05
- over_600_ratio: 40.96
- over_800_ratio: 35.25
- over_1000_ratio: 32.51
- over_400_change_1w: 0.48
- over_800_change_1w: 1.01
- over_1000_change_1w: 0.08
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,52.01,-1.54,34.81,-3.86,30.06,-4.06,0,False,False
20260605,52.11,0.1,35.65,0.84,30.79,0.73,1,True,True
20260612,52.25,0.14,39.07,3.42,31.46,0.67,2,True,True
20260618,52.16,-0.09,39.38,0.31,31.54,0.08,3,False,True
20260626,51.78,-0.38,38.34,-1.04,34.56,3.02,4,False,True
20260703,51.66,-0.12,38.64,0.3,32.88,-1.68,5,False,True
20260709,51.47,-0.19,39.93,1.29,33.32,0.44,6,False,True
20260717,51.66,0.19,38.36,-1.57,34.57,1.25,7,False,True
20260724,51.09,-0.57,39.35,0.99,35.44,0.87,8,False,True
20260731,51.62,0.53,38.62,-0.73,36.81,1.37,9,False,True
20260807,50.57,-1.05,34.24,-4.38,32.43,-4.38,0,False,False
20260814,51.05,0.48,35.25,1.01,32.51,0.08,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8996 | 高力 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/07/16 2.發生緣由:依證券櫃檯買賣中心通知辦理 3.公司債相關資訊: 高力四(89964)轉債相關資訊 到期日期：117/12/06 實際發行總額：新台幣1,000,000,000元整 本月發行餘額：新台幣27,800,000元整(截至115/07/15) 最新轉(交)換價格：232.2 轉換標的收市價格(8996)：1125.00(115/07/16) 轉債收市價格(89964)：516.00(115/07/16) 4.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 8996 | 高力 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/16 2.發生緣由:依證券櫃檯買賣中心通知辦理 3.公司債相關資訊: 高力四(89964)轉債相關資訊 到期日期：117/12/06 實際發行總額：新台幣1,000,000,000元整 本月發行餘額：新台幣27,800,000元整(截至115/07/15) 最新轉(交)換價格：232.2 轉換標的收市價格(8996)：1125.00(115/07/16) 轉債收市價格(89964)：516.00(115/07/16) 4.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 8996 | 高力 | revenue_breakout_low_response | 營收爆發低反應股 | 11 | 51 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.事實發生日:115/07/16 2.發生緣由:依證券櫃檯買賣中心通知辦理 3.公司債相關資訊: 高力四(89964)轉債相關資訊 到期日期：117/12/06 實際發行總額：新台幣1,000,000,000元整 本月發行餘額：新台幣27,800,000元整(截至115/07/15) 最新轉(交)換價格：232.2 轉換標的收市價格(8996)：1125.00(115/07/16) 轉債收市價格(89964)：516.00(115/07/16) 4.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8996 | 高力 | 4 | 4 | 4 | 8 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
