# INDIVIDUAL STOCK CHATGPT PACKET - 1314 中石化

## Metadata
- generated_at: 2026-09-20 22:15:40 Asia/Taipei
- stock_id: 1314
- stock_name: 中石化
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 357
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1314_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1314_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1314_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1314_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1314_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1314_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1314_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1314.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1314.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1314.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1314.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1314_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1314_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1314_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
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
- open: 9.11
- high: 9.37
- low: 8.87
- close: 8.96
- volume: 151096127
- ma5: 8.48
- ema23_primary: 8.23
- distance_to_ema23_pct: 8.86
- ma20: 8.2
- ma60: 8.26
- ma120: 7.91
- return_5d: 10.34
- return_20d: 8.87
- volume_ratio: 4.83
- distance_to_ma20_pct_auxiliary: 9.23
- distance_to_high_60_pct: -16.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,8.23,8.27,7.97,7.98,29069019,7.94,0.56,7.75,8.13,1.11
20260825,7.97,8,7.88,7.9,12245468,7.93,-0.41,7.76,8.14,0.49
20260826,7.95,8.1,7.94,7.99,17894579,7.94,0.66,7.78,8.15,0.75
20260827,8.03,8.33,8.01,8.16,35700316,7.96,2.56,7.82,8.16,1.46
20260828,8.21,8.25,8.03,8.05,18157758,7.96,1.08,7.85,8.16,0.77
20260831,8.02,8.29,8,8.18,23245945,7.98,2.48,7.87,8.16,0.98
20260901,8.19,8.44,8.19,8.26,27691213,8.01,3.18,7.9,8.17,1.14
20260902,8.3,8.33,8.14,8.22,16925294,8.02,2.46,7.92,8.17,0.74
20260903,8.23,8.55,8.12,8.12,34031523,8.03,1.11,7.94,8.18,1.45
20260904,8.15,8.21,8.02,8.12,16389736,8.04,1.01,7.95,8.18,0.7
20260907,8.15,8.19,8.05,8.1,13045132,8.04,0.7,7.97,8.19,0.59
20260908,8.1,8.12,8.06,8.11,14930552,8.05,0.76,7.99,8.19,0.69
20260909,8.13,8.25,8.12,8.21,18123514,8.06,1.83,8.01,8.2,0.84
20260910,8.21,8.21,8.06,8.13,14554049,8.07,0.77,8.04,8.21,0.7
20260911,8.13,8.17,8.08,8.12,8416494,8.07,0.59,8.06,8.22,0.41
20260914,8.15,8.27,8.06,8.22,15174574,8.08,1.67,8.08,8.22,0.75
20260915,8.23,8.24,8.08,8.11,12078524,8.09,0.29,8.09,8.22,0.6
20260916,8.11,8.22,8.1,8.15,17974530,8.09,0.72,8.11,8.23,0.88
20260917,8.23,8.96,8.23,8.96,128600273,8.16,9.74,8.17,8.24,4.94
20260918,9.11,9.37,8.87,8.96,151096127,8.23,8.86,8.2,8.26,4.83
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 42.83
- over_600_ratio: 38.81
- over_800_ratio: 36.14
- over_1000_ratio: 34.43
- over_400_change_1w: 1.71
- over_800_change_1w: 1.8
- over_1000_change_1w: 2
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,41.97,1.82,35.3,1.75,33.47,1.8,2,True,True
20260709,42.19,0.22,35.92,0.62,34,0.53,3,True,True
20260717,41.53,-0.66,35.04,-0.88,33.39,-0.61,0,False,False
20260724,41.14,-0.39,34.7,-0.34,33.01,-0.38,0,False,False
20260731,40.81,-0.33,34.42,-0.28,32.63,-0.38,0,False,False
20260807,40.67,-0.14,34.15,-0.27,32.31,-0.32,0,False,False
20260814,40.2,-0.47,33.58,-0.57,31.72,-0.59,0,False,False
20260821,40.28,0.08,33.59,0.01,31.8,0.08,1,True,True
20260828,40.66,0.38,33.87,0.28,32.12,0.32,2,True,True
20260904,40.87,0.21,34.11,0.24,32.28,0.16,3,True,True
20260911,41.12,0.25,34.34,0.23,32.43,0.15,4,True,True
20260918,42.83,1.71,36.14,1.8,34.43,2,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1314 | 中石化 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | 1.法律事件之當事人:第三人 鼎越開發股份有限公司 2.法律事件之法院名稱或處分機關:臺灣高等地方法院。 3.法律事件之相關文書案號:115年度抗字第1470號刑事裁定。 4.事實發生日:115/09/16 5.發生原委(含爭訟標的):本公司之子公司鼎越開發股份有限公司向京華城股份有限公司 購得台北市松山區西松段三小段156地號土地，前遭臺北地檢署向臺北地院聲請扣押獲 四度裁定，經鼎越開發向高等法院提起第四次抗告，獲高等法院撤銷原裁定 並發回臺北地院。 6.處理過程:委請律師提供專業法律意見並研擬方案。 7.對公司財務業務影響及預估影響金額:無。 8.因應措施及改善情形:本公司將依法處理。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第2款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 1314 | 中石化 | 3 | 2 | 3 | 4 | 8 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
