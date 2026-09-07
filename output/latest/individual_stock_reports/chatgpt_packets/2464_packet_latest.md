# INDIVIDUAL STOCK CHATGPT PACKET - 2464 盟立

## Metadata
- generated_at: 2026-09-06 22:16:26 Asia/Taipei
- stock_id: 2464
- stock_name: 盟立
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2464_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2464_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2464_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2464_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2464_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2464_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2464_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2464.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2464.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2464.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2464.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2464_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2464_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2464_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260904
- open: 223.5
- high: 224
- low: 203
- close: 211
- volume: 54753350
- ma5: 199.9
- ema23_primary: 187.67
- distance_to_ema23_pct: 12.43
- ma20: 191.5
- ma60: 169.44
- ma120: 139.59
- return_5d: 11.05
- return_20d: 21.61
- volume_ratio: 2.9
- distance_to_ma20_pct_auxiliary: 10.18
- distance_to_high_60_pct: -5.8

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,175,186,173.5,180,16706927,156.19,15.25,150.2,158.69,1.84
20260811,180,196,176,187.5,26698078,158.79,18.08,151.62,159.71,2.68
20260812,185.5,205,185.5,196.5,29018273,161.94,21.34,153.47,160.67,2.6
20260813,198,200.5,192,196,17203571,164.78,18.95,155.4,161.68,1.46
20260814,197,198,189.5,192,10004505,167.04,14.94,157.85,162.81,0.84
20260817,197,208,183.5,186,22801999,168.62,10.3,160.43,163.64,1.79
20260818,190,199.5,174.5,178,18539197,169.41,5.07,162.32,164.21,1.38
20260819,172,190,172,181.5,16897448,170.41,6.51,163.85,164.6,1.21
20260820,183,189,176,180.5,12488934,171.25,5.4,165.45,164.72,0.87
20260821,181.5,181.5,173,179,5601206,171.9,4.13,167.07,164.75,0.39
20260824,177,191,175,187.5,11959456,173.2,8.26,169.32,165.07,0.81
20260825,186,193,182,193,14180408,174.85,10.38,172.43,165.22,0.92
20260826,193,194,187.5,192,10392650,176.28,8.92,175.88,165.1,0.67
20260827,194.5,211,194.5,211,13229763,179.17,17.76,180.3,165.53,0.83
20260828,216.5,216.5,190,190,25845387,180.07,5.51,183.07,165.78,1.52
20260831,185,187,175,180,15626012,180.07,-0.04,184.7,165.94,0.89
20260901,183.5,188,177,184.5,10411363,180.44,2.25,185.82,166.27,0.6
20260902,181.5,202,181.5,202,27613956,182.23,10.85,187.43,167.16,1.55
20260903,215,222,214,222,17067426,185.55,19.65,189.62,168.36,0.98
20260904,223.5,224,203,211,54753350,187.67,12.43,191.5,169.44,2.9
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 55.67
- over_600_ratio: 51.49
- over_800_ratio: 49.21
- over_1000_ratio: 48.46
- over_400_change_1w: -0.16
- over_800_change_1w: -1.37
- over_1000_change_1w: -0.52
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,41.33,-3.02,36.09,-3.1,34.78,-2.78,0,False,False
20260626,40.02,-1.31,32.85,-3.24,31.14,-3.64,0,False,False
20260703,45.98,5.96,39.41,6.56,37.72,6.58,1,True,True
20260709,41.03,-4.95,35.33,-4.08,34.13,-3.59,0,False,False
20260717,39.37,-1.66,34.35,-0.98,33.05,-1.08,0,False,False
20260724,39.21,-0.16,34.28,-0.07,34.28,1.23,1,False,True
20260731,39.24,0.03,34.61,0.33,33.37,-0.91,2,False,True
20260807,44.42,5.18,40.24,5.63,38.2,4.83,3,True,True
20260814,50.84,6.42,46.34,6.1,45.51,7.31,4,True,True
20260821,50.7,-0.14,45.43,-0.91,45.06,-0.45,0,False,False
20260828,55.83,5.13,50.58,5.15,48.98,3.92,1,True,True
20260904,55.67,-0.16,49.21,-1.37,48.46,-0.52,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2464 | 盟立 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_put_bullish | stale_signal | 1.董事會決議日期:NA 2.名稱﹝XX公司第X次（有、無）擔保公司債﹞:  盟立自動化股份有限公司國內第三次無擔保轉換公司債 3.是否採總括申報發行公司債(是/否):否 4.發行總額:發行總面額上限新台幣1,000,000仟元 5.每張面額:新台幣10萬元整 6.發行價格:每股新台幣114.07元。 7.發行期間:3年 8.發行利率:票面利率為0% 9.擔保品之種類、名稱、金額及約定事項:不適用。 10.募得價款之用途及運用計畫:償還銀行借款及充實營運資金。 11.承銷方式:採競價拍賣方式辦理公開承銷。 12.公司債受託人:台北富邦商業銀行股份有限公司。 13.承銷或代銷機構:中國信託綜合證券股份有限公司 14.發行保證人:係無擔保轉換公司債，故不適用。 15.代理還本付息機構:中國信託商業銀行股份有限公司代理部。 16.簽證機構:本次係發行無實體債券，故不適用。 17.能轉換股份者，其轉換辦法:相關辦法將依相關法令規定辦理， 俟呈報主管機關申報生效後另行公告。 18.賣回條件:相關辦法將依相關法令規定辦理，俟呈報主管機關 申報生效後另行公告。 19.買回條件:相關辦法將依相關法令規定辦理，俟呈報主管機關 申報生效後另行公告。 20.附有轉換、交換或認股者，其換股基準日:相關辦法將依相關 法令規定辦理，俟呈報主管機關申報生效後另行公告。 21.附有轉換、交換或認股者，對股權可能稀釋情形:相關辦法將 依相關法令規定辦理，俟呈報主管機關申報生效後另行公告。 22.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 23.其他應敘明事項: (1)因資本市場籌資環境變化快速，為掌握訂定發行條件及實際發    行作業之時效，本次募集與發行國內第三次無擔保轉換公司債    籌資計畫有關發行時程、承銷方式、發行額度、發行價格、    發行條件、發行及轉換辦法之訂定，以及資金運用計畫項目、    資金來源、預計資金運用進度、預計可能產生效益及其他相關    事宜，如經主管機關指示、相關法令規則修正或因應金融市場    狀況或客觀環境需修訂或修正時，授權董事長全權處理之。 (2)授權本公司董事長代表本公司簽署一切有關發行國內第三次無    擔保轉換公司債契約及文件，並代表本公司辦理相關發行事宜。 (3)本次發行如有未盡事宜，授權董事長全權處理之。；calendar event: ex_right_dividend on 20260902; status=confirmed; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2464 | 盟立 | 7 | 1 | 5 | 9 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2464 | 盟立 | 115 | 5 | 33610300.0 | 764150.0 | 43.98 | call_put_bullish |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
