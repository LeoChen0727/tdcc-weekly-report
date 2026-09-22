# INDIVIDUAL STOCK CHATGPT PACKET - 2449 京元電子

## Metadata
- generated_at: 2026-09-20 22:16:15 Asia/Taipei
- stock_id: 2449
- stock_name: 京元電子
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2449_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2449_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2449_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2449_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2449_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2449_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2449_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2449.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2449.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2449.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2449.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2449_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2449_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2449_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
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
- date: 20260918
- open: 276.5
- high: 291.5
- low: 274
- close: 291.5
- volume: 61177949
- ma5: 267.3
- ema23_primary: 263.34
- distance_to_ema23_pct: 10.69
- ma20: 262.6
- ma60: 270.37
- ma120: 284.12
- return_5d: 10.84
- return_20d: 25.65
- volume_ratio: 2.65
- distance_to_ma20_pct_auxiliary: 11.01
- distance_to_high_60_pct: -20.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,231.5,243,231,239,13529160,250.34,-4.53,238.6,283.43,0.66
20260825,238,239.5,231,239.5,11213528,249.44,-3.98,238.78,281.95,0.57
20260826,236,246.5,234,244,11870523,248.98,-2,240.35,280.72,0.62
20260827,250,250.5,243,247.5,13085586,248.86,-0.55,242.55,279.73,0.73
20260828,251.5,272,249.5,270,56354325,250.62,7.73,244.88,278.86,2.75
20260831,264.5,264.5,250,257,37673436,251.15,2.33,246.05,277.77,1.81
20260901,260,281.5,259,279,53349538,253.47,10.07,247.72,277.27,2.43
20260902,274.5,283.5,270.5,270.5,34026931,254.89,6.12,248.9,276.97,1.5
20260903,278,278,260,261,25192365,255.4,2.19,249.5,276.47,1.09
20260904,265,267.5,259,262,15925999,255.95,2.36,250.5,276.3,0.69
20260907,268.5,278,266.5,273,26506217,257.37,6.07,251.72,276.32,1.17
20260908,277.5,277.5,267,268.5,16085950,258.3,3.95,252.85,276.09,0.71
20260909,271,276.5,269,270,12493027,259.27,4.14,253.4,275.91,0.56
20260910,268,274,267,271.5,13033964,260.29,4.31,254.3,275.8,0.61
20260911,266,266.5,260,263,17759730,260.52,0.95,255.1,275.51,0.83
20260914,257,265,253,261.5,11531077,260.6,0.35,255.75,274.73,0.54
20260915,260.5,261.5,256.5,257,7605273,260.3,-1.27,256.8,273.36,0.37
20260916,259.5,263,257,261.5,7774589,260.4,0.42,258.12,272.23,0.38
20260917,265.5,274,264.5,265,15860463,260.78,1.62,259.62,271.08,0.77
20260918,276.5,291.5,274,291.5,61177949,263.34,10.69,262.6,270.37,2.65
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 60.64
- over_600_ratio: 58.33
- over_800_ratio: 56.4
- over_1000_ratio: 54.88
- over_400_change_1w: -0.32
- over_800_change_1w: -0.23
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,68.32,1.73,63.32,1.49,61.9,1.77,2,True,True
20260709,67.02,-1.3,62.22,-1.1,60.47,-1.43,0,False,False
20260717,66.55,-0.47,61.78,-0.44,60.09,-0.38,0,False,False
20260724,64.21,-2.34,59.51,-2.27,57.8,-2.29,0,False,False
20260731,62.34,-1.87,57.46,-2.05,55.5,-2.3,0,False,False
20260807,61.74,-0.6,57.01,-0.45,55.67,0.17,1,False,True
20260814,61,-0.74,56.19,-0.82,54.83,-0.84,0,False,False
20260821,59.94,-1.06,55.35,-0.84,54.04,-0.79,0,False,False
20260828,60.19,0.25,55.89,0.54,54.7,0.66,1,True,True
20260904,60.77,0.58,56.48,0.59,54.97,0.27,2,True,True
20260911,60.96,0.19,56.63,0.15,54.89,-0.08,3,False,True
20260918,60.64,-0.32,56.4,-0.23,54.88,-0.01,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2449 | 京元電子 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | call_put_bullish | stale_signal | 1.事實發生日:115/09/17 2.被背書保證之: (1)公司名稱:AeternZ Semiconductor Testing Corporation (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):12,532,813 (4)原背書保證之餘額(仟元):0 (5)本次新增背書保證之金額(仟元):9,566,400 (6)迄事實發生日止背書保證餘額(仟元):9,566,400 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之原因: 子公司與客戶簽署有關產能建置與保留之合約，依客戶要求由本公司擔任連帶保證人 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):7,972 (2)累積盈虧金額(仟元):0 5.解除背書保證責任之: (1)條件: 合約屆期(或終止)止 (2)日期: 合約屆期(或終止)止 6.背書保證之總限額(仟元): 28,198,829 7.迄事實發生日為止，背書保證餘額(仟元): 9,566,400 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 15.27 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 15.28 10.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2449 | 京元電子 | 29 | 1 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2449 | 京元電子 | 313 | 12 | 69043930.0 | 294470.0 | 234.47 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
