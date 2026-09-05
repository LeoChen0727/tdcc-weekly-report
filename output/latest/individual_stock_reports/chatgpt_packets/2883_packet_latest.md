# INDIVIDUAL STOCK CHATGPT PACKET - 2883 凱基金

## Metadata
- generated_at: 2026-09-05 15:53:03 Asia/Taipei
- stock_id: 2883
- stock_name: 凱基金
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2883_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2883_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2883_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2883.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2883.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2883.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2883.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2883_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2883_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2883_latest.md?ref=main

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
- open: 36.4
- high: 36.7
- low: 35.95
- close: 36.7
- volume: 42802542
- ma5: 35.38
- ema23_primary: 32.68
- distance_to_ema23_pct: 12.31
- ma20: 32.4
- ma60: 30.68
- ma120: 26.22
- return_5d: 12.06
- return_20d: 18.96
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: 13.29
- distance_to_high_60_pct: -0.14

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,31,31.05,30.35,31.05,30373456,30.13,3.05,30.29,27.9,0.62
20260811,30.8,31.2,30.65,31.05,21437999,30.21,2.79,30.36,28.05,0.45
20260812,31,31.4,30.55,31.2,29200840,30.29,3.01,30.41,28.22,0.62
20260813,31.4,31.5,30.85,31.5,34357307,30.39,3.65,30.46,28.38,0.74
20260814,31.25,31.75,30.95,31.65,58718628,30.5,3.79,30.55,28.55,1.26
20260817,31.5,31.65,30.9,31.4,52124434,30.57,2.71,30.64,28.72,1.14
20260818,31.1,31.35,30.85,30.95,50381336,30.6,1.14,30.7,28.87,1.09
20260819,30.7,30.85,30.3,30.4,41106180,30.59,-0.61,30.7,29.02,0.91
20260820,30.7,30.7,30.05,30.4,26497717,30.57,-0.56,30.68,29.16,0.6
20260821,30.4,31.55,30.3,31.55,49167372,30.65,2.93,30.72,29.32,1.09
20260824,31.75,31.95,30.7,31,36847710,30.68,1.04,30.73,29.47,0.81
20260825,31,31.7,30.9,31.7,37151287,30.77,3.04,30.84,29.62,0.83
20260826,31.65,33.1,31.6,32.25,65204736,30.89,4.41,31,29.78,1.45
20260827,32.75,33,32.15,32.15,35842285,30.99,3.73,31.16,29.93,0.8
20260828,32.5,32.8,32.15,32.75,20878621,31.14,5.17,31.25,30.04,0.51
20260831,32.7,33.85,32.55,33.85,104070641,31.37,7.92,31.42,30.15,2.4
20260901,33.9,35.1,33.9,34.95,63652325,31.67,10.37,31.64,30.27,1.42
20260902,34.85,35.6,34.6,35.5,47214212,31.98,10.99,31.84,30.42,1.08
20260903,35.65,36.75,35.6,35.9,60617343,32.31,11.11,32.1,30.53,1.36
20260904,36.4,36.7,35.95,36.7,42802542,32.68,12.31,32.4,30.68,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 69.04
- over_600_ratio: 67.31
- over_800_ratio: 66.23
- over_1000_ratio: 65.27
- over_400_change_1w: 0.21
- over_800_change_1w: 0.24
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,67.69,0.1,64.86,0.11,63.93,0.06,4,True,True
20260626,67.59,-0.1,64.72,-0.14,63.78,-0.15,0,False,False
20260703,67.26,-0.33,64.28,-0.44,63.32,-0.46,0,False,False
20260709,67.7,0.44,64.75,0.47,63.82,0.5,1,True,True
20260717,67.79,0.09,64.81,0.06,63.84,0.02,2,True,True
20260724,68.07,0.28,65.15,0.34,64.18,0.34,3,True,True
20260731,68.08,0.01,65.17,0.02,64.22,0.04,4,True,True
20260807,68.41,0.33,65.51,0.34,64.57,0.35,5,True,True
20260814,68.55,0.14,65.64,0.13,64.68,0.11,6,True,True
20260821,68.55,0,65.64,0,64.66,-0.02,0,False,False
20260828,68.83,0.28,65.99,0.35,65.01,0.35,1,True,True
20260904,69.04,0.21,66.23,0.24,65.27,0.26,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2883 | 凱基金 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  | no_signal | continued_2_3d | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: 「中華開發參號大健康創業投資有限合夥」（名稱暫定，下稱「開發參號大健康基金」） 之有限合夥權益。 2.事實發生日:115/08/31 3.交易單位數量、每單位價格及交易總金額: 標的物為有限合夥權益，無交易數量及每單位價格；交易金額中華開發資本管理顧問股 份有限公司（下稱「資本管顧」）以基金出資總額1%（含）為上限、中華開發創業投資股 份有限公司（下稱「開發創投」）以基金出資總額30%（含）為上限，二者合計以基金出 資總額31%（含）或新臺幣9.3億元（含）孰低者為上限參與投資。 4.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司 之關係人者，得免揭露其姓名）: 交易相對人：擬新設立之「開發參號大健康基金」； 與公司之關係：該基金設立後為財報關係人。 5.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及 前次移轉之所有人、前次移轉之所有人與公司及交易相對人間相互之 關係、前次移轉日期及移轉金額: 無前次移轉。 6.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告 關係人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 7.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分 債權如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人 之債權帳面金額: 不適用。 8.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表 說明認列情形）: 不適用。 9.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要 約定事項: 依基金相關協議之約定。 10.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易之決定方式、價格決定之參考依據：依基金相關協議之約定；決策單位： 董事會。 11.取得或處分有價證券標的公司每股淨值:不適用 12.有價證券標的公司私募參考價格與每股交易金額差距達20%以上:不適用 13.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、 持股比例及權利受限情形（如質押情形）: 標的為有限合夥權益，故無交易數量；累積持有本交易證券(含本次交易)之金額及出資 比例：資本管顧以基金出資總額1%（含）為上限、開發創投以基金出資總額30%（含） 為上限，二者合計以基金出資總額31%（含）或新臺幣9.3億元（含）孰低者為上限； 權利受限情形：無。 14.迄目前為止，私募有價證券投資（含本次交易）占公司最近期財 務報表中總資產及歸屬於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 資本管顧、開發創投: 占總資產比例：0.03%、0.62%；占母公司業主之權益比例：0.03%、0.74%；最近期財 務報告營運資金：不適用。 15.經理人及經紀費用: 不適用。 16.取得或處分之具體目的或用途: 投資業務發展需要。 17.本次交易表示異議董事之意見: 無。 18.本次交易為關係人交易: 是 19.董事會通過日期: 20260831 20.監察人承認或審計委員會同意日期: 不適用，依金融控股公司法第45條程序辦理。 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用。 23.會計師姓名: 不適用。 24.會計師開業證書字號: 不適用。 25.其他敘明事項: 前於114年3月7日公告投資開發參號大健康基金，相關投資條件經開發創投及資本管顧董 事會重新檢視後有所調整，二者合計投資上限更新為基金出資總額31%（含）或新臺幣9.3 億元（含）孰低者，爰依規定辦理公告更新。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2883 | 凱基金 | 2 | 2 | 4 | 9 | 18 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2883 | 凱基金 | 27 | 0 | 8801360.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
