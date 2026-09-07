# INDIVIDUAL STOCK CHATGPT PACKET - 2347 聯強

## Metadata
- generated_at: 2026-09-06 22:16:17 Asia/Taipei
- stock_id: 2347
- stock_name: 聯強
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2347_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2347_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2347_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2347_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2347_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2347_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2347_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2347.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2347.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2347.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2347.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2347_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2347_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2347_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- open: 87.2
- high: 88.4
- low: 86.7
- close: 88
- volume: 5869385
- ma5: 86.96
- ema23_primary: 88.02
- distance_to_ema23_pct: -0.02
- ma20: 88.14
- ma60: 89.54
- ma120: 86.17
- return_5d: 1.73
- return_20d: -5.78
- volume_ratio: 1.79
- distance_to_ma20_pct_auxiliary: -0.15
- distance_to_high_60_pct: -10.48

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,93.4,93.7,91.2,91.9,3323865,90.46,1.59,88.96,89.04,0.57
20260811,91.4,91.5,89.4,91,5287542,90.5,0.55,89.36,89.18,0.95
20260812,91,93.5,91,91.6,5781330,90.6,1.11,89.58,89.35,1.06
20260813,91.6,92.3,90.9,91.5,3182215,90.67,0.91,89.78,89.5,0.6
20260814,91.8,92,89.8,90.9,2959675,90.69,0.23,90.06,89.62,0.59
20260817,90.5,91.3,87.6,88.8,4419207,90.53,-1.91,90.31,89.69,0.93
20260818,88.4,88.5,86,86,3645276,90.15,-4.61,90.34,89.72,0.79
20260819,86.1,86.6,85.1,86.3,2827204,89.83,-3.93,90.25,89.76,0.65
20260820,87.5,87.6,85.4,87,4537016,89.6,-2.9,90.2,89.8,1.04
20260821,86.6,88.2,86.2,87.5,1748499,89.42,-2.15,90.15,89.83,0.41
20260824,86.6,89.4,86.6,88.3,1514672,89.33,-1.15,90.14,89.87,0.36
20260825,87.7,87.9,86.4,86.7,2231135,89.11,-2.7,90.17,89.88,0.53
20260826,87.2,87.8,86.8,87.1,1544628,88.94,-2.07,90.25,89.89,0.38
20260827,87.7,87.7,86.6,86.8,2015344,88.76,-2.21,90.29,89.81,0.5
20260828,86.8,87.9,86,86.5,1841582,88.58,-2.34,89.93,89.74,0.53
20260831,86.1,87,85.1,87,3095127,88.44,-1.63,89.69,89.69,0.88
20260901,86.4,87.4,85.6,86,4443086,88.24,-2.54,89.31,89.65,1.23
20260902,86,88.1,85.7,87.4,2624324,88.17,-0.87,88.82,89.69,0.78
20260903,87.1,87.7,86.2,86.4,2677469,88.02,-1.84,88.41,89.61,0.83
20260904,87.2,88.4,86.7,88,5869385,88.02,-0.02,88.14,89.54,1.79
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 88.77
- over_600_ratio: 87.25
- over_800_ratio: 86.23
- over_1000_ratio: 85.1
- over_400_change_1w: -0.02
- over_800_change_1w: -0.15
- over_1000_change_1w: -0.22
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,88.8,0.09,86.15,0,85.08,0.05,7,False,True
20260626,89.05,0.25,86.38,0.23,85.36,0.28,8,True,True
20260703,89.13,0.08,86.36,-0.02,85.39,0.03,9,False,True
20260709,89.15,0.02,86.49,0.13,85.42,0.03,10,True,True
20260717,88.9,-0.25,86.4,-0.09,85.38,-0.04,0,False,False
20260724,88.99,0.09,86.54,0.14,85.42,0.04,1,True,True
20260731,89.07,0.08,86.59,0.05,85.36,-0.06,2,False,True
20260807,89.25,0.18,86.7,0.11,85.69,0.33,3,True,True
20260814,89.14,-0.11,86.68,-0.02,85.63,-0.06,0,False,False
20260821,88.88,-0.26,86.44,-0.24,85.44,-0.19,0,False,False
20260828,88.79,-0.09,86.38,-0.06,85.32,-0.12,1,False,False
20260904,88.77,-0.02,86.23,-0.15,85.1,-0.22,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2347 | 聯強 | pullback_rebound | 回檔後短線轉強 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/31 2.接受資金貸與之: (1)公司名稱:聯強國際股份有限公司 (2)與資金貸與他人公司之關係: 為本公司之母公司 (3)資金貸與之限額(仟元):83,570,542 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):25,320,000 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):25,320,000 (8)本次新增資金貸與之原因: 營運週轉 3.接受資金貸與公司所提供擔保品之: (1)內容: 不適用 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):16,679,470 (2)累積盈虧金額(仟元):59,049,365 5.計息方式: 不計息 6.還款之: (1)條件: 可視資金狀況隨時還款 (2)日期: 可視資金狀況隨時還款 7.迄事實發生日為止，資金貸與餘額(仟元): 153,554,103 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 177.39 9.公司貸與他人資金之來源: 子公司本身、金融機構 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent |
| 20260904 | 2347 | 聯強 | revenue_pullback | 營收成長股價回檔 | 70.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/08/31 2.接受資金貸與之: (1)公司名稱:聯強國際股份有限公司 (2)與資金貸與他人公司之關係: 為本公司之母公司 (3)資金貸與之限額(仟元):83,570,542 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):25,320,000 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):25,320,000 (8)本次新增資金貸與之原因: 營運週轉 3.接受資金貸與公司所提供擔保品之: (1)內容: 不適用 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):16,679,470 (2)累積盈虧金額(仟元):59,049,365 5.計息方式: 不計息 6.還款之: (1)條件: 可視資金狀況隨時還款 (2)日期: 可視資金狀況隨時還款 7.迄事實發生日為止，資金貸與餘額(仟元): 153,554,103 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 177.39 9.公司貸與他人資金之來源: 子公司本身、金融機構 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260904 | 2347 | 聯強 | revenue_breakout_low_response | 營收爆發低反應股 | 18 | 32 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/08/31 2.接受資金貸與之: (1)公司名稱:聯強國際股份有限公司 (2)與資金貸與他人公司之關係: 為本公司之母公司 (3)資金貸與之限額(仟元):83,570,542 (4)原資金貸與之餘額(仟元):0 (5)本次新增資金貸與之金額(仟元):25,320,000 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):25,320,000 (8)本次新增資金貸與之原因: 營運週轉 3.接受資金貸與公司所提供擔保品之: (1)內容: 不適用 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):16,679,470 (2)累積盈虧金額(仟元):59,049,365 5.計息方式: 不計息 6.還款之: (1)條件: 可視資金狀況隨時還款 (2)日期: 可視資金狀況隨時還款 7.迄事實發生日為止，資金貸與餘額(仟元): 153,554,103 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 177.39 9.公司貸與他人資金之來源: 子公司本身、金融機構 10.其他應敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2347 | 聯強 | 15 | 15 | 5 | 10 | 19 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2347 | 聯強 | 7 | 0 | 881280.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
