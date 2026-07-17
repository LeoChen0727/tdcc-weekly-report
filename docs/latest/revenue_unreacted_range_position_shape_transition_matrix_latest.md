# 營收改善但股價尚未反應：三錨點位階與型態轉換矩陣

- generated_at: `2026-07-17 10:06:41 Asia/Taipei`
- model_id: `revenue_unreacted_range`
- artifact_version: `position_shape_transition_matrix_v1_20260717`
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
| revenue_available | 955 | 462 | 48.377 |
| pre_breakout_week_close | 955 | 513 | 53.7173 |
| formal_confirmation_close | 955 | 551 | 57.6963 |

## 主要錨點狀態序列

| row_type | anchor_chronology_id | comparison_sequence_semantics | position_transition_id | shape_transition_id | operation_count | win_rate_pct | avg_return_pct | median_return_pct | p10_return_pct | p90_return_pct | return_ge20_rate_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>rising>rising | 20 | 65.0 | 5.9541 | 11.2487 | -21.1658 | 23.6644 | 15.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>rising>rising | 18 | 27.7778 | -5.8772 | -11.0237 | -26.3474 | 18.5735 | 11.1111 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>rising | 14 | 57.1429 | 7.9253 | 7.4245 | -14.1231 | 37.7888 | 21.4286 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | falling>falling>rising | 14 | 85.7143 | 21.977 | 21.4681 | -1.514 | 50.0746 | 57.1429 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>consolidation | 10 | 70.0 | 2.0609 | 3.4251 | -4.9843 | 7.8644 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>mid_pos_40_75 | consolidation>consolidation>consolidation | 10 | 50.0 | 6.5049 | 1.0407 | -7.1964 | 20.2465 | 10.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 10 | 20.0 | 6.9691 | -11.0948 | -19.3401 | 61.4373 | 20.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>falling>rising | 9 | 77.7778 | 15.9556 | 0.5217 | -8.0822 | 60.6626 | 22.2222 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>rising | 8 | 87.5 | 16.5113 | 9.2232 | 0.9057 | 39.007 | 37.5 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>high_pos_gt75>high_pos_gt75 | consolidation>rising>rising | 8 | 75.0 | 15.0224 | 8.9055 | -3.7839 | 35.9856 | 25.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>consolidation | 7 | 42.8571 | 2.0078 | -3.5503 | -5.7422 | 12.2795 | 14.2857 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | consolidation>consolidation>rising | 7 | 42.8571 | 12.6248 | -3.625 | -13.7038 | 50.6473 | 28.5714 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>high_pos_gt75>high_pos_gt75 | consolidation>consolidation>rising | 7 | 71.4286 | 2.5773 | 4.8499 | -7.6888 | 10.7173 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>mid_pos_40_75 | falling>falling>rising | 7 | 100.0 | 8.1072 | 5.5205 | 2.3996 | 15.4344 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | falling>mixed_or_turn>rising | 7 | 71.4286 | 19.3238 | 27.193 | -14.0815 | 46.1217 | 57.1429 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 7 | 28.5714 | 3.0359 | -10.0 | -23.3584 | 38.2626 | 14.2857 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 6 | 66.6667 | 6.9283 | 4.6726 | -21.1335 | 37.2458 | 33.3333 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>consolidation>rising | 6 | 100.0 | 24.4203 | 9.5333 | 3.9848 | 59.7428 | 16.6667 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | falling>falling>rising | 6 | 50.0 | 14.809 | 8.6305 | -21.1746 | 56.9711 | 50.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>consolidation>rising | 6 | 50.0 | -1.1988 | 1.0934 | -12.4789 | 7.789 | 0.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>high_pos_gt75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 5 | 80.0 | 23.1599 | 17.5676 | -0.7316 | 52.4912 | 40.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | mixed_or_turn>mixed_or_turn>rising | 5 | 60.0 | 22.1146 | 9.4017 | -10.428 | 62.7942 | 40.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>mid_pos_40_75 | consolidation>consolidation>consolidation | 5 | 0.0 | -4.3018 | -3.8636 | -5.7663 | -3.2791 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | rising>consolidation>rising | 5 | 60.0 | -1.3812 | 3.6145 | -15.5161 | 10.5588 | 0.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | consolidation>consolidation>rising | 4 | 75.0 | 23.8651 | 13.4652 | 2.4556 | 53.5947 | 25.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 4 | 25.0 | 1.9746 | -10.1267 | -16.7611 | 30.3915 | 25.0 |
| nonchronological_anchor_state_sequence | latest_source_arrived_after_preweek_before_or_on_trigger | labeled_anchor_comparison_not_chronological_latest_source_after_preweek | mid_pos_40_75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 4 | 25.0 | 7.6724 | -3.7912 | -9.4339 | 33.9496 | 25.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>high_pos_gt75>high_pos_gt75 | rising>consolidation>consolidation | 4 | 0.0 | -4.2809 | -3.7489 | -7.4801 | -1.5072 | 0.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | high_pos_gt75>mid_pos_40_75>high_pos_gt75 | rising>rising>rising | 4 | 100.0 | 54.2271 | 60.4107 | 31.5275 | 71.98 | 100.0 |
| chronological_transition | source_before_or_on_preweek | chronological_source_to_preweek_to_confirmation | low_pos_le40>low_pos_le40>high_pos_gt75 | falling>falling>rising | 4 | 100.0 | 25.7775 | 20.5379 | 3.296 | 52.4507 | 50.0 |
