# INDIVIDUAL STOCK CHATGPT PACKET - 4541 晟田

## Metadata
- generated_at: 2026-09-05 15:53:37 Asia/Taipei
- stock_id: 4541
- stock_name: 晟田
- packet_status: standard_180d_window_packet
- latest_price_date: 20260904
- price_rows: 213
- current_main_price_date: 20260904
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260904-ef2f08472cf64a89
- official_tdcc_signal_date: 20260904
- latest_tdcc_date: 20260904
- tdcc_rows: 19
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4541_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4541_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4541_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4541_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4541.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4541.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4541.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4541.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4541_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4541_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4541_latest.md?ref=main

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
- date: 20260904
- open: 63.2
- high: 63.7
- low: 60.4
- close: 61.2
- volume: 1798000
- ma5: 64.38
- ema23_primary: 65.91
- distance_to_ema23_pct: -7.15
- ma20: 67.58
- ma60: 62.46
- ma120: 53.77
- return_5d: -6.56
- return_20d: -7.13
- volume_ratio: 0.43
- distance_to_ma20_pct_auxiliary: -9.45
- distance_to_high_60_pct: -25

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260810,65,66.2,64.1,65.4,1767000,63.45,3.07,66.73,55.35,0.15
20260811,66,67.3,64.4,66.3,5262000,63.69,4.1,66.52,55.72,0.52
20260812,66.5,71.5,65.1,70.3,6375000,64.24,9.43,66.39,56.16,0.67
20260813,70.6,73.7,70.3,72.6,5102000,64.94,11.8,66.45,56.65,0.57
20260814,72.7,76,69.4,73.9,17541000,65.68,12.51,66.52,57.16,1.97
20260817,73.8,75.5,69.8,72.7,8115000,66.27,9.71,66.7,57.63,1.03
20260818,72.3,75.4,70.4,70.5,6297000,66.62,5.82,66.44,58.07,0.82
20260819,69.8,72.2,67.5,67.6,3794000,66.7,1.35,66.3,58.46,0.57
20260820,67.6,71.9,67.2,67.6,5547000,66.78,1.23,66.23,58.86,0.86
20260821,67.8,69.4,66,68.8,2222000,66.95,2.77,66.11,59.27,0.4
20260824,68.5,69.7,67,67.1,1652000,66.96,0.21,66.12,59.64,0.3
20260825,66.4,67.6,64.6,66.5,1861000,66.92,-0.63,66.3,60,0.38
20260826,66.9,68.7,66.9,67.5,2130000,66.97,0.79,66.61,60.34,0.45
20260827,68,71.7,67.3,67.5,5470000,67.01,0.73,67.16,60.7,1.15
20260828,70,71.1,65,65.5,3876000,66.89,-2.07,67.44,61.01,0.83
20260831,65.5,68.4,64.5,66.6,1953000,66.86,-0.39,67.74,61.33,0.42
20260901,66.7,67.4,66.3,66.5,1087000,66.83,-0.5,67.92,61.65,0.24
20260902,66.2,66.9,64.8,64.8,1391000,66.66,-2.79,67.86,61.96,0.32
20260903,65.6,66.6,62.8,62.8,1350000,66.34,-5.34,67.82,62.22,0.32
20260904,63.2,63.7,60.4,61.2,1798000,65.91,-7.15,67.58,62.46,0.43
```

## Latest TDCC Snapshot
- as_of_date: 20260904
- over_400_ratio: 40.19
- over_600_ratio: 34.23
- over_800_ratio: 30.25
- over_1000_ratio: 27.63
- over_400_change_1w: -1.85
- over_800_change_1w: -2.73
- over_1000_change_1w: -2.77
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260618,38.48,2.65,30.12,1.01,28.65,3.38,4,True,True
20260626,39.19,0.71,32.59,2.47,31.19,2.54,5,True,True
20260703,40.36,1.17,34.48,1.89,30.35,-0.84,6,False,True
20260709,40.34,-0.02,34.47,-0.01,31.68,1.33,7,False,True
20260717,39.62,-0.72,31.03,-3.44,25.56,-6.12,0,False,False
20260724,41.21,1.59,31.98,0.95,26.86,1.3,1,True,True
20260731,41.32,0.11,37.25,5.27,29.64,2.78,2,True,True
20260807,42.23,0.91,32.71,-4.54,30.04,0.4,3,False,True
20260814,47.01,4.78,37.05,4.34,33.06,3.02,4,True,True
20260821,41.94,-5.07,32.24,-4.81,28.36,-4.7,0,False,False
20260828,42.04,0.1,32.98,0.74,30.4,2.04,1,True,True
20260904,40.19,-1.85,30.25,-2.73,27.63,-2.77,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4541 | 晟田 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  |  | stale_signal | 1.董事會決議或公司決定增資基準日期:115/08/26 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/08/25 4.董事會決議(追補)發行日期:115/06/11 5.發行總金額及股數:發行總股數:5,000,000股，發行總金額:50,000,000元 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股發行價格新臺幣50元(補充公告)。 10.員工認股股數:依公司法第267條規定保留增資發行新股之10%，計 500,000股由本公司員工承購。 11.原股東認購比率:現金增資發行新股之80%，計4,000,000股，由原股東按 認股基準日股東名冊所記載之股東之持股比例認購。 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥增資發行新股之 10%，計500,000股採公開申購方式對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股得由股 東在停止過戶日起五日內，逕向本公司股務代理機構辦理併湊，其併湊不 足一股之畸零股及原股東與員工認購不足及逾期未申報併湊之部分，擬授 權董事長洽特定人認購之。 14.本次發行新股之權利義務:本次現金增資發行新股其權利義務與原有發行之 普通股相同。 15.本次增資資金用途:興建廠房、購置機器設備及充實營運資金。 16.現金增資認股基準日:115/09/18 17.最後過戶日:115/09/11 18.停止過戶起始日期:115/09/14 19.停止過戶截止日期:115/09/18 20.股款繳納期間: (1)原股東及員工繳款期間：115/09/22~115/09/30 (2)特定人繳款期間：115/10/01~115/10/05 21.與代收及專戶存儲價款行庫訂約日期:115/09/03(補充公告) 22.委託代收存款機構:凱基商業銀行高雄分行(補充公告) 23.委託存儲款項機構:臺灣銀行高科分行(補充公告) 24.其他應敘明事項: (1)本公司辦理115年現金增資發行普通股5,000仟股乙案，業經金融監督    管理委員會115年8月25日金管證發字1150352698號函申報生效在案。 (2)以上增資相關事宜如經主管機關核定處理、修正或為因應法令修訂及其    他未盡事宜，須予變更時，董事會授權董事長全權辦理修正或調整。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=recent；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260904 | 4541 | 晟田 | 27 | 13 | 5 | 10 | 20 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
