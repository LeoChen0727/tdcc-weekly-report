# INDIVIDUAL STOCK CHATGPT PACKET - 8112 至上

## Metadata
- generated_at: 2026-08-21 22:28:23 Asia/Taipei
- stock_id: 8112
- stock_name: 至上
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8112_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8112_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8112.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8112.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8112.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8112.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8112_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8112_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8112_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260821
- open: 93.5
- high: 94.5
- low: 92.7
- close: 93.5
- volume: 9150843
- ma5: 92.4
- ema23_primary: 90.55
- distance_to_ema23_pct: 3.25
- ma20: 88.65
- ma60: 90.19
- ma120: 86.35
- return_5d: -2.4
- return_20d: 5.89
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: 5.47
- distance_to_high_60_pct: -10.1

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,88,88,81.9,84.3,20410865,87.83,-4.02,87.51,88.79,1.15
20260728,81,81,78,78.2,14401656,87.03,-10.14,86.81,88.73,0.82
20260729,78.7,78.7,73.5,76.7,13783602,86.16,-10.98,86.03,88.64,0.8
20260730,76.2,78.9,73.6,75.6,10179462,85.28,-11.36,85.33,88.48,0.61
20260731,80.6,81.7,78.5,80.3,14689641,84.87,-5.38,84.89,88.38,0.88
20260803,79.1,83,77.2,81.4,16169102,84.58,-3.76,84.31,88.28,1.01
20260804,81.1,85.7,80.8,85.2,17224178,84.63,0.67,84.1,88.22,1.08
20260805,87.1,88.4,86.2,86.2,15378648,84.76,1.7,83.9,88.21,0.98
20260806,86.6,89.2,84.7,89,13976707,85.12,4.56,84.08,88.33,0.93
20260807,89.9,91.9,88.8,91.2,22269743,85.62,6.51,84.39,88.48,1.41
20260810,92.9,93,91.2,92.4,16947208,86.19,7.21,84.64,88.61,1.07
20260811,95,100.5,94.7,100,72928524,87.34,14.5,85.36,88.92,3.87
20260812,100,101.5,96.6,96.9,37212675,88.14,9.94,85.83,89.13,1.87
20260813,98.5,100.5,97.6,97.8,23415579,88.94,9.96,86.43,89.36,1.13
20260814,99.3,99.8,95.1,95.8,20432034,89.51,7.02,87.12,89.56,0.97
20260817,96.2,96.2,93,93.5,15462674,89.84,4.07,87.75,89.69,0.73
20260818,93.3,94.2,90.3,90.3,11463283,89.88,0.46,87.96,89.76,0.54
20260819,88.9,91.8,88.3,91,8972080,89.98,1.14,88.11,89.89,0.45
20260820,91.8,93.8,90.4,93.7,10851249,90.29,3.78,88.39,90.06,0.54
20260821,93.5,94.5,92.7,93.5,9150843,90.55,3.25,88.65,90.19,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 46.06
- over_600_ratio: 44.24
- over_800_ratio: 42.26
- over_1000_ratio: 41.61
- over_400_change_1w: 7.41
- over_800_change_1w: 6.78
- over_1000_change_1w: 7.11
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,38.68,-1.15,35.89,-1.38,34.06,-1.35,0,False,False
20260605,41.62,2.94,39.39,3.5,38.07,4.01,1,True,True
20260612,38.53,-3.09,35.48,-3.91,34.1,-3.97,0,False,False
20260618,39.1,0.57,36.15,0.67,34.97,0.87,1,True,True
20260626,38.56,-0.54,36.22,0.07,34.72,-0.25,2,False,True
20260703,36.1,-2.46,33.93,-2.29,32.09,-2.63,0,False,False
20260709,35.67,-0.43,32.37,-1.56,31.36,-0.73,0,False,False
20260717,35.05,-0.62,31.57,-0.8,31.04,-0.32,0,False,False
20260724,37.39,2.34,34.24,2.67,33.2,2.16,1,True,True
20260731,39.51,2.12,36.36,2.12,35.55,2.35,2,True,True
20260807,38.65,-0.86,35.48,-0.88,34.5,-1.05,0,False,False
20260814,46.06,7.41,42.26,6.78,41.61,7.11,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8112 | 至上 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:高拓國際貿易(上海)有限公司 (2)與提供背書保證公司之關係: 本公司間接持有之100%子公司 (3)背書保證之限額(仟元):26,944,481 (4)原背書保證之餘額(仟元):4,291,850 (5)本次新增背書保證之金額(仟元):666,260 (6)迄事實發生日止背書保證餘額(仟元):4,958,110 (7)被背書保證公司實際動支金額(仟元):2,480,392 (8)本次新增背書保證之原因: 本公司向銀行簽具背書保證票據以取得額度，原額度人民幣14,000萬到期續保， 以因應轉投資子公司營運週轉之需求。 3.被背書保證公司提供擔保品之: (1)內容: 無。 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):383,021 (2)累積盈虧金額(仟元):147,332 5.解除背書保證責任之: (1)條件: 背書保證到期即解除背書保證責任。 (2)日期: 一年到期。 6.背書保證之總限額(仟元): 56,134,335 7.迄事實發生日為止，背書保證餘額(仟元): 22,874,005 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 101.87 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 23.72 10.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 8112 | 至上 | revenue_breakout_low_response | 營收爆發低反應股 | 24 | 1 | A_優先追蹤 |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:高拓國際貿易(上海)有限公司 (2)與提供背書保證公司之關係: 本公司間接持有之100%子公司 (3)背書保證之限額(仟元):26,944,481 (4)原背書保證之餘額(仟元):4,291,850 (5)本次新增背書保證之金額(仟元):666,260 (6)迄事實發生日止背書保證餘額(仟元):4,958,110 (7)被背書保證公司實際動支金額(仟元):2,480,392 (8)本次新增背書保證之原因: 本公司向銀行簽具背書保證票據以取得額度，原額度人民幣14,000萬到期續保， 以因應轉投資子公司營運週轉之需求。 3.被背書保證公司提供擔保品之: (1)內容: 無。 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):383,021 (2)累積盈虧金額(仟元):147,332 5.解除背書保證責任之: (1)條件: 背書保證到期即解除背書保證責任。 (2)日期: 一年到期。 6.背書保證之總限額(仟元): 56,134,335 7.迄事實發生日為止，背書保證餘額(仟元): 22,874,005 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 101.87 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 23.72 10.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8112 | 至上 | 6 | 2 | 5 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 8112 | 至上 | 143 | 5 | 27741160.0 | 25450.0 | 1090.03 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
