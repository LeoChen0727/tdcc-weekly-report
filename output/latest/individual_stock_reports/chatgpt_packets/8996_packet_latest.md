# INDIVIDUAL STOCK CHATGPT PACKET - 8996 高力

## Metadata
- generated_at: 2026-07-13 22:29:13 Asia/Taipei
- stock_id: 8996
- stock_name: 高力
- packet_status: standard_180d_window_packet
- latest_price_date: 20260709
- price_rows: 301
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8996_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8996_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8996_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8996_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8996.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8996.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8996.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8996.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8996_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8996_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8996_latest.md?ref=main

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
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊

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
- decision_score_high
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
- date: 20260709
- open: 1350
- high: 1350
- low: 1220
- close: 1230
- volume: 1967686
- ma5: 1338
- ema23_primary: 1351.07
- distance_to_ema23_pct: -8.96
- ma20: 1399.75
- ma60: 1220.48
- ma120: 1023.41
- return_5d: -13.07
- return_20d: 0.82
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: -12.13
- distance_to_high_60_pct: -26.79

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,1250,1250,1110,1140,4040924,1134.76,0.46,1123.45,1063.8,1.13
20260612,1215,1225,1135,1145,3113938,1135.62,0.83,1128.7,1067.58,0.86
20260615,1195,1255,1190,1255,1450761,1145.57,9.55,1139.2,1072.63,0.41
20260616,1310,1380,1265,1380,3490273,1165.1,18.44,1156.2,1079.78,0.95
20260617,1400,1515,1395,1515,4404786,1194.26,26.86,1182.25,1089.85,1.19
20260618,1555,1660,1555,1590,5947423,1227.24,29.56,1208.5,1102.68,1.53
20260622,1680,1680,1520,1555,3842264,1254.55,23.95,1227.75,1115.73,0.98
20260623,1500,1510,1420,1450,3344487,1270.84,14.1,1243.5,1126.23,0.86
20260624,1415,1500,1375,1450,859746,1285.77,12.77,1253.75,1136.32,0.23
20260625,1485,1485,1410,1460,501103,1300.29,12.28,1266,1146.23,0.14
20260626,1445,1460,1360,1370,1090661,1306.1,4.89,1279.75,1154.15,0.33
20260629,1370,1475,1370,1475,669708,1320.17,11.73,1299,1164.63,0.21
20260630,1450,1590,1450,1550,842000,1339.33,15.73,1324.25,1175.33,0.27
20260701,1620,1620,1540,1555,648000,1357.3,14.57,1349.5,1186.82,0.21
20260702,1510,1510,1410,1415,1098000,1362.11,3.88,1365.5,1195.33,0.37
20260703,1405,1420,1315,1380,1321026,1363.6,1.2,1378.5,1202.98,0.46
20260706,1430,1440,1380,1425,684000,1368.71,4.11,1393.5,1209.9,0.25
20260707,1455,1455,1325,1335,758662,1365.9,-2.26,1399.75,1214.82,0.3
20260708,1335,1415,1295,1320,2225037,1362.08,-3.09,1399.25,1218.57,0.95
20260709,1350,1350,1220,1230,1967686,1351.07,-8.96,1399.75,1220.48,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 51.66
- over_600_ratio: 42.28
- over_800_ratio: 38.64
- over_1000_ratio: 32.88
- over_400_change_1w: -0.12
- over_800_change_1w: 0.3
- over_1000_change_1w: -1.68
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,54.74,,41.17,,36.39,,0,False,False
20260508,53.38,-1.36,40.01,-1.16,35.3,-1.09,1,False,False
20260515,52.71,-0.67,39.62,-0.39,33.2,-2.1,2,False,False
20260522,53.55,0.84,38.67,-0.95,34.12,0.92,3,False,True
20260529,52.01,-1.54,34.81,-3.86,30.06,-4.06,0,False,False
20260605,52.11,0.1,35.65,0.84,30.79,0.73,1,True,True
20260612,52.25,0.14,39.07,3.42,31.46,0.67,2,True,True
20260618,52.16,-0.09,39.38,0.31,31.54,0.08,3,False,True
20260626,51.78,-0.38,38.34,-1.04,34.56,3.02,4,False,True
20260703,51.66,-0.12,38.64,0.3,32.88,-1.68,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 8996 | 高力 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 內容：依高力四發行及轉換辦法第十八條第二項規定辦理。 發行公司於115年07月27日至115年08月27日行使債券贖回權，贖回權價格為債券面額之100.0000% (一)本轉換公司債於發行日後屆滿三個月之翌日(民國113年3月7日)起至發行期間屆滿前四十日(民國117年10月27日)止，若本轉換公司債流通在外餘額低於原發行總額之百分之十時，本公司得於其後任何時間，以掛號寄發一份三十日期滿之「債券收回通知書」(前述期間自本公司發信之日起算，並以該期間屆滿日為債券收回基準日，且前述期間不得為第九條之停止轉換期間)予債券持有人(以「債券收回通知書」寄發日前第五個營業日債券持有人名冊所載者為準，對於其後因買賣或其他原因始取得本轉換公司債之債券持有人，則以公告方式為之)，贖回價格訂為本債券面額，以現金收回其全部債券，並函請櫃檯買賣中心公告。本公司執行收回請求，應於債券收回基準日後五個營業日內，按債券面額以現金收回流通在外之本轉換公司債。 (二)、轉換公司債停止過戶期間：不適用 (三)、通知及受理轉換公司債贖回期間：115年7月27日至115年8月27日 (四)、轉換公司債收回基準日：115年8月27日 (五)、轉換公司債終止櫃檯買賣日期:115年8月28日 (六)、掛號寄發債券收回通知書日期:115年7月24日 (七)、債券收回手續 (1)、債券己存於台灣集中保管結算所股份有限公司者: 債權人得自債券收回通知之始日（115年7月27日）起至屆滿日（115年8月27日）之前一營業日止、由債券持有人向往來券商辦理賣回手續。 (八)、如債券持有人不欲公司行使贖回權，擬請求將本轉換公司債轉換為普通股，最遲應於115年8月31日前至往來證券商辦理轉換手續。 (九)、公司股務代理機構（包括地址及電話）: 兆豐證券(股)公司股務代理本部，地址： 100台北市忠孝東路二段95號1樓，電話： (02)3393-0898。 警語：請投資人注意，具有請求轉換資格者，如未於115年8月31日前以書面請求轉換，本公司將按面額計算以現金收回其全部債券。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 8996 | 高力 | 2 | 2 | 3 | 5 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
