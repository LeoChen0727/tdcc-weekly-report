# INDIVIDUAL STOCK CHATGPT PACKET - 2371 大同

## Metadata
- generated_at: 2026-09-06 22:16:19 Asia/Taipei
- stock_id: 2371
- stock_name: 大同
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 341
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2371_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2371_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2371_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2371_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2371_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2371_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2371_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2371.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2371.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2371.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2371.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2371_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2371_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2371_latest.md?ref=main

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
- date: 20260904
- open: 27.95
- high: 28.2
- low: 27.3
- close: 28.15
- volume: 7257358
- ma5: 28.13
- ema23_primary: 27.45
- distance_to_ema23_pct: 2.55
- ma20: 27.46
- ma60: 26.98
- ma120: 28.79
- return_5d: -1.23
- return_20d: 8.48
- volume_ratio: 0.69
- distance_to_ma20_pct_auxiliary: 2.51
- distance_to_high_60_pct: -5.85

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,26.1,27.35,25.95,26.8,8792500,26.01,3.04,25.77,27.61,1.06
20260811,26,26.6,24.9,25.95,15969288,26,-0.21,25.7,27.56,1.87
20260812,26.25,26.9,26.15,26.35,9406212,26.03,1.22,25.66,27.52,1.08
20260813,26.5,26.75,26.15,26.25,4760128,26.05,0.76,25.61,27.49,0.55
20260814,26.25,26.6,26.1,26.35,5023803,26.08,1.05,25.63,27.46,0.62
20260817,26.8,27.45,26.45,27.45,11349083,26.19,4.81,25.71,27.44,1.4
20260818,27.3,27.45,26.2,26.75,11658213,26.24,1.95,25.71,27.4,1.39
20260819,26.95,27.25,26.45,27,13666275,26.3,2.66,25.74,27.34,1.57
20260820,27.35,27.65,27.2,27.55,10698325,26.41,4.34,25.8,27.3,1.19
20260821,27.85,27.85,27.35,27.6,6031020,26.5,4.13,25.89,27.27,0.68
20260824,27.8,28.05,27.45,27.45,7303019,26.58,3.26,25.98,27.25,0.81
20260825,27.4,27.7,27.1,27.7,5191999,26.68,3.84,26.12,27.21,0.6
20260826,27.7,27.85,27.35,27.65,7019152,26.76,3.33,26.3,27.17,0.85
20260827,27.95,29.9,27.95,29.2,36297869,26.96,8.3,26.59,27.16,3.77
20260828,29.55,29.55,28.2,28.5,18419762,27.09,5.21,26.8,27.11,1.81
20260831,28.2,28.6,28,28.05,8630372,27.17,3.24,26.94,27.04,0.84
20260901,28.15,29.15,28.15,28.65,9887622,27.29,4.97,27.11,27.01,0.95
20260902,28.65,28.7,28.1,28.2,6156837,27.37,3.04,27.24,27,0.59
20260903,28.3,28.5,27.55,27.6,6720599,27.39,0.78,27.35,26.98,0.64
20260904,27.95,28.2,27.3,28.15,7257358,27.45,2.55,27.46,26.98,0.69
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 47.59
- over_600_ratio: 45.41
- over_800_ratio: 43.99
- over_1000_ratio: 42.8
- over_400_change_1w: -0.43
- over_800_change_1w: -0.66
- over_1000_change_1w: -0.45
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,47.15,-0.14,43.63,0.02,42.3,-0.1,1,False,True
20260626,46.74,-0.41,43.27,-0.36,41.9,-0.4,0,False,False
20260703,46.72,-0.02,43.15,-0.12,41.79,-0.11,0,False,False
20260709,46.85,0.13,43.28,0.13,42.02,0.23,1,True,True
20260717,46.99,0.14,43.29,0.01,42.15,0.13,2,True,True
20260724,46.84,-0.15,43.28,-0.01,42.01,-0.14,0,False,False
20260731,47.07,0.23,43.64,0.36,42.32,0.31,1,True,True
20260807,47.14,0.07,43.76,0.12,42.51,0.19,2,True,True
20260814,47.47,0.33,44.06,0.3,42.91,0.4,3,True,True
20260821,47.5,0.03,44.13,0.07,42.85,-0.06,4,False,True
20260828,48.02,0.52,44.65,0.52,43.25,0.4,5,True,True
20260904,47.59,-0.43,43.99,-0.66,42.8,-0.45,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2371 | 大同 | pattern | 型態觀察 | 54.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 坐落新北市中和區健康段478地號等13筆土地之預售屋 2.事實發生日:115/9/2~115/9/2 3.董事會通過日期: 民國115年9月2日 4.其他核決日期: 不適用 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 一、房地共2戶，總價4,817萬元。 二、車位共2位，總價320萬元。 三、交易總金額5,137萬元(總面積約90.92坪，其中車位約19.28坪) 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 一、余信達、林倍宏。 二、關係人。 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 一、選定關係人為交易對象之原因：一般銷售 二、前次移轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、     前次移轉日期及移轉金額：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 為公司銷售之商品，故不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 董事會決議通過後始簽訂契約，依契約條件付款。 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 一、本次交易決定方式：議價 二、價格決定之參考依據：市場行情 三、決策單位：董事會 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 無 23.取得或處分之具體目的或用途: 一般銷售，獲取利益。 24.本次交易表示異議之董事之意見: 無 25.本次交易為關係人交易:是 26.監察人承認或審計委員會同意日期: 民國115年9月2日 27.本次交易係向關係人取得不動產或其使用權資產:是 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2371 | 大同 | 2 | 2 | 4 | 8 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2371 | 大同 | 48 | 2 | 360370.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
