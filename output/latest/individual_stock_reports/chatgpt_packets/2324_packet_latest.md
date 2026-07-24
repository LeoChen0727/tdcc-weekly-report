# INDIVIDUAL STOCK CHATGPT PACKET - 2324 仁寶

## Metadata
- generated_at: 2026-07-24 22:26:41 Asia/Taipei
- stock_id: 2324
- stock_name: 仁寶
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
- individual_report_md_exists: True
- sell_strategy_summary_exists: True
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2324_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2324_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2324_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2324_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2324_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2324_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2324_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2324.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2324.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2324.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2324.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2324_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2324_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2324_latest.md?ref=main

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
- open: 35.6
- high: 36.95
- low: 35.2
- close: 36
- volume: 100499425
- ma5: 36.06
- ema23_primary: 35.95
- distance_to_ema23_pct: 0.14
- ma20: 35.93
- ma60: 34.35
- ma120: 32.61
- return_5d: -1.64
- return_20d: -3.49
- volume_ratio: 1.77
- distance_to_ma20_pct_auxiliary: 0.19
- distance_to_high_60_pct: -24.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,37.8,38.45,37.25,37.75,71745861,36.53,3.33,37.79,32.25,0.39
20260622,38.1,39.2,37.5,37.5,92199498,36.61,2.42,38.09,32.35,0.51
20260623,37.8,38,36.2,36.55,62365832,36.61,-0.16,38.19,32.43,0.37
20260624,36.25,38.4,36.2,37.9,88993364,36.72,3.23,38.4,32.54,0.55
20260625,37.9,38.7,36.85,36.85,65609405,36.73,0.33,38.57,32.65,0.41
20260626,36.4,36.45,34.6,34.8,80548337,36.57,-4.83,38.64,32.76,0.52
20260629,34.75,35.05,34.05,34.2,55785591,36.37,-5.96,38.51,32.88,0.45
20260630,34.85,35.4,34.1,35.3,42524912,36.28,-2.7,38.26,33.01,0.36
20260701,35.5,36.3,34.3,34.6,45261664,36.14,-4.26,37.77,33.13,0.4
20260702,34.15,34.8,34,34.8,33762393,36.03,-3.41,37.16,33.26,0.36
20260703,34.6,35,34.3,34.95,38900932,35.94,-2.75,36.79,33.38,0.47
20260706,35.35,36.7,35.1,35.7,54803161,35.92,-0.61,36.51,33.52,0.72
20260707,36.1,36.3,35.05,35.3,38830036,35.87,-1.58,36.34,33.64,0.55
20260708,35.3,35.5,34.85,35.5,23005012,35.84,-0.94,36.19,33.74,0.36
20260709,36.1,37.65,36.1,36.6,69252207,35.9,1.95,36.17,33.86,1.14
20260713,37.95,38.2,36.2,36.65,64219539,35.96,1.91,36.19,33.98,1.08
20260714,36.8,36.85,34.7,35.55,45695887,35.93,-1.05,36.15,34.09,0.79
20260715,35.75,36.65,35.4,36.15,33170793,35.95,0.57,36.07,34.18,0.6
20260716,36,36.5,35.6,35.95,28718535,35.95,0.01,35.99,34.28,0.53
20260717,35.6,36.95,35.2,36,100499425,35.95,0.14,35.93,34.35,1.77
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 62.75
- over_600_ratio: 61.1
- over_800_ratio: 60
- over_1000_ratio: 59.06
- over_400_change_1w: 0.37
- over_800_change_1w: 0.41
- over_1000_change_1w: 0.48
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.75,,64.96,,63.89,,0,False,False
20260508,67.21,-0.54,64.52,-0.44,63.25,-0.64,0,False,False
20260515,67.2,-0.01,64.45,-0.07,63.29,0.04,1,False,True
20260522,65.9,-1.3,62.97,-1.48,61.87,-1.42,0,False,False
20260529,66.02,0.12,63.14,0.17,61.99,0.12,1,True,True
20260605,64.3,-1.72,61.63,-1.51,60.64,-1.35,0,False,False
20260612,63.87,-0.43,61.3,-0.33,60.4,-0.24,0,False,False
20260618,63.73,-0.14,61.09,-0.21,60.21,-0.19,0,False,False
20260626,62.77,-0.96,60.06,-1.03,59.18,-1.03,0,False,False
20260703,62.07,-0.7,59.34,-0.72,58.38,-0.8,0,False,False
20260709,62.38,0.31,59.59,0.25,58.58,0.2,1,True,True
20260717,62.75,0.37,60,0.41,59.06,0.48,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2324 | 仁寶 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | call_inflow | stale_signal | 1.證券名稱: 台灣大 2.交易日期:115/6/2~115/6/10 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年5月28日 5.交易數量、每單位價格及交易總金額: 3,197,294股；115元；新台幣367,682,000元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益50,510,435元(帳入保留盈餘) 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 0股；0元；-%；無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 總資產比例：35.46%；股東權益比例：107.50%； 營運資金數額；3,048,110,000元 10.取得或處分之具體目的: 營運資金規劃 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2324 | 仁寶 | pullback_rebound | 回檔後短線轉強 | 63.0 |  |  |  |  | call_inflow | stale_signal | 1.證券名稱: 台灣大 2.交易日期:115/6/2~115/6/10 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年5月28日 5.交易數量、每單位價格及交易總金額: 3,197,294股；115元；新台幣367,682,000元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益50,510,435元(帳入保留盈餘) 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 0股；0元；-%；無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 總資產比例：35.46%；股東權益比例：107.50%； 營運資金數額；3,048,110,000元 10.取得或處分之具體目的: 營運資金規劃 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2324 | 仁寶 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | call_inflow | stale_signal | 1.證券名稱: 台灣大 2.交易日期:115/6/2~115/6/10 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年5月28日 5.交易數量、每單位價格及交易總金額: 3,197,294股；115元；新台幣367,682,000元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益50,510,435元(帳入保留盈餘) 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 0股；0元；-%；無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 總資產比例：35.46%；股東權益比例：107.50%； 營運資金數額；3,048,110,000元 10.取得或處分之具體目的: 營運資金規劃 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2324 | 仁寶 | 6 | 3 | 5 | 7 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2324 | 仁寶 | 97 | 4 | 9274900.0 | 26640.0 | 348.16 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
