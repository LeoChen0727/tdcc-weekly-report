# Daily PDF Contract Consumer Governance

The six official ChatGPT-side daily PDFs are consumers of the repository stock
model and event/catalyst contracts. They may render contract-approved model and
catalyst fields, but the PDF layer must not create private scoring, ranking,
buy/sell judgment, or recommendation-reason rules.

## Required Contracts

- `config/stock_model_contract_registry.csv`
- `config/event_catalyst_overlay_contract.csv`

The daily PDF consumer validator is:

```text
python scripts/validate_daily_pdf_contract_consumers.py
```

The validator is required in `.github/workflows/daily_full_pipeline.yml`.
Unit coverage is:

```text
python -m pytest tests/test_daily_pdf_contract_consumers.py -q
```

## Model Contract Rule

Every `model_id` consumed by the daily PDF report-ready model sources must exist
in `config/stock_model_contract_registry.csv` and must have:

```text
approved_for_daily_pdf=true
```

The daily PDF renderer may display program-side fields such as `model_score`,
`model_rank`, and `display_rank`. It must not define a separate PDF-side model
allowlist, scoring function, ranking formula, buy/sell judgment, or selection
reason that bypasses the registry.

Model promotions that make an operation-oriented model visible in the daily PDF
must satisfy the model-change rule in `AGENTS.md` and
`docs/stock_model_contract_governance.md`: the model lane must provide a formal
daily operation-row adapter contract or approved equivalent before the PDF layer
can render buyable or active lifecycle rows. Registry approval alone does not
authorize the PDF renderer to infer lifecycle rows from candidate signal rows,
research/backtest variants, or advisory recommendation artifacts.
The formal daily operation-row adapter contract is required before rendering.
Registry approval alone does not authorize the PDF renderer to infer lifecycle
rows from candidate signal rows, research/backtest variants, or advisory
recommendation artifacts.

## Stable Daily Stock Model Table Rule

Daily stock model sections in the mainstream and non-mainstream recommendation
PDFs must use a stable, complete model roster from report-ready registry and
readiness sources, not only the models that have candidate rows on the current
report date.

The renderer must treat `output/latest/daily_report_model_registry_latest.csv`,
`config/stock_model_contract_registry.csv`,
`output/latest/model_operation_readiness_latest.csv`, and
`output/latest/daily_candidate_model_signals_for_report_latest.csv` as separate
consumer inputs:

- registry / contract / readiness sources decide which PDF-eligible or
  presentation-allowed models must be displayed;
- `daily_candidate_model_signals_for_report_latest.csv` supplies candidate
  rows only;
- an empty candidate set must not remove a model section from the PDF.

For every applicable mainstream or non-mainstream stock PDF, each active
PDF-eligible or presentation-allowed model must render a fixed model block and
table. If the model has zero candidate rows for that report line on the report
date, the table must still be present using the existing business-facing
candidate/operation table style and must include the exact text:

```text
本日無股票推薦
```

This is a presentation and contract rule only. It must not create synthetic
candidate rows, alter stock model conditions, change model scoring or ranking,
promote research variants, or write research/backtest recommendations into the
production baseline.

The PDF must not add a separate technical model status, readiness,
candidate-count, or PDF integration summary table. Registry/readiness fields are
allowed as renderer inputs for deciding the stable roster, but not as standalone
PDF-facing technical diagnostics.

For operation-oriented daily stock models, the digest / highlight PDF model
block must use the same two-table presentation contract as the
`volume_range_breakout` operation section:

1. The first main table is `本日可買 / 已確認買入候選`.
2. The second main table is `操作中`.
3. The first table must contain the `本日無股票推薦` empty-state row when the
   model has no buyable / confirmed buy candidates for that report line.
4. The second table must contain `目前無操作中追蹤列` when there are no active
   operation rows.
5. Digest / highlight model blocks must not use `待確認`, `已失效`, or `已出場`
   as main tables. `待確認` may appear only in the full-list PDF when the model's
   formal adapter provides that state. `已失效` and `已出場` stay in
   audit/lifecycle artifacts and must not be promoted into PDF main tables.

`w_bottom_right_side` and `neckline_volume_breakout_confirmation` now have
formal model-owned PDF operation section adapters and must be rendered from
their dedicated artifacts:

```text
output/latest/daily_w_bottom_right_side_operation_section_latest.csv
output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv
```

The PDF renderer may consume those rows only after
`model_operation_readiness_latest.csv` reports
`pdf_integration_status=pdf_integrated_daily_adapter` and the adapter provides
both `confirmed_operation` and `active_operation` sections. The PDF layer must
fail closed on missing artifacts or missing required columns and must not fall
back to candidate signal rows to infer lifecycle state.

Formal operation adapters must also enforce lifecycle monotonicity before the
PDF layer reads them:

- The same stock must not appear in both `confirmed_operation` and
  `active_operation` for the same model/report line/PDF view on the same
  operation date.
- An existing active position suppresses a new same-stock confirmed row until
  that position exits; the suppression must be recorded in the adapter audit.
- An `active_operation` row must be backed by a prior model-owned buy-ranked
  confirmed row. Historical rows that were not buy-ranked on their confirmation
  date must not be re-promoted into active tracking by newer context.

Future operation-oriented stock models must follow this presentation contract
when their formal PDF operation adapters are wired; do not invent operation
lifecycle rows in the PDF layer before such an adapter exists.

Daily PDF rendering must also emit `chatgpt_daily_pdf_semantic_manifest.csv`.
This manifest is the machine-readable row-level contract for official daily PDF
operation-model sections. For every rendered operation row it must record the
PDF role, PDF view, report line, model id, PDF section, rendered row type,
stock id, source artifact, and source hash. Validators must compare this
manifest with golden semantic cases for known incident dates before a PR or
main run can be treated as complete.

Legacy preview artifacts and preview builders such as
`volume_breakout_operation_pdf_preview` may remain in another owner lane only
while they are still registered and workflow-owned there. They must not be used
as formal daily PDF operation-row sources, runtime manifest sources, or
semantic manifest sources. Removal of such legacy code or artifacts requires
the owning lane to remove its workflow, inventory, validator, and spec
dependencies in the same cleanup PR.

## Event / Catalyst Contract Rule

Every event or catalyst field consumed from daily report sources must exist in
`config/event_catalyst_overlay_contract.csv` and must have:

```text
approved_for_daily_pdf=true
daily_pdf in allowed_consumers
```

Phase-one event/catalyst fields are disclosure-only. Unless a future reviewed
contract explicitly promotes the field:

- `disclosure_only=true` fields must not affect daily PDF ranking or score.
- `score_allowed=false` fields must not enter daily PDF score calculation.
- `ranking_allowed=false` fields must not affect daily PDF ordering.
- `reason_text_allowed=false` fields must not become recommendation,
  strengthening, or selection-reason text.
- degraded event/catalyst sources must not strengthen recommendation reasons.

## Research Boundary

Research/backtest recommendations may be carried as advisory evidence only when
the production model layer preserves promotion and visibility guards. The daily
PDF renderer and official entrypoint must not read research recommendation
outputs directly, and research recommendations must not be written back into the
production baseline without an explicit promotion PR.

## Current Consumer State

The validator reports the current daily PDF model IDs and catalyst/event fields
from the checked-in latest report sources. At the time this contract consumer
gate was added, the active daily PDF model IDs were:

```text
hot_theme_pullback
price_pullback_23ema
pullback_short_reclaim
tdcc_short_term_continuation_d5_d10
volume_range_breakout
w_bottom_right_side
```

The daily candidate source currently exposes contract-approved catalyst/event
fields from `output/latest/all_candidates_latest.csv`. The validator prints the
exact field list on every run and fails closed if an unapproved field appears or
if a disclosure-only field is used in score, ranking, or reason context.
