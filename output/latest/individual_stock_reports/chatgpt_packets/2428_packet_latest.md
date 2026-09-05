# INDIVIDUAL STOCK CHATGPT PACKET - 2428 興勤

## Metadata
- generated_at: 2026-09-05 22:15:58 Asia/Taipei
- stock_id: 2428
- stock_name: 興勤
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2428_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2428_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2428_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2428_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2428.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2428.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2428.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2428.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2428_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2428_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2428_latest.md?ref=main

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
- date: 20260904
- open: 250
- high: 263
- low: 250
- close: 260
- volume: 2467223
- ma5: 252.6
- ema23_primary: 251.98
- distance_to_ema23_pct: 3.18
- ma20: 252.15
- ma60: 268.22
- ma120: 234.05
- return_5d: -0.76
- return_20d: 15.81
- volume_ratio: 1.3
- distance_to_ma20_pct_auxiliary: 3.11
- distance_to_high_60_pct: -28.47

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,229,231.5,228.5,229,351146,245.01,-6.54,241.82,269.69,0.36
20260811,230,238,228,231.5,727310,243.89,-5.08,238.85,270.12,0.8
20260812,245,254.5,242.5,254.5,2289406,244.77,3.97,236.82,270.83,2.37
20260813,255,266,255,259.5,5513682,246,5.49,235.35,271.59,4.62
20260814,260,260,252,255,1739247,246.75,3.34,234.9,272.12,1.45
20260817,254,256,250,254.5,916609,247.4,2.87,235.12,272.53,0.78
20260818,254.5,258,252,252,1008248,247.78,1.7,235.1,272.69,0.86
20260819,248,262.5,247,256.5,1967772,248.51,3.22,235.07,272.92,1.62
20260820,259,281.5,253,267,5192499,250.05,6.78,235.9,273.1,3.62
20260821,264,269,253,253.5,2293535,250.33,1.26,236.53,272.89,1.5
20260824,253.5,258,250.5,250.5,668910,250.35,0.06,237.05,272.19,0.44
20260825,249,250,243.5,249.5,693657,250.28,-0.31,238.72,271.48,0.46
20260826,252.5,253.5,246.5,252,1784744,250.42,0.63,240.88,270.97,1.16
20260827,248.5,254.5,246,253,1510687,250.64,0.94,243.57,270.57,0.97
20260828,256.5,265.5,253.5,262,3339298,251.58,4.14,245.75,270.43,2
20260831,260,266,250,252,2329729,251.62,0.15,247.15,270.21,1.34
20260901,253.5,259,253.5,256,910750,251.98,1.59,248.65,269.76,0.52
20260902,254,256,250,250.5,1282277,251.86,-0.54,249.75,269.39,0.72
20260903,250.5,253,244.5,244.5,1098757,251.25,-2.69,250.38,268.65,0.61
20260904,250,263,250,260,2467223,251.98,3.18,252.15,268.22,1.3
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 59.37
- over_600_ratio: 56.71
- over_800_ratio: 54.49
- over_1000_ratio: 51.77
- over_400_change_1w: -1.34
- over_800_change_1w: 0.6
- over_1000_change_1w: -0.03
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,64.48,0.67,56.48,-0.12,52.45,0.54,2,False,True
20260626,64.15,-0.33,56.05,-0.43,52.55,0.1,3,False,True
20260703,64.33,0.18,55.57,-0.48,52.83,0.28,4,False,True
20260709,64.22,-0.11,55.01,-0.56,50.83,-2,0,False,False
20260717,64.23,0.01,55.04,0.03,50.79,-0.04,1,False,True
20260724,65.28,1.05,54.34,-0.7,50.9,0.11,2,False,True
20260731,65.24,-0.04,55.91,1.57,51.86,0.96,3,False,True
20260807,65.02,-0.22,54.58,-1.33,51.85,-0.01,0,False,False
20260814,62.83,-2.19,53.63,-0.95,50.9,-0.95,0,False,False
20260821,62.25,-0.58,54.83,1.2,52.74,1.84,1,False,True
20260828,60.71,-1.54,53.89,-0.94,51.8,-0.94,0,False,False
20260904,59.37,-1.34,54.49,0.6,51.77,-0.03,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2428 | 興勤 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_strong_inflow | continued_2_3d | 1.證券名稱: 摩根士丹利數字經濟混合型證券投資基金C 2.交易日期:115/7/3~115/7/9 3.董事會通過日期: 民國115年7月9日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量：8,944,365.00單位；每單位價格：人民幣4.5358元； 交易數量：6,705,073.00單位；每單位價格：人民幣4.6382元； 交易總金額：人民幣71,669仟元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益人民幣8,664仟元 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占母公司最近期個體財務報表中總資產之比例：1.12％ 占最近期合併財務報表歸屬於母公司業主之權益之比例：1.48％ 母公司最近期個體財務報表中營運資金數額：新台幣992,843仟元 10.取得或處分之具體目的: 投資理財 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 該基金尚未結算，公告資料之單位價格依115年7月9日 最新估計價格人民幣4.6382元計算。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2428 | 興勤 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_strong_inflow | continued_2_3d | 1.證券名稱: 摩根士丹利數字經濟混合型證券投資基金C 2.交易日期:115/7/3~115/7/9 3.董事會通過日期: 民國115年7月9日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量：8,944,365.00單位；每單位價格：人民幣4.5358元； 交易數量：6,705,073.00單位；每單位價格：人民幣4.6382元； 交易總金額：人民幣71,669仟元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益人民幣8,664仟元 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占母公司最近期個體財務報表中總資產之比例：1.12％ 占最近期合併財務報表歸屬於母公司業主之權益之比例：1.48％ 母公司最近期個體財務報表中營運資金數額：新台幣992,843仟元 10.取得或處分之具體目的: 投資理財 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 該基金尚未結算，公告資料之單位價格依115年7月9日 最新估計價格人民幣4.6382元計算。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2428 | 興勤 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 67.0 |  |  | neckline_challenge |  | call_strong_inflow | continued_2_3d | 1.證券名稱: 摩根士丹利數字經濟混合型證券投資基金C 2.交易日期:115/7/3~115/7/9 3.董事會通過日期: 民國115年7月9日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量：8,944,365.00單位；每單位價格：人民幣4.5358元； 交易數量：6,705,073.00單位；每單位價格：人民幣4.6382元； 交易總金額：人民幣71,669仟元 6.處分利益（或損失）（取得有價證券者不適用）: 處分利益人民幣8,664仟元 7.與交易標的公司之關係: 無 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 無 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占母公司最近期個體財務報表中總資產之比例：1.12％ 占最近期合併財務報表歸屬於母公司業主之權益之比例：1.48％ 母公司最近期個體財務報表中營運資金數額：新台幣992,843仟元 10.取得或處分之具體目的: 投資理財 11.本次交易表示異議董事之意見: 不適用 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用 14.監察人承認或審計委員會同意日期: 不適用 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 該基金尚未結算，公告資料之單位價格依115年7月9日 最新估計價格人民幣4.6382元計算。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2428 | 興勤 | 3 | 2 | 4 | 8 | 14 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2428 | 興勤 | 54 | 0 | 6054140.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
