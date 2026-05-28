# Astrology Rules

Last updated: 2026-05-28

This task is for Zi Wei Dou Shu plus Ba Zi strategy analysis. It is not a daily stock candidate report, holdings report, market timing report, or backtest report.

## Date Rule

Astrology reports are calendar-date reports.

- Use the user's requested calendar date as the report date.
- Do not use `main_price_date` as the astrology report date.
- `main_price_date` is only the latest available stock-market data date.
- If `main_price_date` is older than the requested calendar date, state that market data is only available through that date and continue the astrology report.
- `report_ready=False`, cache miss, raw fetch failure, or stale stock data must not block Ba Zi / Zi Wei calculation.

## Repo Data Role

Repo market data may only support the wealth / stock behavior-risk paragraph.

- It can remind the user about current market risk, trading discipline, and data availability.
- It cannot replace the fixed chart data.
- It cannot be treated as the primary source for astrology timing.
- If repo market data is unreadable, write one short human sentence in the wealth / stock paragraph only, then continue.
- Do not put repo fetch/debug status in the opening section unless the user explicitly asks about data-reading status.
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

## Output

Every daily astrology report should include:

1. Fixed chart verification.
2. Today's Ba Zi year / month / day.
3. Today's Zi Wei month / day palace.
4. What is different from recent days.
5. Combined Ba Zi plus Zi Wei interpretation.
6. Practical strategy for overall state, wealth / stocks, work / rental, relationships, family, health, what to do, what to avoid.
7. Concrete action instructions.

## Visible Report Format

The visible astrology report should start with the calendar-date astrology content, not repo engineering status.

Recommended opening order:

1. Title with the requested calendar date.
2. One-sentence overall conclusion for the day.
3. Fixed chart verification.
4. Today's Ba Zi.
5. Today's Zi Wei.
6. What is different from recent days.
7. Combined interpretation and practical actions.

Do not create a leading section titled "資料日期與流程狀態" for astrology reports. If a data note is necessary, place it as a short note inside the wealth / stock paragraph or at the very end under "資料補充".

## Stock And Wealth Paragraph

When discussing stocks:

- Use real repo stock data if available.
- If repo data is stale, say the available `main_price_date`.
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
