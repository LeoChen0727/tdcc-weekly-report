# INDIVIDUAL STOCK CHATGPT PACKET - 5386 青雲

## Metadata
- generated_at: 2026-08-22 22:28:09 Asia/Taipei
- stock_id: 5386
- stock_name: 青雲
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5386_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5386_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5386_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5386_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5386.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5386.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5386.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5386.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5386_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5386_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5386_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- open: 233
- high: 243.5
- low: 233
- close: 236
- volume: 1374000
- ma5: 232.8
- ema23_primary: 269.34
- distance_to_ema23_pct: -12.38
- ma20: 248.05
- ma60: 382.85
- ma120: 374.94
- return_5d: -9.4
- return_20d: -7.27
- volume_ratio: 1.26
- distance_to_ma20_pct_auxiliary: -4.86
- distance_to_high_60_pct: -62.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,256.5,256.5,242,248,596000,357.39,-30.61,361.45,450.48,0.4
20260728,237,238.5,223.5,223.5,977000,346.23,-35.45,346.43,447.89,0.67
20260729,227,227.5,201.5,214,1328000,335.21,-36.16,333.52,444.82,0.88
20260730,206,225.5,201.5,207,1204000,324.52,-36.21,322.62,440.98,0.8
20260731,224.5,227.5,219,227.5,956000,316.44,-28.11,314.88,436.86,0.62
20260803,225.5,244,224,240,1060000,310.07,-22.6,305.85,432.16,0.73
20260804,239.5,256.5,234.5,248.5,1103000,304.94,-18.51,296.12,428.47,0.8
20260805,259,265,254,257.5,1009000,300.99,-14.45,287.48,425.43,0.74
20260806,252,274.5,252,271,1049000,298.49,-9.21,280.4,422.48,0.78
20260807,271,273.5,265,271,866000,296.2,-8.51,275.38,420.08,0.7
20260810,280,298,276,298,1363000,296.35,0.56,272.73,417.88,1.14
20260811,273.5,284.5,273,274.5,1859000,294.53,-6.8,269.1,415.53,1.53
20260812,276,282,276,278,762000,293.15,-5.17,264.32,412.75,0.64
20260813,285,285,278,278,797000,291.89,-4.76,259.07,410.38,0.68
20260814,278.5,280,260.5,260.5,1390000,289.27,-9.95,253.2,407.57,1.2
20260817,260.5,261,236.5,238.5,1491000,285.04,-16.33,253.38,403.74,1.31
20260818,238.5,246,227.5,228.5,1093000,280.33,-18.49,251.88,399.27,0.96
20260819,224,239,223,230.5,833000,276.18,-16.54,250.12,394.01,0.76
20260820,236.5,238,226.5,230.5,627000,272.37,-15.37,248.97,388.7,0.58
20260821,233,243.5,233,236,1374000,269.34,-12.38,248.05,382.85,1.26
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 35.75
- over_600_ratio: 34.03
- over_800_ratio: 34.03
- over_1000_ratio: 32.37
- over_400_change_1w: -0.03
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,35.52,-2.23,30.78,0,28.28,0,0,False,False
20260612,35.64,0.12,30.78,0,28.28,0,1,False,False
20260618,35.67,0.03,30.78,0,28.28,0,2,False,False
20260626,35.61,-0.06,30.78,0,28.28,0,0,False,False
20260703,36.66,1.05,30.78,0,28.28,0,1,False,False
20260709,36.98,0.32,30.78,0,28.28,0,2,False,False
20260717,37.53,0.55,30.78,0,28.28,0,3,False,False
20260724,34.31,-3.22,30.78,0,28.28,0,0,False,False
20260731,34.31,0,30.78,0,28.28,0,0,False,False
20260807,34.31,0,30.78,0,28.28,0,0,False,False
20260814,35.78,1.47,34.03,3.25,32.37,4.09,1,True,True
20260821,35.75,-0.03,34.03,0,32.37,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5386 | 青雲 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | stale_signal | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):15,146,991 5.1月1日累計至本期止營業毛利(毛損) (仟元):3,616,992 6.1月1日累計至本期止營業利益(損失) (仟元):3,012,377 7.1月1日累計至本期止稅前淨利(淨損) (仟元):2,907,001 8.1月1日累計至本期止本期淨利(淨損) (仟元):2,323,206 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):2,323,206 10.1月1日累計至本期止基本每股盈餘(損失) (元):42.93 11.期末總資產(仟元):9,163,568 12.期末總負債(仟元):5,964,979 13.期末歸屬於母公司業主之權益(仟元):3,198,589 14.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 5386 | 青雲 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):15,146,991 5.1月1日累計至本期止營業毛利(毛損) (仟元):3,616,992 6.1月1日累計至本期止營業利益(損失) (仟元):3,012,377 7.1月1日累計至本期止稅前淨利(淨損) (仟元):2,907,001 8.1月1日累計至本期止本期淨利(淨損) (仟元):2,323,206 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):2,323,206 10.1月1日累計至本期止基本每股盈餘(損失) (元):42.93 11.期末總資產(仟元):9,163,568 12.期末總負債(仟元):5,964,979 13.期末歸屬於母公司業主之權益(仟元):3,198,589 14.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 5386 | 青雲 | revenue_breakout_low_response | 營收爆發低反應股 | 22 | 6 | A_優先追蹤 |  |  |  | stale_signal | 1.提報董事會或經董事會決議日期:115/08/10 2.審計委員會通過日期:115/08/10 3.財務報告或年度自結財務資訊報導期間 起訖日期(XXX/XX/XX~XXX/XX/XX):115/01/01~115/06/30 4.1月1日累計至本期止營業收入(仟元):15,146,991 5.1月1日累計至本期止營業毛利(毛損) (仟元):3,616,992 6.1月1日累計至本期止營業利益(損失) (仟元):3,012,377 7.1月1日累計至本期止稅前淨利(淨損) (仟元):2,907,001 8.1月1日累計至本期止本期淨利(淨損) (仟元):2,323,206 9.1月1日累計至本期止歸屬於母公司業主淨利(損) (仟元):2,323,206 10.1月1日累計至本期止基本每股盈餘(損失) (元):42.93 11.期末總資產(仟元):9,163,568 12.期末總負債(仟元):5,964,979 13.期末歸屬於母公司業主之權益(仟元):3,198,589 14.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 5386 | 青雲 | 1 | 1 | 3 | 7 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
