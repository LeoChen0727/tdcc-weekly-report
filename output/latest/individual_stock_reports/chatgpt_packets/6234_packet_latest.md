# INDIVIDUAL STOCK CHATGPT PACKET - 6234 高僑

## Metadata
- generated_at: 2026-09-19 15:54:14 Asia/Taipei
- stock_id: 6234
- stock_name: 高僑
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6234_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6234_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6234_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6234_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6234_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6234_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6234_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6234.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6234.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6234.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6234.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6234_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6234_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6234_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 35
- high: 38.5
- low: 35
- close: 38.5
- volume: 1245000
- ma5: 35.14
- ema23_primary: 35.39
- distance_to_ema23_pct: 8.79
- ma20: 35.23
- ma60: 37.49
- ma120: 41.01
- return_5d: 15.1
- return_20d: 10.16
- volume_ratio: 4.23
- distance_to_ma20_pct_auxiliary: 9.27
- distance_to_high_60_pct: -27.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,35.45,35.65,34.8,34.9,116000,36.27,-3.79,34.76,40.91,0.25
20260825,34.8,35.15,33.55,35.05,148000,36.17,-3.1,34.81,40.66,0.34
20260826,35.15,37,35.15,36.35,310000,36.19,0.45,35.03,40.45,0.79
20260827,36.1,37.5,36.1,36.7,280000,36.23,1.3,35.4,40.27,0.79
20260828,37.05,37.5,36.2,36.8,373000,36.28,1.44,35.63,40.09,1.06
20260831,36.8,37.1,35.5,35.8,164000,36.24,-1.21,35.81,39.91,0.48
20260901,36.1,36.7,35.8,35.8,264000,36.2,-1.11,35.93,39.72,0.79
20260902,35.8,36,35.5,35.55,132000,36.15,-1.65,35.95,39.59,0.42
20260903,35.95,35.95,34.1,34.1,177000,35.98,-5.22,35.92,39.41,0.58
20260904,34.4,34.4,33,34.2,291000,35.83,-4.54,35.93,39.2,0.96
20260907,34.45,36.3,34.2,35.75,398000,35.82,-0.2,35.84,39.07,1.38
20260908,35.75,35.8,34.1,34.3,347000,35.7,-3.91,35.73,38.92,1.27
20260909,35.7,36.7,34.95,35,355000,35.64,-1.79,35.61,38.79,1.29
20260910,34.65,35.2,34.2,35.2,210000,35.6,-1.13,35.56,38.68,0.79
20260911,34.25,34.5,33.4,33.45,398000,35.42,-5.57,35.37,38.51,1.58
20260914,33.2,34.2,32.65,33.85,212000,35.29,-4.08,35.23,38.33,0.85
20260915,33.75,34.3,33.5,33.5,138000,35.14,-4.67,35.1,38.1,0.57
20260916,33.5,34.9,33.5,34.85,188000,35.12,-0.76,35.08,37.92,0.77
20260917,35.15,35.7,35,35,141000,35.11,-0.31,35.05,37.66,0.58
20260918,35,38.5,35,38.5,1245000,35.39,8.79,35.23,37.49,4.23
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 53.95
- over_600_ratio: 53.4
- over_800_ratio: 52.07
- over_1000_ratio: 50.22
- over_400_change_1w: 0.03
- over_800_change_1w: 0.01
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,54.56,0.19,51.45,-0.05,49.62,-1.05,3,False,False
20260709,54.67,0.11,51.45,0,49.62,0,4,False,False
20260717,53.73,-0.94,51.45,0,49.62,0,0,False,False
20260724,52.9,-0.83,51.56,0.11,49.71,0.09,1,False,True
20260731,53.52,0.62,52.06,0.5,50.21,0.5,2,True,True
20260807,53.99,0.47,52.06,0,50.21,0,3,False,False
20260814,54.13,0.14,52.06,0,50.21,0,4,False,False
20260821,53.79,-0.34,52.06,0,50.21,0,5,False,False
20260828,53.96,0.17,52.06,0,50.21,0,6,False,False
20260904,54.31,0.35,52.06,0,50.21,0,7,False,False
20260911,53.92,-0.39,52.06,0,50.21,0,8,False,False
20260918,53.95,0.03,52.07,0.01,50.22,0.01,9,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6234 | 高僑 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | first_seen | 1.股東會決議日:115/06/26 2.許可從事競業行為之董事姓名及職稱: 獨立董事：趙淑佳 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司 4.許可從事競業行為之期間:任職本公司董事職務期間 5.決議情形（請依公司法第209條說明表決結果）: 經主席徵詢全體出席股東無異議照案通過 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用 7.所擔任該大陸地區事業之公司名稱及職務:不適用 8.所擔任該大陸地區事業地址:不適用 9.所擔任該大陸地區事業營業項目:不適用 10.對本公司財務業務之影響程度:不適用 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用 12.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6234 | 高僑 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | first_seen | 1.股東會決議日:115/06/26 2.許可從事競業行為之董事姓名及職稱: 獨立董事：趙淑佳 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司 4.許可從事競業行為之期間:任職本公司董事職務期間 5.決議情形（請依公司法第209條說明表決結果）: 經主席徵詢全體出席股東無異議照案通過 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用 7.所擔任該大陸地區事業之公司名稱及職務:不適用 8.所擔任該大陸地區事業地址:不適用 9.所擔任該大陸地區事業營業項目:不適用 10.對本公司財務業務之影響程度:不適用 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用 12.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 6234 | 高僑 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  |  | first_seen | 1.股東會決議日:115/06/26 2.許可從事競業行為之董事姓名及職稱: 獨立董事：趙淑佳 3.許可從事競業行為之項目:與本公司營業範圍相同或類似之公司 4.許可從事競業行為之期間:任職本公司董事職務期間 5.決議情形（請依公司法第209條說明表決結果）: 經主席徵詢全體出席股東無異議照案通過 6.所許可之競業行為如屬大陸地區事業之營業者，董事姓名及職稱 （非屬大陸地區事業之營業者，以下請輸〝不適用〞）:不適用 7.所擔任該大陸地區事業之公司名稱及職務:不適用 8.所擔任該大陸地區事業地址:不適用 9.所擔任該大陸地區事業營業項目:不適用 10.對本公司財務業務之影響程度:不適用 11.董事如有對該大陸地區事業從事投資者，其投資金額及持股比例:不適用 12.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6234 | 高僑 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
