# INDIVIDUAL STOCK CHATGPT PACKET - 1101 台泥

## Metadata
- generated_at: 2026-06-21 22:22:28 Asia/Taipei
- stock_id: 1101
- stock_name: 台泥
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 286
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1101_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1101_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1101_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1101_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1101.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1101.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1101.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1101.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1101_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1101_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1101_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: hold_only
- action_rating_label_zh: 已持有續抱
- confidence_level: medium
- thesis_state: unclear
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
- date: 20260618
- open: 24.6
- high: 24.8
- low: 24.5
- close: 24.5
- volume: 33250276
- ma5: 24.59
- ema23_primary: 24.39
- distance_to_ema23_pct: 0.45
- ma20: 24.3
- ma60: 24.34
- ma120: 24.51
- return_5d: 1.03
- return_20d: 1.24
- volume_ratio: 0.96
- distance_to_ma20_pct_auxiliary: 0.81
- distance_to_high_60_pct: -7.2

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,24.2,24.2,23.95,24.1,22434398,24.47,-1.52,24.54,24.54,0.81
20260525,24.1,24.45,23.95,24.3,33786766,24.46,-0.65,24.53,24.5,1.2
20260526,24.3,24.6,23.95,23.95,31297642,24.42,-1.91,24.51,24.46,1.11
20260527,23.95,24.05,23.8,23.85,29819864,24.37,-2.13,24.48,24.42,1.04
20260528,23.85,24,23.65,23.65,35826774,24.31,-2.71,24.44,24.37,1.22
20260529,24.1,24.4,23.9,24.4,49699249,24.32,0.34,24.43,24.35,1.62
20260601,24.4,24.7,24.2,24.55,35557711,24.34,0.88,24.44,24.34,1.15
20260602,24.55,24.8,24.4,24.65,33068326,24.36,1.18,24.46,24.34,1.06
20260603,24.65,25.2,24.45,24.85,45323366,24.4,1.83,24.45,24.33,1.45
20260604,24.9,24.95,24.45,24.45,37205139,24.41,0.18,24.4,24.33,1.19
20260605,24.5,24.6,24.2,24.4,31313266,24.41,-0.03,24.37,24.34,1
20260608,23.85,24,23.55,23.85,51860722,24.36,-2.09,24.3,24.32,1.58
20260609,23.9,24.15,23.85,23.95,27355323,24.33,-1.54,24.25,24.3,0.84
20260610,23.95,24.25,23.85,23.9,31959243,24.29,-1.61,24.2,24.29,0.97
20260611,23.95,24.35,23.8,24.25,31962933,24.29,-0.15,24.19,24.28,0.96
20260612,24.35,24.85,24.25,24.55,30216569,24.31,0.99,24.21,24.28,0.91
20260615,24.95,25.4,24.8,24.85,41019136,24.35,2.04,24.25,24.29,1.22
20260616,25,25.1,24.5,24.5,30785043,24.37,0.55,24.27,24.3,0.91
20260617,24.5,24.8,24.45,24.55,26236790,24.38,0.69,24.29,24.31,0.78
20260618,24.6,24.8,24.5,24.5,33250276,24.39,0.45,24.3,24.34,0.96
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 55.41
- over_600_ratio: 53.62
- over_800_ratio: 52.35
- over_1000_ratio: 51.23
- over_400_change_1w: 0.13
- over_800_change_1w: 0.16
- over_1000_change_1w: 0.11
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.6,,51.39,,50.46,,0,False,False
20260508,54.8,0.2,51.59,0.2,50.56,0.1,1,True,True
20260515,54.84,0.04,51.67,0.08,50.63,0.07,2,True,True
20260522,54.71,-0.13,51.5,-0.17,50.41,-0.22,0,False,False
20260529,54.77,0.06,51.66,0.16,50.56,0.15,1,True,True
20260605,55.22,0.45,52.1,0.44,51.05,0.49,2,True,True
20260612,55.28,0.06,52.19,0.09,51.12,0.07,3,True,True
20260618,55.41,0.13,52.35,0.16,51.23,0.11,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1101 | 台泥 | pattern | 型態觀察 | 54.0 |  |  | base_building |  | no_signal | continued_2_3d | 1.事實發生日:115/06/16 2.公司名稱:臺灣水泥股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:依據本公司國內第一次無擔保轉換公司債發行及轉換辦法第十五條規定 調整轉換價格。 6.因應措施:本公司自115年7月7日(除息基準日)起，本公司國內第一次無擔保轉換 公司債之轉換價格由每股新台幣35.2元調整為34.0元。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: ex_dividend on 20260701; status=confirmed; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1101 | 台泥 | 3 | 3 | 4 | 7 | 8 | continued_2_3d | 連續 3 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 1101 | 台泥 | 36 | 2 | 699550.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
