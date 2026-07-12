# INDIVIDUAL STOCK CHATGPT PACKET - 2404 漢唐

## Metadata
- generated_at: 2026-07-12 22:26:39 Asia/Taipei
- stock_id: 2404
- stock_name: 漢唐
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
- date: 20260709
- open: 1220
- high: 1245
- low: 1200
- close: 1215
- volume: 2001376
- ma5: 1269
- ema23_primary: 1262.44
- distance_to_ema23_pct: -3.76
- ma20: 1294.25
- ma60: 1139.58
- ma120: 1056.12
- return_5d: -12.27
- return_20d: 5.65
- volume_ratio: 0.55
- distance_to_ma20_pct_auxiliary: -6.12
- distance_to_high_60_pct: -16.21

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,1185,1230,1140,1195,4892552,1132.16,5.55,1146.75,1012.23,0.97
20260612,1280,1310,1265,1310,6101859,1146.98,14.21,1162.25,1018.58,1.21
20260615,1380,1430,1360,1380,5578755,1166.4,18.31,1181,1025.95,1.09
20260616,1380,1380,1245,1245,6617233,1172.95,6.14,1191.75,1031.45,1.26
20260617,1225,1295,1225,1280,4750890,1181.87,8.3,1204.5,1037.28,0.91
20260618,1295,1305,1245,1265,3238724,1188.8,6.41,1212.75,1043.12,0.65
20260622,1275,1285,1255,1280,1898021,1196.4,6.99,1219,1048.87,0.39
20260623,1290,1315,1255,1260,2277495,1201.7,4.85,1219.75,1054.15,0.49
20260624,1245,1265,1220,1255,1838096,1206.14,4.05,1219.25,1059.98,0.42
20260625,1265,1380,1240,1365,5934949,1219.38,11.94,1225.75,1068.07,1.34
20260626,1350,1395,1310,1340,4491931,1229.43,8.99,1234.75,1076.47,1.02
20260629,1380,1450,1350,1360,4708422,1240.31,9.65,1245,1085.45,1.05
20260630,1370,1380,1310,1320,2737000,1246.95,5.86,1252.25,1093.55,0.61
20260701,1340,1375,1285,1300,4001000,1251.37,3.89,1259.75,1101.4,0.89
20260702,1295,1390,1285,1385,3464000,1262.51,9.7,1271.25,1110.23,0.78
20260703,1375,1395,1345,1350,1761969,1269.8,6.32,1277.25,1117.67,0.42
20260706,1350,1350,1285,1320,2239000,1273.98,3.61,1283,1124.55,0.56
20260707,1320,1320,1250,1260,2305710,1272.82,-1.01,1290.5,1130.12,0.6
20260708,1265,1275,1180,1200,2328711,1266.75,-5.27,1291,1134.58,0.62
20260709,1220,1245,1200,1215,2001376,1262.44,-3.76,1294.25,1139.58,0.55
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 53.83
- over_600_ratio: 49.21
- over_800_ratio: 43.33
- over_1000_ratio: 39.25
- over_400_change_1w: 0.61
- over_800_change_1w: -0.69
- over_1000_change_1w: -0.79
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.45,,40.52,,37.38,,0,False,False
20260508,48.57,-0.88,39.4,-1.12,35.8,-1.58,0,False,False
20260515,49.12,0.55,38.43,-0.97,36.13,0.33,1,False,True
20260522,51.12,2,40.53,2.1,37.25,1.12,2,True,True
20260529,53.82,2.7,43.84,3.31,39.69,2.44,3,True,True
20260605,52.45,-1.37,42.33,-1.51,37.26,-2.43,0,False,False
20260612,52.33,-0.12,42.48,0.15,38.33,1.07,1,False,True
20260618,53.39,1.06,43.64,1.16,39.46,1.13,2,True,True
20260626,53.22,-0.17,44.02,0.38,40.04,0.58,3,False,True
20260703,53.83,0.61,43.33,-0.69,39.25,-0.79,4,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2404 | 漢唐 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  | call_inflow | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:每股配發現金股息40元 4.除權（息）交易日:115/07/16 5.最後過戶日:115/07/19 6.停止過戶起始日期:115/07/20 7.停止過戶截止日期:115/07/24 8.除權（息）基準日:115/07/24 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/14 13.其他應敘明事項:現金股利發放日為115/08/14(以支票或匯款方式發放)。凡持有本 公司股票而尚未辦理過戶之股東，因最後過戶日115年07月18,19日為假日，故請提前 115年07月17日(星期五)16時30分前親臨本公司股務代理機構：台新綜合證券股份 有限公司/股務代理部（地址：10489台北市中山區建國北路一段96號地下一樓, 電話:02-25048125），辦理過戶手續，掛號郵寄者以(民國 115年 7 月19日） (最後過戶日）郵戳日期為憑，以憑分派現金股利。 凡參加台灣集中保管結算所股份有限公司進行集中辦理過戶者，本公司股務代理人 將依其送交之資料逕行辦理過戶手續。；calendar event: ex_dividend on 20260716; status=confirmed; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2404 | 漢唐 | 13 | 4 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2404 | 漢唐 | 235 | 9 | 26659680.0 | 304640.0 | 87.51 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
