# INDIVIDUAL STOCK CHATGPT PACKET - 3630 新鉅科

## Metadata
- generated_at: 2026-06-20 22:54:38 Asia/Taipei
- stock_id: 3630
- stock_name: 新鉅科
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 152
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3630_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3630_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3630_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3630_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3630_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3630_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3630_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3630.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3630.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3630.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3630.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3630_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3630_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3630_latest.md?ref=main

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
- date: 20260618
- open: 35.35
- high: 36.2
- low: 34.1
- close: 34.8
- volume: 5475000
- ma5: 32.65
- ema23_primary: 29.77
- distance_to_ema23_pct: 16.89
- ma20: 29.07
- ma60: 28.31
- ma120: 29.79
- return_5d: 15.61
- return_20d: 27.47
- volume_ratio: 1.69
- distance_to_ma20_pct_auxiliary: 19.7
- distance_to_high_60_pct: -5.56

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,27.8,27.8,26.95,27.6,27000,27.22,1.39,26.98,28.96,0.03
20260525,27.8,27.85,27,27.05,27000,27.21,-0.58,26.91,28.86,0.03
20260526,27.05,27.5,26.45,27,27000,27.19,-0.7,26.86,28.75,0.03
20260527,27.35,27.35,26,26.15,26000,27.1,-3.52,26.79,28.59,0.03
20260528,26.2,26.6,25.4,25.65,26000,26.98,-4.94,26.7,28.44,0.03
20260529,25.9,26.15,25.85,26.15,26000,26.91,-2.84,26.64,28.33,0.03
20260601,26.3,26.9,26.05,26.5,27000,26.88,-1.41,26.58,28.27,0.04
20260602,26.8,27.2,26.2,27.05,27,26.89,0.58,26.51,28.2,0
20260603,27.2,27.8,26.7,27.35,27000,26.93,1.56,26.5,28.14,0.04
20260604,27.35,30.05,26.7,29.15,29000,27.12,7.5,26.57,28.15,0.05
20260605,29.2,31.45,29.2,29.6,30000,27.32,8.33,26.7,28.16,0.06
20260608,26.65,28.55,26.65,27.85,1704000,27.37,1.76,26.77,28.11,2.96
20260609,28.2,30.6,27.7,30.6,1853000,27.64,10.72,26.98,28.11,3
20260610,32,33.65,30.1,30.4,11979000,27.87,9.09,27.22,28.11,10.24
20260611,29.5,30.1,28.35,30.1,2632000,28.05,7.3,27.47,28.1,2.15
20260612,30.7,31.1,29.1,29.1,2504000,28.14,3.41,27.64,28.07,1.99
20260615,29.25,31.3,29.2,30.5,2948000,28.34,7.63,27.89,28.07,2.13
20260616,30.6,33.55,30.05,33.55,8867000,28.77,16.61,28.27,28.12,5.03
20260617,33.9,36.85,33.75,35.3,26569000,29.32,20.42,28.7,28.21,8.77
20260618,35.35,36.2,34.1,34.8,5475000,29.77,16.89,29.07,28.31,1.69
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 54.17
- over_600_ratio: 52.72
- over_800_ratio: 51.97
- over_1000_ratio: 51.09
- over_400_change_1w: 0.04
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.4,,52.02,,51.58,,0,False,False
20260508,54.2,-0.2,51.94,-0.08,51.09,-0.49,0,False,False
20260515,54.09,-0.11,51.96,0.02,51.09,0,1,False,True
20260522,53.89,-0.2,51.53,-0.43,51.09,0,0,False,False
20260529,54.1,0.21,52.05,0.52,51.61,0.52,1,True,True
20260605,54.91,0.81,52.61,0.56,51.69,0.08,2,True,True
20260612,54.13,-0.78,51.97,-0.64,51.09,-0.6,0,False,False
20260618,54.17,0.04,51.97,0,51.09,0,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3630 | 新鉅科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_right_side |  |  | first_seen | 1.發生變動日期:115/06/17 2.功能性委員會名稱:薪酬委員會 3.舊任者姓名: (1)獨立董事王智信 (2)獨立董事Erwin Limowa (3)獨立董事魏仁裕 4.舊任者簡歷: (1)獨立董事王智信、Master Concept (HK) Limited. CEO (2)獨立董事Erwin Limowa、極穎印刷製品（東莞）有限公司總經理 (3)獨立董事魏仁裕、東博財務管理顧問(股)公司合夥人 5.新任者姓名: 獨立董事：王智信 獨立董事：蔡洲灝 獨立董事：廖苑珊 6.新任者簡歷: 獨立董事：王智信 Master Concept (HK) Limited. CEO 獨立董事：蔡洲灝 國聯創業投資管理顧問股份有限公司 副總經理 獨立董事：廖苑珊 美時化學製藥股份有限公司 公司治理處長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:股東常會全面改選董事後，由新任董事會重新委任。 9.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/21~115/06/20 10.新任生效日期:115/06/17 11.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3630 | 新鉅科 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
