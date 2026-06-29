# INDIVIDUAL STOCK CHATGPT PACKET - 3707 漢磊

## Metadata
- generated_at: 2026-06-29 22:27:04 Asia/Taipei
- stock_id: 3707
- stock_name: 漢磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260629
- price_rows: 158
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3707_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3707_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3707.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3707.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3707.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3707.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3707_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3707_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3707_latest.md?ref=main

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
- date: 20260629
- open: 82
- high: 82
- low: 77.7
- close: 79
- volume: 15418000
- ma5: 87.48
- ema23_primary: 81.78
- distance_to_ema23_pct: -3.4
- ma20: 81.32
- ma60: 71.78
- ma120: 64.35
- return_5d: -13.66
- return_20d: -11.53
- volume_ratio: 1.07
- distance_to_ma20_pct_auxiliary: -2.85
- distance_to_high_60_pct: -21.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260601,90,90.9,83,83.3,85000,77.44,7.57,79.26,63.97,0
20260602,83.2,84.8,80,81.9,82,77.81,5.25,79.58,64.41,0
20260603,83,84.7,80.5,84.3,83000,78.35,7.59,80.14,64.87,0.01
20260604,82.6,83.6,77.5,77.5,80000,78.28,-1,80.28,65.29,0.01
20260605,77.5,79.4,75.1,76.5,77000,78.13,-2.09,80.44,65.69,0.01
20260608,68.9,71.5,68.9,70.6,7365000,77.5,-8.91,80.23,65.95,0.74
20260609,71.5,75.5,69.3,75.3,8754000,77.32,-2.61,80.14,66.28,0.94
20260610,71.7,77.3,71.7,71.9,8530000,76.87,-6.46,80.09,66.54,0.97
20260611,71,74,68.7,74,9192000,76.63,-3.43,79.79,66.79,1.24
20260612,77.7,79.9,77.1,77.1,14085000,76.67,0.56,79.62,67.06,2.52
20260615,81,83.2,80.6,81.7,14713000,77.09,5.98,79.87,67.4,2.78
20260616,82.6,86.8,79.5,79.7,20708000,77.31,3.1,80.22,67.72,3.7
20260617,79.1,83,78.8,80.5,12544000,77.57,3.77,80.61,68.08,2.18
20260618,80.5,84.4,80.2,83.2,18902000,78.04,6.61,80.77,68.48,3.27
20260622,86.5,91.5,86.5,91.5,28965000,79.16,15.58,81.17,69.03,4.01
20260623,94,100.5,93.9,100.5,45967000,80.94,24.16,81.91,69.71,4.83
20260624,95.5,95.5,90.5,90.5,33152000,81.74,10.72,82.28,70.26,2.97
20260625,91,91,85.2,85.8,24363000,82.08,4.54,82.11,70.78,1.97
20260626,85.1,88.8,81.6,81.6,24788000,82.04,-0.53,81.83,71.27,1.82
20260629,82,82,77.7,79,15418000,81.78,-3.4,81.32,71.78,1.07
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 52.39
- over_600_ratio: 51.59
- over_800_ratio: 50.9
- over_1000_ratio: 50.21
- over_400_change_1w: 2.16
- over_800_change_1w: 2.3
- over_1000_change_1w: 3.2
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,47.3,,44.99,,43.85,,0,False,False
20260508,48.13,0.83,46.13,1.14,45.43,1.58,1,True,True
20260515,52.67,4.54,51.16,5.03,50.04,4.61,2,True,True
20260522,53.17,0.5,51.37,0.21,50.72,0.68,3,True,True
20260529,52.75,-0.42,51.11,-0.26,49.76,-0.96,0,False,False
20260605,49.37,-3.38,47.21,-3.9,46.29,-3.47,0,False,False
20260612,49.6,0.23,47.69,0.48,46.58,0.29,1,True,True
20260618,50.23,0.63,48.6,0.91,47.01,0.43,2,True,True
20260626,52.39,2.16,50.9,2.3,50.21,3.2,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 3707 | 漢磊 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.證券名稱: 嘉晶電子股份有限公司普通股 2.交易日期:115/6/26~115/6/26 3.董事會通過日期: 民國115年6月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量: 不超過14,500,000股;  預計交易價格: 6月26日收盤價NT$124.5元(暫定)之上下10%區間內; 預計交易總金額: NT$1,624佰萬元至NT$1,985佰萬元。 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分交易金額扣除成本後之差額約NT$1,550佰萬元，認列科目為資本公積， 尚待會計師查核相關程序及文件後確認。 7.與交易標的公司之關係: 本公司之子公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 152,461,680股；帳面價值NT$2,593佰萬元；52.8%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 13.4%；24.2%；NT$4,316佰萬元。 10.取得或處分之具體目的: 透過處分部分持股來活化資產，以因應未來產業波動或擴充核心業務的資金需求。 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 1.民國115年6月26日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: (1)依內部人持股轉讓相關規定，實際交易日預計將介於6月29日至7月28日。 (2)公告內容係以交易最大股數14,500,000股及6月26日收盤價NT$124.5元(暫定)估算，    實際交易總金額、處分利益及處分後持有股數等，將依實際交易數量及交易價格為準。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |
| 20260629 | 3707 | 漢磊 | revenue_pullback | 營收成長股價回檔 | 67.0 |  |  |  |  |  | stale_signal | 1.證券名稱: 嘉晶電子股份有限公司普通股 2.交易日期:115/6/26~115/6/26 3.董事會通過日期: 民國115年6月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量: 不超過14,500,000股;  預計交易價格: 6月26日收盤價NT$124.5元(暫定)之上下10%區間內; 預計交易總金額: NT$1,624佰萬元至NT$1,985佰萬元。 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分交易金額扣除成本後之差額約NT$1,550佰萬元，認列科目為資本公積， 尚待會計師查核相關程序及文件後確認。 7.與交易標的公司之關係: 本公司之子公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 152,461,680股；帳面價值NT$2,593佰萬元；52.8%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 13.4%；24.2%；NT$4,316佰萬元。 10.取得或處分之具體目的: 透過處分部分持股來活化資產，以因應未來產業波動或擴充核心業務的資金需求。 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 1.民國115年6月26日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: (1)依內部人持股轉讓相關規定，實際交易日預計將介於6月29日至7月28日。 (2)公告內容係以交易最大股數14,500,000股及6月26日收盤價NT$124.5元(暫定)估算，    實際交易總金額、處分利益及處分後持有股數等，將依實際交易數量及交易價格為準。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260629 | 3707 | 漢磊 | 6 | 2 | 5 | 6 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
