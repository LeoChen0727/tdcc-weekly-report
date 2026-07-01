# INDIVIDUAL STOCK CHATGPT PACKET - 6265 方土昶

## Metadata
- generated_at: 2026-07-01 22:28:23 Asia/Taipei
- stock_id: 6265
- stock_name: 方土昶
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 160
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6265_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6265_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6265_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6265_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6265_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6265_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6265_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6265.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6265.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6265.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6265.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6265_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6265_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6265_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- decision_score_high
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
- date: 20260701
- open: 53.9
- high: 54.1
- low: 49.9
- close: 50.3
- volume: 4869000
- ma5: 52.58
- ema23_primary: 54.15
- distance_to_ema23_pct: -7.11
- ma20: 56.3
- ma60: 48.01
- ma120: 44.32
- return_5d: -10.02
- return_20d: -18.34
- volume_ratio: 0.74
- distance_to_ma20_pct_auxiliary: -10.66
- distance_to_high_60_pct: -22.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,62.3,62.8,58.3,58.9,60000,49.69,18.53,48.99,43.06,0.01
20260604,58.5,64.7,58.5,63.9,64000,50.87,25.6,50.01,43.56,0.01
20260605,62,62,57.6,57.6,58000,51.44,11.99,50.69,43.94,0.01
20260608,51.9,53.4,51.9,52.9,5800000,51.56,2.6,51.06,44.2,1.38
20260609,54.3,56.4,52.5,55.5,8307000,51.89,6.97,51.59,44.43,2.06
20260610,57.2,60.5,56.1,56.3,15435000,52.25,7.74,52.27,44.7,3.43
20260611,57.6,59.7,55.1,57.7,11833000,52.71,9.47,52.84,44.92,2.93
20260612,59.4,62.2,58.7,58.9,15440000,53.22,10.67,53.54,45.15,3.72
20260615,60.6,61.1,58.2,58.4,8823000,53.65,8.84,54.17,45.34,2.07
20260616,59.1,60.2,55.7,55.9,9313000,53.84,3.82,54.84,45.51,2.16
20260617,55.4,57.2,54.7,57.2,4924000,54.12,5.69,55.62,45.67,1.15
20260618,56.8,58.4,56.6,57.6,6448000,54.41,5.86,56.31,45.91,1.48
20260622,58.4,61,57.3,59.8,12191000,54.86,9,56.9,46.23,2.46
20260623,61,61,56,56.6,8930000,55.01,2.9,57.09,46.48,1.66
20260624,55.2,56.6,55,55.9,4120000,55.08,1.49,57.23,46.76,0.74
20260625,57.1,58.4,55,55,6131000,55.07,-0.13,57.23,47.03,1.04
20260626,54.6,55.8,52.1,52.2,4772000,54.83,-4.8,57.16,47.25,0.78
20260629,52.5,53.8,51.1,52,2423000,54.6,-4.76,56.99,47.51,0.39
20260630,53.1,53.8,52.2,53.4,1841000,54.5,-2.01,56.87,47.78,0.29
20260701,53.9,54.1,49.9,50.3,4869000,54.15,-7.11,56.3,48.01,0.74
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 46
- over_600_ratio: 44.5
- over_800_ratio: 41.76
- over_1000_ratio: 40.92
- over_400_change_1w: -1.63
- over_800_change_1w: -2.09
- over_1000_change_1w: -0.6
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,49.84,,45.67,,40.22,,0,False,False
20260508,45.63,-4.21,41.1,-4.57,37.99,-2.23,0,False,False
20260515,49.27,3.64,43.64,2.54,39.08,1.09,1,True,True
20260522,45.46,-3.81,41.18,-2.46,38.9,-0.18,0,False,False
20260529,51.51,6.05,46.82,5.64,43.82,4.92,1,True,True
20260605,54.86,3.35,51.89,5.07,46.51,2.69,2,True,True
20260612,46.43,-8.43,44.03,-7.86,41.53,-4.98,0,False,False
20260618,47.63,1.2,43.85,-0.18,41.52,-0.01,1,False,False
20260626,46,-1.63,41.76,-2.09,40.92,-0.6,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6265 | 方土昶 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  |  | stale_signal | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過本公司民國114年度虧損撥補案 3.重要決議事項二、章程修訂:無 4.重要決議事項三、營業報告書及財務報表:  通過本公司民國114年度個體財務報表及合併財務報表暨營業報告書案 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:  通過修訂本公司「取得或處分資產處理程序」案 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260701 | 6265 | 方土昶 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 27.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過本公司民國114年度虧損撥補案 3.重要決議事項二、章程修訂:無 4.重要決議事項三、營業報告書及財務報表:  通過本公司民國114年度個體財務報表及合併財務報表暨營業報告書案 5.重要決議事項四、董監事選舉:無 6.重要決議事項五、其他事項:  通過修訂本公司「取得或處分資產處理程序」案 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6265 | 方土昶 | 8 | 7 | 5 | 8 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
