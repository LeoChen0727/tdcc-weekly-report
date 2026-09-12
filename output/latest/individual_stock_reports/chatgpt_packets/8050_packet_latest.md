# INDIVIDUAL STOCK CHATGPT PACKET - 8050 廣積

## Metadata
- generated_at: 2026-09-12 22:17:57 Asia/Taipei
- stock_id: 8050
- stock_name: 廣積
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260911
- open: 55.8
- high: 57.1
- low: 55.7
- close: 56.1
- volume: 1373000
- ma5: 55.78
- ema23_primary: 56.88
- distance_to_ema23_pct: -1.38
- ma20: 56.47
- ma60: 57.77
- ma120: 52.71
- return_5d: -0.53
- return_20d: -3.28
- volume_ratio: 1.38
- distance_to_ma20_pct_auxiliary: -0.65
- distance_to_high_60_pct: -19.16

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,58.5,59,57,57.3,2082000,59.9,-4.34,60.55,58.04,0.35
20260818,57.3,57.3,55.9,56.4,2018000,59.61,-5.38,60.34,58.08,0.34
20260819,56,56.9,55.7,56.7,1233000,59.37,-4.49,60.12,58.12,0.21
20260820,57,57.6,56.4,57.1,896000,59.18,-3.51,59.83,58.07,0.16
20260821,57.1,57.6,56.5,56.9,735000,58.99,-3.54,59.69,58.05,0.14
20260824,57,57.9,56.5,57.5,942000,58.86,-2.32,59.5,58.04,0.18
20260825,57.9,58,56.8,57.3,741000,58.73,-2.44,59.44,58.01,0.15
20260826,58.1,58.1,57.2,57.9,751000,58.66,-1.3,59.3,58,0.16
20260827,58,58.4,57.3,57.3,886000,58.55,-2.14,59.42,57.95,0.19
20260828,57.6,57.7,56.4,56.4,1134000,58.37,-3.38,59.51,57.9,0.27
20260831,56.5,56.9,56,56.1,795000,58.18,-3.58,59.41,57.89,0.19
20260901,56.3,56.9,56.1,56.5,675000,58.04,-2.66,59.29,57.88,0.17
20260902,56.5,56.7,55.9,56.4,550000,57.91,-2.6,58.87,57.93,0.15
20260903,56.8,56.8,54.2,54.2,1877000,57.6,-5.9,58.42,57.85,0.55
20260904,54.7,56.6,54.7,56.4,1062000,57.5,-1.91,57.79,57.85,0.4
20260907,57,57,55.7,56.6,490000,57.42,-1.43,57.2,57.81,0.26
20260908,56.7,56.7,55.1,55.3,621000,57.25,-3.4,56.88,57.77,0.41
20260909,55.1,56.1,54.9,55.8,418000,57.12,-2.32,56.73,57.75,0.35
20260910,55.7,55.9,55,55.1,640000,56.96,-3.26,56.56,57.75,0.6
20260911,55.8,57.1,55.7,56.1,1373000,56.88,-1.38,56.47,57.77,1.38
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 42.75
- over_600_ratio: 40.25
- over_800_ratio: 38.93
- over_1000_ratio: 36.26
- over_400_change_1w: -0.08
- over_800_change_1w: -0.01
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,42.34,0.21,37.78,-0.01,35.45,-0.01,3,False,False
20260703,42.59,0.25,38.75,0.97,36.04,0.59,4,True,True
20260709,42.92,0.33,38.89,0.14,36.57,0.53,5,True,True
20260717,42.54,-0.38,39.23,0.34,36.53,-0.04,6,False,True
20260724,44.05,1.51,40.52,1.29,37.75,1.22,7,True,True
20260731,43.07,-0.98,38.45,-2.07,36.19,-1.56,0,False,False
20260807,44.59,1.52,41.14,2.69,37.99,1.8,1,True,True
20260814,43.23,-1.36,39.44,-1.7,36.32,-1.67,0,False,False
20260821,42.94,-0.29,39.39,-0.05,36.32,0,1,False,False
20260828,42.57,-0.37,38.99,-0.4,36.32,0,0,False,False
20260904,42.83,0.26,38.94,-0.05,36.28,-0.04,1,False,False
20260911,42.75,-0.08,38.93,-0.01,36.26,-0.02,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8050 | 廣積 | pullback_rebound | 回檔後短線轉強 | 63.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額: (1)盈餘分配現金股利新台幣288,847,092元，每股配發1.42848716元。 (2)資本公積發放現金新台幣145,419,571元，每股發放0.71916940元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:115/07/03 10.債券停止轉換起始日期:115/07/07 11.債券停止轉換截止日期:115/08/01 12.普通股現金股利發放日期:115/08/14 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因本公司庫藏股轉讓予員工，致使流通在外股數發生變動， 依董事會之決議，授權董事長調整配息率；每壹股配發現金(股利) 2.14765656(即每壹股盈餘分配1.42848716元，每壹股資本公積發 放0.71916940元)。 (2)本公司國內第六次無擔保轉換公司債轉換價格從63.3元調整為 60.9元，並自115年8月1日開始適用。 (3)本次以超過票面金額發行股票所得溢額之資本公積發放現金 不須課稅。 (4)凡持有本公司股票而尚未辦理過戶之股東，務請股東於民國 115年07月27日(星期一)辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 8050 | 廣積 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額: (1)盈餘分配現金股利新台幣288,847,092元，每股配發1.42848716元。 (2)資本公積發放現金新台幣145,419,571元，每股發放0.71916940元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:115/07/03 10.債券停止轉換起始日期:115/07/07 11.債券停止轉換截止日期:115/08/01 12.普通股現金股利發放日期:115/08/14 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因本公司庫藏股轉讓予員工，致使流通在外股數發生變動， 依董事會之決議，授權董事長調整配息率；每壹股配發現金(股利) 2.14765656(即每壹股盈餘分配1.42848716元，每壹股資本公積發 放0.71916940元)。 (2)本公司國內第六次無擔保轉換公司債轉換價格從63.3元調整為 60.9元，並自115年8月1日開始適用。 (3)本次以超過票面金額發行股票所得溢額之資本公積發放現金 不須課稅。 (4)凡持有本公司股票而尚未辦理過戶之股東，務請股東於民國 115年07月27日(星期一)辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 8050 | 廣積 | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 50 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/08 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額: (1)盈餘分配現金股利新台幣288,847,092元，每股配發1.42848716元。 (2)資本公積發放現金新台幣145,419,571元，每股發放0.71916940元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:115/07/03 10.債券停止轉換起始日期:115/07/07 11.債券停止轉換截止日期:115/08/01 12.普通股現金股利發放日期:115/08/14 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項: (1)因本公司庫藏股轉讓予員工，致使流通在外股數發生變動， 依董事會之決議，授權董事長調整配息率；每壹股配發現金(股利) 2.14765656(即每壹股盈餘分配1.42848716元，每壹股資本公積發 放0.71916940元)。 (2)本公司國內第六次無擔保轉換公司債轉換價格從63.3元調整為 60.9元，並自115年8月1日開始適用。 (3)本次以超過票面金額發行股票所得溢額之資本公積發放現金 不須課稅。 (4)凡持有本公司股票而尚未辦理過戶之股東，務請股東於民國 115年07月27日(星期一)辦理過戶手續。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8050 | 廣積 | 1 | 1 | 1 | 1 | 5 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
