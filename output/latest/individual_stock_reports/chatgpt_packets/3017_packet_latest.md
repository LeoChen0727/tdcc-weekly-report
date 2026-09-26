# INDIVIDUAL STOCK CHATGPT PACKET - 3017 奇鋐

## Metadata
- generated_at: 2026-09-26 22:16:34 Asia/Taipei
- stock_id: 3017
- stock_name: 奇鋐
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3017_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3017_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3017.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3017.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3017.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3017.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3017_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3017_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3017_latest.md?ref=main

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
- open: 3460
- high: 3600
- low: 3455
- close: 3555
- volume: 2261001
- ma5: 3452
- ema23_primary: 3285.81
- distance_to_ema23_pct: 8.19
- ma20: 3366.75
- ma60: 2869.58
- ma120: 2693.67
- return_5d: 11.62
- return_20d: 6.44
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: 5.59
- distance_to_high_60_pct: -1.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,3360,3450,3320,3360,4035280,2912.78,15.35,2963.25,2580.83,0.85
20260831,3280,3425,3250,3425,4468442,2955.47,15.89,3007,2592.75,0.94
20260901,3435,3465,3350,3410,3084829,2993.35,13.92,3047.5,2606.25,0.67
20260902,3365,3490,3280,3310,3136748,3019.73,9.61,3076.5,2618.58,0.7
20260903,3395,3525,3290,3300,4418016,3043.09,8.44,3094.5,2631.17,1.04
20260904,3465,3570,3410,3570,4515440,3087,15.65,3133.75,2651.33,1.06
20260907,3595,3595,3410,3420,3303272,3114.75,9.8,3166.5,2669.42,0.77
20260908,3455,3455,3245,3285,3350997,3128.94,4.99,3192.75,2684.08,0.78
20260909,3285,3395,3265,3380,2364600,3149.86,7.31,3216.25,2700.25,0.57
20260910,3405,3470,3380,3460,2574023,3175.7,8.95,3229.25,2718.42,0.68
20260911,3360,3390,3300,3370,2111512,3191.9,5.58,3236,2735.17,0.6
20260914,3255,3360,3210,3310,2215371,3201.74,3.38,3244,2750.33,0.64
20260915,3265,3300,3100,3115,3217593,3194.51,-2.49,3248,2761.92,0.93
20260916,3115,3225,3100,3175,2744795,3192.88,-0.56,3252,2774.42,0.81
20260917,3285,3350,3175,3185,3034388,3192.23,-0.23,3262,2785.33,0.9
20260918,3345,3450,3290,3430,3785048,3212.04,6.79,3290.25,2800.75,1.1
20260921,3480,3495,3365,3415,1743425,3228.95,5.76,3318.25,2820.08,0.51
20260922,3500,3505,3385,3390,2288258,3242.37,4.55,3340.25,2838.25,0.68
20260923,3425,3590,3410,3470,2649367,3261.34,6.4,3356,2854,0.81
20260924,3460,3600,3455,3555,2261001,3285.81,8.19,3366.75,2869.58,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 67.59
- over_600_ratio: 61.43
- over_800_ratio: 58
- over_1000_ratio: 54.56
- over_400_change_1w: -0.13
- over_800_change_1w: -0.26
- over_1000_change_1w: -0.47
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,65.29,-0.3,55.43,-0.06,52.18,-0.59,0,False,False
20260717,65.24,-0.05,55.07,-0.36,52.3,0.12,1,False,True
20260724,65.81,0.57,55.94,0.87,52.94,0.64,2,True,True
20260731,66.11,0.3,55.81,-0.13,52.32,-0.62,3,False,False
20260807,67.46,1.35,57.45,1.64,53.32,1,4,True,True
20260814,68.94,1.48,58.7,1.25,54.58,1.26,5,True,True
20260821,68.52,-0.42,58.47,-0.23,54.6,0.02,6,False,True
20260828,68.49,-0.03,58.24,-0.23,54.59,-0.01,0,False,False
20260904,68.66,0.17,58.63,0.39,55.14,0.55,1,False,True
20260911,68.37,-0.29,58.36,-0.27,54.65,-0.49,2,False,False
20260918,67.72,-0.65,58.26,-0.1,55.03,0.38,3,False,True
20260924,67.59,-0.13,58,-0.26,54.56,-0.47,4,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3017 | 奇鋐 | pattern | 型態觀察 | 46.0 |  |  | base_building |  | no_signal | stale_signal | 1.契約種類:工程合約 2.事實發生日:115/9/8~115/9/8 3.董事會通過日期: 民國115年9月8日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 契約相對人：創興國際建設有限公司 與公司之關係：無。 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 與創興國際建設有限公司簽訂AVC TECH. (VIETNAM) CO., LTD.第五期廠房機電工程 契約總金額：約越南盾9,868億（匯率820，約新台幣12.04億元) 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 供生產及營運用 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 不適用 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 3017 | 奇鋐 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | stale_signal | 1.契約種類:工程合約 2.事實發生日:115/9/8~115/9/8 3.董事會通過日期: 民國115年9月8日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 契約相對人：創興國際建設有限公司 與公司之關係：無。 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 與創興國際建設有限公司簽訂AVC TECH. (VIETNAM) CO., LTD.第五期廠房機電工程 契約總金額：約越南盾9,868億（匯率820，約新台幣12.04億元) 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 供生產及營運用 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 不適用 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3017 | 奇鋐 | 12 | 12 | 5 | 10 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3017 | 奇鋐 | 483 | 26 | 71556250.0 | 511300.0 | 139.95 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
