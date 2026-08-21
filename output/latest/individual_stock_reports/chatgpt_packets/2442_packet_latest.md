# INDIVIDUAL STOCK CHATGPT PACKET - 2442 新美齊

## Metadata
- generated_at: 2026-08-21 22:27:00 Asia/Taipei
- stock_id: 2442
- stock_name: 新美齊
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2442_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2442_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2442_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2442_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2442.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2442.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2442.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2442.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2442_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2442_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2442_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260821
- open: 19.55
- high: 19.9
- low: 19.5
- close: 19.9
- volume: 4062478
- ma5: 19.44
- ema23_primary: 19.38
- distance_to_ema23_pct: 2.66
- ma20: 19.32
- ma60: 19.38
- ma120: 19.37
- return_5d: 2.58
- return_20d: 2.84
- volume_ratio: 2.63
- distance_to_ma20_pct_auxiliary: 2.99
- distance_to_high_60_pct: -2.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,19.35,19.35,19.15,19.2,542281,19.32,-0.65,19.34,19.1,0.52
20260728,19.25,19.25,18.95,19,1556162,19.3,-1.54,19.33,19.11,1.44
20260729,19.05,19.25,18.75,19.1,2277879,19.28,-0.94,19.32,19.13,1.98
20260730,19,19.35,19,19.2,1747623,19.27,-0.39,19.31,19.14,1.48
20260731,19.25,19.65,19.25,19.4,1590404,19.28,0.6,19.31,19.15,1.31
20260803,19.4,19.5,19.15,19.2,1500892,19.28,-0.4,19.29,19.16,1.26
20260804,19.35,19.4,18.95,19.1,2654980,19.26,-0.85,19.25,19.17,2.1
20260805,19.3,19.3,18.95,18.95,1657219,19.24,-1.49,19.23,19.17,1.28
20260806,19,19.1,18.85,19,1113844,19.22,-1.13,19.22,19.18,0.86
20260807,19,19.4,19,19.4,1215618,19.23,0.87,19.23,19.2,0.93
20260810,19.5,19.65,19.3,19.65,1468504,19.27,1.99,19.25,19.22,1.1
20260811,19.65,19.7,19.4,19.5,773403,19.29,1.11,19.27,19.24,0.59
20260812,19.5,19.65,19.5,19.6,1458945,19.31,1.49,19.28,19.26,1.08
20260813,19.65,19.65,19.45,19.55,1424601,19.33,1.12,19.28,19.28,1.06
20260814,19.55,19.55,19.3,19.4,1297684,19.34,0.32,19.3,19.3,0.98
20260817,19.5,19.5,19.15,19.15,1496338,19.32,-0.89,19.29,19.3,1.11
20260818,19.15,19.4,19.15,19.3,1066360,19.32,-0.11,19.29,19.32,0.79
20260819,19.2,19.5,19.2,19.35,970421,19.32,0.14,19.29,19.33,0.71
20260820,19.35,19.5,19.35,19.5,1039470,19.34,0.84,19.3,19.35,0.76
20260821,19.55,19.9,19.5,19.9,4062478,19.38,2.66,19.32,19.38,2.63
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 57.61
- over_600_ratio: 54.45
- over_800_ratio: 52.39
- over_1000_ratio: 49.33
- over_400_change_1w: 0.66
- over_800_change_1w: 0.82
- over_1000_change_1w: 0.22
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,57.74,-0.64,53.52,-0.07,51.27,0.23,2,False,True
20260605,57.5,-0.24,53.35,-0.17,50.51,-0.76,0,False,False
20260612,57.46,-0.04,53.25,-0.1,50.46,-0.05,1,False,False
20260618,57.69,0.23,53.28,0.03,50.77,0.31,2,True,True
20260626,57.46,-0.23,53.01,-0.27,50.48,-0.29,0,False,False
20260703,57.54,0.08,52.54,-0.47,50.33,-0.15,1,False,False
20260709,57.42,-0.12,52.43,-0.11,49.99,-0.34,0,False,False
20260717,57.67,0.25,52.42,-0.01,49.71,-0.28,1,False,False
20260724,57.78,0.11,52.71,0.29,50.01,0.3,2,False,True
20260731,57.69,-0.09,52.74,0.03,50.27,0.26,3,False,True
20260807,56.95,-0.74,51.57,-1.17,49.11,-1.16,0,False,False
20260814,57.61,0.66,52.39,0.82,49.33,0.22,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2442 | 新美齊 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: (1)股票股利：每仟股無償配發70股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2元，計新台幣650,464,040元。 3.變更後發放股利種類及金額: (1)股票股利：每仟股無償配發71.11516340股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2.03186184元，計新台幣650,464,040元。 4.變更原因:扣除尚未既得之限制型員工權利新股，不得參與盈餘分配、配股或配息， 依董事會之決議，授權董事長調整股東股利配股配息比率 5.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 2442 | 新美齊 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: (1)股票股利：每仟股無償配發70股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2元，計新台幣650,464,040元。 3.變更後發放股利種類及金額: (1)股票股利：每仟股無償配發71.11516340股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2.03186184元，計新台幣650,464,040元。 4.變更原因:扣除尚未既得之限制型員工權利新股，不得參與盈餘分配、配股或配息， 依董事會之決議，授權董事長調整股東股利配股配息比率 5.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260821 | 2442 | 新美齊 | revenue_breakout_low_response | 營收爆發低反應股 | 16 | 36 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: (1)股票股利：每仟股無償配發70股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2元，計新台幣650,464,040元。 3.變更後發放股利種類及金額: (1)股票股利：每仟股無償配發71.11516340股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2.03186184元，計新台幣650,464,040元。 4.變更原因:扣除尚未既得之限制型員工權利新股，不得參與盈餘分配、配股或配息， 依董事會之決議，授權董事長調整股東股利配股配息比率 5.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260821 | 2442 | 新美齊 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  |  | stale_signal | 1.董事會或股東會決議日期:NA 2.原發放股利種類及金額: (1)股票股利：每仟股無償配發70股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2元，計新台幣650,464,040元。 3.變更後發放股利種類及金額: (1)股票股利：每仟股無償配發71.11516340股，計新台幣227,662,410元；     (普通股股票股利22,141,929股，私募普通股股票股利624,312股)。 (2)現金股利：每股無償配發新台幣2.03186184元，計新台幣650,464,040元。 4.變更原因:扣除尚未既得之限制型員工權利新股，不得參與盈餘分配、配股或配息， 依董事會之決議，授權董事長調整股東股利配股配息比率 5.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2442 | 新美齊 | 2 | 2 | 4 | 6 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
