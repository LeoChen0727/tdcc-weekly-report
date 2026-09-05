# INDIVIDUAL STOCK CHATGPT PACKET - 4551 智伸科

## Metadata
- generated_at: 2026-09-05 15:53:38 Asia/Taipei
- stock_id: 4551
- stock_name: 智伸科
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4551_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4551_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4551_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4551_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4551_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4551_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4551_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4551.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4551.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4551.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4551.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4551_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4551_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4551_latest.md?ref=main

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
- open: 165
- high: 173
- low: 164
- close: 171.5
- volume: 2021752
- ma5: 165.1
- ema23_primary: 166.77
- distance_to_ema23_pct: 2.83
- ma20: 164.03
- ma60: 188.46
- ma120: 164.07
- return_5d: 5.86
- return_20d: 2.39
- volume_ratio: 1.49
- distance_to_ma20_pct_auxiliary: 4.56
- distance_to_high_60_pct: -41.17

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,169.5,174,163.5,174,1011671,179.96,-3.31,176.62,184.1,0.95
20260811,171,171,157,157,2810382,178.04,-11.82,174.07,184.2,2.6
20260812,157.5,172.5,157,172.5,1652649,177.58,-2.86,172.62,184.65,1.51
20260813,174,182,174,174,3294831,177.28,-1.85,171.43,185.12,2.7
20260814,176,176,160.5,162,2594189,176.01,-7.96,170.12,185.34,2
20260817,163,173,162,170.5,1646015,175.55,-2.88,169.68,185.54,1.26
20260818,170.5,173.5,163,163.5,811164,174.55,-6.33,168.72,185.68,0.62
20260819,160.5,164,158,161,875837,173.42,-7.16,167.68,185.74,0.67
20260820,163.5,163.5,159,162,342678,172.47,-6.07,166.38,185.84,0.28
20260821,162,163.5,157,157.5,424131,171.22,-8.01,165.05,185.94,0.35
20260824,156.5,158,153,154,490806,169.78,-9.3,163.65,185.93,0.42
20260825,153,155,149,155,504443,168.55,-8.04,163.05,185.92,0.43
20260826,155,162,154.5,160,512821,167.84,-4.67,163.03,186.03,0.46
20260827,160,173,159.5,170,2138813,168.02,1.18,164.1,186.32,1.82
20260828,172,172.5,162,162,1581599,167.52,-3.29,164.05,186.49,1.27
20260831,164.5,168.5,158,159.5,985562,166.85,-4.41,164.03,186.73,0.79
20260901,162,173,161,167.5,1736135,166.9,0.36,164.25,187.17,1.32
20260902,166,169,163.5,166,796657,166.83,-0.5,164.28,187.61,0.6
20260903,168,169,161,161,831133,166.34,-3.21,163.82,187.89,0.63
20260904,165,173,164,171.5,2021752,166.77,2.83,164.03,188.46,1.49
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 79.17
- over_600_ratio: 74.39
- over_800_ratio: 73.09
- over_1000_ratio: 71.56
- over_400_change_1w: -0.21
- over_800_change_1w: -0.15
- over_1000_change_1w: 0.69
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,81.28,2.08,76.44,1.12,74.22,1.22,3,True,True
20260626,82.61,1.33,79.91,3.47,78.33,4.11,4,True,True
20260703,82.48,-0.13,78.94,-0.97,76.54,-1.79,5,False,False
20260709,82.73,0.25,79.36,0.42,77.04,0.5,6,False,True
20260717,83.05,0.32,79.23,-0.13,77.73,0.69,7,False,True
20260724,81.36,-1.69,77.96,-1.27,75.65,-2.08,0,False,False
20260731,82.79,1.43,78.88,0.92,77.3,1.65,1,True,True
20260807,81.78,-1.01,78.11,-0.77,75.72,-1.58,0,False,False
20260814,79.93,-1.85,73.79,-4.32,72.27,-3.45,0,False,False
20260821,79.47,-0.46,73.42,-0.37,71.13,-1.14,1,False,False
20260828,79.38,-0.09,73.24,-0.18,70.87,-0.26,0,False,False
20260904,79.17,-0.21,73.09,-0.15,71.56,0.69,1,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4551 | 智伸科 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:GLOBAL ADVANCE TECHNOLOGY LIMITED (2)與提供背書保證公司之關係: 100%間接投資之子公司。 (3)背書保證之限額(仟元):14,807,726 (4)原背書保證之餘額(仟元):3,166,380 (5)本次新增背書保證之金額(仟元):1,453,950 (6)迄事實發生日止背書保證餘額(仟元):4,620,330 (7)被背書保證公司實際動支金額(仟元):1,091,361 (8)本次新增背書保證之原因: 協助該子公司取得銀行授信額度 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,964,584 (2)累積盈虧金額(仟元):2,011,754 5.解除背書保證責任之: (1)條件: 合約到期日 (2)日期: 依合約規定 6.背書保證之總限額(仟元): 18,509,658 7.迄事實發生日為止，背書保證餘額(仟元): 4,684,950 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 50.62 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 88.37 10.其他應敘明事項: 1.最近期財務報表係115年第2季財報 2.匯率以115.07.31台灣銀行美金對台幣中間價32.31為準；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 4551 | 智伸科 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:GLOBAL ADVANCE TECHNOLOGY LIMITED (2)與提供背書保證公司之關係: 100%間接投資之子公司。 (3)背書保證之限額(仟元):14,807,726 (4)原背書保證之餘額(仟元):3,166,380 (5)本次新增背書保證之金額(仟元):1,453,950 (6)迄事實發生日止背書保證餘額(仟元):4,620,330 (7)被背書保證公司實際動支金額(仟元):1,091,361 (8)本次新增背書保證之原因: 協助該子公司取得銀行授信額度 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,964,584 (2)累積盈虧金額(仟元):2,011,754 5.解除背書保證責任之: (1)條件: 合約到期日 (2)日期: 依合約規定 6.背書保證之總限額(仟元): 18,509,658 7.迄事實發生日為止，背書保證餘額(仟元): 4,684,950 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 50.62 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 88.37 10.其他應敘明事項: 1.最近期財務報表係115年第2季財報 2.匯率以115.07.31台灣銀行美金對台幣中間價32.31為準；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 4551 | 智伸科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:GLOBAL ADVANCE TECHNOLOGY LIMITED (2)與提供背書保證公司之關係: 100%間接投資之子公司。 (3)背書保證之限額(仟元):14,807,726 (4)原背書保證之餘額(仟元):3,166,380 (5)本次新增背書保證之金額(仟元):1,453,950 (6)迄事實發生日止背書保證餘額(仟元):4,620,330 (7)被背書保證公司實際動支金額(仟元):1,091,361 (8)本次新增背書保證之原因: 協助該子公司取得銀行授信額度 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,964,584 (2)累積盈虧金額(仟元):2,011,754 5.解除背書保證責任之: (1)條件: 合約到期日 (2)日期: 依合約規定 6.背書保證之總限額(仟元): 18,509,658 7.迄事實發生日為止，背書保證餘額(仟元): 4,684,950 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 50.62 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 88.37 10.其他應敘明事項: 1.最近期財務報表係115年第2季財報 2.匯率以115.07.31台灣銀行美金對台幣中間價32.31為準；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4551 | 智伸科 | 1 | 1 | 2 | 3 | 7 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4551 | 智伸科 | 33 | 0 | 3771820.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
