# INDIVIDUAL STOCK CHATGPT PACKET - 6907 雅特力-KY

## Metadata
- generated_at: 2026-08-22 16:01:07 Asia/Taipei
- stock_id: 6907
- stock_name: 雅特力-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 135
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6907_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6907_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6907_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6907_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6907_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6907_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6907_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6907.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6907.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6907.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6907.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6907_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6907_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6907_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260821
- open: 192.5
- high: 192.5
- low: 186.5
- close: 191.5
- volume: 1571000
- ma5: 187.4
- ema23_primary: 184.05
- distance_to_ema23_pct: 4.05
- ma20: 180
- ma60: 170.56
- ma120: 145.65
- return_5d: 8.81
- return_20d: -5.67
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 6.39
- distance_to_high_60_pct: -22.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,200,200,189.5,197,459000,192.17,2.51,193.55,152.35,0.24
20260728,180,186.5,178,178,491000,190.99,-6.8,195.43,153.34,0.25
20260729,172,172,160.5,160.5,446000,188.45,-14.83,196.12,154.07,0.23
20260730,145,164.5,145,150,511000,185.24,-19.03,196.53,154.43,0.27
20260731,163.5,165,160,165,1081000,183.56,-10.11,197.03,155.03,0.57
20260803,164,181.5,158.5,176,1284000,182.93,-3.79,197.3,155.75,0.69
20260804,180,191,174,181.5,2202000,182.81,-0.72,197,156.62,1.31
20260805,188,191,177,177.5,1942000,182.37,-2.67,197.28,157.36,1.19
20260806,177.5,195,175.5,195,2457000,183.42,6.31,197.57,158.51,1.43
20260807,205,214.5,188,189,4154000,183.88,2.78,197.28,159.62,2.41
20260810,199.5,207,186,189.5,2844000,184.35,2.79,197.12,160.75,1.64
20260811,185.5,196,178,187,2039000,184.57,1.32,195.9,161.9,1.28
20260812,182.5,182.5,169.5,170.5,3601000,183.4,-7.03,192.8,162.79,2.13
20260813,170.5,174.5,168,170.5,1900000,182.32,-6.49,189.38,163.78,1.29
20260814,174,180,170.5,176,2019000,181.8,-3.19,186.38,164.89,1.31
20260817,172,175,169.5,171,916000,180.9,-5.47,184.3,165.84,0.58
20260818,173,188,171.5,188,2455000,181.49,3.59,182.6,166.95,1.51
20260819,186,201,182.5,192.5,8769000,182.41,5.53,181.72,168.11,4.34
20260820,203.5,208.5,191,194,4248000,183.37,5.8,180.57,169.32,1.92
20260821,192.5,192.5,186.5,191.5,1571000,184.05,4.05,180,170.56,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 65.63
- over_600_ratio: 63.28
- over_800_ratio: 62.26
- over_1000_ratio: 62.26
- over_400_change_1w: 0
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,69.2,1.26,63.89,-0.58,62.31,-2.16,1,False,False
20260612,69.03,-0.17,63.6,-0.29,62.3,-0.01,0,False,False
20260618,68.47,-0.56,62.3,-1.3,62.3,0,0,False,False
20260626,67.65,-0.82,62.3,0,62.3,0,0,False,False
20260703,66.68,-0.97,62.3,0,62.3,0,0,False,False
20260709,70.36,3.68,64.14,1.84,64.14,1.84,1,True,True
20260717,69.92,-0.44,64.04,-0.1,64.04,-0.1,0,False,False
20260724,68.28,-1.64,64.02,-0.02,64.02,-0.02,0,False,False
20260731,68.28,0,64.02,0,64.02,0,0,False,False
20260807,66.93,-1.35,63.56,-0.46,62.28,-1.74,0,False,False
20260814,65.63,-1.3,62.26,-1.3,62.26,-0.02,0,False,False
20260821,65.63,0,62.26,0,62.26,0,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6907 | 雅特力-KY | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/13 2.發生緣由:依財團法人中華民國證券櫃檯買賣中心通知辦理 3.財務業務資訊: (1)單月                           最近一月單月     去年同月    與去年同期增減%                              (115/06)      (114/06) ------------------------------------------------------------------------ 營業收入(百萬元)               369            173          113.29% 稅前淨利(百萬元)                81             20          305.00% 歸屬母公司業主淨利(百萬元)      71             14          407.14% 每股盈餘(元)                  1.14           0.26          338.46% (2)單季                           最近一季單季     去年同期     與去年同期增減%                            (115第1季)     (114第1季) ------------------------------------------------------------------------ 營業收入(百萬元)               653            374           74.60% 稅前淨利(百萬元)                78             18          333.33% 歸屬母公司業主淨利(百萬元)      68             14          385.71% 每股盈餘(元)                  1.16           0.28          314.29% (3)最近四季累計                                 (114年第2季至115年第1季) ------------------------------------------------------------------------ 營業收入(百萬元)               1,945 稅前淨利(百萬元)                 196 歸屬母公司業主淨利(百萬元)       161 每股盈餘(元)                    3.03 ------------------------------------------------------------------------ 公司每股面額:10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: (1)以上115年6月及去年同期比較數之財務資料係本公司採IFRS會計 準則編製之合併自結數，未經會計師查核(閱)，僅供投資人參考。 (2)最近一季115年第1季係指單季數字，且係本公司採IFRS下編製之合併數， 業經會計師查核(閱)，僅供投資人參考。 (3)最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合併數， 業經會計師查核(閱)，僅供投資人參考。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6907 | 雅特力-KY | 4 | 4 | 4 | 9 | 13 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
