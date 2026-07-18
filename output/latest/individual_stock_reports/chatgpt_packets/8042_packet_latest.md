# INDIVIDUAL STOCK CHATGPT PACKET - 8042 金山電

## Metadata
- generated_at: 2026-07-18 20:55:24 Asia/Taipei
- stock_id: 8042
- stock_name: 金山電
- packet_status: standard_180d_window_packet
- latest_price_date: 20260717
- price_rows: 171
- current_main_price_date: 20260717
- current_main_price_universe_status: current
- current_main_price_universe_source: official_daily_price_latest_main_price_date
- listing_status_source_status: formal_listing_status_source_unavailable
- official_tdcc_signal_date: 20260717
- latest_tdcc_date: 20260717
- tdcc_rows: 11
- tdcc_history_status: tdcc_history_ready
- tdcc_freshness_status: tdcc_window_fresh
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
- Only claim tdcc_history_ready when tdcc_rows >= 8 and latest_tdcc_date equals official_tdcc_signal_date.
- If latest_tdcc_date differs from official_tdcc_signal_date, mark tdcc_window_stale and do not claim current TDCC history.
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
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 營收成長股價回檔，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260717
- open: 130
- high: 135.5
- low: 129.5
- close: 129.5
- volume: 4091000
- ma5: 147.4
- ema23_primary: 165.27
- distance_to_ema23_pct: -21.64
- ma20: 177.35
- ma60: 137.75
- ma120: 98.33
- return_5d: -27.25
- return_20d: -33.76
- volume_ratio: 0.71
- distance_to_ma20_pct_auxiliary: -26.98
- distance_to_high_60_pct: -42.95

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260618,195,198,189.5,195,1802000,152.3,28.04,158.07,100.21,0.48
20260622,199.5,199.5,190,190.5,1294000,155.48,22.52,161.45,102.5,0.34
20260623,191,191,177,177.5,1414000,157.32,12.83,163.57,104.56,0.37
20260624,176,192,176,192,782000,160.21,19.84,165.82,106.89,0.2
20260625,195,200.5,192.5,200.5,1189000,163.57,22.58,168.32,109.36,0.3
20260626,195.5,195.5,180.5,180.5,1074000,164.98,9.41,169.78,111.41,0.27
20260629,180.5,186,169,169,811000,165.31,2.23,170.5,113.33,0.2
20260630,176,185.5,176,185.5,300000,167,11.08,171.32,115.52,0.07
20260701,198,203,190,202,1759000,169.91,18.89,173.32,118.03,0.43
20260702,196.5,206.5,195,206.5,1254000,172.96,19.39,175.55,120.61,0.3
20260703,195,227,186,210.5,31154000,176.09,19.54,178.62,123.21,5.46
20260706,210.5,225.5,189.5,189.5,15957000,177.21,6.94,180.82,125.44,2.46
20260707,185,193.5,171,171,8461000,176.69,-3.22,182.78,127.36,1.23
20260708,170.5,171,158,162,9420000,175.47,-7.67,183.7,129.03,1.3
20260709,167,178,163,178,7290000,175.68,1.32,185.55,130.92,0.96
20260713,176.5,177,160.5,160.5,8500000,174.41,-7.98,185.82,132.52,1.2
20260714,158.5,164,144.5,152,9015000,172.54,-11.91,184.9,133.95,1.21
20260715,160,160,145,151.5,5788000,170.79,-11.29,183.1,135.37,0.75
20260716,145,152.5,141.5,143.5,4255000,168.52,-14.85,180.65,136.69,0.65
20260717,130,135.5,129.5,129.5,4091000,165.27,-21.64,177.35,137.75,0.71
```

## Latest TDCC Snapshot
- as_of_date: 20260717
- over_400_ratio: 67.15
- over_600_ratio: 64.21
- over_800_ratio: 59.52
- over_1000_ratio: 57.65
- over_400_change_1w: -5.35
- over_800_change_1w: -6.98
- over_1000_change_1w: -6.81
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,65.63,,60.4,,59.04,,0,False,False
20260508,73.43,7.8,67.4,7,66.07,7.03,1,True,True
20260515,74.65,1.22,69.81,2.41,67.74,1.67,2,True,True
20260522,74.15,-0.5,69.07,-0.74,67.1,-0.64,0,False,False
20260529,72.66,-1.49,67.68,-1.39,67,-0.1,0,False,False
20260605,72.76,0.1,67.29,-0.39,65.96,-1.04,1,False,False
20260612,72.35,-0.41,66.36,-0.93,64.97,-0.99,0,False,False
20260618,72.1,-0.25,65.95,-0.41,65.33,0.36,1,False,True
20260626,73,0.9,66.41,0.46,65,-0.33,2,False,True
20260703,72.5,-0.5,66.5,0.09,64.46,-0.54,3,False,True
20260717,67.15,-5.35,59.52,-6.98,57.65,-6.81,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8042 | 金山電 | revenue_pullback | 營收成長股價回檔 | 75.0 |  |  |  |  |  | stale_signal | 1.董事會決議日期:115/07/15 2.增資資金來源:現金增資發行新股 3.是否採總括申報發行新股(是，請併敘明預定發行期間/否):否 4.全案發行總金額及股數(如屬盈餘或公積轉增資，發行股數則不含配發給員工部分): 上限普通股12,500仟股 5.採總括申報發行新股案件，本次發行金額及股數:不適用 6.採總括申報發行新股案件，本次發行後，剩餘之金額及股數餘額:不適用 7.每股面額:新臺幣10元 8.發行價格:依「中華民國證券商業同業公會承銷商會員輔導發行公司募集與發行 有價證券自律規則」第六條第一項規定以不低於向金管會申報案件及除權交易日前五個 營業日訂價日前一、三、五個營業日擇一計算之普通股收盤價簡單算術平均數扣除無償 配股除權(或減資除權)及除息後平均股價之七成訂定。實際發行價格及募集金額俟奉主 管機關申報生效後，授權董事長依市場狀況與證券承銷商共同議定之。 9.員工認購股數或配發金額:依公司法第267條規定，保留發行新股總數10%之股份。 10.公開銷售股數:依證券交易法第28-1條，提撥發行新股總額10%辦理公開申購。 11.原股東認購或無償配發比例(請註明暫定每仟股認購或配發股數):其餘80%由原股東按 認股基準日之股東名簿所載持股比例認購。 12.畸零股及逾期未認購股份之處理方式:原股東認購不足一股之畸零股，自停止過戶日 起五日內由股東向本公司股務代理機構辦理拼湊，原股東及員工放棄認購之股份或拼湊 不足一股之畸零股，擬授權董事長洽特定人按發行價格認購之。 13.本次發行新股之權利義務:本次現金增資發行新股採無實體發行，其權利義務與原已 發行普通股股份相同。 14.本次增資資金用途:償還銀行借款。 15.現金減資後再行募資之合理性及必要性 (募資當年度及前一年度有辦理現金減資者適用):不適用 16.其他應敘明事項: (1)本次現金增資發行普通股案於呈奉主管機關核准後，授權董事長訂定認股基準日、 股款繳納期間、增資基準日及其他未盡相關事宜，並於除權交易日前五個營業日召開董 事會決定實際發行價格及辦理增資發行相關事宜。 (2)為掌握訂定發行條件及實際發行作業之時效，現金增資發行新股所訂發行股數、 發行價格、發行條件、募集金額、資金運用狀況暨本案件展延及撤銷等其他有關事項， 如因法令規定或主管機關核定及基於營運評估或因客觀環境須予以修正調整時，擬請董 事會授權董事長全權處理。 (3)為配合前揭現金增資發行普通股之相關發行作業，擬授權本公司董事長代表本公司簽 署一切有關發行之相關契約、文件，並代表本公司辦理相關發行事宜。；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_14d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260717 | 8042 | 金山電 | 2 | 2 | 4 | 9 | 12 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
