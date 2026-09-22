# INDIVIDUAL STOCK CHATGPT PACKET - 2033 佳大

## Metadata
- generated_at: 2026-09-20 22:16:00 Asia/Taipei
- stock_id: 2033
- stock_name: 佳大
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2033_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2033_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2033_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2033_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2033_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2033_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2033_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2033.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2033.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2033.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2033.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2033_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2033_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2033_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- model_recommended
- decision_score_high
- price_structure_not_broken
- revenue_not_deteriorating
- no_major_tdcc_warning
- no_major_volume_price_failure

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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260918
- open: 32.45
- high: 33.9
- low: 31.5
- close: 33.9
- volume: 4589786
- ma5: 28.99
- ema23_primary: 25.89
- distance_to_ema23_pct: 30.96
- ma20: 26.16
- ma60: 20.11
- ma120: 17.95
- return_5d: 19.37
- return_20d: 54.09
- volume_ratio: 2.55
- distance_to_ma20_pct_auxiliary: 29.56
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,21.9,22.35,21.4,22,604140,19.43,13.22,18.89,16.79,0.42
20260825,21.95,23.75,21.95,23.75,1109508,19.79,20.01,19.35,16.93,0.77
20260826,23.7,24.25,22.75,23,648626,20.06,14.67,19.75,17.05,0.44
20260827,22.95,23.9,22.9,23.35,785230,20.33,14.84,20.18,17.19,0.52
20260828,23.7,25.65,23.45,25.65,3683348,20.78,23.46,20.7,17.35,2.2
20260831,28,28.2,25.95,26,4341648,21.21,22.58,21.23,17.52,2.3
20260901,24.45,25.45,23.4,23.9,3447898,21.44,11.5,21.63,17.66,1.68
20260902,23.9,24.9,23.85,24.65,736850,21.7,13.58,22.07,17.8,0.35
20260903,24.45,25.55,24.45,25.55,1081739,22.02,16.01,22.52,17.97,0.54
20260904,25.15,26.65,24.45,26.05,1673188,22.36,16.51,22.98,18.14,0.97
20260907,26.1,27.35,25.7,25.7,1215744,22.64,13.53,23.33,18.31,0.72
20260908,25.7,26.3,25,25.45,531067,22.87,11.27,23.57,18.47,0.34
20260909,25.45,27.85,25.45,27.3,1767984,23.24,17.47,23.84,18.66,1.14
20260910,27.3,28.15,27.25,27.6,1191715,23.6,16.93,24.19,18.86,0.77
20260911,29.5,29.5,27.7,28.4,1191652,24,18.31,24.48,19.07,0.8
20260914,28.15,29.9,26,26.65,1949742,24.22,10.01,24.71,19.25,1.31
20260915,26.7,27.05,25.45,25.5,768559,24.33,4.81,24.89,19.4,0.53
20260916,26,28.05,25.8,28.05,1238288,24.64,13.84,25.16,19.59,0.85
20260917,27.95,30.85,27.8,30.85,3407460,25.16,22.62,25.57,19.82,2.15
20260918,32.45,33.9,31.5,33.9,4589786,25.89,30.96,26.16,20.11,2.55
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 78.33
- over_600_ratio: 75.35
- over_800_ratio: 73.66
- over_1000_ratio: 66.76
- over_400_change_1w: 0.14
- over_800_change_1w: -0.34
- over_1000_change_1w: 0.68
- tdcc_consecutive_up_weeks: 6
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,74.21,0.02,69.37,0.63,61.48,0.63,4,True,True
20260709,74.13,-0.08,69.29,-0.08,61.4,-0.08,0,False,False
20260717,74,-0.13,69.16,-0.13,61.27,-0.13,0,False,False
20260724,73.92,-0.08,69.08,-0.08,61.19,-0.08,0,False,False
20260731,73.6,-0.32,69.06,-0.02,62.16,0.97,1,False,True
20260807,73.59,-0.01,69.03,-0.03,62.13,-0.03,0,False,False
20260814,76.57,2.98,69.53,0.5,61.6,-0.53,1,False,True
20260821,76.61,0.04,70.75,1.22,62.78,1.18,2,False,True
20260828,77.38,0.77,71.5,0.75,63.4,0.62,3,True,True
20260904,77.61,0.23,73.46,1.96,65.37,1.97,4,True,True
20260911,78.19,0.58,74,0.54,66.08,0.71,5,True,True
20260918,78.33,0.14,73.66,-0.34,66.76,0.68,6,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2033 | 佳大 | true_breakout | 嚴格突破 | 104.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 土地：台南市安南區科工段(地號0221-0000) 建物：台南市安南區科技一路10號(建號00633-000) 2.事實發生日:115/9/9~115/9/9 3.董事會通過日期: 民國115年9月9日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 1.土地5704.93平方公尺，折合1725.7413坪 2.廠房7672.59平方公尺，折合2320.96坪 3.交易總金額為 405,000,000元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 億曜企業股份有限公司 (非本公司之關係人)。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用。 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用。 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用。 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依雙方簽署之合約規定付款。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 雙方議價。 12.專業估價者事務所或公司名稱及其估價金額: 大華不動產鑑價公司。 1.勘估標的土地總價為270,941,384元(土地單價:157,000元/坪)。 2.勘估標的建物總價為126,694,400元。 3.勘估標的總合計為397,635,784元。 13.專業估價師姓名: 林振興。 14.專業估價師開業證書字號: (100）北市估字第000178號。 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用。 19.會計師事務所名稱: 不適用。 20.會計師姓名: 不適用。 21.會計師開業證書字號: 不適用。 22.經紀人及經紀費用: 不適用。 23.取得或處分之具體目的或用途: 新設半導體清洗事業部營運所需之廠房及土地。 24.本次交易表示異議之董事之意見: 不適用。 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 民國115年9月9日 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 不適用。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 2033 | 佳大 | 2 | 2 | 3 | 5 | 8 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
