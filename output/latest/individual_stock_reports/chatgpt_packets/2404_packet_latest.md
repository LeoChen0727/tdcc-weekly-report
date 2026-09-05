# INDIVIDUAL STOCK CHATGPT PACKET - 2404 漢唐

## Metadata
- generated_at: 2026-09-05 22:15:56 Asia/Taipei
- stock_id: 2404
- stock_name: 漢唐
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2404_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2404_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2404_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2404_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2404_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2404_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2404_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2404.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2404.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2404.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2404.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2404_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2404_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2404_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260904
- open: 1040
- high: 1085
- low: 1010
- close: 1070
- volume: 1780078
- ma5: 1058
- ema23_primary: 1090.08
- distance_to_ema23_pct: -1.84
- ma20: 1092.25
- ma60: 1174.75
- ma120: 1091.57
- return_5d: -0.47
- return_20d: -6.96
- volume_ratio: 1.3
- distance_to_ma20_pct_auxiliary: -2.04
- distance_to_high_60_pct: -26.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,1150,1180,1135,1150,1179125,1147.48,0.22,1133.75,1192.17,0.52
20260811,1170,1170,1140,1150,1119642,1147.69,0.2,1132,1194.67,0.5
20260812,1150,1170,1135,1135,1163103,1146.63,-1.01,1124.5,1196.83,0.55
20260813,1170,1175,1115,1130,2734052,1145.24,-1.33,1118.5,1198.5,1.31
20260814,1135,1140,1100,1125,1936765,1143.56,-1.62,1116.75,1200.17,0.96
20260817,1120,1165,1120,1155,1164508,1144.51,0.92,1117.75,1201.08,0.59
20260818,1150,1155,1110,1115,1191566,1142.05,-2.37,1116,1200.42,0.62
20260819,1090,1115,1075,1095,1111902,1138.13,-3.79,1112,1197.92,0.59
20260820,1115,1120,1060,1075,1621142,1132.87,-5.11,1107.5,1194.75,0.85
20260821,1075,1080,1050,1060,835869,1126.8,-5.93,1104.5,1191.83,0.45
20260824,1060,1075,1050,1065,596604,1121.65,-5.05,1102,1190.25,0.33
20260825,1060,1080,1055,1070,746264,1117.34,-4.24,1105,1188.83,0.43
20260826,1070,1100,1070,1080,687620,1114.23,-3.07,1108.25,1187.25,0.44
20260827,1090,1095,1065,1075,1452608,1110.96,-3.24,1111.5,1186,0.95
20260828,1080,1095,1070,1075,1240100,1107.97,-2.98,1110.25,1184.67,0.89
20260831,1065,1065,1035,1060,1469391,1103.97,-3.98,1108,1181.83,1.11
20260901,1060,1105,1060,1100,1513709,1103.64,-0.33,1107.5,1180.08,1.15
20260902,1085,1085,1025,1025,2371343,1097.08,-6.57,1103,1178.67,1.76
20260903,1030,1060,1025,1035,1457353,1091.91,-5.21,1096.25,1176.08,1.09
20260904,1040,1085,1010,1070,1780078,1090.08,-1.84,1092.25,1174.75,1.3
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 53.17
- over_600_ratio: 47.44
- over_800_ratio: 43.14
- over_1000_ratio: 38.97
- over_400_change_1w: -0.31
- over_800_change_1w: 0.62
- over_1000_change_1w: -0.76
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,53.39,1.06,43.64,1.16,39.46,1.13,2,True,True
20260626,53.22,-0.17,44.02,0.38,40.04,0.58,3,False,True
20260703,53.83,0.61,43.33,-0.69,39.25,-0.79,4,False,False
20260709,53.11,-0.72,42.82,-0.51,39.19,-0.06,0,False,False
20260717,54.44,1.33,43.7,0.88,40.44,1.25,1,True,True
20260724,54.39,-0.05,42.46,-1.24,41.09,0.65,2,False,True
20260731,54.39,0,44.02,1.56,40.79,-0.3,3,False,True
20260807,53.6,-0.79,43.69,-0.33,40.95,0.16,4,False,True
20260814,53.07,-0.53,43.44,-0.25,40.26,-0.69,0,False,False
20260821,53.41,0.34,42.83,-0.61,39.08,-1.18,1,False,False
20260828,53.48,0.07,42.52,-0.31,39.73,0.65,2,False,True
20260904,53.17,-0.31,43.14,0.62,38.97,-0.76,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2404 | 漢唐 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | call_inflow | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:每股配發現金股息40元 4.除權（息）交易日:115/07/16 5.最後過戶日:115/07/19 6.停止過戶起始日期:115/07/20 7.停止過戶截止日期:115/07/24 8.除權（息）基準日:115/07/24 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/14 13.其他應敘明事項:現金股利發放日為115/08/14(以支票或匯款方式發放)。凡持有本 公司股票而尚未辦理過戶之股東，因最後過戶日115年07月18,19日為假日，故請提前 115年07月17日(星期五)16時30分前親臨本公司股務代理機構：台新綜合證券股份 有限公司/股務代理部（地址：10489台北市中山區建國北路一段96號地下一樓, 電話:02-25048125），辦理過戶手續，掛號郵寄者以(民國 115年 7 月19日） (最後過戶日）郵戳日期為憑，以憑分派現金股利。 凡參加台灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務代理人 將依其送交之資料逕行辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2404 | 漢唐 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:每股配發現金股息40元 4.除權（息）交易日:115/07/16 5.最後過戶日:115/07/19 6.停止過戶起始日期:115/07/20 7.停止過戶截止日期:115/07/24 8.除權（息）基準日:115/07/24 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/14 13.其他應敘明事項:現金股利發放日為115/08/14(以支票或匯款方式發放)。凡持有本 公司股票而尚未辦理過戶之股東，因最後過戶日115年07月18,19日為假日，故請提前 115年07月17日(星期五)16時30分前親臨本公司股務代理機構：台新綜合證券股份 有限公司/股務代理部（地址：10489台北市中山區建國北路一段96號地下一樓, 電話:02-25048125），辦理過戶手續，掛號郵寄者以(民國 115年 7 月19日） (最後過戶日）郵戳日期為憑，以憑分派現金股利。 凡參加台灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務代理人 將依其送交之資料逕行辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2404 | 漢唐 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 53 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:每股配發現金股息40元 4.除權（息）交易日:115/07/16 5.最後過戶日:115/07/19 6.停止過戶起始日期:115/07/20 7.停止過戶截止日期:115/07/24 8.除權（息）基準日:115/07/24 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/14 13.其他應敘明事項:現金股利發放日為115/08/14(以支票或匯款方式發放)。凡持有本 公司股票而尚未辦理過戶之股東，因最後過戶日115年07月18,19日為假日，故請提前 115年07月17日(星期五)16時30分前親臨本公司股務代理機構：台新綜合證券股份 有限公司/股務代理部（地址：10489台北市中山區建國北路一段96號地下一樓, 電話:02-25048125），辦理過戶手續，掛號郵寄者以(民國 115年 7 月19日） (最後過戶日）郵戳日期為憑，以憑分派現金股利。 凡參加台灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務代理人 將依其送交之資料逕行辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2404 | 漢唐 | 2 | 2 | 4 | 6 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2404 | 漢唐 | 228 | 10 | 34976990.0 | 31730.0 | 1102.33 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
