# Daily Volume Breakout Operation Section

- generated_at: `2026-07-09 22:46:06 Asia/Taipei`
- model_id: `volume_range_breakout_v2_low_position_volume_attack,volume_range_breakout_v2_mid_position_momentum_attack`
- source: `daily_candidate_model_signal_log+daily_published_model_snapshots+stock_price_history`
- approval_source: `approved_operation_patterns_latest.csv`
- approved_for_daily: `True`
- approval_version: `volume_range_breakout_v2_formal_operation_20260709`
- source_status: `ready`
- source_rows: `3`
- purpose: production presentation adapter only; PDF/packet 必須讀取本 artifact，且不得重新計算進場、停損、出場或排名。
- sections: confirmed_operation, confirmed_unranked_operation, pending_confirmation, active_operation.

## highlight

### 本日可買 / 已確認買入候選

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 本日無股票推薦         |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無股票推薦           |
|               0 | empty_state | 本日無股票推薦         |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無股票推薦           |

### 已確認但未列買入

| display_order   | row_type   | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level   | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|-----------------|------------|-----------------|--------------|------------------|-----------------|----------------|------------------|---------------|---------------|--------------------|----------------------|---------------------------------------|-----------------------------|---------------------|---------------------|-------------------|

### 待確認

| display_order   | row_type   | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level   | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|-----------------|------------|-----------------|--------------|------------------|-----------------|----------------|------------------|---------------|---------------|--------------------|----------------------|---------------------------------------|-----------------------------|---------------------|---------------------|-------------------|

### 操作中

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 目前無操作中追蹤列       |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前無操作中追蹤列         |
|               0 | empty_state | 目前無操作中追蹤列       |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前無操作中追蹤列         |

## full

### 本日可買 / 已確認買入候選

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 本日無股票推薦         |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無股票推薦           |
|               0 | empty_state | 本日無股票推薦         |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無股票推薦           |

### 已確認但未列買入

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 本日無已確認但未列買入股票   |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無已確認但未列買入股票     |
|               0 | empty_state | 本日無已確認但未列買入股票   |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 本日無已確認但未列買入股票     |

### 待確認

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh           | stop_basis_zh                | exit_rule_zh             | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status    | buy_rank_eligible   | adapter_note_zh                                            |
|----------------:|:------------|:----------------|:-------------|:-------------------------|:-----------------------------|:-------------------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:---------------------|:--------------------|:-----------------------------------------------------------|
|               1 | data        | 6934 心誠鎂        |              | 訊號日後等待隔日續攻收盤確認；未確認前不列買入。 | 待確認成立後才啟動 MA20/EMA23 4日收盤停損。 | 待確認成立後才啟動 D+15 固定收盤出場規則。 | 今日訊號             |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。 |
|               1 | data        | 7823 奧義賽博-KY創   |              | 訊號日後等待隔日續攻收盤確認；未確認前不列買入。 | 待確認成立後才啟動 MA20/EMA23 4日收盤停損。 | 待確認成立後才啟動 D+15 固定收盤出場規則。 | 今日訊號             |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。 |
|               2 | data        | 8929 富堡         |              | 訊號日後等待隔日續攻收盤確認；未確認前不列買入。 | 待確認成立後才啟動 MA20/EMA23 4日收盤停損。 | 待確認成立後才啟動 D+15 固定收盤出場規則。 | 今日訊號             |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | pending_confirmation | False               | 由 v2 正式模型條件與 close-only 確認產生；不使用舊 v1 hidden evidence gate。 |
|               0 | empty_state | 目前無待確認追蹤列       |              |                          |                              |                          |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state          | False               | 目前無待確認追蹤列                                                  |

### 操作中

|   display_order | row_type    | stock_display   | trigger_zh   | entry_basis_zh   | stop_basis_zh   | exit_rule_zh   | pending_age_zh   | sample_size   | win_rate_zh   | median_return_zh   | approved_for_daily   | operation_module_approved_for_daily   | operation_directive_level         | row_action_status   | buy_rank_eligible   | adapter_note_zh   |
|----------------:|:------------|:----------------|:-------------|:-----------------|:----------------|:---------------|:-----------------|:--------------|:--------------|:-------------------|:---------------------|:--------------------------------------|:----------------------------------|:--------------------|:--------------------|:------------------|
|               0 | empty_state | 目前無操作中追蹤列       |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前無操作中追蹤列         |
|               0 | empty_state | 目前無操作中追蹤列       |              |                  |                 |                |                  |               |               |                    | True                 | True                                  | approved_daily_operation_guidance | empty_state         | False               | 目前無操作中追蹤列         |
