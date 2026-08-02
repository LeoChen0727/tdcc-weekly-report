# INDIVIDUAL STOCK CHATGPT PACKET - 8422 可寧衛*

## Metadata
- generated_at: 2026-08-01 22:29:09 Asia/Taipei
- stock_id: 8422
- stock_name: 可寧衛*
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 308
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8422_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8422_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8422_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8422_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8422.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8422.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8422.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8422.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8422_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8422_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8422_latest.md?ref=main

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
- date: 20260730
- open: 24.55
- high: 24.65
- low: 24.2
- close: 24.35
- volume: 6085380
- ma5: 25.16
- ema23_primary: 26.33
- distance_to_ema23_pct: -7.51
- ma20: 26.4
- ma60: 27.28
- ma120: 29.29
- return_5d: -7.24
- return_20d: -9.81
- volume_ratio: 0.57
- distance_to_ma20_pct_auxiliary: -7.77
- distance_to_high_60_pct: -23.06

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,27.1,27.4,26.7,26.8,10432981,28.01,-4.31,28.36,28.11,0.6
20260703,26.6,29.45,26.5,28.35,48454855,28.03,1.12,28.36,28.08,2.54
20260706,28.6,29.8,28.4,28.6,22870629,28.08,1.85,28.39,28.07,1.17
20260707,28.6,28.8,27.8,27.8,13947173,28.06,-0.92,28.43,28.05,0.71
20260708,28,28.15,27.2,27.3,9729554,28,-2.48,28.32,28.02,0.51
20260709,27.2,27.2,26.85,27,6712946,27.91,-3.27,28.16,27.99,0.46
20260713,27.1,27.15,26.4,26.55,11249130,27.8,-4.49,28.02,27.94,0.82
20260714,26.65,26.65,25.5,26.05,11686969,27.65,-5.8,27.87,27.88,0.86
20260715,26.15,26.6,26.05,26.45,3789943,27.55,-4,27.76,27.83,0.29
20260716,26.45,27,26.4,27,4081852,27.51,-1.84,27.7,27.78,0.32
20260717,26.7,26.75,25.85,25.85,8952661,27.37,-5.55,27.57,27.71,0.7
20260720,26,26.25,25.3,25.8,7661803,27.24,-5.28,27.46,27.64,0.61
20260721,26.2,26.5,25.95,26.4,4691732,27.17,-2.83,27.33,27.59,0.39
20260722,26.4,26.8,26,26,5478347,27.07,-3.96,27.18,27.55,0.46
20260723,26.2,26.25,25.9,26.25,4586921,27,-2.79,27.06,27.52,0.39
20260724,26.2,26.35,25.9,26,3340099,26.92,-3.41,26.95,27.48,0.29
20260727,26.25,26.25,25.4,25.7,6647823,26.82,-4.17,26.82,27.44,0.6
20260728,25.45,25.45,24.85,24.95,9958524,26.66,-6.42,26.69,27.4,0.89
20260729,24.8,25.1,24.05,24.8,12381167,26.51,-6.44,26.53,27.34,1.09
20260730,24.55,24.65,24.2,24.35,6085380,26.33,-7.51,26.4,27.28,0.57
```

## Latest TDCC Snapshot
- as_of_date: 20260731
- over_400_ratio: 36.92
- over_600_ratio: 35.02
- over_800_ratio: 34.06
- over_1000_ratio: 33.36
- over_400_change_1w: -0.1
- over_800_change_1w: -0.28
- over_1000_change_1w: -0.23
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260515,38.73,-0.13,36.2,-0.27,35.73,-0.01,0,False,False
20260522,38.88,0.15,36.43,0.23,35.69,-0.04,1,False,True
20260529,38.93,0.05,36.44,0.01,35.83,0.14,2,False,True
20260605,39.16,0.23,36.36,-0.08,35.75,-0.08,3,False,False
20260612,38.41,-0.75,35.7,-0.66,34.9,-0.85,0,False,False
20260618,38.08,-0.33,35.34,-0.36,34.72,-0.18,0,False,False
20260626,37.64,-0.44,34.86,-0.48,34.18,-0.54,0,False,False
20260703,37.35,-0.29,34.72,-0.14,33.7,-0.48,0,False,False
20260709,37.44,0.09,34.89,0.17,34.07,0.37,1,True,True
20260717,36.9,-0.54,34.34,-0.55,33.58,-0.49,0,False,False
20260724,37.02,0.12,34.34,0,33.59,0.01,1,False,True
20260731,36.92,-0.1,34.06,-0.28,33.36,-0.23,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8422 | 可寧衛* | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議日期: 115/07/02 2.名稱﹝XX公司第X次（有、無）擔保公司債﹞: 可寧衛股份有限公司國內第三次無擔保轉換公司債 3.是否採總括申報發行公司債(是/否): 否 4.發行總額: 發行總面額上限為新台幣25億元整 5.每張面額: 新台幣10萬元整 6.發行價格: 底標不低於面額之100%發行，實際發行價格依競價拍賣結果而定。 7.發行期間: 5年 8.發行利率: 票面年利率0% 9.擔保品之種類、名稱、金額及約定事項: 不適用 10.募得價款之用途及運用計畫: 轉投資子公司及償還銀行借款 11.承銷方式: 以競價拍賣方式辦理公開銷售，授權董事長或其指定人員與主辦承銷商共同議定。 12.公司債受託人: 中國信託商業銀行股份有限公司 13.承銷或代銷機構: 中國信託綜合證券股份有限公司 14.發行保證人: 不適用 15.代理還本付息機構: 本公司股務代理機構台新綜合證券股份有限公司股務代理部 16.簽證機構: 本次國內第三次無擔保轉換公司債採無實體發行，故不適用。 17.能轉換股份者，其轉換辦法: 相關辦法將依有關法令規定辦理，並報奉主管機關核准後另行公告。 18.賣回條件: 相關辦法將依有關法令規定辦理，並報奉主管機關核准後另行公告。 19.買回條件: 相關辦法將依有關法令規定辦理，並報奉主管機關核准後另行公告。 20.附有轉換、交換或認股者，其換股基準日: 相關辦法將依有關法令規定辦理，並報奉主管機關核准後另行公告。 21.附有轉換、交換或認股者，對股權可能稀釋情形: 相關辦法將依有關法令規定辦理，並報奉主管機關核准後另行公告。 22.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用): 不適用 23.其他應敘明事項: (1)國內第三次無擔保轉換公司債於主管機關申報生效後，授權董事長另訂發行日，    並向財團法人中華民國證券櫃檯買賣中心申請櫃檯買賣。 (2)因資本市場籌資環境變化快速，為掌握訂定發行條件與實際發行作業時效，    國內第三次無擔保轉換公司債等籌資計畫有關之發行金額、發行條件、    發行及轉換辦法之訂定，以及計畫所需資金總額、資金來源、計畫項目、    資金運用進度、預計可能產生效益及其他相關事宜，如經主管機關指示，    相關法令規則修正，或因應客觀環境需修訂或修正時，授權董事長或    其指定人員全權處理之。 (3)為配合國內第三次無擔保轉換公司債籌資計畫之發行作業，授權本公司董事長    或其指定人員核可並代表本公司簽署一切有關發行國內第三次無擔保轉換公司債    之契約文件，並代表本公司辦理相關發行事宜。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8422 | 可寧衛* | 2 | 2 | 4 | 9 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8422 | 可寧衛* | 62 | 8 | 302010.0 | 7300.0 | 41.37 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
