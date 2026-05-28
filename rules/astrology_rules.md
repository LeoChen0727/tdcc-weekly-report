# Astrology Rules

Last updated: 2026-05-28

This task is for Zi Wei Dou Shu plus Ba Zi strategy analysis. It is not a daily stock candidate report, holdings report, market timing report, or backtest report.

## Highest Priority Rule

Astrology / Zi Wei / Ba Zi reports are calendar-date reports.

- Use the user's requested calendar date as the report date.
- Do not use `main_price_date` as the astrology report date.
- `main_price_date` and `report_ready` are only stock-market data status fields.
- A stale or previous-trading-day `main_price_date` must not block the astrology report.
- Repo stock-market data may only support the wealth / stock behavior-risk paragraph.

## Visible Report Format

The visible astrology report must start with astrology content, not repo engineering status.

Recommended opening order:

1. Title with the requested calendar date.
2. One-sentence overall conclusion for the day.
3. Fixed chart verification.
4. Today's Ba Zi.
5. Today's Zi Wei.
6. What is different from recent days.
7. Combined interpretation and practical actions.

Forbidden opening headings for astrology reports:

- 資料狀態
- 資料日期與流程狀態
- repo 入口讀取狀態
- READ_ME_FIRST 讀取狀態

Do not create a leading section with repo status, raw URL status, Pages status, GitHub API status, `main_price_date`, or `report_ready`.

If a market-data note is necessary, place one short sentence inside the wealth / stock paragraph or at the end under "資料補充".

## Hard Final Check

Before sending the final visible astrology report, inspect the first 300 visible characters.

If the opening contains any of the following before fixed chart / Ba Zi / Zi Wei content, rewrite the report:

- 資料狀態
- 資料日期與流程狀態
- repo
- READ_ME_FIRST
- raw_fetch
- pages
- cache
- GitHub API
- main_price_date
- report_ready

The first visible heading after the title must be astrology content such as "固定命盤核對", "今日八字", or "今日紫微"; it must not be a data-status heading.

## Repo Data Role

Repo market data may only support the wealth / stock behavior-risk paragraph.

- It can remind the user about current market risk, trading discipline, and data availability.
- It cannot replace the fixed chart data.
- It cannot be treated as the primary source for astrology timing.
- If repo market data is unreadable, write one short human sentence in the wealth / stock paragraph only, then continue.
- Do not show raw technical statuses such as `raw_fetch_failed`, `pages_safe_open_failed`, `cache_miss`, `internal_fetch_error`, or `content_not_expanded` in the visible astrology report body.
- If market data is stale or unreadable, the visible wording should be concise, for example: "股票市場資料目前僅作輔助，命理分析仍依 2026-05-28 日曆日期進行。"

## Fixed Chart Data

Use the fixed chart data already defined by the user unless the user provides a correction:

- Male.
- Birth date: 1981-07-27.
- Birth time: 23:10.
- Birth place: Keelung, Taiwan.
- Time zone: Taipei / UTC+8.
- Ba Zi pillars: Xin You, Yi Wei, Bing Wu, Geng Zi.
- Day master: Bing fire.
- Current luck cycle: 2018-2027 Xin Mao.
- Zi Wei life/body palace: Yi Wei with Zi Wei and Po Jun.
- Current major limit: age 44-53, Mao, corresponding to natal Xin Mao wealth palace.
- Natal transformations: Ju Men Hua Lu, Tai Yang Hua Quan, Wen Qu Hua Ke, Wen Chang Hua Ji.

## Daily Output

Every daily astrology report should include:

1. Fixed chart verification.
2. Today's Ba Zi year / month / day.
3. Today's Zi Wei month / day palace.
4. What is different from recent days.
5. Combined Ba Zi plus Zi Wei interpretation.
6. Practical strategy for overall state, wealth / stocks, work / rental, relationships, family, health, what to do, what to avoid.
7. Concrete action instructions.

## Stock And Wealth Paragraph

When discussing stocks:

- Use real repo stock data if available.
- If repo data is stale, mention the available `main_price_date` only in this paragraph or a final data note.
- If repo data is missing, do not invent market facts.
- Astrology can only remind about behavior risk such as chasing, overconfidence, over-leverage, or forcing trades.
- Astrology cannot replace price, TDCC, fundamentals, market regime, or backtest data.
- The stock paragraph must not become a repo status report. Keep market-data availability to one sentence unless the user asks for debugging.

## Prohibitions

- Do not refuse an astrology report because READ_ME_FIRST is stale.
- Do not start an astrology report with repo fetch status, raw URL status, Pages status, or GitHub API status.
- Do not use old stock-market data as if it were today's stock report.
- Do not make astrology a stock buy/sell signal.
- Do not mix Ba Zi solar-term months with Zi Wei Dou Jun lunar-month palace names.
- Do not invent real-time stock prices, holdings, TDCC, or market data.
