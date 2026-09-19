# INDIVIDUAL STOCK CHATGPT PACKET - 3707 漢磊

## Metadata
- generated_at: 2026-09-19 15:53:28 Asia/Taipei
- stock_id: 3707
- stock_name: 漢磊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3707_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3707_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3707_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3707_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3707.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3707.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3707.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3707.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3707_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3707_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3707_latest.md?ref=main

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
- date: 20260918
- open: 62.6
- high: 63.3
- low: 62
- close: 62.9
- volume: 2541000
- ma5: 61.38
- ema23_primary: 61.91
- distance_to_ema23_pct: 1.6
- ma20: 61.73
- ma60: 66.44
- ma120: 68.61
- return_5d: 6.25
- return_20d: 2.61
- volume_ratio: 0.67
- distance_to_ma20_pct_auxiliary: 1.9
- distance_to_high_60_pct: -33.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,62.3,64.9,62,62,5546000,63.74,-2.73,60.21,72.81,1.16
20260825,61.8,62,59.7,62,2690000,63.59,-2.51,60.57,72.36,0.58
20260826,61.7,64.6,61.7,63.6,3672000,63.6,0.01,61.11,72.03,0.83
20260827,63.8,64.4,62.8,63.6,2087000,63.6,0.01,61.85,71.73,0.5
20260828,63.9,65.7,63.8,63.8,3668000,63.61,0.29,62.41,71.38,0.88
20260831,63.1,63.6,61.5,62.5,2777000,63.52,-1.61,62.73,71.13,0.69
20260901,62.5,64.5,62.5,63.2,2660000,63.49,-0.46,62.9,70.91,0.68
20260902,63,63.8,62.2,62.2,1990000,63.39,-1.87,62.88,70.77,0.54
20260903,62.6,63.4,60.5,60.5,3199000,63.15,-4.19,62.8,70.53,0.87
20260904,62,62.4,60.1,62,2418000,63.05,-1.66,62.9,70.36,0.66
20260907,62.8,63.1,61.1,61.2,2232000,62.9,-2.7,62.84,70.15,0.62
20260908,61.8,63.2,60,60,4869000,62.65,-4.24,62.75,69.86,1.3
20260909,60,60.6,59.8,60.1,2049000,62.44,-3.75,62.58,69.5,0.57
20260910,60.2,62.9,59.2,61.8,6674000,62.39,-0.94,62.39,69.2,1.91
20260911,60.6,60.6,58.4,59.2,5159000,62.12,-4.7,62.07,68.85,1.49
20260914,58.3,61.3,57.7,60.2,3436000,61.96,-2.84,61.82,68.47,1.03
20260915,60.4,62.3,58.9,58.9,4058000,61.71,-4.55,61.62,67.92,1.23
20260916,60.3,63,60,63,7055000,61.81,1.92,61.7,67.3,2.01
20260917,63.3,65.7,61.9,61.9,7086000,61.82,0.13,61.65,66.82,1.88
20260918,62.6,63.3,62,62.9,2541000,61.91,1.6,61.73,66.44,0.67
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 45.2
- over_600_ratio: 43.69
- over_800_ratio: 43.5
- over_1000_ratio: 42.37
- over_400_change_1w: 0.19
- over_800_change_1w: 0.18
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,50.5,-1.89,48.81,-2.09,47.68,-2.53,0,False,False
20260709,47.28,-3.22,46.01,-2.8,44.66,-3.02,0,False,False
20260717,46.66,-0.62,44.41,-1.6,43.29,-1.37,0,False,False
20260724,44.88,-1.78,43.37,-1.04,42.22,-1.07,0,False,False
20260731,45,0.12,43.64,0.27,42.12,-0.1,1,False,True
20260807,45.07,0.07,43.52,-0.12,41.98,-0.14,2,False,False
20260814,45.53,0.46,43.82,0.3,42.92,0.94,3,True,True
20260821,45.13,-0.4,43.54,-0.28,41.95,-0.97,0,False,False
20260828,45.21,0.08,43.79,0.25,42.47,0.52,1,True,True
20260904,45.29,0.08,43.57,-0.22,41.98,-0.49,2,False,False
20260911,45.01,-0.28,43.32,-0.25,42.2,0.22,3,False,True
20260918,45.2,0.19,43.5,0.18,42.37,0.17,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3707 | 漢磊 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.證券名稱: 嘉晶電子股份有限公司普通股 2.交易日期:115/6/29~115/6/29 3.董事會通過日期: 民國115年6月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 14,500,000股; NT$115.5;NT$1,675佰萬元 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分交易金額扣除成本後之差額約NT$1,420佰萬元，認列科目為資本公積， 尚待會計師查核相關程序及文件後確認。 7.與交易標的公司之關係: 本公司之子公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 152,461,680股；帳面價值NT$2,682佰萬元；52.8%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 12.9%；23.3%；NT$4,316佰萬元。 10.取得或處分之具體目的: 透過處分部分持股來活化資產，以因應未來產業波動或擴充核心業務的資金需求。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年6月26日 15.前已就同一件事件發布重大訊息日期: 115年6月26日 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 3707 | 漢磊 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | stale_signal | 1.證券名稱: 嘉晶電子股份有限公司普通股 2.交易日期:115/6/29~115/6/29 3.董事會通過日期: 民國115年6月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 14,500,000股; NT$115.5;NT$1,675佰萬元 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分交易金額扣除成本後之差額約NT$1,420佰萬元，認列科目為資本公積， 尚待會計師查核相關程序及文件後確認。 7.與交易標的公司之關係: 本公司之子公司 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 152,461,680股；帳面價值NT$2,682佰萬元；52.8%；無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 12.9%；23.3%；NT$4,316佰萬元。 10.取得或處分之具體目的: 透過處分部分持股來活化資產，以因應未來產業波動或擴充核心業務的資金需求。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 民國115年6月26日 15.前已就同一件事件發布重大訊息日期: 115年6月26日 16.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3707 | 漢磊 | 3 | 3 | 3 | 3 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
