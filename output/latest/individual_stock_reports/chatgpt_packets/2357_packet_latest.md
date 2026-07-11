# INDIVIDUAL STOCK CHATGPT PACKET - 2357 華碩

## Metadata
- generated_at: 2026-07-11 22:26:37 Asia/Taipei
- stock_id: 2357
- stock_name: 華碩
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2357_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2357_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2357_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2357_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2357.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2357.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2357.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2357.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2357_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2357_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2357_latest.md?ref=main

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
- open: 688
- high: 699
- low: 675
- close: 684
- volume: 4811935
- ma5: 677.8
- ema23_primary: 719.57
- distance_to_ema23_pct: -4.94
- ma20: 732.65
- ma60: 699.9
- ma120: 618.84
- return_5d: 2.55
- return_20d: -14.07
- volume_ratio: 0.89
- distance_to_ma20_pct_auxiliary: -6.64
- distance_to_high_60_pct: -29.05

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,791,802,769,784,5245169,765.57,2.41,760.6,649.42,0.79
20260612,791,805,780,785,4371037,767.18,2.32,767.8,652.62,0.67
20260615,803,804,783,792,3780033,769.25,2.96,775.65,655.92,0.58
20260616,794,800,786,791,4159548,771.06,2.59,783.1,659.47,0.64
20260617,790,803,782,803,3336854,773.73,3.78,791.25,663.15,0.52
20260618,807,810,789,789,7939182,775,1.81,797.9,666.92,1.2
20260622,793,806,788,788,3442620,776.08,1.54,803.2,670.63,0.53
20260623,799,819,783,785,6495537,776.83,1.05,807,674.3,1
20260624,775,783,764,771,5156891,776.34,-0.69,810.6,677.58,0.79
20260625,770,773,743,748,6101570,773.98,-3.36,812.95,680.43,0.92
20260626,730,735,700,701,7061186,767.9,-8.71,813.4,682.75,1.05
20260629,702,710,694,703,4626002,762.49,-7.8,810.5,685.32,0.74
20260630,705,711,691,700,7215000,757.28,-7.56,803.65,687.53,1.13
20260701,658,659,635,657,12965000,748.92,-12.27,790.5,689.23,2
20260702,650,667,642,667,5882000,742.1,-10.12,777.3,691.18,0.96
20260703,660,675,657,675,3325491,736.51,-8.35,766.45,693.07,0.56
20260706,681,689,672,680,3215000,731.8,-7.08,755.45,694.93,0.57
20260707,681,681,661,663,3751073,726.06,-8.69,746.4,696.35,0.68
20260708,675,687,670,687,4853620,722.81,-4.95,738.25,698.17,0.89
20260709,688,699,675,684,4811935,719.57,-4.94,732.65,699.9,0.89
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 72.39
- over_600_ratio: 68.88
- over_800_ratio: 65.85
- over_1000_ratio: 62.72
- over_400_change_1w: -0.73
- over_800_change_1w: -1.07
- over_1000_change_1w: -0.33
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.93,,65.12,,61.87,,0,False,False
20260508,71.4,0.47,65.52,0.4,61.93,0.06,1,True,True
20260515,72.15,0.75,66.6,1.08,62.38,0.45,2,True,True
20260522,72.13,-0.02,66.11,-0.49,62.38,0,0,False,False
20260529,72.95,0.82,66.94,0.83,62.85,0.47,1,True,True
20260605,74.56,1.61,68.53,1.59,64.27,1.42,2,True,True
20260612,73.95,-0.61,68.37,-0.16,64.4,0.13,3,False,True
20260618,73.92,-0.03,67.75,-0.62,64.01,-0.39,0,False,False
20260626,73.12,-0.8,66.92,-0.83,63.05,-0.96,0,False,False
20260703,72.39,-0.73,65.85,-1.07,62.72,-0.33,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2357 | 華碩 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | no_signal | stale_signal | 1.董事會決議日期:115/07/10 2.減資緣由:考量公司營運需求，調整資本結構並返還股款。 3.減資金額:巴西幣340,000,000元。 4.消除股份:340,000,000股。 5.減資比率:61.88%。 6.減資後股本:巴西幣209,469,000元。 7.預定股東會日期:115/07/10 8.預計減資新股上市後之上市普通股股數:不適用。 9.預計減資新股上市後之上市普通股股數占已發行普通股比率 （減資後上市普通股股數/減資後已發行普通股股數）:不適用。 10.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用。 11.減資基準日:待當地主管機關核准註冊變更生效後完成。 12.其他應敘明事項: (1)ACBZ以股東會代董事會通過決議。 (2)ACBZ係華碩間接100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260709 | 2357 | 華碩 | revenue_breakout_low_response | 營收爆發低反應股 | 10.0 | 35.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.董事會決議日期:115/07/10 2.減資緣由:考量公司營運需求，調整資本結構並返還股款。 3.減資金額:巴西幣340,000,000元。 4.消除股份:340,000,000股。 5.減資比率:61.88%。 6.減資後股本:巴西幣209,469,000元。 7.預定股東會日期:115/07/10 8.預計減資新股上市後之上市普通股股數:不適用。 9.預計減資新股上市後之上市普通股股數占已發行普通股比率 （減資後上市普通股股數/減資後已發行普通股股數）:不適用。 10.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者， 請說明股權流通性偏低之因應措施:不適用。 11.減資基準日:待當地主管機關核准註冊變更生效後完成。 12.其他應敘明事項: (1)ACBZ以股東會代董事會通過決議。 (2)ACBZ係華碩間接100%持股之重要子公司。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2357 | 華碩 | 2 | 1 | 2 | 2 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2357 | 華碩 | 92 | 5 | 7021090.0 | 142740.0 | 49.19 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
