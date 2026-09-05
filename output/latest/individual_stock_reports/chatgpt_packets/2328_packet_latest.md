# INDIVIDUAL STOCK CHATGPT PACKET - 2328 廣宇

## Metadata
- generated_at: 2026-09-05 22:15:51 Asia/Taipei
- stock_id: 2328
- stock_name: 廣宇
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2328_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2328_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2328_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2328_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2328_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2328_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2328_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2328.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2328.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2328.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2328.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2328_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2328_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2328_latest.md?ref=main

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
- date: 20260904
- open: 46.3
- high: 46.7
- low: 45.8
- close: 46.6
- volume: 1003854
- ma5: 46.9
- ema23_primary: 46.04
- distance_to_ema23_pct: 1.21
- ma20: 46
- ma60: 47.33
- ma120: 48.42
- return_5d: 0
- return_20d: 3.21
- volume_ratio: 0.44
- distance_to_ma20_pct_auxiliary: 1.3
- distance_to_high_60_pct: -14.5

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,45.45,47.1,45.4,47.05,3203581,45.55,3.3,44.93,50.06,1.08
20260811,47,47,45.65,46.1,1808852,45.59,1.12,44.86,49.98,0.64
20260812,46.1,46.85,46.1,46.5,1647385,45.67,1.82,44.68,49.89,0.61
20260813,46.9,47.85,46.25,46.3,2350931,45.72,1.27,44.53,49.81,0.86
20260814,46.3,46.75,45.3,45.55,2394589,45.71,-0.34,44.49,49.73,0.91
20260817,45.9,46.25,45,45.4,1491687,45.68,-0.61,44.51,49.62,0.58
20260818,45.5,45.55,43.9,43.9,1846796,45.53,-3.58,44.38,49.44,0.72
20260819,43.5,47,43.45,46,7207652,45.57,0.94,44.33,49.26,2.55
20260820,45.7,46.2,44.85,45.6,3062914,45.57,0.06,44.28,49.12,1.06
20260821,45.15,45.45,44.8,44.9,1442496,45.52,-1.36,44.26,48.97,0.5
20260824,44.9,45.5,44.85,44.9,1092532,45.47,-1.24,44.25,48.83,0.39
20260825,45,45,43.9,44.7,1025717,45.4,-1.55,44.35,48.65,0.38
20260826,45,45.6,44.7,45.35,1176022,45.4,-0.1,44.6,48.39,0.47
20260827,45.4,47.8,45.4,46.7,4020637,45.51,2.62,45,48.14,1.58
20260828,47,47.4,46.2,46.6,1584646,45.6,2.2,45.27,47.91,0.64
20260831,46.2,47.1,46.1,46.8,1353486,45.7,2.41,45.48,47.73,0.55
20260901,46.9,48.35,46.9,47.5,2818061,45.85,3.6,45.71,47.58,1.12
20260902,47.55,48.7,47.3,47.8,2814892,46.01,3.89,45.9,47.53,1.09
20260903,48.4,48.55,45.75,45.8,2193699,45.99,-0.42,45.93,47.41,0.87
20260904,46.3,46.7,45.8,46.6,1003854,46.04,1.21,46,47.33,0.44
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 40.95
- over_600_ratio: 39.45
- over_800_ratio: 37.96
- over_1000_ratio: 36.75
- over_400_change_1w: 0.38
- over_800_change_1w: 0.09
- over_1000_change_1w: 0.26
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,41.41,0.02,38.73,0.46,37.74,0.82,1,True,True
20260626,41.46,0.05,38.6,-0.13,37.74,0,2,False,False
20260703,40.39,-1.07,37.66,-0.94,36.62,-1.12,0,False,False
20260709,40.2,-0.19,37.59,-0.07,36.24,-0.38,0,False,False
20260717,40.38,0.18,37.65,0.06,36.45,0.21,1,True,True
20260724,40.41,0.03,37.68,0.03,36.49,0.04,2,True,True
20260731,39.73,-0.68,36.95,-0.73,35.6,-0.89,0,False,False
20260807,40.04,0.31,37.35,0.4,35.78,0.18,1,True,True
20260814,40.43,0.39,37.81,0.46,36.41,0.63,2,True,True
20260821,40.31,-0.12,37.68,-0.13,36.12,-0.29,0,False,False
20260828,40.57,0.26,37.87,0.19,36.49,0.37,1,False,True
20260904,40.95,0.38,37.96,0.09,36.75,0.26,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2328 | 廣宇 | pattern | 型態觀察 | 53.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:自民國115/8/31至民國115/8/31 2.本次新增（減少）投資方式: 本公司透過第三地區投資事業比利時 MAGNAX BV 以現金投資邁格能傳動技術（江蘇）有限公司 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:投審司核准 民國115年8月28日 5.交易單位數量、每單位價格及交易總金額: 交易總金額：歐元9,021,760 元(預計總投資金額) 6.大陸被投資公司之公司名稱: 邁格能傳動技術（江蘇）有限公司 7.前開大陸被投資公司之實收資本額: 歐元800,000 元 8.前開大陸被投資公司本次擬新增資本額: 歐元9,021,760元 9.前開大陸被投資公司主要營業項目: 機械傳動設備製造、產業用機械設備維修及安裝、其他電子零組件製造批發等 10.前開大陸被投資公司最近年度財務報表會計師意見型態: 不適用 11.前開大陸被投資公司最近年度財務報表權益總額: 不適用 12.前開大陸被投資公司最近年度財務報表損益金額: 不適用 13.迄目前為止，對前開大陸被投資公司之實際投資金額: 歐元9,235,040元 14.交易相對人及其與公司之關係: 現金增資不適用；母子公司 15.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉 之所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期及移轉金額: 現金增資；不適用 16.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係人之取得 及處分日期、價格及交易當時與公司之關係: 不適用 17.處分利益（或損失）: 不適用 18.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定事項: 由比利時MAGNAX BV 以現金直接投資邁格能傳動技術（江蘇）有限公司 19.本次交易之決定方式、價格決定之參考依據及決策單位: Magnax BV 董事會 20.經紀人: 無 21.取得或處分之具體目的: 長期投資 22.本次交易表示異議董事之意見: 無 23.本次交易為關係人交易:否 24.監察人承認或審計委員會同意日期: 不適用，第三地直接投資 25.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）: 美金215,251,777.89元 26.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 實收資本額之比率: 132.26% 27.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 總資產之比率: 27.18% 28.迄目前為止，投審會核准赴大陸地區投資總額（含本次投資）占最近期財務報表 歸屬於母公司業主之權益之比率: 46.91% 29.迄目前為止，實際赴大陸地區投資總額: 美金204,439,393.06元 30.迄目前為止，實際赴大陸地區投資總額占最近期財務報表實收資本額之比率: 125.62% 31.迄目前為止，實際赴大陸地區投資總額占最近期財務報表總資產之比率: 25.82% 32.迄目前為止，實際赴大陸地區投資總額占最近期財務報表歸屬於母公司業主之權益之比率: 44.55% 33.最近三年度認列投資大陸損益金額: 112年度：新台幣886,345仟元 113年度：新台幣770,869仟元 114年度：新台幣465,291仟元 34.最近三年度獲利匯回金額: 112年度：新台幣517,097仟元 113年度：新台幣      0仟元 114年度：新台幣987,582仟元 35.本次交易會計師出具非合理性意見:不適用 36.會計師事務所名稱: 不適用 37.會計師姓名: 不適用 38.會計師開業證書字號: 不適用 39.前已就同一件事件發布重大訊息日期: 不適用 40.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2328 | 廣宇 | 1 | 1 | 3 | 6 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2328 | 廣宇 | 34 | 1 | 479410.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
