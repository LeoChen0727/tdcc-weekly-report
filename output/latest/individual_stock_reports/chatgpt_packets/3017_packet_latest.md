# INDIVIDUAL STOCK CHATGPT PACKET - 3017 奇鋐

## Metadata
- generated_at: 2026-07-13 22:27:33 Asia/Taipei
- stock_id: 3017
- stock_name: 奇鋐
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3017_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3017_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3017_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3017_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3017.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3017.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3017.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3017.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3017_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3017_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3017_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
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
- date: 20260709
- open: 2380
- high: 2435
- low: 2335
- close: 2350
- volume: 2889551
- ma5: 2511
- ema23_primary: 2495.85
- distance_to_ema23_pct: -5.84
- ma20: 2458
- ma60: 2551.5
- ma120: 2140.67
- return_5d: -14.23
- return_20d: -0.42
- volume_ratio: 0.73
- distance_to_ma20_pct_auxiliary: -4.39
- distance_to_high_60_pct: -21.93

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,2340,2445,2260,2335,4531372,2559.69,-8.78,2567,2436.17,0.86
20260612,2465,2480,2380,2405,2490291,2546.8,-5.57,2564.5,2444.5,0.49
20260615,2475,2475,2410,2410,2107865,2535.4,-4.95,2564.5,2453.83,0.43
20260616,2455,2470,2370,2370,3025487,2521.61,-6.01,2563.5,2459.75,0.62
20260617,2365,2440,2330,2365,3829529,2508.56,-5.72,2564.75,2465,0.78
20260618,2400,2425,2365,2400,3318114,2499.52,-3.98,2560,2471.75,0.68
20260622,2465,2490,2380,2420,3254412,2492.89,-2.92,2553.75,2479.67,0.68
20260623,2455,2475,2400,2425,3079821,2487.23,-2.5,2546.25,2485.08,0.66
20260624,2355,2590,2335,2530,6494281,2490.8,1.57,2536.5,2489.33,1.39
20260625,2595,2635,2485,2505,3833150,2491.98,0.52,2526.75,2494.5,0.83
20260626,2475,2475,2255,2255,6567236,2472.23,-8.79,2510.5,2496.5,1.4
20260629,2220,2315,2220,2300,3084014,2457.88,-6.42,2492.25,2501.67,0.7
20260630,2380,2530,2370,2525,4346000,2463.47,2.5,2479.25,2508.58,1
20260701,2615,2665,2500,2620,4922000,2476.52,5.79,2475.25,2517.75,1.12
20260702,2565,2745,2525,2740,4455000,2498.47,9.67,2469.5,2529.58,1.04
20260703,2690,2780,2665,2760,4659120,2520.27,9.51,2472,2538.42,1.09
20260706,2790,2790,2615,2670,3472000,2532.74,5.42,2475.5,2545.67,0.83
20260707,2670,2670,2410,2450,4349877,2525.85,-3,2469.5,2548.75,1.03
20260708,2425,2440,2290,2325,4441500,2509.11,-7.34,2458.5,2550.83,1.08
20260709,2380,2435,2335,2350,2889551,2495.85,-5.84,2458,2551.5,0.73
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 65.59
- over_600_ratio: 59.65
- over_800_ratio: 55.49
- over_1000_ratio: 52.77
- over_400_change_1w: 0
- over_800_change_1w: -0.02
- over_1000_change_1w: 0.48
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,67.71,,57.68,,54.22,,0,False,False
20260508,65.99,-1.72,56.7,-0.98,53.5,-0.72,0,False,False
20260515,65.99,0,56.04,-0.66,53.28,-0.22,0,False,False
20260522,65.84,-0.15,55.74,-0.3,52.54,-0.74,0,False,False
20260529,65.72,-0.12,55.92,0.18,52.92,0.38,1,False,True
20260605,65.47,-0.25,56.01,0.09,52.07,-0.85,2,False,True
20260612,64.77,-0.7,55.34,-0.67,51.68,-0.39,0,False,False
20260618,65.17,0.4,55.29,-0.05,52.04,0.36,1,False,True
20260626,65.59,0.42,55.51,0.22,52.29,0.25,2,True,True
20260703,65.59,0,55.49,-0.02,52.77,0.48,3,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3017 | 奇鋐 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | put_inflow | stale_signal | 1.事實發生日:115/07/07 2.被背書保證之: (1)公司名稱:深圳興奇宏科技有限公司 (2)與提供背書保證公司之關係: 集團關係企業(皆為本公司間接投資100%之子公司) (3)背書保證之限額(仟元):4,303,797 (4)原背書保證之餘額(仟元):2,485,716 (5)本次新增背書保證之金額(仟元):1,078,707 (6)迄事實發生日止背書保證餘額(仟元):3,564,423 (7)被背書保證公司實際動支金額(仟元):1,224,174 (8)本次新增背書保證之原因: 深圳興奇宏科技有限公司取得銀行借款額度人民幣貳億參仟萬，由集團關係企業 奇宏電子(深圳)有限公司、奇宏電子(成都)有限公司、奇宏光電(武漢)有限公司 共同擔保。 (1)公司名稱:奇宏電子(深圳)有限公司 (2)與提供背書保證公司之關係: 集團關係企業(皆為本公司間接投資100%之子公司) (3)背書保證之限額(仟元):4,303,797 (4)原背書保證之餘額(仟元):3,517,523 (5)本次新增背書保證之金額(仟元):2,110,514 (6)迄事實發生日止背書保證餘額(仟元):5,628,037 (7)被背書保證公司實際動支金額(仟元):2,970,641 (8)本次新增背書保證之原因: 奇宏電子(深圳)有限公司取得銀行借款額度人民幣肆億伍仟萬，由集團關係企業 深圳興奇宏科技有限公司、奇宏電子(成都)有限公司、奇宏光電(武漢)有限公司 共同擔保。 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):1,522,010 (2)累積盈虧金額(仟元):15,324,304 5.解除背書保證責任之: (1)條件: 銀行授信契約到期並還款後，解除背書保證。 (2)日期: 銀行授信契約到期，償還借款日。 6.背書保證之總限額(仟元): 90,329,770 7.迄事實發生日為止，背書保證餘額(仟元): 67,954,866 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 150.46 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 57.17 10.其他應敘明事項: 一、被背書保證公司最近期財務報表之資本(仟元)為： 深圳興奇宏科技有限公司：NTD 879,291 奇宏電子(深圳)有限公司：NTD 642,719  二、被背書保證公司最近期財務報表之累積盈虧金額(仟元)為： 深圳興奇宏科技有限公司：NTD 7,466,334 奇宏電子(深圳)有限公司：NTD 7,857,970；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3017 | 奇鋐 | 9 | 6 | 5 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3017 | 奇鋐 | 375 | 28 | 26311230.0 | 1427340.0 | 18.43 | put_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
