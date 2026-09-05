# INDIVIDUAL STOCK CHATGPT PACKET - 2542 興富發

## Metadata
- generated_at: 2026-09-05 15:52:57 Asia/Taipei
- stock_id: 2542
- stock_name: 興富發
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2542_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2542_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2542_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2542_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2542.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2542.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2542.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2542.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2542_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2542_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2542_latest.md?ref=main

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
- date: 20260904
- open: 48.65
- high: 48.75
- low: 48.1
- close: 48.55
- volume: 6938993
- ma5: 47.94
- ema23_primary: 46.95
- distance_to_ema23_pct: 3.4
- ma20: 47.22
- ma60: 44.97
- ma120: 42.06
- return_5d: 3.3
- return_20d: 9.59
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: 2.82
- distance_to_high_60_pct: -0.92

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,44.05,44.45,43.85,44.35,3422346,43.89,1.06,43.88,43.62,0.41
20260811,44.35,44.55,44.15,44.55,5528238,43.94,1.38,43.94,43.63,0.67
20260812,44.7,44.85,44.5,44.8,6355986,44.01,1.79,44.01,43.64,0.78
20260813,45,46.4,44.9,46.4,16897697,44.21,4.95,44.16,43.68,1.94
20260814,46.2,46.65,45.75,46.2,9265415,44.38,4.11,44.31,43.72,1.09
20260817,46,46.95,45.8,46.8,11721317,44.58,4.98,44.48,43.77,1.4
20260818,47,47.8,46.8,47.75,16522010,44.84,6.48,44.66,43.85,1.97
20260819,47.5,48.2,47.1,48.15,13205723,45.12,6.72,44.83,43.95,1.59
20260820,48.2,48.6,47.75,48.3,10318280,45.38,6.42,45,44.05,1.27
20260821,48.25,49,48.2,48.8,11744799,45.67,6.86,45.23,44.14,1.41
20260824,48.8,48.85,48.05,48.3,7277704,45.89,5.26,45.47,44.24,0.86
20260825,48,48.2,47.1,47.5,7128783,46.02,3.21,45.7,44.34,0.84
20260826,47.5,48,47.25,48,5420281,46.19,3.92,45.94,44.43,0.64
20260827,48,48.1,47.4,47.75,3370771,46.32,3.09,46.1,44.52,0.42
20260828,47.7,47.7,46.95,47,5444582,46.37,1.35,46.26,44.58,0.69
20260831,46.9,47.15,46.5,46.65,5554761,46.4,0.54,46.4,44.64,0.69
20260901,46.55,48,46.55,47.9,8094788,46.52,2.96,46.58,44.72,1.01
20260902,47.55,48,47.55,47.95,4263041,46.64,2.81,46.78,44.82,0.53
20260903,48,48.75,47.85,48.65,10377793,46.81,3.93,47.01,44.91,1.24
20260904,48.65,48.75,48.1,48.55,6938993,46.95,3.4,47.22,44.97,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 66.39
- over_600_ratio: 65.04
- over_800_ratio: 63.67
- over_1000_ratio: 63.06
- over_400_change_1w: 0.12
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.23
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,63.08,0.07,60.43,0.14,59.55,0.18,7,True,True
20260626,62.69,-0.39,60.02,-0.41,59.06,-0.49,0,False,False
20260703,62.27,-0.42,59.4,-0.62,58.56,-0.5,0,False,False
20260709,62.81,0.54,59.89,0.49,59.13,0.57,1,True,True
20260717,63.06,0.25,60.19,0.3,59.43,0.3,2,True,True
20260724,64.01,0.95,61.16,0.97,60.4,0.97,3,True,True
20260731,64.38,0.37,61.59,0.43,60.62,0.22,4,True,True
20260807,64.47,0.09,61.72,0.13,60.88,0.26,5,True,True
20260814,65.14,0.67,62.32,0.6,61.56,0.68,6,True,True
20260821,65.96,0.82,63.23,0.91,62.55,0.99,7,True,True
20260828,66.27,0.31,63.56,0.33,62.83,0.28,8,True,True
20260904,66.39,0.12,63.67,0.11,63.06,0.23,9,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2542 | 興富發 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | call_inflow | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:（Samoa）He-Xin Worldwide Co., Ltd.股權。 標的物性質:40%股權。 2.事實發生日:115/7/8~115/7/8 3.董事會通過日期: 民國115年7月8日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:4,000,000股。 每股交易金額:新台幣81.25元 交易總金額新台幣:325,000,000元(或等值之美元)。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人:（Samoa）Zilei Fortune Enterprises Ltd.。 與公司之關係：非公司之關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 第一期款:簽約支付新台幣32,500,000元 尾款:股權轉讓完成支付新台幣292,500,000元 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格係參考（Samoa）He-Xin Worldwide Co., Ltd. 財務報告淨值及資產公允價值後，並參酌會計師出具之交易 價格合理性意見書，經本公司董事會討論同意後執行。 本次交易單位決策單位：本公司董事會。 13.取得或處分有價證券標的公司每股淨值: 45.95元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止，累積持有本交易證券（含本次交易）數量：4,000,000股。 迄目前為止，累積持有本交易證券（含本次交易）金額：新台幣325,000,000元。 持股比例：40%。 權利受限情形：無。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司最近期財務報表中 占總資產比例：:0.20% 占股東權益比例:0.59% 營運資金數額:67,794,524仟元。 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 長期股權投資，深化業務合作，有效降低建築成本 及保持上游建材來源穩定之營運需求考量。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用，無設置監察人 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 信佑聯合會計師事務所 23.會計師姓名: 林昶佑 24.會計師開業證書字號: 金管會證字第4562號 北市會證字第2785號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d |
| 20260904 | 2542 | 興富發 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | call_inflow | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:（Samoa）He-Xin Worldwide Co., Ltd.股權。 標的物性質:40%股權。 2.事實發生日:115/7/8~115/7/8 3.董事會通過日期: 民國115年7月8日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:4,000,000股。 每股交易金額:新台幣81.25元 交易總金額新台幣:325,000,000元(或等值之美元)。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人:（Samoa）Zilei Fortune Enterprises Ltd.。 與公司之關係：非公司之關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 第一期款:簽約支付新台幣32,500,000元 尾款:股權轉讓完成支付新台幣292,500,000元 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格係參考（Samoa）He-Xin Worldwide Co., Ltd. 財務報告淨值及資產公允價值後，並參酌會計師出具之交易 價格合理性意見書，經本公司董事會討論同意後執行。 本次交易單位決策單位：本公司董事會。 13.取得或處分有價證券標的公司每股淨值: 45.95元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止，累積持有本交易證券（含本次交易）數量：4,000,000股。 迄目前為止，累積持有本交易證券（含本次交易）金額：新台幣325,000,000元。 持股比例：40%。 權利受限情形：無。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司最近期財務報表中 占總資產比例：:0.20% 占股東權益比例:0.59% 營運資金數額:67,794,524仟元。 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 長期股權投資，深化業務合作，有效降低建築成本 及保持上游建材來源穩定之營運需求考量。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用，無設置監察人 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 信佑聯合會計師事務所 23.會計師姓名: 林昶佑 24.會計師開業證書字號: 金管會證字第4562號 北市會證字第2785號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260904 | 2542 | 興富發 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 23 | B_可觀察 |  |  | call_inflow | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:（Samoa）He-Xin Worldwide Co., Ltd.股權。 標的物性質:40%股權。 2.事實發生日:115/7/8~115/7/8 3.董事會通過日期: 民國115年7月8日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:4,000,000股。 每股交易金額:新台幣81.25元 交易總金額新台幣:325,000,000元(或等值之美元)。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人:（Samoa）Zilei Fortune Enterprises Ltd.。 與公司之關係：非公司之關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 第一期款:簽約支付新台幣32,500,000元 尾款:股權轉讓完成支付新台幣292,500,000元 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格係參考（Samoa）He-Xin Worldwide Co., Ltd. 財務報告淨值及資產公允價值後，並參酌會計師出具之交易 價格合理性意見書，經本公司董事會討論同意後執行。 本次交易單位決策單位：本公司董事會。 13.取得或處分有價證券標的公司每股淨值: 45.95元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止，累積持有本交易證券（含本次交易）數量：4,000,000股。 迄目前為止，累積持有本交易證券（含本次交易）金額：新台幣325,000,000元。 持股比例：40%。 權利受限情形：無。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司最近期財務報表中 占總資產比例：:0.20% 占股東權益比例:0.59% 營運資金數額:67,794,524仟元。 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 長期股權投資，深化業務合作，有效降低建築成本 及保持上游建材來源穩定之營運需求考量。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用，無設置監察人 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 信佑聯合會計師事務所 23.會計師姓名: 林昶佑 24.會計師開業證書字號: 金管會證字第4562號 北市會證字第2785號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: ex_dividend on 20260923; status=confirmed; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2542 | 興富發 | 13 | 13 | 5 | 10 | 14 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2542 | 興富發 | 9 | 0 | 1184880.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
