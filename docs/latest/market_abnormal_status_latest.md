# Market Abnormal Status Latest

- generated_at: `2026-07-03 19:32:11 Asia/Taipei`
- source: TWSE / TPEx official OpenAPI
- usage: execution-risk flag for daily candidate, short-term research, and backtest segmentation.
- limitation: historical backtests can only use this flag after daily snapshots accumulate or a verified historical source is backfilled.

## Source Status
| source              | status       |   rows | url                                                                 |
|:--------------------|:-------------|-------:|:--------------------------------------------------------------------|
| twse_disposition    | fetch_failed |      1 | https://openapi.twse.com.tw/v1/announcement/punish                  |
| twse_attention      | fetch_failed |      1 | https://openapi.twse.com.tw/v1/announcement/notice                  |
| twse_attention_note | fetch_failed |      1 | https://openapi.twse.com.tw/v1/announcement/notetrans               |
| tpex_disposition    | ok           |     50 | https://www.tpex.org.tw/openapi/v1/tpex_disposal_information        |
| tpex_attention      | fetch_failed |      1 | https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_information |
| tpex_attention_note | ok           |      2 | https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_note        |
| tpex_trading_mode   | fetch_failed |      1 | https://www.tpex.org.tw/openapi/v1/tpex_cmode                       |

## Counts
| market_abnormal_status   |   count |
|:-------------------------|--------:|
| disposition              |      29 |

## Current Stocks
|   stock_id | stock_name   | source_market   | market_abnormal_status   | market_abnormal_risk_level   | disposition_period               | disposition_reason        | attention_reason   | attention_accumulation_note   | execution_risk_note                         |
|-----------:|:-------------|:----------------|:-------------------------|:-----------------------------|:---------------------------------|:--------------------------|:-------------------|:------------------------------|:--------------------------------------------|
|       2061 | 風青           | TPEx            | disposition              | D_disposition_or_periodic    | 1150624~1150707                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3147 | 大綜           | TPEx            | disposition              | D_disposition_or_periodic    | 1150706~1150717                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3163 | 波若威          | TPEx            | disposition              | D_disposition_or_periodic    | 1150622~1150703                  | 最近10個營業日內有6個營業日           |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3230 | 錦明           | TPEx            | disposition              | D_disposition_or_periodic    | 1150701~1150714; 1150706~1150717 | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3285 | 微端           | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3441 | 聯一光          | TPEx            | disposition              | D_disposition_or_periodic    | 1150622~1150707                  | 連續3個營業日及沖銷標準              |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3624 | 光頡           | TPEx            | disposition              | D_disposition_or_periodic    | 1150624~1150709                  | 連續5個營業日及沖銷標準              |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       3675 | 德微           | TPEx            | disposition              | D_disposition_or_periodic    | 1150625~1150708                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       4556 | 旭然           | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       4923 | 力士           | TPEx            | disposition              | D_disposition_or_periodic    | 1150624~1150707                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       4991 | 環宇-KY        | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 連續5個營業日                   |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5227 | 立凱-KY        | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702; 1150624~1150707 | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5321 | 美而快          | TPEx            | disposition              | D_disposition_or_periodic    | 1150629~1150710                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5425 | 台半           | TPEx            | disposition              | D_disposition_or_periodic    | 1150626~1150709                  | 連續5個營業日                   |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5464 | 霖宏           | TPEx            | disposition              | D_disposition_or_periodic    | 1150629~1150710                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5468 | 凱鈺           | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702; 1150624~1150707 | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       5489 | 彩富           | TPEx            | disposition              | D_disposition_or_periodic    | 1150626~1150709                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6217 | 中探針          | TPEx            | disposition              | D_disposition_or_periodic    | 1150706~1150717                  | 最近10個營業日內有6個營業日           |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6488 | 環球晶          | TPEx            | disposition              | D_disposition_or_periodic    | 1150622~1150703                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6613 | 朋億*          | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6620 | 漢達           | TPEx            | disposition              | D_disposition_or_periodic    | 1150626~1150709                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6683 | 雍智科技         | TPEx            | disposition              | D_disposition_or_periodic    | 1150629~1150710                  | 最近10個營業日內有6個營業日           |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       6693 | 廣閎科          | TPEx            | disposition              | D_disposition_or_periodic    | 1150624~1150707                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       7712 | 博盛半導體        | TPEx            | disposition              | D_disposition_or_periodic    | 1150625~1150708                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       7828 | 創新服務         | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       8024 | 佑華           | TPEx            | disposition              | D_disposition_or_periodic    | 1150630~1150713                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       8027 | 鈦昇           | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 最近10個營業日內有6個營業日           |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       8042 | 金山電          | TPEx            | disposition              | D_disposition_or_periodic    | 1150618~1150702                  | 因連續3個營業日達本中心作業要點第四條第一項第一款 |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |
|       8096 | 擎亞           | TPEx            | disposition              | D_disposition_or_periodic    | 1150624~1150707                  | 最近10個營業日內有6個營業日           |                    |                               | 處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。 |

