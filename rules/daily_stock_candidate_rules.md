# Daily Stock Candidate Rules

Last updated: 2026-05-28

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
6. `output/latest/daily_short_term_specialty_packet_latest.md`
7. `preferred_chatgpt_url` / daily packet
8. Decision CSVs, theme layers, volume-attack layers, warrant reports, market risk reports, catalyst logs, validation files.

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

## PDF Selection Contract

The front priority table in the daily recommendation PDF must be selected by the program-side decision layer, not by raw `score`, raw `rank`, or category score.

- `score` and `rank` are secondary ordering fields only inside the same decision bucket.
- A stock with `decision_priority` below `A_priority_watch` must not be shown as a front priority stock.
- A stock with `why_downgraded`, `downgrade_flags`, `risk_tags`, `must_not_overstate=True`, `revenue_good_eps_unconfirmed_flag=True`, `repeat_appear_label` in stale/repeated/overheated states, `tdcc_distribution_warning`, `mainstream_overheated`, `weak_theme`, `failed_volume_theme`, or `overheated_volume_theme` must not be promoted into the front priority table even if its score or rank is high.
- These rows may remain in the correct line, such as individual latent watch, revenue low-response watch, risk list, or confirmation-needed list.
- PDF tables must surface `why_downgraded` and `next_confirmation` so warning rows are not presented as clean bullish candidates.

Example: a revenue low-response stock with strong revenue, repeated-but-no-breakout, no warrant confirmation, and EPS/gross-margin unconfirmed is a confirmation-needed or latent-watch row. It is not a mainstream priority stock only because raw score or rank is high.

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

## TDCC Overheated Short-Term Edge

If `daily_short_term_specialty_packet_latest.md` exists, it is the mandatory source for the daily short-term specialty section.

Do not confuse `回檔後短線轉強` with the short-term specialty layer:

- `回檔後短線轉強` is one of the fixed six daily candidate categories.
- The short-term specialty layer is a standalone research/reporting section that currently includes TDCC overheated continuation and strict weekly-surge parameter research.

If `tdcc_overheated_short_term_edge_latest.md/csv` exists, the daily report must include it as a standalone specialty subsection:

- Show separate D+5 and D+10 tables.
- Keep close-to-close metrics separate from next-open-to-close metrics.
- Use only `mature_dN=True` samples for win rate and return statistics.
- Treat the signal as `reporting_priority_only` while sample/regime coverage is still limited.
- Do not mix this specialty into the fixed six-category ranking.
- Do not use it to change TDCC / ABM / daily candidate core model weights.
- If the current candidate CSV has matching stocks, show them as a separate TDCC overheated short-term watch list with confirmation and risk notes.

If `weekly_surge_strict_parameter_search_latest.md/csv` exists, the daily report must also include it as a standalone strict weekly-surge research subsection:

- Show separate D+5 and D+10 tables.
- Use the definition `entry = D+1 open` and `hit = D+1 open to D+N high reaches +10%`.
- Show current candidates from `weekly_surge_strict_parameter_candidates_latest.md/csv` when available.
- Treat it as `research_watchlist_and_reporting_priority_only` until more regime samples are available.

## Required Quality Bar

The final report must not be a thin packet summary. It must include:

- mainstream theme matrix
- three-line stock split
- category interpretation
- volume attack x theme analysis
- standalone short-term specialty section with D+5 and D+10 tables
- individual latent watch list
- downgraded / stale / risk list
- warrant auxiliary analysis
- market risk and futures/options background
- next confirmations

If data depth is insufficient, say `資料不足 / 僅能觀察` rather than filling the PDF with generic text.
