# INDIVIDUAL STOCK CHATGPT PACKET - 2605 新興

## Metadata
- generated_at: 2026-09-26 15:51:29 Asia/Taipei
- stock_id: 2605
- stock_name: 新興
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2605_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2605_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2605_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2605_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2605_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2605_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2605_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2605.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2605.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2605.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2605.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2605_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2605_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2605_latest.md?ref=main

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
- date: 20260924
- open: 37.15
- high: 37.2
- low: 36.2
- close: 36.5
- volume: 6256782
- ma5: 36.81
- ema23_primary: 35.95
- distance_to_ema23_pct: 1.53
- ma20: 36.13
- ma60: 33.58
- ma120: 33.24
- return_5d: -1.75
- return_20d: 6.1
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: 1.03
- distance_to_high_60_pct: -6.89

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,34.65,35.6,34.45,35.05,8462440,34.02,3.03,33.94,31.95,0.5
20260831,35.3,35.65,34.95,35.35,8875293,34.13,3.58,34.14,32,0.52
20260901,35.05,35.3,34.65,34.75,6608988,34.18,1.66,34.32,32.04,0.38
20260902,35.1,35.45,34.75,35.05,7593610,34.25,2.33,34.47,32.11,0.43
20260903,36.45,36.75,35.5,35.5,16528623,34.36,3.33,34.65,32.19,0.91
20260904,36,36.6,35.3,35.85,9121757,34.48,3.97,34.81,32.28,0.5
20260907,36,36.6,35.8,36.35,7665129,34.64,4.94,34.97,32.38,0.41
20260908,36,37.15,35.45,36.5,9484244,34.79,4.91,35.16,32.46,0.51
20260909,36.55,37.2,35.85,36.95,14005228,34.97,5.65,35.38,32.55,0.73
20260910,37,38.65,36.05,36.25,24763869,35.08,3.34,35.58,32.62,1.24
20260911,35.95,37.5,35.9,36.5,15254289,35.2,3.7,35.78,32.69,0.75
20260914,36.5,37.1,35.9,36.15,6995523,35.28,2.48,35.95,32.77,0.34
20260915,36.15,36.55,34.85,35.05,8993430,35.26,-0.59,35.94,32.82,0.46
20260916,35.1,36.8,35.1,36.05,12864086,35.32,2.06,35.91,32.9,0.77
20260917,36,37.45,35.65,37.15,14491606,35.48,4.72,35.94,32.99,0.91
20260918,37.15,37.6,36.1,36.1,9451516,35.53,1.61,35.86,33.08,0.65
20260921,36.7,38.2,36.1,37.3,12860816,35.68,4.55,35.89,33.21,0.94
20260922,37.6,37.75,37.1,37.1,5164616,35.79,3.65,35.91,33.33,0.44
20260923,37.6,37.65,36.7,37.05,6734824,35.9,3.21,36.02,33.45,0.62
20260924,37.15,37.2,36.2,36.5,6256782,35.95,1.53,36.13,33.58,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 55.57
- over_600_ratio: 52.7
- over_800_ratio: 51.09
- over_1000_ratio: 49.41
- over_400_change_1w: 0.13
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.23
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,52.79,0.39,49.29,0.87,48.67,0.88,1,True,True
20260717,53.44,0.65,49.87,0.58,49.1,0.43,2,True,True
20260724,54.32,0.88,50.9,1.03,49.85,0.75,3,True,True
20260731,54.34,0.02,50.33,-0.57,49.59,-0.26,4,False,False
20260807,54.95,0.61,50.99,0.66,50.24,0.65,5,True,True
20260814,55.35,0.4,51.12,0.13,49.93,-0.31,6,False,True
20260821,55.19,-0.16,50.98,-0.14,49.91,-0.02,0,False,False
20260828,53.87,-1.32,48.87,-2.11,47.92,-1.99,0,False,False
20260904,54.16,0.29,49.76,0.89,48.41,0.49,1,True,True
20260911,54.21,0.05,49.45,-0.31,48.25,-0.16,2,False,False
20260918,55.44,1.23,50.98,1.53,49.18,0.93,3,True,True
20260924,55.57,0.13,51.09,0.11,49.41,0.23,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2605 | 新興 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 81,770 載重噸，2019年建造之卡姆薩型散裝貨輪。 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 卡姆薩型散裝貨輪壹艘，美金3,850萬元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: MTO MARITIME, S.A., Panama，非本公司關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 簽約後2個營業日內支付15%，預定交船日前3個營業日內支付85%。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 議價，本公司董事會。 12.專業估價者事務所或公司名稱及其估價金額: 不適用。 13.專業估價師姓名: 不適用。 14.專業估價師開業證書字號: 不適用。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 船隊擴編。 24.本次交易表示異議之董事之意見: 無。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用。 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 預計交船日為115年11月下旬至116年2月間。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 2605 | 新興 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 81,770 載重噸，2019年建造之卡姆薩型散裝貨輪。 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 卡姆薩型散裝貨輪壹艘，美金3,850萬元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: MTO MARITIME, S.A., Panama，非本公司關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 簽約後2個營業日內支付15%，預定交船日前3個營業日內支付85%。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 議價，本公司董事會。 12.專業估價者事務所或公司名稱及其估價金額: 不適用。 13.專業估價師姓名: 不適用。 14.專業估價師開業證書字號: 不適用。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 船隊擴編。 24.本次交易表示異議之董事之意見: 無。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用。 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 預計交船日為115年11月下旬至116年2月間。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 2605 | 新興 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 17 | B_可觀察 |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 81,770 載重噸，2019年建造之卡姆薩型散裝貨輪。 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 卡姆薩型散裝貨輪壹艘，美金3,850萬元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: MTO MARITIME, S.A., Panama，非本公司關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 簽約後2個營業日內支付15%，預定交船日前3個營業日內支付85%。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 議價，本公司董事會。 12.專業估價者事務所或公司名稱及其估價金額: 不適用。 13.專業估價師姓名: 不適用。 14.專業估價師開業證書字號: 不適用。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 船隊擴編。 24.本次交易表示異議之董事之意見: 無。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用。 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 預計交船日為115年11月下旬至116年2月間。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2605 | 新興 | 30 | 14 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2605 | 新興 | 67 | 2 | 801590.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
