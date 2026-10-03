# INDIVIDUAL STOCK CHATGPT PACKET - 3311 閎暉

## Metadata
- generated_at: 2026-10-03 15:47:10 Asia/Taipei
- stock_id: 3311
- stock_name: 閎暉
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3311_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3311_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3311_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3311_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3311_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3311_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3311_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3311.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3311.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3311.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3311.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3311_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3311_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3311_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20261002
- open: 48.25
- high: 49.65
- low: 48.15
- close: 49.65
- volume: 2466947
- ma5: 42.41
- ema23_primary: 37.69
- distance_to_ema23_pct: 31.72
- ma20: 36.75
- ma60: 34.35
- ma120: 34.71
- return_5d: 35.29
- return_20d: 53.24
- volume_ratio: 1.66
- distance_to_ma20_pct_auxiliary: 35.11
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,32.4,32.55,31.7,31.75,210688,32.49,-2.28,32.15,34.76,1.36
20260904,31.75,32,31.6,31.95,87050,32.45,-1.53,32.14,34.67,0.57
20260907,32.1,32.1,31.6,31.75,81223,32.39,-1.97,32.11,34.59,0.55
20260908,32,32,31.4,31.55,134953,32.32,-2.38,32.07,34.49,0.9
20260909,31.75,32.4,31.6,32.3,126618,32.32,-0.05,32.09,34.34,0.89
20260910,32,32.05,31.7,31.85,88727,32.28,-1.33,32.04,34.2,0.64
20260911,34.75,35,34.7,35,419620,32.51,7.68,32.18,34.13,2.82
20260914,35.4,36.5,34.1,35,3173601,32.71,6.99,32.33,34.07,10.51
20260915,35,37.6,34.85,36.8,2318623,33.05,11.33,32.59,34.01,5.74
20260916,36.8,38.4,36.05,38.1,2089428,33.47,13.82,32.93,33.99,4.14
20260917,38.3,38.8,37,37,2257336,33.77,9.57,33.2,33.96,3.69
20260918,37,38.8,36.75,38.7,1410503,34.18,13.23,33.53,33.98,2.08
20260921,38.5,38.75,36.55,37.7,942621,34.47,9.36,33.82,33.99,1.31
20260922,37.7,38.85,36.75,36.75,694635,34.66,6.02,34.05,34,0.92
20260923,36.8,37.4,36.6,36.7,318304,34.83,5.36,34.25,33.98,0.42
20260924,36.9,38.65,36.65,38.05,855155,35.1,8.4,34.52,33.98,1.08
20260929,38.45,38.5,37.55,38.15,303974,35.35,7.91,34.8,33.98,0.38
20260930,38,41.95,38,41.05,4650953,35.83,14.57,35.23,34.03,4.51
20261001,42.35,45.15,42.1,45.15,7066254,36.61,23.34,35.88,34.13,5.15
20261002,48.25,49.65,48.15,49.65,2466947,37.69,31.72,36.75,34.35,1.66
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 61.33
- over_600_ratio: 56.41
- over_800_ratio: 53.61
- over_1000_ratio: 51.72
- over_400_change_1w: 3.59
- over_800_change_1w: -0.49
- over_1000_change_1w: 1.13
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,55.74,-0.96,51.98,0.04,50.34,0.04,8,False,True
20260724,56.69,0.95,51.26,-0.72,50.43,0.09,9,False,True
20260731,57.51,0.82,51.41,0.15,50.56,0.13,10,True,True
20260807,57.62,0.11,52.28,0.87,50.62,0.06,11,False,True
20260814,57.8,0.18,52.36,0.08,50.66,0.04,12,True,True
20260821,58.4,0.6,52.59,0.23,50.76,0.1,13,False,True
20260828,58.53,0.13,52.66,0.07,50.8,0.04,14,True,True
20260904,58.38,-0.15,53.64,0.98,51.95,1.15,15,False,True
20260911,57.96,-0.42,53.66,0.02,51.96,0.01,16,False,True
20260918,57.29,-0.67,52.44,-1.22,50.59,-1.37,0,False,False
20260924,57.74,0.45,54.1,1.66,50.59,0,1,False,True
20261002,61.33,3.59,53.61,-0.49,51.72,1.13,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3311 | 閎暉 | true_breakout | 嚴格突破 | 87.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.事實發生日:115/09/30 2.接受資金貸與之: (1)公司名稱:FDK Corporation (2)與資金貸與他人公司之關係: FDK Corporation為持有Xiamen FDK Corporation 100%股權之母公司 (3)資金貸與之限額(仟元):876,774 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):82,040 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):82,040 (8)本次新增資金貸與之原因: 營運週轉 (1)公司名稱:FDK Corporation (2)與資金貸與他人公司之關係: FDK Corporation為持有Fuchi Electronics Co., Ltd. 100%股權之母公司 (3)資金貸與之限額(仟元):612,047 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):254,040 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):254,040 (8)本次新增資金貸與之原因: 營運週轉 (1)公司名稱:FDK Corporation (2)與資金貸與他人公司之關係: FDK Corporation為持有FDK Singapore Pte. Ltd. 100%股權之母公司 (3)資金貸與之限額(仟元):36,837 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):31,755 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):31,755 (8)本次新增資金貸與之原因: 營運週轉 (1)公司名稱:FDK Corporation (2)與資金貸與他人公司之關係: FDK Corporation為持有FDK Hong Kong Ltd. 100%股權之母公司 (3)資金貸與之限額(仟元):118,366 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):63,510 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):63,510 (8)本次新增資金貸與之原因: 營運週轉 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):615,300 (2)累積盈虧金額(仟元):350,275 5.計息方式: 依合約規定 6.還款之: (1)條件: 本金於到期日全部一次償還 (2)日期: 依合約規定辦理 7.迄事實發生日為止，資金貸與餘額(仟元): 659,145 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 18.00 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 3311 | 閎暉 | 3 | 3 | 3 | 5 | 6 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
