# INDIVIDUAL STOCK CHATGPT PACKET - 9945 潤泰新

## Metadata
- generated_at: 2026-09-26 15:53:56 Asia/Taipei
- stock_id: 9945
- stock_name: 潤泰新
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/9945_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/9945_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/9945_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9945_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9945_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/9945_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/9945_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/9945.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/9945.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/9945.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/9945.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/9945_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/9945_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/9945_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 30.35
- high: 30.4
- low: 29.6
- close: 29.9
- volume: 13127733
- ma5: 29.32
- ema23_primary: 28.57
- distance_to_ema23_pct: 4.64
- ma20: 28.41
- ma60: 27.59
- ma120: 26.19
- return_5d: 3.28
- return_20d: 4.55
- volume_ratio: 2.32
- distance_to_ma20_pct_auxiliary: 5.24
- distance_to_high_60_pct: -3.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,28.6,28.6,27.8,28,10359933,28.15,-0.54,28.19,26.95,1.19
20260831,27.9,28,27.7,27.8,4469745,28.12,-1.15,28.23,26.99,0.52
20260901,27.6,28.1,27.6,28.05,4192254,28.12,-0.24,28.3,27.04,0.49
20260902,27.9,28.4,27.85,28.3,3302368,28.13,0.59,28.39,27.1,0.39
20260903,28.3,28.5,28.15,28.25,4124099,28.14,0.38,28.49,27.15,0.49
20260904,28.3,28.5,28.05,28.45,3851767,28.17,1,28.57,27.19,0.46
20260907,28.7,28.7,27.8,27.9,5082933,28.15,-0.87,28.61,27.22,0.61
20260908,27.9,28.15,27.75,28.05,2456877,28.14,-0.31,28.66,27.24,0.3
20260909,28,28.2,27.8,28.2,3065040,28.14,0.2,28.7,27.26,0.38
20260910,27.9,28.05,27.7,27.75,2448901,28.11,-1.28,28.74,27.28,0.31
20260911,27.75,28.1,27.6,28.1,5061036,28.11,-0.03,28.65,27.3,0.79
20260914,27.85,27.95,27.65,27.85,2798187,28.09,-0.85,28.54,27.3,0.51
20260915,27.8,27.95,27.65,27.95,3583516,28.08,-0.45,28.45,27.32,0.7
20260916,28.1,28.4,27.95,28.05,4061805,28.07,-0.09,28.36,27.34,0.82
20260917,28.15,28.95,28.05,28.95,10535444,28.15,2.85,28.32,27.38,2.01
20260918,29.65,29.65,28.7,28.95,11972321,28.21,2.61,28.29,27.41,2.22
20260921,29.15,29.25,28.9,29.25,4897359,28.3,3.36,28.3,27.46,0.95
20260922,29.3,29.4,28.85,28.95,5007814,28.35,2.1,28.32,27.49,0.99
20260923,29.2,29.75,28.95,29.55,8610289,28.45,3.85,28.35,27.54,1.64
20260924,30.35,30.4,29.6,29.9,13127733,28.57,4.64,28.41,27.59,2.32
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 66.36
- over_600_ratio: 64.1
- over_800_ratio: 62.89
- over_1000_ratio: 62.1
- over_400_change_1w: 0.1
- over_800_change_1w: 0.15
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,64.53,-0.43,61.06,-0.54,60.44,-0.36,0,False,False
20260717,64.84,0.31,61.38,0.32,60.79,0.35,1,True,True
20260724,64.96,0.12,61.63,0.25,60.85,0.06,2,True,True
20260731,65.3,0.34,61.97,0.34,61.15,0.3,3,True,True
20260807,65.43,0.13,61.96,-0.01,61.3,0.15,4,False,True
20260814,65.6,0.17,62.18,0.22,61.5,0.2,5,True,True
20260821,66.2,0.6,62.91,0.73,62.16,0.66,6,True,True
20260828,66.15,-0.05,62.84,-0.07,62.07,-0.09,0,False,False
20260904,66.03,-0.12,62.6,-0.24,61.89,-0.18,0,False,False
20260911,66.1,0.07,62.61,0.01,61.86,-0.03,1,False,True
20260918,66.26,0.16,62.74,0.13,62.09,0.23,2,True,True
20260924,66.36,0.1,62.89,0.15,62.1,0.01,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 9945 | 潤泰新 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.契約種類:承攬契約、結算協議書 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 潤德室內裝修設計工程(股)公司、子公司 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: (1)契約內容：【潤泰之森公設景觀梯廳裝修工程】之承攬契約    契約金額：新台幣(以下同)453,021,637元(未稅)    契約起訖日期：開工日起至完工日止之工程期限為450個工作天。 (2)契約內容：【華山松江公設景觀梯廳裝修工程】之結算協議    原契約金額：92,018,778元(未稅)(業經114年03月12日董事會決議並公告)    本次追加金額：3,132,692元(未稅)    結算後總金額：95,151,470元(未稅) 7.專業估價者事務所或公司名稱及其估價結果: 契約內容：【潤泰之森公設景觀梯廳裝修工程】之承攬契約 中鼎不動產估價師事務所   估價金額453,386,946元(未稅) 8.不動產估價師姓名: 中鼎不動產估價師事務所：簡武池 9.不動產估價師開業證書字號: 中鼎不動產估價師事務所：(100)北市估字第000172號 10.取得之具體目的: 公設梯廳景觀裝修承攬及結算 11.本次交易表示異議之董事意見: 不適用 12.本次交易為關係人交易:是 13.監察人承認或審計委員會同意日期: 民國115年9月23日 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 114/03/12 22.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 9945 | 潤泰新 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  | no_signal | stale_signal | 1.契約種類:承攬契約、結算協議書 2.事實發生日:115/9/23~115/9/23 3.董事會通過日期: 民國115年9月23日 4.其他核決日期: 不適用 5.契約相對人及其與公司之關係: 潤德室內裝修設計工程(股)公司、子公司 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: (1)契約內容：【潤泰之森公設景觀梯廳裝修工程】之承攬契約    契約金額：新台幣(以下同)453,021,637元(未稅)    契約起訖日期：開工日起至完工日止之工程期限為450個工作天。 (2)契約內容：【華山松江公設景觀梯廳裝修工程】之結算協議    原契約金額：92,018,778元(未稅)(業經114年03月12日董事會決議並公告)    本次追加金額：3,132,692元(未稅)    結算後總金額：95,151,470元(未稅) 7.專業估價者事務所或公司名稱及其估價結果: 契約內容：【潤泰之森公設景觀梯廳裝修工程】之承攬契約 中鼎不動產估價師事務所   估價金額453,386,946元(未稅) 8.不動產估價師姓名: 中鼎不動產估價師事務所：簡武池 9.不動產估價師開業證書字號: 中鼎不動產估價師事務所：(100)北市估字第000172號 10.取得之具體目的: 公設梯廳景觀裝修承攬及結算 11.本次交易表示異議之董事意見: 不適用 12.本次交易為關係人交易:是 13.監察人承認或審計委員會同意日期: 民國115年9月23日 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 114/03/12 22.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 9945 | 潤泰新 | 8 | 8 | 5 | 8 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 9945 | 潤泰新 | 15 | 0 | 3662260.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
