# INDIVIDUAL STOCK CHATGPT PACKET - 8043 蜜望實

## Metadata
- generated_at: 2026-09-26 15:53:38 Asia/Taipei
- stock_id: 8043
- stock_name: 蜜望實
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 262
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8043_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8043_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8043_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8043_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8043.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8043.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8043.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8043.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8043_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8043_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8043_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- confidence_level: high
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
- decision_score_high
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
- date: 20260924
- open: 131.5
- high: 135.5
- low: 130.5
- close: 133
- volume: 1149000
- ma5: 132.2
- ema23_primary: 135.97
- distance_to_ema23_pct: -2.19
- ma20: 137.05
- ma60: 143.9
- ma120: 137.45
- return_5d: 2.31
- return_20d: -6.34
- volume_ratio: 0.39
- distance_to_ma20_pct_auxiliary: -2.96
- distance_to_high_60_pct: -39.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,149,156,145,148,16493000,141.89,4.3,139.97,162.17,2.75
20260831,144.5,150.5,138,142.5,4634000,141.95,0.39,140.15,162.12,0.77
20260901,142,151.5,142,147,4770000,142.37,3.25,140.62,161.92,0.82
20260902,142.5,144.5,142,142,1329000,142.34,-0.24,140.95,161.37,0.24
20260903,143,145,135,135.5,2194000,141.77,-4.42,140.97,160.42,0.4
20260904,140.5,146,140.5,142,5760000,141.79,0.15,141.78,159.47,1.02
20260907,146,149.5,142.5,144,4931000,141.97,1.43,142.25,158.68,0.86
20260908,142,142.5,138,138,1563000,141.64,-2.57,141.78,157.9,0.3
20260909,136.5,146,136.5,140,2849000,141.5,-1.06,141.4,156.86,0.66
20260910,139.5,144,134,141.5,3141000,141.5,-0,140.78,155.7,0.82
20260911,137,141,135.5,136,1932000,141.04,-3.58,140.28,154.3,0.52
20260914,133.5,135.5,131.5,133,1014000,140.37,-5.25,139.65,152.74,0.28
20260915,134,137,128.5,128.5,1457000,139.38,-7.81,139.15,151.33,0.4
20260916,130,132.5,129,132,870000,138.77,-4.88,138.6,150.17,0.26
20260917,133.5,136.5,130,130,1095000,138.04,-5.82,138.12,149,0.33
20260918,133.5,134,130.5,133,796000,137.62,-3.36,137.82,147.9,0.25
20260921,133.5,137.5,132.5,132.5,1272000,137.19,-3.42,137.7,147.03,0.4
20260922,136,136.5,131,131,998000,136.68,-4.15,137.62,146.28,0.31
20260923,132.5,136,131.5,131.5,1092000,136.24,-3.48,137.5,145.23,0.35
20260924,131.5,135.5,130.5,133,1149000,135.97,-2.19,137.05,143.9,0.39
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 40.06
- over_600_ratio: 38.3
- over_800_ratio: 37.54
- over_1000_ratio: 37.54
- over_400_change_1w: 0.03
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,43.41,-4.14,41.34,-2.92,41.34,-1.86,0,False,False
20260717,41.01,-2.4,39.23,-2.11,38.15,-3.19,0,False,False
20260724,41.45,0.44,37.54,-1.69,37.54,-0.61,1,False,False
20260731,41.47,0.02,39.31,1.77,39.31,1.77,2,True,True
20260807,41.01,-0.46,37.53,-1.78,37.53,-1.78,0,False,False
20260814,41.76,0.75,38.73,1.2,37.53,0,1,False,True
20260821,39.68,-2.08,37.53,-1.2,37.53,0,0,False,False
20260828,39.99,0.31,37.54,0.01,37.54,0.01,1,False,True
20260904,40.1,0.11,37.54,0,37.54,0,2,False,False
20260911,40.37,0.27,37.54,0,37.54,0,3,False,False
20260918,40.03,-0.34,37.54,0,37.54,0,0,False,False
20260924,40.06,0.03,37.54,0,37.54,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 8043 | 蜜望實 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理公告。 3.財務業務資訊: (1)單月                          最近一月單月       去年同月      與去年同期增減% 期間                          (115/05)      (114/05) -------------------------------------------------------------------------- 營業收入(百萬元)                 616          386               59.59% 稅前淨利(百萬元)                  -1          -23               95.65% 歸屬母公司業主淨利(百萬元)        -1          -15               93.33% 每股盈餘(元)                   -0.01        -0.19               94.74%  (2)單季                          最近一季單季        去年同期      與去年同期增減% 期間                        (115第1季)      (114第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                1,903         1,053             80.72% 稅前淨利(百萬元)                  134           -17            888.24% 歸屬母公司業主淨利(百萬元)        108           -25            532.00% 每股盈餘(元)                     1.35         -0.31            535.48% (3)最近四季累計 期間                       (114年第2季至115年第1季) -------------------------------------------------------------------------- 營業收入(百萬元)                6,276 稅前淨利(百萬元)                  293 歸屬母公司業主淨利(百萬元)        266 每股盈餘(元)                     3.33 -------------------------------------------------------------------------- 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:有 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年05月及去年同期比較數之財務資料係本公司 依IFRS會計準則編製之合併自結數，未經會計師查核(核閱)， 僅供投資人參考。 (2)最近一季115年第1季及去年同期比較數係指單季數字， 係本公司依IFRS下編製之合併數，業係經會計師核閱，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季由本公司依IFRS編製之 合併數業經會計師查核(核閱)，僅供投資人參考#欄位說明；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 8043 | 蜜望實 | 2 | 2 | 3 | 6 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
