# INDIVIDUAL STOCK CHATGPT PACKET - 3673 TPK-KY

## Metadata
- generated_at: 2026-09-05 15:53:28 Asia/Taipei
- stock_id: 3673
- stock_name: TPK-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3673_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3673_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3673_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3673_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3673_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3673_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3673_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3673.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3673.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3673.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3673.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3673_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3673_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3673_latest.md?ref=main

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
- date: 20260904
- open: 66
- high: 67.2
- low: 64.7
- close: 65.5
- volume: 2734304
- ma5: 66.64
- ema23_primary: 65.13
- distance_to_ema23_pct: 0.57
- ma20: 64.49
- ma60: 69.38
- ma120: 66.48
- return_5d: -3.11
- return_20d: 8.44
- volume_ratio: 0.53
- distance_to_ma20_pct_auxiliary: 1.57
- distance_to_high_60_pct: -28.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,61.2,64.4,61.1,63.3,5318680,64.13,-1.3,62.19,74.83,0.93
20260811,63.2,64.4,62,62.9,3834114,64.03,-1.76,61.72,74.8,0.7
20260812,63.2,64,63.1,63.2,2910948,63.96,-1.19,61.17,74.71,0.55
20260813,64,64.7,62.4,62.6,2934080,63.85,-1.95,60.72,74.5,0.56
20260814,63,63.3,61.3,61.6,2738453,63.66,-3.23,60.52,74.33,0.56
20260817,61.5,62.8,61.1,62.6,1983039,63.57,-1.53,60.53,74.13,0.43
20260818,62.6,62.6,60.1,60.2,2804720,63.29,-4.88,60.37,73.85,0.61
20260819,59.5,60.4,58.6,59.5,2613447,62.97,-5.52,60.08,73.52,0.59
20260820,63.9,65.4,62.3,65.1,11688998,63.15,3.09,60.12,73.15,2.44
20260821,63.9,64.2,62.1,63.3,6954689,63.16,0.22,60.15,72.74,1.41
20260824,64.8,67,63,63.1,9209008,63.16,-0.09,60.23,72.44,1.78
20260825,63.3,66.1,61.6,66,6578469,63.4,4.11,60.68,72.1,1.26
20260826,66.1,69,65.8,68.1,9758874,63.79,6.76,61.41,71.75,1.87
20260827,68.2,69,66.9,67.5,5197088,64.1,5.31,62.26,71.34,1.01
20260828,68,68.7,67.2,67.6,4678450,64.39,4.99,62.9,70.9,0.91
20260831,67.6,69.5,67.1,68.2,5541636,64.71,5.4,63.42,70.57,1.07
20260901,68.3,69.7,67.7,67.8,4935897,64.96,4.37,63.82,70.27,0.95
20260902,67.4,68.4,66.5,67,4362027,65.13,2.87,64.09,70.01,0.86
20260903,67.4,68.8,64.7,64.7,5624756,65.1,-0.61,64.23,69.64,1.08
20260904,66,67.2,64.7,65.5,2734304,65.13,0.57,64.49,69.38,0.53
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 41.72
- over_600_ratio: 39.32
- over_800_ratio: 38.14
- over_1000_ratio: 36.36
- over_400_change_1w: -0.03
- over_800_change_1w: 0.19
- over_1000_change_1w: 0.84
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,46.53,1.06,42.16,2.81,39.96,2.18,1,True,True
20260626,42.29,-4.24,37.67,-4.49,36.09,-3.87,0,False,False
20260703,43.27,0.98,38.75,1.08,37.44,1.35,1,True,True
20260709,42.66,-0.61,38.37,-0.38,36.84,-0.6,0,False,False
20260717,41.47,-1.19,37.02,-1.35,35.94,-0.9,0,False,False
20260724,41.26,-0.21,36.73,-0.29,35.24,-0.7,0,False,False
20260731,41.82,0.56,37.46,0.73,35.32,0.08,1,True,True
20260807,41.77,-0.05,37.69,0.23,35.71,0.39,2,False,True
20260814,42.11,0.34,38.24,0.55,35.86,0.15,3,False,True
20260821,41.86,-0.25,38.2,-0.04,35.8,-0.06,4,False,False
20260828,41.75,-0.11,37.95,-0.25,35.52,-0.28,0,False,False
20260904,41.72,-0.03,38.14,0.19,36.36,0.84,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3673 | TPK-KY | pattern | 型態觀察 | 48.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/08/19 2.接受資金貸與之: (1)公司名稱:祥達光學(廈門)有限公司 (2)與資金貸與他人公司之關係: 關係企業 (3)資金貸與之限額(仟元):67,416,328 (4)原資金貸與之餘額(仟元):969,300 (5)本次新增資金貸與之金額(仟元):969,300 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):1,938,600 (8)本次新增資金貸與之原因: 充實祥達光學(廈門)有限公司之營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):20,184,097 (2)累積盈虧金額(仟元):-12,815,371 5.計息方式: 廈門子公司加權平均成本 6.還款之: (1)條件: 本金到期清償。同意到期日前提前還款及分期清償借款 (2)日期: 中華民國116年08月18日(預估到期日) 7.迄事實發生日為止，資金貸與餘額(仟元): 87,140,070 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 215.02 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: (1)資金貸與餘額、新增資金貸與之金額之美元數以32.31折算新台幣 (2) 貸出方淨值、接受資金貸與公司最近期財務報表之資本 以115年第&#12752;季會計師核閱報告之數據為準 (3) 接受資金貸與公司最近期財務報表之累積盈虧金額 為115年第&#12752;季會計師核閱報告之美金數以匯率31.995折算新台幣；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3673 | TPK-KY | 6 | 4 | 5 | 8 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3673 | TPK-KY | 74 | 1 | 1910380.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
