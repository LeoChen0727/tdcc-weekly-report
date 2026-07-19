# INDIVIDUAL STOCK CHATGPT PACKET - 2912 統一超

## Metadata
- generated_at: 2026-07-19 22:27:01 Asia/Taipei
- stock_id: 2912
- stock_name: 統一超
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2912_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2912_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2912_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2912_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2912_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2912_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2912_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2912.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2912.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2912.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2912.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2912_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2912_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2912_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 245
- high: 246.5
- low: 240.5
- close: 243
- volume: 5619379
- ma5: 242.9
- ema23_primary: 234.75
- distance_to_ema23_pct: 3.51
- ma20: 232.6
- ma60: 228.03
- ma120: 224.52
- return_5d: 0.83
- return_20d: 6.11
- volume_ratio: 1.52
- distance_to_ma20_pct_auxiliary: 4.47
- distance_to_high_60_pct: -2.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,229,229,223.5,223.5,6802212,226.37,-1.27,224.4,226.3,0.8
20260622,224.5,225.5,221,221,3373046,225.93,-2.18,224.45,226.38,0.4
20260623,221,228,221,227,4448533,226.01,0.44,225.18,226.57,0.55
20260624,227,229,225,225,3823604,225.93,-0.41,225.95,226.65,0.49
20260625,225.5,230.5,225.5,226,4892094,225.94,0.03,226.93,226.69,0.67
20260626,226,227.5,222.5,223,3455022,225.69,-1.19,227.72,226.68,0.52
20260629,225.5,226.5,223.5,224,2538084,225.55,-0.69,228.22,226.68,0.44
20260630,225,225,223,223,2042763,225.34,-1.04,228,226.63,0.39
20260701,223.5,225,221.5,223.5,2501230,225.18,-0.75,227.53,226.57,0.54
20260702,224.5,229.5,224,228.5,3910894,225.46,1.35,227,226.53,0.94
20260703,227,237.5,227,231,3618556,225.92,2.25,226.25,226.57,0.98
20260706,231.5,241,231.5,240,4349150,227.1,5.68,226.65,226.72,1.2
20260707,240,243,239,240,3453101,228.17,5.18,227.55,226.93,0.99
20260708,240,242,239.5,241,2373408,229.24,5.13,228.4,227.19,0.69
20260709,240,244.5,240,241,2936923,230.22,4.68,229.07,227.42,0.86
20260713,240,244,239,239.5,2352106,230.99,3.68,229.6,227.55,0.7
20260714,242,242,238.5,242,2717449,231.91,4.35,230.2,227.68,0.8
20260715,242.5,244.5,241,244.5,3740449,232.96,4.95,231.03,227.8,1.1
20260716,244.5,249,243,245.5,5086551,234,4.91,231.9,227.93,1.43
20260717,245,246.5,240.5,243,5619379,234.75,3.51,232.6,228.03,1.52
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 85.07
- over_600_ratio: 83.45
- over_800_ratio: 81.38
- over_1000_ratio: 80.44
- over_400_change_1w: 0.35
- over_800_change_1w: 0.31
- over_1000_change_1w: 0.23
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,84.6,,80.3,,79.53,,0,False,False
20260508,84.6,0,80.32,0.02,79.54,0.01,1,False,True
20260515,84.44,-0.16,80.36,0.04,79.59,0.05,2,False,True
20260522,84.24,-0.2,80.17,-0.19,79.3,-0.29,0,False,False
20260529,83.1,-1.14,79.11,-1.06,78,-1.3,0,False,False
20260605,84.81,1.71,81.2,2.09,80.45,2.45,1,True,True
20260612,84.48,-0.33,80.84,-0.36,80.2,-0.25,0,False,False
20260618,84.47,-0.01,80.55,-0.29,80.05,-0.15,0,False,False
20260626,84.3,-0.17,80.62,0.07,79.95,-0.1,1,False,True
20260703,84.3,0,80.4,-0.22,79.81,-0.14,0,False,False
20260709,84.72,0.42,81.07,0.67,80.21,0.4,1,True,True
20260717,85.07,0.35,81.38,0.31,80.44,0.23,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2912 | 統一超 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 台中市西屯區潮洋里朝富路116號部份之不動產使用權資產 2.事實發生日:115/6/23~115/6/23 3.董事會通過日期: 民國115年6月23日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 交易單位數量：建物租賃面積約 35 坪 每單位價格:  2026/08/01 ~ 2026/09/30：253,333元/月 (未稅) 2026/10/01 ~ 2026/10/31：253,334元/月 (未稅) 2026/11/01 ~ 2028/06/30：190,000元/月 (未稅) 2028/07/01 ~ 2030/06/30：200,000元/月 (未稅) 2030/07/01 ~ 2032/06/30：210,000元/月 (未稅) 2032/07/01 ~ 2034/06/30：220,000元/月 (未稅) 交易總金額：使用權資產金額18,344,339元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 交易相對人：統一超商股份有限公司 與公司之關係：關係人 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 交易相對人選定關係人之原因：地點符合需求 前次移轉所有人：自然人 前次移轉之所有人與公司及交易相對人間之關係：非關係人 前次移轉日期：於2026年5月15日取得該不動產使用權資產 前次移轉金額：每月租金為460仟元(含稅) 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 0元 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 付款條件：依合約約定 契約限制條款: 無 其他重要約定事項：無 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易決定方式: 依市場行情進行議價 價格決定之參考依據: 依市場行情進行議價 決策單位: 董事會 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 符合業務上整體發展需求，發揮集團最大效益 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 民國 115年 6月 23日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: ex_dividend on 20260730; status=confirmed; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2912 | 統一超 | 11 | 3 | 5 | 10 | 13 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 13 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2912 | 統一超 | 4 | 0 | 2537100.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
