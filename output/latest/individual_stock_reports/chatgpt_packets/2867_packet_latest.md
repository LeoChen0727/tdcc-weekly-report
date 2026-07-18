# INDIVIDUAL STOCK CHATGPT PACKET - 2867 三商壽

## Metadata
- generated_at: 2026-07-18 22:26:51 Asia/Taipei
- stock_id: 2867
- stock_name: 三商壽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 305
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2867_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2867_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2867_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2867_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2867_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2867_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2867_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2867.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2867.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2867.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2867.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2867_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2867_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2867_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- Only claim tdcc_history_ready when tdcc_rows >= 8 and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 8.9
- high: 9.13
- low: 8.88
- close: 8.98
- volume: 37939427
- ma5: 8.88
- ema23_primary: 8.61
- distance_to_ema23_pct: 4.27
- ma20: 8.66
- ma60: 8.12
- ma120: 7.99
- return_5d: 1.35
- return_20d: 4.18
- volume_ratio: 2.34
- distance_to_ma20_pct_auxiliary: 3.64
- distance_to_high_60_pct: -1.64

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,8.65,8.78,8.62,8.74,18362750,8.1,7.87,8,7.83,0.95
20260622,8.75,8.88,8.66,8.69,21713316,8.15,6.61,8.05,7.85,1.08
20260623,8.69,8.83,8.65,8.72,13143359,8.2,6.36,8.11,7.87,0.66
20260624,8.66,8.66,8.51,8.51,19439096,8.22,3.47,8.16,7.88,0.94
20260625,8.6,8.67,8.48,8.59,12569366,8.26,4.06,8.21,7.9,0.6
20260626,8.54,8.59,8.39,8.4,11469909,8.27,1.61,8.26,7.91,0.55
20260629,8.54,8.55,8.38,8.4,9651922,8.28,1.47,8.3,7.92,0.46
20260630,8.47,8.51,8.34,8.34,12407132,8.28,0.68,8.34,7.93,0.6
20260701,8.44,8.49,8.25,8.25,32158634,8.28,-0.37,8.36,7.94,1.52
20260702,8.36,8.52,8.31,8.5,11554198,8.3,2.42,8.38,7.96,0.59
20260703,8.5,8.73,8.5,8.56,11202448,8.32,2.88,8.41,7.97,0.59
20260706,8.56,8.75,8.56,8.74,12403540,8.36,4.6,8.44,7.99,0.66
20260707,8.76,8.78,8.7,8.73,12595581,8.39,4.09,8.48,8,0.67
20260708,8.76,8.9,8.72,8.86,21610573,8.43,5.15,8.51,8.02,1.22
20260709,8.95,8.98,8.76,8.86,13433974,8.46,4.7,8.54,8.04,0.77
20260713,8.86,8.9,8.77,8.83,9959503,8.49,3.97,8.57,8.05,0.57
20260714,8.83,8.85,8.65,8.83,14830041,8.52,3.62,8.6,8.07,0.88
20260715,8.83,8.95,8.82,8.85,10985213,8.55,3.53,8.63,8.08,0.67
20260716,8.9,8.97,8.82,8.91,16286194,8.58,3.86,8.65,8.1,1.07
20260717,8.9,9.13,8.88,8.98,37939427,8.61,4.27,8.66,8.12,2.34
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 85.8
- over_600_ratio: 84.17
- over_800_ratio: 83.27
- over_1000_ratio: 82.4
- over_400_change_1w: 0.17
- over_800_change_1w: 0.22
- over_1000_change_1w: 0.14
- tdcc_consecutive_up_weeks: 11
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,83.32,,80.35,,79.4,,0,False,False
20260508,83.47,0.15,80.54,0.19,79.56,0.16,1,True,True
20260515,83.64,0.17,80.78,0.24,79.82,0.26,2,True,True
20260522,83.79,0.15,80.91,0.13,79.99,0.17,3,True,True
20260529,83.79,0,80.94,0.03,80.05,0.06,4,False,True
20260605,84.37,0.58,81.53,0.59,80.66,0.61,5,True,True
20260612,84.83,0.46,82.09,0.56,81.22,0.56,6,True,True
20260618,85.01,0.18,82.28,0.19,81.42,0.2,7,True,True
20260626,85.18,0.17,82.56,0.28,81.7,0.28,8,True,True
20260703,85.35,0.17,82.69,0.13,81.85,0.15,9,True,True
20260709,85.63,0.28,83.05,0.36,82.26,0.41,10,True,True
20260717,85.8,0.17,83.27,0.22,82.4,0.14,11,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2867 | 三商壽 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬暨提名委員會 3.舊任者姓名: 杜德成(暨召集人) 楊弘毅 柳漢宗 4.舊任者簡歷: 杜德成/三商美邦人壽保險股份有限公司獨立董事 楊弘毅/三商美邦人壽保險股份有限公司獨立董事 柳漢宗/三商美邦人壽保險股份有限公司獨立董事 5.新任者姓名: 杜德成(暨召集人) 楊弘毅 柳漢宗 6.新任者簡歷: 杜德成/三商美邦人壽保險股份有限公司獨立董事 楊弘毅/三商美邦人壽保險股份有限公司獨立董事 柳漢宗/三商美邦人壽保險股份有限公司獨立董事 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，全面改選 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/29 ~ 115/06/14 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 2867 | 三商壽 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.發生變動日期:115/07/16 2.功能性委員會名稱:薪資報酬暨提名委員會 3.舊任者姓名: 杜德成(暨召集人) 楊弘毅 柳漢宗 4.舊任者簡歷: 杜德成/三商美邦人壽保險股份有限公司獨立董事 楊弘毅/三商美邦人壽保險股份有限公司獨立董事 柳漢宗/三商美邦人壽保險股份有限公司獨立董事 5.新任者姓名: 杜德成(暨召集人) 楊弘毅 柳漢宗 6.新任者簡歷: 杜德成/三商美邦人壽保險股份有限公司獨立董事 楊弘毅/三商美邦人壽保險股份有限公司獨立董事 柳漢宗/三商美邦人壽保險股份有限公司獨立董事 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿，全面改選 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/29 ~ 115/06/14 10.新任生效日期:115/07/16 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2867 | 三商壽 | 11 | 2 | 5 | 10 | 19 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 19 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2867 | 三商壽 | 2 | 0 | 2370.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
