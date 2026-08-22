# 營收改善但股價尚未反應：三錨點位階與型態轉換矩陣

- generated_at: `2026-08-23 01:32:06 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `position_shape_transition_matrix_v2_20260822`
- adopted_grid: `rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|d30|none_no_stop_reference`
- 狀態：`research_only`；分類不是正式模型 gate、ranking、PDF 或 promotion evidence。
- 位階：anchor 前 120 個交易日，不含 anchor；低位 <=40%、中位 >40%~75%、高位 >75%。
- 型態：本 revenue 模型自有定義，分盤整、上升、下降、混合／轉折。
- 財報欄位全部排除；本 artifact 僅使用 PIT 月營收來源與 adjusted analysis price。
- `asof_latest_qualifying_trade_date` 可能晚於突破前一週；此時只作標籤順序比較，不宣稱 chronological transition。
- primary 保留 anomaly candidates；候選排除只另列 sensitivity。

## 三錨點覆蓋

| anchor_id | analysis_basis_operation_count | anchor_classification_observed_count | anchor_classification_coverage_pct |
| --- | --- | --- | --- |
| revenue_available | 989 | 462 | 46.7139 |
| pre_breakout_week_close | 989 | 554 | 56.0162 |
| formal_confirmation_close | 989 | 573 | 57.9373 |

## 主要錨點狀態序列

| row_type | anchor_chronology_id | comparison_sequence_semantics | position_transition_id | shape_transition_id | operation_count | win_rate_pct | avg_return_pct | median_return_pct | p10_return_pct | p90_return_pct | return_ge20_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>rising | 19 | 52.6316 | 5.9123 | 5.7426 | -12.695 | 27.6359 | 15.7895 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>rising>rising | 18 | 27.7778 | -6.7025 | -11.3044 | -26.3474 | 14.2851 | 5.5556 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>rising>rising | 17 | 64.7059 | 6.4299 | 11.3208 | -21.2081 | 28.8682 | 17.6471 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | falling>falling>rising | 15 | 80.0 | 19.2615 | 21.0843 | -7.9813 | 48.4002 | 53.3333 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 10 | 20.0 | 6.9691 | -11.0948 | -19.3401 | 61.4373 | 20.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | consolidation>consolidation>rising | 9 | 44.4444 | 10.1582 | -3.625 | -13.8318 | 41.9236 | 22.2222 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>rising | 9 | 77.7778 | 10.789 | 6.7669 | -7.1396 | 35.2564 | 22.2222 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>falling>rising | 9 | 77.7778 | 15.9556 | 0.5217 | -8.0822 | 60.6626 | 22.2222 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 8 | 50.0 | 26.6287 | 0.2372 | -16.9166 | 110.3567 | 25.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>consolidation | 7 | 42.8571 | 2.0078 | -3.5503 | -5.7422 | 12.2795 | 14.2857 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | falling>falling>rising | 7 | 57.1429 | 14.0426 | 9.4444 | -19.8696 | 50.9722 | 42.8571 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>consolidation | 7 | 85.7143 | 2.9835 | 4.6847 | -3.1743 | 8.0629 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>mid_pos_40_75 | falling>falling>rising | 7 | 100.0 | 8.1072 | 5.5205 | 2.3996 | 15.4344 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | falling>mixed_or_turn>rising | 7 | 71.4286 | 19.3238 | 27.193 | -14.0815 | 46.1217 | 57.1429 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>rising | 6 | 83.3333 | 13.2605 | 9.2232 | 0.647 | 29.9113 | 33.3333 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>consolidation>consolidation | 6 | 16.6667 | -1.9813 | -2.4686 | -6.5363 | 3.061 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>high_pos_gt75>high_pos_gt75 | consolidation>rising>rising | 6 | 83.3333 | 18.1598 | 11.1851 | -2.9003 | 46.1947 | 33.3333 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>mid_pos_40_75 | consolidation>consolidation>consolidation | 6 | 16.6667 | -1.5324 | -3.9325 | -8.6057 | 7.941 | 0.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>rising | 5 | 40.0 | -5.2817 | -3.8585 | -12.3774 | 1.0932 | 0.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>high_pos_gt75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 5 | 80.0 | 23.1599 | 17.5676 | -0.7316 | 52.4912 | 40.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 5 | 60.0 | 22.1146 | 9.4017 | -10.428 | 62.7942 | 40.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>consolidation>rising | 5 | 100.0 | 6.5823 | 5.875 | 3.7807 | 9.694 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 5 | 100.0 | 56.772 | 63.0435 | 35.2775 | 72.2666 | 100.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | consolidation>consolidation>consolidation | 5 | 0.0 | -4.3018 | -3.8636 | -5.7663 | -3.2791 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>consolidation>rising | 5 | 60.0 | -2.423 | 3.8647 | -16.3286 | 8.1724 | 0.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 4 | 25.0 | 1.9746 | -10.1267 | -16.7611 | 30.3915 | 25.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>consolidation | 4 | 50.0 | 3.5187 | 5.3192 | -7.8564 | 13.4535 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>rising>rising | 4 | 50.0 | 3.3661 | 4.5436 | -5.9369 | 11.727 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 4 | 50.0 | 2.4229 | -5.9585 | -23.5821 | 35.1331 | 25.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | rising>consolidation>rising | 4 | 75.0 | 58.4283 | 66.3763 | 2.2976 | 108.2008 | 75.0 |
