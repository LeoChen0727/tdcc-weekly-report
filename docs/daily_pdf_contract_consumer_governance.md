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
