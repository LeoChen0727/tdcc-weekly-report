# Daily Stock Candidate Rules

Last updated: 2026-05-29

This task is dedicated to the daily Taiwan full-market candidate report and its six ChatGPT-side PDF deliverables. It must not be mixed with holdings management, single-stock full reports, TDCC weekly reports, standalone market-opening reports, backtest periodic reports, or astrology tasks.

This boundary is only a task router. It does not override the required deliverables, program-side fields, specialty sections, or PDF quality contract below.

## Required Deliverable

When the user asks to do today's daily stock report, execute the task and produce six ChatGPT-side deliverables unless the user explicitly asks for text-only or status-only output:

1. Mainstream daily recommendation highlight PDF.
2. Mainstream complete candidate list PDF.
3. Non-mainstream daily recommendation highlight PDF.
4. Non-mainstream complete candidate list PDF.
5. Warrant market auxiliary analysis PDF.
6. Market risk and index futures/options background PDF.

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

For remote reads, raw GitHub URLs and GitHub API contents are authoritative. GitHub Pages is an auxiliary/share view and must not be used as the first freshness source for daily stock/PDF tasks. If Pages differs from raw/API on `main_price_date`, `commit_sha`, or `report_ready`, ignore Pages and use raw/API. If only stale Pages can be read, stop and report the available date instead of producing a current-date PDF.

## Daily Report Source Preflight

Before generating ChatGPT-side daily PDFs from a local checkout, run `scripts/validate_daily_report_source_preflight.py` or perform the equivalent checks:

- `main_price_date`, `actual_stock_price_history_date`, `stock_monitor_price_date`, `all_candidates_date`, `official_price_fetch_date`, `warrant_flow_date`, and raw source dates must match the target report date.
- `report_ready`, `warrant_ready`, and `daily_pdf_ready` must all be `True`.
- `output/latest/READ_ME_FIRST_DAILY_REPORT.txt` and `output/latest/data_freshness_latest.csv` must agree on date and readiness fields.
- A dirty local checkout is not an official PDF source. Use a clean clone, worktree, or trusted GitHub archive for report generation if the main checkout has uncommitted changes.
- `commit_sha` in README is an artifact source hint. It is allowed to differ from checkout `HEAD` because daily workflows can commit artifacts before publishing README metadata. Do not block a report solely because README `commit_sha` differs from `HEAD`.
- Do not use local `output/latest` as current data unless this preflight passes.
- The canonical source for ChatGPT-side six-PDF rendering is `scripts/generate_chatgpt_side_daily_reports.py`. A OneDrive or ad-hoc helper copy may be used only as an execution copy; durable rendering fixes must be committed through the repo workflow.

## Daily Versus Research Pipeline

The normal daily pipeline must be able to finish without long research jobs.

- The daily report may use the latest available research/backtest outputs, but it must not wait for a full market-timing backtest, weekly surge grid search, surge precondition model rebuild, all-source raw health sweep, or TDCC historical backfill.
- `daily_short_term_specialty_packet_latest.md` is the daily-facing packet for short-term research sections. If deeper research files are stale or missing, report the section as research output unavailable instead of blocking the six daily PDFs.
- Long research outputs are refreshed by `research_backtest_pipeline.yml`.
- TDCC historical data is backfilled by `tdcc_history_backfill.yml`.
- Daily report logic must keep these research sections separate from the six core candidate categories and must not alter core weights unless the backtest rules later mark them mature.
- Daily output commits must not stage TDCC weekly, long research/backtest, or historical backfill outputs. `daily_full_pipeline.yml` must validate staged paths before committing and fail if non-daily owner paths are present.
- `daily_model_parameter_research_latest.csv/md` and `daily_model_parameter_research_horizon_detail_latest.csv/md` are the formal evidence tables for model parameter tuning. They use signal-date next trading day open as entry and report D+1 through D+10 close-return and high-return endpoints separately.
- `daily_model_parameter_recommendations_latest.csv/md` is the program-side interpretation layer for these backtests. It may mark a parameter as `promote_to_pdf_core`, `pdf_secondary_watch`, `score_component_only`, `intraday_target_watch`, or `research_only`.
- These parameter research and recommendation tables are not PDF-side selection rules. The program-side model layer attaches the current recommendation fields into `daily_candidate_model_parameters_latest.csv` and `daily_candidate_model_signals_latest.csv`; ChatGPT must read those fields and must not promote a research-only row by itself.

## Model-Layer Fields Are Binding

Use program-side model-layer fields first:

- `model_id`
- `model_name_zh`
- `model_score`
- `model_rank`
- `display_rank`
- `score_components`
- `score_components_zh`
- `risk_penalty_tags`
- `risk_tags`
- `risk_tags_zh`
- `next_confirmation`
- `next_confirmation_zh`
- `why_selected`
- `why_selected_zh`
- `why_selected_human_zh`
- `theme_final_status`
- `candidate_source_type`
- `candidate_line_group`
- `theme_volume_attack_status`
- `volume_breakout_type`
- `selection_status`
- `volume_breakout_priority`
- `sample_status`
- `tuning_status`

Do not reorder or upgrade stocks by memory when these fields exist. Daily PDF and packet text must not use a separate trading-action layer as a second conclusion over the model layer.

## No Daily PDF Action Rating Layer

Daily PDF and packet output must not depend on action-rating or position-sizing fields. The daily report may describe model hits, model score, rank, risk tags, technical state, TDCC/warrant context, and next confirmation. It must not convert those fields into a program-side buy/sell instruction until a separate historical pattern operation module exists.

## Independent Model Selection Contract

The daily report must use the program-side independent model layer when it exists:

- `daily_candidate_model_layer_packet_latest.md`
- `daily_candidate_model_parameters_latest.md/csv`
- `daily_candidate_model_signals_latest.md/csv`
- `daily_candidate_group_rotation_latest.md/csv`

Each model has its own main conditions. When a stock satisfies a model's main conditions, it is selected into that model. Do not add a second ChatGPT-side "buy / not buy" gate after selection.

After selection, rank stocks inside the same model by program-side fields such as `model_score`, `model_rank`, `score_components`, `risk_penalty_tags`, `TDCC`, warrant, revenue, price position, and structure. Risk fields are penalties, annotations, and ordering inputs. They are not automatic deletion rules unless the program-side model itself marks a hard exclusion.

Mainstream / non-mainstream is a report split only. It must not cap score, veto a model signal, or remove a stock from the model list. Mainstream stocks compare with mainstream stocks; non-mainstream stocks compare with non-mainstream stocks.

If the PDF needs a curated version, show the top rows per model and per report bucket. The complete report should keep the full model list. Do not hard-code the number of models; render all program-side model rows available that day.

If `daily_candidate_group_rotation_latest.md/csv` or the `group_fund_rotation` model row exists, render it as the final `資金進入族群觀察` / theme-fund-rotation table. It is a theme-level end section, not a stock-level core ranking model.

PDF tables must surface risk and confirmation fields so the selected stock is not presented as risk-free. The wording should be "selected by model, ranked with risk/score adjustments", not "selected but cannot buy".

PDF tables must prefer program-side Chinese display columns when present:

- `model_name_zh`
- `source_category_zh`
- `report_bucket_zh`
- `effective_primary_theme_zh`
- `effective_structural_theme_bucket_zh`
- `tdcc_status_zh`
- `warrant_flow_signal_zh`
- `risk_tags_zh`
- `score_components_zh`
- `merged_source_categories_zh`
- `merged_risk_penalty_tags_zh`

Do not print raw English slug columns in investor-facing PDF tables when a `_zh` display column exists. If a required Chinese display value is missing, print `欄位尚未完成` rather than the raw slug.

## Core Categories And Specialty Sections

The core daily candidate categories are controlled by the program-side output. ChatGPT must not invent, delete, rename, or merge core categories by memory.

When the program-side output still uses the six-category model, keep these six core categories for historical tracking and backtest comparability:

1. Strict breakout.
2. Range strengthening / prior-high challenge watch.
3. Revenue breakout, price not yet reacted. If a program field still says `revenue_breakout_low_response`, the user-facing report label should be `營收爆發股價尚未反應股`.
4. Revenue growth pullback.
5. Pullback then short-term strengthening.
6. Pattern watch.

Theme status, volume-attack status, catalyst tags, TDCC tags, warrant tags, non-revenue momentum rows, and backtest research rows are cross-category labels or specialty sections, not new core categories unless the program-side model explicitly changes the core category schema.

`tdcc_short_term_continuation_d5_d10` / `TDCC短線延續模型 D+5/D+10` is a core daily candidate model when it is active in the program-side model registry. It must be rendered with the other model buckets and must not be hidden in a separate specialty-only appendix.

Specialty sections are allowed and required when their program-side files or fields exist. They must be shown outside the core category ranking and must not change core model weights unless the backtest system later marks the signal mature and ready for review.

Required specialty sections when data exists:

- `theme_event_watch_latest.md/csv`: required "近期事件預警 / 主題催化觀察" PDF section. This is an event proximity and theme catalyst context layer, not a standalone buy model. It must help the report surface upcoming exhibitions, product events, earnings/event windows, and related candidate intersections early, but it must not override model selection, price/volume structure, TDCC, revenue, or risk fields.
- `daily_short_term_specialty_packet_latest.md`: supporting D+5 / D+10 short-term research-stat tables. These tables may explain historical D+5/D+10 behavior, but they do not replace the core `TDCC短線延續模型 D+5/D+10` candidate rows.
- `daily_model_parameter_research_latest.md/csv` and `daily_model_parameter_research_horizon_detail_latest.md/csv`: standalone model-parameter research and tuning evidence. Use for backtest discussion and parameter review, not as a hard-coded PDF model list unless the program-side model layer promotes the rule.
- `daily_model_parameter_recommendations_latest.md/csv`: program-side model-parameter usage recommendation. The same recommendation fields are also joined into `daily_candidate_model_signals_latest.csv`. Use these fields to decide whether a backtested parameter is ready for PDF core display, secondary watch, score component only, intraday-target watch, or research-only status.
- `market_abnormal_status_latest.md/csv`: official TWSE/TPEx disposition, attention, periodic-trading, altered-trading, managed-stock, and suspension flags.
- `msci_taiwan_rebalance_backtest_latest.md/csv` and `msci_taiwan_rebalance_events_latest.csv`: MSCI Taiwan addition/deletion event-tag research. Use first trading day after effective date open as the entry basis and D+5/D+10/D+15/D+20 close as exits. Treat this like disposition/attention data: an event tag and research overlay, not a standalone buy/sell signal or core ranking category.
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
Do not infer 族群出量 / volume-spread leaders manually. The only valid source for the spread table is `volume_attack_theme_layer_latest.csv`, especially `theme_spread_decision`, `leader_stock_id`, `second_stock_id`, and `third_stock_id`.

Before using raw industry for grouping, read the program-side taxonomy:

- `output/latest/stock_theme_taxonomy_latest.csv`
- `output/latest/stock_theme_taxonomy_latest.md`
- `output/latest/stock_theme_taxonomy_review_latest.csv`
- `output/latest/stock_theme_taxonomy_review_latest.md`
- `data/theme_events/stock_theme_taxonomy.csv`

The taxonomy fields `primary_theme`, `secondary_themes`, `structural_theme_bucket`, `theme_structural_status`, `theme_mainstream_label`, and `concept_tags` are the authoritative source for cross-industry market themes. They override legacy exchange industry for mainstream / non-mainstream routing.

Mainstream / non-mainstream is split into separate concepts:

- `theme_final_status` / `theme_market_flow_status`: today's flow and breadth state.
- `theme_structural_status`: broad structural bucket, such as `core_mainstream_theme` or `non_mainstream_theme`.
- `structural_theme_bucket`: fine market theme bucket. This may cross industry classifications.
- `market_theme_group`: the primary analysis grouping. It must prefer `structural_theme_bucket`, then `theme_name`, then `industry`.
- `theme_group_source`: records which field supplied `market_theme_group`.

Only stocks with an explicit `structural_theme_bucket` in the core AI/electronics/robotics/semiconductor theme list may enter the mainstream capital line. Official exchange industry alone is not enough. If `stock_theme_taxonomy_review_latest.csv` marks a stock as `industry_core_needs_market_theme`, it must be treated as taxonomy incomplete and cannot enter the mainstream attack list until mapped.

Industry and market theme are not the same thing. A stock can keep its industry while also belonging to a cross-industry theme bucket.

For report grouping and backtest segmentation, use `market_theme_group` before raw industry. Industry is secondary context only. Do not group AI-era stocks only by their legacy exchange industry when a program-side structural theme bucket exists.

Examples:

- 華通 remains PCB, 啟碁 remains networking/communications, but both can belong to `low_earth_orbit_satellite_theme`.
- 南亞 remains plastics, 台玻 remains glass/ceramics, but both can belong to `glass_fiber_ccl_theme`.
- 大銀微系統、上銀、亞德客-KY should be treated as robotics / precision motion or robotics automation when mapped, not merely as generic machinery.
- 佳能 and 亞光 should be treated as robotics / optical sensing or machine-vision camera-module names when mapped, not merely as generic optoelectronics.
- 三集瑞-KY, 國巨 and 凱美 should be grouped under passive components when mapped, even if their exchange industries differ.

Core mainstream theme buckets include low-earth-orbit satellite, glass fiber / CCL, PCB/CCL, CPO / silicon photonics, optical communication, networking, advanced packaging, semiconductor equipment, semiconductor materials, semiconductors, passive components, memory/HBM, AI server, power/thermal, connectors/cables, consumer electronics, robotics/automation.

Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are `non_mainstream_theme` even when daily flow is strong.

Non-mainstream groups with strong daily flow should be shown as non-mainstream rotation, short-term theme, or risk/watch sections; do not call them mainstream leaders.

Mainstream / non-mainstream is a report-section field, not a score penalty and not a buy veto. The model layer must keep model scores and ranks based on each model's own conditions, score components, risk tags, TDCC, volume, price pattern, warrant support, and confirmation state. Use `report_line`, `report_bucket`, `candidate_line_group`, and model rank/display rank to compare core-mainstream, non-mainstream, and unknown-theme names inside their own sections. Do not downgrade a stock only because it is non-mainstream; apply risk display only for actual risk fields such as TDCC distribution, stale signal, overheat, false breakout, missing confirmation, or execution-risk flags.

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

## Volume Attack Rules

The formal daily `volume_range_breakout` model is the independent `放量攻擊模型`. It replaces the old broad volume-breakout/watch/risk taxonomy for PDF model selection.

Hard selection conditions:

- Breakout baseline uses the previous 20 trading days, excluding the signal day.
- Signal-day close must be at least `previous_20d_high * 1.02`.
- `volume_ratio >= 2.0`.
- 20-day average volume must be at least 1000 lots. If raw volume is stored as shares, normalize to lots before applying the threshold.
- The signal day must be a bullish candle: `close > open`, or `open == close and close > previous_close` for limit-up/flat-candle cases.
- No moving-average gate.
- No 60-day-high gate.
- No same-day fake-breakout gate. A real failed breakout can only be confirmed after later trading days.

Official model output:

- Use `volume_breakout_type = bottom_volume_attack`.
- Use `selection_status = selected`.
- Do not split this model into selected/watch/risk rows. Risk is handled by score deductions and risk tags only.

Scoring and ranking may use non-conflicting factors:

- Higher volume ratio.
- Larger breakout magnitude.
- Longer or cleaner platform/consolidation base.
- Better TDCC status.
- Bullish warrant flow.
- Stronger revenue data.
- Lower quantified price position if available.
- Better candle quality. Long upper shadow can deduct attack-quality score once, but must not remove the stock from the model after hard conditions are met.

Do not use these as hard exclusions for this model:

- "Price already rose too much".
- "Overheated".
- Same-day fake breakout.
- Strict 60-day high breakout.
- Neckline challenge.
- MA reclaim / right-side watch.
- Close only near the breakout level without passing the 2% prior-20-day-high threshold.

## TDCC Overheated Short-Term Edge

If `daily_short_term_specialty_packet_latest.md` exists, it is the mandatory source for the daily short-term specialty section.

Do not confuse `回檔後短線轉強` with `TDCC短線延續模型 D+5/D+10`:

- `回檔後短線轉強` is one of the fixed six daily candidate categories.
- `TDCC短線延續模型 D+5/D+10` is its own active core model when present in the program-side registry.
- Separate short-term research/reporting tables may still include TDCC overheated continuation and next-open +10% touch parameter research as supporting evidence.

If `tdcc_overheated_short_term_edge_latest.md/csv` exists, the daily report must include it as a standalone specialty subsection:

- Show separate D+5 and D+10 tables.
- Keep close-to-close metrics separate from next-open-to-close metrics.
- Use only `mature_dN=True` samples for win rate and return statistics.
- Current matching-stock rows must not be presented as stock-specific guaranteed win-rate rows. If several stocks match the same historical rule, show the rule-level D+5/D+10 performance table separately from the current candidate list.
- Preferred current candidate wording: `D+5 next-open win / avg return` and `D+10 next-open win / avg return`. Avoid ambiguous wording such as `歷史勝率 / 相對報酬`.
- Treat the signal as `reporting_priority_only` while sample/regime coverage is still limited.
- Do not use these supporting research tables to override the active core model ranking.
- Do not use it to change TDCC / ABM / daily candidate core model weights.
- If the current candidate CSV has matching stocks, show them as a separate TDCC overheated short-term watch list with confirmation and risk notes.

If `weekly_surge_strict_parameter_search_latest.md/csv` exists, the daily report must also include it as a standalone next-open +10% touch research subsection:

- Show a compact D+1 through D+10 horizon summary, and also show separate D+5 and D+10 detail tables.
- Use the definition `entry = D+1 open` and `hit = D+1 open to D+N high reaches +10%`.
- For sell-point analysis, use `D+1 open` as the entry and `D+N close` as the exit. Report D+1 through D+10 close-exit win rate and average/median return separately from the +10% intraperiod high touch-rate.
- Close-exit win rate must use only rows with a mature `D+N close` as the denominator. Do not count pending rows without D+N close as losses.
- This is not weekly candlestick analysis. The file prefix `weekly_surge` is legacy/backward-compatible only.
- Display title in Chinese: `隔日開盤後 D+1 至 D+10 盤中觸及 +10% 研究`.
- Do not write `週線急漲`, `周線急漲嚴格參數`, `最佳歷史D+5勝率`, or `最佳歷史D+10勝率`.
- The `best_dN_touch_rate_pct` field is a next-open entry high-touch rate, not close-to-close return or D+N close win rate.
- If legacy fields named `best_d5_hit_rate_pct` or `best_d10_hit_rate_pct` still appear, interpret them as `+10% intraperiod high touch rate`, not a close-exit win rate.
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

This task delivers six ChatGPT-side PDFs when the user asks to run the daily recommendation task:

1. `主流每日推薦精華 PDF`
2. `主流完整候選清單 PDF`
3. `非主流每日推薦精華 PDF`
4. `非主流完整候選清單 PDF`
5. `權證市場輔助分析 PDF`
6. `市場風險與大盤期權背景 PDF`

Repo pipeline PDFs are validation/reference artifacts. They cannot be presented as the newly generated ChatGPT-side PDFs unless the user asks only for repo artifact links or status.

The curated recommendation PDF title must be:

`YYYY/M/D 台股推薦標的`

The curated PDF body must not contain repo read flow, internal rule explanations, debug/fallback labels, ChatGPT apologies, version labels such as `v3`, or phrases such as `流程重跑版`. Keep source/date notes minimal and outside the main investment content.

PDF font rule: do not use decorative, special, rare, or novelty fonts. Use common, stable, readable fonts with reliable Chinese support. If font choice is uncertain, prefer the default system sans-serif / CJK font and prioritize readability over style.

The first page must be a compact table, not a long bullet list. It must show 1-2 representative stocks per program-side core category with these columns:

- model / category
- stock
- model rank / display rank
- score / `model_score`
- selected reason from `score_components`, `score_components_zh`, `why_selected`, or `why_selected_zh`
- risk / next confirmation from `risk_tags`, `risk_tags_zh`, `risk_penalty_tags`, and `next_confirmation`

Each core category must then include 3-5 representative stocks when available. If fewer exist, say that program-side qualified rows are insufficient.

Each representative stock must be rendered as an operation card/page, not only a row in a table. Each card must include:

- stock id / name
- model / category
- mainstream or non-mainstream status from program-side fields
- model score / model rank / display rank
- TDCC and warrant status
- selected reason from `score_components`, `score_components_zh`, `why_selected`, or `why_selected_zh`
- risk disclosure from `risk_tags`, `risk_tags_zh`, `risk_penalty_tags`, `must_not_overstate`, `repeated_but_no_breakout`, `needs_eps_confirmation`, and `revenue_good_eps_unconfirmed`
- technical state: latest close, 23EMA, MA20, MA60, prior high, platform, support, resistance, volume, volume ratio, breakout/pullback/failure status
- next confirmation / model continuation condition
- model invalidation or risk-escalation condition
- follow-up tracking condition
- next confirmation without a PDF-side action rating
- K-line chart on the same page or directly adjacent page

K-line charts for representative stocks must use repo price data and show the latest half-year trading window by default, approximately 126 trading days. The chart may read a longer raw price window for technical context, but the PDF-facing chart must not display a 180-day window unless the user explicitly asks for a longer view. The chart must include price, volume, 23EMA as the primary line, MA20/MA60 as supporting lines, prior high/platform/support/resistance, breakout zone, and failure line when applicable. The chart is not decoration; it must match the model confirmation and invalidation text.

The curated PDF must include a `降級 / 鈍化 / 風險清單` near the back. This is a risk summary, not a recommendation table. It should include only stock, original category, risk reason, and presentation note.

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
