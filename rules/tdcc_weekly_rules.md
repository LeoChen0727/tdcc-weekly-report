# TDCC Weekly Report Rules

Last updated: 2026-06-28

This task is the TDCC weekly large-holder flow report. It is not the daily full-market stock recommendation report, holdings management, a single-stock report, market-opening analysis, or backtest tuning report.

## Required Read Order

When producing a TDCC weekly large-holder report, read repo raw / GitHub API structured data first. Do not start from PDFs and do not start from `tdcc_signal_performance_latest.md`.

Required order:

1. `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
2. `rules/master_priority_rules.md`
3. `rules/tdcc_weekly_rules.md`
4. `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv`
5. `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv`
6. `output/latest/tdcc_weekly_report_section_manifest_latest.csv`
7. Corresponding Markdown / PDF files only as cross-checks or shareable attachments.

The report-producing conversation or PDF generator must use these program-side report-ready CSV files as the primary rendering contract:

- `output/latest/tdcc_weekly_candidate_highlight_for_report_latest.csv`
- `output/latest/tdcc_weekly_candidate_full_for_report_latest.csv`
- `output/latest/tdcc_weekly_report_section_manifest_latest.csv`

The following files are supporting data only. They must not override the report-ready CSV date, ranking, row inclusion, section assignment, or display fields:

- `tdcc_weekly_increase_ranking_csv_raw_url`
- `tdcc_consecutive_accumulation_ranking_csv_raw_url`
- `tdcc_weekly_model_cross_summary_csv_raw_url`
- `tdcc_top_risk_list_csv_raw_url`
- `tdcc_chatgpt_tracking_packet_raw_url`
- `tdcc_signal_performance_latest.md`
- older PDFs, Markdown summaries, or prior ChatGPT outputs.

## Date Rules

The TDCC weekly report main date is the unique `signal_date` in the report-ready CSV files, not the daily pipeline `main_price_date` and not any historical signal date in `tdcc_signal_performance_latest.md`.

Do not set or infer an expected latest TDCC date in rules, memory, README text, Pages state, or the computer's current calendar date. The report date is decided only by the program-side report-ready CSV `signal_date` after validation.

Before producing any TDCC weekly PDF or chat report:

1. Read both report-ready CSV files.
2. Validate that each file contains exactly one `signal_date`.
3. Validate that the `signal_date` in the highlight CSV equals the `signal_date` in the full CSV.
4. If a corresponding PDF / MD begins with `TDCC data date` or equivalent date metadata, validate that it equals the report-ready CSV `signal_date`.
5. If any date mismatch exists, stop and report the inconsistency. Do not produce the report.
6. If either report-ready CSV contains multiple `signal_date` values, stop and report the mixed-date error. Do not produce the report.
7. Do not treat any historical `signal_date` from `tdcc_signal_performance_latest.md` as the current weekly report date.
8. The builder must fail before rendering Markdown or PDF if the report-ready CSV files do not expose exactly one matching `signal_date`.
9. The validation artifact must expose the date contract and identify `report_ready_csv_signal_date` as the date source.

## Required Outputs

Every TDCC weekly report task must produce exactly two user-facing report deliverables:

1. TDCC weekly highlight report
2. TDCC weekly full report

Both user-facing deliverables must be PDF files:

- `output/latest/tdcc_weekly_candidate_highlight_latest.pdf`
- `output/latest/tdcc_weekly_candidate_full_latest.pdf`

The canonical latest PDF names above must remain available as internal artifacts. External delivery must also publish date-stamped Chinese PDF copies:

- output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_精華版_{signal_date}.pdf
- output/latest/published_reports/tdcc_weekly/TDCC大戶籌碼週報_完整版_{signal_date}.pdf

The {signal_date} value must come only from the unique matching signal_date in the highlight and full report-ready CSV files. Do not use the computer date, README date, Pages date, daily main_price_date, or old PDF date for external delivery filenames. If highlight and full report-ready CSV dates differ, fail closed before creating the external delivery PDFs.

When reporting TDCC weekly PDF delivery completion to the user, include clickable links to the delivered PDF files when possible. At minimum, include a clickable link to `output/latest/published_reports/tdcc_weekly/` using the absolute local workspace path.

PDF text and table content must use the repo-controlled Traditional Chinese Kai
font asset `assets/fonts/TW-Kai-98_1.ttf`, registered as `TW-Kai`, at 14 pt.
Formal TDCC weekly production PDFs must not silently fall back to OS-installed
fonts, ReportLab built-in CID fonts such as `STSong-Light`, or Noto Sans /
generic sans-serif fonts. If the repo Kai font is missing, cannot be registered,
or the final PDF does not contain a Kai font token, the builder or validator
must fail closed. Page count is not fixed; do not treat five pages as a rule.

TDCC ranking sections and daily-model cross sections must use different PDF table contracts:

- TDCC ranking sections use: section rank, stock id, stock name, TDCC phase, risk bucket, TDCC score, selected reason, next confirmation, operation note.
- Daily-model cross sections use the ranking columns plus daily model, model rank within TDCC list, and model score. Within each model-cross section, the section rank and model rank within the TDCC list must be sorted by `model_score` descending, then daily model display rank ascending, then original TDCC rank ascending. The original TDCC rank remains a reference column, not the primary sort key for the model-cross table.

Ranking fields must render as integers when they are whole numbers. Do not display ranks as `1.00`, `2.00`, or similar decimal strings.

Score fields may use at most two decimals and must strip redundant trailing zeroes, for example `81.30` -> `81.3` and `74.00` -> `74`.

PDF text must not print raw slug or snake_case fields. If a display value has no approved Chinese label, render `資料不足 / 暫用現有資料` instead of the raw token.

## TDCC Data Quality Quarantine

A single-stock TDCC holder distribution anomaly must not make the whole weekly
report fail when the core source date and report-ready section contracts remain
valid. Examples include placeholder-like distributions where one non-total TDCC
level carries essentially 100% of holders and the total holder count is one.

The program-side pipeline must quarantine these stocks before weekly ranking,
report-ready CSV/MD generation, and PDF table rendering. Quarantined stocks must
not appear in `weekly_increase`, `consecutive_accumulation`, model-cross
sections, or full-report PDF tables.

When quarantined TDCC holder distribution rows exist for the report
`signal_date`, the highlight PDF must add a final-page data anomaly note listing
the affected stock codes and the data-quality reason. This note is a data
quality disclosure only; it must not create a buy/sell judgment, recommendation
reason, ranking rule, scoring adjustment, or model judgment.

The validator must check both sides of this contract: quarantined codes are not
present in report-ready tables or the full PDF, and the highlight PDF final page
contains the anomaly note and affected codes.

## Section Manifest Contract

The report generator must render sections dynamically from `output/latest/tdcc_weekly_report_section_manifest_latest.csv` and the report-ready CSV files. Do not hard-code the number of tables in the PDF or Markdown renderer.

The current core sections are:

1. `weekly_increase`: 當週增幅排名.
2. `consecutive_accumulation`: 連續累積排名.
3. `model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10`: 當週增幅榜 × TDCC短線延續模型 D+5/D+10.
4. `model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10`: 連續累積榜 × TDCC短線延續模型 D+5/D+10.

These four sections are the current core manifest defaults, not a permanent four-table rule. If the manifest later adds, disables, or removes a section, the Markdown and PDF output must follow the enabled manifest sections and per-section limits.

The previous week's PDF or any reference PDF is a visual style reference only. It must not override the current report-ready CSV structure, the section manifest, section membership, ordering, limits, ranking, or date.

Each rendered table must correspond to exactly one `section_id`. The generator must filter with the section ID for each section and must not combine multiple `section_id` values into one table. The weekly-increase model-cross section and consecutive-accumulation model-cross section must remain separate sections; they must not be merged through a generic source column.

Daily-model cross sections are intersection disclosures, not primary TDCC ranking gates. If an enabled `table_contract=model_cross` section has zero qualifying rows for the current week, the Markdown/PDF renderer and validator must keep the section visible and render an explicit empty-state message such as no qualifying names this week. This must not fail the weekly workflow, must not fabricate rows, and must not lower ranking/model thresholds. Core TDCC ranking sections such as `weekly_increase` and `consecutive_accumulation` remain fail-closed when empty.

## Ranking Lines

The weekly report has two independent TDCC ranking lines:

1. Weekly increase ranking: stocks with large one-week holder-ratio increases. A single week can qualify.
2. Consecutive accumulation ranking: stocks with at least two weeks of continued accumulation.

These two lists must be ranked separately. Do not merge them into one total ranking.

## Ranking Formula Contract

Effective TDCC holder increase means the holder-ratio change is greater than `0.5` percentage points. Do not treat tiny positive changes such as `0.02` as an effective increase for sync bonuses or high-threshold continuation.

Weekly increase score:

- Base score = `1000-share weekly change * 4 + 800-share weekly change * 3 + 600-share weekly change * 2 + 400-share weekly change * 1`.
- Sync bonus uses effective increases only: four thresholds +15, three thresholds +10, two thresholds +5, otherwise +0.
- Mainstream theme bonus: +5 when `theme_mainstream_status` is a mainstream status.
- Low liquidity penalty: -10 when 20-day average volume is below 1000 lots after normalizing raw share volume to lots.
- Weekly increase ranking is sorted by weekly increase score, then weighted base score, then 1000-share weekly change, then 800-share weekly change.

Consecutive accumulation score:

- Hard inclusion gate: 800-share and 1000-share holders must both have effective increases for at least two consecutive TDCC weeks.
- Base score uses the same weighted weekly-change formula as the weekly increase score.
- Sync bonus uses the same effective-increase threshold and bonus table as the weekly increase score.
- High-threshold continuation bonus: 2 weeks +5, 3 weeks +10, 4 weeks +15, 5 or more weeks capped at +20.
- Mainstream theme bonus and low liquidity penalty use the same definitions as the weekly increase score.
- Consecutive accumulation ranking is sorted by consecutive accumulation score, then effective 800/1000 consecutive weeks, then weighted base score.

## Highlight Report

The highlight report must include every enabled manifest section where `include_in_highlight=True`, using each section's `highlight_limit`.

The current core manifest defaults include:

- top 10 weekly-increase names
- top 10 consecutive-accumulation names
- weekly-increase names cross-ranked by the TDCC short-term continuation D+5/D+10 model, top 10
- consecutive-accumulation names cross-ranked by the TDCC short-term continuation D+5/D+10 model, top 10

The highlight report must make clear whether a row comes from weekly increase, consecutive accumulation, weekly-increase x TDCC short-term continuation D+5/D+10, or consecutive-accumulation x TDCC short-term continuation D+5/D+10.

## Full Report

The full report must include every enabled manifest section where `include_in_full=True`, using each section's `full_limit`. The current core manifest default is at most the top 50 rows per section; if a section has fewer rows than its manifest limit, include all available rows.

## Interpretation Rules

TDCC is a chip-flow background signal, not a standalone buy command.

- `tdcc_weekly_increase_score` ranks one-week large-holder increases.
- `tdcc_consecutive_accumulation_score` ranks continued accumulation.
- `tdcc_phase_group_zh`, `risk_bucket_zh`, `why_selected_zh`, `risk_tags_zh`, `next_confirmation_zh`, `recommended_usage_zh`, `report_usage_zh`, and `operation_note_zh` must be shown or summarized from program-side fields.
- Stocks that are price-leading, overheated, divergent, or data-insufficient must not be described as quiet accumulation.
- Daily model cross rows are used to show where TDCC-selected stocks appear in daily stock-selection models. Do not use them to rewrite TDCC ranking.
- Strength Ranking is not the same as hidden accumulation.
- Pre-Move / ABM is the hidden-accumulation observation line, when it is present in program-side fields.

The report may use practical categories such as priority research, worth tracking, observation only, downgrade / avoid, but these must be derived from program-side display fields and risk buckets. Do not turn them into direct buy or sell commands.

## Report Generator Rules

The report generator must render program-side fields. It must not:

- invent a new TDCC ranking
- combine weekly increase and consecutive accumulation into one rank
- drop rows because they are non-mainstream
- create a PDF-layer buy/sell judgment
- create a PDF-layer mainstream / non-mainstream filter that is not in the program-side table
- create a PDF-layer risk veto that is not in the program-side table
- create new model judgments not present in the program-side table
- turn TDCC risk labels into automatic deletion rules unless the program-side table marks hard exclusion
- use raw PDF artifacts as the primary source when report-ready CSV exists
- use `tdcc_signal_performance_latest.md` as the primary weekly report source
- use a historical signal-performance date as the current weekly report date
- hard-code a fixed section count instead of following the section manifest
- use the section title or source label as a substitute for exact `section_id` filtering

If any report-ready field is missing, write `欄位尚未完成 / 暫用現有資料` rather than guessing.
