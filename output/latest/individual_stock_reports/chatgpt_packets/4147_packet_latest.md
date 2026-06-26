# INDIVIDUAL STOCK CHATGPT PACKET - 4147 中裕

## Metadata
- generated_at: 2026-06-25 22:23:46 Asia/Taipei
- stock_id: 4147
- stock_name: 中裕
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 155
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4147_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4147_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4147_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4147_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4147.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4147.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4147.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4147.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4147_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4147_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4147_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_initial
- entry_style: no_entry_now
- position_sizing: observe_only

### management_plan
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
- date: 20260624
- open: 64.5
- high: 66.7
- low: 62.7
- close: 64.5
- volume: 6328000
- ma5: 60
- ema23_primary: 56.18
- distance_to_ema23_pct: 14.8
- ma20: 55.77
- ma60: 52.79
- ma120: 54.61
- return_5d: 13.56
- return_20d: 32.31
- volume_ratio: 4.77
- distance_to_ma20_pct_auxiliary: 15.65
- distance_to_high_60_pct: -3.3

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,48.7,48.7,47.85,47.85,48000,49.9,-4.11,49.59,51.4,0.06
20260528,47.75,48.1,47,47.1,47000,49.67,-5.17,49.48,51.31,0.06
20260529,47.35,49.25,47.35,49.25,49000,49.63,-0.77,49.47,51.29,0.06
20260601,50.1,54.1,48.85,53.2,53000,49.93,6.55,49.7,51.31,0.07
20260602,52.9,55.2,51.9,52.7,53,50.16,5.06,49.84,51.28,0
20260603,52.9,56.2,52.3,55.8,55000,50.63,10.21,50.16,51.32,0.08
20260604,55.1,59,54.3,58.6,57000,51.29,14.24,50.65,51.45,0.09
20260605,58,58.8,55.2,55.4,56000,51.64,7.29,50.93,51.54,0.1
20260608,52.7,55.5,51.7,54.1,1550000,51.84,4.36,51.2,51.59,2.49
20260609,55,56.5,54.8,55,1128000,52.1,5.56,51.44,51.65,1.77
20260610,56,57.8,55.3,57.6,1908000,52.56,9.58,51.87,51.77,2.74
20260611,57.9,62,56.1,58.6,3880000,53.07,10.43,52.11,51.89,5.24
20260612,59.9,62,56.9,57.3,2768000,53.42,7.27,52.42,51.97,3.45
20260615,57.9,57.9,55.8,56.1,1233000,53.64,4.58,52.72,52.04,1.5
20260616,56.3,57.1,55.7,56.8,758000,53.91,5.37,53.09,52.15,0.93
20260617,57,58.5,56.6,57.2,936000,54.18,5.57,53.51,52.29,1.19
20260618,57.2,58.3,57.1,57.2,957000,54.43,5.09,53.92,52.44,1.22
20260622,57.6,58.3,56.7,57.7,856000,54.7,5.48,54.28,52.52,1.04
20260623,57.9,63.4,57.4,63.4,3855000,55.43,14.38,54.98,52.66,3.81
20260624,64.5,66.7,62.7,64.5,6328000,56.18,14.8,55.77,52.79,4.77
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 51.92
- over_600_ratio: 48.77
- over_800_ratio: 45.68
- over_1000_ratio: 43.12
- over_400_change_1w: -0.77
- over_800_change_1w: -0.05
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,52.43,,45.15,,42.21,,0,False,False
20260508,52.57,0.14,45.28,0.13,42.69,0.48,1,True,True
20260515,52.65,0.08,45.59,0.31,43.29,0.6,2,True,True
20260522,52.23,-0.42,45.28,-0.31,42.99,-0.3,0,False,False
20260529,51.93,-0.3,45.37,0.09,43.42,0.43,1,False,True
20260605,52.76,0.83,45.9,0.53,43.63,0.21,2,True,True
20260612,52.69,-0.07,45.73,-0.17,43.2,-0.43,3,False,False
20260618,51.92,-0.77,45.68,-0.05,43.12,-0.08,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 4147 | 中裕 | true_breakout | 嚴格突破 | 89.0 |  |  | platform_breakout |  |  | continued_overheated | 1.事實發生日:115/06/22 2.契約或承諾相對人:Samsung Biologics Co., Ltd. 3.與公司關係:無 4.契約或承諾起迄日期（或解除日期）:115/06/22 5.主要內容（解除者不適用）:本公司與Samsung Biologics Co., Ltd.簽訂TMB-365 商業產品藥物原料之產品專屬協議（Product Specific Agreement–Commercial Product Drug Substance） 6.限制條款（解除者不適用）:無 7.承諾事項（解除者不適用）:無 8.其他重要約定事項（解除者不適用）:無 9.對公司財務、業務之影響:本公司與Samsung Biologics Co., Ltd.達成深度合作， 全面啟動 TMB-365 的技術移轉與規模化量產，以全力支持臨床試驗以及未來的 全球市場上市供應。 10.具體目的:本公司與Samsung Biologics Co., Ltd.達成深度合作，全面啟動 TMB-365 的技術移轉與規模化量產，以全力支持臨床試驗以及未來的全球市場 上市供應。 11.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 4147 | 中裕 | 2 | 2 | 2 | 2 | 2 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
