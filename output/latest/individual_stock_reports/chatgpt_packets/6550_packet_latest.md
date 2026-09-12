# INDIVIDUAL STOCK CHATGPT PACKET - 6550 北極星藥業-KY

## Metadata
- generated_at: 2026-09-12 15:44:29 Asia/Taipei
- stock_id: 6550
- stock_name: 北極星藥業-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6550_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6550_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6550_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6550_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6550_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6550_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6550_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6550.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6550.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6550.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6550.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6550_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6550_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6550_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 10.15
- high: 10.15
- low: 9.97
- close: 9.97
- volume: 2230580
- ma5: 10.17
- ema23_primary: 10.75
- distance_to_ema23_pct: -7.22
- ma20: 10.74
- ma60: 11.76
- ma120: 14.28
- return_5d: -3.67
- return_20d: -8.95
- volume_ratio: 1.26
- distance_to_ma20_pct_auxiliary: -7.2
- distance_to_high_60_pct: -30.52

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,10.95,11,10.8,10.8,815383,11.53,-6.32,11.36,12.73,0.8
20260818,10.8,10.8,10.15,10.3,2499641,11.43,-9.85,11.26,12.63,2.26
20260819,10.15,10.5,10.1,10.15,845383,11.32,-10.33,11.16,12.52,0.8
20260820,10.3,11.15,10.3,11.15,1976761,11.31,-1.37,11.12,12.45,1.8
20260821,12.25,12.25,12,12.25,1417839,11.38,7.61,11.13,12.42,1.26
20260824,12.95,13,11.4,11.6,6057708,11.4,1.74,11.11,12.37,4.37
20260825,11.45,11.5,10.95,11,1997937,11.37,-3.24,11.09,12.33,1.4
20260826,11.1,11.8,11.1,11.55,2053060,11.38,1.46,11.09,12.31,1.43
20260827,11.8,12.3,11.3,11.35,2022870,11.38,-0.27,11.1,12.27,1.37
20260828,11.5,11.6,11.2,11.2,1154171,11.37,-1.46,11.12,12.24,0.8
20260831,11.2,11.25,10.5,10.7,2173580,11.31,-5.4,11.1,12.2,1.47
20260901,10.6,10.8,10.3,10.7,1501621,11.26,-4.97,11.08,12.15,0.99
20260902,10.5,10.7,10.5,10.6,548603,11.2,-5.4,11.04,12.11,0.37
20260903,10.7,10.7,10.3,10.3,1005655,11.13,-7.45,11,12.06,0.67
20260904,10.3,10.4,10.2,10.35,825107,11.06,-6.46,10.96,12.02,0.54
20260907,10.45,10.45,10.2,10.3,808499,11,-6.37,10.91,11.97,0.53
20260908,10.25,10.35,9.99,10.15,2022559,10.93,-7.13,10.87,11.92,1.27
20260909,10,10.3,9.99,10.25,2692273,10.87,-5.73,10.84,11.87,1.59
20260910,10.3,10.3,10.05,10.2,697251,10.82,-5.7,10.79,11.82,0.42
20260911,10.15,10.15,9.97,9.97,2230580,10.75,-7.22,10.74,11.76,1.26
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 76.55
- over_600_ratio: 74.97
- over_800_ratio: 74.13
- over_1000_ratio: 72.97
- over_400_change_1w: -0.08
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.26
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,77.04,-0.04,74.73,-0.06,73.86,-0.05,0,False,False
20260703,77.11,0.07,74.72,-0.01,73.75,-0.11,1,False,False
20260709,77.11,0,74.78,0.06,73.91,0.16,2,False,True
20260717,77.01,-0.1,74.66,-0.12,73.79,-0.12,0,False,False
20260724,77.05,0.04,74.65,-0.01,73.67,-0.12,1,False,False
20260731,77.11,0.06,74.81,0.16,73.74,0.07,2,True,True
20260807,77.04,-0.07,74.9,0.09,73.85,0.11,3,False,True
20260814,77.06,0.02,74.91,0.01,73.74,-0.11,4,False,True
20260821,77.14,0.08,75.06,0.15,73.9,0.16,5,True,True
20260828,76.73,-0.41,74.37,-0.69,73.4,-0.5,0,False,False
20260904,76.63,-0.1,74.2,-0.17,73.23,-0.17,0,False,False
20260911,76.55,-0.08,74.13,-0.07,72.97,-0.26,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6550 | 北極星藥業-KY | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | first_seen | 1.事實發生日:115/07/01 2.接受資金貸與之: (1)公司名稱:迪瑞藥業(成都)有限公司 (2)與資金貸與他人公司之關係: 本公司直接或間接100%持有之子公司 (3)資金貸與之限額(仟元):480,000 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):414,050 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):414,050 (8)本次新增資金貸與之原因: 供應子公司之短期資金需求 (1)公司名稱:霖揚生技製藥股份有限公司 (2)與資金貸與他人公司之關係: 供應子公司之短期資金需求 (3)資金貸與之限額(仟元):480,000 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):414,050 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):414,050 (8)本次新增資金貸與之原因: 供應子公司之短期資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):3,775,491 (2)累積盈虧金額(仟元):-3,121,537 5.計息方式: 待實際借款時視當時利率訂定之 6.還款之: (1)條件: 到期時還款 (2)日期: 由起借日起一年內還款 7.迄事實發生日為止，資金貸與餘額(仟元): 923,650 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 19.24 9.公司貸與他人資金之來源: 母公司 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 6550 | 北極星藥業-KY | 1 | 1 | 1 | 1 | 4 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
