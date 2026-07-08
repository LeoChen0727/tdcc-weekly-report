# INDIVIDUAL STOCK CHATGPT PACKET - 5468 凱鈺

## Metadata
- generated_at: 2026-07-08 22:27:48 Asia/Taipei
- stock_id: 5468
- stock_name: 凱鈺
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5468_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5468_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5468_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5468_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5468_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5468_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5468_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5468.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5468.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5468.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5468.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5468_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5468_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5468_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
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
- date: 20260708
- open: 31
- high: 33.6
- low: 29.5
- close: 30.9
- volume: 1039000
- ma5: 32.56
- ema23_primary: 28.36
- distance_to_ema23_pct: 8.95
- ma20: 29.17
- ma60: 21.65
- ma120: 19.87
- return_5d: -0.32
- return_20d: 79.65
- volume_ratio: 0.96
- distance_to_ma20_pct_auxiliary: 5.94
- distance_to_high_60_pct: -15.34

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,17.25,18.85,17,18,183000,17.76,1.37,17.65,18.01,4.49
20260611,19.8,19.8,19.8,19.8,466000,17.93,10.45,17.75,18.08,7.43
20260612,21.75,21.75,21.75,21.75,295000,18.25,19.21,17.95,18.16,3.98
20260615,23.9,23.9,23.9,23.9,1466000,18.72,27.69,18.27,18.24,10.13
20260616,26.25,26.25,25.5,26.25,4568000,19.34,35.7,18.73,18.35,12.52
20260617,27.05,27.85,26,27.3,3686000,20.01,36.45,19.25,18.48,6.73
20260618,27.9,30,27.9,30,1309000,20.84,43.95,19.86,18.68,2.14
20260622,33,33,32.6,33,1696000,21.85,51,20.62,18.93,2.44
20260623,36.3,36.3,36.15,36.3,2082000,23.06,57.43,21.54,19.21,2.61
20260624,33,33,32.7,32.7,715000,23.86,37.04,22.29,19.44,0.86
20260625,31.75,31.75,30,30,1199000,24.37,23.09,22.93,19.64,1.34
20260626,30,30,28.6,29.8,507000,24.82,20.04,23.55,19.83,0.55
20260629,30.5,31.4,30,30.15,364000,25.27,19.32,24.2,20.04,0.39
20260630,31.3,31.3,30.55,30.6,209000,25.71,19.01,24.82,20.24,0.22
20260701,31.3,31.3,30,31,334000,26.15,18.53,25.45,20.47,0.35
20260702,30.9,34.05,30.9,33.6,657000,26.77,25.49,26.23,20.73,0.66
20260703,32.8,33.6,31.2,33.6,265000,27.34,22.88,27.01,20.98,0.26
20260706,36.5,36.5,33.65,34.05,217000,27.9,22.04,27.82,21.24,0.21
20260707,34.45,34.55,30.65,30.65,396000,28.13,8.96,28.48,21.44,0.38
20260708,31,33.6,29.5,30.9,1039000,28.36,8.95,29.17,21.65,0.96
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 65
- over_600_ratio: 63.33
- over_800_ratio: 60.91
- over_1000_ratio: 59.25
- over_400_change_1w: -0.26
- over_800_change_1w: -0.26
- over_1000_change_1w: 1.39
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,71.16,,65.31,,61.97,,0,False,False
20260508,71.16,0,65.31,0,61.97,0,0,False,False
20260515,71.17,0.01,65.32,0.01,63.66,1.69,1,True,True
20260522,71.17,0,65.32,0,63.66,0,0,False,False
20260529,71.17,0,65.32,0,63.66,0,0,False,False
20260605,71.19,0.02,65.34,0.02,63.68,0.02,1,True,True
20260612,71.19,0,65.34,0,63.68,0,0,False,False
20260618,67.34,-3.85,62.25,-3.09,59.23,-4.45,0,False,False
20260626,65.26,-2.08,61.17,-1.08,57.86,-1.37,0,False,False
20260703,65,-0.26,60.91,-0.26,59.25,1.39,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 5468 | 凱鈺 | revenue_pullback | 營收成長股價回檔 | 69.0 |  |  |  |  |  | first_seen | 1.事實發生日:115/06/18 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: 本公司之基本資料公告如下:(單位：百萬元) (1)單月           最近一單月        去年同月        與去年同期增減(%)                  (115年05月)      (114年05月) 營業收入               12                  9            35 稅前淨利              0.1                 -2            106(由虧轉盈) 歸屬母公司業主淨利     0.1                 -2            106(由虧轉盈) 每股盈餘(元)       0.0025            -0.0644            104(由虧轉盈)  (2)單季          最近一季單季    去年同季單季     與去年同期增減(%)                   (115/Q1)       (114/Q1) 營業收入               48              29               65 稅前淨利               7                1              623 歸屬母公司業主淨利      7                1              623 每股盈餘(元)        0.12             0.03              340  (3)最近四季累計                 114年第2季至115年第1季 營業收入                    181 稅前淨利                     -8 歸屬母公司業主淨利            -8 每股盈餘(元)              -0.13 公司每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註一：115年5月及去年同期比較數之財務資料係本公司採IFRS會計準 則編製之合併自結數，係未經會計師查核(閱)，僅供投資人參考。 註二：最近一季115年第1季係指單季數字，業經會計師核閱，僅供投資 人參考。 註三：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合 併數，業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 5468 | 凱鈺 | 1 | 1 | 1 | 1 | 4 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
