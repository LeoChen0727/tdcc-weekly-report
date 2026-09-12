# INDIVIDUAL STOCK CHATGPT PACKET - 2543 皇昌

## Metadata
- generated_at: 2026-09-12 15:42:52 Asia/Taipei
- stock_id: 2543
- stock_name: 皇昌
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2543_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2543_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2543_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2543_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2543.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2543.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2543.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2543.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2543_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2543_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2543_latest.md?ref=main

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
- date: 20260911
- open: 38.5
- high: 38.75
- low: 37.9
- close: 37.9
- volume: 1344710
- ma5: 38.82
- ema23_primary: 38.73
- distance_to_ema23_pct: -2.13
- ma20: 38.66
- ma60: 38.86
- ma120: 44.22
- return_5d: -1.43
- return_20d: -2.57
- volume_ratio: 1.85
- distance_to_ma20_pct_auxiliary: -1.98
- distance_to_high_60_pct: -18.67

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,38.7,38.85,38.4,38.75,649756,38.9,-0.38,38.42,41.14,0.51
20260818,38.75,38.8,38.2,38.25,532397,38.84,-1.53,38.34,41.02,0.43
20260819,38,38.65,37.8,38.1,998458,38.78,-1.76,38.29,40.95,0.81
20260820,38.6,39.45,38.45,38.95,1011631,38.8,0.4,38.28,40.92,0.81
20260821,38.9,38.95,38.5,38.95,430518,38.81,0.36,38.3,40.87,0.35
20260824,38.7,39.5,38.6,38.65,414975,38.8,-0.38,38.28,40.82,0.35
20260825,38.6,38.9,38.35,38.5,484823,38.77,-0.7,38.27,40.7,0.42
20260826,38.75,38.8,38.2,38.6,538623,38.76,-0.41,38.38,40.56,0.53
20260827,38.8,39.1,38.5,38.6,543420,38.74,-0.37,38.53,40.44,0.56
20260828,38.7,38.8,38.3,38.3,472138,38.71,-1.05,38.59,40.31,0.51
20260831,38.35,39.8,38.05,39.8,1341149,38.8,2.58,38.71,40.21,1.42
20260901,39.25,39.45,38.55,38.65,1280483,38.79,-0.35,38.81,40.03,1.32
20260902,38.55,38.8,38.15,38.3,557418,38.75,-1.15,38.85,39.88,0.59
20260903,38.45,38.95,38.25,38.35,671813,38.71,-0.94,38.89,39.7,0.7
20260904,38.4,38.7,38.3,38.45,430616,38.69,-0.62,38.85,39.53,0.51
20260907,38.9,38.9,38.25,38.65,661238,38.69,-0.1,38.84,39.39,0.8
20260908,38.65,39.2,38.35,39.05,879180,38.72,0.86,38.82,39.26,1.06
20260909,38.8,39.6,38.8,39.4,638076,38.77,1.61,38.74,39.14,0.85
20260910,39.25,39.5,38.45,39.1,619978,38.8,0.77,38.72,39.01,0.9
20260911,38.5,38.75,37.9,37.9,1344710,38.73,-2.13,38.66,38.86,1.85
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 71.39
- over_600_ratio: 69.53
- over_800_ratio: 68.17
- over_1000_ratio: 67.68
- over_400_change_1w: 0.09
- over_800_change_1w: 0.07
- over_1000_change_1w: 0.07
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,71.38,-0.46,67.87,-0.32,67.03,-0.67,0,False,False
20260703,71.16,-0.22,67.7,-0.17,66.86,-0.17,0,False,False
20260709,71.13,-0.03,67.67,-0.03,66.86,0,0,False,False
20260717,71.28,0.15,67.68,0.01,66.82,-0.04,1,False,True
20260724,71.85,0.57,68.4,0.72,67.39,0.57,2,True,True
20260731,71.87,0.02,68.37,-0.03,67.56,0.17,3,False,True
20260807,71.91,0.04,68.48,0.11,67.3,-0.26,4,False,True
20260814,71.9,-0.01,68.15,-0.33,67.34,0.04,5,False,True
20260821,71.5,-0.4,68.11,-0.04,67.29,-0.05,0,False,False
20260828,71.45,-0.05,68.17,0.06,67.34,0.05,1,False,True
20260904,71.3,-0.15,68.1,-0.07,67.61,0.27,2,False,True
20260911,71.39,0.09,68.17,0.07,67.68,0.07,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2543 | 皇昌 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):4,192,993,463 2.原預定買回之期間:115/05/19~115/07/18 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):35.00~70.00 5.本次實際買回期間:115/05/21~115/06/16 6.本次已買回股份數量(股):14,235,000 7.本次已買回股份總金額(元):661,434,108 8.本次平均每股買回價格(元):46.47 9.累積已持有自己公司股份數量(股):14,235,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.69 11.本次未執行完畢之原因: 維護股東權益並兼顧市場機制，視股價變化及成交量狀況分批買回， 故未能執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260911 | 2543 | 皇昌 | revenue_breakout_low_response | 營收爆發低反應股 | 14 | 23 | B_可觀察 |  |  | no_signal | stale_signal | 1.原預定買回股份總金額上限(元):4,192,993,463 2.原預定買回之期間:115/05/19~115/07/18 3.原預定買回之數量(股):20,000,000 4.原預定買回區間價格(元):35.00~70.00 5.本次實際買回期間:115/05/21~115/06/16 6.本次已買回股份數量(股):14,235,000 7.本次已買回股份總金額(元):661,434,108 8.本次平均每股買回價格(元):46.47 9.累積已持有自己公司股份數量(股):14,235,000 10.累積已持有自己公司股份數量占公司已發行股份總數之比率(%):2.69 11.本次未執行完畢之原因: 維護股東權益並兼顧市場機制，視股價變化及成交量狀況分批買回， 故未能執行完畢 12.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2543 | 皇昌 | 1 | 1 | 1 | 3 | 6 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 2543 | 皇昌 | 12 | 0 | 63220.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
