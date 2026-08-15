# Volume V2 Advisory Lineage Refresh V1

Workflow owner lane: `workflow_automation_maintenance`
Existing artifact/build semantics owner: `daily_production`

## Purpose

This maintenance lane repairs stale provenance after an already-approved
historical price-source correction. It does not change a model condition,
score, rank, threshold, selected stock, operation rule, research result, PDF,
packet contract, or production authority surface.

The only executable entrypoint is the manually dispatched, main-only workflow
`.github/workflows/volume_v2_advisory_lineage_refresh.yml`. It requires the
exact current `main` SHA and the literal confirmation token
`refresh_volume_v2_advisory_lineage`. It has no schedule or push trigger and
does not explicitly dispatch another workflow. A successful bounded push
changes three `docs/latest/*` artifacts, so the repository's existing
`pages.yml` push trigger naturally runs its Pages build and deployment. It does
not trigger Daily Full Pipeline, production PDF generation, or Apps Script.

## Bounded mutation contract

The builders may temporarily touch these thirteen existing paths:

1. `output/latest/volume_breakout_watch_latest.csv`
2. `output/latest/volume_breakout_watch_latest.md`
3. `output/latest/volume_breakout_chatgpt_packet_latest.md`
4. `output/latest/volume_attack_theme_layer_latest.csv`
5. `output/latest/volume_attack_theme_layer_latest.md`
6. `output/latest/volume_attack_theme_stocks_latest.csv`
7. `output/latest/volume_attack_theme_stocks_latest.md`
8. `docs/latest/volume_attack_theme_layer_latest.csv`
9. `docs/latest/volume_attack_theme_layer_latest.md`
10. `docs/latest/volume_attack_theme_stocks_latest.csv`
11. `docs/latest/volume_attack_theme_stocks_latest.md`
12. `output/latest/volume_attack_theme_layer_validation_latest.json`
13. `output/latest/volume_attack_theme_layer_validation_latest.md`

Four timestamp-only validation or presentation artifacts are verified and then
restored to their exact base blobs. The two theme-layer CSV mirrors must remain
semantically unchanged. The final commit is therefore exactly seven paths:

- the refreshed watch CSV;
- the output/docs theme-layer Markdown mirrors;
- the output/docs theme-stock CSV mirrors; and
- the output/docs theme-stock Markdown mirrors.

Any missing path, extra path, deletion, rename, mode change, untracked residue,
or non-exact staged set blocks the commit.

## Business parity contract

The watch must retain the same columns, row order, thirteen stock identities,
dates, scores, ranks, prices, volumes, features, labels, and statuses. Only
`advisory_score_source_sha256` may change, and its replacement must pass the
existing independent historical-slice validator.

The theme-stock rows must retain every business field and row order. Only
`advisory_score_source_sha256` and `volume_watch_source_sha256` may change. The
theme-level CSV must remain identical. The output and docs mirrors must be
byte-identical after each write.

The refresh fails before commit if any model-facing value changes. It does not
run Daily Full Pipeline, render PDFs, call Apps Script, change a formal adapter,
or update a revenue-model artifact.

## Publication boundary

The workflow records the exact base SHA, refuses a dirty checkout, stages only
the seven literal paths, rejects remote-main drift, and creates one local
commit. Validators that require a committed artifact revision, including the
legacy theme-layer validator, run after that local commit and before any
publication. Its two generated validation reports must remain byte-identical to
their committed base artifacts; any post-validation residue blocks publication.
Only a clean, fully validated direct-child commit is sent through one non-force
push. A later or concurrent main writer causes the run to fail; the workflow
never rebases or regenerates against moving main.
