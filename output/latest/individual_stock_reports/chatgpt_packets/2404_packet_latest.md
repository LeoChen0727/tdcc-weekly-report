# INDIVIDUAL STOCK CHATGPT PACKET - 2404 漢唐

## Metadata
- generated_at: 2026-09-26 22:16:20 Asia/Taipei
- stock_id: 2404
- stock_name: 漢唐
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
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
- action_rating_display_zh: 停利
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260924
- open: 1255
- high: 1285
- low: 1205
- close: 1285
- volume: 2827024
- ma5: 1186
- ema23_primary: 1108.68
- distance_to_ema23_pct: 15.9
- ma20: 1083.75
- ma60: 1127.33
- ma120: 1114.37
- return_5d: 24.76
- return_20d: 19.53
- volume_ratio: 1.7
- distance_to_ma20_pct_auxiliary: 18.57
- distance_to_high_60_pct: -7.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,1080,1095,1070,1075,1240100,1107.97,-2.98,1110.25,1184.67,0.89
20260831,1065,1065,1035,1060,1469391,1103.97,-3.98,1108,1181.83,1.11
20260901,1060,1105,1060,1100,1513709,1103.64,-0.33,1107.5,1180.08,1.15
20260902,1085,1085,1025,1025,2371343,1097.08,-6.57,1103,1178.67,1.76
20260903,1030,1060,1025,1035,1457353,1091.91,-5.21,1096.25,1176.08,1.09
20260904,1040,1085,1010,1070,1780078,1090.08,-1.84,1092.25,1174.75,1.3
20260907,1070,1085,1060,1080,951408,1089.24,-0.85,1088.75,1172.83,0.7
20260908,1085,1085,1050,1055,651640,1086.39,-2.89,1084,1168.58,0.49
20260909,1055,1080,1055,1065,1187583,1084.61,-1.81,1080.5,1163.33,0.89
20260910,1055,1065,1040,1060,674867,1082.56,-2.08,1077,1160.25,0.55
20260911,1025,1040,1000,1005,1637345,1076.09,-6.61,1071,1155.67,1.35
20260914,995,1040,992,1015,976489,1071,-5.23,1064,1151.5,0.81
20260915,1015,1050,1015,1035,965057,1068,-3.09,1060,1147.42,0.81
20260916,1040,1060,1030,1035,746369,1065.25,-2.84,1057,1143.67,0.63
20260917,1040,1055,1025,1030,636296,1062.32,-3.04,1054.75,1139.92,0.56
20260918,1040,1130,1040,1125,3305776,1067.54,5.38,1058,1135.92,2.64
20260921,1125,1160,1090,1130,2092541,1072.74,5.34,1061.25,1132.42,1.58
20260922,1140,1175,1130,1140,1655529,1078.35,5.72,1064.75,1128.75,1.21
20260923,1160,1250,1140,1250,5162606,1092.65,14.4,1073.25,1127.58,3.23
20260924,1255,1285,1205,1285,2827024,1108.68,15.9,1083.75,1127.33,1.7
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 55.52
- over_600_ratio: 50.25
- over_800_ratio: 45.49
- over_1000_ratio: 40.82
- over_400_change_1w: 1.94
- over_800_change_1w: 1.16
- over_1000_change_1w: 1.65
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,53.11,-0.72,42.82,-0.51,39.19,-0.06,0,False,False
20260717,54.44,1.33,43.7,0.88,40.44,1.25,1,True,True
20260724,54.39,-0.05,42.46,-1.24,41.09,0.65,2,False,True
20260731,54.39,0,44.02,1.56,40.79,-0.3,3,False,True
20260807,53.6,-0.79,43.69,-0.33,40.95,0.16,4,False,True
20260814,53.07,-0.53,43.44,-0.25,40.26,-0.69,0,False,False
20260821,53.41,0.34,42.83,-0.61,39.08,-1.18,1,False,False
20260828,53.48,0.07,42.52,-0.31,39.73,0.65,2,False,True
20260904,53.17,-0.31,43.14,0.62,38.97,-0.76,3,False,True
20260911,53.37,0.2,44.31,1.17,38.67,-0.3,4,False,True
20260918,53.58,0.21,44.33,0.02,39.17,0.5,5,True,True
20260924,55.52,1.94,45.49,1.16,40.82,1.65,6,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2404 | 漢唐 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | call_inflow | continued_overheated | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:每股配發現金股息40元 4.除權（息）交易日:115/07/16 5.最後過戶日:115/07/19 6.停止過戶起始日期:115/07/20 7.停止過戶截止日期:115/07/24 8.除權（息）基準日:115/07/24 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/14 13.其他應敘明事項:現金股利發放日為115/08/14(以支票或匯款方式發放)。凡持有本 公司股票而尚未辦理過戶之股東，因最後過戶日115年07月18,19日為假日，故請提前 115年07月17日(星期五)16時30分前親臨本公司股務代理機構：台新綜合證券股份 有限公司/股務代理部（地址：10489台北市中山區建國北路一段96號地下一樓, 電話:02-25048125），辦理過戶手續，掛號郵寄者以(民國 115年 7 月19日） (最後過戶日）郵戳日期為憑，以憑分派現金股利。 凡參加台灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務代理人 將依其送交之資料逕行辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2404 | 漢唐 | 5 | 5 | 5 | 7 | 13 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2404 | 漢唐 | 240 | 13 | 63831680.0 | 9200.0 | 6938.23 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
