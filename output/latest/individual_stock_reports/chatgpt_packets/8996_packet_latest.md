# INDIVIDUAL STOCK CHATGPT PACKET - 8996 高力

## Metadata
- generated_at: 2026-09-12 15:45:16 Asia/Taipei
- stock_id: 8996
- stock_name: 高力
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
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
- date: 20260911
- open: 1270
- high: 1365
- low: 1230
- close: 1330
- volume: 5053896
- ma5: 1288
- ema23_primary: 1221.34
- distance_to_ema23_pct: 8.9
- ma20: 1221
- ma60: 1204.78
- ma120: 1147.32
- return_5d: 2.31
- return_20d: 3.91
- volume_ratio: 1.21
- distance_to_ma20_pct_auxiliary: 8.93
- distance_to_high_60_pct: -20.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,1270,1290,1195,1215,2877863,1116.19,8.85,1040.55,1194.37,0.91
20260818,1265,1265,1165,1175,2317593,1121.09,4.81,1050.15,1194.45,0.73
20260819,1105,1155,1105,1135,2003400,1122.25,1.14,1052.9,1194.45,0.64
20260820,1180,1185,1090,1135,2441302,1123.31,1.04,1055.9,1192.62,0.79
20260821,1105,1125,1085,1090,1864549,1120.54,-2.73,1060.15,1190.53,0.6
20260824,1090,1195,1070,1145,3292497,1122.58,2,1067.65,1191.37,1.05
20260825,1120,1215,1120,1215,5250848,1130.28,7.5,1083.1,1193.45,1.6
20260826,1195,1210,1150,1195,3093732,1135.67,5.22,1099.9,1195.95,0.97
20260827,1210,1310,1190,1310,6206231,1150.2,13.89,1126.5,1200.28,1.88
20260828,1275,1300,1250,1265,4224888,1159.77,9.07,1147,1203.12,1.21
20260831,1240,1240,1140,1175,3492957,1161.03,1.2,1158.75,1204.03,0.97
20260901,1175,1200,1150,1175,2309421,1162.2,1.1,1166,1204.87,0.65
20260902,1165,1285,1155,1265,4591240,1170.77,8.05,1177.5,1205.78,1.33
20260903,1285,1310,1185,1185,4551450,1171.95,1.11,1180,1203.37,1.31
20260904,1255,1300,1170,1300,5561008,1182.62,9.93,1192.75,1204.7,1.58
20260907,1390,1410,1205,1240,8775069,1187.4,4.43,1201,1206.37,2.28
20260908,1240,1285,1205,1225,4527634,1190.54,2.89,1209,1207.7,1.13
20260909,1255,1345,1240,1345,6087009,1203.41,11.77,1217.75,1209.2,1.46
20260910,1320,1340,1280,1300,4932329,1211.46,7.31,1218.5,1207.87,1.17
20260911,1270,1365,1230,1330,5053896,1221.34,8.9,1221,1204.78,1.21
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 48.6
- over_600_ratio: 37.85
- over_800_ratio: 29.03
- over_1000_ratio: 24.03
- over_400_change_1w: 0.56
- over_800_change_1w: -3.34
- over_1000_change_1w: -2.39
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,51.78,-0.38,38.34,-1.04,34.56,3.02,4,False,True
20260703,51.66,-0.12,38.64,0.3,32.88,-1.68,5,False,True
20260709,51.47,-0.19,39.93,1.29,33.32,0.44,6,False,True
20260717,51.66,0.19,38.36,-1.57,34.57,1.25,7,False,True
20260724,51.09,-0.57,39.35,0.99,35.44,0.87,8,False,True
20260731,51.62,0.53,38.62,-0.73,36.81,1.37,9,False,True
20260807,50.57,-1.05,34.24,-4.38,32.43,-4.38,0,False,False
20260814,51.05,0.48,35.25,1.01,32.51,0.08,1,True,True
20260821,50.52,-0.53,36.48,1.23,30.86,-1.65,2,False,True
20260828,48.29,-2.23,33.7,-2.78,30.67,-0.19,0,False,False
20260904,48.04,-0.25,32.37,-1.33,26.42,-4.25,0,False,False
20260911,48.6,0.56,29.03,-3.34,24.03,-2.39,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8996 | 高力 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | stale_signal | 1.事實發生日:115/09/07 2.公司名稱:高力熱處理工業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報B4版報導 6.報導內容: 「高力表示，在AI浪潮下，…，第三季起可望逐步回升，維持全年三位數成長 的目標。」 7.發生緣由: (1)有關本公司財務及業務資訊，請以公開資訊觀測站公布之資料為準。 (2)本公司並未做任何財務預測之公布，特此澄清說明。 8.因應措施:本公司於今日接獲通知，公布重大訊息澄清報導。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 8996 | 高力 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/07 2.公司名稱:高力熱處理工業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報B4版報導 6.報導內容: 「高力表示，在AI浪潮下，…，第三季起可望逐步回升，維持全年三位數成長 的目標。」 7.發生緣由: (1)有關本公司財務及業務資訊，請以公開資訊觀測站公布之資料為準。 (2)本公司並未做任何財務預測之公布，特此澄清說明。 8.因應措施:本公司於今日接獲通知，公布重大訊息澄清報導。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 8996 | 高力 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/09/07 2.公司名稱:高力熱處理工業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.傳播媒體名稱:工商時報B4版報導 6.報導內容: 「高力表示，在AI浪潮下，…，第三季起可望逐步回升，維持全年三位數成長 的目標。」 7.發生緣由: (1)有關本公司財務及業務資訊，請以公開資訊觀測站公布之資料為準。 (2)本公司並未做任何財務預測之公布，特此澄清說明。 8.因應措施:本公司於今日接獲通知，公布重大訊息澄清報導。 9.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8996 | 高力 | 18 | 7 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
