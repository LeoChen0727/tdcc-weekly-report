# INDIVIDUAL STOCK CHATGPT PACKET - 3008 大立光

## Metadata
- generated_at: 2026-06-17 22:23:31 Asia/Taipei
- stock_id: 3008
- stock_name: 大立光
- packet_status: standard_180d_window_packet
- latest_price_date: 20260617
- price_rows: 283
- latest_tdcc_date: 20260612
- tdcc_rows: 7
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/3008_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/3008_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/3008_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/3008_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/3008_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3008.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3008.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3008.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3008.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3008_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3008_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3008_latest.md?ref=main

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
- action_rating_display_zh: 停利
- model_category_display_zh: 嚴格突破
- score_interpretation_zh: 模型分數高，代表條件集中度較強。 目前以風險管理為主，不適合新買第一筆。
- action_summary_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。
- entry_strategy_zh: 目前進入停利管理，不建議新買第一筆。
- position_sizing_zh: 僅觀察；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: TDCC 歷史不足、TDCC 轉弱警訊、股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：TDCC 歷史不足、TDCC 轉弱警訊、股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: high_level_distribution_risk
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
- decision_score_high
- price_structure_not_broken
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
- insufficient_tdcc_history
- tdcc_distribution_warning
- price_too_extended

### chatgpt_instruction
- Formal PDF/report output must use ACTION_DISPLAY fields, not raw ACTION_DECISION field names or raw action values.
- Do not print ACTION_DECISION, action_rating, starter_position, decision_score, model_slug, packet, raw field, or 程式端欄位 in investor-facing PDF prose.
- Treat post-entry watch display text as management items, not as buy-before blockers.

## Latest Price Snapshot
- date: 20260617
- open: 5065
- high: 5310
- low: 4960
- close: 5145
- volume: 5581398
- ma5: 4522
- ema23_primary: 3811.46
- distance_to_ema23_pct: 34.99
- ma20: 3831
- ma60: 2945.25
- ma120: 2651.71
- return_5d: 39.81
- return_20d: 49.35
- volume_ratio: 2.15
- distance_to_ma20_pct_auxiliary: 34.3
- distance_to_high_60_pct: -3.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260518,3400,3400,3125,3290,4461026,2737.49,20.18,2704.75,2472.58,2.06
20260519,3445,3615,3325,3365,5982140,2789.78,20.62,2737.5,2490.5,2.57
20260520,3330,3410,3200,3200,1168759,2823.96,13.32,2765.25,2505.08,0.51
20260521,3285,3520,3280,3460,1745376,2876.97,20.27,2809,2524.58,0.76
20260522,3450,3595,3450,3540,1289200,2932.22,20.73,2861.75,2544.08,0.57
20260525,3635,3845,3635,3845,1446961,3008.29,27.81,2928,2567.67,0.64
20260526,3875,3875,3665,3665,1129814,3063.01,19.65,2980.5,2588.5,0.52
20260527,3690,3720,3500,3505,1354119,3099.84,13.07,3026.75,2604.92,0.63
20260528,3505,3630,3420,3425,1352548,3126.94,9.53,3068.25,2621.08,0.63
20260529,3515,3600,3450,3515,1477877,3159.28,11.26,3118.25,2638.83,0.68
20260601,3630,3835,3630,3835,1342805,3215.59,19.26,3181.25,2664.33,0.62
20260602,3780,3850,3705,3850,1408889,3268.46,17.79,3246.5,2689.17,0.64
20260603,3920,4225,3820,3985,3706976,3328.17,19.74,3319.75,2715.92,1.6
20260604,3780,3850,3705,3850,1408889,3371.65,14.19,3383.5,2742,0.61
20260605,3750,3750,3570,3680,2295854,3397.35,8.32,3439,2765,0.97
20260611,4000,4310,4000,4165,4290350,3461.32,20.33,3520,2794.58,1.69
20260612,4300,4355,4020,4020,3557528,3507.88,14.6,3581.25,2822.33,1.39
20260615,4080,4420,4035,4420,3675345,3583.89,23.33,3659.75,2856.92,1.46
20260616,4480,4860,4450,4860,3306359,3690.23,31.7,3746,2899.5,1.34
20260617,5065,5310,4960,5145,5581398,3811.46,34.99,3831,2945.25,2.15
```

## Latest TDCC Snapshot
- as_of_date: 20260612
- over_400_ratio: 56.16
- over_600_ratio: 49.9
- over_800_ratio: 45.26
- over_1000_ratio: 41.78
- over_400_change_1w: -0.31
- over_800_change_1w: 0.87
- over_1000_change_1w: 0.1
- tdcc_consecutive_up_weeks: 5
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,59.04,,47.16,,45.89,,0,False,False
20260508,57.93,-1.11,45.77,-1.39,43.75,-2.14,0,False,False
20260515,57.94,0.01,46.07,0.3,43.44,-0.31,1,False,True
20260522,57.31,-0.63,46.17,0.1,40.8,-2.64,2,False,True
20260529,56.64,-0.67,43.54,-2.63,39.43,-1.37,3,False,False
20260605,56.47,-0.17,44.39,0.85,41.68,2.25,4,False,True
20260612,56.16,-0.31,45.26,0.87,41.78,0.1,5,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3008 | 大立光 | true_breakout | 嚴格突破 | 84.0 |  |  | platform_breakout |  | no_signal | continued_overheated | 1.標的物之名稱及性質（如坐落台中市北區ＸＸ段ＸＸ小段土地）: 機器設備 2.事實發生日:114/9/4~115/6/15 3.董事會通過日期: 不適用 4.其他核決日期: 核決層級:董事長 民國115年6月15日 5.交易單位數量（如ＸＸ平方公尺，折合ＸＸ坪）、每單位價格及交易總金額: 交易數量: 一批；總金額為新台幣647,560,741元 6.交易相對人及其與公司之關係（交易相對人如屬自然人，且非公司之關 係人者，得免揭露其姓名）: 大族激光科技產業集團股份有限公司; 與公司關係:無 7.交易相對人為關係人者，並應公告選定關係人為交易對象之原因及前次移轉之 所有人、前次移轉之所有人與公司及交易相對人間相互之關係、前次移轉日期 及移轉金額: 不適用 8.交易標的最近五年內所有權人曾為公司之關係人者，尚應公告關係 人之取得及處分日期、價格及交易當時與公司之關係: 不適用 9.預計處分利益（或損失）（取得資產者不適用）（遞延者應列表說明 認列情形）: 不適用 10.交付或付款條件（含付款期間及金額）、契約限制條款及其他重要約定 事項: 依訂購協議規定 11.本次交易之決定方式（如招標、比價或議價）、價格決定之參考依據及 決策單位: 交易決定方式:比價及議價;  決策單位: 依本公司核決權限規定辦理 12.專業估價者事務所或公司名稱及其估價金額: 不適用 13.專業估價師姓名: 不適用 14.專業估價師開業證書字號: 不適用 15.估價報告是否為限定價格、特定價格或特殊價格:是 16.是否尚未取得估價報告:否或不適用 17.尚未取得估價報告之原因: 不適用 18.估價結果有重大差異時，其差異原因及會計師意見: 不適用 19.會計師事務所名稱: 不適用 20.會計師姓名: 不適用 21.會計師開業證書字號: 不適用 22.經紀人及經紀費用: 不適用 23.取得或處分之具體目的或用途: 供生產用 24.本次交易表示異議之董事之意見: 不適用 25.本次交易為關係人交易:否 26.監察人承認或審計委員會同意日期: 不適用 27.本次交易係向關係人取得不動產或其使用權資產:否 28.依「公開發行公司取得或處分資產處理準則」第十六條規定 評估之價格:不適用 29.依前項評估之價格較交易價格為低者，依同準則第十七條規 定評估之價格:不適用 30.前已就同一件事件發布重大訊息日期: 不適用 31.其他敘明事項: 無；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3008 | 大立光 | 6 | 3 | 5 | 7 | 7 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260617 | 3008 | 大立光 | 0 | 12 | 0.0 | 577420.0 | 0.0 | no_signal |

## Interpretation Guardrails
- ACTION_DISPLAY is the PDF-visible report language contract.
- ACTION_DECISION is internal model context only; do not print its raw field names or raw values in investor-facing prose.
- Use entry_strategy_zh, position_sizing_zh, add_position_strategy_zh, take_profit_strategy_zh, risk_control_zh, and post_entry_watch_zh for report text.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
