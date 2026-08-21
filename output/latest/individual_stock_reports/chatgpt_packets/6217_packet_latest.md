# INDIVIDUAL STOCK CHATGPT PACKET - 6217 中探針

## Metadata
- generated_at: 2026-08-21 22:27:55 Asia/Taipei
- stock_id: 6217
- stock_name: 中探針
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 203
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6217_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6217_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6217_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6217_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6217_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6217_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6217_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6217.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6217.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6217.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6217.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6217_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6217_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6217_latest.md?ref=main

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
- open: 151.5
- high: 155
- low: 148
- close: 150
- volume: 1277000
- ma5: 156.9
- ema23_primary: 163.21
- distance_to_ema23_pct: -8.09
- ma20: 145.55
- ma60: 210.32
- ma120: 214.44
- return_5d: -11.24
- return_20d: -1.96
- volume_ratio: 0.94
- distance_to_ma20_pct_auxiliary: 3.06
- distance_to_high_60_pct: -54.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,138,138,138,138,363000,210.52,-34.45,219.25,254.08,0.1
20260728,124.5,124.5,124.5,124.5,163000,203.35,-38.78,213.82,251.53,0.05
20260729,112.5,112.5,112.5,112.5,153000,195.78,-42.54,206.65,248.74,0.05
20260730,101.5,101.5,101.5,101.5,284000,187.92,-45.99,198.57,245.47,0.11
20260731,111.5,111.5,93.6,111,3178000,181.51,-38.85,190.88,242.61,1.26
20260803,109.5,122,109.5,122,969000,176.55,-30.9,183.53,239.97,0.43
20260804,126,134,126,134,461000,173.01,-22.55,177.43,237.78,0.21
20260805,147,147,147,147,202000,170.84,-13.95,172.57,235.53,0.09
20260806,138,161.5,138,161.5,965000,170.06,-5.03,167.95,233.05,0.45
20260807,162,172.5,157,165,1449000,169.64,-2.73,163.7,230.12,0.66
20260810,165,173,161,165,4797000,169.25,-2.51,159.82,227.46,2.02
20260811,166.5,166.5,152,153,891000,167.9,-8.87,156,225.01,0.38
20260812,149,156,149,154,654000,166.74,-7.64,152.25,222.67,0.28
20260813,160,169,160,168.5,878000,166.89,0.97,149.78,221.05,0.38
20260814,166,172,160,169,571000,167.06,1.16,148.4,219.88,0.25
20260817,172,172,164,171,492000,167.39,2.16,148.1,218.61,0.22
20260818,176.5,183.5,155,157,4868000,166.53,-5.72,147.5,216.69,2.95
20260819,147.5,164.5,145,153,2763000,165.4,-7.5,146.53,214.48,2.08
20260820,156,157,148.5,153.5,1778000,164.41,-6.63,145.7,212.43,1.31
20260821,151.5,155,148,150,1277000,163.21,-8.09,145.55,210.32,0.94
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 26.89
- over_600_ratio: 25.22
- over_800_ratio: 22.32
- over_1000_ratio: 17.62
- over_400_change_1w: -0.61
- over_800_change_1w: -0.21
- over_1000_change_1w: -1.9
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,36.54,0.62,27.6,-1.47,24.64,0.58,1,False,True
20260605,34.03,-2.51,26.92,-0.68,23.35,-1.29,0,False,False
20260612,33.41,-0.62,23.99,-2.93,20.23,-3.12,0,False,False
20260618,32.23,-1.18,25.24,1.25,22.33,2.1,1,False,True
20260626,29.51,-2.72,23.62,-1.62,21.33,-1,0,False,False
20260703,29.48,-0.03,22.03,-1.59,19.74,-1.59,0,False,False
20260709,29.9,0.42,22.79,0.76,19.79,0.05,1,True,True
20260717,30.19,0.29,22.86,0.07,20.62,0.83,2,False,True
20260724,28.13,-2.06,21.07,-1.79,18.74,-1.88,0,False,False
20260731,27.48,-0.65,21.73,0.66,18.67,-0.07,1,False,True
20260807,27.5,0.02,22.53,0.8,19.52,0.85,2,False,True
20260814,26.89,-0.61,22.32,-0.21,17.62,-1.9,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6217 | 中探針 | revenue_pullback | 營收成長股價回檔 | 62.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/06/29 2.發生緣由:依據財團法人中華民國證券櫃檯買賣中心通知處理及辦理公告 3.財務業務資訊: (1)單月                             最近一月單月    去年同月    與去年同期增減%                               (115/05)      (114/05) ------------------------------------------------------------------------- 營業收入(百萬元)                  406          268            51.49% 稅前淨利(百萬元)                    1          (41)          102.44% 歸屬母公司業主淨利(百萬元)          2          (39)          105.13% 每股盈餘(元)                     0.02        (0.34)          105.88% ========================================================================= (2)單季                             最近一季單季     去年同期     與去年同期增減%                             (115年第1季)   (114年第1季) ------------------------------------------------------------------------- 營業收入(百萬元)                1,079           790           36.58% 稅前淨利(百萬元)                   13           (77)         116.88% 歸屬母公司業主淨利(百萬元)         13           (82)         115.85% 每股盈餘(元)                     0.11         (0.79)         113.92% ========================================================================= (3)最近四季累計                                 114年第2季至115年第1季 ------------------------------------------------------------------------ 營業收入(百萬元)                          3,988 稅前淨利(百萬元)                           (110) 歸屬母公司業主淨利(百萬元)                  (90) 每股盈餘(元)                              (0.75) ======================================================================== 公司每股面額:10元 4.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序 」第4條所列重大訊息之情事（如 「有」，請說明）:無 5.有無「財團法人中華民國證券櫃檯買賣中心對有價證券上櫃公司 重大訊息之查證暨公開處理程序」第11條所列重大訊息說明記者會 之情事:無 6.其他應敘明事項: 註1：以上115年05月及去年同期比較數之財務資料係本公司採IFRS會計      準則編製之合併數，未經會計師查核(閱)，僅供投資人參考 註2：最近一季115年第1季係指單季數字，非為最近財務報告中之累計      數字，且係本公司採IFRS下編製之合併數，業經會計師查核(閱)，      僅供投資人參考 註3：最近四季累計係本公司114年第2季至115年第1季採IFRS編製之合      併數，業經會計師查核(閱)，僅供投資人參考；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 6217 | 中探針 | 1 | 1 | 2 | 2 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
