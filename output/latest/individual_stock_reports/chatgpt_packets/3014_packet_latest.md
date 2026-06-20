# INDIVIDUAL STOCK CHATGPT PACKET - 3014 聯陽

## Metadata
- generated_at: 2026-06-20 22:54:04 Asia/Taipei
- stock_id: 3014
- stock_name: 聯陽
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3014_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3014_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3014_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3014_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3014_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3014_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3014_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3014.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3014.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3014.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3014.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3014_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3014_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3014_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260618
- open: 154
- high: 158
- low: 153.5
- close: 157.5
- volume: 3775602
- ma5: 152.5
- ema23_primary: 146.2
- distance_to_ema23_pct: 7.73
- ma20: 149.07
- ma60: 133.52
- ma120: 125.63
- return_5d: 12.9
- return_20d: 8.62
- volume_ratio: 1.22
- distance_to_ma20_pct_auxiliary: 5.65
- distance_to_high_60_pct: -6.25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,146,149,143,148,4648958,133.73,10.67,133.55,124.02,1.62
20260525,151.5,152.5,148,148.5,3426757,134.96,10.03,134.7,124.47,1.15
20260526,148.5,151.5,147,151,2839111,136.3,10.79,136.03,124.92,0.93
20260527,152,153.5,149,153,3236990,137.69,11.12,137.5,125.42,1.02
20260528,153,156,148,148.5,2680278,138.59,7.15,138.72,125.87,0.81
20260529,151,154,148.5,154,3611307,139.88,10.1,140.22,126.4,1.06
20260601,154,154,149.5,152.5,2901121,140.93,8.21,141.5,127,0.83
20260602,152,153.5,148.5,151,2567637,141.77,6.51,142.5,127.53,0.74
20260603,152.5,152.5,150,151,1321787,142.54,5.94,143.43,128.04,0.38
20260604,150,151,149,150.5,1066742,143.2,5.1,144.38,128.64,0.31
20260605,151.5,153,149.5,152,2624101,143.93,5.6,145.2,129.21,0.85
20260608,141.5,144,139,142.5,2307834,143.81,-0.91,145.38,129.6,0.77
20260609,141.5,141.5,135,140.5,3487582,143.54,-2.12,145.4,129.94,1.24
20260610,140,141.5,136.5,136.5,1287825,142.95,-4.51,145.35,130.24,0.47
20260611,135,142,134,139.5,1706892,142.66,-2.22,145.38,130.61,0.62
20260612,149.5,153,146,153,4672895,143.52,6.6,146.22,131.18,1.66
20260615,165,168,148,150.5,9289739,144.11,4.44,146.97,131.71,2.88
20260616,152,156,148.5,150,2292908,144.6,3.74,147.78,132.25,0.71
20260617,148,152,146.5,151.5,2066227,145.17,4.36,148.45,132.82,0.64
20260618,154,158,153.5,157.5,3775602,146.2,7.73,149.07,133.52,1.22
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 34.54
- over_600_ratio: 28.41
- over_800_ratio: 24.9
- over_1000_ratio: 21.57
- over_400_change_1w: 0.49
- over_800_change_1w: -1.36
- over_1000_change_1w: -0.84
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,33.07,,23.97,,21.38,,0,False,False
20260508,33.49,0.42,23.92,-0.05,21.3,-0.08,1,False,False
20260515,31.86,-1.63,22.52,-1.4,19.34,-1.96,0,False,False
20260522,33.41,1.55,24.56,2.04,21.43,2.09,1,True,True
20260529,35.54,2.13,27.66,3.1,22.84,1.41,2,True,True
20260605,35.27,-0.27,26.86,-0.8,21.46,-1.38,0,False,False
20260612,34.05,-1.22,26.26,-0.6,22.41,0.95,1,False,True
20260618,34.54,0.49,24.9,-1.36,21.57,-0.84,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3014 | 聯陽 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | stale_signal | 1.主管機關核准減資日期:115/06/15 2.辦理資本變更登記完成日期:115/06/15 3.對財務報告之影響（含實收資本額與流通在外股數之差異與對每股淨值之影響）: (1)限制員工權利新股註銷減資前：本公司實收資本額為新台幣1,659,871,240元， 流通在外股數為165,987,124股，每股淨值為新台幣37.3697元(依一一五年第一季 財務報表計算) (2)本次註銷股份：普通股8,000股，每股面額新台幣10元，共計新台幣80,000元。 (3)限制員工權利新股註銷減資後：本公司實收資本額為新台幣1,659,791,240元， 流通在外股數為165,979,124股，每股淨值為新台幣37.3715元(依一一五年第一季 財務報表計算) 4.預計換股作業計畫:不適用 5.預計減資新股上市後之上市普通股股數:不適用 6.預計減資新股上市後之上市普通股股數占已發行普通股比率  （減資後上市普通股股數/減資後已發行普通股股數）:不適用 7.前二項預計減資後上巿普通股股數未達6000萬股且未達25%者，請說明股權流通性偏低   之因應措施:不適用 8.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3014 | 聯陽 | 5 | 3 | 5 | 8 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3014 | 聯陽 | 9 | 0 | 804770.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
