# INDIVIDUAL STOCK CHATGPT PACKET - 3661 世芯-KY

## Metadata
- generated_at: 2026-09-20 22:16:59 Asia/Taipei
- stock_id: 3661
- stock_name: 世芯-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 358
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3661_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3661_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3661_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3661_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3661_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3661_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3661_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3661.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3661.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3661.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3661.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3661_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3661_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3661_latest.md?ref=main

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
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- confidence_level: high
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
- open: 3390
- high: 3540
- low: 3380
- close: 3540
- volume: 5093871
- ma5: 3425
- ema23_primary: 3750.22
- distance_to_ema23_pct: -5.61
- ma20: 3856
- ma60: 3796.58
- ma120: 3951.12
- return_5d: -3.01
- return_20d: -4.32
- volume_ratio: 2.07
- distance_to_ma20_pct_auxiliary: -8.2
- distance_to_high_60_pct: -27.68

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,3730,3795,3680,3735,1136509,3746.3,-0.3,3609.5,3943.75,0.43
20260825,3700,3875,3665,3865,1236396,3756.19,2.9,3647,3934.58,0.48
20260826,3855,4045,3830,3960,2375440,3773.17,4.95,3704.75,3919.67,0.93
20260827,3970,3995,3870,3870,1513027,3781.24,2.35,3759,3907.92,0.61
20260828,3910,4105,3855,4065,2030269,3804.89,6.84,3809.25,3899.08,0.84
20260831,4015,4085,3900,4075,2040909,3827.4,6.47,3850.5,3894.67,0.85
20260901,4235,4350,4170,4275,2521101,3864.7,10.62,3894.75,3894.5,1.02
20260902,4260,4310,4180,4200,1632464,3892.64,7.9,3924.25,3895,0.67
20260903,4210,4260,4010,4050,1876714,3905.75,3.69,3943.75,3891.67,0.77
20260904,4155,4275,4110,4220,1757291,3931.94,7.33,3969,3894.67,0.73
20260907,4175,4180,4000,4040,3204560,3940.95,2.51,3981,3894.33,1.33
20260908,4090,4105,3985,4030,1620933,3948.37,2.07,3984.75,3893.08,0.72
20260909,3985,3990,3850,3905,3254166,3944.75,-1.01,3977.25,3887.33,1.4
20260910,3880,4075,3815,4055,2298103,3953.94,2.56,3970.5,3883,1
20260911,3870,3870,3650,3650,5595150,3928.61,-7.09,3942.5,3871.83,2.33
20260914,3410,3655,3410,3590,2098835,3900.39,-7.96,3919,3858.67,0.92
20260915,3535,3590,3335,3355,2699862,3854.94,-12.97,3901,3842.5,1.22
20260916,3385,3400,3310,3345,1986894,3812.45,-12.26,3886.75,3825.33,0.9
20260917,3365,3430,3260,3295,3207956,3769.33,-12.58,3864,3808.08,1.41
20260918,3390,3540,3380,3540,5093871,3750.22,-5.61,3856,3796.58,2.07
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 33.46
- over_600_ratio: 24.73
- over_800_ratio: 17.95
- over_1000_ratio: 10.7
- over_400_change_1w: -2.31
- over_800_change_1w: -2.19
- over_1000_change_1w: -2.03
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,37.38,1.36,19.94,1.34,13.38,-1.93,1,False,True
20260709,39.02,1.64,21.82,1.88,13.22,-0.16,2,False,True
20260717,37.41,-1.61,20.6,-1.22,16.49,3.27,3,False,True
20260724,36.2,-1.21,20.33,-0.27,17.19,0.7,4,False,True
20260731,35.42,-0.78,20.97,0.64,15.77,-1.42,5,False,True
20260807,36.31,0.89,22.51,1.54,16.31,0.54,6,False,True
20260814,36.61,0.3,21.82,-0.69,13.62,-2.69,7,False,False
20260821,35.84,-0.77,22.44,0.62,14.42,0.8,8,False,True
20260828,34.9,-0.94,20.19,-2.25,11.92,-2.5,0,False,False
20260904,37.51,2.61,21.64,1.45,13.2,1.28,1,True,True
20260911,35.77,-1.74,20.14,-1.5,12.73,-0.47,0,False,False
20260918,33.46,-2.31,17.95,-2.19,10.7,-2.03,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3661 | 世芯-KY | pullback_rebound | 回檔後短線轉強 | 83.0 |  |  |  |  | call_inflow | stale_signal | 1.事實發生日:115/09/17 2.公司名稱:英屬開曼群島商世芯電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:不適用 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): (一)英屬開曼群島商世芯電子股份有限公司於中華民國115年5月26日股東會決議發放 普通股現金股利88,275,709美元，依本公司中華民國115年9月11日配息基準日股東名 簿持有股數為86,305,114股，依中央銀行規定辦理匯兌，每股現金股利折合新台幣  32.57284607元。 (二)現金股利發放至元為止(元以下不計)，其畸零款合計數列入本公司之其他收入， 現金股利發放之匯款或支票處理費用由股東自行負擔。 (三)茲訂定中華民國115年10月8日為本公司現金股利之付款日，委由股務代理機構 中國信託商業銀行代理部(電話:02-66365566)以匯款或掛號郵寄支票方式發放。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |
| 20260918 | 3661 | 世芯-KY | revenue_pullback | 營收成長股價回檔 | 83.0 |  |  |  |  | call_inflow | stale_signal | 1.事實發生日:115/09/17 2.公司名稱:英屬開曼群島商世芯電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:不適用 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): (一)英屬開曼群島商世芯電子股份有限公司於中華民國115年5月26日股東會決議發放 普通股現金股利88,275,709美元，依本公司中華民國115年9月11日配息基準日股東名 簿持有股數為86,305,114股，依中央銀行規定辦理匯兌，每股現金股利折合新台幣  32.57284607元。 (二)現金股利發放至元為止(元以下不計)，其畸零款合計數列入本公司之其他收入， 現金股利發放之匯款或支票處理費用由股東自行負擔。 (三)茲訂定中華民國115年10月8日為本公司現金股利之付款日，委由股務代理機構 中國信託商業銀行代理部(電話:02-66365566)以匯款或掛號郵寄支票方式發放。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3661 | 世芯-KY | revenue_breakout_low_response | 營收爆發低反應股 | 12 | 53 | D_降級_TDCC轉弱 |  |  | call_inflow | stale_signal | 1.事實發生日:115/09/17 2.公司名稱:英屬開曼群島商世芯電子股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:不適用 6.因應措施:不適用 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): (一)英屬開曼群島商世芯電子股份有限公司於中華民國115年5月26日股東會決議發放 普通股現金股利88,275,709美元，依本公司中華民國115年9月11日配息基準日股東名 簿持有股數為86,305,114股，依中央銀行規定辦理匯兌，每股現金股利折合新台幣  32.57284607元。 (二)現金股利發放至元為止(元以下不計)，其畸零款合計數列入本公司之其他收入， 現金股利發放之匯款或支票處理費用由股東自行負擔。 (三)茲訂定中華民國115年10月8日為本公司現金股利之付款日，委由股務代理機構 中國信託商業銀行代理部(電話:02-66365566)以匯款或掛號郵寄支票方式發放。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3661 | 世芯-KY | 1 | 1 | 3 | 8 | 14 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3661 | 世芯-KY | 271 | 17 | 46853810.0 | 1364540.0 | 34.34 | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
