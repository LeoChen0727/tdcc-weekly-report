# INDIVIDUAL STOCK CHATGPT PACKET - 6805 富世達

## Metadata
- generated_at: 2026-05-26 23:02:33 Asia/Taipei
- stock_id: 6805
- stock_name: 富世達
- packet_status: standard_180d_window_packet
- latest_price_date: 20260526
- price_rows: 134
- latest_tdcc_date: 20260522
- tdcc_rows: 4
- tdcc_history_status: insufficient_tdcc_history
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes: TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions

## Stable Read URLs
- packet_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/6805_packet_latest.md
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/6805_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/6805_packet_latest.md?ref=main
- price_window_180_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6805_price_window_180_latest.csv
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6805_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6805_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6805_price_window_180_latest.txt
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6805_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6805_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/6805_price_window_180_latest.html
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/6805_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/6805_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.csv
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.txt
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/6805_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/6805.csv
- price_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/6805.csv
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/6805.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/6805.csv
- tdcc_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/6805.csv
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/6805.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/6805_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/6805_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/6805_latest.md?ref=main

## Data Quality Rules
- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.
- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.
- For chart or K-line work, always read `price_window_180_html_pages_url` or `price_window_180_txt_*` first. The 20-row preview is not enough for technical analysis.
- Single-stock chart and main conclusion should use 23EMA as the primary moving-average observation line.
- MA20 / MA60 / MA120 remain backend auxiliary and backtest fields; do not make them the main chart/conclusion unless the user explicitly asks.
- The full historical CSV remains available for Python backtests.
- If price_rows < 60, do not produce a standard technical report.
- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.
- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.

## Latest Price Snapshot
- date: 20260526
- open: 1750
- high: 1820
- low: 1705
- close: 1785
- volume: 2439880
- ma5: 1771
- ema23_primary: 1841.9
- distance_to_ema23_pct: -3.09
- ma20: 1888.25
- ma60: 1856.67
- ma120: 1667.5
- return_5d: 0.85
- return_20d: -13.77
- volume_ratio: 1.19
- distance_to_ma20_pct_auxiliary: -5.47
- distance_to_high_60_pct: -21.54

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260428,2095,2180,2005,2085,2119322,1893.71,10.1,1885,1729.58,0.98
20260429,2065,2160,2045,2070,1537056,1908.41,8.47,1897,1742.67,0.7
20260430,2080,2115,1995,2070,1768168,1921.87,7.71,1913,1753.67,0.8
20260504,2180,2275,2110,2215,2587650,1946.3,13.81,1927.5,1767.58,1.13
20260505,2160,2165,1995,1995,3283287,1950.36,2.29,1933,1777.33,1.38
20260506,2015,2015,1805,1880,5137849,1944.49,-3.32,1934.5,1785,1.99
20260507,1925,1950,1875,1920,1763898,1942.45,-1.16,1936,1792.17,0.7
20260508,1925,2035,1900,1980,2786603,1945.58,1.77,1943,1800.42,1.08
20260511,2020,2055,1965,1995,1945868,1949.7,2.32,1949.5,1809.92,0.75
20260512,2020,2035,1845,1850,2904762,1941.39,-4.71,1953.75,1817.33,1.13
20260513,1835,1890,1805,1830,2136690,1932.11,-5.28,1958.75,1822.25,0.83
20260514,1875,1885,1780,1780,2191888,1919.43,-7.26,1956.5,1826.5,0.86
20260515,1820,1840,1725,1735,1692195,1904.06,-8.88,1948.25,1829.58,0.67
20260518,1700,1745,1645,1735,981759,1889.98,-8.2,1941.5,1832.75,0.4
20260519,1735,1815,1695,1770,1131323,1879.98,-5.85,1935.25,1836.42,0.46
20260520,1770,1810,1710,1720,1087686,1866.65,-7.86,1925.5,1838.75,0.45
20260521,1770,1810,1755,1810,759562,1861.93,-2.79,1916.75,1843.17,0.33
20260522,1830,1845,1785,1795,989339,1856.35,-3.3,1911,1848.42,0.45
20260525,1825,1825,1740,1745,1813092,1847.07,-5.53,1902.5,1852.83,0.85
20260526,1750,1820,1705,1785,2439880,1841.9,-3.09,1888.25,1856.67,1.19
```

## Latest TDCC Snapshot
- as_of_date: 20260522
- over_400_ratio: 58.18
- over_600_ratio: 52.5
- over_800_ratio: 46.11
- over_1000_ratio: 46.11
- over_400_change_1w: -0.48
- over_800_change_1w: -2
- over_1000_change_1w: -0.57
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,63.78,,51.04,,49.59,,0,False,False
20260508,60.86,-2.92,49.05,-1.99,49.05,-0.54,0,False,False
20260515,58.66,-2.2,48.11,-0.94,46.68,-2.37,0,False,False
20260522,58.18,-0.48,46.11,-2,46.11,-0.57,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6805 | 富世達 | pullback_rebound | 回檔後短線轉強 | 82.0 |  |  |  |  | call_put_bullish | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d |
| 20260526 | 6805 | 富世達 | revenue_pullback | 營收成長股價回檔 | 82.0 |  |  |  |  | call_put_bullish | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |
| 20260526 | 6805 | 富世達 | revenue_breakout_low_response | 營收爆發低反應股 | 12.0 | 21.0 | D_降級_TDCC轉弱 |  |  | call_put_bullish | continued_2_3d | calendar event: monthly_revenue_expected_window on 20260601; status=expected_window; proximity=within_7d；營收轉強但 EPS / 毛利率尚未有結構化資料確認 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6805 | 富世達 | 2 | 2 | 2 | 2 | 2 | continued_2_3d | 連續 2 個交易日上榜，訊號延續但仍需確認。 |

## Warrant Context
| date | stock_id | stock_name | call_warrant_count | put_warrant_count | call_turnover | put_turnover | call_put_turnover_ratio | warrant_flow_signal | warrant_flow_score | warrant_flow_warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260526 | 6805 | 富世達 | 170 | 11 | 30166220.0 | 8840.0 | 3412.47 | call_put_bullish | 3 |  |

## Interpretation Guardrails
- This packet supports analysis; it is not a buy/sell recommendation by itself.
- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.
- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.
- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.
- Warrant signals are auxiliary only and must not be used as a standalone reason.
