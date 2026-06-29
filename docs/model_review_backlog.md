# Model Review Backlog

This backlog is the human-review queue for model surfaces listed in
`config/model_surface_registry.csv`.

It is not a tuning recommendation and does not change production model
conditions, scoring, ranking, PDF layout, or research baselines.

The breakout-related model review is now grouped by shared business meaning in
`docs/specs/breakout_model_taxonomy_governance_handoff.md`. That handoff keeps
`volume_range_breakout` as the current production baseline while
`w_bottom_right_side` and the formal `neckline_volume_breakout_confirmation`
surface remain active production review items. The current
`neckline_volume_breakout_confirmation` v1 surface is explicitly the W-bottom
neckline subtype only; inverse head-and-shoulders, triple bottom, and other
structured neckline subtypes are not mixed into this model. `near_high_neckline_challenge`
and `platform_strengthening` are now deprecated daily production surfaces kept
only for historical audit/research reference.

## How To Use This Backlog

Review means deciding business logic and boundaries, not reviewing code.

For each surface, the owning conversation should answer:

- Is this surface correctly classified?
- Is it allowed to affect stock entry, TDCC weekly ranking, PDF display, or
  disclosure only?
- Does research/backtest evidence match the production surface?
- If not, should the next step be research synchronization, a promotion PR, or
  no production change?

Do not copy research variants into production. Production model changes require
an explicit promotion/sync PR.

## Priority Summary

High-priority manual review:

- Breakout model group: review active models `neckline_volume_breakout_confirmation`,
  `w_bottom_right_side`, and `volume_range_breakout` together before any further
  production tuning.
- `neckline_volume_breakout_confirmation`: formal production code, contract,
  tests, approved operation evidence, and research/backtest parity now exist.
  It is the active W-bottom confirmed-breakout surface replacing the deprecated
  `near_high_neckline_challenge` and `platform_strengthening` daily production
  entries for this subtype only. Other neckline pattern families remain backlog
  work and must not be silently added to this model.
- `descending_resistance_volume_breakout`: keep as a separate future model
  family for descending swing-high resistance-line breakouts. Do not mix this
  with bottom-pattern neckline breakouts.
- `w_bottom_right_side`: keep as a pre-breakout / second-bottom formation
  surface. Its production condition now requires second-arc average volume to
  exceed the first-arc baseline. The same volume-quality rule applies to
  `neckline_volume_breakout_confirmation` for W-bottom neckline breakouts.
  The current early-entry operation and PDF evidence rule is documented in
  `docs/specs/w_bottom_right_side_early_entry_operation_spec.md`.
- `revenue_unreacted_range`: research proxy is broad, so proxy stats must not be
  used directly for production tuning.
- `tdcc_short_term_continuation_d5_d10`: only TDCC-weekly-approved stock model,
  so consumer expansion requires independent review.
- `tdcc_weekly_ranking_formula`: TDCC weekly ranking model, not a stock entry
  model; keep the weekly ranking and buy-signal boundary explicit.
- `group_fund_rotation`: theme-level fund-flow model, not an individual stock
  model; pending backtest optimization.

Medium-priority manual review:

- `price_pullback_23ema`
- `hot_theme_pullback`
- `w_bottom_right_side`
- `pullback_short_reclaim`
- `tdcc_stealth_accumulation`

Low-priority / monitor:

- `volume_range_breakout`
- `event_catalyst_overlay`

## Surface Review Queue

| surface_id | type | owning lane | production stock entry signal | TDCC approved | research parity status | next conversation / lane | priority manual review | next step |
|---|---|---|---|---|---|---|---|---|
| `volume_range_breakout` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `ok` | `daily_model_maintenance`; `research_backtest` only if new evidence appears | low | Keep as current stock contract baseline. Review only if production behavior changes or new research evidence proposes promotion. |
| `price_pullback_23ema` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `warning_research_variant_only` | `research_backtest` first; `daily_model_maintenance` only for explicit promotion/sync PR | medium | Compare advisory research variant to production baseline. Do not tune production from advisory output without promotion evidence. |
| `hot_theme_pullback` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `warning_research_variant_only` | `research_backtest` first; `daily_model_maintenance` only for explicit promotion/sync PR | medium | Confirm whether theme-related research variants are true improvements or only exploratory alternatives. |
| `revenue_unreacted_range` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `warning_research_variant_only` | `research_backtest` first, then `daily_model_maintenance` if promotion is approved | high | Review revenue proxy width and data completeness. Current proxy is too broad for direct production tuning. |
| `w_bottom_right_side` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `ok` | `daily_model_maintenance` owns approved operation v2; `research_backtest` only if new evidence proposes a future change | low | Treat as the second approved daily operation model after `volume_range_breakout`. PDF title evidence uses the approved operation v2 D+20/D+40 structure-stop statistics; raw research variants remain advisory-only unless separately promoted. |
| `neckline_volume_breakout_confirmation` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `ok` | `daily_model_maintenance` owns approved operation v1; `research_backtest` only if new evidence proposes a future change | low | Treat as the active W-bottom neckline confirmed-breakout daily operation model. 45-day context is the entry gate; 90-day context is score/risk adjustment only. It does not include inverse head-and-shoulders, triple bottom, or structured-bottom-other subtypes. |
| `near_high_neckline_challenge` | `stock_entry_model` | `daily_model_maintenance` | deprecated for daily | no | `warning_research_variant_only` | no active tuning lane; historical audit only unless explicitly reactivated | low | Deprecated from daily production after `neckline_volume_breakout_confirmation` became the formal confirmed-breakout model. The old sign-semantics blocker remains historical context, not a tuning backlog item. |
| `platform_strengthening` | `stock_entry_model` | `daily_model_maintenance` | deprecated for daily | no | `warning_research_variant_only` | no active tuning lane; historical audit only unless explicitly reactivated | low | Deprecated from daily production after `neckline_volume_breakout_confirmation` became the formal confirmed-breakout model. Keep for historical audit/research reference only. |
| `pullback_short_reclaim` | `stock_entry_model` | `daily_model_maintenance` | yes | no | `warning_research_variant_only` | `research_backtest` first; `daily_model_maintenance` only for explicit promotion/sync PR | medium | Review reclaim signal definitions and evidence before any production threshold change. |
| `tdcc_stealth_accumulation` | `tdcc_stock_entry_model` | `daily_model_maintenance` | yes | no | `warning_research_variant_only` | `research_backtest` first; `daily_model_maintenance` only for explicit promotion/sync PR | medium | Keep separate from TDCC weekly approval. Review only as a daily stock entry model unless consumer approval changes. |
| `tdcc_short_term_continuation_d5_d10` | `tdcc_specialty_stock_model` | `daily_model_maintenance` | yes | yes | `warning_research_variant_only` | `daily_model_maintenance` for contract ownership; `research_backtest` for parity; `tdcc_weekly_report` for consumer impact | high | Keep as the only TDCC-weekly-approved stock model. Any expansion or scoring change needs contract and parity review. |
| `tdcc_weekly_ranking_formula` | `tdcc_weekly_ranking_model` | `tdcc_weekly_report` | no | yes | `research_backtest_advisory_only` | `tdcc_weekly_report` for report ranking; `research_backtest` for ranking backtest; `model_governance` for classification | high | Review TDCC weekly ranking as a report-ranking model. Do not treat it as a stock entry or buy-signal model. |
| `group_fund_rotation` | `theme_fund_rotation_model` | `daily_model_maintenance` | no | no | `pending_backtest_optimization` | `daily_model_maintenance` for theme model contract; `research_backtest` for optimization evidence; `pdf_layout_maintenance` only for display | high | Create a theme-level contract before tuning. Keep it out of `stock_model_contract_registry.csv`. |
| `event_catalyst_overlay` | `event_catalyst_overlay_surface` | `event_catalyst_maintenance` | no | yes | `disclosure_only_not_ranked` | `event_catalyst_maintenance` for contract/source changes; `model_governance` only if promotion is requested | low | Keep disclosure-only. Scoring or ranking use requires explicit contract and backtest promotion. |

## Recommended Execution Order

1. Breakout model group: use
   `docs/specs/breakout_model_taxonomy_governance_handoff.md` to define the
   taxonomy layer, breakout event feature layer, and stock-entry model layer
   before changing production code.
2. `neckline_volume_breakout_confirmation`: keep as the active W-bottom
   neckline confirmed-breakout model. Future work should tune only with new
   evidence and a formal model-change PR. Other neckline pattern families
   require separate research and promotion before production use.
3. `w_bottom_right_side`: keep as the W-bottom pre-breakout / second-bottom
   formation model. It is now the second approved daily operation model after
   `volume_range_breakout`; use
   `docs/specs/w_bottom_right_side_early_entry_operation_spec.md` for the
   current early-entry buy point, W-structure-low stop, D+20/D+40 exit rule,
   and PDF evidence rule before any future production or daily PDF change.
4. `revenue_unreacted_range`: narrow or validate the research proxy before any
   parameter discussion.
5. `group_fund_rotation`: create a theme-level contract and backtest plan.
6. `tdcc_weekly_ranking_formula`: document TDCC weekly ranking boundaries and
   keep it separate from stock entry models.
7. `tdcc_short_term_continuation_d5_d10`: review TDCC weekly consumer impact
   before any consumer expansion.
8. Remaining `warning_research_variant_only` stock models: handle through
   research parity or explicit promotion/sync PRs.
