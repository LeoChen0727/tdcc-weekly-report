# INDIVIDUAL STOCK CHATGPT PACKET - 6933 AMAX-KY

## Metadata
- generated_at: 2026-09-19 15:54:42 Asia/Taipei
- stock_id: 6933
- stock_name: AMAX-KY
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6933_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6933_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6933_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6933_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6933_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6933_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6933_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6933.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6933.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6933.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6933.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6933_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6933_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6933_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: high_level_distribution_risk
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
- tdcc_distribution_warning
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260918
- open: 355
- high: 360.5
- low: 332
- close: 342
- volume: 3660865
- ma5: 318.7
- ema23_primary: 285.96
- distance_to_ema23_pct: 19.6
- ma20: 293.5
- ma60: 207.73
- ma120: 186.47
- return_5d: 6.88
- return_20d: 84.37
- volume_ratio: 2.66
- distance_to_ma20_pct_auxiliary: 16.52
- distance_to_high_60_pct: -5.13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,185,198,185,194.5,543374,178.72,8.83,175.5,164.12,0.94
20260825,194.5,195.5,186.5,195.5,406258,180.11,8.54,177.43,164.5,0.7
20260826,199,215,197.5,215,1533341,183.02,17.47,180.78,164.93,2.43
20260827,236.5,236.5,236.5,236.5,550758,187.48,26.15,185.72,165.82,0.86
20260828,260,260,256,260,1952815,193.52,34.35,191.22,167.05,2.72
20260831,284,286,283,286,2056481,201.23,42.13,197.82,168.92,2.58
20260901,296,314.5,296,314.5,3418616,210.67,49.29,205.1,171.37,3.75
20260902,314.5,331,309,331,1260106,220.69,49.98,213.38,174.3,1.35
20260903,316,322,301.5,302,1360888,227.47,32.76,220.03,176.7,1.38
20260904,309,319,299,317,956572,234.93,34.93,227.65,179.48,0.95
20260907,319,319,307.5,313,404357,241.44,29.64,234.28,182.22,0.4
20260908,322.5,325,315,317.5,345717,247.78,28.14,240.75,185.01,0.36
20260909,320.5,338,310.5,338,562921,255.29,32.4,247.95,188.07,0.61
20260910,348,354,331.5,336,510177,262.02,28.23,254.88,191.11,0.57
20260911,333,333,315,320,493403,266.85,19.92,261.45,193.86,0.55
20260914,304.5,334.5,294,305.5,1977486,270.07,13.12,267.12,196.33,2.02
20260915,310.5,312,280.5,286,1753249,271.4,5.38,271.85,198.49,1.68
20260916,286,314.5,282.5,314.5,932211,274.99,14.37,278.05,201.19,0.87
20260917,324,345.5,316.5,345.5,2860719,280.87,23.01,285.68,204.45,2.37
20260918,355,360.5,332,342,3660865,285.96,19.6,293.5,207.73,2.66
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 66.73
- over_600_ratio: 65.66
- over_800_ratio: 62.19
- over_1000_ratio: 60.09
- over_400_change_1w: 0.11
- over_800_change_1w: -0.19
- over_1000_change_1w: -0.2
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,61.51,0,61.51,0,61.51,0,0,False,False
20260709,61.51,0,61.51,0,61.51,0,0,False,False
20260717,61.35,-0.16,61.35,-0.16,61.35,-0.16,0,False,False
20260724,61.25,-0.1,61.25,-0.1,61.25,-0.1,0,False,False
20260731,61.2,-0.05,61.2,-0.05,61.2,-0.05,0,False,False
20260807,61.07,-0.13,61.07,-0.13,61.07,-0.13,0,False,False
20260814,61.03,-0.04,61.03,-0.04,61.03,-0.04,0,False,False
20260821,61,-0.03,61,-0.03,61,-0.03,0,False,False
20260828,60.93,-0.07,60.93,-0.07,60.93,-0.07,0,False,False
20260904,66.52,5.59,62.54,1.61,60.57,-0.36,1,False,True
20260911,66.62,0.1,62.38,-0.16,60.29,-0.28,2,False,False
20260918,66.73,0.11,62.19,-0.19,60.09,-0.2,3,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6933 | AMAX-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 1.事實發生日:115/08/26 2.原公告申報日期:115/04/22 3.簡述原公告申報內容: 本公司於115年4月22日董事會決議發行2026年限制員工權利新股200,000股， 公告發行辦法主要內容，並經115年6月5日股東常會決議通過。 4.變動緣由及主要內容: (1)依據主管機關於送件審核過程中之要求，本公司修訂 「2026年度限制員工權利新股發行辦法」部分條款， 並經115年8月26日董事會決議追認通過。 (2)修正前條文: 第九條 實施及修訂 (一)本辦法經董事會三分之二以上董事出席及出席董事超過 二分之一同意，並報主管機關核准後生效，發行前修正時 亦同。嗣後如因法令修改、主管機關審核要求或客觀環境 改變而有修正之必要時，授權董事長修訂本辦法， 嗣後再提董事會追認後始得發行。 (二)本辦法如有未盡事宜，悉依相關法令規定辦理。 (3) 修正後條文: 第九條 實施及修訂 (一)本辦法經董事會三分之二以上董事出席及出席董事超過 二分之一同意，並申報經主管機關核准後生效，發行前如有修正時亦同。 若於送件審核過程中，因主管機關審核之要求而須修正本辦法時， 授權董事長修訂本辦法，嗣後再提董事會追認後始得發行。 (二)本辦法如有未盡事宜，悉依相關 法令規定辦理。 5.變動後對公司財務業務之影響:無。 6.其他應敘明事項:無。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6933 | AMAX-KY | 2 | 2 | 2 | 2 | 8 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 6933 | AMAX-KY | 1 | 0 | 292690.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
