# INDIVIDUAL STOCK CHATGPT PACKET - 3708 上緯投控

## Metadata
- generated_at: 2026-09-20 22:17:02 Asia/Taipei
- stock_id: 3708
- stock_name: 上緯投控
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3708_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3708_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3708_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3708_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3708_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3708_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3708_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3708.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3708.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3708.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3708.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3708_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3708_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3708_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- open: 97
- high: 97.6
- low: 96.5
- close: 96.7
- volume: 1258423
- ma5: 95.8
- ema23_primary: 98.66
- distance_to_ema23_pct: -1.98
- ma20: 99.33
- ma60: 100.68
- ma120: 110.22
- return_5d: 1.04
- return_20d: -6.57
- volume_ratio: 2.55
- distance_to_ma20_pct_auxiliary: -2.65
- distance_to_high_60_pct: -19.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,104,104.5,103,103,373039,101.29,1.69,98.33,106.73,0.67
20260825,102,103,101,101.5,358331,101.3,0.19,98.84,106.35,0.67
20260826,101.5,103,101.5,102.5,322412,101.4,1.08,99.56,106.08,0.66
20260827,102,105,102,103,442043,101.54,1.44,100.33,105.8,0.9
20260828,103,103.5,100.5,101,510739,101.49,-0.49,100.78,105.45,1.03
20260831,101.5,103,100.5,102.5,387310,101.58,0.91,101.33,105.09,0.76
20260901,101,103,100.5,100.5,562417,101.49,-0.97,101.64,104.78,1.08
20260902,100,101.5,100,101,426830,101.45,-0.44,101.83,104.51,0.8
20260903,100.5,101,99.6,100,502519,101.33,-1.31,101.95,104.17,0.92
20260904,100,100.5,98.7,100.5,391115,101.26,-0.75,102.17,103.86,0.71
20260907,100.5,100.5,98.4,99.6,436707,101.12,-1.5,102.06,103.55,0.83
20260908,99.6,100,99.3,99.6,324742,100.99,-1.38,101.91,103.25,0.64
20260909,99.8,100,99.1,99.1,462085,100.83,-1.72,101.67,102.92,0.93
20260910,98.5,99.4,97.1,98.2,631744,100.62,-2.4,101.42,102.61,1.34
20260911,96.2,97.2,95.7,95.7,492780,100.21,-4.5,101.19,102.3,1.1
20260914,94.8,97.5,93.9,96.9,484774,99.93,-3.03,100.86,101.97,1.07
20260915,96.1,97.2,95.4,95.4,237684,99.55,-4.17,100.42,101.64,0.55
20260916,94.6,95.6,93.5,93.5,569232,99.05,-5.6,100.03,101.28,1.32
20260917,93.3,97.4,93.3,96.5,707669,98.84,-2.36,99.67,100.98,1.59
20260918,97,97.6,96.5,96.7,1258423,98.66,-1.98,99.33,100.68,2.55
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 49.44
- over_600_ratio: 44.89
- over_800_ratio: 38.96
- over_1000_ratio: 38.01
- over_400_change_1w: -0.93
- over_800_change_1w: -2.68
- over_1000_change_1w: -2.67
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,50.61,-1.76,42.12,-0.63,41.24,-0.47,0,False,False
20260709,51.02,0.41,41.33,-0.79,40.34,-0.9,1,False,False
20260717,49.77,-1.25,41.29,-0.04,40.3,-0.04,0,False,False
20260724,49.14,-0.63,41.29,0,40.3,0,0,False,False
20260731,49.35,0.21,41.5,0.21,40.51,0.21,1,True,True
20260807,49.49,0.14,41.64,0.14,40.65,0.14,2,True,True
20260814,49.59,0.1,42.3,0.66,41.32,0.67,3,True,True
20260821,49.84,0.25,42.64,0.34,40.72,-0.6,4,False,True
20260828,50,0.16,41.61,-1.03,40.64,-0.08,5,False,False
20260904,49.74,-0.26,41.6,-0.01,40.64,0,0,False,False
20260911,50.37,0.63,41.64,0.04,40.68,0.04,1,True,True
20260918,49.44,-0.93,38.96,-2.68,38.01,-2.67,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3708 | 上緯投控 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | first_seen | 1.事實發生日：民國115年06月11日 2.公司名稱：上緯國際控股股份有限公司(原名：上緯國際投資控股股份有限公司) 3.與公司關係(請輸入本公司或子公司)：本公司 4.相互持股比例：不適用 5.發生緣由： (1)公司名稱變更核准日期/事實發生日：民國115年06月11日 (2)公司名稱變更核准文號：經授商字第11530084540號函 (3)更名案股東會決議通過日期：民國115年05月28日 (4)變更前公司名稱：上緯國際投資控股股份有限公司 (5)變更後公司名稱：上緯國際控股股份有限公司 (6)變更前公司簡稱：上緯投控 (7)變更後公司簡稱：上緯控股 6.因應措施：無 7.其他應敘明事項：(1)本公司於115/6/11收到經濟部變更登記核准函。 (2)依據臺灣證券交易所股份有限公司營業細則第45條規定，於更 名後須連續公告三個月。 (3)本公司股票代號未變動，普通股仍為「3708」；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3708 | 上緯投控 | revenue_breakout_low_response | 營收爆發低反應股 | 17 | 22 | B_可觀察 |  |  | no_signal | first_seen | 1.事實發生日：民國115年06月11日 2.公司名稱：上緯國際控股股份有限公司(原名：上緯國際投資控股股份有限公司) 3.與公司關係(請輸入本公司或子公司)：本公司 4.相互持股比例：不適用 5.發生緣由： (1)公司名稱變更核准日期/事實發生日：民國115年06月11日 (2)公司名稱變更核准文號：經授商字第11530084540號函 (3)更名案股東會決議通過日期：民國115年05月28日 (4)變更前公司名稱：上緯國際投資控股股份有限公司 (5)變更後公司名稱：上緯國際控股股份有限公司 (6)變更前公司簡稱：上緯投控 (7)變更後公司簡稱：上緯控股 6.因應措施：無 7.其他應敘明事項：(1)本公司於115/6/11收到經濟部變更登記核准函。 (2)依據臺灣證券交易所股份有限公司營業細則第45條規定，於更 名後須連續公告三個月。 (3)本公司股票代號未變動，普通股仍為「3708」；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3708 | 上緯投控 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3708 | 上緯投控 | 14 | 0 | 34960.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
