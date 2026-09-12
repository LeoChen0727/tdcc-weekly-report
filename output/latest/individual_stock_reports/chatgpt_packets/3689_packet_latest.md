# INDIVIDUAL STOCK CHATGPT PACKET - 3689 湧德

## Metadata
- generated_at: 2026-09-12 15:43:31 Asia/Taipei
- stock_id: 3689
- stock_name: 湧德
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3689_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3689_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3689_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3689_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3689.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3689.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3689.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3689.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3689_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3689_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3689_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
- take_profit_near_prior_high
- take_profit_on_volume_price_failure
- exit_if_lost_23ema
- exit_if_lost_recent_low
- exit_if_revenue_breaks
- exit_if_tdcc_and_price_both_weaken

### entry_prerequisites
- model_recommended
- decision_score_high
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
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
- tdcc_distribution_warning

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260911
- open: 108
- high: 109
- low: 106
- close: 108.5
- volume: 1149000
- ma5: 110.9
- ema23_primary: 111.72
- distance_to_ema23_pct: -2.88
- ma20: 111.5
- ma60: 112.49
- ma120: 119.45
- return_5d: -6.87
- return_20d: -0.91
- volume_ratio: 0.95
- distance_to_ma20_pct_auxiliary: -2.69
- distance_to_high_60_pct: -16.86

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,110,110.5,109,109.5,402000,109.71,-0.19,107.19,117.5,0.36
20260818,109,109.5,107,107,732000,109.48,-2.27,107.06,117.22,0.65
20260819,105,107.5,104.5,106.5,615000,109.23,-2.5,106.84,116.91,0.55
20260820,108.5,108.5,105.5,106.5,518000,109.01,-2.3,106.67,116.61,0.46
20260821,106.5,107,105.5,106.5,340000,108.8,-2.11,106.59,116.21,0.31
20260824,106.5,108,106.5,107.5,386000,108.69,-1.09,106.47,115.81,0.35
20260825,107.5,107.5,104.5,106,722000,108.46,-2.27,106.59,115.27,0.68
20260826,106.5,109,106.5,108,576000,108.43,-0.39,107.03,114.78,0.59
20260827,109,117,109,115.5,2590000,109.02,5.95,108.03,114.44,2.49
20260828,116.5,120,115,116.5,2972000,109.64,6.26,108.6,114.01,2.63
20260831,115,119,114.5,118.5,1601000,110.38,7.36,109.45,113.64,1.38
20260901,119,121,116.5,118,1698000,111.01,6.29,110.17,113.25,1.39
20260902,118,120.5,117.5,118.5,1442000,111.64,6.15,110.72,113.1,1.15
20260903,122.5,124,114.5,114.5,3809000,111.88,2.35,110.92,112.97,2.9
20260904,117,118,114,116.5,993000,112.26,3.78,111.38,113,0.79
20260907,114,114,112,113,1564000,112.32,0.6,111.5,112.99,1.23
20260908,113,113,110,110.5,991000,112.17,-1.49,111.53,112.9,0.78
20260909,110,112.5,110,112.5,508000,112.2,0.27,111.62,112.78,0.41
20260910,112.5,112.5,110,110,457000,112.01,-1.8,111.55,112.66,0.38
20260911,108,109,106,108.5,1149000,111.72,-2.88,111.5,112.49,0.95
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 25.44
- over_600_ratio: 20.22
- over_800_ratio: 18.1
- over_1000_ratio: 14.1
- over_400_change_1w: -0.33
- over_800_change_1w: -0.03
- over_1000_change_1w: -0.02
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,27.98,0.53,20.12,1.51,14.03,-1.48,1,False,True
20260703,30.76,2.78,21.57,1.45,14.51,0.48,2,True,True
20260709,30.52,-0.24,21.1,-0.47,17.09,2.58,3,False,True
20260717,29.32,-1.2,20.06,-1.04,16.96,-0.13,0,False,False
20260724,28.81,-0.51,19.62,-0.44,16.52,-0.44,1,False,False
20260731,26.74,-2.07,18.24,-1.38,14.04,-2.48,2,False,False
20260807,26.15,-0.59,17,-1.24,12.86,-1.18,0,False,False
20260814,25.7,-0.45,17.03,0.03,12.85,-0.01,1,False,True
20260821,25.94,0.24,18.13,1.1,12.85,0,2,False,True
20260828,26.55,0.61,19.01,0.88,12.85,0,3,False,True
20260904,25.77,-0.78,18.13,-0.88,14.12,1.27,4,False,True
20260911,25.44,-0.33,18.1,-0.03,14.1,-0.02,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3689 | 湧德 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/08/26 2.被背書保證之: (1)公司名稱:U.D.ELECTRONIC VIETNAM COMPANY (2)與提供背書保證公司之關係: 湧德電子股份有限公司對湧德電子股份有限公司持股 100%直接投資之越南湧德有限公司背書保證 (3)背書保證之限額(仟元):4,976,334 (4)原背書保證之餘額(仟元):484,650 (5)本次新增背書保證之金額(仟元):646,200 (6)迄事實發生日止背書保證餘額(仟元):1,130,850 (7)被背書保證公司實際動支金額(仟元):480,050 (8)本次新增背書保證之原因: 融資背書保證。 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):323,100 (2)累積盈虧金額(仟元):-6,237,666,814 5.解除背書保證責任之: (1)條件: 合約終止日。 (2)日期: 合約終止日。 6.背書保證之總限額(仟元): 4,976,334 7.迄事實發生日為止，背書保證餘額(仟元): 4,226,996 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 84.94 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 20.92 10.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260911 | 3689 | 湧德 | revenue_breakout_low_response | 營收爆發低反應股 | 16 | 12 | A_優先追蹤 |  |  |  | stale_signal | 1.事實發生日:115/08/26 2.被背書保證之: (1)公司名稱:U.D.ELECTRONIC VIETNAM COMPANY (2)與提供背書保證公司之關係: 湧德電子股份有限公司對湧德電子股份有限公司持股 100%直接投資之越南湧德有限公司背書保證 (3)背書保證之限額(仟元):4,976,334 (4)原背書保證之餘額(仟元):484,650 (5)本次新增背書保證之金額(仟元):646,200 (6)迄事實發生日止背書保證餘額(仟元):1,130,850 (7)被背書保證公司實際動支金額(仟元):480,050 (8)本次新增背書保證之原因: 融資背書保證。 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):323,100 (2)累積盈虧金額(仟元):-6,237,666,814 5.解除背書保證責任之: (1)條件: 合約終止日。 (2)日期: 合約終止日。 6.背書保證之總限額(仟元): 4,976,334 7.迄事實發生日為止，背書保證餘額(仟元): 4,226,996 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 84.94 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 20.92 10.其他應敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3689 | 湧德 | 1 | 1 | 2 | 6 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
