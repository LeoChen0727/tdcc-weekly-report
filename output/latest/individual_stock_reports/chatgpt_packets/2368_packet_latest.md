# INDIVIDUAL STOCK CHATGPT PACKET - 2368 金像電

## Metadata
- generated_at: 2026-08-09 22:26:39 Asia/Taipei
- stock_id: 2368
- stock_name: 金像電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 319
- current_main_price_date: 20260805
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2368_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2368_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2368_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2368_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2368_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2368_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2368_tdcc_window_latest.txt?ref=main
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
- Only claim tdcc_history_ready when the canonical dataset_id matches, every required official date is present, tdcc_rows >= 8, and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
- A canonical accepted stock-level missing date must be disclosed as tdcc_history_degraded_exception; it must not be treated as a continuous weekly series.
- If the stock is absent from the official current main-price universe, preserve real TDCC dates and mark historical_only_noncurrent; do not infer a formal delisting status.
- If TDCC is current but tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260805
- open: 950
- high: 969
- low: 919
- close: 940
- volume: 13005498
- ma5: 844.6
- ema23_primary: 959.1
- distance_to_ema23_pct: -1.99
- ma20: 929.35
- ma60: 1185.03
- ma120: 1099.96
- return_5d: 28.94
- return_20d: -17.18
- volume_ratio: 2.09
- distance_to_ma20_pct_auxiliary: 1.15
- distance_to_high_60_pct: -40.51

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,1150,1180,1110,1150,3923915,1258.55,-8.63,1272.25,1312.75,0.69
20260709,1125,1140,1065,1075,8061580,1243.26,-13.53,1255,1311.5,1.43
20260713,1085,1105,1040,1045,4210045,1226.74,-14.81,1240,1309.5,0.77
20260714,1040,1070,955,1015,6200585,1209.09,-16.05,1224.75,1307,1.14
20260715,1040,1060,1015,1025,4764532,1193.75,-14.14,1210,1304.5,0.88
20260716,998,1010,981,1005,3284092,1178.02,-14.69,1193,1301.08,0.61
20260717,964,980,927,927,5632652,1157.1,-19.89,1170.85,1296.12,1.02
20260720,936,947,875,927,5875440,1137.93,-18.54,1149.45,1290.73,1.05
20260721,950,980,939,980,4609779,1124.77,-12.87,1128.7,1285.98,0.82
20260722,1005,1010,938,940,8073832,1109.37,-15.27,1112.45,1278.48,1.46
20260723,949,958,930,941,5006114,1095.34,-14.09,1096.75,1270.5,0.92
20260724,925,941,892,901,4067807,1079.14,-16.51,1079.8,1262.35,0.77
20260727,905,907,874,895,2619196,1063.8,-15.87,1065.05,1254.6,0.51
20260728,851,851,809,809,5667389,1042.57,-22.4,1047.75,1244.92,1.09
20260729,805,813,729,729,8159221,1016.44,-28.28,1024.2,1233.07,1.53
20260730,717,779,705,721,9520890,991.82,-27.3,999.25,1220.42,1.71
20260731,793,793,784,793,2926470,975.25,-18.69,977.15,1209.55,0.54
20260803,850,872,841,872,5040562,966.64,-9.79,955.5,1199.92,0.93
20260804,901,903,858,897,13604855,960.84,-6.64,939.1,1192.7,2.34
20260805,950,969,919,940,13005498,959.1,-1.99,929.35,1185.03,2.09
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 78.46
- over_600_ratio: 75.56
- over_800_ratio: 72.31
- over_1000_ratio: 69.97
- over_400_change_1w: -0.28
- over_800_change_1w: -1.05
- over_1000_change_1w: -1.56
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,79.09,-0.28,71.81,-0.1,69.91,0.41,3,False,True
20260529,78.95,-0.14,72.4,0.59,70.3,0.39,4,False,True
20260605,78.49,-0.46,73.04,0.64,70.3,0,5,False,True
20260612,78.77,0.28,73.28,0.24,70.54,0.24,6,True,True
20260618,78.8,0.03,73.22,-0.06,70.65,0.11,7,False,True
20260626,77.87,-0.93,72.53,-0.69,69.64,-1.01,0,False,False
20260703,78.21,0.34,72.95,0.42,70.25,0.61,1,True,True
20260709,78.54,0.33,72.59,-0.36,70.05,-0.2,2,False,False
20260717,78.66,0.12,72.86,0.27,70.49,0.44,3,True,True
20260724,78.6,-0.06,72.73,-0.13,70.89,0.4,4,False,True
20260731,78.74,0.14,73.36,0.63,71.53,0.64,5,True,True
20260807,78.46,-0.28,72.31,-1.05,69.97,-1.56,6,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2368 | 金像電 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：蘇新國用(2008)第009250地號 建物：蘇房權證新區字第00094927號 門牌：蘇州高新區馬運路288號 2.事實發生日:115/7/15~115/7/15 3.董事會通過日期: 民國115年7月15日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 土地：共計53,749.20平方公尺，折合16,259.13坪，交易金額：人民幣71,937,000元整。 建物：共計60,103.01平方公尺，折合18,181.16坪，交易金額：人民幣98,063,000元整。 交易總金額：人民幣170,000,000元整。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 名碩電腦(蘇州)有限公司/非關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依議定買賣契約條件付款 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 本次交易之決定方式：雙方議定 價格決定之參考依據：參考不動產估價報告 決策單位：董事會 12.專業估價者事務所或公司名稱及其估價金額: 蘇州弘遠眾益土地房地產資產評估諮詢有限公司/人民幣163,450,000 13.專業估價師姓名: 吉健華 姚凱方 14.專業估價師開業證書字號: 吉健華(註冊證號：3220170107) 姚凱方(註冊證號：3220180065) 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 為擴建本公司蘇州廠 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2368 | 金像電 | 2 | 2 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2368 | 金像電 | 263 | 20 | 20746710.0 | 1528900.0 | 13.57 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
