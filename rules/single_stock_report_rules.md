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

## ACTION_DECISION Is Binding

The individual stock packet may contain `## ACTION_DECISION`. This is the program-side action decision for report language.

Use these fields directly:

- `action_rating`
- `action_rating_label_zh`
- `confidence_level`
- `thesis_state`
- `entry_style`
- `position_sizing`
- `management_plan`
- `entry_prerequisites`
- `post_entry_watch_items`
- `downgrade_reason`

Allowed `action_rating` values:

- `buy_now`: 建議買進
- `scale_in`: 可分批買進
- `starter_position`: 可小量試單
- `wait_pullback`: 等待回檔
- `wait_reclaim`: 等待站回
- `hold_only`: 已持有續抱
- `take_profit`: 停利
- `reduce`: 減碼
- `avoid`: 不建議買進 / 避開

## Entry Versus Management

Separate first-entry requirements from after-entry monitoring:

- `entry_prerequisites` are buy-first-tranche requirements.
- `post_entry_watch_items` are management checks after entry.

Do not turn `next_monthly_revenue`, `next_tdcc_update`, sector follow-through, event follow-through, or warrant overheat checks into automatic pre-entry blockers unless the packet lists them in `entry_prerequisites`.

If `action_rating` is `buy_now`, `scale_in`, or `starter_position`, do not downgrade it to "等待買點", "等待確認", `wait_pullback`, or `wait_reclaim` unless current repo data directly contradicts `ACTION_DECISION`.

If a downgrade is necessary, the report must state:

- original program-side `action_rating`
- downgraded action
- concrete contradiction or `downgrade_reason`

## Required Report Behavior

The opening conclusion must quote `action_rating_label_zh`.

For `buy_now`, `scale_in`, and `starter_position`, the report must state:

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
