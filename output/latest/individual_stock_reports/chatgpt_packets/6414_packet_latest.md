# INDIVIDUAL STOCK CHATGPT PACKET - 6414 樺漢

## Metadata
- generated_at: 2026-09-06 22:18:05 Asia/Taipei
- stock_id: 6414
- stock_name: 樺漢
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6414_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6414_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6414_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6414_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6414_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6414_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6414_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6414.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6414.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6414.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6414.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6414_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6414_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6414_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260904
- open: 387
- high: 399
- low: 385.5
- close: 395
- volume: 1386327
- ma5: 390.6
- ema23_primary: 405.81
- distance_to_ema23_pct: -2.66
- ma20: 409.05
- ma60: 408.04
- ma120: 364.43
- return_5d: 1.28
- return_20d: -16.67
- volume_ratio: 0.72
- distance_to_ma20_pct_auxiliary: -3.43
- distance_to_high_60_pct: -24.33

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,476,483.5,467.5,482,2382498,437.11,10.27,441.35,394.19,0.58
20260811,474,476,440.5,448.5,3392029,438.06,2.38,444.9,396.34,0.81
20260812,447,459.5,446,455.5,1504936,439.51,3.64,447.95,398.58,0.36
20260813,460,473,450,451,2319984,440.47,2.39,450.5,400.63,0.55
20260814,442,442,406,407,5969868,437.68,-7.01,451.1,401.89,1.36
20260817,408,422,408,417.5,2078491,436,-4.24,451.73,403.06,0.48
20260818,418,419,386.5,389.5,4143465,432.12,-9.86,448.93,403.71,0.97
20260819,388,416.5,385,408.5,3560739,430.15,-5.03,444.85,404.46,0.85
20260820,409,414.5,397,402.5,1952403,427.85,-5.92,439.82,405.24,0.51
20260821,402.5,402.5,395,395,932166,425.11,-7.08,434.57,405.82,0.26
20260824,402.5,404.5,394,395.5,803854,422.64,-6.42,430.9,406.54,0.25
20260825,394.5,394.5,389,394,1000626,420.26,-6.25,428.8,407.1,0.33
20260826,395,398.5,392,398,777016,418.4,-4.88,426.88,407.48,0.28
20260827,398.5,401.5,393.5,393.5,877821,416.33,-5.48,426.4,407.65,0.33
20260828,396,401,389,390,1101127,414.13,-5.83,425.65,407.73,0.46
20260831,386,392.5,380.5,389.5,1375606,412.08,-5.48,423.25,407.73,0.59
20260901,390,399,390,396,1094835,410.74,-3.59,421.23,407.93,0.48
20260902,391,397.5,390,391.5,795633,409.14,-4.31,417.35,408.26,0.37
20260903,393,396,381,381,1142273,406.79,-6.34,413,407.93,0.58
20260904,387,399,385.5,395,1386327,405.81,-2.66,409.05,408.04,0.72
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 62.81
- over_600_ratio: 56.59
- over_800_ratio: 53.99
- over_1000_ratio: 50.09
- over_400_change_1w: -0.75
- over_800_change_1w: -0.75
- over_1000_change_1w: -0.85
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,65.39,-0.53,54.63,0.16,53.43,1.83,7,False,True
20260626,65.95,0.56,52.78,-1.85,50.99,-2.44,8,False,False
20260703,65.87,-0.08,52.38,-0.4,49.96,-1.03,0,False,False
20260709,65.57,-0.3,53.09,0.71,50.89,0.93,1,False,True
20260717,66.3,0.73,52.03,-1.06,49.23,-1.66,2,False,False
20260724,67.44,1.14,54.19,2.16,51.95,2.72,3,True,True
20260731,67.55,0.11,55.53,1.34,52.29,0.34,4,False,True
20260807,67.7,0.15,55.03,-0.5,52.36,0.07,5,False,True
20260814,66.49,-1.21,54.45,-0.58,52.26,-0.1,0,False,False
20260821,64.29,-2.2,53.63,-0.82,50.98,-1.28,0,False,False
20260828,63.56,-0.73,54.74,1.11,50.94,-0.04,1,False,True
20260904,62.81,-0.75,53.99,-0.75,50.09,-0.85,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6414 | 樺漢 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/09/02 2.公司名稱:樺漢科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:更正本公司114年第四季個體、合併財報、115年度第一季合併財報及 iXBRL資訊平台之「子公司昆山力盟機械工業有限公司之投資大陸資訊」 6.更正資訊項目/報表名稱: 114年第四季個體、合併財報及115年度第一季合併財務報告附表八大陸投資資訊 7.更正前金額/內容/頁次: (1)114年第四季個體財務報告第89頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 (2)114年第四季合併財務報告第127頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 (3)115年第一季合併財務報告第93頁    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 8.更正後金額/內容/頁次: (1)114年第四季個體財務報告第89頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：469,913仟元 (2)114年第四季合併財務報告第127頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：469,913仟元 (3)115年第一季合併財務報告第93頁     昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：478,435仟元 9.因應措施:更正後重新上傳至公開資訊觀測站 10.其他應敘明事項:本次更正不影響財務報告之營收及損益；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 6414 | 樺漢 | revenue_breakout_low_response | 營收爆發低反應股 | 11 | 62 | D_降級_TDCC轉弱 |  |  | call_put_bullish | stale_signal | 1.事實發生日:115/09/02 2.公司名稱:樺漢科技股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:更正本公司114年第四季個體、合併財報、115年度第一季合併財報及 iXBRL資訊平台之「子公司昆山力盟機械工業有限公司之投資大陸資訊」 6.更正資訊項目/報表名稱: 114年第四季個體、合併財報及115年度第一季合併財務報告附表八大陸投資資訊 7.更正前金額/內容/頁次: (1)114年第四季個體財務報告第89頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 (2)114年第四季合併財務報告第127頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 (3)115年第一季合併財務報告第93頁    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：0仟元 8.更正後金額/內容/頁次: (1)114年第四季個體財務報告第89頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：469,913仟元 (2)114年第四季合併財務報告第127頁、    昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：469,913仟元 (3)115年第一季合併財務報告第93頁     昆山力盟機械工業有限公司本期期末自台灣匯出累積投資金額：478,435仟元 9.因應措施:更正後重新上傳至公開資訊觀測站 10.其他應敘明事項:本次更正不影響財務報告之營收及損益；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6414 | 樺漢 | 2 | 2 | 4 | 6 | 15 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 6414 | 樺漢 | 79 | 1 | 5046930.0 | 30380.0 | 166.13 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
