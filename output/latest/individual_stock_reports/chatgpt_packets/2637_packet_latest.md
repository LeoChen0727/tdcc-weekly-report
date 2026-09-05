# INDIVIDUAL STOCK CHATGPT PACKET - 2637 慧洋-KY

## Metadata
- generated_at: 2026-09-05 22:16:08 Asia/Taipei
- stock_id: 2637
- stock_name: 慧洋-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 348
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2637_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2637_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2637_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2637_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2637.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2637.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2637.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2637.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2637_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2637_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2637_latest.md?ref=main

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
- action_rating_display_zh: 已持有續抱
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 營收成長股價回檔 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260904
- open: 99.9
- high: 104.5
- low: 97.9
- close: 99.8
- volume: 6217733
- ma5: 97.12
- ema23_primary: 92.27
- distance_to_ema23_pct: 8.16
- ma20: 92.73
- ma60: 83.9
- ma120: 78.43
- return_5d: 8.36
- return_20d: 13.54
- volume_ratio: 0.79
- distance_to_ma20_pct_auxiliary: 7.62
- distance_to_high_60_pct: -7.59

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,88.3,88.7,87.2,88.1,2143215,82.34,6.99,82.67,78.39,0.82
20260811,87.4,87.9,86.6,87.3,1573913,82.75,5.49,82.84,78.64,0.63
20260812,87.3,88.8,86.8,88,1487773,83.19,5.78,83.05,78.89,0.6
20260813,88.3,88.3,85.2,85.2,1692435,83.36,2.21,83.18,79.13,0.68
20260814,85.1,86.2,83.9,85.7,1796802,83.55,2.57,83.5,79.36,0.74
20260817,85.5,87.1,85.5,87,1359134,83.84,3.77,83.89,79.61,0.57
20260818,87,88.8,86.9,88.7,3140972,84.25,5.29,84.27,79.9,1.27
20260819,88.9,92.2,87.6,91.8,11208949,84.88,8.16,84.68,80.18,3.92
20260820,94.7,96,90.5,94.7,9285179,85.69,10.51,85.35,80.51,2.89
20260821,93.5,104,93.4,102,17870989,87.05,17.17,86.26,80.95,4.52
20260824,103,108,96.5,97.1,21718935,87.89,10.48,87,81.29,4.4
20260825,97.8,105,94.7,95.5,35337391,88.52,7.88,87.68,81.62,5.36
20260826,94,98.1,90,91.2,11259226,88.75,2.76,88.22,81.83,1.6
20260827,90.4,95.6,90.1,94.6,6912912,89.23,6.01,89.05,82.12,0.95
20260828,94.6,95.4,90.8,92.1,4464181,89.47,2.94,89.73,82.38,0.61
20260831,92.9,94.5,91,94.1,4948732,89.86,4.72,90.29,82.64,0.66
20260901,93.3,98.2,92.1,95.6,4930344,90.34,5.83,90.88,82.89,0.65
20260902,96.6,97.3,94.9,96.3,2532689,90.83,6.02,91.42,83.19,0.34
20260903,99.6,103,98.5,99.8,7545575,91.58,8.97,92.14,83.5,0.97
20260904,99.9,104.5,97.9,99.8,6217733,92.27,8.16,92.73,83.9,0.79
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 83.68
- over_600_ratio: 81.75
- over_800_ratio: 80.03
- over_1000_ratio: 78.53
- over_400_change_1w: -0.05
- over_800_change_1w: -0.07
- over_1000_change_1w: -0.16
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,81.48,-0.13,78.07,0.04,76.76,-0.2,4,False,True
20260626,81.29,-0.19,77.76,-0.31,76.45,-0.31,0,False,False
20260703,80.96,-0.33,77.44,-0.32,76,-0.45,0,False,False
20260709,81.83,0.87,78.09,0.65,76.9,0.9,1,True,True
20260717,82.48,0.65,79.12,1.03,77.95,1.05,2,True,True
20260724,82.78,0.3,78.79,-0.33,77.86,-0.09,3,False,False
20260731,82.8,0.02,78.71,-0.08,77.65,-0.21,4,False,False
20260807,83.05,0.25,79.55,0.84,78.27,0.62,5,True,True
20260814,83.26,0.21,79.95,0.4,78.55,0.28,6,True,True
20260821,83.67,0.41,80.24,0.29,78.84,0.29,7,True,True
20260828,83.73,0.06,80.1,-0.14,78.69,-0.15,8,False,False
20260904,83.68,-0.05,80.03,-0.07,78.53,-0.16,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2637 | 慧洋-KY | revenue_pullback | 營收成長股價回檔 | 63.0 |  |  |  |  | no_signal | stale_signal | 1.事實發生日:115/09/03 2.公司名稱:慧洋海運股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:補充公告本公司115年08月份自結盈餘 6.因應措施:發佈重大訊息 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本月營業收入：USD   62,865,093  TWD  2,013,191 (仟元) 去年同期變動率      27.12% 累計營業收入：USD  434,300,632  TWD 13,780,359 (仟元) 去年同期變動率      33.66% 本月營業利益：USD   26,262,462  TWD    841,031 (仟元) 去年同期變動率      82.89% 累計營業利益：USD  157,117,255  TWD  4,985,331 (仟元) 去年同期變動率     206.12% 本月稅前損益：USD   36,048,724  TWD  1,154,427 (仟元) 去年同期變動率      82.93% 累計稅前損益：USD  160,136,238  TWD  5,081,122 (仟元) 去年同期變動率     329.05% 本月稅前每股盈餘：  1.55 累計稅前每股盈餘：  6.81  計算基礎：                               期底      月平均    年平均 新台幣/美元                   31.66     32.204    31.730 日圓/美元                    159.57 	 158.83    158.78 流通股數                    746,409,199   -         - 計算EPS流通在外加權平均股數 746,409,199   -         -                               期底      上月底   去年同期 船舶艘數                       127	   129	     131 BDI                           3186       2732      2025 變動分析： 1.船隊變化： 08/14 Amis Wisdom VI(DWT61456/Supramax)出售。 08/20 Bunun Leader(DWT37650/Handy)出售。 2.營運變化：本月進塢船舶8艘。 3.匯率波動：本公司日幣及瑞士法郎借款因匯率波動而產生損益。 4.船舶換約：本月共2艘船舶換約。 5.營業利益：本月營業利益較去年同期增加82.89%，係因2025年整體市況不佳。 6.業外損益：本月因日圓貶值使業外損益部分有匯兌利益約USD30,000元及新台幣 升值使業外損益部分有匯兌損失約USD600,000元及瑞士法郎貶值使業外損益部分有 匯兌利益約US190,000元。本月因出售兩艘船舶，認列處分利益約USD12,000,000元。 編制說明： 1.本公司採用會計準則為IFRS。 2.本公司以美元為功能性貨幣。新台幣數字係以期間平均匯率計算。但評價損益則依據 相關匯率之期底數值計算。 3.變動率係依本月與前期之美金財務數字作為計算基準。 4.每股盈餘(EPS)之計算基準為加權平均股數。 5.折舊及船員薪資成本採整月認列，租金收入則按日數以應計基礎認列，故營運天數對 營收及營業利益偶有影響。 6.船舶潤滑油費用為按月估列，但每季盤點時將依實際消耗量調整之。 7.船舶折舊年數依船況、噸位、規格等可能有出入，但目前新船大多以25年估列之。 　殘值計算則為空船重量(light ship weight)乘以廢鐵價格估列。 8.本財務資訊系本公司自結數，尚未經會計師查核簽證。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2637 | 慧洋-KY | 24 | 2 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 2637 | 慧洋-KY | 38 | 0 | 5551840.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
