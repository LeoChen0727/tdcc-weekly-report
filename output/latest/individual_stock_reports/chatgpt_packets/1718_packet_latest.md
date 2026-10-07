# INDIVIDUAL STOCK CHATGPT PACKET - 1718 中纖

## Metadata
- generated_at: 2026-10-07 22:17:03 Asia/Taipei
- stock_id: 1718
- stock_name: 中纖
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1718_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1718_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1718_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1718_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1718.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1718.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1718.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1718.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1718_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1718_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1718_latest.md?ref=main

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
- date: 20261002
- open: 10.6
- high: 10.85
- low: 10.6
- close: 10.75
- volume: 10159044
- ma5: 10.66
- ema23_primary: 10.66
- distance_to_ema23_pct: 0.84
- ma20: 10.62
- ma60: 11.03
- ma120: 9.68
- return_5d: 1.42
- return_20d: -0.46
- volume_ratio: 0.87
- distance_to_ma20_pct_auxiliary: 1.27
- distance_to_high_60_pct: -28.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,10.85,11.25,10.65,10.7,20408995,10.76,-0.55,10.66,11.2,0.81
20260904,10.8,10.8,10.45,10.6,17782501,10.75,-1.36,10.7,11.23,0.72
20260907,10.75,10.75,10.4,10.45,11225884,10.72,-2.53,10.71,11.25,0.48
20260908,10.45,10.45,10.25,10.4,9237489,10.69,-2.75,10.72,11.27,0.4
20260909,10.5,10.95,10.5,10.85,22005620,10.71,1.33,10.7,11.3,1
20260910,10.8,10.8,10.6,10.6,11453593,10.7,-0.92,10.68,11.32,0.61
20260911,10.6,10.7,10.35,10.4,12521222,10.67,-2.56,10.65,11.33,0.69
20260914,10.35,10.65,10.2,10.55,10779539,10.66,-1.06,10.65,11.34,0.61
20260915,10.6,10.6,10.3,10.4,6493005,10.64,-2.27,10.64,11.35,0.38
20260916,10.4,10.6,10.4,10.5,6566522,10.63,-1.22,10.64,11.37,0.4
20260917,10.55,11,10.5,10.9,20789291,10.65,2.33,10.67,11.4,1.22
20260918,11.05,11.05,10.6,10.6,13481923,10.65,-0.45,10.67,11.41,0.79
20260921,10.6,10.85,10.6,10.75,8391918,10.66,0.88,10.67,11.4,0.5
20260922,10.85,10.9,10.65,10.7,10222817,10.66,0.38,10.67,11.38,0.62
20260923,10.7,10.85,10.6,10.6,6181247,10.65,-0.51,10.66,11.33,0.39
20260924,10.6,10.6,10.4,10.5,5447791,10.64,-1.33,10.65,11.3,0.37
20260929,10.5,10.7,10.5,10.55,5005317,10.63,-0.79,10.64,11.25,0.35
20260930,10.6,10.95,10.55,10.85,16182557,10.65,1.86,10.64,11.18,1.11
20261001,10.8,10.9,10.55,10.65,10229352,10.65,-0.02,10.62,11.1,0.85
20261002,10.6,10.85,10.6,10.75,10159044,10.66,0.84,10.62,11.03,0.87
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 52.98
- over_600_ratio: 51.03
- over_800_ratio: 49.47
- over_1000_ratio: 48.14
- over_400_change_1w: 0.19
- over_800_change_1w: 0.26
- over_1000_change_1w: 0.27
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,53.89,0.89,50.25,0.73,49.41,0.73,1,True,True
20260724,53.1,-0.79,49.37,-0.88,48.42,-0.99,0,False,False
20260731,53.6,0.5,49.76,0.39,48.7,0.28,1,True,True
20260807,50.7,-2.9,46.97,-2.79,45.97,-2.73,0,False,False
20260814,50.67,-0.03,46.85,-0.12,45.84,-0.13,1,False,False
20260821,51.03,0.36,47.2,0.35,46.04,0.2,2,True,True
20260828,51.44,0.41,47.8,0.6,46.48,0.44,3,True,True
20260904,51.42,-0.02,47.78,-0.02,46.35,-0.13,0,False,False
20260911,51.83,0.41,48.29,0.51,46.9,0.55,1,True,True
20260918,52.67,0.84,49.18,0.89,47.8,0.9,2,True,True
20260924,52.79,0.12,49.21,0.03,47.87,0.07,3,True,True
20261002,52.98,0.19,49.47,0.26,48.14,0.27,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1718 | 中纖 | pattern | 型態觀察 | 51.0 |  |  | base_building |  | no_signal | repeated_but_no_breakout | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：高雄市小港區中林子段1086號。 建物：高雄市小港區大業南路22號（中林子段158-1、158-2建號）。 2.事實發生日:115/8/10~115/8/10 3.董事會通過日期: 民國115年8月10日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 土地面積：10,942.00平方公尺，折合3309.96坪。 建物面積：5,370.88平方公尺，折合1624.69坪。 交易總金額：新台幣724,741,000元。 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易對象：壹東實業股份有限公司 與公司之關係：非本公司之關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 295,152,648元 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依合約內容履行。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易之決定方式 : 議價。 價格依據：參考專業估價機構之估價金額及市場行情等因素。 決策單位：經董事會授權董事長全權處理。 12.專業估價者事務所或公司名稱及其估價金額: 宏邦不動產估價師聯合事務所，估價金額：新台幣718,051,778元。 13.專業估價師姓名: 李青塘 14.專業估價師開業證書字號: (108)北市估字第000278號 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 經紀人：台慶不動產 經紀費用：依合約規定 23.取得或處分之具體目的或用途: 活化資產 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 民國115年8月10日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1718 | 中纖 | 1 | 1 | 2 | 4 | 8 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 8 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 1718 | 中纖 | 19 | 0 | 1149610.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
