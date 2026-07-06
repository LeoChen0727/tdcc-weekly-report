# Daily PDF Shared Path Isolation Audit

Scope: ChatGPT-side daily PDF renderer, formal stock model operation adapters, operation section tables, and table drawing helpers.

This audit does not change stock model conditions, scoring, ranking, buy/sell rules, research/backtest baselines, or PDF visual design.

## Result

The shared path inventory is now machine-readable:

- `config/daily_pdf_shared_path_inventory.csv`

The validator is:

- `scripts/validate_daily_pdf_shared_path_isolation.py`

The validator fails closed when a PDF operation-like renderer function is not registered, when an operation-named helper is missing from the inventory, when semantic-manifest operation helpers are missing from the inventory, when a low-level shared function owns business semantics, when a model-specific operation renderer calls another model's frame/filter/table path, or when stock PDF builders bypass the operation dispatcher.

## Allowed Shared Paths

Only low-level PDF utilities are allowed to be shared across PDF outputs and models:

- `table_para`
- `build_table`
- `write_pdf`

These functions may format paragraphs, construct a table from caller-supplied rows/columns, or write a PDF file. They must not choose model sections, report line, row limits, ranking, stock lifecycle, operation state, or business wording.

The validator checks these helpers for business tokens such as `model_id`, `stock_id`, `pdf_section`, `report_line`, `buy_rank_eligible`, `operation_status`, and model constants. If any low-level helper starts using those tokens, it must be split or reclassified before merge.

## Business-Semantic Paths

The following classes are business-semantic and must stay explicitly owned:

- Report-specific PDF builders:
  - `build_mainstream_curated_pdf`
  - `build_non_mainstream_curated_pdf`
  - `build_mainstream_full_candidate_pdf`
  - `build_non_mainstream_full_candidate_pdf`
  - `build_warrant_market_auxiliary_pdf`
  - `build_market_risk_background_pdf`
- Model-specific operation frames, filters, row limits, renderers, and tables.
- Model-specific operation labels and wording helpers.
- Report-specific operation representative/page builders.
- Shared operation summary and semantic-manifest contract helpers.
- The guarded operation dispatcher:
  - `render_model_operation_section_if_applicable`

The dispatcher may route by explicit `model_id` only. It must not infer lifecycle rows, build tables directly, or convert candidate signal rows into operation rows.

## Fix Applied

`price_pullback_23ema` no longer calls the W-bottom line filter. It now has its own line matcher/filter path:

- `price_pullback_operation_row_matches_line`
- `filter_price_pullback_operation_rows_for_line`

This keeps the 23EMA operation renderer independent from the W-bottom operation renderer while preserving the same report-line membership behavior.

## Remaining Rule

Future daily PDF or model operation changes must update the inventory when adding or renaming any function that contains operation semantics, including old or compatibility code paths. A helper is not safe just because it is old. If it can affect model rows, operation state, section placement, table wording, semantic manifest rows, or report-line routing, it must be registered, split, or removed after owner/dependency audit.

At minimum, update the inventory when adding or renaming any function that matches these operation-like surfaces:

- `build_*_operation_table`
- `render_*operation_section`
- `*_operation_frame`
- `filter_*operation_rows_for_line`
- `limit_*operation_rows_for_pdf_view`
- `*_operation_row_matches_line`
- any function name containing `operation`
- semantic manifest helpers that write or select operation rows

Adding a model-owned operation adapter is not enough. The renderer path must also be registered and validated so changing model A cannot silently change model B.
