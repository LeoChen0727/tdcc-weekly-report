# INDIVIDUAL STOCK CHATGPT PACKET - 8050 廣積

## Metadata
- generated_at: 2026-07-25 22:27:53 Asia/Taipei
- stock_id: 8050
- stock_name: 廣積
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8050_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8050_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8050_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8050_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8050_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8050_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8050_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8050.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8050.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8050.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8050.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8050_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8050_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8050_latest.md?ref=main

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
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260717
- open: 60
- high: 60.6
- low: 57
- close: 57.2
- volume: 2170000
- ma5: 60.06
- ema23_primary: 57.04
- distance_to_ema23_pct: 0.28
- ma20: 56.38
- ma60: 52.83
- ma120: 47.33
- return_5d: -1.72
- return_20d: 4.19
- volume_ratio: 1.5
- distance_to_ma20_pct_auxiliary: 1.46
- distance_to_high_60_pct: -13.46

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,55.1,56,55,55.7,684000,55.02,1.24,57.2,47.89,1.05
20260622,55.9,57,55.2,56.2,932000,55.12,1.96,57.32,48.15,1.34
20260623,56.9,57,55,55.4,536000,55.14,0.47,57.35,48.4,0.75
20260624,55.4,55.5,54.7,55.1,558000,55.14,-0.07,57.1,48.64,0.75
20260625,55.3,55.8,54.1,54.1,634000,55.05,-1.73,56.91,48.87,0.82
20260626,54.4,54.4,51.9,52,1004000,54.8,-5.11,56.6,49.07,1.23
20260629,51.5,52.8,51.4,51.5,561000,54.52,-5.54,56.23,49.27,0.66
20260630,51.9,52.5,51.3,52.3,565000,54.34,-3.75,55.91,49.47,0.65
20260701,52.7,53.3,52.1,52.2,442000,54.16,-3.62,55.52,49.66,0.5
20260702,51.9,54.3,51.8,54.2,537000,54.16,0.07,55.27,49.9,0.59
20260703,54.2,56.6,54,55.9,709000,54.31,2.93,55.2,50.16,0.75
20260706,56.7,57.5,56.3,57,897000,54.53,4.53,55.2,50.42,0.91
20260707,57.4,59.2,56.9,57.6,1751000,54.79,5.13,55.41,50.7,1.73
20260708,58.3,59.9,57.8,59.8,2698000,55.21,8.32,55.47,51.01,2.53
20260709,59.6,59.9,58.1,58.2,1244000,55.45,4.95,55.54,51.31,1.28
20260713,63,63,60.4,60.9,4156000,55.91,8.93,55.66,51.64,3.7
20260714,65,65,57.5,60,3543000,56.25,6.67,55.77,51.96,2.91
20260715,62,63.6,60.5,61.1,3000000,56.65,7.85,55.97,52.27,2.28
20260716,61.3,62.5,60,61.1,2296000,57.02,7.15,56.26,52.59,1.65
20260717,60,60.6,57,57.2,2170000,57.04,0.28,56.38,52.83,1.5
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 42.54
- over_600_ratio: 40.59
- over_800_ratio: 39.23
- over_1000_ratio: 36.53
- over_400_change_1w: -0.38
- over_800_change_1w: 0.34
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,43.63,,39.79,,37.99,,0,False,False
20260508,43.24,-0.39,39.32,-0.47,37.45,-0.54,0,False,False
20260515,43.55,0.31,39.29,-0.03,37.44,-0.01,1,False,False
20260522,43.37,-0.18,39.69,0.4,37.44,0,2,False,True
20260529,42.37,-1,38.27,-1.42,36.02,-1.42,0,False,False
20260605,41.89,-0.48,37.87,-0.4,36.02,0,0,False,False
20260612,42.04,0.15,38.2,0.33,35.46,-0.56,1,False,True
20260618,42.13,0.09,37.79,-0.41,35.46,0,2,False,False
20260626,42.34,0.21,37.78,-0.01,35.45,-0.01,3,False,False
20260703,42.59,0.25,38.75,0.97,36.04,0.59,4,True,True
20260709,42.92,0.33,38.89,0.14,36.57,0.53,5,True,True
20260717,42.54,-0.38,39.23,0.34,36.53,-0.04,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8050 | 廣積 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額: (1)盈餘分配現金股利新台幣288,847,092元，每股配發1.42848716元。 (2)資本公積發放現金新台幣145,419,571元，每股發放0.71916940元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:115/07/03 10.債券停止轉換起始日期:115/07/07 11.債券停止轉換截止日期:115/08/01 12.普通股現金股利發放日期:115/08/14 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因本公司庫藏股轉讓予員工，致使流通在外股數發生變動， 依董事會之決議，授權董事長調整配息率；每壹股配發現金(股利) 2.14765656(即每壹股盈餘分配1.42848716元，每壹股資本公積發 放0.71916940元)。 (2)本公司國內第六次無擔保轉換公司債轉換價格從63.3元調整為 60.9元，並自115年8月1日開始適用。 (3)本次以超過票面金額發行股票所得溢額之資本公積發放現金 不須課稅。 (4)凡持有本公司股票而尚未辦理過戶之股東，務請股東於民國 115年07月27日(星期一)辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d |
| 20260717 | 8050 | 廣積 | revenue_breakout_low_response | 營收爆發低反應股 | 17.0 | 15.0 | B_可觀察 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額: (1)盈餘分配現金股利新台幣288,847,092元，每股配發1.42848716元。 (2)資本公積發放現金新台幣145,419,571元，每股發放0.71916940元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:115/07/03 10.債券停止轉換起始日期:115/07/07 11.債券停止轉換截止日期:115/08/01 12.普通股現金股利發放日期:115/08/14 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因本公司庫藏股轉讓予員工，致使流通在外股數發生變動， 依董事會之決議，授權董事長調整配息率；每壹股配發現金(股利) 2.14765656(即每壹股盈餘分配1.42848716元，每壹股資本公積發 放0.71916940元)。 (2)本公司國內第六次無擔保轉換公司債轉換價格從63.3元調整為 60.9元，並自115年8月1日開始適用。 (3)本次以超過票面金額發行股票所得溢額之資本公積發放現金 不須課稅。 (4)凡持有本公司股票而尚未辦理過戶之股東，務請股東於民國 115年07月27日(星期一)辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8050 | 廣積 | 4 | 3 | 4 | 7 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
