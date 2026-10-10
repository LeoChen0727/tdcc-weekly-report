# INDIVIDUAL STOCK CHATGPT PACKET - 8042 金山電

## Metadata
- generated_at: 2026-10-10 22:18:53 Asia/Taipei
- stock_id: 8042
- stock_name: 金山電
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 266
- current_main_price_date: 20261002
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20261002-d841316b0644c08f
- official_tdcc_signal_date: 20261002
- latest_tdcc_date: 20261002
- tdcc_rows: 23
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
- date: 20261002
- open: 117.5
- high: 124
- low: 116
- close: 121
- volume: 10938000
- ma5: 115.2
- ema23_primary: 113.15
- distance_to_ema23_pct: 6.94
- ma20: 113.12
- ma60: 115.64
- ma120: 121.5
- return_5d: 8.52
- return_20d: 9.01
- volume_ratio: 1.89
- distance_to_ma20_pct_auxiliary: 6.96
- distance_to_high_60_pct: -32.02

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,113,113.5,100,100.5,6165000,109.34,-8.08,107.28,138.14,1.18
20260904,104,110.5,104,110.5,8888000,109.43,0.98,106.97,137.63,1.62
20260907,113.5,121.5,111.5,121.5,11464000,110.44,10.02,107.35,137.07,2.01
20260908,121.5,121.5,112,113,10740000,110.65,2.12,107.17,136.12,1.96
20260909,115,117,112,112.5,4856000,110.81,1.53,107.15,134.87,0.9
20260910,111.5,123.5,107.5,120.5,9919000,111.61,7.96,107.35,133.66,1.8
20260911,116,121.5,112.5,113,11068000,111.73,1.14,107.38,132.29,1.88
20260914,110,114.5,108.5,111,3235000,111.67,-0.6,107.5,130.89,0.55
20260915,111,116,110,110,4211000,111.53,-1.37,107.92,129.55,0.7
20260916,111.5,114,110.5,114,1976000,111.74,2.03,108.05,128.49,0.34
20260917,115.5,118,110.5,110.5,3433000,111.63,-1.01,108.53,127.13,0.61
20260918,114,114,110.5,113,1579000,111.75,1.12,109.19,125.67,0.29
20260921,113,117,112.5,113.5,3749000,111.89,1.44,109.92,124.56,0.66
20260922,116.5,117,111.5,111.5,2682000,111.86,-0.32,110.55,123.6,0.47
20260923,112.5,115.5,111.5,111.5,1755000,111.83,-0.29,111.17,122.36,0.31
20260924,110,117,110,114,3557000,112.01,1.78,111.65,120.9,0.63
20260929,113,113,110.5,111.5,2141000,111.97,-0.42,111.78,119.31,0.4
20260930,113,114,111,111.5,1324000,111.93,-0.38,112.1,117.67,0.26
20261001,112,122,112,118,11827000,112.44,4.95,112.62,116.47,2.17
20261002,117.5,124,116,121,10938000,113.15,6.94,113.12,115.64,1.89
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 64.32
- over_600_ratio: 60.62
- over_800_ratio: 58.07
- over_1000_ratio: 57.38
- over_400_change_1w: 0.42
- over_800_change_1w: -0.58
- over_1000_change_1w: 0.16
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,67.15,-0.92,59.52,-2.67,57.65,-1.83,0,False,False
20260724,66.69,-0.46,60.55,1.03,58.47,0.82,1,False,True
20260731,66.34,-0.35,59.82,-0.73,59.15,0.68,2,False,True
20260807,66.17,-0.17,59.58,-0.24,58.18,-0.97,0,False,False
20260814,64.43,-1.74,59.54,-0.04,58.94,0.76,1,False,True
20260821,64.13,-0.3,58.82,-0.72,58.16,-0.78,0,False,False
20260828,65.01,0.88,58.82,0,58.16,0,1,False,False
20260904,63.63,-1.38,58.92,0.1,58.2,0.04,2,False,True
20260911,66.83,3.2,60.28,1.36,59.59,1.39,3,True,True
20260918,64.08,-2.75,58.61,-1.67,57.24,-2.35,0,False,False
20260924,63.9,-0.18,58.65,0.04,57.22,-0.02,1,False,True
20261002,64.32,0.42,58.07,-0.58,57.38,0.16,2,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 8042 | 金山電 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | 1.董事會決議或公司決定增資基準日期:115/08/27 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/08/19 4.董事會決議(追補)發行日期:115/07/31 5.發行總金額及股數:新臺幣90,000仟元、普通股9,000仟股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新臺幣10元 9.發行價格:每股新台幣98元 10.員工認股股數:依公司法第267條規定，保留10%計900仟股由員工認購。 11.原股東認購比率:提撥本次發行股數之80%，計7,200仟股由原股東按認股基準日之股 東名簿所載持股比例認購。 12.公開銷售方式及股數:提撥發行新股總額10%，計900仟股辦理公開申購。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止過戶日 起五日內由股東向本公司股務代理機構辦理拼湊，原股東及員工放棄認購之股份或拼湊 不足一股之畸零股，授權董事長洽特定人按發行價格認購之。 14.本次發行新股之權利義務:與原已發行普通股股份相同 15.本次增資資金用途:償還銀行借款 16.現金增資認股基準日:115/09/28 17.最後過戶日:115/09/23 18.停止過戶起始日期:115/09/24 19.停止過戶截止日期:115/09/28 20.股款繳納期間: 原股東及員工繳款期間：115/10/06~115/11/06 特定人繳款期間：115/11/09~115/11/13 21.與代收及專戶存儲價款行庫訂約日期:115/09/15 22.委託代收存款機構:台北富邦商業銀行土城分行。 23.委託存儲款項機構:第一商業銀行頭前分行。 24.其他應敘明事項: (1)本次現金增資發行普通股9,000仟股乙案，業經金融監督管理委員會115年8月19日金 管證發字第1150352269號函申報生效在案。 (2)除權交易日：115/09/22（最後含權買進日115/09/21） (3)本公司國內第六次無擔保轉換公司債停止受理轉換登記起訖日期115/09/03至 115/09/28日止。債券持有人如擬申請轉換，最遲應於停止受理轉換登記之始日 （115/09/03）之前一營業日前（115/09/01），向往來證券商辦理轉換手續。 (4)本次現金增資之增資基準日為115年11月16日，並授權董事長視日後特定人繳款情 形，如有變更增資基準日之必要時，得調整訂定之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 8042 | 金山電 | 17 | 2 | 5 | 10 | 19 | repeated_but_no_breakout | 近 10 日上榜 10 次、近 20 日上榜 19 次，但尚未有效突破，需等待攻擊確認。 |

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
