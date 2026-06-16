# 每日候選股模型績效月報

- generated_at: `2026-06-16 20:30:18 Asia/Taipei`
- latest_signal_date: `20260616`
- signal_count: `4263`
- period: latest signal month

## 市場背景摘要

- TWSE: close=45809.19, 5d=+2.47%, 10d=+0.55%, 20d=+14.02%, above_ma20=True, above_ma60=True
- TPEX: close=430.26, 5d=+1.31%, 10d=-2.36%, 20d=+8.06%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 1835 | 0.2945156992820936 |  | 4.460897825640571 |  |  |  | 9.920422880926923 | -5.038098452858766 |
| pullback_rebound | 138 | 2.3390328273105165 |  |  |  |  |  | 7.713082103784379 | -4.072839902364078 |
| range_rebound | 845 | -1.9666902214183297 |  | 1.8968205243603797 |  |  |  | 6.125373065717392 | -6.657902788839956 |
| revenue_breakout_low_response | 139 | 2.970928347463374 |  | 9.931062796730215 |  |  |  | 6.5121228192633245 | -2.4383336611580413 |
| revenue_pullback | 973 | -1.844698183957402 |  |  |  |  |  | 6.751352906242096 | -4.706073254173235 |
| true_breakout | 333 | -5.054862991405659 |  | -1.0705739825766414 |  |  |  | 8.434831108088257 | -10.26747971833057 |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 19 | -1.6602910284875483 |  |  |  | 3.5021131556093748 | -3.331719777103851 |
| distribution_warning | 1802 | -1.3217306344352764 |  |  |  | 8.039423024108382 | -5.7399063937945085 |
| mild_accumulation | 1774 | -1.0278359456517512 |  |  |  | 8.359360488627908 | -5.7005397800197635 |
| neutral | 23 | -7.574433565099275 |  |  |  | 5.669920922790023 | -8.031193112186866 |
| strong_accumulation | 644 | 0.20007543209846926 |  |  |  | 8.01455313877187 | -5.0193032598328315 |
| 無TDCC資料 | 1 | 9.132922535211277 |  |  |  | 18.39788732394365 | 6.646126760563398 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1934 | 0.32321711352320365 |  |  |  |
| call_inflow | 345 | -2.4821560594933847 |  |  |  |
| call_put_bullish | 94 | -3.82881907389791 |  |  |  |
| call_strong_inflow | 192 | -1.6278478853956078 |  |  |  |
| mixed_flow | 21 | -5.083064395438563 |  |  |  |
| no_signal | 1645 | -1.9827152761593219 |  |  |  |
| put_inflow | 32 | 10.975936325307035 |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 4124 | -1.0771076060423408 |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 10 | 0.008338661292931704 |  |  |  |
| mainstream_growth | mainstream_growth | 74 | -1.721051031791427 |  |  |  |
| neutral | neutral | 55 | 9.171768664247745 |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 3008 |  |  |  |  |
| 出貨型營收 / 其他 | 984 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 271 |  |  |  |  |

## 財報 / 事件催化層績效

### 類事欣科型

| similar_to_shihsinko_flag | signal_count | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
| False | 4261 | -1.0314608654082424 |  |  |  |  |
| True | 2 |  |  |  |  |  |

### EPS / 毛利率 / 營收待確認

| eps_surprise_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 4263 |  |  |  |

| margin_improvement_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 4263 |  |  |  |

| revenue_good_eps_unconfirmed_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 3250 |  |  |  |
| True | 1013 |  |  |  |

### 利多反應程度

| low_reaction_after_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 724 |  |  |  |
| True | 3539 |  |  |  |

| already_reacted_to_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 3929 |  |  |  |
| True | 334 |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | correction | 119 |  |  |  |
| pattern | strong_bull | 1716 |  |  |  |
| pullback_rebound | correction | 10 |  |  |  |
| pullback_rebound | strong_bull | 128 |  |  |  |
| range_rebound | correction | 41 |  |  |  |
| range_rebound | strong_bull | 804 |  |  |  |
| revenue_breakout_low_response | correction | 25 |  |  |  |
| revenue_breakout_low_response | strong_bull | 114 |  |  |  |
| revenue_pullback | correction | 158 |  |  |  |
| revenue_pullback | strong_bull | 815 |  |  |  |
| true_breakout | correction | 31 |  |  |  |
| true_breakout | strong_bull | 302 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
