# INDIVIDUAL STOCK CHATGPT PACKET - 3048 益登

## Metadata
- generated_at: 2026-08-09 22:27:05 Asia/Taipei
- stock_id: 3048
- stock_name: 益登
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 319
- current_main_price_date: 20260805
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260807-01698d0b1c2355ac
- official_tdcc_signal_date: 20260807
- latest_tdcc_date: 20260807
- tdcc_rows: 15
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3048.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3048.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3048.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3048.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3048_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3048_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3048_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260805
- open: 59
- high: 59.5
- low: 57.2
- close: 58.3
- volume: 15202838
- ma5: 50.78
- ema23_primary: 53.76
- distance_to_ema23_pct: 8.45
- ma20: 52.1
- ma60: 61.7
- ma120: 50.01
- return_5d: 31.9
- return_20d: -3.64
- volume_ratio: 4.1
- distance_to_ma20_pct_auxiliary: 11.89
- distance_to_high_60_pct: -28.82

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,60.5,62.5,58.9,59.5,2932631,65.22,-8.77,67.81,57.94,0.26
20260709,61,61.3,59.6,60,1897212,64.78,-7.38,67.14,58.29,0.21
20260713,60.6,61.6,56.6,57.4,3203977,64.17,-10.55,66.27,58.58,0.41
20260714,57,58,52.2,55.6,3881361,63.45,-12.38,65.39,58.85,0.63
20260715,56.5,57.5,55.2,57.1,2784662,62.92,-9.26,64.58,59.15,0.53
20260716,57,57.2,55.4,55.8,1805815,62.33,-10.48,63.81,59.42,0.38
20260717,52.9,53.7,50.5,50.7,2870790,61.36,-17.38,62.72,59.62,0.62
20260720,51.8,51.8,47.85,49.3,3210843,60.36,-18.32,61.51,59.76,0.76
20260721,49.7,50.5,49.4,50.2,1407753,59.51,-15.65,60.4,59.96,0.36
20260722,50.8,52.2,50.8,50.9,1508179,58.79,-13.42,59.48,60.18,0.42
20260723,51.5,51.8,49.8,50.8,1391461,58.13,-12.6,58.56,60.38,0.41
20260724,50.1,51.5,49.4,50.4,1159547,57.48,-12.32,57.73,60.56,0.36
20260727,50.5,50.9,48.6,49.85,1472102,56.85,-12.31,57.08,60.75,0.49
20260728,48.8,48.8,46.25,46.45,2095644,55.98,-17.02,56.32,60.89,0.7
20260729,47.15,47.15,42.55,44.2,4073864,55,-19.63,55.38,60.98,1.35
20260730,43.9,45.25,42.1,42.75,2173798,53.98,-20.8,54.24,61.03,0.86
20260731,46.8,46.85,45.3,46.25,2108209,53.33,-13.28,53.34,61.11,0.85
20260803,45.5,50.8,45.4,50.8,2812760,53.12,-4.37,52.66,61.26,1.12
20260804,55,55.8,51.7,55.8,16234234,53.35,4.6,52.22,61.48,5.2
20260805,59,59.5,57.2,58.3,15202838,53.76,8.45,52.1,61.7,4.1
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 49.53
- over_600_ratio: 46.25
- over_800_ratio: 44.36
- over_1000_ratio: 43.42
- over_400_change_1w: -1.83
- over_800_change_1w: -2.1
- over_1000_change_1w: -1.46
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,59.18,4.54,54.85,3.57,52.85,3.56,3,True,True
20260529,58.09,-1.09,53.71,-1.14,51.4,-1.45,0,False,False
20260605,52.16,-5.93,48.7,-5.01,46.7,-4.7,0,False,False
20260612,52.97,0.81,49.63,0.93,47.2,0.5,1,True,True
20260618,52.07,-0.9,47.87,-1.76,45.52,-1.68,0,False,False
20260626,52.37,0.3,48.82,0.95,46.85,1.33,1,True,True
20260703,51.25,-1.12,47.2,-1.62,45.88,-0.97,0,False,False
20260709,50.7,-0.55,46.1,-1.1,45.1,-0.78,0,False,False
20260717,50.78,0.08,46.35,0.25,45.35,0.25,1,True,True
20260724,51.32,0.54,46.34,-0.01,45.02,-0.33,2,False,False
20260731,51.36,0.04,46.46,0.12,44.88,-0.14,3,False,True
20260807,49.53,-1.83,44.36,-2.1,43.42,-1.46,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3048 | 益登 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | stale_signal | 1.證券名稱: 蜜望實企業股份有限公司普通股(8043) 2.交易日期:115/7/8~115/7/15 3.董事會通過日期: 民國115年5月13日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量(股):1,983,000  每股平均價格(新台幣元): 160.02 交易總金額(新台幣元):317,321,500 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，不影響本公司當期損益。 7.與交易標的公司之關係: 無。 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 數量：2,119,398股 金額：146,874仟元 持股比例：2.65% 權利受限情形：無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例：3.13%    占母公司業主權益比例：18.91%     營運資金：6,603,994仟元 10.取得或處分之具體目的: 財務投資。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用。 14.監察人承認或審計委員會同意日期: 民國 115年 5月 13日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3048 | 益登 | 2 | 2 | 4 | 9 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3048 | 益登 | 29 | 1 | 468210.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
