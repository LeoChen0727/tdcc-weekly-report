# revenue_unreacted_range PDF consumer v2

## Scope

This is the model-specific PDF consumer for
`revenue_unreacted_range/source_mid_falling v2`. It is a presentation adapter
only. It does not implement, tune, rank, or reselect the monthly-revenue model.
It does not read research artifacts or the legacy generic candidate-signal
surface.

The only allowed operation source is:

`output/latest/daily_revenue_unreacted_range_operation_section_latest.csv`

The implementation is owned by
`scripts/generate_chatgpt_side_daily_reports.py`. The independent source-level
contract validator is
`scripts/validate_revenue_unreacted_range_pdf_consumer_contract.py`, with
behavioral and mutation coverage in
`tests/test_revenue_unreacted_range_pdf_consumer.py`.

The consumer binds these immutable identifiers:

- `operation_module_id=revenue_unreacted_range_source_mid_falling_v2_operation_v2`
- `adapter_schema_version=revenue_unreacted_range_operation_section_schema_v2`
- `lifecycle_contract_version=revenue_unreacted_range_lifecycle_v2`

## Dormant and activation behavior

The consumer remains dormant while both conditions are false:

- `presentation_allowed=True`
- `pdf_integration_status=pdf_integrated_daily_adapter`

In the dormant state it does not require the dedicated artifact and the
existing generic renderer path for `revenue_unreacted_range` is unchanged. A
partial activation, where only one condition is true, fails closed. Once both
are true, the readiness row must also set `formal_model_use_allowed`,
`approved_for_daily`, and `production_allowed` to true, identify the v2 module,
and declare all four adapter sections. Missing or mismatched readiness fails.

After activation the dedicated runtime CSV is mandatory. Missing, empty,
wrong-schema, wrong-module, wrong-lifecycle, disabled-permission, duplicate
display-order, or research/model-signal fallback payloads fail closed.

## Independent rendering contract

The revenue model has model-specific filter, selection, table, and render
functions. It does not reuse the volume, W-bottom, or 23EMA business table
renderers. Shared PDF plumbing remains limited to presentation-neutral helpers
such as `build_table`, typography, spacing, and semantic-manifest serialization.

Highlight PDFs render exactly two main tables, in this order:

1. `本日可買 / 已確認買入候選`: all `confirmed_operation` rows; no fixed cap.
2. `操作中`: at most the first ten `active_operation` rows.

Highlight PDFs never render `confirmed_unranked_operation` or
`pending_confirmation`. Full-list PDFs render all four sections and do not
inherit the highlight active-row cap. The required primary empty states are:

- confirmed: `本日無股票推薦`
- active: `目前無操作中追蹤列`

Rows are filtered by the report line encoded in the dedicated adapter. The PDF
consumer does not infer mainstream/non-mainstream membership from generic
candidate signals.

## Semantic manifest

When dormant, the revenue model is absent from
`chatgpt_daily_pdf_semantic_manifest.csv`. When activated, every revenue row or
empty state in that manifest uses the dedicated artifact path and its canonical
normalized SHA-256. Candidate signals, research outputs, preview artifacts, or
legacy generic rows are forbidden as semantic-manifest sources.

The model remains labeled with its frozen D+2-open entry and D+30-close fixed
exit outcome definition. The consumer does not introduce a stop rule; it only
renders the formal adapter's no-stop disclosure.
