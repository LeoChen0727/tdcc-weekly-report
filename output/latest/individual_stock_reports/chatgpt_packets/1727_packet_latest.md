# INDIVIDUAL STOCK CHATGPT PACKET - 1727 中華化

## Metadata
- generated_at: 2026-09-26 15:51:01 Asia/Taipei
- stock_id: 1727
- stock_name: 中華化
- packet_status: standard_180d_window_packet
- latest_price_date: 20260924
- price_rows: 362
- current_main_price_date: 20260924
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260924-db6f7ba61c9bf627
- official_tdcc_signal_date: 20260924
- latest_tdcc_date: 20260924
- tdcc_rows: 22
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/1727_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/1727_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/1727_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/1727_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/1727.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/1727.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/1727.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/1727.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/1727_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/1727_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/1727_latest.md?ref=main

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
- action_rating_display_zh: 等待回檔
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。
- entry_strategy_zh: 目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。 進場策略：目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: wait_pullback
- action_rating_label_zh: 等待回檔
- confidence_level: medium
- thesis_state: high_level_distribution_risk
- entry_style: pullback_to_support
- position_sizing: observe_only

### management_plan
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260924
- open: 114
- high: 125
- low: 109
- close: 115.5
- volume: 47932996
- ma5: 109.4
- ema23_primary: 97.86
- distance_to_ema23_pct: 18.03
- ma20: 97.5
- ma60: 87.64
- ma120: 84.38
- return_5d: 10
- return_20d: 19.2
- volume_ratio: 5.43
- distance_to_ma20_pct_auxiliary: 18.46
- distance_to_high_60_pct: -7.6

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260828,97.1,100.5,95.3,98.1,7805835,86.13,13.9,83.25,85.63,1.56
20260831,98.1,106,97.3,99.9,10204032,87.28,14.46,84.71,85.78,1.88
20260901,100,101,94.5,95.3,7631288,87.95,8.36,85.86,85.81,1.33
20260902,94.9,96.5,93.4,94.2,3187873,88.47,6.48,86.87,85.84,0.55
20260903,94.1,95.1,89.1,89.2,3460712,88.53,0.76,87.58,85.78,0.59
20260904,90,95.2,88.2,94.7,5890316,89.04,6.35,88.7,85.9,0.96
20260907,94.7,95.4,90.8,91,4256734,89.21,2.01,89.43,85.99,0.68
20260908,91.5,92.3,90.5,90.6,1525491,89.32,1.43,90.13,86.08,0.25
20260909,90.5,92.7,90.2,91.1,1513988,89.47,1.82,90.72,86.17,0.25
20260910,90,92.4,89.9,90.4,1132611,89.55,0.95,91.42,86.25,0.19
20260911,89.1,92.3,89,89.6,1398176,89.55,0.05,92.14,86.18,0.23
20260914,89,89.7,86.2,88.2,1593169,89.44,-1.39,92.42,86.08,0.27
20260915,88,92.8,87.6,90.1,2685038,89.49,0.68,92.47,85.89,0.51
20260916,91.5,98.7,90.9,95.6,8782788,90,6.22,92.62,85.87,1.82
20260917,98.7,105,97.7,105,15353455,91.25,15.06,93.29,86.04,2.93
20260918,105,109.5,102,106,16587496,92.48,14.62,94.08,86.25,2.87
20260921,107,109.5,100.5,103,7483460,93.36,10.33,94.73,86.5,1.25
20260922,103,107,99.6,106,6851763,94.41,12.27,95.47,86.8,1.12
20260923,105,116.5,103,116.5,21402346,96.25,21.04,96.57,87.24,3.13
20260924,114,125,109,115.5,47932996,97.86,18.03,97.5,87.64,5.43
```

## Latest TDCC Snapshot
- as_of_date: 20260924
- over_400_ratio: 68.87
- over_600_ratio: 65.51
- over_800_ratio: 64.97
- over_1000_ratio: 62.27
- over_400_change_1w: 3.99
- over_800_change_1w: 6.47
- over_1000_change_1w: 4.45
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260709,56.43,-0.9,53.48,0.31,52.03,-0.42,5,False,True
20260717,55.37,-1.06,51.16,-2.32,50.51,-1.52,0,False,False
20260724,54.51,-0.86,51.48,0.32,49.39,-1.12,1,False,True
20260731,54.48,-0.03,49.8,-1.68,49.8,0.41,2,False,True
20260807,54.44,-0.04,49.97,0.17,49.24,-0.56,3,False,True
20260814,54.13,-0.31,48.71,-1.26,48.71,-0.53,4,False,False
20260821,56.42,2.29,50.25,1.54,49.51,0.8,5,False,True
20260828,57.79,1.37,53.26,3.01,50.4,0.89,6,True,True
20260904,59.02,1.23,53.97,0.71,51.19,0.79,7,True,True
20260911,58.17,-0.85,51.65,-2.32,50.27,-0.92,0,False,False
20260918,64.88,6.71,58.5,6.85,57.82,7.55,1,True,True
20260924,68.87,3.99,64.97,6.47,62.27,4.45,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1727 | 中華化 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  | call_strong_inflow | stale_signal | 1.董事會決議或公司決定增資基準日期:115/09/23 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/09/17 4.董事會決議(追補)發行日期:115/08/12 5.發行總金額及股數:發行總金額視實際發行價格而定，普通股13,800,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:俟訂價後另行公告 10.員工認股股數:依公司法第267條規定保留10%，計1,380,000股由本公司員工認購。 11.原股東認購比率:增資發行新股80%，計11,040,000股由原股東按認股基準日   股東名簿記載之股東持股比例認購，每仟股的認購86.23682261股。 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥發行新股總額10%，   計1,380,000股辦理公開申購方式對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止過   戶日起5日內由股東自行向本公司股務代理機構辦理拼湊整股認購，其拼湊不足   一股之畸零股及原股東、員工與對外公開承銷放棄認購或認購不足及申報拼   湊之部分，授權董事長洽特定人按發行價格認購。 14.本次發行新股之權利義務:與原有發行之普通股相同。 15.本次增資資金用途:償還銀行貸款、購置機器設備及充實營運資金。 16.現金增資認股基準日:115/10/19 17.最後過戶日:115/10/14 18.停止過戶起始日期:115/10/15 19.停止過戶截止日期:115/10/19 20.股款繳納期間:115/10/21-115/11/21 21.與代收及專戶存儲價款行庫訂約日期:俟正式簽約後另行公告 22.委託代收存款機構:俟正式簽約後另行公告 23.委託存儲款項機構:俟正式簽約後另行公告 24.其他應敘明事項: (1)本公司辦理現金增資發行普通股13,800,000股乙案，    業經金融監督管理委員會於115年09月17日業經金融監督管理委員會    金管證發字第1150354913號函申報生效在案。 (2)以上增資相關事宜如經主管機關核定處理、修正或為因應法令修訂    及其他未盡事宜，須予變更時，擬請董事會授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=within_7d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1727 | 中華化 | 3 | 1 | 3 | 8 | 16 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260924 | 1727 | 中華化 | 31 | 0 | 27738680.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
