# INDIVIDUAL STOCK CHATGPT PACKET - 7610 聯友金屬-創

## Metadata
- generated_at: 2026-09-19 22:17:41 Asia/Taipei
- stock_id: 7610
- stock_name: 聯友金屬-創
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 249
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/7610_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/7610_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7610_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7610_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7610_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7610_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7610_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7610.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7610.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7610.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7610.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7610_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7610_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7610_latest.md?ref=main

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
- date: 20260918
- open: 1820
- high: 1945
- low: 1765
- close: 1945
- volume: 2608870
- ma5: 1776
- ema23_primary: 1790.88
- distance_to_ema23_pct: 8.61
- ma20: 1756.75
- ma60: 1877.08
- ma120: 1494.9
- return_5d: -1.52
- return_20d: 15.43
- volume_ratio: 2.79
- distance_to_ma20_pct_auxiliary: 10.72
- distance_to_high_60_pct: -28.75

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,1770,1820,1660,1710,900470,1740.7,-1.76,1611.25,1921.5,2
20260825,1665,1690,1590,1635,529555,1731.89,-5.59,1625.5,1924.17,1.13
20260826,1615,1670,1590,1610,492577,1721.74,-6.49,1645.25,1924.08,1.01
20260827,1610,1655,1595,1595,382223,1711.17,-6.79,1670.25,1922.58,0.86
20260828,1625,1625,1445,1495,1189663,1693.16,-11.7,1685,1919.83,2.39
20260831,1460,1535,1450,1505,457229,1677.48,-10.28,1694.25,1916.08,0.89
20260901,1525,1630,1485,1605,609180,1671.44,-3.98,1702,1913.67,1.15
20260902,1595,1595,1520,1520,446636,1658.82,-8.37,1698.25,1909.33,0.83
20260903,1540,1670,1540,1655,1152011,1658.5,-0.21,1693.5,1905,1.98
20260904,1820,1820,1820,1820,395227,1671.96,8.85,1692,1906.58,0.68
20260907,2000,2000,2000,2000,327155,1699.3,17.7,1694.5,1914,0.59
20260908,2000,2170,2000,2065,2424763,1729.77,19.38,1704.25,1921.92,3.65
20260909,2065,2110,1985,2030,1223081,1754.79,15.68,1711,1926.67,1.71
20260910,2110,2115,1940,2035,1027843,1778.14,14.45,1722.25,1928.67,1.36
20260911,2000,2035,1950,1975,587269,1794.55,10.06,1733.5,1926.5,0.76
20260914,1920,1920,1780,1780,972335,1793.33,-0.74,1730,1917.58,1.21
20260915,1695,1755,1655,1655,878535,1781.81,-7.12,1725.75,1903.42,1.09
20260916,1685,1810,1630,1730,1215127,1777.49,-2.67,1732,1892,1.46
20260917,1715,1810,1705,1770,866311,1776.87,-0.39,1743.75,1882.17,1.04
20260918,1820,1945,1765,1945,2608870,1790.88,8.61,1756.75,1877.08,2.79
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 50.04
- over_600_ratio: 44.25
- over_800_ratio: 41.07
- over_1000_ratio: 39.66
- over_400_change_1w: -0.65
- over_800_change_1w: -0.64
- over_1000_change_1w: -0.64
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,47.94,-0.35,36.85,-1.58,34.92,0.07,7,False,True
20260709,48.33,0.39,38.85,2,36.93,2.01,8,True,True
20260717,49.28,0.95,39.89,1.04,38.01,1.08,9,True,True
20260724,48.6,-0.68,40.14,0.25,38.26,0.25,10,False,True
20260731,48.87,0.27,40.86,0.72,38.92,0.66,11,False,True
20260807,48.81,-0.06,40.8,-0.06,38.86,-0.06,0,False,False
20260814,58,9.19,50.58,9.78,49,10.14,1,True,True
20260821,50.8,-7.2,41.8,-8.78,38.97,-10.03,0,False,False
20260828,50.4,-0.4,41.42,-0.38,40.01,1.04,1,False,True
20260904,50.12,-0.28,41.27,-0.15,39.86,-0.15,0,False,False
20260911,50.69,0.57,41.71,0.44,40.3,0.44,1,True,True
20260918,50.04,-0.65,41.07,-0.64,39.66,-0.64,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 7610 | 聯友金屬-創 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/08 2.發生緣由:依證券櫃檯買賣中心通知辦理 3.公司債相關資訊: 聯友金屬一創(代號:76101)可轉債相關資訊 到期日期:118/05/20 實際發行總額:新台幣800,000,000元整 本月發行餘額:新台幣592,000,000元整(截至115/09/07未轉換金額) 最新轉(交)換價格:662.30 轉換標的收市價格(7610):2,065.00(115/09/08收盤價) 轉債收市價格(76101):310.00(115/09/08收盤價) 4.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 7610 | 聯友金屬-創 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  |  | repeated_but_no_breakout | 1.事實發生日:115/09/08 2.發生緣由:依證券櫃檯買賣中心通知辦理 3.公司債相關資訊: 聯友金屬一創(代號:76101)可轉債相關資訊 到期日期:118/05/20 實際發行總額:新台幣800,000,000元整 本月發行餘額:新台幣592,000,000元整(截至115/09/07未轉換金額) 最新轉(交)換價格:662.30 轉換標的收市價格(7610):2,065.00(115/09/08收盤價) 轉債收市價格(76101):310.00(115/09/08收盤價) 4.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 7610 | 聯友金屬-創 | 1 | 1 | 3 | 6 | 7 | repeated_but_no_breakout | 近 10 日上榜 6 次、近 20 日上榜 7 次，但尚未有效突破，需等待攻擊確認。 |

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
