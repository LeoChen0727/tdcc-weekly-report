# INDIVIDUAL STOCK CHATGPT PACKET - 2442 新美齊

## Metadata
- generated_at: 2026-07-22 22:27:20 Asia/Taipei
- stock_id: 2442
- stock_name: 新美齊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2442_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2442_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2442.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2442.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2442.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2442.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2442_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2442_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2442_latest.md?ref=main

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
- date: 20260717
- open: 19.5
- high: 19.5
- low: 19
- close: 19.15
- volume: 1832802
- ma5: 19.26
- ema23_primary: 19.34
- distance_to_ema23_pct: -0.97
- ma20: 19.36
- ma60: 19.03
- ma120: 19.88
- return_5d: -0.52
- return_20d: -4.01
- volume_ratio: 1.33
- distance_to_ma20_pct_auxiliary: -1.08
- distance_to_high_60_pct: -6.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,20.05,20.45,19.75,19.85,2904939,19.39,2.37,19.29,19.28,1.15
20260622,19.8,19.8,19.35,19.5,2599723,19.4,0.52,19.34,19.27,1.01
20260623,19.5,19.5,19.25,19.35,1609309,19.4,-0.24,19.39,19.25,0.63
20260624,19.4,19.4,19.15,19.3,1091893,19.39,-0.45,19.43,19.23,0.43
20260625,19.35,19.45,19.25,19.3,1121560,19.38,-0.41,19.48,19.21,0.45
20260626,19.4,19.4,18.95,18.95,1763511,19.34,-2.04,19.49,19.18,0.71
20260629,19,19.3,19,19.25,955773,19.34,-0.45,19.52,19.17,0.4
20260630,19.3,19.35,19.1,19.35,895111,19.34,0.06,19.54,19.14,0.39
20260701,19.4,19.4,19.2,19.35,1163268,19.34,0.06,19.56,19.12,0.52
20260702,19.3,19.4,19.25,19.35,940444,19.34,0.05,19.56,19.11,0.44
20260703,19.35,19.8,19.3,19.7,1904842,19.37,1.71,19.57,19.09,0.92
20260706,19.9,20.05,19.7,19.8,1299973,19.41,2.03,19.56,19.08,0.67
20260707,19.9,19.95,19.35,19.35,1028539,19.4,-0.26,19.55,19.07,0.55
20260708,19.4,19.4,19.2,19.25,1037151,19.39,-0.71,19.54,19.05,0.58
20260709,19.45,19.45,19.15,19.25,946269,19.38,-0.65,19.5,19.04,0.6
20260713,19.4,19.5,19.2,19.25,884360,19.37,-0.6,19.48,19.03,0.59
20260714,19.35,19.35,19.05,19.1,1278325,19.34,-1.26,19.44,19.01,0.9
20260715,19.35,19.4,19.1,19.3,800768,19.34,-0.21,19.41,19.01,0.59
20260716,19.4,19.65,19.3,19.5,1407175,19.35,0.76,19.4,19.03,1.01
20260717,19.5,19.5,19,19.15,1832802,19.34,-0.97,19.36,19.03,1.33
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 57.67
- over_600_ratio: 54.52
- over_800_ratio: 52.42
- over_1000_ratio: 49.71
- over_400_change_1w: 0.25
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.28
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,58.48,,53.53,,51.58,,0,False,False
20260508,58.48,0,53.34,-0.19,51.09,-0.49,1,False,False
20260515,57.96,-0.52,53.33,-0.01,51.09,0,0,False,False
20260522,58.38,0.42,53.59,0.26,51.04,-0.05,1,False,True
20260529,57.74,-0.64,53.52,-0.07,51.27,0.23,2,False,True
20260605,57.5,-0.24,53.35,-0.17,50.51,-0.76,0,False,False
20260612,57.46,-0.04,53.25,-0.1,50.46,-0.05,1,False,False
20260618,57.69,0.23,53.28,0.03,50.77,0.31,2,True,True
20260626,57.46,-0.23,53.01,-0.27,50.48,-0.29,0,False,False
20260703,57.54,0.08,52.54,-0.47,50.33,-0.15,1,False,False
20260709,57.42,-0.12,52.43,-0.11,49.99,-0.34,0,False,False
20260717,57.67,0.25,52.42,-0.01,49.71,-0.28,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2442 | 新美齊 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: (1)齊城資本股份有限公司（原齊城建設股份有限公司）普通股 (2)台北市中正區、中山區共15筆土地及座落之建物、車位。 2.事實發生日:115/7/16~115/7/16 3.董事會通過日期: 民國115年4月14日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: (1)齊城資本股份有限公司（原齊城建設股份有限公司）: 普通股:42,940,000股 每單位價格:10元 (2)台北市中正區、中山區共15筆土地及座落之建物、車位。 不動產土地坪數:29.94坪 不動產建物坪數:343.98坪(含車位) 交易總金額新台幣429,400,000元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人:齊城資本(原齊城建設)股份有限公司 其與公司之關係:齊城資本(原齊城建設)股份有限公司為本公司持股100%之子公司 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: (1)選定關係人為交易對象之原因：集團組織架構調整。 (2)前次移轉資訊：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 本交易為集團組織架構調整，對本公司合併財報無處分損益。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約約定。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 本次交易之決定方式及決策單位：董事會 價格決定之參考依據：係參考本公司持有不動產之原始取得成本及鑑價金額訂定。 12.專業估價者事務所或公司名稱及其估價金額: 宏邦不動產估價師聯合事務所 13.專業估價師姓名: 李青塘 14.專業估價師開業證書字號: 台北市不動產估價師開業證號：(108)北市估字第000278號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 永晟聯合會計師事務所 20.會計師姓名: 伍尚文 21.會計師開業證書字號: 北市會證字第1713號 台省會證字第1951號 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 集團組資架構調整 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 民國115年04月14日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 民國115年04月14日 31.其他敘明事項: 針對115/04/14公告補充說明，修正交易單位數量及交易總金額。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260717 | 2442 | 新美齊 | revenue_breakout_low_response | 營收爆發低反應股 | 15.0 | 29.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: (1)齊城資本股份有限公司（原齊城建設股份有限公司）普通股 (2)台北市中正區、中山區共15筆土地及座落之建物、車位。 2.事實發生日:115/7/16~115/7/16 3.董事會通過日期: 民國115年4月14日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: (1)齊城資本股份有限公司（原齊城建設股份有限公司）: 普通股:42,940,000股 每單位價格:10元 (2)台北市中正區、中山區共15筆土地及座落之建物、車位。 不動產土地坪數:29.94坪 不動產建物坪數:343.98坪(含車位) 交易總金額新台幣429,400,000元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人:齊城資本(原齊城建設)股份有限公司 其與公司之關係:齊城資本(原齊城建設)股份有限公司為本公司持股100%之子公司 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: (1)選定關係人為交易對象之原因：集團組織架構調整。 (2)前次移轉資訊：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 本交易為集團組織架構調整，對本公司合併財報無處分損益。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約約定。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 本次交易之決定方式及決策單位：董事會 價格決定之參考依據：係參考本公司持有不動產之原始取得成本及鑑價金額訂定。 12.專業估價者事務所或公司名稱及其估價金額: 宏邦不動產估價師聯合事務所 13.專業估價師姓名: 李青塘 14.專業估價師開業證書字號: 台北市不動產估價師開業證號：(108)北市估字第000278號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 永晟聯合會計師事務所 20.會計師姓名: 伍尚文 21.會計師開業證書字號: 北市會證字第1713號 台省會證字第1951號 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 集團組資架構調整 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 民國115年04月14日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 民國115年04月14日 31.其他敘明事項: 針對115/04/14公告補充說明，修正交易單位數量及交易總金額。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2442 | 新美齊 | 2 | 2 | 3 | 5 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
