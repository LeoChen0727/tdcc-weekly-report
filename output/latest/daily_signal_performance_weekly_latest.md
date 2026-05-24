# 每日候選股訊號績效週報

- generated_at: `2026-05-24 11:13:40 Asia/Taipei`
- latest_signal_date: `20260524`
- signal_count: `1023`
- period: latest 14 calendar days

## 市場背景摘要

- TWSE: close=42267.97, 5d=+2.66%, 10d=+1.60%, 20d=+12.07%, above_ma20=True, above_ma60=True
- TPEX: close=423.25, 5d=+2.94%, 10d=+3.37%, 20d=+11.00%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 496 |  |  |  |  |  |  | 4.333925680985655 | -0.35174258420396737 |
| range_rebound | 172 |  |  |  |  |  |  | 2.12193675369595 | -4.349889595042786 |
| revenue_breakout_low_response | 41 |  |  |  |  |  |  | 1.4020165308030614 | -1.4328728971409914 |
| revenue_pullback | 314 |  |  |  |  |  |  | 1.5408830266934692 | -2.4495681592046687 |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_warning | 455 |  |  |  |  | 3.472989340176992 | -1.3889696240513556 |
| mild_accumulation | 422 |  |  |  |  | 3.043724328320362 | -1.7760826424498677 |
| neutral | 4 |  |  |  |  | 4.978492488915354 | -1.047250347429024 |
| strong_accumulation | 140 |  |  |  |  | 2.3402362754641532 | -1.4299436145548121 |
| 無TDCC資料 | 2 |  |  |  |  | 2.13468309859155 | 0.4841549295774516 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 514 |  |  |  |  |
| call_inflow | 9 |  |  |  |  |
| no_signal | 500 |  |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 982 |  |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 7 |  |  |  |  |
| mainstream_growth | mainstream_growth | 18 |  |  |  |  |
| neutral | neutral | 16 |  |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 656 |  |  |  |  |
| 出貨型營收 / 其他 | 324 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 43 |  |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | strong_bull | 496 |  |  |  |
| range_rebound | strong_bull | 172 |  |  |  |
| revenue_breakout_low_response | strong_bull | 41 |  |  |  |
| revenue_pullback | strong_bull | 314 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
