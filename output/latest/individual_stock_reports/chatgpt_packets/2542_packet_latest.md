# INDIVIDUAL STOCK CHATGPT PACKET - 2542 興富發

## Metadata
- generated_at: 2026-07-09 22:26:39 Asia/Taipei
- stock_id: 2542
- stock_name: 興富發
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
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260709
- open: 43.5
- high: 43.65
- low: 43.2
- close: 43.6
- volume: 3418034
- ma5: 43.95
- ema23_primary: 43.44
- distance_to_ema23_pct: 0.36
- ma20: 43.85
- ma60: 41.78
- ma120: 39.51
- return_5d: 1.16
- return_20d: -4.07
- volume_ratio: 0.27
- distance_to_ma20_pct_auxiliary: -0.58
- distance_to_high_60_pct: -7.43

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,45.85,46,44.55,45.35,39535484,42.61,6.42,43.23,39.29,2.14
20260612,45.85,47.1,44.9,44.95,31562289,42.81,5,43.28,39.42,1.65
20260615,45.15,45.45,44.3,45.45,12409166,43.03,5.63,43.33,39.57,0.66
20260616,45.45,45.85,44.9,45.05,10473379,43.2,4.29,43.4,39.73,0.56
20260617,44.95,45.85,44.8,45.45,10905865,43.38,4.76,43.48,39.88,0.58
20260618,45.65,47,44.75,44.75,19814060,43.5,2.88,43.54,40.03,1.02
20260622,44.1,44.1,42.6,42.7,24903981,43.43,-1.68,43.51,40.15,1.23
20260623,42.5,42.85,41.95,42.7,8908238,43.37,-1.55,43.53,40.26,0.45
20260624,42.55,43.35,42.3,43.1,9836406,43.35,-0.57,43.56,40.38,0.49
20260625,43.2,43.85,43.2,43.3,5727579,43.34,-0.1,43.57,40.5,0.29
20260626,43.3,43.5,42.85,42.9,6821790,43.31,-0.94,43.62,40.63,0.35
20260629,42.9,43.15,42.65,43.1,3929105,43.29,-0.44,43.67,40.77,0.21
20260630,43,43.35,42.2,43.05,14904000,43.27,-0.51,43.7,40.89,0.78
20260701,43,43,42.2,42.35,13512000,43.19,-1.95,43.69,41.02,0.73
20260702,42.15,43.1,42.1,43.1,6561000,43.19,-0.2,43.7,41.14,0.37
20260703,42.75,43.8,42.75,43.65,7838135,43.22,0.99,43.73,41.26,0.45
20260706,43.8,45,43.7,45,13006000,43.37,3.75,43.83,41.41,0.77
20260707,44.95,45,43.65,44,6939731,43.42,1.33,43.93,41.53,0.42
20260708,43.8,44.25,43.2,43.5,4039678,43.43,0.16,43.95,41.64,0.26
20260709,43.5,43.65,43.2,43.6,3418034,43.44,0.36,43.85,41.78,0.27
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 62.27
- over_600_ratio: 60.65
- over_800_ratio: 59.4
- over_1000_ratio: 58.56
- over_400_change_1w: -0.42
- over_800_change_1w: -0.62
- over_1000_change_1w: -0.5
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,60.72,,58.06,,57.07,,0,False,False
20260508,60.8,0.08,58.08,0.02,57.18,0.11,1,True,True
20260515,61.53,0.73,58.67,0.59,57.9,0.72,2,True,True
20260522,61.84,0.31,59.07,0.4,58.1,0.2,3,True,True
20260529,61.84,0,59.05,-0.02,58.12,0.02,4,False,True
20260605,62.01,0.17,59.22,0.17,58.22,0.1,5,True,True
20260612,63.01,1,60.29,1.07,59.37,1.15,6,True,True
20260618,63.08,0.07,60.43,0.14,59.55,0.18,7,True,True
20260626,62.69,-0.39,60.02,-0.41,59.06,-0.49,0,False,False
20260703,62.27,-0.42,59.4,-0.62,58.56,-0.5,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2542 | 興富發 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:（Samoa）He-Xin Worldwide Co., Ltd.股權。 標的物性質:40%股權。 2.事實發生日:115/7/8~115/7/8 3.董事會通過日期: 民國115年7月8日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:4,000,000股。 每股交易金額:新台幣81.25元 交易總金額新台幣:325,000,000元(或等值之美元)。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人:（Samoa）Zilei Fortune Enterprises Ltd.。 與公司之關係：非公司之關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 第一期款:簽約支付新台幣32,500,000元 尾款:股權轉讓完成支付新台幣292,500,000元 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格係參考（Samoa）He-Xin Worldwide Co., Ltd. 財務報告淨值及資產公允價值後，並參酌會計師出具之交易 價格合理性意見書，經本公司董事會討論同意後執行。 本次交易單位決策單位：本公司董事會。 13.取得或處分有價證券標的公司每股淨值: 45.95元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止，累積持有本交易證券（含本次交易）數量：4,000,000股。 迄目前為止，累積持有本交易證券（含本次交易）金額：新台幣325,000,000元。 持股比例：40%。 權利受限情形：無。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司最近期財務報表中 占總資產比例：:0.20% 占股東權益比例:0.59% 營運資金數額:67,794,524仟元。 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 長期股權投資，深化業務合作，有效降低建築成本 及保持上游建材來源穩定之營運需求考量。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用，無設置監察人 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 信佑聯合會計師事務所 23.會計師姓名: 林昶佑 24.會計師開業證書字號: 金管會證字第4562號 北市會證字第2785號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260709 | 2542 | 興富發 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 24.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 標的物之名稱:（Samoa）He-Xin Worldwide Co., Ltd.股權。 標的物性質:40%股權。 2.事實發生日:115/7/8~115/7/8 3.董事會通過日期: 民國115年7月8日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量:4,000,000股。 每股交易金額:新台幣81.25元 交易總金額新台幣:325,000,000元(或等值之美元)。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人:（Samoa）Zilei Fortune Enterprises Ltd.。 與公司之關係：非公司之關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 第一期款:簽約支付新台幣32,500,000元 尾款:股權轉讓完成支付新台幣292,500,000元 12.本次交易之決定方式、價格決定之參考依據及決策單位: 交易價格係參考（Samoa）He-Xin Worldwide Co., Ltd. 財務報告淨值及資產公允價值後，並參酌會計師出具之交易 價格合理性意見書，經本公司董事會討論同意後執行。 本次交易單位決策單位：本公司董事會。 13.取得或處分有價證券標的公司每股淨值: 45.95元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止，累積持有本交易證券（含本次交易）數量：4,000,000股。 迄目前為止，累積持有本交易證券（含本次交易）金額：新台幣325,000,000元。 持股比例：40%。 權利受限情形：無。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司最近期財務報表中 占總資產比例：:0.20% 占股東權益比例:0.59% 營運資金數額:67,794,524仟元。 16.經紀人及經紀費用: 無 17.取得或處分之具體目的或用途: 長期股權投資，深化業務合作，有效降低建築成本 及保持上游建材來源穩定之營運需求考量。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用，無設置監察人 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 信佑聯合會計師事務所 23.會計師姓名: 林昶佑 24.會計師開業證書字號: 金管會證字第4562號 北市會證字第2785號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2542 | 興富發 | 13 | 13 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2542 | 興富發 | 6 | 0 | 198480.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
