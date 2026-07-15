# INDIVIDUAL STOCK CHATGPT PACKET - 3033 威健

## Metadata
- generated_at: 2026-07-15 22:26:52 Asia/Taipei
- stock_id: 3033
- stock_name: 威健
- packet_status: standard_180d_window_packet
- latest_price_date: 20260715
- price_rows: 304
- latest_tdcc_date: 20260709
- tdcc_rows: 11
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3033_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3033_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3033_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3033_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3033.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3033.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3033.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3033.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3033_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3033_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3033_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## ACTION_DISPLAY
- pdf_visible: true
- action_rating_display_zh: 可小量試單
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。
- entry_strategy_zh: 突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 試單 1/3 部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 嚴格突破，價格結構尚未破壞，操作評級為「可小量試單」。 進場策略：突破後順勢追蹤；可依「試單 1/3 部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: starter_position
- action_rating_label_zh: 可小量試單
- confidence_level: medium
- thesis_state: breakout_confirmed
- entry_style: breakout_follow
- position_sizing: starter_1_3

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
- date: 20260715
- open: 51.4
- high: 55.6
- low: 51.3
- close: 55.6
- volume: 37719657
- ma5: 51.26
- ema23_primary: 50.13
- distance_to_ema23_pct: 10.91
- ma20: 50.09
- ma60: 46.74
- ma120: 39.24
- return_5d: 12.55
- return_20d: 12.1
- volume_ratio: 4.27
- distance_to_ma20_pct_auxiliary: 11.01
- distance_to_high_60_pct: 0

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260616,49.9,49.9,48.7,48.8,5422270,48.43,0.77,50.26,41.42,0.31
20260617,48.5,48.95,47.8,48.9,5305376,48.47,0.89,50.13,41.64,0.34
20260618,49.05,49.75,48.75,49.5,5334905,48.55,1.95,49.98,41.91,0.36
20260622,50.4,51.7,50,51.2,13382386,48.77,4.97,49.85,42.21,0.94
20260623,52.3,52.4,49.7,50.2,12994139,48.89,2.67,49.9,42.49,1.03
20260624,49.75,50.6,49.3,50,5438787,48.99,2.07,49.88,42.77,0.45
20260625,50.7,50.9,49.2,49.25,4956433,49.01,0.49,49.81,43.05,0.43
20260626,49.1,51.3,48.8,49,11261112,49.01,-0.01,49.76,43.33,0.99
20260629,50,50,48.6,48.8,4475160,48.99,-0.39,49.68,43.61,0.4
20260630,49.45,49.7,49.1,49.4,2581764,49.02,0.77,49.71,43.89,0.25
20260701,49.8,51.8,49.4,49.8,9803875,49.09,1.45,49.72,44.19,0.94
20260702,49.45,50.5,48.85,50.4,3699502,49.2,2.44,49.75,44.49,0.36
20260703,50.3,50.8,49.75,50.4,3433651,49.3,2.23,49.77,44.77,0.35
20260706,50.9,51.3,50.2,50.4,3736372,49.39,2.04,49.7,45.06,0.44
20260707,50.8,51.1,49.3,49.4,4374999,49.39,0.02,49.78,45.33,0.54
20260708,49.8,49.95,48.85,49.6,2526868,49.41,0.39,49.71,45.58,0.35
20260709,49.9,50.6,49.3,49.6,3135282,49.42,0.36,49.68,45.84,0.5
20260713,51.3,54.3,50.4,50.9,25713816,49.55,2.73,49.74,46.12,3.62
20260714,51.1,51.7,49.75,50.6,11493770,49.63,1.94,49.79,46.39,1.58
20260715,51.4,55.6,51.3,55.6,37719657,50.13,10.91,50.09,46.74,4.27
```

## Latest TDCC Snapshot
- as_of_date: 20260709
- over_400_ratio: 42.47
- over_600_ratio: 39.41
- over_800_ratio: 37.9
- over_1000_ratio: 36.2
- over_400_change_1w: 0.31
- over_800_change_1w: 0.57
- over_1000_change_1w: 0.43
- tdcc_consecutive_up_weeks: 4
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,36.29,,31.7,,29.62,,0,False,False
20260508,39.57,3.28,34.9,3.2,33.39,3.77,1,True,True
20260515,42.06,2.49,37.54,2.64,36.08,2.69,2,True,True
20260522,41.4,-0.66,37.14,-0.4,35.52,-0.56,0,False,False
20260529,41.88,0.48,36.98,-0.16,35.38,-0.14,1,False,False
20260605,41.74,-0.14,36.94,-0.04,35.04,-0.34,2,False,False
20260612,41.08,-0.66,35.81,-1.13,34.26,-0.78,0,False,False
20260618,41.08,0,36.24,0.43,34.35,0.09,1,False,True
20260626,41.31,0.23,36.33,0.09,34.79,0.44,2,True,True
20260703,42.16,0.85,37.33,1,35.77,0.98,3,True,True
20260709,42.47,0.31,37.9,0.57,36.2,0.43,4,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3033 | 威健 | true_breakout | 嚴格突破 | 129.0 |  |  | breakout_confirmed |  | call_strong_inflow | continued_many_days | 1.事實發生日:115/07/13 2.被背書保證之: (1)公司名稱:Weikeng International Co., Ltd.(WKI) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):10,332,950 (5)本次新增背書保證之金額(仟元):321,500 (6)迄事實發生日止背書保證餘額(仟元):10,654,450 (7)被背書保證公司實際動支金額(仟元):8,076,872 (8)本次新增背書保證之原因: 因子公司WKI營運資金需求下,向台中銀行申請融資 額度(續約+新約),該銀行要求母公司威健實業股份有 限公司為子公司擔保,故背書保證金額增加. (1)公司名稱:WEIKENG TECHNOLOGY PTE LTD. (WTP) (2)與提供背書保證公司之關係: 母子公司 (3)背書保證之限額(仟元):15,974,337 (4)原背書保證之餘額(仟元):1,221,700 (5)本次新增背書保證之金額(仟元):578,700 (6)迄事實發生日止背書保證餘額(仟元):1,800,400 (7)被背書保證公司實際動支金額(仟元):992,637 (8)本次新增背書保證之原因: 因子公司WTP營運資金需求下,向匯豐銀行等申請 融資額度(續約+新約),該銀行要求母公司威健實業 股份有限公司為子公司擔保,故背書保證金額增加. 3.被背書保證公司提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.被背書保證公司最近期財務報表之: (1)資本(仟元):2,506,772 (2)累積盈虧金額(仟元):5,653,175 5.解除背書保證責任之: (1)條件: 子公司與銀行之授信契約到期,已無任何借貸行為且不續約, 即背書保證責任之解除. (2)日期: 解除日期：115/5   USD38,500,000.00    NTD500,000,000             115/6   USD10,000,000.00 6.背書保證之總限額(仟元): 31,948,674 7.迄事實發生日為止，背書保證餘額(仟元): 17,097,020 8.迄事實發生日為止，A提供背書保證餘額占公開發行公司最近期財務報表淨值之 比率: 160.54 9.迄事實發生日為止，背書保證、長期投資及資金貸與餘額合計數達該公開發行公 司最近期財務報表淨值之比率: 160.54 10.其他應敘明事項: WKI資本額：2,171,313仟元  WKI累積盈虧：5,512,109仟元 WTP資本額：335,459仟元    WTP累積盈虧：141,066仟元 新約(係指原舊約續展)董事會已先行通過,致舊約尚未到期之銀行背書保證額度重疊 其金額分別為：WKI：803,750仟元(115/7到期NTD160,750仟元,                              115/8到期NTD385,800仟元,                              115/10到期NTD257,200仟元)              WTP：160,750仟元(115/8到期NTD64,300仟元,                               115/10到期NTD96,450仟元)              WKS：661,780仟元(115/7到期NTD330,890仟元,                              115/9到期NTD330,890仟元)；calendar event: monthly_revenue_expected_window on 20260801; status=expected_window; proximity=within_30d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3033 | 威健 | 22 | 1 | 5 | 10 | 20 | continued_many_days | 連續 22 日上榜，需區分醞釀延續或訊號鈍化。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260715 | 3033 | 威健 | 32 | 0 | 17543350.0 | 0.0 |  | call_strong_inflow |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
