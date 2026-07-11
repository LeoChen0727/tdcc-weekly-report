# INDIVIDUAL STOCK CHATGPT PACKET - 3290 東浦

## Metadata
- generated_at: 2026-07-11 22:27:07 Asia/Taipei
- stock_id: 3290
- stock_name: 東浦
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 166
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3290_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3290_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3290_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3290_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3290_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3290_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3290_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3290.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3290.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3290.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3290.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3290_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3290_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3290_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260709
- open: 69.5
- high: 70.6
- low: 67.8
- close: 68.4
- volume: 1362000
- ma5: 68.62
- ema23_primary: 64.7
- distance_to_ema23_pct: 5.72
- ma20: 67.36
- ma60: 54.77
- ma120: 50.3
- return_5d: -2.56
- return_20d: 18.13
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: 1.54
- distance_to_high_60_pct: -8.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,59.5,63.6,57.1,63.6,7049000,50.63,25.61,49.52,47.45,5.77
20260612,63.6,64.5,60,61.4,7024000,51.53,19.15,50.34,47.72,4.93
20260615,63.5,64.2,60.6,62.5,3495000,52.45,19.17,51.13,48,2.23
20260616,62.4,66.2,60.2,66,3891000,53.57,23.19,52.12,48.36,2.24
20260617,66,66.3,64.6,65.8,3038000,54.59,20.53,53.08,48.72,1.62
20260618,66.3,70.9,66.2,69.8,4257000,55.86,24.95,54.21,49.16,2.06
20260622,71.5,74.8,68,68.8,5360000,56.94,20.83,55.23,49.59,2.3
20260623,68.8,71,67.4,68.9,2596000,57.94,18.93,56.32,50.01,1.06
20260624,67.8,69,66,68.5,2734000,58.82,16.46,57.33,50.43,1.05
20260625,69.2,73.9,68.5,71.3,3057000,59.86,19.12,58.51,50.9,1.11
20260626,71.5,72.6,66.6,66.6,2722000,60.42,10.23,59.44,51.3,0.95
20260629,66.7,68.5,65.2,65.3,1595000,60.83,7.36,60.28,51.71,0.54
20260630,66.6,67.4,65.5,66.4,767000,61.29,8.34,61.16,52.09,0.26
20260701,68.4,70,66.9,69.1,1511000,61.94,11.56,62.19,52.54,0.49
20260702,69.1,70.9,68,70.2,1022000,62.63,12.09,63.28,52.96,0.33
20260703,71,71.9,70,70.4,1226000,63.28,11.26,64.29,53.37,0.39
20260706,71.9,73.8,69.6,70.4,1656000,63.87,10.22,65.3,53.78,0.51
20260707,68.5,71.2,66.5,66.5,1541000,64.09,3.76,66.17,54.12,0.47
20260708,67.1,68.9,65.3,67.4,1450000,64.37,4.72,66.84,54.47,0.47
20260709,69.5,70.6,67.8,68.4,1362000,64.7,5.72,67.36,54.77,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 58.51
- over_600_ratio: 54.67
- over_800_ratio: 49.03
- over_1000_ratio: 47.2
- over_400_change_1w: -0.05
- over_800_change_1w: 0.63
- over_1000_change_1w: -1.2
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.97,,47.23,,45.15,,0,False,False
20260508,55.75,-0.22,47.55,0.32,45.47,0.32,1,False,True
20260515,56.14,0.39,47.15,-0.4,45.07,-0.4,2,False,False
20260522,54.83,-1.31,47.03,-0.12,44.99,-0.08,0,False,False
20260529,55.48,0.65,47.08,0.05,45.05,0.06,1,True,True
20260605,57.75,2.27,49.58,2.5,48.6,3.55,2,True,True
20260612,58.94,1.19,48.96,-0.62,47.95,-0.65,3,False,False
20260618,57.21,-1.73,49,0.04,47.97,0.02,4,False,True
20260626,58.56,1.35,48.4,-0.6,48.4,0.43,5,False,True
20260703,58.51,-0.05,49.03,0.63,47.2,-1.2,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3290 | 東浦 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:  盈餘分配現金股利，每股配發1.5元，計新台幣135,322,551 4.除權（息）交易日:115/07/07 5.最後過戶日:115/07/08 6.停止過戶起始日期:115/07/09 7.停止過戶截止日期:115/07/13 8.除權（息）基準日:115/07/13 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/07/28 13.其他應敘明事項:   (1)除息基準日前，本公司若因增資、買回股份、辦理庫藏股、員工認股權      憑證或公司債之轉讓、轉換、註銷等事項，致影響流通在外股份數量，      致股東配息率因此發生變動時，由董事會授權董事長為該項必要之調整      並全權處理其相關事項。   (2)本次現金股利按分配比例計算至元為止(元以下不計)，配發不足1元之畸      零款合計數，計入本公司其他收入。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |
| 20260709 | 3290 | 東浦 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/06/18 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:  盈餘分配現金股利，每股配發1.5元，計新台幣135,322,551 4.除權（息）交易日:115/07/07 5.最後過戶日:115/07/08 6.停止過戶起始日期:115/07/09 7.停止過戶截止日期:115/07/13 8.除權（息）基準日:115/07/13 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/07/28 13.其他應敘明事項:   (1)除息基準日前，本公司若因增資、買回股份、辦理庫藏股、員工認股權      憑證或公司債之轉讓、轉換、註銷等事項，致影響流通在外股份數量，      致股東配息率因此發生變動時，由董事會授權董事長為該項必要之調整      並全權處理其相關事項。   (2)本次現金股利按分配比例計算至元為止(元以下不計)，配發不足1元之畸      零款合計數，計入本公司其他收入。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3290 | 東浦 | 7 | 7 | 5 | 8 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
