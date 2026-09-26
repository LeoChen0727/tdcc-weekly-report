# INDIVIDUAL STOCK CHATGPT PACKET - 3490 單井

## Metadata
- generated_at: 2026-09-26 22:16:45 Asia/Taipei
- stock_id: 3490
- stock_name: 單井
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3490_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3490_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3490_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3490_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3490_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3490_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3490_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3490.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3490.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3490.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3490.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3490_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3490_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3490_latest.md?ref=main

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
- open: 44.1
- high: 46
- low: 43.75
- close: 45.05
- volume: 2499000
- ma5: 44.85
- ema23_primary: 43.98
- distance_to_ema23_pct: 2.43
- ma20: 44.68
- ma60: 38
- ma120: 35.47
- return_5d: -0.66
- return_20d: -16.57
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 0.82
- distance_to_high_60_pct: -22.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,54.3,54.8,49.8,50.3,6502000,42.5,18.35,40.9,34.41,1.2
20260831,48.1,50.2,45.3,45.5,6189000,42.75,6.43,41.76,34.54,1.1
20260901,45.7,46.3,44.3,46.15,4722000,43.03,7.24,42.65,34.7,0.82
20260902,46,46.45,43.9,46.05,4338000,43.29,6.39,43.52,34.89,0.74
20260903,46.5,47.45,44.8,44.95,3895000,43.42,3.51,44.28,35.06,0.65
20260904,45.65,46.8,45.2,46,2987000,43.64,5.41,45.06,35.29,0.51
20260907,46.25,47.2,45.1,46.15,3131000,43.85,5.25,45.79,35.53,0.54
20260908,45.85,46.3,43.4,43.45,3053000,43.82,-0.83,46.36,35.72,0.53
20260909,43.55,44.75,43.5,44.2,1392000,43.85,0.8,46.9,35.89,0.25
20260910,43.5,43.55,40.8,40.85,2932000,43.6,-6.3,47.1,36.02,0.53
20260911,40.85,43.35,40.15,41.55,3576000,43.43,-4.32,47.19,36.16,0.7
20260914,41.05,43.55,40.75,42.1,2830000,43.32,-2.81,47.17,36.32,0.6
20260915,42.1,43.8,41.75,42,5425000,43.21,-2.79,47.05,36.47,1.22
20260916,42,45.5,41.45,44.8,6905000,43.34,3.37,46.95,36.67,1.65
20260917,45.5,46.2,44.5,45.35,5251000,43.51,4.24,46.76,36.88,1.23
20260918,45.35,45.75,43.85,44.35,3981000,43.58,1.77,46.28,37.09,0.92
20260921,44.35,46,44.3,45.2,3205000,43.71,3.4,46.06,37.34,0.76
20260922,46,46,44.55,45.5,3058000,43.86,3.74,45.6,37.59,0.73
20260923,45.65,45.95,44.1,44.15,2384000,43.89,0.6,45.13,37.82,0.58
20260924,44.1,46,43.75,45.05,2499000,43.98,2.43,44.68,38,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 24.77
- over_600_ratio: 21.32
- over_800_ratio: 19.07
- over_1000_ratio: 19.07
- over_400_change_1w: 0.55
- over_800_change_1w: 1.08
- over_1000_change_1w: 2.8
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,16.27,-1.17,13.68,1.64,12.07,0.03,1,False,True
20260717,16.03,-0.24,12.07,-1.61,12.07,0,0,False,False
20260724,15.93,-0.1,12.07,0,12.07,0,1,False,False
20260731,17.15,1.22,14.26,2.19,14.26,2.19,2,True,True
20260807,16.98,-0.17,14.16,-0.1,14.16,-0.1,0,False,False
20260814,15.72,-1.26,12.1,-2.06,12.1,-2.06,0,False,False
20260821,27.55,11.83,19.87,7.77,19.87,7.77,1,True,True
20260828,29.94,2.39,20.68,0.81,19.22,-0.65,2,False,True
20260904,27.51,-2.43,15.85,-4.83,14.04,-5.18,0,False,False
20260911,27.89,0.38,18.94,3.09,18.94,4.9,1,True,True
20260918,24.22,-3.67,17.99,-0.95,16.27,-2.67,0,False,False
20260924,24.77,0.55,19.07,1.08,19.07,2.8,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3490 | 單井 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.證券名稱: Micron Technology, Inc. (MU-US)普通股 2.交易日期:115/1/30~115/9/22 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年1月30日 5.交易數量、每單位價格及交易總金額: 最近一年累積處分交易數量：5,550股 最近一年累積處分每單位價格：美金663.9666144元 最近一年累積處分交易總金額：美金3,685,014.71元(折合新臺幣115,705,051元) 6.處分利益（或損失）（取得有價證券者不適用）: 處份利益：新台幣16,689,772元 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 迄目前為止持有數量:230股 迄目前為止持有金額:美金210,571.70元(折合新臺幣6,631,483元) 迄目前為止持股比例:0.0000204% 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例:48.72% 占歸屬於母公司業主之權益比例:52.32% 營運資金數額:新臺幣 137,058仟元 10.取得或處分之具體目的: 財務投資 11.本次交易表示異議董事之意見: 無 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 無 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 本投資交易帳列透過損益按公允價值衡量之金融資產；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3490 | 單井 | 6 | 6 | 5 | 8 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
