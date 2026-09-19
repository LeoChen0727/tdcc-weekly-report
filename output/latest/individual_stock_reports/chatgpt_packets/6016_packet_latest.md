# INDIVIDUAL STOCK CHATGPT PACKET - 6016 康和證

## Metadata
- generated_at: 2026-09-19 15:54:03 Asia/Taipei
- stock_id: 6016
- stock_name: 康和證
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6016_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6016_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6016_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6016_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6016_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6016_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6016_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6016.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6016.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6016.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6016.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6016_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6016_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6016_latest.md?ref=main

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
- high: 23.1
- low: 22.5
- close: 23
- volume: 4018000
- ma5: 22.49
- ema23_primary: 21.87
- distance_to_ema23_pct: 5.19
- ma20: 21.65
- ma60: 22.64
- ma120: 22.94
- return_5d: 3.37
- return_20d: 17.35
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: 6.22
- distance_to_high_60_pct: -23.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,19.8,19.8,19.2,19.35,1305000,20.71,-6.56,19.73,25.34,0.31
20260825,19.2,19.3,19,19.3,1432000,20.59,-6.27,19.69,25.17,0.37
20260826,19.45,19.8,19.4,19.8,1922000,20.52,-3.53,19.71,25,0.53
20260827,19.85,20.6,19.85,20.35,3616000,20.51,-0.78,19.78,24.79,0.99
20260828,20.65,21.95,20.65,21.35,9505000,20.58,3.74,19.82,24.55,2.44
20260831,20.9,21.25,20.55,21.2,3646000,20.63,2.75,19.86,24.32,0.92
20260901,21.25,21.8,21.25,21.55,3119000,20.71,4.07,19.92,24.08,0.78
20260902,21.4,21.4,20.65,20.95,6339000,20.73,1.07,19.92,23.89,1.54
20260903,21.25,21.8,21.2,21.4,6322000,20.78,2.96,19.98,23.75,1.49
20260904,21.8,22.4,21.55,22.4,6421000,20.92,7.08,20.11,23.67,1.49
20260907,22.65,22.85,21.8,22.1,8085000,21.02,5.15,20.29,23.59,1.97
20260908,23,23.3,22.6,23.15,11626000,21.2,9.22,20.52,23.5,2.56
20260909,23.35,23.35,22.55,22.9,7378000,21.34,7.32,20.67,23.39,1.62
20260910,22.9,23.05,22.45,22.55,4059000,21.44,5.19,20.79,23.28,0.9
20260911,22.35,22.55,22,22.25,3461000,21.51,3.46,20.89,23.17,0.77
20260914,22.2,22.75,21.95,22.55,3366000,21.59,4.43,21.03,23.07,0.75
20260915,22.5,22.6,21.85,21.9,3882000,21.62,1.3,21.16,22.94,0.85
20260916,21.85,22.3,21.85,22.1,2651000,21.66,2.04,21.3,22.82,0.58
20260917,22.2,23.1,22.2,22.9,5397000,21.76,5.23,21.48,22.73,1.13
20260918,23,23.1,22.5,23,4018000,21.87,5.19,21.65,22.64,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 51.34
- over_600_ratio: 48.31
- over_800_ratio: 46.21
- over_1000_ratio: 45.04
- over_400_change_1w: 0.31
- over_800_change_1w: 0.27
- over_1000_change_1w: 0.5
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,51.54,0,45.74,-0.17,44.02,-0.46,0,False,False
20260709,51.69,0.15,45.89,0.15,44.33,0.31,1,True,True
20260717,51.56,-0.13,46.19,0.3,44.61,0.28,2,False,True
20260724,51.13,-0.43,46.05,-0.14,44.61,0,3,False,False
20260731,50.69,-0.44,45.58,-0.47,43.88,-0.73,0,False,False
20260807,50.72,0.03,45.46,-0.12,43.91,0.03,1,False,True
20260814,50.67,-0.05,45.65,0.19,44.22,0.31,2,False,True
20260821,50.77,0.1,45.7,0.05,44.13,-0.09,3,False,True
20260828,56.24,5.47,51.9,6.2,50.63,6.5,4,True,True
20260904,51.28,-4.96,46.1,-5.8,44.95,-5.68,0,False,False
20260911,51.03,-0.25,45.94,-0.16,44.54,-0.41,0,False,False
20260918,51.34,0.31,46.21,0.27,45.04,0.5,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6016 | 康和證 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/15 2.契約或承諾相對人:元大商業銀行、第一商業銀行、全國農業金庫、臺灣土地銀行、 臺灣中小企業銀行、華南商業銀行、樂天國際商業銀行 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:自首次動用日起算至屆滿三年之日止 5.主要內容（解除者不適用）:總額度新台幣陸拾玖億元整 6.限制條款（解除者不適用）:依聯合授信合約辦理 7.承諾事項（解除者不適用）:依聯合授信合約辦理 8.其他重要約定事項（解除者不適用）:依聯合授信合約辦理 9.對公司財務、業務之影響:償還金融機構借款暨充實中期營運週轉金 10.具體目的:償還金融機構借款暨充實中期營運週轉金 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 6016 | 康和證 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/15 2.契約或承諾相對人:元大商業銀行、第一商業銀行、全國農業金庫、臺灣土地銀行、 臺灣中小企業銀行、華南商業銀行、樂天國際商業銀行 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:自首次動用日起算至屆滿三年之日止 5.主要內容（解除者不適用）:總額度新台幣陸拾玖億元整 6.限制條款（解除者不適用）:依聯合授信合約辦理 7.承諾事項（解除者不適用）:依聯合授信合約辦理 8.其他重要約定事項（解除者不適用）:依聯合授信合約辦理 9.對公司財務、業務之影響:償還金融機構借款暨充實中期營運週轉金 10.具體目的:償還金融機構借款暨充實中期營運週轉金 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6016 | 康和證 | 4 | 4 | 4 | 7 | 9 | repeated_but_no_breakout | 近 10 日上榜 7 次、近 20 日上榜 9 次，但尚未有效突破，需等待攻擊確認。 |

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
