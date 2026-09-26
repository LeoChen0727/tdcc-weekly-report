# INDIVIDUAL STOCK CHATGPT PACKET - 3673 TPK-KY

## Metadata
- generated_at: 2026-09-26 22:16:50 Asia/Taipei
- stock_id: 3673
- stock_name: TPK-KY
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
- date: 20260924
- open: 64.6
- high: 65.9
- low: 64.2
- close: 65.6
- volume: 2491440
- ma5: 65.24
- ema23_primary: 64.55
- distance_to_ema23_pct: 1.63
- ma20: 64.89
- ma60: 65.41
- ma120: 68.83
- return_5d: 2.82
- return_20d: -2.81
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 1.09
- distance_to_high_60_pct: -26.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,68,68.7,67.2,67.6,4678450,64.39,4.99,62.9,70.9,0.91
20260831,67.6,69.5,67.1,68.2,5541636,64.71,5.4,63.42,70.57,1.07
20260901,68.3,69.7,67.7,67.8,4935897,64.96,4.37,63.82,70.27,0.95
20260902,67.4,68.4,66.5,67,4362027,65.13,2.87,64.09,70.01,0.86
20260903,67.4,68.8,64.7,64.7,5624756,65.1,-0.61,64.23,69.64,1.08
20260904,66,67.2,64.7,65.5,2734304,65.13,0.57,64.49,69.38,0.53
20260907,66.1,66.8,65.4,65.8,2723796,65.19,0.94,64.61,69.17,0.55
20260908,66.3,66.8,63.7,63.9,3450909,65.08,-1.81,64.67,68.9,0.69
20260909,64,65.3,64,64.2,2388220,65.01,-1.24,64.72,68.65,0.48
20260910,64.3,64.3,62.3,62.6,2935552,64.81,-3.4,64.72,68.38,0.59
20260911,61.4,62.2,60.5,61.7,1642664,64.55,-4.41,64.72,67.96,0.34
20260914,60.6,65.3,60,63.4,4385449,64.45,-1.63,64.76,67.58,0.88
20260915,63.4,64.2,61.5,61.5,2301828,64.21,-4.21,64.83,67.13,0.46
20260916,62.1,64.8,62.1,64,3259727,64.19,-0.29,65.05,66.83,0.65
20260917,64.2,65.8,63.7,63.8,2864782,64.16,-0.55,64.98,66.5,0.63
20260918,64.5,64.7,63.4,64.5,2447647,64.18,0.49,65.05,66.21,0.56
20260921,64.9,66.8,64.3,65.7,4757379,64.31,2.16,65.17,66.03,1.15
20260922,66.4,67.5,65.4,65.6,4941576,64.42,1.83,65.16,65.85,1.22
20260923,66.3,67.5,64.8,64.8,4047583,64.45,0.54,64.99,65.59,1.08
20260924,64.6,65.9,64.2,65.6,2491440,64.55,1.63,64.89,65.41,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 41.71
- over_600_ratio: 38.93
- over_800_ratio: 37.93
- over_1000_ratio: 35.99
- over_400_change_1w: -0.27
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,42.66,-0.61,38.37,-0.38,36.84,-0.6,0,False,False
20260717,41.47,-1.19,37.02,-1.35,35.94,-0.9,0,False,False
20260724,41.26,-0.21,36.73,-0.29,35.24,-0.7,0,False,False
20260731,41.82,0.56,37.46,0.73,35.32,0.08,1,True,True
20260807,41.77,-0.05,37.69,0.23,35.71,0.39,2,False,True
20260814,42.11,0.34,38.24,0.55,35.86,0.15,3,False,True
20260821,41.86,-0.25,38.2,-0.04,35.8,-0.06,4,False,False
20260828,41.75,-0.11,37.95,-0.25,35.52,-0.28,0,False,False
20260904,41.72,-0.03,38.14,0.19,36.36,0.84,1,False,True
20260911,41.54,-0.18,37.56,-0.58,36.47,0.11,2,False,True
20260918,41.98,0.44,37.98,0.42,36.19,-0.28,3,False,True
20260924,41.71,-0.27,37.93,-0.05,35.99,-0.2,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3673 | TPK-KY | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/08/19 2.接受資金貸與之: (1)公司名稱:祥達光學(廈門)有限公司 (2)與資金貸與他人公司之關係: 關係企業 (3)資金貸與之限額(仟元):67,416,328 (4)原資金貸與之餘額(仟元):969,300 (5)本次新增資金貸與之金額(仟元):969,300 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):1,938,600 (8)本次新增資金貸與之原因: 充實祥達光學(廈門)有限公司之營運資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):20,184,097 (2)累積盈虧金額(仟元):-12,815,371 5.計息方式: 廈門子公司加權平均成本 6.還款之: (1)條件: 本金到期清償。同意到期日前提前還款及分期清償借款 (2)日期: 中華民國116年08月18日(預估到期日) 7.迄事實發生日為止，資金貸與餘額(仟元): 87,140,070 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 215.02 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: (1)資金貸與餘額、新增資金貸與之金額之美元數以32.31折算新台幣 (2) 貸出方淨值、接受資金貸與公司最近期財務報表之資本 以115年第&#12752;季會計師核閱報告之數據為準 (3) 接受資金貸與公司最近期財務報表之累積盈虧金額 為115年第&#12752;季會計師核閱報告之美金數以匯率31.995折算新台幣；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3673 | TPK-KY | 1 | 1 | 3 | 5 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3673 | TPK-KY | 77 | 1 | 1468700.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
