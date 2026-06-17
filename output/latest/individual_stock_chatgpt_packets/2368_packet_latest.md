# INDIVIDUAL STOCK CHATGPT PACKET - 2368 金像電

## Metadata
- generated_at: 2026-06-17 22:23:13 Asia/Taipei
- stock_id: 2368
- stock_name: 金像電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260617
- price_rows: 283
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/2368_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/2368_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2368_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2368_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2368_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2368_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/2368_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/2368_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2368_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2368_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/2368_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/2368_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2368.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2368.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2368.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2368.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2368_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2368_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2368_latest.md?ref=main

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
- risk_control_zh: TDCC 歷史不足
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足

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
- insufficient_tdcc_history

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260617
- open: 1345
- high: 1375
- low: 1340
- close: 1370
- volume: 3261807
- ma5: 1340
- ema23_primary: 1326.85
- distance_to_ema23_pct: 3.25
- ma20: 1326.5
- ma60: 1223.13
- ma120: 968.53
- return_5d: 4.18
- return_20d: 6.2
- volume_ratio: 0.54
- distance_to_ma20_pct_auxiliary: 3.28
- distance_to_high_60_pct: -9.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260518,1220,1270,1215,1250,7982652,1300.01,-3.85,1357.75,1064,1.28
20260519,1260,1325,1245,1285,6451905,1298.76,-1.06,1361.5,1072.13,1.03
20260520,1305,1305,1220,1235,5873749,1293.45,-4.52,1362,1078.62,0.92
20260521,1280,1305,1260,1285,5210531,1292.74,-0.6,1363.75,1086.22,0.81
20260522,1325,1365,1305,1330,5646399,1295.85,2.64,1367,1094.75,0.9
20260525,1400,1455,1360,1425,6665391,1306.61,9.06,1368.75,1104.62,1.08
20260526,1465,1495,1425,1445,5681233,1318.14,9.62,1370,1114.62,0.95
20260527,1450,1470,1370,1375,5687897,1322.88,3.94,1369.25,1123.77,0.95
20260528,1395,1420,1290,1305,5166050,1321.39,-1.24,1366.5,1132.4,0.87
20260529,1335,1360,1275,1320,6593515,1321.27,-0.1,1363,1141.63,1.1
20260601,1345,1350,1300,1325,4844214,1321.58,0.26,1357.25,1151.9,0.8
20260602,1330,1330,1235,1275,7260097,1317.7,-3.24,1347,1160.88,1.17
20260603,1360,1400,1350,1385,7490127,1323.31,4.66,1344,1170.77,1.19
20260604,1330,1330,1235,1275,7260097,1319.29,-3.36,1335.25,1179.33,1.13
20260605,1290,1350,1270,1315,5359587,1318.93,-0.3,1334.5,1187.63,0.84
20260611,1415,1440,1285,1345,7917874,1321.1,1.81,1331.75,1195.08,1.22
20260612,1425,1450,1305,1320,6276215,1321.01,-0.08,1328.25,1201.9,0.96
20260615,1380,1400,1305,1320,5263369,1320.92,-0.07,1326.75,1208.32,0.83
20260616,1330,1370,1320,1345,4085591,1322.93,1.67,1322.5,1215.58,0.66
20260617,1345,1375,1340,1370,3261807,1326.85,3.25,1326.5,1223.13,0.54
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 78.77
- over_600_ratio: 75.01
- over_800_ratio: 73.28
- over_1000_ratio: 70.54
- over_400_change_1w: 0.28
- over_800_change_1w: 0.24
- over_1000_change_1w: 0.24
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,78.83,,71.41,,69.37,,0,False,False
20260508,78.88,0.05,71.26,-0.15,69.22,-0.15,1,False,False
20260515,79.37,0.49,71.91,0.65,69.5,0.28,2,True,True
20260522,79.09,-0.28,71.81,-0.1,69.91,0.41,3,False,True
20260529,78.95,-0.14,72.4,0.59,70.3,0.39,4,False,True
20260605,78.49,-0.46,73.04,0.64,70.3,0,5,False,True
20260612,78.77,0.28,73.28,0.24,70.54,0.24,6,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 2368 | 金像電 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 契約相對人:通州建總集團有限公司 ; 與公司之關係 : 非關係人 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 契約總金額:含稅人民幣187,480,000元(約新台幣877,406,400元 ; 以匯率4.68換算) 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 供生產及營運所需 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期:  14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260623; status=confirmed; proximity=within_7d |
| 20260617 | 2368 | 金像電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.契約種類:自地委建 2.事實發生日:115/6/16~115/6/16 3.董事會通過日期: 民國115年6月16日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 契約相對人:通州建總集團有限公司 ; 與公司之關係 : 非關係人 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 契約總金額:含稅人民幣187,480,000元(約新台幣877,406,400元 ; 以匯率4.68換算) 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 供生產及營運所需 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期:  14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260623; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 2368 | 金像電 | 16 | 13 | 5 | 10 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 2368 | 金像電 | 0 | 23 | 0.0 | 528670.0 | 0.0 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
