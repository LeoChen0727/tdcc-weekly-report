# INDIVIDUAL STOCK CHATGPT PACKET - 6015 宏遠證

## Metadata
- generated_at: 2026-09-20 22:17:37 Asia/Taipei
- stock_id: 6015
- stock_name: 宏遠證
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6015_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6015_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6015_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6015_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6015.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6015.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6015.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6015.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6015_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6015_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6015_latest.md?ref=main

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
- open: 17.4
- high: 17.6
- low: 17.3
- close: 17.6
- volume: 3165000
- ma5: 17.23
- ema23_primary: 16.78
- distance_to_ema23_pct: 4.89
- ma20: 16.72
- ma60: 16.48
- ma120: 16.27
- return_5d: 3.83
- return_20d: 10.69
- volume_ratio: 1.46
- distance_to_ma20_pct_auxiliary: 5.25
- distance_to_high_60_pct: -6.88

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,15.9,16.1,15.75,15.8,788000,15.92,-0.73,15.55,17.33,0.46
20260825,15.75,15.75,15.45,15.55,968000,15.89,-2.11,15.57,17.27,0.6
20260826,15.7,16.05,15.7,15.95,1049000,15.89,0.37,15.63,17.2,0.69
20260827,16.1,16.3,16,16.05,1508000,15.9,0.92,15.71,17.12,1
20260828,16.3,16.75,16.3,16.4,2381000,15.95,2.85,15.74,17.01,1.56
20260831,16.15,16.2,15.8,16.2,1594000,15.97,1.46,15.78,16.91,1.06
20260901,16.35,16.75,16.35,16.6,2370000,16.02,3.63,15.83,16.81,1.49
20260902,16.5,16.55,16.2,16.3,908000,16.04,1.6,15.85,16.74,0.58
20260903,16.4,16.85,16.35,16.4,2104000,16.07,2.04,15.89,16.7,1.31
20260904,16.65,16.85,16.45,16.8,2319000,16.13,4.13,15.97,16.68,1.4
20260907,17.05,17.1,16.55,16.85,2173000,16.19,4.06,16.06,16.66,1.32
20260908,17.75,17.9,17.55,17.85,5927000,16.33,9.3,16.2,16.65,3.16
20260909,18.2,18.2,17.25,17.45,5632000,16.42,6.25,16.27,16.63,2.78
20260910,17.25,17.4,17.1,17.15,1390000,16.48,4.04,16.33,16.61,0.71
20260911,16.8,17.15,16.75,16.95,2035000,16.52,2.58,16.36,16.58,1.05
20260914,16.85,17.4,16.75,17.35,1721000,16.59,4.57,16.43,16.57,0.88
20260915,17.25,17.25,16.75,16.85,1668000,16.61,1.42,16.48,16.53,0.84
20260916,16.8,17.2,16.8,17,1125000,16.65,2.13,16.56,16.5,0.57
20260917,17.15,17.55,17.1,17.35,2645000,16.7,3.86,16.64,16.49,1.28
20260918,17.4,17.6,17.3,17.6,3165000,16.78,4.89,16.72,16.48,1.46
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 51.28
- over_600_ratio: 47.85
- over_800_ratio: 46.08
- over_1000_ratio: 44.28
- over_400_change_1w: 0.23
- over_800_change_1w: 0.38
- over_1000_change_1w: -0.1
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,50.09,-0.05,44.97,-0.68,43.58,-0.55,0,False,False
20260709,50.3,0.21,44.8,-0.17,43.41,-0.17,1,False,False
20260717,49.82,-0.48,44.23,-0.57,42.21,-1.2,0,False,False
20260724,49.61,-0.21,44.38,0.15,41.88,-0.33,1,False,True
20260731,49.41,-0.2,44.17,-0.21,42.09,0.21,2,False,True
20260807,49.61,0.2,44.03,-0.14,42.21,0.12,3,False,True
20260814,49.77,0.16,44.11,0.08,42.03,-0.18,4,False,True
20260821,49.91,0.14,43.89,-0.22,41.59,-0.44,5,False,False
20260828,49.65,-0.26,43.7,-0.19,42.05,0.46,6,False,True
20260904,51.05,1.4,45.79,2.09,44.2,2.15,7,True,True
20260911,51.05,0,45.7,-0.09,44.38,0.18,8,False,True
20260918,51.28,0.23,46.08,0.38,44.28,-0.1,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6015 | 宏遠證 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:宏遠證券股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司自行結算一一五年八月份合併損益：  (1)八月份稅前淨(損)益:404,761仟元，累計至八月底稅前淨(損)益:1,540,867仟元  (2)八月份稅後淨(損)益:392,611仟元，累計至八月底稅後淨(損)益:1,392,044仟元  (3)八月份每股稅後(損)益:0.97元，累計至八月底每股稅後(損)益:3.5元 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6015 | 宏遠證 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:宏遠證券股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司自行結算一一五年八月份合併損益：  (1)八月份稅前淨(損)益:404,761仟元，累計至八月底稅前淨(損)益:1,540,867仟元  (2)八月份稅後淨(損)益:392,611仟元，累計至八月底稅後淨(損)益:1,392,044仟元  (3)八月份每股稅後(損)益:0.97元，累計至八月底每股稅後(損)益:3.5元 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6015 | 宏遠證 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:宏遠證券股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:公告本公司自行結算一一五年八月份合併損益：  (1)八月份稅前淨(損)益:404,761仟元，累計至八月底稅前淨(損)益:1,540,867仟元  (2)八月份稅後淨(損)益:392,611仟元，累計至八月底稅後淨(損)益:1,392,044仟元  (3)八月份每股稅後(損)益:0.97元，累計至八月底每股稅後(損)益:3.5元 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第9款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6015 | 宏遠證 | 4 | 4 | 4 | 7 | 11 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 11 次，但尚未有效突破，需等待攻擊確認。 |

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
