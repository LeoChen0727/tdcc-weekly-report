# INDIVIDUAL STOCK CHATGPT PACKET - 6834 天二科技

## Metadata
- generated_at: 2026-10-07 22:19:27 Asia/Taipei
- stock_id: 6834
- stock_name: 天二科技
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6834_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6834_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6834_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6834_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6834_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6834_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6834_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6834.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6834.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6834.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6834.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6834_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6834_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6834_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 區間內轉強 / 挑戰前高觀察 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_initial
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
- model_recommended
- price_structure_not_broken
- near_23ema_or_support
- revenue_not_deteriorating
- no_major_tdcc_warning
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
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20261002
- open: 118
- high: 131
- low: 118
- close: 131
- volume: 12078273
- ma5: 117.6
- ema23_primary: 107.67
- distance_to_ema23_pct: 21.67
- ma20: 106.33
- ma60: 100.02
- ma120: 85.16
- return_5d: 15.42
- return_20d: 42.08
- volume_ratio: 1.78
- distance_to_ma20_pct_auxiliary: 23.2
- distance_to_high_60_pct: -8.39

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260903,92.1,95,87,87.2,2575546,93.27,-6.51,94.88,100.27,0.66
20260904,90,94.4,89.1,94,4355140,93.33,0.72,95.19,100.67,1.07
20260907,95,99.5,94.2,97,5532933,93.63,3.59,95.2,101.01,1.35
20260908,100,105,97.8,98.7,7653879,94.06,4.94,94.84,101.26,1.94
20260909,99.2,107,98.5,101,6748749,94.64,6.73,94.54,101.42,1.76
20260910,99.9,110,96.4,105.5,7261240,95.54,10.42,94.44,101.78,1.96
20260911,102.5,114.5,100.5,108,15065804,96.58,11.83,94.79,102.04,3.55
20260914,104,104.5,98.1,98.2,7659329,96.71,1.54,94.7,101.99,1.69
20260915,98.2,102,97,97.1,5641078,96.75,0.37,94.8,101.75,1.2
20260916,98.8,100.5,97.5,100,2882279,97.02,3.07,94.89,101.56,0.63
20260917,100,107,100,101.5,6365386,97.39,4.22,95.3,101.21,1.34
20260918,104,110.5,100,110.5,6734855,98.48,12.2,96.33,100.96,1.35
20260921,113,119.5,109.5,115,12137974,99.86,15.16,97.59,100.86,2.2
20260922,120,121,110,111.5,6166638,100.83,10.58,98.66,100.9,1.07
20260923,113,116.5,110.5,113.5,5500627,101.89,11.4,99.83,100.81,0.93
20260924,112,117.5,112,116,5943310,103.06,12.55,101.05,100.62,0.98
20260929,114,116,111.5,112.5,2757804,103.85,8.33,101.96,100.33,0.46
20260930,114,115,109,109,2684385,104.28,4.53,102.92,99.95,0.45
20261001,110,119.5,110,119.5,9597928,105.55,13.22,104.39,99.81,1.5
20261002,118,131,118,131,12078273,107.67,21.67,106.33,100.02,1.78
```

## Latest TDCC Snapshot
- as_of_date: 20261002
- over_400_ratio: 61.99
- over_600_ratio: 56.86
- over_800_ratio: 51.55
- over_1000_ratio: 48.27
- over_400_change_1w: 1.06
- over_800_change_1w: 0.75
- over_1000_change_1w: -0.33
- tdcc_consecutive_up_weeks: 8
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260717,58.21,-3.28,47.01,-3.59,44.81,-0.53,0,False,False
20260724,57.95,-0.26,47.01,0,44.81,0,1,False,False
20260731,57.9,-0.05,49.23,2.22,46.06,1.25,2,False,True
20260807,56.84,-1.06,48.16,-1.07,45.96,-0.1,0,False,False
20260814,56.85,0.01,47.17,-0.99,44.97,-0.99,1,False,False
20260821,57.24,0.39,47.15,-0.02,44.95,-0.02,2,False,False
20260828,56.72,-0.52,47.15,0,44.95,0,3,False,False
20260904,56.3,-0.42,47.15,0,44.95,0,4,False,False
20260911,60.2,3.9,49.52,2.37,46.3,1.35,5,True,True
20260918,60.84,0.64,51.95,2.43,47.8,1.5,6,True,True
20260924,60.93,0.09,50.8,-1.15,48.6,0.8,7,False,True
20261002,61.99,1.06,51.55,0.75,48.27,-0.33,8,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6834 | 天二科技 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_breakout |  | call_strong_inflow | continued_overheated | 1.董事會決議或公司決定增資基準日期:115/09/15 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/09/10 4.董事會決議(追補)發行日期:115/07/30 5.發行總金額及股數: (1)發行總金額:新台幣100,000仟元 (2)發行股數:普通股10,000仟股 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元 9.發行價格:每股新台幣80元。 10.員工認股股數:依公司法第267條規定，保留增資發行股數之10%，計1,000仟 股由員工認購。 11.原股東認購比率:增資發行股數之80%，計8,000仟股由原股東按照認股基準日之 股東名簿記載之持股比例認購。 12.公開銷售方式及股數:依證券交易法第28條之1規定，提撥增資發行股數之10%， 計1,000仟股採公開申購方式對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，由股東於停止過 戶日起五日內，逕向本公司股務代理機構辦理併湊。原股東及員工放棄認購之股份或併 湊後不足一股之畸零股，授權董事長洽特定人按發行價格認購。 14.本次發行新股之權利義務:與原已發行普通股股份相同。 15.本次增資資金用途:償還銀行借款、充實營運資金。 16.現金增資認股基準日:115/10/10 17.最後過戶日:115/10/05 18.停止過戶起始日期:115/10/06 19.停止過戶截止日期:115/10/10 20.股款繳納期間: 原股東及員工股款繳納期間：115/10/14/~115/11/16 特定人繳納期間：115/11/17~115/11/19 21.與代收及專戶存儲價款行庫訂約日期:115/09/23。 22.委託代收存款機構: (1)原股東及員工：台新國際商業銀行雄科分行。 (2)公開承銷：台新國際商業銀行敦南分行。 23.委託存儲款項機構:台新國際商業銀行苓雅分行。 24.其他應敘明事項: (1)本次現金增資發行普通股10,000仟股，每股面額新臺幣10元整，業經 金融監督管理委員會115年09月10日金管證發字第1150354253號函申報生效。 (2)本次現金增資籌資計畫有關之發行金額、發行股數、發行價格、發行時程、 發行條件，以及計畫所需資金總額、資金運用計畫項目、資金來源、預計資金 運用進度、預計可能產生效益及其他相關事宜，如經主管機關指示、相關法令 修正，或因應金融市場狀況或基於營運評估或客觀環境有所變化而需修訂或修 正時，授權董事長全權處理。 (3)本次現金增資如有未盡事宜授權董事長全權處理之。；calendar event: ex_right on 20261002; status=confirmed; proximity=within_3d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6834 | 天二科技 | 6 | 2 | 5 | 9 | 18 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20261002 | 6834 | 天二科技 | 20 | 0 | 14827500.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
