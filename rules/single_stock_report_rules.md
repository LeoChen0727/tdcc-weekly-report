# Single Stock Report Rules

Last updated: 2026-05-31

This task is for one specified stock. It is not the daily full-market candidate report, holdings management, TDCC weekly report, market-opening report, periodic backtest report, or astrology task.

## Required Data Read

Read in this order:

1. `output/latest/READ_ME_FIRST_DAILY_REPORT.txt`
2. `rules/master_priority_rules.md`
3. `rules/single_stock_report_rules.md`
4. `output/latest/individual_stock_read_protocol_latest.md`
5. `output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md`
6. `output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html` or `.txt`
7. `output/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt`
8. `data/stock_price_history/{stock_id}.csv` and `data/tdcc_stock_history/{stock_id}.csv` only when the compact windows are insufficient or a full history is required.

If raw CSV does not expand, use the packet, HTML/TXT price window, TDCC window, index, or GitHub API contents endpoint. Do not replace repo price or TDCC data with external websites.

## Chart Window

For price/pattern analysis, continue to read the 180-trading-day price window because support, resistance, prior highs, and context still need enough history.

For the main K-line chart in the individual stock PDF/report, draw only the latest half-year trading window by default: `126` trading days. Do not make the main report chart 180 days unless the user explicitly asks for a longer view.

## ACTION_DISPLAY Is The PDF Contract

The individual stock packet may contain both `## ACTION_DISPLAY` and `## ACTION_DECISION`.

Formal investor-facing PDF / Markdown reports must use `ACTION_DISPLAY` fields only:

- `action_rating_display_zh`
- `model_category_display_zh`
- `score_interpretation_zh`
- `action_summary_zh`
- `entry_strategy_zh`
- `position_sizing_zh`
- `add_position_strategy_zh`
- `take_profit_strategy_zh`
- `risk_control_zh`
- `post_entry_watch_zh`
- `final_decision_zh`

`ACTION_DECISION` is internal model context. Do not print raw internal field names or raw enum values in formal report prose.

Forbidden in formal PDF / Markdown prose:

- `ACTION_DECISION`
- `action_rating`
- `starter_position`
- `scale_in`
- `buy_now`
- `wait_pullback`
- `wait_reclaim`
- `decision_score`
- `daily_candidate_decision`
- `model_slug`
- `packet`
- `raw field name`
- `程式端欄位`

If a display field is missing, write `資料不足 / 暫用現有資料`; do not expose the raw internal value.

## Entry Versus Management

Separate first-entry language from after-entry monitoring:

- `entry_strategy_zh` describes first-tranche entry conditions and entry style.
- `post_entry_watch_zh` describes management checks after entry.

Do not turn `next_monthly_revenue`, `next_tdcc_update`, sector follow-through, event follow-through, or warrant overheat checks into automatic pre-entry blockers unless the display text explicitly says they are first-entry blockers.

## Required Report Behavior

The opening conclusion must quote `action_rating_display_zh`.

For 建議買進 / 可分批買進 / 可小量試單, the report must state:

- whether the first tranche can be entered now
- suggested position size
- entry style
- add conditions
- take-profit zones or rules
- exit conditions
- post-entry watch items

Do not make every stock "wait for confirmation". Confirmation items must be classified as either first-entry prerequisites or post-entry management.

## Price And TDCC Requirements

For K-line, technical, platform, prior-high, pullback, support/resistance, and 23EMA conclusions, use the 180-day price window.

For TDCC conclusions, use the TDCC window or TDCC history. If TDCC history has fewer than 8 weeks, mark `insufficient_tdcc_history` and make only short-term observations.

External news, company events, broker targets, and industry context may supplement the event/background section, but they must not replace repo price and TDCC data.
