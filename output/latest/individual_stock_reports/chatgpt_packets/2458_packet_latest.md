# INDIVIDUAL STOCK CHATGPT PACKET - 2458 義隆

## Metadata
- generated_at: 2026-10-07 22:17:26 Asia/Taipei
- stock_id: 2458
- stock_name: 義隆
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2458_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2458_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2458_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2458_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2458_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2458_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2458_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2458.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2458.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2458.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2458.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2458_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2458_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2458_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20261002
- open: 138
- high: 139.5
- low: 136.5
- close: 138
- volume: 1469046
- ma5: 137.5
- ema23_primary: 134.87
- distance_to_ema23_pct: 2.32
- ma20: 131.47
- ma60: 146.69
- ma120: 150.81
- return_5d: 6.98
- return_20d: 0.73
- volume_ratio: 1.03
- distance_to_ma20_pct_auxiliary: 4.96
- distance_to_high_60_pct: -27.18

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,137,137.5,133,133,1889453,143.54,-7.34,141.15,158.73,0.81
20260904,133,134,131.5,133,1513536,142.66,-6.77,140.72,158.51,0.73
20260907,128,131,124.5,131,2608621,141.69,-7.54,140,158.26,1.29
20260908,131,131,128,130.5,1544886,140.76,-7.29,139.25,157.99,0.79
20260909,130.5,131,129,130,1027361,139.86,-7.05,138.45,157.64,0.55
20260910,130,130,127.5,128,993979,138.87,-7.83,137.6,157.22,0.55
20260911,126,128,126,126.5,892804,137.84,-8.23,136.7,156.72,0.52
20260914,126,127.5,124.5,126.5,1181243,136.9,-7.59,135.8,155.97,0.69
20260915,126.5,127,125,125,724849,135.9,-8.02,135,155.07,0.45
20260916,126,129.5,126,128.5,756459,135.29,-5.02,134.15,154.45,0.51
20260917,128.5,130.5,128.5,129,904593,134.76,-4.28,133.3,153.87,0.69
20260918,130.5,132.5,128.5,132,1542845,134.53,-1.88,132.88,153.07,1.21
20260921,132,132.5,130,130.5,883659,134.2,-2.75,132.45,152.38,0.69
20260922,132,132,129,129.5,1905883,133.81,-3.22,132.05,151.53,1.48
20260923,130.5,131,128.5,129,1320418,133.41,-3.3,131.53,150.53,1.01
20260924,129,138,128.5,137.5,2731471,133.75,2.81,131.43,149.8,1.99
20260929,138,138,135.5,136,1645198,133.93,1.54,131.3,148.97,1.19
20260930,137,137.5,135.5,137.5,1489305,134.23,2.44,131.4,148.2,1.08
20261001,137,139,136,138.5,1517721,134.59,2.91,131.43,147.53,1.08
20261002,138,139.5,136.5,138,1469046,134.87,2.32,131.47,146.69,1.03
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 57.06
- over_600_ratio: 54.15
- over_800_ratio: 51.77
- over_1000_ratio: 48.44
- over_400_change_1w: 0.07
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.36
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,60.91,0.11,54.26,0.07,49.69,-0.85,2,False,True
20260724,60.78,-0.13,54.06,-0.2,49.8,0.11,3,False,True
20260731,60.19,-0.59,53.06,-1,49.38,-0.42,0,False,False
20260807,58.72,-1.47,52.12,-0.94,48.51,-0.87,0,False,False
20260814,58.95,0.23,52.59,0.47,49.25,0.74,1,True,True
20260821,59.36,0.41,52.96,0.37,49.87,0.62,2,True,True
20260828,58.23,-1.13,52.38,-0.58,49.65,-0.22,0,False,False
20260904,57.39,-0.84,51.45,-0.93,49.02,-0.63,0,False,False
20260911,57.5,0.11,51.88,0.43,48.84,-0.18,1,False,True
20260918,57.31,-0.19,51.82,-0.06,48.77,-0.07,2,False,False
20260924,56.99,-0.32,51.5,-0.32,48.08,-0.69,0,False,False
20261002,57.06,0.07,51.77,0.27,48.44,0.36,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2458 | 義隆 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 57.0 |  |  | neckline_challenge |  | no_signal | continued_2_3d | 1.契約種類:租地委建 2.事實發生日:115/10/1~115/10/1 3.董事會通過日期: 民國115年10月1日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 尚未確定 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 將原112年3月22日董事會通過之預算金額新台幣6,500,000仟元提高 至新台幣7,500,000仟元 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 提升研發及營運效益 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 民國115年10月01日 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 現因建築方案調整及原物料、人力成本上漲，故擬提高AI智慧園區廠辦大樓 預計營造費用額度至新台幣75億元。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2458 | 義隆 | 3 | 3 | 4 | 4 | 4 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 2458 | 義隆 | 44 | 0 | 972110.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
