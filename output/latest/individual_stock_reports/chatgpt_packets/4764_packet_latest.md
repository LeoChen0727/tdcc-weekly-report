# INDIVIDUAL STOCK CHATGPT PACKET - 4764 雙鍵

## Metadata
- generated_at: 2026-07-31 22:27:33 Asia/Taipei
- stock_id: 4764
- stock_name: 雙鍵
- packet_status: standard_180d_window_packet
- latest_price_date: 20260730
- price_rows: 312
- current_main_price_date: 20260730
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- source_tdcc_dataset_id: tdcc-20260724-88f3a903b384007d
- official_tdcc_signal_date: 20260724
- latest_tdcc_date: 20260724
- tdcc_rows: 13
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
- date: 20260730
- open: 228
- high: 268
- low: 228
- close: 236.5
- volume: 4351338
- ma5: 268.9
- ema23_primary: 291.66
- distance_to_ema23_pct: -18.91
- ma20: 299.38
- ma60: 304.52
- ma120: 230.05
- return_5d: -23.59
- return_20d: -21.43
- volume_ratio: 1.33
- distance_to_ma20_pct_auxiliary: -21
- distance_to_high_60_pct: -36.76

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260702,295,306,295,303.5,258452,299.28,1.41,294.62,277.32,0.13
20260703,303.5,307,298,300,285488,299.34,0.22,295.32,280.06,0.15
20260706,301,309.5,301,308,429243,300.06,2.65,296.62,282.7,0.24
20260707,309.5,323,295,297,922381,299.8,-0.94,297.95,285.07,0.52
20260708,293,326.5,267.5,316,5715593,301.15,4.93,300.18,287.49,2.9
20260709,320,347.5,310,336,4606560,304.06,10.51,304.07,289.97,2.16
20260713,320,340,302.5,302.5,2732785,303.93,-0.47,306.32,291.75,1.26
20260714,298.5,332.5,288.5,331.5,5611656,306.23,8.25,309.75,294.05,2.36
20260715,341.5,364.5,320.5,364.5,6732472,311.08,17.17,314.07,296.58,2.57
20260716,355,374,328.5,328.5,7009031,312.53,5.11,315.23,298.17,2.48
20260717,300,313,296,296,2330379,311.16,-4.87,314.23,299.02,0.85
20260720,283,287.5,266.5,266.5,3913225,307.43,-13.31,310.62,299.77,1.45
20260721,272.5,293,270.5,293,2201829,306.23,-4.32,308.68,301.33,0.83
20260722,319.5,322,290,290.5,2262302,304.92,-4.73,305.88,302.86,0.9
20260723,293.5,316.5,282.5,309.5,2871849,305.3,1.37,305.3,304.38,1.11
20260724,297.5,320.5,279.5,279.5,3492363,303.15,-7.8,304.12,305.09,1.3
20260727,281.5,301,272,294.5,2377960,302.43,-2.62,305.07,305.88,0.86
20260728,277.5,303,274,281,4334521,300.65,-6.53,305,306.27,1.47
20260729,281,284,253,253,3134989,296.67,-14.72,302.6,305.76,1.02
20260730,228,268,228,236.5,4351338,291.66,-18.91,299.38,304.52,1.33
```

## Latest TDCC Snapshot
- as_of_date: 20260724
- over_400_ratio: 77.13
- over_600_ratio: 72.93
- over_800_ratio: 68.69
- over_1000_ratio: 66.6
- over_400_change_1w: 0.21
- over_800_change_1w: -1.04
- over_1000_change_1w: 0.17
- tdcc_consecutive_up_weeks: 7
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260508,79.18,0.48,74.02,0.4,71.01,0.42,1,True,True
20260515,78.88,-0.3,74.03,0.01,70.95,-0.06,2,False,True
20260522,77.35,-1.53,73.57,-0.46,68.25,-2.7,3,False,False
20260529,75.24,-2.11,71.55,-2.02,67.56,-0.69,0,False,False
20260605,74.17,-1.07,67.74,-3.81,66.64,-0.92,0,False,False
20260612,74.35,0.18,67.13,-0.61,63.86,-2.78,1,False,False
20260618,74.91,0.56,68.27,1.14,64.99,1.13,2,True,True
20260626,75.48,0.57,68.79,0.52,65.74,0.75,3,True,True
20260703,75.98,0.5,68.84,0.05,65.7,-0.04,4,False,True
20260709,75.99,0.01,68.14,-0.7,63.96,-1.74,5,False,False
20260717,76.92,0.93,69.73,1.59,66.43,2.47,6,True,True
20260724,77.13,0.21,68.69,-1.04,66.6,0.17,7,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 4764 | 雙鍵 | revenue_pullback | 營收成長股價回檔 | 55.0 |  |  |  |  | call_inflow | stale_signal | 1.董事會決議或公司決定增資基準日期:115/07/09 2.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 3.主管機關申報生效日期:115/07/08 4.董事會決議(追補)發行日期:115/06/05 5.發行總金額及股數:新台幣60,000,000元，普通股6,000,000股。 6.採總括申報發行新股案件，本次發行金額及股數:不適用 7.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 8.每股面額:新台幣10元。 9.發行價格:每股新台幣230元。(補充公告) 10.員工認股股數:發行新股總數之15%，計900,000股。 11.原股東認購比率:發行新股總數之75%，計4,500,000股，由原股東按認股基準日 股東名冊所記載之股東之持股比例認購。 12.公開銷售方式及股數:發行新股總數之10%，計600,000股，對外公開承銷。 13.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，由股東自停止過 戶起五日內自行向本公司股務代理機構辦理拼湊成整股認購，原股東及員工放棄認購或 拼湊後仍不足一股之畸零股部份，授權董事長洽特定人認購之。 14.本次發行新股之權利義務:與原已發行普通股股份相同。 15.本次增資資金用途:償還銀行借款及充實營運資金。 16.現金增資認股基準日:115/08/01 17.最後過戶日:115/07/27 18.停止過戶起始日期:115/07/28 19.停止過戶截止日期:115/08/01 20.股款繳納期間: (1)原股東及員工股款繳納期間:115/08/06~115/08/12。 (2)特定人繳納期間:115/08/13~115/08/17。 21.與代收及專戶存儲價款行庫訂約日期:115/07/09 22.委託代收存款機構:元大商業銀行股份有限公司營業部及全國各分行。 23.委託存儲款項機構:元大商業銀行股份有限公司中山北路分行。 24.其他應敘明事項: (1)本公司115年度現金增資發行新股，經金融監督管理委員會115年07月08日金 管證發字第1150348105號函申報生效在案。 (2)本次現金增資之發行價格、發行條件、發行時程，以及本計畫所需資金總額、資金 來源、計畫項目、資金運用進度、預計可能產生效益及其他相關事宜，如遇法令變更、 經主管機關修正、或因應主客觀環境因素而須修正或調整時，授權董事長全權處理之。；calendar event: ex_right on 20260724; status=confirmed; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 4764 | 雙鍵 | 7 | 2 | 5 | 7 | 11 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 4764 | 雙鍵 | 23 | 0 | 2080250.0 | 0.0 |  | call_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
