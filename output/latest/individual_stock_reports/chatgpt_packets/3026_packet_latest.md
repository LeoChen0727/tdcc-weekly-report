# INDIVIDUAL STOCK CHATGPT PACKET - 3026 禾伸堂

## Metadata
- generated_at: 2026-09-12 15:43:06 Asia/Taipei
- stock_id: 3026
- stock_name: 禾伸堂
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 353
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3026_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3026_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3026_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3026_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3026_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3026_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3026_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3026.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3026.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3026.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3026.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3026_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3026_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3026_latest.md?ref=main

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
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 782
- high: 803
- low: 737
- close: 744
- volume: 14914692
- ma5: 764.6
- ema23_primary: 702.35
- distance_to_ema23_pct: 5.93
- ma20: 700.95
- ma60: 712.91
- ma120: 542.26
- return_5d: 6.13
- return_20d: 14.99
- volume_ratio: 1.67
- distance_to_ma20_pct_auxiliary: 6.14
- distance_to_high_60_pct: -28.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,647,692,605,689,1451748,634.35,8.62,586.23,699.87,0.23
20260818,673,685,656,668,1321195,637.15,4.84,585.52,703.06,0.24
20260819,646,692,641,690,1797462,641.55,7.55,586.88,705.84,0.33
20260820,714,714,675,710,1288951,647.26,9.69,587.52,708.17,0.24
20260821,701,745,639,639,13288166,646.57,-1.17,587.48,708.69,2.22
20260824,645,670,621,643,12901313,646.27,-0.51,590.38,709.33,1.98
20260825,643,643,590,628,7687272,644.75,-2.6,595.42,709.11,1.12
20260826,627,630,591,614,8416228,642.19,-4.39,602.4,708.14,1.16
20260827,639,675,606,675,6925051,644.92,4.66,614.77,708.56,0.93
20260828,719,742,707,742,15081013,653.01,13.63,629.38,710.26,1.92
20260831,742,766,712,742,16901442,660.43,12.35,643.5,712.26,1.98
20260901,769,795,730,731,12797881,666.31,9.71,655.15,714.01,1.42
20260902,718,743,686,686,6999229,667.95,2.7,662.1,715.42,0.75
20260903,691,699,632,638,7150909,665.45,-4.13,664.35,715.04,0.75
20260904,692,701,683,701,7288466,668.42,4.87,672.65,716.02,0.74
20260907,770,771,761,771,3646503,676.96,13.89,681.8,717.29,0.37
20260908,750,776,738,747,11962376,682.8,9.4,686.85,717.01,1.27
20260909,775,793,747,758,12792343,689.07,10,690.5,715.64,1.45
20260910,763,826,730,803,13763005,698.56,14.95,696.1,715.44,1.66
20260911,782,803,737,744,14914692,702.35,5.93,700.95,712.91,1.67
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 57.45
- over_600_ratio: 50.28
- over_800_ratio: 44.76
- over_1000_ratio: 37.88
- over_400_change_1w: 2.44
- over_800_change_1w: 2.69
- over_1000_change_1w: -0.57
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,56.1,-1.14,45.14,-1.15,40.9,-0.52,0,False,False
20260703,56.06,-0.04,45.87,0.73,41.16,0.26,1,False,True
20260709,56.78,0.72,47.82,1.95,41.28,0.12,2,True,True
20260717,57.82,1.04,49.93,2.11,43.38,2.1,3,True,True
20260724,58.78,0.96,48.91,-1.02,42.86,-0.52,4,False,False
20260731,58.75,-0.03,47.5,-1.41,41.55,-1.31,0,False,False
20260807,57.25,-1.5,47.53,0.03,42.01,0.46,1,False,True
20260814,55.46,-1.79,44.89,-2.64,38.86,-3.15,0,False,False
20260821,56.52,1.06,45.83,0.94,38.92,0.06,1,True,True
20260828,55.69,-0.83,44.22,-1.61,37.89,-1.03,0,False,False
20260904,55.01,-0.68,42.07,-2.15,38.45,0.56,1,False,True
20260911,57.45,2.44,44.76,2.69,37.88,-0.57,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3026 | 禾伸堂 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/06/16 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理公告 3.財務業務資訊: 期間　　　　　　　(月)                   (季)              (最近四季累計) ＝＝＝＝  ＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝ 　＝＝＝＝＝＝＝ 　　　　　最近一月　  與去年同期　 最近一季　 與去年同期　  (114年第2季至 科目　　　(115年5月)　　增減%　   (115年第1季)　　增減% 　   115年第1季) 　　　　      (合併自結數)  　         (合併核閱數)       (合併查核/核閱數) ＝＝＝＝　＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝   ＝＝＝＝＝＝＝ 營業收入　  1,291.19 　   21.34%　　3,618.45　     6.36%　　    13,643.30 （百萬） 稅前淨利      201.80     235.56%　    568.65　    94.65%　　     1,467.33 （百萬）　　 歸屬母公司    168.40     207.44%　　  474.58　　  70.41%　　     1,287.79 業主淨利 （百萬） 每股盈餘        1.02     207.44% 　　   2.86　　  70.41%　           7.76 （元） 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告:無。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |
| 20260911 | 3026 | 禾伸堂 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | no_signal | repeated_but_no_breakout | 1.事實發生日:115/06/16 2.發生緣由:依臺灣證券交易所股份有限公司通知辦理公告 3.財務業務資訊: 期間　　　　　　　(月)                   (季)              (最近四季累計) ＝＝＝＝  ＝＝＝＝＝＝＝＝＝＝＝　＝＝＝＝＝＝＝＝＝＝＝ 　＝＝＝＝＝＝＝ 　　　　　最近一月　  與去年同期　 最近一季　 與去年同期　  (114年第2季至 科目　　　(115年5月)　　增減%　   (115年第1季)　　增減% 　   115年第1季) 　　　　      (合併自結數)  　         (合併核閱數)       (合併查核/核閱數) ＝＝＝＝　＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝  ＝＝＝＝＝   ＝＝＝＝＝＝＝ 營業收入　  1,291.19 　   21.34%　　3,618.45　     6.36%　　    13,643.30 （百萬） 稅前淨利      201.80     235.56%　    568.65　    94.65%　　     1,467.33 （百萬）　　 歸屬母公司    168.40     207.44%　　  474.58　　  70.41%　　     1,287.79 業主淨利 （百萬） 每股盈餘        1.02     207.44% 　　   2.86　　  70.41%　           7.76 （元） 4.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第4條所列重大訊息之情事（如「有」，請說明）:無。 5.有無「臺灣證券交易所股份有限公司對有價證券上市公司重大訊息之查證暨公開處理   程序」第11條所列重大訊息說明記者會之情事:無。 6.完整財務資訊請至公開資訊觀測站查閱，路徑如下： (1)近期營業收入及損益資訊：基本資料>精華版 (2)歷史每月營業收入：營運概況>每月營收>採用IFRSs後之月營業收入資訊 (3)歷史損益(會計師查核/核閱數)：財務報表>採IFRSs後>合併/個別報表>綜合損益表 (4)歷史損益(自願性公告自結數)：營運概況>自結損益公告:無。 7.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3026 | 禾伸堂 | 4 | 1 | 4 | 8 | 16 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 16 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 3026 | 禾伸堂 | 40 | 0 | 664330.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
