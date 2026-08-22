# INDIVIDUAL STOCK CHATGPT PACKET - 3044 健鼎

## Metadata
- generated_at: 2026-08-22 22:27:18 Asia/Taipei
- stock_id: 3044
- stock_name: 健鼎
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3044_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3044_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3044_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3044_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3044_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3044_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3044_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3044.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3044.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3044.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3044.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3044_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3044_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3044_latest.md?ref=main

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
- open: 504
- high: 515
- low: 455
- close: 459
- volume: 9309480
- ma5: 479.3
- ema23_primary: 446.09
- distance_to_ema23_pct: 2.89
- ma20: 423.23
- ma60: 465.04
- ma120: 441.1
- return_5d: -5.94
- return_20d: 16.79
- volume_ratio: 2.12
- distance_to_ma20_pct_auxiliary: 8.45
- distance_to_high_60_pct: -23.24

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,400,400,385,390.5,1354486,443.3,-11.91,447.85,484.76,0.39
20260728,377,379,358.5,359.5,2532780,436.32,-17.61,440.85,483.27,0.75
20260729,360,361,327,339.5,5677503,428.25,-20.72,431.93,481.18,1.65
20260730,345,359,332,342,2826978,421.06,-18.78,423.73,478.8,0.85
20260731,374,374,362.5,369,3814394,416.72,-11.45,416.88,476.82,1.19
20260803,364,379.5,356,374,3557410,413.16,-9.48,409.57,474.72,1.08
20260804,375,397,371,392,3573260,411.4,-4.72,403.88,473.23,1.07
20260805,399,409.5,395,398.5,4190490,410.32,-2.88,400.02,471.72,1.25
20260806,395,405,383.5,397.5,2466063,409.26,-2.87,396.3,470.32,0.74
20260807,401.5,403,392.5,394,2043936,407.98,-3.43,393.57,468.07,0.64
20260810,396.5,410.5,396.5,401.5,2116540,407.44,-1.46,391.7,466.23,0.68
20260811,441.5,441.5,430,441.5,8896410,410.28,7.61,392.7,465.63,2.64
20260812,485.5,485.5,485.5,485.5,2995810,416.55,16.55,395.68,465.91,0.88
20260813,502,524,485.5,495,14144741,423.09,17,399.32,466.45,3.63
20260814,492,505,486,488,5439626,428.5,13.89,403.85,466.88,1.37
20260817,481,491,480,483,2654773,433.04,11.54,408.6,466.79,0.67
20260818,493,502,482,488.5,3068950,437.66,11.62,412.8,466.76,0.77
20260819,474.5,501,468,480.5,4782368,441.23,8.9,415.95,466.53,1.18
20260820,485,490,470,485.5,2505588,444.92,9.12,419.93,466.12,0.62
20260821,504,515,455,459,9309480,446.09,2.89,423.23,465.04,2.12
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 79.55
- over_600_ratio: 74.87
- over_800_ratio: 71.84
- over_1000_ratio: 69.45
- over_400_change_1w: -0.02
- over_800_change_1w: 0.11
- over_1000_change_1w: -0.42
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,80.63,-0.23,72.85,-0.51,70.56,0.03,2,False,True
20260612,80.53,-0.1,72.55,-0.3,70.63,0.07,3,False,True
20260618,81.21,0.68,73.27,0.72,71.53,0.9,4,False,True
20260626,80.79,-0.42,72.77,-0.5,70.7,-0.83,0,False,False
20260703,80.48,-0.31,72.46,-0.31,70.35,-0.35,0,False,False
20260709,80.01,-0.47,72.15,-0.31,69.73,-0.62,0,False,False
20260717,79.53,-0.48,71.94,-0.21,69.56,-0.17,0,False,False
20260724,79.43,-0.1,72.19,0.25,70.03,0.47,1,False,True
20260731,79.4,-0.03,72.37,0.18,70.16,0.13,2,False,True
20260807,79.2,-0.2,71.5,-0.87,69.34,-0.82,0,False,False
20260814,79.57,0.37,71.73,0.23,69.87,0.53,1,True,True
20260821,79.55,-0.02,71.84,0.11,69.45,-0.42,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3044 | 健鼎 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/07/09 2.接受資金貸與之: (1)公司名稱:Tripod Overseas Co.,Ltd. (2)與資金貸與他人公司之關係: Tripod Overseas Co., Ltd為J & J Holding Co., Ltd.直接持有百分之百之子公司。 (3)資金貸與之限額(仟元):130,850,979 (4)原資金貸與之餘額(仟元):17,055,038 (5)本次新增資金貸與之金額(仟元):2,659,475 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:否 (7)迄事實發生日止資金貸與餘額(仟元):19,714,513 (8)本次新增資金貸與之原因: 短期融通資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):4,076,800 (2)累積盈虧金額(仟元):45,186,870 5.計息方式: 不計息。 6.還款之: (1)條件: 借款到期之次日，全數清償本金及利息，亦得提前償還。 (2)日期: 116年07月08日 7.迄事實發生日為止，資金貸與餘額(仟元): 32,620,325 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 55.95 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 3044 | 健鼎 | revenue_breakout_low_response | 營收爆發低反應股 | 16 | 32 | B_可觀察 |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/07/09 2.接受資金貸與之: (1)公司名稱:Tripod Overseas Co.,Ltd. (2)與資金貸與他人公司之關係: Tripod Overseas Co., Ltd為J & J Holding Co., Ltd.直接持有百分之百之子公司。 (3)資金貸與之限額(仟元):130,850,979 (4)原資金貸與之餘額(仟元):17,055,038 (5)本次新增資金貸與之金額(仟元):2,659,475 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:否 (7)迄事實發生日止資金貸與餘額(仟元):19,714,513 (8)本次新增資金貸與之原因: 短期融通資金需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):4,076,800 (2)累積盈虧金額(仟元):45,186,870 5.計息方式: 不計息。 6.還款之: (1)條件: 借款到期之次日，全數清償本金及利息，亦得提前償還。 (2)日期: 116年07月08日 7.迄事實發生日為止，資金貸與餘額(仟元): 32,620,325 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 55.95 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3044 | 健鼎 | 4 | 4 | 4 | 5 | 14 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 3044 | 健鼎 | 84 | 2 | 15232960.0 | 14760.0 | 1032.04 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
