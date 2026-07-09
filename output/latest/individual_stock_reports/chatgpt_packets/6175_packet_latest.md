# INDIVIDUAL STOCK CHATGPT PACKET - 6175 立敦

## Metadata
- generated_at: 2026-07-09 22:27:31 Asia/Taipei
- stock_id: 6175
- stock_name: 立敦
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6175_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6175_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6175_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6175_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6175_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6175_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6175_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6175.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6175.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6175.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6175.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6175_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6175_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6175_latest.md?ref=main

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
- date: 20260709
- open: 108
- high: 110.5
- low: 105
- close: 105
- volume: 3561000
- ma5: 110.1
- ema23_primary: 105.89
- distance_to_ema23_pct: -0.84
- ma20: 108.94
- ma60: 88.22
- ma120: 68.59
- return_5d: -4.11
- return_20d: 5.11
- volume_ratio: 0.3
- distance_to_ma20_pct_auxiliary: -3.61
- distance_to_high_60_pct: -14.63

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,101.5,106,96.6,103,19824000,90.16,14.24,92.5,69.11,2.31
20260612,107,109,98.5,98.6,15167000,90.87,8.51,93.73,69.91,1.82
20260615,101.5,108,101.5,108,12425000,92.29,17.02,95.4,70.89,1.5
20260616,109,110.5,97.7,98.1,14636000,92.78,5.74,96.6,71.72,1.7
20260617,96.6,107.5,96.6,107.5,12673000,94,14.36,97.9,72.73,1.44
20260618,108,117,105.5,114,28378000,95.67,19.16,99.34,73.87,3.18
20260622,113.5,115,108,109,11266000,96.78,12.63,100.38,74.94,1.19
20260623,113,116,109,110.5,14486000,97.92,12.84,101.19,76.02,1.42
20260624,109.5,116,109,115.5,11916000,99.39,16.21,102.33,77.2,1.1
20260625,116,123,113,116.5,17939000,100.81,15.56,103.28,78.39,1.53
20260626,115,121,111,111,11500000,101.66,9.18,103.48,79.4,0.94
20260629,110,111,104.5,106,8016000,102.03,3.9,103.64,80.38,0.63
20260630,109.5,116,108.5,112.5,7432000,102.9,9.33,104.27,81.45,0.57
20260701,115,120,108,108.5,11912000,103.36,4.97,104.94,82.48,0.87
20260702,107.5,111.5,106.5,109.5,3862000,103.88,5.41,105.86,83.55,0.28
20260703,108,117.5,108,115,9215000,104.8,9.73,107.21,84.62,0.65
20260706,116.5,119.5,110.5,116.5,9620000,105.78,10.14,108.2,85.7,0.65
20260707,116.5,119.5,105.5,107,7592000,105.88,1.06,108.53,86.6,0.55
20260708,109,110,103,107,4792000,105.97,0.97,108.68,87.42,0.37
20260709,108,110.5,105,105,3561000,105.89,-0.84,108.94,88.22,0.3
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 62.3
- over_600_ratio: 59.18
- over_800_ratio: 57.08
- over_1000_ratio: 55.92
- over_400_change_1w: -0.85
- over_800_change_1w: 0.56
- over_1000_change_1w: -0.01
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.02,,59.49,,57.26,,0,False,False
20260508,63.23,0.21,58.17,-1.32,56.43,-0.83,1,False,False
20260515,62.66,-0.57,57.01,-1.16,56.42,-0.01,0,False,False
20260522,62.57,-0.09,57.99,0.98,56.26,-0.16,1,False,True
20260529,66.97,4.4,61.35,3.36,60.13,3.87,2,True,True
20260605,64.08,-2.89,58.93,-2.42,57.76,-2.37,0,False,False
20260612,63.7,-0.38,58.15,-0.78,57.6,-0.16,0,False,False
20260618,65.58,1.88,60.55,2.4,59.3,1.7,1,True,True
20260626,63.15,-2.43,56.52,-4.03,55.93,-3.37,0,False,False
20260703,62.3,-0.85,57.08,0.56,55.92,-0.01,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 6175 | 立敦 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/06/22 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                             最近一月單月     去年同月       與去年同期                               (115/05)       (114/05)          增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)              473             378          25.13%    稅前淨利(百萬元)               78              45          72.68%    本期淨利(百萬元)               64              16         300.00%    每股盈餘(元)                 0.43            0.11         290.91%   =======================  ==============  ==============  ==============    (2)單季                            最近一季單季     去年同期       與去年同期                             (115第1季)      (114第1季)        增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)            1,118          1,072           4.29%    稅前淨利(損)(百萬元)          171            174          -1.72%    本期淨利(損)(百萬元)          111            109           1.83%    每股盈餘(元)                 0.74           0.73           1.37%   =======================  ==============  ==============  ==============    (3)最近四季累計                               114年第2季至115年第1季   -----------------------  -----------------------------    營業收入(百萬元)                  4,213    稅前淨利(百萬元)                    681    本期淨利(百萬元)                    403    每股盈餘(元)                       2.69   每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之    合併數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係    本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經    會計師查核(閱)，僅供投資人參考。 |
| 20260709 | 6175 | 立敦 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/22 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理。 3.財務業務資訊: (1)單月                             最近一月單月     去年同月       與去年同期                               (115/05)       (114/05)          增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)              473             378          25.13%    稅前淨利(百萬元)               78              45          72.68%    本期淨利(百萬元)               64              16         300.00%    每股盈餘(元)                 0.43            0.11         290.91%   =======================  ==============  ==============  ==============    (2)單季                            最近一季單季     去年同期       與去年同期                             (115第1季)      (114第1季)        增減%   -----------------------  --------------  --------------  --------------    營業收入(百萬元)            1,118          1,072           4.29%    稅前淨利(損)(百萬元)          171            174          -1.72%    本期淨利(損)(百萬元)          111            109           1.83%    每股盈餘(元)                 0.74           0.73           1.37%   =======================  ==============  ==============  ==============    (3)最近四季累計                               114年第2季至115年第1季   -----------------------  -----------------------------    營業收入(百萬元)                  4,213    稅前淨利(百萬元)                    681    本期淨利(百萬元)                    403    每股盈餘(元)                       2.69   每股面額：10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年5月及去年同期比較數之財務資料係本公司採IFRS會計準則編製之    合併數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，非為最近財務報告中之累計數字，且係    本公司採IFRS下編製之合併數，業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數，業經    會計師查核(閱)，僅供投資人參考。；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 6175 | 立敦 | 3 | 3 | 4 | 8 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
