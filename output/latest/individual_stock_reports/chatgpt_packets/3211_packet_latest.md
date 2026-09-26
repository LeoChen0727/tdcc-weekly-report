# INDIVIDUAL STOCK CHATGPT PACKET - 3211 順達

## Metadata
- generated_at: 2026-09-26 22:16:39 Asia/Taipei
- stock_id: 3211
- stock_name: 順達
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3211.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3211.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3211.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3211.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3211_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3211_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3211_latest.md?ref=main

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
- date: 20260924
- open: 383.5
- high: 383.5
- low: 374.5
- close: 378.5
- volume: 1163000
- ma5: 379.8
- ema23_primary: 374.44
- distance_to_ema23_pct: 1.09
- ma20: 378.05
- ma60: 376.61
- ma120: 386.51
- return_5d: 4.99
- return_20d: -4.78
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: 0.12
- distance_to_high_60_pct: -23.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,407.5,414.5,397.5,400,11113000,369.64,8.21,365.02,389.82,1.25
20260831,390,401.5,383,386.5,4505000,371.04,4.17,368.9,388.7,0.51
20260901,395.5,410,385,406,9549000,373.95,8.57,372.95,388.42,1.07
20260902,399,400.5,392,392,2717000,375.46,4.41,376.32,388.4,0.31
20260903,394.5,396.5,375,375,6072000,375.42,-0.11,377.25,387.62,0.72
20260904,382,387,374.5,386,3296000,376.3,2.58,379.62,387.3,0.41
20260907,398,398,383.5,384,3200000,376.94,1.87,380.32,387.06,0.42
20260908,387,389,373,375.5,2289000,376.82,-0.35,379.1,386.35,0.34
20260909,378,381.5,365,367,4826000,376,-2.39,376.85,385.32,0.77
20260910,368,382.5,367,374,3851000,375.84,-0.49,375.23,384.27,0.64
20260911,366,368.5,361,362,1692000,374.68,-3.39,373.77,383.17,0.29
20260914,356,372,349,362.5,2313000,373.67,-2.99,372.3,381.94,0.4
20260915,361,369.5,358,361,1875000,372.61,-3.12,371.23,380.42,0.33
20260916,362.5,377,362.5,370,2578000,372.4,-0.64,371.27,379.46,0.46
20260917,375.5,379.5,360.5,360.5,2265000,371.4,-2.94,371.55,378.48,0.42
20260918,368,369,361.5,368,1570000,371.12,-0.84,372.43,377.82,0.3
20260921,375,397,370,387.5,8625000,372.49,4.03,375.5,377.77,1.64
20260922,393,398,381,385,6065000,373.53,3.07,378.2,377.65,1.14
20260923,390.5,390.5,380,380,1762000,374.07,1.59,379,377.1,0.36
20260924,383.5,383.5,374.5,378.5,1163000,374.44,1.09,378.05,376.61,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 49.44
- over_600_ratio: 43.85
- over_800_ratio: 42.04
- over_1000_ratio: 39.19
- over_400_change_1w: 1.52
- over_800_change_1w: 1.8
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,53.45,1.36,45.37,-0.03,42.46,-0.11,2,False,False
20260717,54.05,0.6,45.38,0.01,41.85,-0.61,3,False,True
20260724,53.56,-0.49,44.68,-0.7,40.68,-1.17,0,False,False
20260731,51.13,-2.43,42.51,-2.17,39.01,-1.67,0,False,False
20260807,50.85,-0.28,41.64,-0.87,36.14,-2.87,0,False,False
20260814,52.94,2.09,42.55,0.91,39.76,3.62,1,True,True
20260821,50.41,-2.53,40.72,-1.83,38.3,-1.46,0,False,False
20260828,50.63,0.22,41.16,0.44,40.63,2.33,1,False,True
20260904,50.21,-0.42,41.25,0.09,38.94,-1.69,2,False,True
20260911,49.27,-0.94,41.08,-0.17,39.3,0.36,3,False,True
20260918,47.92,-1.35,40.24,-0.84,39.18,-0.12,0,False,False
20260924,49.44,1.52,42.04,1.8,39.19,0.01,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3211 | 順達 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會決議日期:115/07/29 2.增資資金來源:員工認股權憑證執行轉換 3.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 4.全案發行總金額及股數(如屬盈餘或公積轉增資，發行股數則不含配發給員工部分):  不適用 5.採總括申報發行新股案件，本次發行金額及股數:不適用 6.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 7.每股面額:新台幣10元 8.發行價格:每股認購價格新台幣67.60元 9.員工認購股數或配發金額:82,000股 10.公開銷售股數:不適用 11.原股東認購或無償配發比例(請註明暫定每仟股認購或配發股數):不適用 12.畸零股及逾期未認購股份之處理方式:不適用 13.本次發行新股之權利義務:與已發行普通股股票相同 14.本次增資資金用途:不適用 15.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 16.其他應敘明事項:   (1)本次員工認股權憑證轉換新股之增資基準日訂為115年07月29日。   (2)本次增資後實收資本額為新台幣1,543,870,210元。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 3211 | 順達 | 2 | 2 | 3 | 6 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
