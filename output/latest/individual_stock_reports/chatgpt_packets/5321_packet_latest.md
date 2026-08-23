# INDIVIDUAL STOCK CHATGPT PACKET - 5321 美而快

## Metadata
- generated_at: 2026-08-23 22:28:26 Asia/Taipei
- stock_id: 5321
- stock_name: 美而快
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5321_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5321_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5321_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5321_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5321_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5321_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5321_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5321.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5321.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5321.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5321.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5321_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5321_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5321_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
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
- date: 20260821
- open: 70.7
- high: 78
- low: 70.7
- close: 72.9
- volume: 1151000
- ma5: 71.34
- ema23_primary: 61.5
- distance_to_ema23_pct: 18.53
- ma20: 59.49
- ma60: 54.74
- ma120: 40.31
- return_5d: 14.62
- return_20d: 23.77
- volume_ratio: 2.05
- distance_to_ma20_pct_auxiliary: 22.54
- distance_to_high_60_pct: -6.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,57.6,63,54.3,55,892000,54.97,0.05,58.42,45.02,1.74
20260728,55.3,57,52.7,54,311000,54.89,-1.63,57.63,45.54,0.65
20260729,54.1,57.4,51.8,53.8,489000,54.8,-1.83,57.18,46.07,1.07
20260730,53.8,56.8,51.1,52,350000,54.57,-4.71,56.95,46.58,0.79
20260731,53.5,56.7,53.1,53.3,178000,54.46,-2.13,56.56,47.1,0.43
20260803,53.3,56.1,52.8,55.9,188000,54.58,2.42,56.25,47.67,0.45
20260804,56.8,56.8,53.4,53.6,154000,54.5,-1.65,55.98,48.19,0.37
20260805,53.8,54.1,52.5,53,249000,54.38,-2.53,55.72,48.7,0.59
20260806,53.2,55.1,52.6,54.3,189000,54.37,-0.13,55.4,49.23,0.45
20260807,55.6,56,53.7,54,184000,54.34,-0.62,55.04,49.75,0.44
20260810,54.9,56.1,54.5,56.1,173000,54.48,2.96,54.84,50.29,0.42
20260811,56.1,57.4,54.6,55.6,216000,54.58,1.87,54.8,50.82,0.57
20260812,55.6,57.5,55.6,56.9,158000,54.77,3.89,54.74,51.32,0.44
20260813,57,62.5,56.9,62,1062000,55.37,11.97,54.96,51.87,2.69
20260814,60,65,59.8,63.6,701000,56.06,13.45,55.44,52.39,1.74
20260817,63.6,69.9,62.2,68,1647000,57.05,19.18,56.15,52.93,3.6
20260818,69.4,73,69,72.9,1500000,58.37,24.88,57.16,53.5,2.92
20260819,71.5,72,67.5,71,760000,59.43,19.47,57.97,53.97,1.41
20260820,71.5,72.7,67.5,71.9,660000,60.47,18.91,58.79,54.38,1.17
20260821,70.7,78,70.7,72.9,1151000,61.5,18.53,59.49,54.74,2.05
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 59.69
- over_600_ratio: 51.23
- over_800_ratio: 50.05
- over_1000_ratio: 47.34
- over_400_change_1w: -1.15
- over_800_change_1w: -0.14
- over_1000_change_1w: -0.14
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,60.58,-1.85,49.48,0.04,46.08,0.04,5,False,True
20260612,60.53,-0.05,49.5,0.02,46.1,0.02,6,False,True
20260618,60.44,-0.09,51,1.5,46.06,-0.04,7,False,True
20260626,57.1,-3.34,44.98,-6.02,43.45,-2.61,0,False,False
20260703,58.13,1.03,47,2.02,43.96,0.51,1,True,True
20260709,58.01,-0.12,46.88,-0.12,42.01,-1.95,0,False,False
20260717,57.81,-0.2,46.68,-0.2,42,-0.01,0,False,False
20260724,57.46,-0.35,44.97,-1.71,41.93,-0.07,0,False,False
20260731,62,4.54,50.78,5.81,48.07,6.14,1,True,True
20260807,61.89,-0.11,50.79,0.01,48.08,0.01,2,False,True
20260814,60.84,-1.05,50.19,-0.6,47.48,-0.6,0,False,False
20260821,59.69,-1.15,50.05,-0.14,47.34,-0.14,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5321 | 美而快 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | 1.事實發生日:115/06/26 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (1)單月                      最近一月單月       去年同月       與去年同期增減%                       (115/05)         (114/05) ----------------------------------------------------------------------- 營業收入(百萬元)         191.62         234.69            -18.35% 稅前淨利(百萬元)          -8.90           3.80            由盈轉虧 歸屬於母公司 稅後純益(百萬元)          -7.94           0.03            由盈轉虧 每股盈餘(元)              -0.15           0.00            由盈轉虧 ======================================================================== (2)單季                      最近一季單季       去年同期       與去年同期增減%                        (115第1季)       (114第1季) ----------------------------------------------------------------------- 營業收入(百萬元)         568.52           734.12          -22.56% 稅前淨利(百萬元)        -129.84            22.14          由盈轉虧 歸屬於母公司 稅後純益(百萬元)        -126.14             3.29          由盈轉虧 每股盈餘(元)              -2.37             0.06          由盈轉虧 ======================================================================= (3)最近四季累計                           114年第2季至115年第1季 營業收入(百萬元)               2,676.72 稅前淨利(百萬元)                -102.34 歸屬於母公司 稅後純益(百萬元)                -143.80 每股盈餘(元)                      -2.70 (4)公司每股面額:10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: (1)：以上115年05月及去年同期比較數之財務資料係本公司採IFRS會計準則 編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)：最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字， 且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數， 業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5321 | 美而快 | 1 | 1 | 1 | 1 | 2 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
