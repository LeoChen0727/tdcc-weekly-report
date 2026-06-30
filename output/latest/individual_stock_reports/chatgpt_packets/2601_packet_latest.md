# INDIVIDUAL STOCK CHATGPT PACKET - 2601 益航

## Metadata
- generated_at: 2026-06-30 22:26:47 Asia/Taipei
- stock_id: 2601
- stock_name: 益航
- packet_status: standard_180d_window_packet
- latest_price_date: 20260630
- price_rows: 293
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2601_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2601_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2601_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2601.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2601.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2601.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2601.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2601_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2601_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2601_latest.md?ref=main

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
- date: 20260630
- open: 5.45
- high: 5.45
- low: 5.36
- close: 5.45
- volume: 1571000
- ma5: 5.44
- ema23_primary: 5.58
- distance_to_ema23_pct: -2.26
- ma20: 5.79
- ma60: 5.44
- ma120: 5.61
- return_5d: -2.15
- return_20d: -5.38
- volume_ratio: 0.47
- distance_to_ma20_pct_auxiliary: -5.86
- distance_to_high_60_pct: -20.9

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260602,6.33,6.33,6.27,6.33,6290340,5.25,20.62,5.06,5.59,2.25
20260603,6.89,6.89,6.36,6.4,17416607,5.34,19.77,5.14,5.58,4.96
20260604,6.15,6.2,6,6.08,6913074,5.41,12.49,5.2,5.57,1.87
20260605,6.08,6.38,6.02,6.17,5436271,5.47,12.82,5.26,5.56,1.4
20260608,5.71,6,5.71,5.89,3465703,5.5,7.01,5.31,5.55,0.87
20260609,5.89,6.09,5.86,5.88,2034877,5.54,6.23,5.35,5.54,0.52
20260610,5.88,5.99,5.82,5.83,1899065,5.56,4.86,5.4,5.54,0.48
20260611,5.89,5.89,5.55,5.71,1529516,5.57,2.47,5.45,5.53,0.39
20260612,5.68,5.84,5.68,5.75,1794253,5.59,2.91,5.5,5.52,0.46
20260615,5.84,5.98,5.81,5.85,1370196,5.61,4.3,5.55,5.51,0.35
20260616,5.85,5.85,5.7,5.72,1466782,5.62,1.81,5.59,5.51,0.38
20260617,5.81,6.05,5.55,5.9,2768978,5.64,4.58,5.64,5.5,0.72
20260618,5.97,5.98,5.8,5.81,1743215,5.66,2.73,5.68,5.5,0.46
20260622,6,6,5.6,5.68,2764903,5.66,0.39,5.71,5.49,0.72
20260623,5.68,5.68,5.5,5.57,2281554,5.65,-1.42,5.73,5.49,0.6
20260624,5.55,5.61,5.46,5.54,1255085,5.64,-1.8,5.76,5.48,0.33
20260625,5.54,5.6,5.49,5.49,1722052,5.63,-2.46,5.78,5.47,0.46
20260626,5.38,5.56,5.35,5.35,2115168,5.61,-4.56,5.8,5.45,0.57
20260629,5.35,5.45,5.35,5.39,1120456,5.59,-3.53,5.8,5.45,0.31
20260630,5.45,5.45,5.36,5.45,1571000,5.58,-2.26,5.79,5.44,0.47
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 32.35
- over_600_ratio: 29.54
- over_800_ratio: 28.75
- over_1000_ratio: 26.7
- over_400_change_1w: -0.05
- over_800_change_1w: 0.08
- over_1000_change_1w: -0.04
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,31.86,,28.55,,26.32,,0,False,False
20260508,32.3,0.44,28.62,0.07,26.48,0.16,1,True,True
20260515,32.04,-0.26,28.46,-0.16,26.42,-0.06,0,False,False
20260522,32.09,0.05,28.42,-0.04,26.51,0.09,1,False,True
20260529,32.26,0.17,28.82,0.4,26.91,0.4,2,True,True
20260605,32.45,0.19,28.8,-0.02,26.77,-0.14,3,False,False
20260612,32.34,-0.11,28.71,-0.09,26.45,-0.32,0,False,False
20260618,32.4,0.06,28.67,-0.04,26.74,0.29,1,False,True
20260626,32.35,-0.05,28.75,0.08,26.7,-0.04,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2601 | 益航 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  |  | stale_signal | 1.事實發生日:115/06/18 2.公司名稱:益航股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:本公司115年6月18日股東常會決議通過辦理減資，依公司法第281條準 用同法第73及74條規定，辦理致債權人公告。 6.因應措施: (1)本公司業經115年6月18日股東常會決議通過辦理減資彌補虧損。 (2)本公司實收資本額為新台幣8,247,760,670元，分為824,776,067股，每股面額 新台幣10元，為健全公司財務結構與未來營運發展需求，擬辦理減少資本額新台幣 1,343,970,560元，以彌補累積虧損，銷除已發行股份134,397,056股，減資比率 16.2949753%，減資後實收資本額為新台幣6,903,790,110元。 (3)經股東常會決議通過及主管機關核准後，由董事長另訂減資基準日與減資換發 股票基準日。 (4)本公司債權人如對前述減少資本之決議有異議者，請於公告日起三十一日內以 書面檢附債權證明文件親交或郵寄(以郵戳日為憑)向本公司提出聲明，逾期未表示異議 視為無異議。債權人提出異議後，若轉讓債權，則喪失異議權，已向本公司提出之異議 視為撤回，特此公告。 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本次減資為彌補虧損，無實質現金流出，對公司營運資金無重大影響。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260630 | 2601 | 益航 | 2 | 2 | 4 | 7 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
