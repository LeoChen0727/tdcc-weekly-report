# Daily Volume Breakout Operation Section

- generated_at: `2026-07-08 19:58:40 Asia/Taipei`
- model_id: `volume_range_breakout`
- source: `daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history`
- approval_source: `approved_operation_patterns_latest.csv`
- approved_for_daily: `True`
- approval_version: `volume_breakout_operation_v1_20260615`
- source_status: `ready`
- source_rows: `24`
- purpose: production presentation adapter only; PDF/packet 必須讀取本 artifact，且不得重新計算進場、停損、出場或排名。
- sections: confirmed_operation, confirmed_unranked_operation, pending_confirmation, active_operation.

## highlight

### 已確認操作

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh      |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:---------------------|
|               0 | empty_state | 目前無資料           |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前沒有符合研究證據門檻的已確認操作列。 |

### 已確認但未通過買入排名門檻

| display_order   | row_type   | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level   | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|-----------------|------------|-----------------|--------------|------------------|-----------------|----------------|------------------|---------------|---------------|--------------------|----------------------|---------------------------------------|-----------------------------|---------------------|---------------------|-------------------|

### 待確認

| display_order   | row_type   | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level   | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|-----------------|------------|-----------------|--------------|------------------|-----------------|----------------|------------------|---------------|---------------|--------------------|----------------------|---------------------------------------|-----------------------------|---------------------|---------------------|-------------------|

### 操作中

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 目前無資料           |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前沒有操作中追蹤列。       |

## full

### 已確認操作

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh      |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:---------------------|
|               0 | empty_state | 目前無資料           |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前沒有符合研究證據門檻的已確認操作列。 |

### 已確認但未通過買入排名門檻

|   display_order | row_type   | stock_display   | trigger_zh   | entry_basis_zh       | stop_basis_zh   | exit_rule_zh   | pending_age_zh   |   sample_size | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status        | buy_rank_eligible   | adapter_note_zh              |
|----------------:|:-----------|:----------------|:-------------|:---------------------|:----------------|:---------------|:-----------------|--------------:|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:-------------------------|:--------------------|:-----------------------------|
|               2 | data       | 8421 旭源         | 隔日突破訊號高點     | 已確認但未通過買入排名門檻，不列進場價。 | 未列買入排名，不列停損價。   | 未列買入排名，不列出場規則。 |                  |           481 | 38.67%        | -3.14%             | True                 | True                                  | approved_daily_operation_guidance | confirmed_not_buy_ranked | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               3 | data       | 6703 軒郁         | 回測 5 日線後站回   | 已確認但未通過買入排名門檻，不列進場價。 | 未列買入排名，不列停損價。   | 未列買入排名，不列出場規則。 |                  |           186 | 42.47%        | -1.19%             | True                 | True                                  | approved_daily_operation_guidance | confirmed_not_buy_ranked | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               4 | data       | 8261 富鼎         | 回測 5 日線後站回   | 已確認但未通過買入排名門檻，不列進場價。 | 未列買入排名，不列停損價。   | 未列買入排名，不列出場規則。 |                  |            20 | 45.00%        | -1.50%             | True                 | True                                  | approved_daily_operation_guidance | confirmed_not_buy_ranked | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               7 | data       | 2511 太子         | 回測 5 日線後站回   | 已確認但未通過買入排名門檻，不列進場價。 | 未列買入排名，不列停損價。   | 未列買入排名，不列出場規則。 |                  |           284 | 40.49%        | -1.28%             | True                 | True                                  | approved_daily_operation_guidance | confirmed_not_buy_ranked | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               9 | data       | 2208 台船         | 回測 5 日線後站回   | 已確認但未通過買入排名門檻，不列進場價。 | 未列買入排名，不列停損價。   | 未列買入排名，不列出場規則。 |                  |           800 | 37.00%        | -2.05%             | True                 | True                                  | approved_daily_operation_guidance | confirmed_not_buy_ranked | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |

### 待確認

|   display_order | row_type   | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   |   sample_size |   win_rate_zh | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status    | buy_rank_eligible   | adapter_note_zh              |
|----------------:|:-----------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|--------------:|--------------:|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:---------------------|:--------------------|:-----------------------------|
|               1 | data       | 2395 研華         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               1 | data       | 4160 訊聯基因       |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+1 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               1 | data       | 4541 晟田         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+5 待確認          |          3059 |         44.34 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               1 | data       | 6637 醫影         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               2 | data       | 1796 金穎生技       |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               2 | data       | 3022 威強電        |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               2 | data       | 3066 李洲         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+1 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               3 | data       | 2061 風青         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               3 | data       | 2601 益航         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               3 | data       | 8930 青鋼         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+1 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               4 | data       | 6612 奈米醫材       |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+1 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               4 | data       | 6901 鑽石投資       |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               5 | data       | 2645 長榮航太       |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+5 待確認          |          3059 |         44.34 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               5 | data       | 6712 長聖         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | 今日訊號             |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               5 | data       | 6907 雅特力-KY     |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+2 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|               9 | data       | 1709 和益         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+5 待確認          |          3059 |         44.34 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|              12 | data       | 1326 台化         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+3 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|              18 | data       | 4911 德英         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+3 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |
|              23 | data       | 1409 新纖         |              | 尚未確認，不列進場價       | 尚未確認，不列停損價      | 待確認後才顯示操作規則    | D+3 待確認          |          3101 |         44.46 |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由已發布模型快照與價格資料重建 D0-D10 操作狀態。 |

### 操作中

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 目前無資料           |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前沒有操作中追蹤列。       |
