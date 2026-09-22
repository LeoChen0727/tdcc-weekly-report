# INDIVIDUAL STOCK CHATGPT PACKET - 3045 台灣大

## Metadata
- generated_at: 2026-09-20 22:16:37 Asia/Taipei
- stock_id: 3045
- stock_name: 台灣大
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
- tdcc_rows: 43
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3045_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3045_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3045_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3045_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3045_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3045_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3045_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3045.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3045.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3045.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3045.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3045_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3045_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3045_latest.md?ref=main

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
- date: 20260918
- open: 124.5
- high: 125.5
- low: 123
- close: 124
- volume: 18171327
- ma5: 123.6
- ema23_primary: 118.83
- distance_to_ema23_pct: 4.35
- ma20: 118.7
- ma60: 114.68
- ma120: 114
- return_5d: 2.48
- return_20d: 7.83
- volume_ratio: 2.22
- distance_to_ma20_pct_auxiliary: 4.46
- distance_to_high_60_pct: -1.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,115,115,114,115,9496643,112.3,2.4,111.8,114.24,0.76
20260825,115,115.5,114.5,115.5,8753438,112.57,2.61,111.88,114.31,0.71
20260826,115,115.5,114.5,115.5,9525190,112.81,2.38,111.97,114.33,0.79
20260827,116,116,115,115.5,7773618,113.03,2.18,112.05,114.33,0.66
20260828,115.5,115.5,114.5,115.5,8414134,113.24,2,112.2,114.33,0.75
20260831,115,116,114.5,116,9272070,113.47,2.23,112.4,114.33,0.83
20260901,115,116,113.5,115.5,12275130,113.64,1.64,112.62,114.32,1.09
20260902,115.5,116,114.5,116,5665186,113.84,1.9,112.9,114.33,0.5
20260903,116,118,115.5,118,13130153,114.18,3.34,113.28,114.35,1.13
20260904,117.5,118,116.5,118,5076578,114.5,3.06,113.6,114.35,0.44
20260907,118,118,116.5,117,4447140,114.71,2,113.92,114.32,0.39
20260908,116.5,118,116.5,118,4457218,114.98,2.62,114.35,114.29,0.41
20260909,117.5,119.5,117,119.5,8127829,115.36,3.59,114.85,114.29,0.75
20260910,119,120,119,120,4119530,115.75,3.67,115.42,114.28,0.4
20260911,119,121,119,121,5785236,116.18,4.14,116.08,114.32,0.57
20260914,120.5,121.5,120,121.5,4598994,116.63,4.18,116.6,114.36,0.49
20260915,121.5,124.5,121,124,10604689,117.24,5.76,117.25,114.45,1.12
20260916,124,124.5,122.5,124.5,8257070,117.85,5.65,117.8,114.54,0.96
20260917,124.5,124.5,122.5,124,5985415,118.36,4.77,118.25,114.62,0.75
20260918,124.5,125.5,123,124,18171327,118.83,4.35,118.7,114.68,2.22
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 92.96
- over_600_ratio: 92.02
- over_800_ratio: 91.34
- over_1000_ratio: 90.36
- over_400_change_1w: 0.17
- over_800_change_1w: 0.2
- over_1000_change_1w: 0.12
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,92.81,0.15,91.25,0.15,90.49,0.11,5,True,True
20260709,92.62,-0.19,91.09,-0.16,90.35,-0.14,0,False,False
20260717,92.3,-0.32,90.75,-0.34,89.98,-0.37,0,False,False
20260724,92.44,0.14,90.91,0.16,90.14,0.16,1,True,True
20260731,92.61,0.17,91.01,0.1,90.24,0.1,2,True,True
20260807,92.32,-0.29,90.72,-0.29,90,-0.24,0,False,False
20260814,91.91,-0.41,90.14,-0.58,89.49,-0.51,0,False,False
20260821,92.27,0.36,90.56,0.42,89.76,0.27,1,True,True
20260828,92.51,0.24,90.82,0.26,90.07,0.31,2,True,True
20260904,92.67,0.16,90.97,0.15,90.09,0.02,3,True,True
20260911,92.79,0.12,91.14,0.17,90.24,0.15,4,True,True
20260918,92.96,0.17,91.34,0.2,90.36,0.12,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3045 | 台灣大 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 南投市中興路6*6號2樓部分房屋及屋頂層部分 2.事實發生日:115/9/15~115/9/15 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事會授權董事長先行決行，事後提報最近期董事會追認 民國115年9月15日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 交易單位數量：16.91坪 每單位價格：每坪租金每個月347元(含稅) 租金總金額：每個月5,859元(含稅) 使用權資產金額：195,591元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 台灣固網股份有限公司，子公司 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 選定關係人為交易對象之原因：考量關係人房舍資產位置及客戶使用電信服務之需求， 為該區域最適建設位置 前次移轉之所有人：富邦產物保險(股)公司 前次移轉之所有人與公司及交易相對人間相互之關係：關係人 前次移轉日期及移轉金額：115/12/1~118/11/30，每個月租金11,800元 本公司向富邦產物保險股份有限公司承租34.0坪再轉租16.91坪予台灣固網(股)公司 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 關係人之取得日期及價格： 富邦產物保險股份有限公司76/9/12以新台幣8,085,032元自地自建 交易當時與公司之關係：關係人 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 0 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交付或付款條件：月收 租期：115/12/1~118/11/30 契約限制條款及其他重要約定：無 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 董事長授權經理部門依內部管理辦法規定辦理 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 無 23.取得或處分之具體目的或用途: 轉租予台灣固網，以擴展其固定網路涵蓋範圍，佈放光纜及建設傳輸設備， 提供消費者穩定、快速、優質的電信服務 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 俟民國115年11月11日審計委員會同意 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 嗣後租金有變動之可能；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3045 | 台灣大 | 19 | 1 | 5 | 10 | 19 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 19 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3045 | 台灣大 | 1 | 0 | 0.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
