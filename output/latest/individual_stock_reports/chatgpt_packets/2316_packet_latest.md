# INDIVIDUAL STOCK CHATGPT PACKET - 2316 楠梓電

## Metadata
- generated_at: 2026-08-22 15:59:42 Asia/Taipei
- stock_id: 2316
- stock_name: 楠梓電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2316_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2316_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2316_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2316_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2316_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2316_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2316_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2316.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2316.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2316.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2316.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2316_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2316_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2316_latest.md?ref=main

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
- date: 20260821
- open: 157.5
- high: 163
- low: 155.5
- close: 158.5
- volume: 1669559
- ma5: 159.1
- ema23_primary: 161.71
- distance_to_ema23_pct: -1.98
- ma20: 155.25
- ma60: 175.51
- ma120: 144.97
- return_5d: -0.94
- return_20d: 1.6
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 2.09
- distance_to_high_60_pct: -36.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,155,157,148.5,155,1467261,178.07,-12.96,187.95,169.2,0.6
20260728,148,148,141,142.5,2212479,175.11,-18.62,184.57,169.7,0.9
20260729,143,146,128.5,136.5,3826289,171.89,-20.59,180.55,170.07,1.47
20260730,137,139,127,129.5,2717711,168.36,-23.08,176.12,170.26,1
20260731,142,142,142,142,671618,166.16,-14.54,172.53,170.68,0.25
20260803,145.5,152,143.5,149,2247825,164.73,-9.55,168.9,171.22,0.81
20260804,147.5,154,146,152.5,1596848,163.71,-6.85,165.72,171.88,0.58
20260805,157.5,161,155.5,159.5,1930330,163.36,-2.36,163.43,172.48,0.68
20260806,157,165.5,153,162.5,1966798,163.29,-0.48,160.65,172.93,0.69
20260807,163.5,164.5,158,159.5,1769366,162.97,-2.13,158.22,173.22,0.63
20260810,162,166.5,161,163.5,2036652,163.02,0.3,157.12,173.71,0.75
20260811,168.5,179,167,172,3375318,163.77,5.03,156.53,174.42,1.27
20260812,165,166,160.5,161.5,3591921,163.58,-1.27,155.68,175,1.35
20260813,163.5,170,163,164,2985159,163.61,0.24,155.03,175.42,1.1
20260814,164.5,164.5,158.5,160,1720273,163.31,-2.03,155.05,175.79,0.65
20260817,160.5,169,158,167,2077633,163.62,2.07,155.75,176.06,0.8
20260818,168,168.5,158.5,159,3092112,163.23,-2.59,155.93,176.15,1.18
20260819,153,163,153,155.5,3257021,162.59,-4.36,155.62,175.93,1.28
20260820,157.5,159.5,153,155.5,4138705,162,-4.01,155.12,175.67,1.68
20260821,157.5,163,155.5,158.5,1669559,161.71,-1.98,155.25,175.51,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 64.31
- over_600_ratio: 61.46
- over_800_ratio: 59.99
- over_1000_ratio: 57.55
- over_400_change_1w: -0.67
- over_800_change_1w: -0.75
- over_1000_change_1w: -1.3
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,64.28,-0.83,58.02,-2.12,55.56,-0.61,0,False,False
20260612,64.7,0.42,60.09,2.07,57.66,2.1,1,True,True
20260618,67.88,3.18,59.93,-0.16,58.42,0.76,2,False,True
20260626,68.03,0.15,61.09,1.16,59.59,1.17,3,True,True
20260703,67.33,-0.7,61.31,0.22,59.84,0.25,4,False,True
20260709,67.25,-0.08,61.38,0.07,59.78,-0.06,5,False,True
20260717,65.81,-1.44,60.26,-1.12,58.67,-1.11,0,False,False
20260724,65.09,-0.72,59.87,-0.39,58.39,-0.28,0,False,False
20260731,64.92,-0.17,59.44,-0.43,58.01,-0.38,0,False,False
20260807,65.09,0.17,60.07,0.63,58.64,0.63,1,True,True
20260814,64.98,-0.11,60.74,0.67,58.85,0.21,2,False,True
20260821,64.31,-0.67,59.99,-0.75,57.55,-1.3,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2316 | 楠梓電 | pattern | 型態觀察 | 45.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 江蘇省昆山市玉山鎮楠梓路255號 2.事實發生日:115/8/10~115/8/10 3.董事會通過日期: 民國115年8月10日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 房屋租賃面積：11,500平方公尺，折合3,478.51坪 每單位價格：每月租金人民幣23萬元 (約新台幣106萬元) 交易總金額：售後租回取得之使用權資產人民幣6,086,414元 (約新台幣2817.7萬元) 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：昆山滬利微電有限公司 與公司之關係：關聯企業 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 選定關係人為交易對象之原因：營運策略考量 前次移轉之所有人、移轉價格及取得日期:不適用(售後租回) 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 取得及處分日期：不適用(售後租回) 取得及處分價格：不適用(售後租回) 與公司之關係：不適用(售後租回) 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交付或付款條件：依合約規定 契約限制條款：無 其他重要約定事項：租約到期有優先承租權 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易之決定方式：依據市場行情進行議價 決策單位：董事長 12.專業估價者事務所或公司名稱及其估價金額: 專業估價者事務所：智上會計師事務所 估價金額：人民幣6,086,414元 13.專業估價師姓名: 陳美琴 14.專業估價師開業證書字號: 金管會證字第8803號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 供生產及營運使用 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:是 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:28,177,000元 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 使用權資產折現後之租賃給付為人民幣23,326,977元整，本次使用權資產所涉及之不動產 移轉已符合IFRS 15所定銷售認列條件，故將本交易作為售後租回交易處理。 依IFRS 16規定，先創電子於租賃開始日就廠房售後租回所認列之使用權資產金額為人民 幣6,086,414元。其計算如下： 人民幣23,457,416元（不動產原帳面金額）× 23,326,977元（為 10 年使用權資產之折 現後租賃給付）÷ 89,903,611元（不動產之公允價值）= 6,086,414元。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2316 | 楠梓電 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 江蘇省昆山市玉山鎮楠梓路255號 2.事實發生日:115/8/10~115/8/10 3.董事會通過日期: 民國115年8月10日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 房屋租賃面積：11,500平方公尺，折合3,478.51坪 每單位價格：每月租金人民幣23萬元 (約新台幣106萬元) 交易總金額：售後租回取得之使用權資產人民幣6,086,414元 (約新台幣2817.7萬元) 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：昆山滬利微電有限公司 與公司之關係：關聯企業 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 選定關係人為交易對象之原因：營運策略考量 前次移轉之所有人、移轉價格及取得日期:不適用(售後租回) 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 取得及處分日期：不適用(售後租回) 取得及處分價格：不適用(售後租回) 與公司之關係：不適用(售後租回) 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交付或付款條件：依合約規定 契約限制條款：無 其他重要約定事項：租約到期有優先承租權 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易之決定方式：依據市場行情進行議價 決策單位：董事長 12.專業估價者事務所或公司名稱及其估價金額: 專業估價者事務所：智上會計師事務所 估價金額：人民幣6,086,414元 13.專業估價師姓名: 陳美琴 14.專業估價師開業證書字號: 金管會證字第8803號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 供生產及營運使用 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:是 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:28,177,000元 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 使用權資產折現後之租賃給付為人民幣23,326,977元整，本次使用權資產所涉及之不動產 移轉已符合IFRS 15所定銷售認列條件，故將本交易作為售後租回交易處理。 依IFRS 16規定，先創電子於租賃開始日就廠房售後租回所認列之使用權資產金額為人民 幣6,086,414元。其計算如下： 人民幣23,457,416元（不動產原帳面金額）× 23,326,977元（為 10 年使用權資產之折 現後租賃給付）÷ 89,903,611元（不動產之公允價值）= 6,086,414元。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2316 | 楠梓電 | 6 | 6 | 5 | 9 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2316 | 楠梓電 | 89 | 0 | 9359220.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
