# INDIVIDUAL STOCK CHATGPT PACKET - 8042 金山電

## Metadata
- generated_at: 2026-09-12 22:17:57 Asia/Taipei
- stock_id: 8042
- stock_name: 金山電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260911
- price_rows: 218
- current_main_price_date: 20260911
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260911-3ac576b2856cc687
- official_tdcc_signal_date: 20260911
- latest_tdcc_date: 20260911
- tdcc_rows: 20
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/8042_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/8042_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/8042_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8042_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8042_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/8042_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/8042_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/8042.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/8042.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/8042.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/8042.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/8042_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/8042_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/8042_latest.md?ref=main

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
- model_category_display_zh: 型態觀察
- score_interpretation_zh: 模型分數偏低，僅適合作為低部位觀察。 目前以既有部位管理與條件追蹤為主。
- action_summary_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。
- entry_strategy_zh: 已持有以續抱管理為主；新買需等待重新出現進場條件。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 型態觀察 目前屬於「訊號不明」，以既有部位管理與條件追蹤為主。 進場策略：已持有以續抱管理為主；新買需等待重新出現進場條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260911
- open: 116
- high: 121.5
- low: 112.5
- close: 113
- volume: 11068000
- ma5: 116.1
- ema23_primary: 111.73
- distance_to_ema23_pct: 1.14
- ma20: 107.38
- ma60: 132.29
- ma120: 115.08
- return_5d: 2.26
- return_20d: 0.44
- volume_ratio: 1.88
- distance_to_ma20_pct_auxiliary: 5.24
- distance_to_high_60_pct: -50.22

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260817,110.5,111,106,108.5,2189000,120.28,-9.8,111.69,147.75,0.43
20260818,108.5,109.5,101,101.5,2233000,118.72,-14.5,110.75,147.39,0.46
20260819,99.2,111.5,98.5,111.5,5692000,118.12,-5.6,109.84,147,1.18
20260820,110.5,111,100.5,101,8503000,116.69,-13.45,108.72,146.23,1.69
20260821,101,103,99,99.6,2616000,115.27,-13.59,108,145.38,0.52
20260824,98.9,102.5,98.9,99,1512000,113.91,-13.09,107.08,144.51,0.31
20260825,97.6,99.4,93.2,98.9,2357000,112.66,-12.21,106.72,143.58,0.49
20260826,99,100.5,97.1,99,1900000,111.52,-11.23,106.9,142.41,0.4
20260827,100.5,107,98.1,104.5,4577000,110.94,-5.8,107.64,141.46,0.98
20260828,109,114,105.5,109,8456000,110.77,-1.6,108.15,140.57,1.67
20260831,107,115,100.5,105,5613000,110.29,-4.8,107.97,139.84,1.07
20260901,105.5,114,105.5,107.5,4390000,110.06,-2.33,107.83,139.21,0.85
20260902,106,114,101.5,111,4403000,110.14,0.78,107.88,138.86,0.86
20260903,113,113.5,100,100.5,6165000,109.34,-8.08,107.28,138.14,1.18
20260904,104,110.5,104,110.5,8888000,109.43,0.98,106.97,137.63,1.62
20260907,113.5,121.5,111.5,121.5,11464000,110.44,10.02,107.35,137.07,2.01
20260908,121.5,121.5,112,113,10740000,110.65,2.12,107.17,136.12,1.96
20260909,115,117,112,112.5,4856000,110.81,1.53,107.15,134.87,0.9
20260910,111.5,123.5,107.5,120.5,9919000,111.61,7.96,107.35,133.66,1.8
20260911,116,121.5,112.5,113,11068000,111.73,1.14,107.38,132.29,1.88
```

## Latest TDCC Snapshot
- as_of_date: 20260911
- over_400_ratio: 66.83
- over_600_ratio: 62.86
- over_800_ratio: 60.28
- over_1000_ratio: 59.59
- over_400_change_1w: 3.2
- over_800_change_1w: 1.36
- over_1000_change_1w: 1.39
- tdcc_consecutive_up_weeks: 3
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260626,73,0.9,66.41,0.46,65,-0.33,2,False,True
20260703,72.5,-0.5,66.5,0.09,64.46,-0.54,3,False,True
20260709,68.07,-4.43,62.19,-4.31,59.48,-4.98,0,False,False
20260717,67.15,-0.92,59.52,-2.67,57.65,-1.83,0,False,False
20260724,66.69,-0.46,60.55,1.03,58.47,0.82,1,False,True
20260731,66.34,-0.35,59.82,-0.73,59.15,0.68,2,False,True
20260807,66.17,-0.17,59.58,-0.24,58.18,-0.97,0,False,False
20260814,64.43,-1.74,59.54,-0.04,58.94,0.76,1,False,True
20260821,64.13,-0.3,58.82,-0.72,58.16,-0.78,0,False,False
20260828,65.01,0.88,58.82,0,58.16,0,1,False,False
20260904,63.63,-1.38,58.92,0.1,58.2,0.04,2,False,True
20260911,66.83,3.2,60.28,1.36,59.59,1.39,3,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8042 | 金山電 | pattern | 型態觀察 | 54.0 |  |  | platform_right_side |  |  | repeated_but_no_breakout | 1.董事會決議或公司決定增資基準日期:115/08/27 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/08/19 4.董事會決議(追補)發行日期:115/07/31 5.發行總金額及股數:新臺幣90,000仟元、普通股9,000仟股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新臺幣10元 9.發行價格:俟定價後另行公告 10.員工認股股數:依公司法第267條規定，保留10%計900仟股由員工認購。 11.原股東認購比率:提撥本次發行股數之80%，計7,200仟股由原股東按認股基準日之股 東名簿所載持股比例認購。 12.公開銷售方式及股數:提撥發行新股總額10%，計900仟股辦理公開申購。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止過戶日 起五日內由股東向本公司股務代理機構辦理拼湊，原股東及員工放棄認購之股份或拼湊 不足一股之畸零股，授權董事長洽特定人按發行價格認購之。 14.本次發行新股之權利義務:與原已發行普通股股份相同 15.本次增資資金用途:償還銀行借款 16.現金增資認股基準日:115/09/28 17.最後過戶日:115/09/23 18.停止過戶起始日期:115/09/24 19.停止過戶截止日期:115/09/28 20.股款繳納期間: 原股東及員工繳款期間：115/10/06~115/11/06 特定人繳款期間：115/11/09~115/11/13 21.與代收及專戶存儲價款行庫訂約日期:待正式簽約後另行公告之。 22.委託代收存款機構:待正式簽約後另行公告之。 23.委託存儲款項機構:待正式簽約後另行公告之。 24.其他應敘明事項: (1)本次現金增資發行普通股9,000仟股乙案，業經金融監督管理委員會115年8月19日金 管證發字第1150352269號函申報生效在案。 (2)除權交易日：115/09/22（最後含權買進日115/09/21） (3)本公司國內第六次無擔保轉換公司債停止受理轉換登記起訖日期115/09/03至 115/09/28日止。債券持有人如擬申請轉換，最遲應於停止受理轉換登記之始日 （115/09/03）之前一營業日前（115/09/01），向往來證券商辦理轉換手續。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260911 | 8042 | 金山電 | 6 | 1 | 5 | 8 | 17 | repeated_but_no_breakout | 近 10 日上榜 8 次、近 20 日上榜 17 次，但尚未有效突破，需等待攻擊確認。 |

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
