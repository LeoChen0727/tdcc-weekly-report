# INDIVIDUAL STOCK CHATGPT PACKET - 8064 東捷

## Metadata
- generated_at: 2026-07-05 22:28:23 Asia/Taipei
- stock_id: 8064
- stock_name: 東捷
- packet_status: standard_180d_window_packet
- latest_price_date: 20260703
- price_rows: 162
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8064_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8064_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8064_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8064_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8064_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8064_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8064_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8064.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8064.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8064.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8064.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8064_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8064_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8064_latest.md?ref=main

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
- date: 20260703
- open: 145.5
- high: 149
- low: 143
- close: 145.5
- volume: 4458000
- ma5: 143.8
- ema23_primary: 144.01
- distance_to_ema23_pct: 1.03
- ma20: 146.68
- ma60: 123.58
- ma120: 89.69
- return_5d: 8.58
- return_20d: -13.91
- volume_ratio: 0.46
- distance_to_ma20_pct_auxiliary: -0.8
- distance_to_high_60_pct: -23.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,164,173.5,157,166,166000,136.84,21.31,138.32,98.14,0.06
20260608,149.5,156.5,149.5,152,9044000,138.1,10.06,140.25,99.74,2.78
20260609,152.5,157,147,149,12220000,139.01,7.19,141.78,101.27,3.39
20260610,140,163,138,138.5,24196000,138.97,-0.34,142.78,102.64,5.2
20260611,140.5,143,130,133,12462000,138.47,-3.95,143.65,103.83,2.44
20260612,141.5,143,134,134.5,7994000,138.14,-2.64,144.38,104.97,1.54
20260615,139,143.5,138.5,139.5,5771000,138.25,0.9,144.75,106.17,1.1
20260616,143,148.5,138,140,9249000,138.4,1.16,144.9,107.39,1.71
20260617,139,154,136,154,17274000,139.7,10.24,146.43,108.89,2.91
20260618,159,160,153.5,156,14511000,141.06,10.59,148.2,110.31,2.54
20260622,161.5,171.5,158,165.5,19350000,143.09,15.66,149.85,111.99,2.9
20260623,165.5,166.5,153,156,10213000,144.17,8.21,150.38,113.45,1.42
20260624,151.5,161,151.5,152,7027000,144.82,4.96,150.53,114.74,0.93
20260625,156,156,144.5,144.5,5296000,144.8,-0.2,150.6,115.97,0.68
20260626,146,147.5,133,134,4953000,143.9,-6.88,150.65,117.09,0.62
20260629,135,138.5,131.5,133,3291000,142.99,-6.99,150.15,118.26,0.4
20260630,138,146,137.5,146,4958000,143.24,1.93,149.6,119.61,0.59
20260701,148,160,148,148,13325000,143.64,3.04,149.15,120.98,1.47
20260702,144,152.5,143.5,146.5,6085000,143.87,1.82,147.85,122.34,0.65
20260703,145.5,149,143,145.5,4458000,144.01,1.03,146.68,123.58,0.46
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 45.9
- over_600_ratio: 42.9
- over_800_ratio: 40.69
- over_1000_ratio: 38.8
- over_400_change_1w: -1.49
- over_800_change_1w: -0.63
- over_1000_change_1w: -0.63
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,57.56,,52.1,,49.21,,0,False,False
20260508,53.42,-4.14,47.44,-4.66,45.56,-3.65,0,False,False
20260515,52.56,-0.86,46.02,-1.42,45.07,-0.49,0,False,False
20260522,49.43,-3.13,43.4,-2.62,41.39,-3.68,0,False,False
20260529,47.44,-1.99,42.77,-0.63,40.75,-0.64,0,False,False
20260605,49.29,1.85,43.54,0.77,41.53,0.78,1,True,True
20260612,46.5,-2.79,40.9,-2.64,38.98,-2.55,0,False,False
20260618,48.06,1.56,42.06,1.16,39.16,0.18,1,True,True
20260626,47.39,-0.67,41.32,-0.74,39.43,0.27,2,False,True
20260703,45.9,-1.49,40.69,-0.63,38.8,-0.63,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 8064 | 東捷 | pattern | 型態觀察 | 43.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/06/23 2.發生緣由:依據財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (一)單月                  最近一月單月                去年同月                    115/5月                   114/5月      與去年同期增減% ----------------------------------------------------------------------- 營業收入(百萬元)       156                    189                 (17%) 稅前淨利(百萬元)         2                    (17)                虧轉盈 歸屬母公司業主淨利      (5)                   (15)                (67%) (百萬元) 每股盈餘(元)          (0.03)                  (0.09)              虧轉盈 ==============================================  (二)單季                   單一季單季                去年同期                    115/第1季               114/第1季     與去年同期增減% ----------------------------------------------------------------------- 營業收入(百萬元)       673                    518                   30% 稅前淨利(百萬元)        77                   (118)                虧轉盈 歸屬母公司業主淨利      58                   (108)                虧轉盈 (百萬元) 每股盈餘(元)          0.35                  (0.66)                虧轉盈 ==============================================  (三)最近四季累計       114年第2季至115年第1季 -------------------------------------------------------------------- 營業收入(百萬元)                   3,026 稅前淨利(百萬元)                     531 歸屬母公司業主淨利                   391 (百萬元) 每股盈餘(元)                        2.37 ============================================ 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無。 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無。 6.其他應敘明事項: 註1：以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計 準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 註2：最近一季115年第1季係指單季數字，係經會計師核閱。 註3：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數， 業經會計師查核(閱)。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 8064 | 東捷 | 4 | 4 | 4 | 8 | 8 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
