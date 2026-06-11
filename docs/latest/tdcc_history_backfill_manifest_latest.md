# TDCC History Backfill Manifest

- generated_at: 2026-05-25 12:40:31 Asia/Taipei
- universe: chatgpt-top
- stocks_selected: 80
- dates_selected: 26
- date_range: 20251121 ~ 20260522
- fetched_ok: 24
- skipped_existing: 2056
- failed_or_empty: 0
- dry_run: False

## Notes

- TDCC OpenData only exposes latest all-market data. Historical backfill uses the official TDCC query page by stock id and weekly date.
- This script intentionally defaults to a bounded stock universe to avoid thousands of repeated requests against the official site.
- Re-run `python scripts/build_tdcc_stock_history.py` after backfill to rebuild `data/tdcc_stock_history/{stock_id}.csv`.

## Latest Rows

| generated_at                    |     date |   stock_id | stock_name   | status           | message   |
|:--------------------------------|---------:|-----------:|:-------------|:-----------------|:----------|
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1460 | 宏遠         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1452 | 宏益         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1474 | 弘裕         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1584 | 精剛         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1471 | 首利         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1805 | 寶徠         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1414 | 東和         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1438 | 三地開發     | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1626 | 艾美特-KY    | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1799 | 易威         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1443 | 立益物流     | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1614 | 三洋電       | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1617 | 榮星         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1760 | 寶齡富錦     | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1308 | 亞聚         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1535 | 中宇         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1906 | 寶隆         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1304 | 台聚         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1305 | 華夏         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1325 | 恆大         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1402 | 遠東新       | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1410 | 南染         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1563 | 巧新         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1586 | 和勤         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1217 | 愛之味       | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1447 | 力鵬         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1455 | 集盛         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1467 | 南緯         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       1582 | 信錦         | skipped_existing |           |
| 2026-05-25 12:40:31 Asia/Taipei | 20251121 |       2618 | 長榮航       | ok               |           |
