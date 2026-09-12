# INDIVIDUAL STOCK CHATGPT PACKET - 2880 華南金

## Metadata
- generated_at: 2026-09-12 15:43:00 Asia/Taipei
- stock_id: 2880
- stock_name: 華南金
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2880_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2880_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2880_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2880_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2880.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2880.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2880.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2880.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2880_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2880_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2880_latest.md?ref=main

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
- date: 20260911
- open: 44.75
- high: 45.9
- low: 44.6
- close: 45.85
- volume: 18673673
- ma5: 44.9
- ema23_primary: 42.54
- distance_to_ema23_pct: 7.79
- ma20: 41.64
- ma60: 40.65
- ma120: 37.22
- return_5d: 4.2
- return_20d: 17.71
- volume_ratio: 0.91
- distance_to_ma20_pct_auxiliary: 10.11
- distance_to_high_60_pct: -0.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,38.6,39.25,38,39.2,46041639,41.26,-4.99,42.08,38.2,1.46
20260818,38.9,40.1,38.7,39.7,33199568,41.13,-3.48,42.02,38.33,1.04
20260819,39.55,39.7,38.65,39,24299348,40.95,-4.77,41.91,38.47,0.76
20260820,39.05,39.2,38.6,38.8,12367958,40.77,-4.84,41.79,38.62,0.4
20260821,38.65,39.8,38.6,39.6,17503839,40.68,-2.65,41.73,38.78,0.57
20260824,39.5,40.25,39.15,39.25,12930557,40.56,-3.22,41.63,38.94,0.43
20260825,39.15,40.5,39.15,39.8,17557402,40.49,-1.71,41.55,39.09,0.59
20260826,39.6,40.1,39.25,39.6,13831992,40.42,-2.03,41.44,39.21,0.48
20260827,39.8,40.05,39.35,39.35,9459728,40.33,-2.43,41.27,39.3,0.34
20260828,39.35,41.2,39.35,40.25,30246901,40.32,-0.18,41.1,39.36,1.1
20260831,40.25,41.4,40.2,41.35,48578786,40.41,2.33,41.02,39.42,1.72
20260901,40.8,42.2,40.8,41.95,23432105,40.54,3.48,40.95,39.54,0.83
20260902,41.95,43,41.5,43,22882451,40.74,5.54,40.91,39.7,0.81
20260903,42.9,43.75,42.65,43.45,16242371,40.97,6.06,40.88,39.83,0.59
20260904,43.75,44,43.15,44,12694801,41.22,6.74,40.86,39.98,0.47
20260907,44.7,44.7,43.95,44.35,13082688,41.48,6.91,40.88,40.12,0.49
20260908,44.5,45.25,44.1,45.15,13254248,41.79,8.05,40.95,40.27,0.51
20260909,44.85,45.25,44.05,44.35,9120535,42,5.59,41.01,40.4,0.37
20260910,44.35,45.6,44.2,44.8,13056360,42.23,6.08,41.3,40.52,0.6
20260911,44.75,45.9,44.6,45.85,18673673,42.54,7.79,41.64,40.65,0.91
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 82.05
- over_600_ratio: 80.96
- over_800_ratio: 80.25
- over_1000_ratio: 79.63
- over_400_change_1w: 0.08
- over_800_change_1w: 0.08
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,81.26,0.06,79.46,0.06,78.8,0.06,4,True,True
20260703,81.31,0.05,79.51,0.05,78.88,0.08,5,True,True
20260709,81.43,0.12,79.65,0.14,79,0.12,6,True,True
20260717,81.5,0.07,79.69,0.04,79.05,0.05,7,True,True
20260724,81.71,0.21,79.93,0.24,79.28,0.23,8,True,True
20260731,81.99,0.28,80.23,0.3,79.58,0.3,9,True,True
20260807,81.94,-0.05,80.16,-0.07,79.53,-0.05,0,False,False
20260814,81.61,-0.33,79.81,-0.35,79.15,-0.38,0,False,False
20260821,81.76,0.15,79.98,0.17,79.3,0.15,1,True,True
20260828,81.86,0.1,80.07,0.09,79.47,0.17,2,True,True
20260904,81.97,0.11,80.17,0.1,79.58,0.11,3,True,True
20260911,82.05,0.08,80.25,0.08,79.63,0.05,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2880 | 華南金 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | continued_many_days | 1.事實發生日:115/09/10 2.公司名稱:華南金融控股股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:無 5.發生緣由:公告本公司115年8月份自結盈餘 6.因應措施:無 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):  華南金控本月合併稅前淨利為40.02億元、合併稅後淨利為33.71億元； 累計合併稅前淨利286.32億元、合併稅後淨利為240.22億元，每股稅後盈餘為1.71元， 每股淨值為17.63元。  主要子公司自結合併損益說明如下： 華南銀行本月合併稅前淨利為33.10億元、合併稅後淨利為27.90億元； 累計合併稅前淨利226.00億元、合併稅後淨利為189.91億元，每股稅後盈餘為1.78元， 每股淨值為24.22元。             華南金融控股公司暨主要子公司115年8月份合併獲利(損失)資料：  　　　　　　　自結合併　自結合併　累計合併　累計合併　累計合併　累計合併 　　　　　　　稅前淨利　稅後淨利　稅前淨利　稅後淨利　每股稅前　每股稅後                 (損)      (損)      (損)      (損)      盈餘      盈餘 　　　　　　　（億元）　（億元）　（億元）　（億元）　 (虧損)    (虧損)                                                         (元)      (元) 華南金控　　　  40.02　   33.71　  286.32　  240.22 　  2.04　　  1.71 華南銀行　　　  33.10　　 27.90　  226.00　　189.91　   2.12　　  1.78 華南永昌證券　   5.18　    4.54 　  46.50　   39.85　　 7.10　　  6.09 華南產險    　   2.32　　  1.85 　  17.91　　 15.06 　  8.95　　  7.52 註1:上述資料均係集團自結合併數字 註2:未適用天災保險準備金之累計合併稅後每股盈餘(虧損) 　　華南金控為1.71元、華南產險為7.46元；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2880 | 華南金 | 10 | 9 | 5 | 10 | 14 | continued_many_days | 連續 10 日上榜，需區分醞釀延續或訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2880 | 華南金 | 4 | 0 | 217270.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
