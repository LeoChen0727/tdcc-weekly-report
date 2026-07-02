# INDIVIDUAL STOCK CHATGPT PACKET - 8112 至上

## Metadata
- generated_at: 2026-07-02 22:28:19 Asia/Taipei
- stock_id: 8112
- stock_name: 至上
- packet_status: standard_180d_window_packet
- latest_price_date: 20260702
- price_rows: 296
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8112_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8112_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8112_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8112_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8112.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8112.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8112.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8112.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8112_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8112_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8112_latest.md?ref=main

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
- date: 20260702
- open: 88.3
- high: 90
- low: 86.8
- close: 89
- volume: 15209000
- ma5: 90.88
- ema23_primary: 92.41
- distance_to_ema23_pct: -3.69
- ma20: 94.03
- ma60: 88.23
- ma120: 83
- return_5d: -6.41
- return_20d: -5.72
- volume_ratio: 0.49
- distance_to_ma20_pct_auxiliary: -5.35
- distance_to_high_60_pct: -14.42

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260604,93.5,99,93.4,95.6,61466415,87.53,9.22,86.64,84.73,1.83
20260605,95.1,95.1,89.3,92.6,43713028,87.96,5.28,86.81,84.98,1.28
20260608,83.7,86.1,83.6,84.7,21743961,87.68,-3.4,86.7,84.97,0.64
20260609,86,91.9,85.2,91.2,26610267,87.98,3.66,87.17,85,0.81
20260610,92.4,98.4,91.6,92.6,60537547,88.36,4.8,87.69,85.09,1.72
20260611,95.1,97.6,90.7,95.5,54814646,88.96,7.36,88.24,85.25,1.5
20260612,98.3,104,98.2,98.8,68028936,89.78,10.05,89.1,85.37,1.75
20260615,101,101,96.8,97.3,38836098,90.4,7.63,89.76,85.41,0.97
20260616,98,99.3,95.8,95.8,20881295,90.85,5.44,90.37,85.48,0.52
20260617,95.4,98,94.3,96.8,17417421,91.35,5.97,91.01,85.62,0.44
20260618,97.5,99,97.2,98.2,16490673,91.92,6.83,91.64,85.89,0.42
20260622,99.8,103.5,98.3,100.5,38207426,92.64,8.49,92.36,86.25,0.96
20260623,101,101.5,94.7,95.8,32163046,92.9,3.12,92.98,86.46,0.8
20260624,94.4,96.5,93.8,95.8,12052857,93.14,2.86,93.61,86.73,0.3
20260625,97.2,97.8,94.5,95.1,12602389,93.3,1.92,94.06,87.01,0.33
20260626,95,96.5,91.2,91.2,17981798,93.13,-2.07,94.32,87.24,0.48
20260629,91.9,96.5,90.9,92.1,17742767,93.04,-1.01,94.5,87.54,0.48
20260630,93.1,93.7,90.4,92.4,21020000,92.99,-0.63,94.55,87.81,0.6
20260701,92.8,92.9,89.7,89.7,18652000,92.72,-3.25,94.31,88.05,0.58
20260702,88.3,90,86.8,89,15209000,92.41,-3.69,94.03,88.23,0.49
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 38.56
- over_600_ratio: 36.88
- over_800_ratio: 36.22
- over_1000_ratio: 34.72
- over_400_change_1w: -0.54
- over_800_change_1w: 0.07
- over_1000_change_1w: -0.25
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,46.32,,43.67,,42.34,,0,False,False
20260508,46.33,0.01,43.72,0.05,42.01,-0.33,1,False,True
20260515,41.47,-4.86,39.03,-4.69,36.85,-5.16,0,False,False
20260522,39.83,-1.64,37.27,-1.76,35.41,-1.44,0,False,False
20260529,38.68,-1.15,35.89,-1.38,34.06,-1.35,0,False,False
20260605,41.62,2.94,39.39,3.5,38.07,4.01,1,True,True
20260612,38.53,-3.09,35.48,-3.91,34.1,-3.97,0,False,False
20260618,39.1,0.57,36.15,0.67,34.97,0.87,1,True,True
20260626,38.56,-0.54,36.22,0.07,34.72,-0.25,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 8112 | 至上 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.事實發生日:115/06/29 2.被背書保證之: (1)公司名稱:高拓國際貿易(上海)有限公司 (2)與提供背書保證公司之關係: 本公司間接持有之100%子公司 (3)背書保證之限額(仟元):23,253,740 (4)原背書保證之餘額(仟元):4,332,906 (5)本次新增背書保證之金額(仟元):459,840 (6)迄事實發生日止背書保證餘額(仟元):4,792,746 (7)被背書保證公司實際動支金額(仟元):2,027,330 (8)本次新增背書保證之原因: 本公司向銀行簽具背書保證票據以取得額度，原額度人民幣10,000萬到期續保， 以因應轉投資子公司營運週轉之需求。 3.被背書保證公司提供擔保品之: (1)內容: 無。 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):370,095 (2)累積盈虧金額(仟元):159,786 5.解除背書保證責任之: (1)條件: 背書保證到期即解除背書保證責任。 (2)日期: 一年到期。 6.背書保證之總限額(仟元): 48,445,293 7.迄事實發生日為止，背書保證餘額(仟元): 20,608,821 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 106.35 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 26.64 10.其他應敘明事項: 無。；calendar event: ex_right_dividend on 20260706; status=confirmed; proximity=within_7d |
| 20260702 | 8112 | 至上 | revenue_pullback | 營收成長股價回檔 | 90.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/06/29 2.被背書保證之: (1)公司名稱:高拓國際貿易(上海)有限公司 (2)與提供背書保證公司之關係: 本公司間接持有之100%子公司 (3)背書保證之限額(仟元):23,253,740 (4)原背書保證之餘額(仟元):4,332,906 (5)本次新增背書保證之金額(仟元):459,840 (6)迄事實發生日止背書保證餘額(仟元):4,792,746 (7)被背書保證公司實際動支金額(仟元):2,027,330 (8)本次新增背書保證之原因: 本公司向銀行簽具背書保證票據以取得額度，原額度人民幣10,000萬到期續保， 以因應轉投資子公司營運週轉之需求。 3.被背書保證公司提供擔保品之: (1)內容: 無。 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):370,095 (2)累積盈虧金額(仟元):159,786 5.解除背書保證責任之: (1)條件: 背書保證到期即解除背書保證責任。 (2)日期: 一年到期。 6.背書保證之總限額(仟元): 48,445,293 7.迄事實發生日為止，背書保證餘額(仟元): 20,608,821 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 106.35 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 26.64 10.其他應敘明事項: 無。；calendar event: ex_right_dividend on 20260706; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260702 | 8112 | 至上 | revenue_breakout_low_response | 營收爆發低反應股 | 17.0 | 25.0 | D_降級_TDCC轉弱 |  |  | no_signal | stale_signal | 1.事實發生日:115/06/29 2.被背書保證之: (1)公司名稱:高拓國際貿易(上海)有限公司 (2)與提供背書保證公司之關係: 本公司間接持有之100%子公司 (3)背書保證之限額(仟元):23,253,740 (4)原背書保證之餘額(仟元):4,332,906 (5)本次新增背書保證之金額(仟元):459,840 (6)迄事實發生日止背書保證餘額(仟元):4,792,746 (7)被背書保證公司實際動支金額(仟元):2,027,330 (8)本次新增背書保證之原因: 本公司向銀行簽具背書保證票據以取得額度，原額度人民幣10,000萬到期續保， 以因應轉投資子公司營運週轉之需求。 3.被背書保證公司提供擔保品之: (1)內容: 無。 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):370,095 (2)累積盈虧金額(仟元):159,786 5.解除背書保證責任之: (1)條件: 背書保證到期即解除背書保證責任。 (2)日期: 一年到期。 6.背書保證之總限額(仟元): 48,445,293 7.迄事實發生日為止，背書保證餘額(仟元): 20,608,821 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 106.35 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 26.64 10.其他應敘明事項: 無。；calendar event: ex_right_dividend on 20260706; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 8112 | 至上 | 25 | 10 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 8112 | 至上 | 147 | 3 | 8578850.0 | 777820.0 | 11.03 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
