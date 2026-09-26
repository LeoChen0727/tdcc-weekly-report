# INDIVIDUAL STOCK CHATGPT PACKET - 2406 國碩

## Metadata
- generated_at: 2026-09-26 15:51:19 Asia/Taipei
- stock_id: 2406
- stock_name: 國碩
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 回檔後短線轉強
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 回檔後短線轉強，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260924
- open: 30.3
- high: 31.5
- low: 30.3
- close: 30.5
- volume: 10613029
- ma5: 29.71
- ema23_primary: 28.53
- distance_to_ema23_pct: 6.91
- ma20: 27.8
- ma60: 30.97
- ma120: 32.41
- return_5d: 14.66
- return_20d: 6.27
- volume_ratio: 1.98
- distance_to_ma20_pct_auxiliary: 9.7
- distance_to_high_60_pct: -30.84

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,28.9,29.3,28.65,28.65,3080599,30.16,-5,30.06,33.72,0.61
20260831,28.5,28.75,27.85,28.05,3132529,29.98,-6.44,29.92,33.55,0.65
20260901,28.15,28.8,28.15,28.4,2884365,29.85,-4.86,29.77,33.44,0.61
20260902,28.25,28.5,27.9,27.9,2962726,29.69,-6.02,29.53,33.38,0.7
20260903,28,28.25,27,27.05,4151276,29.47,-8.2,29.27,33.24,1.01
20260904,27.4,27.4,26.75,27.25,3061571,29.28,-6.94,29.07,33.1,0.75
20260907,27.5,27.7,27.2,27.25,2054941,29.11,-6.4,28.83,32.9,0.51
20260908,27.45,27.45,26.9,26.9,2237101,28.93,-7.01,28.59,32.7,0.58
20260909,27.25,27.4,26.9,27.35,2266549,28.8,-5.03,28.38,32.51,0.61
20260910,27.35,27.35,26.6,26.9,2722263,28.64,-6.07,28.14,32.38,0.77
20260911,26.5,26.9,26.3,26.4,3041349,28.45,-7.21,28,32.21,1
20260914,26.4,27,26.1,26.5,1734464,28.29,-6.33,27.86,32.07,0.6
20260915,26.5,26.95,25.85,25.85,1698955,28.09,-7.96,27.71,31.91,0.62
20260916,26.05,26.65,26,26.45,1661791,27.95,-5.37,27.61,31.79,0.62
20260917,26.7,27.3,26.6,26.6,1984659,27.84,-4.45,27.5,31.66,0.74
20260918,27.1,28.05,26.55,27.65,4682700,27.82,-0.62,27.46,31.53,1.66
20260921,28.35,30.4,28.05,30.4,12317610,28.04,8.43,27.57,31.46,3.75
20260922,30.95,31,29.5,30.1,33061443,28.21,6.7,27.66,31.33,6.98
20260923,30.7,30.9,29.55,29.9,7690881,28.35,5.47,27.71,31.13,1.55
20260924,30.3,31.5,30.3,30.5,10613029,28.53,6.91,27.8,30.97,1.98
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 23.61
- over_600_ratio: 20.71
- over_800_ratio: 19.52
- over_1000_ratio: 16.92
- over_400_change_1w: -0.69
- over_800_change_1w: -1.29
- over_1000_change_1w: -0.36
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,34.17,-3.2,31.42,-2.5,28.64,-2.44,0,False,False
20260717,31.26,-2.91,28.01,-3.41,25.78,-2.86,0,False,False
20260724,29.21,-2.05,25.62,-2.39,23.62,-2.16,0,False,False
20260731,27.32,-1.89,23.88,-1.74,21.32,-2.3,0,False,False
20260807,26.42,-0.9,23.05,-0.83,20.49,-0.83,0,False,False
20260814,26.73,0.31,22.69,-0.36,19.83,-0.66,1,False,False
20260821,25.17,-1.56,21.35,-1.34,18.48,-1.35,0,False,False
20260828,24.66,-0.51,20.69,-0.66,17.82,-0.66,0,False,False
20260904,24.11,-0.55,19.91,-0.78,17.36,-0.46,0,False,False
20260911,24.49,0.38,20.82,0.91,17.21,-0.15,1,False,True
20260918,24.3,-0.19,20.81,-0.01,17.28,0.07,2,False,True
20260924,23.61,-0.69,19.52,-1.29,16.92,-0.36,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2406 | 國碩 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | continued_overheated | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認本公司114年度虧損撥補案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表:  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)配合子公司禾迅綠電(股)公司未來申請股票上市（櫃）計畫，本公司得辦理對禾迅     綠電(股)公司釋股作業暨放棄參與其現金增資計畫案。  (2)本公司辦理私募普通股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |
| 20260924 | 2406 | 國碩 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | continued_overheated | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認本公司114年度虧損撥補案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表:  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)配合子公司禾迅綠電(股)公司未來申請股票上市（櫃）計畫，本公司得辦理對禾迅     綠電(股)公司釋股作業暨放棄參與其現金增資計畫案。  (2)本公司辦理私募普通股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260924 | 2406 | 國碩 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 1.股東常會日期:115/06/26 2.重要決議事項一、盈餘分配或盈虧撥補:通過承認本公司114年度虧損撥補案。 3.重要決議事項二、章程修訂:無。 4.重要決議事項三、營業報告書及財務報表:  通過承認114年度營業報告書及財務報表案。 5.重要決議事項四、董監事選舉:無。 6.重要決議事項五、其他事項:  (1)配合子公司禾迅綠電(股)公司未來申請股票上市（櫃）計畫，本公司得辦理對禾迅     綠電(股)公司釋股作業暨放棄參與其現金增資計畫案。  (2)本公司辦理私募普通股案。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2406 | 國碩 | 60 | 14 | 5 | 10 | 20 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 2406 | 國碩 | 24 | 0 | 446360.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
