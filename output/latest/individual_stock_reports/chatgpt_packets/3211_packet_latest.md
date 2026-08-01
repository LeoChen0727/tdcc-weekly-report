# INDIVIDUAL STOCK CHATGPT PACKET - 3211 順達

## Metadata
- generated_at: 2026-08-01 22:27:21 Asia/Taipei
- stock_id: 3211
- stock_name: 順達
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 180
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260731-0b236a2d4a043618
- official_tdcc_signal_date: 20260731
- latest_tdcc_date: 20260731
- tdcc_rows: 14
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3211_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3211_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3211_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3211.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3211.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3211.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3211.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3211_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3211_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3211_latest.md?ref=main

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
- date: 20260730
- open: 278.5
- high: 314.5
- low: 278.5
- close: 285.5
- volume: 7183000
- ma5: 337.3
- ema23_primary: 381.44
- distance_to_ema23_pct: -25.15
- ma20: 392.15
- ma60: 404.02
- ma120: 368.41
- return_5d: -27.08
- return_20d: -30.02
- volume_ratio: 1.02
- distance_to_ma20_pct_auxiliary: -27.2
- distance_to_high_60_pct: -42.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,393.5,406.5,389.5,406.5,4209000,413.58,-1.71,418.02,397.24,0.79
20260703,402.5,408.5,399,401,1546000,412.53,-2.8,415.38,397.62,0.29
20260706,417.5,434.5,409,422.5,8631000,413.37,2.21,415.35,398.55,1.49
20260707,443,458.5,388.5,389,13314000,411.33,-5.43,415.15,398.78,2.21
20260708,425.5,427.5,425.5,427.5,4310000,412.68,3.59,415.43,399.92,0.75
20260709,455,470,433.5,454,27742000,416.12,9.1,417.88,401.65,4.09
20260713,490,495,449.5,457.5,15153000,419.57,9.04,420.82,403.48,2.11
20260714,451,452,412,440,7839000,421.28,4.44,421.93,405,1.07
20260715,446,446,425.5,427,7640000,421.75,1.24,421.85,406.13,1.03
20260716,424.5,439,416,426.5,4692000,422.15,1.03,421.3,407.09,0.65
20260717,408,418,385.5,385.5,5712000,419.09,-8.02,419.18,407.19,0.78
20260720,368,379,348.5,354,6053000,413.67,-14.42,415.07,406.18,0.83
20260721,357,380,354.5,380,3849000,410.86,-7.51,411.45,405.94,0.55
20260722,394,398,385,394,4696000,409.46,-3.78,409.77,406.15,0.68
20260723,397,398,382,391.5,3711000,407.96,-4.04,408.4,406.25,0.54
20260724,385,395.5,380,382,2789000,405.8,-5.86,407.1,406.36,0.41
20260727,381.5,386,365.5,374,2703000,403.15,-7.23,406.3,406.55,0.4
20260728,362,362,337,337,2792000,397.64,-15.25,403.52,406.16,0.41
20260729,326.5,328,303.5,308,5807000,390.17,-21.06,398.27,405.31,0.84
20260730,278.5,314.5,278.5,285.5,7183000,381.44,-25.15,392.15,404.02,1.02
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 51.13
- over_600_ratio: 46.58
- over_800_ratio: 42.51
- over_1000_ratio: 39.01
- over_400_change_1w: -2.43
- over_800_change_1w: -2.17
- over_1000_change_1w: -1.67
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,51.09,-1.72,45.49,-0.31,39.56,-0.27,0,False,False
20260522,48.79,-2.3,41.75,-3.74,37.67,-1.89,0,False,False
20260529,58.76,9.97,50.64,8.89,47.6,9.93,1,True,True
20260605,56.1,-2.66,48.7,-1.94,42.87,-4.73,0,False,False
20260612,54.18,-1.92,47.37,-1.33,44.29,1.42,1,False,True
20260618,54.71,0.53,47.9,0.53,45.39,1.1,2,True,True
20260626,53.66,-1.05,45.05,-2.85,43.91,-1.48,0,False,False
20260703,52.09,-1.57,45.4,0.35,42.57,-1.34,1,False,True
20260709,53.45,1.36,45.37,-0.03,42.46,-0.11,2,False,False
20260717,54.05,0.6,45.38,0.01,41.85,-0.61,3,False,True
20260724,53.56,-0.49,44.68,-0.7,40.68,-1.17,0,False,False
20260731,51.13,-2.43,42.51,-2.17,39.01,-1.67,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3211 | 順達 | revenue_pullback | 營收成長股價回檔 | 69.0 |  |  |  |  |  | stale_signal | 1.事實發生日:115/07/13 2.原公告申報日期:115/04/30 3.簡述原公告申報內容:  本公司於115年4月30日董事會決議通過發行115年限制員工權利新股一案，業經 115年6月11日股東會通過。 4.變動緣由及主要內容:  (1)依據金融監督管理委員會審案要求，修正本公司115年限制員工權利新股發行　  辦法部分條文，業經115年7月13日董事會通過。  (2)修正前條文:  第五條 限制員工權利新股既得條件及股份權利內容受限情形：  (一)略  (二)略  (三)既得條件分為A、B類兩種  1.A類員工自認購限制員工權利新股後屆滿一年起於各既得期限屆滿仍在職，同時須符  合公司整體財務業務績效及個人績效評核指標，且未曾有違反與本公司簽訂之聘僱契  約書、廉潔承諾書及公司工作規則等情事，可分別達成既得條件之股份比例依本公司  訂定之限制員工權利新股發行辦法分配之，各期可分別達成既得條件之股份比例如下  :  屆滿1年：3分之1  屆滿2年：3分之1  屆滿3年：3分之1  2.B類員工自認購限制員工權利新股後屆滿一年六個月起於各既得期限屆滿仍在職，同  時須符合公司整體財務業務績效及個人績效評核指標，且未曾有違反與本公司簽訂之聘  僱契約書、廉潔承諾書及公司工作規則等情事，可分別達成既得條件之股份比例依本公  司訂定之限制員工權利新股發行辦法分配之，各期可分別達成既得條件之股份比例如下  :  屆滿1年6個月： 4分之1  屆滿2年6個月： 4分之1  屆滿3年6個月： 2分之1  (四)略  (五)略  (六)略  (七)略  (3)修正後條文:  第五條 限制員工權利新股既得條件及股份權利內容受限情形：  (一)略  (二)略  (三)既得條件分為A、B類兩種，B類係指已認購本公司114年發行之限制員工權利新股，  其餘員工屬於A類。  1.A類員工自認購限制員工權利新股後屆滿一年起於各既得期限屆滿仍在職，同時須符  合公司整體財務業務績效即公司營業收入預算達成率70%以上(含)及個人績效在各屆滿  日前最近期個人績效D+以上(含)評核指標，且未曾有違反與本公司簽訂之聘僱契約書  、廉潔承諾書及公司工作規則等情事，可分別達成既得條件之股份比例依本公司訂定  之限制員工權利新股發行辦法分配之，各期可分別達成既得條件之股份比例如下:  屆滿1年： 3分之1  屆滿2年： 3分之1  屆滿3年： 3分之1  2.B類員工自認購限制員工權利新股後屆滿一年六個月起於各既得期限屆滿仍在職，同  時須符合公司整體財務業務績效即公司備援電池模組營業收入預算達成率70%以上(含)  及個人績效在各屆滿日前最近期個人績效D+以上(含)評核指標，且未曾有違反與本公  司簽訂之聘僱契約書、廉潔承諾書及公司工作規則等情事，可分別達成既得條件之股  份比例依本公司訂定之限制員工權利新股發行辦法分配之，各期可分別達成既得條件  之股份比例如下:  屆滿1年6個月： 4分之1  屆滿2年6個月： 4分之1  屆滿3年6個月： 2分之1  (四)略  (五)略  (六)略  (七)略 5.變動後對公司財務業務之影響:無。 6.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3211 | 順達 | 7 | 2 | 5 | 9 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
