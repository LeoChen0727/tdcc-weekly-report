# Diagnostic Stale Artifact Review - 20260621

Source inventory: `config/output_latest_artifact_inventory.csv`

Filter: `classification=diagnostic_stale_candidate`

Scope: daily-production review of 18 diagnostic/stale CSV/MD artifacts. This review does not process `unknown`, `individual_stock`, `research_backtest`, `tdcc_weekly`, or daily market PDF artifacts. It does not change daily six-PDF stock selection, ranking, scoring, or buy/sell logic.

## Summary

- Reviewed artifacts: 18
- Relocated to `output/latest/diagnostics/`: 2
- Permanent deletes: 0
- Root compatibility aliases retained: 0 for relocated files
- Root diagnostic aliases kept because daily or repair workflows still write/stage them: 9
- Same-family root debug alias kept because another root MD links to it: 1
- Marked for research/backtest lane follow-up due producer/workflow evidence: 6
- Tracked root diagnostic artifacts relocated by this PR: 2
- Filesystem `output/latest` root CSV/MD count after relocation: 264

## Reference Method

Each artifact was checked with `rg` using both its full root path and basename across:

- `.github`
- `scripts`
- `tests`
- `docs`
- `config`
- `output/latest`
- `docs/latest`

The prior audit document and `config/output_latest_artifact_inventory.csv` were treated as inventory evidence, not consumer evidence.

## Actions

The only physical moves in this PR are low-risk orphan diagnostics:

| source | target | root alias |
| --- | --- | --- |
| `output/latest/chip_flow_source_status_latest.md` | `output/latest/diagnostics/chip_flow_source_status_latest.md` | no |
| `output/latest/repair_one_daily_price_latest.md` | `output/latest/diagnostics/repair_one_daily_price_latest.md` | no |

These two files had no `rg` consumer/producer evidence outside inventory and the prior audit.

## Review Table

| path | recommendation | reference summary | target | alias |
| --- | --- | --- | --- | --- |
| `output/latest/candidate_repeat_appearance_validation_latest.md` | keep diagnostic latest alias | `validate_candidate_repeat_appearance.py` writes it; `daily_full_pipeline.yml` runs the validator. | same | yes |
| `output/latest/chip_flow_source_status_latest.md` | relocate to diagnostics | No `rg` scripts, validators, docs, or workflows consumer/producer found. | `output/latest/diagnostics/chip_flow_source_status_latest.md` | no |
| `output/latest/daily_candidate_regression_2484_latest.csv` | keep diagnostic latest alias | `validate_daily_candidate_regression_cases.py` writes it; `daily_full_pipeline.yml` runs the validator. | same | yes |
| `output/latest/daily_candidate_regression_2484_latest.md` | keep diagnostic latest alias | `validate_daily_candidate_regression_cases.py` writes it; `daily_full_pipeline.yml` runs the validator. | same | yes |
| `output/latest/daily_candidate_regression_8069_latest.csv` | keep diagnostic latest alias | `validate_daily_candidate_regression_cases.py` writes it; `daily_full_pipeline.yml` runs the validator. | same | yes |
| `output/latest/daily_candidate_regression_8069_latest.md` | keep diagnostic latest alias | `validate_daily_candidate_regression_cases.py` writes it; `daily_full_pipeline.yml` runs the validator. | same | yes |
| `output/latest/daily_data_layer_consistency_audit_latest.md` | keep diagnostic latest alias | `audit_daily_data_layer_consistency.py` writes it; `daily_full_pipeline.yml` runs and stages the audit output. | same | yes |
| `output/latest/daily_price_history_continuity_latest.md` | keep diagnostic latest alias | `validate_daily_price_history_continuity.py` writes it; daily and repair workflows stage it. | same | yes |
| `output/latest/repair_daily_price_range_latest.csv` | keep diagnostic latest alias | `repair_daily_price_range.py` writes it; repair workflows stage `repair_daily_price_range_latest.*`. | same | yes |
| `output/latest/repair_daily_price_range_latest.md` | keep diagnostic latest alias | `repair_daily_price_range.py` writes it; repair workflows stage `repair_daily_price_range_latest.*`. | same | yes |
| `output/latest/repair_one_daily_price_latest.md` | relocate to diagnostics | No `rg` scripts, validators, docs, or workflows consumer/producer found. | `output/latest/diagnostics/repair_one_daily_price_latest.md` | no |
| `output/latest/revenue_breakout_low_response_debug_latest.md` | keep until same-family review | `output/latest/revenue_breakout_low_response_latest.md` links to this root debug artifact. | same | yes |
| `output/latest/volume_breakout_buy_signal_evidence_registry_latest.csv` | review in research/backtest lane | `build_volume_breakout_buy_signal_grid.py` writes it; contract doc references this exact root path; producer workflow is research_backtest. | same | yes |
| `output/latest/volume_breakout_buy_signal_proposal_latest.md` | review in research/backtest lane | `build_volume_breakout_buy_signal_grid.py` writes it; producer workflow is research_backtest. | same | yes |
| `output/latest/volume_breakout_tdcc_buy_signal_evidence_registry_latest.csv` | review in research/backtest lane | `build_volume_breakout_tdcc_buy_signal_grid.py` writes it; producer workflow and tests are research_backtest. | same | yes |
| `output/latest/volume_breakout_tdcc_buy_signal_proposal_latest.md` | review in research/backtest lane | `build_volume_breakout_tdcc_buy_signal_grid.py` writes it; producer workflow and tests are research_backtest. | same | yes |
| `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.csv` | review in research/backtest lane | `research_weekly_20pct_surge_volume.py` writes it; research workflows reference the script. | same | yes |
| `output/latest/weekly_10pct_vs_20pct_surge_volume_comparison_latest.md` | review in research/backtest lane | `research_weekly_20pct_surge_volume.py` writes it; research workflows reference the script. | same | yes |

## Follow-Up Boundaries

- Do not delete the two relocated diagnostics without a later cleanup PR.
- Do not move the research/backtest-produced rows in this daily-production PR.
- Do not move workflow-produced root diagnostics unless the producer constants, workflow staging patterns, and any validator/test references are migrated together.
- Do not handle the `unknown` 30 rows in this PR.
