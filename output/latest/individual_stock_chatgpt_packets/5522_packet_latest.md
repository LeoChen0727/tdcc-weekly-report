# INDIVIDUAL STOCK CHATGPT PACKET - 5522 遠雄

## Metadata
- generated_at: 2026-06-19 22:24:18 Asia/Taipei
- stock_id: 5522
- stock_name: 遠雄
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/5522_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/5522_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/5522_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/5522_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/5522_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5522.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5522.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5522.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5522.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5522_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5522_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5522_latest.md?ref=main

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
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 歷史不足
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足

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
- insufficient_tdcc_history

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260618
- open: 75.1
- high: 76.7
- low: 74.2
- close: 74.4
- volume: 2047135
- ma5: 76.66
- ema23_primary: 74.9
- distance_to_ema23_pct: -0.67
- ma20: 74.87
- ma60: 72.1
- ma120: 70.98
- return_5d: -7
- return_20d: 5.68
- volume_ratio: 1.24
- distance_to_ma20_pct_auxiliary: -0.63
- distance_to_high_60_pct: -11.32

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,70.3,70.3,69.5,69.5,931098,70.29,-1.13,70,69.67,1.09
20260525,69.9,70.6,68.7,69.2,883165,70.2,-1.43,69.99,69.7,1.02
20260526,69.3,71.2,69.2,71.1,924632,70.28,1.17,70.09,69.76,1.05
20260527,71.2,71.3,70.3,71.2,531484,70.35,1.2,70.23,69.81,0.61
20260528,71.5,72.7,70.8,72,1327165,70.49,2.14,70.37,69.88,1.47
20260529,72,72.7,71.5,72.7,1807328,70.68,2.86,70.56,69.96,1.93
20260601,72.8,74.2,71.9,74.2,1485785,70.97,4.55,70.81,70.09,1.51
20260602,74.1,75.1,73.7,75.1,1394974,71.31,5.31,71.11,70.23,1.35
20260603,75.5,76.7,74,76.2,1886766,71.72,6.25,71.46,70.39,1.72
20260604,75.8,76.4,74.3,74.4,1527146,71.94,3.41,71.69,70.56,1.37
20260605,74.1,76.6,74,76.1,1238287,72.29,5.27,72,70.74,1.11
20260608,72.5,75.3,72.5,74.2,765602,72.45,2.42,72.08,70.88,0.71
20260609,73.2,77.5,73.2,76,1668782,72.75,4.47,72.39,71.06,1.54
20260610,75.5,83.3,74.6,82.2,5246941,73.53,11.79,72.97,71.32,3.98
20260611,83.8,83.9,77.8,80,3510676,74.07,8,73.45,71.52,2.4
20260612,80.7,82.3,79.3,80,1537012,74.57,7.29,73.92,71.69,1.03
20260615,81,81,77.1,77.7,1076473,74.83,3.84,74.19,71.81,0.73
20260616,77.5,78,76.2,76.2,1231832,74.94,1.68,74.46,71.94,0.82
20260617,76,76,74.3,75,1983596,74.95,0.07,74.67,72,1.26
20260618,75.1,76.7,74.2,74.4,2047135,74.9,-0.67,74.87,72.1,1.24
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 89.54
- over_600_ratio: 89
- over_800_ratio: 88.21
- over_1000_ratio: 87.21
- over_400_change_1w: 0.24
- over_800_change_1w: 0.4
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,88.9,,87.68,,86.8,,0,False,False
20260508,89.02,0.12,87.65,-0.03,86.89,0.09,1,False,True
20260515,89.02,0,87.41,-0.24,86.65,-0.24,0,False,False
20260522,89.06,0.04,87.39,-0.02,86.72,0.07,1,False,True
20260529,89.04,-0.02,87.75,0.36,86.75,0.03,2,False,True
20260605,89.3,0.26,87.81,0.06,87.04,0.29,3,True,True
20260612,89.54,0.24,88.21,0.4,87.21,0.17,4,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 5522 | 遠雄 | revenue_pullback | 營收成長股價回檔 | 70.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | repeated_but_no_breakout | 1.契約種類:自地委建 2.事實發生日:115/6/15~115/6/15 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年5月17日 5.契約相對人及其與公司之關係: 交易對象：玴偉工程股份有限公司  與公司之關係：無 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 本次簽訂建築工程契約為：高雄市楠梓區藍田西段住宅大樓 新建工程（水電消防工程）承攬契約書 契約總金額為新台幣628,000仟元 限制條款及其他重要約定事項：無 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 擴增公司營業收入 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 不適用 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260618 | 5522 | 遠雄 | revenue_breakout_low_response | 營收爆發低反應股 | 20.0 | 15.0 | B_可觀察 |  |  |  | repeated_but_no_breakout | 1.契約種類:自地委建 2.事實發生日:115/6/15~115/6/15 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長核決 民國115年5月17日 5.契約相對人及其與公司之關係: 交易對象：玴偉工程股份有限公司  與公司之關係：無 6.契約主要內容（含契約總金額、預計參與投入之金額及契約起迄日期） 、限制條款及其他重要約定事項: 本次簽訂建築工程契約為：高雄市楠梓區藍田西段住宅大樓 新建工程（水電消防工程）承攬契約書 契約總金額為新台幣628,000仟元 限制條款及其他重要約定事項：無 7.專業估價者事務所或公司名稱及其估價結果: 不適用 8.不動產估價師姓名: 不適用 9.不動產估價師開業證書字號: 不適用 10.取得之具體目的: 擴增公司營業收入 11.本次交易表示異議之董事意見: 無 12.本次交易為關係人交易:否 13.監察人承認或審計委員會同意日期: 不適用 14.估價報告是否為限定價格、特定價格或特殊價格:否或不適用 15.是否尚未取得估價報告:否或不適用 16.尚未取得估價報告之原因: 不適用 17.估價結果有重大差異時，其差異原因及會計師意見: 不適用 18.會計師事務所名稱: 不適用 19.會計師姓名: 不適用 20.會計師開業證書字號: 不適用 21.前已就同一件事件發布重大訊息日期: 不適用 22.其他敘明事項: 無；calendar event: ex_dividend on 20260625; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 5522 | 遠雄 | 12 | 8 | 5 | 10 | 12 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 12 次，但尚未有效突破，需等待攻擊確認。 |

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
