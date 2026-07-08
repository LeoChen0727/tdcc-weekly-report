# INDIVIDUAL STOCK CHATGPT PACKET - 6712 長聖

## Metadata
- generated_at: 2026-07-08 22:28:16 Asia/Taipei
- stock_id: 6712
- stock_name: 長聖
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 165
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/6712_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/6712_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/6712_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6712_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6712_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/6712_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/6712_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6712.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6712.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6712.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6712.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6712_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6712_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6712_latest.md?ref=main

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
- risk_control_zh: 股價乖離過大
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 嚴格突破 已出現風險管理訊號，操作評級為「停利」。 進場策略：目前進入停利管理，不建議新買第一筆。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：股價乖離過大

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: take_profit
- action_rating_label_zh: 停利
- confidence_level: low
- thesis_state: breakout_confirmed
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
- date: 20260708
- open: 183
- high: 184
- low: 173.5
- close: 183
- volume: 4039000
- ma5: 167
- ema23_primary: 152.92
- distance_to_ema23_pct: 19.67
- ma20: 150.35
- ma60: 140.43
- ma120: 145.15
- return_5d: 16.93
- return_20d: 34.56
- volume_ratio: 3.57
- distance_to_ma20_pct_auxiliary: 21.72
- distance_to_high_60_pct: -0.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,136,138,135,136,255000,135.93,0.05,134.45,137.27,1.24
20260611,137,138,135,135.5,232000,135.9,-0.29,134.72,137.18,1.15
20260612,137,138,135.5,136.5,167000,135.95,0.41,135.15,137.09,0.83
20260615,138.5,139,137.5,138.5,231000,136.16,1.72,135.43,137.03,1.23
20260616,139.5,140,137,138.5,249000,136.35,1.57,135.68,137.03,1.32
20260617,139,141,138,138,291000,136.49,1.11,135.93,136.97,1.49
20260618,139.5,139.5,138,139,217000,136.7,1.68,136.1,136.94,1.13
20260622,140,143.5,139.5,142.5,656000,137.18,3.88,136.55,136.95,3.01
20260623,144,144.5,140,141.5,306000,137.54,2.88,137,136.93,1.35
20260624,143,155.5,143,152.5,2504000,138.79,9.88,138.05,137.12,7.25
20260625,152.5,154.5,149.5,153,1156000,139.97,9.31,139.15,137.32,2.91
20260626,152.5,152.5,147.5,147.5,475000,140.6,4.91,139.95,137.44,1.15
20260629,156.5,162,154.5,158,3082000,142.05,11.23,141.15,137.76,5.49
20260630,162.5,165,158,158.5,1431000,143.42,10.51,142.28,138.03,2.29
20260701,159,159.5,155,156.5,656000,144.51,8.3,143.2,138.3,1
20260702,156.5,158.5,153,153.5,671000,145.26,5.67,144,138.5,0.98
20260703,155.5,164,154.5,159.5,1033000,146.45,8.91,145,138.81,1.41
20260706,163,167.5,160.5,161.5,763000,147.7,9.34,146.07,139.14,1
20260707,170,177.5,168,177.5,4230000,150.18,18.19,148,139.75,4.44
20260708,183,184,173.5,183,4039000,152.92,19.67,150.35,140.43,3.57
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 42.04
- over_600_ratio: 37.39
- over_800_ratio: 33.89
- over_1000_ratio: 32.16
- over_400_change_1w: -1.22
- over_800_change_1w: -0.86
- over_1000_change_1w: 0.01
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,40.68,,33.72,,31.01,,0,False,False
20260508,40.91,0.23,33.79,0.07,31.08,0.07,1,True,True
20260515,40.92,0.01,33.76,-0.03,31.09,0.01,2,False,True
20260522,40.89,-0.03,33.77,0.01,31.1,0.01,3,False,True
20260529,41.65,0.76,33.77,0,31.1,0,4,False,False
20260605,42.15,0.5,34.64,0.87,31.04,-0.06,5,False,True
20260612,42.81,0.66,34.79,0.15,32.16,1.12,6,True,True
20260618,42.86,0.05,34.84,0.05,32.21,0.05,7,True,True
20260626,43.26,0.4,34.75,-0.09,32.15,-0.06,8,False,False
20260703,42.04,-1.22,33.89,-0.86,32.16,0.01,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6712 | 長聖 | true_breakout | 嚴格突破 | 93.0 |  |  | breakout_confirmed |  |  | continued_overheated | 1.事實發生日:115/06/28 2.研發新藥名稱或代號:嵌合抗原受體T細胞(CAR001) 3.用途:治療復發/難治性實體腫瘤；台灣藥品臨床試驗資訊網連結網址：   https://e-sub.fda.gov.tw/ClinicalTrialInfo/case-search/ES-CCAR01-A3301 4.預計進行之所有研發階段:Phase Ⅰ/Ⅱa 臨床試驗/Phase Ⅱb臨床試驗/Phase Ⅲ臨床   試驗/新藥查驗登記審核 5.目前進行中之研發階段(請說明目前之研發階段係屬提出申請/通過核准/不通過核准 ，若未通過者，請說明公司所面臨之風險及因應措施；另請說明未來經營方向及已投 入累積研發費用):   (1)提出申請/通過核准/不通過核准/各期人體試驗(含期中分析)結果/發生其他影響新      藥研發之重大事件：本公司已完成 CAR001 用於治療復發／難治性實體腫瘤之美國      FDA及台灣TFDA核准之Phase I/IIa臨床試驗中 Phase I 劑量遞增（Dose      Escalation）部分。經安全性監測委員會（SMC）完成審查後，並獲台灣 TFDA 同      意依原核准之臨床試驗計畫啟動 Phase IIa 劑量擴展（Dose Expansion）收案。      A.臨床試驗設計介紹：        a.計畫名稱：一項臨床一／二a期、單組、劑量遞增及劑量擴展之開放性試驗，          評估同種異體嵌合抗原受體（CAR）Gamma-Delta T細胞 CAR001 用於治療復          發／難治性實體腫瘤患者之可行性、安全性及有效性。        b.試驗目的：          (i)Phase I主要目的：評估 CAR001 於受試者之安全性及耐受性，並確認最             大耐受劑量（Maximum Tolerated Dose, MTD）。          (ii)Phase IIa主要目的：評估 CAR001 於復發／難治性實體腫瘤受試者之              初步療效，包括客觀反應率（Objective Response Rate, ORR）等療效              指標，並持續評估其安全性。        c.試驗階段分級：Phase I/IIa臨床試驗。        d.藥品名稱：CAR001。        e.宣稱適應症：復發/難治性實體腫瘤。        f.評估指標：          (i)主要評估指標：             **Phase I：**確認 CAR001 於受試者之最大耐受劑量（Maximum                        Tolerated Dose, MTD）。             **Phase IIa：**客觀反應率（Objective Response Rate, ORR）。          (ii)次要評估指標：不良事件（AE）及嚴重不良事件（SAE）發生率、生命              徵象、實驗室檢查、心電圖及理學檢查等安全性評估，以及其他療效評              估指標。        g.試驗計畫受試者收納人數：Phase Ⅰ受試者15人。      B.主要及次要評估指標之統計結果及統計上之意義：本試驗已完成 Phase I 劑        量遞增試驗，其主要目的為評估 CAR001 之安全性及確認最大耐受劑量（MTD）        。截至目前臨床試驗結果，未觀察到劑量限制性毒性（Dose Limiting        Toxicity, DLT），且未發生與 CAR001 相關之嚴重安全性不良反應，經安全性        監測委員會（SMC）審查後，支持依原核准之臨床試驗計畫推進至 Phase IIa        劑量擴展試驗。      C.單一臨床試驗結果，並不足以充分反映未來新藥開發上市之成敗，投資人應審慎        判斷謹慎投資。   (2)未通過目的事業主管機關許可、各期人體臨床試驗(含期中分析)結果未達統計上顯      著意義或發生其他影響新藥研發之重大事件者，公司所面臨之風險及因應措施：不      適用。   (3)已通過目的事業主管機關許可、各期人體臨床試驗(含期中分析)結果達統計上著意      義或發生其他影響新藥研發之重大事件者，未來經營方向：本公司將持續依美國      FDA 及台灣 TFDA 核准之 Phase I/IIa 臨床試驗計畫推進 Phase IIa 臨床試驗，      並依臨床試驗執行進度、安全性及療效結果，規劃後續 Phase IIb、Phase III 臨      床開發、法規申請及國際授權合作，以推動 CAR001 全球產品開發。   (4)已投入之累積研發費用：因涉及未來授權談判資訊及保護商業競爭機密，以保障公      司及投資人權益，故不予揭露。 6.將再進行之下一階段研發(請說明預計完成時間及預計應負擔之義務):   (1)預計完成時間：實際時程將依臨床執行進度而定。   (2)預計應負擔之義務：將依專屬授權契約書約定支付授權金，及臨床試驗相關研發費      用、行政規費等。 7.市場現況:2024年CAR-T市場規模估計103.8億美元，至2033年將可達1079.2億美元，   2024-2033年複合年成長率(CAGR)為30%。 8.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第8款所定 對股東權益或證券價格有重大影響之事項):無。 9.新藥開發時程長、投入經費高且未保證一定能成功，此等可能使投資面臨風險，投    資人應審慎判斷謹慎投資。:；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 6712 | 長聖 | 2 | 2 | 3 | 6 | 6 | continued_overheated | 連續上榜但短線過熱，需避免追高並等待量價重新確認。 |

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
