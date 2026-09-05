# INDIVIDUAL STOCK CHATGPT PACKET - 2353 宏碁

## Metadata
- generated_at: 2026-09-05 22:15:52 Asia/Taipei
- stock_id: 2353
- stock_name: 宏碁
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
- individual_report_md_exists: True
- sell_strategy_summary_exists: True
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2353_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2353_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2353_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2353_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2353_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2353_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2353_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2353.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2353.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2353.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2353.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2353_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2353_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2353_latest.md?ref=main

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
- open: 31.95
- high: 33.05
- low: 31.95
- close: 32.7
- volume: 40071025
- ma5: 31.87
- ema23_primary: 31.26
- distance_to_ema23_pct: 4.59
- ma20: 31.36
- ma60: 31.73
- ma120: 30.67
- return_5d: 6
- return_20d: 8.1
- volume_ratio: 2.12
- distance_to_ma20_pct_auxiliary: 4.27
- distance_to_high_60_pct: -17.01

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,30.3,31,30,31,20786468,30.36,2.09,29.8,32.49,0.79
20260811,30.9,31.05,30.5,31.05,12528592,30.42,2.06,29.82,32.55,0.51
20260812,31,31.95,30.85,31.75,24980900,30.53,3.99,29.85,32.62,1.06
20260813,32.2,32.5,31.5,31.55,26523495,30.62,3.05,29.89,32.68,1.13
20260814,31.8,33.2,31.8,32.3,59634972,30.76,5.01,30.03,32.76,2.43
20260817,32.5,32.55,30.75,31.45,36593527,30.82,2.06,30.14,32.81,1.46
20260818,31.1,31.1,30.45,30.55,15383939,30.79,-0.79,30.16,32.83,0.62
20260819,30.1,31,30.05,30.9,12354545,30.8,0.32,30.17,32.8,0.51
20260820,31,31.4,30.8,31,12951230,30.82,0.59,30.21,32.79,0.54
20260821,31,31,30.5,30.7,8315197,30.81,-0.35,30.25,32.78,0.35
20260824,30.7,31.6,30.7,31.1,12582129,30.83,0.87,30.3,32.76,0.53
20260825,31.15,31.3,30.7,31.05,6407332,30.85,0.64,30.41,32.69,0.29
20260826,31,31.5,30.9,31.4,8644574,30.9,1.63,30.55,32.57,0.41
20260827,31.35,31.6,31.2,31.2,8344432,30.92,0.9,30.71,32.38,0.41
20260828,31.4,31.45,30.8,30.85,8501451,30.92,-0.21,30.81,32.17,0.45
20260831,30.8,31.5,30.55,31.5,11097480,30.96,1.73,30.95,32.05,0.6
20260901,31.35,31.75,31.2,31.75,13430684,31.03,2.32,31.08,31.93,0.72
20260902,31.5,32.2,31.3,32.15,18102445,31.12,3.3,31.18,31.88,1.02
20260903,32.3,32.7,31.25,31.25,19934079,31.13,0.37,31.24,31.79,1.11
20260904,31.95,33.05,31.95,32.7,40071025,31.26,4.59,31.36,31.73,2.12
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 37.82
- over_600_ratio: 35.84
- over_800_ratio: 34.62
- over_1000_ratio: 33.65
- over_400_change_1w: 0.28
- over_800_change_1w: 0.26
- over_1000_change_1w: 0.24
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,38.98,-1.69,35.96,-1.67,35.06,-1.68,0,False,False
20260626,38.6,-0.38,35.47,-0.49,34.6,-0.46,0,False,False
20260703,38.02,-0.58,34.76,-0.71,33.92,-0.68,0,False,False
20260709,37.89,-0.13,34.71,-0.05,33.88,-0.04,0,False,False
20260717,37.21,-0.68,34.08,-0.63,33.19,-0.69,0,False,False
20260724,36.66,-0.55,33.32,-0.76,32.4,-0.79,0,False,False
20260731,36.3,-0.36,33,-0.32,32.05,-0.35,0,False,False
20260807,36.78,0.48,33.47,0.47,32.53,0.48,1,True,True
20260814,37.27,0.49,34.1,0.63,33.07,0.54,2,True,True
20260821,37.45,0.18,34.33,0.23,33.33,0.26,3,True,True
20260828,37.54,0.09,34.36,0.03,33.41,0.08,4,True,True
20260904,37.82,0.28,34.62,0.26,33.65,0.24,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2353 | 宏碁 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/06/24 2.接受資金貸與之: (1)公司名稱:Acer America Corporation(AAC) (2)與資金貸與他人公司之關係: AAC為AAH 100%持股之孫公司 (3)資金貸與之限額(仟元):37,455,717 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):2,822,580 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:否 (7)迄事實發生日止資金貸與餘額(仟元):2,822,580 (8)本次新增資金貸與之原因: 因應AAC營運需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):7,306,548 (2)累積盈虧金額(仟元):47,670 5.計息方式: 3.85% 6.還款之: (1)條件: 借款期限十二個月 (2)日期: 民國116年5月20日 7.迄事實發生日為止，資金貸與餘額(仟元): 13,560,054 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 18.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2353 | 宏碁 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/06/24 2.接受資金貸與之: (1)公司名稱:Acer America Corporation(AAC) (2)與資金貸與他人公司之關係: AAC為AAH 100%持股之孫公司 (3)資金貸與之限額(仟元):37,455,717 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):2,822,580 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:否 (7)迄事實發生日止資金貸與餘額(仟元):2,822,580 (8)本次新增資金貸與之原因: 因應AAC營運需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):7,306,548 (2)累積盈虧金額(仟元):47,670 5.計息方式: 3.85% 6.還款之: (1)條件: 借款期限十二個月 (2)日期: 民國116年5月20日 7.迄事實發生日為止，資金貸與餘額(仟元): 13,560,054 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 18.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2353 | 宏碁 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/06/24 2.接受資金貸與之: (1)公司名稱:Acer America Corporation(AAC) (2)與資金貸與他人公司之關係: AAC為AAH 100%持股之孫公司 (3)資金貸與之限額(仟元):37,455,717 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):2,822,580 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:否 (7)迄事實發生日止資金貸與餘額(仟元):2,822,580 (8)本次新增資金貸與之原因: 因應AAC營運需求 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):7,306,548 (2)累積盈虧金額(仟元):47,670 5.計息方式: 3.85% 6.還款之: (1)條件: 借款期限十二個月 (2)日期: 民國116年5月20日 7.迄事實發生日為止，資金貸與餘額(仟元): 13,560,054 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 18.62 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2353 | 宏碁 | 13 | 2 | 5 | 10 | 14 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 14 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2353 | 宏碁 | 60 | 6 | 5785840.0 | 6840.0 | 845.88 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
