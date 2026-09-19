# INDIVIDUAL STOCK CHATGPT PACKET - 2348 海悅

## Metadata
- generated_at: 2026-09-19 15:52:35 Asia/Taipei
- stock_id: 2348
- stock_name: 海悅
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2348_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2348_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2348.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2348.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2348.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2348.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2348_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2348_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2348_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260918
- open: 79
- high: 79
- low: 73.2
- close: 74.2
- volume: 2168062
- ma5: 71.8
- ema23_primary: 71.64
- distance_to_ema23_pct: 3.57
- ma20: 71.36
- ma60: 73.04
- ma120: 73.14
- return_5d: 5.55
- return_20d: 2.49
- volume_ratio: 5.31
- distance_to_ma20_pct_auxiliary: 3.99
- distance_to_high_60_pct: -9.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,72.4,73,71.1,71.6,240451,72.09,-0.68,71.7,73.5,0.42
20260825,71.5,71.5,70.1,70.1,186296,71.92,-2.53,71.39,73.53,0.34
20260826,70.1,71.3,70,71.1,210474,71.85,-1.05,71.18,73.55,0.4
20260827,71.7,72.2,70.5,71.7,321810,71.84,-0.19,70.95,73.57,0.62
20260828,71.9,72.2,70.7,72.1,277047,71.86,0.33,70.71,73.52,0.55
20260831,71.5,72,70.6,70.6,245765,71.76,-1.61,70.52,73.46,0.54
20260901,70.3,71.1,70.3,70.7,103375,71.67,-1.35,70.67,73.43,0.25
20260902,70.5,71.1,70.4,71.1,80133,71.62,-0.73,70.78,73.44,0.2
20260903,71.2,71.7,70.7,71.1,176989,71.58,-0.67,70.86,73.44,0.51
20260904,70.8,72.4,70.7,72.1,286185,71.62,0.67,70.89,73.34,0.88
20260907,72.2,72.3,70.8,71.2,361862,71.59,-0.54,70.89,73.31,1.17
20260908,71.2,72.4,70.8,71.9,314800,71.61,0.4,70.97,73.3,1.04
20260909,71.6,71.6,69.9,71.2,584752,71.58,-0.53,71,73.28,1.87
20260910,70.3,71.3,70.3,71.3,267400,71.55,-0.36,71.07,73.22,0.88
20260911,71,71,70.1,70.3,282334,71.45,-1.61,71.11,73.1,0.93
20260914,70,70.7,69.1,70.5,278257,71.37,-1.22,71.11,72.99,0.91
20260915,69.8,70.5,69.7,70.2,171609,71.27,-1.51,71.15,72.96,0.58
20260916,70.1,70.3,69.7,70.2,590768,71.18,-1.38,71.16,72.94,1.89
20260917,69.7,74.1,69.7,73.9,1013530,71.41,3.49,71.27,72.99,3.12
20260918,79,79,73.2,74.2,2168062,71.64,3.57,71.36,73.04,5.31
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 70.03
- over_600_ratio: 68.25
- over_800_ratio: 67.01
- over_1000_ratio: 65.24
- over_400_change_1w: 0.64
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,68.17,-0.25,66.07,0.01,65.47,0.01,1,False,True
20260709,68.84,0.67,66.12,0.05,65.52,0.05,2,True,True
20260717,69.04,0.2,66.08,-0.04,65.48,-0.04,3,False,False
20260724,69.35,0.31,67.24,1.16,65.5,0.02,4,True,True
20260731,69.83,0.48,66.72,-0.52,65.56,0.06,5,False,True
20260807,69.15,-0.68,66.13,-0.59,65.53,-0.03,0,False,False
20260814,68.87,-0.28,66.06,-0.07,65.46,-0.07,0,False,False
20260821,68.83,-0.04,66.65,0.59,65.51,0.05,1,False,True
20260828,68.97,0.14,67.17,0.52,65.46,-0.05,2,False,True
20260904,68.98,0.01,67.19,0.02,65.41,-0.05,3,False,True
20260911,69.39,0.41,67.05,-0.14,65.26,-0.15,4,False,False
20260918,70.03,0.64,67.01,-0.04,65.24,-0.02,5,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2348 | 海悅 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | continued_2_3d | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：新北市新店區寶元段931、945、946、947地號等4筆土地 建物：新北市新店區寶元段1843建號及其所有地上物 本公司持有比例為20%。 2.事實發生日:115/9/17~115/9/17 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年9月17日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 土地面積計5,684.78平方公尺(折合約1,719.65坪) 建物及其所有地上物面積合計約1,623.84平方公尺(折合約491.21坪) 交易總金額為新台幣3,523,160,000元，本公司持有比例為20%。 本公司交易金額為新臺幣704,632,000元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：屬自然人且非本公司之關係人，故不揭露其姓名 與公司之關係：非公司關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約約定方式辦理 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 決定方式：議價 決策單位：董事會授權董事長決行 12.專業估價者事務所或公司名稱及其估價金額: 宏邦不動產估價師聯合事務所，估價金額：新台幣711,935,100元 13.專業估價師姓名: 宏邦不動產估價師聯合事務所：李青塘估價師 14.專業估價師開業證書字號: 李青塘估價師：(108)北市估字第000278號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 開發興建以供出售，與其他公司聯盟合作。 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 2348 | 海悅 | revenue_breakout_low_response | 營收爆發低反應股 | 20 | 25 | D_僅留完整清單 |  |  | call_inflow | continued_2_3d | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：新北市新店區寶元段931、945、946、947地號等4筆土地 建物：新北市新店區寶元段1843建號及其所有地上物 本公司持有比例為20%。 2.事實發生日:115/9/17~115/9/17 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年9月17日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 土地面積計5,684.78平方公尺(折合約1,719.65坪) 建物及其所有地上物面積合計約1,623.84平方公尺(折合約491.21坪) 交易總金額為新台幣3,523,160,000元，本公司持有比例為20%。 本公司交易金額為新臺幣704,632,000元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：屬自然人且非本公司之關係人，故不揭露其姓名 與公司之關係：非公司關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約約定方式辦理 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 決定方式：議價 決策單位：董事會授權董事長決行 12.專業估價者事務所或公司名稱及其估價金額: 宏邦不動產估價師聯合事務所，估價金額：新台幣711,935,100元 13.專業估價師姓名: 宏邦不動產估價師聯合事務所：李青塘估價師 14.專業估價師開業證書字號: 李青塘估價師：(108)北市估字第000278號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 開發興建以供出售，與其他公司聯盟合作。 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2348 | 海悅 | 2 | 2 | 2 | 2 | 2 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2348 | 海悅 | 6 | 0 | 1165350.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
