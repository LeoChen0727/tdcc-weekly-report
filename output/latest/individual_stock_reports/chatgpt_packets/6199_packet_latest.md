# INDIVIDUAL STOCK CHATGPT PACKET - 6199 天品

## Metadata
- generated_at: 2026-09-26 22:17:19 Asia/Taipei
- stock_id: 6199
- stock_name: 天品
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6199_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6199_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6199.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6199.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6199.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6199.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6199_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6199_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6199_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- tdcc_distribution_warning
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260924
- open: 122
- high: 125
- low: 118.5
- close: 124
- volume: 5871000
- ma5: 118
- ema23_primary: 105.28
- distance_to_ema23_pct: 17.78
- ma20: 102.58
- ma60: 100.31
- ma120: 99.62
- return_5d: 18.1
- return_20d: 34.2
- volume_ratio: 1.94
- distance_to_ma20_pct_auxiliary: 20.88
- distance_to_high_60_pct: -0.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,92.4,93.6,91.9,93.3,591000,96,-2.81,96.2,98.29,1.03
20260831,93.3,93.3,91.8,92.8,412000,95.73,-3.06,95.97,98.33,0.7
20260901,92.1,93.9,92.1,93.1,717000,95.51,-2.53,95.66,98.38,1.18
20260902,92.7,95.6,92.2,95.2,673000,95.49,-0.3,95.5,98.4,1.09
20260903,95.2,97.7,94,95.2,2043000,95.46,-0.28,95.44,98.38,2.92
20260904,95.2,96.4,94.7,96.1,2686000,95.52,0.61,95.44,98.37,3.31
20260907,96.1,97.2,95,96.2,1582000,95.57,0.66,95.37,98.37,1.82
20260908,96.2,97.1,95.3,96.5,1234000,95.65,0.89,95.27,98.36,1.35
20260909,96.5,97.7,96.1,97.1,1367000,95.77,1.39,94.95,98.53,1.43
20260910,97.1,98.1,95.6,97.3,2128000,95.9,1.46,94.95,98.61,2.07
20260911,97.3,98.8,89.8,98.4,3134000,96.11,2.39,94.91,98.72,2.69
20260914,98.4,101,97.7,100.5,3116000,96.47,4.17,95.11,98.71,2.41
20260915,100.5,102.5,98,102.5,3079000,96.98,5.7,95.5,98.73,2.15
20260916,101.5,103,99.3,102.5,3767000,97.44,5.2,95.83,98.74,2.44
20260917,102.5,106,101,105,3489000,98.07,7.07,96.38,98.83,2.05
20260918,105,113,103.5,113,4218000,99.31,13.78,97.33,99.04,2.25
20260921,112.5,118.5,105.5,114.5,8092000,100.58,13.84,98.38,99.29,3.6
20260922,115,118.5,114.5,116.5,7291000,101.9,14.32,99.52,99.58,2.83
20260923,116.5,122,116,122,5040000,103.58,17.79,101,99.92,1.83
20260924,122,125,118.5,124,5871000,105.28,17.78,102.58,100.31,1.94
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 84.89
- over_600_ratio: 81.55
- over_800_ratio: 79.22
- over_1000_ratio: 77.81
- over_400_change_1w: 1.13
- over_800_change_1w: 0.14
- over_1000_change_1w: -1.27
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,83.29,1.92,78.34,1.71,77.01,1.73,8,True,True
20260717,83.44,0.15,77.54,-0.8,77.54,0.53,9,False,True
20260724,83.31,-0.13,77.52,-0.02,77.52,-0.02,0,False,False
20260731,82.02,-1.29,78.29,0.77,78.29,0.77,1,False,True
20260807,82.59,0.57,78.32,0.03,78.32,0.03,2,False,True
20260814,82.58,-0.01,78.15,-0.17,78.15,-0.17,0,False,False
20260821,82.71,0.13,78.15,0,78.15,0,1,False,False
20260828,81.84,-0.87,78.12,-0.03,78.12,-0.03,0,False,False
20260904,81.6,-0.24,78.14,0.02,78.14,0.02,1,False,True
20260911,82.05,0.45,77.62,-0.52,76.08,-2.06,2,False,False
20260918,83.76,1.71,79.08,1.46,79.08,3,3,True,True
20260924,84.89,1.13,79.22,0.14,77.81,-1.27,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6199 | 天品 | true_breakout | 嚴格突破 | 84.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.董事會決議日期：115/07/01 2.股東臨時會召開日期：115/07/29 3.股東臨時會召開地點：新北市中和區板南路659號19樓(元隆捷運雙星B棟) 4.股東臨時會召開方式(實體股東會/視訊輔助股東會/視訊股東會)：實體股東會 5.召集事由一：討論事項 (1)：子公司天品國際股份有限公司以自地委建方式與關係人「宏固營造工程股份有限公司」 簽訂「基隆孝光閣」工程承攬契約案 (2)：本公司「公司章程」修訂案 6.臨時動議： 7.停止過戶起始日期：115/06/30 8.停止過戶截止日期：115/07/29 9.其他應敘明事項：(1)本次股東會股東得以電子方式行使表決權，行使期間自民國115年7月14日 至115年7月26日止，電子投票平台為台灣集中保管結算所股東會電子投票平台， 網址：https://stockservices.tdcc.com.tw。 (2)115/7/1董事會新增討論事項第二案。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 6199 | 天品 | 14 | 2 | 5 | 10 | 15 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
