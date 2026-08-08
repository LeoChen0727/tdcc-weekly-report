# INDIVIDUAL STOCK CHATGPT PACKET - 3209 全科

## Metadata
- generated_at: 2026-08-08 22:27:19 Asia/Taipei
- stock_id: 3209
- stock_name: 全科
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3209_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3209_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3209_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3209_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3209_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3209_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3209_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3209.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3209.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3209.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3209.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3209_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3209_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3209_latest.md?ref=main

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
- high: 60.2
- low: 58.6
- close: 58.7
- volume: 2217610
- ma5: 56.08
- ema23_primary: 57.68
- distance_to_ema23_pct: 1.76
- ma20: 57.13
- ma60: 64.22
- ma120: 53.66
- return_5d: 9.93
- return_20d: 0.34
- volume_ratio: 1.38
- distance_to_ma20_pct_auxiliary: 2.75
- distance_to_high_60_pct: -29.87

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,58.1,59.2,56.6,57.2,1383926,61.78,-7.41,60.48,62.46,0.69
20260709,57.6,60.6,57.3,58.8,1653443,61.53,-4.44,60.17,62.67,0.93
20260713,61.8,62.9,59,59.9,2470430,61.4,-2.44,60.08,62.9,1.45
20260714,60,60.1,57.4,58.6,1484442,61.16,-4.19,59.95,63.1,0.93
20260715,59.6,62.9,59,60.3,2551636,61.09,-1.29,59.9,63.31,1.58
20260716,60.6,60.7,58.5,60,1104394,61,-1.64,59.87,63.5,0.7
20260717,59.2,59.2,55.6,55.9,1855710,60.57,-7.72,59.65,63.62,1.17
20260720,56.7,56.7,53.3,55.5,1831138,60.15,-7.73,59.31,63.72,1.16
20260721,55.5,57.8,55.3,57.3,1565855,59.91,-4.36,59.03,63.84,1.01
20260722,57.5,58,56.7,57.2,1281525,59.69,-4.17,58.8,63.89,0.83
20260723,57.3,58,56.7,58,1108583,59.55,-2.6,58.64,63.97,0.73
20260724,57.4,58.7,57.4,57.9,848512,59.41,-2.54,58.51,64.04,0.56
20260727,57.9,58.2,55.9,57.2,1183529,59.23,-3.42,58.35,64.14,0.79
20260728,56.1,56.1,54.5,55,1482132,58.87,-6.58,58.19,64.19,1.01
20260729,55,55.2,51.4,53.4,2494861,58.42,-8.59,57.9,64.22,1.61
20260730,53,53.7,51.7,52.3,1730809,57.91,-9.68,57.63,64.19,1.11
20260731,54.6,56.6,54.2,55.8,1422063,57.73,-3.35,57.47,64.19,0.92
20260803,55.5,56.5,54.6,55.5,995036,57.55,-3.56,57.23,64.2,0.65
20260804,55.2,58.2,55.1,58.1,1582198,57.59,0.88,57.12,64.25,1.01
20260805,59,60.2,58.6,58.7,2217610,57.68,1.76,57.13,64.22,1.38
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 47.64
- over_600_ratio: 44.12
- over_800_ratio: 40.89
- over_1000_ratio: 38.24
- over_400_change_1w: 0.28
- over_800_change_1w: -0.14
- over_1000_change_1w: 0.22
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,48.65,-0.18,41.87,-0.26,40.76,-0.32,3,False,False
20260529,49.59,0.94,42.22,0.35,41.1,0.34,4,True,True
20260605,48.82,-0.77,41.71,-0.51,40.21,-0.89,0,False,False
20260612,48.71,-0.11,41.93,0.22,39.62,-0.59,1,False,True
20260618,48.54,-0.17,41.34,-0.59,39.01,-0.61,0,False,False
20260626,47.67,-0.87,41,-0.34,37.86,-1.15,0,False,False
20260703,47.6,-0.07,41.12,0.12,39.24,1.38,1,False,True
20260709,47.23,-0.37,40.76,-0.36,38.44,-0.8,0,False,False
20260717,46.77,-0.46,40.51,-0.25,37.81,-0.63,0,False,False
20260724,47.08,0.31,40.52,0.01,37.87,0.06,1,True,True
20260731,47.36,0.28,41.03,0.51,38.02,0.15,2,True,True
20260807,47.64,0.28,40.89,-0.14,38.24,0.22,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3209 | 全科 | revenue_pullback | 營收成長股價回檔 | 57.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/06/22 2.接受資金貸與之: (1)公司名稱:全科科技股份有限公司 (2)與資金貸與他人公司之關係: Alltek Group Corp. 為本公司100% 持有之子公司 (3)資金貸與之限額(仟元):1,919,877 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):658,455 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):658,455 (8)本次新增資金貸與之原因: 借款人之營運需要 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):2,353,912 (2)累積盈虧金額(仟元):1,127,518 5.計息方式: 依雙方協議 6.還款之: (1)條件: 依雙方協議 (2)日期: 依雙方協議 7.迄事實發生日為止，資金貸與餘額(仟元): 7,883,337 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 150.40 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 3209 | 全科 | revenue_breakout_low_response | 營收爆發低反應股 | 20.0 | 3.0 | A_優先追蹤 |  |  | no_signal | stale_signal | 1.事實發生日:115/06/22 2.接受資金貸與之: (1)公司名稱:全科科技股份有限公司 (2)與資金貸與他人公司之關係: Alltek Group Corp. 為本公司100% 持有之子公司 (3)資金貸與之限額(仟元):1,919,877 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):658,455 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):658,455 (8)本次新增資金貸與之原因: 借款人之營運需要 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):2,353,912 (2)累積盈虧金額(仟元):1,127,518 5.計息方式: 依雙方協議 6.還款之: (1)條件: 依雙方協議 (2)日期: 依雙方協議 7.迄事實發生日為止，資金貸與餘額(仟元): 7,883,337 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 150.40 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3209 | 全科 | 6 | 2 | 5 | 8 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3209 | 全科 | 7 | 0 | 337450.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
