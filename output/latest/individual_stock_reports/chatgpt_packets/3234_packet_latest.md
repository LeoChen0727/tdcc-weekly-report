# INDIVIDUAL STOCK CHATGPT PACKET - 3234 光環

## Metadata
- generated_at: 2026-09-06 22:16:55 Asia/Taipei
- stock_id: 3234
- stock_name: 光環
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3234_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3234_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3234_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3234_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3234.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3234.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3234.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3234.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3234_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3234_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3234_latest.md?ref=main

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
- action_summary_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「高位派發風險」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
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
- date: 20260904
- open: 203
- high: 209
- low: 190
- close: 206
- volume: 5383000
- ma5: 199.3
- ema23_primary: 164.92
- distance_to_ema23_pct: 24.91
- ma20: 164.12
- ma60: 132.4
- ma120: 118.57
- return_5d: 13.5
- return_20d: 91.63
- volume_ratio: 1.12
- distance_to_ma20_pct_auxiliary: 25.51
- distance_to_high_60_pct: -6.36

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,118,118,116,118,2420000,109.31,7.95,104.88,115.09,1.61
20260811,120,124.5,114,121.5,2521000,110.33,10.13,105.41,115.51,1.68
20260812,117,133.5,117,133,5601000,112.22,18.52,106.38,116.12,3.3
20260813,133.5,146,133.5,141,7968000,114.62,23.02,108.03,116.94,3.87
20260814,138,141,134.5,136.5,3410000,116.44,17.23,109.83,117.6,1.62
20260817,139.5,150,137.5,150,5893000,119.24,25.8,112.52,118.46,2.53
20260818,149,154,141,146,5490000,121.47,20.2,114.88,119.16,2.13
20260819,138.5,149.5,138,147.5,3352000,123.64,19.3,116.83,119.84,1.25
20260820,153,153,142,151,4023000,125.92,19.92,119,120.51,1.46
20260821,150,152.5,141.5,151,3609000,128.01,17.96,121.18,121.3,1.27
20260824,150.5,166,148,166,7477000,131.17,26.55,124.2,122.43,2.36
20260825,162,182.5,158,182.5,8851000,135.45,34.74,128.34,123.67,2.48
20260826,179.5,185.5,174,180.5,4177000,139.2,29.67,132.86,124.7,1.13
20260827,179,186,178.5,180,2947000,142.6,26.22,137.51,125.53,0.77
20260828,183,186,181,181.5,2192000,145.85,24.45,141.8,126.18,0.56
20260831,180,185,170,185,3259000,149.11,24.07,145.85,126.98,0.81
20260901,185,203,183.5,200,3479000,153.35,30.42,150.2,128.24,0.86
20260902,199,220,199,211,7818000,158.15,33.41,155,129.69,1.8
20260903,211,214,193.5,194.5,6156000,161.18,20.67,159.2,130.85,1.34
20260904,203,209,190,206,5383000,164.92,24.91,164.12,132.4,1.12
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 36.21
- over_600_ratio: 32.72
- over_800_ratio: 28.45
- over_1000_ratio: 27.69
- over_400_change_1w: -0.03
- over_800_change_1w: 1.07
- over_1000_change_1w: 1.83
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,33.89,-2.29,24.59,-2.98,23.01,-1.34,0,False,False
20260626,33.31,-0.58,25.09,0.5,24.33,1.32,1,False,True
20260703,32.99,-0.32,25.09,0,23.45,-0.88,2,False,False
20260709,33.03,0.04,25.12,0.03,23.61,0.16,3,True,True
20260717,31.36,-1.67,23.45,-1.67,22.69,-0.92,0,False,False
20260724,31.71,0.35,21.72,-1.73,20.96,-1.73,1,False,False
20260731,30.87,-0.84,21.82,0.1,21.06,0.1,2,False,True
20260807,31.11,0.24,21.49,-0.33,20.73,-0.33,3,False,False
20260814,32.99,1.88,23.41,1.92,21.89,1.16,4,True,True
20260821,33.94,0.95,25.66,2.25,23.27,1.38,5,True,True
20260828,36.24,2.3,27.38,1.72,25.86,2.59,6,True,True
20260904,36.21,-0.03,28.45,1.07,27.69,1.83,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3234 | 光環 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | stale_signal | 1.事實發生日:115/06/24 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                        最近一月單月       去年同月         與去年同期增減%                         (115年05月)      (114年05月) --------------------------------------------------------------------------- 營業收入(百萬元)              57             50                  14.00% 稅前淨利(百萬元)             -12            -24                  50.00% 歸屬母公司業主淨利(百萬元)   -11            -23                  52.17% 每股盈餘(元)               -0.10          -0.20                  50.00%  (2)單季                        最近一季單季       去年同期         與去年同期增減%                        (115年第1季)     (114年第1季) --------------------------------------------------------------------------- 營業收入(百萬元)             183            206                -11.17% 稅前淨利(百萬元)             -36              6               -700.00% 歸屬母公司業主淨利(百萬元)   -36              8               -550.00% 每股盈餘(元)               -0.32           0.07               -557.14%  (3)最近四季累計                         (114年第2季至115年第1季) --------------------------------------------------------------------------- 營業收入(百萬元)                 660 稅前淨利(百萬元)                -203 歸屬母公司業主淨利(百萬元)      -200 每股盈餘(元)                   -1.79  --------------------------------------------------------------------------- 公司每股面額:10元  註:以上115年05月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之合併數    ，未經會計師查核(閱)，僅供投資人參考。 註:最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係本公司    採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 註:最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經會計師    查核(閱)，僅供投資人參考。 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 3234 | 光環 | 1 | 1 | 2 | 5 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
