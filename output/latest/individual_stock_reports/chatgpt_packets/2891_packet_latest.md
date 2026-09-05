# INDIVIDUAL STOCK CHATGPT PACKET - 2891 中信金

## Metadata
- generated_at: 2026-09-05 22:16:14 Asia/Taipei
- stock_id: 2891
- stock_name: 中信金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2891_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2891_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2891_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2891_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2891_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2891_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2891_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2891.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2891.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2891.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2891.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2891_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2891_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2891_latest.md?ref=main

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
- open: 67.3
- high: 68.4
- low: 66.7
- close: 68.4
- volume: 29198109
- ma5: 66.74
- ema23_primary: 65.61
- distance_to_ema23_pct: 4.25
- ma20: 65.61
- ma60: 66.61
- ma120: 61.28
- return_5d: 6.21
- return_20d: 4.27
- volume_ratio: 0.88
- distance_to_ma20_pct_auxiliary: 4.25
- distance_to_high_60_pct: -7.07

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,65.8,66.5,64.9,66.5,22731119,65.09,2.17,63.83,65.28,0.5
20260811,67,67.3,66.3,66.8,28839763,65.23,2.41,63.92,65.48,0.67
20260812,66.3,67,65.5,66.6,39347639,65.34,1.92,64.08,65.68,0.96
20260813,66.3,66.5,65.2,66.5,27983908,65.44,1.62,64.25,65.86,0.7
20260814,66.9,67.2,65.2,65.8,26085471,65.47,0.5,64.44,66,0.71
20260817,66.3,66.3,65.2,65.6,26449448,65.48,0.18,64.64,66.13,0.76
20260818,66.2,66.5,65.9,66.5,26516862,65.57,1.43,64.83,66.28,0.79
20260819,66.4,66.4,64.7,64.9,34561497,65.51,-0.93,64.88,66.41,1.03
20260820,65,65.2,62.1,63.4,60861192,65.33,-2.96,64.87,66.5,1.75
20260821,63.7,65.5,63,65,51685764,65.31,-0.47,64.94,66.6,1.42
20260824,64.9,65.6,63.6,63.6,17542213,65.16,-2.4,64.97,66.67,0.49
20260825,63.1,64.7,63.1,64.5,21957765,65.11,-0.94,65.08,66.74,0.63
20260826,64,65.3,63.9,64.6,28409411,65.07,-0.72,65.2,66.78,0.84
20260827,64.6,65.1,63.8,63.8,25965855,64.96,-1.79,65.24,66.77,0.79
20260828,63.8,64.6,63.7,64.4,33878789,64.91,-0.79,65.22,66.67,1.05
20260831,63.5,65,63.5,64.7,40176473,64.9,-0.3,65.21,66.62,1.25
20260901,65.5,66.5,65.1,66.5,39727859,65.03,2.26,65.3,66.61,1.24
20260902,65.8,66.7,65.4,66.6,40072437,65.16,2.21,65.33,66.64,1.24
20260903,66.6,68,66.3,67.5,44127663,65.36,3.28,65.47,66.61,1.35
20260904,67.3,68.4,66.7,68.4,29198109,65.61,4.25,65.61,66.61,0.88
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 81.88
- over_600_ratio: 80.68
- over_800_ratio: 79.77
- over_1000_ratio: 79.07
- over_400_change_1w: 0.13
- over_800_change_1w: 0.16
- over_1000_change_1w: 0.15
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,82.13,0.02,80.13,0.02,79.39,0.02,1,True,True
20260626,82.11,-0.02,80.05,-0.08,79.34,-0.05,0,False,False
20260703,82.19,0.08,80.16,0.11,79.44,0.1,1,True,True
20260709,82.24,0.05,80.18,0.02,79.47,0.03,2,True,True
20260717,81.81,-0.43,79.71,-0.47,78.99,-0.48,0,False,False
20260724,81.73,-0.08,79.61,-0.1,78.88,-0.11,0,False,False
20260731,81.78,0.05,79.66,0.05,78.95,0.07,1,True,True
20260807,81.83,0.05,79.72,0.06,79,0.05,2,True,True
20260814,81.84,0.01,79.71,-0.01,78.98,-0.02,3,False,False
20260821,81.76,-0.08,79.64,-0.07,78.92,-0.06,0,False,False
20260828,81.75,-0.01,79.61,-0.03,78.92,0,0,False,False
20260904,81.88,0.13,79.77,0.16,79.07,0.15,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2891 | 中信金 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: LIGHTSPEED PLATINUM, L.P.；為私募基金 2.事實發生日:115/09/03 3.交易單位數量、每單位價格及交易總金額: 不適用、不適用、3百萬美元 4.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司 之關係人者，得免揭露其姓名）: Lightspeed Platinum General Partner, L.P.、非關係人 5.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及 前次移轉之所有人、前次移轉之所有人與公司及交易相對人間相互之 關係、前次移轉日期及移轉金額: 不適用 6.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告 關係人之取得及處分日期、價格及交易當時與公司之關係: 不適用 7.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分 債權如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人 之債權帳面金額: 不適用 8.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表 說明認列情形）: 不適用 9.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要 約定事項: 交付或付款條件（含付款期間及金額）：依合約約定辦理； 契約限制條款及其他重要約定事項：依合約約定辦理 10.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易之決定方式、價格決定之參考依據：依合約約定辦理 決策單位：依本公司核決權限 11.取得或處分有價證券標的公司每股淨值:不適用 12.有價證券標的公司私募參考價格與每股交易金額差距達20%以上:不適用 13.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、 持股比例及權利受限情形（如質押情形）: 母公司：無持有此交易證券 本公司：不適用、3百萬美元、預計約0.5%、無 子公司：無持有此交易證券 14.迄目前為止，私募有價證券投資（含本次交易）占公司最近期財 務報表中總資產及歸屬於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 佔總資產比例3%、佔歸屬於母公司業主之權益比例19%、 營運資金：不適用 15.經理人及經紀費用: 不適用 16.取得或處分之具體目的或用途: 依保險法之規定，為壽險資金之運用 17.本次交易表示異議董事之意見: 不適用 18.本次交易為關係人交易: 否 19.董事會通過日期: 不適用，非屬董事會核決權限 20.監察人承認或審計委員會同意日期: 不適用，非屬董事會核決權限 21.本次交易會計師出具非合理性意見:否 22.會計師事務所名稱: 青田會計師事務所 23.會計師姓名: 許明雄 24.會計師開業證書字號: 北市會證字第3723號 25.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2891 | 中信金 | 4 | 1 | 4 | 4 | 8 | repeated_but_no_breakout | 近 10 日上榜 4 次、近 20 日上榜 8 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2891 | 中信金 | 25 | 0 | 3737600.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
