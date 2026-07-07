# INDIVIDUAL STOCK CHATGPT PACKET - 2637 慧洋-KY

## Metadata
- generated_at: 2026-07-07 22:27:05 Asia/Taipei
- stock_id: 2637
- stock_name: 慧洋-KY
- packet_status: standard_180d_window_packet
- latest_price_date: 20260707
- price_rows: 299
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
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
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: healthy_pullback
- entry_style: pullback_to_23ema
- position_sizing: half_position

### management_plan
- buy_first_tranche_near_support
- add_on_23ema_hold
- add_on_reclaim_23ema
- add_on_breakout
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
- date: 20260707
- open: 77.8
- high: 79.7
- low: 77.8
- close: 79
- volume: 4476071
- ma5: 74.96
- ema23_primary: 75.59
- distance_to_ema23_pct: 4.51
- ma20: 76.17
- ma60: 74.87
- ma120: 72.56
- return_5d: 8.82
- return_20d: 0.64
- volume_ratio: 1.01
- distance_to_ma20_pct_auxiliary: 3.71
- distance_to_high_60_pct: -5.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260609,78.8,81.5,78.6,80.9,10323999,76.06,6.37,75.44,72.81,2.02
20260610,77.2,78.2,75.6,76,11440134,76.05,-0.07,75.55,72.97,2.04
20260611,76,78.3,75.9,78.3,7257113,76.24,2.7,75.72,73.09,1.24
20260612,78.5,79.7,77.4,78.5,6639638,76.43,2.71,76,73.21,1.1
20260615,79,79.8,77.2,79.2,4322269,76.66,3.32,76.32,73.33,0.7
20260616,79.2,80.7,77.5,78.4,6026130,76.8,2.08,76.7,73.44,0.95
20260617,78.4,78.4,75.8,77.4,4925604,76.85,0.71,76.98,73.56,0.76
20260618,76.8,77.4,75.4,77.4,5408866,76.9,0.65,77.25,73.72,0.82
20260622,77.9,77.9,76.3,77.1,2003159,76.92,0.24,77.55,73.85,0.3
20260623,77.3,77.4,76.2,76.8,2241864,76.91,-0.14,77.64,73.95,0.35
20260624,76.7,76.8,75.1,75.7,2701575,76.81,-1.44,77.68,74.07,0.42
20260625,76,76.3,75.4,76.1,2628435,76.75,-0.84,77.69,74.19,0.42
20260626,75.6,75.9,71.6,71.7,4074745,76.33,-6.06,77.44,74.24,0.66
20260629,72.4,73.1,70.9,72.6,2266513,76.02,-4.49,77.31,74.33,0.37
20260630,72.9,73.3,72.2,72.6,1905000,75.73,-4.13,77,74.39,0.32
20260701,73.6,73.6,71,71.4,2532000,75.37,-5.27,76.72,74.45,0.44
20260702,71.2,72.2,70.8,71.7,1546000,75.06,-4.48,76.45,74.51,0.27
20260703,71.7,74.4,71.7,74.3,2188340,75,-0.93,76.26,74.59,0.41
20260706,76.9,78.9,76.1,78.4,3787000,75.28,4.14,76.15,74.72,0.8
20260707,77.8,79.7,77.8,79,4476071,75.59,4.51,76.17,74.87,1.01
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 80.96
- over_600_ratio: 79.25
- over_800_ratio: 77.44
- over_1000_ratio: 76
- over_400_change_1w: -0.33
- over_800_change_1w: -0.32
- over_1000_change_1w: -0.45
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,80.24,,76.52,,75.35,,0,False,False
20260508,81.02,0.78,77.13,0.61,75.94,0.59,1,True,True
20260515,80.87,-0.15,76.95,-0.18,75.76,-0.18,0,False,False
20260522,80.69,-0.18,76.72,-0.23,75.18,-0.58,0,False,False
20260529,81.11,0.42,77.47,0.75,75.81,0.63,1,True,True
20260605,81.35,0.24,77.48,0.01,76.4,0.59,2,True,True
20260612,81.61,0.26,78.03,0.55,76.96,0.56,3,True,True
20260618,81.48,-0.13,78.07,0.04,76.76,-0.2,4,False,True
20260626,81.29,-0.19,77.76,-0.31,76.45,-0.31,0,False,False
20260703,80.96,-0.33,77.44,-0.32,76,-0.45,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260707 | 2637 | 慧洋-KY | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_inflow | repeated_but_no_breakout | 1.事實發生日:115/07/03 2.公司名稱:慧洋海運股份有限公司 3.與公司關係(請輸入本公司或子公司):本公司 4.相互持股比例:不適用 5.發生緣由:補充公告本公司115年06月份自結盈餘 6.因應措施:發佈重大訊息 7.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時   符合證券交易法施行細則第7條第9款所定對股東權益或證券價格有重大影響之事項): 本月營業收入：USD   59,404,563  TWD  1,877,838 (仟元) 去年同期變動率      48.23% 累計營業收入：USD  306,296,491  TWD  9,679,888 (仟元) 去年同期變動率      33.37% 本月營業利益：USD   26,102,519  TWD    825,126 (仟元) 去年同期變動率     268.24% 累計營業利益：USD  102,195,568  TWD  3,229,687 (仟元) 去年同期變動率     286.64% 本月稅前損益：USD   29,634,788  TWD    936,785 (仟元) 去年同期變動率    2150.10% 累計稅前損益：USD   97,082,878  TWD  3,068,110 (仟元) 去年同期變動率     945.74% 本月稅前每股盈餘：  1.26 累計稅前每股盈餘：  4.11  計算基礎：                               期底      月平均    年平均 新台幣/美元                   31.83     31.611    31.603 日圓/美元                    162.26 	 160.66    158.15 流通股數                    746,409,199   -         - 計算EPS流通在外加權平均股數 746,409,199   -         -                               期底      上月底   去年同期 船舶艘數                       130	   130	     132 BDI                           2501       3224      1489 變動分析： 1.船隊變化： 06/11 Taokas Wisdom(DWT31943/Handy)出售。 06/22 Paiwan Elegance(DWT40000/Handy)加入營運。 2.營運變化：本月進塢船舶3艘。 3.匯率波動：本公司日幣及瑞士法郎借款因匯率波動而產生損益。 4.船舶換約：本月換約船舶1艘。 5.營業利益：本月營業利益較去年同期增加268.24%，係因2025年上半年市況不佳。 6.業外損益：本月因日圓貶值使業外損益部分有匯兌利益約USD500,000元及新台幣 貶值使業外損益部分有匯兌利益約USD1,400,000元及瑞士法郎升值使業外損益部分有 匯兌利益約US2,900,000元。本月另因出售一艘船舶，認列處分利益約USD960,000元。 編制說明： 1.本公司採用會計準則為IFRS。 2.本公司以美元為功能性貨幣。新台幣數字係以期間平均匯率計算。但評價損益則依據 相關匯率之期底數值計算。 3.變動率係依本月與前期之美金財務數字作為計算基準。 4.每股盈餘(EPS)之計算基準為加權平均股數。 5.折舊及船員薪資成本採整月認列，租金收入則按日數以應計基礎認列，故營運天數對 營收及營業利益偶有影響。 6.船舶潤滑油費用為按月估列，但每季盤點時將依實際消耗量調整之。 7.船舶折舊年數依船況、噸位、規格等可能有出入，但目前新船大多以25年估列之。 　殘值計算則為空船重量(light ship weight)乘以廢鐵價格估列。 8.本財務資訊系本公司自結數，尚未經會計師查核簽證。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260707 | 2637 | 慧洋-KY | 4 | 1 | 4 | 9 | 18 | repeated_but_no_breakout | 近 10 日上榜 9 次、近 20 日上榜 18 次，但尚未有效突破，需等待攻擊確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260707 | 2637 | 慧洋-KY | 21 | 0 | 2366620.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
