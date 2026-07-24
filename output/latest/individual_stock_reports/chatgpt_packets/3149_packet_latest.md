# INDIVIDUAL STOCK CHATGPT PACKET - 3149 正達

## Metadata
- generated_at: 2026-07-24 22:27:01 Asia/Taipei
- stock_id: 3149
- stock_name: 正達
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 306
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 12
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3149_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3149_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3149_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3149_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3149_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3149_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3149_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3149.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3149.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3149.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3149.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3149_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3149_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3149_latest.md?ref=main

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
- action_rating_display_zh: 可分批買進
- model_category_display_zh: 營收成長股價回檔
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
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
- date: 20260717
- open: 81.8
- high: 89.8
- low: 79.3
- close: 79.6
- volume: 15884113
- ma5: 88.58
- ema23_primary: 88.19
- distance_to_ema23_pct: -9.74
- ma20: 92.56
- ma60: 73.87
- ma120: 61.16
- return_5d: -11.06
- return_20d: -15.05
- volume_ratio: 0.93
- distance_to_ma20_pct_auxiliary: -14.01
- distance_to_high_60_pct: -26.97

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,96.3,96.3,93.7,95,5487747,78.89,20.42,80.83,58.4,0.26
20260622,99,104.5,99,104.5,7386968,81.03,28.97,83.1,59.43,0.37
20260623,103,106.5,94.1,94.1,29907719,82.11,14.6,84.56,60.26,1.54
20260624,91.9,103.5,91.3,102,35986755,83.77,21.76,86.25,61.18,1.87
20260625,106,106,97.5,100,19115583,85.12,17.48,87.98,62.08,1.01
20260626,100,109,97.5,97.8,29433525,86.18,13.48,89.52,62.96,1.57
20260629,98,101,92.7,92.7,19314301,86.72,6.89,90.59,63.78,1.06
20260630,96,101.5,95.1,101.5,26009336,87.96,15.4,91.75,64.72,1.35
20260701,103.5,105,93.5,94,30766534,88.46,6.26,92.15,65.56,1.63
20260702,90,95.3,89.3,90.5,16364988,88.63,2.11,92.14,66.38,0.95
20260703,90,91.2,86.1,87.2,17207301,88.51,-1.48,91.94,67.11,1.08
20260706,88.7,91.5,87.8,87.9,9560577,88.46,-0.63,91.8,67.89,0.65
20260707,88.9,90.3,84.3,86.2,10761415,88.27,-2.35,91.77,68.64,0.73
20260708,86.5,87.7,83.8,85.5,7512410,88.04,-2.89,91.69,69.37,0.51
20260709,87,92.7,86,89.5,14243359,88.16,1.52,92.05,70.14,0.94
20260713,91,95.5,90.4,92.3,15950647,88.51,4.29,92.64,70.98,1.02
20260714,93,93.3,84.6,87.3,8530608,88.41,-1.25,92.86,71.73,0.54
20260715,89.2,91,87.4,90.2,5774000,88.56,1.86,93,72.53,0.36
20260716,88.9,97.8,88.9,93.5,15539391,88.97,5.09,93.27,73.32,0.93
20260717,81.8,89.8,79.3,79.6,15884113,88.19,-9.74,92.56,73.87,0.93
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 25.19
- over_600_ratio: 21.78
- over_800_ratio: 21.11
- over_1000_ratio: 19.14
- over_400_change_1w: 1.63
- over_800_change_1w: 2.19
- over_1000_change_1w: 2.21
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,34.35,,28.63,,26.97,,0,False,False
20260508,33.04,-1.31,27.3,-1.33,26.08,-0.89,0,False,False
20260515,33.36,0.32,27.44,0.14,24.61,-1.47,1,False,True
20260522,27.66,-5.7,22.98,-4.46,22.15,-2.46,0,False,False
20260529,30.7,3.04,26.63,3.65,25.03,2.88,1,True,True
20260605,27.36,-3.34,23.34,-3.29,21.35,-3.68,0,False,False
20260612,28.17,0.81,23.77,0.43,22.21,0.86,1,True,True
20260618,29.01,0.84,25.12,1.35,23.2,0.99,2,True,True
20260626,25.16,-3.85,20.47,-4.65,18.8,-4.4,0,False,False
20260703,23.05,-2.11,19.24,-1.23,16.51,-2.29,0,False,False
20260709,23.56,0.51,18.92,-0.32,16.93,0.42,1,False,True
20260717,25.19,1.63,21.11,2.19,19.14,2.21,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3149 | 正達 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | stale_signal | 1.董事會決議或公司決定增資基準日期:115/07/02 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/06/30 4.董事會決議(追補)發行日期:115/03/20 5.發行總金額及股數:   (1)發行總金額：新台幣3,660,000,000元   (2)發行股數：60,000,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股發行價格新台幣61元整。 10.員工認股股數:   依公司法267條規定，保留10%（計6,000,000股）由本公司員工認購 11.原股東認購比率:   增資發行股數之80%（計48,000,000股），由原股東按照認股基準日   股東名簿記載之持股比例認購，每仟股可認購212.17007178股 12.公開銷售方式及股數:   依證券交易法第28條之1規定，發行新股額度10%（計6,000,000股）   對外公開承銷 13.畸零股及逾期未認購股份之處理方式:   原股東認購不足一股之畸零股，由股東自停止過戶日起五日內自行至本公司股務   代理機構辦理拼湊一整股認購。原股東及員工放棄認購或拼湊不足一股之畸零股   部分，由董事會授權董事長洽特定人按發行價格認足。 14.本次發行新股之權利義務:與已發行之原有股份相同。 15.本次增資資金用途:充實營運資金、償還銀行借款、購買機器設備及廠務設施、   轉投資子公司 16.現金增資認股基準日:115/07/25 17.最後過戶日:115/07/20 18.停止過戶起始日期:115/07/21 19.停止過戶截止日期:115/07/25 20.股款繳納期間:    (1)原股東及員工股款繳納期間：115/07/29~115/08/04    (2)特定人認股繳款期間：115/08/05~115/08/06 21.與代收及專戶存儲價款行庫訂約日期:115/07/13 (補充公告) 22.委託代收存款機構:合作金庫商業銀行北苗栗分行。(補充公告) 23.委託存儲款項機構:板信商業銀行苗栗分行。(補充公告) 24.其他應敘明事項:    (1)本次現金增資發行新股業經金融監督管理委員會115年6月30日金管證發字        第1150339318號函核准在案。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 3149 | 正達 | 18 | 2 | 5 | 10 | 18 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
