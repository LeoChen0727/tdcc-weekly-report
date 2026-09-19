# INDIVIDUAL STOCK CHATGPT PACKET - 6451 訊芯-KY

## Metadata
- generated_at: 2026-09-19 22:17:19 Asia/Taipei
- stock_id: 6451
- stock_name: 訊芯-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6451_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6451_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6451_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6451_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6451_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6451_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6451_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6451.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6451.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6451.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6451.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6451_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6451_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6451_latest.md?ref=main

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
- open: 427.5
- high: 443.5
- low: 421
- close: 443.5
- volume: 4028344
- ma5: 419
- ema23_primary: 432.1
- distance_to_ema23_pct: 2.64
- ma20: 436.65
- ma60: 447.17
- ma120: 475.23
- return_5d: 8.3
- return_20d: 6.1
- volume_ratio: 0.82
- distance_to_ma20_pct_auxiliary: 1.57
- distance_to_high_60_pct: -31.35

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,416,423.5,400,400,2696160,430.37,-7.06,410.23,497.18,0.68
20260825,396,426.5,384.5,423,2791721,429.76,-1.57,412.35,494.73,0.71
20260826,423,463.5,420,454.5,6516404,431.82,5.25,417.95,491.85,1.58
20260827,456,471.5,434,452,10343290,433.5,4.27,424.45,488.4,2.35
20260828,456,462.5,441,453.5,5524831,435.17,4.21,430.07,483.89,1.23
20260831,443.5,456,426,456,3770094,436.9,4.37,434.15,480.16,0.84
20260901,453.5,469.5,442,455,5338016,438.41,3.78,437.35,476.64,1.19
20260902,453,500,447.5,500,10313171,443.54,12.73,440.85,474.98,2.09
20260903,505,505,450,450,13899708,444.08,1.33,440.75,472.21,2.7
20260904,455.5,459.5,440.5,449,5030233,444.49,1.01,442.15,470.44,1
20260907,459,477,447,448.5,5514785,444.83,0.83,441.77,469.59,1.08
20260908,457,458,433,435,2689560,444.01,-2.03,441.88,468.48,0.52
20260909,435,451.5,423.5,427,3734080,442.59,-3.52,440.68,466.86,0.71
20260910,427,441,421,425,2689509,441.12,-3.66,440.12,464.79,0.5
20260911,420,420,408,409.5,1880454,438.49,-6.61,439.32,462.57,0.35
20260914,400,428,397,417.5,2234288,436.74,-4.41,437.27,460.18,0.41
20260915,412.5,418.5,393.5,394,2301670,433.18,-9.04,435.93,456.46,0.44
20260916,400.5,427,399.5,421,3127610,432.16,-2.58,436.27,453.54,0.62
20260917,423,442,418,419,4393185,431.07,-2.8,435.38,450.01,0.88
20260918,427.5,443.5,421,443.5,4028344,432.1,2.64,436.65,447.17,0.82
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 64.25
- over_600_ratio: 62.22
- over_800_ratio: 59.72
- over_1000_ratio: 59.72
- over_400_change_1w: -1.32
- over_800_change_1w: -1.03
- over_1000_change_1w: -1.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,70.73,-0.78,66.19,-2.95,64.56,-0.65,0,False,False
20260709,70.56,-0.17,67.62,1.43,64.41,-0.15,1,False,True
20260717,70.87,0.31,66.04,-1.58,63.55,-0.86,2,False,False
20260724,70.56,-0.31,66.32,0.28,64.74,1.19,3,False,True
20260731,69.67,-0.89,65.64,-0.68,62.73,-2.01,0,False,False
20260807,69.69,0.02,62.83,-2.81,62.13,-0.6,1,False,False
20260814,69.74,0.05,64.78,1.95,62.61,0.48,2,False,True
20260821,68.33,-1.41,63.31,-1.47,62.58,-0.03,0,False,False
20260828,68.27,-0.06,62.91,-0.4,62.16,-0.42,1,False,False
20260904,66.01,-2.26,60.96,-1.95,60.96,-1.2,0,False,False
20260911,65.57,-0.44,60.75,-0.21,60.75,-0.21,0,False,False
20260918,64.25,-1.32,59.72,-1.03,59.72,-1.03,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6451 | 訊芯-KY | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | repeated_but_no_breakout | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件，如股息率等）: 訊芯科技(香港)有限公司(以下簡稱：訊芯香港)及 ShunSin Technology (Vietnam) Company Limited (以下簡稱：訊芯越南) 性質：股權 2.事實發生日:115/8/26~115/8/26 3.董事會通過日期: 民國115年8月26日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 訊芯香港：增資美金65,000,000元 訊芯越南：增資美金65,000,000元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之 關係人者，得免揭露其姓名）: 訊芯香港：本公司全資子公司 訊芯越南：本公司全資子公司 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移 轉之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次 移轉日期及移轉金額: 選定關係人為交易對象之原因：參與子公司之現增 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取 得及處分日期、價格及交易當時與公司之關係: 不適用 9.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分債權 如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人之債權 帳面金額: 不適用 10.處分利益（或損失）（取得有價證券者不適用）（原遞延者應列表說明 認列情形）: 不適用 11.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 現金支付 12.本次交易之決定方式、價格決定之參考依據及決策單位: 董事會決議 13.取得或處分有價證券標的公司每股淨值: 不適用 14.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 金額：訊芯香港USD 312,170,000       訊芯越南USD 175,000,000 持股比例：100% 權利受限情形：無 15.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列 之有價證券投資（含本次交易）占公司最近期財務報表中總資產及歸屬 於母公司業主之權益之比例暨最近期財務報表中營運資金數額（註二）: 有價證券投資（含本次交易）占公司(115年Q2個體)財務報表中總資產比例： 訊芯香港 55.75%及訊芯越南 31.25% 有價證券投資（含本次交易）占公司(115年Q2個體) 財務報表中歸屬於母公司業主之權益之比例： 訊芯香港 118.97%及訊芯越南 66.69% 營運資金(115年Q2合併)：4,535,101仟元 16.經紀人及經紀費用: 不適用 17.取得或處分之具體目的或用途: 長期股權投資 18.本次交易表示異議董事之意見: 無 19.本次交易為關係人交易:是 20.監察人承認或審計委員會同意日期: 1.民國 115 年 8 月 26 日 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.是否涉及營運模式變更:否 26.營運模式變更說明: 不適用 27.過去一年及預計未來一年內與交易相對人交易情形: 不適用 28.資金來源: 不適用 29.前已就同一件事件發布重大訊息日期: 不適用 30.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6451 | 訊芯-KY | 1 | 1 | 2 | 5 | 13 | repeated_but_no_breakout | 近 10 日上榜 5 次、近 20 日上榜 13 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6451 | 訊芯-KY | 49 | 2 | 9296380.0 | 203940.0 | 45.58 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
