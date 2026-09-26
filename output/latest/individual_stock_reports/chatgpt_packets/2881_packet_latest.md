# INDIVIDUAL STOCK CHATGPT PACKET - 2881 富邦金

## Metadata
- generated_at: 2026-09-26 22:16:31 Asia/Taipei
- stock_id: 2881
- stock_name: 富邦金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2881_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2881_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2881_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2881_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2881_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2881_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2881_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2881.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2881.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2881.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2881.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2881_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2881_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2881_latest.md?ref=main

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
- open: 151.5
- high: 153
- low: 150
- close: 150
- volume: 8417116
- ma5: 152.5
- ema23_primary: 147.25
- distance_to_ema23_pct: 1.87
- ma20: 149.43
- ma60: 134.96
- ma120: 120.1
- return_5d: -0.99
- return_20d: 6.01
- volume_ratio: 0.48
- distance_to_ma20_pct_auxiliary: 0.38
- distance_to_high_60_pct: -4.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,141,144.5,140.5,144,16595185,132.15,8.97,131.25,128.17,0.84
20260831,143,145,142,144,33320565,133.13,8.16,131.97,128.67,1.64
20260901,143.5,145,141.5,145,19553535,134.12,8.11,132.8,129.12,0.99
20260902,144.5,145,142.5,143.5,13285257,134.9,6.37,133.5,129.57,0.67
20260903,144,148.5,143,147,20256586,135.91,8.16,134.55,129.94,1.03
20260904,147.5,151.5,147,150.5,19146551,137.13,9.75,135.72,130.41,0.95
20260907,155,155.5,148,149.5,21676639,138.16,8.21,136.78,130.81,1.05
20260908,149.5,150.5,148,149,12457783,139.06,7.15,137.82,131.26,0.6
20260909,148.5,149,145,147,16660623,139.72,5.21,138.82,131.58,0.79
20260910,146,149,146,148.5,12504942,140.45,5.73,139.82,131.86,0.59
20260911,146,148.5,144,148.5,10662888,141.13,5.23,140.78,132.07,0.5
20260914,146.5,154.5,146,154,19008138,142.2,8.3,142.2,132.34,0.91
20260915,154,154.5,149.5,151,15894184,142.93,5.64,143.28,132.55,0.77
20260916,152,153,150,153,20793317,143.77,6.42,144.5,132.81,0.99
20260917,153,154.5,151,151.5,14045882,144.41,4.91,145.68,133.09,0.68
20260918,152.5,152.5,148,150.5,28248424,144.92,3.85,146.5,133.33,1.39
20260921,150.5,156,149.5,154.5,15221165,145.72,6.03,147.62,133.68,0.75
20260922,156.5,156.5,153.5,154.5,17070787,146.45,5.5,148.28,134.11,0.91
20260923,155.5,155.5,152.5,153,14875887,147,4.08,149,134.5,0.82
20260924,151.5,153,150,150,8417116,147.25,1.87,149.43,134.96,0.48
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 86.8
- over_600_ratio: 85.88
- over_800_ratio: 85.17
- over_1000_ratio: 84.6
- over_400_change_1w: 0.02
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,86.33,0.02,84.63,-0.03,84.17,-0.02,1,False,False
20260717,86.32,-0.01,84.63,0,84.15,-0.02,0,False,False
20260724,86.38,0.06,84.69,0.06,84.17,0.02,1,True,True
20260731,86.44,0.06,84.78,0.09,84.23,0.06,2,True,True
20260807,86.45,0.01,84.79,0.01,84.28,0.05,3,True,True
20260814,86.46,0.01,84.8,0.01,84.26,-0.02,4,False,True
20260821,86.49,0.03,84.82,0.02,84.28,0.02,5,True,True
20260828,86.66,0.17,84.98,0.16,84.42,0.14,6,True,True
20260904,86.72,0.06,85.04,0.06,84.5,0.08,7,True,True
20260911,86.77,0.05,85.11,0.07,84.56,0.06,8,True,True
20260918,86.78,0.01,85.15,0.04,84.58,0.02,9,True,True
20260924,86.8,0.02,85.17,0.02,84.6,0.02,10,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2881 | 富邦金 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: Bayfront IABS IX Pte. Ltd發行之資產基礎證券 2.事實發生日:115/9/22~115/9/22 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:執行信貸委員會 民國115年9月21日 5.交易數量、每單位價格及交易總金額: 單位數量：無 每單位價格：無 交易總金額：美金21,000,000元（更新） 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: SOCIETE GENERALE SA, 非實質關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交付或付款條件：於交割日一次付清交付 契約限制條款：無 其他重要約定事項：無 12.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易之決定方式：根據證券發行條款 價格決定之參考依據：依市場價格行情決定 決策單位：依本公司核決權限辦理 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 金控：無 富邦銀行（香港）數量：無 金額：美金21,000,000元（更新） 持股比例及權利受限情形：無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 佔富邦金控：24.51%; 29.64%; 不適用（更新） 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 投資於具有永續性要素的資產基礎證券，以獲得合理的回報 18.本次交易表示異議董事之意見: 不適用 19.本次交易為關係人交易:否 20.監察人承認或審計委員會同意日期: 不適用 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 過去一年：透過同一交易相對人認購資產基礎證券, 分別為 1.114年11月18日認購Bayfront IABS VII Pte Ltd 發行之 資產基礎證券美金30,000,000元; 2.115年4月28日認購Bayfront IABS VIII Pte Ltd 發行之 資產基礎證券美金40,000,000元 未來一年：將視市場情況及本公司策略而定 28.資金來源: 營運資金 29.前已就同一件事件發布重大訊息日期: 115年9月21日 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2881 | 富邦金 | 4 | 4 | 4 | 6 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2881 | 富邦金 | 46 | 1 | 1663440.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
