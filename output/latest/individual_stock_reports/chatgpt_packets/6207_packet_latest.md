# INDIVIDUAL STOCK CHATGPT PACKET - 6207 雷科

## Metadata
- generated_at: 2026-06-30 22:27:53 Asia/Taipei
- stock_id: 6207
- stock_name: 雷科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 159
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6207_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6207_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6207_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6207_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6207_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6207_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6207_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6207.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6207.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6207.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6207.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6207_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6207_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6207_latest.md?ref=main

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
- date: 20260630
- open: 139
- high: 146.5
- low: 137.5
- close: 146.5
- volume: 7913000
- ma5: 147.8
- ema23_primary: 136.01
- distance_to_ema23_pct: 7.71
- ma20: 143.78
- ma60: 95.08
- ma120: 74.06
- return_5d: -5.79
- return_20d: 19.59
- volume_ratio: 0.63
- distance_to_ma20_pct_auxiliary: 1.9
- distance_to_high_60_pct: -19.28

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,128.5,133,122,127,127,90.28,40.67,87.95,65.9,0
20260603,130,139.5,129.5,139.5,137000,94.38,47.8,91.49,67.31,0.01
20260604,142,153,141,153,148000,99.27,54.13,95.69,68.98,0.02
20260605,155,164,141.5,144.5,151000,103.04,40.24,99.73,70.53,0.02
20260608,130.5,130.5,130.5,130.5,2684000,105.32,23.9,102.84,71.82,0.32
20260609,134,141,122,122.5,23084000,106.76,14.75,105.53,72.99,2.49
20260610,125,134.5,124.5,134.5,12038000,109.07,23.32,108.84,74.35,1.25
20260611,134.5,135,121.5,125,23997000,110.4,13.23,111.58,75.56,2.31
20260612,131,134,124,124,16893000,111.53,11.18,113.92,76.76,1.56
20260615,131,136,131,136,7483000,113.57,19.75,116.47,78.15,0.81
20260616,141.5,149.5,141,149.5,8726000,116.56,28.26,119.75,79.81,1.16
20260617,147,164,142,164,41838000,120.52,36.08,123.92,81.71,5.34
20260618,164.5,171,160.5,165.5,29362000,124.26,33.18,127.76,83.56,3.51
20260622,171,181.5,165,165.5,25188000,127.7,29.6,131.54,85.38,2.62
20260623,168,168,155,155.5,13376000,130.02,19.6,134.38,87.04,1.3
20260624,152.5,163.5,152,159.5,12797000,132.47,20.4,136.93,88.8,1.17
20260625,163.5,163.5,152.5,154.5,7023000,134.31,15.03,139.47,90.51,0.62
20260626,152.5,157,144,145,7793000,135.2,7.25,141.47,92.08,0.67
20260629,142.5,142.5,132.5,133.5,10150000,135.06,-1.15,142.57,93.48,0.84
20260630,139,146.5,137.5,146.5,7913000,136.01,7.71,143.78,95.08,0.63
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 20.51
- over_600_ratio: 14.83
- over_800_ratio: 13.34
- over_1000_ratio: 12.34
- over_400_change_1w: -8.05
- over_800_change_1w: -5.16
- over_1000_change_1w: -4.26
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,17.47,,13.95,,11.79,,0,False,False
20260508,17.87,0.4,14.31,0.36,13.21,1.42,1,False,True
20260515,20.12,2.25,14.49,0.18,13.39,0.18,2,True,True
20260522,26.75,6.63,19.26,4.77,17.03,3.64,3,True,True
20260529,22.55,-4.2,14.51,-4.75,12.52,-4.51,0,False,False
20260605,27.41,4.86,19.97,5.46,14.86,2.34,1,True,True
20260612,21.9,-5.51,13.22,-6.75,12.15,-2.71,0,False,False
20260618,28.56,6.66,18.5,5.28,16.6,4.45,1,True,True
20260626,20.51,-8.05,13.34,-5.16,12.34,-4.26,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 6207 | 雷科 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/06/24 2.發生緣由:依據財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告 3.財務業務資訊: 單月                       115年05月        114年05月     與去年同期增減% ----------------------  --------------  --------------  ------------------ 營業收入(百萬元)             117.99           90.92            29.78 稅前淨利(百萬元)              25.78           (7.09)          虧轉盈 歸屬母公司淨利(百萬元)        22.87           (9.76)          虧轉盈 每股盈餘(  元  )               0.26           (0.12)          虧轉盈 ========================================================================== 最近一季單季(註1)         115年第1季       114年第1季     與去年同期增減% ----------------------  --------------  --------------  ------------------ 營業收入(百萬元)                273             279            (2.15) 稅前淨利(百萬元)                 12              32           (62.50) 歸屬母公司淨利(百萬元)            5              27           (81.48) 每股盈餘(  元  )               0.06            0.33           (81.82) =========================================================================== 最近四季累計(註2)             114年第2季~115年第1季 -----------------------     -------------------------- 營業收入(百萬元)                      1,108 稅前淨利(百萬元)                         65 歸屬母公司淨利(百萬元)                   50 每股盈餘(  元  )                       0.63 =========================================================================== 公司每股面額10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註1：以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計 準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第1季係指單季數字，係經會計師核閱。 註3：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數， 業經會計師查核。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 6207 | 雷科 | 1 | 1 | 2 | 4 | 5 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
