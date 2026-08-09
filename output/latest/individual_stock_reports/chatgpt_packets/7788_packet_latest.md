# INDIVIDUAL STOCK CHATGPT PACKET - 7788 松川精密

## Metadata
- generated_at: 2026-08-09 22:28:49 Asia/Taipei
- stock_id: 7788
- stock_name: 松川精密
- packet_status: standard_180d_window_packet
- latest_price_date: 20260805
- price_rows: 193
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
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/7788_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/7788_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/7788_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7788_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7788_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/7788_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/7788_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/7788.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/7788.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/7788.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/7788.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/7788_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/7788_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/7788_latest.md?ref=main

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
- date: 20260805
- open: 208
- high: 215
- low: 205.5
- close: 210
- volume: 1060141
- ma5: 193.8
- ema23_primary: 218.57
- distance_to_ema23_pct: -3.92
- ma20: 224.38
- ma60: 227.5
- ma120: 194.09
- return_5d: 12.9
- return_20d: -9.68
- volume_ratio: 0.59
- distance_to_ma20_pct_auxiliary: -6.41
- distance_to_high_60_pct: -31.26

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260708,238,244.5,231,242.5,874059,244.98,-1.01,260.48,209.38,0.33
20260709,256,259.5,250,250.5,2579844,245.44,2.06,260.07,211.12,1
20260713,258.5,264.5,250,259,2252773,246.57,5.04,259.48,212.89,0.97
20260714,258,277.5,255.5,273,5803949,248.77,9.74,259.82,214.92,2.4
20260715,274.5,274.5,260,269.5,2715427,250.5,7.58,260.5,216.69,1.14
20260716,266,271.5,260.5,261,1293955,251.37,3.83,259.85,218.26,0.58
20260717,250.5,256.5,235,235,5342296,250.01,-6,257.85,219.42,2.27
20260720,235,240,220,233,1965298,248.59,-6.27,254.9,220.48,0.87
20260721,236.5,237.5,223,229,1014061,246.96,-7.27,252.28,221.47,0.47
20260722,230,244,230,239.5,1265729,246.34,-2.78,250.32,222.63,0.6
20260723,242.5,243,229.5,230,728269,244.98,-6.11,248.57,223.66,0.36
20260724,228.5,229,205.5,207,1891942,241.81,-14.4,246.18,224.33,0.92
20260727,207,213.5,204,207.5,666921,238.95,-13.16,244.05,224.91,0.33
20260728,201.5,203,195,196,822821,235.37,-16.73,240.5,225.4,0.42
20260729,199.5,199.5,180,186,1557061,231.26,-19.57,236.95,225.72,0.84
20260730,184.5,188.5,171.5,173.5,1413971,226.45,-23.38,232.93,225.81,0.77
20260731,190.5,190.5,183,189.5,832048,223.37,-15.16,229.97,226.23,0.45
20260803,187.5,200,185,192.5,863877,220.79,-12.81,227.28,226.58,0.47
20260804,189,204,188.5,203.5,938106,219.35,-7.23,225.5,227.04,0.52
20260805,208,215,205.5,210,1060141,218.57,-3.92,224.38,227.5,0.59
```

## Latest TDCC Snapshot
- as_of_date: 20260807
- over_400_ratio: 70.23
- over_600_ratio: 62.32
- over_800_ratio: 60.81
- over_1000_ratio: 56.53
- over_400_change_1w: -0.86
- over_800_change_1w: -0.42
- over_1000_change_1w: -0.37
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260522,77.77,1.46,66.97,1.04,62.65,1.14,1,True,True
20260529,77.21,-0.56,67.07,0.1,62.84,0.19,2,False,True
20260605,74.91,-2.3,65.22,-1.85,62,-0.84,0,False,False
20260612,75.61,0.7,65.34,0.12,63.13,1.13,1,True,True
20260618,72.92,-2.69,63.5,-1.84,61.29,-1.84,0,False,False
20260626,71.57,-1.35,62.67,-0.83,59.22,-2.07,0,False,False
20260703,70.54,-1.03,59.33,-3.34,57.12,-2.1,0,False,False
20260709,69.74,-0.8,59.33,0,57.12,0,0,False,False
20260717,69.47,-0.27,59.33,0,57.12,0,0,False,False
20260724,69.56,0.09,60,0.67,55.69,-1.43,1,False,True
20260731,71.09,1.53,61.23,1.23,56.9,1.21,2,True,True
20260807,70.23,-0.86,60.81,-0.42,56.53,-0.37,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 7788 | 松川精密 | revenue_pullback | 營收成長股價回檔 | 77.0 |  |  |  |  | no_signal | stale_signal | 1.董事會、股東會決議或公司決定日期:115/07/07 2.除權、息類別（請填入「除權」、「除息」或「除權息」）:除息 3.普通股發放股利種類及金額:現金股利新台幣159,491,986元，每股配發新台幣2元。 4.除權（息）交易日:115/07/24 5.最後過戶日:115/07/27 6.停止過戶起始日期:115/07/28 7.停止過戶截止日期:115/08/01 8.除權（息）基準日:115/08/01 9.債券最後申請轉換日期:不適用 10.債券停止轉換起始日期:不適用 11.債券停止轉換截止日期:不適用 12.普通股現金股利發放日期:115/08/21 13.現金股利之一部或全部是否以外幣發放(請填入「是」或「否」):否 14.外幣現金股利發放幣別:不適用 15.外幣現金股利發放對象:不適用 16.外幣現金股利匯率決定方式:不適用 17.其他應敘明事項:無；calendar event: ex_dividend on 20260724; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 7788 | 松川精密 | 2 | 2 | 4 | 7 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 7788 | 松川精密 | 36 | 1 | 8670430.0 | 840.0 | 10321.94 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
