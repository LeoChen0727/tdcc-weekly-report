# INDIVIDUAL STOCK CHATGPT PACKET - 2498 宏達電

## Metadata
- generated_at: 2026-09-26 22:16:24 Asia/Taipei
- stock_id: 2498
- stock_name: 宏達電
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2498_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2498_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2498_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2498_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2498_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2498_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2498_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2498.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2498.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2498.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2498.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2498_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2498_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2498_latest.md?ref=main

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
- date: 20260924
- open: 41.65
- high: 42.3
- low: 41.4
- close: 41.8
- volume: 7183755
- ma5: 40.64
- ema23_primary: 40.54
- distance_to_ema23_pct: 3.11
- ma20: 40.53
- ma60: 41.12
- ma120: 42.16
- return_5d: 4.89
- return_20d: 3.21
- volume_ratio: 1.25
- distance_to_ma20_pct_auxiliary: 3.12
- distance_to_high_60_pct: -11.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,40.65,41.25,40.4,40.55,2636413,40.68,-0.33,40.36,42.53,0.76
20260831,40.65,40.9,40.15,40.2,3277335,40.64,-1.09,40.38,42.41,0.93
20260901,40.7,41.9,40.45,40.9,4649290,40.67,0.58,40.41,42.32,1.32
20260902,40.9,42.2,40.3,41.65,5875912,40.75,2.21,40.48,42.31,1.66
20260903,41.3,43.3,41,41.6,12708286,40.82,1.91,40.52,42.28,3.18
20260904,42.35,42.55,41.6,41.6,9265593,40.88,1.75,40.61,42.28,2.15
20260907,41.7,41.9,41,41,4139799,40.89,0.26,40.62,42.26,0.96
20260908,41,41.45,40.2,40.2,3851454,40.84,-1.56,40.61,42.21,0.88
20260909,40.4,40.75,40.25,40.5,2128506,40.81,-0.75,40.61,42.12,0.49
20260910,40.4,40.6,40.15,40.15,1864450,40.75,-1.48,40.61,42.05,0.43
20260911,39.9,40.3,39.8,39.95,1980958,40.69,-1.81,40.59,41.93,0.47
20260914,39.9,40.25,39.85,39.9,1741906,40.62,-1.77,40.53,41.82,0.42
20260915,39.95,40.15,39.2,39.25,2667623,40.51,-3.1,40.52,41.63,0.66
20260916,39.45,40.5,39.45,40.2,3120072,40.48,-0.69,40.54,41.52,0.78
20260917,40.25,40.4,39.85,39.85,4471663,40.43,-1.43,40.53,41.41,1.16
20260918,40.2,40.25,39.55,39.55,10516652,40.35,-1.99,40.46,41.3,2.51
20260921,40,40.4,39.8,40.1,3173733,40.33,-0.58,40.44,41.26,0.75
20260922,40.4,40.75,39.65,40.1,4952959,40.31,-0.53,40.42,41.2,1.14
20260923,41.75,44,41.4,41.65,24654023,40.43,3.03,40.47,41.14,4.49
20260924,41.65,42.3,41.4,41.8,7183755,40.54,3.11,40.53,41.12,1.25
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 38.99
- over_600_ratio: 36.73
- over_800_ratio: 34.8
- over_1000_ratio: 33.46
- over_400_change_1w: -0.15
- over_800_change_1w: -0.22
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,39.33,-0.06,34.76,-0.53,33.82,0.12,1,False,True
20260717,39.22,-0.11,34.73,-0.03,33.78,-0.04,0,False,False
20260724,39.37,0.15,35.05,0.32,34.22,0.44,1,True,True
20260731,39.17,-0.2,35.01,-0.04,33.77,-0.45,0,False,False
20260807,39.45,0.28,35.3,0.29,34.48,0.71,1,True,True
20260814,39.54,0.09,35.27,-0.03,34.34,-0.14,2,False,False
20260821,39.32,-0.22,35.27,0,34.21,-0.13,3,False,False
20260828,39.56,0.24,35.56,0.29,34.32,0.11,4,True,True
20260904,39.61,0.05,35.66,0.1,34.29,-0.03,5,False,True
20260911,39.03,-0.58,34.95,-0.71,33.71,-0.58,0,False,False
20260918,39.14,0.11,35.02,0.07,33.45,-0.26,1,False,True
20260924,38.99,-0.15,34.8,-0.22,33.46,0.01,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2498 | 宏達電 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | call_put_bullish | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: Apollo Sports Capital Holdings (Overseas), L.P. 2.事實發生日:115/09/23 3.交易單位數量、每單位價格及交易總金額: 交易單位數量：不適用 每單位價格：不適用 交易總金額：不超過美金18,000,000元 4.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司 之關係人者，得免揭露其姓名）: Apollo Sports Capital Holdings (Overseas), L.P.; 非關係人 5.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及 前次移轉之所有人、前次移轉之所有人與公司及交易相對人間相互之 關係、前次移轉日期及移轉金額: 不適用 6.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告 關係人之取得及處分日期、價格及交易當時與公司之關係: 不適用 7.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分 債權如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人 之債權帳面金額: 不適用 8.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表 說明認列情形）: 不適用 9.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要 約定事項: 依合約規定 10.本次交易之決定方式、價格決定之參考依據及決策單位: 依合約規定；依本公司「取得或處分資產處理程序」規範之核決權限辦理 11.取得或處分有價證券標的公司每股淨值:不適用 12.有價證券標的公司私募參考價格與每股交易金額差距達20%以上:不適用 13.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、 持股比例及權利受限情形（如質押情形）: 累積持有之數量：不適用 累積持有之金額：美金18,000,000元 持股比例：不適用 權利受限情形：無 14.迄目前為止，私募有價證券投資（含本次交易）占公司最近期財 務報表中總資產及歸屬於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 佔總資產比例：19.65% 佔歸屬於母公司業主之權益比例：28.43% 營運資金數額：新台幣-7,051,317仟元 15.經理人及經紀費用: 無 16.取得或處分之具體目的或用途: 資金運用 17.本次交易表示異議董事之意見: 無 18.本次交易為關係人交易: 否 19.董事會通過日期: 不適用 20.監察人承認或審計委員會同意日期: 不適用 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 元和聯合會計師事務所 23.會計師姓名: 阮瓊華 24.會計師開業證書字號: 83台財證登(六)字第2719號 25.其他敘明事項: 上述台幣金額以美元兌新台幣匯率 1: 31.8750計算。實際數值將以交易當日為準。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2498 | 宏達電 | 1 | 1 | 1 | 1 | 5 | repeated_but_no_breakout | 近 10 日上榜 1 次、近 20 日上榜 5 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2498 | 宏達電 | 60 | 1 | 5701550.0 | 3040.0 | 1875.51 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
