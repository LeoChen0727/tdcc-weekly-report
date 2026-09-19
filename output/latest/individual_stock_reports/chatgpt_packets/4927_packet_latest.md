# INDIVIDUAL STOCK CHATGPT PACKET - 4927 泰鼎-KY

## Metadata
- generated_at: 2026-09-19 22:16:53 Asia/Taipei
- stock_id: 4927
- stock_name: 泰鼎-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4927_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4927_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4927_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4927_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4927_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4927_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4927_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4927.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4927.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4927.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4927.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4927_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4927_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4927_latest.md?ref=main

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
- action_summary_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
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
- date: 20260918
- open: 43.85
- high: 44.25
- low: 42.8
- close: 44.25
- volume: 4819377
- ma5: 42.29
- ema23_primary: 40.48
- distance_to_ema23_pct: 9.32
- ma20: 41.08
- ma60: 38.14
- ma120: 44.73
- return_5d: 7.14
- return_20d: 33.89
- volume_ratio: 0.99
- distance_to_ma20_pct_auxiliary: 7.71
- distance_to_high_60_pct: -9.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,32.75,35.55,32.75,34.7,3516806,34.25,1.32,32.27,41.28,1.09
20260825,34.45,35.6,33.3,35.55,2368811,34.36,3.48,32.49,40.93,0.75
20260826,35.5,37.55,35.4,37,4681244,34.58,7.01,32.92,40.62,1.57
20260827,38.25,40.7,37.75,40.45,11969946,35.06,15.36,33.6,40.42,3.57
20260828,40.4,44.2,39.4,43,11801891,35.73,20.36,34.29,40.27,3.12
20260831,42.45,43.5,40.3,40.35,5683301,36.11,11.74,34.8,40.06,1.45
20260901,41.2,42.75,40.6,41.75,4442337,36.58,14.13,35.36,39.89,1.12
20260902,41.4,45.1,41.15,42.3,6930586,37.06,14.15,35.88,39.75,1.67
20260903,42.5,43.45,40.45,40.55,4106241,37.35,8.57,36.16,39.51,0.98
20260904,41.05,41.95,40,41.9,2401251,37.73,11.06,36.6,39.38,0.62
20260907,42.3,44.85,42.15,43,6268476,38.17,12.66,37.06,39.29,1.56
20260908,44.1,46,42.8,43.05,7483397,38.57,11.6,37.52,39.18,1.75
20260909,44.05,44.25,41.7,42.55,4060149,38.91,9.37,37.92,39.03,0.92
20260910,41.85,43.15,41.85,42.75,2441660,39.23,8.98,38.34,38.91,0.55
20260911,42.15,42.45,41,41.3,1805392,39.4,4.83,38.73,38.77,0.41
20260914,40.9,41.85,40.65,41.15,1794524,39.54,4.06,39.11,38.6,0.41
20260915,41.15,41.5,40.05,40.05,1538858,39.59,1.17,39.48,38.4,0.35
20260916,40.05,43.2,40.05,42.6,2927230,39.84,6.93,39.99,38.3,0.66
20260917,43.05,45.45,43,43.4,6486759,40.13,8.14,40.52,38.21,1.37
20260918,43.85,44.25,42.8,44.25,4819377,40.48,9.32,41.08,38.14,0.99
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 27.81
- over_600_ratio: 23.2
- over_800_ratio: 20.84
- over_1000_ratio: 17.76
- over_400_change_1w: 0.44
- over_800_change_1w: 0.81
- over_1000_change_1w: 0.55
- tdcc_consecutive_up_weeks: 10
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,25.88,-0.76,19.59,-0.71,16.54,-1.77,0,False,False
20260709,23.94,-1.94,17.39,-2.2,14.99,-1.55,0,False,False
20260717,24.24,0.3,17.8,0.41,16.07,1.08,1,True,True
20260724,24.34,0.1,17.51,-0.29,15.11,-0.96,2,False,False
20260731,24.82,0.48,17.59,0.08,14.86,-0.25,3,False,True
20260807,25.32,0.5,18.13,0.54,15.34,0.48,4,False,True
20260814,24.43,-0.89,17.59,-0.54,15.88,0.54,5,False,True
20260821,24.87,0.44,17.21,-0.38,15.83,-0.05,6,False,False
20260828,26.37,1.5,18.19,0.98,15.85,0.02,7,True,True
20260904,26.92,0.55,19.03,0.84,16.68,0.83,8,True,True
20260911,27.37,0.45,20.03,1,17.21,0.53,9,True,True
20260918,27.81,0.44,20.84,0.81,17.76,0.55,10,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4927 | 泰鼎-KY | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | continued_overheated | 1.事實發生日:115/09/15 2.公司名稱:Apex Circuit (Thailand) Co., Ltd. 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例: Apex Circuit (Thailand) Co., Ltd.為本公司持有99.69%之子公司 5.發生緣由: (1)依金融監督管理委員會115年9月3日金管證審字第1150353421號函示辦理。 (2)子公司Apex Circuit (Thailand) Co., Ltd.因財報淨值下降，致資金貸與餘額 超過所訂限額。 6.因應措施: (1)本公司依資金貸與改善計畫督促子公司辦理改善措施如下: (A)持續落實各項營運改善措施，提升營運績效及獲利能力，強化財務結構， 以提升整體淨值；(B)將視借款償還情形及資金需求，適時檢討及調整資金貸與額度， 以逐步改善並解除資金貸與超限情形。 (2)改善計畫未執行完成前,本公司將按季公告執行情形及逐季提報董事會控管。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 4927 | 泰鼎-KY | 3 | 3 | 4 | 5 | 13 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
