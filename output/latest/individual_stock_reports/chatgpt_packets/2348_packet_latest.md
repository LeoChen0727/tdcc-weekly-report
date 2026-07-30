# INDIVIDUAL STOCK CHATGPT PACKET - 2348 海悅

## Metadata
- generated_at: 2026-07-31 01:14:39 Asia/Taipei
- stock_id: 2348
- stock_name: 海悅
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 315
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260724-88f3a903b384007d
- official_tdcc_signal_date: 20260724
- latest_tdcc_date: 20260724
- tdcc_rows: 13
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2348_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2348_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2348_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2348_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2348.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2348.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2348.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2348.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2348_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2348_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2348_latest.md?ref=main

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
- date: 20260730
- open: 74.9
- high: 77
- low: 74.1
- close: 76.3
- volume: 367815
- ma5: 76.78
- ema23_primary: 76.21
- distance_to_ema23_pct: 0.12
- ma20: 76.81
- ma60: 73.11
- ma120: 74.47
- return_5d: -3.66
- return_20d: 7.01
- volume_ratio: 0.54
- distance_to_ma20_pct_auxiliary: -0.66
- distance_to_high_60_pct: -7.29

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,71.5,72,71.3,71.8,295694,72.08,-0.38,72.8,72.62,0.22
20260703,72,76.6,72,76,1606325,72.4,4.97,72.88,72.56,1.16
20260706,76,77.9,75.3,76.3,716994,72.73,4.91,73.08,72.55,0.52
20260707,77.2,79,74.6,74.7,913362,72.89,2.48,73.27,72.51,0.65
20260708,74.7,77,74.7,76.1,585746,73.16,4.02,73.52,72.48,0.42
20260709,77.2,78.5,75.6,75.9,489881,73.39,3.42,73.41,72.45,0.43
20260713,76,78.3,74.5,76.9,595540,73.68,4.37,73.62,72.41,0.63
20260714,77.5,78.4,75,76,730170,73.87,2.88,73.78,72.37,0.85
20260715,76.6,77,76.1,76.2,340086,74.07,2.88,73.97,72.35,0.41
20260716,77,82.3,76.4,79.9,1867658,74.55,7.17,74.23,72.4,2.18
20260717,79.9,79.9,77.2,78,1027175,74.84,4.22,74.25,72.41,1.24
20260720,78.7,78.9,76.5,77.5,686156,75.06,3.25,74.28,72.42,0.91
20260721,78.2,79.8,78,78.9,568816,75.38,4.67,74.63,72.5,0.87
20260722,79.1,79.7,78.5,78.8,324231,75.67,4.14,75,72.59,0.51
20260723,78.7,79.3,77.4,79.2,454969,75.96,4.26,75.41,72.71,0.71
20260724,78.8,78.8,77,78.2,408197,76.15,2.69,75.77,72.81,0.63
20260727,78.8,78.8,77.5,77.8,490272,76.29,1.99,76.14,72.89,0.75
20260728,77.5,77.5,76,76.4,506464,76.3,0.14,76.39,72.98,0.77
20260729,76.4,77,73.5,75.2,738915,76.2,-1.32,76.56,73.03,1.08
20260730,74.9,77,74.1,76.3,367815,76.21,0.12,76.81,73.11,0.54
```

## Latest TDCC Snapshot
- as_of_date: 20260724
- over_400_ratio: 69.35
- over_600_ratio: 67.72
- over_800_ratio: 67.24
- over_1000_ratio: 65.5
- over_400_change_1w: 0.31
- over_800_change_1w: 1.16
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260508,70.62,-0.08,68.31,-0.08,67.13,-0.01,0,False,False
20260515,70.54,-0.08,68.23,-0.08,67.11,-0.02,0,False,False
20260522,70.52,-0.02,67.71,-0.52,67.11,0,0,False,False
20260529,70.49,-0.03,67.72,0.01,67.12,0.01,1,False,True
20260605,70.13,-0.36,67.72,0,67.12,0,0,False,False
20260612,69.79,-0.34,67.98,0.26,67.38,0.26,1,False,True
20260618,69.06,-0.73,66.84,-1.14,66.24,-1.14,0,False,False
20260626,68.42,-0.64,66.06,-0.78,65.46,-0.78,0,False,False
20260703,68.17,-0.25,66.07,0.01,65.47,0.01,1,False,True
20260709,68.84,0.67,66.12,0.05,65.52,0.05,2,True,True
20260717,69.04,0.2,66.08,-0.04,65.48,-0.04,3,False,False
20260724,69.35,0.31,67.24,1.16,65.5,0.02,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2348 | 海悅 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/17 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放特別股股利種類及金額: 特別股現金股息每股配發新台幣1.6元，合計為新台幣48,000,000元; 4.除權（息）交易日:115/08/04 5.最後過戶日:115/08/05 6.停止過戶起始日期:115/08/06 7.停止過戶截止日期:115/08/10 8.除權（息）基準日:115/08/10 9.特別股最後申請轉換日期:NA 10.特別股停止轉換起始日期:NA 11.特別股停止轉換截止日期:NA 12.特別股現金股利發放日期:115/09/08 13.其他應敘明事項: (1)擬定115年8月10日為除息基準日，依法自115年8月6日至115年8月10日止停止股票 過戶，凡持有本公司股票而尚未辦理過戶之股東，請於民國115年8月5日16時30分前 親臨本公司股務代理機構「群益金鼎證券股份有限公司股務代理部」(台北市大安區 敦化南路2段97號B2，電話：02-27023999)辦理過戶手續，以憑辦理配息事宜，掛號 郵寄者以民國115年8月5日(最後過戶日)郵戳日期為憑。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2348 | 海悅 | revenue_breakout_low_response | 營收爆發低反應股 | 15.0 | 28.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/17 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放特別股股利種類及金額: 特別股現金股息每股配發新台幣1.6元，合計為新台幣48,000,000元; 4.除權（息）交易日:115/08/04 5.最後過戶日:115/08/05 6.停止過戶起始日期:115/08/06 7.停止過戶截止日期:115/08/10 8.除權（息）基準日:115/08/10 9.特別股最後申請轉換日期:NA 10.特別股停止轉換起始日期:NA 11.特別股停止轉換截止日期:NA 12.特別股現金股利發放日期:115/09/08 13.其他應敘明事項: (1)擬定115年8月10日為除息基準日，依法自115年8月6日至115年8月10日止停止股票 過戶，凡持有本公司股票而尚未辦理過戶之股東，請於民國115年8月5日16時30分前 親臨本公司股務代理機構「群益金鼎證券股份有限公司股務代理部」(台北市大安區 敦化南路2段97號B2，電話：02-27023999)辦理過戶手續，以憑辦理配息事宜，掛號 郵寄者以民國115年8月5日(最後過戶日)郵戳日期為憑。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2348 | 海悅 | 2 | 2 | 2 | 3 | 4 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2348 | 海悅 | 8 | 0 | 330590.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
