# INDIVIDUAL STOCK CHATGPT PACKET - 3372 典範

## Metadata
- generated_at: 2026-09-19 22:16:30 Asia/Taipei
- stock_id: 3372
- stock_name: 典範
- packet_status: standard_180d_window_packet
- latest_price_date: 20260918
- price_rows: 258
- current_main_price_date: 20260918
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260918-b805c742e5cccca5
- official_tdcc_signal_date: 20260918
- latest_tdcc_date: 20260918
- tdcc_rows: 21
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3372_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3372_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3372_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3372_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3372.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3372.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3372.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3372.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3372_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3372_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3372_latest.md?ref=main

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
- date: 20260918
- open: 16.6
- high: 16.75
- low: 16.05
- close: 16.4
- volume: 2204000
- ma5: 15.3
- ema23_primary: 15.16
- distance_to_ema23_pct: 8.16
- ma20: 14.9
- ma60: 16.39
- ma120: 18.25
- return_5d: 14.69
- return_20d: 8.61
- volume_ratio: 4.26
- distance_to_ma20_pct_auxiliary: 10.05
- distance_to_high_60_pct: -27.27

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260824,15.1,15.35,14.95,14.95,275000,15.91,-6.03,15.43,18.36,0.58
20260825,14.85,15,14.6,15,178000,15.83,-5.27,15.39,18.24,0.39
20260826,15,15.1,14.8,14.95,216000,15.76,-5.14,15.39,18.13,0.52
20260827,15.2,15.25,14.9,15.1,307000,15.71,-3.86,15.45,18.01,0.79
20260828,15.1,15.6,15.1,15.35,364000,15.68,-2.08,15.46,17.9,0.97
20260831,15.2,15.2,14.8,14.95,326000,15.62,-4.26,15.44,17.77,0.88
20260901,14.95,15.1,14.9,14.95,311000,15.56,-3.92,15.41,17.66,0.87
20260902,14.9,14.95,14.8,14.95,261000,15.51,-3.6,15.37,17.58,0.77
20260903,15.05,15.25,14.6,14.6,419000,15.43,-5.4,15.31,17.49,1.21
20260904,14.65,14.8,14.4,14.7,296000,15.37,-4.37,15.27,17.41,0.88
20260907,14.7,14.7,14.5,14.5,375000,15.3,-5.23,15.17,17.32,1.15
20260908,14.55,14.55,14.3,14.35,400000,15.22,-5.72,15.08,17.23,1.24
20260909,14.55,14.55,14.3,14.5,203000,15.16,-4.36,15,17.14,0.65
20260910,14.5,14.5,14.3,14.4,254000,15.1,-4.62,14.91,17.04,0.82
20260911,14.4,14.4,14.15,14.3,250000,15.03,-4.86,14.84,16.95,0.85
20260914,14.3,14.8,14.1,14.55,315000,14.99,-2.94,14.8,16.85,1.1
20260915,14.55,14.55,14.15,14.2,302000,14.92,-4.86,14.76,16.73,1.06
20260916,14.2,15.45,14.2,14.95,537000,14.93,0.16,14.76,16.59,1.79
20260917,15,16.4,14.7,16.4,2554000,15.05,8.97,14.84,16.48,6.11
20260918,16.6,16.75,16.05,16.4,2204000,15.16,8.16,14.9,16.39,4.26
```

## Latest TDCC Snapshot
- as_of_date: 20260918
- over_400_ratio: 54
- over_600_ratio: 52.59
- over_800_ratio: 51.4
- over_1000_ratio: 50.98
- over_400_change_1w: 0.4
- over_800_change_1w: 0.19
- over_1000_change_1w: 0.19
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260703,48.39,-0.69,45.81,-0.72,44.37,-0.65,0,False,False
20260709,47.71,-0.68,45.37,-0.44,44.34,-0.03,0,False,False
20260717,46.61,-1.1,44.12,-1.25,43.64,-0.7,0,False,False
20260724,54.37,7.76,51.63,7.51,50.82,7.18,1,True,True
20260731,54.55,0.18,51.99,0.36,50.82,0,2,False,True
20260807,54.48,-0.07,51.59,-0.4,50.82,0,0,False,False
20260814,54.3,-0.18,51.24,-0.35,50.82,0,0,False,False
20260821,54.02,-0.28,51.21,-0.03,50.79,-0.03,0,False,False
20260828,53.63,-0.39,51.21,0,50.79,0,0,False,False
20260904,53.58,-0.05,51.21,0,50.79,0,0,False,False
20260911,53.6,0.02,51.21,0,50.79,0,1,False,False
20260918,54,0.4,51.4,0.19,50.98,0.19,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3372 | 典範 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  |  | continued_2_3d | 1.董事會決議或公司決定增資基準日期:115/06/12 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/06/10 4.董事會決議(追補)發行日期:115/03/03 5.發行總金額及股數:總金額600,000,000元；60,000,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股新台幣16.8元 10.員工認股股數:依公司法第267條規定，保留增資發行股數之10%， 計6,000,000股由本公司員工承購。 11.原股東認購比率:80%計48,000,000股 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥發行新股總額10% 計6,000,000股對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股得由股東在 停止過戶日起五日內，逕向本公司股務代理機構辦理拼湊，其拼湊不足一股之 畸零股及原股東及員工放棄認購或認購不足及逾期未申報拼湊之部分， 擬授權董事長洽特定人按發行價格認購之。對外公開承銷認購不足部分， 擬依「中華民國證券商業同業公會證券商承銷或再行銷售有價證券處理辦法」 規定辦理。 14.本次發行新股之權利義務:與已發行之原有股份相同。 15.本次增資資金用途:支應資本支出、充實營運資金。 16.現金增資認股基準日:115/07/06 17.最後過戶日:115/07/01 18.停止過戶起始日期:115/07/02 19.停止過戶截止日期:115/07/06 20.股款繳納期間: (1)原股東及員工繳款期間:115/07/09~115/07/15 (2)特定人繳款期間:115/07/16~115/07/20 21.與代收及專戶存儲價款行庫訂約日期:民國115年06月23日 22.委託代收存款機構:臺灣銀行股份有限公司高雄加工出口區分行及全台分行 23.委託存儲款項機構:元大銀行高雄分行 24.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260918 | 3372 | 典範 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | continued_2_3d | 1.董事會決議或公司決定增資基準日期:115/06/12 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/06/10 4.董事會決議(追補)發行日期:115/03/03 5.發行總金額及股數:總金額600,000,000元；60,000,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股新台幣16.8元 10.員工認股股數:依公司法第267條規定，保留增資發行股數之10%， 計6,000,000股由本公司員工承購。 11.原股東認購比率:80%計48,000,000股 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥發行新股總額10% 計6,000,000股對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股得由股東在 停止過戶日起五日內，逕向本公司股務代理機構辦理拼湊，其拼湊不足一股之 畸零股及原股東及員工放棄認購或認購不足及逾期未申報拼湊之部分， 擬授權董事長洽特定人按發行價格認購之。對外公開承銷認購不足部分， 擬依「中華民國證券商業同業公會證券商承銷或再行銷售有價證券處理辦法」 規定辦理。 14.本次發行新股之權利義務:與已發行之原有股份相同。 15.本次增資資金用途:支應資本支出、充實營運資金。 16.現金增資認股基準日:115/07/06 17.最後過戶日:115/07/01 18.停止過戶起始日期:115/07/02 19.停止過戶截止日期:115/07/06 20.股款繳納期間: (1)原股東及員工繳款期間:115/07/09~115/07/15 (2)特定人繳款期間:115/07/16~115/07/20 21.與代收及專戶存儲價款行庫訂約日期:民國115年06月23日 22.委託代收存款機構:臺灣銀行股份有限公司高雄加工出口區分行及全台分行 23.委託存儲款項機構:元大銀行高雄分行 24.其他應敘明事項:無；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260918 | 3372 | 典範 | 2 | 2 | 2 | 2 | 2 | continued_2_3d | 連續 2 日上榜，訊號延續，但仍需量價與籌碼確認。 |

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
