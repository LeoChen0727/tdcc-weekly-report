# INDIVIDUAL STOCK CHATGPT PACKET - 2890 永豐金

## Metadata
- generated_at: 2026-07-23 22:27:05 Asia/Taipei
- stock_id: 2890
- stock_name: 永豐金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2890_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2890_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2890_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2890_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2890.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2890.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2890.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2890.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2890_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2890_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2890_latest.md?ref=main

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
- date: 20260717
- open: 39.75
- high: 40.05
- low: 39.4
- close: 40
- volume: 49256681
- ma5: 39.93
- ema23_primary: 38.81
- distance_to_ema23_pct: 3.06
- ma20: 40.04
- ma60: 34.31
- ma120: 32.7
- return_5d: -1.11
- return_20d: 10.04
- volume_ratio: 0.89
- distance_to_ma20_pct_auxiliary: -0.09
- distance_to_high_60_pct: -5.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,37.6,39.9,37.2,39.8,148015065,33.27,19.61,32.51,31.82,2.57
20260622,40.75,40.75,39.6,39.8,93780276,33.82,17.69,33.05,31.96,1.57
20260623,40,40.3,39.1,39.8,61232581,34.32,15.98,33.59,32.09,1.01
20260624,39.6,40.9,38.9,39.55,65823679,34.75,13.8,34.09,32.23,1.06
20260625,39.6,40.1,39.35,39.95,59931513,35.19,13.54,34.6,32.36,0.95
20260626,39.55,39.85,39,39.15,43325431,35.52,10.23,35.09,32.5,0.68
20260629,39.3,39.8,38.95,39.5,48480064,35.85,10.19,35.56,32.65,0.77
20260630,39.85,40.3,39.3,39.9,69890542,36.19,10.26,36.03,32.79,1.08
20260701,40,40.65,39.15,40,107513542,36.5,9.58,36.48,32.92,1.59
20260702,39.6,39.9,39.2,39.5,60662238,36.75,7.47,36.81,33.04,0.92
20260703,39.15,40.35,39.15,39.7,25809189,37,7.3,37.14,33.16,0.4
20260706,40.05,41,39.95,41,35911839,37.33,9.82,37.55,33.29,0.56
20260707,41,41.8,40.85,41.1,45168859,37.65,9.17,38.01,33.43,0.71
20260708,41.8,42,41.25,41.9,31400453,38,10.26,38.4,33.58,0.51
20260709,42.05,42.3,40.35,40.45,26714324,38.2,5.88,38.77,33.7,0.44
20260713,41.75,41.75,40,40.2,31611423,38.37,4.77,39.12,33.82,0.53
20260714,40.6,40.6,39,39.65,35527189,38.48,3.05,39.39,33.93,0.61
20260715,39.8,40.3,39.45,39.95,32360511,38.6,3.5,39.63,34.05,0.57
20260716,40.2,40.4,39.65,39.85,29736368,38.7,2.96,39.85,34.17,0.53
20260717,39.75,40.05,39.4,40,49256681,38.81,3.06,40.04,34.31,0.89
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 80.81
- over_600_ratio: 79.55
- over_800_ratio: 78.48
- over_1000_ratio: 77.57
- over_400_change_1w: -0.08
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.1
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.49,,78.1,,77.19,,0,False,False
20260508,80.31,-0.18,77.91,-0.19,76.99,-0.2,0,False,False
20260515,80.1,-0.21,77.68,-0.23,76.81,-0.18,0,False,False
20260522,79.88,-0.22,77.46,-0.22,76.56,-0.25,0,False,False
20260529,79.64,-0.24,77.22,-0.24,76.34,-0.22,0,False,False
20260605,79.97,0.33,77.57,0.35,76.68,0.34,1,True,True
20260612,80.22,0.25,77.81,0.24,76.97,0.29,2,True,True
20260618,80.48,0.26,78.04,0.23,77.2,0.23,3,True,True
20260626,80.72,0.24,78.35,0.31,77.49,0.29,4,True,True
20260703,80.81,0.09,78.46,0.11,77.59,0.1,5,True,True
20260709,80.89,0.08,78.56,0.1,77.67,0.08,6,True,True
20260717,80.81,-0.08,78.48,-0.08,77.57,-0.1,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2890 | 永豐金 | pattern | 型態觀察 | 54.0 |  |  | pullback_right_side |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 聯合授信案授信資產之轉讓。 2.事實發生日:115/7/14~115/7/14 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年7月14日 5.交易單位數量、每單位價格及交易總金額: 英鎊9,462,213元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: (1)交易相對人：Lloyds Bank Plc或其他潛在交易對手。 (2)與公司之關係：非關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表說明 認列情形）: 無。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依聯合授信合約相關規定辦理。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依本行分層負責管理辦法辦理，相關條件 依聯合授信合約及一般聯合授信之市場慣例為之。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 不適用。 16.經紀人及經紀費用: 不適用。 17.取得或處分之具體目的或用途: 降低授信暴險部位。 18.本次交易表示異議董事之意見: 不適用。 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用。 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用。 28.資金來源: 不適用。 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 總交易金額依115/7/9 GBP/NTD= 43.1163元換算之。；calendar event: ex_right_dividend on 20260723; status=confirmed; proximity=within_7d |
| 20260717 | 2890 | 永豐金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 聯合授信案授信資產之轉讓。 2.事實發生日:115/7/14~115/7/14 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年7月14日 5.交易單位數量、每單位價格及交易總金額: 英鎊9,462,213元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: (1)交易相對人：Lloyds Bank Plc或其他潛在交易對手。 (2)與公司之關係：非關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表說明 認列情形）: 無。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依聯合授信合約相關規定辦理。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依本行分層負責管理辦法辦理，相關條件 依聯合授信合約及一般聯合授信之市場慣例為之。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 不適用。 16.經紀人及經紀費用: 不適用。 17.取得或處分之具體目的或用途: 降低授信暴險部位。 18.本次交易表示異議董事之意見: 不適用。 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用。 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用。 28.資金來源: 不適用。 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 總交易金額依115/7/9 GBP/NTD= 43.1163元換算之。；calendar event: ex_right_dividend on 20260723; status=confirmed; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2890 | 永豐金 | 15 | 5 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2890 | 永豐金 | 21 | 0 | 1281380.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
