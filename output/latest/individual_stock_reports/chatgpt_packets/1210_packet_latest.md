# INDIVIDUAL STOCK CHATGPT PACKET - 1210 大成

## Metadata
- generated_at: 2026-07-14 22:26:18 Asia/Taipei
- stock_id: 1210
- stock_name: 大成
- packet_status: standard_180d_window_packet
- latest_price_date: 20260713
- price_rows: 302
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1210_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1210_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1210_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1210_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1210_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1210_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1210_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1210.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1210.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1210.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1210.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1210_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1210_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1210_latest.md?ref=main

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
- date: 20260713
- open: 57.1
- high: 58.2
- low: 57.1
- close: 57.9
- volume: 2824026
- ma5: 57.78
- ema23_primary: 56.1
- distance_to_ema23_pct: 3.21
- ma20: 56.12
- ma60: 54.21
- ma120: 53.34
- return_5d: -0.17
- return_20d: 3.95
- volume_ratio: 0.85
- distance_to_ma20_pct_auxiliary: 3.16
- distance_to_high_60_pct: -2.69

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260612,55.4,55.8,54.5,55.3,4658995,53.72,2.93,53.37,53.6,0.87
20260615,55.3,55.8,54.5,55.8,4898174,53.9,3.53,53.52,53.64,0.89
20260616,55.9,55.9,54.8,55.6,3595750,54.04,2.89,53.62,53.69,0.65
20260617,55.2,55.7,54.9,55.1,2517752,54.13,1.8,53.73,53.71,0.45
20260618,55.1,55.7,54.7,54.7,3386112,54.18,0.97,53.82,53.72,0.59
20260622,54.7,55,54.6,54.7,1631362,54.22,0.89,53.94,53.73,0.29
20260623,55,55,54.5,54.6,2311671,54.25,0.64,54.06,53.74,0.41
20260624,54.6,55.5,54.5,54.8,1691084,54.3,0.93,54.2,53.76,0.3
20260625,55.2,56,54.9,55.7,3797127,54.41,2.36,54.4,53.78,0.67
20260626,55.7,55.8,55.1,55.2,1718904,54.48,1.32,54.56,53.79,0.3
20260629,55.2,56,55.2,55.2,3533572,54.54,1.21,54.7,53.81,0.62
20260630,55.5,55.9,55.1,55.5,2167000,54.62,1.61,54.84,53.82,0.38
20260701,55.8,55.9,55,55.8,2745000,54.72,1.98,54.99,53.84,0.52
20260702,55.8,57.6,55.7,57.6,6983000,54.96,4.81,55.19,53.89,1.37
20260703,57.5,59,57.3,58,5765678,55.21,5.05,55.38,53.95,1.18
20260706,58.1,59.5,58.1,58.8,3859000,55.51,5.93,55.6,54.02,0.85
20260707,58.9,59.3,58.1,58.3,2662754,55.74,4.59,55.81,54.09,0.64
20260708,58.4,58.5,56.7,56.9,4066476,55.84,1.9,55.94,54.12,1.03
20260709,56.7,57.5,56.7,57,1943675,55.94,1.9,56.02,54.16,0.55
20260713,57.1,58.2,57.1,57.9,2824026,56.1,3.21,56.12,54.21,0.85
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 65.21
- over_600_ratio: 63.34
- over_800_ratio: 61.98
- over_1000_ratio: 60.95
- over_400_change_1w: 0.73
- over_800_change_1w: 0.71
- over_1000_change_1w: 0.39
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.5,,60.28,,59.32,,0,False,False
20260508,63,-0.5,59.8,-0.48,58.73,-0.59,0,False,False
20260515,62.89,-0.11,59.63,-0.17,58.64,-0.09,0,False,False
20260522,63.02,0.13,59.88,0.25,58.9,0.26,1,True,True
20260529,62.65,-0.37,59.77,-0.11,58.68,-0.22,0,False,False
20260605,63.02,0.37,59.68,-0.09,58.61,-0.07,1,False,False
20260612,64.02,1,60.6,0.92,59.71,1.1,2,True,True
20260618,64.31,0.29,61.05,0.45,60.36,0.65,3,True,True
20260626,64.48,0.17,61.27,0.22,60.56,0.2,4,True,True
20260703,65.21,0.73,61.98,0.71,60.95,0.39,5,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 1210 | 大成 | pattern | 型態觀察 | 54.0 |  |  | early_entry_watch |  | no_signal | stale_signal | 1.發生變動日期:115/06/26 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:獨立非執行董事、非執行董事 3.舊任者職稱及姓名: 獨立非執行董事:夏立言 非執行董事: 韓家宇 非執行董事: 韓家宸 非執行董事: 韓家寰 4.舊任者簡歷: 獨立非執行董事:夏立言 大成食品亞洲有限公司獨立非執行董事 非執行董事: 韓家宇 大成食品亞洲有限公司非執行董事 非執行董事: 韓家宸 大成食品亞洲有限公司非執行董事 非執行董事: 韓家寰 大成食品亞洲有限公司非執行董事 5.新任者職稱及姓名: 獨立非執行董事:夏立言 非執行董事: 韓家宇 非執行董事: 韓家宸 非執行董事: 韓家寰 6.新任者簡歷: 獨立非執行董事:夏立言 大成食品亞洲有限公司獨立非執行董事 非執行董事: 韓家宇 大成食品亞洲有限公司非執行董事 非執行董事: 韓家宸 大成食品亞洲有限公司非執行董事 非執行董事: 韓家寰 大成食品亞洲有限公司非執行董事 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:董監事任期屆滿全面改選 9.新任者選任時持股數: 獨立非執行董事:夏立言 0股 非執行董事: 韓家宇 0股 非執行董事: 韓家宸 0股 非執行董事: 韓家寰 344,000股 10.原任期（例xx/xx/xx ~ xx/xx/xx）: 獨立非執行董事:夏立言 112/06/29~115年股東會結束 非執行董事: 韓家宇 113/06/28~116年股東會結束 非執行董事: 韓家宸 113/06/28~116年股東會結束 非執行董事: 韓家寰 113/06/28~116年股東會結束 11.新任生效日期:115/06/26 12.同任期董事變動比率:任期屆滿改選，故不適用。 13.同任期獨立董事變動比率:任期屆滿改選，故不適用。 14.同任期監察人變動比率:無監察人，故不適用。 15.屬三分之一以上董事發生變動（請輸入是或否）:是 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項):無；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 1210 | 大成 | 2 | 2 | 4 | 8 | 17 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260713 | 1210 | 大成 | 2 | 0 | 112080.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
