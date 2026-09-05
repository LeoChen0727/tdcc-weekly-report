# INDIVIDUAL STOCK CHATGPT PACKET - 6016 康和證

## Metadata
- generated_at: 2026-09-05 15:53:58 Asia/Taipei
- stock_id: 6016
- stock_name: 康和證
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
- action_summary_zh: 型態觀察 目前屬於「初步突破」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「初步突破」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: breakout_initial
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
- date: 20260904
- open: 21.8
- high: 22.4
- low: 21.55
- close: 22.4
- volume: 6421000
- ma5: 21.5
- ema23_primary: 20.92
- distance_to_ema23_pct: 7.08
- ma20: 20.11
- ma60: 23.67
- ma120: 22.51
- return_5d: 4.92
- return_20d: 13.13
- volume_ratio: 1.49
- distance_to_ma20_pct_auxiliary: 11.42
- distance_to_high_60_pct: -27.04

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,18.65,19.05,18.35,18.4,12507000,22.35,-17.67,22.18,25.99,2.1
20260811,18.2,18.7,18,18.65,2888000,22.04,-15.39,21.84,25.93,0.51
20260812,18.7,20.1,18.7,19.85,6959000,21.86,-9.19,21.55,25.9,1.19
20260813,20.1,20.6,19.85,20.1,4538000,21.71,-7.43,21.28,25.87,0.77
20260814,20.2,20.75,20.05,20.15,4818000,21.58,-6.64,21.09,25.84,0.84
20260817,20.15,20.15,19.75,19.8,3148000,21.43,-7.62,20.88,25.8,0.56
20260818,19.8,19.9,19.25,19.4,2576000,21.26,-8.77,20.63,25.74,0.46
20260819,19.2,19.25,19,19.15,1422000,21.09,-9.19,20.35,25.67,0.26
20260820,19.2,19.4,19,19.35,2228000,20.94,-7.61,20.09,25.59,0.43
20260821,19.35,19.75,19.3,19.6,1733000,20.83,-5.91,19.84,25.47,0.36
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
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 51.28
- over_600_ratio: 48.12
- over_800_ratio: 46.1
- over_1000_ratio: 44.95
- over_400_change_1w: -4.96
- over_800_change_1w: -5.8
- over_1000_change_1w: -5.68
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,52.65,-1.11,47.26,-0.86,45.72,-1.22,0,False,False
20260626,51.54,-1.11,45.91,-1.35,44.48,-1.24,0,False,False
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
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6016 | 康和證 | pattern | 型態觀察 | 49.0 |  |  | platform_right_side |  |  | continued_2_3d | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 康和期貨普通股 2.事實發生日:115/7/9~115/7/9 3.董事會通過日期: 民國115年7月9日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 依持股比例認購康和期貨 交易數量：預計普通股15,935仟股 每單位價格：暫訂新台幣20元 交易總金額：預計新台幣318,700仟元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 交易相對人：康和期貨(股)公司 其與公司之關係：為本公司95.71%持有之子公司 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 康和期貨為本公司持股95.71%之子公司， 此次現金增資，本公司依持股比例認購， 認股期間過後，如有原股東及員工放棄認購之部分，本公司得參與認購。 前次移轉日期及移轉金額：不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 交付或付款條件：於康和期貨取得主管機關核准後，辦理認購事宜。 契約限制條款及其他重要約定事項：無。 12.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易係以現金增資方式認購 價格決定之參考依據：以康和期貨115年5月31日每股淨值19.54元作為 參考依據，暫訂每股價格20元。 決策單位：董事會 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 含本次交易後，本公司持有康和期貨子公司 累計持有股數 : 預計93,941仟股 累計投資金額 : 預計878,354仟元 持股比例 : 預計93.94% 權利受限情形：無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 總資產比例：83.75% 股東權益比例：329.74% 營運資金數額：6,365,764仟元 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 增進期貨業務發展。 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:是 20.監察人承認或審計委員會同意日期: 民國115年7月7日 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 無 28.資金來源: 公司自有資金 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6016 | 康和證 | 2 | 1 | 3 | 4 | 6 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
