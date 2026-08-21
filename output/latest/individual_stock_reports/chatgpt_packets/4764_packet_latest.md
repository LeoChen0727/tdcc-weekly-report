# INDIVIDUAL STOCK CHATGPT PACKET - 4764 雙鍵

## Metadata
- generated_at: 2026-08-21 22:27:37 Asia/Taipei
- stock_id: 4764
- stock_name: 雙鍵
- packet_status: standard_180d_window_packet
- latest_price_date: 20260821
- price_rows: 335
- current_main_price_date: 20260821
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260814-4a7d44bd65038f59
- official_tdcc_signal_date: 20260814
- latest_tdcc_date: 20260814
- tdcc_rows: 16
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
- tdcc_continuity_status: complete
- tdcc_missing_official_dates: 
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4764_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4764_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4764_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4764_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4764_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4764_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4764_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4764.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4764.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4764.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4764.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4764_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4764_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4764_latest.md?ref=main

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
- date: 20260821
- open: 211
- high: 231.5
- low: 209.5
- close: 219
- volume: 1863227
- ma5: 212.8
- ema23_primary: 245.92
- distance_to_ema23_pct: -10.95
- ma20: 243.5
- ma60: 281.94
- ma120: 246.35
- return_5d: -5.6
- return_20d: -21.65
- volume_ratio: 0.87
- distance_to_ma20_pct_auxiliary: -10.06
- distance_to_high_60_pct: -41.44

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260727,281.5,301,272,294.5,2377960,302.43,-2.62,305.07,305.88,0.86
20260728,277.5,303,274,281,4334521,300.65,-6.53,305,306.27,1.47
20260729,281,284,253,253,3134989,296.67,-14.72,302.6,305.76,1.02
20260730,228,268,228,236.5,4351338,291.66,-18.91,299.38,304.52,1.33
20260731,260,260,253.5,260,959680,289.02,-10.04,297.2,303.15,0.29
20260803,261.5,278,259,263,2170121,286.85,-8.32,295.35,302.03,0.64
20260804,261,270,256,259,1719062,284.53,-8.97,292.9,300.68,0.49
20260805,268,283,260,261,1650483,282.57,-7.63,291.1,299.68,0.47
20260806,260,268,255,262.5,1854780,280.9,-6.55,288.43,298.65,0.56
20260807,259,261,236.5,236.5,2559361,277.2,-14.68,283.45,297.34,0.8
20260810,235.5,239,226,232,2484954,273.43,-15.15,279.93,296.04,0.78
20260811,234,243.5,224,240.5,1523858,270.69,-11.15,275.38,295.19,0.51
20260812,240.5,258,240.5,249.5,1850927,268.92,-7.22,269.62,294.35,0.67
20260813,252.5,256.5,243.5,245,1353817,266.93,-8.22,265.45,293.36,0.55
20260814,241,250,223,232,3332685,264.02,-12.13,262.25,291.73,1.32
20260817,234.5,238,224.5,225,951871,260.77,-13.72,260.18,290.14,0.4
20260818,227,227.5,203,206,1896012,256.2,-19.59,255.82,288.24,0.8
20260819,202,210,200.5,203,892302,251.77,-19.37,251.45,285.76,0.39
20260820,200,211,196.5,211,1454582,248.37,-15.05,246.53,283.64,0.66
20260821,211,231.5,209.5,219,1863227,245.92,-10.95,243.5,281.94,0.87
```

## Latest TDCC Snapshot
- as_of_date: 20260814
- over_400_ratio: 74.71
- over_600_ratio: 71.45
- over_800_ratio: 68.11
- over_1000_ratio: 67.01
- over_400_change_1w: -0.68
- over_800_change_1w: -0.3
- over_1000_change_1w: -0.3
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260529,75.24,-2.11,71.55,-2.02,67.56,-0.69,0,False,False
20260605,74.17,-1.07,67.74,-3.81,66.64,-0.92,0,False,False
20260612,74.35,0.18,67.13,-0.61,63.86,-2.78,1,False,False
20260618,74.91,0.56,68.27,1.14,64.99,1.13,2,True,True
20260626,75.48,0.57,68.79,0.52,65.74,0.75,3,True,True
20260703,75.98,0.5,68.84,0.05,65.7,-0.04,4,False,True
20260709,75.99,0.01,68.14,-0.7,63.96,-1.74,5,False,False
20260717,76.92,0.93,69.73,1.59,66.43,2.47,6,True,True
20260724,77.13,0.21,68.69,-1.04,66.6,0.17,7,False,True
20260731,76.01,-1.12,70.02,1.33,68.92,2.32,8,False,True
20260807,75.39,-0.62,68.41,-1.61,67.31,-1.61,0,False,False
20260814,74.71,-0.68,68.11,-0.3,67.01,-0.3,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4764 | 雙鍵 | pattern | 型態觀察 | 35.0 |  |  | pullback_entry_zone |  | call_inflow | stale_signal | 1.董事會決議或公司決定增資基準日期:115/07/09 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/07/08 4.董事會決議(追補)發行日期:115/06/05 5.發行總金額及股數:新台幣60,000,000元，普通股6,000,000股。 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元。 9.發行價格:每股新台幣230元。(補充公告) 10.員工認股股數:發行新股總數之15%，計900,000股。 11.原股東認購比率:發行新股總數之75%，計4,500,000股，由原股東按認股基準日 股東名冊所記載之股東之持股比例認購。 12.公開銷售方式及股數:發行新股總數之10%，計600,000股，對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，由股東自停止過 戶起五日內自行向本公司股務代理機構辦理拼湊成整股認購，原股東及員工放棄認購或 拼湊後仍不足一股之畸零股部份，授權董事長洽特定人認購之。 14.本次發行新股之權利義務:與原已發行普通股股份相同。 15.本次增資資金用途:償還銀行借款及充實營運資金。 16.現金增資認股基準日:115/08/01 17.最後過戶日:115/07/27 18.停止過戶起始日期:115/07/28 19.停止過戶截止日期:115/08/01 20.股款繳納期間: (1)原股東及員工股款繳納期間:115/08/06~115/08/12。 (2)特定人繳納期間:115/08/13~115/08/17。 21.與代收及專戶存儲價款行庫訂約日期:115/07/09 22.委託代收存款機構:元大商業銀行股份有限公司營業部及全國各分行。 23.委託存儲款項機構:元大商業銀行股份有限公司中山北路分行。 24.其他應敘明事項: (1)本公司115年度現金增資發行新股，經金融監督管理委員會115年07月08日金 管證發字第1150348105號函申報生效在案。 (2)本次現金增資之發行價格、發行條件、發行時程，以及本計畫所需資金總額、資金 來源、計畫項目、資金運用進度、預計可能產生效益及其他相關事宜，如遇法令變更、 經主管機關修正、或因應主客觀環境因素而須修正或調整時，授權董事長全權處理之。；calendar event: monthly_revenue_expected_window on 20260901; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4764 | 雙鍵 | 1 | 1 | 2 | 7 | 9 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260821 | 4764 | 雙鍵 | 22 | 0 | 1648940.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
