# INDIVIDUAL STOCK CHATGPT PACKET - 1714 和桐

## Metadata
- generated_at: 2026-08-22 15:59:34 Asia/Taipei
- stock_id: 1714
- stock_name: 和桐
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1714_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1714_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1714_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1714_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1714_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1714_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1714_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1714.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1714.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1714.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1714.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1714_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1714_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1714_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260821
- open: 17
- high: 17.35
- low: 16.85
- close: 17
- volume: 12832352
- ma5: 16.96
- ema23_primary: 16.21
- distance_to_ema23_pct: 4.85
- ma20: 15.56
- ma60: 15.91
- ma120: 12.79
- return_5d: 3.66
- return_20d: 14.09
- volume_ratio: 0.64
- distance_to_ma20_pct_auxiliary: 9.27
- distance_to_high_60_pct: -32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,14.8,14.95,14.05,14.45,16338477,16.28,-11.26,17.43,14,0.56
20260728,14.2,14.2,13.55,13.65,13842768,16.06,-15.03,17.17,14.07,0.47
20260729,13.85,13.85,12.8,13.2,17962178,15.83,-16.59,16.85,14.14,0.6
20260730,13,13.25,12.45,12.6,13790296,15.56,-19.01,16.51,14.19,0.46
20260731,13.85,13.85,12.75,13.05,14765765,15.35,-14.97,16.13,14.26,0.48
20260803,13.05,14.35,12.95,14.35,18803193,15.26,-5.99,15.71,14.34,0.61
20260804,14.35,14.55,13.65,14.55,21367010,15.21,-4.31,15.39,14.43,0.87
20260805,15.15,15.3,14.6,14.75,17469654,15.17,-2.75,15.19,14.51,0.81
20260806,15.95,16.2,15.9,16.2,19116072,15.25,6.21,15.11,14.61,0.95
20260807,17,17,15.5,15.75,47332567,15.29,2.98,15.04,14.71,2.22
20260810,16,17.25,15.95,16.65,35835088,15.41,8.06,15.04,14.82,1.69
20260811,16.45,17.2,16.25,16.65,23078549,15.51,7.34,15.02,14.94,1.15
20260812,16.65,17.5,16.65,17.4,24787527,15.67,11.05,15.05,15.06,1.23
20260813,17.4,17.55,16.55,16.7,28694877,15.75,6,15.07,15.18,1.38
20260814,16.7,17.1,16.25,16.4,17141341,15.81,3.74,15.13,15.29,0.83
20260817,16.75,17.5,16.5,17.15,24001086,15.92,7.73,15.24,15.42,1.16
20260818,17.2,17.3,16.55,16.9,13519524,16,5.61,15.32,15.54,0.66
20260819,16.65,16.95,16.55,16.75,7761869,16.06,4.27,15.38,15.66,0.39
20260820,16.9,17.2,16.85,17,10251277,16.14,5.31,15.45,15.78,0.52
20260821,17,17.35,16.85,17,12832352,16.21,4.85,15.56,15.91,0.64
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 53.83
- over_600_ratio: 51.6
- over_800_ratio: 50.13
- over_1000_ratio: 48.79
- over_400_change_1w: 0.76
- over_800_change_1w: 1.04
- over_1000_change_1w: 0.69
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,64.6,1.64,60.23,2.1,58.37,2.05,1,True,True
20260612,65.07,0.47,60.98,0.75,59.12,0.75,2,True,True
20260618,62.93,-2.14,59.13,-1.85,57.64,-1.48,0,False,False
20260626,61.98,-0.95,58.64,-0.49,56.99,-0.65,0,False,False
20260703,62.1,0.12,58.75,0.11,57.02,0.03,1,True,True
20260709,55.86,-6.24,52.11,-6.64,50.84,-6.18,0,False,False
20260717,54.66,-1.2,51.23,-0.88,49.78,-1.06,0,False,False
20260724,54.8,0.14,51.39,0.16,50.22,0.44,1,True,True
20260731,55.33,0.53,51.42,0.03,50.45,0.23,2,True,True
20260807,55.09,-0.24,51.52,0.1,50.53,0.08,3,False,True
20260814,53.07,-2.02,49.09,-2.43,48.1,-2.43,0,False,False
20260821,53.83,0.76,50.13,1.04,48.79,0.69,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1714 | 和桐 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_strong_inflow | stale_signal | 1.事實發生日:115/07/07 2.公司名稱:和桐化學股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不通用 5.發生緣由:更正115年3月~5月資金貸與資訊揭露明細表 6.更正資訊項目/報表名稱:115年3月~5月資金貸與資訊揭露明細表 7.更正前金額/內容/頁次: (1)115年3月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:0仟元 (2)115年4月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:0仟元 (3)115年5月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:0仟元 8.更正後金額/內容/頁次: (1)115年3月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:150,000仟元 (2)115年4月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:150,000仟元 (3)115年5月 編號0 資金貸出之公司:和桐化學股份有限公司 貸與對象:中華全球石油股份有限公司 期末餘額:150,000仟元 9.因應措施:更正後重新上傳至公開資訊觀測站。 10.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1714 | 和桐 | 6 | 6 | 5 | 9 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1714 | 和桐 | 14 | 0 | 5474460.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
