# INDIVIDUAL STOCK CHATGPT PACKET - 6831 邁科

## Metadata
- generated_at: 2026-07-01 22:28:39 Asia/Taipei
- stock_id: 6831
- stock_name: 邁科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260701
- price_rows: 143
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6831_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6831_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6831_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6831_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6831_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6831_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6831_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6831.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6831.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6831.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6831.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6831_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6831_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6831_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260701
- open: 948
- high: 955
- low: 877
- close: 903
- volume: 2174000
- ma5: 849.6
- ema23_primary: 783.1
- distance_to_ema23_pct: 15.31
- ma20: 778.3
- ma60: 651.65
- ma120: 472.06
- return_5d: 5.99
- return_20d: 31.63
- volume_ratio: 1.57
- distance_to_ma20_pct_auxiliary: 16.02
- distance_to_high_60_pct: -5.45

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260603,701,743,680,726,2295577,690.34,5.17,717.2,512.45,1.37
20260604,716,736,712,721,646992,692.9,4.06,725.3,520.02,0.41
20260605,721,750,701,739,1601126,696.74,6.07,735.25,527.65,1.05
20260608,670,730,670,715,966863,698.26,2.4,741.3,534.7,0.66
20260609,736,786,722,776,1837200,704.74,10.11,748.8,542.65,1.26
20260610,770,784,709,731,1141157,706.93,3.41,750.95,549.52,0.83
20260611,692,730,670,719,1208721,707.93,1.56,750.8,556.18,0.98
20260612,748,755,721,727,702280,709.52,2.46,750.9,562.99,0.57
20260615,746,765,718,747,1073212,712.64,4.82,751.65,570.16,0.86
20260616,749,752,705,705,672191,712.01,-0.98,750.25,576.36,0.54
20260617,716,743,704,740,716917,714.34,3.59,751.25,582.61,0.57
20260618,740,780,740,773,892908,719.23,7.48,750.85,589.96,0.71
20260622,840,840,794,817,1654202,727.38,12.32,752.4,597.94,1.26
20260623,823,849,819,830,1529851,735.93,12.78,754.3,605.73,1.12
20260624,820,885,800,852,1823901,745.6,14.27,755.9,613.42,1.27
20260625,870,909,857,881,2196663,756.88,16.4,758.95,621.51,1.45
20260626,892,898,793,797,1451334,760.23,4.84,759.3,628.48,0.93
20260629,806,850,790,794,1023509,763.04,4.06,761.9,635.27,0.68
20260630,829,873,803,873,2090000,772.2,13.05,767.45,643.04,1.44
20260701,948,955,877,903,2174000,783.1,15.31,778.3,651.65,1.57
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 61.73
- over_600_ratio: 56.11
- over_800_ratio: 47.56
- over_1000_ratio: 43.54
- over_400_change_1w: 1.53
- over_800_change_1w: 0.8
- over_1000_change_1w: 0.8
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.61,,44.2,,37.72,,0,False,False
20260508,57.41,-2.2,44.15,-0.05,37.67,-0.05,0,False,False
20260515,62.01,4.6,45.51,1.36,37.64,-0.03,1,False,True
20260522,62.6,0.59,44.82,-0.69,40.8,3.16,2,False,True
20260529,62.57,-0.03,45.25,0.43,41.23,0.43,3,False,True
20260605,59.88,-2.69,44.02,-1.23,37.56,-3.67,0,False,False
20260612,60.23,0.35,46.19,2.17,42.17,4.61,1,True,True
20260618,60.2,-0.03,46.76,0.57,42.74,0.57,2,False,True
20260626,61.73,1.53,47.56,0.8,43.54,0.8,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6831 | 邁科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | continued_overheated | 1.股東常會日期:115/06/23 2.重要決議事項一、盈餘分配或盈虧撥補:承認民國114年度盈餘分派 3.重要決議事項二、章程修訂:無 4.重要決議事項三、營業報告書及財務報表:承認民國114年度營業報告書及財務報表 5.重要決議事項四、董監事選舉:本公司增選董事二席 6.重要決議事項五、其他事項: (1)通過修訂本公司「取得或處分資產處理程序」案 (2)通過本公司發行限制員工權利新股案 (3)通過解除本公司董事競業禁止之限制案 7.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6831 | 邁科 | 2 | 2 | 3 | 4 | 7 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260701 | 6831 | 邁科 | 19 | 0 | 7423140.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
