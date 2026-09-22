# INDIVIDUAL STOCK CHATGPT PACKET - 3550 聯穎

## Metadata
- generated_at: 2026-09-20 22:16:55 Asia/Taipei
- stock_id: 3550
- stock_name: 聯穎
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3550_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3550_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3550_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3550_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3550.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3550.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3550.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3550.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3550_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3550_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3550_latest.md?ref=main

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
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 回檔後短線轉強 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260918
- open: 23
- high: 24.75
- low: 22.9
- close: 23.7
- volume: 2990142
- ma5: 22.35
- ema23_primary: 22.87
- distance_to_ema23_pct: 3.61
- ma20: 23
- ma60: 24.27
- ma120: 23.52
- return_5d: 7.97
- return_20d: 2.82
- volume_ratio: 2.39
- distance_to_ma20_pct_auxiliary: 3.04
- distance_to_high_60_pct: -37.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,22.9,23.55,22.9,23,919697,23.26,-1.11,22.27,25.95,0.47
20260825,23.2,23.5,22.5,23.3,1002633,23.26,0.16,22.43,26,0.52
20260826,23.7,24.5,23.45,23.75,1840694,23.3,1.92,22.66,26.04,0.95
20260827,23.85,24.25,23.5,23.9,1264116,23.35,2.35,22.93,26.09,0.66
20260828,24.15,24.85,24,24.3,2063941,23.43,3.71,23.16,26.13,1.04
20260831,24.35,25.3,23.8,23.8,2273901,23.46,1.44,23.3,26.12,1.12
20260901,23.65,24.15,23.5,23.65,1197891,23.48,0.73,23.39,26.12,0.59
20260902,23.65,24.1,23.45,23.5,925154,23.48,0.09,23.44,26.12,0.47
20260903,23.75,24.05,22.95,22.95,963825,23.44,-2.07,23.45,26.07,0.51
20260904,23.15,23.95,22.45,23.2,1254082,23.42,-0.92,23.38,25.98,0.72
20260907,23.45,23.55,22.85,22.95,892571,23.38,-1.83,23.34,25.89,0.59
20260908,22.7,23.05,22.5,22.65,689530,23.32,-2.86,23.32,25.78,0.48
20260909,22.7,22.95,22.5,22.9,621351,23.28,-1.64,23.29,25.69,0.45
20260910,22.85,22.85,22.45,22.45,542517,23.21,-3.28,23.21,25.55,0.44
20260911,21.95,22.25,21.95,21.95,579447,23.11,-5.01,23.13,25.36,0.51
20260914,21.9,22.15,21.65,21.7,514696,22.99,-5.61,23.05,25.1,0.46
20260915,21.75,22.1,21.2,21.2,615041,22.84,-7.18,22.98,24.85,0.58
20260916,21.6,22.5,21.4,22.4,895643,22.8,-1.77,22.96,24.64,0.85
20260917,22.75,23.65,22.5,22.75,3015363,22.8,-0.22,22.97,24.42,2.63
20260918,23,24.75,22.9,23.7,2990142,22.87,3.61,23,24.27,2.39
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 43.52
- over_600_ratio: 40.69
- over_800_ratio: 36.11
- over_1000_ratio: 31.08
- over_400_change_1w: 0.08
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.26
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,51.29,1.07,41.94,-1.87,38.56,-1.75,1,False,False
20260709,44.51,-6.78,39.08,-2.86,33.88,-4.68,0,False,False
20260717,45.12,0.61,39.58,0.5,33.57,-0.31,1,False,True
20260724,45.14,0.02,39.23,-0.35,34.09,0.52,2,False,True
20260731,44.16,-0.98,38.54,-0.69,34.24,0.15,3,False,True
20260807,43.03,-1.13,38.14,-0.4,33.84,-0.4,0,False,False
20260814,41.73,-1.3,36.5,-1.64,34.05,0.21,1,False,True
20260821,42.06,0.33,36.42,-0.08,33.97,-0.08,2,False,False
20260828,43.12,1.06,36.52,0.1,34.07,0.1,3,True,True
20260904,43.42,0.3,36.66,0.14,33.46,-0.61,4,False,True
20260911,43.44,0.02,36.26,-0.4,31.34,-2.12,5,False,False
20260918,43.52,0.08,36.11,-0.15,31.08,-0.26,6,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3550 | 聯穎 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  |  | continued_2_3d | 1.事實發生日:115/07/13 2.公司名稱:昆山廣穎電線有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由: (1)依據金融監督管理委員會115年7月6日金管證審字第1150347406號函示辦理。 (2)本公司之子公司昆山廣穎電線有限公司因盈餘分配致財報淨值下降， 造成資金貸與超限，應訂定改善計畫。 6.因應措施: (1)本案已訂定改善計畫，並已依規定將相關改善計畫送獨立董事備查。 (2)本公司已督促子公司於6月底前還款將資金貸與餘額降至限額內， 至此改善計畫已執行完成。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本公司擬於近期董事會報告本案，並報告改善計畫已執行完成， 且會依函示於下一次股東會報告。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 3550 | 聯穎 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_2_3d | 1.事實發生日:115/07/13 2.公司名稱:昆山廣穎電線有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由: (1)依據金融監督管理委員會115年7月6日金管證審字第1150347406號函示辦理。 (2)本公司之子公司昆山廣穎電線有限公司因盈餘分配致財報淨值下降， 造成資金貸與超限，應訂定改善計畫。 6.因應措施: (1)本案已訂定改善計畫，並已依規定將相關改善計畫送獨立董事備查。 (2)本公司已督促子公司於6月底前還款將資金貸與餘額降至限額內， 至此改善計畫已執行完成。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本公司擬於近期董事會報告本案，並報告改善計畫已執行完成， 且會依函示於下一次股東會報告。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3550 | 聯穎 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | 1.事實發生日:115/07/13 2.公司名稱:昆山廣穎電線有限公司 3.與公司關係(請輸入本公司或子公司):子公司 4.相互持股比例:不適用 5.發生緣由: (1)依據金融監督管理委員會115年7月6日金管證審字第1150347406號函示辦理。 (2)本公司之子公司昆山廣穎電線有限公司因盈餘分配致財報淨值下降， 造成資金貸與超限，應訂定改善計畫。 6.因應措施: (1)本案已訂定改善計畫，並已依規定將相關改善計畫送獨立董事備查。 (2)本公司已督促子公司於6月底前還款將資金貸與餘額降至限額內， 至此改善計畫已執行完成。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本公司擬於近期董事會報告本案，並報告改善計畫已執行完成， 且會依函示於下一次股東會報告。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3550 | 聯穎 | 2 | 2 | 2 | 3 | 10 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
