# INDIVIDUAL STOCK CHATGPT PACKET - 5269 祥碩

## Metadata
- generated_at: 2026-07-03 22:27:27 Asia/Taipei
- stock_id: 5269
- stock_name: 祥碩
- packet_status: standard_180d_window_packet
- latest_price_date: 20260703
- price_rows: 297
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5269_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5269_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5269_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5269_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5269_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5269_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5269_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5269.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5269.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5269.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5269.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5269_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5269_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5269_latest.md?ref=main

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
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- date: 20260703
- open: 1510
- high: 1585
- low: 1500
- close: 1530
- volume: 1799131
- ma5: 1493
- ema23_primary: 1448.52
- distance_to_ema23_pct: 5.62
- ma20: 1430
- ma60: 1390.92
- ma120: 1317.54
- return_5d: 12.09
- return_20d: -2.55
- volume_ratio: 1.48
- distance_to_ma20_pct_auxiliary: 6.99
- distance_to_high_60_pct: -7.83

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260605,1570,1570,1495,1525,1332317,1463.68,4.19,1478.5,1308.33,0.52
20260608,1375,1420,1375,1400,1542981,1458.38,-4,1479,1310.67,0.62
20260609,1415,1465,1390,1440,1193487,1456.84,-1.16,1474.75,1314.25,0.53
20260610,1385,1410,1320,1325,2290023,1445.86,-8.36,1469.5,1315.92,1.12
20260611,1310,1345,1275,1330,1232988,1436.2,-7.39,1462.75,1317.92,0.64
20260612,1380,1395,1360,1375,938820,1431.1,-3.92,1458.75,1320.75,0.51
20260615,1400,1415,1380,1380,772833,1426.84,-3.28,1458.25,1322.92,0.44
20260616,1395,1400,1365,1380,665876,1422.94,-3.02,1458.25,1325.83,0.38
20260617,1370,1435,1360,1425,1070861,1423.11,0.13,1460.25,1329.58,0.63
20260618,1455,1475,1425,1455,1126161,1425.77,2.05,1462.5,1334.5,0.69
20260622,1470,1480,1445,1450,833855,1427.79,1.56,1461,1339.42,0.52
20260623,1460,1470,1400,1425,892824,1427.56,-0.18,1455.5,1343.58,0.59
20260624,1395,1430,1385,1425,637646,1427.34,-0.16,1449.5,1347.67,0.45
20260625,1435,1445,1415,1435,671689,1427.98,0.49,1446.5,1352.17,0.5
20260626,1420,1430,1365,1365,944858,1422.73,-4.06,1442.75,1356.42,0.72
20260629,1390,1500,1385,1475,2006581,1427.09,3.36,1443.25,1363.25,1.49
20260630,1510,1510,1470,1470,1224000,1430.66,2.75,1440.75,1369.5,0.91
20260701,1500,1535,1470,1470,1702000,1433.94,2.51,1434.75,1376.33,1.39
20260702,1450,1550,1450,1520,1482000,1441.11,5.47,1432,1383.92,1.23
20260703,1510,1585,1500,1530,1799131,1448.52,5.62,1430,1390.92,1.48
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 55.56
- over_600_ratio: 53.42
- over_800_ratio: 51.61
- over_1000_ratio: 51.61
- over_400_change_1w: 0.01
- over_800_change_1w: 0
- over_1000_change_1w: 0
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.83,,55.66,,55.66,,0,False,False
20260508,58.33,-1.5,54.25,-1.41,54.25,-1.41,0,False,False
20260515,56.62,-1.71,53.59,-0.66,53.59,-0.66,0,False,False
20260522,54.68,-1.94,51.18,-2.41,51.18,-2.41,0,False,False
20260529,54.94,0.26,51.18,0,51.18,0,1,False,False
20260605,55.79,0.85,51.61,0.43,51.61,0.43,2,True,True
20260612,55.49,-0.3,51.61,0,51.61,0,3,False,False
20260618,55.55,0.06,51.61,0,51.61,0,4,False,False
20260626,55.56,0.01,51.61,0,51.61,0,5,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5269 | 祥碩 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | no_signal | stale_signal | 1.發生變動日期:115/06/17 2.選任或變動人員別（請輸入法人董事、法人監察人、獨立董事、自然人董事   或自然人監察人）:法人董事、獨立董事、自然人董事 3.舊任者職稱及姓名: (一)董事：     華碩電腦(股)公司代表人：徐世昌     華碩電腦(股)公司代表人：沈振來     華碩電腦(股)公司代表人：林哲偉     許金川 (二)獨立董事：     詹宏志     謝劍平     吳靜吉     金聯舫 4.舊任者簡歷: (一)董事：     華碩電腦(股)公司代表人徐世昌：祥碩科技(股)公司董事長     華碩電腦(股)公司代表人沈振來：祥碩科技(股)公司董事     華碩電腦(股)公司代表人林哲偉：祥碩科技(股)公司總經理     許金川：國立台灣大學醫學院內科名譽教授 (二)獨立董事：     詹宏志：網路家庭國際資訊(股)公司董事長     謝劍平：台灣科技大學財務金融所教授     吳靜吉：政治大學名譽教授     金聯舫：清華大學科管院榮譽講座教授 5.新任者職稱及姓名: (一)董事：     華碩電腦(股)公司代表人：徐世昌     華碩電腦(股)公司代表人：沈振來     華碩電腦(股)公司代表人：林哲偉     華碩電腦(股)公司代表人：許先越     許金川 (二)獨立董事：     謝劍平     金聯舫     林嬋娟     高壽延 6.新任者簡歷: (一)董事：     華碩電腦(股)公司代表人徐世昌：祥碩科技(股)公司董事長     華碩電腦(股)公司代表人沈振來：祥碩科技(股)公司董事     華碩電腦(股)公司代表人林哲偉：祥碩科技(股)公司總經理     華碩電腦(股)公司代表人許先越：華碩電腦(股)公司董事兼共同執行長     許金川：國立台灣大學醫學院內科名譽教授 (二)獨立董事：     謝劍平：台灣科技大學財務金融所教授     金聯舫：清華大學科管院榮譽講座教授     林嬋娟：臺灣大學會計學系名譽教授     高壽延：陽明交通大學牙醫學院教授 7.異動情形（請輸入「辭職」、「解任」、「任期屆滿」、「逝世」或「新任」）: 任期屆滿 8.異動原因:任期屆滿全面改選 9.新任者選任時持股數: (一)董事：     華碩電腦(股)公司：24,457,660股     許金川：0股 (二)獨立董事：     謝劍平：0股     金聯舫：0股     林嬋娟：0股     高壽延：0股 10.原任期（例xx/xx/xx ~ xx/xx/xx）:112/06/16~115/06/15 11.新任生效日期:115/06/17 12.同任期董事變動比率:不適用(董事全面改選) 13.同任期獨立董事變動比率:不適用(董事全面改選) 14.同任期監察人變動比率:不適用。 15.屬三分之一以上董事發生變動（請輸入是或否）:否。 16.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司，本則重大訊息同時    符合證券交易法施行細則第7條第6款所定對股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5269 | 祥碩 | 2 | 2 | 4 | 5 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 5269 | 祥碩 | 160 | 0 | 42820840.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
