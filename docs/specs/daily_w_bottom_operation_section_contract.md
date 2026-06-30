# Daily W-Bottom Operation Section Contract

Owner lane: `daily_model_maintenance`

Producer:

```text
python scripts/build_daily_w_bottom_operation_sections.py
```

Validator:

```text
python scripts/validate_daily_w_bottom_operation_sections.py
```

## Scope

This contract covers only the two formal W-bottom daily operation models:

| model_id | meaning | output artifact |
|---|---|---|
| `w_bottom_right_side` | W-bottom right-low early entry | `output/latest/daily_w_bottom_right_side_operation_section_latest.csv` |
| `neckline_volume_breakout_confirmation` | W-bottom neckline volume breakout confirmation | `output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv` |

These adapters do not change production model conditions, scoring, or ranking.
They translate already-approved model signals into model-owned operation rows
that PDF renderers may consume.

## PDF Views

Digest/highlight PDFs may render only these sections:

```text
confirmed_operation
active_operation
```

Full-list PDFs may render the same two sections. A future `pending_confirmation`
section needs a separate model contract update before it can appear in full-list
PDFs.

Empty-state rows are part of the table:

| section | empty-state text |
|---|---|
| `confirmed_operation` | `本日無股票推薦` |
| `active_operation` | `目前無操作中追蹤列` |

Do not create a separate standalone `本日無股票推薦` section.

## Approved PDF Consumer Fields

PDF renderers may read these fields directly:

```text
model_id
model_name_zh
pdf_view
pdf_section
pdf_section_zh
row_type
operation_asof_date
report_line
report_line_memberships
display_order
stock_id
stock_name
stock_display
operation_status_zh
quality_status_zh
row_action_status
buy_rank_eligible
signal_date
entry_basis_zh
entry_date
entry_price
entry_price_status_zh
stop_loss_price
stop_loss_label_zh
stop_basis_zh
exit_rule_zh
planned_holding_days
operation_age_days
risk_tags_zh
tdcc_status_zh
sample_size
win_rate_zh
avg_return_zh
median_return_zh
pdf_note_zh
adapter_note_zh
```

The PDF renderer must not recompute:

- buy eligibility;
- active lifecycle;
- stop-loss state;
- exit state;
- `new` versus `repeated` as the main table structure.

`same_model_repeat_*` information may remain a supporting label elsewhere, but
it is not the operation-table structure for these models.

## Lifecycle Source

The adapter uses:

```text
daily_candidate_model_signal_log
daily_published_model_snapshots
production_w_bottom_detector
stock_price_history
approved_operation_patterns_latest.csv
```

It must not use raw `output/latest/research_backtest/*detail*` rows as
production lifecycle rows. Research detail rows remain advisory unless a later
promotion PR explicitly changes the production contract.

## Model-Specific Rules

`w_bottom_right_side`:

```text
entry_rule_id=right_low_signal_next_open
stop_loss_rule_id=w_structure_low_close_stop
exit_rule_id=d20_gain10_else_d40_close
planned_holding_days=40
```

`neckline_volume_breakout_confirmation`:

```text
entry_rule_id=close_ge_1pct_within_3_sessions_next_open
stop_loss_rule_id=no_fixed_stop_loss_20d_operation_rule
exit_rule_id=tp10_close_win_5pct_pullback_neutral_else_20d_close_loss
planned_holding_days=20
```

## Forbidden

- Do not let the PDF renderer infer W-bottom operation rows from candidate
  signal rows.
- Do not merge `w_bottom_right_side` and
  `neckline_volume_breakout_confirmation` semantics.
- Do not write research variants into the production baseline.
- Do not change model condition, scoring, or ranking in this adapter contract.
