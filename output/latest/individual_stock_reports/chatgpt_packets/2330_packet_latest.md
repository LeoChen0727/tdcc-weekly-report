# INDIVIDUAL STOCK CHATGPT PACKET - 2330 台積電

## Metadata
- generated_at: 2026-08-08 22:26:46 Asia/Taipei
- stock_id: 2330
- stock_name: 台積電
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
- individual_report_md_exists: True
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2330_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2330_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2330_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2330_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2330.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2330.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2330.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2330.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2330_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2330_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2330_latest.md?ref=main

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
- date: 20260805
- open: 2385
- high: 2415
- low: 2370
- close: 2405
- volume: 36782301
- ma5: 2345
- ema23_primary: 2360.55
- distance_to_ema23_pct: 1.88
- ma20: 2369
- ma60: 2352.42
- ma120: 2157.33
- return_5d: 9.32
- return_20d: -1.43
- volume_ratio: 0.87
- distance_to_ma20_pct_auxiliary: 1.52
- distance_to_high_60_pct: -5.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,2445,2465,2420,2465,25519599,2400.02,2.71,2403.25,2287.92,0.64
20260709,2450,2460,2415,2415,34681018,2401.27,0.57,2411.25,2293.92,0.9
20260713,2460,2480,2440,2440,35310380,2404.5,1.48,2420.75,2299.92,0.93
20260714,2410,2430,2390,2420,42857055,2405.79,0.59,2426.25,2305.5,1.1
20260715,2425,2460,2415,2440,33665566,2408.64,1.3,2429.5,2312.33,0.86
20260716,2430,2470,2420,2470,30538604,2413.76,2.33,2433,2319.75,0.79
20260717,2375,2395,2290,2290,97362670,2403.44,-4.72,2428.25,2323.75,2.31
20260720,2300,2345,2300,2320,55790346,2396.49,-3.19,2423.75,2328.25,1.31
20260721,2350,2410,2345,2410,31605663,2397.61,0.52,2418.75,2333.75,0.76
20260722,2440,2445,2385,2400,31653123,2397.81,0.09,2414.25,2337.33,0.76
20260723,2385,2405,2370,2405,28001492,2398.41,0.27,2415,2339.67,0.71
20260724,2355,2365,2345,2350,24810509,2394.38,-1.85,2413,2341.92,0.64
20260727,2330,2365,2330,2350,28939466,2390.68,-1.7,2413.5,2344.75,0.77
20260728,2270,2305,2270,2280,45333029,2381.46,-4.26,2409,2347.17,1.2
20260729,2260,2280,2180,2200,68139691,2366.34,-7.03,2398.5,2345.92,1.76
20260730,2205,2260,2190,2205,47256177,2352.89,-6.29,2383.5,2345.17,1.21
20260731,2350,2425,2345,2425,69478145,2358.9,2.8,2381.5,2348.08,1.7
20260803,2390,2395,2365,2370,35209944,2359.82,0.43,2377.75,2349.08,0.86
20260804,2335,2360,2310,2320,41021199,2356.51,-1.55,2370.75,2349.58,0.98
20260805,2385,2415,2370,2405,36782301,2360.55,1.88,2369,2352.42,0.87
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 87.43
- over_600_ratio: 86.33
- over_800_ratio: 85.39
- over_1000_ratio: 84.67
- over_400_change_1w: 0.04
- over_800_change_1w: 0.03
- over_1000_change_1w: 0.05
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,88.1,-0.08,86.11,-0.1,85.39,-0.08,0,False,False
20260529,88.12,0.02,86.14,0.03,85.41,0.02,1,True,True
20260605,88.12,0,86.14,0,85.42,0.01,2,False,True
20260612,87.89,-0.23,85.94,-0.2,85.18,-0.24,0,False,False
20260618,87.92,0.03,85.98,0.04,85.22,0.04,1,True,True
20260626,87.83,-0.09,85.84,-0.14,85.11,-0.11,0,False,False
20260703,87.81,-0.02,85.82,-0.02,85.09,-0.02,0,False,False
20260709,87.74,-0.07,85.76,-0.06,85.01,-0.08,0,False,False
20260717,87.67,-0.07,85.66,-0.1,84.91,-0.1,0,False,False
20260724,87.48,-0.19,85.47,-0.19,84.7,-0.21,0,False,False
20260731,87.39,-0.09,85.36,-0.11,84.62,-0.08,0,False,False
20260807,87.43,0.04,85.39,0.03,84.67,0.05,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2330 | 台積電 | revenue_pullback | 營收成長股價回檔 | 84.0 |  |  |  |  | mixed_flow | stale_signal | 1.事實發生日:115/07/16 2.公司名稱:台灣積體電路製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:不適用 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 台積公司今（16）日公佈2026年第二季財務報告，合併營收約新台幣1兆2,703億8千 萬元，稅後純益約新台幣7,065億6千萬元，每股盈餘為新台幣27.25元（折合美國存 託憑證每單位為4.31美元）。  與去年同期相較，2026年第二季營收增加了36.0%，稅後純益與每股盈餘皆增加了 77.4%。與前一季相較，2026年第二季營收增加了12.0%，稅後純益則增加了23.4%。 以上財務數字皆為合併財務報表數字，且係依照金管會認可之國際財務報導準則 （TIFRS）所編製。  若以美元計算，2026年第二季營收為402億，較去年同期增加了33.7%，較前一季增 加了12.0%。  2026年第二季毛利率為67.7%，營業利益率為60.3%，稅後純益率則為55.6%。  2奈米製程出貨佔台積公司2026年第二季晶圓銷售金額的3%；3奈米製程出貨佔全季 晶圓銷售金額的30%，5奈米製程出貨佔全季晶圓銷售金額的33%；7奈米製程出貨則 佔全季晶圓銷售金額的11%。總體而言，先進製程（包含7奈米及更先進製程）的營 收達到全季晶圓銷售金額的77%。  台積公司財務長暨發言人黃仁昭資深副總經理表示：「台積公司2026年第二季的業 績受惠於市場對我們先進製程技術的強大需求。進入2026年第三季，對台積公司先 進製程技術持續的強勁需求，包含2奈米製程技術的快速產能提升，將繼續支持我們 的業績表現。」  根據對當前業務狀況的評估，台積公司2026年第三季的業績展望如下：  ‧合併營收預計介於446億美元到458億美元之間； 若以新台幣32元兌1美元匯率假設，則 ‧毛利率預計介於65%到67%之間； ‧營業利益率預計介於56%到58%之間。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260717 | 2330 | 台積電 | revenue_breakout_low_response | 營收爆發低反應股 | 16.0 | 26.0 | D_降級_TDCC轉弱 |  |  | mixed_flow | stale_signal | 1.事實發生日:115/07/16 2.公司名稱:台灣積體電路製造股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:不適用 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 台積公司今（16）日公佈2026年第二季財務報告，合併營收約新台幣1兆2,703億8千 萬元，稅後純益約新台幣7,065億6千萬元，每股盈餘為新台幣27.25元（折合美國存 託憑證每單位為4.31美元）。  與去年同期相較，2026年第二季營收增加了36.0%，稅後純益與每股盈餘皆增加了 77.4%。與前一季相較，2026年第二季營收增加了12.0%，稅後純益則增加了23.4%。 以上財務數字皆為合併財務報表數字，且係依照金管會認可之國際財務報導準則 （TIFRS）所編製。  若以美元計算，2026年第二季營收為402億，較去年同期增加了33.7%，較前一季增 加了12.0%。  2026年第二季毛利率為67.7%，營業利益率為60.3%，稅後純益率則為55.6%。  2奈米製程出貨佔台積公司2026年第二季晶圓銷售金額的3%；3奈米製程出貨佔全季 晶圓銷售金額的30%，5奈米製程出貨佔全季晶圓銷售金額的33%；7奈米製程出貨則 佔全季晶圓銷售金額的11%。總體而言，先進製程（包含7奈米及更先進製程）的營 收達到全季晶圓銷售金額的77%。  台積公司財務長暨發言人黃仁昭資深副總經理表示：「台積公司2026年第二季的業 績受惠於市場對我們先進製程技術的強大需求。進入2026年第三季，對台積公司先 進製程技術持續的強勁需求，包含2奈米製程技術的快速產能提升，將繼續支持我們 的業績表現。」  根據對當前業務狀況的評估，台積公司2026年第三季的業績展望如下：  ‧合併營收預計介於446億美元到458億美元之間； 若以新台幣32元兌1美元匯率假設，則 ‧毛利率預計介於65%到67%之間； ‧營業利益率預計介於56%到58%之間。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2330 | 台積電 | 29 | 2 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 2330 | 台積電 | 907 | 180 | 255147980.0 | 13912570.0 | 18.34 | mixed_flow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
