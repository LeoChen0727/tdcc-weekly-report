# INDIVIDUAL STOCK CHATGPT PACKET - 6533 晶心科

## Metadata
- generated_at: 2026-10-07 22:19:13 Asia/Taipei
- stock_id: 6533
- stock_name: 晶心科
- packet_status: standard_180d_window_packet
- latest_price_date: 20261002
- price_rows: 366
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6533_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6533_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6533_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6533_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6533_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6533_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6533_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6533.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6533.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6533.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6533.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6533_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6533_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6533_latest.md?ref=main

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
- date: 20261002
- open: 366.5
- high: 366.5
- low: 350.5
- close: 352
- volume: 7574941
- ma5: 326.3
- ema23_primary: 278.02
- distance_to_ema23_pct: 26.61
- ma20: 269.05
- ma60: 246.37
- ma120: 233.05
- return_5d: 40.24
- return_20d: 33.59
- volume_ratio: 1.96
- distance_to_ma20_pct_auxiliary: 30.83
- distance_to_high_60_pct: -3.96

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,264,273.5,263.5,264,1829812,250.39,5.44,254.55,224.38,0.91
20260904,270,271,262,264,811244,251.52,4.96,254.95,225.45,0.44
20260907,255.5,262,255,257,1508129,251.98,1.99,255.3,226.46,0.94
20260908,256.5,261.5,252.5,256,1516453,252.31,1.46,255.6,227.38,1.05
20260909,257.5,258,253,253.5,563432,252.41,0.43,255.55,228.16,0.4
20260910,253.5,255,245,246,993166,251.88,-2.33,255.38,228.9,0.71
20260911,239,239.5,231,232.5,1125823,250.26,-7.1,254.68,229.42,0.81
20260914,230,240,230,232,1020624,248.74,-6.73,254.1,229.93,0.73
20260915,232,234,224,224.5,612997,246.72,-9.01,253.07,230.22,0.44
20260916,224.5,229,224.5,229,503592,245.25,-6.62,252.1,230.59,0.37
20260917,232,251.5,232,251.5,2132108,245.77,2.33,252.4,231.38,1.47
20260918,255,276,250,270.5,4601141,247.83,9.15,253.43,232.51,2.78
20260921,269,270.5,260,263.5,1937477,249.13,5.77,254.28,233.7,1.12
20260922,268.5,278.5,254.5,254.5,4446657,249.58,1.97,254.43,234.76,2.32
20260923,259,264,249.5,251,1894521,249.7,0.52,253.53,235.66,1.02
20260924,251,276,250,276,6688397,251.89,9.57,253.9,237.01,3.18
20260929,272.5,303.5,268,303.5,11054299,256.19,18.47,255.8,238.7,4.22
20260930,316,333.5,301,333.5,9824741,262.63,26.98,259.43,240.93,3.2
20261001,346,366.5,337,366.5,16660559,271.29,35.1,264.62,243.7,4.68
20261002,366.5,366.5,350.5,352,7574941,278.02,26.61,269.05,246.37,1.96
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 30.72
- over_600_ratio: 26.78
- over_800_ratio: 23.97
- over_1000_ratio: 20.21
- over_400_change_1w: 9.45
- over_800_change_1w: 6.54
- over_1000_change_1w: 4.66
- tdcc_consecutive_up_weeks: 2
- all_thresholds_up: True
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,22.76,0.82,18.23,-0.03,16.34,-0.03,1,False,False
20260724,21.9,-0.86,18.22,-0.01,16.33,-0.01,0,False,False
20260731,21.91,0.01,18.23,0.01,16.34,0.01,1,True,True
20260807,23.69,1.78,18.17,-0.06,16.28,-0.06,2,False,False
20260814,20.88,-2.81,18.01,-0.16,16.13,-0.15,0,False,False
20260821,20.76,-0.12,18.02,0.01,16.14,0.01,1,False,True
20260828,20.81,0.05,17.98,-0.04,16.1,-0.04,2,False,False
20260904,20.75,-0.06,17.99,0.01,16.11,0.01,3,False,True
20260911,19.93,-0.82,17.99,0,16.11,0,0,False,False
20260918,19.69,-0.24,17.75,-0.24,15.87,-0.24,0,False,False
20260924,21.27,1.58,17.43,-0.32,15.55,-0.32,1,False,False
20261002,30.72,9.45,23.97,6.54,20.21,4.66,2,True,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6533 | 晶心科 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 68.0 |  |  | neckline_challenge |  | no_signal | continued_overheated | 1.董事會決議或公司決定增資基準日期:115/08/10 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/08/10 4.董事會決議(追補)發行日期:115/05/11 5.發行總金額及股數: 發行總金額：發行總面額新台幣68,000,000元。 發行總股數：普通股6,800,000股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股新台幣195.00元。(補充公告) 10.員工認股股數: 依公司法第267條規定，保留發行新股總額10%計680,000股由本公司員工認購。 11.原股東認購比率: 80%，計5,440,000股，由原股東按照認股基準日股東名簿記載之持股比例認購， 每仟股可認購107.40181948股。 12.公開銷售方式及股數: 依證券交易法第28條之1規定，提撥發行新股總額10%計680,000股對外公開承銷。 13.畸零股及逾期未認購股份之處理方式: 原股東認購不足一股之畸零股得由股東自行在停止過戶日起五日內，逕向本公司 股務代理機構辦理拼湊成一整股認購，其拼湊不足一股之畸零股及原股東、員工 放棄認購或認購不足及逾期未辦理拼湊之部份，擬授權董事長洽特定人按發行價 格認購。 14.本次發行新股之權利義務:與原已發行之股份相同。 15.本次增資資金用途:充實營運資金。 16.現金增資認股基準日:115/09/13 17.最後過戶日:115/09/08 18.停止過戶起始日期:115/09/09 19.停止過戶截止日期:115/09/13 20.股款繳納期間: 原股東及員工股款繳納期間：115年9月17日至115年10月19日 特定人認股繳款日期：115年10月20日至115年10月27日 21.與代收及專戶存儲價款行庫訂約日期:115年8月31日(補充公告) 22.委託代收存款機構:永豐商業銀行股份有限公司新竹分行。(補充公告) 23.委託存儲款項機構:聯邦商業銀行股份有限公司竹北分行。(補充公告) 24.其他應敘明事項: (1)本公司辦理115年現金增資發行新股6,800,000股乙案，業經金管會115年    8月10日金管證發字第1150350140號函生效在案。 (2)最後過戶日:115年9月8日 (3)本次現金增資發行計劃所訂之內容及其他相關未盡事宜，如遇法令變更、    經主管機關修正、客觀環境改變或因應主客觀環境需要而須修正或調整時    ，包括向主管機關申請延期或撤銷，授權董事長得全權辦理修正或調整。；calendar event: monthly_revenue_expected_window on 20261001; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6533 | 晶心科 | 7 | 1 | 5 | 9 | 14 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6533 | 晶心科 | 2 | 0 | 906930.0 | 0.0 |  | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
