# revenue_unreacted_range/source_mid_falling v2 Daily Operation Section

- Producer owner: daily_model_maintenance.
- Runtime selection inputs: objective monthly revenue, stock price history, and config taxonomy only.
- Active rows additionally require a prior model-owned formal confirmed history row.
- Rule is frozen; forward holdout is post-launch monitoring and cannot tune this producer.

| pdf_view | pdf_section_zh | row_type | report_line | stock_display | operation_status_zh | signal_date | confirmation_date | entry_date | row_action_status | buy_rank_eligible |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full | 操作中 | empty_state | mainstream |  | 目前無操作中追蹤列 |  |  |  | empty_state | False |
| full | 本日可買 / 已確認買入候選 | empty_state | mainstream |  | 本日無股票推薦 |  |  |  | empty_state | False |
| full | 已確認但未列買入 | empty_state | mainstream |  | 目前無已確認但未列入買進排序列 |  |  |  | empty_state | False |
| full | 待確認 | empty_state | mainstream |  | 目前無待確認列 |  |  |  | empty_state | False |
| full | 操作中 | empty_state | non_mainstream |  | 目前無操作中追蹤列 |  |  |  | empty_state | False |
| full | 本日可買 / 已確認買入候選 | empty_state | non_mainstream |  | 本日無股票推薦 |  |  |  | empty_state | False |
| full | 已確認但未列買入 | empty_state | non_mainstream |  | 目前無已確認但未列入買進排序列 |  |  |  | empty_state | False |
| full | 待確認 | data | non_mainstream | 1326 台化 | 待確認 | 20260831 |  |  | pending_confirmation | False |
| highlight | 操作中 | empty_state | mainstream |  | 目前無操作中追蹤列 |  |  |  | empty_state | False |
| highlight | 本日可買 / 已確認買入候選 | empty_state | mainstream |  | 本日無股票推薦 |  |  |  | empty_state | False |
| highlight | 操作中 | empty_state | non_mainstream |  | 目前無操作中追蹤列 |  |  |  | empty_state | False |
| highlight | 本日可買 / 已確認買入候選 | empty_state | non_mainstream |  | 本日無股票推薦 |  |  |  | empty_state | False |
