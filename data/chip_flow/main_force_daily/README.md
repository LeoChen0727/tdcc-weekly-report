# Main Force / Eight Institution Source Data

Put daily or historical chip-flow CSV files in this folder when this data source is available.

The scanner reads every CSV under:

```text
data/chip_flow/main_force_daily/*.csv
```

It looks for stocks where this value is positive for at least three consecutive trading rows ending on the latest source date:

```text
主力買賣超 - 八大法人買賣超 - 八大行庫買賣超
```

Supported column names are flexible. A source file can provide either a precomputed value column, or all three component columns.

Required identity columns:

```text
date / 日期 / 交易日期
stock_id / 股票代號 / 證券代號 / code / ticker
stock_name / 股票名稱 / 證券名稱 / name
```

Component columns:

```text
main_force_net_buy / 主力買賣超 / 主力買超 / 主力淨買超
eight_institution_net_buy / 八大法人買賣超 / 八大法人買超 / 法人買賣超 / 三大法人買賣超
eight_bank_net_buy / 八大行庫買賣超 / 八大行庫買超 / 八大公股買賣超 / 八大官股買賣超
```

Precomputed value column:

```text
main_force_minus_eight_value / 主力扣八大買賣超 / 主力扣八大 / 主力買賣超-八大法人買賣超-八大行庫買賣超
```

Output files:

```text
output/latest/main_force_eight_positive_latest.csv
output/latest/main_force_eight_positive_latest.md
output/latest/main_force_eight_positive_latest.json
docs/latest/main_force_eight_positive_latest.csv
docs/latest/main_force_eight_positive_latest.md
docs/latest/main_force_eight_positive_latest.json
output/history/main_force_eight_positive/
```
