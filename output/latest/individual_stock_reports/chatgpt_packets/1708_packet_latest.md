# INDIVIDUAL STOCK CHATGPT PACKET - 1708 東鹼

## Metadata
- generated_at: 2026-08-22 15:59:34 Asia/Taipei
- stock_id: 1708
- stock_name: 東鹼
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 338
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260821-d1df4c843f691346
- official_tdcc_signal_date: 20260821
- latest_tdcc_date: 20260821
- tdcc_rows: 17
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1708_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1708_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1708_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1708_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1708_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1708_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1708_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1708.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1708.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1708.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1708.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1708_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1708_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1708_latest.md?ref=main

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
- date: 20260821
- open: 50.7
- high: 52.8
- low: 50.3
- close: 51.4
- volume: 9466486
- ma5: 50.18
- ema23_primary: 50.32
- distance_to_ema23_pct: 2.15
- ma20: 49.39
- ma60: 50.34
- ma120: 45.31
- return_5d: 6.64
- return_20d: -2.47
- volume_ratio: 2.92
- distance_to_ma20_pct_auxiliary: 4.07
- distance_to_high_60_pct: -19.94

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,53.5,53.5,50.9,52.5,2262044,53.54,-1.95,55.69,47.32,0.26
20260728,51,51.1,48.5,49.55,4384490,53.21,-6.88,55.47,47.45,0.51
20260729,50.2,50.2,46.5,47.5,5458012,52.73,-9.93,55.18,47.59,0.66
20260730,46.7,47.7,46.1,46.2,3058347,52.19,-11.48,54.9,47.69,0.38
20260731,48.45,49,47.1,48.25,3174675,51.86,-6.96,54.46,47.84,0.44
20260803,47.5,49.2,47.15,48.6,2944332,51.59,-5.79,53.85,48.01,0.51
20260804,48.3,50.4,47.95,49.7,3316969,51.43,-3.37,53.26,48.22,0.64
20260805,50.5,51.1,50,50.1,3120464,51.32,-2.38,52.76,48.39,0.66
20260806,50,50.7,49.35,49.75,1765715,51.19,-2.81,52.25,48.52,0.4
20260807,50.2,50.2,48.65,48.75,2074005,50.99,-4.39,51.74,48.64,0.5
20260810,49.7,50.5,49.15,49.95,2761628,50.9,-1.87,51.45,48.8,0.71
20260811,49.5,49.85,48.8,49.25,1885892,50.76,-2.98,51.09,48.96,0.52
20260812,49.65,50.5,49.2,49.3,2264033,50.64,-2.65,50.72,49.12,0.65
20260813,49.8,50,49.15,49.3,1900708,50.53,-2.43,50.38,49.28,0.56
20260814,49.6,49.6,48.05,48.2,2513522,50.34,-4.24,50.17,49.42,0.8
20260817,48.2,49.7,48.2,48.8,1711710,50.21,-2.8,49.98,49.57,0.58
20260818,49,50.3,48.8,50.1,3299660,50.2,-0.2,49.83,49.75,1.12
20260819,49.5,50.1,48.85,49.8,2136739,50.16,-0.73,49.61,49.92,0.74
20260820,50.4,51.7,49.8,50.8,5348357,50.22,1.16,49.45,50.12,1.84
20260821,50.7,52.8,50.3,51.4,9466486,50.32,2.15,49.39,50.34,2.92
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 39.44
- over_600_ratio: 38.33
- over_800_ratio: 35.33
- over_1000_ratio: 33.47
- over_400_change_1w: -0.13
- over_800_change_1w: -0.34
- over_1000_change_1w: -0.41
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,49.25,2.67,45.04,2.41,42.48,2.05,1,True,True
20260612,45.85,-3.4,41.83,-3.21,39.63,-2.85,0,False,False
20260618,45.66,-0.19,40.8,-1.03,39.71,0.08,1,False,True
20260626,45.42,-0.24,41.59,0.79,39.83,0.12,2,False,True
20260703,44.42,-1,40.2,-1.39,37.75,-2.08,0,False,False
20260709,42.8,-1.62,39.45,-0.75,38.03,0.28,1,False,True
20260717,41.21,-1.59,37.88,-1.57,35.69,-2.34,0,False,False
20260724,40.9,-0.31,37.13,-0.75,34.67,-1.02,0,False,False
20260731,39.94,-0.96,35.92,-1.21,34.45,-0.22,0,False,False
20260807,39.49,-0.45,35.37,-0.55,33.9,-0.55,1,False,False
20260814,39.57,0.08,35.67,0.3,33.88,-0.02,2,False,True
20260821,39.44,-0.13,35.33,-0.34,33.47,-0.41,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1708 | 東鹼 | pullback_rebound | 回檔後短線轉強 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:Sesoda Steamship Corporation (2)與提供背書保證公司之關係: 本公司持股達100%之被投資公司 (3)背書保證之限額(仟元):7,618,391 (4)原背書保證之餘額(仟元):1,290,000 (5)本次新增背書保證之金額(仟元):967,500 (6)迄事實發生日止背書保證餘額(仟元):2,257,500 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之原因: 原短期融資額度續約 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):1,757,883 (2)累積盈虧金額(仟元):4,284,914 5.解除背書保證責任之: (1)條件: 依合約約定 (2)日期: 依合約約定 6.背書保證之總限額(仟元): 38,091,955 7.迄事實發生日為止，背書保證餘額(仟元): 3,148,308 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 41.33 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 107.83 10.其他應敘明事項: 美金匯率: @32.25 最近期財務報告:115年第二季；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |
| 20260821 | 1708 | 東鹼 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:Sesoda Steamship Corporation (2)與提供背書保證公司之關係: 本公司持股達100%之被投資公司 (3)背書保證之限額(仟元):7,618,391 (4)原背書保證之餘額(仟元):1,290,000 (5)本次新增背書保證之金額(仟元):967,500 (6)迄事實發生日止背書保證餘額(仟元):2,257,500 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之原因: 原短期融資額度續約 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):1,757,883 (2)累積盈虧金額(仟元):4,284,914 5.解除背書保證責任之: (1)條件: 依合約約定 (2)日期: 依合約約定 6.背書保證之總限額(仟元): 38,091,955 7.迄事實發生日為止，背書保證餘額(仟元): 3,148,308 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 41.33 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 107.83 10.其他應敘明事項: 美金匯率: @32.25 最近期財務報告:115年第二季；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 1708 | 東鹼 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/08/10 2.被背書保證之: (1)公司名稱:Sesoda Steamship Corporation (2)與提供背書保證公司之關係: 本公司持股達100%之被投資公司 (3)背書保證之限額(仟元):7,618,391 (4)原背書保證之餘額(仟元):1,290,000 (5)本次新增背書保證之金額(仟元):967,500 (6)迄事實發生日止背書保證餘額(仟元):2,257,500 (7)被背書保證公司實際動支金額(仟元):0 (8)本次新增背書保證之原因: 原短期融資額度續約 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):1,757,883 (2)累積盈虧金額(仟元):4,284,914 5.解除背書保證責任之: (1)條件: 依合約約定 (2)日期: 依合約約定 6.背書保證之總限額(仟元): 38,091,955 7.迄事實發生日為止，背書保證餘額(仟元): 3,148,308 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 41.33 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 107.83 10.其他應敘明事項: 美金匯率: @32.25 最近期財務報告:115年第二季；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1708 | 東鹼 | 4 | 4 | 4 | 6 | 9 | repeated_but_no_breakout | 近 10 日上榜 6 次、近 20 日上榜 9 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 1708 | 東鹼 | 35 | 0 | 1983100.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
