# INDIVIDUAL STOCK CHATGPT PACKET - 1447 力鵬

## Metadata
- generated_at: 2026-07-28 22:26:43 Asia/Taipei
- stock_id: 1447
- stock_name: 力鵬
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 34
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1447_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1447_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1447_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1447_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1447_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1447_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1447_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1447.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1447.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1447.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1447.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1447_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1447_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1447_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260717
- open: 8.15
- high: 8.3
- low: 8.15
- close: 8.16
- volume: 2301151
- ma5: 8.43
- ema23_primary: 7.83
- distance_to_ema23_pct: 4.27
- ma20: 7.8
- ma60: 6.38
- ma120: 5.88
- return_5d: -2.63
- return_20d: 33.77
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: 4.59
- distance_to_high_60_pct: -24.09

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,6.1,6.16,6.03,6.03,1595661,6.08,-0.75,6.2,5.53,0.53
20260622,6.07,6.08,5.97,6.02,1604966,6.07,-0.84,6.21,5.54,0.54
20260623,6.02,6.14,5.95,6.07,1767452,6.07,-0.02,6.22,5.56,0.6
20260624,6.07,6.24,5.96,6.19,1289358,6.08,1.79,6.25,5.58,0.45
20260625,6.18,6.2,6.07,6.11,992157,6.08,0.44,6.28,5.59,0.36
20260626,6.11,6.33,6.04,6.22,2473062,6.09,2.05,6.3,5.61,0.88
20260629,6.4,6.84,6.4,6.84,4881834,6.16,11.1,6.34,5.64,1.74
20260630,7.52,7.52,7.52,7.52,4325235,6.27,19.93,6.4,5.68,1.51
20260701,8.27,8.27,8.27,8.27,10173212,6.44,28.47,6.49,5.73,3.14
20260702,8.5,9.09,8.32,9.09,38683419,6.66,36.52,6.6,5.8,8.18
20260703,9.95,9.99,9.63,9.99,37908670,6.94,44.03,6.77,5.88,6.03
20260706,10.75,10.75,9.3,9.51,20850345,7.15,33,6.92,5.95,2.9
20260707,9.51,9.51,8.99,9,8330661,7.3,23.21,7.04,6.02,1.13
20260708,8.82,8.89,8.3,8.65,4838717,7.42,16.63,7.14,6.07,0.65
20260709,8.7,8.7,8.31,8.38,2675444,7.5,11.78,7.23,6.12,0.35
20260713,8.54,8.8,8.4,8.43,2883862,7.57,11.29,7.34,6.18,0.38
20260714,8.43,8.5,7.98,8.07,3094568,7.62,5.96,7.44,6.22,0.41
20260715,8.3,8.87,8.3,8.87,3141778,7.72,14.89,7.57,6.28,0.41
20260716,8.87,9.2,8.6,8.62,3419701,7.8,10.58,7.7,6.34,0.44
20260717,8.15,8.3,8.15,8.16,2301151,7.83,4.27,7.8,6.38,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 69.88
- over_600_ratio: 68.25
- over_800_ratio: 66.88
- over_1000_ratio: 65.81
- over_400_change_1w: 0
- over_800_change_1w: -0.02
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,69.98,-0.16,66.51,-0.13,65.23,-0.13,0,False,False
20260508,70.06,0.08,66.53,0.02,65.04,-0.19,1,False,True
20260515,70.31,0.25,66.84,0.31,65.45,0.41,2,True,True
20260522,71.23,0.92,67.98,1.14,66.69,1.24,3,True,True
20260529,71.5,0.27,68.12,0.14,66.83,0.14,4,True,True
20260605,71.29,-0.21,67.74,-0.38,66.46,-0.37,0,False,False
20260612,71.19,-0.1,67.65,-0.09,66.47,0.01,1,False,True
20260618,71.33,0.14,67.72,0.07,66.54,0.07,2,True,True
20260626,71.46,0.13,67.84,0.12,66.56,0.02,3,True,True
20260703,71.1,-0.36,67.87,0.03,66.71,0.15,4,False,True
20260709,69.88,-1.22,66.9,-0.97,65.82,-0.89,0,False,False
20260717,69.88,0,66.88,-0.02,65.81,-0.01,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1447 | 力鵬 | revenue_pullback | 營收成長股價回檔 | 83.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/03 2.被背書保證之: (1)公司名稱:伊德石化股份有限公司 (2)與提供背書保證公司之關係: 本公司之子公司 (3)背書保證之限額(仟元):1,521,322 (4)原背書保證之餘額(仟元):893,760 (5)本次新增背書保證之金額(仟元):478,800 (6)迄事實發生日止背書保證餘額(仟元):1,372,560 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之原因: 子公司因銀行融資需要，由母公司提供背書保證。 (1)公司名稱:伊頓石化國際股份有限公司 (2)與提供背書保證公司之關係: 本公司之孫公司 (3)背書保證之限額(仟元):1,521,322 (4)原背書保證之餘額(仟元):510,720 (5)本次新增背書保證之金額(仟元):478,800 (6)迄事實發生日止背書保證餘額(仟元):989,520 (7)被背書保證公司實際動支金額(仟元):170,453 (8)本次新增背書保證之原因: 孫公司因銀行融資需要，由母公司提供背書保證。 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):70,229 (2)累積盈虧金額(仟元):40,830 5.解除背書保證責任之: (1)條件: 額度到期且債務清償完結。 (2)日期: 額度到期且債務清償完結。 6.背書保證之總限額(仟元): 3,042,644 7.迄事實發生日為止，背書保證餘額(仟元): 1,532,160 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 20.14 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 38.58 10.其他應敘明事項: (1)新增背書保證實際金額為1,500萬美金， 係由伊德石化股份有限公司及伊頓石化國際 股份有限公司共用額度，實質為同一筆書保證。 (2)上述申報金額以新台幣對美元匯率31.92計算。 (3)伊德石化股份有限公司:最近期財務報表之資本70,200仟元， 最近期財務報表之累積盈虧金額24,009仟元。 (4)伊頓石化國際股份有限公司:最近期財務報表之資本29仟元， 最近期財務報表之累積盈虧金額16,821仟元。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 1447 | 力鵬 | 1 | 1 | 1 | 3 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
