# INDIVIDUAL STOCK CHATGPT PACKET - 3441 聯一光電

## Metadata
- generated_at: 2026-08-22 16:00:12 Asia/Taipei
- stock_id: 3441
- stock_name: 聯一光電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3441_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3441_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3441_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3441_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3441_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3441_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3441_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3441.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3441.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3441.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3441.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3441_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3441_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3441_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260821
- open: 102
- high: 107
- low: 95.5
- close: 107
- volume: 48653000
- ma5: 93.28
- ema23_primary: 84.91
- distance_to_ema23_pct: 26.01
- ma20: 85.72
- ma60: 75.57
- ma120: 55.82
- return_5d: 27.68
- return_20d: 66.41
- volume_ratio: 2.22
- distance_to_ma20_pct_auxiliary: 24.82
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,65,70.7,65,70.7,12333000,69.44,1.81,70.92,62.14,3.59
20260728,67.5,77.7,67,77.2,26591000,70.09,10.15,70.97,62.87,5.66
20260729,77.5,84.9,75,84.8,58554000,71.31,18.91,71.2,63.72,7.72
20260730,84,90.5,76.4,76.4,37237000,71.74,6.5,71.17,64.38,3.96
20260731,81.7,84,78.9,84,16122000,72.76,15.45,71.36,65.11,1.59
20260803,87,92.4,83.3,92.4,32991000,74.4,24.2,72.05,66,2.8
20260804,93.5,95.8,85.5,89.6,49089000,75.66,18.42,72.58,66.78,3.46
20260805,90.3,93.8,85,85.4,22356000,76.47,11.67,73.29,67.53,1.47
20260806,84.6,89.4,81.3,88.4,13687000,77.47,14.11,74.25,68.34,0.87
20260807,87,94.3,84.4,84.4,17339000,78.05,8.14,75.08,69.09,1.06
20260810,82.7,84,79,79.5,8144000,78.17,1.71,75.34,69.7,0.49
20260811,79.2,82,77.9,79.3,4922000,78.26,1.33,75.94,70.28,0.29
20260812,79.3,87.2,79.2,87.2,10760000,79.01,10.37,77.07,71.01,0.63
20260813,87.4,88.7,85,85,11425000,79.51,6.91,77.83,71.7,0.66
20260814,86,88.9,80,83.8,10023000,79.86,4.93,78.62,72.3,0.57
20260817,83,91,82.6,87.4,18810000,80.49,8.58,79.81,72.87,1.03
20260818,87.4,90.5,84.6,86.2,12749000,80.97,6.46,80.94,73.44,0.68
20260819,83.6,90.3,82.2,88.5,9559000,81.59,8.46,82.16,73.95,0.5
20260820,93.3,97.3,91.7,97.3,17226000,82.9,17.36,83.59,74.64,0.88
20260821,102,107,95.5,107,48653000,84.91,26.01,85.72,75.57,2.22
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 29.76
- over_600_ratio: 25.16
- over_800_ratio: 19.78
- over_1000_ratio: 17.66
- over_400_change_1w: 7.7
- over_800_change_1w: 3.16
- over_1000_change_1w: 3.16
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,25.55,-1.19,19.39,0,15.14,0,0,False,False
20260612,31.05,5.5,19.71,0.32,15.12,-0.02,1,False,True
20260618,30.94,-0.11,21.68,1.97,17.47,2.35,2,False,True
20260626,28.79,-2.15,21.22,-0.46,14.75,-2.72,0,False,False
20260703,28.08,-0.71,16.79,-4.43,14.67,-0.08,0,False,False
20260709,27.77,-0.31,16.74,-0.05,14.62,-0.05,0,False,False
20260717,24.46,-3.31,16.74,0,14.62,0,0,False,False
20260724,26.91,2.45,19.74,3,17.62,3,1,True,True
20260731,28.28,1.37,20.85,1.11,14.57,-3.05,2,False,True
20260807,23.76,-4.52,16.62,-4.23,14.5,-0.07,0,False,False
20260814,22.06,-1.7,16.62,0,14.5,0,0,False,False
20260821,29.76,7.7,19.78,3.16,17.66,3.16,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3441 | 聯一光電 | true_breakout | 嚴格突破 | 94.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.事實發生日:115/08/19 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: 單月(註1)                 115年7月       114年7月    與去年同期增減% ----------------------  ------------  -------------  ----------------- 營業收入(百萬元)            51.37          45.83       12.11 稅前淨利(百萬元)            23.29          24.05       -3.14 歸屬母公司淨利(百萬元)      18.22          19.62       -7.13 每股盈餘(  元  )             0.46           0.49       -6.12 ====================================================================== 最近一季單季(註2)        115年第2季     114年第2季   與去年同期增減% ----------------------  ------------  -------------  ----------------- 營業收入(百萬元)           141.91          92.95       52.66 稅前淨利(百萬元)            37.41         -26.24      242.60 由虧轉盈 歸屬母公司淨利(百萬元)      27.66         -24.09      214.83 由虧轉盈 每股盈餘(  元  )             0.69          -0.60      215.00 由虧轉盈 ====================================================================== 最近四季累計(註3)             114年第3季~115年第2季 -----------------------     -------------------------- 營業收入(百萬元)                      496.75 稅前淨利(百萬元)                      132.85 歸屬母公司淨利(百萬元)                 97.28 每股盈餘(  元  )                        2.43 ====================================================================== 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註1：以上115年7月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之合併數 ，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第2季係指單季數字，非為最近財務報告中之累計數字，且係本公司 採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註3：最近四季累計係本公司114年第3季至115年第2季採IFRS編製之合併數，業經會計師 查核(閱)，僅供投資人參考。 註4：公告上述EPS依目前流通在外股數400,399,200股計算。 註5：公告上述與去年同期增減%係依照仟元金額計算。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3441 | 聯一光電 | 6 | 2 | 5 | 9 | 13 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
