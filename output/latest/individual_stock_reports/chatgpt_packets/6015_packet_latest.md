# INDIVIDUAL STOCK CHATGPT PACKET - 6015 宏遠證

## Metadata
- generated_at: 2026-08-09 22:28:01 Asia/Taipei
- stock_id: 6015
- stock_name: 宏遠證
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 184
- current_main_price_date: 20260805
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: high
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
- decision_score_high
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
- date: 20260805
- open: 16
- high: 16.15
- low: 15.85
- close: 15.95
- volume: 1188000
- ma5: 15.45
- ema23_primary: 16.3
- distance_to_ema23_pct: -2.13
- ma20: 16.3
- ma60: 17.34
- ma120: 15.55
- return_5d: 8.5
- return_20d: -8.33
- volume_ratio: 0.54
- distance_to_ma20_pct_auxiliary: -2.16
- distance_to_high_60_pct: -33.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,18.3,18.9,17.9,18.15,5898000,17.96,1.07,18.03,16.71,1.53
20260709,18.2,18.2,17.65,17.65,3343000,17.93,-1.57,18.01,16.78,0.94
20260713,17.8,18,17.15,17.3,3500000,17.88,-3.24,17.98,16.84,1.01
20260714,17.25,17.35,16.3,16.8,3992000,17.79,-5.56,17.9,16.9,1.17
20260715,17.1,17.6,16.95,17.55,2114000,17.77,-1.23,17.83,16.98,0.65
20260716,17.4,17.75,17.2,17.3,1472000,17.73,-2.43,17.78,17.05,0.47
20260717,17,17.1,16.4,16.5,2694000,17.63,-6.4,17.69,17.1,0.86
20260720,16.5,16.6,15.85,16,1792000,17.49,-8.53,17.57,17.14,0.58
20260721,16.2,16.45,16.2,16.4,633000,17.4,-5.75,17.45,17.2,0.22
20260722,16.6,16.9,16.6,16.6,1033000,17.33,-4.24,17.34,17.25,0.38
20260723,16.7,16.8,16.3,16.35,909000,17.25,-5.23,17.25,17.28,0.35
20260724,16.25,16.5,16.05,16.2,1750000,17.16,-5.62,17.16,17.32,0.7
20260727,16.2,16.2,15.8,16.1,1270000,17.08,-5.71,17.09,17.35,0.54
20260728,15.75,15.85,15.15,15.2,2687000,16.92,-10.16,16.98,17.37,1.14
20260729,15.3,15.45,14.2,14.7,2897000,16.73,-12.16,16.84,17.37,1.2
20260730,14.6,14.95,14.35,14.55,1817000,16.55,-12.1,16.69,17.37,0.76
20260731,15.2,15.8,15.2,15.65,2167000,16.48,-5.02,16.61,17.38,0.91
20260803,15.55,15.8,15.35,15.55,1852000,16.4,-5.18,16.5,17.37,0.78
20260804,15.6,15.75,15.4,15.55,767000,16.33,-4.77,16.38,17.36,0.34
20260805,16,16.15,15.85,15.95,1188000,16.3,-2.13,16.3,17.34,0.54
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 49.61
- over_600_ratio: 45.57
- over_800_ratio: 44.03
- over_1000_ratio: 42.21
- over_400_change_1w: 0.2
- over_800_change_1w: -0.14
- over_1000_change_1w: 0.12
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,51.29,0.13,45.87,-0.28,44.95,-0.28,3,False,False
20260529,53.12,1.83,47.14,1.27,46,1.05,4,True,True
20260605,53.44,0.32,48.24,1.1,46.72,0.72,5,True,True
20260612,52.28,-1.16,47.05,-1.19,45.93,-0.79,0,False,False
20260618,51.31,-0.97,46.53,-0.52,45.19,-0.74,0,False,False
20260626,50.14,-1.17,45.65,-0.88,44.13,-1.06,0,False,False
20260703,50.09,-0.05,44.97,-0.68,43.58,-0.55,0,False,False
20260709,50.3,0.21,44.8,-0.17,43.41,-0.17,1,False,False
20260717,49.82,-0.48,44.23,-0.57,42.21,-1.2,0,False,False
20260724,49.61,-0.21,44.38,0.15,41.88,-0.33,1,False,True
20260731,49.41,-0.2,44.17,-0.21,42.09,0.21,2,False,True
20260807,49.61,0.2,44.03,-0.14,42.21,0.12,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6015 | 宏遠證 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期:115/07/16 2.增資資金來源:國內第一次及第二次無擔保轉換公司債 3.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 4.全案發行總金額及股數(如屬盈餘或公積轉增資，發行股數則不含配發給員工部分): 發行總金額：新台幣104,658,080元 發行股數：普通股10,465,808股 5.採總括申報發行新股案件，本次發行金額及股數:不適用 6.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 7.每股面額:新臺幣10元 8.發行價格:不適用 9.員工認購股數或配發金額:不適用 10.公開銷售股數:不適用 11.原股東認購或無償配發比例(請註明暫定每仟股認購或配發股數):不適用 12.畸零股及逾期未認購股份之處理方式:不適用 13.本次發行新股之權利義務:與原已發行普通股股份相同 14.本次增資資金用途:不適用 15.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 16.其他應敘明事項: 本公司國內第一次及第二次無擔保轉換公司債換發新股之增資基準日為115年7月16日。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 6015 | 宏遠證 | 2 | 2 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
