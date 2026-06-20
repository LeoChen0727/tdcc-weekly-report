# Event Catalyst Overlay Governance

## Purpose

The event/catalyst overlay contract controls how catalyst and event-calendar fields may be consumed by:

- daily stock recommendation PDFs
- TDCC weekly reports
- individual stock analysis PDFs
- report packets and validation tooling

The first phase is disclosure-only. Catalyst and event fields may be shown as source-backed context, but they must not change score, ranking, upgrade/downgrade state, or formal recommendation reason text.

## Contract File

The source of truth is:

```text
config/event_catalyst_overlay_contract.csv
```

Every row declares one overlay field and its allowed consumer behavior:

- `allowed_effect` must be one of `disclosure_only`, `reason_text_only`, `risk_flag`, `score_overlay`, or `ranking_modifier`.
- Current phase requires `allowed_effect=disclosure_only`.
- Current phase requires `score_allowed=false`, `ranking_allowed=false`, `reason_text_allowed=false`, and `disclosure_only=true`.
- `source_file` must be repo-relative and must not point to legacy date folders or helper copies.
- `degraded_behavior` must explicitly block score, rank, and recommendation reason effects.

## Hard Rules

1. Catalyst or calendar fields cannot affect score or ranking before a reviewed backtest proves the effect.
2. Degraded or stale source rows cannot affect score, ranking, upgrade/downgrade state, or recommendation reasons.
3. PDF renderers cannot convert catalyst context into recommendation reasons on their own.
4. Any score or ranking use requires a separate promotion PR that updates the contract, validator, evidence, and affected consumers together.

## PDF Usage

PDF and report consumers may display contracted fields only as structured disclosure. Acceptable wording should preserve source state, confidence, stale/degraded status, and pending-review status. The PDF layer must not infer stronger investment meaning from a field name such as `catalyst_strength_score`, `event_proximity_score`, `similar_to_shihsinko_flag`, or `catalyst_summary`.

If a PDF needs a reason-text field in the future, the field must first become an upstream structured reason with explicit contract approval. The PDF renderer still cannot invent the reason.

## Promotion Requirements

A promotion PR that allows `score_overlay`, `ranking_modifier`, or `reason_text_only` must include:

- backtest evidence showing the event/catalyst field improves the target model or report outcome
- source-quality rules for stale, degraded, partial, and missing data
- human review approval for the changed effect
- validator updates that keep degraded sources blocked
- affected consumer updates for daily PDF, TDCC weekly, and individual PDF boundaries
- tests or workflow validation proving the new effect is intentional

Research or backtest evidence is advisory until the promotion PR is merged. Research parameters or catalyst effects must not be copied into daily production by default.

## Validation

Run:

```text
python scripts/validate_event_catalyst_overlay_contract.py
python scripts/validate_catalyst_layer.py
```

The overlay contract validator fails if any phase-one field allows scoring, ranking, or recommendation reason text.
