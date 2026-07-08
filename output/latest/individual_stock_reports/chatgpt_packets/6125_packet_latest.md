# INDIVIDUAL STOCK CHATGPT PACKET - 6125 廣運

## Metadata
- generated_at: 2026-07-08 22:27:55 Asia/Taipei
- stock_id: 6125
- stock_name: 廣運
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 165
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6125_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6125_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6125_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6125_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6125_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6125_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6125_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6125.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6125.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6125.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6125.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6125_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6125_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6125_latest.md?ref=main

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
- date: 20260708
- open: 57.9
- high: 58.1
- low: 56.2
- close: 57.7
- volume: 1040000
- ma5: 59.06
- ema23_primary: 60.12
- distance_to_ema23_pct: -4.03
- ma20: 59.84
- ma60: 60.02
- ma120: 61.74
- return_5d: -1.2
- return_20d: -7.53
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: -3.58
- distance_to_high_60_pct: -23.98

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,61.9,63.6,59.5,59.5,1702000,63.03,-5.6,63.23,59.01,1.97
20260611,60.3,60.7,58.4,59.9,1753000,62.77,-4.57,63.3,58.99,1.96
20260612,61.1,62.2,60.4,60.5,1687000,62.58,-3.33,63.38,58.93,1.96
20260615,61.7,62.2,61.1,61.4,1076000,62.48,-1.73,63.55,58.9,1.28
20260616,61.5,61.9,59.8,59.8,1075000,62.26,-3.95,63.71,58.89,1.33
20260617,59,61.2,59,60.7,1044000,62.13,-2.3,64.01,58.91,1.36
20260618,60.7,66.3,60.7,63.6,4990000,62.25,2.16,64.36,59,5.32
20260622,64,64.5,62.5,62.6,2449000,62.28,0.51,64.52,59.07,2.32
20260623,63.2,63.2,60.8,60.8,1957000,62.16,-2.18,64.29,59.11,1.7
20260624,60.6,61.3,59.6,60.3,1417000,62,-2.75,63.88,59.16,1.16
20260625,60.9,60.9,59.6,59.8,1133000,61.82,-3.27,63.59,59.21,0.89
20260626,59.9,59.9,57,57,1888000,61.42,-7.19,63.16,59.23,1.39
20260629,57,58.3,56.4,57.8,797000,61.12,-5.43,62.71,59.31,0.57
20260630,58,59.8,57.8,59.5,825000,60.98,-2.43,62.02,59.39,0.57
20260701,59.6,60.2,58.3,58.4,907000,60.77,-3.89,61.39,59.48,0.61
20260702,58.2,60.3,57.4,60,1072000,60.7,-1.16,60.92,59.62,0.7
20260703,60.3,60.5,59.4,59.7,1032000,60.62,-1.52,60.58,59.73,0.65
20260706,60,61.3,59.7,60.1,1181000,60.58,-0.79,60.34,59.87,0.72
20260707,60.8,60.9,57.5,57.8,1090000,60.34,-4.22,60.08,59.96,0.7
20260708,57.9,58.1,56.2,57.7,1040000,60.12,-4.03,59.84,60.02,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 36.53
- over_600_ratio: 34.01
- over_800_ratio: 33.26
- over_1000_ratio: 31.13
- over_400_change_1w: 0.34
- over_800_change_1w: -0.04
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,36.21,,31.66,,30.61,,0,False,False
20260508,36.32,0.11,31.8,0.14,31.14,0.53,1,False,True
20260515,36.68,0.36,31.82,0.02,30.77,-0.37,2,False,True
20260522,36.48,-0.2,32.07,0.25,30.29,-0.48,3,False,True
20260529,36.69,0.21,32.49,0.42,30.37,0.08,4,True,True
20260605,36.88,0.19,33.27,0.78,31.83,1.46,5,True,True
20260612,36.41,-0.47,33.08,-0.19,31.64,-0.19,0,False,False
20260618,36.36,-0.05,33.11,0.03,31.67,0.03,1,False,True
20260626,36.19,-0.17,33.3,0.19,31.17,-0.5,2,False,True
20260703,36.53,0.34,33.26,-0.04,31.13,-0.04,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6125 | 廣運 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/07 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:  現金配發資本公積金額為103,604,460元，每股配發現金股利0.4元。  現金配發未分配盈餘金額為25,901,115元，每股配發現金股利0.1元。 4.除權（息）交易日:115/08/06 5.最後過戶日:115/08/07 6.停止過戶起始日期:115/08/08 7.停止過戶截止日期:115/08/12 8.除權（息）基準日:115/08/12 9.債券最後申請轉換日期:115/07/16 10.債券停止轉換起始日期:115/07/20 11.債券停止轉換截止日期:115/08/12 12.普通股現金股利發放日期:115/08/31 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:  (1)每位股東配發之現金股利按分配比例計算至元為止，不足一元之畸零款合計數，     轉入公司其他收入。  (2)本次現金股利發放案，如因本公司流通在外股數發生變動，致使股東配息比率發     生變動須修正時，授權董事長調整之。  (3)本公司國內第五次無擔保轉換公司債之轉換價格之調整，授權董事長依本公司發     行及轉換辦法調整之，調整後轉換價格將另行公告。  (4)如股利發放當日因颱風、豪雨、地震或其他天然災害，致部分或全部地區依政府     公告停止上班，為確保作業順利進行，股利發放日將順延至次一正常上班日辦理。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260708 | 6125 | 廣運 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 18.0 | B_可觀察 |  |  |  | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/07 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.發放普通股股利種類及金額:  現金配發資本公積金額為103,604,460元，每股配發現金股利0.4元。  現金配發未分配盈餘金額為25,901,115元，每股配發現金股利0.1元。 4.除權（息）交易日:115/08/06 5.最後過戶日:115/08/07 6.停止過戶起始日期:115/08/08 7.停止過戶截止日期:115/08/12 8.除權（息）基準日:115/08/12 9.債券最後申請轉換日期:115/07/16 10.債券停止轉換起始日期:115/07/20 11.債券停止轉換截止日期:115/08/12 12.普通股現金股利發放日期:115/08/31 13.以外幣發放現金股利(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:  (1)每位股東配發之現金股利按分配比例計算至元為止，不足一元之畸零款合計數，     轉入公司其他收入。  (2)本次現金股利發放案，如因本公司流通在外股數發生變動，致使股東配息比率發     生變動須修正時，授權董事長調整之。  (3)本公司國內第五次無擔保轉換公司債之轉換價格之調整，授權董事長依本公司發     行及轉換辦法調整之，調整後轉換價格將另行公告。  (4)如股利發放當日因颱風、豪雨、地震或其他天然災害，致部分或全部地區依政府     公告停止上班，為確保作業順利進行，股利發放日將順延至次一正常上班日辦理。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6125 | 廣運 | 5 | 5 | 5 | 7 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
