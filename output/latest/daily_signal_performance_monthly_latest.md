# 每日候選股模型績效月報

- generated_at: `2026-05-23 21:14:30 Asia/Taipei`
- latest_signal_date: `20260523`
- signal_count: `456`
- period: latest signal month

## 市場背景摘要

- TWSE: close=42267.97, 5d=+2.66%, 10d=+1.60%, 20d=+12.07%, above_ma20=True, above_ma60=True
- TPEX: close=423.25, 5d=+2.94%, 10d=+3.37%, 20d=+11.00%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 248 |  |  |  |  |  |  |  |  |
| range_rebound | 67 |  |  |  |  |  |  |  |  |
| revenue_breakout_low_response | 19 |  |  |  |  |  |  |  |  |
| revenue_pullback | 122 |  |  |  |  |  |  |  |  |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_warning | 203 |  |  |  |  |  |  |
| mild_accumulation | 188 |  |  |  |  |  |  |
| neutral | 2 |  |  |  |  |  |  |
| strong_accumulation | 62 |  |  |  |  |  |  |
| 無TDCC資料 | 1 |  |  |  |  |  |  |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 188 |  |  |  |  |
| no_signal | 268 |  |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 437 |  |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 3 |  |  |  |  |
| mainstream_growth | mainstream_growth | 8 |  |  |  |  |
| neutral | neutral | 8 |  |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 309 |  |  |  |  |
| 出貨型營收 / 其他 | 125 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 22 |  |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | strong_bull | 248 |  |  |  |
| range_rebound | strong_bull | 67 |  |  |  |
| revenue_breakout_low_response | strong_bull | 19 |  |  |  |
| revenue_pullback | strong_bull | 122 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
