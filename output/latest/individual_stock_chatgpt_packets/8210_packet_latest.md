# INDIVIDUAL STOCK CHATGPT PACKET - 8210 勤誠

## Metadata
- generated_at: 2026-06-18 22:25:02 Asia/Taipei
- stock_id: 8210
- stock_name: 勤誠
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 287
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/8210_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/8210_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8210_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8210_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8210_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8210_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/8210_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/8210_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8210_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8210_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/8210_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/8210_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8210.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8210.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8210.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8210.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8210_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8210_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8210_latest.md?ref=main

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
- risk_control_zh: TDCC 歷史不足
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足

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
- insufficient_tdcc_history

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 1385
- high: 1385
- low: 1345
- close: 1365
- volume: 1146686
- ma5: 1393
- ema23_primary: 1380.73
- distance_to_ema23_pct: -1.14
- ma20: 1403
- ma60: 1213.03
- ma120: 1072.51
- return_5d: -5.21
- return_20d: 2.25
- volume_ratio: 0.66
- distance_to_ma20_pct_auxiliary: -2.71
- distance_to_high_60_pct: -14.15

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,1350,1380,1330,1345,1307613,1281.9,4.92,1320.25,1052.37,0.4
20260525,1400,1455,1380,1435,1653950,1294.66,10.84,1331.5,1061.78,0.54
20260526,1470,1470,1410,1440,1471408,1306.77,10.2,1345.25,1070.63,0.52
20260527,1470,1470,1385,1395,1433207,1314.12,6.15,1356.5,1078.58,0.52
20260528,1400,1420,1315,1325,1726727,1315.03,0.76,1366.75,1085.1,0.63
20260529,1360,1380,1335,1365,1081877,1319.19,3.47,1378.5,1092.65,0.41
20260601,1395,1450,1375,1400,898622,1325.93,5.59,1391,1101.32,0.34
20260602,1410,1465,1350,1375,1496306,1330.01,3.38,1396.5,1108.73,0.58
20260603,1390,1470,1380,1455,1832144,1340.43,8.55,1403,1117.33,0.76
20260604,1440,1475,1380,1420,2305632,1347.06,5.41,1409.5,1126.48,1.08
20260605,1420,1420,1320,1370,1727293,1348.97,1.56,1407.25,1134.53,0.9
20260608,1235,1405,1235,1375,2323580,1351.14,1.77,1398.25,1142.55,1.26
20260609,1410,1510,1380,1510,2963382,1364.38,10.67,1396.25,1153.03,1.7
20260610,1490,1565,1425,1445,3592273,1371.1,5.39,1392.5,1162.22,2.06
20260611,1460,1460,1385,1440,1487382,1376.84,4.59,1391.5,1171.42,0.88
20260612,1495,1520,1445,1475,2007424,1385.02,6.5,1394.75,1181.32,1.17
20260615,1510,1520,1425,1430,1406570,1388.77,2.97,1397.25,1190.32,0.82
20260616,1440,1440,1330,1350,1918902,1385.54,-2.56,1398.5,1197.95,1.09
20260617,1330,1370,1330,1345,877641,1382.16,-2.69,1401.5,1205.17,0.5
20260618,1385,1385,1345,1365,1146686,1380.73,-1.14,1403,1213.03,0.66
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 73.19
- over_600_ratio: 69.01
- over_800_ratio: 66.23
- over_1000_ratio: 63.4
- over_400_change_1w: 2.14
- over_800_change_1w: 1.58
- over_1000_change_1w: 0.93
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,70.73,,65.5,,62.59,,0,False,False
20260508,71.72,0.99,64.94,-0.56,61.32,-1.27,1,False,False
20260515,73.21,1.49,65.76,0.82,62.94,1.62,2,True,True
20260522,73.2,-0.01,65.42,-0.34,61.93,-1.01,3,False,False
20260529,71.51,-1.69,64.85,-0.57,62.67,0.74,4,False,True
20260605,71.05,-0.46,64.65,-0.2,62.47,-0.2,0,False,False
20260612,73.19,2.14,66.23,1.58,63.4,0.93,1,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8210 | 勤誠 | pattern | 型態觀察 | 40.0 |  |  | pullback_entry_zone |  | no_signal | stale_signal | 1.標的物之名稱及性質（屬特別股者，並應標明特別股約定發行條件， 如股息率等）: Andra Capital Fund LP私募基金 2.事實發生日:115/06/16 3.交易單位數量、每單位價格及交易總金額: 無交易數量，無單位價格，認購總金額為美金200萬 4.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司 之關係人者，得免揭露其姓名）: Andra Capital Fund LP，無 5.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及 前次移轉之所有人、前次移轉之所有人與公司及交易相對人間相互之 關係、前次移轉日期及移轉金額: 不適用 6.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告 關係人之取得及處分日期、價格及交易當時與公司之關係: 不適用 7.本次係處分債權之相關事項（含處分之債權附隨擔保品種類、處分 債權如有屬對關係人債權者尚需公告關係人名稱及本次處分該關係人 之債權帳面金額: 不適用 8.處分利益（或損失）（取得有價證券者不適用）（遞延者應列表 說明認列情形）: 不適用 9.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要 約定事項: 依據私募基金合約約定 10.本次交易之決定方式、價格決定之參考依據及決策單位: 本次交易之決定方式、價格決定之參考依據：依據私募基金合約約定 決策單位：依公司核決權限辦理 11.取得或處分有價證券標的公司每股淨值:不適用 12.有價證券標的公司私募參考價格與每股交易金額差距達20%以上:不適用 13.迄目前為止，累積持有本交易證券（含本次交易）之數量、金額、 持股比例及權利受限情形（如質押情形）: 累積持有之數量:不適用。 累積持有之金額: 美金600萬元 持股比例：不適用 權利受限情形：無 14.迄目前為止，私募有價證券投資（含本次交易）占公司最近期財 務報表中總資產及歸屬於母公司業主之權益之比例暨最近期財務報表中營運資金數額: 占總資產比例：0.71% 占歸屬於母公司業主之權益比例：1.49% 營運資金數額：8,439,060仟元 15.經理人及經紀費用: 無 16.取得或處分之具體目的或用途: 長期投資 17.本次交易表示異議董事之意見: 無 18.本次交易為關係人交易: 否 19.董事會通過日期: 不適用 20.監察人承認或審計委員會同意日期: 不適用 21.本次交易會計師出具非合理性意見:不適用 22.會計師事務所名稱: 不適用 23.會計師姓名: 不適用 24.會計師開業證書字號: 不適用 25.其他敘明事項: (1)最近期財務報表係以本公司115年第一季會計師核閱報告之數據為準。 (2)最近期個體財務報表係以本公司114年度會計師查核報告之數據為準。 (3)金額涉及匯率換算者均係美元數以31.36折算新台幣。；calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8210 | 勤誠 | 1 | 1 | 4 | 7 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 8210 | 勤誠 | 182 | 5 | 6920480.0 | 69800.0 | 99.15 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
