# Individual PDF Contract Consumer Governance

## Purpose

Individual stock PDFs are consumers of formal model and event/catalyst data. They
may present approved structured artifacts, but they must not create independent
stock-selection, scoring, ranking, recommendation-reason, or buy/sell judgment
rules in the PDF layer.

This governance is enforced by:

```text
python scripts/validate_individual_pdf_contract_consumers.py
```

## Required Contracts

Individual PDF consumers must use these contracts:

```text
config/stock_model_contract_registry.csv
config/event_catalyst_overlay_contract.csv
```

`conversation_role=individual_pdf_report` must also remain registered in:

```text
C:\Users\p4693\Documents\Codex\projects\taiwan-stock-recommendation\docs-and-workflow\conversation_lane_registry.csv
```

## Model Consumer Rules

- Every explicit `model_id` used by individual PDF outputs must exist in
  `stock_model_contract_registry.csv`.
- A model may be consumed by individual PDFs only when
  `approved_for_individual_pdf=true`.
- Missing approval is not implicit approval.
- Individual PDFs may display prepared source fields, but they must not define
  new model conditions, score functions, ranking weights, or promotion rules.

## Event And Catalyst Consumer Rules

- Every event/catalyst field used by the individual PDF consumer must exist in
  `event_catalyst_overlay_contract.csv`.
- A field may be consumed only when `approved_for_individual_pdf=true` and
  `allowed_consumers` includes `individual_pdf`.
- `disclosure_only=true` fields may be disclosed as source context only.
- `score_allowed=false` fields must not affect scores.
- `ranking_allowed=false` fields must not affect ordering.
- `reason_text_allowed=false` fields must not be converted into recommendation
  strengthening reasons.
- Degraded fields whose `degraded_behavior` includes `no_reason` must not be
  used to strengthen recommendation text.

## PDF Layer Boundary

The individual PDF layer must not define private `pdf_side_*` scoring, ranking,
recommendation, or buy/sell judgment rules. It must also not consume:

- daily stock recommendation official PDF outputs under
  `chatgpt_side_outputs_official`;
- TDCC weekly report PDF outputs;
- research/backtest recommendation outputs;
- retired helper copies or random date-folder outputs.

The current report language boundary is:

- `ACTION_DISPLAY` is the PDF-visible report language contract.
- `ACTION_DECISION` is internal model context and must not be printed as raw
  field names or raw values in investor-facing PDF prose.

## Validation Command Set

For this consumer boundary, run:

```text
python scripts/validate_individual_pdf_contract_consumers.py
python scripts/validate_individual_stock_outputs.py --all
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_event_catalyst_overlay_contract.py
python scripts/validate_tdcc_report_contract_consumers.py
python scripts/validate_daily_production_boundaries.py
python -m pytest tests/test_individual_pdf_contract_consumers.py tests/test_individual_stock_outputs.py -q
```

The ideal individual PDF boundary change does not modify TDCC weekly report
logic, daily stock recommendation model/ranking logic, or research/backtest
parameters.
