# INDIVIDUAL STOCK CHATGPT PACKET - 2476 鉅祥

## Metadata
- generated_at: 2026-09-20 22:16:17 Asia/Taipei
- stock_id: 2476
- stock_name: 鉅祥
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2476_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2476_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2476_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2476_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2476.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2476.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2476.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2476.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2476_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2476_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2476_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 120.5
- high: 126
- low: 119
- close: 124
- volume: 2036068
- ma5: 119.5
- ema23_primary: 120.84
- distance_to_ema23_pct: 2.61
- ma20: 121.58
- ma60: 122.37
- ma120: 118.89
- return_5d: 5.08
- return_20d: 6.44
- volume_ratio: 1.4
- distance_to_ma20_pct_auxiliary: 1.99
- distance_to_high_60_pct: -11.43

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,116,118,114,115.5,858844,120.33,-4.01,119.12,122.73,0.47
20260825,115,120.5,112.5,120.5,2196705,120.34,0.13,119.6,122.71,1.2
20260826,120,127,119.5,125.5,3530774,120.77,3.91,120.58,122.77,1.95
20260827,125.5,128,124,126.5,2486571,121.25,4.33,121.62,122.89,1.35
20260828,126.5,127.5,123.5,125.5,2057693,121.61,3.2,122.22,122.93,1.1
20260831,124.5,126,122.5,125.5,1342005,121.93,2.93,122.55,123.01,0.73
20260901,126,130,125.5,127.5,2318908,122.39,4.17,122.97,123.13,1.22
20260902,127,127.5,125,125.5,989187,122.65,2.32,123.03,123.26,0.53
20260903,126.5,126.5,121.5,122.5,1245283,122.64,-0.11,122.78,123.21,0.68
20260904,124.5,124.5,119.5,121,1628089,122.5,-1.23,122.55,123.25,0.88
20260907,124,124,120.5,122,1138213,122.46,-0.38,122.35,123.3,0.63
20260908,122,123.5,118,119.5,1514963,122.21,-2.22,122.1,123.24,0.84
20260909,119,120.5,118.5,120,866060,122.03,-1.66,121.7,123.11,0.5
20260910,118.5,119.5,117.5,119,645900,121.78,-2.28,121.5,123.1,0.39
20260911,117.5,118.5,116,118,931731,121.46,-2.85,121.4,123.03,0.58
20260914,117.5,120.5,115,119.5,1103850,121.3,-1.48,121.4,122.93,0.68
20260915,118,120,116.5,117,691939,120.94,-3.26,121.28,122.79,0.45
20260916,117.5,118.5,116.5,117.5,734370,120.65,-2.61,121.2,122.61,0.5
20260917,118,120.5,117.5,119.5,774132,120.56,-0.88,121.2,122.47,0.53
20260918,120.5,126,119,124,2036068,120.84,2.61,121.58,122.37,1.4
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 67.78
- over_600_ratio: 64.97
- over_800_ratio: 61.13
- over_1000_ratio: 59.95
- over_400_change_1w: -0.02
- over_800_change_1w: -0.37
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 18
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,66.2,0.44,60.2,0.74,57.75,-0.06,7,False,True
20260709,66.28,0.08,59.76,-0.44,58.13,0.38,8,False,True
20260717,67.21,0.93,60.83,1.07,58.81,0.68,9,True,True
20260724,67.02,-0.19,61.12,0.29,59.53,0.72,10,False,True
20260731,67.32,0.3,61.11,-0.01,59.91,0.38,11,False,True
20260807,68.01,0.69,62.31,1.2,60.28,0.37,12,False,True
20260814,67.55,-0.46,62.19,-0.12,61.02,0.74,13,False,True
20260821,67.31,-0.24,62.19,0,60.58,-0.44,14,False,False
20260828,67.88,0.57,62.26,0.07,59.43,-1.15,15,False,True
20260904,67.87,-0.01,61.64,-0.62,59.23,-0.2,16,False,False
20260911,67.8,-0.07,61.5,-0.14,59.95,0.72,17,False,True
20260918,67.78,-0.02,61.13,-0.37,59.95,0,18,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2476 | 鉅祥 | pullback_rebound | 回檔後短線轉強 | 62.0 |  |  |  |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:鉅祥企業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由: (1)合併營業收入(當月與去年同期比較)(單位：新台幣仟元)   項目     115年08月  114年08月  成長率 --------   ---------  --------- -------- 合併營收    950,786    674,112   41.04% (2)合併營業收入(當月與上月比較)(單位：新台幣仟元)   項目     115年08月  115年07月  成長率 --------   ---------  --------- -------- 合併營收    950,786    970,526   -2.03% (3)累計合併營業收入(單位：新台幣仟元)   項目     115年01-08月   114年01-08月  成長率 --------- -------------  ------------- -------- 合併營收    6,655,990      4,760,639    39.81% 上列數字係本公司自結數，未經會計師簽證或核閱。 6.因應措施:發布重大訊息 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):  無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 2476 | 鉅祥 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:鉅祥企業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由: (1)合併營業收入(當月與去年同期比較)(單位：新台幣仟元)   項目     115年08月  114年08月  成長率 --------   ---------  --------- -------- 合併營收    950,786    674,112   41.04% (2)合併營業收入(當月與上月比較)(單位：新台幣仟元)   項目     115年08月  115年07月  成長率 --------   ---------  --------- -------- 合併營收    950,786    970,526   -2.03% (3)累計合併營業收入(單位：新台幣仟元)   項目     115年01-08月   114年01-08月  成長率 --------- -------------  ------------- -------- 合併營收    6,655,990      4,760,639    39.81% 上列數字係本公司自結數，未經會計師簽證或核閱。 6.因應措施:發布重大訊息 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):  無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 2476 | 鉅祥 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/09/07 2.公司名稱:鉅祥企業股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由: (1)合併營業收入(當月與去年同期比較)(單位：新台幣仟元)   項目     115年08月  114年08月  成長率 --------   ---------  --------- -------- 合併營收    950,786    674,112   41.04% (2)合併營業收入(當月與上月比較)(單位：新台幣仟元)   項目     115年08月  115年07月  成長率 --------   ---------  --------- -------- 合併營收    950,786    970,526   -2.03% (3)累計合併營業收入(單位：新台幣仟元)   項目     115年01-08月   114年01-08月  成長率 --------- -------------  ------------- -------- 合併營收    6,655,990      4,760,639    39.81% 上列數字係本公司自結數，未經會計師簽證或核閱。 6.因應措施:發布重大訊息 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項):  無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2476 | 鉅祥 | 1 | 1 | 1 | 5 | 14 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2476 | 鉅祥 | 88 | 0 | 13007610.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
