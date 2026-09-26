# INDIVIDUAL STOCK CHATGPT PACKET - 3294 英濟

## Metadata
- generated_at: 2026-09-26 22:16:41 Asia/Taipei
- stock_id: 3294
- stock_name: 英濟
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3294_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3294_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3294_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3294_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3294.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3294.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3294.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3294.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3294_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3294_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3294_latest.md?ref=main

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
- date: 20260924
- open: 34
- high: 36.15
- low: 33
- close: 33.65
- volume: 7904000
- ma5: 31.82
- ema23_primary: 30.7
- distance_to_ema23_pct: 9.62
- ma20: 30.26
- ma60: 31.58
- ma120: 33.61
- return_5d: 12.17
- return_20d: 7.68
- volume_ratio: 11.72
- distance_to_ma20_pct_auxiliary: 11.19
- distance_to_high_60_pct: -19.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,31.65,31.65,30.9,31,194000,31.1,-0.31,30.73,34.06,0.68
20260831,31,31.2,30.3,30.45,169000,31.04,-1.91,30.78,33.91,0.6
20260901,30.6,30.85,30.3,30.6,192000,31.01,-1.31,30.79,33.78,0.69
20260902,30.1,30.6,30.1,30.2,218000,30.94,-2.39,30.77,33.67,0.81
20260903,30.45,31.2,29.55,29.55,477000,30.82,-4.13,30.73,33.52,1.7
20260904,30.15,30.65,29.5,30,265000,30.76,-2.46,30.72,33.4,0.94
20260907,30.05,30.2,29.75,29.85,155000,30.68,-2.7,30.67,33.31,0.57
20260908,29.9,30.3,29.7,29.7,243000,30.6,-2.93,30.59,33.21,0.93
20260909,29.85,30,29.6,29.7,174000,30.52,-2.7,30.48,33.04,0.7
20260910,29.9,29.9,29.1,29.35,253000,30.43,-3.53,30.37,32.9,1.02
20260911,28.8,29.2,28.7,28.85,215000,30.29,-4.77,30.24,32.71,0.88
20260914,28.85,29.4,28.6,29,179000,30.19,-3.93,30.14,32.53,0.79
20260915,28.75,29.4,28.65,28.65,203000,30.06,-4.69,30.04,32.35,0.92
20260916,28.7,29.25,28.7,29.25,182000,29.99,-2.47,29.98,32.19,0.82
20260917,30.3,30.5,29.65,30,272000,29.99,0.03,29.96,32.02,1.23
20260918,30.05,30.45,29.75,30.3,310000,30.02,0.94,29.95,31.86,1.34
20260921,30.3,30.85,30.15,30.8,274000,30.08,2.38,29.98,31.76,1.16
20260922,31.05,31.2,30,30.65,344000,30.13,1.73,29.99,31.67,1.39
20260923,32,33.7,32,33.7,1264000,30.43,10.76,30.14,31.62,4.19
20260924,34,36.15,33,33.65,7904000,30.7,9.62,30.26,31.58,11.72
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 51.75
- over_600_ratio: 50.21
- over_800_ratio: 49.74
- over_1000_ratio: 46.98
- over_400_change_1w: -0.16
- over_800_change_1w: 0.11
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,53.2,0.22,49.98,0.02,47.87,0.02,1,False,True
20260717,52.71,-0.49,49.9,-0.08,47.08,-0.79,0,False,False
20260724,52.31,-0.4,49.84,-0.06,47.07,-0.01,1,False,False
20260731,51.89,-0.42,49.78,-0.06,47.01,-0.06,0,False,False
20260807,52.19,0.3,49.78,0,47.01,0,1,False,False
20260814,51.79,-0.4,50.6,0.82,47.05,0.04,2,False,True
20260821,51.81,0.02,49.65,-0.95,46.88,-0.17,3,False,False
20260828,51.83,0.02,49.66,0.01,46.89,0.01,4,True,True
20260904,51.76,-0.07,49.64,-0.02,46.88,-0.01,0,False,False
20260911,51.72,-0.04,49.63,-0.01,46.87,-0.01,0,False,False
20260918,51.91,0.19,49.63,0,46.87,0,1,False,False
20260924,51.75,-0.16,49.74,0.11,46.98,0.11,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3294 | 英濟 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_overheated | 1.發生變動日期:115/06/18 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、 自然人董事或自然人監察人）:法人董事、自然人監察人 3.舊任者職稱及姓名: 法人董事：英濟股份有限公司代表人徐文麟 法人董事：英濟股份有限公司代表人姜同會 自然人董事：增田麻言 自然人監察人：張嘉正 4.舊任者簡歷: 徐文麟：英濟股份有限公司董事長 姜同會：英濟股份有限公司總經理 增田麻言：Barintec Co., Ltd.董事長 張嘉正：英濟股份有限公司財務長 5.新任者職稱及姓名: 法人董事：英濟股份有限公司代表人徐文麟 自然人監察人：張嘉正 6.新任者簡歷: 徐文麟：英濟股份有限公司董事長 張嘉正：英濟股份有限公司財務長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿改選 9.新任者選任時持股數: 法人董事：英濟股份有限公司代表人徐文麟-1,498,699股 自然人監察人：張嘉正-0股 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/04/25~115/04/24 11.新任生效日期:115/06/18~118/06/17 12.同任期董事變動比率:2/3 13.同任期獨立董事變動比率:不適用 14.同任期監察人變動比率:0 15.屬三分之一以上董事發生變動（請輸入是或否）:是 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第6款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3294 | 英濟 | 2 | 2 | 2 | 2 | 2 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
