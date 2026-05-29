# Daily Stock Candidate Rules

Last updated: 2026-05-28

This task is dedicated to the daily Taiwan full-market candidate report and its four ChatGPT-side PDF deliverables. It must not be mixed with holdings management, single-stock full reports, TDCC weekly reports, standalone market-opening reports, backtest periodic reports, or astrology tasks.

This boundary is only a task router. It does not override the required deliverables, program-side fields, specialty sections, or PDF quality contract below.

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

## Daily Versus Research Pipeline

The normal daily pipeline must be able to finish without long research jobs.

- The daily report may use the latest available research/backtest outputs, but it must not wait for a full market-timing backtest, weekly surge grid search, surge precondition model rebuild, all-source raw health sweep, or TDCC historical backfill.
- `daily_short_term_specialty_packet_latest.md` is the daily-facing packet for short-term research sections. If deeper research files are stale or missing, report the section as research output unavailable instead of blocking the four daily PDFs.
- Long research outputs are refreshed by `research_backtest_pipeline.yml`.
- TDCC historical data is backfilled by `tdcc_history_backfill.yml`.
- Daily report logic must keep these research sections separate from the six core candidate categories and must not alter core weights unless the backtest rules later mark them mature.

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

## Core Categories And Specialty Sections

The core daily candidate categories are controlled by the program-side output. ChatGPT must not invent, delete, rename, or merge core categories by memory.

When the program-side output still uses the six-category model, keep these six core categories for historical tracking and backtest comparability:

1. Strict breakout.
2. Range strengthening / prior-high challenge watch.
3. Revenue breakout, price not yet reacted. If a program field still says `revenue_breakout_low_response`, the user-facing report label should be `營收爆發股價尚未反應股`.
4. Revenue growth pullback.
5. Pullback then short-term strengthening.
6. Pattern watch.

Theme status, volume-attack status, catalyst tags, TDCC tags, warrant tags, short-term edge rows, non-revenue momentum rows, and backtest research rows are cross-category labels or specialty sections, not new core categories unless the program-side model explicitly changes the core category schema.

Specialty sections are allowed and required when their program-side files or fields exist. They must be shown outside the core category ranking and must not change core model weights unless the backtest system later marks the signal mature and ready for review.

Required specialty sections when data exists:

- `daily_short_term_specialty_packet_latest.md`: standalone D+5 / D+10 short-term specialty.
- `market_abnormal_status_latest.md/csv`: official TWSE/TPEx disposition, attention, periodic-trading, altered-trading, managed-stock, and suspension flags.
- `tdcc_overheated_short_term_edge_latest.md/csv`: standalone TDCC overheated short-term edge.
- `weekly_surge_strict_parameter_search_latest.md/csv`: legacy filename for standalone next-open +10% touch parameter research. Do not translate this as `周線急漲`.
- `explosive_volume_up_backtest_latest.md/csv`, `explosive_volume_up_position_backtest_latest.csv`, and `explosive_volume_up_events_latest.csv`: standalone explosive-volume-up research. This is a research/watch section only. It uses D+1 open as the entry basis and separates close-return win rate from intraperiod high-hit rate.
- Explosive-volume-up interpretation must first split price position: bottom/low-zone volume reversal, low-to-mid reclaim, near-high attack, and high-zone extension/chase. Do not mix bottom reversal with high-zone distribution/chase. Theme/mainstream status is the second filter, not a replacement for price-position filtering.
- Explosive-volume-up signal timing is after the signal-day close. Entry statistics use next trading day open. `high_hit_rate` means the post-entry holding-window high reached the target; it is not an intraday entry rule.
- Stricter explosive-volume-up quality requires a red candle with meaningful real body and limited upper shadow. Prefer `strict_red_close_near_high` first, then `relaxed_red_small_upper_shadow`; long-upper-shadow or failed-close rows are lower quality even if volume is large.
- `volume_attack_theme_layer_latest.md/csv` and `volume_attack_theme_stocks_latest.md/csv`: standalone volume attack x theme early-mainstream section.
- `non_revenue_momentum_watch_latest.md/csv`, if present: standalone non-revenue momentum / theme-fund-first section.

## Required Three Lines

The daily report must separate:

1. Mainstream-funding line / dual-confirmation priority stocks.
2. Volume attack x theme early-mainstream stocks.
3. Individual latent watch stocks.

Do not mix these into one total ranking. Different category scores are not directly comparable.

## Theme And Volume Attack Status

Every mainstream / volume-attack / early-mainstream table must include:

- `theme_final_status`
- `theme_market_flow_status`
- `theme_structural_status`
- `market_theme_group`
- `theme_group_source`
- `theme_mainstream_label`
- `theme_volume_attack_status`

Use `volume_attack_theme_layer_latest.md/csv` and `volume_attack_theme_stocks_latest.md/csv`.

Do not infer mainstream/non-mainstream from memory.

Mainstream / non-mainstream is split into separate concepts:

- `theme_final_status` / `theme_market_flow_status`: today's flow and breadth state.
- `theme_structural_status`: broad structural bucket, such as core_mainstream_theme or non_mainstream_theme.
- `structural_theme_bucket`: fine market theme bucket. This may cross industry classifications.
- `market_theme_group`: the primary analysis grouping. It must prefer `structural_theme_bucket`, then `theme_name`, then `industry`.
- `theme_group_source`: records which field supplied `market_theme_group`.

Only `theme_structural_status=core_mainstream_theme` may enter the mainstream capital line.

Industry and market theme are not the same thing. A stock can keep its industry while also belonging to a cross-industry theme bucket.

For report grouping and backtest segmentation, use `market_theme_group` before raw industry. Industry is secondary context only. Do not group AI-era stocks only by their legacy exchange industry when a program-side structural theme bucket exists.

Examples:

- 華通 remains PCB, 啟碁 remains networking/communications, but both can belong to `low_earth_orbit_satellite_theme`.
- 南亞 remains plastics, 台玻 remains glass/ceramics, but both can belong to `glass_fiber_ccl_theme`.

Core mainstream theme buckets include low-earth-orbit satellite, glass fiber / CCL, PCB/CCL, CPO / silicon photonics, optical communication, networking, advanced packaging, semiconductor equipment, semiconductor materials, semiconductors, passive components, memory/HBM, AI server, power/thermal, connectors/cables, consumer electronics, robotics/automation.

Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are `non_mainstream_theme` even when daily flow is strong.

Non-mainstream groups with strong daily flow should be shown as non-mainstream rotation, short-term theme, or risk/watch sections; do not call them mainstream leaders.

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
- The short-term specialty layer is a standalone research/reporting section that currently includes TDCC overheated continuation and next-open +10% touch parameter research.

If `tdcc_overheated_short_term_edge_latest.md/csv` exists, the daily report must include it as a standalone specialty subsection:

- Show separate D+5 and D+10 tables.
- Keep close-to-close metrics separate from next-open-to-close metrics.
- Use only `mature_dN=True` samples for win rate and return statistics.
- Treat the signal as `reporting_priority_only` while sample/regime coverage is still limited.
- Do not mix this specialty into the fixed six-category ranking.
- Do not use it to change TDCC / ABM / daily candidate core model weights.
- If the current candidate CSV has matching stocks, show them as a separate TDCC overheated short-term watch list with confirmation and risk notes.

If `weekly_surge_strict_parameter_search_latest.md/csv` exists, the daily report must also include it as a standalone next-open +10% touch research subsection:

- Show a compact D+1 through D+10 horizon summary, and also show separate D+5 and D+10 detail tables.
- Use the definition `entry = D+1 open` and `hit = D+1 open to D+N high reaches +10%`.
- For sell-point analysis, use `D+1 open` as the entry and `D+N close` as the exit. Report D+1 through D+10 close-exit win rate and average/median return separately from the +10% intraperiod high touch-rate.
- Close-exit win rate must use only rows with a mature `D+N close` as the denominator. Do not count pending rows without D+N close as losses.
- This is not weekly candlestick analysis. The file prefix `weekly_surge` is legacy/backward-compatible only.
- Display title in Chinese: `隔日開盤買進後 D+1 至 D+10 盤中觸及 +10% 研究`.
- Do not write `周線急漲嚴格參數`.
- The win rate is a next-open entry touch-rate, not close-to-close return or D+N close win rate.
- Show current candidates from `weekly_surge_strict_parameter_candidates_latest.md/csv` when available.
- Treat it as `research_watchlist_and_reporting_priority_only` until more regime samples are available.
- If `market_abnormal_status_latest.md/csv` marks a stock as disposition, attention, attention accumulation, periodic trading, altered trading, managed stock, or suspension, show it as an execution-risk overlay. Do not describe it as a clean breakout or clean short-term edge.
- Historical backtests must not apply today's abnormal-status list to past signals. Until verified historical snapshots are available, mark the disposition filter as `disposition_history_not_backfilled`.

## Non-Revenue Momentum Specialty

If `non_revenue_momentum_watch_latest.md/csv` exists, the daily report must include a standalone section named `非營收驅動強勢股 / 題材資金先行`.

This section is for stocks where price, volume, theme, TDCC, or warrant flow is moving before revenue, EPS, or gross margin confirmation. It is not a seventh core category and must not change core model weights.

Required fields to show when available:

- `non_revenue_momentum_type`
- `revenue_confirmation_status`
- `theme_final_status`
- `theme_volume_attack_status`
- `volume_breakout_type`
- `volume_ratio`
- `tdcc_status`
- `warrant_flow_signal`
- `next_confirmation`

Interpretation:

- `A_fund_flow_confirmed_revenue_unconfirmed`: funds/price/theme are already confirming, but EPS/gross margin/revenue confirmation is still required.
- `B_turnaround_theme_watch`: theme or fund flow is improving, but price confirmation is incomplete.
- `C_hot_money_watch`: short-term hot money or technical movement exists, but fundamentals are not confirmed.
- `D_overheated_or_failed_risk`: overheated, failed breakout, TDCC distribution, or other risk warning exists; do not promote to main attack list.

Rows in this section must use conditional language: wait for EPS/gross margin/revenue confirmation, confirmed volume follow-through, or price holding above the breakout/support area. Do not present these rows as clean revenue-backed growth stocks.

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

## Daily Recommendation ChatGPT-Side PDF Contract

This task delivers four ChatGPT-side PDFs when the user asks to run the daily recommendation task:

1. `每日推薦分析 PDF`
2. `完整候選清單補充 PDF`
3. `權證市場輔助分析 PDF`
4. `市場風險與大盤期權背景 PDF`

Repo pipeline PDFs are validation/reference artifacts. They cannot be presented as the newly generated ChatGPT-side PDFs unless the user asks only for repo artifact links or status.

The curated recommendation PDF title must be:

`YYYY/M/D 台股推薦標的`

The curated PDF body must not contain repo read flow, internal rule explanations, debug/fallback labels, ChatGPT apologies, version labels such as `v3`, or phrases such as `流程重跑版`. Keep source/date notes minimal and outside the main investment content.

PDF font rule: do not use decorative, special, rare, or novelty fonts. Use common, stable, readable fonts with reliable Chinese support. If font choice is uncertain, prefer the default system sans-serif / CJK font and prioritize readability over style.

The first page must be a compact table, not a long bullet list. It must show 1-2 representative stocks per program-side core category with these columns:

- category
- stock
- rating / `decision_priority`
- score / `decision_score`
- selected reason from `why_selected`
- risk / next confirmation from `why_downgraded`, `risk_tags`, `downgrade_flags`, and `next_confirmation`

Each core category must then include 3-5 representative stocks when available. If fewer exist, say that program-side qualified rows are insufficient.

Each representative stock must be rendered as an operation card/page, not only a row in a table. Each card must include:

- stock id / name
- category
- mainstream or non-mainstream status from program-side fields
- rating / score / rank
- TDCC and warrant status
- selected reason from `why_selected`
- downgrade/risk disclosure from `why_downgraded`, `risk_tags`, `downgrade_flags`, `must_not_overstate`, `repeated_but_no_breakout`, `needs_eps_confirmation`, and `revenue_good_eps_unconfirmed`
- technical state: latest close, 23EMA, MA20, MA60, prior high, platform, support, resistance, volume, volume ratio, breakout/pullback/failure status
- conditional buy trigger
- take-profit / reduce / exit trigger
- no-buy condition
- next confirmation with `trigger + action`
- K-line chart on the same page or directly adjacent page

K-line charts for representative stocks must use repo price data / 180-day windows when available. The chart must include price, volume, 23EMA as the primary line, MA20/MA60 as supporting lines, prior high/platform/support/resistance, breakout zone, and failure line when applicable. The chart is not decoration; it must match the buy/exit text.

The curated PDF must include a `降級 / 鈍化 / 風險清單` near the back. This is a risk summary, not a recommendation table. It should include only stock, original category, risk reason, and handling action.

Wide tables must be split into readable tables or operation cards. Do not put long `why_selected`, `why_downgraded`, or `next_confirmation` text into a narrow table cell.

Before delivering the curated PDF, check:

- title is `YYYY/M/D 台股推薦標的`
- no repo/debug/read-flow text appears in the body
- first page has category representative table
- each representative stock has rating, score, reason, risk, next confirmation, technical state, buy trigger, exit trigger, no-buy condition, and K-line chart
- mainstream / non-mainstream split is visible
- required specialty sections with D+5 / D+10 data are present when files exist
- risk list exists
- tables are readable and not clipped
