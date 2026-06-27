# INDIVIDUAL STOCK CHATGPT PACKET - 4416 三圓

## Metadata
- generated_at: 2026-06-27 22:23:45 Asia/Taipei
- stock_id: 4416
- stock_name: 三圓
- packet_status: standard_180d_window_packet
- latest_price_date: 20260626
- price_rows: 157
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4416_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4416_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4416_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4416_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4416.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4416.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4416.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4416.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4416_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4416_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4416_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

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
- date: 20260626
- open: 13.4
- high: 13.4
- low: 12.55
- close: 13.05
- volume: 4645000
- ma5: 11.29
- ema23_primary: 11.18
- distance_to_ema23_pct: 16.69
- ma20: 10.98
- ma60: 12.16
- ma120: 18.4
- return_5d: 30.5
- return_20d: 20.83
- volume_ratio: 7.05
- distance_to_ma20_pct_auxiliary: 18.84
- distance_to_high_60_pct: -21.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260529,10.95,11.15,10.85,10.9,11000,12,-9.18,11.84,13.45,0.1
20260601,10.9,11.5,10.9,11.45,11000,11.96,-4.23,11.78,13.3,0.13
20260602,11.4,12.4,11.4,12.1,12,11.97,1.11,11.75,13.19,0
20260603,12.2,12.2,11.7,11.7,12000,11.95,-2.05,11.71,13.11,0.16
20260604,11.7,12,11.6,11.6,12000,11.92,-2.65,11.66,13.05,0.19
20260605,11.6,11.7,11.4,11.5,12000,11.88,-3.21,11.61,13,0.21
20260608,11.45,11.45,10.75,11.25,182000,11.83,-4.89,11.55,12.96,2.88
20260609,11.15,11.15,10.65,10.7,488000,11.73,-8.82,11.47,12.91,5.91
20260610,10.7,10.85,10.55,10.6,214000,11.64,-8.94,11.38,12.84,2.4
20260611,10.6,10.75,10.5,10.5,154000,11.55,-9.05,11.29,12.77,1.67
20260612,10.55,10.7,10.5,10.55,197000,11.46,-7.96,11.24,12.67,2.21
20260615,10.6,10.85,10.6,10.7,151000,11.4,-6.13,11.2,12.6,1.75
20260616,10.65,10.65,10.25,10.3,415000,11.31,-8.91,11.14,12.52,3.98
20260617,10.25,10.25,9.27,9.33,1890000,11.14,-16.27,11.04,12.43,9.74
20260618,10.25,10.25,9.55,10,1837000,11.05,-9.48,10.97,12.36,6.51
20260622,9.98,10.5,9.76,10,961000,10.96,-8.76,10.91,12.3,2.92
20260623,10,10.3,9.87,10.1,295000,10.89,-7.24,10.8,12.26,0.86
20260624,10.15,11.1,10.15,11.1,739000,10.91,1.78,10.8,12.22,1.94
20260625,12,12.2,12,12.2,950000,11.01,10.77,10.87,12.18,2.22
20260626,13.4,13.4,12.55,13.05,4645000,11.18,16.69,10.98,12.16,7.05
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 78.41
- over_600_ratio: 71.76
- over_800_ratio: 67.94
- over_1000_ratio: 63.99
- over_400_change_1w: -0.87
- over_800_change_1w: -1.83
- over_1000_change_1w: -3.11
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,82.06,,72.78,,70.11,,0,False,False
20260508,82.06,0,72.78,0,70.11,0,0,False,False
20260515,82.68,0.62,72.85,0.07,70.18,0.07,1,True,True
20260522,82.73,0.05,72.88,0.03,70.21,0.03,2,True,True
20260529,80.22,-2.51,69.98,-2.9,67.31,-2.9,0,False,False
20260605,79.96,-0.26,69.77,-0.21,67.1,-0.21,0,False,False
20260612,79.28,-0.68,69.77,0,67.1,0,0,False,False
20260618,78.41,-0.87,67.94,-1.83,63.99,-3.11,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 4416 | 三圓 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | first_seen | 1.櫃買中心公告處置之日期:NA 2.公司名稱(或負責人姓名):王雅麟 3.與公司關係﹝請輸入本公司、本公司負責人、母公司或子公司﹞:本公司董事長 4.若為母公司或子公司，其相互持股比例:不適用 5.櫃買中心公告處置引用之業務規則條款及發生緣由: 第4條之1上櫃公司或其負責人發生存款不足之退票事由；董事長王雅麟先生 退票事由 6.處理結果(請輸入〝變更交易方法〞、〝停止買賣〞或〝終止上櫃〞):不適用 7.股票開始(併案)變更交易方法/停止買賣/終止上櫃之日期:NA 8.退票、拒絕往來之日期:115/06/25 9.退票張數及金額:1張，$1,500,000 10.退票之往來銀行:合作金庫 11.退票後之清償註記日期:NA 12.退票之清償方式(請輸入〝已實際償付票款〞或〝以換票方式遞延票據債務〞): 與持票人協商清償註記。 13.公告拒絕往來之票據交換所（拒絕往來時適用，否則請輸[不適用]）:不適用 14.因應及保全措施:無 15.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第1款所定對 股東權益或證券價格有重大影響之事項): (1)本公司於115/06/25日獲悉，董事長發生退票情事。 (2)截至本日共有7張支票尚未清償註記，金額共計新台幣87,145,000元，已與 持票人協商清償註記。 (3)該事件係法人董事之個別事務，與本公司營運及財務業務無涉，亦對本公司無 重大影響。 16.(風險警示)發生存款不足退票而致上櫃有價證券列為變更交易方法， 三個月內無法達成補正程序而致停止買賣， 有金融機構拒絕往來紀錄或前開停止買賣情事 六個月內無法達成補正程序並檢附相關書件證明者， 有價證券將有終止上櫃之虞， 提醒投資人審慎注意投資風險:不適用；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260626 | 4416 | 三圓 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
