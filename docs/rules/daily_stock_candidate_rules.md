# Daily Stock Candidate Rules

Last updated: 2026-05-27

This task is the daily Taiwan full-market candidate report. It is not a holdings report, single-stock report, backtest report, or pure repo-status check.

## Required Deliverable

When the user asks to do today's daily stock report, execute the task and produce four ChatGPT-side deliverables unless the user explicitly asks for text-only or status-only output:

1. Daily recommendation analysis PDF.
2. Complete candidate list supplement PDF.
3. Warrant market auxiliary analysis PDF.
4. Market risk and index futures/options background PDF.

Repo pipeline PDFs are source/share artifacts. They are not the final ChatGPT-side deliverable for this task.

If ChatGPT cannot create PDFs in the current environment, it must say that clearly. It must not pretend repo PDFs are newly generated ChatGPT deliverables.

## Required Data Read

Read in this order:

1. `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
2. `rules/master_priority_rules.md`
3. `rules/daily_stock_candidate_rules.md`
4. `output/latest/CHATGPT_DAILY_REPORT_RULES.txt`
5. `output/latest/chatgpt_indicator_usage_guide_latest.md`
6. `preferred_chatgpt_url` / daily packet
7. Decision CSVs, theme layers, volume-attack layers, warrant reports, market risk reports, catalyst logs, validation files.

If a CSV shows `Total lines: 1`, continue via packet / GitHub API / index fallback. Do not use a thin summary as a complete report.

## Program-Side Fields Are Binding

Use program-side fields first:

- `decision_priority`
- `decision_score`
- `why_selected`
- `why_downgraded`
- `next_confirmation`
- `theme_final_status`
- `candidate_source_type`
- `candidate_line_group`
- `theme_volume_attack_status`
- `volume_breakout_type`
- `selection_status`
- `volume_breakout_priority`
- `sample_status`
- `tuning_status`

Do not reorder or upgrade stocks by memory when these fields exist.

## Six Categories Remain Fixed

Do not add a seventh major category:

1. Strict breakout.
2. Range strengthening / prior-high challenge watch.
3. Revenue breakout low response.
4. Revenue growth pullback.
5. Pullback then short-term strengthening.
6. Pattern watch.

Theme status, volume-attack status, catalyst tags, TDCC tags, and warrant tags are cross-category labels, not new major categories.

## Required Three Lines

The daily report must separate:

1. Mainstream-funding line / dual-confirmation priority stocks.
2. Volume attack x theme early-mainstream stocks.
3. Individual latent watch stocks.

Do not mix these into one total ranking. Different category scores are not directly comparable.

## Theme And Volume Attack Status

Every mainstream / volume-attack / early-mainstream table must include:

- `theme_final_status`
- `theme_volume_attack_status`

Use `volume_attack_theme_layer_latest.md/csv` and `volume_attack_theme_stocks_latest.md/csv`.

Do not infer mainstream/non-mainstream from memory.

Allowed volume-attack theme statuses:

- `confirmed_volume_theme`
- `early_mainstream_candidate`
- `watch_volume_theme`
- `single_stock_volume_attack`
- `non_mainstream_volume_watch`
- `weak_or_non_mainstream_volume_watch`
- `overheated_volume_theme`
- `failed_volume_theme`
- `theme_status_missing`
- `insufficient_data`

`theme_status_missing` means the theme mapping is not reliable. Do not classify it as mainstream or non-mainstream.

## Volume Breakout Rules

Strict 60-day high breakout is not the only volume breakout.

Use `volume_breakout_type`:

- `range_breakout_volume`
- `range_breakout_watch`
- `strict_high_breakout`
- `ma_reclaim_volume_attack`
- `near_high_volume_watch`
- `failed_range_breakout_risk`

If strict breakout is empty, do not write that there is no volume attack. Check range breakout and watch rows.

## Required Quality Bar

The final report must not be a thin packet summary. It must include:

- mainstream theme matrix
- three-line stock split
- category interpretation
- volume attack x theme analysis
- individual latent watch list
- downgraded / stale / risk list
- warrant auxiliary analysis
- market risk and futures/options background
- next confirmations

If data depth is insufficient, say `資料不足 / 僅能觀察` rather than filling the PDF with generic text.

