# INDIVIDUAL STOCK CHATGPT PACKET - 7799 禾榮科

## Metadata
- generated_at: 2026-09-12 22:17:55 Asia/Taipei
- stock_id: 7799
- stock_name: 禾榮科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 240
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/7799_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/7799_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7799_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7799_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7799.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7799.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7799.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7799.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7799_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7799_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7799_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 436
- high: 436.5
- low: 412.5
- close: 414.5
- volume: 1310142
- ma5: 400.7
- ema23_primary: 378.92
- distance_to_ema23_pct: 9.39
- ma20: 372.35
- ma60: 384.84
- ma120: 370.34
- return_5d: 12.03
- return_20d: 12.94
- volume_ratio: 3.31
- distance_to_ma20_pct_auxiliary: 11.32
- distance_to_high_60_pct: -12.37

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,367,367.5,350,350,275371,369.96,-5.39,368.07,375.03,0.76
20260818,351.5,352.5,347,351,98768,368.38,-4.72,364.38,375.41,0.29
20260819,350.5,353,345,345,128144,366.43,-5.85,361.12,375.52,0.41
20260820,348.5,379.5,348,379.5,737333,367.52,3.26,360.18,376.37,2.25
20260821,372,376,358.5,358.5,398303,366.77,-2.25,358.12,376.98,1.2
20260824,365,369,353,355,208689,365.79,-2.95,356.07,377.54,0.63
20260825,357,359,350.5,356.5,98417,365.01,-2.33,355.95,378.18,0.34
20260826,356.5,373.5,356.5,366,247608,365.09,0.25,357.07,378.78,0.98
20260827,372.5,395.5,371.5,383.5,604246,366.63,4.6,359.25,379.74,2.31
20260828,389,389.5,376,379,311715,367.66,3.08,360.77,380.67,1.21
20260831,383,386,367,367.5,255014,367.65,-0.04,361.55,380.87,0.99
20260901,370,371,365.5,370,185617,367.84,0.59,362.3,380.53,0.74
20260902,371.5,375,360,360,244293,367.19,-1.96,362.23,380.24,0.97
20260903,366.5,366.5,352,352,217617,365.92,-3.8,361.98,380.04,0.87
20260904,355,373,353.5,370,318974,366.26,1.02,362.73,380.53,1.23
20260907,380,403,370.5,395,670481,368.66,7.15,364.57,381.54,2.36
20260908,396,397.5,381,382.5,318908,369.81,3.43,365.75,382.15,1.1
20260909,391.5,395,383.5,386.5,297254,371.2,4.12,366.98,382.73,1.01
20260910,400,425,392,425,997569,375.68,13.13,369.98,383.88,2.94
20260911,436,436.5,412.5,414.5,1310142,378.92,9.39,372.35,384.84,3.31
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 79.36
- over_600_ratio: 74.75
- over_800_ratio: 73.49
- over_1000_ratio: 70.61
- over_400_change_1w: 0.55
- over_800_change_1w: -0.08
- over_1000_change_1w: -0.07
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,79.54,-0.72,74.75,-0.02,71.82,-0.01,0,False,False
20260703,79.46,-0.08,74.69,-0.06,71.77,-0.05,0,False,False
20260709,79.26,-0.2,74.48,-0.21,71.57,-0.2,0,False,False
20260717,79.14,-0.12,74.34,-0.14,71.43,-0.14,0,False,False
20260724,79.5,0.36,74.41,0.07,71.5,0.07,1,True,True
20260731,79.08,-0.42,74.21,-0.2,71.3,-0.2,0,False,False
20260807,79.01,-0.07,73.83,-0.38,70.94,-0.36,0,False,False
20260814,78.96,-0.05,73.77,-0.06,70.88,-0.06,0,False,False
20260821,78.91,-0.05,73.72,-0.05,70.83,-0.05,0,False,False
20260828,79.1,0.19,73.63,-0.09,70.74,-0.09,1,False,False
20260904,78.81,-0.29,73.57,-0.06,70.68,-0.06,0,False,False
20260911,79.36,0.55,73.49,-0.08,70.61,-0.07,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 7799 | 禾榮科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | first_seen | 1.事實發生日:115/07/15 2.研發新藥名稱或代號:B10 L-BPA注射液 3.用途:評估硼中子捕獲治療(BNCT)作為術前輔助治療局部晚期口腔癌的安全性和有效性 4.預計進行之所有研發階段:第一及第二期臨床試驗 5.目前進行中之研發階段(請說明目前之研發階段係屬提出申請/通過核准/ 不通過核准，若未通過者，請說明公司所面臨之風險及因應措施； 另請說明未來經營方向及已投入累積研發費用): (1)提出申請/ 通過核准/ 不通過核准/ 各期人體臨床試驗   (含期中分析)結果/發生其他影響新藥研發之重大事件：本   公司研發之B10 L-BPA注射液通過台灣衛生福利部食品藥物   管理署(TFDA)新藥臨床試驗(IND)審查，將啟動前輔助治療   局部晚期口腔癌之第一及第二期學術研究用人體臨床試驗。 (2)未通過目的事業主管機關許可、各期人體臨床試驗(含期中    分析)結果未達統計上顯著意義或發生其他影響新藥研發之    重大事件者，公司所面臨之風險及因應措施：    不適用。 (3)已通過目的事業主管機關許可、各期人體臨床試驗(含期中    分析)結果達統計上顯著意義或發生其他影響新藥研發之重    大事件者，未來經營方向：不適用。 (4)已投入之累積研發費用：因涉及未來市場行銷策略及授權資訊   ，為保障公司及投投資人權益，暫不予公開揭露。 6.將再進行之下一階段研發(請說明預計完成時間及預計應負擔之義務): (1)預計完成時間：實際時程將依台灣衛生福利部食品藥物管理署(TFDA)審核進度而定。 (2)預計應負擔之義務：不適用。 7.市場現況:在頭頸癌治療領域，針對局部晚期（Locally Advanced）  可手術切除腫瘤之患者，先透過術前輔助治療（Neoadjuvant  Therapy）達到手術前有效縮減腫瘤體積、提升手術切除率並保留 器官功能，一直是臨床上的重大挑戰。傳統的術前輔助治療，包括 誘導化療或同步放化療，常因全身性毒性副作用及對周邊健康組織 的潛在損傷，可能增加術後併發症或影響傷口癒合，在臨床應用中 面臨一定侷限。目前硼中子捕獲治療BNCT的臨床試驗絕大多數集中 在復發性或無法手術或難治性腫瘤，尚未有臨床試驗將BNCT用於術 前輔助治療，先進行有效縮減腫瘤體積，再執行手術切除腫瘤之療 法。根據現有的臨床研究數據顯示，硼中子捕獲療法BNCT具細胞級 精準殺傷的潛力；其中，口腔癌屬頭頸癌的一種癌種，有機會以此 類患者提供一項潛在療法之選擇。 從市場規模來看，頭頸癌每年全球新診斷病例達 170 萬例，其中 約有 30%-40%的患者屬於局部晚期，是術前輔助治療的目標群體， 此臨床應用可補足口腔癌治療期別與類型更全面之潛在市場。本次 研究將進一步評估BNCT作為術前輔助治療(Neoadjuvant Therapy) 策略之一，是否有機會協助部分腫瘤位置或範圍較具挑戰性的患者 ，透過腫瘤控制與後續外科手術整合，建立新的臨床應用方向。 8.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項): 學術型臨床試驗偏向以科學或醫療研究為主要目的，由醫療院所、學術單位或研究人員 主導進行，公司多為贊助者(Sponsor)，提供資源支持學研單位進行研究。 其臨床成果用途偏向學術發表、臨床指引修訂、醫療品質提升。 9.新藥開發時程長、投入經費高且未保證一定能成功，此等可能使投資面臨風險，投    資人應審慎判斷謹慎投資。:；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 7799 | 禾榮科 | 1 | 1 | 1 | 1 | 3 | first_seen | 首次上榜或資料有限，需後續確認。 |

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
