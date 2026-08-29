# revenue_unreacted_range disabled operation adapter v1

## Scope and status

This contract prepares a model-owned operation schema for
`revenue_unreacted_range/source_mid_falling v2`. It is disabled preparation,
not a production adapter. The module is
`scripts/revenue_unreacted_range_operation_adapter.py` and its immutable IDs
are:

- `operation_module_id=revenue_unreacted_range_source_mid_falling_v2_operation_v1`
- `adapter_schema_version=revenue_unreacted_range_operation_section_schema_v1`
- `lifecycle_contract_version=revenue_unreacted_range_lifecycle_v1`

The module is in-memory only. It has no CLI, writer, runtime artifact,
`output/latest` path, `docs/latest` path, PDF consumer, packet consumer, Daily
Full hook, Apps Script hook, or production hook. A later formal promotion must
use a new append-only contract/version; this v1 preparation must not be mutated
into an approved adapter.

The required permissions remain fixed:

```text
formal_model_use_allowed=False
approved_for_daily=False
presentation_allowed=False
production_allowed=False
```

`operation_directive_level` remains `no_operation_directive`. No row from this
module is a formal buy, sell, stop-loss, exit, or profit-taking instruction.

## Fixed model and operation semantics

The selected model and thresholds are frozen. This adapter cannot add a
condition, change a threshold, reselect the sample, or use forward-holdout
observations to tune the model.

The module binds
`rule_spec_id=revenue_unreacted_range_source_mid_falling_d30_v1` and canonical
rule SHA-256
`1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633`.
That rule keeps the preselected monthly-revenue gate, `40 < position_120d_pct <=
75`, `shape_return20_pct < -5`, `shape_ema23_slope5_pct < 0`, the registered
0..60 trading-day source-to-trigger window, and the registered close-confirmed
price trigger unchanged. `selection_policy=fixed_preselected_no_reselection`
and `holdout_use_policy=natural_maturity_observation_only_no_tuning` are part of
every disabled empty row.

The operation timing contract is fixed:

- confirmation: `D+1_analysis_close>trigger_analysis_close`
- entry: `D+2_analysis_open`
- exit: `D+30_analysis_close_offset29`
- holding contract: 30 trading sessions including entry, exit index offset 29
- stop: `none_no_stop_reference`
- price semantics: close-only confirmation and fixed future close exit; no
  intraday high/low trigger, stop, exit, win, failure, or realized return

The fundamental boundary is monthly revenue only. EPS, gross margin, operating
margin, operating income, non-operating income, net income, and quarterly or
annual financial-statement fields are forbidden as conditions, scores,
rankings, promotion evidence, or adapter fields.

## Disabled empty state

The preparation returns exactly eight deterministic in-memory rows: two report
lines (`mainstream`, `non_mainstream`) times four lifecycle sections. All rows
have `row_type=empty_state`, no stock or operation identity, and the following
exact text:

| section | empty text |
| --- | --- |
| `pending_confirmation` | `目前無待確認列` |
| `confirmed_operation` | `本日無股票推薦` |
| `confirmed_unranked_operation` | `目前無已確認但未列入買進排序列` |
| `active_operation` | `目前無操作中追蹤列` |

The empty rows are a schema-validation fixture only. They are not written to a
runtime artifact and are not available to any renderer.

## Lifecycle invariants

`scripts/validate_revenue_unreacted_range_operation_adapter.py` validates the
disabled module and intentionally rejects `--phase production-approval`.
In-memory lifecycle validation enforces:

1. exact schema and unique report-line/section identity;
2. empty and data rows cannot coexist in disabled preparation;
3. an `active_operation` must descend from that same operation's prior selected
   `confirmed_operation`;
4. `confirmed_unranked_operation` can never become active;
5. the same stock and report line cannot have overlapping operations or a new
   confirmation before the prior operation exits;
6. lifecycle dates and states are monotonic, and an exited operation cannot be
   revived;
7. a same-stock re-entry confirmation must occur after, not on, the prior exit
   date;
8. every non-empty lifecycle validation must receive an explicit point-in-time
   trading-calendar sequence, and confirmation, entry, and fixed exit must be
   exactly D+1, D+2, and the 30th holding session (entry index +29);
9. the same stock, report line, and date cannot appear in both selected and
   unranked confirmation sections, even when operation keys differ.

These checks prepare the formal boundary without claiming that a daily adapter
or operation artifact exists.
