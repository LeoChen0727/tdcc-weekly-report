# INDIVIDUAL STOCK CHATGPT PACKET - 2406 國碩

## Metadata
- generated_at: 2026-08-22 22:26:55 Asia/Taipei
- stock_id: 2406
- stock_name: 國碩
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2406_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2406_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2406_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2406_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2406_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2406_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2406_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2406.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2406.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2406.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2406.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2406_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2406_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2406_latest.md?ref=main

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
- date: 20260821
- open: 28.55
- high: 28.8
- low: 28.35
- close: 28.45
- volume: 1856551
- ma5: 28.77
- ema23_primary: 31.02
- distance_to_ema23_pct: -8.28
- ma20: 30.54
- ma60: 34.3
- ma120: 33.72
- return_5d: -2.57
- return_20d: -14.69
- volume_ratio: 0.29
- distance_to_ma20_pct_auxiliary: -6.84
- distance_to_high_60_pct: -38.08

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,33.65,34,32.6,33.25,8501274,35.08,-5.21,36.52,35.03,0.33
20260728,32,32,30.8,30.85,6752607,34.73,-11.16,36.16,35.04,0.27
20260729,31,31.35,27.8,28.75,13052174,34.23,-16.01,35.51,34.97,0.59
20260730,28.1,29.9,27.9,28.35,7121738,33.74,-15.97,34.91,34.9,0.41
20260731,30.4,31.15,30.2,31.15,9103610,33.52,-7.08,34.38,34.88,0.63
20260803,30.55,32,30.4,30.9,7658507,33.3,-7.22,33.87,34.81,0.57
20260804,30.8,31.8,30.8,31.3,4979158,33.14,-5.54,33.36,34.78,0.41
20260805,32.1,33.3,31.35,32.85,12125005,33.11,-0.79,33.05,34.74,1.07
20260806,32.25,32.85,31.65,32.15,6335174,33.03,-2.67,32.7,34.7,0.58
20260807,32.15,32.4,31.35,31.35,3985203,32.89,-4.69,32.35,34.67,0.39
20260810,31.7,32.25,31.55,31.95,3442113,32.81,-2.63,32.09,34.67,0.36
20260811,32.15,32.6,31.75,31.75,5541596,32.73,-2.98,31.93,34.69,0.63
20260812,31.8,32.2,31.6,31.65,4271523,32.64,-3.02,31.77,34.69,0.49
20260813,32.05,32.5,31.5,31.5,6739448,32.54,-3.2,31.64,34.68,0.77
20260814,30.35,30.5,29,29.2,13319126,32.26,-9.49,31.57,34.67,1.53
20260817,29.2,29.8,28.95,29.5,4800766,32.03,-7.91,31.53,34.65,0.57
20260818,29.65,29.65,28.7,28.75,4189618,31.76,-9.47,31.36,34.6,0.51
20260819,28.2,28.65,28,28.55,2916471,31.49,-9.34,31.02,34.51,0.37
20260820,29,29.15,28.45,28.6,2261351,31.25,-8.48,30.79,34.41,0.33
20260821,28.55,28.8,28.35,28.45,1856551,31.02,-8.28,30.54,34.3,0.29
```

## Latest TDCC Snapshot
- as_of_date: 20260821
- over_400_ratio: 25.17
- over_600_ratio: 22.82
- over_800_ratio: 21.35
- over_1000_ratio: 18.48
- over_400_change_1w: -1.56
- over_800_change_1w: -1.34
- over_1000_change_1w: -1.35
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260605,41.17,4.07,36.89,3.6,35.16,4.13,2,True,True
20260612,40.9,-0.27,36.45,-0.44,34.24,-0.92,0,False,False
20260618,38,-2.9,33.47,-2.98,31.47,-2.77,0,False,False
20260626,35.47,-2.53,30.35,-3.12,27.76,-3.71,0,False,False
20260703,37.37,1.9,33.92,3.57,31.08,3.32,1,True,True
20260709,34.17,-3.2,31.42,-2.5,28.64,-2.44,0,False,False
20260717,31.26,-2.91,28.01,-3.41,25.78,-2.86,0,False,False
20260724,29.21,-2.05,25.62,-2.39,23.62,-2.16,0,False,False
20260731,27.32,-1.89,23.88,-1.74,21.32,-2.3,0,False,False
20260807,26.42,-0.9,23.05,-0.83,20.49,-0.83,0,False,False
20260814,26.73,0.31,22.69,-0.36,19.83,-0.66,1,False,False
20260821,25.17,-1.56,21.35,-1.34,18.48,-1.35,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2406 | 國碩 | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | stale_signal | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認本公司114年度虧損撥補案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表:  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)配合子公司禾迅綠電(股)公司未來申請股票上市（櫃）計畫，本公司得辦理對禾迅     綠電(股)公司釋股作業暨放棄參與其現金增資計畫案。  (2)本公司辦理私募普通股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260821 | 2406 | 國碩 | revenue_breakout_low_response | 營收爆發低反應股 | 11 | 50 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認本公司114年度虧損撥補案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表:  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)配合子公司禾迅綠電(股)公司未來申請股票上市（櫃）計畫，本公司得辦理對禾迅     綠電(股)公司釋股作業暨放棄參與其現金增資計畫案。  (2)本公司辦理私募普通股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2406 | 國碩 | 39 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 2406 | 國碩 | 22 | 0 | 8900.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
