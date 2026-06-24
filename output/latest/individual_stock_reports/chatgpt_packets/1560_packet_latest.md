# INDIVIDUAL STOCK CHATGPT PACKET - 1560 中砂

## Metadata
- generated_at: 2026-06-24 22:22:50 Asia/Taipei
- stock_id: 1560
- stock_name: 中砂
- packet_status: standard_180d_window_packet
- latest_price_date: 20260624
- price_rows: 290
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1560_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1560_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1560_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1560_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1560.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1560.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1560.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1560.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1560_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1560_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1560_latest.md?ref=main

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
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
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
- date: 20260624
- open: 719
- high: 770
- low: 719
- close: 749
- volume: 3155320
- ma5: 710.8
- ema23_primary: 680.79
- distance_to_ema23_pct: 10.02
- ma20: 692.8
- ma60: 604.68
- ma120: 519.45
- return_5d: 10.31
- return_20d: 0.94
- volume_ratio: 1.89
- distance_to_ma20_pct_auxiliary: 8.11
- distance_to_high_60_pct: -2.73

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260527,750,750,723,727,2063773,630.46,15.31,629.25,534.08,0.69
20260528,736,741,708,717,1691134,637.68,12.44,639.05,537.59,0.57
20260529,726,731,707,718,1503335,644.37,11.43,647.95,541.27,0.52
20260601,721,727,709,717,1098703,650.42,10.24,655.95,545.48,0.4
20260602,711,715,688,697,3369946,654.3,6.53,662.2,549.12,1.19
20260603,707,733,707,727,1623409,660.36,10.09,669.75,553.12,0.6
20260604,717,730,710,716,1516519,665,7.67,676.7,557.54,0.57
20260605,715,715,694,698,1136132,667.75,4.53,683,561.34,0.45
20260608,629,655,629,649,1525931,666.19,-2.58,684,564.12,0.64
20260609,655,674,655,665,1385999,666.09,-0.16,683.85,567.6,0.64
20260610,655,665,602,609,1587205,661.33,-7.91,682.65,570.08,0.77
20260611,609,631,588,628,2074728,658.55,-4.64,681.55,572.99,1.05
20260612,650,662,636,652,1280779,658.01,-0.91,682.05,576.33,0.67
20260615,672,711,670,703,2024876,661.76,6.23,684.75,579.96,1.04
20260616,711,718,676,679,1637290,663.19,2.38,686.5,583.49,0.83
20260617,679,690,674,687,827697,665.18,3.28,690.4,587.04,0.45
20260618,692,704,689,700,946904,668.08,4.78,691.95,591.34,0.53
20260622,718,744,713,713,1830864,671.82,6.13,693.2,595.79,1.1
20260623,716,722,698,705,1047999,674.59,4.51,692.45,599.88,0.65
20260624,719,770,719,749,3155320,680.79,10.02,692.8,604.68,1.89
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 64.81
- over_600_ratio: 60.19
- over_800_ratio: 53.48
- over_1000_ratio: 48.5
- over_400_change_1w: -0.1
- over_800_change_1w: -1.23
- over_1000_change_1w: -1.37
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.89,,55.66,,51.34,,0,False,False
20260508,66.22,0.33,55.28,-0.38,50.27,-1.07,1,False,False
20260515,67.02,0.8,57.56,2.28,51.36,1.09,2,True,True
20260522,66.78,-0.24,56.1,-1.46,51.1,-0.26,0,False,False
20260529,66.11,-0.67,56.32,0.22,50.85,-0.25,1,False,True
20260605,65.82,-0.29,53.74,-2.58,48.86,-1.99,0,False,False
20260612,64.91,-0.91,54.71,0.97,49.87,1.01,1,False,True
20260618,64.81,-0.1,53.48,-1.23,48.5,-1.37,2,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 1560 | 中砂 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  | call_strong_inflow | continued_2_3d | 1.發生變動日期:115/06/23 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事、獨立董事 3.舊任者職稱及姓名:     職  稱            姓         名   ----------   ----------------------------     董事      金敏投資(股)公司法代：林伯全     董事      金泉投資(股)公司法代：白文亮     董事      金敏投資(股)公司法代：謝榮哲     董事      利和投資(股)公司法代：白景中     董事      金齊投資有限公司法代：李偉彰     董事      金齊投資有限公司法代：洪福益     獨立董事  蔡新源     獨立董事  廖伯熙     獨立董事  蕭文億 4.舊任者簡歷:        姓             名               簡                  歷   ----------------------------  ------------------------------------   金敏投資(股)公司法代：林伯全  本公司董事長   金泉投資(股)公司法代：白文亮  本公司副董事長   金敏投資(股)公司法代：謝榮哲  本公司執行長   利和投資(股)公司法代：白景中  本公司副總經理 　金齊投資有限公司法代：李偉彰  本公司鑽石事業部總經理、本公司發言人 　金齊投資有限公司法代：洪福益  本公司晶圓事業部總經理   蔡新源                        創新智基投融服務(股)公司董事長   廖伯熙                        華南工程(股)公司董事長   蕭文億                        岩鼎資本股份有限公司董事長 5.新任者職稱及姓名:     職  稱            姓         名   ----------   ----------------------------     董事      金敏投資(股)公司法代：林伯全     董事      金泉投資(股)公司法代：白文亮     董事      金敏投資(股)公司法代：謝榮哲     董事      利和投資(股)公司法代：白景中     董事      金齊投資有限公司法代：李偉彰     董事      金齊投資有限公司法代：洪福益     獨立董事  林日璇     獨立董事  張清福     獨立董事  蕭文億 6.新任者簡歷:        姓             名               簡                  歷   ----------------------------  ------------------------------------   金敏投資(股)公司法代：林伯全  本公司董事長   金泉投資(股)公司法代：白文亮  本公司副董事長   金敏投資(股)公司法代：謝榮哲  本公司執行長   利和投資(股)公司法代：白景中  本公司副總經理   金齊投資有限公司法代：李偉彰  本公司鑽石事業部總經理、本公司發言人   金齊投資有限公司法代：洪福益  本公司晶圓事業部總經理   林日璇                        政治大學傳播學院特聘教授   張清福                        曾任勤業眾信聯合會計師事務所合夥會計師   蕭文億                        岩鼎資本股份有限公司董事長 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿全面改選 9.新任者選任時持股數:        姓             名         持有股數   ----------------------------  ----------   金敏投資(股)公司法代：林伯全  9,892,423   金泉投資(股)公司法代：白文亮  4,117,167   金敏投資(股)公司法代：謝榮哲  9,892,423   利和投資(股)公司法代：白景中  2,471,420   金齊投資有限公司法代：李偉彰  4,796,000   金齊投資有限公司法代：洪福益  4,796,000   林日璇                                0   張清福                                0   蕭文億                                0 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/20 ~ 115/06/19 11.新任生效日期:115/06/23 12.同任期董事變動比率:全面改選 13.同任期獨立董事變動比率:全面改選 14.同任期監察人變動比率:不適用 15.屬三分之一以上董事發生變動（請輸入是或否）:否 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項): 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 1560 | 中砂 | 2 | 1 | 2 | 6 | 7 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260624 | 1560 | 中砂 | 133 | 0 | 30532970.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
