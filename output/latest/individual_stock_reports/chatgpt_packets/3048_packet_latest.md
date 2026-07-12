# INDIVIDUAL STOCK CHATGPT PACKET - 3048 益登

## Metadata
- generated_at: 2026-07-12 22:26:57 Asia/Taipei
- stock_id: 3048
- stock_name: 益登
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3048_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3048_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3048_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3048.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3048.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3048.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3048.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3048_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3048_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3048_latest.md?ref=main

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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260709
- open: 61
- high: 61.3
- low: 59.6
- close: 60
- volume: 1897212
- ma5: 61.8
- ema23_primary: 64.78
- distance_to_ema23_pct: -7.38
- ma20: 67.14
- ma60: 58.29
- ma120: 48.51
- return_5d: -6.69
- return_20d: -18.14
- volume_ratio: 0.21
- distance_to_ma20_pct_auxiliary: -10.64
- distance_to_high_60_pct: -26.74

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,73.2,76,71.5,75,32055691,64.9,15.56,68.37,49.04,1.43
20260612,76,77.9,72.5,73,35966873,65.58,11.32,69.22,49.59,1.57
20260615,73.5,76.7,72.6,73.5,21406739,66.24,10.96,70.03,50.13,1
20260616,74.2,75,71.1,71.1,10550107,66.64,6.69,70.78,50.6,0.5
20260617,70.5,73.2,69,72.6,6509417,67.14,8.13,71.32,51.15,0.32
20260618,72,75.5,71.8,73.5,11027285,67.67,8.62,71.61,51.73,0.53
20260622,74,74.4,72.3,72.4,8478065,68.06,6.37,71.5,52.3,0.42
20260623,72.6,72.8,69.1,69.3,7447514,68.17,1.66,71.3,52.82,0.4
20260624,68.3,69.7,67.3,69,4671911,68.24,1.12,71.1,53.35,0.26
20260625,69.7,70.1,66.2,67,5322986,68.13,-1.66,70.95,53.85,0.3
20260626,66.1,67.2,62.9,63,4947214,67.71,-6.95,70.49,54.31,0.3
20260629,63,63.9,61.2,61.6,3225243,67.2,-8.33,69.97,54.76,0.2
20260630,62.6,63.6,61.4,62.9,3318000,66.84,-5.89,69.69,55.23,0.22
20260701,64.3,68.8,64.2,65.7,11844000,66.74,-1.56,69.22,55.76,0.8
20260702,64,64.7,63.2,64.3,3074000,66.54,-3.37,68.97,56.26,0.23
20260703,63.8,64.9,63.3,64.4,2022463,66.36,-2.96,68.81,56.74,0.15
20260706,66,66.8,63.6,64.6,3881000,66.22,-2.44,68.72,57.23,0.3
20260707,64.2,64.6,60,60.5,3435576,65.74,-7.97,68.42,57.61,0.27
20260708,60.5,62.5,58.9,59.5,2932631,65.22,-8.77,67.81,57.94,0.26
20260709,61,61.3,59.6,60,1897212,64.78,-7.38,67.14,58.29,0.21
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 51.25
- over_600_ratio: 48.47
- over_800_ratio: 47.2
- over_1000_ratio: 45.88
- over_400_change_1w: -1.12
- over_800_change_1w: -1.62
- over_1000_change_1w: -0.97
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,45.89,,42.1,,40.12,,0,False,False
20260508,47.07,1.18,42.35,0.25,40.99,0.87,1,True,True
20260515,54.64,7.57,51.28,8.93,49.29,8.3,2,True,True
20260522,59.18,4.54,54.85,3.57,52.85,3.56,3,True,True
20260529,58.09,-1.09,53.71,-1.14,51.4,-1.45,0,False,False
20260605,52.16,-5.93,48.7,-5.01,46.7,-4.7,0,False,False
20260612,52.97,0.81,49.63,0.93,47.2,0.5,1,True,True
20260618,52.07,-0.9,47.87,-1.76,45.52,-1.68,0,False,False
20260626,52.37,0.3,48.82,0.95,46.85,1.33,1,True,True
20260703,51.25,-1.12,47.2,-1.62,45.88,-0.97,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3048 | 益登 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | call_strong_inflow | stale_signal | 1.證券名稱: 蜜望實企業股份有限公司普通股(8043) 2.交易日期:115/7/2~115/7/7 3.董事會通過日期: 民國115年5月13日 4.其他核決日期: 不適用 5.交易數量、每單位價格及交易總金額: 交易數量(股):1,546,000  每股平均價格(新台幣元): 202.88 交易總金額(新台幣元):313,650,500 6.處分利益（或損失）（取得有價證券者不適用）: 本次處分為出售透過其他綜合損益按公允價值衡量之金融資產， 處分結果將計入資產負債表之權益項下，不影響本公司當期損益。 7.與交易標的公司之關係: 無。 8.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、持股 比例及權利受限情形（如質押情形）: 數量：4,102,398股 金額：284,296仟元 持股比例：5.13% 權利受限情形：無。 9.迄目前為止，依「公開發行公司取得或處分資產處理準則」第三條所列之有價證券投 資（含本次交易）占公司最近期財務報表中總資產及歸屬於母公司業主之權益之比例 暨最近期財務報表中營運資金數額: 占總資產比例：3.52%    占母公司業主權益比例：21.27%     營運資金：6,603,994仟元 10.取得或處分之具體目的: 財務投資。 11.本次交易表示異議董事之意見: 無。 12.本次交易為關係人交易: 否 13.交易相對人及其與公司之關係: 不適用。 14.監察人承認或審計委員會同意日期: 民國 115年 5月 13日 15.前已就同一件事件發布重大訊息日期: 不適用 16.其他敘明事項: 無。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3048 | 益登 | 21 | 6 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 3048 | 益登 | 27 | 1 | 3413160.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
