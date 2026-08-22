# INDIVIDUAL STOCK CHATGPT PACKET - 2890 永豐金

## Metadata
- generated_at: 2026-08-22 15:59:58 Asia/Taipei
- stock_id: 2890
- stock_name: 永豐金
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
- date: 20260821
- open: 39.3
- high: 39.8
- low: 39.15
- close: 39.6
- volume: 12337566
- ma5: 39.51
- ema23_primary: 39.42
- distance_to_ema23_pct: 0.45
- ma20: 39.45
- ma60: 38
- ma120: 34.71
- return_5d: -2.34
- return_20d: 2.72
- volume_ratio: 0.45
- distance_to_ma20_pct_auxiliary: 0.38
- distance_to_high_60_pct: -6.38

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,39.7,39.8,38.85,39.6,45966658,39.05,1.42,39.97,35.08,0.95
20260728,39,39.55,38.6,38.65,31273955,39.01,-0.93,39.92,35.21,0.66
20260729,39.1,39.2,38.15,38.6,39245879,38.98,-0.97,39.86,35.34,0.85
20260730,39.1,39.1,38,38.85,40014220,38.97,-0.3,39.8,35.48,0.94
20260731,39.1,41.05,39,40.6,49257750,39.1,3.82,39.86,35.64,1.17
20260803,40,40.5,39.5,40.05,26559143,39.18,2.21,39.88,35.79,0.63
20260804,39.3,40.6,39.3,39.6,31750523,39.22,0.97,39.8,35.94,0.76
20260805,39.8,40.1,39.4,39.55,20888840,39.25,0.78,39.73,36.09,0.51
20260806,39.2,39.6,38.7,38.7,15994820,39.2,-1.28,39.57,36.22,0.4
20260807,39.05,39.25,38.8,38.95,8967206,39.18,-0.59,39.49,36.36,0.23
20260810,38.9,39,38.45,38.9,10456774,39.16,-0.65,39.43,36.5,0.28
20260811,39,39.25,38.4,39.05,23661078,39.15,-0.25,39.4,36.65,0.63
20260812,39.15,39.9,39,39.85,19290517,39.21,1.64,39.39,36.81,0.53
20260813,40.2,40.2,39.3,39.95,20565942,39.27,1.74,39.4,36.98,0.57
20260814,40.1,40.95,39.6,40.55,35464151,39.37,2.99,39.42,37.16,1
20260817,40,40.05,38.75,39.6,49677583,39.39,0.52,39.42,37.32,1.41
20260818,39.55,40.5,39.35,39.6,30985498,39.41,0.48,39.39,37.5,0.91
20260819,39.6,39.7,39.1,39.4,24546731,39.41,-0.02,39.34,37.67,0.78
20260820,39.8,39.8,39.1,39.35,14323553,39.4,-0.14,39.4,37.83,0.5
20260821,39.3,39.8,39.15,39.6,12337566,39.42,0.45,39.45,38,0.45
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 81.3
- over_600_ratio: 80.04
- over_800_ratio: 78.98
- over_1000_ratio: 78.11
- over_400_change_1w: 0.38
- over_800_change_1w: 0.39
- over_1000_change_1w: 0.41
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,79.97,0.33,77.57,0.35,76.68,0.34,1,True,True
20260612,80.22,0.25,77.81,0.24,76.97,0.29,2,True,True
20260618,80.48,0.26,78.04,0.23,77.2,0.23,3,True,True
20260626,80.72,0.24,78.35,0.31,77.49,0.29,4,True,True
20260703,80.81,0.09,78.46,0.11,77.59,0.1,5,True,True
20260709,80.89,0.08,78.56,0.1,77.67,0.08,6,True,True
20260717,80.81,-0.08,78.48,-0.08,77.57,-0.1,0,False,False
20260724,80.75,-0.06,78.42,-0.06,77.54,-0.03,0,False,False
20260731,80.88,0.13,78.55,0.13,77.67,0.13,1,True,True
20260807,80.93,0.05,78.59,0.04,77.69,0.02,2,True,True
20260814,80.92,-0.01,78.59,0,77.7,0.01,3,False,True
20260821,81.3,0.38,78.98,0.39,78.11,0.41,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2890 | 永豐金 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | call_inflow | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 聯合授信案授信資產之轉讓。 2.事實發生日:115/8/19~115/8/19 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年8月19日 5.交易單位數量、每單位價格及交易總金額: 港幣160,800,000元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: (1)交易相對人：CITIBANK, N.A.或其他潛在交易對手。 (2)與公司之關係：非關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表說明 認列情形）: 無。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依聯合授信合約相關規定辦理。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依本行分層負責管理辦法辦理，相關條件依聯合授信合約 及一般聯合授信之市場慣例為之。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 不適用。 16.經紀人及經紀費用: 不適用。 17.取得或處分之具體目的或用途: 降低授信暴險部位。 18.本次交易表示異議董事之意見: 不適用。 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用。 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用。 28.資金來源: 不適用。 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 總交易金額依115/8/13 HKD/NTD= 4.1266元換算之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2890 | 永豐金 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_inflow | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 聯合授信案授信資產之轉讓。 2.事實發生日:115/8/19~115/8/19 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年8月19日 5.交易單位數量、每單位價格及交易總金額: 港幣160,800,000元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: (1)交易相對人：CITIBANK, N.A.或其他潛在交易對手。 (2)與公司之關係：非關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用。 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用。 10.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表說明 認列情形）: 無。 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依聯合授信合約相關規定辦理。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依本行分層負責管理辦法辦理，相關條件依聯合授信合約 及一般聯合授信之市場慣例為之。 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 不適用。 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 不適用。 16.經紀人及經紀費用: 不適用。 17.取得或處分之具體目的或用途: 降低授信暴險部位。 18.本次交易表示異議董事之意見: 不適用。 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用。 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用。 28.資金來源: 不適用。 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 總交易金額依115/8/13 HKD/NTD= 4.1266元換算之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2890 | 永豐金 | 19 | 6 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2890 | 永豐金 | 19 | 0 | 2575010.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
