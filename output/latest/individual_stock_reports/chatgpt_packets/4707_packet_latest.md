# INDIVIDUAL STOCK CHATGPT PACKET - 4707 磐亞

## Metadata
- generated_at: 2026-09-26 22:17:00 Asia/Taipei
- stock_id: 4707
- stock_name: 磐亞
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4707_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4707_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4707_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4707_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4707_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4707_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4707_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4707.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4707.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4707.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4707.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4707_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4707_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4707_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260924
- open: 29.2
- high: 31
- low: 29.1
- close: 30
- volume: 3453000
- ma5: 29.2
- ema23_primary: 29.22
- distance_to_ema23_pct: 2.67
- ma20: 28.93
- ma60: 31.8
- ma120: 24.66
- return_5d: 11.94
- return_20d: -6.83
- volume_ratio: 1.32
- distance_to_ma20_pct_auxiliary: 3.69
- distance_to_high_60_pct: -33.33

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,32.35,33.45,32,32.55,2398000,32.35,0.61,32.07,29.94,0.46
20260831,32.8,34.85,32.25,33.4,3593000,32.44,2.96,32.46,30.14,0.69
20260901,33.5,34.35,32.25,32.25,3647000,32.42,-0.54,32.67,30.35,0.7
20260902,32.5,32.5,31.4,31.45,2035000,32.34,-2.76,32.7,30.55,0.4
20260903,31.65,32.15,30.4,30.4,2296000,32.18,-5.53,32.53,30.71,0.5
20260904,31.1,31.15,29.2,30.1,2901000,32.01,-5.96,32.44,30.9,0.66
20260907,30.8,30.8,28.2,28.3,4113000,31.7,-10.72,32.26,31.04,0.94
20260908,28.8,29.1,28,28.3,1800000,31.42,-9.92,32.17,31.18,0.44
20260909,28,28.85,26.7,27.2,5861000,31.06,-12.44,31.88,31.29,1.44
20260910,27.2,27.2,26.2,26.75,2621000,30.7,-12.88,31.6,31.39,0.7
20260911,26.1,26.7,26.1,26.15,2050000,30.33,-13.77,31.33,31.45,0.56
20260914,26.1,26.3,25.2,26.1,1552000,29.97,-12.92,31.02,31.51,0.43
20260915,25.85,26.3,25.65,26.15,993000,29.65,-11.82,30.69,31.55,0.28
20260916,26.15,27.5,26.15,26.75,1596000,29.41,-9.05,30.45,31.65,0.46
20260917,27,27.65,26.8,26.8,1568000,29.19,-8.2,30.17,31.71,0.46
20260918,27,28.25,27,28,1483000,29.1,-3.76,29.92,31.75,0.44
20260921,28.25,30.7,28.25,29.1,3899000,29.1,0.02,29.59,31.78,1.33
20260922,29.5,29.75,28.65,29.7,2359000,29.15,1.9,29.32,31.77,0.84
20260923,30,30.55,29,29.2,1934000,29.15,0.17,29.04,31.77,0.73
20260924,29.2,31,29.1,30,3453000,29.22,2.67,28.93,31.8,1.32
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 70.76
- over_600_ratio: 69.18
- over_800_ratio: 67.52
- over_1000_ratio: 65.82
- over_400_change_1w: 0.02
- over_800_change_1w: 0.04
- over_1000_change_1w: 0.55
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,71.24,-0.6,68.29,-0.36,66.07,0.13,10,False,True
20260717,71.54,0.3,68.48,0.19,66.21,0.14,11,True,True
20260724,71.48,-0.06,68.2,-0.28,65.97,-0.24,0,False,False
20260731,71.19,-0.29,67.81,-0.39,66.24,0.27,1,False,True
20260807,71.52,0.33,68.29,0.48,66.97,0.73,2,True,True
20260814,71.88,0.36,68.53,0.24,67.45,0.48,3,True,True
20260821,71.99,0.11,68.73,0.2,67.65,0.2,4,True,True
20260828,71.75,-0.24,68.46,-0.27,67.38,-0.27,0,False,False
20260904,71.44,-0.31,67.88,-0.58,66.8,-0.58,0,False,False
20260911,70.89,-0.55,67.54,-0.34,65.57,-1.23,0,False,False
20260918,70.74,-0.15,67.48,-0.06,65.27,-0.3,0,False,False
20260924,70.76,0.02,67.52,0.04,65.82,0.55,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4707 | 磐亞 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 67.0 |  |  | neckline_challenge |  |  | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 富騰國際實業股份有限公司普通股 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易總金額：董事會決議以特定人身份認購新台幣3億元為限 每單位價格：每股30元溢價認購 交易數量：1,000萬股為限 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 富騰國際實業股份有限公司；非本公司關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依據現金&#22679;資認股協議書約定 12.本次交易之決定方式、價格決定之參考依據及決策單位: 依據富騰公司董事會決議辦理 13.取得或處分有價證券標的公司每股淨值: 11.69元 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 累積持有本交易證券(含本次交易)之數量：1,000萬股 累積持有本交易證券(含本次交易)之金額：新台幣3億元 持股比例：51.1% 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資占最近期財報總資產比例：75.42% 有價證券投資占最近期財報歸屬於母公司業主之權益比例：106.44% 最近期財報營運資金數額：-1,279,698仟元 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 股權投資 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 民國115年9月23日 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 安誠會計師事務所 23.會計師姓名: 陳靖玲 24.會計師開業證書字號: 北市會證字第943號 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 依公司核決權限、取處程序辦理。 富騰公司本次發行新股除依法保留百分之十由員工認購外， 其餘由原股東按原持股比例認購，逾期未認股或認購不足 之股份，該公司授權董事長洽由特定人認足之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 4707 | 磐亞 | 5 | 1 | 5 | 5 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
