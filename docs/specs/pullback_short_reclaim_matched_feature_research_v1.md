# 回檔後短線轉強：同訊號日連續特徵研究 v1

授權：使用者要求將 `pullback_short_reclaim` 從每日 PDF 撤下，但繼續升級研究。
本研究只補足 PR #700 尚未回答的分析單位、集中度與連續特徵問題；它不是正式模型、
選股條件、最佳門檻搜尋、操作規則、PDF 輸入或 promotion evidence。

## 固定來源

唯一來源是 main commit `f4e71df3ffcf2982bcc1dc6972599717d461d082` 的兩個 immutable blobs：

- `output/research/pullback_short_reclaim/pullback_short_reclaim_23ema_condition_comparison_v1_detail.csv`
  - raw SHA-256 `34a3a327a980b1caba4aa54f510f80cfb40a48034e9268cff5de804e653144e4`
- `output/research/pullback_short_reclaim/pullback_short_reclaim_23ema_condition_comparison_v1_manifest.json`
  - raw SHA-256 `82936597ae0e8e61c45aac92aa6049a10c35eecc2a30a31d3116600dd7f247f9`

Producer 不重跑舊 producer、不重算股價或訊號、不讀 mutable `latest`，也不 import
23EMA 或正式模型 business functions。來源必須仍為 3020 原列、2992 個
`primary_metric_included=True` unique signal events，且任一 D5/D10/D20
`comparison_anomaly_candidate=True` 的 event union 必須仍為 8 筆。

## 不重做 PR #700

PR #700 已完整比較 `ret20_5_25`、`tdcc_positive`、`obv_positive`、
`technical_quality` 四個既定旗標，在 all／每月、D5/D10/D20、三種 metric basis、
三種 feature population 中列出高報酬／一般非負／虧損比例。不得把相同旗標比例、
相同月份切片或相同 D5/D10/D20 報表重新包裝為新研究。

本研究的新問題只有：

1. 同一 `signal_date` 內，高報酬、一般非負與虧損股票的連續
   `return_20d`、`RSI14`、`MACD histogram`、`model_score` 分布有何差異。
2. 每個 signal date 的高報酬－虧損 median 差是否同方向；日期等權與事件等權必須分列。
3. 結果有多少集中在少數日期、重複股票、互相重疊的固定持有區間及既有 8 個
   comparison anomaly candidate events。

不搜尋新門檻、不做排列最佳化、不新增選股、不改 entry／exit／stop；高報酬仍固定為
`>=10%`、一般非負為 `0%<=return<10%`、虧損為 `<0%`、尾端虧損為 `<=-10%`。

## 四份 model-owned 輸出

Owner 是 `pullback_short_reclaim_matched_feature_research`。固定 prefix：

`output/research/pullback_short_reclaim/pullback_short_reclaim_matched_feature_research_v1_`

輸出只有：

- `metrics.csv`
- `features.csv`
- `audit.csv`
- `manifest.json`

### metrics.csv ordered schema

```text
artifact_version,model_id,period,horizon,metric_basis,return_cost_basis,aggregation_basis,
signal_count,mature_count,immature_count,unique_stock_count,signal_date_count,
win_count,win_rate_pct,neutral_count,neutral_rate_pct,failure_count,failure_rate_pct,
average_return_pct,median_return_pct,high_return_ge10_count,high_return_ge10_rate_pct,
loss_count,loss_rate_pct,tail_loss_le_minus10_count,tail_loss_le_minus10_rate_pct,
source_anomaly_candidate_count,comparison_anomaly_candidate_count,
union_review_candidate_event_count,primary_retains_unresolved_candidates,
sensitivity_is_corrected_primary,first_publication_pit_proven,first_publication_pit_status,
total_return_complete,
formal_use_allowed,trade_eligible,promotion_evidence_allowed,operation_contract_status
```

每個 `period=all|YYYYMM`、`horizon=5|10|20` 恰好一列。只允許
`metric_basis=raw_primary_including_unresolved` 與
`aggregation_basis=unique_signal_event_equal_weight`。所有 unresolved candidates 保留；
這張表不得包含 candidate-excluded 替代結果。每列都必須明列
`return_cost_basis=raw_return_before_costs_slippage_and_tax`，以及
`first_publication_pit_proven=False`、`first_publication_pit_status=unknown_not_proven`；
固定 source commit 只凍結既有 evidence，不能把未知 PIT 改寫成已證明。

### features.csv ordered schema

```text
artifact_version,model_id,period,signal_date,horizon,feature_id,source_field,row_type,
outcome_band,aggregation_basis,population_count,value_count,missing_value_count,
q1,median,q3,iqr,high_value_count,loss_value_count,high_median,loss_median,
high_minus_loss_median,paired_signal_date_count,paired_status,positive_difference_count,
zero_difference_count,negative_difference_count,positive_difference_rate_pct,
negative_difference_rate_pct,feature_scale_note,
primary_retains_unresolved_candidates,first_publication_pit_proven,
formal_use_allowed,promotion_evidence_allowed
```

固定 feature：

- `return_20d` ← `feature_return_20d`
- `rsi14` ← `feature_price_pullback_rsi14`
- `macd_hist` ← `feature_price_pullback_macd_hist`
- `model_score` ← `model_score`

固定 row types：

- `period_event_equal_outcome_band`：all／月內事件等權的 high／middle／loss N、Q1、median、Q3、IQR。
- `signal_date_outcome_band`：單一 signal date 內事件等權的 high／middle／loss分布。
- `signal_date_high_loss_contrast`：同日 high median 減 loss median；任一側無有效值時差值必須空白。
- `period_date_equal_high_loss_contrast`：只對有雙方的同日 median 差做日期等權分布；
  `paired_signal_date_count` 與正／零／負差異日期數及比率必須明列，不得拿事件數冒充日期數，
  也不得只挑同方向或有利月份呈現。

Outcome-band rows 的 `population_count` 是該 band 的事件數，`value_count` 才是 feature
非缺值 N，兩者差額必須等於 `missing_value_count`；不得用全體成熟事件數冒充 band N。

Quartile method 固定為 pandas linear interpolation。MACD histogram 是未正規化的 raw value，
不同股票尺度不可直接相比；其跨股 median／IQR 只能描述，不得單獨支持門檻或推薦條件。

### audit.csv ordered schema

```text
artifact_version,model_id,period,horizon,audit_type,audit_key,signal_date,stock_id,
signal_event_id,report_line,identity_disposition,source_duplicate_count,entry_date,exit_date,
maturity_status,return_pct,signal_count,mature_count,
unique_stock_count,signal_date_count,largest_signal_date,largest_signal_date_count,
largest_signal_date_share_pct,repeated_stock_count,repeated_stock_signal_count,
overlap_pair_count,overlap_stock_count,overlap_eligible_event_count,
overlap_not_assessed_event_count,boundary_touch_pair_count,overlap_interval_basis,
overlap_interpretation,source_row_count,canonical_signal_event_count,
source_duplicate_group_count,source_duplicate_extra_row_count,
canonical_same_stock_signal_date_group_count,canonical_same_stock_signal_date_event_count,
canonical_same_stock_signal_date_cross_report_line_group_count,
review_candidate_union_event_count,
review_candidate_mature_count,review_candidate_return_sum_pct,
review_candidate_average_point_contribution_pct,primary_return_sum_pct,
review_candidate_share_of_primary_return_sum_pct,primary_average_return_pct,
candidate_exclusion_sensitivity_average_return_pct,candidate_exclusion_sensitivity_delta_pct,
review_candidate_disposition,review_candidate_reason,audit_status,
primary_retains_unresolved_candidates,
sensitivity_is_corrected_primary,first_publication_pit_proven,formal_use_allowed,
promotion_evidence_allowed,operation_contract_status
```

固定 audit types：

- `source_identity_summary`
- `source_duplicate_identity`
- `period_concentration`
- `period_stock_interval_overlap`
- `review_candidate_union_contribution`
- `review_candidate_event`

Identity audit 必須揭露 3020 source rows、2992 canonical unique signal events、28 個
`source_duplicate_count=2` 的 canonical identities 與 28 個 upstream duplicate extra rows；
逐一列出這 28 個 `signal_event_id`、`report_line`、`stock_id`、`signal_date`，並保留 upstream
`identity_disposition`。若 canonical corpus 存在同 stock／同 signal date 的多 identity 或跨
`report_line` identity，必須另外計數；不得再按 stock/date 任意二次去重。本固定來源兩者皆為 0。

Overlap 只依已成熟且 `entry_date`、固定 horizon `exit_date` 均可解析的事件閉區間，計算同股
區間 pair 是否交疊；未成熟事件明列為 `overlap_not_assessed_event_count`，不能視為無重疊。
同日一個 interval close 與另一個 interval open 的端點相接，保守計入 inclusive overlap 並另列
`boundary_touch_pair_count`，但只能稱日期區間相交，不能稱已證明的實際持倉衝突。這是對既有
研究事件相依性的診斷，不是把樣本改造成 non-overlapping trades，也不創造正式 position ledger。
8-event union contribution 保留在 primary；排除 union 的平均只可標為 sensitivity，
`sensitivity_is_corrected_primary=False`。在觸發 horizon 的逐事件列，
`review_candidate_disposition` 必須仍為 `unresolved_anomaly_candidate`；不得用數值幅度直接改判。

### manifest.json

Manifest 必須保存 source commit/path/raw SHA、三個 CSV SHA、三份 ordered schema、固定 periods、
horizons、feature／row types、`quantile_method=linear`、`union_review_candidate_event_count=8`、
snapshot coverage 與下列限制。Validator 必須獨立重算三份 CSV，不得 import producer。

## 必須保留的限制

- 原 price source 是 `mutable_current_file_unpinned`；本研究的 source commit pin 只凍結已產出的
  evidence，不能倒推 event-time immutable price lineage 已成立。
- `trading_calendar_status=stock_price_row_sequence_only_no_market_calendar_proof`；固定第 N 筆價格列
  不等於官方市場日曆已證明。
- 同股重疊 audit 不會使 `non_overlapping_trades_proven` 變成 true。
- 202607 的 context schema 自 20260703 才開始；202608 只含 manifest 既有九個 snapshot dates；
  月份是 same-sample diagnostics，不是完整月或獨立 OOS。
- 8 個 review candidates 全留在 primary。統計幅度只是 investigation trigger，不是 data error、
  non-comparable 或 final disposition。
- `first_publication_pit_proven=False`、`total_return_complete=False`、
  `formal_use_allowed=False`、`trade_eligible=False`、
  `promotion_evidence_allowed=False`、`operation_contract_status=decision_required`。
- 不修改正式模型、23EMA、原 evidence、adapter、readiness、workflow 或 PDF；不開始 90 天觀察。
- 本研究 primary corpus 是全部 `primary_metric_included=True` unique events；不得與 PR #700 的
  complete-schema 或其他 feature population 指標混稱同一母體，更不得把母體差異描述為改善。

## 寫入與驗證保護

Producer 寫入前必須通過 exact ownership registration，保護 HEAD、index、registered sentinels
與兩個固定 source artifacts；run 中只允許四個新 artifact paths。已存在且 bytes 不同的
artifact 必須 fail closed。Registry 尚未完成前只能執行 pure build functions／pytest temp
fixtures，不得產生正式 artifact。
