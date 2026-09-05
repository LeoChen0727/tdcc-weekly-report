# INDIVIDUAL STOCK CHATGPT PACKET - 6199 天品

## Metadata
- generated_at: 2026-09-05 22:17:28 Asia/Taipei
- stock_id: 6199
- stock_name: 天品
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6199_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6199_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6199_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6199_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6199.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6199.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6199.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6199.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6199_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6199_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6199_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260904
- open: 95.2
- high: 96.4
- low: 94.7
- close: 96.1
- volume: 2686000
- ma5: 94.48
- ema23_primary: 95.52
- distance_to_ema23_pct: 0.61
- ma20: 95.44
- ma60: 98.37
- ma120: 99.47
- return_5d: 3
- return_20d: 0.1
- volume_ratio: 3.31
- distance_to_ma20_pct_auxiliary: 0.69
- distance_to_high_60_pct: -11.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,96.3,98.2,96.3,97.7,408000,98.91,-1.22,99.28,98.31,0.81
20260811,97.8,99,97.3,98.5,356000,98.87,-0.38,99,98.33,0.74
20260812,99.1,104,99.1,103.5,586000,99.26,4.27,99.06,98.38,1.29
20260813,103,104.5,97,97.3,609000,99.09,-1.81,98.72,98.31,1.35
20260814,97.5,99.4,97.4,99.2,423000,99.1,0.1,98.68,98.31,0.93
20260817,98.8,99.3,96.6,96.6,535000,98.89,-2.32,98.72,98.25,1.14
20260818,95.9,96.2,94.2,94.6,352000,98.54,-3.99,98.42,98.17,0.75
20260819,95,99.8,95,95.9,1508000,98.32,-2.46,98.31,98.12,2.8
20260820,96,96.8,94.1,94.1,329000,97.97,-3.95,97.73,98.12,0.63
20260821,93,94.9,92.5,93.9,723000,97.63,-3.82,97.28,98.11,1.33
20260824,94,94.2,92.5,93.5,700000,97.28,-3.89,96.95,98.13,1.22
20260825,92.7,94.1,91.8,93.7,754000,96.98,-3.39,96.71,98.18,1.29
20260826,93.7,95.8,92,92.3,1514000,96.59,-4.45,96.62,98.22,2.53
20260827,92.3,92.6,91.5,92.4,302000,96.24,-3.99,96.53,98.25,0.52
20260828,92.4,93.6,91.9,93.3,591000,96,-2.81,96.2,98.29,1.03
20260831,93.3,93.3,91.8,92.8,412000,95.73,-3.06,95.97,98.33,0.7
20260901,92.1,93.9,92.1,93.1,717000,95.51,-2.53,95.66,98.38,1.18
20260902,92.7,95.6,92.2,95.2,673000,95.49,-0.3,95.5,98.4,1.09
20260903,95.2,97.7,94,95.2,2043000,95.46,-0.28,95.44,98.38,2.92
20260904,95.2,96.4,94.7,96.1,2686000,95.52,0.61,95.44,98.37,3.31
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 81.6
- over_600_ratio: 79.43
- over_800_ratio: 78.14
- over_1000_ratio: 78.14
- over_400_change_1w: -0.24
- over_800_change_1w: 0.02
- over_1000_change_1w: 0.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,79.22,0.68,74.61,0.12,74.61,0.12,5,True,True
20260626,79.85,0.63,75.04,0.43,75.04,0.43,6,True,True
20260703,81.37,1.52,76.63,1.59,75.28,0.24,7,True,True
20260709,83.29,1.92,78.34,1.71,77.01,1.73,8,True,True
20260717,83.44,0.15,77.54,-0.8,77.54,0.53,9,False,True
20260724,83.31,-0.13,77.52,-0.02,77.52,-0.02,0,False,False
20260731,82.02,-1.29,78.29,0.77,78.29,0.77,1,False,True
20260807,82.59,0.57,78.32,0.03,78.32,0.03,2,False,True
20260814,82.58,-0.01,78.15,-0.17,78.15,-0.17,0,False,False
20260821,82.71,0.13,78.15,0,78.15,0,1,False,False
20260828,81.84,-0.87,78.12,-0.03,78.12,-0.03,0,False,False
20260904,81.6,-0.24,78.14,0.02,78.14,0.02,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6199 | 天品 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期：115/07/01 2.股東臨時會召開日期：115/07/29 3.股東臨時會召開地點：新北市中和區板南路659號19樓(元隆捷運雙星B棟) 4.股東臨時會召開方式(實體股東會/視訊輔助股東會/視訊股東會)：實體股東會 5.召集事由一：討論事項 (1)：子公司天品國際股份有限公司以自地委建方式與關係人「宏固營造工程股份有限公司」 簽訂「基隆孝光閣」工程承攬契約案 (2)：本公司「公司章程」修訂案 6.臨時動議： 7.停止過戶起始日期：115/06/30 8.停止過戶截止日期：115/07/29 9.其他應敘明事項：(1)本次股東會股東得以電子方式行使表決權，行使期間自民國115年7月14日 至115年7月26日止，電子投票平台為台灣集中保管結算所股東會電子投票平台， 網址：https://stockservices.tdcc.com.tw。 (2)115/7/1董事會新增討論事項第二案。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 6199 | 天品 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期：115/07/01 2.股東臨時會召開日期：115/07/29 3.股東臨時會召開地點：新北市中和區板南路659號19樓(元隆捷運雙星B棟) 4.股東臨時會召開方式(實體股東會/視訊輔助股東會/視訊股東會)：實體股東會 5.召集事由一：討論事項 (1)：子公司天品國際股份有限公司以自地委建方式與關係人「宏固營造工程股份有限公司」 簽訂「基隆孝光閣」工程承攬契約案 (2)：本公司「公司章程」修訂案 6.臨時動議： 7.停止過戶起始日期：115/06/30 8.停止過戶截止日期：115/07/29 9.其他應敘明事項：(1)本次股東會股東得以電子方式行使表決權，行使期間自民國115年7月14日 至115年7月26日止，電子投票平台為台灣集中保管結算所股東會電子投票平台， 網址：https://stockservices.tdcc.com.tw。 (2)115/7/1董事會新增討論事項第二案。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 6199 | 天品 | revenue_breakout_low_response | 營收爆發低反應股 | 13 | 44 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.董事會決議日期：115/07/01 2.股東臨時會召開日期：115/07/29 3.股東臨時會召開地點：新北市中和區板南路659號19樓(元隆捷運雙星B棟) 4.股東臨時會召開方式(實體股東會/視訊輔助股東會/視訊股東會)：實體股東會 5.召集事由一：討論事項 (1)：子公司天品國際股份有限公司以自地委建方式與關係人「宏固營造工程股份有限公司」 簽訂「基隆孝光閣」工程承攬契約案 (2)：本公司「公司章程」修訂案 6.臨時動議： 7.停止過戶起始日期：115/06/30 8.停止過戶截止日期：115/07/29 9.其他應敘明事項：(1)本次股東會股東得以電子方式行使表決權，行使期間自民國115年7月14日 至115年7月26日止，電子投票平台為台灣集中保管結算所股東會電子投票平台， 網址：https://stockservices.tdcc.com.tw。 (2)115/7/1董事會新增討論事項第二案。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 6199 | 天品 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.董事會決議日期：115/07/01 2.股東臨時會召開日期：115/07/29 3.股東臨時會召開地點：新北市中和區板南路659號19樓(元隆捷運雙星B棟) 4.股東臨時會召開方式(實體股東會/視訊輔助股東會/視訊股東會)：實體股東會 5.召集事由一：討論事項 (1)：子公司天品國際股份有限公司以自地委建方式與關係人「宏固營造工程股份有限公司」 簽訂「基隆孝光閣」工程承攬契約案 (2)：本公司「公司章程」修訂案 6.臨時動議： 7.停止過戶起始日期：115/06/30 8.停止過戶截止日期：115/07/29 9.其他應敘明事項：(1)本次股東會股東得以電子方式行使表決權，行使期間自民國115年7月14日 至115年7月26日止，電子投票平台為台灣集中保管結算所股東會電子投票平台， 網址：https://stockservices.tdcc.com.tw。 (2)115/7/1董事會新增討論事項第二案。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6199 | 天品 | 2 | 2 | 2 | 3 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
