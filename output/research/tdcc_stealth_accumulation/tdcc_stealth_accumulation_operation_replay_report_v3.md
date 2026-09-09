# TDCC 潛伏吸籌：方案 A 操作回放 v3

本版已逐事件執行研究規則；歷史資訊、官方日曆、成交與公司行動證據不足，未建立可證明的實現持倉。這不是零報酬結論，也不是正式可交易回測。

- 原始來源：`7ef37a966280201a5ee236856306fdb513de7092`；accepted v2：`2244a0a36c4542cd62948b50f12ef98ade50e1df`。
- 固定 v2：6,821 訊號列、520 股、5,108 個股票＋訊號日；本版 15,324 個事件／horizon 評估。
- entry=D0，D+5/D+10/D+20 以交易所日曆預定，不跳到下一筆有效價格；三個帳本獨立。
- repo 日曆可重現預定日，但未升格為完整官方事件核驗。缺證逐列列於 events.evidence_missing。
- 基準各邊滑價0.1%；0與0.2%僅敏感度；Decimal成本無中間四捨五入。
- 月營收只保留既有lineage；不加入EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報。

| 帳本 | 事件 | 欄位衝突 | 未成熟事件 | 缺證事件 | 持倉 | 已實現 | 淨勝率／平均／中位 |
|---|---:|---:|---:|---:|---:|---:|---|
| D+5 | 5108 | 429 | 821 | 5108 | 0 | 0 | 不可評估（非0） |
| D+10 | 5108 | 429 | 1260 | 5108 | 0 | 0 | 不可評估（非0） |
| D+20 | 5108 | 429 | 1784 | 5108 | 0 | 0 | 不可評估（非0） |

## 缺預定入場價格：保留身分，不挪動日期

- `1909`：訊號日 `20260811`，預定入場 `20260812`；固定來源缺該股票開盤價格，不改用後一筆價格。
- `5371`：訊號日 `20260821`，預定入場 `20260824`；固定來源缺該股票開盤價格，不改用後一筆價格。

## 既有訊號列基準：保持原樣，不與新持倉績效混稱

以下是 accepted v2 summary 的原始欄位快照，未重算或覆寫；它是訊號列加權、原價格序列口徑的歷史觀察，不是方案 A 可交易持倉績效。

```json
[
  {
    "artifact_version": "tdcc_stealth_accumulation_historical_selector_field_contract_replay_v2",
    "replay_kind": "research_only_enum_field_contract_repair_same_historical_population",
    "model_id": "tdcc_stealth_accumulation",
    "model_name_zh": "TDCC潛伏吸籌模型",
    "source_ref": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_sha": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_time": "2026-09-07T18:39:08Z",
    "production_source_sha256": "93ad31cedbc7132a4f34a6e83fd34b0ed163bcd1e7f47b722a0727d0a3acdd6c",
    "selector_contract_version": "current_selector_with_model_owned_enum_fallback_v2",
    "selector_contract_sha256": "13b511f898de561c4c42d8c17dd857b9e55b87b829d8421b95eca951b5ba4767",
    "horizon": "D5",
    "entry_basis": "signal_close_confirmed_next_available_trading_day_open",
    "exit_basis": "fixed_future_D5_close_research_only",
    "cost_basis": "gross_before_fees_taxes_and_slippage",
    "selected_snapshot_count": "36",
    "snapshot_report_date_min": "20260615",
    "snapshot_report_date_max": "20260907",
    "candidate_row_count": "19361",
    "selector_selected_count": "6821",
    "published_membership_match_count": "0",
    "overlap_signal_count": "6301",
    "evaluated_count": "5706",
    "right_censored_count": "1115",
    "invalid_price_count": "0",
    "win_count": "2037",
    "neutral_count": "84",
    "failure_count": "3585",
    "win_rate_pct": "35.699264",
    "neutral_rate_pct": "1.472135",
    "failure_rate_pct": "62.828601",
    "average_return_pct": "-2.288835",
    "median_return_pct": "-2.090592",
    "high_return_hit_count": "309",
    "high_return_hit_rate_pct": "5.415352",
    "loss_count": "3585",
    "loss_rate_pct": "62.828601",
    "unresolved_anomaly_candidate_count": "1",
    "primary_metric_basis": "all_selected_rows_including_overlaps_and_unresolved_anomaly_candidates",
    "sensitivity_analysis_basis": "excluding_unresolved_anomaly_candidates_only",
    "sensitivity_is_corrected_primary": "False",
    "sensitivity_evaluated_count": "5705",
    "sensitivity_excluded_anomaly_candidate_count": "1",
    "sensitivity_win_rate_pct": "35.687993",
    "sensitivity_average_return_pct": "-2.297154",
    "sensitivity_median_return_pct": "-2.090592",
    "candidate_snapshot_pit_status": "immutable_commit_bound_snapshot_generated_at_recorded_not_complete_event_time_PIT_proof",
    "outcome_price_lineage_status": "immutable_source_commit_bound_date_files_adjustment_basis_unverified",
    "phase_classifier_status": "not_invoked_model_owned_enum_field_contract_repair_v2",
    "formal_use": "False",
    "trade_eligible": "False",
    "promotion_evidence_allowed": "False",
    "promotion_status": "research_only_blocked",
    "promotion_blockers": "not_as_published_reconstruction;incomplete_event_time_PIT_proof;price_adjustment_basis_unverified;formal_operation_rules_undecided;field_contract_repair_is_research_only_not_production_semantics",
    "detail_artifact_sha256": "4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3",
    "observed_min_return_pct": "-41.499472",
    "observed_max_return_pct": "48.593750",
    "automatic_anomaly_candidate_count": "1",
    "bounded_large_return_spotcheck_count": "2",
    "large_return_review_status": "unresolved_not_an_exclusion_or_correction"
  },
  {
    "artifact_version": "tdcc_stealth_accumulation_historical_selector_field_contract_replay_v2",
    "replay_kind": "research_only_enum_field_contract_repair_same_historical_population",
    "model_id": "tdcc_stealth_accumulation",
    "model_name_zh": "TDCC潛伏吸籌模型",
    "source_ref": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_sha": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_time": "2026-09-07T18:39:08Z",
    "production_source_sha256": "93ad31cedbc7132a4f34a6e83fd34b0ed163bcd1e7f47b722a0727d0a3acdd6c",
    "selector_contract_version": "current_selector_with_model_owned_enum_fallback_v2",
    "selector_contract_sha256": "13b511f898de561c4c42d8c17dd857b9e55b87b829d8421b95eca951b5ba4767",
    "horizon": "D10",
    "entry_basis": "signal_close_confirmed_next_available_trading_day_open",
    "exit_basis": "fixed_future_D10_close_research_only",
    "cost_basis": "gross_before_fees_taxes_and_slippage",
    "selected_snapshot_count": "36",
    "snapshot_report_date_min": "20260615",
    "snapshot_report_date_max": "20260907",
    "candidate_row_count": "19361",
    "selector_selected_count": "6821",
    "published_membership_match_count": "0",
    "overlap_signal_count": "6301",
    "evaluated_count": "5082",
    "right_censored_count": "1739",
    "invalid_price_count": "0",
    "win_count": "1498",
    "neutral_count": "60",
    "failure_count": "3524",
    "win_rate_pct": "29.476584",
    "neutral_rate_pct": "1.180638",
    "failure_rate_pct": "69.342778",
    "average_return_pct": "-5.351211",
    "median_return_pct": "-4.717073",
    "high_return_hit_count": "327",
    "high_return_hit_rate_pct": "6.434475",
    "loss_count": "3524",
    "loss_rate_pct": "69.342778",
    "unresolved_anomaly_candidate_count": "1",
    "primary_metric_basis": "all_selected_rows_including_overlaps_and_unresolved_anomaly_candidates",
    "sensitivity_analysis_basis": "excluding_unresolved_anomaly_candidates_only",
    "sensitivity_is_corrected_primary": "False",
    "sensitivity_evaluated_count": "5081",
    "sensitivity_excluded_anomaly_candidate_count": "1",
    "sensitivity_win_rate_pct": "29.462704",
    "sensitivity_average_return_pct": "-5.369150",
    "sensitivity_median_return_pct": "-4.721030",
    "candidate_snapshot_pit_status": "immutable_commit_bound_snapshot_generated_at_recorded_not_complete_event_time_PIT_proof",
    "outcome_price_lineage_status": "immutable_source_commit_bound_date_files_adjustment_basis_unverified",
    "phase_classifier_status": "not_invoked_model_owned_enum_field_contract_repair_v2",
    "formal_use": "False",
    "trade_eligible": "False",
    "promotion_evidence_allowed": "False",
    "promotion_status": "research_only_blocked",
    "promotion_blockers": "not_as_published_reconstruction;incomplete_event_time_PIT_proof;price_adjustment_basis_unverified;formal_operation_rules_undecided;field_contract_repair_is_research_only_not_production_semantics",
    "detail_artifact_sha256": "4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3",
    "observed_min_return_pct": "-48.083333",
    "observed_max_return_pct": "85.795455",
    "automatic_anomaly_candidate_count": "1",
    "bounded_large_return_spotcheck_count": "2",
    "large_return_review_status": "unresolved_not_an_exclusion_or_correction"
  },
  {
    "artifact_version": "tdcc_stealth_accumulation_historical_selector_field_contract_replay_v2",
    "replay_kind": "research_only_enum_field_contract_repair_same_historical_population",
    "model_id": "tdcc_stealth_accumulation",
    "model_name_zh": "TDCC潛伏吸籌模型",
    "source_ref": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_sha": "7ef37a966280201a5ee236856306fdb513de7092",
    "source_commit_time": "2026-09-07T18:39:08Z",
    "production_source_sha256": "93ad31cedbc7132a4f34a6e83fd34b0ed163bcd1e7f47b722a0727d0a3acdd6c",
    "selector_contract_version": "current_selector_with_model_owned_enum_fallback_v2",
    "selector_contract_sha256": "13b511f898de561c4c42d8c17dd857b9e55b87b829d8421b95eca951b5ba4767",
    "horizon": "D20",
    "entry_basis": "signal_close_confirmed_next_available_trading_day_open",
    "exit_basis": "fixed_future_D20_close_research_only",
    "cost_basis": "gross_before_fees_taxes_and_slippage",
    "selected_snapshot_count": "36",
    "snapshot_report_date_min": "20260615",
    "snapshot_report_date_max": "20260907",
    "candidate_row_count": "19361",
    "selector_selected_count": "6821",
    "published_membership_match_count": "0",
    "overlap_signal_count": "6301",
    "evaluated_count": "4322",
    "right_censored_count": "2499",
    "invalid_price_count": "0",
    "win_count": "1072",
    "neutral_count": "34",
    "failure_count": "3216",
    "win_rate_pct": "24.803332",
    "neutral_rate_pct": "0.786673",
    "failure_rate_pct": "74.409995",
    "average_return_pct": "-8.255696",
    "median_return_pct": "-7.969639",
    "high_return_hit_count": "337",
    "high_return_hit_rate_pct": "7.797316",
    "loss_count": "3216",
    "loss_rate_pct": "74.409995",
    "unresolved_anomaly_candidate_count": "1",
    "primary_metric_basis": "all_selected_rows_including_overlaps_and_unresolved_anomaly_candidates",
    "sensitivity_analysis_basis": "excluding_unresolved_anomaly_candidates_only",
    "sensitivity_is_corrected_primary": "False",
    "sensitivity_evaluated_count": "4321",
    "sensitivity_excluded_anomaly_candidate_count": "1",
    "sensitivity_win_rate_pct": "24.785929",
    "sensitivity_average_return_pct": "-8.267469",
    "sensitivity_median_return_pct": "-7.969639",
    "candidate_snapshot_pit_status": "immutable_commit_bound_snapshot_generated_at_recorded_not_complete_event_time_PIT_proof",
    "outcome_price_lineage_status": "immutable_source_commit_bound_date_files_adjustment_basis_unverified",
    "phase_classifier_status": "not_invoked_model_owned_enum_field_contract_repair_v2",
    "formal_use": "False",
    "trade_eligible": "False",
    "promotion_evidence_allowed": "False",
    "promotion_status": "research_only_blocked",
    "promotion_blockers": "not_as_published_reconstruction;incomplete_event_time_PIT_proof;price_adjustment_basis_unverified;formal_operation_rules_undecided;field_contract_repair_is_research_only_not_production_semantics",
    "detail_artifact_sha256": "4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3",
    "observed_min_return_pct": "-56.709265",
    "observed_max_return_pct": "68.188976",
    "automatic_anomaly_candidate_count": "1",
    "bounded_large_return_spotcheck_count": "2",
    "large_return_review_status": "unresolved_not_an_exclusion_or_correction"
  }
]
```

## 六筆異常候選全部保留

六筆仍為 unresolved_anomaly_candidate；未刪除原主結果。排除候選的 summary 列只屬 sensitivity，不是修正／清理績效。數值大小不自行判定資料錯誤或非可比。

- 8261／20260616／d10_max_observed_return：保留；歷史可用、成交及公司行動證據仍缺。
- 2492／20260709／d5_min_observed_return：保留；歷史可用、成交及公司行動證據仍缺。
- 1447／20260626／d5_max_observed_return：保留；歷史可用、成交及公司行動證據仍缺。
- 3624／20260714／d10_min_observed_return：保留；歷史可用、成交及公司行動證據仍缺。
- 8358／20260630／d20_min_observed_return：保留；歷史可用、成交及公司行動證據仍缺。
- 3653／20260717／d20_max_observed_return：保留；歷史可用、成交及公司行動證據仍缺。

## 使用界線

獨立 validator 與合成測試驗證規則實作；它們不能補造缺失的歷史證據。後續高低報酬特徵比較須同買點、出場窗、持倉及異常口徑，不能用本版缺證樣本新增條件或升級模型。

`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。無正式推薦、PDF、operation adapter 或 production 修改。
